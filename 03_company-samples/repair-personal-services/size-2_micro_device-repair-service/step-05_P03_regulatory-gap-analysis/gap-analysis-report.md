# Regulatory Gap Analysis: Cris Santos Company | Other Services (except Public Administration) | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop, NAICS 811210) |
| Tier / Vertical | Micro / Other Services (except Public Administration) |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, 2024-02-26), all 106 subcategories. **Voluntary benchmark: no sector cybersecurity rule applies** (section 1). Label `N81-BM` in the other deliverables |
| Secondary (binding law) | FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n) (N81-R01); Florida Information Protection Act, Fla. Stat. 501.171 (2026) (N81-R02); other states' breach laws (N81-R02); FTC Disposal Rule, 16 CFR 682.3, for the 2 background check reports only (N81-R04) |
| Secondary (binding by contract) | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (October 2024) (N81-R03) |
| Sanitization reference | NIST SP 800-88 Rev. 2, *Guidelines for Media Sanitization* (final, September 2025) |
| Assessment dates | 2026-07-20 to 2026-07-31 (shop walkthrough and SYS-01 searches 2026-07-22) |
| Assessor | Shop Manager (Security and Privacy Lead) with the MSP lead technician and the Owner |
| Workbook | `gap-analysis.csv` (143 rows) |
| Approved | Owner, 2026-08-31 |

## 1. Applicability
**No sector cybersecurity regulation applies.** No federal agency issues cybersecurity rules for repair shops. The vertical's research (`02_industry-rules/repair-personal-services/`) names NIST CSF 2.0 as the benchmark for this reason. This analysis confirms it for a 7-person, SBA-small repair shop in Florida. The shop's binding security duties come from general law and its merchant agreement. Each candidate was checked against its source:

| Requirement | Test (source text) | Decision |
|---|---|---|
| **FTC Act Section 5** (N81-R01) | 45(a)(1) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful. 45(n): a practice is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition." No size threshold | **Applies.** The shop is a for-profit business in commerce. Deception covers the intake form's privacy promise and the website's AI claim; unfairness covers unreasonable handling of customer devices and data. Rows G-107 to G-109 |
| **Fla. Stat. 501.171** (N81-R02) | A covered entity is a "commercial entity that acquires, maintains, stores, or uses personal information" ((1)(b)); a sole proprietorship is expressly included, so size is no exemption. Personal information includes a name with medical information, biometric data, or "any information regarding an individual's geolocation", and "a user name or e-mail address, in combination with a password or security question and answer that would permit access to an online account" ((1)(g)) | **Applies.** SYS-01 holds about 310 customer email and password pairs. Customer phones in custody hold location history, health data, and saved credentials linked to a named customer. Subsections (2) to (6) and (8) are rows G-110 to G-115 |
| **Other states' breach laws** (N81-R02) | Each state's own statute | **Applies** to the about 4% of customers with out-of-state addresses. Treated generically (row G-116); counsel applies each state's law at the time |
| **FTC Disposal Rule** (N81-R04) | Applies to any person under FTC jurisdiction that possesses "consumer information", meaning a consumer report or information derived from one (16 CFR 682.1(b), 682.2(b)) | **Applies narrowly.** Only the 2 background check reports on technicians are consumer reports. **Customer device data is not consumer report information**, so the Disposal Rule does not govern device wiping. That duty comes from Fla. Stat. 501.171(8) and FTC Act Section 5 instead (row G-117) |
| **PCI DSS v4.0.1** (N81-R03) | Contractual, through the merchant agreement. The processor confirmed validation on **SAQ P2PE** (letter 2026-04-15, fictional). The v4.0.1 SAQ P2PE (October 2024) was read for this analysis. Its eligibility section says a mail or telephone order merchant can qualify when staff key card data directly and only into a terminal from the validated P2PE solution (paraphrased) | **Applies by contract.** The eligibility criteria plus the 22 requirement lines in SAQ P2PE are rows G-118 to G-140 |
| FTC Safeguards Rule, COPPA (N81-R05), HIPAA (N81-R06) | 16 CFR 314.1(b); 16 CFR Part 312; 45 CFR 160.103 | **Not applicable** (rows G-141 to G-143). The shop extends no credit and offers no financing; its website and messaging are not directed to children; it is not a covered entity or business associate |
| Florida Digital Bill of Rights | A "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one more test (online advertising revenue, a smart speaker service, or an app store) | **Not applicable.** The shop's revenue is about $1.1 million. Not given a row |

**Why the Disposal Rule question matters.** Repair shops often assume the FTC Disposal Rule governs wiping customer devices. It does not: it covers consumer reports only. The duty to dispose of customer data properly comes from Fla. Stat. 501.171(8): each covered entity "shall take all reasonable measures to dispose, or arrange for the disposal, of customer records containing personal information within its custody or control when the records are no longer to be retained," by "shredding, erasing, or otherwise modifying the personal information in the records to make it unreadable or undecipherable through any means." Customer records are material "provided by an individual in this state to a covered entity for the purpose of purchasing or leasing a product or obtaining a service" ((1)(c)). Intake forms and ticket records clearly qualify. **Author interpretation, for counsel to confirm:** devices left for recycling and the copies the shop makes during data transfer and recovery also qualify. The shop will treat them as customer records either way, and will use SP 800-88 Rev. 2 as the method.

