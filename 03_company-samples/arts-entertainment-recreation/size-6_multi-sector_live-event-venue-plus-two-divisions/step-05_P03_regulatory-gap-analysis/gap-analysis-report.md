# Regulatory Gap Analysis: Cris Santos Company Holdings | Arts, Entertainment, and Recreation | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Arts, Entertainment, and Recreation (focus division: Live Venues) |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024). A contractual standard enforced through merchant and client agreements, **not law** (N71-R04; N72-R01 for the hotels division) |
| Division obligations | Live Venues: PCI DSS as a Level 1 merchant, plus the FTC fee rule, FTC Act Section 5, ADA ticketing rules, and the BOTS Act. Hotels and Restaurants: PCI DSS as a merchant, the fee rule for lodging, FTC Act, Florida guest register. Ticketing and Streaming: PCI DSS as a service provider, SOC 2 commitments, FTC Act, CCPA, DOJ Data Security Program, and the group's SEC duties |
| Gap tables | `gap-analysis.csv` (Live Venues, 81 rows); `gap-analysis-hotels-restaurants.csv` (34 rows); `gap-analysis-ticketing-streaming.csv` (48 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads, coordinated by the Group PCI program director and the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv), with one row per requirement for each division and the group. This section restates the results for the rules analyzed here.

### 1.1 Three PCI DSS roles in one group
PCI SSC sets no size tiers. Merchant levels and validation methods come from the card brands and each acquirer. Visa's *What To Do If Compromised* (v10.0, effective 2026-06-25) lists Visa merchant levels by annual Visa transactions: **Level 1, more than 6,000,000; Level 2, 1,000,001 to 6,000,000; Level 3, 1 to 1,000,000**. Other brands' levels were not verified; each acquirer applies them.

| Division | PCI role | Volume (fictional) | Validation (acquirer or client requirement) |
|---|---|---|---|
| Live Venues | Merchant of record for its tickets, food and beverage, parking, and merchandise | About 61 million card transactions a year, about 33 million Visa: **Visa Level 1** | Annual **ROC by a QSA** and quarterly ASV scans (acquirer letter 2026-04-15). 2026 ROC due 2026-11-30 |
| Hotels and Restaurants | Merchant of record for rooms and dining | About 24 million transactions, about 5.4 million Visa: **Visa Level 2** | **SAQ D for Merchants** with quarterly ASV scans (acquirer letter 2026-04-15). Due 2026-12-31 |
| Ticketing and Streaming | **Service provider** to 1,150 clients and to the two group merchants (the TVOP stores, processes, and transmits their card data); also merchant of record for streaming | About 4.6 million streaming transactions | Service provider **ROC by a QSA** (AOC 2026-03-31), required by acquirers and client agreements. The streaming acquirer accepts that ROC for the streaming channel |

**Why this matters.** The TVOP is a third-party service provider to its own sister divisions. Live Venues and Hotels and Restaurants must manage it under Requirement 12.8 like any outside provider, and the TVOP owes them the Requirement 12.9 acknowledgments it owes outside clients. Where a merchant adds content to the TVOP's hosted payment page (tags through the tag manager), that content is the merchant's responsibility under 6.4.3 and 11.6.1, and the platform's responsibility as the host of the page. Both sides have a gap.

**Scope by channel (Live Venues).**
| Channel | How card data flows | Scope effect |
|---|---|---|
| Online and mobile ticket sales (TVOP) | Hosted payment fields on the TVOP; tokens back to Live Venues | Live Venues relies on the TVOP AOC; **tags Live Venues adds to checkout pages are in its scope** (G-027, G-055) |
| Box office at 30 integrated venues | Validated P2PE devices | Reduced scope: device inspections and P2PE instruction manual (9.5) |
| Food, beverage, merchandise at 30 venues | Validated P2PE devices (about 5,900) | Reduced scope as above |
| **8 acquired theaters** | Seller's ticketing SaaS and a legacy POS with about 410 non-P2PE terminals on flat networks; full card numbers in a local database | **Full scope.** Not in the 2025 scope document (G-060). Most Partially met PCI rows trace here |

