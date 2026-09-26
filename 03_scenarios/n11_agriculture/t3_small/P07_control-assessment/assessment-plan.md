# Security Assessment Plan and Summary: Cris Santos Company | Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm) |
| System assessed | Farm Management and Irrigation Control Platform (FMICP), per the SSP (P02) |
| Tier / Vertical | Small / Agriculture, Forestry, Fishing and Hunting |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted by the Operations and Technology Manager; OT tests run with the Irrigation Technician present |
| Assessment window | 2026-08-03 to 2026-08-07 (pump house and North Block testing on 2026-08-05) |
| Benchmark | CSF 2.0 (P03). Results also feed the Produce Safety and H-2A record findings in P03 |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **21 controls, 179 determination statements.** Controls were chosen because they support the four High risks in P01, cover the High gaps in P03, or protect the regulated records in SYS-01.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, IA-2(1), IA-5 | Shared and stale accounts (P03 G-053, G-057; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1)); R-010, R-012, R-014 | Focused | Focused (all 4 departures from the 2025-26 season; all OT devices with a web interface) |
| AC-17, MA-4 | Integrator always-on remote access; R-002 (High) | Focused | Focused |
| SC-7 | Flat network; R-022; R-001 (High) | Focused | Focused (tested from the office, the packing shed Wi-Fi, and the pump house) |
| CP-2, CP-4, CP-9 | No plan, no tests, exposed backups; R-003 and R-007 (High) | Focused | Focused |
| SI-2, SI-3, SI-4 | Patching, malware, and monitoring; R-001, R-013 | Focused | Focused (office endpoints and the HMI) |
| RA-3, RA-5 | Risk assessment and vulnerability management | Basic | Basic |
| AU-6 | No log review (P03 G-077) | Basic | Basic |
| AT-2, IR-4, IR-6 | Awareness and incident handling (P03 G-059, G-086) | Basic | Focused (8 staff interviewed, 4 in Spanish) |
| CM-8 | Inventory (P03 G-032) | Basic | Focused (walkthrough of the pump house and North Block) |
| SA-9 | Supplier oversight (P03 G-026) | Focused | Focused (integrator, dealer, AI vendor, FMIS vendor, MSP) |

## 2. Methods and objects
- **Examine:** identity provider and SYS-01 user exports, backup console and July job reports, remote tool connection history, firewall and switch configurations, the integrator, dealer, AI vendor, FMIS vendor, and MSP agreements, training records, the 2026 risk register (P01), and walkthrough notes.
- **Interview:** majority owner and General Manager, Farm Manager, Operations and Technology Manager, Irrigation Technician, Office and HR Manager, Food Safety and Packing Lead, the MSP technician, the integrator's field engineer, and 8 randomly selected staff (incident reporting and phishing awareness).
- **Test:**
  - reachability of the HMI and PLC programming port from the packing shed Wi-Fi and the office network
  - default-credential test on the LoRaWAN gateway, 5 pivot panel modems, and cooler sensor hub, using web sign-in pages only
  - sign-in tests on a harvest tablet and the HMI, and an administrator sign-in with MFA
  - antivirus test file on 2 laptops and review of where the alert went
  - external scan of the farm's public IP address

## 3. Rules of engagement (OT safety first)
- **No active scanning of the PLC, VFDs, or pivot controllers.** SP 800-82 Rev. 3 warns that active scans can disrupt OT. Reachability was shown with a single connection attempt to the PLC programming port, not a scan.
- OT tests ran on 2026-08-05 between 06:00 and 10:00, outside irrigation run times, with the Irrigation Technician present and pumps in local control.
- No settings were changed on any OT device. Default-password tests stopped at the sign-in success page.
- No personal data was copied off site. Screenshots of personnel and tally records were redacted.
- The assessor was to stop and notify the Operations and Technology Manager on finding any critical exposure. One was found (below) and reported the same morning.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 34 |
| Other than satisfied | 145 |

**Fully other than satisfied (12 controls):** AC-17, AT-2, AU-6, CP-2, CP-4, IA-2, IR-4, IR-6, MA-4, RA-5, SA-9, SI-4. No plan, process, or technology existed for these.
**Fully satisfied:** IA-2(1). Administrator accounts for the identity provider, SYS-01, and the cloud tenant all require MFA.
**Largely satisfied:** RA-3 (the 2026 risk assessment exists; review and update not yet practiced) and SI-3 (antivirus detects and quarantines, but nobody sees the alerts).

**What the tests showed:**
- From the packing shed Wi-Fi, a laptop reached the HMI and the PLC programming port (SC-07a.[04]). Anyone who learns the Wi-Fi key could reach irrigation control.
- The remote tool history shows 23 integrator sessions in 2026, none recorded or approved by the farm (MA-4).
- SYS-01 shows 14 irrigation schedule changes in July 2026 that nobody reviewed (AU-6).

**New finding (critical exposure, reported 2026-08-05):** the LoRaWAN gateway and 2 of the 5 pivot panel modems accept the manufacturer's default admin password (IA-05e.). This was not known before testing. It was added to the risk register as R-014 and to POAM-013. The passwords are scheduled to be changed by 2026-09-30.

All 20 controls with weaknesses have POA&M items in `poam.csv`. The six High items are POAM-002 to POAM-007.

## 5. Deliverables
`assessment-results.csv` (179 rows), `poam.csv` (20 items), and this plan and summary. The results were accepted by the majority owner and General Manager on 2026-08-31.