**When a technician's access becomes a breach.** Fla. Stat. 501.171(1)(a) excludes "good faith access of personal information by an employee or agent of the covered entity ... provided that the information is not used for a purpose unrelated to the business or subject to further unauthorized use." Opening the camera app to test the camera is good-faith access. Browsing or copying a customer's photos is not. That line is the basis for the access standard in POL-04 4.4 and the Branch A steps in the P08 runbook.

**FTC precedent on access to consumer devices.** The closest FTC precedent is *In re DesignerWare, LLC* and seven rent-to-own operators (2012-2013), where the FTC treated covert collection of data from consumers' rented computers as an unfair practice. The lesson for a small shop: its duty does not depend on its size or on being authorized by a manufacturer. It must make its own practices reasonable and its statements to customers true.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). The FTC and Florida rows follow the statutes' own subsections. PCI DSS rows are the SAQ P2PE eligibility criteria plus each requirement line in the v4.0.1 SAQ P2PE, listed by number with short topic labels written for this analysis. **PCI DSS is copyrighted; read the official SAQ for the text.**
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of key controls from that list or close to it. All other rows use an **author mapping**; no official NIST mapping exists for the FTC Act, the Florida statute, or PCI DSS v4.0.1.
3. **Documentary evidence.** Each status rests on a named document or record: the intake form and website, the SYS-01 user and role lists, the SYS-01 field searches on 2026-07-22 (passcodes, account passwords, card numbers), the bench storage listing, the bench PC software list, the MSP's patch, antivirus, encryption, and backup reports, the firewall rule export, the merchant agreement and processor letter, the contract folder, the screening reports, and the customer email about the 2026-03-14 complaint. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then (for example, policies approved 2026-08-31) are reflected in the target dates but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 1 | 11 | 19 | 0 | 31 |
| IDENTIFY (ID) | 0 | 7 | 14 | 0 | 21 |
| PROTECT (PR) | 3 | 11 | 7 | 1 | 22 |
| DETECT (DE) | 0 | 2 | 9 | 0 | 11 |
| RESPOND (RS) | 0 | 3 | 10 | 0 | 13 |
| RECOVER (RC) | 0 | 2 | 6 | 0 | 8 |
| **CSF 2.0 subtotal** | **4** | **36** | **65** | **1** | **106** |
| FTC Act Section 5 | 0 | 0 | 3 | 0 | 3 |
| Fla. Stat. 501.171 | 0 | 5 | 1 | 0 | 6 |
| Other states' breach laws | 0 | 1 | 0 | 0 | 1 |
| FTC Disposal Rule (background reports) | 0 | 1 | 0 | 0 | 1 |
| PCI DSS v4.0.1 SAQ P2PE | 1 | 2 | 18 | 2 | 23 |
| Applicability screen | 0 | 0 | 0 | 3 | 3 |
| **Total** | **5** | **45** | **87** | **6** | **143** |

Of the 132 unmet or partially met rows, 20 are rated High, 67 Moderate, and 45 Low.

**Reading the pattern.** This is an early-stage program, as expected for a 7-person shop: almost nothing was written down before July 2026, so most GOVERN, DETECT, RESPOND, and RECOVER rows are Not met. What the shop has comes free from its vendors (SaaS encryption, MFA on named accounts, P2PE). The gaps that matter most are the ones specific to a repair shop: **what technicians can reach on customer devices and in ticket notes, how long customer data is kept, and how devices are wiped.** Eleven of the 20 High gaps sit in those three areas (G-016, G-037, G-038, G-053, G-057, G-061, G-077, G-091, G-107, G-109, G-115). The PCI rows are mostly Not met because SAQ P2PE's few requirements are all paperwork the shop never did (policy, terminal list, inspections, training, vendor list), not because card data is exposed in its systems, with one important exception: card numbers in 11 ticket notes (G-118, G-120, G-121).

