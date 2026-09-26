# Security Assessment Plan and Summary: Cris Santos Company | Chemical | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| System assessed | Process Control and Batch Management System (PCBMS), per the SSP (P02) |
| Tier / Vertical | Small / Chemical |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent OT security assessor. Not involved in designing or operating the controls. Escorted in OT areas by the Controls Engineer |
| Assessment window | 2026-08-10 to 2026-08-14. OT testing 2026-08-12, during a planned Blend Hall A maintenance day with the blend tanks empty and the ammonia process isolated |
| Also supports | CISA RBPS 8 measure "conduct recurring audits" (P03 G-013, voluntary benchmark); POL-01 4.9 |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 181 determination statements.** Controls were chosen because they address the four High risks in P01 (R-001, R-002, R-006, R-007), the High gaps in P03, or the OT gaps listed in `../scenario-facts.md` section 4.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, SC-7 | Remote access and network paths into OT; R-001, R-002; G-004, G-035 (High) | Focused | Focused |
| AC-2, IA-2, IA-5 | Shared and orphaned OT accounts; R-004, R-012, R-028; G-003, G-008, G-009 | Focused | Comprehensive (all DCS accounts and rack cards) |
| CM-2, CM-3, CM-5, CM-7, CM-8 | Change control, SIS protection, inventory; R-005, R-007; G-032, G-040 | Focused | Focused |
| CP-2, CP-4, CP-9 | OT recovery; R-006 (High); G-020, G-036 | Focused | Focused |
| SI-2, SI-3, SI-4, AU-6 | Patching, malware, monitoring; R-008, R-010; G-018, G-033 | Basic | Focused |
| MP-7 | Removable media on HMIs; R-009 | Basic | Focused |
| IR-4, IR-6 | OT incident handling and release notification path; R-027; G-016, G-055 | Focused | Basic |
| AT-3 | Role-based OT training; R-030; G-011 | Basic | Basic |
| SA-9 | Integrator and vendor oversight; R-013, R-029; G-038 | Basic | Focused |

## 2. Methods and objects
- **Examine:** DCS user list and security configuration, firewall rule export, historian network settings, EWS and HMI installed software lists, backup job logs, MOC procedure and log, patch records, the IT incident plan and emergency action plan, training records, vendor agreements, the ERP vendor SOC 2 report.
- **Interview:** Plant Manager, Controls Engineer, IT Manager, EHS Manager, Process Engineer, HR Manager, Controller, 3 Shift Supervisors, both I&E technicians, and the DCS integrator's lead engineer.
- **Test (2026-08-12 unless noted):**
  - login tests at 3 operator stations and the EWS
  - inspection of the SIS keyswitch position and SIS engineering access
  - reachability test from an office PC to the historian's control-side address
  - a 2-hour passive network capture on the supervisory network (no active scanning)
  - USB device history on 3 operator stations and the EWS
  - attempted restore of one recipe file to spare DCS hardware
  - default credential test on the loading rack PLC, with the rack idle
  - a call test from the control room with the business network switch unplugged
  - a harmless antivirus test file on an office PC and a historian client

## 3. Rules of engagement
- **No active scanning of the control or SIS networks.** Only passive capture, per SP 800-82 Rev. 3 guidance that active scans can disrupt OT devices.
- All OT tests ran on the planned maintenance day, with the blend tanks empty, the ammonia process isolated, and the Controls Engineer present. The Shift Supervisor could stop any test.
- No change was made to DCS or SIS configuration. The SIS was inspected, not written to.
- **Stop-and-notify rule:** any finding that could affect process safety is reported at once to the Plant Manager and the Controls Engineer. It was used once (see section 4).
- No recipes or configuration files left the site. Screenshots of passwords were redacted.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 36 |
| Other than satisfied | 145 |
| **Total** | **181** |

**Fully other than satisfied (10 controls):** AC-17, AU-6, CM-2, CM-5, CM-8, CP-4, IA-2, MP-7, SI-3, SI-4. No plan, process, or technology existed for these on the PCBMS.

**Partly satisfied:**
- SC-7: a firewall does control the external interface.
- CP-9: nightly configuration and recipe exports run.
- SI-2: vendor-qualified patches are tested before installation.
- IA-5: the identity provider manages VPN authenticators well.
- AC-2: 13 of 26 statements are satisfied, mostly for identity provider accounts.

**New finding (stop-and-notify used).** On 2026-08-12 the assessor found the SIS keyswitch in the remote program position, with SIS engineering software installed on the DCS engineering workstation (CM-05[03], CM-05[06]). Together these meant the SIS logic could have been changed from the DCS EWS, which the integrator's remote tool also reached.
- The Controls Engineer returned the keyswitch to run and locked it the same day.
- The Plant Manager added a keyswitch check to each shift's rounds on 2026-09-15.
- The finding became P01 R-007 (High), P03 G-040 and G-052, and POAM-003.

**Other results that changed the picture:**
- An office PC reached the historian's control-side address, bypassing the firewall (SC-07a.[04]).
- The passive capture found 11 devices not in the DCS project file (CM-08).
- The call test showed no dial tone in the control room with the business network down (IR-06b.). The RMP notification path depends on the office network.
- Two DCS accounts and one loading rack card belonging to departed staff were active. They were disabled on 2026-08-14.

**POA&M.** All 22 controls have weaknesses, so there are 22 POA&M items in `poam.csv`: 10 High and 12 Moderate. POA&M risk levels use the P01 scale, taking into account the related P01 risk and P03 gap. The High items are POAM-001 to POAM-009 and POAM-011.

## 5. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-10 | Kickoff; document collection; interviews (office) |
| 2026-08-11 | Interviews (plant); walkthrough of the control room, engineering office, and server room |
| 2026-08-12 | OT testing on the planned Blend Hall A maintenance day |
| 2026-08-13 | Vendor, training, and backup evidence review |
| 2026-08-14 | Exit briefing; departed staff accounts disabled |
| 2026-08-21 | Draft results |
| 2026-09-04 | Results and POA&M accepted by the VP Operations; High items acknowledged by the CEO |

Deliverables: `assessment-results.csv` (181 rows), `poam.csv` (22 items), and this plan and summary. Next assessment: August 2027 (POL-01 4.9), before the DCS upgrade at the 2027 turnaround.
