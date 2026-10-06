# Regulatory Gap Analysis: Cris Santos Company Holdings | Accommodation and Food Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Accommodation and Food Services (focus division: Hotels) |
| Primary standard (Hotels) | PCI DSS v4.0.1 (PCI Security Standards Council, published 2024-06-11), as **merchant and service provider**. A contractual standard enforced through the acquirer agreements, **not law** (N72-R01) |
| Division regulations | Attractions: PCI DSS v4.0.1 as merchant (N71-R04) and the COPPA Rule, 16 CFR Part 312 (N71-R06). Vacation Ownership: the FTC Safeguards Rule, 16 CFR Part 314 (N53-R01), with the Red Flags Rule (16 CFR 681.1), Regulation B (12 CFR 1002.9), Fla. Stat. 721.13(12)(c), and PCI DSS SAQ D (N53-R04) |
| Group-wide obligations | FTC Act Section 5 (N72-R02), 16 CFR Part 464, state breach notification and data security laws (N72-R04; Florida worked example), the CCPA cybersecurity audit regulations (N53-R03), SEC Form 8-K Item 1.05 and Reg S-K Item 106 (N53-R05) |
| Gap tables | `gap-analysis.csv` (Hotels and group-wide, 106 rows); `gap-analysis-attractions.csv` (42 rows); `gap-analysis-vacation-ownership.csv` (44 rows) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads (the Vacation Ownership lead as Qualified Individual), the Group Director of Payments and PCI Compliance, and the Group Chief Privacy Officer, coordinated by the Group Chief Risk Officer; reviewed by group internal audit |
| Approved | Group CISO and Group General Counsel, 2026-09-08; roadmap reviewed by the board risk committee, 2026-09-10 |

## 1. Applicability
### 1.1 Who is what under PCI DSS
PCI SSC sets no size tiers. Card brands and acquirers set merchant levels and validation methods; their thresholds were not verified from a card brand primary source, so no level number is stated. Each division validates under its own acquirer agreement:

| Entity | PCI DSS role | Validation (fictional contract terms) |
|---|---|---|
| Hotels (30 owned or leased hotels) | Merchant (Acquirer A) | Annual QSA Report on Compliance; 2025 ROC compliant with 4 compensating controls; 2026 ROC due 2026-11-30 |
| Hotels (58 managed hotels) | **Third-party service provider** to the owners, who are the merchants of record; the division designs, connects, and operates their PMS, POS, payment, and property networks | Service provider ROC dated 2026-03-20. The service-provider-only requirements apply: 11.4.6, 12.4.1, 12.4.2, 12.5.2.1, 12.9.1, and 12.9.2 |
| Attractions | Merchant (Acquirer B) | QSA ROC; 2026 ROC due 2026-12-15 |
| Vacation Ownership | Merchant (Acquirer C) | SAQ D for Merchants, because sales gallery terminals connect to division workstations; 2026 SAQ due 2026-12-31 |
| Corporate (SYS-G4) | Shared CDE used by all three divisions | Tested within each division's validation; the 2026 service provider ROC covers it in full |

**Not a franchisor, but a manager.** The group does not franchise. But *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), affirmed that the FTC may treat unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a) in a case about a hotel company that managed its branded hotels' PMS systems. The FTC alleged card data in clear text, default passwords, no firewalls between hotel PMS systems, the corporate network, and the internet, an out-of-date operating system, no inventory, and unrestricted vendor access. **The group operates the systems at its 58 managed hotels, so it is measured on them** (row G-076). Three of those practices are open today: unrestricted legacy POS vendor access, default lock server passwords, and an operating system that leaves support on 2027-01-31.

**Current version.** PCI DSS v4.0.1 is current. Its publication added no new requirements; requirements introduced as future-dated in v4.0 have been in force since 2025-03-31. PCI SSC ran a request for comments on v4.0.1 in June and July 2026 toward the next version.

