# Regulatory Gap Analysis: Cris Santos Company | Accommodation and Food Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, published 2024-06-11). A contractual standard enforced through the merchant agreement, **not law** (N72-R01) |
| Other rules for the primary business line | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n), with the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N72-R02); FTC Disposal Rule, 16 CFR 682.3 (N72-R03); FACTA receipt truncation, 15 U.S.C. 1681c(g); Fla. Stat. 509.101(2) and 501.171(2), (6)(a), and (8) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 and P10 results through 2026-09-04 |
| Assessor | GRC Analyst and the Security Manager, with the General Counsel and the vCISO; reviewed by the co-sourced internal audit firm. This is the company's own readiness work before the QSA-supported assessment from 2026-10-05 |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** owning and operating 6 Florida hotels, with card payments at front desks, outlets, the CRO, group sales, and online.

### 1.1 Franchised and independent hotels
**Decision: the company owns its PCI DSS program for all 6 hotels, including the franchised ones.** It is the merchant of record for all 10 merchant accounts. At Resorts 1 and 2 it chooses and runs every system. At Hotels 3 to 6 the franchisor mandates and runs the PMS, central reservation system, gateway, and property firewalls, so part of the control set is the franchisor's. The franchise agreements require brand standards but **do not say which PCI DSS requirements each party meets**. Requirement 12.8.5 expects exactly that record (row G-087).

The key precedent is *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24). The Third Circuit affirmed that the FTC can challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), and that the company had fair notice. The FTC alleged that the franchisor, which connected and managed its branded hotels' PMS systems, allowed card data in clear text, easily guessed and default passwords, no firewalls between hotel systems, the corporate network, and the internet, an out-of-date operating system, unrestricted vendor access, and weak detection and incident response. Three intrusions in 2008 and 2009 were alleged to have exposed over 619,000 accounts and caused at least $10.6 million in fraud loss. Two lessons apply here:
- **As franchisee**, the company cannot assume the franchisor's controls protect its hotels. It must know which controls the franchisor runs and get evidence (rows G-001, G-004, G-087).
- **As operator**, several of the company's own gaps match the Wyndham list: card data stored in clear text (G-010), a default password (G-007), weak separation between hotel networks and the corporate network (G-003), unsupported operating systems (G-071), and unrestricted vendor access (G-077).

### 1.2 PCI DSS validation and scope
**PCI DSS applies by contract.** PCI SSC sets no size tiers; merchant levels and validation rules come from the card brands and the acquirer. In a letter dated 2026-05-18 (fictional), the acquirer required the company to validate all 10 MIDs as one merchant with an **SAQ D for Merchants** prepared with a QSA firm and signed by an officer, plus passing quarterly ASV scans. This analysis does not restate brand level thresholds, because they were not verified from a card brand source. Visa's public compliance page states that a merchant's level is based on its total Visa transaction volume over 12 months. The company runs about 1.05 million card transactions a year across all brands.

**Why the scope is large today, channel by channel:**
| Channel | Design | Effect on scope |
|---|---|---|
| Resort front desks | Validated P2PE devices, semi-integrated with SYS-01 | Small: device custody and inspection only |
| Resort 1 outlets | Cloud POS with validated P2PE devices | Small |
| Resort 2 outlets | Legacy POS; card data passes in clear through workstations and the server | **Full CDE:** POS VLAN, server, workstations, and anything that can reach them (including the corporate directory, row G-003) |
| Hotels 3 to 6 front desks | Brand terminals (not P2PE) on a flat staff network | **Full CDE:** every device on the staff network, including staff Wi-Fi (G-008) |
| CRO phone payments | Agents key card numbers into SYS-01 on general-purpose PCs | **CDE:** 22 CRO PCs and the CRO network segment |
| Call recordings | Spoken card numbers and security codes stored | **CDE:** the call recording store, its account, and 14 users (P04 finding 1) |
| Group sales and catering email | Card forms in 6 shared mailboxes | **CDE:** the mailboxes and their users |
| Online travel agency virtual cards | Vault in SYS-01; displayed to users with the permission | Users with the display permission (G-069) |
| Booking engine | Vendor payment form embedded in an iframe on company-managed websites | The website pages fall under 6.4.3 and 11.6.1 (G-072, G-085) |

The 2025 SAQ D was signed without the call recording store or the mailboxes in scope (G-086).

**Scope reduction for 2027.** If the company (a) purges stored card data and stops accepting forms by email, (b) uses pause-and-resume recording and keypad entry devices in the CRO, (c) replaces the Resort 2 POS with a validated P2PE solution, and (d) agrees with the franchisor on validated P2PE terminals and a separate terminal network at Hotels 3 to 6, most of the systems above leave the CDE. The company would still validate with SAQ D in 2027 because of the remaining channels, but far fewer requirements would apply to far fewer systems. This is subject to the QSA scoping review in October and November 2026.

