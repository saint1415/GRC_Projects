# Risk Register Report: Cris Santos Company Holdings | Retail Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Retail Trade, Wholesale Trade, Finance and Insurance) |
| Focus division | Grocery Retail (NAICS 445110), a Level 1 merchant under PCI DSS v4.0.1 |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | PCI DSS v4.0.1 targeted risk analyses and annual risk review for the retail CDE (N44-45-R01, Req. 12.3.1); the written risk assessment for Financial Services under the FTC Safeguards Rule (N44-45-R03, 16 CFR 314.4(b)(1)) |
| Registers | `risk-register.csv` (group), `risk-register-grocery-retail.csv`, `risk-register-grocery-wholesale.csv`, `risk-register-financial-services.csv` |
| Fieldwork | 2026-05-01 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-10 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that handles card data, Rewards Card customer information, customer and loyalty data, or that keeps stores and distribution centers running, in the three divisions, plus the corporate shared services they depend on: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and data centers, SYS-G4 digital front door, and SYS-G5 ERP. Division systems are SYS-D1 to SYS-D6 (`../00_company-facts.md` sections 3 and 7).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Grocery Retail, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact, not copied from the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks that could expose card data or Financial Services customer information at High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), the 2025 ROC, and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to the BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators and the card brands at once, SEC disclosure, and effects on more than one division.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 9 | 3 | 0 | 16 | n/a |
| Grocery Retail | 0 | 3 | 17 | 8 | 0 | 28 | 14 |
| Grocery Wholesale | 0 | 1 | 10 | 5 | 0 | 16 | 8 |
| Financial Services | 0 | 2 | 9 | 5 | 0 | 16 | 10 |
| **All registers** | **0** | **10** | **45** | **21** | **0** | **76** | **32** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Malicious script loaded through the shared tag management service skims card data on payment pages of more than one division | RT-001, RT-002, WD-006, FS-002 | Payment-pages-only tag container; tamper detection on all four payment pages with alerts to the SOC; isolated Rewards Card frame | Group digital director | 2026-11-30 |
| GR-02 | Ransomware spreads through shared services and stops stores, distribution centers, and card servicing at once | RT-006, WD-003, FS-013 | Acquired store and OT segmentation; full-volume WMS restore test; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-04 | AI in pricing, credit, and loss prevention harms customers or breaks consumer finance and consumer protection law | RT-015, RT-017, RT-028, FS-001, FS-012, FS-015 | Group AI governance program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-08 | A critical third party (processor, card processing platform, tag or script vendor) has an outage or breach affecting several divisions | RT-024, FS-003, WD-008 | Complete the TPSP list and responsibility matrix; Safeguards-based review of the card platform | Group Chief Risk Officer | 2027-03-31 |

### Grocery Retail (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| RT-001 | Malicious script on the web checkout overlays the hosted payment fields and captures brand card data | Payment-pages-only container; alerts to the SOC with a 1-hour response; monitoring on the app web view | Grocery Retail chief digital officer | 2026-11-30 |
| RT-002 | The Rewards Card number and code are captured from the company-hosted field on the checkout page | Isolated Rewards Card payment frame served by Financial Services | Grocery Retail chief digital officer | 2027-03-31 |
| RT-003 | Memory-scraping malware on legacy lanes at the 46 acquired stores | Segment POS VLANs, move vendor access to PAM, MFA for back office, patch within 30 days | Grocery Retail CISO | 2026-11-30 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| WD-001 | Grocery Wholesale | Ransomware enters through an OT vendor's always-on remote access and stops picking at the automated distribution centers | Grocery Wholesale security and compliance lead | 2026-12-31 |
| FS-001 | Financial Services | The credit decision model gives inaccurate adverse action reasons or produces disparate outcomes (12 CFR 1002.9(b)(2)) | Financial Services chief credit officer | 2026-12-31 |
| FS-003 | Financial Services | The card processing platform vendor is breached or unavailable (16 CFR 314.4(f)) | Financial Services CISO | 2027-03-31 |

### What the results say
The retail PCI DSS program is mature: Level 1 ROCs since 2015, encryption at the PIN pad, processor tokens, hosted payment fields, and a 24x7 SOC. There are no Very High risks. The High risks cluster around **what the divisions share and where one division's data passes through another's systems**:
1. **Payment pages and the shared tag container** (GR-01, scenario gaps 1 and 2). The same service that marketing uses to add scripts reaches three divisions' pages. The retail checkout is the most exposed, and the Rewards Card field on it belongs to a different regulatory program.
2. **The acquired stores** (RT-003, rolled into GR-10 at Moderate for the group). The 2025 acquisition brought legacy POS and flat networks into the CDE (scenario gap 3).
3. **AI in regulated decisions** (GR-04, FS-001). The credit decision model's reason codes were not revalidated after retraining (scenario gap 8), and the pricing engine has no emergency price freeze.
4. **Third parties** (GR-08). The card processing platform and the script vendors are the group's least-watched dependencies.

The distribution center OT risk (WD-001, gap 6) is the only High in Grocery Wholesale. It matters to the focus division because every group store depends on those distribution centers (P05).

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** payment page script governance and the Rewards Card frame (GR-01); acquired store remediation and migration (GR-10); OT segmentation (GR-13); group AI governance program (GR-04); third-party oversight (GR-08); SIEM onboarding of remaining sources (GR-12).
- **Accepted (all Low):** RT-018 (storefront denial of service), RT-021 (lost handheld), WD-015 (labor optimization metrics), FS-016 (paper disposal).
- **Contract and process actions:** opt-out suppression in the CDP (GR-09, RT-016, FS-006); the FTC notice and Reg Z steps in the notification matrix (GR-03, FS-008).
- **Treatment status:** 44 risks are In progress, 28 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-10. The Financial Services register and its treatment plans also feed the Qualified Individual's annual written report to the Financial Services board (16 CFR 314.4(i)), due 2026-12-31. The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here.

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-10.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the six High division risks, 2026-09-10.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-10.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident.