### 1.2 FTC Safeguards Rule: the finance subsidiary
The Safeguards Rule applies to financial institutions under FTC jurisdiction, which 314.1(b) says include "finance companies." Cris Santos Vacation Finance, LLC extends consumer credit for timeshare purchases (about 126,000 active loans) and is not a bank, so it is covered. The 314.6 exceptions for institutions with customer information on fewer than 5,000 consumers do not apply. Three consequences shape this analysis:
- **The Qualified Individual works for an affiliate.** The Vacation Ownership security and compliance lead is employed by Cris Santos Vacation Ownership, Inc., not by the finance subsidiary. 314.4(a)(1) to (3) therefore require the finance subsidiary to keep responsibility, name a senior officer to direct and oversee the Qualified Individual (its president), and require the affiliate to keep a program that protects it (row V-003).
- **Customer information has left the division.** Owners' bank account and routing numbers for about 212,000 autopay owners were copied to the group guest profile hub (SYS-G5) in 2025. Customer information is any record about a customer "handled or maintained by or on behalf of you or your affiliates," so the hub is now part of the finance subsidiary's Safeguards Rule scope (row V-006).
- **The FTC notice clock can start in the group SOC.** A notification event is treated as discovered when it is known to any employee, officer, or other agent (314.4(j)(2)). The group SOC monitors the division, so P08 starts the 30-day clock there.

The **Red Flags Rule** (16 CFR 681.1) applies because consumer timeshare loans are covered accounts, and **Regulation B** (12 CFR 1002.9) applies to the credit decisions of the AI credit model. CCPA rights do not reach loan data subject to GLBA (Civ. Code 1798.145(e)), but the CCPA still applies to the group's other California personal information.

### 1.3 COPPA: the Junior Explorers kids' club
The park app's kids' club is an online service directed to children, and Cris Santos Parks and Attractions, LLC is its operator (312.2). The amended rule took effect 2025-06-23 with compliance required by 2026-04-22, including the written children's information security program (312.8(b)) and the written retention policy (312.10). The club launched in 2025-11, before the compliance date, and was not updated (scenario gap 4).

### 1.4 Other applicability decisions
| Regulation | Applies? | Basis |
|---|---|---|
| 16 CFR Part 464 (N72-R02) | **Yes** | Covers "short-term lodging, including temporary sleeping accommodations at a hotel" and vacation rentals, and "live-event tickets" (464.1). 90 FR 2066 (rule text at 2166), published 2025-01-10, effective 2025-05-12; text checked on eCFR as of 2026-09-23. Total price, including mandatory fees, more prominently than other pricing (464.2(a)-(b)); excluded government charges and the final amount before the consumer pays (464.2(c)); fees not misrepresented (464.3). Whether general admission park tickets are "live-event tickets" is unsettled; counsel treats them as a watch item |
| FTC Disposal Rule (N72-R03) | **Yes** | Background checks (all divisions) and consumer reports in loan files (finance subsidiary) |
| State breach and data security laws (N72-R04) | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example. Florida personal information includes biometric data as defined in s. 501.702 and geolocation (501.171(1)(g)1.a.(VI)-(VII)), which matters for gate templates and the park app |
| Fla. Stat. 509.101(2) | **Yes** | 26 Florida hotels keep a guest register with dates of occupancy and rates; it may be electronic; registers older than 2 years need not be made available |
| Fla. Stat. 501.160 | **Yes (cautious reading)** | The statute names dwelling units and commodities rather than hotels; the group treats room rates during a declared emergency as covered |
| Fla. Stat. 721.13(12)(c) | **Yes** | The managing entity of Florida timeshare plans must keep the records supporting each decision to reserve accommodations for 5 years and produce them to the division on investigation; such records are trade secrets if filed under 721.071 |
| CCPA cybersecurity audit (N53-R03) | **Yes** | 5 California hotels; revenue far above $26,625,000; personal information of more than 250,000 California consumers. First audit report due 2028-04-01 |
| SEC Item 1.05 and Item 106 (N53-R05) | **Yes** | Publicly traded SEC registrant |
| Florida Digital Bill of Rights (Fla. Stat. 501.702) | **No** | A "controller" must exceed $1 billion in global gross annual revenue **and** (a) earn 50% or more of revenue from online advertising, (b) operate a consumer smart speaker and voice command service, or (c) operate an app store with at least 250,000 applications. The group exceeds $1 billion but meets none of (a) to (c) |
| Illinois BIPA (N72-R05) | **No** | No Illinois operations; finger-scan gates run only at the 3 Florida parks. The statute text was not verified (N72-R05 is marked unverified) |
| Gaming rules (N71-R01 to N71-R03) | **No** | No casino or gaming at any park or resort |
| HIPAA | **No** | Park first-aid stations do not bill health plans electronically |
| CIRCIA (N72-R06) | **Not in force** | Final rule not published as of 2026-09-25. The proposed size criterion would cover the group |

