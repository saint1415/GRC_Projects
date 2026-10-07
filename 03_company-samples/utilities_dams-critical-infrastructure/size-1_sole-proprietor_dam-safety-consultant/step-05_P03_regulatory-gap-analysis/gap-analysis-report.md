# Regulatory Gap Analysis: Cris Santos Company | Dams | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Dams |
| Regulation analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (C-DAMS-R01), **as it reaches the business through Client A's Consultant Security and Confidentiality Agreement (CSCA-A (1) to (9))** |
| Also analyzed | CEII rules (18 CFR 388.113(g)(1), (g)(5), and (h)(2)); the 18 CFR Part 12 Subpart D independent consultant rules that govern the Client A report; Client B's agreement (GRS-B (1) to (3)); Fla. Stat. 501.171 (narrow) |
| Versions checked | Security Program Rev. 3A as published on ferc.gov; 18 CFR 12.3, 12.10, 12.31, 12.34, 12.36, and 388.113 read from the eCFR (version date 2026-09-23); NERC BES Definition Reference Document version 3 (2026-04-30) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-engineer, with the on-call IT technician (under NDA since 2026-07-14). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**The FERC Security Program does not apply to the business directly (G-001, G-002).** It is guidance that FERC's Division of Dam Safety and Inspections applies to its licensees and exemptees. Its duties (Security Group classification, Security Assessment, Security Plan, the Section 9 cyber measures, and the annual certification letter) all belong to the dam owner. The business holds no license. In the program's own words it is a "non-owner": Rev. 3A 7.3 says owners may let outside parties with a need to know review a Security Plan, but no outside agency or non-owner may request or keep hard copies of it.

**It applies by contract, and the contract is binding.** Client A's dam is high hazard and in Security Group 2, and its control system is remote-capable, so Client A must control third-party remote access, train every control system user, protect security-sensitive information, and report incidents (Rev. 3A 3.2, 4.2, 7.3, Table 9.3a, Form 3 Q12, Q17). It wrote those duties into CSCA-A:

| CSCA-A term | Program source | Rows |
|---|---|---|
| (1) Storage of security-sensitive material and CEII; (2) Security Plan and Form 3 only in the portal or on site | 3.2 (OPSEC); 3.4.3.4 and 8.0 (marking); 7.3 | G-006 to G-008 |
| (3) Gateway only, MFA, windows, view-only, business-only device; (4) session log | Table 9.3a (remote and third-party connections; segregation); Form 3 Q12a-12c | G-009 to G-011 |
| (5) Training; (6) no removable media | Table 9.3a (training); Form 3 Q17 | G-012, G-013 |
| (7) 24-hour incident notice | 4.2; supports Client A's 18 CFR 12.10 report | G-014 |
| (8) Return or destroy; (9) no other person without approval | 7.3; Table 9.3a (roles with third-party contractors); Form 1 Q22 | G-015, G-016 |

A breach of these terms is not a FERC violation by the consultant. It can, however, leave **Client A** unable to show FERC that its third-party access and its security-sensitive information are under control at its next inspection.

**Three other sets of binding duties are added:**
- **CEII.** The owner holds Client A's CEII as Client A's non-employee agent, which 388.113(g)(1) allows with the owner/operator's written authorization (G-017). The owner also holds an upstream project's CEII under a non-disclosure agreement (388.113(g)(5)); 388.113(h)(2) sets its minimum terms: purpose only, authorized recipients only, a secure place, destroy or return on request, FERC audit, protection after a designation lapses, and prompt reporting of unauthorized disclosures (G-018 to G-025).
- **Part 12 Subpart D.** The owner is Client A's approved independent consultant. 12.31(a) and 12.34 make that approval personal, and 12.36(g) and (h) require a statement of independence and a signed and sealed report. Two of those rules have security consequences: the signing certificate must be protected, and AI tools must not produce the conclusions (G-026 to G-030).
- **Client B's agreement** (G-031 to G-033) and **Fla. Stat. 501.171**, which reaches only the field assistant's W-9 (G-034 to G-036).

**Not applicable, with reasons (G-001 to G-005):** the Security Program's licensee duties and Section 9 measures (no license; no control system), 18 CFR 12.10 (binds applicants and licensees; the consultant's part is the 24-hour client notice), NERC CIP (not registered; Client A's two units of about 14 MVA at 69 kV and Client B's project fall outside BES Inclusion I2, which needs 100 kV or above and more than 20 MVA per unit or 75 MVA per plant), and CIRCIA (proposed only).

