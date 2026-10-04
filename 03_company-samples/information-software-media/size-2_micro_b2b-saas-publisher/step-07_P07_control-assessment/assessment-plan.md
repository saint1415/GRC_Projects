# Security Assessment Plan and Summary: Cris Santos Company | Information | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| System assessed | Vendor Compliance Platform (VCP), per the SSP (P02), including the contract developer's personal laptop as an out-of-boundary device holding company data |
| Tier / Vertical | Micro / Information |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk analysis (P01) or the gap analysis (P03), operates no control, and will not be the SOC 2 auditor. Accompanied by the CTO; MSP lead technician on call |
| Assessment window | 2026-08-24 to 2026-08-26 (plan agreed 2026-08-14) |
| Also supports | SOC 2 Type 1 readiness (P09); the FTC "Start with Security" practices tested in P03 |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 85 determination statements.** Controls were chosen because they support the Very High and High risks in P01 (the static CI key, five full administrators, false statements), cover the High gaps in P03, test the P08 incident scenario, or test what the MSP, the sub-processors, and the contractor do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Ad hoc offboarding; accounts outside single sign-on (P01 R-010; P03 G-016) | Focused | Comprehensive (every account in the cloud account, repository, admin console, support desk, and suite) |
| AC-6 | Five full administrators and the CI key (R-002; G-005) | Focused | Comprehensive |
| IA-2(1) | MFA on privileged access; security exhibit promise (R-025; G-009) | Focused | Comprehensive for privileged accounts |
| IA-5 | Static CI key and unrotated secrets (R-001, R-024; G-007) | Focused | Comprehensive for machine credentials |
| AU-2, AU-6 | No data-level logging or review (R-001; G-014; P08 scenario) | Focused | Focused (cloud account, document bucket, database) |
| CP-9, CP-4 | Backups and recovery; security exhibit backup promise (R-007, R-008; G-039) | Focused | Focused |
| IR-6 | 72-hour DPA notice and Florida 10-day notice (R-009; G-031, G-035) | Basic | Focused (5 of 7 staff and the contractor interviewed) |
| SA-9 | Sub-processor and MSP oversight; model provider not listed (R-016; G-021, G-022, G-036) | Focused | Comprehensive (5 sub-processors and the MSP) |
| SA-3(2) | Production extracts on laptops (R-003; G-003) | Basic | Comprehensive (all 4 developers' laptops) |
| SC-28 | Public tax ID and encryption claims (R-005; G-032, G-033) | Basic | Comprehensive (all data stores) |
| RA-5 | Unmanaged dependency alerts; no scanning (R-013; G-020, G-023) | Basic | Focused |
| PS-7 | Contractor and MSP security terms (R-003, R-012; G-015) | Basic | Comprehensive (contractor and MSP) |

## 2. Methods and objects
- **Examine:** cloud permission, logging, encryption, and backup settings; access key report and CI secret list; container definitions; user lists for every system; staff and contractor roster; offboarding emails; DPA and sub-processor list; vendor contracts and the model provider's API terms; MSP contract; contractor agreement; dependency alert list; P01 risk register.
- **Interview:** Chief Executive Officer, CTO, Senior Software Engineer, Software Engineer, Customer Success Manager, Operations and Finance Manager, the contract developer, and the MSP lead technician.
- **Test:**
  - every account list compared against the roster
  - an administrator-only action attempted with the contractor's cloud account (it succeeded)
  - sign-in to the internal admin console without a second factor (it succeeded)
  - deletion and attempted restore of a test file in a copy of the bucket configuration (it could not be restored)
  - a customer user's view of W-9 fields in a test tenant (full Social Security numbers shown)
  - a file listing of the contractor's personal laptop, with consent, looking for company data and keys

### MSP and contractor evidence requested
The MSP operates the laptop controls and the suite, and the contractor holds company data on a personal device, so evidence came from both. Requested on 2026-08-14 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| Suite MFA report, including the MSP's 2 administrator accounts | MSP | IA-2(1), AC-2 | Yes, 2026-08-19 |
| Laptop encryption, antivirus, and patch reports | MSP | SC-28, SI-3, SI-2 | Yes, 2026-08-19 |
| List of MSP technicians with administrator access and how changes are notified | MSP | PS-7, AC-2 | Partly: list received 2026-08-21; no notice process exists |
| Suite sign-in log for the former Customer Success Manager | MSP | AC-2 | Yes, 2026-08-21 (no sign-ins after departure) |
| Device details for the personal laptop (encryption, antivirus, operating system version) | Contractor | SA-3(2), PS-7 | Not available: the contractor could not show encryption status; follow-up in POAM-014 |

## 3. Rules of engagement
- No testing that could affect customers. Tests ran against a test tenant and a copy of the bucket configuration; the administrator test performed a harmless, reversible tagging change.
- No customer data left the company's systems. Screenshots were redacted before they went into the evidence folder. The contractor's laptop was examined on a video call; no files were copied.
- The assessor would tell the CTO at once about any critical exposure. The extracts on the contractor's laptop and the admin console finding were reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 72 |
| **Total** | **85** |

**Fully other than satisfied (9 of 14 controls):** AC-6, IA-2(1), AU-2, AU-6, CP-4, IR-6, SA-3(2), SC-28, PS-7. No process or technology met the objective.
**Partly satisfied:** RA-5 (4 of 9: the repository host's alerts work, but nobody acts on them), IA-5 (3 of 10: account issuance works, machine credentials do not), AC-2 (3 of 26: managers and the roster exist, the process does not), CP-9 (2 of 6), and SA-9 (1 of 6).

This is the expected result for a 7-person company assessed for the first time: good cloud and SaaS defaults, and almost no written process or evidence around them.

**New findings from testing:**
1. The contractor's personal laptop held the CI key and 3 production extracts with vendor tax IDs, the newest from 2026-07-14 (SA-03(02)a.[03], IA-05g.). The extracts were deleted on 2026-08-28, confirmed in writing. The key is retired under POAM-004.
2. The internal admin console accepted a password alone (IA-02(01)). POAM-003.
3. The root account password is in a vault entry shared with all engineers and the contractor, and has not changed since 2024 (AC-02k.[02], IA-05i.). Added to the risk register as R-025.
4. The former Customer Success Manager's admin console and support desk accounts were still active 5 months after departure, and the Account Executive kept admin console access after moving to sales in 2025 (AC-02f.[03], AC-02f.[04]). Both removed 2026-08-26. The support desk's sign-in history showed no use after the former employee left, but the admin console records no sign-ins, so use there cannot be ruled out (an AU-2 finding).

All 14 controls have at least one weakness and a POA&M item in `poam.csv`. The 7 High items are POAM-002, POAM-003, POAM-004, POAM-005, POAM-007, POAM-011, and POAM-014: credentials, administrator rights, logging, backups, and the contractor. They are the same theme as P01: one key and one unmanaged laptop reach everything.

## 5. Deliverables
`assessment-results.csv` (85 rows), `poam.csv` (14 items), and this plan and summary. The Chief Executive Officer accepted the results on 2026-09-15.
