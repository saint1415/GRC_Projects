# SOC 2 Readiness Summary: Cris Santos Company | Commercial Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Micro / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Target report | None. Readiness self-assessment only; no Type 1 or Type 2 audit is planned (section 1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the largest tenant's security questionnaire |
| Part B | Access control and video platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Property Manager with the independent consultant; approved by the Managing Member 2026-08-31 |

## 1. Why SOC 2 for this organization
A landlord is **not** a SOC 2 service organization in the usual sense: it leases space, and the vertical overlay names no SOC 2 alternative for commercial facilities. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a tenant questionnaire.** In July 2026 the largest Property A tenant, an insurance company's regional claims office of about 9,000 sq ft, sent a vendor security questionnaire as part of its lease renewal (the renewal decision is due 2027-01-31). The tenant's own vendor risk program covers its landlord because the landlord holds its employees' names, badge photos, and door history, and records them on video. The questions follow the Trust Services Criteria for Security and Confidentiality. The company will answer with this self-assessment, the P07 POA&M, and a named security contact. The response is due 2026-09-30.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. An audit would also cost far more than the tenant asked for; its questionnaire instructions accept a self-assessment from a landlord.

**B. Relying on the platform vendor.** The access control and video platform vendor carries most of the company's inherited controls for doors and cameras (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight (SA-9; CPG 1.D).

**Why Confidentiality and not another category.** The tenant's concern is how its employees' credential data, door history, and video are protected, kept, and disposed of. Availability of doors and cooling is covered by lease service terms, not by the questionnaire. Processing Integrity does not fit a landlord, and the company makes no privacy notice commitments that the Privacy criteria would test.

## 2. System description (scope)
- **Services:** building access, building climate control, and video surveillance at two properties for 33 tenants; credential administration for about 300 holders.
- **Infrastructure and software:** the BAACS (SSP, P02): the BAS at Property A, the cloud access control and video platform with 9 door controllers and 28 cameras, and the property networks; supporting SaaS (productivity suite, property management system).
- **People:** 7 employees, the MSP, the controls contractor, and the security integrator.
- **Data:** credential holder data, door history, badge photos, video (Confidential); applicant and guarantor files (Restricted; not part of the tenant's question, but handled under the same C1 retention and disposal rules).
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 17 | 11 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security and privacy lead designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a first risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked monthly

**Not ready:**
- CC1.4: no training beyond a new-hire video
- CC2.1: no inventory of building devices or data locations
- CC3.4 and CC8.1: changes (including the face match feature) made without approval
- CC6.1 and CC6.2: single-factor administrator access, shared accounts, flat network
- CC6.5 and C1.2: no retention or disposal records
- CC7.1, CC7.2, CC7.3: no baselines, monitoring, or triage criteria
- CC7.5: recovery unproven (the same gap as risk R-002)

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Platform vendor SOC 2 review | CC9.2, CC6.4 | Yes | Bridge letter (2026-10) |
| MFA settings screenshots for platform administrators and backup console | CC6.1 | No | 2026-09 (POAM-002) |
| Quarterly credential confirmations from tenant contacts | CC6.2, CC6.4 | No | From 2026-10 |
| Monthly account and log review checklists | CC6.2, CC7.2 | No | Monthly from 2026-10 |
| Disposal records and retention schedule | CC6.5, C1.2 | Schedule yes (POL-04 4.8); records no | From 2026-10 |
| Video and door-history release log | C1.1 | No | From 2026-09 |
| Restore test records | CC7.5 | No | Quarterly from 2026-10 |
| Training and phishing simulation records | CC1.4, CC2.2 | New-hire only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-03-31. One exception (1 of 40 sampled production changes without documented approval), remediated.
- **Availability:** the 99.9% monthly target and 72 hours of offline credential caching **meet the BIA** for access control (BP-01 MTD 24 h).
- **Controls the company must run.** The report lists complementary user entity controls: administrator account management including MFA, timely credential removal, review of administrator activity, protection of the network the devices sit on, and approval of feature settings. **All five are open gaps at the company** (POAM-001, POAM-002, POAM-004, POAM-010, POAM-013). The vendor's controls protect the company only once those gaps are closed.
- **Analytics are outside the report.** The face match feature was released after the report period and is not in the system description, so there is no assurance over how face templates are stored or deleted (P10).
- **Follow-ups:** request a bridge letter to 2026-09-30; ask whether analytics features will be in the next report; ask for 24-hour incident notice at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC3.4 | Acknowledgments; questionnaire response; P10 decision on face match; MFA on administrators (POAM-002) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC5.1, CC5.2, CC5.3, CC6.1 to CC6.8, CC7.1 to CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; training (POAM-012); inventory (POAM-005); departure checklist and named accounts (POAM-001); credential review (POAM-010); disposal records; remote access service (POAM-003); segmentation (POAM-004); EDR; log review (POAM-013); restore tests and contingency plan (POAM-007, POAM-008); security addendum (POAM-009) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the tenant:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Property Manager as the tenant security contact, and commit to an updated self-assessment in January 2027, before the tenant's renewal decision is due.
