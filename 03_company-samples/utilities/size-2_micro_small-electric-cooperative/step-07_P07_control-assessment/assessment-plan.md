# Security Assessment Plan and Summary: Cris Santos Company | Utilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative) |
| System assessed | Distribution SCADA and Outage Management System (DSOMS), per the SSP (P02) |
| Tier / Vertical | Micro / Utilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent consultant with OT experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Line Superintendent in the field and the Office and Finance Manager in the office; MSP lead technician and the SCADA vendor's support lead on call |
| Assessment window | 2026-08-10 to 2026-08-12 (substation and field testing 2026-08-11) |
| Also serves as | Evidence for the borrower's periodic analysis of security practices (7 CFR 1730.22(a)) and the inspection of cyber components (1730.21) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 118 determination statements.** Controls were chosen because they support the three High risks in P01 (SCADA takeover, exposed field modems, payment fraud), test RUS gaps in P03, or test what vendors and the MSP do for the cooperative.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared SCADA login; former employee (P01 R-001, R-010; P03 G-002) | Focused | Comprehensive (SCADA, AMI, outage module, vault; all 7 staff and vendor accounts) |
| AC-6 | AMI mass disconnect rights (R-003) | Focused | Comprehensive (all 4 AMI command users) |
| AC-17 | Vendor standing access; HMI open to the internet (R-008) | Focused | Focused |
| IA-2(1) | No MFA on SCADA, AMI, vault (R-001) | Focused | Comprehensive (every administrator login) |
| IA-5 | Default device passwords; shared password (R-002, R-010) | Focused | Focused (Substation 1 controls, line reclosers LR-2 and LR-4, all 6 modem addresses) |
| CM-8 | No OT inventory (P03 G-002, G-023) | Basic | Basic |
| SC-7 | Private network versus public-IP modems (R-002) | Focused | Comprehensive (all 6 modem addresses) |
| SI-2 | Unmanaged operations endpoints; no firmware updates (R-016) | Focused | Focused (3 endpoints, 2 recloser controls) |
| CP-9 | Settings backups by hand; vault not immutable (R-007) | Focused | Focused |
| CP-2 | ERP without a Business Continuity Section (P03 G-030; R-012) | Focused | Comprehensive (whole ERP) |
| IR-6 | No reporting rule; DOE-417 unknown (R-014, R-015) | Basic | Comprehensive (all 7 staff interviewed) |
| AT-2 | No training; 2025 bank-change email (R-004) | Basic | Comprehensive (all 7 staff) |
| PE-3 | Substation keys (R-020) | Basic | Focused (Substation 1 and 2 line recloser sites) |

## 2. Methods and objects
- **Examine:** SCADA, AMI, outage module, and vault user and role lists; tenant security settings; the SCADA vendor support access list and SOC 2 report; the 2021 ERP, its contact list, 2024 activation notes, and exercise sign-in sheets; the 2005 VRA; vendor contracts; training records; the personnel file for the May 2025 departure; the MSP evidence listed below.
- **Interview:** all 7 staff, the MSP lead technician, and the SCADA vendor's support lead.
- **Test:**
  - user lists compared with the staff roster in SCADA, AMI, the outage module, and the vault
  - sign-in attempts to SCADA, AMI, and vault administrator accounts with the account holder present, to see whether a second factor was asked for
  - password checks on recloser controls at Substation 1 and line recloser LR-2 (local port, Line Superintendent present)
  - an internet reachability check of the 6 line recloser modem addresses from an outside connection (connection only; no login beyond the management page prompt, which accepted the installer default password at LR-4)
  - patch status of the operations workstation, the Meter and Service Technician's laptop, and 1 truck tablet; firmware versions read from 2 recloser controls
  - vault object listing and storage settings (retention, versioning, login method)

### MSP and vendor evidence requested
The MSP operates the office computers and the vault, and the SCADA vendor operates the master station, so evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| MSP monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-07 |
| MSP antivirus console export | SI-2 (context) | Yes, 2026-08-07 |
| Vault storage settings, object listing, and administrator login method | CP-9, IA-2(1) | Yes, 2026-08-10 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| MSP technician list and MFA on its remote management platform | AC-17 | Not received by fieldwork end; follow-up in R-009 |
| SCADA vendor support access list and sign-in history (90 days) | AC-2, AC-17 | Yes, 2026-08-06 |
| SCADA vendor SOC 2 Type 2 report | CP-9, AC-17 | Yes, 2026-08-06 (reviewed in full on 2026-08-20, P09) |
| AMI vendor SOC 2 report | AC-6 (context) | Requested 2026-08-14 after fieldwork; not received |

## 3. Rules of engagement
- **Safety and service first.** No test could operate a device or change a setting. Field tests at Substation 1 and the line recloser sites were done on 2026-08-11 in fair weather, with the Line Superintendent present and the G&T control center told in advance. The assessor read settings and firmware versions only; any change was made by the Line Superintendent.
- **No live SCADA commands.** SCADA tests were limited to sign-in prompts and settings screens.
- **Data.** No member personal information left the office. Screenshots were redacted before they went into the evidence folder.
- **Stop and tell.** The assessor would stop and tell the Line Superintendent at once about any critical exposure. The LR-4 modem finding was reported within the hour on 2026-08-11. The Line Superintendent changed all 6 modem passwords and the MSP had the carrier close the management ports on 2026-08-12.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 23 |
| Other than satisfied | 95 |
| **Total** | **118** |

**Fully other than satisfied:** AC-6, AC-17, IA-2(1), CM-8, IR-6, AT-2. No process or technology met any objective.
**Partly satisfied:** PE-3 (fence, gate, and escort work; keys do not), CP-2 (the ERP is a good storm plan with clear roles and restoration priorities, but it does not cover computer systems), CP-9 (office data is copied nightly; device settings are not), AC-2 (roles in AMI and the outage module fit the jobs; SCADA does not).

**New findings from testing:**
1. The management page of the LR-4 line recloser modem answered from the internet and accepted the installer's default password (IA-05e., SC-07a.[02]). Corrected 2026-08-12. P01 R-002 was rewritten on 2026-08-12; POAM-003 and POAM-006.
2. Recloser controls at Substation 1 and LR-2 still accept the vendor default password at the local port (IA-05e.). POAM-006.
3. The operations workstation was missing 4 months of operating system updates and signs in to SCADA automatically (SI-02a.[03]). POAM-008.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001, POAM-002, POAM-003, and POAM-006. All four concern who can operate field devices remotely, the same theme as the P01 High risks.

## 5. Deliverables
`assessment-results.csv` (118 rows), `poam.csv` (13 items), and this plan and summary. The General Manager accepted the results on 2026-08-31.
