# Regulatory Gap Analysis: Cris Santos Company | Construction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| Tier / Vertical | Sole Proprietorship / Construction |
| Primary regulation | FAR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems (NOV 2021), as verified by CMMC Level 1 (Self) under 32 CFR Part 170 and DFARS 252.204-7021 (NOV 2025) |
| Secondary regulation | FAR 52.204-25, Prohibition on Contracting for Certain Telecommunications and Video Surveillance Services or Equipment (NOV 2021), Section 889 |
| Applicability only | DFARS 252.204-7012 (MAY 2024) |
| Text verified | eCFR, 48 CFR (FAR 2.101, 4.1903, 52.204-21, 52.204-25; DFARS 252.204-7021) and 32 CFR Part 170, as of 2026-09-23 |
| Assessment dates | 2026-07-13 to 2026-07-17 (self-assessment); G-006 updated after P07 testing on 2026-07-21 |
| Assessor | Owner, with the on-call IT technician on 2026-07-15 and 2026-07-16. Evidence is self-attested and checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**FAR 52.204-21 applies now, through FC-1.** The clause is in the VA contract. FAR 4.1903 requires it whenever "the contractor or a subcontractor at any tier may have Federal contract information residing in or transiting through its information system". It has **no dollar threshold and no size exemption**. A "covered contractor information system" is any system "owned or operated by a contractor that processes, stores, or transmits Federal contract information" (52.204-21(a)). For this company that is the owner's own laptop, personal phone, home network, and SaaS accounts. FC-1 drawings, submittals, daily logs, and pay apps are FCI. Simple transactional information needed to process payments is excluded.

**CMMC Level 1 applies before the DoD subcontract is awarded.**
- 32 CFR Part 170 applies to DoD contract and **subcontract** awardees that will process, store, or transmit FCI on contractor information systems (170.3(a)(1)). The program applies above the micro-purchase threshold (170.3(c)), which is only $2,000 for construction subject to the wage rate requirements (FAR 2.101). The roughly $45,000 subcontract is well above it.
- A subcontractor that will handle only FCI needs **Level 1 (Self)** (170.23(a)(1)). The prime must make sure the owner has a current status before awarding the subcontract (DFARS 252.204-7021(f)(2)), and the owner must have achieved Level 1 (Self) and submitted an affirmation in SPRS before award (170.15(b)).
- Level 1 is exactly the 15 FAR 52.204-21 requirements, assessed with the NIST SP 800-171A (June 2018) objectives (170.15(c)(1)). Every requirement must be MET, **no POA&M is permitted** (170.15(a)(1)), and results are scored MET or NOT MET in their entirety (170.24(c)(1)). A requirement that does not apply is assessed as MET (170.24(b)(3)).
- The owner, as the senior person in the company, is the Affirming Official (170.22(a)(1)) and must affirm after the self-assessment and every year (170.22(b)(1)).

**FAR 52.204-25 (Section 889) applies now, through FC-1.** No size exemption. Two prohibitions matter:
- **(b)(1):** do not provide covered equipment to the Government. FC-1 has no network or camera equipment, but the DoD subcontract includes a wireless door-access upgrade.
- **(b)(2):** do not *use* covered equipment, "regardless of whether that use is in performance of work under a Federal contract." This reached the owner's own mobile hotspot (G-028).

**DFARS 252.204-7012 does not apply.** FC-1 is a civilian contract, and the DoD subcontract is expected to carry FCI only. If CUI ever appears, the owner will refuse it (G-018, G-032), because a one-person firm cannot reasonably meet NIST SP 800-171 and CMMC Level 2.

