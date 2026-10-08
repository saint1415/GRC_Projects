# Regulatory Gap Analysis: Cris Santos Company | Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Tier / Vertical | Sole Proprietorship / Manufacturing (NAICS 332710) |
| Regulation analyzed | FAR 52.204-21 Basic Safeguarding (NOV 2021) and CMMC Level 1 (Self) (32 CFR Part 170; DFARS 252.204-7021, NOV 2025), both by flowdown from the aerospace customer |
| Benchmark | NIST CSF 2.0, using the Small Business Quick-Start Guide (NIST SP 1300, February 2024) |
| Also checked | FD&C Act section 524B and the QMSR (not applicable, with reasons); OEM contract terms that flow from the QMSR |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment). Regulatory text re-read on eCFR on 2026-09-27 |
| Assessor | Owner-machinist, with the on-call IT technician (under NDA since 2026-08-07). Evidence is self-attested |
| Adopted | 2026-09-04 |

## 1. Applicability
**The vertical's primary regulation does not apply.** Section 524B of the FD&C Act binds "a person who submits" a 510(k), PMA, PDP, De Novo, or HDE for a cyber device (21 U.S.C. 360n-2(a)). The shop makes machined components to OEM drawings and submits nothing to FDA. The three OEM customers are the submitters and carry 524B for their devices.

**The QMSR binds the OEMs, not the shop.** The Quality Management System Regulation (21 CFR Part 820), which incorporates ISO 13485 by reference, took effect on 2026-02-02 (89 FR 7496). Section 820.1(a)(2) says it does not apply to manufacturers of components or parts of finished devices, which are "encouraged to consider provisions of this regulation as appropriate." The OEMs meet their own purchasing-control duty (820.10(a), ISO 13485 clause 7.4) by putting requirements into supplier quality agreements and POs. Those contract terms (rows G-030 to G-033) are what the shop must meet.

**FAR 52.204-21 applies by flowdown.** The aerospace customer is a DoD subcontractor. FAR 52.204-21(c) requires the clause to flow to any subcontract "in which the subcontractor may have Federal contract information residing in or transiting through its information system," including commercial products other than COTS items. The customer's drawings are "not intended for public release" and are "generated for the Government under a contract" (the FCI definition in 52.204-21(a)). They arrive by email and portal, sit in the shop's file plan, and become CNC programs on the laptop. So the shop's systems are covered contractor information systems, and the 15 requirements in 52.204-21(b)(1) apply to them. There is no size exemption.

**CMMC Level 1 (Self) applies from the next award.** DFARS 252.204-7021(f) and 32 CFR 170.23(a)(1) require a prime to flow CMMC down to any subcontractor that will process FCI, and a subcontractor that handles FCI only needs Level 1 (Self). CMMC Phase 1 began on 2025-11-10, when the DFARS acquisition rule took effect (32 CFR 170.3(e)(1)). The customer's supplier letter (2026-06-15) says the shop must hold a Final Level 1 (Self) status and an affirmation in SPRS before the December 2026 award. Level 1 means:
- a self-assessment of the same 15 FAR requirements (32 CFR 170.14(c)), scored with the SP 800-171A objectives (170.15(c)(1));
- a MET result on every requirement, with **no POA&M allowed** (170.15(a)(1));
- results in SPRS with the CAGE code(s) for the systems in scope (170.15(a)(1)(i));
- an affirmation by the affirming official after the assessment and every year (170.22);
- evidence kept for six years (170.15(c)(2)).

**Scoping helps a machine shop.** Operational technology is a "specialized asset" that is not part of the Level 1 assessment scope (170.19(b)(2)(ii)). The CNC controllers are therefore not assessed, although FAR 52.204-21 itself has no such carve-out, so the shop still protects them where it can.

**Not applicable today, with the trigger that would change it (5 rows):**
- **DFARS 252.204-7012** and **CMMC Level 2**: the customer sends no CUI or covered defense information and does not flow 7012 down. Trigger: a drawing marked CUI or with a DoD distribution statement.
- **ITAR registration** (22 CFR 122.1(a)): one occasion of manufacturing a defense article requires registration, even with no exports. The customer states its parts are not defense articles. Trigger: an ITAR marking or a customer statement that a part is a defense article.
- **Section 524B** and the **QMSR** directly, as above.

