# SOC 2 Readiness Summary: Cris Santos Company | Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) |
| Tier / Vertical | Micro / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. The farm is not a service organization and will not seek a SOC 2 report |
| Part A | Farm readiness self-assessment (`soc2-readiness.csv`), used to answer the packer-shipper's grower security and continuity questionnaire |
| Part B | Review of the farm management software (FMIS, SYS-01) vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager (Security Coordinator) with the independent consultant; approved by the Owner and General Manager 2026-08-31 |

## 1. Why SOC 2 for this organization
A crop farm is **not** a SOC 2 service organization. It grows and sells watermelons, peanuts, and cotton; it does not run systems or process data for other businesses. The assurance its main buyer has always asked for is food safety: the packer-shipper requires an annual third-party food safety audit, which the farm passed in April 2026. That audit does not cover cybersecurity. The vertical overlay names no assurance alternative to SOC 2 for agriculture.

The Trust Services Criteria are used here for two practical reasons.

**A. Answering the grower questionnaire.** With its 2026 grower agreement renewal, the packer-shipper added a grower security and continuity questionnaire. It wants to know whether a grower can keep harvest records, lot traceability, and committed loads going through an outage or a cyber attack, and whether the grower will tell it quickly. Its questions follow the Security and Availability criteria. The farm will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due **2026-10-15**.

**The farm will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the farm's controls were defined in August 2026. An audit would cost more than a year of the farm's whole security budget (P01 section 4). The questionnaire accepts a self-assessment.

**B. Relying on the FMIS vendor.** SYS-01 is the farm's system of record and the path to the pivots. The vendor's SOC 2 Type 2 report is the main evidence for the controls the farm inherits (P02 section 10.2, P04). Until August 2026 the farm had never asked for it (P03 G-028).

**Why Availability and not another category.** The questionnaire is about continuity: loads, harvest records, and traceability. The farm's High processes are irrigation, harvest dispatch, and daily records (P05), and all three depend on SYS-01 and the pump station. Worker personal information is covered under the Security criteria and the Fla. Stat. 501.171 rows of P03, so Confidentiality was not added. Processing Integrity and Privacy do not apply, because the farm processes nothing for others and makes no privacy commitments to the packer-shipper.

## 2. System description (scope)
- **Services:** growing and harvesting watermelons, peanuts, and cotton; harvest and load records for the packer-shipper; the internal services that support them (irrigation, daily hours and Produce Safety records, payroll).
- **Infrastructure and software:** the Farm Management and Irrigation Control Platform (SSP, P02): SYS-01 with its irrigation module, the productivity suite, 8 devices, the shop network, the pump station and 5 pivots, and the MSP-run cloud backup. Interfaces to telematics, the drone, and the agronomy analytics pilot.
- **People:** 7 employees, the MSP, and the irrigation dealer.
- **Data:** Produce Safety records, H-2A earnings records, worker personal information, operator location history, harvest and load records, yields.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 17 | 10 | 0 |
| Availability (A1, 3) | 1 | 0 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready (7):**
- CC1.3: Security Coordinator designated in writing; roles defined
- CC3.1, CC3.2, CC3.3: risk tolerance set; 2026 risk assessment done, including payment diversion and records fraud
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked on the POA&M
- A1.1: SaaS capacity covered by the vendors; the single shop internet line accepted as a Low risk (R-012)

