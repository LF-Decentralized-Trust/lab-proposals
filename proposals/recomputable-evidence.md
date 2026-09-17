# recomputable-evidence

Proposed in [#2](https://github.com/LF-Decentralized-Trust/lab-proposals/issues/2) by @giskard09.

## Section 1: Mission and Scope

### Short Description

A neutral home for testing whether independently-authored evidence-record specifications
compose without silently laundering authority between them — criteria as substrate, not a
single reference implementation owned by any one contributor. Neutrality is enforced as a
testable rubric, not asserted: a composition fails if removing one party's signature still
validates under another party's spec.

### Scope of Lab

Multiple independent groups (AXES, argentum-core/action-ref, Tersign, trust-evidence-format,
and others) are converging on overlapping primitives for verifiable evidence of agent/system
actions — canonicalization, custody/independence assertions, delegation chains — without a
shared, neutral venue to test cross-implementation composition. Today that testing happens ad
hoc, bilaterally, across unrelated GitHub threads, with no persistent record of which
cross-suite checks passed.

This lab does not propose a single winning spec. It proposes a venue where:

- **Neutrality criteria** for judging composition and independence between
  independently-stewarded specs are authored jointly by the specs' own stewards — not
  delivered by one author for others to ratify. First concrete instance already merged: an
  independence rubric (R1–R5, stdlib-only Python verifier, 5 signed fixtures —
  valid-composition, laundered-authority, copy-with-binding, or-composition-scope-boundary,
  cross-suite-binding; curve-agnostic, Ed25519 and BIP340/Schnorr both pass), authored by one
  founding committer, independently re-run cold by another, with the binding hash under a
  lab-owned domain-separation tag (`recomputable-evidence.independence:v1:`) rather than any
  single member spec's own tag — a third founding committer flagged that neutrality gap before
  merge, the fix shipped, and only then did the criteria merge. See
  `giskard09/composed-attestation-3leg-worked-example` PR#2 (merged).
- **Cross-suite conformance fixtures** (byte-pinned, reproducible offline, no live-endpoint
  dependency) accumulate as the actual evidence of interoperability — checkable, not asserted.
  Initial pair: action-ref/custody-ref and the AXES Golden Trace corpus, expanding as other
  specs opt in. The independence rubric above already covers a curve-agnostic cross-suite
  binding case, marked explicitly incomplete (`NEEDED_FROM_CO_SUITE`) where a piece depends on
  another party's in-progress work — an honest partial result kept in place of a disguised one.
- Any spec entering keeps its own repo, stewardship, and identity — nothing is folded, merged,
  or squash-committed into a combined history. A criteria set that no single implementation
  owns is a stronger criteria set than one authored and graded by the same party.

### Alignment with LFDT Mission

LFDT's mission is neutral, vendor-independent infrastructure for decentralized trust —
governed jointly, not owned by whichever contributor got there first. This lab applies that
same principle one layer up: instead of proposing a neutral protocol, it proposes a neutral
*test* for whether protocols that already exist independently (several outside LFDT entirely)
actually compose without one silently subsuming another's authority. The deliverable is
infrastructure other specs plug into — fixtures and a verifier, not a single winning
implementation — which is the same shape as other interoperability-focused LFDT work.

### Relation to Existing LFDT Labs and Projects

`LF-Decentralized-Trust-labs#411` (aeoess, `agent-authority-conformance`) sits in the same
general space — conformance for agent evidence. This is not a competing claim on that
territory: different entry point. `agent-authority-conformance` sets a conformance bar for one
spec family; `recomputable-evidence` tests composition *between* independently-governed spec
families that have no reason to standardize on each other's format. The two can coexist and
may cross-reference fixtures later if useful to both — no such cross-reference exists yet, and
this proposal does not depend on one.

## Section 2: Lab Details

### Does this lab produce code?

Yes — fixtures, verifiers, CI tooling (Apache 2.0, DCO sign-off).

### Does this lab produce a specification?

No, not initially. The independence rubric (`rubric.md`) is normative-language criteria text
shipped alongside the code, but the lab is not proposing to bring the four member specs
(action-ref, CTEF, AXES, custody-ref) under a shared CSL specification — each keeps its own
license and governance, per the Scope above. If the rubric itself grows into standalone
standards-track work, that would be raised with stewards as a separate step, not assumed here.

### Pre-existing Repositories

https://github.com/giskard09/action-ref-conformance

Relicensed Apache-2.0 (commit `5fb8f2ad`). Disclosed proactively: only 1 of 6 commits in this
repo's history currently carries a DCO `Signed-off-by` line — per the onboarding process, this
will need squashing into a single signed-off commit for the lab repository. Flagging this now
rather than leaving it for a steward to find. Deliberately not proposing `argentum-core` (many
commits, several distinct external contributors) as the seed — squashing or relicensing that
history would erase real external attribution and break hashes already cited in public
threads. The lab starts from the smallest clean seed, not the biggest existing repo.

### Initial Committers

- https://github.com/giskard09
- https://github.com/azender1 (SafeAgent — integrator partner under a signed Revenue Share
  Agreement with us; naming the commercial tie here rather than leaving it for a steward to
  find. Recusal: azender1 recuses from any decision that directly affects his own commercial
  interest — e.g., prioritization of a spec he has a stake in, or test design that would
  advantage it — a plain governance rule, not a special exception.)
