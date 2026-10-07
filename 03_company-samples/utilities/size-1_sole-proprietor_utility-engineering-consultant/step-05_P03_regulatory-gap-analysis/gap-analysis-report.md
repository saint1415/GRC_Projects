# Regulatory Gap Analysis: Cris Santos Company | Utilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Utilities |
| Regulation analyzed | NERC CIP Reliability Standards (N22-R01), **as they reach the business through client contracts**: Client A's Supplier Security Addendum (SSA-A, flowing down CIP-004-7 R6, CIP-011-3 R1, and CIP-013-2 R1 Part 1.2) and Client B's Vendor Access Agreement (VAA-B, flowing down CIP-003-9 Attachment 1 Sections 4, 5, and 6) |
| Also analyzed | FERC CEII non-disclosure agreement (18 CFR 388.113(h)(2)); Fla. Stat. 501.171 (narrow); Client C confidentiality clause |
| Versions checked | Standard texts read from nerc.com: CIP-003-9, CIP-004-7, CIP-011-3, CIP-013-2 (current enforceable versions per N22-R01, verified 2026-09-25). 18 CFR 388.113 and Fla. Stat. 501.171 read from the official sources |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-engineer, with the on-call IT technician (under NDA since 2026-07-17). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**NERC CIP does not apply to the business directly (G-006).** Section 215 of the Federal Power Act (16 U.S.C. 824o) makes the Reliability Standards binding on users, owners, and operators of the bulk-power system, and each CIP standard names who must comply in its Applicability section 4.1: Balancing Authority, a Distribution Provider that owns qualifying protection or restoration Facilities, Generator Operator, Generator Owner, Reliability Coordinator, Transmission Operator, and Transmission Owner. The business is not on the NERC Compliance Registry and performs none of these functions. It is a vendor to two Responsible Entities.

**It applies by contract, and the contracts are binding.** Each client has to show its own regulator that it controls vendor risk, so it writes the CIP requirements it owns into the vendor's contract:

| Client | Client's CIP position | Contract | Requirements passed down |
|---|---|---|---|
| Client A (generation and transmission cooperative) | Medium impact BES Cyber Systems at some 230 kV substations | SSA-A, signed 2025-01-15 | CIP-011-3 R1 Part 1.2 (protect and securely handle BCSI); CIP-004-7 R6 Parts 6.1 to 6.3 (authorize, verify, and revoke BCSI access); CIP-013-2 R1 Parts 1.2.1, 1.2.2, and 1.2.4 (vendor incident notice, coordination, and vulnerability disclosure) |
| Client B (municipal electric utility, registered Distribution Provider) | Low impact BES Cyber Systems (115 kV protection relays at two substations) | VAA-B, signed 2026-03-02 | CIP-003-9 R2 Attachment 1 Section 5.2 (Transient Cyber Assets managed by another party), Section 5.3 (Removable Media), Section 6 (vendor electronic remote access), and Section 4 (incident response) |

A breach of these terms is not a NERC violation by the consultant. It can, however, become a potential violation **for the client**: for example, Client A's CIP-004-7 R6 Part 6.1 requires it to authorize BCSI access before access is provisioned. That is why the drafter's access (G-010) was reported to Client A within 24 hours and the decision on its own compliance was left to Client A.

**Two other binding duties are added:**
- **FERC CEII NDA.** The owner obtained CEII from FERC for the Client D study under 18 CFR 388.113(g)(5). The non-disclosure agreement required by 388.113(h)(2) sets minimum terms: use only for the stated purpose, discuss only with authorized recipients, keep in a secure place, destroy or return on request, accept FERC audit, and promptly report unauthorized disclosures (G-025 to G-030). The requester verification is valid for the rest of calendar year 2026 (388.113(g)(5)(v)).
- **Fla. Stat. 501.171.** A sole proprietorship that maintains personal information is a "covered entity" (501.171(1)(b)). Here that means only the drafter's W-9 and the owner's own records (G-031 to G-033).

The Client C confidentiality clause is a contract, not a regulation, but it is included (G-034) because the AI upload broke it.

**Not applicable, with reasons (G-001 to G-005):** TSA Security Directive Pipeline-2021-02G (N22-R02; no pipelines), NRC 10 CFR 73.54 (N22-R03; no reactors), SDWA section 1433 (N22-R04; no water systems), NERC EOP-004-4 (registered entities only), and Form DOE-417 (electric utilities and other listed filers only). The clients file their own EOP-004 and DOE-417 reports; the consultant's job is to tell them quickly (G-013, G-024).

