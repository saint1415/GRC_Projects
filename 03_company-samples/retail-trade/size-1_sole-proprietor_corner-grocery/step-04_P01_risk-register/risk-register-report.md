# Risk Register Report: Cris Santos Company | Retail Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Size tier | Sole Proprietorship (owner only, 0 employees; unpaid family member at the register about 8 hours a week) |
| Vertical | Retail Trade |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | The annual risk assessment that PCI DSS v4.0.1 Requirement 12.3 expects (N44-45-R01), and the risk basis for "reasonable security" under FTC Act Section 5 (N44-45-R02) and Fla. Stat. 501.171(2). This is the store's first one |
| Prepared | 2026-08-14 by the owner, with the outside IT helper |
| Risk owner and approver | Owner (every risk) |
| Approved | 2026-09-04 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: SYS-01 to SYS-10, the storefront, and the contracted services (processor, website builder, POS app vendor, ISP, distributor, AI chatbot vendor). Processes come from the BIA (P05).

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, the owner applies three fixed rules:
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan. Not accepted as-is. Any risk that exposes full card data is never accepted.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the gap analysis (P03), and a walk through the store, the router, the laptop, and every SaaS account with the outside IT helper on 2026-08-11 and 2026-08-12.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale. Combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories.
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 9 |
| Low | 3 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Online store admin takeover used for e-commerce skimming | High | MFA and unique passphrase; no custom code or add-ons on checkout; monthly activity check | Owner | 2026-09-15 |
| R-002 | Paper card data with security codes stolen from the drawer or trash | High | Never write card data; shredder; locked drawer | Owner | 2026-09-15 |
| R-004 | Personal email takeover exposes customers and resets the store password | High | MFA now; separate business email later | Owner | 2026-09-15 |
| R-003 | Shared Wi-Fi reaches the card terminal; default router password | Moderate | Guest network; separate terminal network; new passwords | Owner | 2026-12-31 |
| R-013 | Compromise not recognized; processor 24-hour term missed | Moderate | P08 runbook, printed contacts, walkthrough | Owner | 2026-09-30 |
| R-014 | Continued PCI DSS non-compliance and fees | Moderate | Correct portal answers; complete both SAQs with evidence | Owner | 2026-11-30 |

The three High risks share one cause: **anyone who gets one password can reach customer card data.** The email password opens the online store, the online store decides where shoppers pay, and until 2026-08-11 full card data sat on paper in an open drawer. Two free settings (MFA on email and the online store) and one habit (never write card data down) bring R-001, R-002, and R-004 down within two weeks of adoption.

## 4. Treatment summary
- **Free fixes first (by 2026-09-15):** MFA on email and the online store, unique passphrases, no card data on paper, shredder (about $60).
- **By 2026-09-30:** router and Wi-Fi passwords, guest network, separate POS user, terminal inspection and serial number, laptop encryption, AI chatbot rules (R-008, R-009), the P08 runbook.
- **Budgeted (about $300 a year):** a password manager, a business email account with version history for files, and a small second router or a router with VLAN support to put the terminal on its own network (R-003, R-012).
- **By 2026-11-30:** both SAQs completed with evidence (R-014).
- **Accepted (Low):** R-011 (processor or internet outage; cash sales continue) and R-015 (hurricane; cloud services reachable from home).

**Feedback from the control assessment (P07):** the terminal's factory-default manager password (found 2026-08-13) is part of R-006, and the default router password is part of R-003.

## 5. Approval
Owner, 2026-09-04: approved all treatment plans and the two acceptances. Next full review August 2027, before each annual SAQ, or sooner after a new system, a new vendor, a hire, or an incident.