**Current version.** PCI DSS v4.0.1 is the current version. Its publication added no new requirements; the requirements introduced as future-dated in v4.0 have been in force since 2025-03-31 (PCI SSC blog, 2024-06-11).

### 1.3 Other rules, decided at this size
| Rule | Applies? | Basis |
|---|---|---|
| FTC Act Section 5 (N72-R02) | **Yes** | No size threshold. Deception (45(a)(1)) covers privacy, security, and pricing claims; unfairness (45(n)) covers practices that cause or are likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits |
| 16 CFR Part 464 (N72-R02) | **Yes** | Covers "short-term lodging, including temporary sleeping accommodations at a hotel" (464.1). Any offer, display, or advertisement of a price must show the total price, including mandatory fees such as the $40 resort fee, more prominently than other pricing (464.2(a)-(b)). Government taxes may be excluded but must be disclosed with the final amount before the guest pays (464.1, 464.2(c)). Fees must not be misrepresented (464.3). Rule published at 90 FR 2066 (rule text at 2166), 2025-01-10; effective 2025-05-12; no amendments on eCFR as of 2026-09-23 |
| FTC Disposal Rule (N72-R03) | **Yes** | The company obtains background-check reports on applicants (16 CFR 682.3) |
| FACTA receipt truncation | **Yes** | 15 U.S.C. 1681c(g)(1) bars printing more than the last 5 digits of the card number or the expiration date on electronically printed receipts (verified on govinfo.gov) |
| Fla. Stat. 509.101(2) | **Yes** | Each operator of a transient establishment must keep a chronological register of guests with dates of occupancy and rates, available for inspection; it may be electronic; registers more than 2 years old need not be made available (verified on flsenate.gov, 2026 statutes). This sets a **2-year floor**, not a reason to keep everything |
| Fla. Stat. 501.171(2), (6)(a), (8) | **Yes** | (2) reasonable security for electronic personal information; (6)(a) third-party agent notice within 10 days, which applies to the company **as agent for the REIT-owned hotels from 2027-01-01**; (8) disposal. Breach notice under (3)-(5) is handled in P08. Personal information includes ID numbers, card numbers with any required security code, and biometric data as defined in 501.702 (501.171(1)(g)1.a.) |
| CIRCIA (N72-R06) | **Not yet** | Proposed only (89 FR 23644); no final rule as of 2026-09-25. Commercial Facilities entities have no sector criterion, but proposed 226.2(a) would cover entities that exceed the SBA size standard. The company exceeds it ($100 million against $40.0 million), so it would likely be covered if the rule is finalized as proposed. Tracked in P08 |
| CCPA | **Watch item** | Revenue exceeds the $26,625,000 threshold, but the company has no California establishment, employees, or property. Counsel advised on 2026-07-28 that whether national online marketing to California residents is "doing business in California" is unsettled. CCPA rows are not rated; the privacy notice update (G-089) follows CCPA-style disclosures as a precaution |
| Florida Digital Bill of Rights | **No** | A controller under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests (online advertising revenue, a smart speaker service, or an app store). The company meets none |
| Illinois BIPA (N72-R05) | **No** | No Illinois operations or employees |
| FTC Safeguards and Red Flags Rules | **No** | No consumer credit is extended; direct billing to group clients is business credit |
| HIPAA; SEC disclosure rules; federal contract clauses | **No** | Not a covered entity; privately held; no federal contracts |

