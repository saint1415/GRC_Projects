# SOC 2 Readiness Summary: Cris Santos Company | Management of Companies and Enterprises | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| Tier / Vertical | Micro / Management of Companies and Enterprises |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Office readiness self-assessment (`soc2-readiness.csv`), used to answer a custodian's due diligence questionnaire and to report to the Board of Managers |
| Part B | Investment platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-10 by the Family Office Director with the independent consultant; approved by the Principal 2026-09-18 |

## 1. Why SOC 2 for this organization
A single-family office is **not** a SOC 2 service organization. It serves only the family and the family's own companies, not outside customers. The Trust Services Criteria are used here for three practical reasons.

**A. Answering a custodian.** In August 2026 one of the two custodians sent a due diligence questionnaire about the office's controls, because the office holds delegated access to family accounts. Its questions follow the Trust Services Criteria for security and confidentiality. The office will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-30.

**B. Reporting to the family.** The Board of Managers asked for a plain measure of readiness it can track year to year. The same checklist serves as an appendix to the Family Office Director's annual written report.

**The office will not get a SOC 2 audit.** It has no customers who need one, most of its controls were defined in September 2026, and a Type 2 report needs controls that have operated over a period, usually 6 to 12 months. The custodian accepted a self-assessment in its questionnaire instructions.

**C. Relying on a vendor.** The investment platform holds positions and account numbers for every family account and is the vendor with the broadest view of family wealth. Its SOC 2 Type 2 report is the main evidence for the controls the office inherits from it, and reviewing it is part of service provider oversight under 16 CFR 314.4(f)(3) and SA-9.

**Why Confidentiality and not another category.** The family's main concern is exposure of its information: identity documents, estate plans, account numbers, and where family members live and travel. Confidentiality (C1) tests exactly that: identifying confidential information and disposing of it. Availability is covered by the BIA (P05), and every critical system is SaaS or bank-hosted. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** subsidiary oversight, investment management for family clients, and family administration (payments, payroll, accounting, records).
- **Infrastructure and software:** the Family Office Shared Services Platform (SSP, P02): accounting, productivity and identity, bill pay, payroll, bank and custodian portals, investment platform, document vault, 8 laptops, office network, and the SYS-11 cloud workload.
- **People:** 7 staff, 9 subsidiary guests, 11 family members as vault users, and the MSP.
- **Data:** family members' personal and financial information; household and office employee data; subsidiary financial information.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 16 | 10 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Qualified Individual designated; roles written
- CC3.1, CC3.2, and CC3.3: risk framing set, a 2026 risk assessment done, and **fraud risk analyzed**, because payment fraud is the office's top risk
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked
- CC6.4: physical access (locked suite, safe for tokens and originals; vendor data centers under SOC 2)

**Not ready:**
- CC2.1 and C1.2: no data inventory and no disposal of old confidential records
- CC3.4: the AI assistant pilot started with no change review
- CC6.2, CC6.3, and CC6.5: access granted without approval, too broad (the Family site), and never removed on schedule
- CC7.1, CC7.2, CC7.3, CC7.5: no scanning, no monitoring, no incident records, no tested restore
- CC8.1: the MSP changes settings without recorded approval

## 4. Evidence inventory
The questionnaire asks for evidence. What the office can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC3.3, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-10) |
| Board minutes and the annual written report | CC1.2 | Yes (2026-09-18) | Each September |
| Investment platform SOC 2 review | CC9.2 | Yes | Bridge letter (2027-01); accounting vendor review (2027-03) |
| Payment log with callbacks | CC3.3, CC9.1 | No | From 2026-10-15 |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-11 |
| Vulnerability scan reports | CC7.1 | No | Monthly from 2026-11 |
| Restore test records | CC7.5 | No | From 2026-10 (SYS-11), quarterly after |
| Training and phishing simulation records | CC1.4, CC2.2 | Video list only | From 2026-10 |
| Disposal log | CC6.5, C1.2 | Shredding receipts only | From 2027-03 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the investment platform report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception (a departed vendor employee kept access for 9 days), remediated.
- **Confidentiality:** customer data is used only to provide the service and is deleted within 90 days of termination on request. The office will ask for written certification of deletion at contract end.
- **Controls the office must run.** The report lists complementary user entity controls: user provisioning and removal, MFA through the customer's single sign-on, periodic access review, review of custodian feed authorizations, and protection of customer credentials. Three are open gaps at the office: removal and review (POAM-001, POAM-013) and phishable MFA (POAM-002). The office had never reviewed its feed authorizations; they now join the quarterly access review. **The vendor's controls protect the family only once the office's side is done.**
- **Follow-ups:** request a bridge letter to 2026-12-31; ask how the vendor monitors its carved-out hosting provider; ask for 24-hour incident notice and a Florida third-party agent clause at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-12-31) | CC1.1, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, C1.1 | Acknowledgments; callback letter; questionnaire response; security keys and SYS-11 port (POAM-002); account procedure (POAM-001); need-to-know folders (POAM-005); alerts and log review (POAM-003); scans (POAM-011); backup and restore tests (POAM-006, POAM-007); tabletop (POAM-008); incident log (POAM-009); data inventory; change approval |
| 2027 Q1 | CC6.5, CC9.2, C1.2 | Retention schedule and first disposal (POAM-012); MSP amendment and accounting vendor review (POAM-010) |
| 2027 Q3 | CC1.2 | Second annual written report to the Board of Managers |

**Response to the custodian:** send this summary, the readiness checklist, and the POA&M by 2026-10-30, name the Family Office Director as security contact, and commit to an updated self-assessment in September 2027.