### 1.2 The scope decision for the 2026 Live Venues ROC (for the Group CISO by 2026-10-15)
| Option | What it takes | 2026 result |
|---|---|---|
| **A. Assess the theaters as they are** | The QSA assesses the theater environments in the 2026 ROC | Not in Place findings on many requirements; a Non-Compliant ROC and an action plan for the acquirer |
| **B. Interim fix, then assess (recommended)** | By 2026-11-15: purge stored card numbers; replace the about 410 terminals with the group's validated P2PE devices on standalone connections; EDR and log forwarding on remaining theater systems; add theater addresses to ASV scans | The theaters' card channels become P2PE channels with reduced scope. Still needs the acquirer's agreement to the timing; migration to the TVOP follows by 2027-03-31 |

Option B costs about $1.4 million (fictional), mainly devices and installation. **It does not remove the theaters from the security program.** Segmentation, EDR, logging, and patching remain needed for reasonable security under FTC Act Section 5 and state law (G-069, G-081). Rows affected carry a scope note in `pending_rule_change`.

### 1.3 Secondary rules
- **FTC Act Section 5** applies to every division with no size threshold: deception (45(a)(1)) and unfairness (45(n)).
- **Rule on Unfair or Deceptive Fees, 16 CFR Part 464** (effective 2025-05-12). Its "covered good or service" means live-event tickets and short-term lodging (464.1), so it reaches **two divisions**: Live Venues (tickets) and Hotels and Restaurants (rooms, including the $32 resort fee at 9 venue hotels). Any price offered, displayed, or advertised must include the total price (464.2(a)), more prominently than other pricing (464.2(b)); excluded charges and the final amount must be disclosed before payment (464.2(c)); fees must not be misrepresented (464.3). The TVOP renders checkout prices for all tenants, so its product design also matters for clients.
- **ADA Title III ticketing, 28 CFR 36.302(f).** Accessible seating must be available during the same hours, stages of sale, and methods of distribution (36.302(f)(1)(ii)); its price may not be set higher than other tickets in the same seating section, and it must be available at all price levels (36.302(f)(3)); where more than four tickets may be bought, patrons with disabilities may buy the same number (36.302(f)(4)(iv)).
- **BOTS Act, 15 U.S.C. 45c.** It makes it unlawful to circumvent a security measure or access control system a ticket issuer uses to enforce posted purchase limits or online purchasing order rules, and to sell tickets obtained that way (45c(a)(1)). A "ticket issuer" may include the operator of the venue, the promoter of an event, and an agent for any such person; an "event" takes place in a venue with capacity over 200. Live Venues is a ticket issuer and the TVOP acts as its agent. The Act places no compliance duty on the group; bot detection records are evidence (P10).
- **Fla. Stat. 817.36** (worked example): 817.36(5) provides a civil penalty for intentionally using or selling software to circumvent a ticket seller's security measures. The resale limits bind resellers, not the group.

### 1.4 Excluded requirements, with reasons
- **Nevada Reg. 5.260, NIGC MICS, and casino BSA/AML (N71-R01 to R03):** no division conducts gaming or holds a gaming license.
- **COPPA (N71-R06, N51-R02):** all services are general audience and accounts require age 18 or older.
- **FedRAMP (N51-R07), FCC CPNI (N51-R06), PADFA (N51-R05):** no federal customers; not a carrier; not a data broker.
- **Illinois BIPA (N72-R05):** the hotels division collects no biometric identifiers, and the current text was not verified. The Live Venues face entry pilot runs at 2 Florida amphitheaters (P10).
- **CIRCIA (N72-R06):** proposed only; no final rule published as of 2026-09-25.

