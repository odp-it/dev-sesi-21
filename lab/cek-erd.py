#!/usr/bin/env python3
"""Cek otomatis ERD dan kamus data (Sesi 21). Membaca XML Draw.io di file .drawio.png atau .drawio.

Dijalankan di dalam container oracle-alp (Python sudah ada di image), dari folder `lab`:

    docker cp cek-erd.py oracle-alp:/tmp/cek-erd.py
    docker cp erd-alp-<nama-tim>.drawio.png oracle-alp:/tmp/erd-cek.drawio.png
    docker cp kamus-data-<nama-tim>.md oracle-alp:/tmp/kamus-cek.md
    docker exec oracle-alp python3 /tmp/cek-erd.py /tmp/erd-cek.drawio.png /tmp/kamus-cek.md

Argumen kedua (kamus data) boleh dikosongkan: kriteria 7 dan 8 bernilai 0.
Skrip hanya membaca dua file itu: file tim dan database tidak diubah. Hanya pustaka standar Python 3.8+.
Skor otomatis maksimal 80. Sisa 20 poin dinilai manual (lihat rubrik di README).
"""
import base64
import html
import os
import re
import struct
import sys
import textwrap
import urllib.parse
import xml.etree.ElementTree as ET
import zlib

MIN_TABEL = 4
KEYS = {"PK", "FK", "UQ", "UK"}
ONE = {"ERone", "ERmandOne", "ERzeroToOne"}
MANY = {"ERmany", "ERoneToMany", "ERzeroToMany"}
TIPE = re.compile(r"^(NUMBER(\(\d+(,\d+)?\))?|N?VARCHAR2\(\d+(CHAR|BYTE)?\)|CHAR(\(\d+(CHAR|BYTE)?\))?|DATE|"
                  r"TIMESTAMP(\(\d\))?(WITH(LOCAL)?TIMEZONE)?|CLOB|BLOB|BOOLEAN)$")
UANG = re.compile(r"amount|balance|price|saldo|nominal|harga|biaya")
BUKAN_UANG = re.compile(r"(_id|_no|_type|_status|_code|_date|_at)$")


class FileSalah(Exception):
    pass


# ---------- baca file Draw.io ----------

def png_xml(data):
    """XML diagram dari chunk teks PNG (VS Code: tEXt mxfile; Draw.io desktop: zTXt mxGraphModel)."""
    i = 8
    while i + 8 <= len(data):
        n = struct.unpack(">I", data[i:i + 4])[0]
        kind, body = data[i + 4:i + 8], data[i + 8:i + 8 + n]
        i += 12 + n
        if kind not in (b"tEXt", b"zTXt", b"iTXt") or b"\0" not in body:
            continue
        key, rest = body.split(b"\0", 1)
        if key not in (b"mxfile", b"mxGraphModel"):
            continue
        if kind == b"zTXt":
            raw = inflate(rest[1:])
        elif kind == b"iTXt":
            flag, rest = rest[0], rest[2:]
            raw = rest.split(b"\0", 2)[2]
            raw = inflate(raw) if flag else raw
        else:
            raw = rest
        text = raw.decode("utf-8", "replace").strip()
        return urllib.parse.unquote(text) if text.startswith("%") else text
    raise FileSalah("PNG ini tidak berisi data diagram. Pakai file .drawio.png yang dibuat dan disimpan di editor "
                    "Draw.io, bukan screenshot atau hasil export tanpa salinan diagram.")


def inflate(data):
    try:
        return zlib.decompress(data)
    except zlib.error:
        return zlib.decompress(data, -15)


