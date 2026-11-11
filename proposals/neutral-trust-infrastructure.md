# Neutral Trust Infrastructure

Proposed in [#36](https://github.com/LF-Decentralized-Trust/lab-proposals/issues/36) by @abisheakp197.

## Section 1: Mission and Scope

### Short Description

A post-quantum runtime enforcement sidecar providing cryptographic trust and execution boundaries for autonomous AI agents.

### Scope of Lab

The Neutral Trust Infrastructure (NTI) Lab will maintain and develop a vendor-neutral, post-quantum (ML-DSA-87) runtime enforcement sidecar for AI agents. The lab's mission is to secure the machine economy by ensuring that AI agent actions are cryptographically authorized at the exact moment of execution, without relying on centralized gatekeepers.
      Origin: NTI was born out of the W3C AI Agent Protocol and AIWSS Community Groups, recognizing that identity and evidence layers need a standardized, fail-closed runtime enforcement layer. The lab will maintain the reference implementation, publish conformance test vectors, and drive adoption across open-source AI frameworks.

### Alignment with LFDT Mission

LFDT's mission is to build open, decentralized trust. NTI aligns perfectly by solving the "execution gap" in decentralized AI. A verifiable credential or DID is useless if the agent executing the action can be compromised at runtime. NTI provides the decentralized, neutral infrastructure required to enforce policy mathematically, ensuring no single entity controls the trust layer for the machine economy.

### Relation to Existing LFDT Labs and Projects

NTI is complementary to existing LFDT identity and credentialing projects (e.g., Identus, AnonCreds, ThunderID). NTI does not issue identities or credentials; it acts as the Layer 1 runtime enforcement boundary that verifies the cryptographic receipts issued by those systems when an AI agent executes a tool call. It interoperates cleanly with the Agent Passport System (APS) and the Agent Authority Conformance Lab.

## Section 2: Lab Details

### Does this lab produce code?

Yes

### Does this lab produce a specification?

Yes

### Pre-existing Repositories

- https://github.com/abisheakp197/Neutral-Trust-Infrastructure
- https://github.com/abisheakp197/nti-spec

### Initial Committers

- Abisheak P. (@abisheakp197) - Lead Architect
  - Tymofii Pidlisnyi (@aeoess) - Agent Passport System
  - Steven Zhao (@zhaoxinghua09-cell) - Independent Researcher
  - Larry Lewis (@llewis) - Chair, W3C Agent Trust Protocol CG

### Sponsor

Tymofii Pidlisnyi (tima@aeoess.com) - Maintainer, Agent Authority Conformance LFDT Lab

### Licensing

- [x] I understand that all code hosted in LFDT Labs must be made available under an Apache 2.0 license with DCO sign-off.
- [x] I understand that all specification and standards work in LFDT Labs is done under the Community Specification License 1.0 and the rest of the CSL framework.

### Governance Model or Practice

NTI utilizes a rough-consensus governance model documented in the repository's GOVERNANCE.md. The TSC consists of the initial committers, and decisions are made transparently via public GitHub issues and pull requests. DCO is fully enforced.

### Security

The project has an active SECURITY.md, DCO enforcement, and relies on OpenSSF Scorecard and CodeQL for continuous scanning. Branch protection rulesets are active. A reproducible cryptographic witness package (S4/S5/S6 seals) is published, and an independent security assessment via the AACP (REMORA) framework has been documented and remediated.

### Infrastructure and Tooling

Currently utilizing GitHub Actions for CI/CD, CodeQL for security scanning, Sigstore for release signing, and Dependabot for dependency management. Anticipating the need for LFDT-hosted mailing lists and potential HSM integration for the conformance lab in the future.

### Evidence of Adoption and Use Cases

NTI has been formally endorsed by W3C members (Atharv, Prashanna Bableshwar, Daveed Benjamin). It features a live cryptographic witness package and has been integrated into the Agent Passport System (APS) conformance lab for delegation chain verification. It is designed to wrap and secure leading open-source frameworks like CrewAI, LangChain, and AutoGen.

### Roadmap

12-month public roadmap available at: https://github.com/abisheakp197/nti-spec/blob/main/docs/ROADMAP.md (Milestones include: LFDT Lab onboarding, v1.0 Specification release, third-party security audit, and Rust/Python SDK hardening).

## Section 3: Existing Assets

### Existing Name and Logo

Name: Neutral Trust Infrastructure (NTI). No trademark or official logo currently filed.

### Website URL

https://nti-leaderboard.vercel.app

### Social Media Accounts

None

### Trademark and Accounts Signoff

- [x] If the lab is accepted, I agree to donate all related trademarks and accounts to the LFDT.

## Section 4: Contact Information

### Contact name(s) and email(s)

Abisheak P. - abisheakp197@gmail.com

### Contributing or sponsoring entity signatory information

If an individual or individual(s):
| Name | Country | Email address |
|---|---|---|
| Abisheak P. | India | abisheakp197@gmail.com |

### Additional Information

Regarding the REMORA/AACP assessment: This was an independent assessment run by Stian Skogbrott. While the publication's claim ceiling is SECOND_IMPLEMENTATION/BCR-2 (not a formal independent audit), the findings regarding Merkle odd-node duplication and key binding were validated, remediated, and regression-tested in our main branch.
      Regarding Diversity: We have met the ≥2 organization requirement by including maintainers from NTI, APS, and independent researchers, alongside a W3C CG Chair.
      Regarding the Name: If "Neutral Trust Infrastructure" conflicts with trademark counsel review, alternates we have considered are: "NTI Labs", "Neutral Execution Layer", or "NTI Protocol".