## 2. Regulation-by-division matrix
| Requirement | Hotels | Attractions | Vacation Ownership | Group (corporate) |
|---|---|---|---|---|
| PCI DSS v4.0.1 (N72-R01, N71-R04, N53-R04) | **Primary.** Merchant ROC and service provider ROC | **Primary.** Merchant ROC | Applies. SAQ D for Merchants | SYS-G4 shared CDE in all three validations |
| FTC Act Section 5 (N72-R02, N71-R05, N53-R02) | Applies, including managed hotel systems (*Wyndham*) | Applies (app and biometric data) | Applies | Applies (privacy notices; guest profile hub) |
| FTC Safeguards Rule (N53-R01) | Not applicable | Not applicable | **Primary.** Finance subsidiary | Applies to the guest profile hub and shared services that hold customer information |
| FTC Red Flags Rule; Regulation B | Not applicable | Not applicable | Applies (finance subsidiary) | Group AI standard (P10) |
| COPPA Rule (N71-R06) | Not applicable (no child-directed service) | **Primary for the kids' club** | Not applicable | Group policy POL-04 |
| 16 CFR Part 464 | Applies (room rates, resort fees) | Applies (live-event tickets) | Applies (vacation rentals) | Not applicable |
| Fla. Stat. 509.101; 501.160 | Applies (26 Florida hotels) | Not applicable | Not applicable | Not applicable |
| Fla. Stat. 721.13(12)(c) | Not applicable | Not applicable | Applies (Florida plans) | Not applicable |
| State breach laws (N72-R04) | Applies; third-party agent to managed hotel owners | Applies; biometric and geolocation data | Applies | **Coordinates** (P08) |
| CCPA and CPPA regulations (N53-R03) | Applies (5 California hotels) | Applies | Applies except GLBA-covered loan data | Cybersecurity audit run by group internal audit |
| SEC Item 1.05 and Item 106 (N53-R05) | Via group | Via group | Via group | **Applies** |
| Gaming rules (N71-R01 to N71-R03) | Not applicable | Not applicable (no gaming) | Not applicable | Not applicable |
| CIRCIA (N72-R06) | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |

## 3. Method
1. **Requirements.** PCI DSS was broken into its requirement groups, with 14 defined requirements on their own rows because they are service-provider-only or carry the largest risk, plus the appendices. **Labels are short topics written for this analysis, not PCI SSC text**, because PCI DSS is copyrighted; read the requirement text in the group's licensed copy of v4.0.1. Attractions and Vacation Ownership rows cover the requirements where their evidence differs from Hotels; every other requirement relies on the same group common controls (P02 common control catalog). Safeguards Rule, COPPA, Red Flags, Regulation B, and Part 464 rows were read from the eCFR (versions as of 2026-09-23); Florida rows from the Florida Legislature's 2026 statutes; SEC rows from 17 CFR 229.106 and Form 8-K Item 1.05.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS, the Safeguards Rule, or COPPA was used.
3. **Evidence.** Interviews, document review, configuration exports, the 2026 penetration and segmentation tests, a mailbox discovery scan (2026-06), price display and chatbot tests, a sample of 60 adverse action notices, and the P07 assessment results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 scale and given an owner and a date. Where a gap matches a P01 risk, the gap carries the same level.

