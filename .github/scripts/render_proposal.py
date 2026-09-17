#!/usr/bin/env python3
"""Render a Lab Proposal issue body into proposals/<slug>.md.

Reads the issue body from $ISSUE_BODY and splits it on the ``### <label>``
headings that GitHub issue forms produce. Hand-written issues that copy the
form's headings work too: a blank line after the heading is optional, and
stray ``#``/``##`` headings and ``---`` rules between fields are ignored.
Emits ``lab_name`` and ``path`` as step outputs.
"""

import os
import re
import sys
from pathlib import Path

# (heading, [aliases]) in form order. Aliases cover older hand-written
# proposals whose headings differ slightly from the form.
SECTIONS = [
    ("Section 1: Mission and Scope", [
        ("Short Description", []),
        ("Scope of Lab", []),
        ("Alignment with LFDT Mission", []),
        ("Relation to Existing LFDT Labs and Projects", []),
    ]),
    ("Section 2: Lab Details", [
        ("Does this lab produce code?", []),
        ("Does this lab produce a specification?", []),
        ("Pre-existing Repositories", ["Pre-existing Repository"]),
        ("Initial Committers", []),
        ("Sponsor", []),
        ("Licensing", []),
        ("Governance Model or Practice", []),
        ("Security", []),
        ("Infrastructure and Tooling", []),
        ("Evidence of Adoption and Use Cases", []),
        ("Roadmap", []),
    ]),
    ("Section 3: Existing Assets", [
        ("Existing Name and Logo", []),
        ("Website URL", []),
        ("Social Media Accounts", []),
        ("Trademark and Accounts Signoff", []),
    ]),
    ("Section 4: Contact Information", [
        ("Contact name(s) and email(s)", []),
        ("Contributing or sponsoring entity signatory information", []),
        ("Additional Information", []),
    ]),
]

HEADING = re.compile(r"^###\s+(.+?)\s*$")
NOISE = re.compile(r"^(#{1,2}\s|---\s*$)")


def norm(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def parse(body):
    """Return {normalised heading: value} for every ### heading in the body."""
    fields = {}
    current = None
    for line in body.splitlines():
        m = HEADING.match(line)
        if m:
            current = norm(m.group(1))
            fields[current] = []
        elif current is not None:
            fields[current].append(line.rstrip())
    out = {}
    for key, lines in fields.items():
        while lines and (not lines[-1].strip() or NOISE.match(lines[-1])):
            lines.pop()
        while lines and not lines[0].strip():
            lines.pop(0)
        value = "\n".join(lines).strip()
        out[key] = "" if value == "_No response_" else value
    return out


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "unnamed-lab"


def main():
    fields = parse(os.environ["ISSUE_BODY"])
    lab_name = fields.get(norm("Lab Name"), "")
    if not lab_name:
        sys.exit("Lab Name is empty or missing; refusing to render")

    issue_number = os.environ["ISSUE_NUMBER"]
    issue_url = os.environ["ISSUE_URL"]
    author = os.environ["ISSUE_AUTHOR"]

    used = {norm("Lab Name")}
    lines = [
        f"# {lab_name}",
        "",
        f"Proposed in [#{issue_number}]({issue_url}) by @{author}.",
        "",
    ]
    for section, headings in SECTIONS:
        body = []
        for heading, aliases in headings:
            for candidate in [heading] + aliases:
                key = norm(candidate)
                if key in fields:
                    used.add(key)
                    if fields[key]:
                        body += [f"### {heading}", "", fields[key], ""]
                    break
        if body:
            lines += [f"## {section}", ""] + body

    for key in fields:
        if key not in used:
            print(f"::warning::ignored unknown heading '{key}'")

    path = Path("proposals") / f"{slugify(lab_name)}.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {path}")

    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write(f"lab_name={lab_name}\n")
        out.write(f"path={path}\n")


if __name__ == "__main__":
    main()
