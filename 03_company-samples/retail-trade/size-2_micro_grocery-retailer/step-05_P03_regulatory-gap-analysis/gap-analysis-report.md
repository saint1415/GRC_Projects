# Regulatory Gap Analysis: Cris Santos Company | Retail Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Tier / Vertical | Micro / Retail Trade |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N44-45-R01) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) (N44-45-R02), plus a one-row check of FACTA receipt truncation, 15 U.S.C. 1681c(g) (N44-45-R05) |
| Assessment dates | 2026-07-20 to 2026-07-31; FTC offer rows refreshed with the P10 test on 2026-08-25 |
| Assessor | Store Manager (Security and PCI Lead) with the MSP technician and the Bookkeeper |
| Approved | Owner, 2026-08-31 |

## 1. Applicability
**PCI DSS applies by contract.** The store accepts payment cards, and its merchant agreement with the payment provider requires PCI DSS compliance. PCI SSC sets no size tiers. Merchant levels and validation rules come from the card brands and the acquirer: Visa, for example, sets the level from a merchant's total Visa transactions over 12 months and makes acquirers responsible for having their merchants validate at the right level. The level thresholds were not verified from a card brand source, so this analysis does not state the store's level. In its compliance notice of 2026-06-10, the provider asked for **SAQ P2PE** for the store and **SAQ A** for the online store, due 2026-11-30.

**Why the store's PCI scope is small (scope reduction reasoning):**
- **In the store, validated P2PE.** The 2 countertop terminals belong to the provider's validated, PCI-listed P2PE solution. Card data is encrypted inside the terminal and only the provider can decrypt it. The POS tablets, the office PC, and the store network see only encrypted data and are not part of a cardholder data environment (CDE). SAQ P2PE v4.0.1 covers only Requirements 3.1, 3.2, 3.3, 9.1, 9.4, 9.5, 12.1, 12.6, 12.8, and 12.10, and only for merchants that meet its eligibility criteria: **all** payment processing for the channel goes through the validated P2PE solution, the only systems that handle account data are the solution's terminals, and the merchant follows the P2PE Instruction Manual.
- **The mobile reader breaks that eligibility.** About 250 card payments a year are taken at the curb or on delivery with a Bluetooth reader paired to the store phone. The reader comes from the same provider but **is not part of its P2PE solution**. The 2025 SAQ P2PE was signed without anyone noticing. Until the reader is retired (or replaced with a device in the P2PE solution), the store cannot truthfully attest SAQ P2PE eligibility. This is the most important finding of this analysis (row G-060, 12.5; P01 R-003).
- **Online, provider-hosted card fields.** The online store runs on the provider's platform, and the card fields on the checkout page are served by the provider inside a frame. Card data goes from the customer's browser to the provider, and the store receives a token. **The page around the card fields is still the store's responsibility:** the 4 scripts the store added through the custom code setting load on the checkout page, and a malicious script can draw a fake card form over the real one. This is why PCI DSS v4.0.1 Requirements **6.4.3** (manage payment page scripts) and **11.6.1** (detect changes and tampering on payment pages) matter here.
- **SAQ A eligibility.** Since the January 2025 SAQ A revision (effective 2025-03-31), SAQ A no longer lists 6.4.3 and 11.6.1. Instead, a merchant whose page embeds a processor's payment form confirms that its site is **not susceptible to attacks from scripts** that could affect its e-commerce systems. PCI SSC FAQ 1588 says a merchant can confirm this by using techniques such as those in 6.4.3 and 11.6.1, or by getting confirmation from its compliant processor that the processor's solution protects the merchant's page. PCI SSC states that the revision does not remove or weaken the underlying requirements. The 2025 SAQ A was signed with this statement checked and no evidence.

**Rows marked Not applicable** (29) fall into three groups:
- requirements for CDE networks and systems the store does not have, because of P2PE and the provider-hosted checkout (Requirements 1, 2.3, 5.2-5.3, 9.2-9.3, 10, 11.2, 11.4-11.5);
- requirements with nothing to protect, because no card data or keys are stored and no staff see clear-text card data (3.5-3.7, 12.7);
- requirements for service providers or special designations only (12.4, 12.9, Appendices A1-A3).