## 4. Results
### 4.1 Hotels and group-wide obligations (`gap-analysis.csv`)
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 3 | 2 | 0 | 0 | 5 |
| PCI Req 2 Secure configurations | 2 | 1 | 0 | 0 | 3 |
| PCI Req 3 Stored account data | 5 | 2 | 0 | 0 | 7 |
| PCI Req 4 Transmission | 2 | 0 | 0 | 0 | 2 |
| PCI Req 5 Malware and phishing | 3 | 1 | 0 | 0 | 4 |
| PCI Req 6 Secure systems and software | 5 | 1 | 0 | 0 | 6 |
| PCI Req 7 Restrict access | 3 | 0 | 0 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 2 | 5 | 0 | 0 | 7 |
| PCI Req 9 Physical access and devices | 4 | 1 | 0 | 0 | 5 |
| PCI Req 10 Logging | 6 | 2 | 0 | 0 | 8 |
| PCI Req 11 Security testing | 6 | 1 | 0 | 0 | 7 |
| PCI Req 12 Policies and programs | 10 | 5 | 0 | 0 | 15 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **Hotels PCI DSS subtotal** | **51** | **21** | **0** | **3** | **75** |
| Hotels: FTC Act Section 5 | 1 | 1 | 0 | 0 | 2 |
| Hotels: 16 CFR Part 464 | 5 | 0 | 1 | 0 | 6 |
| Hotels: FTC Disposal Rule | 1 | 0 | 0 | 0 | 1 |
| Hotels: Fla. Stat. 509.101(2) and 501.160 | 1 | 1 | 0 | 0 | 2 |
| Group: FTC Act Section 5 | 0 | 2 | 0 | 0 | 2 |
| Group: state breach laws and Fla. Stat. 501.171 | 0 | 5 | 1 | 0 | 6 |
| Group: CCPA cybersecurity audit | 0 | 1 | 0 | 0 | 1 |
| Group: SEC Form 8-K Item 1.05 and Reg S-K Item 106 | 5 | 3 | 0 | 0 | 8 |
| Group: Florida Digital Bill of Rights, BIPA, CIRCIA | 0 | 0 | 0 | 3 | 3 |
| **Total (106)** | **64** | **34** | **2** | **6** | **106** |

**Hotels PCI DSS: 51 Met, 21 Partially met, 0 Not met, 3 N/A.** The partially met rows are concentrated in Requirements 8 and 12 and come from five sources: the shared legacy POS and its vendor (5.2, 6.3, 8.2, 8.3, 8.4, 8.4.2, 10.4, 10.4.1.1, 12.8), the CRS integration credential (8.6), building systems and managed-hotel inventories (1.2, 2.2, 9.5, 11.4), the owner relationship (1.4, 12.9.1, 12.9.2), and card handling and process items (3.2, 3.4, 12.6, 12.10). None is in the tokenization service or the card vault, which the QSA tested without exceptions. Four of these rows (5.2, 8.2, 8.3, 10.4.1.1) are the 2025 ROC compensating controls, which must be revalidated before the 2026 QSA fieldwork.

**Not met:** G-079 (the guest chatbot quotes nightly rates without the mandatory resort fee at 6 resort hotels, 16 CFR 464.2) and G-094 (no retention schedule for 52 million guest profiles, Fla. Stat. 501.171(8)).

Gap risk levels in this table: 10 High, 23 Moderate, 3 Low.

### 4.2 Attractions (`gap-analysis-attractions.csv`)
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS (20 selected rows) | 11 | 9 | 0 | 0 | 20 |
| COPPA Rule (16 CFR Part 312) | 2 | 5 | 7 | 0 | 14 |
| FTC Act Section 5 | 1 | 1 | 0 | 0 | 2 |
| Fla. Stat. 501.171 (biometric and geolocation data; disposal) | 0 | 1 | 1 | 0 | 2 |
| 16 CFR Part 464 (live-event tickets) | 0 | 1 | 0 | 0 | 1 |
| Gaming rules (N71-R01 to N71-R03) | 0 | 0 | 0 | 3 | 3 |
| **Total (42)** | **14** | **17** | **8** | **3** | **42** |

