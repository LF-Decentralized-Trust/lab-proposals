#!/usr/bin/env python3
"""Render a parsed Lab Proposal issue form into proposals/<slug>.md.

Reads the JSON emitted by stefanbuck/github-issue-parser from $ISSUE_JSON
(keys are the form field ids) and writes the markdown file. Emits
``lab_name`` and ``path`` as step outputs.
"""

import json
import os
import re
import sys
from pathlib import Path

# (field id, heading) in the order they appear in the form. Fields with an
# empty value are skipped so the file only carries what the proposer filled in.
SECTIONS = [
    ("Section 1: Mission and Scope", [
        ("short-description", "Short Description"),
        ("scope", "Scope of Lab"),
        ("lfdt-alignment", "Alignment with LFDT Mission"),
        ("relation-to-existing", "Relation to Existing LFDT Labs and Projects"),
    ]),
    ("Section 2: Lab Details", [
        ("activity-code", "Does this lab produce code?"),
        ("activity-spec", "Does this lab produce a specification?"),
        ("repo-url", "Pre-existing Repositories"),
        ("initial-committers", "Initial Committers"),
        ("sponsor", "Sponsor"),
        ("license", "Licensing"),
        ("governance", "Governance Model or Practice"),
        ("security", "Security"),
        ("infrastructure", "Infrastructure and Tooling"),
        ("adoption", "Evidence of Adoption and Use Cases"),
        ("roadmap", "Roadmap"),
    ]),
    ("Section 3: Existing Assets", [
        ("name-and-logo", "Existing Name and Logo"),
        ("website", "Website URL"),
        ("social-media", "Social Media Accounts"),
        ("trademark", "Trademark and Accounts Signoff"),
    ]),
    ("Section 4: Contact Information", [
        ("contact", "Contact name(s) and email(s)"),
        ("signatory", "Contributing or sponsoring entity signatory information"),
        ("additional-info", "Additional Information"),
    ]),
]


def clean(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(f"- {v}" for v in value)
    value = str(value).strip()
    return "" if value == "_No response_" else value


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "unnamed-lab"


def main():
    form = json.loads(os.environ["ISSUE_JSON"])
    lab_name = clean(form.get("lab-name"))
    if not lab_name:
        sys.exit("lab-name is empty; refusing to render")

    issue_number = os.environ["ISSUE_NUMBER"]
    issue_url = os.environ["ISSUE_URL"]
    author = os.environ["ISSUE_AUTHOR"]

    lines = [
        f"# {lab_name}",
        "",
        f"Proposed in [#{issue_number}]({issue_url}) by @{author}.",
        "",
    ]
    for section, fields in SECTIONS:
        body = []
        for field_id, heading in fields:
            value = clean(form.get(field_id))
            if value:
                body += [f"### {heading}", "", value, ""]
        if body:
            lines += [f"## {section}", ""] + body

    path = Path("proposals") / f"{slugify(lab_name)}.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {path}")

    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write(f"lab_name={lab_name}\n")
        out.write(f"path={path}\n")


if __name__ == "__main__":
    main()