## 2. Regulation-by-division matrix
| Requirement | Live Venues | Hotels and Restaurants | Ticketing and Streaming | Group (corporate) |
|---|---|---|---|---|
| N71-R04 / N72-R01 PCI DSS v4.0.1 | **Primary.** Level 1 merchant, ROC | Applies. Level 2 merchant, SAQ D | Applies. **Service provider** ROC; Appendix A1 (multi-tenant); streaming merchant | Common controls carved into all three validations |
| N71-R05 / N72-R02 / N51-R01 FTC Act Section 5 | Applies (security, privacy notice, posted limits) | Applies (FTC v. Wyndham, 3d Cir. 2015) | Applies (security and client data statements) | Applies |
| 16 CFR Part 464 (fees) | **Applies** (live-event tickets) | **Applies** (short-term lodging) | Product duty: the TVOP renders prices for all tenants | Group General Counsel owns the price display standard |
| 28 CFR 36.302(f) ADA ticketing | **Applies** (venues; pricing and bot modules) | Not applicable (no ticketing; ADA lodging rules outside this analysis) | Product duty for client tenants (pricing and bot modules) | Group AI standard (P10) |
| BOTS Act 15 U.S.C. 45c; Fla. Stat. 817.36 | Protects (ticket issuer) | Not applicable | Protects (agent of ticket issuers) | n/a |
| N72-R03 FTC Disposal Rule | Applies (background checks; shared HR) | Applies | Applies | Group HR |
| Fla. Stat. 509.101(2) guest register | Not applicable | **Applies** (Florida hotels) | Not applicable | n/a |
| N72-R04 State breach notification laws | Each state where affected individuals reside (Florida worked example: 501.171) | Same | Same, plus third-party agent duties to clients (501.171(6)) | Coordinates (P08) |
| N51-R03 CCPA and CPPA regulations | Applies via the group (business) | Applies via the group | Service provider to client businesses; cybersecurity audit first report due 2028-04-01 | **Applies** (business; revenue above threshold) |
| N51-R04 DOJ Data Security Program | Applies (covered personal identifiers above bulk threshold) | Applies | Applies (vendor screening) | Group vendor screening |
| N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| SOC 2 (contractual) | Not in scope (P09) | Not in scope (P09) | Annual Type 2 (P09) | Group services carved in |
| N71-R01 to R03 gaming; N71-R06 / N51-R02 COPPA; N51-R05 to R07; N72-R05; N72-R06 | Not applicable | Not applicable | Not applicable | Not applicable |

## 3. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and requirement groups (for example 8.2). Requirements that decide scope or carry the largest risk were taken to the defined-requirement level (6.4.1, 6.4.2, 6.4.3, 11.6.1), and the service-provider-only requirements were added for the TVOP (for example 3.6.1.1, 11.4.6, 11.4.7, 11.5.1.1, 12.4.2, 12.5.2.1, 12.9.1, 12.9.2). Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; read the requirement text in the group's licensed copy of v4.0.1. No newer PCI DSS version was found on the PCI SSC standards page as of 2026-09-26.
2. **Law rows** cite text read on uscode.house.gov (15 U.S.C. 45, 45c), the eCFR as of 2026-09-23 (16 CFR Part 464, 28 CFR 36.302(f)), and the Florida Legislature's 2026 statutes. SOC 2 rows list criterion IDs only.
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1, Part 464, or the AICPA criteria to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Current state was established from the intake evidence (EV-001 to EV-074: configuration exports, the 2025 ROC, the 2026 service provider ROC and AOC, acquirer letters, client agreements, scope documents, and the SOC 2 report), gap analysis interviews with each division (EV-087 Live Venues, EV-088 Hotels and Restaurants, EV-089 Ticketing and Streaming), hotel network walks (EV-085), the Live Venues supplement v2026 (EV-086), the TVOP scope confirmation and QSA comments (EV-090), channel audits of hotel rates (EV-091), price display and on-sale captures (EV-092, EV-093), the acquired theater POS review (EV-094), the July segmentation test (EV-095), hotel mailbox scans on 2026-07-20 (EV-096, with the purge record EV-099), a checkout scan of all tenants on 2026-07-21 (EV-097), card data discovery scans at the acquired theaters on 2026-07-22 (EV-098), pricing logs for 40 sampled events and on-sale tests from the P10 fieldwork (EV-101, EV-102), and P07 test results. The `evidence` column in each gap table cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 4. Results
### 4.0 Group gaps
Seven gaps cross divisions or sit in shared services. They are numbered here and cited as group gaps 1 to 7 across this sample.
1. **Checkout script control at platform scale.** The hosted checkout loads platform scripts and the tags tenants add through the tag manager. The script inventory and change-and-tamper detection cover the 14 platform scripts only; tenant-added tags (23 on group venue checkout pages, and tags on the payment pages of 641 client tenants) are not inventoried, authorized, or monitored (EV-049, EV-065, EV-097; P07 CM-8, SI-7).
2. **Acquired theaters.** The 8 theaters acquired in 2025-10 still run the seller's ticketing system and a POS with about 410 non-P2PE terminals on flat networks, outside the group PCI scope document, the SOC, and SYS-G1. Migration is due 2027-03-31 (EV-044, EV-050, EV-094, EV-098; P07 SC-7).
3. **Patron data platform purpose and minimization.** SYS-G4 combines ticketing, hotel, dining, and streaming profiles. Purposes and notices differ by division, the nightly hotel export copies identity document numbers that no use needs, and a TVOP feed brings all tenants' purchaser data for model training (EV-037, EV-038, EV-039, EV-055).
4. **AI in pricing and access decisions.** Dynamic pricing and bot detection run for group venues and client tenants without group AI approval, accessible seating parity controls, or bias measurement, and the face-based express entry pilot started at 2 amphitheaters without a privacy review (EV-035, EV-072, EV-084; P10 EV-101 to EV-103).
5. **Shared incident notification.** A TVOP incident triggers duties as a service provider to clients, as a merchant in three roles, card brand clocks, state breach laws, and SEC disclosure. The single notification matrix has not been exercised, and client notice terms vary (EV-025, EV-026, EV-063).
6. **Common control inheritance.** Documented for the ticketing platform and Live Venues, but not for Hotels and Restaurants, whose PMS uses local accounts outside SYS-G1 (EV-017, EV-054, EV-058).
7. **Division supplement drift.** The Hotels and Restaurants standards were last aligned to group policy in 2024 (EV-058).

