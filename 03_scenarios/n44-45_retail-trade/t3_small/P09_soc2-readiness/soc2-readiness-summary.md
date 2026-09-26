# SOC 2 Readiness Summary: Cris Santos Company | Retail Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| Tier / Vertical | Small / Retail Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Internal benchmark; no CPA-issued SOC 2 report is planned |
| Part A | Security-only readiness benchmark (`soc2-readiness.csv`) |
| Part B | Review of the POS vendor's and storefront vendor's assurance reports (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-28 by the IT Manager, with the Controller for Part B (fieldwork 2026-08-24 to 2026-08-28) |
| Approved | General Manager, 2026-09-04 |

## 1. Why SOC 2 (or an alternative) for this organization
**SOC 2 is not the company's assurance mechanism.** SOC 2 reports on controls at a *service organization*, a company that provides services to other businesses. A grocery store sells to consumers. No customer, bank, or partner has asked the company for a SOC 2 report.

**PCI DSS validation is the assurance that matters.** The acquirer confirmed in its letter of 2026-06-15 that the company validates each year by self-assessment, with SAQ P2PE for the store and SAQ A for online orders, due 2026-11-30 (P03). That is the assurance the company's bank and the card brands rely on.

SOC 2 appears here for two practical reasons:

**A. Security-only internal benchmark.** The PCI DSS scope is deliberately small, because P2PE and the processor's payment form keep card data out of company systems. So the SAQs say little about how the company protects **loyalty data, online accounts, and the checkout page's surroundings**, which is where FTC Act Section 5 expects reasonable security (P03 row G-071). The Security criteria (CC1-CC9) give the General Manager and the majority owner one broad yardstick for the whole program, using work already done in P01, P02, P06, and P07.

Other options considered:
- **A formal SOC 2 audit:** no one requires it, and it would cost more than the security fixes it would measure.
- **Relying on the SAQs alone:** they cover card data only.

**B. Third-party risk management.** The company depends on two vendors whose controls it cannot see directly:
- the **storefront vendor**, which hosts the checkout page and customer accounts;
- the **POS vendor**, which runs the registers and back office and has remote access to the store.

Their assurance reports are the evidence for the controls the company inherits (P02, P04). PCI DSS Requirement 12.8 also expects an annual check of service providers' compliance status.

## 2. System description (scope)
- **Services:** online ordering, loyalty, and the checkout page that hosts the processor's payment form, plus the administrator access that manages them.
- **Infrastructure and software:** the E-commerce and Loyalty Platform (SSP, P02) and its cloud tenant (P04).
- **People:** the 5 office staff who administer the platform, the E-commerce and Marketing Manager, and the marketing contractor.
- **Data:** customer accounts, loyalty member data, order history, prices and offers. No card data is stored.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

The in-store POS system is outside Part A. It is covered by the SAQ P2PE and by the POS vendor review in Part B.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 20 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: the Information Security Lead and reporting lines are designated
- CC3.1 and CC3.2: objectives are set and the risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M
- CC6.4: physical access is inherited from providers and the office is locked

**Not ready:**
- CC6.8 and CC8.1: no control over scripts or changes on the checkout page (the same gap as P01 R-001)
- CC6.3: 4 former employees still active and no access reviews
- CC7.1 and CC7.2: no change detection, scanning, or monitoring
- CC7.5: loyalty database recovery unproven
- CC2.3: the privacy notice does not match data sharing
- CC3.4: the pricing engine went live without a change review

The weakest area is **CC6.8, CC7.1, and CC8.1 together**: nobody controls or watches what runs on the checkout page. The same finding blocks the SAQ A eligibility statement (P03).

## 4. Findings from the vendor reports (Part B)
- **Storefront vendor:** SOC 2 Type 2 (Security and Availability), unqualified, 12 months to 2026-03-31, with one remediated change-approval exception. The stated 4-hour recovery time **meets the BIA** (P05 BP-02 RTO 8 hours). Its service provider AOC (2026-05) states that **the merchant is responsible for scripts it adds to its own pages**. That matches the P04 finding: the vendor's assurance does not cover the company's checkout scripts.
- **POS vendor:** a SOC 2 **Type 1** only, as of 2025-12-31. A Type 1 shows that controls were designed, not that they worked over time, so it gives less assurance. It has no PCI DSS AOC. The vendor states it does not handle card data, because the PIN pads belong to the processor's P2PE solution. **Follow-up:** request a Type 2 report at the next cycle and a bridge letter.
- **Controls the company must run (CUECs).** Both reports depend on the company running controls that are open gaps today:
  - unique POS back office accounts (P01 R-006; the shared administrator account breaks this)
  - approval of vendor remote sessions (POL-02 4.11)
  - storefront MFA (POAM-001)
  - control of checkout scripts (POAM-003, POAM-004)
  - admin log review (POAM-010)

  **The vendors' controls only protect the company once these gaps are closed.**
- **Contracts:** ask both vendors for incident notice within 24 hours at renewal. Fla. Stat. 501.171(6) sets 10 days as the outer limit for a third-party agent.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.8, CC8.1, CC7.1, CC6.1-CC6.3, CC2.3, CC7.4 | Script inventory and approvals, monitoring alerts, change records, access review records, updated privacy notice, tabletop report |
| 2027 Q1 | CC7.2, CC7.5, CC6.6, CC9.1, CC9.2 | Weekly log review checklists, restore test records, VLAN change record, continuity plan, provider responsibility matrix and current AOCs |
| 2027 Q2 | CC1.2, CC1.4, CC3.3, CC4.1 | Owner review minutes, training records, refund report reviews, quarterly app reviews |

**Next benchmark:** repeat this self-assessment in August 2027, after the 2026 SAQs are filed and the High POA&M items are closed.
