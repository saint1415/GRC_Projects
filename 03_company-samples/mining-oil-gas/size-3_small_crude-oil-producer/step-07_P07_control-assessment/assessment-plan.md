# Security Assessment Plan and Summary: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer) |
| System assessed | Field SCADA and Production Accounting System (FSPA), per the SSP (P02) |
| Tier / Vertical | Small / Mining, Quarrying, and Oil and Gas Extraction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with the OT discussion in the SP 800-82 Rev. 3 overlay (Appendix F) used to judge OT-specific alternatives |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted in the OCC and at field sites by the SCADA and Automation Supervisor |
| Assessment window | 2026-08-03 to 2026-08-07 (field site testing 2026-08-05) |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary; P03). No binding federal sector rule requires this assessment |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **21 controls, 191 determination statements.** Controls were chosen because they address the three High risks in P01 (the IT-to-SCADA ransomware path, vendor remote access, and backups), the High and Moderate gaps in P03, or the recovery values in the BIA (P05).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, MA-4, IA-2(1) | Integrator remote access (R-002, High; P03 PR.AA-03, DE.CM-06) | Focused | Focused (every remote access path) |
| SC-7 | IT/OT segmentation and exposed modems (R-001, High; P03 PR.IR-01) | Focused | Comprehensive (all external and IT/OT interfaces) |
| CP-2, CP-4, CP-9 | Backups and recovery (R-003, High; P05 key findings) | Focused | Focused |
| AC-2, IA-2, IA-5 | Shared accounts, late removal, credentials (R-010, R-011) | Focused | Focused (sample of 8 terminations; 12 modems) |
| CM-3, CM-8 | Change control and OT inventory (R-006, R-012) | Focused | Basic (6 field sites spot-checked) |
| SI-2, SI-3, SI-4, RA-5, AU-6 | Patching, malware, monitoring (R-005, R-013, R-025) | Basic | Focused |
| IR-4 | Incident handling (R-026) | Focused | Basic |
| AT-2 | Training gap for field staff (P03 PR.AT-01) | Basic | Focused (8 field staff, 2 Production Controllers) |
| SA-9 | Supplier security (P03 GV.SC-05) | Basic | Focused (3 contracts) |
| PE-3 | OCC and field site physical access | Basic | Focused (OCC, 2 tank batteries, 3 well pads) |

## 2. Methods and objects
- **Examine:** IT/OT firewall and cloud network rule exports, identity provider and SCADA account lists, remote access tool configuration, backup logs and storage locations, controller program files on technician laptops, patch and scan reports, the emergency response plan, POL-01 to POL-05, the P08 runbook, contracts, training rosters, badge and key records.
- **Interview:** CFO, VP Operations, IT Manager, SCADA and Automation Supervisor, the integrator's lead engineer, HR Manager, 2 Production Controllers, 2 automation technicians, and 8 randomly selected field staff (incident reporting and phishing awareness).
- **Test:**
  - external scan of the company's internet addresses and the cellular modem address ranges
  - login test on 12 sampled cellular modems (with the carrier's approval), to check for default credentials
  - reachability test of the integrator's remote access tool
  - administrator sign-in with a hardware key; sign-in attempts to SCADA engineer accounts without MFA
  - malware test file on a corporate laptop and one HMI (alert routing)
  - comparison of 6 field sites against the integrator's drawings
  - review of HMI sign-in practice during a shift change at the OCC

## 3. Rules of engagement
- **No active scanning of the SCADA network or field controllers.** SP 800-82 Rev. 3 (Appendix E.2.3) advises extreme caution with active scanning on an operational OT network because it can cause device instability, so OT evidence came from configuration exports, observation, and passive review. The only tests touching field equipment were logins to modem management pages, not to the controllers behind them.
- Modem and HMI tests ran with a Production Controller watching the affected sites on SCADA, and the SCADA and Automation Supervisor could stop testing at any time.
- No production data or royalty owner data left the company. Screenshots were redacted.
- The assessor would stop and notify the IT Manager and VP Operations on finding any critical exposure. **This happened once** (see section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 60 |
| Other than satisfied | 131 |

**Fully other than satisfied:** AC-17, AU-6, CM-3, CP-4, IA-2, IA-2(1). No plan, process, or technology existed for these.
**Largely satisfied:** PE-3 at the OCC (badges, visitor escort), CP-2 for the parts the existing emergency response plan covers (roles, contacts, manual operations), SI-3 detection and quarantine, and RA-5 for the corporate and cloud side.

**New finding (critical exposure, reported the same day):** 3 of 12 sampled well-pad cellular modems were on a public mobile network, with their web management page reachable from the internet and the manufacturer's default admin password (IA-05e.; SC-07a.[02]). This was not known before testing. The assessor stopped and notified the IT Manager and VP Operations at 14:10 on 2026-08-05. The SCADA and Automation Supervisor changed the three passwords that evening. The finding was added to the risk register as R-032 and to POAM-013, and moving the modems to the private network is due 2026-09-30.

All 21 controls have at least one weakness, so each has a POA&M item in `poam.csv`. The High items are POAM-001 to POAM-004, POAM-015, and POAM-016, all tied to the three High risks in P01.

## 5. Deliverables
`assessment-results.csv` (191 rows), `poam.csv` (21 items), and this plan and summary. The results were accepted by the CFO and the VP Operations on 2026-08-31.
