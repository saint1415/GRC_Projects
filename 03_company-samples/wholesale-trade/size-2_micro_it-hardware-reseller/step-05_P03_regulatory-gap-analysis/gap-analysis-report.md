# Regulatory Gap Analysis: Cris Santos Company | Wholesale Trade | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| Tier / Vertical | Micro / Wholesale Trade |
| Primary regulation | FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems (15 requirements), assessed as the CMMC Level 1 (Self) requirements (32 CFR 170.14(c)(2) and 170.15), for the FCI order stream |
| Secondary | Section 889 (FAR 52.204-25 and 52.204-26); DFARS 252.246-7008 (sources of electronic parts); CMMC status and affirmation (DFARS 252.204-7021; 32 CFR 170.15, 170.19, 170.22); Fla. Stat. 501.171(2) and (8); applicability check of DFARS 252.204-7012, -7019, and -7020 |
| Assessment dates | 2026-07-13 to 2026-07-24 (row G-017 updated 2026-08-11 with a P07 finding) |
| Assessor | Operations Manager (security and compliance lead) with the Owner, the Federal Account Manager, and the MSP lead technician |
| Workbook | `gap-analysis.csv` (30 rows) |
| Approved | 2026-08-31 by the Owner |

## 1. Applicability
**The vertical's default rule does not bind at this size.** The Wholesale Trade default is NIST SP 800-171 Rev. 2 under DFARS 252.204-7012 and CMMC Level 2. That rule applies to "covered contractor information systems", which 252.204-7012(a) defines as systems that process, store, or transmit **covered defense information**. A review of all 34 DoD orders and their attachments on 2026-07-20 found no CUI markings and no covered defense information. The company therefore has no covered contractor information system under that clause, and 252.204-7019(b) requires an SP 800-171 assessment only "if the Offeror is required to implement NIST SP 800-171". Both are recorded as Not applicable (G-027, G-028), with a trigger to reassess if CUI ever arrives.

**FAR 52.204-21 applies.** The 19 DoD setup orders include the clause, and the company's systems hold Federal Contract Information: information "not intended for public release, that is provided by or generated for the Government under a contract to develop or deliver a product or service to the Government" (52.204-21(a)). Equipment lists with asset tags, user and room assignments, and delivery details meet that definition; simple transactional information such as payment data does not. There is no size exemption. The clause does not reach the 15 COTS-only orders: FAR 4.1902 applies the subpart to acquisitions of commercial products "other than commercially available off-the-shelf items".

**CMMC Level 1 (Self) applies to setup orders since 2026-02.** CMMC applies to DoD solicitations and contracts where a contractor will process FCI or CUI on its systems, "except those exclusively for COTS items", above the micro-purchase threshold (32 CFR 170.3(c)). Phase 1 began with the DFARS rule on 2025-11-10 (170.3(e)(1)). Level 1 requires a MET result on all 15 requirements, with **no POA&M** (170.15(a)(1); 170.21(a)(1)), an annual self-assessment entered in SPRS, an affirmation by the Affirming Official (170.22), and 6 years of evidence (170.15(c)(2)).

**Section 889 applies to every DoD order.** FAR 52.204-25 is prescribed for all solicitations and contracts (FAR 4.2105(b)), and the SAM representation at 52.204-26 covers both what the company provides and what it **uses**.

**DFARS 252.246-7008 applies** to the DoD setup orders and the Federal Prime orders, which include it. It is prescribed for DoD purchases of end items containing electronic parts, including commercial products (DFARS 246.870-3(b)). On counsel's advice the company treats the finished products it resells as assemblies containing electronic parts.

**Not applicable, with reasons:**
- FAR 52.204-21(b)(1)(xi): no publicly accessible components inside the boundary (G-011).
- SEC disclosure rules (private), CCPA/CPRA (no California business; revenue far below the threshold), CTPAT (voluntary; not an importer of record), Trade Agreements Act (no GSA schedule; no 2026 order includes the clause). See `../00_company-facts.md` section 1.

## 2. Method
1. **Requirements.** The 15 requirements are quoted from 48 CFR 52.204-21(b)(1). CMMC practice IDs and the SP 800-171 Rev. 2 equivalents come from Table 2 to 32 CFR 170.15(c)(1)(ii). Clause rows cite the eCFR text of each clause and regulation (current as of 2026-09-23); Florida rows cite the statute as published by the Florida Legislature.
2. **Crosswalk.** For the 15 FAR rows, SP 800-53 controls come from the SP 800-171 Rev. 2 Appendix D mapping of the equivalent requirement, refined to Rev. 5 by the author, and CSF 2.0 subcategories are derived from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference (two rows, AC-22 and MP-6, have no CSF mapping there). All other rows use an **author mapping**, labeled as such.
3. **Documentary evidence.** Each status rests on a named document or record: ERP and suite user lists, the Orders folder permission report, the ERP item master extract, the review of 34 DoD orders, the MSP console, patch, and encryption reports, the firewall rule export, the SAM and SPRS records, the purchase order template, and a walkthrough of the office and stockroom on 2026-07-15. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. For CMMC scoring, a requirement is either MET or NOT MET (32 CFR 170.24), so every Partially met FAR row counts as NOT MET.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FAR 52.204-21 (CMMC Level 1) | 3 | 9 | 2 | 1 | 15 |
| FAR 52.204-25 and 52.204-26 (Section 889) | 0 | 1 | 3 | 0 | 4 |
| DFARS 252.246-7008 (sources of electronic parts) | 0 | 2 | 2 | 0 | 4 |
| CMMC Level 1 status and affirmation | 0 | 1 | 2 | 0 | 3 |
| DFARS 252.204-7012 and 252.204-7019/-7020 (applicability check) | 0 | 0 | 0 | 2 | 2 |
| Fla. Stat. 501.171 | 0 | 2 | 0 | 0 | 2 |
| **Total (30)** | **3** | **15** | **9** | **3** | **30** |