**COPPA is the Attractions problem, not PCI DSS.** The PCI gaps repeat the Hotels findings for the shared legacy POS at 96 kiosks and carts, plus 3 agency-built ticket microsites without script controls (6.4.3, 11.6.1). The kids' club has 7 Not met rows: no written children's information security program (312.8(b)) or annual evaluation (312.8(b)(5)); no written retention policy (312.10) and therefore none in the online notice (312.4(d)); one email consent that covers both collection and disclosure to a marketing analytics vendor (312.5(a)(2)), which also makes email-plus consent unavailable (312.5(b)(2)(viii)); and no written security assurances from that vendor (312.8(c)). The feed to the analytics vendor was stopped on 2026-09-01 until separate consent and assurances exist.

Gap risk levels: 9 High (7 COPPA, plus 5.2 and 8.4.2), 13 Moderate, 3 Low.

### 4.3 Vacation Ownership (`gap-analysis-vacation-ownership.csv`)
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FTC Safeguards Rule (16 CFR 314.3-314.4) | 7 | 12 | 5 | 0 | 24 |
| FTC Red Flags Rule (16 CFR 681.1) | 1 | 3 | 0 | 0 | 4 |
| Regulation B (12 CFR 1002.9) | 1 | 1 | 0 | 0 | 2 |
| Fla. Stat. 721.13(12)(c) | 0 | 0 | 1 | 0 | 1 |
| PCI DSS SAQ D (10 selected rows) | 3 | 7 | 0 | 0 | 10 |
| 16 CFR Part 464, Disposal Rule, FTC Act Section 5 | 2 | 1 | 0 | 0 | 3 |
| **Total (44)** | **14** | **24** | **6** | **0** | **44** |

**Safeguards Rule Not met:** encryption at rest for the loan document archive (314.4(c)(3)); MFA for 340 users without the Qualified Individual's written approval of an equivalent (314.4(c)(5)); testing that excluded the legacy data center (314.4(d)(2)); service provider assessments lapsed for 12 of 31 providers (314.4(f)(3)); and no FTC notification procedure (314.4(j)). **Also Not met:** decision records for the inventory forecasting model (Fla. Stat. 721.13(12)(c)).

The governance elements are in place: a Qualified Individual, a written risk assessment (P01), and the first annual written report to the finance subsidiary board on 2026-09-10. The gaps are technical controls that the acquired division never brought up to the group baseline, which is why most close when the division moves to SYS-G1, group EDR, and the SIEM (POAM-006, POAM-020).

