# Security Assessment Plan and Summary: Cris Santos Company | Public Administration | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| System assessed | Hosted Case Management Service (HCMS), per the SSP (P02), with the 2 laptops approved for SC-01 |
| Tier / Vertical | Micro / Public Administration |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Operations Manager; the Lead Platform Engineer ran the technical tests under observation; MSP lead technician on call |
| Assessment window | 2026-08-17 to 2026-08-19 (on site 2026-08-18) |
| Criteria | The SSP control statements (P02, draft of 2026-08-14), the draft policies POL-02 to POL-04 (version of 2026-08-14), the CJIS Security Policy v6.1 values for the AC-01 workspace, and the Pub. 1075 terms for SC-01 |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 85 determination statements.** Controls were chosen because they support the Very High and High risks in P01 (ransomware through an administrator laptop, CJI theft, restore failure, late agency notice, MSP compromise), carry a CJIS value the AC-01 contract enforces, or test what the MSP and the platform vendor do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6 | Support role reached every workspace; administrator accounts used daily (P01 R-001, R-003, R-022; P03 G-002, G-006) | Focused | Comprehensive (all staff accounts; 10-account agency sample) |
| IA-2(1), IA-5 | SSH key-only access to the server that holds CHRI files; credential handling (R-009; CJ-05) | Focused | Focused (SYS-02, 2 laptops, repository) |
| PS-3 | Unscreened staff with CJI access (R-003; CJ-03) | Focused | Comprehensive (all 5 staff with CJI roles; 2 SC-01 staff) |
| AT-2 | No training beyond agency courses; overdue FTI recertification (R-007; PB-02) | Basic | Focused (6 of 7 staff interviewed) |
| AU-11 | CJIS 1-year retention (R-008; CJ-08) | Basic | Basic |
| CP-9 | Exports next to the server; unproven recovery (R-001, R-004) | Focused | Focused |
| IR-6 | 1-hour CJI rule; FTI reporting (R-005; CJ-09; PB-08) | Basic | Focused (6 of 7 staff) |
| SC-7, SC-13, SC-28 | Server network rules; FIPS 140-3 cutoff on 2026-09-21; CJI at rest on laptops (R-002, R-010, R-020; CJ-10, CJ-11) | Focused | Focused (SYS-02; all 8 laptops for SC-28) |
| SI-2 | Server 3 months behind; MSP patching (R-009) | Focused | Focused (SYS-02; 3 laptops) |
| SA-9 | No vendor oversight: platform vendor, MSP, helpdesk, AI add-on (R-012, R-013, R-019) | Focused | Comprehensive (all 4 providers that touch agency data or administer systems) |

## 2. Methods and objects
- **Examine:** platform user, role, and tenant settings exports; SYS-02 security group, SSH, crypto policy, package, and log rotation outputs; bucket configuration; the contracts with the 4 agencies, the prime, the MSP, and the vendors; FedRAMP listings and the platform vendor's SOC 2 report and letters; AC-01 screening confirmations and training records; the revenue agency's training certificates and device approval; draft POL-02 to POL-04; the MSP evidence listed below.
- **Interview:** owner, Operations Manager, Lead Platform Engineer, both Platform Developers, the Implementation and Support Analyst, the Integration Consultant (training and incident reporting), the MSP lead technician, and the AC-03 IT manager (agency account changes).
- **Test (run by the Lead Platform Engineer with the assessor watching):**
  - staff and agency account lists compared with the staff list and a 10-account sample of agency requests
  - an SSH sign-in to SYS-02 to check for a second factor
  - a review of every SYS-02 security group rule
  - a search of the repository for stored passwords, keys, and tokens
  - the cipher and module report for one SFTP pull from the sheriff's drop
  - encryption status on all 8 laptops through the MSP console, and patch status on 3 laptops and SYS-02
  - a listing of the SYS-02 working folder and the export bucket

### MSP evidence requested
The MSP operates the laptop and suite controls, so evidence came from it. Requested on 2026-08-10 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and pilot-ring description | SI-2 | Yes, 2026-08-14 |
| Antivirus console export (all laptops) | SI-3 (context for R-001) | Yes, 2026-08-14 |
| Laptop encryption report, including key length | SC-28 | Yes, 2026-08-14 (key length added on request 2026-08-18) |
| Suite MFA report and backup job report (July 2026) | IA-2(1), CP-9 | Yes, 2026-08-14 |
| Technician list with access to company laptops, and MFA on the remote management console | AC-17, SA-9 | **Not received by fieldwork end**; follow-up in POAM-014 |
| Remote session log for July 2026 | MA-4, SA-9 | **Not received by fieldwork end**; follow-up in POAM-014 |

## 3. Rules of engagement
- No testing that could disrupt agency work. Tests ran on 2026-08-18 between 6 p.m. and 8 p.m., outside the agencies' business hours, and the nightly sheriff load was left untouched.
- No agency data left company systems. The assessor viewed records only on screen and kept redacted screenshots; no CJI or FTI went into the evidence folder or the report.
- The SC-01 laptops were checked through the MSP console only. The assessor did not connect to the revenue agency's virtual desktop.
- The assessor would stop and tell the Operations Manager at once about any critical exposure. The open SSH rule and the password in the repository were both reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 64 |
| **Total** | **85** |

**Fully other than satisfied (8 of 14):** AC-6, IA-2(1), PS-3, AT-2, AU-11, SC-13, SC-28, SA-9. No process or technology met the objective.
**Partly satisfied:** AC-2 (8 of 26: roles and authorizations are sound; procedures, reviews, and departures are not), SI-2 (4 of 10: the MSP's laptop patching works; the server does not), SC-7 (3 of 6), IA-5 (3 of 10), CP-9 (2 of 6), IR-6 (1 of 2).

**New findings from testing:**
1. A SYS-02 security group rule allowed SSH from any internet address. It was added in May 2026 for remote work and never removed (SC-07a.[02]). Removed on 2026-08-18; the 14 days of available logs showed no successful sign-in from an unknown address. Added to the risk register as R-024 (closed) and POAM-010.
2. The sheriff's file-drop password was stored in plain text in an interface script in the repository, visible to all 5 repository users (IA-05g.). Sheriff IT rotated it on 2026-08-20. Added as R-025 and POAM-004.
3. 3 of 8 laptops use 128-bit full-disk encryption, the operating system default when they were set up, where the CJIS Security Policy requires 256-bit keys for CJI at rest outside a physically secure location (SC-28). POAM-012; the gap analysis row CJ-11 was updated.

All 14 controls have at least one weakness and a POA&M item in `poam.csv`. The 9 High items share the P01 theme: one administrator laptop or one server reaches everything (POAM-001, POAM-002, POAM-007, POAM-008, POAM-013), and the agency terms the company already works under are not met (POAM-005, POAM-009, POAM-011, POAM-014).

## 5. Deliverables
`assessment-results.csv` (85 rows), `poam.csv` (14 items), and this plan and summary. The owner accepted the results on 2026-08-31. A copy of the summary and the POA&M goes to AC-01 and AC-02 by 2026-10-30 (SSP section 4.2).