Not applicable to PCI does not mean unneeded. Network separation, antivirus, and log review are still part of reasonable security under FTC Act Section 5 (row G-071) and appear in P01 and P07.

**Secondary regulation.** FTC Act Section 5 applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)). It may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits to consumers or competition (45(n)). This matters for the loyalty data, the website's claims, and the AI offers feature (P10). FACTA receipt truncation applies to any business that accepts cards and was checked in one row.

**Not applicable, with reasons:** FTC Safeguards Rule and Red Flags Rule (no store credit, house accounts, or covered accounts), CCPA (no California business and far below the revenue threshold), COPPA (the online store is not directed to children), INFORM Consumers Act (no third-party sellers), SEC disclosure (privately held), and HIPAA (no pharmacy). The store is an FNS-authorized SNAP retailer (7 CFR 278.1); SNAP program rules are outside this analysis. EBT cards are not payment-brand cards, so PCI DSS does not cover them, but they are read on the same P2PE terminals. Florida breach notification (Fla. Stat. 501.171) is handled in P08.

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their requirement groups (for example 8.2). The two payment-page requirements were taken to the defined-requirement level (6.4.3 and 11.6.1), and 6.4 was split into its three defined requirements. The appendices were added. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; read the requirement text in the official standard. The requirements in SAQ P2PE and its eligibility criteria were confirmed in the SAQ P2PE for PCI DSS v4.0.1 (October 2024). The SAQ A change comes from PCI SSC pages (blog posts dated 2025-01-30, 2025-02-28, and 2025-03-10).
2. **FTC and FACTA rows** cite the statute text (15 U.S.C. 45(a)(1), 45(n); 15 U.S.C. 1681c(g)).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 to CSF 2.0 or SP 800-53 was used.
4. **Documentary evidence.** Each status rests on a named document or record: the 2025 SAQs, the merchant agreement, the provider's compliance notice and P2PE solution listing, the provider's AOC, dashboard and online store user lists, POS code list, payroll roster, custom code setting, a browser capture of the checkout page (2026-07-28), a mailbox and office PC search (2026-07-28), receipts, and a store walkthrough (2026-07-22). Interviews covered all 7 staff, the marketing freelancer, and the MSP technician.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**, except the two AI offer rows (G-072, G-073), which use the P10 test of 2026-08-25. Actions completed later are noted in the remediation column but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 0 | 0 | 5 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 1 | 1 | 3 |
| PCI Req 3 Stored account data | 2 | 1 | 1 | 3 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 1 | 1 | 2 | 4 |
| PCI Req 6 Secure systems and software | 2 | 1 | 4 | 0 | 7 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 2 | 3 | 0 | 6 |
| PCI Req 9 Physical access and terminals | 1 | 0 | 2 | 2 | 5 |
| PCI Req 10 Logging | 0 | 0 | 0 | 7 | 7 |
| PCI Req 11 Security testing | 0 | 1 | 2 | 3 | 6 |
| PCI Req 12 Policies and programs | 0 | 1 | 6 | 3 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **7** | **10** | **22** | **29** | **68** |
| FTC Act Section 5 | 0 | 4 | 1 | 0 | 5 |
| FACTA receipt truncation | 1 | 0 | 0 | 0 | 1 |
| **Total (74)** | **8** | **14** | **23** | **29** | **74** |

Of the 37 rows with gaps, 6 are rated High, 16 Moderate, and 15 Low.

**What the numbers say.** What the provider does is strong: P2PE, the hosted card fields, platform patching, and the web application firewall are all Met or inherited. What the store does is mostly missing: no written policies, no scope document, no terminal checks, no training, and no incident plan. That is typical of a 7-person business that bought a good platform and assumed it covered everything. Most Not met rows need a page of procedure, not new technology.

