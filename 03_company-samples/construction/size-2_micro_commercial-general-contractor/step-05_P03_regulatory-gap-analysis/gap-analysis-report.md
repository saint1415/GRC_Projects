# Regulatory Gap Analysis: Cris Santos Company | Construction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Micro / Construction |
| Primary regulation | FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems (NOV 2021), as verified by CMMC Level 1 (Self) under 32 CFR Part 170 and DFARS 252.204-7021 (NOV 2025) |
| Secondary regulation | FAR 52.204-25, Prohibition on Contracting for Certain Telecommunications and Video Surveillance Services or Equipment (NOV 2021), Section 889 |
| Applicability only | DFARS 252.204-7012 (MAY 2024) |
| Text verified | eCFR, 48 CFR and 32 CFR Part 170 as of 2026-09-23 |
| Assessment dates | 2026-07-20 to 2026-07-31; Section 889 rows updated 2026-07-28 after the FC-1 submittal finding |
| Assessor | Office Manager (security and compliance lead) with the MSP lead technician; outside government contracts counsel consulted on Section 889 |
| Approved | 2026-08-31 by the Owner and President |

## 1. Applicability
**FAR 52.204-21 applies now.** The clause is in the company's one federal contract (FC-1, VA). It protects any "covered contractor information system", meaning a contractor-owned or -operated system that "processes, stores, or transmits Federal contract information" (52.204-21(a)). Drawings, submittals, schedules, daily logs, certified payrolls, and pay apps prepared for FC-1 are FCI. Simple transactional information needed to process payments is excluded from the definition. There is **no size exemption**: the only exclusion is for acquisitions of commercially available off-the-shelf (COTS) items, which does not describe a construction contract. The clause must also be flowed down to subcontractors that may hold FCI (52.204-21(c)).

**CMMC Level 1 applies from the next DoD award.**
- 32 CFR Part 170 applies to DoD contractors and subcontractors that will process, store, or transmit FCI or CUI on contractor information systems (170.3(a)(1)). Level 1 consists of exactly the 15 requirements in FAR 52.204-21(b)(1)(i)-(xv) (170.14(c)(2)).
- The DoD pre-solicitation notice (July 2026) says the solicitation will require **Level 1 (Self)** through DFARS 252.204-7021. Before award, the company must achieve that status and have an affirmation in SPRS (170.15(b)). Award is expected in January 2027, so the target is 2026-12-15.
- Level 1 is **all or nothing**. Every requirement must be MET, **no POA&M is permitted** (170.15(a)(1); 170.21(a)(1)), and results are scored MET or NOT MET in their entirety (170.24(c)(1)). The self-assessment must use the NIST SP 800-171A (June 2018) objectives for the mapped requirements (170.15(c)(1)).

**FAR 52.204-25 (Section 889) applies now.** It is in FC-1, with no size exemption. Two prohibitions apply:
- **(b)(1):** the company must not *provide* covered equipment to the Government. The company does not install security systems itself, but its low-voltage subcontractor does, under the company's prime contract. The company is responsible for what its subcontractors deliver.
- **(b)(2):** the company must not *use* covered equipment, "regardless of whether that use is in performance of work under a Federal contract."

Video surveillance equipment from Hytera, Hikvision, and Dahua (and their subsidiaries and affiliates) is covered only when used "for the purpose of public safety, security of Government facilities, physical security surveillance of critical infrastructure, and other national security purposes" (52.204-25(a)). Cameras that secure a VA clinic fall inside that purpose. On counsel's advice, the company's rule is simpler and stricter than the clause: **no products from any listed entity, or its subsidiaries or affiliates, on any project or in company use** (POL-02 A.8).

**DFARS 252.204-7012 does not apply today.** The company has no DoD contract. The expected DoD job involves FCI only. If CUI ever arrived, the company would need NIST SP 800-171, 72-hour incident reporting, and at least CMMC Level 2.

**Escalation decision.** A 7-person company cannot carry the 110 NIST SP 800-171 requirements and a third-party assessment. On 2026-08-31 the Owner decided not to bid work that needs CUI. The decision will be revisited in the 2027 risk assessment. Until then, the intake check in G-018 must catch any CUI that arrives unexpectedly.

**Not a size question.** None of these rules has a small-business exemption. The company's size changes only *how* it meets them: the MSP runs most technical controls, and one part-time lead keeps the evidence.