def pages(path):
    """Daftar elemen mxGraphModel, satu per halaman diagram."""
    with open(path, "rb") as f:
        data = f.read()
    if not data.strip():
        raise FileSalah("File kosong (0 byte). Gambar diagram lalu simpan (Ctrl+S atau Command+S).")
    text = png_xml(data) if data[:8] == b"\x89PNG\r\n\x1a\n" else data.decode("utf-8", "replace")
    try:
        root = ET.fromstring(text.strip())
        if root.tag == "mxGraphModel":
            return [root]
        out = []
        for dia in root.iter("diagram"):
            model = dia.find("mxGraphModel")
            if model is None and (dia.text or "").strip():  # halaman terkompresi
                raw = inflate(base64.b64decode(dia.text.strip())).decode("utf-8")
                model = ET.fromstring(urllib.parse.unquote(raw))
            if model is not None:
                out.append(model)
    except (ET.ParseError, ValueError, zlib.error):
        raise FileSalah("Isi file bukan diagram Draw.io yang bisa dibaca.")
    if not out and root.tag != "mxfile":
        raise FileSalah("Isi file bukan diagram Draw.io.")
    return out


def plain(value):
    s = re.sub(r"<(br|/div|/p)[^>]*>", " ", value or "", flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", "", s)).replace("\xa0", " ")
    return " ".join(s.split())


def cells(model):
    out = {}
    root = model.find("root")
    for el in (root if root is not None else []):
        if el.tag == "mxCell":
            cell, cid, value = el, el.get("id"), el.get("value")
        else:  # <object>/<UserObject> membungkus mxCell
            cell = el.find("mxCell")
            if cell is None:
                continue
            cid, value = el.get("id"), el.get("label")
        style = cell.get("style") or ""
        geo = cell.find("mxGeometry")
        out[cid] = {"id": cid, "value": plain(value), "parent": cell.get("parent"), "edge": cell.get("edge") == "1",
                    "vertex": cell.get("vertex") == "1", "source": cell.get("source"), "target": cell.get("target"),
                    "style": dict(p.split("=", 1) for p in style.split(";") if "=" in p),
                    "x": float(geo.get("x", 0)) if geo is not None else 0.0,
                    "y": float(geo.get("y", 0)) if geo is not None else 0.0}
    return out


def parse_row(parts):
    """['PK', 'branch_id NUMBER'] -> (kunci, nama kolom, tipe)."""
    keys, rest = set(), []
    for part in parts:
        for tok in re.split(r"\s+", part):
            bare = tok.strip(",/·|;:()-").upper() if not re.search(r"\(\d", tok) else tok.upper()
            pieces = [p for p in re.split(r"[,/·|]+", bare) if p]
            if pieces and all(re.sub(r"\d+$", "", p) in KEYS for p in pieces):
                keys.update("UQ" if p.startswith("UK") else re.sub(r"\d+$", "", p) for p in pieces)
            elif tok.strip(",·|;:-"):
                rest.append(tok)
    if not rest:
        return keys, "", ""
    name = rest[0].rstrip(":")
    tail = " ".join(rest[1:]).lstrip(":- ").upper()
    tail = re.split(r"\s+(?:NOT\s+NULL|NULL|DEFAULT|CHECK|UNIQUE)\b", " " + tail)[0].strip()
    tail = re.sub(r"\s*\(\s*", "(", tail)
    tail = re.sub(r"\s*\)", ")", tail)
    tail = re.sub(r"\s*,\s*", ",", tail).rstrip(",")
    return keys, name, tail.replace(" ", "")


def tables_of(model):
    c = cells(model)
    kids = {}
    for cell in c.values():
        kids.setdefault(cell["parent"], []).append(cell)
    tables, drafts = {}, []
    for cell in c.values():
        st = cell["style"]
        if not cell["vertex"] or not (st.get("shape") == "table" or st.get("childLayout") == "stackLayout"):
            continue
        cols = []
        for row in sorted(kids.get(cell["id"], []), key=lambda r: r["y"]):
            if not row["vertex"]:
                continue
            parts = [k["value"] for k in sorted(kids.get(row["id"], []), key=lambda k: k["x"])]
            keys, name, typ = parse_row([row["value"]] + parts)
            if name and not re.match(r"^(Row|UniqueID|Item)$", name, re.I):
                cols.append({"id": row["id"], "name": name, "type": typ, "keys": keys})
        title = cell["value"]
        if title.lower() in ("", "table") or len(cols) < 2:
            drafts.append(title or "(tanpa judul)")
        else:
            tables[cell["id"]] = {"name": title, "cols": cols}
    return c, tables, drafts


def read_erd(path):
    best = ({}, {}, [])
    for model in pages(path):  # halaman dengan tabel terbanyak yang dinilai
        found = tables_of(model)
        if len(found[1]) > len(best[1]) or not best[0]:
            best = found
    return best


def relations(c, tables):
    """Garis relasi -> (daftar relasi sah, jumlah garis antar tabel, catatan)."""
    rows = {col["id"]: (tid, col) for tid, t in tables.items() for col in t["cols"]}

    def locate(cid):
        seen = set()
        while cid in c and cid not in seen:
            seen.add(cid)
            if cid in rows:
                return rows[cid]
            if cid in tables:
                return cid, None
            cid = c[cid]["parent"]
        return None

    valid, lines, notes, done = [], 0, [], set()
    for e in c.values():
        if not e["edge"]:
            continue
        a, b = locate(e["source"]), locate(e["target"])
        if not a or not b:
            notes.append("Ada garis yang salah satu ujungnya tidak menempel ke tabel (tarik sampai titik hijau).")
            continue
        label = "%s - %s" % (tables[a[0]]["name"], tables[b[0]]["name"])
        key = frozenset([a[1]["id"] if a[1] else a[0], b[1]["id"] if b[1] else b[0]])
        if key in done or (a[0] == b[0] and len(key) == 1):
            continue
        done.add(key)
        lines += 1
        s, t = e["style"].get("startArrow"), e["style"].get("endArrow")
        if s not in ONE | MANY or t not in ONE | MANY:
            notes.append("Garis %s belum crow's foot di kedua ujung (Line Start dan Line End)." % label)
        elif s in MANY and t in MANY:
            notes.append("Garis %s bersisi banyak di dua ujung (N:M): pecah dengan tabel penghubung." % label)
        else:
            if s in MANY:
                many, one = a, b
            elif t in MANY:
                many, one = b, a
            else:  # 1:1, sisi anak = ujung yang menempel ke baris FK
                many, one = (a, b) if a[1] and "FK" in a[1]["keys"] else (b, a)
            ok = bool(many[1] and one[1] and "FK" in many[1]["keys"] and one[1]["keys"] & {"PK", "UQ"})
            if not ok:
                notes.append("Garis %s: ujung sisi banyak harus menempel ke baris FK, ujung lain ke baris PK." % label)
            valid.append({"many": many, "one": one, "fk_ok": ok})
    used = {r["many"][1]["id"] for r in valid if r["fk_ok"]}
    for t in tables.values():
        for col in t["cols"]:
            if "FK" in col["keys"] and col["id"] not in used:
                notes.append("%s.%s ditandai FK tetapi belum punya garis relasi yang benar." % (t["name"], col["name"]))
    return valid, lines, notes


# ---------- kamus data ----------

def read_kamus(path):
    """{TABEL: {kolom: {tipe, wajib, constraint, contoh}}} dari bagian '## Tabel: `NAMA`'."""
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        text = f.read()
    out, table, head = {}, None, None
    for line in text.splitlines():
        m = re.match(r"^#{1,4}\s*Tabel\s*:\s*[`*]*([A-Za-z_]\w*)", line.strip())
        if m:
            table, head = m.group(1).upper(), None
            out.setdefault(table, {})
            continue
        if line.startswith("#"):
            table = None
            continue
        if table is None or not line.strip().startswith("|"):
            continue
        row = [x.strip().replace("`", "") for x in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if head is None:
            low = [x.lower() for x in row]
            if low and low[0] == "kolom":
                head = {key: next((i for i, h in enumerate(low) if h.startswith(key)), None)
                        for key in ("kolom", "tipe", "wajib", "constraint", "contoh")}
            continue
        get = {k: (row[i] if i is not None and i < len(row) else "") for k, i in head.items()}
        name = get["kolom"].lower()
        if name and not set(name) <= set("-: "):
            out[table][name] = get
    return {t: cols for t, cols in out.items() if cols and t != "NAMA_TABEL"}


# ---------- nilai ----------

def poin(maks, benar, dari, faktor=1.0):
    return 0 if dari <= 0 else int(maks * min(benar, dari) / dari * faktor + 0.5)


def nilai(erd_path, kamus_path=None):
    c, tables, drafts = read_erd(erd_path)
    valid, lines, notes = relations(c, tables)
    for d in drafts:
        notes.append("Tabel '%s' tidak dihitung: ganti judul bawaan dan isi minimal 2 baris kolom." % d)

    n = len(tables)
    faktor = min(n, MIN_TABEL) / MIN_TABEL
    allcols = [(t["name"], col) for t in tables.values() for col in t["cols"]]
    ncol = len(allcols)
    npk = sum(any("PK" in col["keys"] for col in t["cols"]) for t in tables.values())
    for t in tables.values():
        if not any("PK" in col["keys"] for col in t["cols"]):
            notes.append("%s belum punya baris PK." % t["name"])
    target = max(n, MIN_TABEL) - 1
    fk_ok = sum(r["fk_ok"] for r in valid)

    typed = 0
    for tname, col in allcols:
        typ = col["type"]
        money = UANG.search(col["name"].lower()) and not BUKAN_UANG.search(col["name"].lower()) \
            and not col["keys"] & {"PK", "FK"}
        if not TIPE.match(typ):
            notes.append("%s.%s: tipe '%s' bukan tipe Oracle yang dipakai di lab." % (tname, col["name"], typ or "-"))
        elif money and not re.match(r"^NUMBER\(\d+,2\)$", typ):
            notes.append("%s.%s: kolom uang memakai NUMBER(15,2)." % (tname, col["name"]))
        else:
            typed += 1

    named, total_names = 0, n + ncol
    seen = set()
    for t in tables.values():
        if re.match(r"^[A-Z][A-Z0-9_]*$", t["name"]) and t["name"] not in seen:
            named += 1
        else:
            notes.append("Nama tabel '%s': pakai HURUF_BESAR, tanpa spasi, dan tidak kembar." % t["name"])
        seen.add(t["name"])
    for tname, col in allcols:
        if re.match(r"^[a-z][a-z0-9_]*$", col["name"]):
            named += 1
        else:
            notes.append("%s.%s: nama kolom memakai snake_case huruf kecil." % (tname, col["name"]))

    kamus, kamus_note = {}, None
    if kamus_path:
        kamus = read_kamus(kamus_path)
    else:
        kamus_note = "Kamus data belum diberikan: kriteria 7 dan 8 bernilai 0."
    match = full = 0
    extra = 0
    erd_names = {t["name"].upper() for t in tables.values()}
    for t in tables.values():
        sect = kamus.get(t["name"].upper(), {})
        names = {col["name"].lower() for col in t["cols"]}
        extra += len(set(sect) - names)
        for x in sorted(set(sect) - names):
            notes.append("Kamus %s.%s tidak ada di ERD." % (t["name"], x))
        if kamus_path and not sect:
            notes.append("Kamus belum punya bagian '## Tabel: `%s`'." % t["name"])
            continue
        for col in t["cols"]:
            k = sect.get(col["name"].lower())
            if k is None:
                if kamus_path:
                    notes.append("%s.%s belum ada di kamus." % (t["name"], col["name"]))
                continue
            ktype = re.sub(r"\s+", "", k["tipe"]).upper()
            if col["type"] and ktype == col["type"]:
                match += 1
            else:
                notes.append("%s.%s: tipe di ERD '%s', di kamus '%s'." %
                             (t["name"], col["name"], col["type"] or "-", k["tipe"] or "-"))
            problem = []
            if k["wajib"].upper() not in ("YA", "TIDAK"):
                problem.append("Wajib diisi (YA/TIDAK)")
            if k["contoh"].strip().upper() in ("", "TODO", "..."):
                problem.append("Contoh nilai")
            cons = k["constraint"].upper()
            if "TODO" in cons:
                problem.append("Constraint masih TODO")
            elif "PK" in col["keys"] and "PK" not in cons:
                problem.append("Constraint PK")
            elif "FK" in col["keys"]:
                ref = re.search(r"FK\s*(?:->|→|-&GT;)\s*([A-Z_]\w*)", cons)
                if not ref or ref.group(1) not in erd_names:
                    problem.append("Constraint 'FK -> TABEL'")
            if problem:
                notes.append("Kamus %s.%s belum lengkap: %s." % (t["name"], col["name"], ", ".join(problem)))
            else:
                full += 1
    for x in sorted(set(kamus) - erd_names):
        notes.append("Kamus punya tabel %s yang tidak ada di ERD." % x)
    if kamus_note:
        notes.append(kamus_note)

    result = [
        ("1. Jumlah tabel (min. %d)" % MIN_TABEL, "%d tabel" % n, poin(10, n, MIN_TABEL), 10),
        ("2. Tabel punya PK", "%d dari %d" % (npk, n), poin(10, npk, n, faktor), 10),
        ("3. Relasi crow's foot", "%d relasi" % len(valid), poin(15, len(valid), target) if n > 1 else 0, 15),
        ("4. FK di sisi banyak", "%d dari %d garis" % (fk_ok, lines),
         poin(10, fk_ok, max(lines, target)) if n > 1 else 0, 10),
        ("5. Tipe data Oracle", "%d dari %d kolom" % (typed, ncol), poin(10, typed, ncol, faktor), 10),
        ("6. Penamaan tabel dan kolom", "%d dari %d nama" % (named, total_names),
         poin(5, named, total_names, faktor), 5),
        ("7. Kamus sama dengan ERD", "%d dari %d kolom" % (match, ncol + extra),
         poin(15, match, ncol + extra, faktor), 15),
        ("8. Kamus lengkap", "%d dari %d kolom" % (full, ncol), poin(5, full, ncol, faktor), 5),
    ]
    return result, list(dict.fromkeys(notes)), [t["name"] for t in tables.values()]


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    paths = sys.argv[1:]
    for p in paths:
        if not os.path.isfile(p):
            sys.exit("File tidak ditemukan: %s (sudah dijalankan docker cp untuk file ini?)" % p)
    line = "-" * 62
    print("Cek ERD Sesi 21")
    try:
        result, notes, names = nilai(*paths)
    except FileSalah as exc:
        print(line)
        print("ERD tidak bisa dinilai: %s" % exc)
        print("%-52s%3d / 80" % ("Subtotal otomatis", 0))
        sys.exit(1)
    except PermissionError as exc:
        sys.exit("File tidak bisa dibaca di container: %s" % exc)
    print(textwrap.fill("Tabel terbaca: %s" % (", ".join(names) or "(tidak ada)"), 62, subsequent_indent="  "))
    print(line)
    print("%-31s %-22s%s" % ("Kriteria", "Hasil", "   Poin"))
    print(line)
    for name, found, got, maks in result:
        print("%-31s %-22s%2d / %d" % (name, found, got, maks))
    print(line)
    print("%-54s%2d / 80" % ("Subtotal otomatis", sum(r[2] for r in result)))
    if notes:
        print("\nCatatan (%d):" % len(notes))
        for n in notes[:12]:
            print("- " + n)
        if len(notes) > 12:
            print("- ... %d catatan lain, muncul setelah yang di atas diperbaiki." % (len(notes) - 12))


if __name__ == "__main__":
    main()
