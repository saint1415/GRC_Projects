# Regulatory Gap Analysis: Cris Santos Company | Accommodation and Food Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel with restaurant and bars) |
| Tier / Vertical | Small / Accommodation and Food Services |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, published 2024-06-11). A contractual standard enforced through the two merchant agreements, **not law** (N72-R01) |
| Secondary regulation | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n), with the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N72-R02). Short checks: FTC Disposal Rule 16 CFR 682.3 (N72-R03); Fla. Stat. 509.101(2), 501.171(2) and (8) |
| Assessment dates | 2026-07-13 to 2026-07-24; evidence refreshed with P07 and P10 results through 2026-08-21 |
| Assessor | IT Manager (Information Security Lead) with the Controller, the Front Office Manager, and the Director of Sales and Marketing |
| Approved | General Manager, 2026-08-31 |

## 1. Applicability

### 1.1 Franchise or independent
**Decision: the hotel is independent, and the company alone owns its PCI program.** A franchised hotel usually has to use the brand's mandated PMS and network and follow the brand's PCI program, so part of the control set is shared with the franchisor. The hotel left its brand in 2021. Since then no franchisor designs, connects, or monitors its systems.

The key precedent on hotel security is *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24). The Third Circuit affirmed that the FTC can challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), and that the company had fair notice. The FTC alleged that the franchisor, which managed its branded hotels' PMS systems, allowed card data in clear text, easy and default passwords, no firewalls between hotel PMS systems, its network, and the internet, an out-of-date operating system, unrestricted vendor access, and weak detection and incident response. Three intrusions in 2008 and 2009 were alleged to have exposed over 619,000 accounts and caused at least $10.6 million in fraud loss. For an independent hotel the lesson applies directly: **the FTC measures the hotel's own practices, and several of them match the Wyndham list today** (rows G-007, G-010, G-003, G-032, G-034, G-045).

### 1.2 PCI DSS, merchant level, and SAQ type
**PCI DSS applies by contract** to both merchant accounts. PCI SSC sets no size tiers; card brands and acquirers set merchant levels and validation methods. Visa's program page says a merchant's total Visa transaction volume over 12 months determines its level, but the level thresholds could not be retrieved from a Visa primary source, so **no level number is stated here**. The acquirer's letter of 2026-05-20 (fictional) confirms that the hotel validates by annual self-assessment questionnaire (SAQ), with no Report on Compliance. The hotel runs about 97,000 card transactions a year across all brands (section 1 of `../00_company-facts.md`).

**The SAQ type follows the payment design, not the merchant's size.** PCI SSC published the SAQs for v4.0.1 on 2024-10-15 (PCI SSC bulletin). The v4 SAQ family (PCI SSC blog, 2024-03-27) includes SAQ A, A-EP, B, B-IP, C-VT, C, P2PE, SPoC, and D (separate versions for merchants and service providers). Eligibility was tested channel by channel:

| Channel | Design | SAQ tested | Result |
|---|---|---|---|
| Booking engine (MID-1) | Vendor-hosted payment page on the vendor's own address; hotel receives a token | SAQ A | Would fit on its own, but MID-1 also carries the front desk channels |
| Front desk card-present (MID-1) | Chip terminals, semi-integrated, **not** a validated P2PE solution, on the flat staff network | SAQ B-IP, SAQ P2PE | Not eligible: terminals are not standalone on their own network zone and are not P2PE |
| Phone and card forms (MID-1) | Staff key card numbers into the PMS in a browser on general-purpose PCs; forms stored in email | SAQ C-VT, SAQ C | Not eligible: the PMS is not a virtual terminal on an isolated computer, and card data is **stored electronically** (email) |
| Online travel agency virtual cards (MID-1) | Full numbers displayed in the PMS on front office PCs | SAQ A | Not eligible: hotel systems display and process card data |
| Restaurant and bars (MID-2) | Validated P2PE solution listed by PCI SSC; no electronic storage | SAQ P2PE | **Eligible**, as long as the P2PE Instruction Manual is followed |

**Result:** MID-1 Rooms must validate on **SAQ D for Merchants** for 2026; MID-2 Food and beverage on **SAQ P2PE**. The acquirer agreed by email on 2026-08-12 (fictional). The 2025 **SAQ A for both accounts was the wrong questionnaire**. It was signed on a vendor salesperson's advice without scoping (row G-059).