## 2. Method
1. **Requirements.** Each paragraph of FAR 52.204-21(b)(1) is one row, using the clause's own numbering and quoting its text. Requirement (ix) is split into its three phrases, as in 32 CFR 170.15 Table 2, giving 17 rows for the 15 requirements. Clause paragraphs (b)(2) and (c), the CMMC program duties (32 CFR 170.15, 170.19, 170.22, 170.23; DFARS 252.204-7021), FAR 52.204-25, and the applicability of DFARS 252.204-7012 are separate rows. Total: 34 rows.
2. **Crosswalk.**
   - Each FAR requirement follows an official chain: 32 CFR 170.15 Table 2 maps it to its NIST SP 800-171 R2 requirement.
   - The Rev. 3 successor requirement comes from the Rev. 3 withdrawal notes (for example, 3.10.3-3.10.5 were incorporated into 03.10.07).
   - CSF 2.0 subcategories come from NIST's CSF 2.0-to-SP 800-171 Rev. 3 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-171r3.csv`).
   - SP 800-53 controls come from the SP 800-171 Rev. 3 tailoring tables.
   - Where NIST publishes no CSF mapping (03.01.20, 03.01.22, 03.08.03), and for the CMMC, Section 889, and DFARS rows, the mapping is the author's and is labeled so in `crosswalk_source`.
3. **Documentary evidence.** Each status rests on a named document or record:
   - user exports from the productivity suite and SYS-01, and the SYS-02 and bank portal role lists
   - the MSP's device list, patch report, antivirus console export, firewall rule export, and backup job report
   - the FC-1 contract, its subcontracts, the subcontract template, and the FC-1 submittal log
   - the SAM registration record, the website history, and the alarm panel log
   - a walkthrough of the office and 2 jobsites (2026-07-22), and interviews with all 5 staff who use systems, both Carpenters (visitors and keys), and the MSP lead technician
4. **Status.** Each row is rated Met, Partially met, Not met, or Not applicable as of the end of fieldwork (2026-07-31). For CMMC readiness, anything other than Met counts as NOT MET under 170.24(c)(1).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21 (17 requirement rows plus (b)(2) and (c)) | 4 | 10 | 4 | 1 |
| CMMC program duties (32 CFR 170; DFARS 252.204-7021) | 0 | 1 | 6 | 0 |
| FAR 52.204-25 Section 889 | 0 | 5 | 0 | 0 |
| DFARS 252.204-7012 (applicability) | 0 | 0 | 0 | 3 |
| **Total (34)** | **4** | **16** | **10** | **4** |

Of the 26 unmet or partially met rows, 3 are High gap risk, 14 Moderate, and 9 Low.

**Headline: the company could not achieve Final Level 1 (Self) today.** 4 of the 17 FAR requirement rows are met: G-013 (no public-facing systems to separate, which 32 CFR 170.24(b)(3) treats as MET) and G-015 to G-017 (malicious code protection, which the MSP runs). The other 13 rows (G-001 to G-012 and G-014) must reach Met before the Owner can affirm. The same gaps mean the company is **not fully meeting a clause already in FC-1**. That is a present contract compliance issue, not only a future eligibility issue.

**What the numbers say.** The MSP-run controls score best (antivirus, patching of laptops, the firewall). The weakest areas are the ones only the company can fix: who has access, where drawings go, physical keys and visitors, and the paperwork the Government relies on (subcontract flowdown, SAM representations, SPRS).