### 4.1 Live Venues (`gap-analysis.csv`)
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 2 | 3 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 3 | 4 | 0 | 0 | 7 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 2 | 2 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 1 | 2 | 1 | 3 | 7 |
| PCI Req 7 Restrict access | 3 | 0 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 2 | 4 | 0 | 0 | 6 |
| PCI Req 9 Physical access and devices | 4 | 1 | 0 | 0 | 5 |
| PCI Req 10 Logging | 4 | 3 | 0 | 0 | 7 |
| PCI Req 11 Security testing | 1 | 4 | 1 | 0 | 6 |
| PCI Req 12 Policies and programs | 5 | 4 | 0 | 1 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **30** | **29** | **2** | **7** | **68** |
| FTC Act Section 5 | 0 | 3 | 0 | 0 | 3 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 2 | 1 | 0 | 4 |
| ADA Title III ticketing | 1 | 1 | 1 | 0 | 3 |
| BOTS Act and Fla. Stat. 817.36 (applicability) | 0 | 0 | 0 | 2 | 2 |
| Florida Information Protection Act (501.171(2)) | 0 | 1 | 0 | 0 | 1 |
| **Total (81)** | **32** | **36** | **4** | **9** | **81** |

Of the 40 rows with gaps, 9 are rated High, 27 Moderate, and 4 Low. Live Venues runs a defined PCI program: at the 30 integrated venues, P2PE and tokenization keep card data off its networks and most requirements are met. **Twenty-three of the 29 Partially met PCI rows trace mainly to the 8 acquired theaters**, and three more (8.2, 10.4, 12.8) partly. The two Not met PCI rows are the payment page script requirements (6.4.3, 11.6.1), caused by the 23 tags Live Venues marketing added to its checkout pages. The other Not met rows are pricing practices: advertised prices without mandatory fees (464.2(a)) and accessible seat prices raised by the pricing module (36.302(f)(3)).

### 4.2 Hotels and Restaurants (`gap-analysis-hotels-restaurants.csv`)
| Regulation | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI DSS (SAQ D, requirement groups) | 5 | 15 | 4 | 0 | 24 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 2 | 1 | 0 | 4 |
| FTC Act Section 5; FTC Disposal Rule | 0 | 2 | 0 | 0 | 2 |
| Florida guest register and 501.171(2) | 1 | 1 | 0 | 0 | 2 |
| Illinois BIPA; CIRCIA (applicability) | 0 | 0 | 0 | 2 | 2 |
| **Total (34)** | **7** | **20** | **5** | **2** | **34** |

Of the 25 rows with gaps, 2 are High, 20 Moderate, and 3 Low. **Not met:** front desk network segmentation (1.2 and 1.3), PMS account management (8.2), PMS log retention (10.5), tags on the hotels tenant's checkout (6.4.3), and total price in all rate channels (464.2(a)). The FTC alleged similar front desk and PMS weaknesses against a hotel franchisor in *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), where the court confirmed the FTC's authority to treat unreasonable cybersecurity as unfair. The SAQ D due 2026-12-31 cannot honestly attest "In Place" for these rows; the hotels division should agree a remediation timeline with its acquirer before signing.

