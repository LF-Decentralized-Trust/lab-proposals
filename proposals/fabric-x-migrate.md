# Fabric-X-Migrate

Proposed in [#21](https://github.com/LF-Decentralized-Trust/lab-proposals/issues/21) by @syndbg.

## Section 1: Mission and Scope

### Short Description

A CLI tool to migrate application state from Hyperledger Fabric into Fabric-X. The proposed CLI name is `fxmigrate`.

### Scope of Lab

The goal of this lab is to bring the complete Fabric-to-Fabric-X migration tool into production-usable state and maintain it as an LFDT Labs project. It will move the existing `fabric-x-migrate-poc` (https://github.com/syndbg/fabric-x-migrate-poc) tool into an LFDT Labs repository, then develop and release it as the `fxmigrate` CLI.

`fxmigrate` will provide an end-to-end workflow for migrating Fabric application state from peer snapshots into Fabric-X.

This work originates from the Fabric-X snapshot migration RFC ([PR #9](https://github.com/hyperledger/fabric-x-rfcs/pull/9)), which led to the migration proof of concept. The existing test harness exercises both database backends, Classic snapshot formats, a real Arma orderer, two running committers, and backup, restore, and catch-up.

### Alignment with LFDT Mission

The lab will provide open tooling for organizations moving existing ledger state to Fabric-X. It builds on LFDT ledger projects and lets operators and contributors improve compatibility and safety practices in the open. An LFDT Lab is a suitable early-stage home while the contributor community, governance, adoption, and releases develop.

### Relation to Existing LFDT Labs and Projects

Hyperledger Fabric is the source ledger and Fabric-X is the target runtime. `fxmigrate` prepares target application state. It does not replace either ledger or change their protocols. The LFDT Labs organization also hosts a Fabric-X block explorer, which helps inspect a running network. This proposal focuses on importing state before application traffic starts.

## Section 2: Lab Details

### Does this lab produce code?

Yes

### Does this lab produce a specification?

No

### Pre-existing Repositories

- https://github.com/syndbg/fabric-x-migrate-poc/

### Initial Committers

- https://github.com/syndbg/

### Licensing

- [x] I understand that all code hosted in LFDT Labs must be made available under an Apache 2.0 license with DCO sign-off.
- [x] I understand that all specification and standards work in LFDT Labs is done under the Community Specification License 1.0 and the rest of the CSL framework.

### Governance Model or Practice

The PoC has no documented lab governance. Proposed starting practice: make decisions in public issues and pull requests, require review before merge.

### Security

The lab should document vulnerability reporting, dependency scanning, release signing, and the limits of source verification. One way to do it is via an explicit SECURITY.md policy based on other LFDT projects and then also dependabot configuration to ensure CVE updates cadence. Note dependabot would also include cooldown days to avoid 0 day exploits, although nowadays it should have a 3 days default.

### Infrastructure and Tooling

The PoC uses Go, GitHub Actions, Fabric, PostgreSQL, YugabyteDB, and local Arma acceptance tests. The lab will need a hosted GitHub repository, CI for supported snapshot formats and database backends, and a reviewed release process for `fxmigrate`. No production service infrastructure is proposed.

### Evidence of Adoption and Use Cases

No production adopters are claimed. Evidence today is the PoC and its tests: snapshot import, application authorization checks, and backup, restore, and catch-up scenarios against PostgreSQL and YugabyteDB. This demonstrates a controlled test setup, not customer deployment or production readiness.

## Section 3: Existing Assets

### Existing Name and Logo

The existing repository is named `fabric-x-migrate-poc`; the proposed CLI is `fxmigrate`. No lab logo or registered mark.

### Trademark and Accounts Signoff

- [x] If the lab is accepted, I agree to donate all related trademarks and accounts to the LFDT.

## Section 4: Contact Information

### Contact name(s) and email(s)

Anton Antonov — anton.synd.antonov@gmail.com