**MFA note.** FAR 52.204-21 does not require multi-factor authentication. The company already uses push MFA and is moving the payment roles to security keys because of business email compromise (P01 R-001), not because this clause requires it.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No self-assessment; Level 1 not achievable | 32 CFR 170.15; 170.21(a)(1) | High | Close all requirement gaps; self-assess against SP 800-171A objectives; SPRS entry and affirmation | Office Manager; Owner | 2026-12-15 |
| One person controls vendor bank details; flat shared drive | 52.204-21(b)(1)(ii) | High | Owner approval of bank changes after a call-back; folders by role | Owner | 2026-09-30 |
| Shared and default passwords; tablet without passcode | 52.204-21(b)(1)(vi) | High | Retire shared password; change defaults; device management | Office Manager (MSP performs) | 2026-10-31 |
| FCI in personal email and the AI tool | 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2) | Moderate | Approved-systems list; block forwarding; AI tool conditions or no FCI uploads | Project Manager and Estimator | 2026-10-15 |
| Late removal of leavers and closed-project users | 52.204-21(b)(1)(i) | Moderate | Termination checklist; closeout removal | Office Manager | 2026-10-31 |
| Visitors on the company network | 52.204-21(b)(1)(x) | Moderate | Separate guest Wi-Fi; monthly log check | Office Manager (MSP performs) | 2026-10-31 |
| No submittal screening for covered equipment | 52.204-25(b)(1) | Moderate | Section 889 check in submittal review; approved-manufacturer list | Project Manager and Estimator | 2026-09-30 |
| Clause substance not flowed down | 52.204-21(c); 52.204-25(e); 32 CFR 170.23 | Moderate | Federal subcontract rider; SPRS status check before DoD subcontract awards | Owner | 2026-09-30 (CMMC check 2026-12-15) |
| Representations without a documented inquiry | 52.204-26 | Moderate | Documented reasonable inquiry; counsel review | Owner | 2026-10-31 |
| No sanitization records; keys, codes, and visitors unmanaged | 52.204-21(b)(1)(vii), (ix) | Low | Wipe and destruction records; key list; individual alarm codes; visitor sheet | Office Manager; Owner | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07). For CMMC purposes the POA&M is an internal work plan only. It cannot be used to claim Level 1 status.

## 5. Remediation plan
The plan fits a 7-person company: most actions are MSP settings, one-page procedures, or contract riders, not new systems. The MSP does the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Payments, paperwork, and people | 2026-09-30 | Owner approval of bank changes; termination checklist; subcontract rider reissued to the 6 FC-1 subcontractors; Section 889 submittal check; pre-posting checklist; visitor sheet; key list, rekey, and individual alarm codes; Section 889 reporting procedure | G-002, G-004, G-009, G-010, G-011, G-019, G-027, G-029, G-030 |
| 2. Accounts, devices, and network | 2026-10-31 | Named access to the bids mailbox; default passwords changed; phones and tablets in device management; separate guest Wi-Fi; firmware updates and first vulnerability scan; approved-systems list and forwarding block; wipe records; SAM inquiry documented; service provider confirmations | G-001, G-003, G-005, G-006, G-007, G-008, G-012, G-014, G-028, G-031 |
| 3. Scope and evidence | 2026-11-30 | Inventory complete; no FCI outside the PPS; evidence folder with deletion lock; readiness walk-through with the P07 consultant | G-020, G-024, G-025 |
| 4. Self-assessment and affirmation | 2026-12-15 | Self-assessment against the SP 800-171A objectives; SPRS access and entry; counsel review of the evidence binder; Owner's affirmation; CMMC flowdown and subcontractor status check ready for the DoD job | G-021, G-022, G-023, G-026 |
| 5. Annual cycle | 2027-07-31 to 2027-12-15 | Risk assessment update (July); control assessment (August); Level 1 self-assessment and affirmation repeated before the status is a year old | G-021, G-023 |

**Progress check.** The Office Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

**A word on affirmations.** The SPRS affirmation and the SAM representations are statements to the Government. An inaccurate one creates legal exposure, including under the False Claims Act (31 U.S.C. 3729). FAR 52.222-8(b)(4) gives the same warning for certified payrolls. The Owner will affirm only against a completed evidence binder reviewed by counsel (P01 R-007).

## 6. Pending regulatory changes
None of these is treated as a current obligation.
- **Revolutionary FAR Overhaul (RFO).** A proposed rule (FR Doc. 2026-12559, published 2026-06-23; comments were due 2026-07-23) would move information security clauses to FAR part 40. Its conversion table maps 52.204-21 to a proposed 52.240-5. It would also add CUI clauses (proposed 52.240-6 and 52.240-7). No final rule has been published. The `pending_rule_change` column flags affected rows.
- **CMMC phase-in.** Phase 2 (planned for 2026-11-10, when Level 2 (C3PAO) was to become a condition of award where required) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. Until 2028-11-09 DoD includes clause 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). On or after 2028-11-10 the clause goes into solicitations and contracts wherever contractor systems process, store, or transmit FCI or CUI, except buys solely for COTS items (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). 32 CFR 170.3(e) itself is unchanged. None of this changes Level 1 content. It means that from 2028-11-10 every future DoD job with FCI on company systems will carry the requirement.
- **Level 2 still uses SP 800-171 R2.** 32 CFR 170.14(c)(3) ties Level 2 to NIST SP 800-171 R2, even though NIST has published Rev. 3. This matters only if the Owner reverses the decision on CUI work.
