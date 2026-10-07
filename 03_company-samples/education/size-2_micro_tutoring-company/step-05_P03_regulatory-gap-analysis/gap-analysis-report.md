# Regulatory Gap Analysis: Cris Santos Company | Educational Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| Tier / Vertical | Micro / Educational Services |
| Regulation analyzed | Children's Online Privacy Protection Rule (COPPA Rule), 16 CFR Part 312 (N61-R03), as amended by 90 FR 16918 (Apr. 22, 2025): effective June 23, 2025; compliance date April 22, 2026 (except 312.11(d)(1), (d)(4), and (g)). Text checked on eCFR |
| Secondary | FERPA duties that flow down through the school district contract (N61-R01), 34 CFR 99.31 and 99.33 |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | Center Director (Information Security Coordinator) with the MSP lead technician |
| Approved | 2026-08-28 by the Owner |

## 1. Applicability
**Why not the vertical's default regulation.** The Educational Services default for P03 is the GLBA Safeguards Rule as enforced by Federal Student Aid for Title IV institutions. It does not reach this company: it is not a Title IV institution, it has no Program Participation Agreement, and it offers families no loans, payment plans, or other financial products. The rule that governs its core service is COPPA.

**The COPPA Rule applies.** The company is an "operator" (16 CFR 312.2): it operates an online service for commercial purposes, the tutoring platform's student portal and online classroom, and children's personal information is collected and maintained on its behalf by the platform vendor. The service is directed to children: its subject matter is K-12 tutoring, and about 250 of its 420 students are under 13. The personal information collected includes children's names, user names, photographs and video or audio files containing a child's image or voice (online sessions and recordings), and work samples combined with those identifiers (312.2, "personal information" paragraphs (1), (4), (8), and (11)). The nonprofit exclusion in the operator definition does not apply to a for-profit LLC.

**There is no size exemption.** The 2025 amendment to 312.8(b) scales the written information security program to "the sensitivity of the personal information collected from children and the operator's size, complexity, and nature and scope of activities." A 7-person company may keep the program short. It may not skip it.

**Compliance date.** The amended rule's compliance date was April 22, 2026. Fieldwork ended 2026-07-24, so every amended requirement (for example, the written security program in 312.8(b), the written retention policy in 312.10, and separate consent for non-integral disclosures in 312.5(a)(2)) was already due.

**School use.** For the 90 district program students, the company relies on the district's authorization instead of collecting consent from each parent. The FTC proposed codifying a school authorization exception in 2024 but did **not** finalize it; the final rule says the Commission will continue to enforce COPPA in the ed tech context consistent with its existing guidance (90 FR 16918, Part I.A). The company therefore documents the district's authorization and keeps the program data to the school's educational purpose (row G-019). Privacy counsel will confirm this approach as part of the notice rewrite.

**FERPA reaches the company only through the contract.** The company receives no funds under a Department of Education program, so it is not an educational agency or institution under 34 CFR 99.1. The district may disclose program students' education records to it as a contractor treated as a school official, but only if the company stays under the district's direct control for use and maintenance of the records and follows the redisclosure limits in 99.33(a) (99.31(a)(1)(i)(B)). Those conditions are in the data privacy agreement, so four FERPA rows were added as a short secondary section. If a future district contract is paid from a federal program grant or subgrant, counsel should re-check 99.1(c) before signing.

**Excluded, with reasons (8 rows):** the 312.4(c) and 312.5(c) notice content and consent exceptions that the company does not use (5 rows), the 312.4(d)(3)-(4) notice items tied to exceptions it does not use (2 rows), and 312.11 safe harbor programs (voluntary; 1 row).

**Related rules considered but not analyzed row by row:**
- **Fla. Stat. 501.171** (reasonable measures, breach notice, disposal) drives the P08 notification matrix and the disposal rule in POL-04.
- **COPPA has no breach notification requirement.** Breach notice duties come from Florida law and the district contract (P08).
- **CIRCIA** (N61-R06) is proposed only and would not reach the company under the proposed criteria.

## 2. Method
1. **Requirements.** Each row is a paragraph of 16 CFR 312.4 to 312.11 at the level the rule itself uses (for example, 312.4(c)(1)(i) to (vii)), plus four FERPA paragraphs. Summaries paraphrase public-domain regulatory text.
2. **Requirement type.** COPPA has no required/addressable split. Its duties are **Mandatory**. Rows tied to an exception or "if applicable" wording are **Conditional**. The FERPA rows are **conditions of disclosure** that reach the company through the contract.
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5, including the privacy controls PT-3, PT-4, PT-5, AC-3(14), and SI-18(4). These are **author mappings**; NIST publishes no official mapping for 16 CFR Part 312.
4. **Documentary evidence.** Each status rests on a named document or record: the website privacy notice (copy of 2026-07-14), the enrollment agreement and the SYS-02 consent records, the platform's trial account list and settings, the platform terms of service, parent request emails, the shared-drive permission report, contractor agreements, the district contract and data privacy agreement, and the MSP's reports. Interviews covered the Owner, all staff, 3 contractor tutors, and the MSP lead technician.
5. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since then (for example, the policies approved 2026-08-28) are noted in the remediation columns but do not change the status.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 312.4 Notice | 1 | 5 | 5 | 5 |
| 312.5 Parental consent | 0 | 2 | 1 | 2 |
| 312.6 Parental review | 1 | 3 | 1 | 0 |
| 312.7 No conditioning | 1 | 0 | 0 | 0 |
| 312.8 Confidentiality, security, and integrity | 1 | 3 | 4 | 0 |
| 312.10 Retention and deletion | 0 | 0 | 5 | 0 |
| 312.11 Safe harbor programs | 0 | 0 | 0 | 1 |
| **COPPA subtotal (41)** | **4** | **13** | **16** | **8** |
| FERPA through the district contract (4) | 0 | 4 | 0 | 0 |
| **Total (45)** | **4** | **17** | **16** | **8** |