**Which revision.** Revision 3A is the latest version that could be confirmed on ferc.gov. **Action:** ask Client A's Compliance and Security Coordinator to confirm the current revision before the 2026-11-16 field inspection.

## 2. Method
1. **Requirements.** Each CSCA-A and GRS-B term was split into checkable rows and traced to the Security Program section or Form question it passes down. The CEII rows follow 388.113(h)(2) term by term. FERC documents and the CFR are U.S. government works; short phrases are quoted where the wording matters.
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 columns are an **author mapping**. NIST has published no mapping for the FERC program, the CEII rules, or these contracts.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: the suite sharing and activity report (2026-07-22), the laptop and phone settings (2026-07-23), the USB drive, the Client A enablement emails and session list, the CEII authorization, grant letter, and non-disclosure agreement, and the home office walkthrough (2026-07-21).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 levels.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Not applicable directly (G-001 to G-005) | 0 | 0 | 0 | 5 |
| Client A CSCA-A (Security Program flow-down) | 3 | 5 | 3 | 0 |
| CEII (18 CFR 388.113) | 4 | 3 | 2 | 0 |
| 18 CFR Part 12 Subpart D | 2 | 3 | 0 | 0 |
| Client B GRS-B | 0 | 1 | 2 | 0 |
| Fla. Stat. 501.171 | 1 | 2 | 0 | 0 |
| **Total (36)** | **10** | **14** | **7** | **5** |

Of the 21 unmet or partially met rows, gap risk is **3 High, 10 Moderate, and 8 Low**. The High gaps are the unencrypted USB copy of CEII (G-006 and G-021, one fix for two duties) and the gateway sessions from the mixed-use administrator laptop with a saved password (G-010).

**What Client A's controls hide.** Client A's side of the gateway is met (G-009): named account, MFA, windows, view-only. Client A's weekly review would still see a stolen session as the owner's own, because the owner keeps no session log to compare (G-011). That is why the P08 runbook starts from Client A's call.

## 4. Action list (half page)
In order. The first five cost little or nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Encrypted backup drive; wipe the old one; keep it in the locked cabinet | G-006, G-021 | High | 2026-09-30 |
| 2 | Standard daily account; password manager; phone hotspot for gateway sessions | G-010 | High | 2026-09-30 |
| 3 | MFA on the Client B platform and the accounting SaaS | G-032, G-034 | Moderate | 2026-09-15 |
| 4 | Portal-only rule for security-sensitive material; ask Client A for view-only; marking template | G-008, G-007 | Moderate | 2026-09-30 |
| 5 | Adopt the P08 runbook, notification matrix, and printed contact sheet (Client A, Client B, FERC CEII Coordinator) | G-014, G-025, G-033, G-036 | Moderate | 2026-09-30 |
| 6 | Pre-release CEII check on every Client B deliverable | G-020 | Moderate | 2026-09-30 |
| 7 | Keep the AI vendor's deletion confirmation; Client B consent before any reuse | G-031 | Moderate | 2026-09-30 |
| 8 | Gateway session log and weekly review answers | G-011 | Moderate | 2026-10-31 |
| 9 | Field assistant agreement, briefing, and Client A approval | G-016 | Moderate | 2026-10-31 |
| 10 | Client information and CEII register; certificate to the former client | G-015, G-022, G-023 | Low | 2026-10-31 |
| 11 | Hardware token for the signing certificate | G-030 | Moderate | 2026-12-31 |

High and Moderate gaps are linked to the risk register (P01: R-001, R-002, R-003, R-004, R-005, R-006, R-007, R-009, R-011, R-013) and to the POA&M (P07).

## 5. Pending regulatory changes
None of these is a current obligation.
- **FERC Security Program:** no newer revision confirmed (see section 1). If a new revision changes third-party access or information protection, expect Client A to reissue CSCA-A; recheck rows G-006 to G-016 then.
- **CIRCIA:** the final rule has not been published as of 2026-09-25. Recheck whether the business or its clients are covered when it is final.
- **CEII verification:** not a rule change, but the upstream project verification ends 2026-12-31 (388.113(g)(5)(v)); a new request is needed for any 2027 work.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
