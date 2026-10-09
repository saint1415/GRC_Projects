# Security Assessment Plan and Summary: Cris Santos Company | Food and Agriculture | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| System assessed | Plant Production and Cold-Chain Monitoring System (PPCM: SYS-01 to SYS-07, SYS-14, SYS-15), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Food and Agriculture |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, and 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The Security Manager and the Controls Engineering Manager arranged access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (OT testing in the sanitation windows: Plant 1 2026-08-08 to 2026-08-09; Plant 2 2026-08-15 to 2026-08-16) |
| Also satisfies | Annual internal IT audit; the annual independent assessment in POL-01 4.11 |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **32 controls, 244 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- test the control side of the binding-rule gaps in P03 (record integrity, change control, incident response, remote access to refrigeration controls);
- confirm two strengths the SOC 2 work in P09 relies on (RA-3 and SC-28).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle and shared OT accounts; 9 CFR 417.5(b); R-020 | Focused | Focused (25 of 74 terminations; all 31 transfers) |
| AC-5, AC-6, CM-5 | Setpoint and recipe changes by shared logins; 417.2(c)(3); R-003, R-004 | Comprehensive | Comprehensive (all HMI setpoint screens on the sampled lines; all Plant 2 blenders) |
| AC-17, MA-4 | OT remote access; R-002 (Very High), R-005, R-023 | Comprehensive | Comprehensive (every remote path at both plants) |
| IA-2, IA-2(1), IA-5 | Unique identification, MFA, default and shared credentials; R-019, R-052 | Focused | Comprehensive (all 22 privileged IdP and cloud accounts; all 47 OT privileged accounts); 14 inspection devices and 20 HMIs for default credentials |
| AT-2 | Floor workforce awareness; R-046 | Basic | Focused (20 floor worker interviews) |
| AU-2, AU-6, SI-4 | OT logging and monitoring; R-009, R-045 | Focused | Focused |
| CM-3 | OT change control; 417.4(a)(3)(i); 1910.119(l); R-004 | Focused | Focused (25 of 186 Plant 1; all 41 Plant 2 changes) |
| CM-7, CM-8 | Least functionality and inventory; R-010, R-011 | Focused | Focused (20 HMIs, 6 OT servers; physical count of Lines 5-7) |
| CP-2, CP-4, CP-9, CP-10 | OT recovery; R-001 (Very High), R-007, R-008, R-016 | Comprehensive | Comprehensive |
| IR-4, IR-8 | Incident handling tied to food safety and PSM; 417.3(b); 418.2; R-015, R-051 | Focused | Focused (10 of 17 incidents) |
| PE-3 | Physical protection of OT spaces; R-047 | Basic | Focused (both plants) |
| RA-3 | Risk assessment (strength relied on by P01 and P09) | Basic | Basic |
| RA-5, SI-2 | Vulnerability and flaw remediation; R-041 | Focused | Comprehensive (all 64 Critical and High findings) |
| SA-9, SR-6 | Vendor oversight; R-023, R-024 | Focused | Comprehensive (all 26 vendors with OT, cloud, or data access) |
| SC-7 | Segmentation; R-001 (Very High) | Comprehensive | Comprehensive (both plants) |
| SC-28 | Encryption at rest (strength relied on by P09) | Basic | Focused (30 laptops) |
| SI-7 | Integrity of programs, firmware, and CCP records; 417.5(d); R-006 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items. Where the population is small or the risk is high, the whole population was tested. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations of identity provider account holders (2025-07-01 to 2026-06-30) | 74 | 25 | AC-2, PS-4 |
| Transfers | 31 | 31 | AC-2 |
| Privileged identity provider and cloud accounts | 22 | 22 | IA-2(1), AC-6 |
| OT privileged and engineering accounts | 47 | 47 | IA-2(1), AC-6 |
| OT change records, 2026 Q1-Q2 | 186 Plant 1; 41 Plant 2 | 25 Plant 1; 41 Plant 2 | CM-3 |
| MES formulation releases, 2026 Q2 | 58 | 15 | AC-5, SI-7 |
| Inspection devices (x-ray units, metal detectors) | 14 | 14 (default-credential test) | IA-5 |
| HMIs | 86 | 20 (services and credentials) | CM-7, IA-5 |
| Cloud backup job days (July 2026) | 30 | 30 | CP-9 |
| Critical and High vulnerability findings (2026 Q1-Q2) | 64 | 64 | RA-5, SI-2 |
| Security incidents (12 months to 2026-06-30) | 17 | 10 | IR-4 |
| Vendors with OT, cloud, or data access | 26 | 26 | SA-9, SR-6 |
| Laptops | about 400 | 30 | SC-28 |
| Floor workers for awareness interviews | about 620 | 20 (10 per plant) | AT-2 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts; the SSP draft
  - identity provider, cloud, HMI, MES, and Plant 2 directory account exports
  - change tickets, MES release logs, historian and records application settings
  - backup, patch, scan, and EDR reports; restore test records
  - vendor files and contracts; the 2024 IR plan and the P08 drafts
  - PSM management of change and emergency plans (for the coordination objectives)