## 4. Priority gaps and roadmap
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Mobile reader outside P2PE; no scope document; 2025 SAQs attested without evidence | G-060 (12.5) | High | Retire the reader; scope and data-flow document; evidence for each SAQ answer | Owner | 2026-11-30 |
| Payment page scripts not managed | G-027 (6.4.3) | High | Remove store-added scripts from checkout; approved script list; provider checkout script restriction | Store Manager | 2026-10-15 |
| No payment page change and tamper detection | G-055 (11.6.1) | High | Monitoring service with alerts; frequency set by a targeted risk analysis | Store Manager | 2026-11-15 |
| Two administrator logins without MFA | G-035 (8.4) | High | MFA on every dashboard and online store login | Store Manager | 2026-10-15 |
| No incident response plan | G-065 (12.10) | High | POL-03 and P08 runbook (approved 2026-08-31); wallet cards; tabletop | Store Manager | 2026-11-30 |
| Security program not yet reasonable for customer data | G-071 (FTC 45(n)) | High | P01 treatments and P07 POA&M | Store Manager | 2026-12-31 |
| No terminal list, inspections, or tamper training | G-042 (9.5) | Moderate | Terminal list; daily inspection log; training | Store Manager | 2026-10-15 |
| Shared cashier code; leaver not removed | G-033 (8.2) | Moderate | Personal codes; last-day checklist; monthly review | Store Manager | 2026-09-30 |
| No service provider management | G-063 (12.8) | Moderate | Provider list and responsibility matrix; freelancer agreement; yearly AOC check | Bookkeeper | 2026-11-30 |
| No change control on the online store | G-028 (6.5) | Moderate | Store Manager approves and logs every custom code change | Store Manager | 2026-09-30 |
| Privacy notice does not match practice | G-069 (FTC 45(a)(1)) | Moderate | Rewrite notice | Owner | 2026-10-31 |
| AI offer and markdown claims unsubstantiated | G-072 (FTC 45(a)(1)) | Moderate | Claims checklist and campaign records (P10) | Owner | 2026-10-31 |

**Before signing the 2026 SAQs (due 2026-11-30):** close G-060, G-027, G-055, and G-035, keep evidence for the SAQ A script-attack statement, and keep the terminal list and inspection logs for SAQ P2PE 9.5. If the mobile reader is still in use on that date, the Owner should not sign SAQ P2PE and should ask the provider how the store must validate.

**Remediation phases:**
| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Quick fixes | 2026-09-30 | Card data rule; delete the emailed card number and the loyalty export; personal POS codes and last-day checklist; change control and custom code review; policies published and acknowledged | G-009, G-010, G-022, G-023, G-028, G-029, G-032, G-033, G-056, G-057 |
| 2. Payment page and access | 2026-10-15 | Scripts off checkout; app clean-up; MFA everywhere; least-privilege roles; terminal list, inspections, and training; accurate security claim | G-007, G-024, G-027, G-030, G-034, G-035, G-037, G-038, G-042, G-070 |
| 3. Training, notice, and claims | 2026-10-31 | Awareness and phishing training; anti-phishing process; rewritten privacy notice; offer claims checklist and fairness check | G-016, G-017, G-018, G-021, G-061, G-069, G-072, G-073 |
| 4. Monitoring and scope | 2026-11-30 | Payment page monitoring; targeted risk analyses; configuration standard; service provider list and scanning responsibility; scope document and SAQ evidence; incident tabletop | G-006, G-050, G-052, G-055, G-058, G-060, G-063, G-065 |
| 5. Program | 2026-12-31 | Remaining P01 treatments and P07 POA&M items | G-071 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June-July 2026) toward the next version. The analysis will be updated when a new version is published.
- **FTC.** No pending FTC rule changes the store's duties. The FTC's 2024 surveillance pricing 6(b) study is a study, not a rule, but it shows FTC interest in prices or offers set from personal data (P10).
- None of these is treated as a current obligation.
