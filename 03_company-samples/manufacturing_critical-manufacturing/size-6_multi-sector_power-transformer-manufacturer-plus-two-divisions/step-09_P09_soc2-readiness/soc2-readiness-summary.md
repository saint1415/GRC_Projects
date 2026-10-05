# SOC 2 Readiness Summary: Cris Santos Company Holdings | Critical Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Critical Manufacturing (focus division: Transformer Manufacturing) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; no criteria text is reproduced |
| Scoping | Per division (section 1). Two readiness reports: the Transformer Manufacturing Fleet Monitoring Service (`soc2-readiness.csv`) and the Grid Engineering client project platform (`soc2-readiness-project-platform.csv`). The Electric Utility is out of scope |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the FMS general manager and the Grid Engineering security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division and service line is whether other organizations rely on its controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Transformer Manufacturing | **Fleet Monitoring Service** (SYS-M6): SaaS asset-health monitoring for about 70 utility subscribers and 18,000 transformers | **Yes.** Utilities send their transformer data to it and rely on its controls; subscribers began asking for a Type 2 report in 2026 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Transformer Manufacturing | Transformers, TMUs, and field service | No. These are products and on-site services, not a hosted service whose controls customers rely on. Product security assurance runs through the 140 utility addenda (P03 G-091 to G-096) | Out of scope | n/a | n/a |
| Grid Engineering | **Client project platform** (SYS-S1): document management for about 3,900 projects, holding client BCSI and CEII | **Yes.** Existing report | **In scope (full).** Existing annual Type 2 | Security, Confidentiality | Type 2, 12 months ending 2026-06-30 (issued); next period ends 2027-06-30 |
| Electric Utility | Electric transmission and distribution service to 1.4 million meters | **No** | **Out of scope** (reasons below) | n/a | n/a |
| Corporate shared services | Identity, SOC, cloud platform | Internal provider only | Carved in to both reports as internal shared services | n/a | n/a |

**Why the Electric Utility is out of scope:**
1. **No user entities.** Retail customers buy electric service. They do not build their own control environment on the utility's systems, which is what a SOC 2 report is for.
2. **Assurance comes from regulators instead.** Its BES Cyber Systems are subject to NERC CIP compliance monitoring and audits by SERC (last audit 2024-10), and the utility files EOP-004-4 and DOE-417 reports (P03 regulation-by-division matrix).
3. **Wholesale counterparties and the RC** rely on NERC standards and operating agreements, not on a SOC report.
4. **Revisit trigger:** if the utility starts hosting systems or data for other utilities (for example, shared outage management), assess whether a SOC 2 report is needed.

**Other assurance options considered.** The vertical overlay names no standard assurance mechanism for critical manufacturing. For the TMU product (not a service), the group considered a secure development certification against ISA/IEC 62443-4-1 for the Grid Products group, separate from SOC 2, and will decide after the signing and SBOM work (POAM-010, POAM-018) is complete. SOC 2 remains the right report for both hosted services because subscribers and clients ask for it by name.