- **Interview:**
  - vCISO, IT Director, Security Manager, OT security engineer, GRC Analyst
  - Controls Engineering Manager and 2 controls engineers
  - VP FSQA, both plant FSQA managers, both Plant Managers
  - Director of Engineering and Maintenance; HR Director
  - the MSSP service lead; both controls integrators
  - 20 randomly selected floor workers
- **Test (OT tests only in the sanitation windows, with the Controls Engineering Manager present):**
  - MFA sign-in tests on all 22 privileged identity provider and cloud accounts
  - default-credential tests on 14 inspection devices and 20 HMIs (read-only checks; no settings changed)
  - port and service scan of 20 HMIs and 6 OT servers, rate-limited and approved by the integrators
  - reachability tests: Plant 2 office VLAN to a blender HMI; Plant 1 business network to level 2
  - a new device connected to a Plant 1 level 2 switch to test detection
  - an altered formulation copy loaded to the MES test environment to test integrity checking
  - a connection attempt to the Plant 2 VPN with the shared account (then disabled)
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one records application table from the backup account

### What each test could show
The 2026 policies (P06), the standards index, and the P08 runbooks were drafts during fieldwork; they were approved on 2026-09-15 and the policies take effect on 2026-10-01. The 2024 policies, standards, and plans were in force, so controls built on them were tested for operation. A requirement that only a draft introduces has not operated yet, so the drafts were reviewed for design only. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control was in place before fieldwork and was tested on samples or live systems (122 Satisfied, 56 Other than satisfied) | 178 |
| Design | The requirement comes from a 2026 draft (the quarterly access review in POL-02; the food safety, FSIS notice, and PSM steps in the P08 runbooks); its design was reviewed. Operation is tested at the 2027 Q3 follow-up | 4 |
| Not implemented | Nothing existed to test | 62 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on). Each sample population in section 2 comes from an intake export: terminations and transfers from the HR report (EV-003), privileged identity provider and cloud accounts from EV-006, OT privileged and engineering accounts from EV-007, OT change records from EV-027, MES formulation releases from EV-026, HMIs from the Plant 1 sensor export and the Plant 2 equipment list (EV-011, EV-012), inspection devices from EV-011 and EV-012, Critical and High findings from the scan reports (EV-018), incidents from the incident log (EV-033), vendors from the contract register (EV-048), laptops from the endpoint console (EV-010), and floor workers from the HR roster (EV-003).

## 4. Rules of engagement
- No testing that could affect product, people, or the ammonia systems. OT tests ran only when lines were down for sanitation, with the Controls Engineering Manager and the relevant plant FSQA manager present. No setpoint, recipe, or controller value was changed. Refrigeration controllers were examined only, never tested.
- No production data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system.
- Stop-and-notify rule: any critical exposure is reported to the Security Manager and the vCISO the same day. **Used twice:**
  - On 2026-08-08 the assessors found that the Plant 1 Line 6 x-ray unit (foreign material CCP) accepted the manufacturer default administrator password on its web service. The password was changed on 2026-08-09, and the company logged the finding as P01 R-052 on 2026-08-10.
  - On 2026-08-15 the assessors confirmed that the Plant 2 VPN accepted the shared integrator account without MFA. The Security Manager disabled the account outside supervised sessions; that became the interim condition in the SSP (section 4.2).

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 122 |
| Other than satisfied | 122 |
| **Total** | **244** |

