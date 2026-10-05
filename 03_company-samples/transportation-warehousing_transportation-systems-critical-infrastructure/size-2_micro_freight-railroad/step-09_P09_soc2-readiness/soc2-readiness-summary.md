# SOC 2 Readiness Summary: Cris Santos Company | Transportation Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (short line freight railroad, 16 route miles, north Florida) |
| Tier / Vertical | Micro / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. No SOC 2 examination is planned (see section 1) |
| Part A | Railroad readiness self-assessment (`soc2-readiness.csv`), used to answer the connecting Class I's cybersecurity questionnaire |
| Part B | Review of the operations SaaS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-19 to 2026-08-21 by the Office Manager (Security Lead) with the Owner and General Manager; approved by the Owner and General Manager 2026-08-31 |

## 1. Why SOC 2 for this organization
**The railroad is not a SOC 2 service organization.** It moves freight for 6 customers under rates and contracts. No customer relies on the railroad's IT controls for its own financial reporting or system security. The vertical overlay names no SOC 2 alternative for rail; assurance in this sector comes from regulators instead (TSA for the Security Coordinator and reporting rules, FRA for safety, PHMSA rules for hazmat security plans).

The Trust Services Criteria are used here for two practical reasons.

**A. Answering the Class I's questionnaire.** On 2026-07-20 the connecting Class I sent its connected short lines a cybersecurity questionnaire about the security and availability of interchange data. The railroad exchanges waybills and interchange reports with the Class I by EDI from the operations system (SYS-01), and runs one turn a day onto the Class I's main line. The questions follow the Trust Services Criteria. The railroad will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-30.

**The railroad will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the railroad's controls were defined in August 2026. An audit would cost a large share of the railroad's yearly security budget (about $4,040 a year, P01) and the Class I did not ask for one.

**B. Relying on the operations SaaS vendor.** SYS-01 carries movement authority, car management, and interchange EDI (P05 BP-01 to BP-03), and the vendor provides several inherited controls in the SSP (P02 section on inherited controls: CP-9, AC-7, AU-11, AC-3). The vendor **is** a service organization for the railroad, so its SOC 2 Type 2 report is the right evidence. Reviewing it every year is part of POL-02 A.5 and CC9.2.

**Why Availability and not another category.** The Class I needs to know that interchange data and the daily turn will keep flowing, and the railroad cannot issue movement authority from the operations system without the vendor and the internet line (P05). Confidentiality of employee information and SSI is covered under the Security criteria. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** freight rail service on 16 route miles for 6 customers, and the daily interchange turn to the Class I's yard.
- **Infrastructure and software:** the Train Dispatch and Operations Back Office (TDOB, the SSP system in P02): the operations system, productivity suite, endpoints and crew tablets, office network, suite backup, radio dispatch system, and locomotive telematics.
- **People:** 7 employees, the MSP, and the operations SaaS vendor.
- **Data:** movement authority records, car and waybill data, interchange EDI, the hazmat car list, SSI, and employee personal information.
- **Procedures:** POL-02, POL-03, POL-04, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 19 | 8 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security Lead designated in writing; primary and alternate TSA Security Coordinators reported to TSA
- CC3.1 and CC3.2: risk tolerance set; 2026 risk assessment (22 risks) and BIA done
- CC4.1 and CC4.2: independent assessment done (84 determination statements); 12 POA&M items tracked
- CC6.4: office and enginehouse locked with an alarm; vendor data centers covered by SOC 2 reports

**Not ready:**
- CC2.1: no inventory of devices, radio and telematics components, SaaS accounts, or Restricted information
- CC6.2 and CC6.3: shared crew login; access granted and removed without a process; SSI open to every account
- CC7.1 and CC7.2: no vulnerability scanning or monitoring; unsupported operating system on the dispatch desktop
- CC7.3: the 2025 mailbox compromise was never evaluated as a TSA-reportable cyber attack
- CC7.5 and A1.3: recovery unproven (the same gap as risks R-002 and R-005)
- CC8.1: the MSP changes devices, including the dispatch desktop, without the railroad's approval

The Not ready criteria line up with the High POA&M items in P07 (POAM-003 to POAM-006). Closing them and POAM-001, POAM-008, and POAM-011 would move all of them to Partially ready or Ready.

## 4. Evidence inventory
The questionnaire asks for evidence. What the railroad can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| POL-02, POL-03, POL-04; Security Lead designation; Security Coordinator letter to TSA | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M review notes (2026-09) |
| Operations SaaS vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| MSP monthly patch report and antivirus export | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Hazmat security training records | CC1.4 | Yes | Cyber training and phishing simulation records (from 2026-10) |
| Account reconciliation and sign-in review records | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Restore test records and weekly operations data exports | CC7.5, A1.2, A1.3 | No | From 2026-09-30 |
| Paper dispatch drill and tabletop report | CC7.4, A1.3 | No | 2026-11 |
| MSP contract amendment and technician list | CC5.2, CC6.6, CC8.1, CC9.2 | No | 2026-12 |

## 5. Findings from the operations SaaS vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-03-31. One exception (late removal of 2 of 20 sampled departed vendor staff), remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the railroad's BIA** for dispatching (BP-01: RTO 4 h, RPO 1 h). That is why P01 R-011 was accepted at Low.
- **Controls the railroad must run.** The report lists complementary user entity controls: named user accounts, timely removal, MFA enforcement, role assignment, and review of user and audit reports. Three are open gaps at the railroad: the shared crew login and late removal (POAM-001) and no review of reports (POAM-008). **The vendor's controls protect the railroad only once those gaps close.**
- **Follow-ups:**
  - Request a bridge letter covering 2026-04-01 to 2026-09-30 by 2026-10-31.
  - Start the weekly export of car inventory and authority history so the railroad holds its own copy (POAM-003).
  - Ask for security incident notice within 24 hours at renewal, so the railroad can meet its own 24-hour TSA report (1570.203).
  - Ask how the vendor oversees its carved-out hosting and EDI network providers.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2 | Acknowledgments; staff briefing and reporting cards (POAM-006); MFA on MSP-held and telematics logins (POAM-002) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1 to CC7.5, CC8.1, CC9.1, CC9.2, A1.1 to A1.3 | Questionnaire response (2026-10-30); inventory; TSA report form (POAM-006); training (POAM-007); named crew accounts and termination checklist (POAM-001); restricted SSI folder (POAM-012); sign-in review (POAM-008); backup upgrade, restore tests, contingency plan, paper dispatch drill, and tabletop (POAM-003, POAM-004); EDR (POAM-005); dispatch segment and desktop replacement (POAM-010, POAM-011); MSP amendment and AI pilot terms (POAM-009); cellular failover router |
| 2027 Q3 | CC3.3 | Billing and waybill fraud scenarios in the July 2027 risk assessment |

**Response to the Class I:** send this summary, the readiness checklist, and the POA&M by 2026-10-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027.