Of the 24 unmet or partially met rows, by gap risk: 2 Very High, 5 High, 15 Moderate, 2 Low.

**What the numbers mean for CMMC Level 1.** Only the 3 malware rows (G-013 to G-015) are MET, and G-011 is not applicable. **11 of the 15 requirements are NOT MET**, so the Level 1 MET result entered in SPRS on 2026-03-02 is not supported (G-024, G-025). Level 1 allows no POA&M, so every one of the 11 must be fully met before a supported result can be entered.

**What the numbers say.** The MSP's endpoint tools carry the technical basics. The gaps are in what only the company can do: decide who sees FCI, control the stockroom, write down its sourcing rules, and check before it affirms or represents anything to the Government.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Unsupported Level 1 result and affirmation | 32 CFR 170.15, 170.22; 252.204-7021(d) (G-024, G-025) | Very High | On counsel's advice, correct the SPRS entry; no new setup orders until a documented self-assessment shows all 15 MET | Owner | 2026-10-31 |
| SAM "does not use" representation made without inquiry; covered camera recorder in use | 52.204-26(c); 52.204-25(b)(2) (G-017) | High | Recorder replaced 2026-08-20; counsel reviews the representation and any report; documented reasonable inquiry each year | Owner | 2026-09-30 |
| No Section 889 screening | 52.204-25(b)(1) (G-016) | High | Manufacturer of record; screening list; hard block on DoD quotes | Federal Account Manager | 2026-10-31 |
| Brokers used on DoD orders without notice or authentication | 252.246-7008(b) (G-020, G-021) | High | Authorized sources only for DoD orders; counsel advises on 3 past orders; notice procedure | Owner; Purchasing and Inventory Coordinator | 2026-09-30 and 2026-11-30 |
| FCI access not limited | 52.204-21(b)(1)(i) (G-001) | High | Restricted FCI folder; named accounts; termination checklist | Operations Manager | 2026-10-31 |
| No visitor control; no media sanitization | 52.204-21(b)(1)(ix), (vii) (G-009, G-007) | Moderate | Escort rule, visitor log, individual alarm codes; disposal rule and log | Operations Manager | 2026-10-31 |
| No Section 889 report procedure; no flowdown | 52.204-25(d), (e); 252.246-7008(e) (G-018, G-019, G-023) | Moderate | P08 runbook; DIBNet accounts; purchase order terms | Owner | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01: R-001, R-002, R-004, R-024) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are one-page procedures, purchase order wording, or MSP settings. The MSP does the technical work under the Operations Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop the exposure | 2026-09-30 | Counsel engaged for the SPRS correction, the 52.204-26 representation, and the 3 broker orders; DoD orders from authorized sources only (from 2026-09-01); bank-detail call-back; named portal accounts; remove the password spreadsheet; website posting rule | G-004, G-005, G-006, G-017, G-021 |
| 2. Meet all 15 FAR requirements | 2026-10-31 | Restricted FCI folder; termination checklist; ERP administrators reduced to 2; external systems rule and phone app protection; disposal rule and log; door, escort, visitor log, and alarm codes; bench and camera network segments; firewall firmware and patch time limits; Section 889 screening list and ERP block; DIBNet accounts; purchase order flowdown terms; documented Level 1 self-assessment and a supported SPRS entry and affirmation | G-001 to G-003, G-007 to G-010, G-012, G-016, G-018, G-019, G-023 to G-026, G-029, G-030 |
| 3. Supply chain program | 2026-11-30 | C-SCRM plan with the sourcing order, broker approval checklist, receiving inspection, and traceability records | G-020, G-022 |
| 4. Annual cycle | 2027-03-02 and 2027-07-31 | Annual Level 1 self-assessment and affirmation (no later than one year after the corrected entry); risk assessment update; recheck of the not-applicable rows | G-011, G-024, G-025, G-027, G-028 |

**Business decision tied to the plan.** Because Level 1 allows no POA&M, the Owner decided that the company will not accept new DoD setup orders after 2026-10-31 unless Phase 2 is complete and documented. COTS-only orders, which carry no FAR 52.204-21 or CMMC requirement, continue.

**Progress check.** The Operations Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
These are **proposed** and are not treated as current obligations. The `pending_rule_change` column flags the 19 affected rows.

- **FAR overhaul, parts 1, 2, 4, 33, 39, 40, and 53** (FR Doc. 2026-12559, 91 FR 37550, 2026-06-23; comments closed 2026-07-23). If finalized as proposed:
  - FAR 52.204-21 would be replaced by a new **FAR 52.240-5, Covered Federal Information**, with the same 15 safeguarding requirements and a new duty to protect covered Federal information from unauthorized disclosure when it is handled outside a covered contractor information system (G-001 to G-015).
  - FAR 52.204-25 and other security prohibitions would be consolidated into a new **FAR 52.240-3, Security Prohibitions and Exclusions**, with one written report to the contracting office within **72 hours** in place of today's 1-business-day and 10-business-day reports (G-016 to G-019).
- A Federal Register search (checked 2026-10-04) found no proposed rule published since 2025 that names DFARS 252.246-7008 or the CMMC program. CMMC Phase 2 (2026-11-10) is already scheduled in 32 CFR 170.3(e)(2) and does not change Level 1.
