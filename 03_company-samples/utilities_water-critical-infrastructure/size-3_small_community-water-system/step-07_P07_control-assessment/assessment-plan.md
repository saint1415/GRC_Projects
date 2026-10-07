# Security Assessment Plan and Summary: Cris Santos Company | Water and Wastewater Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system) |
| System assessed | Water Treatment SCADA System (WTSS), per the SSP (P02) |
| Tier / Vertical | Small / Water and Wastewater Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT considerations from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls, and independent of the SCADA integrator. Escorted by the IT Manager and, at plants, by the Chief Plant Operator on duty |
| Assessment window | 2026-08-03 to 2026-08-07 (site visits to WTP-1, WTP-2, and 6 remote sites on 2026-08-05) |
| Also supports | The automated-systems element of the SDWA section 1433 RRA (42 U.S.C. 300i-2(a)(1)(A)(ii)) and the ERP revision |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **20 controls, 175 determination statements.** Controls were chosen because they support the five High risks in P01, cover the High gaps in the P03 cyber element, or are the controls an attacker would defeat in the P08 scenario (remote access to an HMI).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, AC-17(1), MA-4, IA-2(1) | Remote and vendor access (P03 G-028, G-029); R-001, R-002 (High) | Focused | Comprehensive (every remote path) |
| AC-2, AC-6, IA-2, IA-5 | Shared and default credentials (G-027); R-007, R-027, R-031 | Focused | Focused |
| SC-7, CM-7 | Segmentation (G-037); R-003 (High) | Focused | Focused |
| CP-2, CP-9 | ERP and OT backups (G-012 to G-014, G-033); R-006 (High) | Focused | Focused |
| IR-4, IR-8 | No OT incident capability (G-041, G-043) | Basic | Basic |
| CM-8, RA-5 | Inventory and vulnerability identification (G-023, G-025) | Focused | Comprehensive (all sites) |
| SI-2, SI-4, AU-6 | Patching, monitoring, log review (G-035, G-036, G-039, G-040); R-005, R-009 | Basic | Focused |
| AT-3 | OT role-based training (G-031) | Basic | Focused |

## 2. Methods and objects
- **Examine:** HMI, engineering workstation, and VPN user lists; firewall rule export; remote desktop agent settings and connection history; backup console; 2021 ERP and 2026 RRA review memo; training records; patch and version records; the 2017 as-built list.
- **Interview:** General Manager, Operations Manager, IT Manager, both Chief Plant Operators, both SCADA and Instrumentation Technicians, the Safety and Compliance Coordinator, the integrator's lead engineer, and 6 operators (incident reporting awareness and remote access habits).
- **Test:**
  - sign-in tests on the VPN and engineering workstation (to confirm password-only access)
  - HMI login test at WTP-1 and WTP-2 (shared account)
  - an external exposure scan of company and carrier-facing addresses (2026-08-04)
  - physical check of devices against the 2017 as-built list at all visited sites
  - a network trace of historian traffic across the IT/OT firewall
  - a check that historian data reaches the cloud replica (2026-08-06)

## 3. Rules of engagement
- **No active scanning or testing inside the OT network.** OT devices can fail when scanned. Inside OT, the assessor used only passive methods: configuration review, network traces from a mirror port, and physical inspection. SP 800-82 Rev. 3 advises this caution for OT.
- No change to any setpoint, PLC, or HMI configuration. A licensed operator was present for every action in a control room.
- The external scan targeted only company-owned addresses and the carrier-facing modem addresses, with the carrier's written permission.
- The assessor stopped and notified the IT Manager and Operations Manager on finding any critical exposure. **One was found** (see section 4). It was fixed during fieldwork.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 31 |
| Other than satisfied | 144 |

**Fully other than satisfied (12 controls):** AC-6, AC-17, AC-17(1), IA-2, IA-2(1), AT-3, AU-6, IR-4, IR-8, MA-4, RA-5, SI-4. No documented process or technology existed for these at the time of fieldwork. The P08 runbook and the P06 policies were approved on 2026-08-31, after fieldwork, so they could not be credited.
**Largely satisfied:** CP-2 (12 of 24): the ERP's emergency roles, contacts, approvals, and drill lessons are sound; the missing parts are all cyber. AC-2 (9 of 26): account requests and approvals work; removal and review do not.

**New finding (critical exposure):** the external scan on 2026-08-04 found web administration on 4 cellular modems at well sites reachable from the internet with default credentials (IA-05e.; SC-07b.). An attacker could have reached the well RTUs behind them. The SCADA and Instrumentation Technicians disabled the web administration and changed the passwords on 2026-08-06. This was added to the risk register as R-031 and to POAM-005, and it is why the carrier's private network plan with no public addressing is now required.

All 20 controls have weaknesses and POA&M items in `poam.csv` (20 items: 9 High, 11 Moderate). The High items are POAM-002 to POAM-006, POAM-008 to POAM-010, and POAM-020.

## 5. Deliverables
`assessment-results.csv` (175 rows), `poam.csv` (20 items), this plan and summary. The results were accepted by the General Manager on 2026-08-31.
