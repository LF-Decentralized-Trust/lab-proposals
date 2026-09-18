# Open Privacy Suite

Proposed in [#3](https://github.com/LF-Decentralized-Trust/lab-proposals/issues/3) by @IvanBelyakoff.

## Section 1: Mission and Scope

### Short Description

A privacy and access-control gateway for EVM permissioned networks: it sits between clients and the node as the sole RPC entry point, and enforces per-organisation transaction privacy, role-based method access, and auditable selective disclosure.

### Scope of Lab

## Mission

Permissioned EVM networks are shared ledgers, which means every participant can by default read every other participant's transactions. That is acceptable for a consortium of peers and unacceptable for regulated institutions, which need transaction confidentiality from each other while still giving auditors and regulators a provable, selective view.

Open Privacy Suite provides that layer as open source infrastructure rather than as a per-deployment integration.

## Our work

The gateway is deployed as the only network path between clients and the execution node, so a denial has no alternative route. On that chokepoint it enforces:

- **Identity-bound RPC access** — callers authenticate with verifiable credentials (ZK-proof based, via Privado ID / Iden3, plus enterprise SSO), and every request is resolved to an organisation and a set of claims before it reaches the node.
- **Hierarchical role-based access control** — per-organisation groups with method allowlists and contract-level grants, so what an account may call is policy, not a network-wide constant.
- **Transaction and event-log privacy** — responses are filtered and redacted so a caller sees only the transactions, receipts, logs, and balances its organisation is entitled to see, including for indexed chain data served through a block explorer.
- **Selective disclosure** — a request-and-grant workflow that lets a counterparty or regulator be given visibility into specific contracts or transactions, with the grant recorded rather than implied.
- **Tamper-evident audit** — access decisions and RBAC changes are written to a hash-chained audit log whose integrity is verified on a schedule, so the record of who saw what can be shown to an auditor.

## Origin and history

The lab exists because of a demand the market keeps making and existing tooling keeps answering expensively. Institutions want to operate on shared EVM infrastructure without exposing their business to the other participants on it — but they want that without replacing the execution client they already run, without a bespoke consensus, and without rewriting contracts that are already deployed and audited. Approaches that place privacy in the ledger or in the contract layer ask for exactly those changes, and the cost of making them is a large part of why privacy on permissioned chains is still delivered as bespoke integration work.

Open Privacy Suite was built to that constraint: the enforcement point was moved to the RPC boundary, where it can be applied in front of an unmodified node and unmodified contracts. The code is already public under Apache 2.0 at https://github.com/gateway-fm/open-privacy-suite

## Initial scope

- The gateway itself: authentication, RBAC, response redaction, disclosure workflow, audit log.
- Its administrative API and dashboard for managing organisations, groups, claims, and grants.
- The privacy-aware read path for indexed chain data.
- Documentation for operators deploying it, and the end-to-end test suite that demonstrates the access and visibility rules.

Out of scope: the execution client, the indexer, and the block explorer frontend, which are integrated with but developed outside this lab.

### Alignment with LFDT Mission

Privacy on permissioned EVM chains is today mostly solved per deployment, by integration work that is neither reviewable nor reusable, and whose access rules are impossible for a third party to audit. Access control that decides who may read financial data belongs in code that can be inspected.

LFDT is the right home because this component sits exactly where LFDT's existing work meets: enterprise-grade permissioned ledgers on one side, decentralized identity credentials on the other. Developing it in the open under LFDT lets the design be reviewed by people who are not the vendor, lets operators verify the enforcement rules they depend on, and gives implementers a common starting point instead of rebuilding the same gateway. Neutral governance matters more than usual here, because the users of this component are institutions that need to trust enforcement rules they did not write themselves.

### Relation to Existing LFDT Labs and Projects

The lab is a privacy and policy layer above the execution client, complementing rather than duplicating existing LFDT work. It is designed for EVM permissioned networks of the kind Besu serves, and it authenticates callers with verifiable credentials — today ZK-proof based credentials (Privado ID / Iden3) and enterprise SSO — which is the natural integration point for the credential formats the LFDT identity projects produce. It is not a ledger, a consensus mechanism, or a credential format, so it does not overlap with those projects; it is the enforcement point that sits between them.

What makes it distinct: existing privacy approaches for permissioned EVM chains generally work at the ledger or transaction layer (private state, off-chain payloads). This lab works at the RPC chokepoint instead, which means it applies to unmodified execution clients, covers indexed read paths (explorers, APIs) that ledger-level privacy schemes leave uncovered, and makes the access decision itself auditable.

## Section 2: Lab Details

### Does this lab produce code?

Yes

### Does this lab produce a specification?

No

### Pre-existing Repositories

https://github.com/gateway-fm/open-privacy-suite

### Initial Committers

- https://github.com/IvanBelyakoff — Ivan Belyakov, Gateway.fm
- https://github.com/mandrigin — Igor Mandrigin, Gateway.fm

### Licensing

- [x] I understand that all code hosted in LFDT Labs must be made available under an Apache 2.0 license with DCO sign-off.
- [x] I understand that all specification and standards work in LFDT Labs is done under the Community Specification License 1.0 and the rest of the CSL framework.

### Governance Model or Practice

Current governance is documented at https://github.com/gateway-fm/open-privacy-suite/blob/main/GOVERNANCE.md — routine technical decisions are made through pull request review, and larger changes (licensing, release artifacts, deployment posture, public API compatibility) require maintainer approval. Inbound contributions are accepted under Apache-2.0 with DCO sign-off.

That document describes a single-company maintainer model, which we expect to replace with a governance model appropriate to a lab as other organizations join, and we would welcome the stewards' guidance on what that should look like.

### Security

- Security policy and private reporting process: https://github.com/gateway-fm/open-privacy-suite/blob/main/SECURITY.md — vulnerabilities are reported privately to security@gateway.fm rather than as public issues, and stay private until a fix or mitigation is available.
- Dependency updates are automated through Dependabot.
- CI enforces DCO sign-off on every commit, and includes a dedicated privacy-bypass test suite alongside the unit and end-to-end tests, so that a regression which leaks data across organisations fails the build.
- No OpenSSF Best Practices badge yet; we intend to pursue one.
- Per GOVERNANCE.md the current posture is source-only: no official binaries or container images are published until SBOM, provenance, and binary-distribution license obligations are complete.

### Infrastructure and Tooling

Today: Go backend, Solidity contracts (Foundry), a web frontend, and protobuf/buf-generated APIs. CI and release automation run on GitHub Actions — build and test, DCO check, container builds, releases and release-note linting, Playwright end-to-end tests, and the privacy-bypass suite. Documentation is published as a static site through GitHub Pages. Deployment is via Docker Compose bundles for demo, development, and production topologies.

Anticipated needs from LFDT: the usual community infrastructure — a chat channel, a mailing list, and a home for the documentation site under the lab's own name.

## Section 3: Existing Assets

### Existing Name and Logo

The name "Open Privacy Suite" is currently used for the public repository at https://github.com/gateway-fm/open-privacy-suite. It is not trademarked, and there is no logo associated with the work. We understand the name is subject to review by LFDT trademark counsel and that a lab cannot be named after a product or an existing entity; if alternates are needed for that review, we will supply three or four on request.

### Website URL

https://gateway-fm.github.io/open-privacy-suite/ — the documentation site, published on GitHub Pages. We do not own a dedicated domain for the work and have not purchased any.

### Trademark and Accounts Signoff

- [x] If the lab is accepted, I agree to donate all related trademarks and accounts to the LFDT.

## Section 4: Contact Information

### Contact name(s) and email(s)

Ivan Belyakov (ivan.beliakov@gateway.fm)
Igor Mandrigin (igor@gateway.fm)

### Contributing or sponsoring entity signatory information

If an organization:
| Name | Address | Type (e.g., Delaware corporation) | Signatory name and title | Email address |
|-----------|-----------|-----------|-----------|-----------|
|            |            |            |            |            |

Or, if an individual or individual(s):
| Name | Country | Email address |
|-----------|-----------|-----------|
|            |            |            |
|            |            |            |
|            |            |            |

### Additional Information

**Sponsor.** This proposal does not currently have a sponsor. We would welcome an introduction to a suitable sponsor if the stewards consider one necessary.

**Existing repository and DCO.** The code at https://github.com/gateway-fm/open-privacy-suite is already public under Apache 2.0. DCO sign-off has been enforced on every commit since July 2026, but commits predating that are not signed off, so we plan to bring the code in as a single signed-off initial commit against a new repository in the labs organization, rather than requesting a transfer of the existing repository. All contributions to date are from Gateway.fm employees, so relicensing and sign-off are not blocked by outside contributors.

**Naming.** We have not purchased any domains and will not. Alternates for trademark review can be supplied on request.
