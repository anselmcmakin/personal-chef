"""Personal Chef skill lint. Run: python3 tests/lint_skills.py [skills_dir]  (default: ./skills)
Checks frontmatter, size, and the lines live installs depend on (resume line, install counter URL, Walmart hard rules)."""
import pathlib, re, sys
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "skills")
EXPECTED = {"dinner-plan-getting-started", "dinner-plan-weekly-menu", "dinner-plan-recipe-cards-grocery-list", "dinner-plan-walmart-cart"}
MUST = {
 "dinner-plan-getting-started": ["`Personal Chef setup: Q<n> next`", "`Personal Chef setup: done`",
   "https://github.com/anselmcmakin/personal-chef/releases/download/counter-v1/installed.txt",
   "Never save passwords, payment details, or a street address."],
 "dinner-plan-walmart-cart": ["Never check out, place an order, reserve a time slot, or pay.",
   "Never type, ask for, or see a password or code"],
}
BANNED = [r"\bTODO\b", r"\bFIXME\b", r"lorem ipsum", r"/home/box/agent-data"]
fails = []
def check(c, msg): print(("PASS " if c else "FAIL ") + msg); c or fails.append(msg)
dirs = {p.name for p in root.iterdir() if p.is_dir()}
check(EXPECTED <= dirs, f"all 4 skills present ({sorted(EXPECTED - dirs) or 'ok'})")
for d in sorted(dirs):
    t = (root / d / "SKILL.md").read_text()
    m = re.match(r"---\nname: (.+)\ndescription: >-\n((?:  .+\n)+)---\n", t)
    check(bool(m), f"{d}: frontmatter")
    if m:
        check(m.group(1).strip() == d, f"{d}: name matches folder")
        check(20 <= len(" ".join(m.group(2).split())) <= 500, f"{d}: description length")
    check(len(t.splitlines()) <= 200, f"{d}: under 200 lines ({len(t.splitlines())})")
    for b in BANNED: check(not re.search(b, t, re.I), f"{d}: no '{b}'")
    for s in MUST.get(d, []): check(s in t, f"{d}: keeps {s[:60]}")
print(f"{'FAILED' if fails else 'OK'}: {len(fails)} failure(s)"); sys.exit(1 if fails else 0)