**Rows marked Not applicable (7):** requirements for keys the company does not hold (3.6, 3.7), service-provider-only groups (12.4, 12.9), and Appendices A1 to A3.

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their 63 requirement groups, plus the 3 appendices. **21 defined requirements** were taken to their own rows because they decide scope or carry the largest risk (3.3.1, 3.3.1.2, 3.4.1, 5.4.1, 6.3.3, 6.4.3, 7.2.4, 8.2.2, 8.2.6, 8.4.2, 8.4.3, 9.5.1.1 to 9.5.1.3, 10.4.1, 10.5.1, 11.3.2, 11.4.5, 11.6.1, 12.5.2, 12.8.5). Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted; read the requirement text in the official standard. Requirement numbers were checked against the company's licensed copy and against the public PCI SSC self-assessment questionnaires for v4.0 (SAQ A, SAQ C-VT, and SAQ P2PE).
2. **FTC, FACTA, and Florida rows** cite text verified on govinfo.gov (15 U.S.C. 1681c(g)), eCFR (16 CFR Parts 464 and 682, 2026-09-23 version), the Federal Register, and the Florida Senate site (2026 statutes: 501.171, 509.101).
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 to CSF 2.0 or SP 800-53 was used.
4. **Evidence.** Interviews with the CFO, General Counsel, IT Director, Vice President of Sales and Marketing, Director of Central Reservations, Director of Revenue Management, all 6 General Managers, both Resort Directors of Food and Beverage, the MSSP service lead, and the franchisor's regional IT contact; document review (2025 SAQ D, merchant agreement, acquirer letter, franchise agreements, vendor AOCs and SOC 2 reports, privacy notice); configuration exports; a data discovery scan of mailboxes and file shares on 2026-07-21; browser captures of the booking pages on 2026-07-23; and walkthroughs at all 6 hotels from 2026-07-13 to 2026-07-24.
5. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, with sizes from the co-sourced internal audit firm's attribute sampling table (25 items for a moderate-risk control operating many times a year):
   - terminations: 25 of 212; transfers: 25 of 70; hires in sensitive roles: 25;
   - SYS-01 permissions: all 162 users; brand PMS accounts: all 64;
   - call recordings: 60 from July 2026 (13 held a card number and security code, about 22%, which applied to about 148,000 recordings gives the estimate of 31,000);
   - payment devices: 120 of 120 reconciled to lists; inspection logs: 13 weeks at 6 hotels;
   - critical patches: 14 of 14 released in the last 12 months for in-scope systems;
   - booking page scripts: 23 of 23; ASV reports: the last 4 quarters; vendor AOCs and SOC 2 reports: 31 of 31;
   - receipts: 40 across 6 hotels; chatbot rate answers: 20; CRO test calls: 20; cloud change tickets: 20.
   Each `evidence` cell names the sample and its result.
6. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 1 | 3 | 1 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 0 | 2 | 6 | 2 | 10 |
| PCI Req 4 Transmission | 1 | 1 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 3 | 2 | 0 | 0 | 5 |
| PCI Req 6 Secure systems and software | 0 | 5 | 2 | 0 | 7 |
| PCI Req 7 Restrict access | 2 | 1 | 1 | 0 | 4 |
| PCI Req 8 Identify and authenticate | 3 | 3 | 4 | 0 | 10 |
| PCI Req 9 Physical access and devices | 0 | 7 | 1 | 0 | 8 |
| PCI Req 10 Logging | 0 | 6 | 3 | 0 | 9 |
| PCI Req 11 Security testing | 1 | 4 | 4 | 0 | 9 |
| PCI Req 12 Policies and programs | 2 | 4 | 4 | 2 | 12 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **13** | **39** | **28** | **7** | **87** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| 16 CFR Part 464 (fees) | 2 | 1 | 1 | 0 | 4 |
| FTC Disposal Rule | 0 | 1 | 0 | 0 | 1 |
| FACTA receipt truncation | 1 | 0 | 0 | 0 | 1 |
| Florida Statutes (509.101, 501.171) | 1 | 2 | 1 | 0 | 4 |
| **Total** | **17** | **45** | **31** | **7** | **100** |

**PCI DSS detail.** The 87 PCI rows are 63 requirement groups (10 Met, 35 Partially met, 14 Not met, 4 N/A), 21 defined requirements (3 Met, 4 Partially met, 14 Not met), and 3 appendices (N/A). The defined requirements fare worse than the groups because they were chosen for being the riskiest.

**Gap risk ratings (76 rows Partially met or Not met):** 28 High, 34 Moderate, 14 Low.

**Reading the results.** The company has a real program: MFA everywhere it controls identity, EDR, ASV scans, P2PE at the resort front desks and Resort 1, current policies, and good receipts and fee displays on the booking engine. The gaps concentrate in five places:
- card data stored where no process needs it (Requirement 3);
- the legacy Resort 2 POS and flat networks at the franchised hotels (Requirements 1, 2, 6);
- vendor and franchisor access and oversight (8.4.3, 12.8, 12.8.5);
- logging and testing coverage (Requirements 10 and 11);
- scope never documented (12.5.2).

