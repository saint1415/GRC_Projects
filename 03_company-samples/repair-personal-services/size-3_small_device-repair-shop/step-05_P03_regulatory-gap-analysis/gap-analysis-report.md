# Regulatory Gap Analysis: Cris Santos Company | Other Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service, NAICS 811210) |
| Tier / Vertical | Small / Other Services (except Public Administration) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary benchmark: no sector cybersecurity rule applies** (section 1). Label `N81-BM` in the other deliverables |
| Secondary (binding law) | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n) (N81-R01); Florida Information Protection Act, Fla. Stat. 501.171 (2026) (N81-R02); FTC Disposal Rule, 16 CFR 682.3, for background check reports only (N81-R04) |
| Secondary (binding by contract) | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (October 2024) (N81-R03); Manufacturer A authorized service provider agreement (fictional terms) |
| Sanitization reference | NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of December 2014) |
| Assessment dates | 2026-07-20 to 2026-07-31 (store walkthroughs 2026-07-22 and 2026-07-23). G-055 updated 2026-08-12 with the P07 storage console finding |
| Assessor | IT Manager (Information Security Lead) with the Operations Manager and the Controller; applicability reviewed with outside counsel |
| Workbook | `gap-analysis.csv` (144 rows) |
| Approved | General Manager, 2026-09-04 |

## 1. Applicability
**No sector cybersecurity regulation applies.** No federal agency issues cybersecurity rules for repair shops. The vertical's research (`02_industry-rules/repair-personal-services/`) names NIST CSF 2.0 as the benchmark for this reason, and this analysis confirms it for a 60-person, SBA-small repair company in Florida. The company's binding security duties come from general law, its merchant agreement, and its manufacturer program agreements. Each candidate was checked against its source:

| Requirement | Test (source text) | Decision |
|---|---|---|
| **FTC Act Section 5** (N81-R01) | 45(a)(1) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful. 45(n): a practice is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition." No size threshold | **Applies.** The company is a for-profit business in commerce. Deception covers its privacy and AI claims; unfairness covers unreasonable handling of customer devices and data |
| **Fla. Stat. 501.171** (N81-R02) | A covered entity is a "commercial entity that acquires, maintains, stores, or uses personal information" (1)(b). Personal information includes a name with medical information, biometric data, or "any information regarding an individual's geolocation", and "a user name or e-mail address, in combination with a password ... that would permit access to an online account" ((1)(g)) | **Applies.** SYS-01 holds about 2,900 customer email and password pairs. Customer phones in custody hold location history, health data, and saved credentials linked to a named customer. Subsections (2) to (6) and (8) are rows G-110 to G-115 |
| **FTC Disposal Rule** (N81-R04) | Applies to any person under FTC jurisdiction that possesses "consumer information", meaning a consumer report or information derived from one (16 CFR 682.1(b), 682.2(b)) | **Applies narrowly.** Only the background check reports on technicians and applicants are consumer reports. **Customer device data is not consumer report information**, so the Disposal Rule does not govern device wiping. Device and record disposal is covered by Fla. Stat. 501.171(8) and FTC Act Section 5 instead (row G-117) |
| **PCI DSS v4.0.1** (N81-R03) | Contractual, through the merchant agreement. The acquirer confirmed validation on **SAQ P2PE** (letter 2026-05-20, fictional). The v4.0.1 SAQ P2PE exists: PCI SSC published the v4.0.1 SAQs on 15 October 2024, and the SAQ P2PE for v4.0.1 is dated October 2024 | **Applies by contract.** Eligibility criteria plus the 22 requirement lines in SAQ P2PE are rows G-118 to G-140. The PCI SSC standards page (checked 2026-09-26) shows no newer version |
| **Manufacturer A program agreement** | Contract (fictional terms, scenario facts section 1) | **Applies by contract.** One summary row (G-141); the 2026-10 program audit will test it |
| FTC Safeguards Rule, COPPA, HIPAA | 16 CFR 314.1(b); 16 CFR Part 312; 45 CFR 160.103 | **Not applicable** (rows G-142 to G-144 give the reasons) |