Gap risk levels: 3 High (314.4(c)(1), (c)(3), (c)(5)), 22 Moderate, 5 Low.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Legacy POS vendor access, no EDR, late patches (1) | Hotels, Attractions | PCI 5.2, 6.3, 8.2, 8.4, 8.4.2, 12.8; 45(a)(1), 45(n) | High | Vendor through PAM by 2026-12-31; revalidate compensating controls; P2PE replacement by 2027-06-30 | Group CISO | 2027-06-30 |
| 2 | Guest profile hub credential and owners' bank data (2) | All | PCI 8.6; 314.4(c)(1); 45(n) | High | Least privilege for the CRS integration account; 90-day rotation; bank data out of the hub (POAM-003, POAM-013) | Group Chief Privacy Officer | 2026-12-31 |
| 3 | Safeguards Rule technical controls (3) | Vacation Ownership | 314.4(c)(3), (c)(5), (c)(8), (d)(2), (f)(3) | High | Encrypt the archive; MFA; SIEM; test the legacy data center; assess 12 providers (POAM-006, POAM-010, POAM-020 to POAM-022) | Qualified Individual | 2027-03-31 |
| 4 | Kids' club program, consent, and retention (4) | Attractions | 312.4, 312.5(a)(2), 312.5(b)(2)(viii), 312.8(b)-(c), 312.10 | High | Written program; separate consent; retention policy; vendor assurances (POAM-017, POAM-018, POAM-025) | Attractions digital products director | 2026-12-31 |
| 5 | Door lock default passwords (penetration test) | Hotels | PCI 2.2, 11.4; 45(n) | High | Change, scan, retest (POAM-011) | Hotels vice president of engineering | 2026-10-31 |
| 6 | Biometric gate templates (5) | Attractions | 501.171(1)(g)1.a.(VI), (8); 45(n) | Moderate | Delete 30 days after pass expiry; vendor assurance (POAM-017, POAM-018) | Attractions vice president of park operations | 2027-03-31 |
| 7 | Management agreements and owner responsibility matrices (6) | Hotels | PCI 12.9.1, 12.9.2; state third-party agent duties; 501.171(6) | Moderate | Side letters for 31 pre-2020 agreements; matrix to all 41 ownership groups (POAM-026) | Group General Counsel | 2027-06-30 |
| 8 | Supplements and inheritance (7) | Vacation Ownership, Attractions | 314.3(a); 314.4(g) | Moderate | Re-issue the Vacation Ownership supplement; document inheritance; ride control in the Attractions supplement (POAM-024, POAM-027) | Group CISO | 2026-12-31 |
| 9 | Multi-regulator notification not exercised (8) | All | 314.4(h)-(j); 501.171(3)-(6); Form 8-K Item 1.05; PCI 12.10 | Moderate | Adopt the P08 matrix; cross-division tabletop by 2026-12-15 (POAM-008, POAM-009, POAM-023) | Group General Counsel | 2026-12-15 |
| 10 | AI rules: total price, adverse action reasons, inventory records, emergency pricing (10) | Hotels, Vacation Ownership | 464.2; 1002.9(b)(2); 721.13(12)(c); 501.160 | Moderate | Conditions in P10 (POAM-028, POAM-031, POAM-032) | Group Chief Risk Officer | 2026-12-31 |
| 11 | Guest profile retention (12) | All | 501.171(8) | Moderate | Retention schedule and first purge (POAM-030) | Group Chief Privacy Officer | 2027-03-31 |
| 12 | Red Flags program update | Vacation Ownership | 681.1(d), (e)(3) | Moderate | Update for gallery tablets and synthetic identity patterns (POAM-029) | Finance subsidiary compliance officer | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-025 to POAM-032 trace directly to this analysis.

**Before Hotels QSA fieldwork (starts 2026-10-19):** close G-007 (lock server passwords) and G-054 (retest); refresh the four compensating control worksheets (G-019, G-032, G-033, G-047); and have dated plans for G-034 and G-035. Where a requirement cannot be met by the ROC date, the Group Director of Payments and PCI Compliance agrees the approach with the acquirer and the QSA rather than reporting it "In Place" without evidence.

## 6. Pending regulatory changes and watch items
- **PCI DSS.** v4.0.1 remains current. The 2026 request for comments may lead to a new version; the analysis will be updated when one is published.
- **CIRCIA.** Final rule not published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **CCPA cybersecurity audit.** First audit period 2027-01-01 to 2028-01-01; report due 2028-04-01.
- **Colorado SB26-189** (effective 2027-01-01) covers AI that materially influences consequential decisions, including lending and employment. It affects the credit model and the proposed applicant screening tool if used for Colorado consumers or applicants (P10).
- **FTC AI accuracy policy statement** (proposed, July 2026) is not final.
- **Live-event tickets.** Whether general admission theme park tickets fall under 16 CFR 464 is unsettled; the store already shows total price.
- None of these is treated as a current obligation.

## 7. Approval
Approved by the Group CISO and the Group General Counsel on 2026-09-08. The Qualified Individual presented the Vacation Ownership table to the finance subsidiary board, and the roadmap was reviewed by the board risk committee, on 2026-09-10. Next reassessment: 2027-05 to 2027-07, or after a new version of PCI DSS.
