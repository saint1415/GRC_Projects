# SOC 2 Readiness Summary: Cris Santos Company | Food and Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Tier / Vertical | Micro / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the regional grocery chain's supplier security questionnaire |
| Part B | Cold-chain monitoring vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the independent consultant; approved by the owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person meat plant is **not** a SOC 2 service organization. It sells food, not services to other businesses' systems. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a customer questionnaire.** The 12-store regional grocery chain that became a customer in May 2026 sent a supplier security questionnaire in July. It asks how the supplier protects its systems and whether it can keep supplying during an outage. Its questions follow the Trust Services Criteria. The company will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. An audit would also cost more than the company's entire 2026 security budget. The grocery chain's questionnaire instructions accept a self-assessment from small suppliers.

**B. Relying on the cold-chain vendor.** The cold-chain monitoring service watches every cooler, the freezer, the blast chill cooler, and the truck, and it records the chilling CCP. Its SOC 2 Type 2 report is the evidence for the controls the company inherits from it (P02 section 10.2). Reviewing it each year is part of vendor oversight (SA-9).

**Why Availability and not another category.** The grocery chain cares most about continuity of supply, and the plant's most time-critical process is cold storage monitoring (P05 MTD 2 hours). Formulation confidentiality is covered under the Security criteria. Processing Integrity was considered because labels and lot codes must be accurate, but the company processes no data for others, and label accuracy is governed by the FSIS rules analyzed in P03. Privacy does not fit: the company holds no consumer personal information.

## 2. System description (scope)
- **Services:** sausage, smoked meats, and jerky for about 40 wholesale accounts, including the grocery chain, and a retail counter.
- **Infrastructure and software:** the Plant Production and Cold-Chain Monitoring System (SSP, P02): smokehouse controller, line controls and label printer, labeling PC, cold-chain service, records app, productivity suite, accounting service, office network, and cloud backup.
- **People:** 7 employees, the MSP, and the equipment vendors.
- **Data:** food safety settings and records, orders and lot data, employee data.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 17 | 9 | 0 |
| Availability (A1, 3) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security and compliance lead designated in writing; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (keyed doors, alarm, visitor sign-in; vendor data centers under SOC 2)
- CC6.7: encrypted connections to every SaaS service

**Not ready:**
- CC2.1: no inventory of plant equipment (3 of 17 devices listed)
- CC3.4 and CC8.1: changes to machines, settings, and the AI camera are not assessed or approved
- CC6.2 and CC6.3: access granted and removed without a process; shared logins
- CC7.1, CC7.2, CC7.3: no scanning, monitoring, setting comparison, or incident records
- CC7.5, A1.2, A1.3: recovery unproven, machine settings not backed up, no standby power (the same gaps as risks R-006 and R-014)

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Cold-chain vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| BIA summary (P05) | CC9.1, A1.1 | Yes | Contingency plan and downtime binder (2026-11) |
| MSP monthly report (patching, antivirus, backup) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Change log for cycles, formulations, labels, and IT | CC3.4, CC8.1 | No | From 2026-10 |
| Restore test records and manual monitoring drill | CC7.5, A1.3 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the cold-chain vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (1 of 25 production changes lacked documented approval), remediated.
- **Availability:** the vendor's 99.9% monthly availability target and 5-minute alert delivery **meet the BIA** for the vendor's side (MTD 2 h, RTO 1 h for BP-02). The weak links are on the plant's side: one gateway on the office network, one internet line, and one alert recipient.
- **Controls the company must run.** The report lists complementary user entity controls: user accounts and MFA, alert recipients and escalation, keeping gateways powered and connected, reviewing gateway offline notifications, and reporting sensor faults. Three are open gaps at the plant: the shared dashboard login (POAM-001), single-recipient alerts, and unanswered gateway offline events (P01 R-004). **The vendor's controls protect the plant only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask how the vendor monitors the carved-out text message provider; ask for 24-hour incident notice at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC7.3 | Acknowledgments; questionnaire response with a named security contact; reporting cards; incident log; MFA on firewall and backup console (POAM-004) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.1-A1.3 | Monthly oversight notes; training (POAM-005); inventory (POAM-007); named accounts and checklists (POAM-001, POAM-003); change log; plant network (POAM-012); vendor MFA (POAM-002); EDR (POAM-013); restore tests, immutable backups, and offline machine settings (POAM-009, POAM-010); contingency plan (POAM-008); MSP amendment (POAM-011); gateway cellular backup |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk review |

**Response to the grocery chain:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.