**Not ready (12):**
- CC2.1: no inventory of devices, OT, or data
- CC6.2, CC6.3: access granted and removed without a process (shared crew login, the former bookkeeper's mailbox)
- CC6.5: an old desktop given away without a recorded wipe
- CC6.6: the dealer gateway and the flat network reach the pump station
- CC7.1, CC7.2, CC7.3: no scanning, no monitoring of irrigation commands, no incident records
- CC7.5, A1.2, A1.3: recovery unproven (the same gap as P01 R-004)
- CC8.1: the dealer changes the pump station program without approval

The pattern matches P03 and P07: the farm now governs and assesses risk, but **controls over the dealer's access, over detection, and over recovery are not yet operating**. Those are exactly the areas the packer-shipper asks about.

## 4. Evidence inventory
What the farm can send with the questionnaire now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments in English and Spanish (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M meeting notes (2026-09) |
| BIA summary (P05) and P08 runbook contact chain | CC7.4, CC9.1 | Yes | Tabletop report (2026-11) |
| FMIS vendor SOC 2 review | CC9.2, A1.1, A1.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC5.2, CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account checklists and monthly reconciliation | CC6.2, CC6.3 | No | Monthly from 2026-10 |
| One-page inventory | CC2.1 | No | 2026-10 |
| Dealer session and change log | CC8.1, CC5.2 | No | Each session from 2026-10 |
| Restore test records and SYS-01 export log | CC7.5, A1.2, A1.3 | No | First test 2026-09; quarterly and monthly after |
| Training records | CC1.4 | Produce Safety only | Security training 2026-11 |
| Hand-operation drill record | CC9.1, A1.3 | No | 2027-02, before the season |

## 5. Findings from the FMIS vendor report (Part B)
- **Opinion:** Type 2, unmodified, for the 12 months ending 2026-03-31, covering Security and Availability. One exception (a skipped quarterly access review for vendor database administrators), performed late with no inappropriate access found.
- **Carve-out that matters:** the pivot manufacturer's connectivity service, which carries SYS-01 commands to the pivot panels, is a carved-out subservice organization. That is the path an attacker would use to start or stop pivots through SYS-01 (P04 finding 4). The farm will ask for the vendor's review of that provider.
- **Availability:** the stated RPO of 1 hour meets the BIA (the strictest RPO is 4 hours for BP-03). The stated RTO of 8 hours **equals** the 8-hour RTO for irrigation and harvest dispatch (BP-01, BP-02), with no margin. Hand operation and paper forms carry the first hours of any vendor outage. A stated recovery commitment goes into the contract at renewal (R-011).
- **Controls the farm must run (CUECs):** four were mapped. Two are open gaps at the farm: MFA for every user (POAM-008) and review of audit and irrigation change reports (R-003). Two are only partly in place: user provisioning and removal (shared crew login, POAM-001) and protection of the tablets and phones that run the app (R-015). **The vendor's controls protect the farm's records and pivots only once the farm closes these gaps.**
- **Incident notice:** "without undue delay," with no time frame. Seek a 72-hour term at renewal.
- **Follow-ups:** request a bridge letter to 2026-09-30 by 2026-10-31; request the connectivity provider review; confirm the access review fix in the next report.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC6.1 | Signed acknowledgments; MFA for every SYS-01 user, mailbox, and the backup console (POAM-008) |
| 2026 Q4 | CC1.2, CC1.4, CC2.1, CC2.2, CC2.3, CC3.4, CC5.2, CC6.2, CC6.3, CC6.4, CC6.5, CC6.6, CC6.7, CC6.8, CC7.2, CC7.3, CC7.4, CC7.5, CC8.1, CC9.2 | Questionnaire response and security contact (2026-10-15); inventory; account checklists and named crew accounts (POAM-001); on-request dealer access and session log (POAM-002, POAM-009); pump station segment (POAM-006); EDR (POAM-005); reporting cards (POAM-013); training (POAM-012); backup upgrade and restore tests (POAM-003); tabletop; supplier terms (POAM-010) |
| 2027 Q1 | CC5.1, CC5.3, CC7.1, CC9.1, A1.2, A1.3 | Firmware updates (POAM-011); surge protection; contingency plan with the hand-operation procedure; drill before the season (POAM-004) |
| 2027 Q3 | CC1.5 | Policies operated through one full season |

**Response to the packer-shipper:** send this summary, the readiness checklist, and the POA&M by 2026-10-15, name the Security Coordinator as security contact, confirm the 24-hour notice commitment in the grower agreement, and commit to an updated self-assessment before the 2027 harvest (May 2027).
