# Security Assessment Plan and Report: Cris Santos Company | Health Care | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-specialty medical group) |
| System assessed | Laboratory Information System (LIS), CSC-SYS-LIS-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Health Care and Social Assistance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | HIPAA evaluation (45 CFR 164.308(a)(8)); annual assessment for the LIS authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 1, AU 6, CA 1, CM 5, CP 4, IA 4, IR 3, PS 1, RA 2, SA 2, SC 3, SI 5), 263 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (ransomware, acquired-practice integration, medical devices, result integrity);
- cover HIPAA Required implementation specifications with gaps in P03;
- protect LIS result integrity (the High-baseline supplements in P02 section 6);
- are common controls the LIS inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-034; 164.308(a)(3)(ii)(C) | Comprehensive | Comprehensive | 1,184 LIS account events (2026-01-01 to 2026-06-30); 1,236 terminations of staff with LIS or EHR access (88 at AQ-06 to AQ-08) | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AQ) | 22 / 4 |
| AC-2(3) | R-034 | Focused | Comprehensive | 3,620 accounts (520 workforce; 3,100 outreach portal) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-009 | Focused | Focused | 520 workforce LIS users | 25 users (random) | 1 / 0 |
| AC-5 | R-009; 42 CFR 493.1291(a) | Comprehensive | Comprehensive | 14 users with the build administrator role | 100% | 1 / 1 |
| AC-6 | R-021 | Focused | Focused | 1,840 PAM elevation sessions to LIS servers and database | 25 sessions (random) | 1 / 0 |
| AC-7 | R-024 | Basic | Focused | n/a (configuration) | SSO and outreach portal lockout tested with 2 test accounts | 2 / 0 |
| AC-17 | R-011 | Focused | Comprehensive | 9 instrument platforms; 3 remote access paths | 100% | 3 / 1 |
| AT-2 | R-001; 164.308(a)(5) | Basic | Focused | 12,000 workforce (452 lab staff) | 60 workforce training records (random); phishing results for 6 months | 10 / 0 |
| AU-2 | R-010 | Focused | Focused | n/a (configuration) | 5 event types generated in test | 6 / 0 |
| AU-6 | R-016; R-010; 164.308(a)(1)(ii)(D) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 41 log sources on the LIS order and result path | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-10 | R-009; 42 CFR 493.1291(a) | Focused | Focused | About 3.1 million autoverified results in the period | 25 results (random) | 0 / 1 |
| AU-11 | R-057 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-010 | Basic | Focused | n/a (configuration) | 4 LIS servers and 2 middleware servers | 3 / 0 |
| CA-7 | 164.308(a)(8) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-009 | Focused | Focused | 6 servers | 100% | 4 / 1 |
| CM-3 | R-009; 42 CFR 493.1291(a) | Comprehensive | Comprehensive | 184 LIS change records (2026-01-01 to 2026-06-30) | 40 changes (random) | 8 / 2 |
| CM-5 | R-009 | Focused | Focused | 184 changes | 10 changes traced to PAM sessions | 6 / 0 |
| CM-6 | R-006 | Focused | Comprehensive | 20 components (4 LIS servers, 2 middleware, 14 analyzer workstations) | 100% | 4 / 2 |
| CM-8 | R-007 | Comprehensive | Comprehensive | About 1,900 devices at the central lab and patient service centers | 60 physical devices traced to the CMDB (random, 5 sites) | 5 / 1 |
| CP-2 | R-031 | Comprehensive | Focused | n/a (plan) | Plan v4 examined; 3 interviews | 22 / 2 |
| CP-4 | R-031 | Focused | Focused | 1 annual DR test | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-031 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-021 | Basic | Focused | 520 workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-021 | Focused | Comprehensive | 22 privileged LIS and database accounts | 100% | 1 / 0 |
| IA-5 | R-058 | Focused | Comprehensive | About 60 analyzers | 100% (tested with vendor approval, after hours) | 9 / 1 |
| IA-8 | R-034 | Focused | Comprehensive | 3,100 outreach portal accounts | 100% (data analytic) | 0 / 1 |
| IR-4 | R-060 | Focused | Focused | 212 security incidents (6 at AQ sites) | 25 incidents (random) plus all 6 AQ incidents | 11 / 2 |
| IR-6 | R-001 | Basic | Focused | 212 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-017 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with General Counsel, CFO, CISO | 15 / 2 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,236 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | 164.308(a)(1)(ii)(A) | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-006 | Focused | Focused | 1,904 vulnerability findings on LIS components | 60 findings (random) | 8 / 1 |
| SA-9 | R-037 | Focused | Comprehensive | 11 external services supporting the LIS | 100% | 5 / 1 |
| SA-22 | R-006 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-003 | Comprehensive | Focused | n/a (architecture) | Test from AQ-07 site network to interface engine | 5 / 1 |
| SC-8 | R-059 | Basic | Focused | All LIS interfaces | 100% (TLS scan; lab segment capture) | 0 / 1 |
| SC-28 | R-022 | Basic | Focused | n/a (configuration) | Database and backup encryption inspected | 1 / 0 |
| SI-2 | R-006 | Focused | Focused | 212 patches | 25 patches (random) | 9 / 1 |
| SI-4 | R-008 | Focused | Focused | 159 sites (64 without NAC) | Rogue device test at 2 patient service centers without NAC | 11 / 1 |
| SI-7 | R-010; 42 CFR 493.1291(a) | Comprehensive | Focused | n/a | File integrity monitoring and result integrity controls examined | 4 / 2 |
| SI-7(1) | R-010 | Focused | Focused | n/a | Integrity check logs examined | 2 / 1 |
| SI-10 | R-009 | Focused | Focused | 20 malformed test messages | 100% in the test environment | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AU-10, CP-9, IA-2, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 3,620 accounts for inactivity, all 60 analyzers for default credentials).
- **Stratification:** terminations were stratified so the acquired practices (7% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key patient-safety control (CM-3, AC-5, AU-10) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, LIS role matrix and audit trails, change tickets and validation records, backup and DR test reports, vulnerability scans, vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Laboratory Services; Laboratory Director; LIS Application Manager; Director of Security Operations; Director of Identity and Access Management; Director of Clinical Engineering; Director of Network Engineering; General Counsel; CFO; CISO; 20 randomly selected lab staff.
- **Test:** access tests with test accounts; lockout tests; default-credential tests on analyzers (with vendor approval, outside testing hours); a network reachability test from the AQ-07 site network; a rogue device test at two patient service centers; TLS scans and a packet capture on the lab segment; malformed HL7 messages in the test environment; a restore observation.

## 4. Rules of engagement
- No testing could affect patient testing or result delivery. Analyzer tests ran during scheduled maintenance windows with the Laboratory Director's approval and a technologist present.
- Malformed message tests ran only in the validation environment.
- The rogue device test used an audit-owned laptop with no ePHI, pre-approved by the CISO and the site managers.
- No ePHI left the group's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor passwords on 3 analyzers (reported 2026-08-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Laboratory Services |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (263 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 228 |
| Other than satisfied | 35 |
| **Total** | **263** |

**Controls with at least one Other than satisfied statement: 26 of 44:** AC-2, AC-2(3), AC-5, AC-17, AU-6, AU-10, CM-2, CM-3, CM-6, CM-8, CP-2, CP-10, IA-5, IA-8, IR-4, IR-8, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SI-7, SI-7(1).

**Fully Other than satisfied:** AU-10, IA-8, SC-8 (each has a single determination statement).

**Themes:**
1. **Acquired-practice integration** drives the identity (AC-2, PS-4), monitoring (AU-6), network (SC-7), and incident handling (IR-4) findings.
2. **Result integrity** is the main system-specific weakness: separation of duties (AC-5), change control for autoverification rules (CM-3), attribution of autoverified results (AU-10), and result reconciliation (SI-7, SI-7(1)).
3. **Medical devices and analyzers:** unsupported components (SA-22, CM-6), patching (RA-5, SI-2), inventory (CM-8), vendor remote access (AC-17), and default credentials (IA-5).
4. **Disclosure readiness:** the SEC materiality step has not been exercised with the current disclosure committee (IR-8).

**Strengths:** identity and privileged access (IA-2, IA-2(1), AC-6), immutable logs and backups (AU-9, CP-9), vulnerability scanning cadence, workforce training, and message validation (SI-10) were all Satisfied.

**New finding during testing:** default vendor service passwords on 3 analyzers (IA-05e.). Added to the risk register as R-058 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 23 items: 18 from this assessment and 5 carried from the P03 gap analysis (POAM-019 to POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 11 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 16 |
| Open | 7 |

## 8. Conclusion
Internal Audit concludes that the LIS control environment is **effective with exceptions**. Enterprise common controls for identity, logging, backup, and monitoring operate effectively. The exceptions concentrate in result-integrity controls and in controls that depend on integrating the acquired practices. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