**Why the Disposal Rule question matters.** Repair shops often assume the FTC Disposal Rule governs wiping customer devices. It does not: it covers consumer reports only. The duty to dispose of customer data properly comes from Fla. Stat. 501.171(8), which requires "all reasonable measures to dispose ... of customer records containing personal information ... by shredding, erasing, or otherwise modifying the personal information ... to make it unreadable or undecipherable." Customer records are material "provided by an individual in this state to a covered entity for the purpose of ... obtaining a service" ((1)(c)). Intake forms and ticket records clearly qualify. **Author interpretation, for counsel to confirm:** devices left for recycling and the copies the lab makes during data recovery also qualify. The company will treat them as customer records either way, and will use SP 800-88 Rev. 2 as the method.

**FTC precedent on access to consumer devices.** A search of ftc.gov found **no FTC enforcement action against a repair shop for technician snooping**. The closest precedent is *In re DesignerWare, LLC* and seven rent-to-own operators (complaints announced 2012-09-25; final orders 2013-04-15). The FTC treated covert collection of data from consumers' rented computers (screenshots, keystrokes, webcam photos, location) as an unfair practice and banned it. The FTC's May 2021 report to Congress on repair restrictions, *Nixing the Fix*, records manufacturers' argument that independent shops endanger customer data, and concludes: "The record contains no empirical evidence to suggest that independent repair shops are more or less likely than authorized repair shops to compromise or misuse customer data" (page 31). The lesson for this company: its duty does not depend on authorized status. It must make its own practices reasonable and its privacy statements true.

**When a technician's access becomes a breach.** Fla. Stat. 501.171(1)(a) excludes "good faith access of personal information by an employee or agent ... provided that the information is not used for a purpose unrelated to the business." Opening the photo app to test the camera is good-faith access. Browsing or copying a customer's photos is not. That line is the basis for the access standard in POL-04 4.4 and the breach branch of the P08 runbook.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). The FTC and Florida rows follow the statutes' own subsections. PCI DSS rows are the SAQ P2PE eligibility criteria plus each requirement line in the v4.0.1 SAQ P2PE, listed by number with short topic labels written for this analysis. **PCI DSS is copyrighted; read the official standard for the text.** The requirement list was read from the v4.0.1 SAQ P2PE (October 2024).
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of key controls from that list. All other rows use an **author mapping**; no official NIST mapping exists for the FTC Act, the Florida statute, or PCI DSS v4.0.1.
3. **Evidence.** Interviews (General Manager, Operations Manager, Controller, Customer Experience Manager, Data Recovery Lead, 4 Store Managers, 6 technicians, 4 customer service advisors), document review (intake form, privacy statement, merchant agreement and acquirer letter, program agreements, vendor contracts, the April 2026 complaint file), SYS-01 role and field searches on 2026-07-22, a lab storage listing, and walkthroughs of all four stores and the Depot.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 5 | 15 | 11 | 0 | 31 |
| IDENTIFY (ID) | 2 | 9 | 10 | 0 | 21 |
| PROTECT (PR) | 2 | 14 | 6 | 0 | 22 |
| DETECT (DE) | 0 | 4 | 7 | 0 | 11 |
| RESPOND (RS) | 0 | 9 | 4 | 0 | 13 |
| RECOVER (RC) | 0 | 5 | 3 | 0 | 8 |
| **CSF 2.0 subtotal** | **9** | **56** | **41** | **0** | **106** |
| FTC Act Section 5 | 0 | 0 | 3 | 0 | 3 |
| Fla. Stat. 501.171 | 0 | 6 | 0 | 0 | 6 |
| Other states' breach laws | 0 | 1 | 0 | 0 | 1 |
| FTC Disposal Rule (background reports) | 0 | 1 | 0 | 0 | 1 |
| PCI DSS v4.0.1 SAQ P2PE | 1 | 11 | 9 | 2 | 23 |
| Manufacturer A agreement | 0 | 1 | 0 | 0 | 1 |
| Applicability screen | 0 | 0 | 0 | 3 | 3 |
| **Total** | **10** | **76** | **53** | **5** | **144** |

Of the 129 unmet or partially met rows, 18 are rated High, 57 Moderate, 53 Low, and 1 Very Low.

