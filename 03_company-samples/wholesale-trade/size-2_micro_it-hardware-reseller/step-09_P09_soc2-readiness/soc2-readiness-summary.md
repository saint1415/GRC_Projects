# SOC 2 Readiness Summary: Cris Santos Company | Wholesale Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| Tier / Vertical | Micro / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the Federal Prime's annual supplier security questionnaire |
| Part B | ERP vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Operations Manager with the independent consultant; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person reseller is **not** a SOC 2 service organization in the usual sense: it sells products, and its customers do not rely on company-run systems except the small customer portal, which is the ERP vendor's SaaS. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** In July 2026 the Federal Prime sent its annual supplier security questionnaire. The Prime sends the company DoD equipment lists and delivery details for setup orders and must check that its suppliers protect them. The questionnaire follows the Trust Services Criteria. The company will answer with this self-assessment, the relevant POA&M items (P07), and a named security contact. The response is due 2026-09-30.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. The cost would also be out of scale with $1.1 million in revenue. The Federal Prime accepts a self-assessment. The questionnaire is also **not** a substitute for the CMMC Level 1 self-assessment, which the Prime separately expects to see in SPRS (P03 G-024).

**B. Relying on the ERP vendor.** The ERP vendor carries most of the company's inherited controls (P02 section 10.2) and holds the FCI attached to DoD orders. Its SOC 2 Type 2 report is the evidence for those controls, and reviewing it each year is part of vendor oversight (SA-9; 32 CFR 170.19(b)(3)).

**Why Confidentiality and not another category.** What the Federal Prime and DoD customers care about is that equipment lists, user and room assignments, and delivery details stay private. That is a Confidentiality question. Availability matters to the company, but the Prime did not ask about it and the BIA (P05) covers it. Processing Integrity and Privacy were not requested.

**Truthful answers.** Any security claim the company makes in the questionnaire must match this assessment. Overstated answers would raise the same problem as the unsupported SPRS entry (P01 R-004) and could be an unfair or deceptive practice under the FTC Act (N42-R01).

## 2. System description (scope)
- **Services:** reselling and setting up IT hardware and software; the customer ordering portal.
- **Infrastructure and software:** the Reseller Operations Platform (SSP, P02): ERP with customer portal, productivity suite, suite backup, 9 computers and the setup bench, office network.
- **People:** 7 staff and the MSP.
- **Data:** FCI (equipment lists and delivery details), customer orders and pricing, supplier bank details, employee records.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 18 | 8 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: security lead and Affirming Official designated; roles defined
- CC3.1, CC3.2, CC3.3: risk tolerance set; 2026 risk assessment with supplier and fraud risks
- CC4.1, CC4.2: independent assessment done; deficiencies tracked
- CC6.8: endpoint protection on every computer

**Not ready:**
- CC1.4: no training
- CC2.1: no inventory of devices or of where FCI lives (the covered camera recorder was missed)
- CC6.2: access granted and removed without a process (the former technician)
- CC6.5 and C1.2: no disposal or deletion records
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC8.1: no change approval (the AI auto-submit was turned on without review)

**Most important partial item:** C1.1. FCI is classified as Restricted in POL-04 but still sits in a folder all 7 staff can open and in local copies (P01 R-012).

## 4. Evidence inventory
What the company can send the Federal Prime now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| ERP vendor SOC 2 review | CC9.2, C1.1 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, endpoint protection, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Disposal log and bench job deletion records | CC6.5, C1.2 | No | From 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the ERP vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (a late quarterly review of vendor staff access), remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the company's BIA** (BP-01: RTO 8 h, RPO 1 h).
- **Confidentiality terms conflict with company policy.** The system description says customer data may be used in de-identified form to improve features, and the AI service behind the reorder feature is a carved-out subservice organization. POL-04 4.9 does not allow FCI in any AI tool, so DoD orders must be excluded from the reorder feed and written terms obtained (P10).
- **Controls the company must run.** The report lists complementary user entity controls: user provisioning and removal, role assignment, MFA enforcement, review of access and audit logs, and the decision whether customer portal users must use MFA. Removal (POAM-001) and log review are open gaps at the company. **The vendor's controls protect the company's data only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask how the vendor monitors the AI subservice organization; ask for 72-hour incident notice at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC7.3 | Acknowledgments; questionnaire response; incident log; MFA on MSP-held logins (POAM-003) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1 to CC6.7, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; training (POAM-004); inventory (POAM-005); named accounts and termination process (POAM-001, POAM-002); restricted FCI folder; disposal log (POAM-008); visitor control (POAM-009); scanning and firmware (POAM-011); backup and restore tests (POAM-006); tabletop; contingency plan; MSP and supplier reviews (POAM-010, POAM-012) |

**Response to the Federal Prime:** send this summary, the readiness checklist, and the relevant POA&M items by 2026-09-30, name the Operations Manager as security contact, disclose that the SPRS entry is being corrected on counsel's advice, and commit to an updated self-assessment in April 2027.
