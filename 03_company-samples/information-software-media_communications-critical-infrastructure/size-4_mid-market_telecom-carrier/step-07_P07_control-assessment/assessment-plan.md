# Security Assessment Plan and Summary: Cris Santos Company | Communications | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| System assessed | Network Operations and Customer Billing Platform (OSS/BSS: SYS-01 to SYS-05, SYS-09, SYS-13, SYS-16, SYS-18), per the SSP (P02), with its interfaces to the network elements it manages |
| Tier / Vertical | Mid-Market / Communications |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 network specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The GRC analyst coordinated access but did not select samples or rate findings. The Security Manager, who reports to the CTO, had no role in rating |
| Assessment window | 2026-08-03 to 2026-08-21 (site work 2026-08-10 to 2026-08-13; network tests in maintenance windows 2026-08-12 and 2026-08-13) |
| Also supports | The evidence behind the annual CPNI certification statement (47 CFR 64.2009(e)); the annual internal IT audit |
| Results accepted | Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 234 determination statements.** Every determination statement for each selected control was assessed. Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- support the CPNI, CALEA, outage, and 911 requirements with gaps in the gap analysis (P03);
- support inherited-control reliance and the SOC 2 readiness work for Business Services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; R-023; 64.2010(a) | Focused | Focused (samples of 25) |
| AC-6, IA-2, IA-2(1), IA-5 | Management plane and privileged access; R-002, R-004 (High) | Comprehensive | Comprehensive (25 privileged accounts; 20 access elements, 2 SBCs) |
| AC-17, MA-4 | Vendor remote access; R-051 | Focused | Comprehensive (all July 2026 vendor sessions) |
| AT-3 | CPNI and role-based training; 64.2009(b); R-007 | Focused | Focused |
| AU-2, AU-6, AU-11, SI-4 | Monitoring gaps; R-009 (High); 64.2010(a) | Focused | Focused |
| CM-2, CM-3, CM-6, CM-8 | Configuration and inventory; R-032, R-042, R-043, R-050 | Focused | Focused (25 changes; 25 cabinet switches; 40-device count at POP-A) |
| CP-2, CP-4, CP-9, CP-10 | Recovery; R-003 (High), R-026, R-027 | Comprehensive | Comprehensive |
| IA-8 | Customer authentication; 64.2010(c), (e); R-006 (High) | Comprehensive | Comprehensive (portal, app, chatbot, SYS-18) |
| IR-4, IR-6, IR-8 | Incident capability and CPNI notice; 64.2011; R-011 | Focused | Focused |
| PE-3 | Physical access to central offices, POPs, cabinets; 1.20003 (CALEA room) | Basic | Focused (5 sites, 4 cabinets) |
| PT-4 | CPNI approval before use; 64.2007, 64.2009(a); R-037 | Focused | Focused |
| RA-5, SI-2 | Network element vulnerabilities; R-001 (Very High) | Comprehensive | Comprehensive (50 critical findings) |
| SA-9, SR-6 | Vendors with CPNI or network access; R-024 | Focused | Focused (34 vendors) |
| SA-22 | Unsupported components; R-030, R-031 | Basic | Comprehensive |
| SC-5, SC-7 | DDoS and segmentation; R-028, R-002, R-005 | Focused | Focused (reachability test at POP-A) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control operating many times a year with moderate risk; 5 to 10 items for weekly or monthly controls; the whole population when it is small. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Transfers | 77 | 25 | AC-2 |
| New BSS accounts | 188 | 25 | AC-2 |
| Privileged accounts across all admin planes | 118 | 25 for MFA tests | IA-2(1) |
| Access elements for configuration and credential tests | about 2,100 | 20 access elements and 2 SBCs | AC-6, IA-2, IA-5 |
| Cabinet switches for SNMP and management service checks | 268 | 25 | CM-6, IA-5 |
| Changes (network, Business Services, cloud), 2026 Q2 | 412 | 25 | CM-3 |
| Devices physically counted at POP-A | 40 | 40 | CM-8 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Vendor remote sessions (July 2026) | 47 | 47 | AC-17, MA-4 |
| Incidents (2025-07 to 2026-06) | 41 | 10 | IR-4 |
| Critical vulnerability findings (2026 Q1-Q2) | 50 | 50 | RA-5, SI-2 |
| Vendors with CPNI, PII, or network access | 34 | 34 | SA-9, SR-6 |
| Staff for reporting-awareness interviews | 850 | 15 | IR-6 |
| Sites for walkthroughs | 9 central offices, 2 POPs, 268 cabinets | CO-1, CO-4, CO-6, POP-A, POP-B, 4 cabinets | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:** policies (2024 set and 2026 drafts); the SSP draft; IdP, BSS, SYS-18, TACACS+, and cloud exports; network element configurations; backup, patch, scan, and MDR reports; vendor contracts; the incident log and 2025 tabletop report; the NOC outage plan; change tickets.
- **Interview:** vCISO, CTO, IT Director, Security Manager and analysts, Vice President of Regulatory Affairs, Vice President of Network Operations, NOC Director, Director of Network Engineering, Director of Customer Operations, Director of Business Services, Billing Director, Marketing Director, HR Director, the MDR service lead, and 15 randomly selected staff.
- **Test:**
  - MFA sign-in tests on 25 sampled privileged accounts
  - login tests with the shared local account on 10 access elements and 2 SBCs (with NOC supervision)
  - SNMP and Telnet checks on 25 cabinet switches
  - reachability test from a corporate VLAN at POP-A to the management plane
  - portal, app, chatbot, and SYS-18 password reset tests with test accounts
  - a simulated impossible-travel sign-in to test MDR escalation
  - a restore of one mediation file from the backup account
  - an EICAR test file on 5 endpoints (all quarantined)
  - a BSS query of call detail views without a matching care ticket

