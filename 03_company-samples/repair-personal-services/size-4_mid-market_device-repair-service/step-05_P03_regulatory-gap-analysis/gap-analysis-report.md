# Regulatory Gap Analysis: Cris Santos Company | Other Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain, NAICS 811210) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary benchmark: no sector cybersecurity rule applies** (section 1). Label `N81-BM` in the other deliverables |
| Secondary (binding law) | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n) (N81-R01); Florida Information Protection Act, Fla. Stat. 501.171 (2026), as covered entity and as third-party agent (N81-R02); other states' breach laws (N81-R02); FTC Disposal Rule, 16 CFR 682.3, for background check reports only (N81-R04) |
| Secondary (binding by contract) | PCI DSS v4.0.1: SAQ P2PE (October 2024) for the card-present channel and the SAQ A eligibility criteria (January 2025 revision) for the e-commerce channel (N81-R03); Manufacturer A program agreement; Partner P1 and P2 agreements (fictional terms) |
| Sanitization reference | NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of December 2014) |
| Assessment dates | 2026-07-06 to 2026-07-31 (site visits 2026-07-14 to 2026-07-23); evidence refreshed with P07 results through 2026-08-21 |
| Assessor | GRC Analyst and the Privacy and Compliance Manager, with the vCISO; applicability reviewed with the General Counsel and outside counsel; reviewed by the co-sourced internal audit firm |
| Workbook | `gap-analysis.csv` (152 rows) |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** consumer, mail-in, warranty, partner, and business account repair of personal electronics, with data recovery and recycling.

**No sector cybersecurity regulation applies.** No federal agency issues cybersecurity rules for repair businesses. The vertical research (`02_industry-rules/repair-personal-services/`) names NIST CSF 2.0 as the benchmark for that reason, and this analysis confirms it for a 600-person company. What changes at this size is not the benchmark but the **number of binding duties around it**: a second payment channel the company builds itself, a partner role in which the company holds other companies' customer data, more states, and the loss of SBA-small status. Each candidate was checked against its source:

| Requirement | Test (source text) | Decision |
|---|---|---|
| **FTC Act Section 5** (N81-R01) | 45(a)(1) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful. 45(n): a practice is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition." No size threshold | **Applies.** Deception covers the intake notice, the privacy page, and the AI accuracy claim. Unfairness covers unreasonable handling of customer devices and data |
| **Fla. Stat. 501.171 as covered entity** (N81-R02) | A covered entity is a "commercial entity that acquires, maintains, stores, or uses personal information" ((1)(b)). Personal information includes a name with medical, biometric, or geolocation information, and "a user name or e-mail address, in combination with a password or security question and answer that would permit access to an online account" ((1)(g)) | **Applies.** SYS-01 still holds about 640 email and password pairs in legacy notes, and devices and lab images hold health and location data linked to named customers. Subsections (2) to (6) and (8) are rows G-110 to G-116 |
| **Fla. Stat. 501.171 as third-party agent** | A third-party agent is "an entity that has been contracted to maintain, store, or process personal information on behalf of a covered entity" ((1)(h)); it must notify the covered entity "no later than 10 days following the determination of the breach" ((6)(a)) | **Applies (author interpretation, counsel to confirm)** when the company processes claim data for Partners P1 and P2. The partner agreements set a shorter 48-hour term (row G-115) |
| **Other states' breach laws** (N81-R02) | Each state's statute, for residents of that state | **Applies.** About 10% of tickets and most partner claims involve residents of other states (row G-117) |
| **FTC Disposal Rule** (N81-R04) | Applies to any person under FTC jurisdiction that possesses "consumer information", meaning a consumer report or information derived from one (16 CFR 682.1(b), 682.2(b)) | **Applies narrowly** to background check reports. **Customer device data is not consumer report information**, so device and record disposal is governed by Fla. Stat. 501.171(8) and Section 5 instead (row G-118) |
| **PCI DSS v4.0.1** (N81-R03) | Contractual, through the merchant agreement. The acquirer confirmed SAQ P2PE (card-present) and SAQ A (e-commerce) in its letter of 2026-04-15 (fictional). PCI SSC published the v4.0.1 SAQs on 15 October 2024 and revised SAQ A in January 2025: it removed requirements 6.4.3, 11.6.1, and 12.3.1 and added an eligibility criterion that the merchant confirm "their site is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s)" (PCI SSC blog announcing the January 2025 SAQ A) | **Applies by contract.** SAQ P2PE eligibility and its 22 requirement lines are rows G-119 to G-141. For the e-commerce channel, this analysis tests the SAQ A eligibility criteria (G-142), because they decide whether SAQ A can be used at all, and the two underlying PCI DSS requirements that show the script criterion is met (G-143, G-144). The remaining SAQ A lines are completed by the CFO with the company's QSA advisor before attestation |
| **Manufacturer A agreement and partner agreements** | Contracts (fictional terms, scenario facts section 1) | **Apply by contract** (rows G-145 and G-146) |
| FTC Safeguards Rule, COPPA, Florida Digital Bill of Rights, CIRCIA | 16 CFR 314.1(b); 16 CFR Part 312; Fla. Stat. 501.702; 6 U.S.C. 681-681g | **Not applicable** today (rows G-147, G-148, G-150, G-152 give the reasons). The Florida Digital Bill of Rights applies only to controllers above $1 billion in global gross annual revenue that also meet one of three further tests |
| HIPAA | 45 CFR 160.103 | **Not applicable as designed**, but tested: the company declines work that would make it a business associate, and 2 cases slipped through in 2026 (row G-149) |
| State comprehensive privacy laws without a numeric threshold (Texas example, Tex. Bus. & Com. Code 541.002) | These laws exclude SBA-small businesses; the company is not SBA-small and serves residents of those states by mail-in | **Likely applies.** The duties are privacy program duties, owned by the Privacy and Compliance Manager outside this security analysis (row G-151) |