### 4.3 Ticketing and Streaming (`gap-analysis-ticketing-streaming.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI DSS (service provider) | 18 | 11 | 2 | 0 | 31 |
| SOC 2 commitments | 1 | 4 | 0 | 0 | 5 |
| FTC Act Section 5 | 0 | 2 | 0 | 0 | 2 |
| CCPA and CPPA regulations | 0 | 2 | 0 | 0 | 2 |
| DOJ Data Security Program | 1 | 0 | 0 | 0 | 1 |
| PADFA, COPPA, FedRAMP, FCC CPNI | 0 | 0 | 0 | 4 | 4 |
| SEC disclosure (group, tracked here) | 0 | 2 | 0 | 0 | 2 |
| Florida third-party agent notice (501.171(6)) | 0 | 1 | 0 | 0 | 1 |
| **Total (48)** | **20** | **22** | **2** | **4** | **48** |

Of the 24 rows with gaps, 3 are High, 17 Moderate, and 4 Low. The CDE itself is strong: tokenization, HSM key management, segmentation tested every six months, and covert channel detection are all met. **Not met:** 6.4.3 and 11.6.1 for every tenant's payment page. The scope document of 2026-06-30 treats tenant tags as the client's responsibility, but the platform serves the page and its content security policy allows the tags (TS-G26); the QSA has already questioned this. Client agreements are the other weak area: 212 pre-2024 agreements lack the 12.9.1 acknowledgment and CCPA service provider terms, and the training feed uses all tenants' purchaser data.

## 5. Group roadmap
| # | Gap (group gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Tenant tags on payment pages (1) | All, and 1,150 clients | PCI DSS 6.4.3, 11.6.1, 12.5.2.1, 12.9.2 | High | Block tags in every checkout step; inventory, authorization, and tamper detection for all tenants; revised scope and responsibility matrix | Chief Technology Officer | 2026-11-30 |
| 2 | Acquired theaters outside scope and controls (2) | LV | PCI DSS 1.3, 3.2, 5.2, 12.5 | High | Option B interim fix; migration to the TVOP | Group PCI program director | 2026-11-15 (interim); 2027-03-31 |
| 3 | Price displays omit mandatory fees | LV, HO | 16 CFR 464.2(a)-(b), 464.3 | High | Group price display standard; channel audits; pre-publication checks | Group General Counsel | 2026-10-31 |
| 4 | Accessible seating price parity and accessible challenge (4) | LV, TS | 28 CFR 36.302(f)(1)(ii), (f)(3) | High | Remove accessible levels from auto-apply; product safeguard for clients; accessible challenge default | VP Product, Pricing and Access | 2026-11-30 |
| 5 | Front desk card data on flat networks; PMS accounts and logs | HO | PCI DSS 1.3, 8.2, 10.5; FTC Act 45(n) | High | Validated P2PE at front desks; PMS single sign-on; PMS logs to the SIEM | Director of Hotel Technology | 2027-03-31 |
| 6 | Data purpose on the patron data platform (3) | All | FTC Act 45(a)(1); 501.171(2); CCPA service provider terms | Moderate | Stop identity number export; filter the training feed by contract; amend 212 client agreements | Group Chief Privacy Officer | 2027-03-31 |
| 7 | Notification paths not exercised (5) | All | PCI DSS 12.10; 501.171(6); Form 8-K Item 1.05 | Moderate | Client notice register; multi-role matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 8 | Hotels scope, inheritance, and supplement drift (6, 7) | HO | PCI DSS 12.1, 12.4, 12.5 | Moderate | Inheritance matrix; re-issued supplement; before the SAQ is signed | Hotels security and compliance lead | 2026-12-15 |
| 9 | Third-party service providers not managed | All | PCI DSS 12.8 | Moderate | Script vendors, channel manager, seller's ticketing vendor added with evidence | Group PCI program director | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-010 and POAM-022 to POAM-026 trace directly to this analysis and to P10.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect. The analysis will be updated when PCI SSC publishes a new version.
- **TICKET Act (H.R. 1402, 119th Congress).** Passed the House on 2025-04-29 and was placed on the Senate calendar on 2025-09-16. **Not law** (bill status as recorded in the Small sample, from govinfo.gov, last updated 2026-07-10). It would add all-in pricing and speculative-ticket rules by statute. Not treated as a current obligation.
- **CIRCIA.** Final rule not published as of 2026-09-25. Reporting is voluntary until a final rule takes effect.
- **CCPA cybersecurity audits.** First audit report due 2028-04-01 for businesses with 2026 annual gross revenue over $100 million (N51-R03). The group is in that band; the plan is due 2027-06-30 (TS-G40).
