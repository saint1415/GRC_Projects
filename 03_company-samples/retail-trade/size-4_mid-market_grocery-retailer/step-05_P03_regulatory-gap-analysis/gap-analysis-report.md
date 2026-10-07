# Regulatory Gap Analysis: Cris Santos Company | Retail Trade | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through the merchant agreement, **not law** (N44-45-R01) |
| Other rules for the primary business line | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n) (N44-45-R02); FACTA receipt truncation, 15 U.S.C. 1681c(g) (N44-45-R05); Florida Information Protection Act reasonable security and disposal duties, Fla. Stat. 501.171(2) and (8) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 and P10 results through 2026-09-04 |
| Assessor | Security Manager and the GRC analyst, with the Privacy and Compliance Manager and the vCISO; reviewed by the co-sourced internal audit firm. This is the company's own readiness work before the QSA's assessment in October and November 2026 |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** grocery retailing in 5 Florida stores and online, with card, SNAP EBT, and catering payments.

| Rule | Applies? | Basis |
|---|---|---|
| PCI DSS v4.0.1 | **Yes, by contract** | The company accepts payment cards, and its merchant agreement requires PCI DSS compliance. PCI SSC sets no size tiers; merchant levels and validation rules come from the card brands and the acquirer. In a letter dated 2026-05-15 (fictional), the acquirer confirmed the company's level under its program and the validation it requires: an annual **SAQ D for Merchants** prepared with a QSA firm and signed by the Chief Financial Officer, plus quarterly ASV scans. This analysis does not restate brand level thresholds, because they were not verified from a card brand source. Visa's public compliance page confirms that a merchant's level is based on its total Visa transaction volume over 12 months and that acquirers must make sure merchants validate at the right level (usa.visa.com, checked 2026-10-04) |
| FTC Act Section 5 | **Yes** | No size threshold. Deception (45(a)(1)) covers privacy, security, and pricing claims; unfairness (45(n)) covers practices that cause or are likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits |
| FACTA receipt truncation | **Yes** | Any business that accepts cards. Checked in one row |
| Fla. Stat. 501.171(2) and (8) | **Yes** | The company is a covered entity that maintains personal information of Florida residents. Subsection (2) requires reasonable measures to protect and secure electronic personal information; subsection (8) requires disposal by shredding, erasing, or otherwise making records unreadable. Breach notice duties (subsections (3) to (6)) are handled in P08 |

**Why the company's PCI scope is large (and how it will shrink):**
- **In store, encryption that is not P2PE-validated.** The PIN pads are PCI-approved devices and encrypt card data at the moment of reading with the processor's service. That service is not on the PCI SSC list of validated P2PE solutions, so the QSA treats the registers, store POS servers, store POS VLANs, and the POS head-office application as the CDE. That is why Requirements 1, 5, 10, and 11 apply in full here, unlike in a P2PE store. **Roadmap:** the 2027 terminal refresh moves the stores to a validated P2PE solution, which would take the registers and store servers out of scope if the P2PE Instruction Manual is followed (P01 R-003).
- **Online, the processor's hosted payment fields.** Card data goes from the browser or app straight to the processor, and the e-commerce platform receives a token. The checkout pages that host the fields are still in scope for **6.4.3** (manage payment page scripts) and **11.6.1** (detect changes and tampering), because a malicious script on the page can capture what customers type.
- **Service-desk virtual terminal.** Catering phone orders are keyed into the processor's virtual terminal on 5 service-desk PCs, which brings those PCs into scope.
- **SAQ D, not SAQ A.** The January 2025 SAQ A revision (effective 2025-03-31) changed how SAQ A merchants report the script requirements. It does not affect this company, which validates all channels with SAQ D, where 6.4.3 and 11.6.1 are assessed directly.

**Rows marked Not applicable (8):** requirements for keys the company does not hold (3.6, 3.7); wireless networks connected to the CDE (2.3; none exist); service-provider-only groups (12.4, 12.9); and Appendices A1 to A3.

