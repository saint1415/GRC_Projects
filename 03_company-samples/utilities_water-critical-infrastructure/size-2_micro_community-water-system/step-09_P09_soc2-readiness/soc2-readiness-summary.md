# SOC 2 Readiness Summary: Cris Santos Company | Water and Wastewater Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (privately held community water system, 2,850 population served) |
| Tier / Vertical | Micro / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. Readiness self-assessment only; no SOC 2 examination is planned |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the cyber insurer's renewal questionnaire |
| Part B | Remote monitoring vendor's SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the Chief Operator and the independent OT security consultant; statuses updated to the policy approval date and approved by the Owner and General Manager on 2026-08-31 |

## 1. Why SOC 2 for this organization
A community water system is **not** a SOC 2 service organization. It sells water to residents, not services that affect other businesses' controls. The Trust Services Criteria are used here for two practical reasons.

**A. Answering the cyber insurer.** The cyber policy renews on 2026-11-01, and the insurer's renewal questionnaire is due 2026-10-01. It asks about MFA on remote access, backups and restore tests, network separation of control systems, patching, training, vendor access, and an incident response plan. The Office Manager answers each question from this self-assessment and attaches the POA&M (P07), so the answers are consistent, honest, and backed by evidence. Using the TSC structure also means the same checklist can be updated each year and reused for any future questionnaire.

**The company will not get a SOC 2 audit.** No customer, regulator, or partner has asked for one; a Type 2 report needs controls that have operated for months, and most of the company's controls were defined in August 2026; and the cost would be out of proportion for a $1.1 million utility. The insurer accepts a self-assessment with its questionnaire.

**B. Relying on the remote monitoring vendor.** The vendor's cloud service carries the remote alarms and the 2-year trend history that the company relies on (P05 BP-03, BP-04), and it is the only cloud workload that touches the plant (P04). Its SOC 2 Type 2 report is the evidence for the controls the company inherits from it (P02 section 10.2). Reviewing it each year is part of vendor oversight under SA-9 and POL-02 A.5.

**Why Availability and not another category.** The company's mission is continuous safe water, and its BIA is built around how long each function can be down (P05). The insurer's questions about backups and recovery map to Availability. Customer personal information is protected under the Security criteria and Fla. Stat. 501.171. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** drinking water supply, treatment, storage, and distribution for 2,850 people (1,190 connections); billing and customer service.
- **Infrastructure:** the Water Treatment SCADA System (SSP, P02): HMI computer, plant PLC and 2 RTUs, cellular modems, remote desktop tool, alarm dialer, remote monitoring gateway; the office network and 6 computers; standby generators and the emergency interconnect.
- **Software and cloud services:** remote monitoring service, productivity suite, billing system with customer portal, accounting and payroll, office backup.
- **People:** 7 employees, the SCADA integrator, the MSP, and the remote monitoring vendor.
- **Data:** process and compliance data (chlorine residual record), OT configuration, customer personal information, payroll.
- **Procedures:** POL-02, POL-03, POL-04, the P08 runbook, the 2023 emergency plan.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 16 | 9 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: coordinator and OT security decision owner designated in writing
- CC3.1 and CC3.2: recovery objectives and risk tolerance set; first risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked monthly
- CC5.1: 38 controls selected in the SSP
- CC6.4: fenced, locked, and alarmed plant
- CC9.1 and A1.1: generators, interconnect, insurance, and spare treatment capacity

**Not ready:**
- CC2.1: no OT inventory
- CC6.1, CC6.2, CC6.3: shared credentials and no MFA on the paths that reach the plant; a former operator kept the remote password for 4 months
- CC6.6: flat network and exposed modems
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, no access monitoring, no incident records
- CC8.1: PLC and HMI changes and the AI feature made without approval
- A1.3: no recovery or restore testing

These are the same weaknesses as the 4 High risks in P01 and the 8 High POA&M items in P07.

## 4. Evidence inventory
The insurer asks for evidence of key controls. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| P08 runbook and notification matrix | CC7.4 | Yes | Tabletop and drill report (2026-11) |
| MFA settings for the remote desktop tool, remote monitoring service, and firewall login | CC6.1 | No (email, billing, accounting only) | Screenshots when POAM-002 and POAM-004 close (2026-09-30) |
| Offline PLC and HMI backup log | CC7.5, A1.2 | No | Monthly from 2026-09-15 |
| Office backup restore test record | A1.3 | No | Quarterly from 2026-09-30 |
| Remote access connection review checklist | CC7.2 | No | Weekly from 2026-10 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |
| Remote monitoring vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| Generator test log; interconnect agreement | CC9.1, A1.2 | Yes | Monthly (existing) |

## 5. Findings from the remote monitoring vendor's report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, Security and Availability. One exception (2 of 40 sampled production changes without documented approval), remediated by the vendor.
- **Availability:** the stated recovery time of 8 hours and recovery point of 1 hour **meet the company's BIA** for remote monitoring (RTO 24 h, RPO 24 h). The alarm dialer, which does not depend on the vendor, stays the alarm of record.
- **Controls the company must run.** The report's complementary user entity controls include managing users, enabling MFA, protecting gateway credentials, controlling the write-back setting, and reviewing user access and sign-in reports. Two are open gaps at the company: MFA (POAM-004) and user and sign-in review (POAM-001; POL-02 B.8). **The vendor's controls protect the company only once those gaps are closed.**
- **Not covered:** the anomaly detection feature launched after the report period, so no independent assurance exists for it yet. The vendor's terms also allow use of de-identified customer data to improve its analytics. Both feed the P10 conditions.
- **Follow-ups:** bridge letter to 2026-09-30; 24-hour incident notice in the contract addendum; opt-out from data use for model improvement.

## 6. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC6.3, A1.2, and the MFA part of CC6.1 | Acknowledgments; MFA and named remote accounts (POAM-002, POAM-004); termination checklist; offline PLC copies and first restore test (POAM-005); questionnaire answered 2026-10-01 with the status at that date |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC3.4, CC5.2, CC5.3, CC6.1, CC6.2, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.2, A1.3 | OT inventory (POAM-008); OT network and private carrier plan (POAM-006); CISA scanning (POAM-009); patch plan and HMI malware protection (POAM-010); contract addenda (POAM-011); training (POAM-013); log reviews; tabletop and drill; P10 conditions |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk review |

**Response to the insurer:** answer the questionnaire by 2026-10-01 from this checklist, attach the POA&M, name the Office Manager as security contact, and send an update before the 2026-11-01 renewal if POAM-002 and POAM-004 have closed. The self-assessment is repeated each August with the policy review.
