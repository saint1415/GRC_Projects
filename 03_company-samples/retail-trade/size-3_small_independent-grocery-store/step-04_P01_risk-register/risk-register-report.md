# Risk Register Report: Cris Santos Company | Retail Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| Size tier | Small (60 employees) |
| Vertical | Retail Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | PCI DSS v4.0.1 Requirement 12.3 (risks to the cardholder data environment identified and managed) and the "reasonable security" expectation under FTC Act Section 5 |
| Prepared | 2026-07-31 by the IT Manager (Information Security Lead); R-009 and R-032 updated 2026-08-14 after P07 testing |
| Approved | 2026-09-04 by the General Manager (Moderate and below) and the majority owner (High) |

## 1. Scope and risk framing
**Scope.** The whole business: the store, the E-commerce and Loyalty Platform (P02), card acceptance in the store and online, the store network and building systems, and the vendors that touch customer or card data (`../00_company-facts.md` sections 3 and 4). The business processes come from the BIA (P05).

**What the company protects most:**
- Card data typed into the online checkout (the company never stores it, but its checkout page can expose it)
- About 21,000 loyalty members' contact details and purchase history
- The ability to sell (registers and card authorization) and to keep refrigerated stock safe

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the General Manager may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. A High risk that affects card data or food safety may not be accepted without treatment.

This is the company's first documented risk assessment. The 2025 SAQs were completed without one.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews (General Manager, Controller, E-commerce and Marketing Manager, Store Manager), a store walkthrough on 2026-07-22, and the gap analysis (P03).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were rated and combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, contractual and regulatory, food safety, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 23 |
| Low | 6 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Malicious script on the checkout page skims card data (e-commerce skimming) | High | Script inventory and approval; integrity settings; payment-page tamper detection | E-commerce and Marketing Manager | 2026-11-15 |
| R-002 | Marketing contractor's storefront account taken over and used to add a malicious tag | High | Single sign-on with MFA; no script rights for the contractor | IT Manager | 2026-10-15 |
| R-004 | Ransomware spreads from an office PC to the POS back office and refrigeration controllers | High | Separate VLANs for IoT and POS back office; EDR; offline price file | IT Manager | 2027-01-31 |
| R-006 | Shared POS administrator account misused, including to break P2PE scope | Moderate | Named accounts; password change; monthly setting check | Store Manager | 2026-10-31 |
| R-015 | Dynamic pricing raises prices in lower-income delivery zones | Moderate | Zone feature disabled; monthly fairness tests (P10) | E-commerce and Marketing Manager | 2026-10-31 |
| R-003 | Loyalty exports leaked or reused by the marketing contractor | Moderate | Stop emailed exports; data use and security addendum | E-commerce and Marketing Manager | 2026-10-31 |

Two High risks share one theme: **the checkout page is the company's real card-data exposure.** Point-to-point encryption and the embedded payment form keep card numbers out of company systems, but anyone who can change the page that hosts the form can capture what customers type (R-001, R-002, and R-032). Fixing script control also reduces R-008 (inaccurate SAQ attestation) and R-010 (late incident response).

The third High risk (R-004) comes from the flat corporate network. Refrigeration controllers and the POS back office can be reached from office PCs, so one infected PC could stop sales and put refrigerated stock at risk.

R-032 was added on 2026-08-14 after control assessment testing (P07) found a retired storefront app that still had permission to change the theme code. P07 testing also confirmed R-009 (4 former employees still active).

## 4. Treatment summary
- **Funded (2026 Q4 budget, $31,500):**
  - Payment-page script monitoring service ($6,000 a year)
  - Network switch upgrade and VLAN work for IoT and POS back office ($9,000)
  - Endpoint detection and response for 16 PCs ($4,500 a year)
  - Cellular failover on the firewall ($1,200 plus service)
  - Separate backup account and log storage ($2,800 a year)
  - Optional QSA review of the 2026 SAQs ($8,000)
- **Accepted:**
  - R-020 (Moderate): storefront outage; the vendor's recovery commitment meets the BIA
  - R-027 (Low): lost handheld; remote wipe exists
  - R-028 (Low): denial of service; vendor-managed
- **Contract actions:** data use and security addendum for the marketing contractor (R-003) by 2026-10-31; pricing vendor addendum (R-025) and service provider responsibility matrix (R-021) by 2026-11-30.

## 5. Approval
- General Manager: approved Moderate and Low treatments and acceptances, 2026-09-04.
- Majority owner: approved the High-risk treatment plans and the budget, 2026-09-04.
- Next full review: July 2027, or sooner after a major change (for example a new payment channel) or an incident.
