# SOC 2 Readiness Summary: Cris Santos Company | Government Services and Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Tier / Vertical | Micro / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the county's annual vendor security questionnaire |
| Part B | Access control vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office and Compliance Manager with the independent consultant; approved by the owner 2026-08-31 |

## 1. Why SOC 2 for this organization
**The company is a service organization to the county.** It runs the county's access control and video service on its own tenant (SYS-01), holds about 1,050 county cardholder records and 52 face templates, and can change schedules and setpoints in 4 county buildings (SYS-02, SYS-03). That is exactly the kind of outsourced service a SOC 2 report is meant to describe.

**A. Answering the county questionnaire.** The county security exhibit requires an annual vendor security questionnaire answered with a SOC 2 report **or an equivalent readiness self-assessment**. The county sent the 2026 questionnaire on 2026-07-01; the answer is due 2026-09-30. The company will answer with this summary, the readiness checklist, the POA&M (P07), and a named security contact.

**The company will not get a SOC 2 audit this year.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. A Type 1 report could follow once the High POA&M items close; the owner will decide in 2027 Q2 whether the county relationship justifies the cost.

**B. Relying on the access control vendor.** The SYS-01 vendor carries most of the platform controls behind the county's cardholder data (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of provider oversight under SA-9 and POL-02 A.5.

**Why Confidentiality and not another category.** The county's questions focus on who can see its cardholder data, face templates, door schedules, and security layouts, all of which are Restricted under POL-04 and largely exempt from public disclosure (Fla. Stat. 119.071(3)). Availability was not selected: door controllers and BAS controllers keep running on their own if the company's services fail (P05), and recovery is covered under CC7.5 and CC9.1. Processing Integrity and Privacy were not requested; the county, not the company, deals with its employees as data subjects.

## 2. System description (scope)
- **Services:** managed access control and video for 4 county buildings; 24x7 BAS alarm monitoring and remote BAS operation for 4 county and 3 city buildings; facilities support.
- **Infrastructure and software:** the Building Systems Operations Platform (SSP, P02): SYS-01, SYS-02, 7 gateways, the productivity suite, the CMMS, the suite backup, 16 company devices, the office network.
- **People:** 7 employees and the MSP.
- **Data:** cardholder records, access history, video, face templates, BAS data, drawings (including CUI from the federal subcontract), work orders.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 19 | 8 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Information Security Officer designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked office; gateways in locked customer rooms; vendor data centers under SOC 2)

**Not ready:**
- CC2.1: no inventory of components or data locations
- CC6.2 and CC6.3: accounts created without approval; all technicians are administrators; late removal
- CC7.1, CC7.2, CC7.3: no scanning, no log review or alerts, no incident log
- CC7.5: engineering records not backed up and never restored (the same gap as risk R-006)
- CC8.1: gateway and platform setting changes need no approval
- C1.2: no disposal log and no contract-end return procedure

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| SSP summary (P02) | CC5.1, CC6.1 | Yes | Annual update |
| SYS-01 vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10); face module letter (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC5.2, CC6.8 | Yes (July 2026) | Monthly |
| Account reconciliation and weekly log review checklists | CC6.2, CC6.3, CC7.2 | No | From 2026-10 |
| Restore test records (suite and controller programs) | CC7.5 | No | Quarterly from 2026-10 |
| Gateway firmware and change records | CC7.1, CC8.1 | No | Quarterly from 2026-11 |
| Training and phishing simulation records | CC1.4, CC2.2 | Customer courses only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |
| Disposal log; restricted folder permission report | C1.1, C1.2 | No | From 2026-10 |

## 5. Findings from the access control vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (3 of 40 sampled production changes lacked documented approval), remediated.
- **Recovery:** recovery point of 1 hour meets the BIA; recovery time of 4 hours **misses the 2-hour RTO for lockdown and badge administration** (BP-02). Compensated by door controllers that work offline and by manual lockdown steps (P01 R-011).
- **The face verification module is not covered.** It was released after the report period. Until the vendor's next report or a vendor letter, the controls over face templates are unevidenced (P10 condition).
- **Controls the company must run.** The report lists complementary user entity controls: administrator provisioning and removal, MFA enforcement, review of administrator activity, and prompt notice of suspected compromise. Two are open gaps at the company: removal (POAM-001, POAM-006) and review (POAM-008). **The vendor's controls protect the county's data only once those gaps close.**
- **Follow-ups:** bridge letter to 2026-09-30; face module letter; ask for 24-hour incident notice at renewal (the vendor commits to 72 hours today, and the county clock is 24 hours).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC6.2 (start) | Acknowledgments; reporting card (POAM-011); termination checklist (POAM-006); questionnaire answer |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.1-CC5.3, CC6.1-CC6.3, CC6.5-CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Named accounts and MFA (POAM-001, POAM-002); VPN limits (POAM-003); backups and restore tests (POAM-004); provider terms (POAM-005); log review (POAM-008); inventory (POAM-009); firmware (POAM-010); CUI folder (POAM-012); contingency plan; disposal log; training |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk update |

**Response to the county:** send this summary, the readiness checklist, the SSP summary, and the POA&M by 2026-09-30; name the Office and Compliance Manager as security contact; commit to an updated self-assessment in April 2027 and to a decision on a SOC 2 Type 1 report in 2027 Q2.
