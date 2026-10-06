# SOC 2 Readiness Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Micro / Professional, Scientific, and Technical Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Firm readiness self-assessment (`soc2-readiness.csv`), used to answer a payroll client's vendor security questionnaire |
| Part B | Tax software vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager (Qualified Individual) with the independent consultant; approved by the Owner CPA 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person CPA firm is **not** a SOC 2 service organization in the sense its clients would audit. It prepares returns and keeps books; it does not run a system that other companies rely on for their own controls. The firm also does not perform SOC examinations for anyone. SOC reports are a service larger CPA firms sell, and that work would bring attest independence rules this firm does not take on. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** In June 2026 the firm's largest bookkeeping and payroll client, a property management company with about 140 employees on payroll, sent a vendor security questionnaire. The client's own lender and insurer ask it how its payroll provider protects employee SSNs and bank accounts. The questions follow the Trust Services Criteria for security and confidentiality. The firm will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-09-30.

**The firm will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the firm's controls were defined in August 2026. An audit would also cost more than the firm's whole security budget. The client's questionnaire accepts a self-assessment.

**B. Relying on the tax software vendor.** The tax software vendor carries most of the firm's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of service provider oversight under 16 CFR 314.4(f)(3).

**Why Confidentiality and not another category.** What the payroll client, and every individual client, cares about most is that their tax and payroll information stays confidential and is disposed of when no longer needed. That is what C1.1 and C1.2 test. It also lines up with the firm's two most specific legal duties: IRC 7216 limits on disclosure and the Safeguards Rule disposal requirement (314.4(c)(6)). Availability matters in the deadline weeks, but the client did not ask about it; the BIA (P05) covers it internally. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** individual and business tax preparation; bookkeeping and payroll for 38 small businesses; IRS notice responses.
- **Infrastructure and software:** the Client Tax Platform (SSP, P02): tax software, client portal, productivity suite, suite backup, 8 computers and the MFP, office network; plus the payroll platform (SYS-04) for this client's data.
- **People:** 7 employees, a seasonal assistant, and the MSP.
- **Data:** tax return information, customer information, payroll employee data.
- **Procedures:** POL-02, POL-03, POL-04, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 15 | 12 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Qualified Individual designated in writing; roles defined
- CC3.1 and CC3.2: objectives and risk tolerance set; 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; weaknesses tracked
- CC6.4: physical access (locked suite and cabinets; vendor data centers under SOC 2)

**Not ready:**
- CC1.4: security training was a single 2024 video
- CC2.1: no inventory of systems or data locations
- CC3.4: the AI assistant was adopted without any assessment
- CC6.2 and CC6.3: access granted and removed without a process; everyday administrator accounts; all folders open to all staff
- CC6.5 and C1.2: no disposal of electronic records since 2016
- CC6.7: returns emailed as plain attachments; firm email on unmanaged phones
- CC7.1, CC7.2, CC7.3: no scanning, monitoring, or event review
- CC7.5: no full restore test
- CC8.1: the MSP changes settings without approval

**What matters most to the payroll client.** Its employees' SSNs and bank accounts sit in the payroll platform and in the firm's client folders. Today every firm employee can open those folders (CC6.3, C1.1), and a payroll bank change requested by email is not called back (P01 R-003). Both are fixed by 2026-10-31 (POAM-004) and 2026-09-30 (call-back rule, POL-02 C.3), and the response will say so.

## 4. Evidence inventory
The questionnaire asks for evidence. What the firm can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly program review notes (2026-09) |
| Tax software vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC5.2, CC6.8 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Change log | CC8.1 | No | From 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | 2024 only | From 2026-12 |
| Retention schedule and disposal records | CC6.5, C1.2 | Paper shredding certificates only | Schedule 2027-06 |
| Tabletop exercise report | CC7.4 | No | 2026-12 |

## 5. Findings from the tax software vendor report (Part B)
- **Opinion:** Type 2, unmodified, 12 months ending 2026-03-31. One exception (customer approval not recorded for 2 of 25 support screen-sharing sessions), remediated in 2026-01.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the firm's BIA** (RTO 8 h, RPO 1 h for BP-01 and BP-02).
- **Data location:** U.S. production and backup data centers, which supports the preparer-to-preparer permission in 26 CFR 301.7216-2(d)(1).
- **Controls the firm must run.** The report lists complementary user entity controls: prompt user removal, least-privilege roles, review of user activity, protection of workstations and credentials, and prompt notice of suspected account compromise. **All five are open gaps at the firm today** (POAM-001, POAM-004, POAM-005, POAM-014, POAM-007). The vendor's controls protect the firm only once those gaps close.
- **AI feature:** the vendor's optional AI document extraction is outside the tested scope. It stays off (P10 inventory AI-002).
- **Follow-ups:** bridge letter to 2026-09-30; 72-hour incident notice in the contract at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.3, CC6.1, CC6.6 | Acknowledgments; questionnaire response with a named security contact; number matching and legacy authentication blocked (POAM-002); MFA on MSP-held logins (POAM-003) |
| 2026 Q4 | CC1.2, CC1.5, CC2.1, CC2.2, CC3.4, CC5.2, CC5.3, CC6.2, CC6.3, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, C1.1 | Monthly program review notes; tabletop (POAM-007); inventory; pre-adoption checklist; account process and folder limits (POAM-001, POAM-004, POAM-010); portal-only delivery (POAM-013); EDR; alerts and log review (POAM-005); restore tests (POAM-009); change log; contingency plan; vendor reviews (POAM-012) |
| 2027 Q1 | CC1.4, CC5.1, CC6.5 | Training and first phishing simulation before the season (POAM-006); remaining P01 treatments by 2027-01-15; MFP drive wipe at lease end (POAM-014) |
| 2027 Q2 to Q3 | C1.2, CC3.3 | Retention schedule and first purge (2027-06-30); insider fraud scenarios in the July 2027 risk assessment |

**Response to the payroll client:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027, after the filing season.