**What changed from a smaller repair shop.** The size exemptions that kept a small shop out of some laws do not help here. The company is above its SBA size standard, so state privacy laws that exclude only SBA-small businesses can reach it. And its mail-in checkout page means it is responsible for an e-commerce channel, where the PCI DSS risk is script injection on a page the company hosts, not card data in its systems.

**Why the Disposal Rule question still matters.** The FTC Disposal Rule is often assumed to govern wiping customer devices. It covers consumer reports only. The duty to dispose of customer data properly comes from Fla. Stat. 501.171(8), which requires "all reasonable measures to dispose, or arrange for the disposal, of customer records containing personal information within its custody or control when the records are no longer to be retained," by "shredding, erasing, or otherwise modifying the personal information in the records to make it unreadable or undecipherable through any means." **Author interpretation, for counsel to confirm:** recycling devices and lab copies are customer records for this purpose. The company treats them that way either way and uses SP 800-88 Rev. 2 as the method, including verification (section 4.5.1), validation (section 4.5.2), and a certificate for each sanitized device (section 4.6 and Appendix C).

**When a technician's access becomes a breach.** Fla. Stat. 501.171(1)(a) excludes "good faith access of personal information by an employee or agent of the covered entity... provided that the information is not used for a purpose unrelated to the business." Opening the camera app to test the camera is good-faith access. Copying a customer's photos to a personal phone, as in the March 2026 Store 17 case, is not. That line is the basis for the customer data access standard (POL-04 4.4) and the breach branch of the P08 runbook.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). The FTC and Florida rows follow the statutes' own subsections. PCI DSS rows are the SAQ P2PE eligibility criteria and each requirement line in the v4.0.1 SAQ P2PE (October 2024), plus the SAQ A eligibility criteria and PCI DSS v4.0.1 6.4.3 and 11.6.1, listed by number with short topic labels written for this analysis. **PCI DSS is copyrighted; read the official standard for the text.**
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of key controls from that list. All other rows use an **author mapping**; no official NIST mapping exists for the FTC Act, the Florida statute, or PCI DSS v4.0.1.
3. **Evidence.** Interviews (COO, CFO, General Counsel, Director of Retail Operations, 4 Regional Managers, 8 Store Managers, Depot Director, Data Recovery Manager, Director of Partner Programs, Director of Customer Experience, Digital Engineering Manager, HR Director, 12 technicians, 8 advisors, 5 contact center agents), document review (policies, contracts, the acquirer letter, partner and program agreements, the Store 17 case file, the 2026-05 penetration test), system queries, and walkthroughs of 8 of 34 stores (2 per region), the Depot, and the corporate office.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, using the co-sourced internal audit firm's attribute sampling table (25 items for a control operating many times a year with moderate risk):
   - terminations: 25 of 286 (2025-07-01 to 2026-06-30);
   - new hires (background checks): 25 of 301;
   - incidents (breach decisions): 10 of 41;
   - customer complaints alleging device access: 10 of 23;
   - recycling devices: 20 at the Depot and 30 at 6 stores;
   - contracts with customer data: 26 of 26 (full population);
   - PIN pad inspection logs: 34 stores for 8 weeks (full population);
   - SYS-01 notes: full-population pattern searches on 2026-07-15 (passcodes, passwords, card numbers);
   - lab storage: full listing of cases by age;
   - data recovery intake 2026: full screening by client type;
   - marketing lists: 4 of 4.
   Each `evidence` cell names the sample and its result.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 12 | 18 | 1 | 0 | 31 |
