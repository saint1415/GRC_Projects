# Security Assessment Plan and Summary: Cris Santos Company | Dams | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project, Florida) |
| System assessed | Hydro Plant Control and Dam Monitoring System (HPCDMS), per the SSP (P02) |
| Tier / Vertical | Micro / Dams |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent OT security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03), did not design the control system, and operates no control. Accompanied by the Controls and Electrical Technician; the Plant Superintendent approved every test on site |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Also supports | The Security Assessment that FERC highly recommends for Group 3 dams (Rev. 3A 3.3.3) and the annual assessment in POL-02 A.6 |
| Accepted | 2026-08-31 by the Owner and General Manager |

## 1. Scope and controls selected
Micro tier scope: 10 to 15 controls. **13 controls, 100 determination statements.** Controls were chosen because they support the four High risks in P01 (remote access, the integrator link, office-to-OT spread, and OT recovery), carry the High gaps in P03, or test what the integrator and the MSP do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, IA-2(1) | Shared remote desktop password with full gate control, no MFA (P01 R-001; P03 G-041, G-013) | Focused | Comprehensive (both remote paths; all 64 sessions in the 30-day log) |
| MA-4 | Integrator's always-on cellular VPN (R-003; G-041) | Focused | Comprehensive (all 2026 work orders) |
| SC-7 | Office network can reach the HMI PC; router bypasses the firewall (R-004; G-039) | Focused | Focused (one connection test from an office laptop) |
| CP-9 | No company-held PLC, HMI, governor, or exciter copies (R-005; G-035) | Focused | Comprehensive (every OT controller and the HMI) |
| AC-2, IA-5 | Shared OT accounts and passwords; 2024 departure (R-002, R-010) | Focused | Comprehensive (all 7 staff and 2 integrator engineers; every device with a web login) |
| AU-6 | Nobody reviews remote sessions (R-001; G-037) | Focused | Comprehensive (64 sessions reconciled) |
| CM-8 | No OT inventory (G-026) | Basic | Comprehensive (walkthrough of every OT location) |
| SI-2 | Unsupported HMI operating system (R-006; G-033) | Basic | Focused (HMI PC, engineering laptop, gate PLC firmware) |
| IR-6 | Cyber events not known to be 18 CFR 12.10 conditions (R-007; G-047) | Basic | Focused (5 of 7 staff interviewed) |
| PE-3 | Physical protection of panels and the hoist house (R-022; G-025, G-043) | Basic | Comprehensive (all locked areas and keys) |
| SA-9 | No security terms with the integrator, MSP, or monitoring vendor (R-018, R-023; G-030) | Basic | Comprehensive (all 5 vendors with access or data) |

## 2. Methods and objects
- **Examine:** suite user export and sharing settings; remote desktop tool settings and its 30-day connection log (2026-07-12 to 2026-08-10); HMI user list and event journal; the integrator's 2015 network drawing, firewall rule description, and 2026 work orders; the integrator's file list of PLC and HMI copies; MSP contract, patch report, and backup job report; vendor contracts and subscription terms; 2024 and 2025 reports to the Regional Engineer; EAP and ODSP.
- **Interview:** Owner and General Manager, Plant Superintendent, Controls and Electrical Technician, Office and Compliance Administrator, 2 operator-mechanics, the MSP technician, and the integrator's lead engineer.
- **Test:**
  - reconcile every remote session in the 30-day log with the on-call rota and integrator work orders
  - from an office laptop, try to reach the HMI PC by remote desktop and file sharing
  - sign in to the remote desktop tool, the firewall administrator page, and the monitoring portal administrator account to see whether a second factor is asked for
  - try manufacturer default credentials on every device with a web login (camera NVR, cellular data gateway, firewall, switches)
  - walk every locked area with the Plant Superintendent and check keys and combinations

