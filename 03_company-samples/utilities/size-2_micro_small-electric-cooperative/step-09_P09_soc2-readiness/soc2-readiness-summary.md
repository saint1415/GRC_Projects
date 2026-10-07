# SOC 2 Readiness Summary: Cris Santos Company | Utilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative) |
| Tier / Vertical | Micro / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Part A | Cooperative readiness self-assessment (`soc2-readiness.csv`), used to answer the G&T's member cybersecurity questionnaire |
| Part B | Hosted SCADA vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office and Finance Manager (Security Coordinator) and the Line Superintendent with the independent consultant; approved by the General Manager 2026-08-31 |

## 1. Why SOC 2 for this organization
An electric cooperative is **not** a SOC 2 service organization. It delivers electricity to its members; it does not provide services that affect other companies' financial reporting or systems. The Trust Services Criteria are used here for two practical reasons.

**A. Answering the G&T's questionnaire.** On 2026-06-15 the G&T sent its member cooperatives their first cybersecurity questionnaire, due 2026-10-30. The G&T's control center depends on accurate status from its members during emergencies, and a compromised member system could be used to disturb load at a delivery point. Its questions follow the Trust Services Criteria for security and availability. The cooperative will answer with this self-assessment, the P07 POA&M, and a named security contact.

**The cooperative will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the cooperative's controls were defined in August and September 2026. An audit would also cost several times the cooperative's yearly security budget. The G&T's instructions accept a self-assessment.

**B. Relying on the hosted SCADA vendor.** The SCADA vendor runs the master station the cooperative uses to operate its grid. Its SOC 2 Type 2 report is the evidence for the controls the cooperative inherits (P02 section 10.2). Reviewing it each year is part of the operator oversight that RUS expects for portions of the system the borrower does not operate (7 CFR 1730.20 and 1730.22(a)).

**Why Availability and not another category.** The G&T needs to know that the cooperative can see and control its feeders and report outages, and the cooperative cannot run remote switching without SCADA (P05 BP-02). Confidentiality of member data is covered under the Security criteria and Fla. Stat. 501.171. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** electric distribution to about 820 meters on 3 feeders; outage response; load control in coordination with the G&T.
- **Infrastructure and software:** the DSOMS (SSP, P02): hosted SCADA, substation and field devices, AMI head-end, the outage module, operations endpoints, and the settings backups. Office systems and the business suite support it.
- **People:** 7 employees, the MSP, and vendor support staff.
- **Data:** SCADA commands, alarms, and settings; outage records; member contact data and the medical-needs list.
- **Procedures:** POL-02, POL-03, POL-04, the ERP, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 18 | 10 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security Coordinator and OT lead designated in writing; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked and reported to the Board

**Not ready:**
- CC1.4: no security training for anyone
- CC2.1: no inventory of OT devices or operations endpoints
- CC6.1, CC6.2, CC6.3: shared SCADA login, no MFA on SCADA or AMI, no account process or reviews
- CC6.6: line recloser modems on public-IP plans and standing vendor access (the LR-4 finding)
- CC7.1, CC7.2: no vulnerability scanning, firmware tracking, or security monitoring
- CC7.5, A1.3: no tested way to rebuild a device or SCADA after a compromise (risk R-007)
- CC8.1: setting changes are not recorded or approved

**What the G&T will see.** The cooperative's governance is now in place, but the controls that would stop someone from operating its reclosers remotely are not yet. The answer will say so plainly, with dates, rather than claim readiness the cooperative does not have.

## 4. Evidence inventory
The questionnaire asks for evidence. What the cooperative can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04; Board minutes 2026-09-17 | CC1.2, CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| SCADA vendor SOC 2 review | CC9.2, A1.2 | Yes | Bridge letter (2027-01); AMI vendor report review when received |
| P08 runbook and the DOE-417 filing arrangement | CC7.3, CC7.4, CC2.3 | Runbook yes; arrangement no | Arrangement by 2026-10-31 |
| MSP monthly report (patching, antivirus) | CC6.8, CC7.1 | Yes (July 2026) | Monthly, including operations endpoints from 2026-11 |
| SCADA and AMI account reviews; SCADA sign-in alert log | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-11 |
| Settings restore test records | CC7.5, A1.3 | No | Quarterly from 2026-11 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |
| OT inventory with firmware versions | CC2.1, CC7.1 | No | 2026-10-31 |
| Tabletop exercise report | CC7.4 | No | 2026-11-18 |

## 5. Findings from the SCADA vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception: vendor support access to one customer's VPN endpoint was removed late after a staff transfer (1 of 20 tested); remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour, with a second hosting site tested twice a year, **meet the cooperative's BIA** (BP-02 RTO 8 h, RPO 24 h).
- **Controls the cooperative must run.** The report lists complementary user entity controls: named accounts, MFA, prompt removal of users, limits on who and which devices may sign in, review of the customer event log and vendor support sessions, and protection of field devices and their communications. **Every one is an open gap at the cooperative** (POAM-001 to POAM-004). The vendor's controls protect the master station; they do not stop someone with the cooperative's shared password from using it.
- **Field devices are out of scope.** The report covers nothing at Substation 1 or the line recloser sites. Those are the cooperative's alone (P04).
- **Follow-ups:** request a bridge letter to 2026-12-31; ask for the list of vendor staff with access to the cooperative gateway; ask for 24-hour incident notice and an account lock on request at contract renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-10-30, questionnaire due) | CC1.1, CC2.2, CC2.3, CC5.3, CC6.2, CC6.7, CC7.3 | Acknowledgments; reporting cards and DOE-417 arrangement (POAM-011); onboarding and termination checklists (POAM-001); questionnaire response |
| 2026 Q4 (by 2026-12-31) | CC1.4, CC1.5, CC2.1, CC3.4, CC5.2, CC6.1, CC6.3, CC6.5, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.2, A1.2 | Named SCADA accounts and MFA (POAM-001, POAM-002); private network for modems (POAM-003); vendor access on request (POAM-004); inventory (POAM-005); endpoint management (POAM-008); AMI two-person rule (POAM-009); settings backups and restore tests (POAM-007); training (POAM-012); tabletop; vendor contract terms |
| 2027 Q1 | CC1.2, CC5.1, CC6.4, CC9.1, A1.1 | First yearly Board report; ERP update (POAM-010); restricted keys (POAM-013); second carrier |
| 2027 Q2-Q3 | CC3.3, A1.3 | ERP exercise with a cyber scenario (May 2027); fraud scenarios in the July 2027 risk update |

**Response to the G&T:** send this summary, the readiness checklist, and the POA&M by 2026-10-30; name the Security Coordinator as security contact and the Line Superintendent as OT contact; commit to an updated self-assessment in April 2027.