Of the 33 unmet or partially met rows, 29 are Mandatory COPPA requirements and 4 are FERPA conditions of disclosure. By gap risk: 3 High, 23 Moderate, 7 Low.

**What the numbers say.** The company does a few things well: it designated a security coordinator, uses a recognized consent method (a card transaction) for most families, does not ask children for more information than tutoring needs, and answers parents quickly. The worst areas are the ones the 2025 amendments added or sharpened: no written security program, no written retention policy, nothing deleted since 2019, and no due diligence on vendors. Every 312.10 row is Not met.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No written information security program after the compliance date | 312.8(b) | High | SSP (P02) and policies (P06) adopted as the written program | Center Director | 2026-08-28 (done) |
| Children's accounts created before consent; no consent to the AI module change | 312.5(a)(1) | High | Consent step before any account; end trial accounts; new consent before any AI restart | Director of Tutoring | 2026-09-30 |
| No MFA in the platform; open "Student files" folder; rosters on personal computers | 312.8(b)(3) | High | MFA, folder restriction, contractor device rules, segmentation | Center Director | 2026-12-31 |
| Online and direct notices incomplete | 312.4(a), (c)(1), (d)(2), (d)(5) | Moderate | New children's privacy notice and direct notice, reviewed by counsel | Center Director | 2026-10-31 |
| Possible non-integral disclosure to the platform vendor for AI training | 312.5(a)(2); 312.8(c); 99.33(a) | Moderate | Data processing addendum barring model training; AI module off | Director of Tutoring | 2026-10-31 |
| No vendor due diligence or written assurances | 312.8(c) | Moderate | Addendum with security assurances; yearly SOC 2 review; MSP and contractor terms | Center Director | 2026-10-31 |
| No retention policy; records and recordings kept since 2019 | 312.10 | Moderate | POL-04 4.9 schedule; platform retention settings; first purge | Center Director | 2026-11-30 |
| No identity check on parent requests | 312.6(a)(3)(i) | Moderate | Portal sign-in or call-back verification; request log | Center Director | 2026-10-31 |
| District rosters outside the district's control | 99.31(a)(1)(i)(B); 99.31(a)(1)(ii) | Moderate | Platform-only access by assignment; contractor deletion attestations | Director of Tutoring | 2026-09-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are notice text, platform settings, and one-page procedures, not new systems. The MSP does the technical work under the Center Director's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Program and consent | 2026-09-30 | Written program adopted (done 2026-08-28); consent before any account; end trial accounts and delete trial data without consent; stop roster emails; new contractor agreement; platform-only roster access | 312.8(b); 312.5(a)(1); 99.31(a)(1)(i)(B); 99.31(a)(1)(ii); 99.33(a)(2) |
| 2. Notices and vendors | 2026-10-31 | New online notice and direct notice; links in the student portal and classroom; consent form for bank-debit families; written district authorization; data processing addendum; parent request procedure with verification; data inventory; MFA everywhere; log and account review starts; restore test | 312.4(a), (b), (c)(1)(ii)-(v), (d), (d)(1), (d)(2), (d)(5); 312.5(a)(2), (b); 312.6(a)(1)-(3)(i); 312.8(b)(2), (b)(4), (c); 312.10 (notice); 99.33(a)(1) |
| 3. Retention | 2026-11-30 | Platform retention settings; first purge of former students' records and old recordings; deletion record; shred bin | 312.10 (all rows) |
| 4. Safeguards | 2026-12-31 | Folder restriction; network segmentation; EDR and alerts; backup upgrade | 312.8(a), (b)(3) |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk assessment update (July); program evaluation and policy review (August) | 312.8(b)(2), (b)(5) |

**Progress check.** The Center Director reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **COPPA Rule:** the 2025 amendments are final and in force; the safe harbor items in 312.11(d)(1), (d)(4), and (g) are excluded from the April 22, 2026 compliance date and do not apply to the company, which belongs to no safe harbor program. No further FTC amendment was identified. The FTC's 2024 proposals on ed tech and school authorization were **not** finalized and are not treated as rules.
- **FERPA:** the FTC noted that the Department of Education intends to propose FERPA amendments. Nothing has been proposed that changes the analysis above; the company will re-check at the July 2027 review.
- **CIRCIA** (N61-R06) remains proposed only (89 FR 23644) and is not a current obligation.

The `pending_rule_change` column in `gap-analysis.csv` is "None" for every row because no pending change affects a row today.
