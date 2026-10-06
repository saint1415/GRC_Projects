# Regulatory Gap Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (live event venue operator with ticketing; private equity-backed; three Florida venues) |
| Tier / Vertical | Mid-Market / Arts, Entertainment, and Recreation |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, June 2024), assessed as readiness for the 2026 Report on Compliance (ROC). A contractual standard enforced through the merchant agreement, **not law** (N71-R04) |
| Other rules analyzed | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n), and the Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (both N71-R05); ADA Title III ticketing rules, 28 CFR 36.302(f); Florida Information Protection Act, Fla. Stat. 501.171(2) and (8); a one-row applicability check of the BOTS Act, 15 U.S.C. 45c |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC Analyst and the Security Manager with the CFO, the General Counsel, and the business owners; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 (scope decision by the Chief Executive Officer the same day) |

## 1. Applicability

### 1.1 PCI DSS applies by contract, and the company now needs a ROC
The company accepts payment cards through two merchant accounts, and its merchant agreement requires PCI DSS compliance. PCI SSC sets no size tiers. Merchant levels and validation rules come from the card brands and the acquirer.

**Merchant level.** The acquirer's letter of 2026-03-16 (fictional) classifies the company as a **Visa Level 2 merchant**. That is consistent with Visa's own table: *What To Do If Compromised* (v10.0, effective 2026-06-25) lists Level 2 merchants as those with 1,000,001 to 6,000,000 Visa transactions a year. The company runs about 1.6 million Visa transactions a year across both accounts, up from under 1 million before it took over the Amphitheater in 2025. The same Visa document says Level 1 and Level 2 merchants are among the entities more likely to be required to retain a PCI Forensic Investigator after a compromise, which matters for P08. Other brands' level definitions were not verified; the acquirer applies them.

**Validation required for 2026 (the acquirer's requirement):**
| Merchant account | Channels | Validation | Due |
|---|---|---|---|
| MID-T (tickets) | Online (vendor checkout form embedded in the company's event pages), box office (standalone validated P2PE devices), phone, group, and premium (virtual terminal) | **ROC by a QSA** and AOC; quarterly ASV scans | 2026-12-15 |
| MID-F (food, beverage, merchandise) | Card present at bars, stands, and merchandise tables, all on a PCI-listed validated P2PE solution | **SAQ P2PE** and AOC | 2026-12-15 |

**Why the 2025 validation no longer fits.** In 2025 the company filed SAQ A for MID-T. SAQ A covers card-not-present channels that are fully outsourced. Two things fall outside it: the virtual terminal, where staff type card numbers into a browser on general-purpose laptops, and the company's own website pages, which embed the payment form and load 31 third-party scripts. PCI DSS v4.0.1 places the scripts on a merchant's page that embeds a provider's payment form within the merchant's responsibility for Requirements 6.4.3 and 11.6.1. A ROC covers all applicable requirements, which is why this analysis rates every requirement group, plus the defined requirements that decide the result.

### 1.2 The scope decision (made by the CEO on 2026-09-15)
| Option | What it takes | Effect on the 2026 ROC |
|---|---|---|
| A. Validate the current scope | Bring the corporate segment at 4 sites and all 494 other laptops and PCs up to CDE controls (segmentation tests, internal scans, logging, intrusion detection) by QSA fieldwork on 2026-11-02 | Not achievable in time; the AOC would be Non-Compliant with a long remediation plan |
| **B. Reduce scope first (chosen)** | By 2026-10-30: replace the virtual terminal with 26 standalone validated P2PE devices that accept keyed phone orders (about $14,000, fictional), so no card number reaches a laptop; purge the card data found in the CRM and mailboxes; and put the payment page script controls (6.4.3, 11.6.1) in place on the website | The laptops and the corporate segment leave the CDE. The ROC then covers the website and cloud systems that serve the payment pages, the ticketing tenant settings, identity, and the P2PE devices. The 6 rows marked with a scope note leave the ROC scope |

Option B does not remove the need for the controls in those 6 rows. Network separation, wireless checks, and remote access MFA remain part of reasonable security under FTC Act Section 5 and Fla. Stat. 501.171(2), and stay in P01 and P07.

**Readiness forecast.** If the 11 High rows due by 2026-10-31 close as planned (the other 2, G-070 and G-074, are due later), the remaining open rows are mostly Moderate and Low process and documentation items. The QSA will decide what is In Place. Rows still open at fieldwork will be reported as Not in Place, and the AOC may be Non-Compliant with a remediation plan that the acquirer must accept. The CFO has told the acquirer that this is possible.

### 1.3 Other rules for the primary business line
- **FTC Act Section 5** applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)). It may treat a practice as unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that benefits to consumers or competition do not outweigh (45(n)).
- **Rule on Unfair or Deceptive Fees, 16 CFR Part 464** (90 FR 2166, published 2025-01-10, effective 2025-05-12). "Covered good or service" includes live-event tickets (464.1). Any business that offers, displays, or advertises a price must disclose the total price clearly and conspicuously (464.2(a)) and more prominently than other pricing information (464.2(b)). Before the patron pays, excluded fees and the final amount must be disclosed (464.2(c)). Fees may not be misrepresented (464.3). The rule reaches the company's own website calendar and emails, not just the vendor's checkout.
- **ADA Title III ticketing rules, 28 CFR 36.302(f).** Each venue is a place of public accommodation. The rules cover equal opportunity to buy accessible seating at the same stages and through the same channels ((f)(1)(ii)), identification of accessible seating ((f)(2)), price parity ((f)(3)), multiple-ticket purchases ((f)(4)), and a ban on requiring proof of disability ((f)(8)). They bind the pricing and bot settings in the ticketing tenant (P10).
- **Florida Information Protection Act.** Fla. Stat. 501.171(2) requires reasonable measures to protect electronic personal information, and 501.171(8) requires disposal of customer records containing personal information when they are no longer retained. Personal information includes a name with a card number and any required security code (501.171(1)(g)1.a.(III)). Breach notification under 501.171(3) to (6) is handled in P08.
- **BOTS Act, 15 U.S.C. 45c.** The company is a "ticket issuer" and its venues exceed the 200-person capacity in the Act's definition of an event. The Act places **no compliance duty** on the company; it protects the company. Bot detection records are evidence for FTC or state enforcement (P10).

