# SOC 2 Readiness Summary: Cris Santos Company | Health Care | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| Tier / Vertical | Micro / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Practice readiness self-assessment (`soc2-readiness.csv`), used to answer the referral network's questionnaire |
| Part B | EHR vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the independent consultant; approved by the owner physician 2026-08-31 |

## 1. Why SOC 2 for this organization
A two-physician office is **not** a SOC 2 service organization. It treats patients; it does not provide services to other businesses. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** In July 2026 a local hospital's referral network sent the practice a security questionnaire. The network shares patients and referral information with its member offices and asked about security and availability. Its questions follow the Trust Services Criteria. The practice will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30.

**The practice will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the practice's controls were defined in August 2026. An audit would also cost far more than the network asked for. The network accepted a self-assessment in its questionnaire instructions.

**B. Relying on the EHR vendor.** The EHR vendor carries most of the practice's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight under 45 CFR 164.308(b) and SA-9.

**Why Availability and not another category.** The referral network needs to know it can reach the practice and that referrals will not be lost. The practice cannot see patients without the EHR and the internet (P05). Confidentiality of patient information is covered under the Security criteria and the HIPAA Privacy Rule. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** primary care for about 3,500 patients, referrals to and from the network.
- **Infrastructure and software:** the Office Clinical Platform (SSP, P02): EHR/PM, productivity suite, cloud fax, file-sync backup, 12 devices, office network.
- **People:** 7 workforce members and the MSP.
- **Data:** ePHI, claims, workforce data.
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
- CC1.3: Security and Privacy Officer designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk analysis done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked suite; vendor data centers under SOC 2)
- CC6.6: firewall, separated guest Wi-Fi, MFA

**Not ready:**
- CC2.1: no inventory of devices or ePHI
- CC3.3: fraud risk not assessed
- CC6.2 and CC6.3: access granted and removed without a process (the former MA account)
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC7.5, A1.2, A1.3: recovery unproven (the same gap as risk R-005)
- CC8.1: the MSP changes devices without the practice's approval

## 4. Evidence inventory
The questionnaire asks for evidence. What the practice can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| EHR vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| BAA list | CC9.2 | Yes | AI scribe BAA; MSP subcontractor confirmation (2026-09 to 2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Restore test records | CC7.5, A1.3 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | New-hire only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the EHR vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (late removal of 2 of 25 departed vendor employees), remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 15 minutes **meet the practice's BIA** (RTO 4 h, RPO 1 h for BP-01 to BP-03).
- **Controls the practice must run.** The report lists complementary user entity controls: user provisioning and removal, role assignment, MFA enforcement, and review of user access and audit reports. Two are open gaps at the practice: removal (POAM-001, POAM-006) and review (POAM-008). **The vendor's controls protect the practice only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask how the vendor monitors the carved-out clearinghouse; ask for 24-hour incident notice at BAA renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC6.1, CC6.2 | Acknowledgments; questionnaire response; MFA on MSP-held logins (POAM-002); onboarding checklist (POAM-001) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.3, CC6.5, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, A1.1-A1.3 | Monthly oversight notes; annual training (POAM-007); inventory; remaining SSP controls; termination process (POAM-006); EDR (POAM-005); log review (POAM-008); restore tests and backup upgrade (POAM-003, POAM-004); contingency plan; failover router; MSP review (POAM-009) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk analysis |

**Response to the referral network:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.