**Reading the pattern.** The company has the basics that vendors give it for free (SaaS encryption, SSO with MFA for office staff, P2PE). It is weakest exactly where a repair shop is different from other businesses: **what technicians can do with customer devices, how long the company keeps customer data, and how it wipes devices.** Twelve of the 18 High gaps sit in those three areas (G-016, G-037, G-038, G-053, G-057, G-061, G-063, G-077, G-091, G-109, G-110, G-115).

## 4. Priority gaps and roadmap
| Gap | Rows | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Privacy statement says technicians never access data; not true in practice | G-107 | High | Rewrite the intake notice to describe the access that testing needs; make it true through the access standard | Customer Experience Manager | 2026-10-15 |
| Passcodes and account passwords in ticket notes, visible to all users | G-037, G-057, G-061, G-110 | High | Stop collecting account passwords; restricted passcode field purged at release; purge 48,000 historical notes | IT Manager | 2026-11-15 |
| Unlimited technician access to device contents; no logs; no confidentiality agreements | G-016, G-063, G-077, G-091, G-109 | High | Customer data access standard (POL-04 4.4); named bench accounts; USB block; session logging; signed agreements | Operations Manager | 2026-12-31 |
| Shared counter and portal logins; no MFA on counter tablets | G-053, G-055, G-141 | High | Named accounts with MFA; named Manufacturer A portal accounts before the 2026-10 audit | IT Manager | 2026-10-31 |
| Recovered data kept forever; no sanitization standard for recycling devices | G-038, G-115 | High | 30-day retention after delivery; purge 4.2 TB backlog; SP 800-88 Rev. 2 methods with a certificate per device | Operations Manager | 2026-12-31 |
| Backups exposed and untested | G-064, G-101 | High | Separate immutable backup account; quarterly restore tests | IT Manager | 2026-12-31 (first test 2026-10-31) |
| Flat store networks with customer devices on them | G-071 | High | Bench and customer-device VLAN | IT Manager | 2027-01-31 |
| No incident response plan | G-052, G-140 | High | POL-03 and P08 approved; tabletop exercise | IT Manager | 2026-11-30 |
| Card numbers in ticket notes; PIN pad controls missing (SAQ P2PE eligibility) | G-118, G-120, G-121, G-123, G-126 to G-128, G-130 | Moderate | Purge and block card-number patterns; terminal list, weekly inspections, and training | Controller | 2026-10-31 |
| Unsubstantiated "99% accurate" AI claim | G-108 | Moderate | Remove the claim; measure accuracy (P10) | Customer Experience Manager | 2026-09-30 |
| No vendor terms for recycler, courier, and AI vendors | G-026, G-114 | Moderate | Contract addendum with security, data-use, deletion, and breach notice terms | Controller | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Before signing the 2026 SAQ P2PE (due 2026-11-30):** close G-118, G-120, G-121, G-123, G-126 to G-128, and G-130, and keep the evidence (purge record, pattern block, terminal list, inspection logs, training roster). If card numbers are found electronically again, the Controller must not attest to the eligibility criteria and must ask the acquirer how to validate.

**Before the Manufacturer A audit (2026-10):** named portal accounts (G-141), the 24-hour notice procedure (P08), and the signed access standard (POL-04 4.4).

## 5. Pending changes and watch items
None of these is a current obligation.
- **PCI DSS.** v4.0.1 remains current per the PCI SSC standards page (checked 2026-09-26). Recheck before each annual SAQ.
- **NIST SP 800-88 Rev. 2** (September 2025) is final and is the method used here. It points to IEEE 2883 for technology-specific sanitization techniques and treats sanitization as a program (Section 4), with verification (4.5.1) and a sample certificate of sanitization (Appendix C).
- **FTC AI accuracy policy statement** (Docket FTC-2026-0727, proposed July 2026, per `00_universal-framework/cross-sector/`) is not final. It is relevant to the chatbot and diagnostics claims (P10).
- **Florida.** Fla. Stat. 501.171 was last amended in 2026 (ch. 2026-52, per the statute history); the 2026 text is used here. Recheck each July.
