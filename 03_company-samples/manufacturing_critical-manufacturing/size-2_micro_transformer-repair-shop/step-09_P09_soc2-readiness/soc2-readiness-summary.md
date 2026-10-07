# SOC 2 Readiness Summary: Cris Santos Company | Critical Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) |
| Tier / Vertical | Micro / Critical Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Shop readiness self-assessment (`soc2-readiness.csv`), used to answer the G&T cooperative's vendor security questionnaire |
| Part B | ERP vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the independent consultant; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A transformer repair shop is **not** a SOC 2 service organization. It rebuilds and sells transformers and does repair work; it does not host systems or process data for customers. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** In July 2026 the G&T cooperative sent the shop a vendor security questionnaire as part of its supply chain program. It asks for a SOC 2 report or an equivalent self-assessment, and its questions follow the Trust Services Criteria. The shop will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30.

**The shop will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the shop's controls were defined in August 2026. The cost would also be out of proportion for a 7-person shop. The cooperative's questionnaire instructions accept a self-assessment from small vendors.

**B. Relying on the ERP vendor.** The ERP vendor carries most of the shop's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight (SA-9; CSF GV.SC-07).

**Why Availability and not another category.** The cooperative relies on the shop for repairs at its substations and, after storms, for rebuilt units. Its questionnaire asks whether the shop can keep working and recover after an incident. The BIA (P05) shows the shop stops shipping without the test PC and the ERP. Confidentiality of customer data is covered under the Security criteria and POL-04. Processing Integrity and Privacy were not asked for.

## 2. System description (scope)
- **Services:** repair, rewinding, and remanufacturing of distribution transformers; field service at customer sites, including the cooperative's substations.
- **Infrastructure and software:** the ERP and Job Scheduling Platform (SSP, P02): the ERP, productivity suite, suite backup, 8 devices, the test PC, and the network.
- **People:** 7 employees and the MSP.
- **Data:** customer test reports and site data, the rewind data sheet library, FCI, employee personal information.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 17 | 11 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security Coordinator designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked

**Not ready:**
- CC1.4: no security training
- CC2.1: no inventory of devices, vendors, or data
- CC3.4: changes (AI-001, the port-forwarding rule) went in without review
- CC6.2, CC6.3, CC6.5: access granted and removed without a process; no disposal records
- CC7.1, CC7.2, CC7.3: no scanning, monitoring, or incident records
- CC7.5, A1.2, A1.3: recovery unproven (the same gap as risks R-002 and R-011)
- CC8.1: the MSP and vendors change systems without the shop's approval

## 4. Evidence inventory
The questionnaire asks for evidence. What the shop can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| ERP vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| Leaver checklist and cooperative access notices | CC6.3, CC2.3 | Corrective plan sent 2026-07-20 | Each departure from 2026-09 |
| MSP monthly report (patching, antivirus, encryption, backup) | CC6.8, CC7.1, A1.2 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Restore test records | CC7.5, A1.3 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the ERP vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, no exceptions. The cloud hosting provider and the payment processor are carved out.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the shop's BIA** (RTO 8 h, RPO 4 h for BP-01 and BP-05).
- **Controls the shop must run.** The report lists complementary user entity controls: user provisioning and removal, role assignment, enabling MFA, review of user access and audit reports, and protecting data the customer exports. Four are open gaps at the shop: MFA (POAM-002), removal (POAM-001, POAM-013), review (POAM-001), and the export it has not yet set up (POAM-007). **The vendor's controls protect the shop only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; enable the weekly export; ask for 24-hour incident notice at renewal so the shop can meet the cooperative's 72-hour clock.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC5.3, CC6.2, CC6.7, CC7.3 | Acknowledgments; staff briefing; obligations list and templates (POAM-011); onboarding checklist (POAM-001); public links off; incident log; questionnaire response |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC6.1, CC6.3, CC6.4, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.1, A1.2, A1.3 | Monthly oversight notes; training (POAM-010); inventory (POAM-004); change review step; ERP MFA (POAM-002); leaver process (POAM-013); visitor sign-in; disposal records; remote access and modem (POAM-005, POAM-006); EDR (POAM-009); test PC replacement (POAM-008); networks and log forwarding (POAM-003); tabletop; backups and restore tests (POAM-007); contingency plan; failover router; vendor terms (POAM-012) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the cooperative:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, confirm the corrective plan for the missed access notice, and commit to an updated self-assessment in April 2027.
