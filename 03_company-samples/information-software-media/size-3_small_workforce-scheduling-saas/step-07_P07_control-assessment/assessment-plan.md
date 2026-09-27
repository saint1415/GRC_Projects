# Security Assessment Plan and Summary: Cris Santos Company | Information | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| System assessed | Workforce Scheduling Platform (WSP), per the SSP (P02), including the connected staging environment |
| Tier / Vertical | Small / Information |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not the SOC 2 service auditor and not involved in designing or operating the controls. Supported by the IT Manager as coordinator |
| Assessment window | 2026-08-31 to 2026-09-04 (plan agreed 2026-08-24) |
| Also supports | SOC 2 Type 2 readiness (P09); the FTC "Start with Security" practices tested in P03 |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **23 controls, 164 determination statements.** Controls were chosen because they address the 4 High risks in P01, the 6 High gaps in P03, the 3 SOC 2 Type 1 exceptions, or the P08 incident scenario, or because the company makes a public claim about them (encryption, MFA).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, AC-6(9) | Shared break-glass role and broad CI keys: R-001, R-002 (High); P03 G-005, G-032; Type 1 exception 1 | Focused | Comprehensive (all production, staging, and repository accounts) |
| AC-3 | Tenant isolation: R-005 (High); P03 G-013 | Focused | Focused (40 of about 190 API endpoints) |
| IA-2(1), IA-5 | Public MFA claim; static CI keys: R-001, R-030; P03 G-007 | Focused | Comprehensive for privileged and machine credentials |
| AU-2, AU-6, AU-11, SI-4 | No monitoring of data leaving the platform: R-031; P03 G-014; P08 scenario | Focused | Focused (production account, database, payroll export bucket) |
| SA-3(2) | Production data in staging: R-003 (High); P03 G-003; Type 1 exception 2 | Basic | Comprehensive |
| SA-9 | Sub-processor oversight: R-004, R-019; P03 G-021, G-022, G-036; Type 1 exception 3 | Focused | Comprehensive (all 6 sub-processors) |
| SA-11, CM-3 | Secure development and change control: R-005; P03 G-009, G-019, G-020; SOC 2 CC8.1 | Focused | Focused (25 pull requests; 90-day bypass log) |
| CP-2, CP-4, CP-9 | Availability new to SOC 2 scope: R-006, R-007, R-028; P03 G-039 | Focused | Focused |
| IR-4, IR-6 | Untested plan; 72-hour and 48-hour customer notice: R-009; P03 G-030, G-031, G-035 | Focused | Basic |
| RA-5 | Unenforced image scanning: R-013; P03 G-020, G-023 | Basic | Focused |
| SC-28 | Public encryption claim: P03 G-034 | Basic | Comprehensive (all data stores) |
| SI-12 | 90-day deletion promise: R-011; P03 G-037 | Basic | Focused |
| AT-3 | No secure coding training: P03 G-017 | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider, cloud IAM, database, and repository account exports; the vault checkout log; logging, retention, backup, and encryption settings; CI configuration and branch protection; the January 2026 penetration test and restore test records; sub-processor contracts and the AI model provider's API terms; the SOC 2 Type 1 report; incident tickets and training records.
- **Interview:** CTO, IT Manager, Platform Engineering Lead, Engineering Manager, COO, Customer Support Manager, People Operations Manager, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - cross-tenant requests from 2 assessor test tenants against 40 sampled API endpoints
  - sign-in tests with hardware keys for 2 production engineers and 1 identity provider administrator
  - permission simulation for one CI key and for snapshot deletion
  - a simulated bulk read of 200 test files from the payroll export bucket, to see whether any alert fires
  - a read-only secret scan of repository history
  - a test session under the break-glass role, to see what is logged

## 3. Rules of engagement
- Testing used 2 assessor test tenants with synthetic data. No customer data was copied, exported, or viewed beyond configuration screens.
- The assessor received a named, read-only role that expired at the end of fieldwork. The break-glass test session was run by the Platform Engineering Lead with the assessor observing; no data was changed.
- The simulated bulk read used test files placed in a separate prefix of the payroll export bucket and removed afterward.
- No load, denial-of-service, or social engineering tests. Tests ran outside the shift-change peaks (after 10:00 Eastern).
- The assessor would stop and notify the IT Manager and CTO on finding any critical exposure. One was found and handled that way (section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 59 |
| Other than satisfied | 105 |
| **Total** | **164** |

**Fully other than satisfied:** AC-6, AC-6(9), AU-6, AU-11, SA-3(2), CP-2, and AT-3. No working process or technology existed for these.
**Satisfied in full:** AC-3 (every sampled endpoint blocked cross-tenant requests), IA-2(1) (hardware-key MFA for all privileged accounts), and SC-28 (encryption at rest on every data store). The public encryption and MFA claims are accurate.
**Mostly satisfied:** CM-3 (7 of 10) and RA-5 (6 of 9): the processes exist but are not enforced.

**Key test result.** The simulated bulk read of 200 payroll export test files raised no alert, and object-level access was not logged, so the read could not be seen afterward either. This is the P08 scenario in practice: a leaked CI key could copy payroll exports with no trace (POAM-005 to POAM-008).

**New finding.** Two former contractors still had source repository access through local accounts outside single sign-on (AC-02f.[04] and [05]). The assessor reported it the same day. The IT Manager removed the accounts on 2026-09-04, and it was added to the risk register as R-015. POAM-001 closes the process gap.

All 20 controls with weaknesses have POA&M items in `poam.csv`: 8 High (POAM-001 to POAM-005, POAM-007, POAM-009, and POAM-010) and 12 Moderate. 9 items are in progress and 11 are open.

## 5. Deliverables
`assessment-results.csv` (164 rows), `poam.csv` (20 items), and this plan and summary. The CTO accepted the results and the POA&M on 2026-09-22. The Chief Executive Officer approved the High items' dates on the same day. The IT Manager reviews the POA&M monthly with the CTO (CA-5).