**Other retail rules, decided at this size:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Safeguards Rule, 16 CFR Part 314 (N44-45-R03) | No | The company issues no store credit card, offers no deferred payment, and does not cash checks or sell money services, so it is not a financial institution under Part 314 |
| FTC Red Flags Rule, 16 CFR 681.1 (N44-45-R04) | No | No covered accounts (no credit extended) |
| CCPA and CPPA regulations (N44-45-R06) | No | Revenue (about $100 million) exceeds the $26,625,000 threshold, but the company does not do business in California. Recheck before any expansion of online sales outside Florida |
| COPPA Rule, 16 CFR Part 312 (N44-45-R07) | No | The website and app are not directed to children; loyalty members must be 18 or older |
| INFORM Consumers Act, 15 U.S.C. 45f (N44-45-R08) | No | The company does not operate an online marketplace. On the delivery marketplace it is a seller; collecting and verifying seller information is the marketplace's duty |
| Florida Digital Bill of Rights, Fla. Stat. 501.701 et seq. | No | A "controller" must have more than $1 billion in global gross annual revenue and meet other criteria (Fla. Stat. 501.702, verified on the Florida Legislature site) |
| SNAP retailer rules, 7 CFR Part 278 | Yes, as an operating authorization | All 5 stores are FNS-authorized (7 CFR 278.1, 278.2). A review of Part 278 (eCFR, 2026-09-23 version) found no cybersecurity control requirements for retailers. EBT skimming risk is handled through PIN pad controls (row 9.5; P01 R-049) |
| HIPAA | No | No pharmacy (owners' decision) |
| SEC disclosure rules | No | Privately held |

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their requirement groups (for example 8.2). The payment page requirements were taken to the defined-requirement level (6.4.1 to 6.4.3 and 11.6.1). Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; read the requirement text in the official standard. Requirement numbers used in this analysis were checked against the company's licensed copy and against the public PCI SSC self-assessment questionnaires (SAQ A, SAQ C-VT, and SAQ P2PE for v4.0), which list, among others, 1.3, 1.5, 2.2, 2.3, 3.3, 3.4, 5.2 to 5.4, 6.3, 6.4.3, 8.2 to 8.4, 9.4, 9.5.1, 11.3.2, 11.6.1, 12.1, 12.6, 12.8, and 12.10.
2. **FTC, FACTA, and Florida rows** cite statute text, verified on uscode.house.gov (15 U.S.C. 45(a)(1), 45(n), 1681c(g)) and on the Florida Legislature site (Fla. Stat. 501.171(2), (8); 501.702).
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Interviews with the Chief Financial Officer, IT Director, Director of E-commerce and Marketing, Director of Store Operations, Director of Fresh Departments, the 5 Store Managers, and the marketing agency; document review (2025 SAQ D and AOC, merchant agreement, acquirer letter, TPSP AOCs, contracts); configuration exports; browser captures of the website and app checkouts on 2026-07-22; a data discovery scan of file services and mailboxes on 2026-07-21; and walkthroughs at all 5 stores from 2026-07-20 to 2026-07-24.
5. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, with sizes from the co-sourced internal audit firm's attribute sampling table (25 items for a moderate-risk control operating many times a year):
   - terminations: 25 of 268; transfers: 25 of 85;
   - checkout page publishes: 20 of 64 in Q2 2026;
   - checkout scripts: 23 of 23; PIN pads: 65 of 65 reconciled; inspection logs: 13 weeks at 5 stores;
   - critical POS patches: 12 of 12 released in the last 12 months;
   - receipts: 40 across 5 stores (lanes, self-checkouts, catering);
   - TPSP AOCs: 14 of 14; hires in sensitive roles: 25 of 25;
   - store servers: 5 of 5 benchmark-scanned; registers: 10 of 65.
   Each `evidence` cell names the sample and its result.
6. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 2 | 2 | 1 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 1 | 1 | 3 |
| PCI Req 3 Stored account data | 2 | 1 | 2 | 2 | 7 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 2 | 2 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 2 | 2 | 3 | 0 | 7 |
| PCI Req 7 Restrict access | 2 | 1 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 2 | 2 | 2 | 0 | 6 |
| PCI Req 9 Physical access and PIN pads | 1 | 3 | 1 | 0 | 5 |
| PCI Req 10 Logging and monitoring | 1 | 3 | 3 | 0 | 7 |
| PCI Req 11 Security testing | 1 | 4 | 1 | 0 | 6 |
| PCI Req 12 Policies and programs | 3 | 4 | 1 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **19** | **26** | **15** | **8** | **68** |
| FTC Act Section 5 | 0 | 5 | 1 | 0 | 6 |
| FACTA receipt truncation | 1 | 0 | 0 | 0 | 1 |
| Florida Information Protection Act (501.171(2), (8)) | 0 | 2 | 0 | 0 | 2 |
| **Total (77)** | **20** | **33** | **16** | **8** | **77** |

**Gap risk ratings (49 rows Partially met or Not met):** 15 High, 26 Moderate, 8 Low.

**Reading the results.** The company has a defined program and passes its external scans, but its 2025 SAQ D overstated readiness in three places the QSA will test closely:
- **the store CDE:** logs are not collected or reviewed (10.2, 10.4, 10.5), vendor access is shared and lacks MFA (8.2, 8.4), and an unmanaged vendor modem opened a path from the internet (1.4);
- **the checkout pages:** scripts are not managed and the app checkout is not monitored (6.4.3, 11.6.1);
- **card data outside the payment systems:** catering forms with security codes (3.2, 3.3, 9.4).

The scope document has not been confirmed since the cloud move (12.5), which the QSA will ask for first.

## 4. Priority gaps
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Untrusted vendor modem into the CDE | G-004 (1.4) | High | Sweep all stores; contract ban on unapproved connections | IT Director | 2026-10-31 |
| Scope not confirmed since the cloud move | G-060 (12.5) | High | Updated scope and data-flow document | IT Director | 2026-10-15 |
| Security codes and card numbers on catering forms | G-010, G-011 (3.2, 3.3) | High | Destroy forms; new catering payment procedure | Director of Fresh Departments | 2026-10-31 |
| Payment page scripts not managed | G-027 (6.4.3) | High | Inventory, justification, integrity values; tag manager off checkout | Director of E-commerce and Marketing | 2026-11-15 |
| App checkout not monitored | G-055 (11.6.1) | High | Extend tamper detection; targeted risk analysis | Director of E-commerce and Marketing | 2026-11-15 |
| Shared vendor and virtual terminal accounts; terminated users | G-033 (8.2) | High | Named accounts; POS accounts tied to the HR feed | IT Director | 2026-12-31 |
| No MFA for agency and POS vendor access | G-035 (8.4) | High | Single sign-on and the access broker with MFA | Security Manager | 2026-12-31 |
| CDE logs not collected or reviewed | G-044, G-046 (10.2, 10.4) | High | SIEM onboarding with daily automated review | Security Manager | 2026-11-30 |
| No internal or segmentation penetration test | G-053 (11.4) | High | Test before QSA fieldwork | Security Manager | 2026-10-16 |
| CDE configuration below baseline | G-007 (2.2) | High | STD-01 baselines; default-credential sweep | Security Manager | 2027-01-31 |
| TPSP management incomplete | G-063 (12.8) | High | List, matrix, annual AOC tracking, contract terms | Privacy and Compliance Manager | 2026-12-31 |
| Privacy notice does not match data sharing | G-069 (FTC 45(a)(1)) | High | Pause pilot; rewrite notice; review gate | General Counsel | 2026-11-30 |
| Security program not yet reasonable for loyalty data | G-071 (FTC 45(a)(1), 45(n)) | High | P01 treatments and P07 POA&M | IT Director | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

**Before the CFO signs the 2026 AOC (due 2026-12-31):** close G-004, G-010, G-011, G-027, G-044, G-046, G-053, and G-060, and show progress on G-033 and G-035. If any of these is still open when the QSA finishes fieldwork on 2026-11-20, the company should not attest to full compliance. It should discuss with the acquirer whether to report the open items with a remediation plan, as the acquirer's program allows.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Before the QSA** | 2026 Q4 (to 2026-11-20) | Scope document; store device sweep; catering procedure; script inventory and app checkout monitoring; CDE logs in the SIEM; internal and segmentation penetration test; privacy notice rewrite | G-004, G-010, G-011, G-027, G-044, G-046, G-053, G-055, G-060, G-069 |
| **2. Vendor and access** | 2026 Q4 to 2027 Q1 | Named, brokered vendor access with MFA; POS accounts from the HR feed; TPSP program; credential vaulting | G-033, G-035, G-037, G-063 |
| **3. Baselines and testing** | 2027 Q1 | STD-01 and STD-02 issued; register and store server baselines; quarterly internal scans; file change-detection | G-007, G-043, G-052, G-054 |
| **4. Shrink the scope** | 2027 Q2 to Q3 | Validated P2PE at the terminal refresh (completion 2027-09-30); dedicated virtual terminal PCs or PIN pad payment for catering; SOC 2 observation period for the supplier offers service (P09) | Reduces Requirements 1, 5, 10, 11 scope in stores |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June to July 2026) toward the next version. The analysis will be updated when a new version is published.
- **FTC.** A proposed FTC policy statement on AI accuracy (Docket FTC-2026-0727, July 2026) is not final. It is relevant to the chatbot and pricing tools in P10 but is not treated as a current obligation.
- **State privacy laws.** If online sales or stores expand beyond Florida, recheck state comprehensive privacy laws (for example, thresholds based on consumer counts in other states) and the CCPA.
- None of these is treated as a current obligation.
