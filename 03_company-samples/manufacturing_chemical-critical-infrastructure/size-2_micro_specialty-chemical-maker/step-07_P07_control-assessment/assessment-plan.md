# Security Assessment Plan and Summary: Cris Santos Company | Chemical | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| System assessed | Blending and Business Platform (BBP), per the SSP (P02) |
| Tier / Vertical | Micro / Chemical |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT testing cautions from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent OT-experienced security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager (Security Coordinator) and, for blend room tests, the Operations Manager. MSP lead technician on site for office tests; integrator lead engineer on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11, blending stopped for the day) |
| Benchmark served | CISA RBPS 8 security measure on recurring audits (P03 G-013), as a voluntary benchmark (C-CHEMICAL-R01) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 99 determination statements.** Controls were chosen because they support the three High risks in P01 (remote access to the PLC, ransomware over the flat network, and no recovery path), cover the High gaps in P03, or test what the MSP and the integrator do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-17 | Always-on integrator remote access (P01 R-001; P03 G-004, G-012) | Focused | Comprehensive (portal, gateway, HMI services, 1 month of sessions) |
| IA-2(1) | MFA on privileged and remote logins, including MSP-held logins (R-001, R-017, R-018) | Focused | Comprehensive (every login that can change a system) |
| AC-2, PS-4 | Shared HMI login; departed operator and bookkeeper (R-004, R-017; G-005, G-008) | Focused | Comprehensive (all 7 staff in every SaaS service, the portal, and the HMI) |
| CP-9, CP-4 | No backup of the PLC program and HMI project; nothing restore-tested (R-005, R-018; G-020) | Focused | Focused |
| SC-7 | HMI PC on the flat office network (R-002; G-006, G-014) | Focused | Focused (office and guest Wi-Fi; PLC excluded from active testing) |
| SI-2, SI-3 | HMI PC unpatched with no antivirus; MSP patching and antivirus (R-002, R-003; G-017) | Focused | Focused (HMI PC, 3 office computers, alert routing) |
| CM-3 | Unlogged, unapproved recipe and alarm limit changes (R-006; G-007) | Focused | Focused (10 batch tickets) |
| AT-2, IR-6 | No cyber training; no reporting rule; call list on the office phones (R-013, R-014, R-023; G-011, G-016, G-034) | Basic | Focused (5 of 7 staff interviewed) |
| SA-9 | No security terms for the integrator or MSP; AI feature switched on without notice (R-007, R-010, R-016) | Focused | Comprehensive (all 7 vendors that run or reach company systems) |

## 2. Methods and objects
- **Examine:** SaaS user exports (suite, accounting, SDS, payroll); the HMI user list and services list; the integrator portal's account page, session log, and AI feature settings; the MSP contract and integrator service agreement; the accounting vendor's SOC 2 report; the DOT training binder; termination records; the emergency action plan; 10 batch tickets from June and July 2026; and the MSP and integrator evidence listed below.
- **Interview:** the Owner, the Operations Manager, the Office Manager, 5 of 7 staff (training and incident reporting), the MSP lead technician, and the integrator lead engineer (by phone).
- **Test:**
  - user lists compared with the staff roster in every SaaS service, the portal, and the HMI
  - sign-in attempts without a second factor to the portal, the accounting service, the firewall management page, and the backup console (with the MSP present)
  - a limited port check of the HMI PC from an office laptop and from a laptop on the guest Wi-Fi; the PLC and gateway were not scanned
  - patch and version checks on the HMI PC and 3 office computers
  - an industry-standard harmless antivirus test file on 1 office desktop, and an after-hours test alert to check routing
  - the 10 batch tickets compared with the recipes stored on the HMI

### MSP and integrator evidence requested
The MSP and the integrator operate most technical controls, so much of the evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| Monthly patch report (July 2026) and patch policy | MSP | SI-2 | Yes, 2026-08-07 |
| Antivirus console export (all devices) | MSP | SI-3 | Yes, 2026-08-07 |
| Firewall rule export and Wi-Fi configuration | MSP | SC-7 | Yes, 2026-08-07 |
| Backup job report (July 2026), retention settings, and vendor encryption documentation | MSP | CP-9 | Yes, 2026-08-10 |
| Record of any restore test | MSP | CP-4 | No record exists (confirmed by the MSP) |
| Technician list with access to the company, and MFA on the remote management platform | MSP | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-013 |
| Portal session log (July 2026) and list of integrator staff using the shared login | Integrator | AC-17, AC-2 | Session log yes, 2026-08-06; staff list not provided |
| Date and checksum of its copy of the PLC program and HMI project | Integrator | CP-9 | Date only (2023); no checksum exists |
| HMI software, PLC firmware, and gateway firmware versions | Integrator | SI-2 | Yes, 2026-08-10 |

## 3. Rules of engagement
- **Safety first.** Blending was stopped for the day on 2026-08-11, with the T-1 heater and all dosing pumps off and tote valves closed by the Operations Manager before any blend room test.
- **No active testing of the PLC or gateway.** SP 800-82 Rev. 3 warns that scans can upset controllers. Tests touched only the HMI PC, and only with a port check that the integrator agreed to in advance. No settings were changed on the HMI, PLC, gateway, or portal.
- **No data left the site.** Screenshots of recipes were cropped to the recipe name before they went into the evidence folder (Restricted under POL-04).
- **Stop and tell.** The assessor would stop and tell the Owner at once about any critical exposure. The guest Wi-Fi finding was reported the same afternoon, and until the MSP separates it, the guest Wi-Fi password is given out only on request (R-011).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 84 |
| **Total** | **99** |

**Fully other than satisfied:** AC-17, IA-2(1), CP-4, SI-2, AT-2, IR-6. No process or technology met the objective.
**Partly satisfied:** SI-3 (office computers detect and quarantine malware; the HMI PC has no protection, and alerts after hours are missed) and PS-4 (keys and equipment come back; access and shared secrets do not change). The other controls met only a few statements, mostly where the MSP or a SaaS vendor does the work.

**New findings from testing:**
1. A laptop on the guest Wi-Fi reached the HMI PC's remote desktop service (SC-07a.[04], SC-07b.). Added to the risk register as R-011 on 2026-08-11 and to POAM-006.
2. Two of 10 sampled batch tickets did not match the recipe stored on the HMI, and no record shows who changed it (CM-03b.[02]). QC had passed both batches. POAM-009.
3. The portal session log shows 14 integrator sessions in July 2026, 9 of them outside business hours, none approved in advance (AC-17b.). The integrator says all were routine monitoring. POAM-001.
4. The after-hours antivirus test alert was not seen until the next morning, and the company is never told of detections (SI-03c.02[02]). POAM-008.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001, POAM-002, POAM-004, POAM-005, and POAM-006: remote access, MFA, backup, restore testing, and network separation. They are the same three themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (99 rows), `poam.csv` (13 items: 5 High, 8 Moderate), and this plan and summary. The Owner and President accepted the results on 2026-08-31.
