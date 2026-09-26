# Regulatory Gap Analysis: Cris Santos Company | Retail Trade | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| Tier / Vertical | Small / Retail Trade |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N44-45-R01) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) (N44-45-R02), plus a one-row check of FACTA receipt truncation, 15 U.S.C. 1681c(g) (N44-45-R05) |
| Assessment dates | 2026-07-20 to 2026-07-31; evidence refreshed with P07 and P10 results through 2026-08-28 |
| Assessor | IT Manager (Information Security Lead) with the Controller and the E-commerce and Marketing Manager |
| Approved | General Manager, 2026-09-04 |

## 1. Applicability
**PCI DSS applies by contract.** The company accepts payment cards, and its merchant agreement requires PCI DSS compliance. PCI SSC sets no size tiers. Merchant levels and validation rules come from the card brands and the acquirer. In a letter dated 2026-06-15 (fictional), **the acquirer confirmed the validation type**: an annual self-assessment using **SAQ P2PE** for the store and **SAQ A** for the online channel, due 2026-11-30. This analysis does not state brand level thresholds, because they were not verified from a card brand source.

**Why the company's PCI scope is small (scope reduction reasoning):**
- **In store, validated P2PE.** Cards are read only by PIN pads that belong to a point-to-point encryption solution validated and listed by the PCI SSC. The card data is encrypted inside the device, and only the solution provider can decrypt it. Registers, the POS back office, and the store network therefore handle only encrypted data and are not part of a cardholder data environment (CDE). Three conditions keep this true: the P2PE Instruction Manual is followed, PIN pads are inspected for tampering (Requirement 9.5), and card numbers can be entered **only** on the PIN pads. Manual card entry on register keyboards is disabled today, and that setting must stay locked (P01 R-006).
- **Online, the processor's embedded payment form.** The checkout page shows a payment form served by the processor inside an inline frame. Card data goes from the customer's browser directly to the processor, and the storefront receives a token. **The page around the form is still in scope in practice:** a malicious script on that page can overlay or read the form. This is why PCI DSS v4.0.1 Requirements **6.4.3** (manage payment page scripts) and **11.6.1** (detect changes and tampering on payment pages) matter here.
- **SAQ A eligibility.** Since the January 2025 SAQ A revision (effective 2025-03-31), SAQ A no longer lists 6.4.3 and 11.6.1. Instead, a merchant whose page embeds a processor's form must confirm that its site is **not susceptible to attacks from scripts** that could affect its e-commerce systems. PCI SSC FAQ 1588 says a merchant can confirm this by using techniques such as those in 6.4.3 and 11.6.1, or by getting confirmation from its compliant processor that the processor's solution protects the merchant's page. PCI SSC states that the revision does not remove or weaken the underlying requirements. **The 2025 SAQ A was signed with this criterion checked but with no evidence.** That is the most important finding of this analysis.

**Rows marked Not applicable** (28) fall into three groups:
- requirements for CDE networks and systems the company does not have, because of P2PE and the embedded form (Requirements 1, 5.2-5.3, 9.2-9.3, 10, 11.2, 11.4-11.5);
- requirements with nothing to protect because no card data or keys are stored (3.5-3.7);
- requirements for service providers or special designations only (12.4, 12.9, Appendices A1-A3).

Not applicable to PCI does not mean unneeded. Network separation, anti-malware, and log review are still part of reasonable security under FTC Act Section 5 (row G-071) and appear in P01 and P07.

**Secondary regulation.** FTC Act Section 5 applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)). It may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits to consumers or competition (45(n)). This matters for loyalty data and for the pricing engine (P10). FACTA receipt truncation applies to any business that accepts cards and was checked in one row.

