# Security Assessment Plan and Summary: Cris Santos Company | Critical Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| System assessed | ERP and Production Scheduling Platform (EPSP), per the SSP (P02), with its IT/OT boundary and remote access paths into the plant |
| Tier / Vertical | Small / Critical Manufacturing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Contracted independent assessor with OT experience, not involved in designing or operating the controls. Escorted by the IT Manager (IT) and the Controls Engineer (plant) |
| Assessment window | 2026-08-10 to 2026-08-15 (campus walkthrough 2026-08-12; OT tests in the Saturday maintenance window on 2026-08-15) |
| Also supports | Answers to utility supplier security questionnaires (P09); CSF 2.0 ID.IM-01 improvement input |

## 1. Scope and controls selected
Small tier scope: 15 to 25 controls. **22 controls, 164 determination statements.** Every determination statement of each selected control was assessed. Controls were chosen because they:
- support the Very High and High risks in P01;
- address the High gaps in P03 on the EPSP, the IT/OT boundary, and remote access;
- underpin the utility addendum duties (incident notice, access notice) and the FAR 52.204-21 safeguards.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| SC-7, CM-7, CM-8 | Flat plant network, dual-homed MES, unknown components (P03 G-046, G-018); R-001 (Very High) | Focused | Focused (both firewalls, MES server, 5 kiosks) |
| AC-17, MA-4 | Always-on OEM routers (G-034, G-051); R-003 (High) | Focused | Focused (all 3 routers) |
| AC-2, AC-6, IA-2(1), IA-5, PS-4 | Shared and default credentials, ERP super users, late disablement (G-033, G-035, G-009, G-084); R-007, R-016 | Focused | Focused |
| CP-4, CP-9 | Exposed, untested backups (G-041, G-060); R-002 (High), R-021 | Focused | Focused |
| IR-4, IR-6 | No IT/OT response or notice process (G-032, G-057, G-082); R-006 (High) | Focused | Basic |
| AU-6, SI-4 | No monitoring or log review (G-049, G-050); R-026 | Basic | Basic |
| RA-5, SI-2, SI-3 | Vulnerability, patching, and malware gaps on the EPSP (G-024, G-043, G-052); R-009, R-027 | Focused | Focused |
| AT-2 | Untrained production and field staff (G-037); R-004 | Basic | Focused (interviews on both shifts) |
| PE-3, SC-8 | Physical and transmission safeguards that FAR 52.204-21 relies on (G-071, G-072, G-040) | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider, ERP, and MES user exports; ERP role report; edge and IT/OT firewall rule exports; OEM router configurations; backup job reports and settings; MSP scan and patch reports; EDR console; training records; HR termination tickets; the IT call list; utility addenda; the draft SSP (0.1) and draft P08 runbook.
- **Interview:** VP Operations, IT Manager, Controls Engineer, Plant Manager, Production Planning Manager, Contracts and Compliance Manager, Field Service Manager, HR Manager, MSP lead technician, and 10 staff (6 production workers on both shifts, 2 field technicians, 2 office staff).
- **Test:**
  - administrator sign-in to the cloud console and identity provider with and without a hardware key;
  - a backup deletion attempt with an administrator role, in a test vault;
  - a TLS scan of the ERP, identity provider, EDI, and productivity suite endpoints;
  - a malware test file on 2 laptops;
  - reachability from an engineering workstation to HMI ports on the plant network;
  - a login check on each OEM router with the Controls Engineer;
  - a default-credential check on the web configuration pages of plant HMIs.

## 3. Rules of engagement
- **Safety first.** All plant tests ran on 2026-08-15 in the Saturday maintenance window, with the Plant Manager's written approval and the Controls Engineer present. The drying ovens were cold and the oil fill station was shut down during the HMI checks.
- **No active scanning of plant equipment.** Plant tests were limited to reachability checks from one workstation, configuration reviews, and manual credential checks on web pages the OEMs confirmed were safe to access. No setting was changed.
- No design data or FCI left the company. Screenshots were redacted.
- **Stop and notify.** The assessor was to stop and notify the Controls Engineer on finding any critical exposure. One was found (below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 58 |
| Other than satisfied | 106 |
| **Total** | **164** |

**Fully other than satisfied (6 controls):** AC-6, AC-17, AU-6, CP-4, IR-4, IR-6. No plan, process, or technology existed for these at the time of fieldwork.

**Largely other than satisfied:** SI-4 (11 of 12), MA-4 (7 of 8), AT-2 (9 of 10), SC-7 (5 of 6), SI-2 (7 of 10).

**Fully satisfied (3 controls):** IA-2(1) (hardware-key MFA for administrators), PE-3 (badge access and escorts in both server rooms), and SC-8 (TLS and IPsec on every external path).

**New finding (stop and notify):** the web configuration page of the vapor-phase drying oven HMI accepted the OEM default password (IA-05e.). Anyone on the plant network, and anyone who reached it from the office, could have changed drying recipes or alarms. The assessor stopped and told the Controls Engineer at once. The Controls Engineer blocked the HMI's web port at the IT/OT firewall on 2026-08-17 as an interim measure. The password change and web interface shutdown need an OEM visit, scheduled before 2026-09-30. The finding was added to the risk register as R-034 (High) and to the POA&M as POAM-004.

All 19 controls with weaknesses have POA&M items in `poam.csv`: 8 High (POAM-001 to POAM-008) and 11 Moderate (POAM-009 to POAM-019). Twelve are in progress and 7 are open.

## 5. Deliverables
`assessment-results.csv` (164 rows), `poam.csv` (19 items), and this plan and summary. The VP Operations accepted the results and the POA&M on 2026-09-04. The President approved the High items and their budget the same day.