Two related items: FAR 52.204-25 (Section 889) also flows down, but only its reporting duty matters to a parts supplier (row G-006). HIPAA does not apply (no PHI).

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** FAR 52.204-21 rows follow the clause structure, paragraphs (b)(1)(i) to (xv) and (c), with a short quote of each requirement (public-domain regulation text). CMMC rows cite the 32 CFR 170 and DFARS 252.204-7021 paragraphs. OEM rows are the shop's contract terms. Benchmark rows are the 22 CSF 2.0 categories, with the SP 1300 quick-start actions in the author's words.
2. **Crosswalk.** For the FAR rows, the CMMC requirement ID and SP 800-171 R2 number come from 32 CFR 170.15(c)(1)(ii) Table 2 (official). The CSF 2.0 and SP 800-53 columns are an **author mapping**. For the CSF benchmark rows, the SP 800-53 controls are a subset of NIST's official CSF 2.0 informative references.
3. **Evidence.** Self-attested by the owner, checked on screen with the IT technician (account and sharing settings, router settings, sent email, website gallery, drawer inventory, and a walkthrough on 2026-08-11).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps rated on the P01 scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Applicability checks (524B, QMSR, DFARS 7012, CMMC Level 2, ITAR) | 5 | 0 | 0 | 0 | 5 |
| FAR 52.204-25 (Section 889) | 1 | 0 | 1 | 0 | 0 |
| FAR 52.204-21 (15 requirements plus flowdown) | 16 | 4 | 8 | 4 | 0 |
| CMMC Level 1 (Self) program | 7 | 0 | 1 | 6 | 0 |
| OEM contract terms (QMSR flowed by contract) | 4 | 0 | 3 | 1 | 0 |
| NIST CSF 2.0 benchmark (22 categories) | 22 | 1 | 10 | 11 | 0 |
| **Total** | **55** | **5** | **23** | **22** | **5** |

The 45 unmet or partially met rows break down by gap risk as 11 High, 20 Moderate, and 14 Low.

**The main finding:** 11 of the 15 FAR 52.204-21 requirements are not fully met, and Level 1 allows no plan of action. Every one of them must be fixed, not just scheduled, before the owner can honestly affirm in SPRS. Most fixes are settings and habits, not purchases: a visitor log, a password on the VMC share, named-person sharing, a disposal record, and a list of approved external systems. The one purchase is a small business router that can separate the laptop and VMC from visitors.

## 4. Action list (half page)
In order. The CMMC deadline drives the sequence.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt POL-01 (roles, affirming official, risk rules, retention) | CSF GV.PO, GV.RR; 170.15(c)(2) | Moderate | 2026-09-04 (done) |
| 2 | Visitor log, escort rule, key list; website photo check | 52.204-21(b)(1)(iv), (viii), (ix) | Moderate | 2026-09-30 |
| 3 | App-based MFA on accounting and email; password manager | 52.204-21(b)(1)(vi); CSF PR.AA | High | 2026-09-30 |
| 4 | Approved external systems list; no customer content in the AI assistant; processors get PO and spec only | 52.204-21(b)(1)(iii), (c); 7021(f) | High | 2026-10-31 |
| 5 | New router: separate wired segment for laptop and VMC, guest Wi-Fi, share password, logs | 52.204-21(b)(1)(i), (x) | High | 2026-10-31 |
| 6 | Standard user account; named-person sharing with expiry; close 27 open links | 52.204-21(b)(1)(ii) | Moderate | 2026-10-31 |
| 7 | Wipe the old laptop and destroy old sticks, with a disposal record | 52.204-21(b)(1)(vii) | Moderate | 2026-10-31 |
| 8 | Monthly update check for CAM software and router firmware | 52.204-21(b)(1)(xii) | Moderate | 2026-10-31 |
| 9 | CAGE code and SPRS access; scope statement | 170.15(a)(1)(i); 170.19(b) | High | 2026-11-15 |
| 10 | Level 1 self-assessment (all MET), SPRS entry, affirmation | 170.15; 170.22; 7021(d) | High | 2026-11-30 |
| 11 | Separate backup with test restore; read-only released OEM programs | OEM SQA; CSF PR.DS, RC.RP | High | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **FAR rewrite.** The proposed Revolutionary FAR Overhaul (FR Doc. 2026-12559, June 23, 2026) would move information-security clauses into FAR part 40. It is **proposed, not final**. The shop should check the clause numbers on each new aerospace PO.
- **CMMC phases.** Phase 2 (planned for 2026-11-10, 32 CFR 170.3(e)(2)) is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 suspending CMMC Phase 2. This is in effect, not pending. Phase 2 would have added Level 2 (C3PAO) requirements for CUI. Level 1 does not change: during the suspension requiring activities may still require Level 1 (Self) or Level 2 (Self), and until 2028-11-09 DoD includes clause 252.204-7021 when a program office requires a specific CMMC level (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). The aerospace customer's Level 1 (Self) flowdown stands.
- **CIRCIA** (proposed 6 CFR part 226) is **not in effect**; no final rule had been published as of 2026-09-25. The proposed critical manufacturing criterion lists NAICS 331, 333, 335, and 336, not 332, and the shop is below its SBA size standard, so it would probably not be covered. Recheck when the final rule is published.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these proposals is treated as a current obligation.