| IDENTIFY (ID) | 7 | 13 | 1 | 0 | 21 |
| PROTECT (PR) | 5 | 17 | 0 | 0 | 22 |
| DETECT (DE) | 4 | 7 | 0 | 0 | 11 |
| RESPOND (RS) | 4 | 9 | 0 | 0 | 13 |
| RECOVER (RC) | 1 | 6 | 1 | 0 | 8 |
| **CSF 2.0 subtotal** | **33** | **70** | **3** | **0** | **106** |
| FTC Act Section 5 | 0 | 2 | 1 | 0 | 3 |
| Fla. Stat. 501.171 | 0 | 7 | 0 | 0 | 7 |
| Other states' breach laws | 0 | 1 | 0 | 0 | 1 |
| FTC Disposal Rule (background reports) | 0 | 1 | 0 | 0 | 1 |
| PCI DSS v4.0.1 SAQ P2PE | 8 | 13 | 0 | 2 | 23 |
| PCI DSS v4.0.1 e-commerce (SAQ A eligibility) | 0 | 0 | 3 | 0 | 3 |
| Manufacturer A agreement | 0 | 1 | 0 | 0 | 1 |
| Partner agreements | 0 | 1 | 0 | 0 | 1 |
| Applicability screen | 0 | 2 | 0 | 4 | 6 |
| **Total** | **41** | **98** | **7** | **6** | **152** |

Of the 105 Partially met or Not met rows, 23 are rated High, 59 Moderate, and 23 Low.

**Reading the pattern.** The company has a defined program: governance, risk management, identity, encryption in SaaS and cloud, detection by the MSSP, and the P2PE design are Met or close. The gaps are **gaps in scale**: designs that work at the Depot and the newer stores but not yet at the 14 legacy stores; retention rules that exist but are not enforced on old data; and the newest channels (the checkout page and the partner API) built faster than their security testing. Only 7 rows are Not met. Four of them concern the e-commerce channel and the AI claim (G-108, G-142 to G-144), and three concern supplier terms and recovery testing (G-026, G-050, G-101).

