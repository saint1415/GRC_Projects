# SOC 2 Readiness Summary: Cris Santos Company | Administrative and Support Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Micro / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Firm readiness self-assessment (`soc2-readiness.csv`), used to answer the largest client's security questionnaire |
| Part B | Payroll vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Operations Manager with the independent consultant; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A temporary staffing firm is **not** a SOC 2 service organization. It supplies people to work under clients' supervision; it does not run a system that stores or processes client data on the clients' behalf. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a client questionnaire.** In June 2026 the firm's largest client, a regional distributor (about 22% of receipts), sent a vendor security questionnaire. It asks whether the firm has a SOC 2 report and, if not, how it protects confidential information, including the client's contacts and rates and the personal information of the associates the firm places at its warehouses. The response is due 2026-09-30. The firm will answer with this self-assessment, the POA&M (P07), and a named security contact.

**The firm will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the firm's controls were defined in August 2026. An audit would also cost a large share of a year's profit for a $1.1 million firm. The questionnaire allows a self-assessment with supporting documents.

**B. Relying on the payroll vendor.** The payroll service holds every worker's SSN and bank account and moves the firm's payroll money (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for the controls the firm inherits, and reviewing it each year is part of vendor oversight (POL-02 A.5; SA-9).

**Why Confidentiality and not another category.** The client asked how the firm protects confidential information, and the firm's largest gaps are about confidential records it keeps: Form I-9 copies, consumer reports, and SSN exports (P03). Availability matters to associates (weekly pay) but the client did not ask about it, and payroll availability rests mostly on the payroll vendor, whose Availability criteria are covered in Part B. Processing Integrity was not asked about. **Privacy** was considered: it would test the firm's notice, consent, and disclosure practices toward candidates and associates. It was not selected for this questionnaire, but the privacy points the firm must meet by law (FCRA notices, Florida breach notice, Form I-9 use limits) are assessed in P03.

## 2. System description (scope)
- **Services:** temporary staffing and direct-hire placement for about 30 clients in one Central Florida metro area.
- **Infrastructure and software:** the Payroll and Applicant Tracking System (SSP, P02): staffing ATS, payroll and timekeeping service, productivity suite, suite backup, 8 laptops, applicant tablet, scanner, office network.
- **People:** 7 staff and the MSP.
- **Data:** associate and staff payroll and identity data, Form I-9 records, consumer reports, applicant records, client contacts and rates.
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
- CC1.3: Security and Privacy Lead designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked suite and records room; vendor data centers under their SOC 2 reports)

**Not ready:**
- CC2.1: no inventory of where confidential records are kept
- CC6.2 and CC6.3: access granted and removed without a process (two departed users kept access)
- CC6.5 and C1.2: no disposal records for devices, and nothing purged since 2017
- CC7.2 and CC7.3: no monitoring of payroll or suite activity and no incident records
- CC7.5: recovery unproven (backup never restored; manual payroll never tried)
- CC8.1: the AI feature and payroll settings were changed without review

## 4. Evidence inventory
The questionnaire asks for evidence. What the firm can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Payroll vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| MFA settings screenshots | CC6.1, CC6.6 | Yes (suite, ATS) | Payroll and MSP-held logins after POAM-004 (2026-10) |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Change log | CC8.1 | No | From 2026-09 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Purge and wiping records | CC6.5, C1.2 | Shredding certificates only | First purge by 2026-12 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-09 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the payroll vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception: for 2 of 40 sampled bank-change requests submitted through vendor support, the vendor's call-back was not documented. Management added a mandatory field.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the firm's BIA** for payroll (BP-02: RTO 8 h, RPO 24 h).
- **Controls the firm must run.** The report lists complementary user entity controls: provisioning and removing the firm's administrators, enabling MFA for them, reviewing bank-change and payroll register reports before submitting payroll, and verifying changes the firm's own staff enter. Three are open gaps at the firm: MFA by SMS code (POAM-004), no review of bank-change reports (POAM-006), and no call-back on staff-entered changes (POL-02 B.4). **These are exactly the weaknesses in the P08 scenario. The vendor's strong platform does not protect the firm until they close.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for 72-hour incident notice at renewal; confirm in the next report that the call-back fix operated all year.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC5.3, CC6.2, CC6.6, CC7.3 | Acknowledgments; questionnaire response; termination checklist (POAM-001); MFA on MSP-held logins (POAM-004); incident log |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.1, CC5.2, CC6.1, CC6.3, CC6.5, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; client security terms register; training (POAM-005); inventory; folder restriction (POAM-002); payroll MFA and alerts (POAM-004, POAM-006); wiping and purge (POAM-010, POAM-013); restore tests and tabletop (POAM-007, POAM-008); change log; contingency plan; vendor reviews (POAM-012) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the client:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Operations Manager as security contact, and commit to an updated self-assessment in April 2027.
