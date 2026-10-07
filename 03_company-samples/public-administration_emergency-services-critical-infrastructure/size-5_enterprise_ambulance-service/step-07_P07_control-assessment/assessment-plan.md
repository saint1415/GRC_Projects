# Security Assessment Plan and Report: Cris Santos Company | Emergency Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider) |
| System assessed | Enterprise Dispatch and Patient Care Platform (EDPCP), CSC-SYS-EDPCP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Emergency Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. A former CAD administrator who joined Internal Audit in 2026 was kept off the CM-3 and AC-5 tests |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | HIPAA evaluation (45 CFR 164.308(a)(8)); annual assessment for the EDPCP authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 1, AU 5, CA 1, CM 5, CP 6, IA 4, IR 3, PE 1, PS 1, RA 2, SA 2, SC 3, SI 3), 271 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (ransomware against dispatch, failover time, the AQ-01 pathway, fleet devices, untested CAD configuration changes);
- cover HIPAA Required implementation specifications with gaps in P03;
- test the High-baseline availability supplements that matter most for dispatch (CP-4(2), CP-7, CP-10);
- are common controls the EDPCP inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-034; 164.308(a)(3)(ii)(C) | Comprehensive | Comprehensive | 1,240 CAD and ePCR account events; 1,410 terminations (96 at AQ-01) | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AQ-01) | 22 / 4 |
| AC-2(3) | R-034 | Focused | Comprehensive | About 14,300 accounts (CAD, ePCR, hospital portal) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-010 | Focused | Focused | 1,900 CAD users | 25 users (random) | 1 / 0 |
| AC-5 | R-008 | Comprehensive | Comprehensive | 22 CAD administrators | 100% | 2 / 0 |
| AC-6 | R-021 | Focused | Focused | 1,620 PAM elevation sessions | 25 sessions (random) | 1 / 0 |
| AC-7 | R-024 | Basic | Focused | n/a (configuration) | 2 test accounts | 2 / 0 |
| AC-17 | R-009; R-030 | Focused | Comprehensive | 6 remote access paths | 100% | 3 / 1 |
| AT-2 | R-001; 164.308(a)(5) | Basic | Focused | 12,000 workforce (850 dispatchers) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AU-2 | R-056; 164.312(b) | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-010; R-016; 164.308(a)(1)(ii)(D) | Comprehensive | Comprehensive | 26 weeks of SOC reviews; 43 log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings; deletion attempt | 2 / 0 |
| AU-11 | R-057 | Basic | Basic | n/a (configuration) | Retention settings | 1 / 0 |
| AU-12 | R-016 | Basic | Focused | n/a (configuration) | 6 CAD servers, CAD-to-CAD hub, mobile gateway | 3 / 0 |
| CA-7 | 164.308(a)(8) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-001 | Focused | Comprehensive | 236 servers and consoles | 100% | 4 / 1 |
| CM-3 | R-008 | Comprehensive | Comprehensive | 212 CAD change records (128 response plan, run card, or unit recommendation changes) | 40 changes (random) | 8 / 2 |
| CM-5 | R-008 | Focused | Focused | 212 changes | 10 changes traced to PAM | 6 / 0 |
| CM-6 | R-006 | Focused | Comprehensive | About 1,290 routers; 236 servers and consoles | 100% | 4 / 2 |
| CM-8 | R-006; 164.310(d) | Comprehensive | Comprehensive | About 9,600 fleet devices | 60 devices traced (random, 6 stations) | 5 / 1 |
| CP-2 | R-005; R-001 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; 3 interviews | 22 / 2 |
| CP-4 | R-005 | Focused | Focused | 12 drills; 1 regional failover test | 100% | 5 / 0 |
| CP-4(2) | R-028; R-005 | Focused | Comprehensive | 3 enterprise communications centers | 100% | 0 / 2 |
| CP-7 | R-028 | Basic | Focused | n/a (configuration) | Standby region and center position mapping examined | 4 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-005 | Focused | Focused | 1 regional failover test | 100% | 1 / 1 |
| IA-2 | R-058 | Focused | Comprehensive | 1,900 CAD accounts; about 1,290 MDCs | 25 sign-ins (random); 100% of MDC configurations | 1 / 1 |
| IA-2(1) | R-021 | Focused | Comprehensive | 34 privileged accounts | 100% | 1 / 0 |
| IA-5 | R-009 | Focused | Comprehensive | 12 radio console gateways | 100% (vendor-approved, in maintenance windows) | 9 / 1 |
| IA-8 | R-034 | Focused | Comprehensive | About 2,600 hospital portal accounts | 100% (data analytic) | 0 / 1 |
| IR-4 | R-060; R-001 | Focused | Focused | 214 incidents (5 at AQ-01) | 25 incidents (random) plus all 5 AQ-01 incidents | 11 / 2 |
| IR-6 | R-001 | Basic | Focused | 214 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-017 | Comprehensive | Focused | n/a (plan) | Plan and playbook examined; interviews with the General Counsel, CFO, CISO | 15 / 2 |
| PE-3 | R-063 | Basic | Comprehensive | 3 communications centers | 100% walkthrough; 25 badge events (random) | 12 / 0 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,410 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | 164.308(a)(1)(ii)(A) | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-001; R-006 | Focused | Focused | 2,140 vulnerability findings | 60 findings (random) | 8 / 1 |
| SA-9 | R-025; R-037 | Focused | Comprehensive | 12 external services | 100% | 5 / 1 |
| SA-22 | R-006 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-003 | Comprehensive | Focused | n/a (architecture) | Reachability test from the AQ-01 site network | 5 / 1 |
| SC-8 | R-059 | Basic | Focused | 30 PSAP interfaces, mobile gateway, ePCR interfaces | 100% (TLS scan) | 0 / 1 |
| SC-28 | R-022 | Basic | Focused | n/a (configuration) | Encryption settings inspected | 1 / 0 |
| SI-2 | R-001; R-048 | Focused | Focused | 228 patches | 25 patches (random) | 9 / 1 |
| SI-4 | R-001; R-016 | Focused | Focused | 231 sites | Test device on the console segment; AQ-01 coverage review | 11 / 1 |
| SI-10 | R-008; R-039 | Focused | Focused | 20 malformed and out-of-scope messages | 100% in the CAD training environment | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CP-9, IA-2, IR-4, IR-6, PE-3, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; quarterly drills and the annual test, every occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 14,300 accounts for inactivity, all 12 radio console gateways for default credentials, all 30 PSAP interfaces for TLS).
- **Stratification:** terminations were stratified so AQ-01 (7% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key dispatch-safety control (CM-3, AC-5, CP-10) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, CAD role matrix and audit trails, CAD change tickets and test records, drill and failover test reports, backup reports, vulnerability scans, vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Communications Centers; Director of CAD and Dispatch Systems; Medical Director for Communications; an RCC-3 supervisor; ePCR Application Manager; Director of Security Operations; Director of Identity and Access Management; Director of Endpoint and Mobile Engineering; Director of Network Engineering; General Counsel; CFO; CISO; 20 randomly selected dispatchers and field staff.
- **Test:** access tests with test accounts; lockout tests; default-credential tests on radio console gateways (with vendor approval, in maintenance windows); a network reachability test from the AQ-01 site network; a test device on the console segment; TLS scans of PSAP and mobile interfaces; malformed and out-of-scope PSAP messages in the CAD training environment; a restore observation.

## 4. Rules of engagement
- No testing could affect live dispatch. Console and gateway tests ran only in scheduled maintenance windows, with the center manager's approval, a supervisor present, and manual dispatch staffed in case of disruption.
- Malformed message tests ran only in the CAD training environment.
- The test device on the console segment was an audit-owned laptop with no ePHI, pre-approved by the CISO and the Vice President, Communications Centers.
- No ePHI left the company's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor passwords on 4 radio console gateways (reported 2026-08-12; changed 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Communications Centers |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (271 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 238 |
| Other than satisfied | 33 |
| **Total** | **271** |

**Controls with at least one Other than satisfied statement: 24 of 44:** AC-2, AC-2(3), AC-17, AU-6, CM-2, CM-3, CM-6, CM-8, CP-2, CP-4(2), CP-10, IA-2, IA-5, IA-8, IR-4, IR-8, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4.

**Fully Other than satisfied:** CP-4(2) (both statements), IA-8 and SC-8 (each has a single determination statement).

**Themes:**
1. **Dispatch recovery** is the main system-specific weakness: the regional failover missed the 1-hour RTO (CP-10), RCC-3 has never failed over (CP-4(2)), and the plan has not absorbed the test's lessons (CP-2).
2. **Dispatch configuration integrity:** response plan and run card changes are approved inside the centers without independent testing (CM-3).
3. **Acquired-operation integration** drives the identity (AC-2, PS-4), monitoring (AU-6, SI-4), network (SC-7), and incident handling (IR-4) findings.
4. **Fleet and console edge:** end-of-support routers (SA-22, CM-6), console patching (RA-5, SI-2), baseline drift (CM-2), inventory (CM-8), shared MDC logins (IA-2), vendor remote access (AC-17), and default gateway passwords (IA-5).
5. **Disclosure readiness:** the SEC materiality step has never been exercised for a dispatch outage (IR-8).

**Strengths:** manual dispatch drills (CP-4), separation of CAD administration duties (AC-5), privileged access (IA-2(1), AC-6), immutable logs and backups (AU-9, CP-9), physical security of the dispatch floors (PE-3), workforce training (AT-2), and PSAP message validation that drops law enforcement fields (SI-10) were all Satisfied.

**New finding during testing:** default vendor passwords on 4 radio console gateways (IA-05e.). Added to the risk register as R-009 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 23 items: 16 from this assessment and 7 carried from the P03 gap analysis (POAM-007, POAM-013, and POAM-019 to POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 11 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the EDPCP control environment is **effective with exceptions**. Enterprise common controls for identity, logging, backup, physical security, and monitoring operate effectively, and manual dispatch is well drilled. The exceptions concentrate in recovery time, dispatch configuration change control, fleet edge devices, and controls that depend on integrating AQ-01. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