**State privacy laws (applicability only, not rated):**
| Law | Finding |
|---|---|
| Florida Digital Bill of Rights | **Not applicable.** A controller under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests (50% or more of revenue from online advertising, a consumer smart speaker and voice service, or an app store with at least 250,000 applications). The company has $100 million in revenue |
| Texas Data Privacy and Security Act | **Under counsel review.** It has no consumer-count threshold and reaches persons that produce products or services consumed by Texas residents, process personal data, and are not SBA-defined small businesses (Tex. Bus. & Com. Code 541.002). The company is not SBA-small, and about 25,000 patron accounts have Texas billing addresses. The General Counsel will decide by 2026-12-31 (P01 R-048) |
| Other state comprehensive privacy laws | Counsel will test each state's consumer-count thresholds against patron counts by billing state. No state other than Florida has more than about 40,000 patron accounts |

**Not applicable, with reasons:** Nevada Regulation 5.260, NIGC MICS, and the casino BSA/AML rules (N71-R01 to R03), because there is no gaming; COPPA (N71-R06), because the website, ticketing pages, and app are not directed to children and accounts require age 18 or older; SEC disclosure (privately held); CIRCIA (final rule not published).

## 2. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and their requirement groups. Where a single defined requirement decides the result, it was rated on its own: 6.4.1, 6.4.2, 6.4.3, 8.4.1, 8.4.2, 8.4.3, 11.3.1, 11.3.2, 11.6.1, 12.5.1, 12.5.2, and 12.5.3. The appendices were added. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; the company holds a licensed copy of v4.0.1. The FTC, ADA, and Florida rows cite the statute or rule text (uscode.house.gov, eCFR as of 2026-09-23, and the Florida Statutes).
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1, Part 464, 28 CFR 36.302, or Fla. Stat. 501.171 to CSF 2.0 or SP 800-53 was used.
3. **Evidence.** Interviews with the CEO, CFO, General Counsel, and every business owner; document review (2025 SAQs, merchant agreement, acquirer letter, vendor AOCs and SOC 2 reports, policies); configuration exports; browser captures of 10 event pages on 2026-07-20; a card data discovery scan on 2026-07-22; observation of a high-demand on-sale (2026-07-15) and an Amphitheater show night (2026-07-18); and walkthroughs at all 4 sites.
4. **Evidence sampling.** Where a control operates many times, a sample was tested from a system-generated population, using the co-sourced internal audit firm's attribute sampling table (25 items for controls operating many times a year; all items for small populations). Each `evidence` cell names the sample and the result. The main samples:
   - ticketing venue users: 186 of 186; terminations: 25 of 96; transfers: 25 of 51;
   - payment page scripts: 31 of 31; event pages captured: 10;
   - ticketing setting changes: 25 of 214; infrastructure changes: 25 of 61;
   - CMS plug-ins: 23 of 23; internal scan reports: 6 of 6 months; ASV reports: 4 of 4 quarters;
   - P2PE devices: 284 POS and 18 box office devices reconciled; inspection records: 10 event days;
   - laptops: 20 of 520; training records: 25 of 600; HR screening files: 15;
   - calendar listings: 40 of 312; email campaigns: 12 of 58; social posts: 20;
   - dynamic pricing logs: 14 reserved-seat shows; vendor files: 12 service providers.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 1 | 3 | 1 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 2 | 1 | 0 | 3 |
