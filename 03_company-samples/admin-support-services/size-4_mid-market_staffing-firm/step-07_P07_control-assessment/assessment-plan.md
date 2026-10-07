# Security Assessment Plan and Summary: Cris Santos Company | Administrative and Support and Waste Management | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) |
| System assessed | Associate Payroll and Applicant Tracking Platform (APATP), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the board audit committee. The firm designs and operates none of the assessed controls and will not perform the SOC 2 examination (P09). The Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-17 to 2026-09-04 (site testing 2026-08-25 to 2026-08-27 at HQ, Branch 6, Branch 9, and On-site Program 2) |
| Also supports | The inspection and quality assurance program for electronic Forms I-9 (8 CFR 274a.2(e)(1)(iii)); CSF 2.0 ID.IM-01; SOC 2 readiness evidence (P09) |
| Results accepted | Chief Operating Officer, 2026-09-22; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **35 controls, 247 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the binding I-9, E-Verify, FCRA, ADA, and Florida gaps and the High CSF gaps in the gap analysis (P03);
- support processes rated High in the BIA (P05), especially payroll and credential verification;
- will be tested by the service auditor in the SOC 2 examination of Managed Workforce Solutions (P09).

| Control | Why selected (risk ID or gap row) | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-3, AC-5, AC-6 | Access to I-9 images, consumer reports, SSNs, medical files, and payroll; R-003, R-006, R-009, R-010; G-057, G-121 | Focused | Focused (samples of 25 and 15; all E-Verify and VMS users) |
| IA-2, IA-2(1), IA-5, AC-17 | Associate and payroll sign-in, the integration key, contractor access; R-001, R-002, R-052; G-055, G-070 | Comprehensive | Comprehensive (all privileged accounts reviewed; 25 MFA tests) |
| IA-12 | Remote I-9 examinations; R-033; G-108 | Basic | Focused |
| AT-2, AT-3 | Training gaps; R-002; G-059, G-060 | Basic | Focused |
| AU-2, AU-6, AU-12, SI-4 | SaaS visibility; I-9 audit trail; R-021, R-042; G-068, G-077, G-124 | Focused | Focused |
| CM-3, CM-8 | Change control and inventory; R-046; G-045, G-037 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Contingency and recovery, manual payroll; R-004 (Very High), R-005, R-026; G-064, G-102, G-122 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; R-022; G-086, G-141 | Focused | Basic |
| MP-6, SI-12 | Disposal and retention; R-014; G-038, G-139 | Basic | Focused |
| PE-3 | Branch physical access; G-058 | Basic | Focused (4 sites) |
| PT-5 | FCRA, AI, biometric, and recording notices; R-008, R-015, R-034; G-151 | Focused | Focused |
| RA-3, RA-5, SI-2 | Risk assessment and vulnerability management; R-036; G-039 | Focused | Focused (all 41 critical findings) |
| SA-9, SR-6 | Vendor oversight; R-017, R-029 to R-031; G-022 to G-031 | Focused | Focused (20 contracts) |
| SC-7, SC-28 | Kiosk networks and encryption; R-019; G-071 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control operating many times a year at moderate risk; 5 to 15 for weekly, monthly, or small populations; the whole population where it is small or risk is high. Populations were extracted in the auditors' presence and samples chosen at random.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Internal staff terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 (via AC-2) |
| Internal transfers | 38 | 15 | AC-2 |
| E-Verify and VMS user accounts | 22 and 28 | All | AC-2 |
| Privileged accounts (all admin planes) | 31 | 25 for MFA tests; all 31 for rights review | IA-2(1), AC-6 |
| ATS configuration changes (2026 H1) | about 140 | 10 | CM-3 |
| Remote I-9 examinations (2026 H1) | about 900 | 15 | IA-12 |
| Endpoints | about 970 | 30 (inventory and encryption) | CM-8, SC-28 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Vendor contracts with personal information | 64 | 20 | SA-9 |
| Incidents (2025-2026) | 46 | 10 | IR-4 |
| Critical vulnerability findings (2026 H1) | 41 | 41 | RA-5, SI-2 |
| Asset disposals and reuse wipes (2025-2026) | 37 | 10 | MP-6 |
| Outbound recruiter call recordings | about 9,000 a month | 20 | PT-5 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Sites for walkthroughs | 21 | 4 (HQ with Branch 1, Branch 6, Branch 9, On-site Program 2) | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts; the SSP draft; the BIA
  - IdP, ATS, payroll, E-Verify, VMS, credentialing, warehouse, and cloud exports
  - backup, patch, scan, and EDR reports; container registry and repository settings
  - vendor contracts and SOC 2 reports
  - the incident log and the 2026 H1 pay diversion case files
  - career site notices, text assistant scripts, clock enrollment records, and call recordings
  - destruction certificates and asset records
- **Interview:**
  - vCISO, Security Manager, security analyst, GRC analyst, IT Director
  - Director of Compliance and Privacy, General Counsel, Director of Payroll and Billing, Credentialing Manager, Director of Recruiting Operations, Contact Center Manager
  - the MSSP service lead and the integration contractor's lead developer
  - 15 randomly selected staff, including on-site coordinators
