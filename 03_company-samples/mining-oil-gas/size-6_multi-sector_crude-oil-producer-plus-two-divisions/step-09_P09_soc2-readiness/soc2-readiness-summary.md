# SOC 2 Readiness Summary: Cris Santos Company Holdings | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are listed by ID with short topic labels; the AICPA text is not reproduced |
| Scoping | Per division (section 1). One readiness report: the Crude Logistics shipper services platform (`soc2-readiness.csv`). Crude Oil Production and Power Generation are out of scope |
| Categories in scope | Security, Availability, Processing Integrity, Confidentiality (Privacy not in scope) |
| Target report | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, issued before the end of 2027 |
| Prepared | Self-assessment 2026-08-31 to 2026-09-04 by the Group Chief Risk Officer's assurance team with the Crude Logistics security and compliance lead; approved 2026-09-17 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Crude Logistics | Gathering, trunk line, and trucking for about 85 third-party shippers, with the shipper services platform (SYS-M3): nominations, run tickets, measurement and allocation statements | **Yes.** Shippers rely on its run tickets, measurement, and statements for their own revenue, royalty, and tax reporting. About 120 security questionnaires were answered in 2025, and the three largest shippers asked for a SOC 2 Type 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Processing Integrity, Confidentiality | Type 1 as of 2027-03-31, then Type 2 |
| Crude Oil Production | Crude and gas sales; operator of wells for about 2,600 non-operating working interest owners | **No SOC 2.** Purchasers and the gas processor buy commodities, not a service. Non-operating partners rely on the division's joint interest billing, which is a financial reporting matter they audit under their operating agreements' audit clauses | **Out of scope** | n/a | n/a |
| Power Generation | Wholesale electricity sales | **No.** Market operators and counterparties buy energy, not an outsourced service; reliability assurance comes from NERC standards and Regional Entity audits | **Out of scope** | n/a | n/a |

**Why Processing Integrity is in scope.** The shippers' main question is whether run tickets, measured volumes, and allocation statements are complete and accurate, because they pay royalties and taxes on them. Security and Availability alone would not answer it.

**Why Privacy is not in scope.** Shippers are businesses. The platform holds driver names on run tickets but makes no privacy commitments to individuals; driver and royalty owner personal data are governed by POL-04 and state law (P03), not by this report.

**Revisit triggers:** if non-operating partners ask for assurance over joint interest billing, assess a SOC 1 report for Production; if Power Generation begins operating plants for other owners, assess whether those owners are user entities.

**Other assurance options considered.** No sector-specific assurance mechanism is named in the vertical overlay for oil and gas or for transportation. Some shippers accept a completed industry questionnaire with the group's P03 and P07 results; the three largest asked specifically for SOC 2, so SOC 2 is the primary report.

## 2. System description (scope)
- **Services:** shipper nominations, truck dispatch, electronic run tickets, custody transfer measurement data (from the SYS-M2 measurement data system), monthly allocation statements, and the shipper portal.
- **Infrastructure and software:** SYS-M3 on cloud provider A (containers, managed database, web application firewall), backups in provider B; the run ticket app on managed driver phones; the measurement data system interface. Group identity (SYS-G1), SOC (SYS-G2), and cloud platform (SYS-G3) are **carved in** as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the customer identity vendor for shipper sign-in; the telematics vendor (location and ELD data used by dispatch).
- **Out of the system boundary:** the pipeline SCADA and Pipeline Control Center (SYS-M1) and the field flow computers themselves (operational technology covered by Part 195 and the P02 approach), and Production division systems.
- **People:** about 300 Crude Logistics staff in commercial, dispatch, and measurement roles, plus the group SOC and identity teams.
- **Data:** shipper nominations, volumes, run tickets, and statements (Confidential under POL-04).
- **Complementary user entity controls:** shippers manage their own portal users and review statements within the dispute window in their contracts.

## 3. Readiness results
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 8 | 1 |  |
| Availability (A1, 3) | 2 | 1 |  |  |
| Processing Integrity (PI1, 5) | 3 | 2 |  |  |
| Confidentiality (C1, 2) |  | 2 |  |  |
| Privacy (P1-P8, 18) |  |  |  | 18 |

**Why many Security criteria are already Ready:** control environment, identity, network, monitoring, backup, and change controls come from group common controls that internal audit assessed once in P07, and the platform's own pipeline-based change process is mature.

**Not ready:** CC2.3. There is no system description and no written statement of service commitments to shippers, and the notification matrix does not include shipper notice terms.

**Partially ready (13):** CC1.3, CC3.2, CC3.4, CC4.1, CC5.3, CC6.3, CC7.4, CC9.2, A1.3, C1.1, C1.2, PI1.1, PI1.3. Most trace to the division's governance gaps (supplement drift and undocumented inheritance, scenario gaps 6 and 9) and to data handling outside the portal (emailed statements, no offboarding deletion).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC1.3, CC5.3, CC7.4 | Re-issued supplement with the group severity scale (POAM-020); inheritance matrix (POAM-019) |
| 2026 Q4 | CC3.4, PI1.3, C1.1 | Change checklist for vendor platform changes; independent review of allocation formula changes; portal-only statement delivery |
| 2027 Q1 | CC2.3, PI1.1, CC3.2, CC4.1, CC6.3, C1.2 | System description with security, availability, processing integrity, and confidentiality commitments; shipper notice terms in the P08 matrix; updated security plan risk assessment (POAM-018); platform-specific assessment; load visibility by region; offboarding procedure. **Type 1 as of 2027-03-31** |
| 2027 Q2 to Q3 | All in-scope criteria; A1.3; CC9.2 | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30); regional failover test; telematics contract terms and vendor review |

**Communication:** the Crude Logistics commercial director sends the three largest shippers a readiness letter with this timeline, and answers other shippers' questionnaires with the Type 1 report once issued.
