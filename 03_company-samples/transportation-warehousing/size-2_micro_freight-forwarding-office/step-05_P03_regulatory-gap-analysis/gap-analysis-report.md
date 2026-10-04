# Regulatory Gap Analysis: Cris Santos Company | Transportation and Warehousing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office, NAICS 488510) |
| Tier / Vertical | Micro / Transportation and Warehousing |
| Regulation analyzed | 19 CFR Part 111 (customs brokers), Subparts A, C, and F, with the 19 CFR 163.5 storage standards that 111.21(c) and 111.23(a) bring in. Modernization rule 87 FR 63267 (2022-10-18), effective 2022-12-19; continuing education rule 88 FR 41224 (2023-06-23), effective 2023-07-24. Text checked against eCFR as of 2026-09-23 |
| Secondary rows | 46 CFR 515.33 (ocean freight forwarder records), 15 CFR 30.10(a) (export records), Fla. Stat. 501.171 |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | Office and Compliance Manager (Security Coordinator) with the MSP lead technician and the Entry Supervisor |
| Approved | 2026-08-31 by the owner |

## 1. Applicability
**The vertical's default regulation does not apply.** The vertical's primary regulation is the USCG maritime cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01). Section 101.605(a) applies it to owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have security plans under 33 CFR Parts 104, 105, and 106. The company operates no vessel or facility and has no MTSA security plan; its cargo moves through terminals run by others (G-049). There is no flow-down: no terminal contract imposes Subpart F duties on the company.

**What does apply.** The company is a licensed customs broker, so **19 CFR Part 111 applies in full**. Part 111 has no size threshold or small-business exemption. The duties that matter most for security are:
- **111.21(b)**, added by the 2022 modernization rule: notify the CBP Security Operations Center electronically within 72 hours of discovering any known breach of electronic or physical records relating to customs business, with any known compromised importer identification numbers, then an updated list within 10 business days.
- **111.23(a)**: keep originals of records, including electronic records, within the customs territory of the United States.
- **111.24**: client records are confidential and may be disclosed only to the listed parties or with the client's written authorization.
- **111.28**: responsible supervision and control, including training, written instructions, and recorded review of employees' work; employee lists to CBP within 30 days of hires and terminations.
- **163.5**, brought in by 111.21(c) and 111.23(a): the rules for storing records in an alternative format (scanned images).

**Other transportation requirements considered and excluded:**
- TSA indirect air carrier rule, 49 CFR Part 1548 (G-050): it governs indirect air carriers engaged in the air transportation of property. The company arranges ocean freight only and refers air shipments to other forwarders.
- TSA rail, pipeline, and aviation directives (N48-49-R02 to R04): the company is none of these.
- CMMC (N48-49-R07): no DoD contracts. SEC rules (N48-49-R08): privately held.
- CTPAT (N48-49-R05, G-051): voluntary, and the company is not a partner. Its minimum security criteria reach the company through six CTPAT importer clients' business partner questionnaires. That is a contract expectation, answered in P09, not a legal duty.

**Secondary rows.** The company is an FMC-licensed ocean freight forwarder (46 CFR 515.33 records), an authorized agent for export filings (15 CFR 30.10(a) records), and holds Social Security numbers of about 25 individual importers and 7 employees (Fla. Stat. 501.171).

## 2. Method
1. **Requirements.** Rows follow the regulation's own structure: each paragraph of Part 111 Subparts A to C and F and of 163.5 that imposes a duty relevant to the company's records, people, systems, or money, at the most granular citation that can be checked separately. Definitions, the licensing application process, examinations, and the disciplinary procedure (Subparts D and E) set context and have no rows. Brief quotes are used; this is public-domain federal text.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has published no mapping for Part 111.
3. **Documentary evidence.** Each status rests on a named record: eCBP screens and submission history, license and permit records, the customs platform user list and settings, the suite settings and user export, a sample of 10 shipment files and 10 POAs, ACE statement history, the termination record for the former Entry Writer, shredding certificates, the 2019 procedures manual, and a walkthrough of the office and the archive on 2026-07-22 and 2026-07-23. Interviews covered all 7 employees and the MSP lead technician.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then are noted in the remediation column but do not change the status. "Not applicable" is used only for duties not triggered (G-028, G-030), an exemption (G-040), and the three applicability rows.
5. **Regulatory driver labels.** The vertical requirement list has no customs broker entry, so the other deliverables cite these sections directly (for example "19 CFR 111.21(b)").

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Subparts A and B: license, permit, point of contact (111.2-111.19) | 4 | 2 | 0 | 0 |
| Subpart C: records and confidentiality (111.21-111.26) | 2 | 8 | 2 | 0 |
| Subpart C: supervision, employees, payments, conduct (111.28-111.39) | 8 | 5 | 1 | 2 |
| Subpart F: continuing education (111.102) | 0 | 2 | 0 | 0 |
| 19 CFR 163.5 storage standards | 1 | 2 | 3 | 1 |
| Secondary: 46 CFR 515.33, 15 CFR 30.10, Fla. Stat. 501.171 | 1 | 3 | 1 | 0 |
| Applicability checks (Subpart F of 33 CFR 101, 49 CFR 1548, CTPAT) | 0 | 0 | 0 | 3 |
| **Total (51)** | **16** | **22** | **7** | **6** |

