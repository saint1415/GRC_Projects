# Regulatory Gap Analysis: Cris Santos Company | Construction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Small / Construction |
| Primary regulation | FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems (NOV 2021), as verified by CMMC Level 1 (Self) under 32 CFR Part 170 and DFARS 252.204-7021 (NOV 2025) |
| Secondary regulation | FAR 52.204-25, Prohibition on Contracting for Certain Telecommunications and Video Surveillance Services or Equipment (NOV 2021), Section 889 |
| Applicability only | DFARS 252.204-7012 (MAY 2024) |
| Text verified | eCFR, 48 CFR and 32 CFR Part 170 as of 2026-09-23 |
| Assessment dates | 2026-07-13 to 2026-07-24; Section 889 rows updated 2026-08-07 after the P07 finding |
| Assessor | IT Manager with the Contracts Administrator and outside government contracts counsel |

## 1. Applicability
**FAR 52.204-21 applies now.** The clause is in all three federal contracts (FC-1 VA, FC-2 GSA, FC-3 DoD). It protects any "covered contractor information system", meaning a contractor-owned or -operated system that "processes, stores, or transmits Federal contract information" (52.204-21(a)). Drawings, submittals, schedules, daily logs, certified payrolls, and pay apps prepared for these contracts are FCI. Simple transactional information needed to process payments is excluded from the definition. There is **no size exemption**; the only exclusion is for acquisitions of commercially available off-the-shelf (COTS) items, which does not describe construction contracts. The clause must also be flowed down to subcontractors that may hold FCI (52.204-21(c)).

**CMMC Level 1 applies from the next DoD award, and possibly sooner.**
- 32 CFR Part 170 applies to DoD contractors and subcontractors that will process, store, or transmit FCI or CUI on contractor information systems (170.3(a)(1)). Level 1 consists of exactly the 15 requirements in FAR 52.204-21(b)(1)(i)-(xv) (170.14(c)(2)).
- FC-3 was awarded before Phase 1 began (2025-11-10), so it contains no DFARS 252.204-7021 clause today. During Phase 1, DoD may also require Level 1 (Self) as a condition of exercising an option on an older contract (170.3(e)(1)). The FC-3 parent contract has option periods, so this is a live risk.
- The DoD solicitation expected in 2026 Q4 is expected to require **Level 1 (Self)**. Before award, the company must achieve that status and submit an affirmation in SPRS (170.15(b)).
- Level 1 is **all or nothing**: every requirement must be MET, **no POA&M is permitted** (170.15(a)(1); 170.21(a)(1)), and results are scored MET or NOT MET in their entirety (170.24(c)(1)). The self-assessment must use the NIST SP 800-171A (June 2018) objectives for the mapped requirements (170.15(c)(1)).
- Specialized assets (IoT, OT, test equipment) are not part of the Level 1 scope (170.19(b)(2)(ii)). The company does not treat its client-installed systems as company assets at all.

**FAR 52.204-25 (Section 889) applies now, and matters more than usual here.** It is in all three federal contracts, with no size exemption. Two prohibitions apply:
- **(b)(1):** the company must not provide covered equipment to the Government. The security systems group installs cameras, recorders, and network switches in federal buildings, so this is a direct operational risk.
- **(b)(2):** the company must not *use* covered equipment, "regardless of whether that use is in performance of work under a Federal contract."

Video surveillance equipment from Hytera, Hikvision, and Dahua is covered only when used "for the purpose of public safety, security of Government facilities, physical security surveillance of critical infrastructure, and other national security purposes" (52.204-25(a)). Equipment installed to secure a federal building falls inside that purpose. Screening each purpose case by case is error-prone. On counsel's advice, the company's rule is simpler and stricter than the clause: **no products from any listed entity, or its subsidiaries or affiliates, on any project or in company use.**

**DFARS 252.204-7012 does not apply in practice today.** FC-3 includes the clause, but its duties attach to "covered contractor information systems" that hold covered defense information (CDI). No CDI has been marked, identified, or provided on FC-3. If CUI arrives, the company would need NIST SP 800-171, 72-hour incident reporting, and at least CMMC Level 2.

**Escalation decision.** The company is not ready for CUI. On 2026-08-31 the President decided not to pursue the DoD design-build opportunity with CUI facility drawings, and not to accept CUI work before 2028. The decision will be revisited in the 2027 risk assessment. Until then, the intake check in G-018 must catch any CUI that arrives unexpectedly.

**Not a size question.** None of these rules has a small-business exemption. The company's size only shapes *how* it meets them (for example, an MSP-run control rather than in-house staff).

## 2. Method
1. **Requirements.** Each paragraph of FAR 52.204-21(b)(1) is one row, using the clause's own numbering and quoting its text. Requirement (ix) is split into its three phrases, as in 32 CFR 170.15 Table 2, giving 17 rows for the 15 requirements. Clause paragraphs (b)(2) and (c), the CMMC program duties (32 CFR 170.15, 170.19, 170.22, 170.23; DFARS 252.204-7021), FAR 52.204-25, and the applicability of DFARS 252.204-7012 are separate rows.
2. **Crosswalk.**
   - Each FAR requirement follows an official chain: 32 CFR 170.15 Table 2 maps it to its NIST SP 800-171 R2 requirement.
   - The Rev. 3 successor requirement comes from the Rev. 3 withdrawal notes (for example, 3.10.3-3.10.5 were incorporated into 03.10.07).
   - CSF 2.0 subcategories come from NIST's CSF 2.0-to-SP 800-171 Rev. 3 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-171r3.csv`).
   - SP 800-53 controls come from the SP 800-171 Rev. 3 tailoring tables.
   - Where NIST publishes no CSF mapping (03.01.20, 03.01.22, 03.08.03), and for the CMMC, Section 889, and DFARS rows, the mapping is the author's and is labeled so in `crosswalk_source`.
