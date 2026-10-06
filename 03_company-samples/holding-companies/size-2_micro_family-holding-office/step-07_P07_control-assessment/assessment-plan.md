# Security Assessment Plan and Summary: Cris Santos Company | Management of Companies and Enterprises | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (family holding company and single-family office) |
| System assessed | Family Office Shared Services Platform (FOSSP), per the SSP (P02) |
| Tier / Vertical | Micro / Management of Companies and Enterprises |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician present for technical tests |
| Assessment window | 2026-08-31 to 2026-09-02 (on site 2026-09-01) |
| Also supports | The Safeguards Rule duty to regularly test or monitor the effectiveness of key controls (16 CFR 314.4(d)(1)) and to adjust the program afterwards (314.4(g)) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 89 determination statements.** Controls were chosen because they support the four High risks in P01 (mailbox takeover, spoofed payment requests, family record theft, MSP admin compromise), cover Safeguards Rule elements with gaps in P03, or test what the MSP does on the office's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Departed subsidiary controller kept guest access for 6 months; shared MSP admin account (P01 R-005, R-008; P03 314.4(c)(1)(i)) | Focused | Comprehensive (all 7 staff, 9 guests, MSP accounts, bank entitlements) |
| AC-6 | Family site open to all staff (R-003, R-004; 314.4(c)(1)(ii)) | Focused | Focused (SYS-02 sites, SYS-03 roles) |
| IA-2(1) | MFA on administrator access, including SYS-11 and the MSP (R-001, R-005; 314.4(c)(5)) | Focused | Focused |
| AT-2(3) | Email payment fraud is the top risk (R-002; PR.AT-02) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (R-001; 314.4(c)(8)) | Basic | Basic |
| CP-9, CP-4 | No independent backup and no restore test (R-006, R-007) | Focused | Focused |
| IR-8, IR-6 | No plan; near miss never reported (R-016) | Basic | Focused (draft runbook; 5 staff) |
| SA-9 | No provider oversight (R-005, R-010, R-011; 314.4(f)) | Focused | Comprehensive (all providers that hold or reach family information) |
| RA-5 | No scanning; SYS-11 exposed (R-007) | Basic | Focused (external check of the office IP and SYS-11) |
| SI-12 | Records kept since 2009 (R-012; 314.4(c)(6)) | Basic | Focused (file date sampling; vault links) |

## 2. Methods and objects
- **Examine:** SYS-02 user, guest, site permission, admin role, and MFA reports; SYS-01, SYS-03, SYS-04, SYS-06, SYS-07 user lists; bank entitlement reports; the MSP contract and service description; SaaS terms and the two SOC 2 reports on file; the P01 risk register; the draft P08 runbook (version 0.9, 2026-08-28); SYS-11 snapshot policy and cloud firewall rules; the MSP evidence listed below.
- **Interview:** Family Office Director, Controller, Office Manager, Senior Accountant, Executive Assistant (5 of 7 staff for training and incident reporting), and the MSP lead technician.
- **Test:**
  - user and guest lists compared against the staff roster and the subsidiaries' current contacts
  - a sign-in attempt to SYS-11 as local administrator without a second factor (with the MSP present)
  - an external port check of the office IP address and SYS-11 (with MSP consent)
  - a test edit of a dummy payee under the Senior Accountant role in the bill pay platform, with the Controller present (deleted afterwards)
  - file date sampling in the Family site and the vault, and a review of active vault share links

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-24 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 (context for RA-5) | Yes, 2026-08-28 |
| Antivirus console export (all devices and SYS-11) | SI-3 | Yes, 2026-08-28 |
| Laptop encryption report | SC-28 | Yes, 2026-08-28 |
| SYS-11 snapshot policy and cloud firewall rule export | CP-9, SC-7 | Yes, 2026-08-31 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Vulnerability scan reports | RA-5 | None exist (confirmed by the MSP) |
| Technician list, use of the shared admin account, MFA on the remote management platform | AC-2, SA-9 | Not received by fieldwork end; follow-up in POAM-010 |
| Subcontractor list | SA-9 | Not received by fieldwork end; follow-up in POAM-010 |

## 3. Rules of engagement
- No testing that could move money or disturb a payment run. The bill pay test used a dummy payee with no payment, and bank portals were examined through entitlement reports only.
- No family personal information left the office. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Family Office Director at once about any critical exposure. The bill pay approval gap was reported the same day and fixed on 2026-09-04.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 68 |
| **Total** | **89** |

**Fully other than satisfied:** AC-6, IA-2(1), AT-2(3), AU-6, CP-4, IR-6, RA-5. No process or technology met the objective.
**Partly satisfied:** IR-8 (the draft runbook meets 9 of 17 objectives on content; it is not yet approved, distributed, protected, or measured), PS-4 (exit steps work; deadlines and token return do not), and CP-9 (SYS-11 system-level backups exist; user-level backups and protection from deletion do not).

**New findings from testing:**
1. The bill pay platform let the Senior Accountant role edit a payee's bank details and release payment with no second approval (AC-06). Added to the risk register as R-023 and to POAM-005. The Controller turned on dual approval on 2026-09-04.
2. SYS-11 accepted a local administrator password alone over remote desktop (IA-02(01)). POAM-002.
3. The vault held 37 share links to the CPA firm and counsel with no expiry, the oldest from 2023 (SI-12[04]). All were disabled on 2026-09-02. POAM-012.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-004, and POAM-005: sign-in strength, payment-fraud training, and need-to-know access, the same themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (89 rows), `poam.csv` (13 items), and this plan and summary. The Principal accepted the results on 2026-09-18.