Other than satisfied statements by risk: 12 Very High, 80 High, 30 Moderate.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | Moderate | POAM-001 |
| AC-5 | 0 | 2 | High | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-003 |
| AC-17 | 2 | 2 | Very High | POAM-004 |
| AT-2 | 7 | 3 | Moderate | POAM-005 |
| AU-2 | 3 | 3 | High | POAM-006 |
| AU-6 | 2 | 1 | High | POAM-006 |
| CM-3 | 3 | 7 | High | POAM-007 |
| CM-5 | 2 | 4 | High | POAM-002 |
| CM-7 | 3 | 3 | Moderate | POAM-008 |
| CM-8 | 2 | 4 | Moderate | POAM-008 |
| CP-2 | 5 | 19 | High | POAM-009 |
| CP-4 | 2 | 3 | High | POAM-010 |
| CP-9 | 2 | 4 | High | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 0 | 2 | High | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-003 |
| IA-5 | 6 | 4 | High | POAM-011 |
| IR-4 | 8 | 5 | High | POAM-012 |
| IR-8 | 11 | 6 | High | POAM-012 |
| MA-4 | 1 | 7 | Very High | POAM-004 |
| PE-3 | 8 | 4 | Moderate | POAM-013 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | Moderate | POAM-014 |
| SA-9 | 2 | 4 | High | POAM-015 |
| SC-7 | 3 | 3 | Very High | POAM-016 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 7 | 3 | Moderate | POAM-014 |
| SI-4 | 6 | 6 | High | POAM-006 |
| SI-7 | 1 | 5 | High | POAM-017 |
| SR-6 | 0 | 1 | High | POAM-015 |

**Fully satisfied (2 controls):** RA-3 (the SP 800-30 risk assessment) and SC-28 (cloud data encrypted with company-managed keys; all 30 sampled laptops encrypted).

**Fully other than satisfied (6 controls):** AC-5, AC-6, CP-10, IA-2, IA-2(1), and SR-6. IA-2(1) is the clearest example of the company's split: all 22 privileged identity provider and cloud accounts required MFA, and none of the 47 OT privileged and engineering accounts did.

**Themes:**
1. **IT is close to sound; OT is not.** Where a statement was tested on both layers, the IT half usually passed (MFA, encryption, EDR, cloud backups, MSSP escalation in 22 minutes) and the OT half failed.
2. **Shared OT identities defeat several controls at once** (AC-2, AC-5, AC-6, CM-5, IA-2, IA-5). They are also why electronic CCP records cannot be attributed (P03 G-040, G-042).
3. **Plant 2 accounts for both Very High results** (AC-17 and MA-4 through remote access, SC-7 through the flat network).
4. **Recovery of OT is unplanned and untested** (CP-2, CP-4, CP-9, CP-10). The cloud restore test in this assessment succeeded in 40 minutes, which shows the method works.

**POA&M:** 30 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Five more items come from the gap analysis, the SOC 2 readiness assessment, and the AI assessment (POAM-018 food defense reanalysis and Injector 2 interlock, POAM-019 Plant 2 cold-chain alerting, POAM-020 PSM and RMP change and emergency plans, POAM-021 AI governance, POAM-022 SOC 2 readiness). The total is 22 items: 2 Very High, 15 High, and 5 Moderate. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued; OT test plan approved by the Controls Engineering Manager and both Plant Managers |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-08 to 2026-08-09 | Plant 1 OT tests (sanitation window) |
| 2026-08-10 to 2026-08-14 | IT tests; corporate interviews |
| 2026-08-15 to 2026-08-16 | Plant 2 OT tests (sanitation window) |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (244 rows); `poam.csv` (22 items).