3. **Evidence.** Current state was established from:
   - interviews with the CFO, Accounting Manager, Contracts Administrator, VP Operations, Systems Integration Manager, IT Manager, 3 Project Managers, and 2 superintendents
   - system exports from the identity provider, the ERP, SYS-01, and the antivirus console
   - a review of the subcontract template and SAM record
   - walkthroughs of the main office and 2 jobsites (2026-07-21)
4. **Status.** Each row is rated Met, Partially met, Not met, or Not applicable. For CMMC readiness, anything other than Met counts as NOT MET under 170.24(c)(1).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21 (17 requirement rows plus (b)(2) and (c)) | 3 | 11 | 4 | 1 |
| CMMC program duties (32 CFR 170; DFARS 252.204-7021) | 0 | 1 | 6 | 0 |
| FAR 52.204-25 Section 889 | 0 | 4 | 1 | 0 |
| DFARS 252.204-7012 (applicability) | 0 | 0 | 0 | 3 |
| **Total (34)** | **3** | **16** | **11** | **4** |

**Headline: the company could not achieve Final Level 1 (Self) today.** Only 3 of the 17 FAR requirement rows (G-015 to G-017, malicious code protection) are met. All other requirement rows (G-001 to G-014) must reach Met before the President can affirm. The same gaps mean the company is **not fully meeting a clause already in its three federal contracts**. That is a present contract compliance issue, not only a future eligibility issue.

**MFA note.** FAR 52.204-21 does not require multi-factor authentication. The company already uses push MFA and is moving payment roles to phishing-resistant MFA because of business email compromise (P01 R-001), not because this clause requires it.

## 4. Priority gaps and roadmap
Target: all Level 1 requirements Met by **2026-11-30**, readiness check in early December, SPRS entry and affirmation by **2026-12-15**.

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No self-assessment; Level 1 not achievable | 32 CFR 170.15; 170.21(a)(1) | High | Close all requirement gaps; self-assess against SP 800-171A objectives; SPRS and affirmation | IT Manager; President | 2026-12-15 |
| Shared accounts, default passwords, push MFA | 52.204-21(b)(1)(v)-(vi) | High | Named accounts; change defaults; phishing-resistant MFA for payment roles | IT Manager | 2026-11-30 |
| No separation of duties on vendor master and ACH | 52.204-21(b)(1)(ii) | High | Split vendor-master edits from payment release; dual ACH approval | Accounting Manager | 2026-09-30 |
| Covered video surveillance equipment on FC-1 | 52.204-25(b)(1) | Moderate | Replace equipment; submittal screening; approved-manufacturer list | Systems Integration Manager | 2026-10-31 |
| FCI in personal email and the AI tool | 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2) | Moderate | Approved external systems list; AI enterprise terms or stop federal uploads | IT Manager | 2026-10-31 |
| Public file-transfer portal on the internal subnet | 52.204-21(b)(1)(xi) | Moderate | Separate public subnet | IT Manager | 2026-10-31 |
| Stale external users and late terminations | 52.204-21(b)(1)(i) | Moderate | Closeout removal; same-day disable | IT Manager | 2026-10-31 |
| Clause substance not flowed down | 52.204-21(c); 52.204-25(e); 32 CFR 170.23 | Moderate | Federal subcontract rider; CMMC status check before award | Contracts Administrator | 2026-10-31 (CMMC check 2026-12-15) |
| Representations without a documented inquiry | 52.204-26 | Moderate | Documented reasonable inquiry; counsel review | Contracts Administrator | 2026-10-31 |
| No media sanitization; physical access devices unmanaged | 52.204-21(b)(1)(vii), (ix) | Low | Wipe standard and certificates; key and badge inventory | IT Manager; VP Operations | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). For CMMC purposes the POA&M is an internal work plan only. It cannot be used to claim Level 1 status.

**A word on affirmations.** The SPRS affirmation and the SAM representations are statements to the Government. An inaccurate one creates legal exposure, including under the False Claims Act (31 U.S.C. 3729). FAR 52.222-8(b)(4) gives the same warning for certified payrolls. The President will affirm only against a completed evidence binder reviewed by counsel (P01 R-008).

## 5. Pending regulatory changes
None of these is treated as a current obligation.
- **Revolutionary FAR Overhaul (RFO).** A proposed rule (FR Doc. 2026-12559, June 23, 2026) would move information security clauses to FAR part 40. Its conversion table maps 52.204-21 to a proposed 52.240-5. The clause mapping was read from the proposal and is not final. It would also add CUI clauses (proposed 52.240-6 and 52.240-7) based on NIST SP 800-171 Rev. 3, with CUI incident reporting within 72 hours. Comments closed 2026-07-23; no final rule has been published. The `pending_rule_change` column flags affected rows.
- **CMMC phase-in.** Phase 2 (planned for 2026-11-10, when Level 2 (C3PAO) would have become a condition of award where required) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 suspending CMMC Phase 2. This suspension is in effect, not pending. During the suspension requiring activities may require Level 1 (Self) or Level 2 (Self), and until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The expected 2026 Q4 Level 1 (Self) solicitation fits that rule, and FAR 52.204-21 is already in all three federal contracts. The rule text still shows Phase 3 beginning 2027-11-10; Phase 4 (full implementation, including option periods) begins 2028-11-10 (32 CFR 170.3(e)). None of these changes Level 1 content. By Phase 4, every applicable DoD contract, including option periods on older contracts, will carry the requirement.
- **Level 2 still uses SP 800-171 R2.** 32 CFR 170.14(c)(3) ties Level 2 to NIST SP 800-171 R2, even though NIST has published Rev. 3. This matters only if the company pursues CUI work after 2028.