### Vendor evidence requested
The integrator and the MSP operate many of the technical controls, so evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| Firewall rule description and administrator login settings | Integrator | SC-7, IA-2(1) | Yes, 2026-08-07 |
| 2026 work orders for remote support | Integrator | MA-4, AU-6 | Yes, 2026-08-07 |
| List and dates of PLC, HMI, governor, and exciter copies | Integrator | CP-9 | Yes, 2026-08-10 (newest 2023-05-18; no governor or exciter settings) |
| 2023 firmware and software update work order with bench test notes | Integrator | SI-2 | Yes, 2026-08-10 |
| Patch report and backup job report (July 2026) | MSP | SI-2 (office side), CP-9 | Yes, 2026-08-07 |
| Account creation and removal procedure | MSP | AC-2, IA-5 | Yes, 2026-08-07 |
| Monitoring vendor SOC 2 Type 2 report | Monitoring vendor | SA-9 | Yes, 2026-08-06 (reviewed in P09 on 2026-08-20) |

## 3. Rules of engagement
- **No test may move a gate, start or stop a unit, or change a setpoint.** Tests on the HMI PC were read-only and ran during staffed hours with an operator-mechanic at the gate panels.
- No active scanning of PLCs, governors, exciters, or relays. Their status came from documents, the HMI, and the integrator. Default-credential checks were limited to web logins, one attempt each.
- No CEII left the site. Screenshots were kept in the restricted folder.
- The assessor would stop and tell the Plant Superintendent at once about any critical exposure. The default passwords and the written HMI password were reported the same day; the written password was removed on 2026-08-11.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 79 |
| **Total** | **100** |

| Control | Satisfied | Other than satisfied |
|---|---|---|
| AC-2 | 2 | 24 |
| AC-17 | 0 | 4 |
| IA-2(1) | 0 | 1 |
| SC-7 | 1 | 5 |
| MA-4 | 1 | 7 |
| CP-9 | 2 | 4 |
| CM-8 | 0 | 6 |
| SI-2 | 4 | 6 |
| IA-5 | 3 | 7 |
| AU-6 | 0 | 3 |
| IR-6 | 1 | 1 |
| PE-3 | 6 | 6 |
| SA-9 | 1 | 5 |

**Fully other than satisfied:** AC-17, IA-2(1), CM-8, and AU-6. Nothing governs remote access, nothing records what is in the control system, and nobody reads the logs.
**Strongest:** PE-3 (fence, locks, escorts, and public separation work; key control does not) and SI-2 (the integrator bench-tests updates; nobody tracks or applies them on OT).

**New findings from testing:**
1. The camera NVR administrator account and the cellular data gateway web page accepted manufacturer default passwords (IA-05e.). Added to the risk register as R-010 on 2026-08-12; POAM-009.
2. The HMI password was written on a card in a control desk drawer (IA-05g.). Removed the same day; POAM-009.
3. An office laptop reached the HMI PC by remote desktop and file sharing (SC-07a.[04]). POAM-004.
4. Of 64 remote sessions in 30 days, 3 matched neither the on-call rota nor a work order. On 2026-08-13 the integrator confirmed they came from an engineer's home computer during an unlogged support call (AC-17b., AU-06a.). No sign of misuse, but the company could not have known. POAM-002, POAM-010.
5. The former operator-mechanic never returned a hoist house key, and the lock was not changed (PE-03g.[02]). POAM-012.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`: 13 items, of which 4 are High (POAM-002, POAM-004, POAM-005, POAM-006), 8 Moderate, and 1 Low. As of 2026-08-31, 6 are in progress and 7 open. The High items are the same remote access and recovery theme as the P01 High risks.

## 5. Deliverables
`assessment-results.csv` (100 rows), `poam.csv` (13 items), and this plan and summary. The Owner and General Manager accepted the results and the POA&M on 2026-08-31. The POA&M also serves as the remediation plan for the voluntary Section 9 benchmark (P03) and will be shown to the FERC engineer at the next inspection.