- **Test:**
  - a recruiter-role test account (created with COO approval) opening I-9 images, consumer reports, and credential files
  - a warehouse query from an analyst account
  - a test export of 5,000 associate records by a test payroll user, then a check for alerts
  - MFA sign-in tests on 25 privileged accounts
  - a container image and repository scan for credentials (with the IT Director present)
  - a restore of one integration platform container from the backup account
  - a read of a scanned Form I-9 in the archive, then a log search
  - a reachability test from a Branch 9 kiosk to staff devices
  - a simulated impossible-travel sign-in to test MSSP escalation

## 4. Rules of engagement
- No testing that could disrupt payroll week. Payroll tests ran on Monday and Tuesday with the Director of Payroll and Billing present; the test export used a test user and was deleted under supervision.
- No Restricted data left firm systems. Screenshots were redacted, and evidence was kept in the audit firm's encrypted workpaper system.
- Stop-and-notify rule: any critical exposure is reported to the IT Director and the vCISO the same day. **Used once:** on 2026-08-26 the auditors found the payroll API key in the integration container image and repository. The key was rotated on 2026-08-27, and the firm logged the finding as P01 R-052 on 2026-08-26.
- Medical documents seen during the AC-3 test were not opened beyond confirming access.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 136 |
| Other than satisfied | 111 |
| **Total** | **247** |

Other than satisfied statements by risk: 38 High, 55 Moderate, 18 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | High, Moderate, Low | POAM-001, POAM-006 |
| AC-3 | 0 | 1 | High | POAM-002 |
| AC-5 | 0 | 2 | Moderate | POAM-021 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 3 | 1 | Moderate | POAM-004 |
| AT-2 | 8 | 2 | Low | POAM-005 |
| AT-3 | 4 | 5 | Moderate, Low | POAM-022 |
| AU-2 | 1 | 5 | High, Moderate | POAM-006 |
| AU-6 | 1 | 2 | High, Moderate | POAM-006 |
| AU-12 | 1 | 2 | Moderate | POAM-006 |
| CM-3 | 4 | 6 | High, Moderate | POAM-007 |
| CM-8 | 3 | 3 | Moderate | POAM-008 |
| CP-2 | 5 | 19 | High | POAM-009, POAM-011 |
| CP-4 | 2 | 3 | High | POAM-010 |
| CP-9 | 4 | 2 | High, Moderate | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 1 | 1 | High | POAM-003 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High, Low | POAM-001, POAM-003, POAM-004 |
| IA-12 | 3 | 2 | Moderate | POAM-019 |
| IR-4 | 7 | 6 | Moderate, Low | POAM-012 |
| IR-6 | 1 | 1 | Low | POAM-005 |
| IR-8 | 13 | 4 | Moderate, Low | POAM-012 |
| MP-6 | 2 | 2 | Moderate | POAM-014 |
| PE-3 | 9 | 3 | Low | POAM-013 |
| PT-5 | 2 | 4 | Moderate | POAM-015, POAM-020 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-016 |
| SA-9 | 1 | 5 | Moderate | POAM-017 |
| SC-7 | 4 | 2 | Moderate | POAM-018 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 5 | 5 | Moderate, Low | POAM-016 |
| SI-4 | 10 | 2 | High, Moderate | POAM-006 |
| SI-12 | 0 | 4 | Moderate | POAM-014 |
| SR-6 | 0 | 1 | Moderate | POAM-017 |

**Fully satisfied (3 controls):** IA-2(1) (MFA on all 25 sampled privileged accounts), RA-3 (the 2026 SP 800-30 assessment), and SC-28 (encryption at rest on every sampled store and device). The MSSP escalation test was answered in 18 minutes, and all 30 July backup jobs succeeded, which confirms the strengths in the scenario facts.

**Fully other than satisfied (6 controls):** AC-3, AC-5, AC-6, CP-10, SI-12, and SR-6.

**Themes:**
1. **Access to Restricted data is far wider than the law and the policies allow** (AC-3, AC-6, AC-5): 262 users with I-9 and consumer report access, 46 with full SSNs.
2. **Secrets and sign-ins where pay moves are weak** (IA-2, IA-5, AC-17): associate SMS codes and the exposed payroll API key.
3. **The firm can detect endpoint attacks but not SaaS misuse** (AU-2, AU-6, SI-4): a 5,000-record payroll export raised no alert.
4. **Recovery is unproven, and payroll has no manual fallback** (CP-2, CP-4, CP-10): the integration platform restore failed because its secrets were outside the backup scope.

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 22 POA&M items (POAM-001 to POAM-022), because related controls share an item. Three more items come from the gap analysis and the AI assessment (POAM-023 electronic I-9 program, POAM-024 AI governance conditions, POAM-025 ADA medical files). The total is 25 items: 8 High, 15 Moderate, and 2 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-10 | Plan and sample requests issued |
| 2026-08-17 to 2026-08-21 | Document examination and interviews |
| 2026-08-25 to 2026-08-27 | Site walkthroughs and technical tests |
| 2026-08-28 to 2026-09-04 | Analysis, draft findings, management responses |
| 2026-09-22 | Results and POA&M accepted by the COO and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (247 rows); `poam.csv` (25 items).
