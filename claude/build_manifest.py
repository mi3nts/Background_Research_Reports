# -*- coding: utf-8 -*-
"""Rebuild Reports/reports.json by SCANNING the Reports/ tree.

Scanning is idempotent and self-heals after a failed run: it never appends
blindly, it just describes what is actually on disk. Mirrors the result into
'MINTS Calendar Report Site/' if that directory still exists.
"""
import os, re, json, datetime, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CADENCES = ["daily", "weekly", "monthly", "yearly"]
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
MIRROR = os.path.join(ROOT, "MINTS Calendar Report Site")


def _title(cad, d):
    if cad == "daily":
        return "Daily digest — %s" % d.strftime("%-d %b %Y")
    if cad == "weekly":
        start = d - datetime.timedelta(days=6)
        return "Week %d · %s – %s" % (
            d.isocalendar()[1],
            start.strftime("%-d %b" if start.year == d.year else "%-d %b %Y"),
            d.strftime("%-d %b %Y"))
    if cad == "monthly":
        return "Monthly review — %s" % d.strftime("%B %Y")
    return "Annual review — %d" % d.year


def build():
    man, problems = {}, []
    for cad in CADENCES:
        folder = os.path.join(ROOT, "Reports", cad)
        # git does not track empty directories, so a fresh clone has no
        # weekly/monthly/yearly folders at all. Create them before scanning.
        os.makedirs(folder, exist_ok=True)
        entries = []
        if os.path.isdir(folder):
            for fn in sorted(os.listdir(folder)):
                # Dot-files are scratch, not reports. The repo mount is delete-restricted,
                # so a superseded rollup is renamed aside as `.trash_*.pdf` and gitignored
                # rather than removed; scanning it produced a spurious PROBLEMS line on
                # every run from 08-08 onward. Skip them silently.
                if fn.startswith(".") or not fn.lower().endswith(".pdf"):
                    continue
                m = DATE_RE.search(fn)
                if not m:
                    problems.append("%s/%s: no parseable YYYY-MM-DD" % (cad, fn))
                    continue
                try:
                    d = datetime.date(*map(int, m.groups()))
                except ValueError:
                    problems.append("%s/%s: invalid date" % (cad, fn))
                    continue
                entries.append({"file": fn, "title": _title(cad, d), "_d": d.isoformat()})
        entries.sort(key=lambda e: e["_d"], reverse=True)   # newest first
        man[cad] = [{"file": e["file"], "title": e["title"]} for e in entries]
    return man, problems


def validate(man):
    bad = []
    for cad, items in man.items():
        for it in items:
            p = os.path.join(ROOT, "Reports", cad, it["file"])
            if not os.path.exists(p):
                bad.append(p)
            if not DATE_RE.search(it["file"]):
                bad.append("unparseable: " + it["file"])
    return bad


if __name__ == "__main__":
    man, problems = build()
    out = os.path.join(ROOT, "Reports", "reports.json")
    json.dump(man, open(out, "w"), indent=2)
    bad = validate(man)
    if os.path.isdir(MIRROR):
        mrep = os.path.join(MIRROR, "Reports")
        copied = 0
        for cad in CADENCES:
            os.makedirs(os.path.join(mrep, cad), exist_ok=True)
            for it in man[cad]:
                src = os.path.join(ROOT, "Reports", cad, it["file"])
                dst = os.path.join(mrep, cad, it["file"])
                # Copy when missing OR when the bytes differ. The previous
                # `if not exists` guard meant a *reissued* PDF never propagated,
                # so the mirror silently drifted: on 31 Jul it still held the
                # pre-correction 28/29 Jul issues and an unproofed 30 Jul build.
                if (not os.path.exists(dst)
                        or os.path.getsize(dst) != os.path.getsize(src)
                        or open(dst, "rb").read() != open(src, "rb").read()):
                    shutil.copy2(src, dst)
                    copied += 1
        json.dump(man, open(os.path.join(mrep, "reports.json"), "w"), indent=2)
        print("mirrored to %s (%d PDF(s) refreshed)" % (mrep, copied))
    print(json.dumps({k: len(v) for k, v in man.items()}))
    if problems:
        print("PROBLEMS:", problems)
    if bad:
        raise SystemExit("MANIFEST VALIDATION FAILED: %s" % bad)
    print("manifest OK")