Gap risk for the 29 Not met or Partially met rows: 3 High, 18 Moderate, 8 Low.

**What the numbers say.** The licensing and conduct duties are mostly met: the company has its license, permit, contacts, and payment discipline in order. The gaps sit where customs duties meet information security: the 72-hour CBP breach notice has no procedure (G-008, G-009), scanned records replaced paper without the 163.5 notice and safeguards (G-037 to G-043), data location and confidentiality are unproven for the SaaS and backup vendors (G-013, G-015), and supervision of employees' and the AI feature's work is not recorded (G-020, G-021, G-033).

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No 72-hour breach notice procedure; importer numbers not mapped | 111.21(b) | High | Notice step and email template (POL-03, P08); data map | Office and Compliance Manager | 2026-10-31 |
| Alternative storage used without notice to CBP | 163.5(b)(1) | High | Send the notice; keep paper until 30 days after it | Office and Compliance Manager | 2026-09-30 |
| Backup copy of records unproven and weakly protected | 163.5(b)(2)(vi) | High | Restore test; quarterly tests; MFA on the console | Office and Compliance Manager (MSP performs) | 2026-10-31 |
| Terminated employee reported late; signing authority withdrawal not notified | 111.28(b)(3); 111.2(a)(2)(ii)(B) | Moderate | Last-day checklist with CBP steps | Office and Compliance Manager | 2026-09-30 |
| Data location not confirmed | 111.23(a) | Moderate | Confirm and set U.S. storage for suite and backup | Office and Compliance Manager | 2026-10-31 |
| No written client authorization for service providers; public AI use | 111.24 | Moderate | Client terms clause (counsel); AI rule in POL-02 | Owner | 2026-12-31 |
| Employee and AI-assisted work not reviewed on record | 111.28(a)(8); 111.39(b) | Moderate | Monthly recorded review sample; broker approval of AI suggestions | Entry Supervisor | 2026-10-31 |
| No storage procedure or yearly test | 163.5(b)(2)(i), (iv) | Moderate | Written procedure; yearly retrieval test | Office and Compliance Manager | 2026-10-31 |
| Continuing education behind; status report not planned | 111.102(b); 111.30(d) | Moderate | Credit plan; filing calendar | Entry Supervisor; Owner | 2027-01-31; 2027-02-01 |
| No Florida breach notice procedure | Fla. Stat. 501.171(3)-(4), (6) | Moderate | P08 matrix; vendor 10-day notice terms | Office and Compliance Manager | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person office: most actions are one-page procedures, CBP submissions, or MSP settings, not new systems.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. CBP notices and people | 2026-09-30 | Alternative storage notice to CBP Regulatory Audit; scanning procedure; last-day checklist with the CBP employee list and signing authority steps; backup point of contact; wipe confirmations | G-037, G-038, G-024, G-002, G-004, G-047 |
| 2. Records and breach readiness | 2026-10-31 | 72-hour notice procedure and template; importer number data map; data regions confirmed; retention policy; retrieval procedure and first yearly test; backup restore test and MFA; training; recorded entry review; AI suggestion rule | G-008, G-009, G-010, G-013, G-014, G-017, G-018, G-020, G-021, G-033, G-041, G-043, G-048 |
| 3. Contracts and continuity | 2026-11-30 to 2026-12-31 | Client terms clause; messaging app replaced by a shared mailbox; new-client check and separation reporting; index of older scans; second licensed officer; continuing education records folder; supervision plan review | G-005, G-006, G-007, G-015, G-016, G-031, G-032, G-036, G-039, G-044, G-046 |
| 4. Annual cycle | 2027-01-31 to 2027-02-01 | Continuing education complete; triennial status report filed with certification | G-029, G-035 |

**Progress check.** The Office and Compliance Manager reports progress to the owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **No proposed change to Part 111 is pending.** A Federal Register search on 2026-10-04 for CBP rules on customs brokers found the 2022 modernization rule (87 FR 63267), the 2022 district permit fee rule (87 FR 63262), and the 2023 continuing education rule (88 FR 41224), all in force, and no later proposal. The `pending_rule_change` column is therefore "None" on every row.
- **The first continuing education certification** is a scheduled event, not a rule change: individual brokers certify with the status report due 2027-02-01 (111.101; 111.30(d)).
- **CIRCIA** (6 U.S.C. 681-681g): the final rule had not been published as of 2026-09-25. It is not treated as a current obligation (see P08).