**Scope reduction for 2027.** If the hotel (a) purges stored card data and stops accepting card forms by email, (b) moves front desk and phone payments to a validated P2PE solution with keypad entry, (c) charges virtual cards through the PMS without displaying them, and (d) keeps the booking engine fully outsourced, MID-1 could move to SAQ P2PE plus SAQ A, **subject to acquirer approval and a QSA scoping review**. This is the single most valuable change: it removes most of the 55 PCI gaps below from scope rather than fixing them one by one.

**Current version.** PCI DSS v4.0.1 is the current version. Its publication added no new requirements; the requirements introduced as future-dated in v4.0 have been in force since 2025-03-31 (PCI SSC blog, 2024-06-11). PCI SSC ran a request for comments on v4.0.1 from 2026-06-03 to 2026-07-20 toward the next version.

### 1.3 Secondary regulation and short checks
- **FTC Act Section 5** applies with no size threshold. The FTC may treat broken privacy or security promises as deceptive (45(a)(1)) and unreasonable security as unfair if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits (45(n)).
- **16 CFR Part 464** (90 FR 2066, 2025-01-10; effective 2025-05-12; no amendments as of 2026-09-23 on eCFR) covers "short-term lodging, including temporary sleeping accommodations at a hotel" (464.1). Any offer, display, or advertisement of a price must show the **total price**, including mandatory fees such as the $35 amenity fee, more prominently than other pricing (464.2(a)-(b)). Government taxes may be excluded but must be disclosed with the final amount before the guest pays (464.1, 464.2(c)). Fees must not be misrepresented (464.3). This bears on the AI pricing and chatbot use cases (P10).
- **FTC Disposal Rule** (16 CFR 682.3): the hotel obtains background-check reports on applicants.
- **Fla. Stat. 509.101(2)**: each transient establishment must keep a chronological guest register with dates of occupancy and rates, available to the division for inspection, and may keep it electronically. Registers more than 2 years old need not be made available. This sets a **2-year floor** for register data, not a reason to keep everything forever.
- **Fla. Stat. 501.171(2) and (8)**: reasonable security for electronic personal information, and disposal of customer records when they are no longer to be retained. Breach notice under 501.171(3)-(6) is handled in P08.

**Not applicable, with reasons:** CIRCIA (proposed only; the hotel is below the SBA size standard), Illinois BIPA (no Illinois operations), FTC Safeguards and Red Flags Rules (no consumer credit), CCPA (no California business and revenue below $26,625,000), HIPAA, and SEC disclosure.

## 2. Method
1. **Requirements.** PCI DSS was broken down into its 12 principal requirements and their requirement groups, plus the appendices. Three items were taken to the defined-requirement level because they decide scope or carry the largest risk: 3.3.1, 6.4.3, and 11.6.1. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard. Group numbers come from the company's licensed copy of v4.0.1.
2. **FTC, Part 464, and Florida rows** cite the text verified on uscode.house.gov, eCFR (2026-09-23), the Federal Register, and the Florida Legislature's 2026 statutes.
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** No official NIST mapping from PCI DSS v4.0.1 was used.
4. **Evidence.** Interviews (majority owner, General Manager, Controller, Front Office Manager, Director of Sales and Marketing, Chief Engineer, MSP lead technician), document review (2025 SAQs, merchant agreements, acquirer letter, vendor AOCs and SOC 2 report, privacy policy), configuration exports (firewall, PMS permissions and users, identity provider), a mailbox search on 2026-07-20, a network scan on 2026-07-16, and a hotel walkthrough on 2026-07-15.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 3 | 2 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 0 | 0 | 5 | 2 | 7 |
| PCI Req 4 Transmission | 0 | 1 | 1 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 0 | 1 | 4 | 1 | 6 |
| PCI Req 7 Restrict access | 1 | 1 | 1 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 1 | 2 | 3 | 0 | 6 |
| PCI Req 9 Physical access and devices | 0 | 3 | 2 | 0 | 5 |
| PCI Req 10 Logging | 0 | 2 | 5 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 5 | 1 | 6 |
| PCI Req 12 Policies and programs | 1 | 4 | 3 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **3** | **21** | **34** | **9** | **67** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| 16 CFR Part 464 (fees) | 1 | 1 | 2 | 0 | 4 |
| FTC Disposal Rule | 0 | 1 | 0 | 0 | 1 |
| Florida Statutes (509.101, 501.171) | 1 | 1 | 1 | 0 | 3 |
| **Total (78)** | **5** | **26** | **38** | **9** | **78** |

