# Security Assessment Plan and Summary: Cris Santos Company | Energy | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) |
| System assessed | Pipeline SCADA and Gas Control System (PSGCS), per the SSP (P02) |
| Tier / Vertical | Small / Energy |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in designing or operating the controls. Escorted by the SCADA Engineer in OT areas |
| Assessment window | 2026-08-24 to 2026-08-28 (Compressor Station 1 and two valve sites visited 2026-08-26) |
| Also supports | The first-year assessment that SD 02G Section III.G would require on TSA designation (readiness only) |

## 1. Scope and controls selected
Small tier scope: 15 to 25 controls. **21 controls, 195 determination statements.** Controls were chosen for three reasons:
- They address the five High risks in P01.
- They address the High CSF benchmark gaps in P03.
- They support the SCADA-relevant 192.631 duties with gaps (change management and point verification).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, IA-2(1), IA-5 | Shared OT accounts; no MFA for OT administrators (P03 G-048, G-049); R-006 | Focused | Focused (all 9 SCADA accounts, OT domain) |
| AC-17, MA-4, SC-7 | Integrator remote access and the DMZ (R-002, R-003, High) | Focused | Focused |
| CP-2, CP-4, CP-9 | SCADA recovery (R-004, High); 192.631(c)(3)-(4) tests | Focused | Focused |
| IR-4, IR-8 | No cyber incident capability (R-001, R-012, High) | Focused | Basic |
| SI-4, AU-6 | No OT monitoring (R-005; P03 G-061) | Basic | Basic |
| CM-3, CM-8 | SCADA change control and inventory (192.631(c)(2), (f); R-009, R-028) | Focused | Focused (2 sampled display changes, 3 field sites) |
| SI-2, RA-5 | OT patching and vulnerabilities (R-007) | Basic | Basic |
| RA-3 | Risk assessment | Basic | Basic |
| SA-9 | Supplier security (R-016; P03 G-038) | Focused | Focused (4 contracts) |
| AT-3 | Role-based training (192.631(h); R-011) | Basic | Focused (6 controllers, SCADA Engineer) |

## 2. Methods and objects
- **Examine:** OT domain and SCADA user exports, firewall rule export, jump host and remote access configuration, backup job logs, the CRM manual, the emergency and manual operation plans, test reports, MOC forms and SCADA change history, contracts, training records, and the P01 risk register.
- **Interview:** President, VP Operations, Gas Control Manager, 3 controllers (one per shift pattern), SCADA Engineer, IT Manager, MSP lead, and HR Manager.
- **Test (read-only or vendor-approved, never on a live control path):**
  - an inbound connection attempt from the business network to the SCADA network (blocked);
  - a check of the remote access path at 02:00 on 2026-08-25;
  - HMI sign-in tests on 3 consoles;
  - a login test with manufacturer default credentials on cellular gateways at 2 valve sites and Compressor Station 1, done with the vendor's approval and with the controller informed;
  - a restore of one SCADA configuration file to the spare engineering laptop;
  - a comparison of the field inventory against the SCADA point list at the 3 sites visited.

## 3. Rules of engagement
- **No active scanning of OT.** SP 800-82 Rev. 3 warns that active scanning can disrupt control systems. OT vulnerability information was gathered from build sheets, vendor advisories, and configuration exports.
- Every test near OT was approved in advance by the Gas Control Manager and announced to the controller on duty. The controller could stop any test.
- No field device setting was changed. The default-password test stopped at the login banner, and nothing was changed.
- The assessor would stop and notify the Gas Control Manager on finding any exposure that could affect pipeline control. One finding met this bar: the default gateway passwords (see section 4). It was reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 56 |
| Other than satisfied | 139 |

**Fully other than satisfied:** AC-17, AU-6, IA-2(1), IR-8, and SI-4. No plan, process, or technology existed for these at fieldwork.
**Largely satisfied:** CP-2 (the emergency and manual operation plans are solid for non-cyber events), CP-4 (192.631 tests), RA-3 (now that the 2026 assessment exists), SC-7 (deny-by-default DMZ), and IA-2 (individual SCADA application accounts).

**New finding:** 3 cellular gateways at remote valve sites accepted the manufacturer default password (IA-05e.). This was not known before testing. The gateways sit on the carrier private network, but anyone with access to that network could have reached their management page. The finding was added to the risk register as R-008 and to POAM-012. The passwords are scheduled to be changed by 2026-09-30.

**Other test observations:**
- The integrator VPN was connected at 02:00 with no open ticket (AC-17b., MA-04e.).
- One departed contractor was still enabled in the OT domain (AC-02h.02). It was disabled during the assessment week and is tracked in POAM-001.

All 21 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-003, POAM-005, POAM-006, POAM-007, and POAM-014.

## 5. Deliverables
- `assessment-results.csv` (195 rows)
- `poam.csv` (21 items: 6 High, 14 Moderate, 1 Low)
- this plan and summary

The results were accepted by the President on 2026-09-24.