## 4. Priority gaps
| Gap | Rows | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Checkout page scripts unmanaged; SAQ A eligibility cannot be confirmed | G-047, G-075, G-142, G-143, G-144 | High | Script inventory and authorization, content security policy, change and tamper detection (POAM-012) | Digital Engineering Manager | 2026-11-30 |
| Manufacturer A terms breached (leaver accounts, late notice, portal MFA) | G-145 | High | Fix before the 2026-10 audit (POAM-025) | Director of Partner Programs | 2026-10-15 |
| Intake notice overstates technician controls; unsubstantiated AI claim | G-107, G-108 | High; Moderate | Correct the notice; remove the claim (POAM-020) | Director of Customer Experience | 2026-10-15 |
| Card numbers in contact center notes; terminal inspections incomplete | G-119, G-121, G-122, G-127 to G-129, G-131 | High; Moderate | Purge and block patterns; inspection checklists; terminal list reconciliation; training (POAM-015, POAM-011, POAM-017) | Chief Financial Officer | 2026-11-15 |
| Legacy credential notes and data kept past retention | G-037, G-110, G-116 | High | Bulk redaction; fix the lab purge job; purge records older than 3 years after last service (POAM-015, POAM-004) | Privacy and Compliance Manager | 2026-11-30 to 2027-03-31 |
| Technician controls missing at 14 legacy stores | G-057, G-063, G-109 | High | Standard bench image with session recording, USB blocking, and EDR (POAM-002) | Director of Retail Operations | 2027-03-31 |
| Sanitization records and validation | G-038, G-116 | High | All drop-offs to the Depot line under SP 800-88 Rev. 2; serial-level recycler certificates (POAM-005) | Depot Director | 2026-12-31 |
| No visibility of SYS-01 exports or application events | G-068, G-077, G-091 | High | SIEM onboarding and bulk export alerts (POAM-003) | Security Manager | 2027-01-31 |
| Recovery unproven; no contingency plan | G-050, G-052, G-064, G-101 | High | Contingency plan; quarterly restore tests; tabletops (POAM-007, POAM-010) | IT Director | 2027-01-31 to 2027-02-28 |
| Older lab shelf unencrypted | G-061 | High | Encrypt the shelf (POAM-019) | IT Director | 2027-03-31 |
| Vendors without security or data-use terms | G-026, G-114, G-136, G-137 | Moderate | Security and data-use addendum for 7 vendors (POAM-009) | Chief Financial Officer | 2026-12-31 |
| Partner duties (48-hour notice, claim data use) and HIPAA screen | G-115, G-146, G-149 | Moderate | Partner notice procedure and marketing exclusion (POAM-024); health care client intake flag (POAM-021) | Director of Partner Programs; Privacy and Compliance Manager | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

**Before signing the 2026 SAQs (due 2026-12-15):**
- **SAQ P2PE:** close G-119, G-121, G-122, and G-127 to G-129, and keep the evidence (purge record, pattern block, reconciled terminal list, 8 weeks of complete inspection logs, training roster).
- **SAQ A:** the CFO must not attest to the script eligibility criterion until G-142 to G-144 are closed and the change detection has run for at least 30 days. If they are not closed in time, the CFO asks the acquirer how to validate the channel.

**Before the Manufacturer A audit (2026-10):** G-145 (leaver accounts removed, portal MFA enforced, 24-hour notice procedure in P08) and an evidence pack showing the data access standard and the session recording at Manufacturer A stores.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Contracts and claims first** | 2026 Q4 | Manufacturer A audit fixes; AI claim removed and intake notice corrected; checkout page protection; card-number purge and terminal controls; legacy note redaction; lab purge job fixed; vendor addenda | G-107, G-108, G-119 to G-131, G-142 to G-145, G-110 (in part), G-026 |
| **2. Visibility and recovery** | 2027 Q1 | SIEM onboarding of SYS-01, lab, and portal logs; contingency plan; first restore tests; tabletops; pipeline scanning; standards issued | G-050, G-052, G-064, G-068, G-077, G-091, G-101, PR.PS-06 row (G-070) |
| **3. Legacy stores** | 2027 Q1-Q2 | Standard bench image at the last 14 stores; segmentation of 12 older stores; unsupported bench PCs replaced; records older than 3 years purged | G-057, G-063, G-109, PR.IR-01 row (G-071), G-116 |
| **4. Prove it** | 2027 Q2-Q4 | SOC 2 Type 2 observation period from 2027-04-01 (P09); annual risk assessment (July 2027); second annual control assessment | GV.OV and ID.IM rows; Partner agreement row G-146 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending changes and watch items
None of these is a current obligation.
- **PCI DSS.** v4.0.1 remains the version used by the acquirer letter. Recheck the PCI SSC document library before each annual SAQ, including any newer SAQ A revision.
- **CIRCIA.** The final rule was not published as of 2026-09-25 (row G-152). If it is published, counsel assesses whether the company falls in a covered critical infrastructure sector.
- **FTC AI accuracy policy statement** (Docket FTC-2026-0727, proposed July 2026, per `00_universal-framework/cross-sector/`) is not final. It is relevant to the AI claims and outputs reviewed in P10.
- **State AI and privacy laws.** Colorado SB26-189 (effective 2027-01-01) covers consequential decisions such as employment. The company hires only in Florida today, so it is not expected to apply, but P10 tracks it for the applicant ranking tool (AI-005).
- **NIST SP 800-88 Rev. 2** (September 2025) is final and is the method used here.
- **Florida.** Fla. Stat. 501.171 was last amended in 2026 (ch. 2026-52, per the statute history); the 2026 text is used here. Recheck each July.
