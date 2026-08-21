# LFDT Lab Proposals

This repository is where new labs are proposed to [LF Decentralized Trust](https://www.lfdecentralizedtrust.org/).

[LFDT Labs](https://www.lfdecentralizedtrust.org/projects/labs) is a home for early-stage work — a place to build community, contribution, and momentum before a project is mature enough to stand as a top-level LFDT project. Labs are governed by the [overarching lab charter](https://github.com/LF-Decentralized-Trust-labs/governance/blob/main/lf-decentralized-trust-labs_Charter.pdf).

**To propose a lab, [open a Lab Proposal issue](../../issues/new?template=lab-proposal.yml).** Filling out that form is the entire submission.

> [!NOTE]
> This replaces the previous process of forking the labs repository, writing a `[labname].md` proposal, and opening a pull request. You no longer need to do any of that. Blank issues are disabled — every proposal comes in through the form so that stewards see the same information for every lab.

---

## Before you file

A few things are worth settling before you start typing, because they are the most common reasons a proposal stalls.

### Is a lab the right fit?

Labs are for early-stage work. If your work is already mature — with adoption, multiple maintainer organizations, and established governance — you may want to propose it as an incubating project under the [project lifecycle](https://lf-decentralized-trust.github.io/governance/governing-documents/project-lifecycle/) instead.

If you aren't sure which fits, **propose it as a lab and say so under _Additional Information_**. LFDT staff will discuss the options with you.

### What will the lab produce?

A lab can be **a software project**, **a specification**, or **both**. You check one or both boxes on the form, and the answer determines the licensing:

| Activity | License | Also required |
| --- | --- | --- |
| Code | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [DCO](https://developercertificate.org/) sign-off on all commits |
| Specification | [Community Specification License 1.0](https://github.com/CommunitySpecification/1.0/blob/master/01-community-specification-license-v1.md) | The rest of the [CSL](https://github.com/CommunitySpecification/Community_Specification) framework: [CLA](https://github.com/CommunitySpecification/1.0/blob/master/00-contributor-license-agreement.md), [governance](https://github.com/CommunitySpecification/1.0/blob/master/05-governance.md), [code of conduct](https://github.com/CommunitySpecification/1.0/blob/master/08-code-of-conduct.md) |

There is no alternative license option for either. A lab that does both keeps them separate: the code under Apache 2.0, the specification under CSL.

Specifications need CSL rather than an open source license because a specification is a blueprint implemented independently across many codebases, and its patent and copyright grants have to reach all of those implementations. See [getting started with CSL](https://github.com/CommunitySpecification/1.0/blob/master/getting-started.md).

If your code or specification is currently under a different license, say so under _Additional Information_ and we will discuss it with you.

### Pick a name that can survive review

A lab **cannot** be named after a product, a network, or an existing entity. The lab needs its own distinct identity.

Read the [LFDT Naming Guidelines](https://github.com/LF-Decentralized-Trust/wiki/wiki/Naming-Guidelines) first, then check that your candidate:

- is not already in use generally, or in the decentralized technology space
- is clear of trademarks (USPTO, EUIPO, WIPO)
- has `.org` / `.io` domains available
- has no conflicting GitHub presence
- carries no offensive or controversial associations

> [!WARNING]
> **Do not purchase domains yourself.** Buying a domain adds a 90-day transfer delay. LFDT will acquire them.

Names are reviewed by LFDT trademark counsel, so it helps to have **3–4 alternates ready**. List them under _Additional Information_.

### If you have an existing repository

You can bring an existing repository to LFDT Labs, and there are two ways it can happen — a transfer of the existing repository, or a fresh repository in the labs organization that you push into. Either way:

- **Every commit must carry a DCO sign-off** (`git commit -s`, producing a `Signed-off-by:` line). If your existing history does not have it, you will need to **squash the history into a single signed-off commit** for the new lab repository. Plan for this: it means the imported repository starts without its original commit history.
- **The code must be relicensable to Apache 2.0.** If contributions came from people whose sign-off you cannot obtain, raise it under _Additional Information_ before you file.
- **Do not transfer anything yet.** Asset transfer happens during onboarding, after the proposal is approved, coordinated with LFDT staff.

Link the repository in the _Pre-existing Repository_ field so stewards can look at it.

---

## Filing the proposal

[Open a Lab Proposal issue](../../issues/new?template=lab-proposal.yml) and fill out the form. The issue title is prefilled as `[Lab Proposal] <Lab Name>` — replace `<Lab Name>` with your proposed name. The issue is labeled `New Proposal` automatically.

The form has four sections. **Required** fields are marked below; everything else is optional, and "we don't have that yet" is a perfectly good answer for an early-stage lab — leave it blank rather than inventing something.

### Section 1: Mission and Scope

| Field | Required | What to put in it |
| --- | --- | --- |
| **Lab Name** | ✅ | The proposed name, chosen against the naming guidance above. |
| **Short Description** | ✅ | One or two sentences. This becomes the GitHub repository description, so write it as such. |
| **Scope of Lab** | ✅ | What the lab does, its mission, and its origin and history. Give stewards enough to understand the work you intend to do. |
| **Alignment with LFDT Mission** | ✅ | How the lab fits LFDT's mission, and why LFDT is the right home for it. |
| **Relation to Existing LFDT Labs and Projects** | ✅ | What makes it unique, or what makes it better at solving a problem than what already exists. Look through the current labs and projects before answering. |

### Section 2: Lab Details

| Field | Required | What to put in it |
| --- | --- | --- |
| **Technical Activity Type** | — | Check **Code project**, **Specification**, or both. Check at least one — GitHub cannot enforce this for you. |
| **Pre-existing Repository** | | A link to the repository you want to bring in, if any. See [If you have an existing repository](#if-you-have-an-existing-repository). |
| **Initial Committers** | ✅ | GitHub IDs as URLs, one per line. Names and affiliations are helpful but optional. |
| **Sponsor** | | Optional. A sponsor must be a maintainer of an LFDT project, a TAC member, a GB member, or a SIG chair. They help you make connections in the community and help validate that the proposal is cogent and novel — no obligations beyond that initial support. |
| **Licensing** | ✅ | Two acknowledgement checkboxes, both required for every lab regardless of activity type. |
| **Governance Model or Practice** | | A link to `GOVERNANCE.md` or similar, or a description of how the lab will make decisions. |
| **Security** | | An [OpenSSF Best Practices badge](https://www.bestpractices.dev/) link, or a description of your posture — vulnerability reporting, dependency scanning, release signing. |
| **Infrastructure and Tooling** | | What you use today and what you anticipate needing: CI, build and release tooling, hosting, mailing lists, chat. |
| **Evidence of Adoption and Use Cases** | | Examples or references of adoption or application of the work. |
| **Roadmap** | | A link to, or a summary of, a 12-month public roadmap. |

### Section 3: Existing Assets

Tell us about anything already attached to the work — a website, a social media account, a logo, a trademark on the name.

| Field | Required | What to put in it |
| --- | --- | --- |
| **Existing Name and Logo** | | Any existing name and logo, and whether either is trademarked. |
| **Website URL** | | Domains you own, or the URL of the website or documentation portal. |
| **Social Media Accounts** | | Links to existing accounts. |
| **Trademark and Accounts Signoff** | ✅ | A required acknowledgement — see below. |

> [!IMPORTANT]
> By submitting, you agree that **if the lab is accepted, all related trademarks and accounts are donated to LFDT**. See [Section 9 of the LFDT Charter](https://www.lfdecentralizedtrust.org/about/charter).
>
> If you'd prefer not to transfer the trademarks and accounts, that's a conversation, not a dead end — we can work out a new name for the lab so you retain the existing name and its assets. Note it under _Additional Information_.

### Section 4: Contact Information

| Field | Required | What to put in it |
| --- | --- | --- |
| **Contact name(s) and email(s)** | ✅ | The main point(s) of contact, comma-separated. Issues here are public — if you'd rather not post an email address, give a LinkedIn profile or another way to reach you. |
| **Contributing or sponsoring entity signatory** | | Only needed if you have existing assets (trademarks, domains, accounts) to contribute. This is whoever signs the Contribution Agreement assigning those assets to the Linux Foundation. Fill in the organization table or the individual table in the field. |
| **Additional Information** | | Anything else stewards should know: name alternates, an unusual license situation, incubating-project ambitions, open questions. |

---

## What happens next

The issue label tracks where your proposal stands, so you can see its status at a glance:

| Label | Meaning |
| --- | --- |
| `New Proposal` | You submitted the form. Applied automatically. |
| `Steward Review` | The labs stewards are evaluating whether the lab is cogent and novel, and whether LFDT is the right home for it. |
| `Approved` | You work with LFDT staff on onboarding: existing asset transfer (if applicable), repository creation or transfer, infrastructure setup, and announcement. |
| `Declined` | Stewards will explain why, and where the work might fit better. |

Stewards review each proposal to make sure it is **cogent** — clear enough to understand what you intend to build — and **novel** in its conception, its proposed execution, or its interested community.

Review happens in the open, in the issue. Stewards may ask questions there; **answer in the comments rather than editing the issue body**, so the discussion stays readable. If you need to correct a field, edit it and leave a comment saying what changed.

There is no fixed SLA. If a proposal has gone quiet, a polite comment on the issue is the right nudge.

---

## Questions

If something in the form is unclear, or you want to talk through fit before filing, open an issue anyway and say so under _Additional Information_ — a partially-formed proposal that starts a conversation is more useful than a proposal that never gets filed.