## 4. Priority gaps
| Gap | Rows | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Intake form promises technicians never access personal data; not true in practice | G-107 | High | Rewrite the notice to describe the access testing needs; make it true through the access standard | Owner | 2026-09-30 |
| Passcodes and account passwords in ticket notes visible to all users | G-057, G-061, G-109, G-110 | High | Stop collecting account passwords; restricted passcode field cleared at release; purge about 5,200 historical notes | Shop Manager | 2026-10-31 |
| No limit on technician access to device contents; no logs; no confidentiality agreements | G-016, G-077, G-091 | High | Customer device access standard (POL-04 4.4); named bench accounts; USB storage blocked; session logging; signed agreements | Owner; Senior Technician | 2026-12-31 |
| Shared Counter login; MFA gaps on admin logins | G-053, G-055 | High | Named counter accounts with MFA; MFA on the backup console, firewall, and bench storage | Shop Manager | 2026-09-30 |
| Customer data kept forever; no sanitization standard | G-037, G-038, G-115 | High | 30-day retention after collection; purge the 2.3 TB backlog; SP 800-88 Rev. 2 methods with a record per device | Senior Technician | 2026-11-30 |
| Customer devices on the staff network | G-071 | High | Separate network for customer devices and bench equipment | Shop Manager (MSP performs) | 2026-12-31 |
| Backups untested, deletable, and keep customer data a year | G-064, G-101 | High | MFA and immutable retention; quarterly restore tests; 30-day retention for bench data | Shop Manager (MSP performs) | 2026-10-31 (first test 2026-09-30) |
| No incident plan; notice duties unknown | G-052, G-095, G-140 | High | POL-03 and the P08 runbook approved 2026-08-31; tabletop by 2026-11-30 | Shop Manager | 2026-11-30 |
| No training | G-059, G-130, G-134 | High | Training at hire and yearly; phishing simulations; terminal tamper training | Shop Manager | 2026-10-31 |
| Card numbers in ticket notes and on sticky notes (SAQ P2PE eligibility) | G-118, G-120, G-121, G-123, G-125 | High | Purge; key phone payments straight into the terminal; shredder at the counter | Shop Manager | 2026-09-30 |
| Terminal controls from the P2PE Instruction Manual missing | G-126 to G-128, G-130 | Moderate | Terminal list, weekly inspections, tamper training, spare locked away | Shop Manager | 2026-10-31 |
| Unsubstantiated AI claim on the website | G-108 | Moderate | Remove the claim (P10) | Owner | 2026-09-30 |
| No vendor terms for the recovery lab, courier, recycler, and AI provider | G-025, G-026, G-114 | Moderate | Standard security and data-use terms with 10-day breach notice | Owner | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High gap, and every Moderate gap tied to a risk, is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person shop: most actions are one-page procedures, SYS-01 settings, or MSP work, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop the worst exposures | 2026-09-30 | Named counter accounts with MFA; MFA on MSP-held and bench storage admin logins; stop collecting account passwords; purge card-number notes; phone payments straight into the terminal; shredder; rewrite the intake notice and remove the AI claim; confidentiality agreements; leaver checklist; first restore test; signed policy acknowledgments | G-016, G-053, G-055, G-101, G-107, G-108, G-118, G-120, G-121, G-123, G-125, G-131, G-133 |
| 2. Know what the shop has | 2026-10-31 | One-page inventory with terminal serial numbers and where customer data lives; vendor list; restricted passcode field and historical purge; terminal inspections; training and phishing simulations; sanitization standard with records; monthly SYS-01 export review; backup immutability | G-037, G-038, G-057, G-061, G-064, G-059, G-077, G-110, G-126 to G-128, G-130, G-134, G-135 |
| 3. Contain the bench | 2026-12-31 | Retention purge of the bench storage and backup; bench storage encryption; separate network; bench PCs under MSP management with EDR and a standard image; approved tool list; USB storage blocked; vendor terms; tabletop exercise | G-071, G-091, G-115, G-025, G-026, G-114, G-052 |
| 4. Annual cycle | 2027-07-31 to 2027-08-31 | Risk assessment update (July); independent assessment and policy review (August) | GV.OV, GV.PO-02, ID.IM-01 rows |

Items already closed by approval on 2026-08-31: the policies (G-017, G-119, G-122) and the incident response plan (G-086, G-140). They remain "Not met" in the CSV because the status reflects fieldwork.

**Before signing the 2026 SAQ P2PE (due 2026-12-15):** close G-118, G-120, G-121, G-123, G-125 to G-128, and G-130, and keep the evidence (purge record, terminal list, inspection logs, training roster). If card numbers are found in any electronic record again, the Shop Manager must not attest to the eligibility criteria and must ask the processor how to validate.

**Progress check.** The Shop Manager reports progress to the Owner at the monthly 30-minute security check-in, using the P07 POA&M as the tracker.

## 6. Pending changes and watch items
None of these is a current obligation.
- **PCI DSS.** v4.0.1 and its October 2024 SAQ P2PE are current as used here. Recheck the PCI SSC document library before each annual SAQ.
- **NIST SP 800-88 Rev. 2** (September 2025) is final and is the method used here. It describes three sanitization methods (Clear, Purge, Destroy; section 3.1), cryptographic erase (section 3.2), sanitization as a program (section 4), verification (4.5.1), and a sample certificate of sanitization (Appendix C). It points to IEEE 2883 for media-specific techniques.
- **FTC AI-accuracy policy statement** (Docket FTC-2026-0727, proposed July 2026, per `00_universal-framework/cross-sector/us-cross-sector-obligations.md`) is not final. It is relevant to the AI assistant (P10).
- **Florida.** Fla. Stat. 501.171 was last amended in 2026 (ch. 2026-52, per the statute history); the 2026 text is used here. Recheck each July.