**Not applicable, with reasons:** FTC Safeguards Rule and Red Flags Rule (no store credit or covered accounts), CCPA (no California business and revenue below $26,625,000), COPPA (members are 18 or older and the site is not directed to children), INFORM Consumers Act (no third-party sellers), SEC disclosure (privately held), and HIPAA (no pharmacy). Florida breach notification (Fla. Stat. 501.171) is handled in P08.

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their requirement groups (for example 8.2). The two payment-page requirements were taken to the defined-requirement level (6.4.3 and 11.6.1), and 6.4 was split into its three defined requirements. The appendices were added. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard. The numbering of 6.4.3 and 11.6.1 and the SAQ A change were confirmed on PCI SSC pages (blog posts dated 2025-01-30, 2025-02-28, and 2025-03-10). The other group numbers come from the company's licensed copy of v4.0.1.
2. **FTC and FACTA rows** cite the statute text, verified on uscode.house.gov (15 U.S.C. 45(a)(1), 45(n)).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Interviews (majority owner, General Manager, Controller, E-commerce and Marketing Manager, Store Manager, marketing contractor), document review (2025 SAQs, merchant agreement, acquirer letter, vendor AOCs and SOC 2 reports), configuration exports, a browser capture of the checkout page on 2026-07-28, a mailbox search, and a store walkthrough on 2026-07-22.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

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
| PCI Req 9 Physical access and PIN pads | 1 | 1 | 1 | 2 | 5 |
| PCI Req 10 Logging | 0 | 0 | 0 | 7 | 7 |
| PCI Req 11 Security testing | 0 | 1 | 2 | 3 | 6 |
| PCI Req 12 Policies and programs | 1 | 5 | 2 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **8** | **15** | **17** | **28** | **68** |
| FTC Act Section 5 | 0 | 4 | 2 | 0 | 6 |
| FACTA receipt truncation | 1 | 0 | 0 | 0 | 1 |
| **Total (75)** | **9** | **19** | **19** | **28** | **75** |

Of the 38 rows with gaps, 6 are rated High, 20 Moderate, and 12 Low.

## 4. Priority gaps and roadmap
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Payment page scripts not managed | G-027 (6.4.3) | High | Script inventory with justification and approval; integrity settings; tag manager off checkout | E-commerce and Marketing Manager | 2026-11-15 |
| No payment page change and tamper detection | G-055 (11.6.1) | High | Monitoring service with alerts; frequency set by targeted risk analysis | E-commerce and Marketing Manager | 2026-11-15 |
| Two storefront administrator accounts without MFA | G-035 (8.4) | High | Contractor to single sign-on with MFA; delete legacy account | IT Manager | 2026-10-15 |
| No PCI scope document; 2025 SAQs attested without evidence | G-060 (12.5) | High | Scope and data-flow document; evidence file for each SAQ answer | Controller | 2026-11-30 |
| No incident response plan | G-065 (12.10) | High | POL-03 and P08 runbook; tabletop | IT Manager | 2026-11-30 |
| Security program not yet reasonable for loyalty data | G-071 (FTC 45(n)) | High | P01 treatments and P07 POA&M | IT Manager | 2027-01-31 |
| Former employees active; shared legacy account | G-033 (8.2) | Moderate | Same-day removal; quarterly review | HR and Payroll Specialist | 2026-10-31 |
| No change control on the checkout page | G-028 (6.5) | Moderate | Change request and approval for theme and tag changes | E-commerce and Marketing Manager | 2026-11-15 |
| PIN pad inspections not recorded | G-042 (9.5) | Moderate | Reconcile inventory; inspection logs; training | Store Manager | 2026-10-15 |
| Service provider management incomplete | G-063 (12.8) | Moderate | Provider list, responsibility matrix, annual AOC check | Controller | 2026-11-30 |
| Privacy notice does not match data sharing | G-069 (FTC 45(a)(1)) | Moderate | Rewrite notice | E-commerce and Marketing Manager | 2026-10-31 |
| Online price-match banner is inaccurate | G-072 (FTC 45(a)(1)) | Moderate | Correct the banner; substantiation file | E-commerce and Marketing Manager | 2026-10-31 |

**Before signing the 2026 SAQs (due 2026-11-30):** close G-027, G-055, G-035, and G-060, and keep evidence for the SAQ A script-attack eligibility criterion. Otherwise the company should not check that criterion again, and should ask the acquirer how to validate the online channel.

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June-July 2026) toward the next version. The analysis will be updated when a new version is published.
- **FTC.** A proposed FTC policy statement on AI accuracy (Docket FTC-2026-0727, July 2026) is not final. The FTC's 2024 surveillance pricing 6(b) study produced staff research summaries in January 2025. It is a study, not a rule, but it shows the FTC's interest in individualized pricing based on personal data (P10).
- None of these is treated as a current obligation.