## 4. Priority gaps
| Gap | Rows | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Security codes and card numbers in mailboxes and call recordings | G-010, G-011, G-067, G-068 (3.2, 3.3, 3.3.1, 3.3.1.2) | High | Purge; data loss prevention rules; pause-and-resume recording | CFO; Director of Central Reservations | 2026-12-31 |
| Scope not documented | G-058, G-086 (12.5, 12.5.2) | High | Scope document with the QSA firm | CFO | 2026-11-20 |
| Vendor remote access without MFA | G-033, G-077 (8.4, 8.4.3) | High | Vendor access only through the broker | Security Manager | 2026-11-30 |
| Default password and unneeded services on vendor systems | G-007 (2.2) | High | Sweep and harden | IT Director | 2026-10-31 |
| Excess card display rights | G-012, G-069 (3.4, 3.4.1) | High | Remove from 38 users | Resort Front Office Managers | 2026-10-31 |
| Card forms in an unlocked binder | G-039 (9.4) | High | Destroy and lock | CFO | 2026-10-31 |
| Late removal in the brand PMS | G-031 (8.2) | High | Removal within 1 business day | HR Director | 2026-11-30 |
| CDE not isolated at Resort 2 and Hotels 3 to 6 | G-003 (1.3) | High | Block directory traffic; VLANs behind brand firewalls | IT Director | 2027-03-31 |
| Unsupported systems in the CDE | G-024, G-071 (6.3, 6.3.3) | High | Replace both servers; isolate until then | IT Director | 2027-06-30 |
| Logging and daily review | G-042, G-044, G-081 (10.2, 10.4, 10.4.1) | High | Onboard sources; automated daily review | Security Manager | 2027-01-31 |
| Scanning and segmentation testing | G-050, G-084 (11.3, 11.4.5) | High | Scan Hotels 3 to 6; segmentation test | Security Manager | 2026-12-31 |
| Third-party oversight and the franchisor matrix | G-061, G-087 (12.8, 12.8.5) | High | AOCs; annual reviews; signed matrix | GRC Analyst; General Counsel | 2027-03-31 |
| Untested incident response plan | G-063 (12.10) | High | Card compromise tabletop | Security Manager | 2026-11-30 |
| Security not yet reasonable (FTC, Florida) | G-088, G-098 | High | Execute the roadmap | vCISO | 2027-06-30 |
| Partial prices in chatbot and CRO quotes | G-092 (464.2) | Moderate | Total price first | Vice President of Sales and Marketing | 2026-10-31 |
| False "we do not store card data" statement | G-089 (45(a)(1)) | Moderate | Rewrite the notice | General Counsel | 2026-10-31 |
| No retention schedule | G-100 (501.171(8)) | Moderate | Schedule; purge ID scans | General Counsel | 2026-12-31 |

**Before the CFO signs the 2026 SAQ D (due 2026-12-31):** complete G-086 (scope), the purge in G-010 and G-067, G-077 (vendor MFA), G-084 (segmentation test), and G-069 (display rights). For any requirement that cannot be met by the due date, the CFO agrees the reporting approach with the acquirer and the QSA firm rather than answering "In Place" without evidence.

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Stop storing and stop the open doors** | 2026 Q4 | Purge card data from mailboxes, recordings, and paper; pause-and-resume recording; vendor access through the broker; display rights cut; default-password sweep; scope document; segmentation test; card compromise tabletop; total price in chatbot and CRO quotes; privacy notice rewritten | G-010, G-011, G-039, G-067 to G-069, G-077, G-086, G-084, G-063, G-092, G-089 |
| **2. See and test everything in scope** | 2027 Q1 | SIEM onboarding of POS, lock servers, and Hotels 3 to 6; daily automated review; EDR on all PCs; internal penetration test; reviews every 6 months; signed franchisor matrix; current AOCs for all card vendors; payment page script controls | G-042, G-044, G-081, G-019, G-051, G-073, G-087, G-061, G-072, G-085 |
| **3. Shrink the CDE** | 2027 Q2 | Resort 2 P2PE cloud POS; Resort 2 lock server replaced; keypad entry in the CRO; VLANs behind the brand firewalls; retention schedule enforced | G-003, G-024, G-071, G-008, G-100 |
| **4. Sustain** | 2027 Q3-Q4 | 2027 SAQ D on the reduced scope; SOC 2 Type 2 observation period (P09); annual risk assessment; vendor reassessments | G-058, G-061, G-088, G-098 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments toward the next version in 2026; the analysis will be updated when a new version is published.
- **CIRCIA.** The final rule was not published as of 2026-09-25. If finalized as proposed, the company would likely be covered and would report covered cyber incidents within 72 hours and ransom payments within 24 hours (proposed 6 CFR 226.5). P08 carries it as a watch row.
- **FTC fee rules.** A proposed FTC rulemaking on fees for food and grocery ordered through online delivery platforms (91 FR 20381, 2026-04-16) is not final and targets delivery platforms, not hotels.
- **FTC AI accuracy policy statement** (proposed, July 2026) is not final (P10).
- **CCPA** remains a watch item (section 1.3).
- None of these is treated as a current obligation.
