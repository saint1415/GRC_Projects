# Risk Register Report: Cris Santos Company | Retail Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Size tier | Micro (7 employees) |
| Vertical | Retail Trade |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | PCI DSS v4.0.1 Requirement 12.3 (risks to the cardholder data environment) and the FTC Act Section 5 reasonable-security expectation (N44-45-R01, N44-45-R02) |
| Prepared | 2026-07-31 by the Store Manager (Security and PCI Lead) with the MSP technician |
| Updated | 2026-08-12 (R-025 added from P07 testing); 2026-08-26 (R-018, R-019 updated from the P10 assessment); 2026-08-31 (R-008 treated; R-023 and R-024 accepted) |
| Approved | 2026-08-31 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors. That covers every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-11), the store itself, and the vendors that handle card or customer data or run systems for the store: the payment and commerce platform provider, the MSP, the productivity suite vendor, the marketing freelancer, and the 4 script vendors whose code runs on the online store.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Store Manager may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. Any risk to card data at High is never accepted, because the merchant agreement makes the store liable for a compromise.

This is the store's first documented risk assessment. Before 2026, security decisions were made by the Owner case by case, with the MSP's advice.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), and interviews with the Owner, the Store Manager, the Bookkeeper, both Cashiers, the Order Picker and Delivery Driver, the marketing freelancer, and the MSP technician (2026-07-20 to 2026-07-31). A browser capture of the checkout page (2026-07-28) and a store walkthrough (2026-07-22) added evidence.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, together with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a store with about $3,000 of sales a day, a card compromise with forensic costs and card brand fees, or a closure of more than 2 days, is rated High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 2 |
| Moderate | 15 |
| Low | 8 |
| **Total** | **25** |

Status: 8 In progress, 14 Open, 3 Closed (R-008 treated; R-023 and R-024 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Malicious script on the checkout page skims card data | High | Remove scripts from checkout; approved script list; provider script restriction; payment page monitoring | Store Manager | 2026-11-15 |
| R-002 | Freelancer's administrator login taken over to inject a script | High | MFA on every administrator login; content-only role; freelancer agreement | Store Manager | 2026-10-15 |
| R-012 | Card compromise handled late (24-hour provider notice, Florida 30-day clock) | Moderate | POL-03 and P08 runbook; wallet cards; tabletop | Store Manager | 2026-11-30 |
| R-003 | Mobile reader outside the P2PE solution; 2025 SAQ P2PE wrong | Moderate | Retire the reader; written scope before the 2026 SAQs | Owner | 2026-11-30 |
| R-025 | Administrator login used to change the payout bank account | Moderate | Payout changes by the Owner only, with MFA; alerts | Owner | 2026-10-15 |
| R-015 | Cooler fails overnight and the alert never arrives | Moderate | Offline alert; closing log; failover router | Owner | 2026-10-31 |

**The common theme is the online checkout page.** The provider protects its own card fields, but the store lets scripts and an outside administrator change the page around them (R-001, R-002). The same small fixes, MFA and a short approved script list, also reduce R-005, R-011, and R-025. In the store, card data is well protected by P2PE, so in-store risks are about devices and people (R-004, R-009) rather than data.

**Risks that were fixed or found during the work:**
- R-008: the MSP closed the internet port that exposed the CCTV recorder and changed its default password on 2026-08-14. The risk is closed.
- R-010: the former cashier's POS code was disabled on 2026-07-21, the day it was found. The POS activity report showed no use after the last shift. The process gap remains open.
- R-025: added on 2026-08-12 after P07 testing showed that any administrator, including the Store Manager without MFA, could change the payout bank account.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the Owner; about $1,300 one-time and $1,900 a year):**
  - Payment page monitoring service: about $600 a year
  - Cellular failover router: about $350 one-time and $300 a year
  - Security awareness training with phishing exercises for 7 people: about $400 a year
  - Second Wi-Fi network setup, office PC encryption, and restore test by the MSP: about $650 of MSP time (one-time)
  - Mobile device management for the store phone and tablets (MSP add-on): about $600 a year
  - Independent assessment in 2026 (P07): about $300 one-time beyond the MSP's included hours
- **No cost:** MFA, personal POS codes, removing scripts, terminal inspections, deleting the loyalty export, and the policies are staff time.
- **Accepted:** R-023 (Low; provider controls receipt format), R-024 (Low; provider controls customer sign-in and fraud screening).
- **Contract actions:** written freelancer agreement (R-002, R-011) by 2026-09-30; MSP evidence of MFA and technician list at the next monthly review (P07 POAM-010).

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, a second store, a new payment provider, or new AI features) or an incident.