| PCI Req 3 Stored account data | 0 | 2 | 3 | 2 | 7 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 4 | 0 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 2 | 4 | 1 | 0 | 7 |
| PCI Req 7 Restrict access | 1 | 2 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 6 | 1 | 0 | 8 |
| PCI Req 9 Physical access and POI devices | 0 | 5 | 0 | 0 | 5 |
| PCI Req 10 Logging and monitoring | 1 | 5 | 1 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 6 | 1 | 0 | 7 |
| PCI Req 12 Policies and programs | 1 | 7 | 1 | 3 | 12 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **12** | **43** | **10** | **8** | **73** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| FTC Rule on Unfair or Deceptive Fees | 1 | 1 | 2 | 0 | 4 |
| ADA Title III ticketing rules | 2 | 1 | 2 | 0 | 5 |
| Florida Information Protection Act | 0 | 1 | 1 | 0 | 2 |
| BOTS Act (applicability check) | 0 | 0 | 0 | 1 | 1 |
| **Total (88)** | **15** | **48** | **16** | **9** | **88** |

The 88 rows are 58 PCI requirement groups, 12 PCI defined requirements, 3 appendices, 6 statute rows, 5 regulation rows, and 4 rule rows.

**Gap risk ratings (64 rows Partially met or Not met):** 13 High, 36 Moderate, 15 Low.

**Reading the results.** The company is a mid-market program with real strengths: EDR and anti-phishing (Requirement 5 fully Met), validated P2PE at every box office and bar, SSO with MFA for employees, a web application firewall, passing ASV scans, and isolated backups. The gaps cluster where the company grew faster than its 2025 SAQ A validation:
- the payment page scripts and change detection (6.4.3, 11.6.1);
- the virtual terminal channel and the card data it leaked into the CRM (1.3, 3.2, 3.3);
- accounts outside SSO and the API key (8.2, 8.4.1, 8.4.2, 8.6);
- log review for the SaaS and website sources (10.4);
- scope documentation (12.5.2) and incident procedures for card compromise (12.10);
- fee display and accessible seating rules in pricing (464.2, 36.302(f)).

