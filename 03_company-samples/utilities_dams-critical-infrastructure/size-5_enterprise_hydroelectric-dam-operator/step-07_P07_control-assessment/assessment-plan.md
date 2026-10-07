# Security Assessment Plan and Report: Cris Santos Company | Dams | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company) |
| System assessed | Hydro Fleet Control and Dam Monitoring System (HFCDMS), CSC-OT-HFC-001, per the SSP (P02), including the enterprise and OT common controls it inherits |
| Tier / Vertical | Enterprise / Dams |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and two IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with two OT specialists from a co-sourced firm. None of the assessors designs or operates the controls. The GRC team and the NERC compliance team (second line) supported scoping only. The co-sourced firm does not perform the plant vulnerability assessments it was asked to evaluate (POAM-004 uses a different firm) |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork, including site walkthroughs at HOC-A, HOC-B, DEV-04, PD-04, and PD-06 on 2026-07-14 to 2026-07-17); report issued 2026-09-04; presented to the audit committee and the safety, risk, and reliability committee on 2026-09-10 |
| Also satisfies | Annual assessment for the HFCDMS authorization (P02 section 4.2); independent assessment evidence for FERC Form 3 Questions 24b and 31; input to the NERC internal controls program (not a substitute for SERC audits) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **48 controls (AC 7, AT 1, AU 4, CA 1, CM 6, CP 6, IA 3, IR 3, MA 1, MP 1, PE 3, PS 1, RA 2, SA 2, SC 2, SI 3, SR 2), 297 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (Piedmont remote access, monitoring below the HOC, legacy equipment, recovery, vendor concentration);
- carry Section 9 enhanced measures and NERC CIP requirements with gaps or high consequence in P03;
- protect integrity and availability of gate and unit control, the High impact objectives in P02 section 6;
- are common controls the HFCDMS inherits that no other assessment covered this year.

