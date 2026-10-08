# Regulatory Gap Analysis: Cris Santos Company Holdings | Other Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Other Services (except Public Administration) (focus division: Device Repair) |
| Primary benchmark (focus division) | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary: no sector cybersecurity rule applies to device repair** (section 1). Label `N81-BM` in the other deliverables |
| Binding rules for Device Repair | FTC Act Section 5 (N81-R01); state breach, data security, and disposal law, with Fla. Stat. 501.171 (2026) as the worked example (N81-R02); FTC Disposal Rule for background check reports only (N81-R04); PCI DSS v4.0.1 by contract (N81-R03); manufacturer, TPA, and enterprise contracts |
| Division rule sets | Electronics Retail: PCI DSS v4.0.1 as its primary standard (N44-45-R01) with FTC Act, FACTA, and applicability screens. IT Support Services: an applicability finding for its vertical's primary rule (FTC Safeguards Rule, N54-R01), the HIPAA Security Rule as a business associate (N54-R06), PCI DSS service provider duties, SOC 2 commitments, and the FTC Act |
| Gap tables | `gap-analysis.csv` (Device Repair, 148 rows); `gap-analysis-electronics-retail.csv` (67 rows); `gap-analysis-it-support.csv` (37 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads and division counsel, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit. The QSA was not involved; this is the internal pre-assessment before both 2026-2027 ROCs |

## 1. Applicability
### 1.1 What binds each division, at this size
| Division | Rule | Why it applies (or not) |
|---|---|---|
| Device Repair | NIST CSF 2.0 (benchmark) | No federal agency issues cybersecurity rules for repair businesses. The vertical profile names CSF 2.0 as the benchmark for that reason, and nothing about a 17,500-person national chain changes it. Size changes the depth (all 106 subcategories, evidence from a formal assessment), not the answer |
| Device Repair | FTC Act Section 5 | 15 U.S.C. 45(a)(1) and 45(n); no size threshold. The division is a for-profit business in commerce |
| Device Repair | Fla. Stat. 501.171 and other states' laws | A covered entity is a "commercial entity that acquires, maintains, stores, or uses personal information" (501.171(1)(b)). Personal information includes "a user name or e-mail address, in combination with a password or security question and answer that would permit access to an online account" (501.171(1)(g)1.b.), which the STPP holds in notes for about 96,000 customers, as well as medical, biometric, and geolocation information that customer devices carry |
| Device Repair | PCI DSS v4.0.1 | Contractual. The division is a separate merchant with about 6.7 million Visa transactions a year. Visa assigns **Level 1** to merchants processing over 6 million Visa transactions a year across all channels and requires an annual ROC by a QSA (or an internal resource if signed by an officer) and an AOC; merchant level is based on the corporate entity's total Visa volume (Visa merchant and service provider levels page, read 2026-10-06). The acquirer's letter of 2026-02-16 (fictional) confirms Level 1 |
| Device Repair | FTC Disposal Rule | 16 CFR 682.3; covers consumer report information only (682.1(b)): the technicians' background check reports. **It does not govern wiping customer devices** (section 1.3) |
| Electronics Retail | PCI DSS v4.0.1 | Level 1 merchant (about 74 million card transactions a year); annual ROC by a QSA since 2014 |
| Electronics Retail | FTC Act Section 5; FACTA | No size threshold (15 U.S.C. 45(a), 45(n); 15 U.S.C. 1681c(g)) |
| IT Support | HIPAA Security Rule, Breach Notification Rule (164.410), and Privacy Rule business associate provisions | A business associate of 610 medical and dental practices (45 CFR 160.103), directly subject to Subpart C (164.302). No size exemption; 164.306(b) lets the division consider its size and capabilities in choosing *how* to comply |
| IT Support | FTC Safeguards Rule (the professional services vertical's primary rule) | **Does not bind the division directly** (section 1.4) |
| IT Support | PCI DSS v4.0.1 service provider duties | It manages point-of-sale networks for 520 merchants, so it can affect their cardholder data security (12.9) |
| Group | SEC Reg S-K Item 106; Form 8-K Item 1.05 | Publicly traded SEC registrant (N52-R08) |
| Group | State comprehensive consumer privacy laws | Several of the 26 states have them (the cross-sector register counts 19 state laws in effect as of 2026-09-25). They are handled by the Group Chief Privacy Officer's privacy program and are outside this security gap analysis |

**Not applicable, with reasons:** the FTC Safeguards Rule for Device Repair and Retail (neither extends credit; rows G-144 and ER-G62); the FTC Red Flags Rule (no covered accounts); HIPAA for Device Repair and Retail (no covered entity or business associate function; the data recovery service is not offered to health care accounts); COPPA (nothing directed to children; loyalty members are 18 or older); the INFORM Consumers Act (no third-party sellers); CCPA and the CPPA regulations (no business in California); the Florida Digital Bill of Rights (the group has more than $1 billion in revenue but meets none of the online advertising, smart speaker, or app store tests in Fla. Stat. 501.702); FAR 52.204-21, DFARS 252.204-7012, and CMMC (no federal contracts). CIRCIA is not in effect (no final rule as of 2026-09-25).

### 1.2 Why Device Repair's PCI scope is small and its ROC still matters
The repair stores and depots use a **PCI-listed validated P2PE solution**, so card data is encrypted in the terminal and the STPP, bench workstations, and store networks never see it. The online booking page uses the processor's hosted payment fields. That keeps most of the division out of scope, which is why only 22 rows apply. Level 1 still means a ROC, not a self-assessment. The QSA will look hardest at what can break the P2PE assumption: card numbers keyed or written outside terminals for phone payments (G-118, G-121, G-122), paper at depot cashier desks (G-129), and the booking page scripts (G-126, G-133). Shared bench logins are a serious problem (G-053), but not a PCI DSS one, because benches never touch card data.

### 1.3 The disposal question at a national scale
Repair businesses often assume the FTC Disposal Rule governs wiping customer devices. It does not: it covers consumer report information only (16 CFR 682.1(b)). For customer devices and records the duty comes from Fla. Stat. 501.171(8), which requires "all reasonable measures to dispose, or arrange for the disposal, of customer records containing personal information ... by shredding, erasing, or otherwise modifying the personal information in the records to make it unreadable or undecipherable through any means," and from the equivalent laws of other states. Customer records are material "provided by an individual in this state to a covered entity for the purpose of purchasing or leasing a product or obtaining a service" (501.171(1)(c)). Intake forms and tickets clearly qualify. **Author interpretation, for counsel to confirm:** trade-in devices (about 1.1 million a year, bought by Retail), recycling drop-offs (about 640,000 a year), and recovered data copies also qualify. The group treats them as customer records either way and uses **NIST SP 800-88 Rev. 2** (September 2025; it supersedes Rev. 1 of December 2014) as the method: clear, purge, or destroy (Section 3.1), IEEE 2883 for media-specific techniques, verification (4.5.1), and the sample certificate of sanitization (Appendix C).

### 1.4 Why the professional services primary rule does not bind IT Support directly
The Safeguards Rule applies to financial institutions, which 16 CFR 314.2(h) defines by financial activity. Its examples include "an accountant or other tax preparation service that is in the business of completing income tax returns" (314.2(h)(2)(viii)). IT Support prepares no returns and extends no credit, so it is not one. It is a **service provider** (314.2(r)) to 380 accounting and tax firms that are. Those firms must select capable providers, require safeguards by contract, and assess providers periodically (314.4(f)). The rule therefore reaches IT Support through contracts and due diligence (IT-G28), and the division's real binding regulation is HIPAA, as a business associate of 610 practices.

### 1.5 When a technician's access becomes a breach
Fla. Stat. 501.171(1)(a) excludes "good faith access of personal information by an employee or agent of the covered entity ... provided that the information is not used for a purpose unrelated to the business or subject to further unauthorized use." Opening the camera app to test the camera is good-faith access. Browsing or copying a customer's photos is not. With 37 complaints in 2025-2026 and no session record at stores, the division cannot show which side of that line most access falls on (G-094). That is why bench session logging is both a security control and a breach-scoping tool (P08).

### 1.6 FTC precedent
A search of ftc.gov found no FTC enforcement action against a repair business for technician snooping. The closest precedent is *In re DesignerWare, LLC* and seven rent-to-own operators (complaints announced 2012-09-25; final orders 2013-04-15): the FTC treated covert collection of data from consumers' rented computers as unfair and banned it. The FTC's May 2021 report *Nixing the Fix* found no empirical evidence that independent repair shops are more or less likely than authorized ones to compromise customer data. The lesson for the group is the same as for a small shop: its duty does not depend on authorized status, and its statements about technician access must be true (G-107).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Regulation-by-division matrix
| Requirement | Device Repair | Electronics Retail | IT Support Services | Group (corporate) |
|---|---|---|---|---|
| N81-BM NIST CSF 2.0 | **Primary benchmark** (all 106 subcategories) | Used for program reporting | Used for program reporting | Group policies aligned to it |
| N81-R01 / N44-45-R02 FTC Act Section 5 | Applies (intake notice, AI claims, device handling) | Applies (privacy notice, security; facial recognition precedent) | Applies (support claims; session handling) | Applies |
| N81-R02 State breach, data security, and disposal laws (Fla. Stat. 501.171 worked example) | Applies (covered entity; third-party agent of the TPA) | Applies (covered entity) | Applies (third-party agent for customers' data) | Coordinates notices (P08) |
| N81-R03 / N44-45-R01 PCI DSS v4.0.1 | **Applies.** Level 1 merchant; validated P2PE; ROC due 2027-03-31 | **Primary.** Level 1 merchant; ROC due 2026-12-15 | Service provider duties (12.9) for 520 POS network customers | Common controls in both responsibility matrices |
| N81-R04 FTC Disposal Rule | Applies (background reports) | Applies (background reports) | Applies (background reports) | Group HR (SYS-G5) |
| N81-R05 / N44-45-R07 COPPA | Not applicable | Not applicable | Not applicable | Not applicable |
| N81-R06 HIPAA (as covered entity) | Not applicable | Not applicable | Not a covered entity | Not applicable |
| N54-R06 HIPAA as business associate | Not applicable (no health care data recovery) | Not applicable | **Applies** (610 practices) | Group SOC and identity support it under the division's subcontractor terms |
| N54-R01 / N44-45-R03 FTC Safeguards Rule | Not applicable | Not applicable (co-branded card issued by a bank) | Through customer contracts only (314.4(f)) | Not applicable |
| N44-45-R05 FACTA truncation | Applies (receipts at repair stores) | Applies | Not applicable (no card receipts) | Not applicable |
| N44-45-R06 CCPA; N44-45-R08 INFORM | Not applicable | Not applicable | Not applicable | Not applicable |
| N54-R04 / N54-R05 FAR, DFARS, CMMC | Not applicable | Not applicable | Not applicable (no federal contracts) | Not applicable |
| N54-R09 CIRCIA (proposed) | Tracked only | Tracked only | Tracked only (proposed IT entity criteria) | Tracked only |
| N52-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** |
| State comprehensive privacy laws | Group privacy program | Group privacy program | Group privacy program | Group Chief Privacy Officer |
| Contracts | Manufacturer A and B (24-hour notice); TPA (48-hour notice); enterprise depot contracts (72-hour notice); repair merchant agreement (24-hour notice) | Retail merchant agreement (24-hour notice) | BAAs (10 days standard; 5 business days for 47 practices); managed services contracts; SOC 2 | Intercompany service agreements |

## 3. Method
1. **Requirements.** Device Repair's benchmark rows are every CSF 2.0 subcategory, quoted from the CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). FTC Act, Florida, and Disposal Rule rows follow the statutes' own subsections (Fla. Stat. 501.171 read in its 2026 text on the Florida Legislature's official statutes site). HIPAA rows and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 through the Health Care crosswalk in `02_industry-rules/health-care/`. **PCI DSS is copyrighted.** Its rows list requirement numbers with short topic labels written for this analysis, not PCI SSC text; read the requirements in the group's licensed copy of v4.0.1.
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`; column `sp800_53_controls` is the author's selection. HIPAA rows carry the Health Care crosswalk's **author mapping** and NIST's official SP 800-66 mapping. All other rows use an **author mapping**; no official NIST mapping exists for PCI DSS v4.0.1, the FTC Act, or the Florida statute.
3. **Evidence.** Interviews with each division's security, compliance, legal, operations, and digital leads; document review (both 2025 ROCs and AOCs, the P2PE listing, acquirer letters, manufacturer and TPA agreements, BAAs, the 2026 SOC 2 report); STPP field searches and a data discovery scan in July 2026; walkthroughs at 24 repair stores, 12 in-store counters, all 5 depots, and both labs; browser captures of both merchants' payment pages; the 2026 retail segmentation test; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 4. Results
### 4.1 Device Repair (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 19 | 12 | 0 | 0 | 31 |
| IDENTIFY (ID) | 9 | 11 | 1 | 0 | 21 |
| PROTECT (PR) | 11 | 10 | 1 | 0 | 22 |
| DETECT (DE) | 8 | 3 | 0 | 0 | 11 |
| RESPOND (RS) | 10 | 3 | 0 | 0 | 13 |
| RECOVER (RC) | 7 | 1 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **64** | **40** | **2** | **0** | **106** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| Fla. Stat. 501.171 | 1 | 5 | 0 | 0 | 6 |
| Other states' breach laws | 0 | 1 | 0 | 0 | 1 |
| FTC Disposal Rule (background reports) | 1 | 0 | 0 | 0 | 1 |
| PCI DSS v4.0.1 (repair merchant) | 11 | 8 | 2 | 1 | 22 |
| Manufacturer, TPA, and enterprise contracts | 0 | 4 | 0 | 0 | 4 |
| Applicability screens | 0 | 0 | 0 | 5 | 5 |
| **Total** | **77** | **60** | **5** | **6** | **148** |

Of the 65 rows with gaps, 18 are rated High, 41 Moderate, and 6 Low.

**Reading the pattern.** The division inherits a mature group program, so GOVERN, DETECT, RESPOND, and RECOVER are mostly Met. Its gaps are where a repair business differs from other businesses: **what technicians can do with customer devices, what credentials the business keeps, which tools run on the bench, and how devices are wiped.** 14 of the 18 High gaps sit in those four areas: bench access (G-053, G-057, G-063, G-094, G-077, G-107), credentials (G-061, G-110, G-109), bench tools (G-022, G-026, G-045, G-047, G-069). The other four are the in-store counter network (G-034, G-071) and disposal (G-038, G-115). The 2 Not met CSF outcomes are both about the bench: software integrity before use (ID.RA-09) and preventing unauthorized software (PR.PS-05).

### 4.2 Electronics Retail (`gap-analysis-electronics-retail.csv`)
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI DSS v4.0.1 (Req. 1 to 12 and appendices) | 45 | 8 | 0 | 2 | 55 |
| FTC Act Section 5 | 2 | 1 | 0 | 0 | 3 |
| FACTA truncation | 1 | 0 | 0 | 0 | 1 |
| Fla. Stat. 501.171 and other states' laws | 0 | 2 | 0 | 0 | 2 |
| Applicability screens (Safeguards, Red Flags, COPPA, INFORM, CCPA, Florida Digital Bill of Rights) | 0 | 0 | 0 | 6 | 6 |
| **Total** | **48** | **11** | **0** | **8** | **67** |

Of the 11 rows with gaps, 5 are High, 4 Moderate, and 2 Low.

**The retail program is mature where it has always been tested.** 45 of 53 applicable PCI DSS rows are Met. Its High gaps are **caused at the boundary with Device Repair**: the in-store counter bench networks reach lanes at 112 stores (1.3, 1.4, 11.4), plus the checkout tag container (6.4.3) and the FTC Act row that summarizes both. Before the QSA closes fieldwork (2026-11-20), the counter networks must be separated and retested, or the group must agree with the QSA and the acquirer how those stores are treated.

### 4.3 IT Support Services (`gap-analysis-it-support.csv`)
| Obligation group | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| HIPAA Security Rule (business associate; 24 selected rows) | 12 | 12 | 0 | 0 | 24 |
| HIPAA Breach Notification (164.410) and Privacy Rule business associate provisions | 0 | 3 | 0 | 0 | 3 |
| FTC Safeguards Rule (applicability finding; customer flow-down) | 0 | 1 | 0 | 0 | 1 |
| PCI DSS v4.0.1 service provider duties (12.9) | 1 | 1 | 0 | 0 | 2 |
| SOC 2 commitments | 0 | 1 | 0 | 0 | 1 |
| FTC Act Section 5 and state third-party agent duties | 1 | 2 | 0 | 0 | 3 |
| Applicability screens (FAR, DFARS and CMMC, CIRCIA) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **14** | **20** | **0** | **3** | **37** |

Of the 20 rows with gaps, 3 are High, 13 Moderate, and 4 Low. Of the 12 partially met Security Rule rows, 6 are Required implementation specifications, 4 Addressable, and 2 standards. **Addressable is not optional:** the division must implement each one, implement an equivalent, or document why neither is reasonable and appropriate (164.306(d)(3)). None is being documented as unreasonable.

**The division's risk is concentration.** Its HIPAA basics are in place (BAAs, unique IDs, encryption, backups, evaluation through SOC 2). The High gaps are about the RMM: risk management of three High risks (164.308(a)(1)(ii)(B)), 14 standing global administrators who could reach every practice (164.308(a)(4)(ii)(B)), and the FTC Act unfairness row that covers consumers' devices. The new AI agent is outside the risk analysis, the subcontractor agreements, and the SOC 2 description (IT-G01, IT-G13, IT-G31).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | In-store counter networks reach retail lanes (3) | DR, ER | PCI DSS 1.3, 1.4, 11.4; CSF PR.IR-01 | High | Separate counter networks at 112 stores; retest | Electronics Retail CISO with the Device Repair CISO | 2026-11-15 |
| 2 | Passcodes and account credentials in notes, transcripts, and attachments (1) | DR, IT, Group | Fla. Stat. 501.171(2); 15 U.S.C. 45(n); 164.308(a)(5)(ii)(D) | High | Vault everywhere; purge; stop collecting account passwords; redact transcripts | Group Chief Privacy Officer | 2027-01-31 |
| 3 | Technician access to device content unrecorded; shared bench logins (2) | DR, IT | 15 U.S.C. 45(a)(1), 45(n); Fla. Stat. 501.171(1)(a); CSF PR.AA-01, PR.DS-10 | High | Named bench accounts; session logging; USB block; signed standard | Device Repair chief operating officer | 2027-03-31 |
| 4 | Bench tool supply chain (5) | DR | CSF GV.SC-01, GV.SC-05, ID.RA-09, PR.PS-05 | High | Review gate; signed updates through the group channel; allow-listing | Device Repair CISO | 2027-03-31 |
| 5 | RMM privileged access (6) | IT | 164.308(a)(4)(ii)(B); 164.308(a)(1)(ii)(B) | High | Break-glass only; phishing-resistant MFA; two-person script approval | IT Support security and compliance lead | 2026-12-31 |
| 6 | Sanitization on SP 800-88 Rev. 2 with per-device records (4) | DR, ER | Fla. Stat. 501.171(8); CSF ID.AM-08 | High | New standard; serial capture for drop-offs; verification sampling at every depot | Device Repair chief operating officer | 2026-12-31 |
| 7 | Payment page scripts on both merchants' pages | DR, ER | PCI DSS 6.4.3, 11.6.1 | High (ER) / Moderate (DR) | Payment-pages-only container; real-time alerts | Group chief digital officer | 2026-11-30 |
| 8 | Card data outside the P2PE terminals | DR | PCI DSS 3.2.1, 3.3.1.2, 9.4 | Moderate | Phone payments only on terminals; purge; quarterly discovery | Device Repair chief financial officer | 2026-11-30 |
| 9 | AI claims and AI vendor terms (7) | DR, IT, Group | 15 U.S.C. 45(a)(1); 164.308(b)(1); 164.504(e)(2)(ii)(D) | Moderate | Withdraw the claim; vendor and subcontractor terms; agent in the risk analysis and SOC 2 description | Group Chief Risk Officer | 2026-12-31 |
| 10 | Cross-division notification (8) | All | Fla. Stat. 501.171(3)-(6); 164.410; PCI DSS 12.10.1; contracts; Form 8-K Item 1.05 | Moderate | Complete the matrix; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 11 | Inheritance for depots and labs (9) | DR | CSF GV.RR-02; PCI DSS 12.4 | Moderate | Inheritance matrix before repair QSA fieldwork | Device Repair CISO | 2026-12-31 |
| 12 | Device Repair supplement drift (10) | DR | CSF GV.PO-02, GV.OC-03 | Moderate | Re-issue with an in-store counter annex | Device Repair CISO | 2026-11-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-021 to POAM-025 trace directly to this analysis).

**Before the retail QSA fieldwork closes (2026-11-20):** close roadmap items 1 and 7 for the retail checkout, and re-confirm retail scope with the counter networks (ER-G49).
**Before the Manufacturer A audit (2026-11):** named portal accounts, the 24-hour notice procedure, and signatures on the access standard (G-140, G-141).
**Before the repair QSA fieldwork (2027-01-11):** items 6 and 8, scope re-confirmation (G-135), and the depot and lab inheritance matrix (item 11).

## 6. Pending changes and watch items
None of these is treated as a current obligation.
- **PCI DSS.** v4.0.1 remains current. PCI SSC ran a request for comments (June to July 2026) toward the next version. Rows carry this in `pending_rule_change`.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is proposed only; the regulatory agenda projects a final rule in July 2027. If finalized as proposed, IT Support's 4 addressable gaps would become mandatory, a written technology asset inventory and network map would be required, and business associates would notify covered entities within 24 hours of activating a contingency plan.
- **FTC AI accuracy policy statement** (Docket FTC-2026-0727, proposed July 2026) is not final. It is relevant to the AI diagnostics claim (G-108) and the chatbot (P10).
- **CIRCIA.** Reporting is not in effect (no final rule as of 2026-09-25). The proposed rule's IT entity criteria could reach IT Support; the group tracks it.
- **State comprehensive privacy laws.** Several take effect in 2027 in states where the group may operate; the Group Chief Privacy Officer tracks them (P01 GR-20).