## 2. Method
1. **Requirements.** Each SSA-A and VAA-B term was split into checkable rows and traced to the CIP requirement part it flows down. CIP summaries are written in this repository's own words; the standards' text is not reproduced. The CEII rows follow the minimum NDA terms in 18 CFR 388.113(h)(2).
2. **Crosswalk.** CSF 2.0 and SP 800-53 Rev. 5 columns are an **author mapping**. NIST has published no official mapping for NERC CIP or for these contract terms.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: the file suite sharing report and activity log (2026-07-22), mailbox searches, device and account settings (2026-07-23), Client B checklists and session approvals, Client A notices, and the CEII archive.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 levels.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Regimes not applicable or not direct (G-001 to G-006) | 0 | 0 | 0 | 6 |
| Client A SSA-A (CIP-004-7, CIP-011-3, CIP-013-2 flow-down) | 4 | 6 | 3 | 0 |
| Client B VAA-B (CIP-003-9 flow-down) | 2 | 2 | 1 | 0 |
| FERC CEII NDA (18 CFR 388.113(h)(2)) | 3 | 3 | 0 | 0 |
| Fla. Stat. 501.171 | 0 | 3 | 0 | 0 |
| Client C contract | 0 | 0 | 1 | 0 |
| **Total (34)** | **9** | **14** | **5** | **6** |

Of the 19 unmet or partially met rows, gap risk is **3 High, 10 Moderate, and 6 Low**. The High gaps are BCSI copies in the mailbox (G-007), the gateway session path over a shared home network with push approvals (G-022), and the saved gateway password (G-023).

**What the client-run controls hide.** Client B's on-site checks are met (G-020, G-021), but they see only the moment of connection. They do not see that the same laptop reads email under an administrator account, or that the USB drives carry personal files. Those risks sit in P01 (R-002, R-007) even though no contract row fails.

## 4. Action list (half page)
In order. The first five cost nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Delete the saved gateway password; password manager; never approve a push the owner did not start | G-023, G-022 | High | 2026-09-15 |
| 2 | Authenticator app on the suite; MFA on the accounting SaaS; photo sync off and cloud copies deleted | G-018, G-031, G-009 | Moderate | 2026-09-15 |
| 3 | Delete Client A BCSI copies from email and the suite; owner-only client folders | G-007 | High | 2026-09-30 |
| 4 | Phone hotspot for gateway sessions until the business network is separate (2026-10-31) | G-022 | High | 2026-09-30 |
| 5 | Adopt the P08 runbook, notification matrix, and printed contact sheet (Client A, Client B, FERC) | G-013, G-024, G-030, G-033 | Moderate | 2026-09-30 |
| 6 | Signed drafter access agreement; quarterly share review | G-010 | Moderate | 2026-09-30 |
| 7 | Tell Client C; consent or rebuild the forecast; deletion request to the AI provider | G-034 | Moderate | 2026-09-30 |
| 8 | Client information register (BCSI and CEII); certify the two 2025 Client A projects | G-016, G-028, G-029 | Moderate | 2026-10-31 |
| 9 | Vendor advisory watch for the settings and analysis software | G-015 | Moderate | 2026-10-31 |
| 10 | Attach the sharing report to the next Client A access verification (due by 2027-02-12) | G-011 | Moderate | 2026-10-31 |

High and Moderate gaps are linked to the risk register (P01: R-001, R-003, R-004, R-005, R-008, R-009, R-012, R-013, R-014) and to the POA&M (P07).

## 5. Pending regulatory changes
None of these is a current obligation. Dates come from the NERC CIP standards page (N22-R01, verified 2026-09-25).
- **Virtualization revisions, effective 2028-07-01:** CIP-003-10, CIP-004-8, CIP-011-4.1, and CIP-013-3 replace the versions passed down today. Expect Client A and Client B to reissue SSA-A and VAA-B; recheck every row then.
- **CIP-003-11, effective 2029-07-01:** rewrites the low impact electronic access controls and moves the vendor remote access methods into Attachment 1 Section 3. Client B's gateway rules may tighten.
- **Supply chain:** FERC has directed further revisions to the supply chain standards (final action effective 2025-11-24). Client A's SSA-A items (5) and (6) may expand when NERC files them.
- **CIP-015-1 (2028-10-01) and CIP-015-2 (2029-10-01):** internal network security monitoring at the clients' high and medium impact systems. No direct effect on the consultant.
- **CIRCIA:** the final rule has not been published (not in effect). Recheck whether the business or its clients are covered when it is final.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