## 2. System descriptions (scope)
### 2.1 Fleet Monitoring Service (Transformer Manufacturing)
- **Services:** ingestion of TMU dissolved gas, temperature, bushing, and load data pushed by utilities from their own data platforms; asset-health scores and alerts from the transformer asset-health analytics (AI-003); subscriber dashboards and reports.
- **Infrastructure and software:** SYS-M6 on cloud provider B (container platform, managed database, warm standby region); utility-initiated, one-way, mutually authenticated TLS ingestion. The FMS has **no connection into utility networks or to TMUs**. Group identity (SYS-G1), SOC (SYS-G2), and landing zone (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider B.
- **People:** about 60 FMS engineers and data scientists plus group SOC and identity teams.
- **Data:** subscriber transformer condition data and asset records (Confidential under POL-04); subscriber user contacts.
- **Complementary user entity controls:** subscribers manage their own user accounts and MFA, control what TMU data they push, and protect the client certificates used for ingestion.

### 2.2 Client project platform (Grid Engineering)
- **Services:** project document management, drawing and settings release, and client sharing for about 260 utility clients and the affiliated Electric Utility.
- **Infrastructure and software:** SYS-S1 on cloud provider B; group common controls carved in (once the inheritance matrix exists, POAM-014).
- **Subservice organizations (carve-out):** cloud provider B.
- **Data:** client BCSI, CEII, protection settings, drawings, and federal contract information.
- **Complementary user entity controls:** clients approve which engineers may see their BCSI folders and tell Grid Engineering when their own staff leave.

## 3. Readiness results
### 3.1 Fleet Monitoring Service (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **28** | **8** | **2** | **23** |

**Why so many Ready criteria for a first-time report:** the control environment, risk assessment, identity, network, endpoint, and SOC criteria are met by group common controls that P07 assessed once (113 of 131 common statements satisfied).
**Not ready:** CC2.3 (no system description and no written security, availability, or notice commitments to subscribers) and A1.3 (the warm standby region has never been failed over in a test).
**Partially ready:** CC3.4 and CC8.1 (AI-003 model and configuration changes were outside change control until 2026-08), CC4.1 (FMS-specific controls not yet in the internal audit sample), CC6.1 (tenant isolation tests manual; P01 MF-010), CC7.2 (FMS application logs of cross-tenant access not in the SIEM), CC7.4 (no subscriber notice terms or contacts), A1.2 (no availability commitment stated), and C1.2 (no deletion procedure for departing subscribers).

**Processing Integrity** is out of scope for the first report, but subscribers already ask how accurate the asset-health scores are. The P10 assessment rates AI-003 Medium tier and recommends deciding on Processing Integrity before the first Type 2 period.

### 3.2 Client project platform (`soc2-readiness-project-platform.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 7 | 0 | 0 |
| Availability (A1, 3) | 0 | 0 | 0 | 3 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **26** | **9** | **0** | **26** |

The platform has an issued Type 2 report, so nothing is Not ready, but the 2026 report carried a deviation and management responses that the next period must clear. **Partially ready:** CC2.3 and CC9.2 (the system description presents group services as division controls, and the platform does not monitor them as providers; scenario gap 6), CC5.3 (2023 standards conflict with group policy), CC6.3, CC6.7, and C1.1 (BCSI and CEII folders not separately restricted; personal cloud storage not blocked), CC7.2 (90-day log retention against a 12-month commitment), CC7.4 (no client terms register or notice route), and C1.2 (closed-project folders kept on legacy file servers). The exercise scenario in P08 showed why C1.2 matters: those archives were the client data stolen.

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | Project platform | CC7.2, CC7.4 | 1-year log archive (POAM-022); client terms register and SOC handoff; tabletop record (POAM-012) |
| 2026 Q4 | Project platform | CC2.3, CC5.3, CC9.2, CC6.3, CC6.7, C1.1 | Inheritance matrix and revised description (POAM-014); re-issued standards; restricted folder permission reports and endpoint policy (POAM-013) |
| 2026 Q4 | FMS | CC3.4, CC8.1, CC6.1, CC7.2 | AI-003 change gate records; automated cross-tenant tests; SIEM rules |
| 2027 Q1 | FMS | CC2.3, CC7.4, A1.2, A1.3, C1.2, CC4.1 | System description and service commitments; subscriber notice terms; failover test; deletion procedure; internal audit test plan. **Type 1 as of 2027-03-31** |
| 2027 Q2 | Project platform | C1.2 | Return or destruction certificates for closed projects; archive migration |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for the project platform period ending 2027-06-30 and the FMS first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the FMS general manager sends subscribers a readiness letter with the 2027 timeline. The Grid Engineering chief operating officer briefs the clients who received the 2026 report on the management responses and the 2026 Q4 fixes.