The Piedmont plants are outside the HFCDMS boundary (P02 section 2) and were assessed through the P03 gap analysis; their weaknesses are carried here as POAM-001 and POAM-002 so leadership tracks one list.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-056; CIP-004-7 R4 | Comprehensive | Comprehensive | 1,240 OT domain account events (2026-01-01 to 2026-06-30); 412 people with CIP access | 60 account events (random); 2 quarterly CIP access verifications | 26 / 0 |
| AC-3 | R-036; CIP-011-3 R1 | Focused | Comprehensive | SCADA role matrix; 3 BCSI repositories and enterprise file shares | 100% (role export; DLP scan) | 0 / 1 |
| AC-4 | R-007; Section 9 segregation | Focused | Focused | 21 data diodes; HOC ESP rule base (612 rules) | 5 diodes tested; 60 rules (random) | 1 / 0 |
| AC-5 | R-005; Section 9 enhanced access control | Focused | Comprehensive | 64 engineers and 82 operators | 100% (role export) | 2 / 0 |
| AC-6 | R-004 | Focused | Focused | 2,310 OT PAM elevation sessions | 25 sessions (random) | 1 / 0 |
| AC-17 | R-003; R-054; CIP-005-7 R2 | Comprehensive | Comprehensive | 61 remote and third-party paths (58 registered plus 3 found); 4,180 vendor sessions | 100% of paths (network discovery and cellular survey at 44 dams); 60 sessions (random) | 3 / 1 |
| AC-17(1) | R-054 | Focused | Comprehensive | 61 remote paths | 100% | 0 / 2 |
| AT-2 | R-059; CIP-004-7 R1 | Basic | Focused | 12,000 workforce (1,420 with OT access; 412 with CIP access) | 60 training records (random); 4 quarterly CIP awareness bulletins | 10 / 0 |
| AU-2 | R-008; CIP-007-6 R4 | Focused | Focused | HOC log sources; 98 plant HMIs | Event types generated in test at HOC-A; 10 plant HMIs (random) | 5 / 1 |
| AU-6 | R-008; R-002; Form 3 Q14 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 35 plants | 5 weeks (random); 100% of plants | 2 / 1 |
| AU-9 | R-001 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-12 | R-008 | Basic | Focused | HOC components; plant devices | 12 HOC servers; 10 plant devices | 2 / 1 |
| CA-7 | Form 3 Q14; continuous monitoring | Focused | Basic | 6 monthly OT metric packages | 3 months (random) | 10 / 1 |
| CM-2 | R-013; CIP-010-4 R1 | Focused | Focused | 412 HOC Cyber Assets; 35 plant baselines | 25 HOC assets (random); 5 plant baselines | 5 / 0 |
| CM-3 | R-034; CIP-010-4 R1 | Comprehensive | Comprehensive | 312 OT change records (2026-01-01 to 2026-06-30) | 40 changes (random, stratified: 20 HOC, 20 plant) | 9 / 1 |
| CM-5 | R-034 | Focused | Focused | 312 changes | 10 changes traced to PAM sessions | 6 / 0 |
| CM-6 | R-022 | Focused | Comprehensive | 412 HOC Cyber Assets | 100% (configuration compliance scan) | 6 / 0 |
| CM-7 | CIP-007-6 R1 | Focused | Comprehensive | 412 HOC Cyber Assets | 100% (port scan against documented need) | 6 / 0 |
| CM-8 | R-008; Section 9.2 | Comprehensive | Comprehensive | About 6,800 OT components | 60 physical devices traced to the inventory (random, 6 plants) | 4 / 2 |
| CP-2 | R-012; CIP-009-6 R1 | Comprehensive | Focused | n/a (plan) | Recovery plans v7 examined; 4 interviews | 24 / 0 |
| CP-4 | CIP-009-6 R2 | Focused | Focused | 1 annual failover exercise; 1 backup restore test | 100% | 5 / 0 |
| CP-7 | R-012 | Focused | Focused | 1 failover exercise | 100% | 3 / 1 |
| CP-8 | R-021; R-014; CIP-012-2 R1.2 | Focused | Comprehensive | 35 plants; 2 HOCs | 100% (circuit inventory) | 0 / 1 |
| CP-9 | R-013; Form 3 Q16 | Focused | Comprehensive | 181 nightly SCADA backup jobs; logic copies for 35 plants | 25 jobs (random); 100% of plants | 5 / 1 |
| CP-10 | R-012 | Focused | Focused | 1 failover exercise | 100% | 1 / 1 |
| IA-2 | R-004; CIP-007-6 R5 | Basic | Focused | About 900 OT domain accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | CIP-005-7 R2.3 | Focused | Comprehensive | 64 privileged OT accounts | 100% | 1 / 0 |
| IA-5 | CIP-007-6 R5.4 to R5.6; Form 1 Q6 | Focused | Comprehensive | 412 HOC Cyber Assets; 120 plant devices with web or console logins | 100% at HOC (analytic); 120 plant devices tested with vendor-approved tools | 10 / 0 |
| IR-4 | R-002; CIP-008-6 R1.4 | Focused | Focused | 148 OT-related security cases (2025-07 to 2026-06) | 25 cases (random) | 13 / 0 |
| IR-6 | CIP-008-6 R4; 18 CFR 12.10 | Basic | Focused | 148 cases; 2 attempts to compromise evaluated | 25 cases; both evaluations | 2 / 0 |
| IR-8 | R-047; Form 3 Q25 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with the General Counsel, CFO, CISO, and Director, NERC Compliance | 15 / 2 |
| MA-4 | R-024; R-054 | Focused | Comprehensive | 4,180 vendor sessions; 3 datalogger vendors | 60 sessions (random); all 3 vendors | 7 / 1 |
| MP-7 | R-023; CIP-010-4 R4; CIP-003-9 Att. 1 Sec. 5 | Focused | Focused | 1,140 contractor plant visits | 25 visits (random) | 1 / 1 |
| PE-3 | R-011; CIP-006-6 R1 | Comprehensive | Focused | HOC PSPs; 23 Group 1 and 2 dams | PACS reports for 2 HOCs; walkthroughs at 5 sites | 12 / 0 |
| PE-6 | CIP-006-6 R1.5 | Focused | Focused | PSP alarms (2026-01 to 2026-06) | 25 alarms (random) | 5 / 0 |
| PE-11 | 18 CFR 12.54(c) | Basic | Focused | HOC UPS; standby power at 36 gated dams in scope | 100% of 2026 load test records | 1 / 0 |
| PS-4 | R-056; CIP-004-7 R5.1 | Comprehensive | Comprehensive | 412 terminations of people with CIP access | 60 (random) | 4 / 1 |
| RA-3 | Form 3 Q23, Q30 | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-008; Section 9 enhanced vulnerability assessment | Focused | Comprehensive | 35 plants; 2 HOCs | 100% | 7 / 2 |
| SA-9 | R-024; R-054 | Focused | Comprehensive | 14 external services supporting the HFCDMS | 100% | 5 / 1 |
| SA-22 | R-006; R-022 | Focused | Comprehensive | About 1,150 OT hosts | 100% (analytic) | 1 / 1 |
| SC-7 | R-007; CIP-005-7 R1 | Comprehensive | Focused | n/a (architecture) | Reachability tests from the corporate network and one plant to the HOC ESP; cellular survey | 5 / 1 |
| SC-8 | CIP-012-2 R1.1 | Basic | Focused | ICCP and inter-HOC links | 100% (configuration and traffic capture) | 1 / 0 |
| SI-2 | R-022; CIP-007-6 R2 | Focused | Focused | 12 patch evaluation cycles; about 1,150 OT hosts | 12 cycles; 25 patches (random) | 9 / 1 |
| SI-3 | CIP-007-6 R3 | Focused | Focused | 412 HOC Cyber Assets; 73 allowlisted hosts | 25 hosts (random) | 8 / 0 |
| SI-4 | R-008; R-054; Form 3 Q14 | Comprehensive | Comprehensive | 35 plants; 2 HOCs | 100% (sensor coverage); detection test at HOC-A | 10 / 2 |
| SR-5 | R-024 | Focused | Comprehensive | 31 OT contracts signed or renewed (2025-07 to 2026-06) | 100% | 2 / 1 |
| SR-6 | CIP-013-2 R2 | Focused | Focused | 22 tier-1 OT vendors | 10 (random) | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic or a small population allowed it.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, AT-2, CM-8, PS-4, and the AC-17 and MA-4 vendor session samples.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection. Used for CM-3, stratified 20 HOC and 20 plant changes so that plant engineering practices were tested.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated through the period. Used for AC-6, CM-2, CP-9, IA-2, IR-4, IR-6, MP-7, PE-6, SI-2, and SI-3.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; quarterly, every quarter in the period; annual, the single occurrence.
- **Small populations and analytics:** every plant (35), every remote path (61), every privileged OT account (64), and every HOC Cyber Asset for configuration and default credential tests.
- **Physical verification:** OT inventory accuracy (CM-8) was tested by tracing devices found in the field to the inventory at 6 plants chosen at random, and a cellular modem survey was run at all 44 instrumented dams in scope; that survey found the POAM-012 paths.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects gate operation or a CIP time limit (PS-4, AC-17, CM-3 for gate logic) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), CIP evidence packages, Section 9 determinations, identity governance and PAM records, Intermediate System session logs, OT change records, backup and logic copy registers, the failover exercise report, vulnerability assessment schedules, vendor contracts, the incident response plan and materiality playbook.
- **Interview:** Senior Vice President, Hydro Operations (CIP Senior Manager); Director, Hydro Operations Center; Director, Hydro Control Systems Engineering; Director, OT Security; Director, OT Network Engineering; Director of Security Operations; Director, NERC Compliance; Vice President, Dam Safety; General Counsel; CFO; 3 plant managers; 12 HOC operators; 3 datalogger vendors.
- **Test:** access and lockout tests with test accounts; default-credential tests on plant devices (vendor-approved tools, during maintenance windows); one-way flow tests on 5 data diodes; reachability tests from the corporate network and a plant toward the HOC ESP; a cellular modem survey; a SIEM detection test at HOC-A; malicious code test file; observation of a partial switchover to HOC-B.

