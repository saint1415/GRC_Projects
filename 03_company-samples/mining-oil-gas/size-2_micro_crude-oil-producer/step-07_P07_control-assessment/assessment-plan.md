# Security Assessment Plan and Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field) |
| System assessed | Field SCADA and Production Accounting System (FSPA), per the SSP (P02) |
| Tier / Vertical | Micro / Mining, Quarrying, and Oil and Gas Extraction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with the OT discussion in the SP 800-82 Rev. 3 overlay (Appendix F) used to judge OT-specific alternatives |
| Assessor and independence | Independent consultant with OT experience, under a fixed-fee engagement. Did not take part in the risk analysis (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager at the main office and the Field Superintendent at the field office; MSP lead technician and the integrator's technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (field office testing 2026-08-11) |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary; P03). No binding federal sector rule requires this assessment |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 110 determination statements.** Controls were chosen because they support the High risks in P01 (the ransomware path through the flat field office network, vendor remote access, and the SCADA backup), cover High and Moderate gaps in P03, or test what the MSP does on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, IA-2(1) | Integrator remote access and administrator logins without MFA (R-002; P03 PR.AA-03) | Focused | Comprehensive (every remote access path and administrator login) |
| SC-7 | Flat field office network (R-001; P03 PR.IR-01) | Focused | Comprehensive (both offices' internet connections) |
| CP-9, CP-4 | SCADA backup and restore (R-003; P05 key findings) | Focused | Focused |
| AC-2, PS-4 | Shared accounts and the March 2026 departure (R-007, R-008) | Focused | Comprehensive (all accounts in 5 systems) |
| SI-2, SI-3 | Unsupported SCADA host; MSP patching and antivirus (R-006, R-011, R-017) | Focused | Focused (3 computers including the SCADA host) |
| CM-8 | No OT inventory (R-010; P03 ID.AM-01) | Basic | Focused (3 well sites, tank battery, SWD facility) |
| AT-2 | No training (P03 PR.AT-01) | Basic | Comprehensive (all 7 staff interviewed) |
| IR-8 | No incident plan (R-019) | Basic | Basic |
| SA-9 | Vendor oversight; write-back enabled by the vendor (R-014, R-022) | Focused | Comprehensive (all 4 critical vendors) |

## 2. Methods and objects
- **Examine:** account lists from the suite, production accounting, the bank portal, the mobile viewer, and the SCADA host; the March 2026 termination record; the main-office firewall rule export and the field office router configuration; the SCADA host update history and antivirus log; the emergency response plan; contracts; the production accounting SOC 2 report and the SCADA vendor whitepaper; the MSP evidence listed below.
- **Interview:** Owner, Office Manager, Production Accountant, Field Superintendent, Field Technician, both Lease Operators, the MSP lead technician, and the integrator's technician.
- **Test:**
  - account lists compared with the staff and vendor list in 5 systems
  - external scan of both offices' internet addresses (2026-08-11), with a rescan after the fix (2026-08-12)
  - sign-in attempts without a second factor to the backup console, mobile viewer administrator, SCADA host administrator, and the integrator tool
  - patch status on 3 computers, including the SCADA host and the engineering laptop
  - an industry-standard harmless antivirus test file on 1 office laptop and the shared field desktop, and an after-hours test alert
  - comparison of 3 well sites, the tank battery, and the SWD facility with the integrator's 2019 drawings

### MSP evidence requested
The MSP operates most office controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-07 |
| Antivirus console export (all managed devices) | SI-3 | Yes, 2026-08-07 |
| Laptop encryption and MDM reports | SC-28, AC-19 (context) | Yes, 2026-08-07 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-10 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Main-office firewall rule export | SC-7 | Yes, 2026-08-07 |
| Technician list and evidence of MFA on the remote management platform | AC-17 (context), SA-9 | Not received by fieldwork end; follow-up in POAM-013 |

## 3. Rules of engagement
- **No active scanning of the field network or controllers.** SP 800-82 Rev. 3 (Appendix E.2.3) advises extreme caution with active scanning on an operational OT network because it can cause device instability. The external scan covered only the two offices' public internet addresses. OT evidence came from configuration review, observation, and the drawings.
- Tests on the SCADA host and field office ran with the Field Superintendent watching the HMI, and either the Field Superintendent or the Field Technician could stop testing at any time. No settings on the SCADA host were changed by the assessor.
- No owner or employee data left the company. Screenshots were redacted.
- The assessor would stop and tell the Owner and the Field Superintendent at once about any critical exposure. **This happened once** (section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 18 |
| Other than satisfied | 92 |
| **Total** | **110** |

**Fully other than satisfied:** AC-17, IA-2(1), CP-4, AT-2, IR-8. No process or technology met the objective.
**Largely satisfied:** SI-3 on the office computers (detection, quarantine, and scanning work; after-hours alerting and the SCADA host do not).

**New findings from testing:**
1. **Critical exposure, reported the same day.** The external scan found a remote desktop port on the field office router forwarded to the SCADA host and reachable from the internet (AC-17b.; SC-07a.[02]). The integrator had set it up in 2022 as a fallback and nobody at the company knew. The assessor stopped and called the Owner and the Field Superintendent at 15:10 on 2026-08-11. The Field Superintendent removed the rule at 15:40, and the rescan on 2026-08-12 confirmed it closed. The SCADA host event log had already overwritten older entries, so earlier sign-ins could not be ruled out; the host is being replaced (POAM-008). Added to the risk register as R-025 and to POAM-001.
2. An unused account for a radio contractor whose work ended in 2023 was still on the SCADA host (AC-02f.[05]). POAM-005.
3. The after-hours antivirus test alert sat in the MSP queue until the next business morning (SI-03c.02[02]). POAM-009.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001 to POAM-004: remote access, the field office boundary, and the SCADA backup and restore, the same themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (110 rows), `poam.csv` (13 items), and this plan and summary. The Owner accepted the results on 2026-08-31.
