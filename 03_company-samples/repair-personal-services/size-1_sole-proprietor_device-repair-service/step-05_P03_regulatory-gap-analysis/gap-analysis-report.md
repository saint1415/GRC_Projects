# Regulatory Gap Analysis: Cris Santos Company | Other Services (except Public Administration) | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service, NAICS 811210) |
| Tier / Vertical | Sole Proprietorship / Other Services (except Public Administration) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary benchmark: no sector cybersecurity rule applies** (section 1). Label `N81-BM` in the other deliverables |
| Secondary (binding law) | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n) (N81-R01); Florida Information Protection Act, Fla. Stat. 501.171 (2026) (N81-R02), plus other states' breach laws |
| Secondary (binding by contract) | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (October 2024) (N81-R03) |
| Sanitization reference | NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of December 2014) |
| Assessment dates | 2026-07-20 to 2026-07-27 (self-assessment). SYS-01 note search and shop walkthrough 2026-07-20; bench PC and email checks 2026-07-27 |
| Assessor | Owner-technician, with the independent security consultant on the two on-site days. **Evidence is self-attested**, checked on screen where possible |
| Workbook | `gap-analysis.csv` (144 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
**No sector cybersecurity regulation applies.** No federal agency issues cybersecurity rules for repair shops, and the vertical research (`02_industry-rules/repair-personal-services/`) names NIST CSF 2.0 as the benchmark for that reason. The shop's binding duties come from general law and its merchant agreement. Each candidate was checked against its source text:

| Requirement | Test (source text) | Decision |
|---|---|---|
| **FTC Act Section 5** (N81-R01) | 45(a)(1) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful. 45(n): a practice is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition." No size threshold | **Applies.** The shop is a for-profit business in commerce. Deception covers the intake form promise and the website's wiping claim; unfairness covers how customer devices and data are handled (rows G-107 to G-109) |
| **Fla. Stat. 501.171** (N81-R02) | "Covered entity" means "a sole proprietorship, partnership, corporation, trust, estate, cooperative, association, or other commercial entity that acquires, maintains, stores, or uses personal information" ((1)(b)). Personal information includes a name with a card number plus a required code, a name with medical, biometric, or geolocation information, and "a user name or e-mail address, in combination with a password or security question and answer that would permit access to an online account" ((1)(g)) | **Applies, by name.** Unlike many laws, this one lists the sole proprietorship expressly. SYS-01 holds about 85 email and password pairs, and sticky notes held card numbers with security codes. Subsections (2) to (6) and (8) are rows G-110 to G-115 |
| **PCI DSS v4.0.1** (N81-R03) | Contractual, through the merchant agreement. The processor asks for SAQ P2PE. The v4.0.1 SAQ P2PE (October 2024) eligibility: all processing through a validated PCI-listed P2PE solution, no other electronic receipt, transmission, or storage of account data, any retained account data on paper only, and all PIM controls in place | **Applies by contract.** Eligibility plus the 22 requirement lines are rows G-117 to G-139. Never completed before |
| **FTC Disposal Rule** (N81-R04) | Applies to any person under FTC jurisdiction that possesses "consumer information", meaning a consumer report or information derived from one (16 CFR 682.1(b), 682.2(b)) | **Does not apply at this size.** With no employees and no background checks, the shop holds no consumer reports. The Small sample of this industry is covered only because it runs background checks on technicians. Customer device data is never consumer report information (row G-140) |
| COPPA, HIPAA, FTC Safeguards Rule, Florida Digital Bill of Rights | 16 CFR Part 312; 45 CFR 160.103; 16 CFR 314.1(b); Fla. Stat. 501.702 | **Not applicable** (rows G-141 to G-144 give the reasons; for example a Digital Bill of Rights "controller" must exceed $1 billion in global gross annual revenue) |

**Disposal of customer devices and data.** Repair shops often assume the FTC Disposal Rule governs wiping customer devices. It does not. The duty comes from Fla. Stat. 501.171(8): "all reasonable measures to dispose, or arrange for the disposal, of customer records containing personal information ... by shredding, erasing, or otherwise modifying the personal information in the records to make it unreadable or undecipherable through any means." Customer records are material "provided by an individual in this state to a covered entity for the purpose of ... obtaining a service" ((1)(c)). Intake forms and ticket records clearly qualify. **Author interpretation, for counsel to confirm:** transfer and recovery copies and devices left for recycling qualify too. The shop treats them as customer records either way and uses SP 800-88 Rev. 2 as the method: clear (3.1.1), purge (3.1.2), or destroy (3.1.3), with verification (4.5.1) and a record modeled on the sample certificate of sanitization (Appendix C).

**When looking becomes a breach.** Fla. Stat. 501.171(1)(a) says good-faith access by an employee or agent "does not constitute a breach of security, provided that the information is not used for a purpose unrelated to the business or subject to further unauthorized use." Opening the camera app to test a new camera is good-faith access. Scrolling through a customer's photos is not. POL-01 8.4 writes this line down for the owner and the fill-in technician.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). The FTC and Florida rows follow the statutes' own subsections. PCI DSS rows are the SAQ P2PE eligibility criteria plus each requirement line in the v4.0.1 SAQ P2PE, listed by number with short topic labels written for this analysis. **PCI DSS is copyrighted; read the official SAQ for the text.**
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of key controls from that list. All other rows use an **author mapping**; no official NIST mapping exists for the FTC Act, the Florida statute, or PCI DSS v4.0.1.
3. **Evidence.** Self-attested by the owner and checked on screen with the consultant: a SYS-01 ticket note search (2026-07-20), the counter drawer, router and device settings, the bench PC software and folders, the drop-off bin, email rules, the intake form, the website, and the contract folder.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. A one-person shop marks a CSF outcome Not applicable only when the activity does not exist at all (for example software development).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 8 | 10 | 13 | 0 | 31 |
| IDENTIFY (ID) | 4 | 8 | 8 | 1 | 21 |
| PROTECT (PR) | 4 | 9 | 7 | 2 | 22 |
| DETECT (DE) | 1 | 2 | 8 | 0 | 11 |
| RESPOND (RS) | 0 | 2 | 11 | 0 | 13 |
| RECOVER (RC) | 0 | 2 | 6 | 0 | 8 |
| **CSF 2.0 subtotal** | **17** | **33** | **53** | **3** | **106** |
| FTC Act Section 5 | 0 | 0 | 3 | 0 | 3 |
| Fla. Stat. 501.171 | 0 | 2 | 4 | 0 | 6 |
| Other states' breach laws | 0 | 0 | 1 | 0 | 1 |
| PCI DSS v4.0.1 SAQ P2PE | 1 | 5 | 15 | 2 | 23 |
| Applicability screen | 0 | 0 | 0 | 5 | 5 |
| **Total** | **18** | **40** | **76** | **10** | **144** |

Of the 116 unmet or partially met rows, 9 are rated High, 36 Moderate, and 71 Low.

**Reading the pattern.** Most Met rows are in Govern and Identify, because the first risk assessment and BIA (July 2026) created them. Respond and Recover are almost entirely Not met, which is normal for a one-person business that has never had a plan; most of those rows close together when the P08 runbook is adopted and walked through. **The High gaps sit where a repair shop differs from other small businesses:** what it keeps from customers' devices (G-037, G-038, G-061, G-115), who can sign in and see it (G-053, G-055, G-057), and whether its handling is fair to customers (G-109, G-110).

## 4. Action list (half page)
In order. The first five cost nothing and take less than a day in total.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Shred the 6 card notes; key phone payments straight into the terminal; purge the 4 card numbers in notes | G-117, G-119, G-120, G-124 | Moderate | 2026-09-15 |
| 2 | Bench PC password and lock; remove the "military standards" claim; turn off AI training; sign-in alerts to the phone | G-108, G-061, G-083 | Moderate | 2026-09-15 |
| 3 | Named fill-in SYS-01 account without export rights; new password; MFA on SYS-01 and the camera account | G-053, G-055, G-057 | High | 2026-09-15 to 2026-09-30 |
| 4 | Rewrite the intake notice; adopt the customer data access rules (POL-01 8.4); fill-in agreement with confidentiality terms | G-107, G-016, G-026 | Moderate | 2026-09-30 |
| 5 | Adopt and print the P08 runbook and notification matrix; record and weekly-inspect the terminal | G-052, G-095, G-111, G-112, G-125 to G-127, G-139 | Moderate | 2026-09-30 |
| 6 | Restricted passcode field cleared at release; stop collecting account passwords; purge historical notes | G-037, G-110 | High | 2026-10-31 |
| 7 | Encrypt the bench PC; replace the drives with encrypted drives; delete copies 14 days after delivery; purge the 1.6 TB backlog | G-038, G-061, G-109, G-115 | High | 2026-10-31 |
| 8 | SP 800-88 Rev. 2 procedure and per-device log for drop-off devices | G-038, G-115 | High | 2026-10-31 |
| 9 | Guest and bench Wi-Fi networks; router password and firmware | G-071, G-065, G-066 | Moderate | 2026-10-31 |
| 10 | Vendor list with notice terms; recycler data addendum; AI business terms or stop | G-025, G-026, G-114 | Moderate | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Before signing the 2026 SAQ P2PE (due 2026-12-31):** close G-117, G-119, G-120, G-124, G-126, G-127, and G-129, read the PIM, and keep the evidence (shredding note, purge record, terminal list, inspection log). If card numbers turn up electronically again, the owner must not attest to the eligibility criteria and must ask the processor how to validate.

## 5. Watch items
None of these is a current obligation.
- **PCI DSS.** v4.0.1 is the current version. Recheck the PCI SSC standards page before each annual SAQ.
- **NIST SP 800-88 Rev. 2** (September 2025) is final and is the method used here. It points to IEEE 2883 for technology-specific techniques.
- **FTC AI accuracy policy statement** (Docket FTC-2026-0727, proposed July 2026, per `00_universal-framework/cross-sector/`) is not final. Relevant only if the shop ever makes claims about AI diagnostics (P10).
- **Florida.** Fla. Stat. 501.171 is read as in force in 2026. Recheck each July.
- **First hire.** Hiring an employee or running a background check would bring in the FTC Disposal Rule (N81-R04) and the workforce rows of CSF (GV.RR-04, PR.AT-01) at full weight.