- https://github.com/magentixai (Martin Sansone — Founder of Magentix AI, author of the
  Enhanced Fraud Data standard at Pay.UK; also steering the x402 Foundation TSC
  evidence-record charter, a related but separate institutional track from this lab)
- https://github.com/kenneives (AgentGraph/AgentAvow; authored the independence rubric cited
  above under Scope of Lab)

### Sponsor

https://github.com/arsulegai — Arun S M, TAC Chair, LF Decentralized Trust. Not yet
approached directly. Cleared internally by two of the four founding committers before listing
him here: kenneives (2026-08-15, "OK to arsulegai as sponsor, conditioned on Martin also
signing off") and magentixai/Sansone (2026-08-17, asked whether TAC-chair-as-sponsor creates a
conflict when the same person might later weigh in as a steward — confirmed against LFDT's own
governance docs that sponsor and steward are separate roles and he is not currently on the
steward list, no structural conflict — Sansone gave explicit sign-off after that, not just
non-objection). No firm commitment from arsulegai himself yet; listing him here is the
founding cohort's proposal, not a confirmed sponsorship — happy to have stewards treat this
field as provisional if he has not been reached by the time of review.

### Licensing

☑ I understand that all code hosted in LFDT Labs must be made available under an Apache 2.0
license with DCO sign-off.
☑ I understand that all specification and standards work in LFDT Labs is done under the
Community Specification License 1.0 and the rest of the CSL framework.

### Governance Model or Practice

No formal `GOVERNANCE.md` yet. First concrete mechanism: neutrality criteria are authored
jointly by founding committers and merged only after independent re-verification by a
different committer than the author — demonstrated in PR#2 above, where one committer authored
the rubric, a second independently re-ran it cold, and a third found and required a fix to a
non-neutral domain-separation tag before merge.

### Security

No OpenSSF Best Practices badge yet. No formal vulnerability-reporting process yet — this is
an early-stage lab; will establish one as adoption grows.

### Infrastructure and Tooling

GitHub Actions CI already in use on the seed repo and on member-spec repos (e.g.
`argentum-core`'s Contributor Check + lint/audit gates). No dedicated mailing list or chat yet.

### Evidence of Adoption and Use Cases

- Independence rubric (PR#2) verified independently, cold, by a founding committer other than
  its author — not just declared, re-run.
- `action_ref` (one of the specs this lab's fixtures cover) has independent third-party
  cross-implementation verification: two separate outside implementers (whawk46,
  SolomonisBlack/GVP) each ran their own canonicalizer against published test vectors with
  zero byte-level divergence, on different days, without coordinating with each other.
- SafeAgent (azender1, integrator partner) runs `action_ref`-based trails in production on
  every settle call, anchored on Arbitrum mainnet — not a demo, a live commercial deployment.
- Cross-spec convergence in the open: independent implementers on unrelated projects
  (`microsoft/agent-governance-toolkit`, x402 Foundation issues) have converged on the same
  domain-separation and instance-binding disciplines this lab's rubric encodes, without
  prompting, across at least three separate specs in August 2026 alone.
- RFC 8785 (JCS) fixture pack cross-checked independently against the `rfc8785` PyPI reference
  implementation (v0.1.4) by a founding committer, reproduced cold rather than trusted from a
  prior write-up: 4/4 vectors pass.

### Roadmap

No published 12-month roadmap yet. Near-term, concrete: fold the pending
`NEEDED_FROM_CO_SUITE` cross-suite-binding fixture once the counterpart spec's binding_ref
lands; onboard additional independently-governed specs' fixtures as they opt in.

## Section 3: Existing Assets

### Existing Name and Logo

None.

### Website URL

None.

### Social Media Accounts

None.

### Trademark and Accounts Signoff

☑ If the lab is accepted, I agree to donate all related trademarks and accounts to the LFDT.

## Section 4: Contact Information

### Contact name(s) and email(s)

Pablo Etcheverry — https://www.linkedin.com/in/pablo-etcheverry-5924119/

### Contributing or sponsoring entity signatory information

(blank — no existing assets to transfer: no trademark, no domain, no accounts)

### Additional Information

Naming — disclosing this proactively rather than waiting for trademark counsel to find it:
`github.com/RecomputableEvidence` exists (account created 2025-09-21) with an active
repository (`fork-public-evidence`, pushed as recently as today) in an adjacent domain —
boundary-recording for AI-assisted workflow handoffs, not evidence-record interop testing.
Zero followers, zero stars, no organizational affiliation found. We believe the name remains
available for the lab (different scope, different kind of GitHub entity — a lab name vs. a
personal account name), but are flagging it rather than asserting "zero collisions." Three
alternates we'd be glad to use if counsel prefers, all verified as free GitHub usernames today:
`recomputable-attestation`, `cross-suite-evidence`, `composable-evidence-criteria`.

This lab deliberately coexists with LF-Decentralized-Trust-labs#411 (aeoess) — see Relation
to Existing Labs above, same general space, different entry point, no claim of exclusive
territory.
