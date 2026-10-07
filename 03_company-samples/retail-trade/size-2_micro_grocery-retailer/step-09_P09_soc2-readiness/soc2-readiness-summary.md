# SOC 2 Readiness Summary: Cris Santos Company | Retail Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Tier / Vertical | Micro / Retail Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Availability (A1) |
| Target report | None. Readiness self-assessment only; no SOC 2 examination is planned |
| Part A | Store readiness self-assessment (`soc2-readiness.csv`), used to answer the cyber insurer's renewal application |
| Part B | Payment and commerce platform provider SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-08-26 by the Store Manager with the Bookkeeper; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A neighborhood grocery store is **not** a SOC 2 service organization. It sells groceries to consumers; it does not provide services to other businesses. **PCI DSS validation is the store's assurance mechanism** for card payments (the SAQs due 2026-11-30, P03). The Trust Services Criteria are used here for two practical reasons.

**A. Answering the insurer.** The cyber liability endorsement renews on 2026-11-01, and the renewal application is due 2026-10-15. Its security questions (MFA, backups, training, incident plan, vendor oversight) follow the same topics as the Security and Availability criteria. The Owner will answer them from this self-assessment, the POA&M (P07), and the P08 runbook, and will answer honestly where controls are not yet in place.

**The store will not get a SOC 2 audit.** Nobody has asked for one, a Type 2 report needs controls that have operated for months, and most of the store's controls were defined in August 2026. An audit would cost far more than the store's whole security budget.

**B. Relying on the provider.** The payment and commerce platform provider carries most of the store's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report and PCI DSS AOC are the evidence for those controls, and reading them each year is part of service provider oversight (PCI DSS 12.8.4; SA-9).

**Why Availability and not another category.** When the platform or the internet is down, the store loses most of its sales within hours (P05 BP-01, MTD 4 hours), and the insurer's application asks about business interruption. Confidentiality of customer data is covered under the Security criteria. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** in-store grocery sales with card, SNAP EBT, and cash; online ordering with curbside pickup and local delivery; loyalty program.
- **Infrastructure and software:** the Store Commerce Platform (SSP, P02): commerce platform, online store, P2PE terminals, the office PC and laptop, POS tablets, store phone, and store network.
- **People:** 7 workforce members, the MSP, and the marketing freelancer.
- **Data:** loyalty and online customer data, truncated card data and tokens, payout details.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 17 | 10 | 0 |
| Availability (A1, 3) | 0 | 2 | 1 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and PCI Lead designated; roles defined
- CC3.1, CC3.2, and CC3.3: risk tolerance set; first risk assessment done, including fraud scenarios (refunds, payouts, supplier payments)
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked by the Owner

**Not ready:**
- CC1.4: no training of any kind
- CC2.1: no inventory or terminal list
- CC2.3: the privacy notice and the checkout security claim are inaccurate
- CC3.4 and CC8.1: online store scripts and the AI feature went live with no review or approval
- CC6.2: shared cashier code; a former cashier's code active for 4 months
- CC7.1, CC7.2, and CC7.3: no change detection on the checkout page, no monitoring, no incident records
- CC7.5 and A1.3: no restore or cash-only drill has ever been done

## 4. Evidence inventory
The insurer's application asks for yes or no answers and may ask for proof. What the store can show now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation memo; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Provider SOC 2 and AOC review | CC9.2, A1.2 | Yes | Bridge letter (2026-10) |
| MFA settings screenshots for every administrator login | CC6.1 | Owner only | All logins (2026-10-15) |
| MSP monthly report (patching, antivirus, firewall) | CC5.2, CC6.8 | Yes (July 2026) | Monthly |
| Account review and terminal inspection sheets | CC6.2, CC6.4 | No | From 2026-09 (inspections daily, accounts monthly) |
| Approved script list and change log | CC3.4, CC8.1 | No | From 2026-09-30 |
| Restore test record and tabletop report | CC7.4, CC7.5, A1.3 | No | 2026-09-30 and 2026-11-30 |
| Training and phishing exercise records | CC1.4 | No | From 2026-10 |

## 5. Findings from the provider report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (support staff access without a ticket reference in 3 of 40 samples), remediated.
- **Availability:** the provider's stated RTO of 4 hours meets the store's 8-hour RTO for online ordering (BP-02) but **not** the 2-hour RTO for in-store checkout (BP-01). The store covers the difference with cash-only trading (P05; P01 R-013).
- **Controls the store must run.** The report lists complementary user entity controls: managing users and MFA, the code and scripts the merchant adds to its online store, inspecting payment devices and following the P2PE Instruction Manual, reviewing the activity log, and reporting suspected incidents. **Every one of them is an open gap at the store** (POAM-001 to POAM-005, POAM-009, POAM-013). The provider's strong controls protect the store only once those close.
- **PCI DSS:** the provider's AOC (2026-04) covers processing, P2PE, and online store hosting. The P2PE listing covers the countertop terminal model only, which confirms that the mobile reader is outside the P2PE solution (P03 G-060).
- **Follow-ups:** request a bridge letter to 2026-09-30; ask whether the AI offers feature will be in the next report; ask the provider to confirm its breach notice to merchants meets the 10-day limit in Fla. Stat. 501.171(6)(a).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC3.4, CC5.3, CC6.2, CC6.5, CC6.7, CC7.3, CC8.1 | Acknowledgments; change approval rule; checklists; personal POS codes (POAM-004, POAM-006); tablet reset; export deleted; incident log |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.2, CC2.3, CC5.1, CC5.2, CC6.1, CC6.3, CC6.4, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC9.1, CC9.2, A1.1, A1.2, A1.3 | MFA (POAM-005); scripts and monitoring (POAM-001, POAM-002, POAM-013); inventory (POAM-003); network separation (POAM-007); training (POAM-008, POAM-009); restore test (POAM-011); service providers (POAM-010); notice rewrite; continuity plan; failover router; tabletop |

**Answer to the insurer by 2026-10-15:** answer each question as of the submission date, attach the summary of this self-assessment and the POA&M if the carrier allows, and name the Store Manager as security contact. Update the self-assessment in August 2027.