## 4. Rules of engagement
- **No test could change a gate, unit, or setpoint.** Plant tests ran only with the plant manager's approval, with the affected gates and units in local control and an operator present.
- Active scanning was not used on PLCs or governors; plant device tests used vendor-approved, read-only tools.
- Tests on HOC Cyber Assets were coordinated with the NERC compliance team so that CIP-010 baselines and change records stayed accurate.
- All workpapers containing BCSI or CEII were stored in the restricted repository (POL-04).
- Critical exposures were reported to the CISO and the Vice President, Dam Safety within 24 hours. One was: the cellular datalogger paths (reported 2026-08-31; modems disabled 2026-09-02).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-14 to 2026-07-17 | Site walkthroughs at HOC-A, HOC-B, DEV-04, PD-04, and PD-06 |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including the cellular survey |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, CIP Senior Manager, and Vice President, Dam Safety |
| 2026-09-10 | Presented to the audit committee and the safety, risk, and reliability committee |

Deliverables: this plan and report, `assessment-results.csv` (297 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 268 |
| Other than satisfied | 29 |
| **Total** | **297** |

**Controls with at least one Other than satisfied statement: 24 of 48:** AC-3, AC-17, AC-17(1), AU-2, AU-6, AU-12, CA-7, CM-3, CM-8, CP-7, CP-8, CP-9, CP-10, IR-8, MA-4, MP-7, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-4, SR-5.

**Fully Other than satisfied:** AC-3, AC-17(1), CP-8 (AC-3 has 1 statement, AC-17(1) has 2 statements, CP-8 has 1 statement).

**Themes:**
1. **Seeing and assessing below the HOC:** monitoring (SI-4, AU-6, CA-7) and vulnerability assessment (RA-5) reach the HOC hub but not every plant.
2. **Undocumented vendor paths:** the cellular datalogger connections (AC-17, AC-17(1), MA-4, SC-7, SI-4) were the one new finding, and the most urgent.
3. **Legacy equipment:** unsupported HMIs and gate workstations (SA-22, SI-2, RA-5, AU-2, AU-12) and stale logic copies (CP-9).
4. **Recovery and resilience:** HOC failover (CP-7, CP-10) and telecom diversity (CP-8).
5. **Third parties:** the OEM contract (SR-5, SA-9).
6. **Two potential CIP issues:** late physical access removal (PS-4) and BCSI outside an authorized repository (AC-3). Both were self-reported to SERC on 2026-09-30.
7. **Disclosure readiness:** the incident plan has not been exercised with the current disclosure committee (IR-8).

**Strengths:** HOC identity and privileged access (AC-2, AC-6, IA-2, IA-2(1), IA-5), segregation and one-way data flow (AC-4, AC-5), configuration management at the HOC (CM-2, CM-5, CM-6, CM-7), physical security (PE-3, PE-6), encryption of real-time data (SC-8), malicious code protection (SI-3), and incident handling (IR-4, IR-6) were all Satisfied.

## 7. POA&M summary
`poam.csv` holds 23 items: 14 from this assessment and 9 carried from the P03 gap analysis, the P05 BIA, the P09 readiness review, and the P10 AI assessment, so leadership tracks one list.

| Risk level | Items |
|---|---|
| Very High | 1 |
| High | 14 |
| Moderate | 8 |
| Low | 0 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 3 |

The Section 9 subset of this POA&M is the plan and schedule filed with FERC under Rev. 3A 9.1.1.3. CIP-related items (POAM-001, POAM-006, POAM-016) also have mitigation plans with SERC.

## 8. Conclusion
Internal Audit concludes that the HFCDMS control environment is **effective with exceptions**. The HOC medium impact controls, identity, configuration management, physical security, and incident handling operate effectively. The exceptions concentrate in coverage below the HOC (monitoring, vulnerability assessment, inventory), legacy plant equipment, recovery time, and third parties, plus one undocumented vendor path that has been contained. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