## 4. Priority gaps
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Card numbers in CRM notes and mailboxes | G-010 (3.2) | High | Purge; block card numbers in CRM fields; email data loss prevention | Director of Premium Seating and Group Sales | 2026-09-30 |
| Security codes in 9 CRM notes | G-011 (3.3) | High | Delete at once; installments only through the card vault | Director of Premium Seating and Group Sales | 2026-09-30 |
| Shared and stale local ticketing accounts | G-033 (8.2) | High | Disable departed and inactive accounts; named break-glass accounts | Vice President of Ticketing | 2026-09-30 |
| Advertised prices omit mandatory fees | G-077 (464.2(a)) | High | Total price in every listing, email, and post; pre-publication check | Vice President of Marketing and Digital | 2026-09-30 |
| Scope never documented | G-064 (12.5.2) | High | Scope document with the P2PE scope reduction | Security Manager | 2026-10-23 |
| Virtual terminal laptops on the corporate segment | G-003 (1.3) | High | Standalone validated P2PE devices for keyed orders | Vice President of Ticketing | 2026-10-30 |
| Unmanaged scripts around the payment form | G-027 (6.4.3) | High | Inventory, authorization, justification, integrity; tag manager on SSO with two-person publishing | Vice President of Marketing and Digital | 2026-10-30 |
| No payment page change detection | G-058 (11.6.1) | High | Monitoring service with alerts to the MSSP | Vice President of Marketing and Digital | 2026-10-30 |
| No review of ticketing, website, and partner logs | G-048 (10.4) | High | SIEM sources and use cases; daily automated review | Security Manager | 2026-10-30 |
| Admin access without MFA | G-035 (8.4.1) | High | App-based MFA on break-glass accounts; tag manager on SSO | Security Manager | 2026-10-31 |
| Local accounts without MFA | G-036 (8.4.2) | High | SSO or vendor MFA for all local accounts | Vice President of Ticketing | 2026-10-31 |
| Incident plan untested for card compromise | G-070 (12.10) | High | Tabletop on 2026-11-04; crisis team training | Security Manager | 2026-11-30 |
| Security not yet reasonable for 1.1 million patron records | G-074 (45(n)) | High | P01 treatments and the P07 POA&M | Security Manager | 2026-12-31 |
| Over-privileged, unrotated API key | G-039 (8.6) | Moderate | Read-only key in the secrets service | IT Director | 2026-10-15 |
| Accessible seating priced above parity | G-083 (36.302(f)(3)) | Moderate | Remove from auto-apply; daily parity check; refunds | Vice President of Ticketing | 2026-09-30 |
| Wheelchair-space orders capped at 4 | G-084 (36.302(f)(4)) | Moderate | Match the posted limit of 8 | Vice President of Ticketing | 2026-10-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Stop the leaks** | By 2026-09-30 | Card data purged and blocked; departed accounts disabled; total-price displays; accessible seating parity; ASV scope extended to the 4 site addresses | G-010, G-011, G-033, G-077, G-083, G-055 |
| **2. Reduce scope and protect the payment page** | 2026-10-01 to 2026-10-30, before QSA fieldwork | Virtual terminal replaced by P2PE devices; script controls and change detection; local accounts on SSO or MFA; API key replaced; scope document; targeted risk analyses; internal and external penetration tests; SaaS and website logs in the SIEM | G-003, G-027, G-058, G-035, G-036, G-039, G-064, G-048, G-061, G-056 |
| **3. ROC and remediation** | 2026-11-02 to 2026-12-15 | QSA fieldwork; card compromise tabletop; AOCs submitted with any remediation plan | G-070, G-067 |
| **4. Harden and sustain** | 2027 Q1-Q2 | Segmentation of physical security and production; hardening standards; privileged access management for all admin planes; County PAC onboarding inside the documented scope | G-004, G-007, G-008, G-057 |

Progress is reported quarterly to the audit committee as the count of rows moving to Met.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 is the version in effect for this analysis. The analysis will be updated when PCI SSC publishes a new version.
- **TICKET Act (H.R. 1402, 119th Congress).** Passed the House on 2025-04-29 and was placed on the Senate calendar on 2025-09-16. It is **not law**. It would add all-in pricing and speculative-ticket rules by statute. Not treated as a current obligation.
- **FTC v. Live Nation Entertainment and Ticketmaster** (filed 2025-09-18, C.D. Cal., with seven states). The complaint alleges deceptive advertised prices, deception about the enforcement of posted ticket limits, and BOTS Act violations. These are allegations, not findings, but they show why a posted limit must match how it is enforced (G-076).
- **Executive Order 14254** (2025-03-31) directs the FTC to enforce the BOTS Act rigorously.
- **CIRCIA.** The final rule had not been published as of 2026-09-25. If it is finalized as proposed, entities in a critical infrastructure sector that exceed their SBA size standard would report covered incidents; the company is above its SBA standard and in the Commercial Facilities Sector. Tracked in P08, not treated as a current obligation.