**Not a size question.** None of these rules has a small-business or one-person exemption. Size only shapes *how* the owner meets them: settings in SaaS accounts and on two devices, a home office door lock, and a paper visitor log.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** Each paragraph of FAR 52.204-21(b)(1) is one row with the clause's own text. Requirement (ix) is split into its three phrases, as in 32 CFR 170.15 Table 2, giving 17 rows for the 15 requirements. Clause paragraphs (b)(2) and (c), the CMMC duties, FAR 52.204-25, and the applicability of DFARS 252.204-7012 are separate rows. **32 rows in all.**
2. **Crosswalk.** FAR rows follow the official chain used in the Small construction sample: 32 CFR 170.15 Table 2 maps each requirement to NIST SP 800-171 R2; the Rev. 3 withdrawal notes give the Rev. 3 successor; CSF 2.0 comes from NIST's CSF 2.0-to-SP 800-171 Rev. 3 mapping; SP 800-53 comes from the SP 800-171 Rev. 3 tailoring tables. Where NIST publishes no mapping, and for the CMMC, Section 889, and DFARS rows, the mapping is the author's and is labeled so in `crosswalk_source`.
3. **Evidence.** Self-attested by the owner, checked on screen with the IT technician (account and user lists, device settings, router settings, the AI tool's upload history), a walkthrough of the home office, truck, and storage unit on 2026-07-15, and a review of the subcontract form and SAM record.
4. **Status.** Met, Partially met, Not met, or Not applicable. For CMMC readiness, anything other than Met (or Not applicable) counts as NOT MET under 170.24(c)(1).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FAR 52.204-21 (17 requirement rows plus (b)(2) and (c)) | 3 | 10 | 4 | 2 |
| CMMC program duties (32 CFR 170; DFARS 252.204-7021) | 0 | 1 | 6 | 0 |
| FAR 52.204-25 Section 889 | 0 | 4 | 1 | 0 |
| DFARS 252.204-7012 (applicability) | 0 | 0 | 0 | 1 |
| **Total (32)** | **3** | **15** | **11** | **3** |

Of the 26 rows not met or partially met, gap risk is 2 High, 14 Moderate, and 10 Low.

**Headline: the owner could not achieve Final Level 1 (Self) today.** Of the 17 FAR requirement rows, only the 3 malicious code rows (G-015 to G-017) are met and 1 is not applicable (G-013). The other 13 must reach Met before the owner can affirm. The same gaps mean the company is **not fully meeting a clause already in FC-1**, which is a present contract compliance issue, not only a future eligibility issue.

**MFA note.** FAR 52.204-21 does not require multi-factor authentication. The owner is adding MFA and a security key because of business email compromise (P01 R-001), not because the clause requires it.

## 4. Action list (half page)
Target: every Level 1 requirement Met by **2026-11-15**, self-assessment by **2026-11-20**, SPRS entry and affirmation by **2026-11-30**.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Password manager; MFA on SYS-01 and SYS-02; security key on email; no default device passwords | 52.204-21(b)(1)(vi) | High | 2026-10-31 |
| 2 | Separate laptop accounts for family; separate accounting account for the bookkeeper; remove stale portal users | 52.204-21(b)(1)(i), (ii), (v) | Moderate | 2026-09-30 |
| 3 | Approved locations for FCI; photo sync off; no FCI in the AI tool without no-training terms | 52.204-21(b)(1)(iii); DFARS 252.204-7021(d)(2) | Moderate | 2026-09-30 |
| 4 | Separate work network; update or replace the router | 52.204-21(b)(1)(x), (xii) | Moderate | 2026-09-30 |
| 5 | Federal subcontract rider with 52.204-21 and 52.204-25 substance; plan the lower-tier CMMC approach | 52.204-21(c); 52.204-25(e); 32 CFR 170.23 | Moderate | 2026-10-31 |
| 6 | Return the hotspot; purchase check; documented inquiry before each SAM renewal; ask whether to update the SAM representation | 52.204-25(b)(2); 52.204-26 | Moderate | 2026-10-31 |
| 7 | Wipe the old laptop; office door lock; truck box; visitor log; key list | 52.204-21(b)(1)(vii)-(ix) | Low | 2026-10-31 |
| 8 | Self-assessment against the 800-171A objectives, with the IT technician as an outside reader | 32 CFR 170.15(c)(1) | High | 2026-11-20 |
| 9 | SPRS access, results entry, and affirmation; evidence kept 6 years | 32 CFR 170.15(a)(1)(i), (c)(2); 170.22 | Moderate | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). For CMMC purposes the POA&M is an internal work plan only. It cannot be used to claim Level 1 status.

**A word on affirmations.** The SPRS affirmation and the SAM representations are statements to the Government. An inaccurate one creates legal exposure, including under the False Claims Act (31 U.S.C. 3729). The owner will affirm only against a complete evidence folder, and will ask a government contracting assistance counselor or counsel to look at the January 2026 SAM representation (G-031).

## 5. Pending regulatory changes
None of these is treated as a current obligation.
- **Revolutionary FAR Overhaul (RFO).** A proposed rule (FR Doc. 2026-12559, published 2026-06-23; comments closed 2026-07-23) would move information security clauses into FAR part 40 and renumber them, and would add CUI clauses based on NIST SP 800-171 Rev. 3. It is not final. The `pending_rule_change` column flags the affected rows.
- **CMMC phase-in.** Phase 2 was planned for 2026-11-10 (32 CFR 170.3(e)) but is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. Under DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5), DoD includes clause 252.204-7021 until 2028-11-09 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self). On or after 2028-11-10, DoD includes the clause whenever the contractor will process, store, or transmit FCI or CUI on its own systems (except COTS-only buys). None of this changes Level 1 content. Unlike the proposed items, this suspension is in effect.