## 4. Rules of engagement
- **No service impact.** Network tests ran only in approved maintenance windows with the NOC watching. No test touched 911 trunks, the voice core call path, or SYS-10. Login tests used read-only commands.
- **No CPNI left company systems.** Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- **Stop-and-notify.** Any critical exposure is reported to the CTO and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported the shared vendor VPN account with standing access to the management network and a password unchanged since 2023. The company restricted the account to approved windows on 2026-08-14 and logged the finding as P01 R-051.
- The 3 agents found viewing call detail with no related ticket (AU-6 test) were referred to the Vice President of Regulatory Affairs under the CPNI procedures, not investigated by the assessors.
- The SNMP finding on cabinet switches was logged as P01 R-032 on 2026-08-14.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 132 |
| Other than satisfied | 102 |
| **Total** | **234** |

Other than satisfied statements by risk: 49 High, 49 Moderate, 4 Low.

| Control | Satisfied | Other than satisfied | Risk (highest) | POA&M |
|---|---|---|---|---|
| AC-2 | 20 | 6 | High | POAM-001; POAM-002 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-3 | 5 | 4 | Moderate | POAM-004 |
| AU-2 | 2 | 4 | Moderate | POAM-005 |
| AU-6 | 1 | 2 | High | POAM-005 |
| AU-11 | 0 | 1 | Moderate | POAM-005 |
| CM-2 | 2 | 3 | Moderate | POAM-006 |
| CM-3 | 6 | 4 | Moderate | POAM-007 |
| CM-6 | 3 | 3 | Moderate | POAM-006 |
| CM-8 | 2 | 4 | Moderate | POAM-008 |
| CP-2 | 10 | 14 | High | POAM-009 |
| CP-4 | 1 | 4 | High | POAM-010 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 1 | 1 | High | POAM-002 |
| IA-2(1) | 0 | 1 | High | POAM-002 |
| IA-5 | 6 | 4 | High | POAM-002 |
| IA-8 | 0 | 1 | High | POAM-011 |
| IR-4 | 9 | 4 | Moderate | POAM-012 |
| IR-6 | 1 | 1 | Moderate | POAM-012 |
| IR-8 | 10 | 7 | Moderate | POAM-012 |
| MA-4 | 3 | 5 | High | POAM-003 |
| PE-3 | 8 | 4 | Low | POAM-013 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| PT-4 | 0 | 1 | Moderate | POAM-019 |
| RA-5 | 6 | 3 | High | POAM-014 |
| SA-9 | 3 | 3 | Moderate | POAM-015 |
| SA-22 | 1 | 1 | Moderate | POAM-017 |
| SC-5 | 2 | 0 | n/a | n/a |
| SC-7 | 4 | 2 | High | POAM-018 |
| SI-2 | 7 | 3 | High | POAM-014 |
| SI-4 | 8 | 4 | High | POAM-005 |
| SR-6 | 0 | 1 | Moderate | POAM-015 |

**Fully satisfied (2 controls):** CP-9 (daily, isolated, write-once, encrypted backups in a second region) and SC-5 (always-on scrubbing that mitigated 3 attacks in 2026).

**Fully other than satisfied (7 controls):** AC-6, AU-11, CP-10, IA-2(1), IA-8, PT-4, and SR-6.

**Themes:**
1. **The management plane is the largest exposure.** Shared accounts without MFA (AC-6, IA-2, IA-2(1), IA-5), a vendor VPN account with standing access (AC-17, MA-4), and reachability from POP corporate VLANs (SC-7). Core routers are protected; access elements, SBCs, and POPs are not.
2. **The company cannot see network element activity** (AU-2, AU-6, AU-11, SI-4) or vulnerabilities (RA-5, SI-2). The MDR covers IT, not the network.
3. **IT recovery is unproven** (CP-2, CP-4, CP-10), although backups are strong (CP-9).
4. **CPNI controls slipped in new channels** (IA-8 chatbot fallback and SYS-18 reset; PT-4 approval checks; AT-3 vendor training).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 18 POA&M items from this assessment (POAM-001 to POAM-015, POAM-017, POAM-018, and POAM-019), because related controls share an item. Seven more items come from the gap analysis and the AI assessment: POAM-016 (SYS-18 CPNI duties), POAM-020 (CALEA refiling), POAM-021 (911 reliability and PSAP contacts), POAM-022 (RMD and traceback), POAM-023 (Covered List check), POAM-024 (AI governance), and POAM-025 (CPNI certification evidence and records). The total is 25 items: 9 High, 14 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Site walkthroughs and technical tests (maintenance windows on 2026-08-12 and 2026-08-13) |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (234 rows); `poam.csv` (25 items).
