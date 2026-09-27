# Security Assessment Plan and Summary: Cris Santos Company | Government Services and Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| System assessed | Facility Operations Technology Platform (FOTP), per the SSP (P02) |
| Tier / Vertical | Small / Government Services and Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor with OT experience. Not involved in operating or designing the controls. Escorted by the IT Manager at the ROC and by the Site Managers at customer sites |
| Assessment window | 2026-08-03 to 2026-08-07 (county site tests 2026-08-05 after hours; restore test 2026-08-06) |
| Also satisfies | The state contract exhibit's annual independent assessment (SP 800-53 CA-2) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 163 determination statements.** Controls were chosen because they support the Very High and High risks in P01, cover the High gaps in P03, or map to the FAR 52.204-21 and CUI terms of the federal contract.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17, IA-2, IA-2(1), IA-5 | Remote access and credentials on OT (R-001, R-002, R-003) | Focused | Focused (all 6 sites' remote paths) |
| AC-2, AC-6, PS-4 | Deprovisioning, shared accounts, PIV return (R-005, R-012; FAR 52.204-9) | Focused | Focused |
| SC-7, CM-6, CM-8 | OT segmentation, hardening, inventory (R-004, R-032) | Focused | Focused (county government center and 2 service centers) |
| SI-2, RA-5 | Firmware and vulnerability management (R-016) | Focused | Basic |
| CP-2, CP-4, CP-9 | Recovery of the supervisory platform and programs (R-006, R-007, R-008) | Focused | Focused |
| AU-6 | No monitoring (R-017) | Basic | Basic |
| IR-4, IR-6 | Customer notice deadlines (R-011) | Focused | Basic |
| SA-9, SR-3 | Subcontractors; Section 889 and FASCSA (R-009, R-019) | Focused | Focused |
| MP-4, AT-3 | CUI handling and role-based training (R-010, R-033) | Basic | Focused |

GSA's own systems (SYS-10) were not assessed. GSA assesses them under its ATO.

## 2. Methods and objects
- **Examine:** identity provider, access control, and BAS user lists; VPN route tables; edge firewall rules; CMMS asset lists; backup settings; purchase records; subcontracts; training records; the GSA PIV roster; POL-01 to POL-05; the BIA; the P08 runbook.
- **Interview:** COO, IT Manager, IT/OT Systems Administrator, Controls Engineering Manager, Security Systems Supervisor, Contracts Manager, HR Manager, 3 Site Managers, and 8 randomly selected technicians and ROC operators (incident reporting awareness).
- **Test:**
  - connection test from a technician laptop to confirm whether the VPN reaches site networks without the jump host
  - sign-in tests, including MFA on privileged accounts
  - default-credential test on 40 BACnet controllers and 9 NVRs, read-only, after hours, with written county approval and the county facilities manager present
  - passive BACnet discovery at the county government center (listen-only, no active scanning of controllers)
  - traceroute from a county office network jack to OT devices at a service center
  - restore of one supervisory database to an isolated VM

## 3. Rules of engagement
- No test could change a setpoint, schedule, door state, or program. Credential tests used read-only sessions, and the county facilities manager watched each one.
- No active vulnerability scans against field controllers. SP 800-82 Rev. 3 warns that active scanning can disrupt OT devices.
- Customer approval was obtained in writing before any test on a customer network.
- No cardholder data, face templates, or CUI left company systems. Screenshots were redacted.
- The assessor would stop and notify the IT Manager and the affected Site Manager on finding any exposure that needed action within 24 hours. **One stop occurred:** the integrator remote-support tool (below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 33 |
| Other than satisfied | 130 |

**Fully other than satisfied (11):** AC-6, AC-17, AT-3, AU-6, CM-6, CP-2, CP-4, IA-2, IA-2(1), RA-5, SR-3. No documented process or working mechanism existed for these.

**Largely satisfied:** IR-6 (the matrix exists; staff awareness is the gap), SA-9 (vendor SOC 2 reviews work; subcontractors are the gap), CP-9 (daily backups run and restore works, but backups are exposed), AC-2 (provisioning works; removal and shared accounts are the gaps).

**Stop-and-notify finding (2026-08-04):** the integrator's remote-support tool on a county engineering workstation, first seen in the July walkthrough, was confirmed active and reachable with no MFA or approval. The assessor escalated it under the rules of engagement. The COO directed the integrator to disable the tool between visits from 2026-08-05 (interim, checked weekly), and it is to be removed by 2026-10-15 (POAM-001). The county was notified the same day under the contract's notice clause.

**New findings from testing:**
- Default passwords on 9 BACnet controllers and 1 NVR (IA-05e.). Risk R-003 re-rated on 2026-08-06; POAM-002.
- 23 BACnet devices at the county government center missing from the asset list (CM-08a.01). Risk R-032 added on 2026-08-05; POAM-013.
- The test restore of a supervisory database worked but took 9 hours because there was no procedure (CP-09d.[03]); POAM-007 and POAM-009.

Every one of the 22 controls had at least one weakness. They are covered by 21 POA&M items in `poam.csv` (IA-2 and IA-2(1) share POAM-003): 1 Very High (POAM-001), 9 High (POAM-002 to POAM-010), and 11 Moderate.

## 5. Deliverables
`assessment-results.csv` (163 rows), `poam.csv` (21 items), and this plan and summary. The COO accepted the results on 2026-08-31. The SSP and POA&M go to the state agency by 2026-10-31.
