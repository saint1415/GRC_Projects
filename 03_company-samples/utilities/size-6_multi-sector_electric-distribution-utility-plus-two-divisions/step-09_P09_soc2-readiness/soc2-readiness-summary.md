# SOC 2 Readiness Summary: Cris Santos Company Holdings | Utilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: Engineering Services client project platform (`soc2-readiness.csv`). The Electric Utility and Gas Production are out of scope; the Electric Utility's review of its AMI vendor's SOC 2 report is in `vendor-soc2-review.csv` |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Engineering Services security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build into their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Engineering Services | Engineering and NERC CIP consulting delivered through the client project platform (SYS-S1), for about 300 utilities | **Yes.** Clients rely on its controls for their CEII and BCSI and for their own CIP-011-3 and CIP-013-2 obligations, and ask for a SOC 2 report | **In scope.** Type 1 issued as of 2026-03-31 | Security, Availability, Confidentiality | Type 2 for 2027-01-01 to 2027-06-30 |
| Electric Utility | Retail electric delivery to 2.4 million customers | **No.** Customers buy electricity; they do not rely on its systems as part of their own controls | **Out of scope** (reasons below); reviews its vendors' SOC 2 reports instead | n/a | n/a |
| Gas Production | Gas sales to 14 generating plants | **No.** Generators buy a commodity, not an outsourced service | **Out of scope** | n/a | n/a |

**Why the Electric Utility is out of scope:**
1. **No user entities.** Retail customers and the state regulator are not user entities. No one relies on the Electric Utility's controls as part of their own control environment.
2. **Assurance comes from regulators instead.** The vertical's assurance alternative is NERC CIP compliance audits by the Regional Entity, which are mandatory for the Electric Utility (SERC audited it in 2024). The state public service commission oversees service quality.
3. **Its own reliance runs the other way.** The Electric Utility relies on vendors' SOC 2 reports for its SaaS systems. The AMI head-end vendor's report was reviewed this year (`vendor-soc2-review.csv`): reliable, with two exceptions to follow up and one complementary user entity control (bulk disconnect thresholds) not yet configured (P01 EU-015).
4. **Revisit trigger:** if the Electric Utility starts offering shared services to other utilities (for example, hosting distribution systems for municipal utilities), assess the need for a SOC 2 report.

**Why Gas Production is out of scope:** it sells gas under supply contracts; generators rely on deliveries, not on its systems. Its security assurance to the group comes from P03 and P07. **Revisit trigger:** if it takes on operating gathering or processing for third parties.

**Other assurance options considered.** Some utility clients accept a completed industry vendor security questionnaire or audit the vendor directly under their CIP-013-2 processes. Engineering Services will keep answering those, but a SOC 2 Type 2 report reduces the number of client audits, which was the business reason for starting the program.

## 2. System description (scope): Engineering Services client project platform
- **Services:** transmission, distribution, substation, protection and control, and SCADA/EMS engineering; NERC CIP consulting; exchange of drawings, settings files, and studies with clients.
- **Infrastructure and software:** SYS-S1 on cloud provider B (document management and collaboration, group-managed keys, 4-hour snapshots, immutable copies in the group vault); SYS-G1 identity and SYS-G2 SOC as internal shared services. **To add:** SYS-G4, through which engineers reach client and affiliate OT, and the AI design assistant pilot (scenario gaps 1 and 5).
- **Subservice organizations (carve-out):** cloud provider B; the third-party AI service, if the pilot continues.
- **People:** about 24,600 Engineering Services employees, plus group identity, SOC, and cloud teams.
- **Data:** client CEII and BCSI, client project data, Federal Contract Information for federal civilian clients.
- **Complementary user entity controls:** clients approve access lists for their CEII and BCSI folders, notify Engineering Services of their own access revocations, and review delivered files with the published hashes.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria:** control environment, risk assessment, monitoring, identity, network, and SOC criteria are met by group common controls, which P07 assessed once for all divisions, and were already tested for the Type 1 report.

**Not ready:** CC6.3. CEII and BCSI folders inherit project-wide group permissions; a non-project engineer opened restricted folders on 9 of 25 sampled projects (P07; POAM-020). A Type 2 auditor would almost certainly report this as an exception.

**Partially ready:** CC2.3 (system description and client notice commitments), CC3.4 (AI pilot started without a change assessment), CC6.2 (contractor deprovisioning; client-approved access lists), CC6.7 (personal cloud storage and AI uploads), CC7.1 (two provider B accounts outside guardrails), CC7.4 (client notices not part of incident response), CC9.2 (AI service not assessed), A1.3 (restore testing), C1.1 (inconsistent CEII and BCSI classification), and C1.2 (no destruction certificates at project close).

**Processing Integrity and Privacy** are out of scope: Engineering Services makes no processing integrity commitments, and SYS-S1 does not hold personal information collected for clients. **Revisit trigger:** if the AI design assistant becomes part of a client deliverable, clients may ask for processing integrity commitments (P10).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.3, CC6.2, CC6.7, C1.1 | Restricted folder design; client-approved access lists; personal storage block; AI upload block; folder classification at project setup |
| 2026 Q4 | CC2.3, CC3.4, CC9.2, CC7.4 | Updated system description (SYS-G4, AI service); client notice register; AI service assessment; tabletop record (2026-12-15) |
| 2026 Q4 | CC7.1 | Guardrail coverage report for all provider B accounts |
| 2027 Q1 | A1.3, C1.2 | Quarterly restore test; regional outage tabletop; close-out certificates |
| 2027 Q1 to Q2 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-01-01 to 2027-06-30) |

**Start date is a decision.** If CC6.3 is not remediated by 2026-12-31, the group will move the Type 2 period start to 2027-04-01 rather than carry a known exception into the first report.

**Communication:** the Engineering Services chief operating officer sends the top 40 clients a readiness letter with the 2027 timeline and the changes to CEII and BCSI folder access.