Of the 64 rows with gaps, 13 are rated High, 31 Moderate, and 20 Low.

**MID-2 (SAQ P2PE).** The restaurant channel is affected only by rows marked "MID-2 SAQ P2PE" in `applies_at_this_tier`: 3.1, 3.2, 3.3.1, 9.1, 9.4, 9.5, 12.1, 12.5, 12.6, 12.8, and 12.10. Its main gaps are device inspections (9.5) and the shared program gaps. The restaurant does not handle card forms, so 3.2 and 3.3.1 findings come from MID-1.

## 4. Priority gaps and roadmap
| Gap | Row | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Security codes kept on card forms | G-011 (3.3.1) | High | Purge now; never collect the code | Controller | 2026-09-30 |
| Card forms in email and an unlocked binder | G-010 (3.2), G-040 (9.4) | High | Purge; payment links replace forms; lock and retire the binder | Controller; Front Office Manager | 2026-10-31 |
| Shared, stale, and standing vendor accounts | G-032 (8.2) | High | Named accounts; same-day removal; on-request vendor access | IT Manager | 2026-10-31 |
| No MFA for PMS users or vendor remote tools | G-034 (8.4) | High | Single sign-on with MFA for all PMS users; MFA on remote tools | IT Manager | 2026-10-31 |
| Excess card-display rights | G-029 (7.2) | High | Remove from 11 users; reviews every 6 months | Front Office Manager | 2026-10-31 |
| Lock server default password | G-007 (2.2) | High | Change now; hardening standard | IT Manager | 2026-10-31 |
| No vulnerability or ASV scans | G-051 (11.3) | High | Quarterly internal and ASV scans | IT Manager | 2026-10-31 |
| No incident response plan | G-064 (12.10) | High | POL-03 and P08; tabletop | IT Manager | 2026-11-30 |
| Flat staff network | G-003 (1.3) | High | Payment, lock, CCTV, and office VLANs | IT Manager | 2026-12-31 |
| Wrong SAQ; no scope document | G-059 (12.5) | High | Scope document; QSA scoping review; SAQ D and SAQ P2PE | Controller | 2026-12-31 |
| Unsupported lock server | G-024 (6.3) | High | Upgrade with the lock vendor | Chief Engineer | 2027-03-31 |
| Security not yet reasonable (FTC) | G-068 (45(a), 45(n)) | High | Execute P01 and P07 plans | General Manager | 2027-01-31 |
| False "we do not store card data" claim | G-069 (45(a)(1)) | Moderate | Rewrite privacy policy | Director of Sales and Marketing | 2026-09-30 |
| Partial prices in chatbot, phone quotes, and website banner; wrong fee description | G-071, G-072, G-074 (464.2, 464.3) | Moderate | Total price first everywhere; correct fee description | Director of Sales and Marketing | 2026-09-30 |
| No retention schedule | G-078 (501.171(8)) | Moderate | Register 2 years; ID scans checkout plus 30 days | Front Office Manager | 2026-12-31 |

**Before signing the 2026 SAQs (due 2026-12-31):** complete G-011, G-010, G-059, and G-051 (passing ASV scans are needed for SAQ D), and have compensating or remediated status for every other SAQ D requirement. Where a requirement cannot be met by the due date, the Controller should agree the reporting approach with the acquirer rather than attest "In Place" without evidence, which is what happened in 2025.

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 remains current. The 2026 request for comments may lead to a new version; the analysis will be updated when one is published.
- **FTC fee rules.** A proposed FTC rulemaking on fees for food and grocery ordered through online delivery platforms (91 FR 20381, 2026-04-16; comments closed 2026-05-18) is not final and targets delivery platforms, not restaurants.
- **FTC AI accuracy policy statement** (proposed, July 2026) is not final (P10).
- **CIRCIA** final rule not published as of 2026-09-25.
- None of these is treated as a current obligation.
