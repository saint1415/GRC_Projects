# Security Assessment Plan and Report: Cris Santos Company | Healthcare and Public Health | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| System assessed | Enterprise Clinical Information System (ECIS), CSC-SYS-ECIS-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Healthcare and Public Health |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. A clinical auditor (a registered nurse in Internal Audit) observed downtime and diversion procedures. The GRC team (second line) supported scoping only |
| Assessment window | 2026-06-22 to 2026-08-07 (fieldwork); report issued 2026-08-14; presented to the audit committee and the risk committee on 2026-09-15 |
| Also satisfies | HIPAA evaluation (45 CFR 164.308(a)(8)); annual assessment for the ECIS authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 6, AT 2, AU 5, CA 1, CM 5, CP 4, IA 4, IR 3, MA 1, PS 2, RA 2, SA 2, SC 4, SI 5), 289 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware and cyber recovery, H-08, service accounts, medical devices, diversion readiness);
- cover HIPAA Required implementation specifications and hospital conditions with gaps in P03;
- protect record integrity (CMS 482.24(b); CLIA 493.1291(a)) and Part 2 records;
- are common controls the ECIS inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-012; R-013; 164.308(a)(3)(ii)(C) | Comprehensive | Comprehensive | 2,960 departures of staff with EHR access (1,610 agency or contracted); 1,840 access requests; about 1,150 service accounts | 60 departures (stratified: 30 employees, 30 agency or contracted); 60 access requests (random); 100% of service accounts (vault analytic) | 22 / 4 |
| AC-2(3) | R-030 | Focused | Comprehensive | 19,500 workforce and 1,450 affiliate accounts | 100% (data analytic) | 3 / 1 |
| AC-3 | R-016; 482.24(b)(3) | Focused | Focused | About 19,000 workforce EHR users | 25 users (random) tested against role templates | 1 / 0 |
| AC-5 | R-027; 482.24(b) | Comprehensive | Comprehensive | 38 users with build or migration roles | 100% | 2 / 0 |
| AC-6 | R-047 | Focused | Focused | 2,410 PAM elevation sessions to ECIS servers and databases | 25 sessions (random) | 1 / 0 |
| AC-17 | R-011; R-052 | Focused | Comprehensive | 7 remote access paths (workforce, affiliate, EHR vendor, 4 device and analyzer vendor paths) | 100% | 3 / 1 |
| AT-2 | R-021; 164.308(a)(5) | Basic | Focused | 12,000 employees plus agency staff | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-058; 482.15(d)(1) | Focused | Focused | About 3,900 charge nurses, ED staff, and unit clerks | 60 training records (stratified by hospital) | 7 / 2 |
| AU-2 | R-014; R-041 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-014; R-041; 164.308(a)(1)(ii)(D) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 214 log sources on clinical data paths | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-047 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested with an administrator account | 2 / 0 |
| AU-10 | R-027; 482.24(c)(1) | Focused | Focused | About 9.4 million signed notes, orders, and verifications in the period | 25 signed entries (random) | 1 / 0 |
| AU-12 | R-041 | Basic | Focused | n/a (configuration) | 6 ECIS servers and 2 integration engine nodes | 3 / 0 |
| CA-7 | 164.308(a)(8) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-046 | Focused | Focused | About 60 ECIS servers | 20 servers (random) | 5 / 0 |
| CM-3 | R-027; 482.24(b) | Comprehensive | Comprehensive | 1,262 ECIS change records (2026-01-01 to 2026-06-30), 184 of them emergency changes | 40 emergency changes (random); 25 standard changes (random) | 8 / 2 |
| CM-5 | R-027 | Focused | Focused | 1,262 changes | 10 changes traced to PAM sessions | 6 / 0 |
| CM-6 | R-056 | Focused | Comprehensive | 16 clinical device integration gateways; 20 ECIS servers | 100% of gateways; 20 servers (same sample as CM-2) | 4 / 2 |
| CM-8 | R-007 | Comprehensive | Comprehensive | About 41,000 networked medical devices; about 900 BCA computers | 60 devices traced from the floor to the inventory (random, 8 hospitals); 100% of BCA computers | 5 / 1 |
| CP-2 | R-001; R-004; R-009 | Comprehensive | Focused | n/a (plan) | ECIS contingency plan v6 examined; 5 interviews | 21 / 3 |
| CP-4 | R-004; R-009 | Focused | Focused | 2 tests in the period (failover 2026-03-21; restore 2026-04-18) | 100% | 4 / 1 |
| CP-9 | R-001 | Focused | Focused | 182 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-004 | Focused | Focused | 2 recovery tests | 100% | 1 / 1 |
| IA-2 | R-021 | Basic | Focused | About 19,000 workforce users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-047 | Focused | Comprehensive | 22 privileged ECIS accounts | 100% | 1 / 0 |
| IA-5 | R-012; R-056 | Focused | Comprehensive | About 1,150 service accounts; 16 device integration gateways | 100% (vault analytic); 100% of gateways (tested with vendor approval, after hours) | 8 / 2 |
| IA-8 | R-030 | Focused | Comprehensive | 1,450 affiliate accounts | 100% (data analytic) | 0 / 1 |
| IR-4 | R-001 | Focused | Focused | 388 security incidents | 25 incidents (random) | 13 / 0 |
| IR-6 | R-001 | Basic | Focused | 388 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-015 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with the General Counsel, CFO, COO, CISO | 15 / 2 |
| MA-4 | R-011 | Focused | Comprehensive | 4 vendor remote maintenance paths for devices and analyzers | 100% | 6 / 2 |
| PS-4 | R-013 | Comprehensive | Comprehensive | 2,960 departures | 60 (same sample as AC-2) | 4 / 1 |
| PS-7 | R-013 | Focused | Focused | 42 staffing agency contracts | 10 contracts (random) | 3 / 2 |
| RA-3 | 164.308(a)(1)(ii)(A) | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-057 | Focused | Focused | 2,318 vulnerability findings on ECIS components | 60 critical and high findings (random) | 8 / 1 |
| SA-9 | R-019 | Focused | Comprehensive | 17 external services supporting the ECIS | 100% | 5 / 1 |
| SA-22 | R-006 | Focused | Comprehensive | Unsupported component list (about 2,600 devices system-wide; 140 that feed the ECIS) | 100% of the 140 that feed the ECIS | 1 / 1 |
| SC-4 | R-016; 2.16(a)(1)(ii) | Focused | Focused | 1,140 Part 2 encounters | 60 (random) | 1 / 1 |
| SC-7 | R-003 | Comprehensive | Focused | n/a (architecture) | Reachability test from the H-08 network to the integration engine and ECIS tiers | 5 / 1 |
| SC-8 | R-059 | Basic | Focused | About 640 interfaces | 100% (TLS scan) | 1 / 0 |
| SC-28 | R-025 | Basic | Focused | n/a (configuration) | Database, backup, and BCA cache encryption inspected | 1 / 0 |
| SI-2 | R-057 | Focused | Focused | 264 patches on ECIS servers | 25 patches (random) | 9 / 1 |
| SI-3 | R-001 | Basic | Focused | ECIS servers and BCA computers | 20 servers and 25 BCA computers (random) | 8 / 0 |
| SI-4 | R-014; R-041 | Focused | Focused | 61 sites; 214 clinical-path log sources | Detection test on 2 device segments (H-02, H-06); 100% of sources | 10 / 2 |
| SI-7 | R-026; 493.1291(a) | Comprehensive | Focused | n/a | File integrity monitoring and result integrity controls examined; 60 results traced end to end | 4 / 2 |
| SI-10 | R-026 | Focused | Focused | 20 malformed test messages | 100% in the test environment | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-3, CM-8, RA-5, and SC-4.
- **Key manual controls with smaller or riskier populations:** 40 items for emergency changes (CM-3), the population most likely to bypass review.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AU-10, CP-9, IA-2, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 1,150 service accounts for vaulting, all 1,450 affiliate accounts for inactivity, all 16 device gateways for default credentials).
- **Stratification:** departures were stratified so agency and contracted staff (54% of the population) got 30 of 60 items; device traces covered all 8 hospitals.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key patient-safety control (CM-3, AC-5, AU-10, SI-7, SC-4) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

### What each test could show
The 2026 revisions of POL-01 to POL-05 (P06) were drafts during fieldwork; POL-02 to POL-05 were approved on 2026-08-24 and POL-01 on 2026-09-15, and the set takes effect on 2026-10-01. Internal Audit therefore tested each control as it operated under the policy hierarchy in force (EV-028), and reviewed the draft 2026 statements for design only. Any statement the 2026 revision adds has not operated yet; its operation is tested at the 2027-03 follow-up. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control was in force during the period and was tested on samples, full populations or live systems | 286 (250 Satisfied, 36 Other than satisfied) |
| Design | The control is new (a draft 2026 policy statement); only its design was reviewed. Operation is tested at the 2027-03 follow-up | 0 (the draft statements were reviewed against the policy text, not scored as determination statements) |
| Not implemented | Nothing existed to test: detection of results misfiled or changed between analyzer and chart (SI-07a.[03]), a defined response to such changes (SI-07b.[03]), and monitoring of staffing agency compliance with security terms (PS-07e.) | 3 |
| **Total** | | **289** |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each sample was drawn from. Populations came from the intake exports where the period allowed (for example the PAM and identity governance records, EV-003 and EV-004, the HR and staffing records, EV-005 and EV-006, and the ECIS change records, EV-057) and were refreshed to 2026-06-30 at kickoff.

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, EHR security class matrix and audit trails, change records, backup and recovery test reports, vulnerability scans, the vendor register, the incident response plan, materiality playbook, and disclosure committee minutes, the unified emergency plan and downtime procedures.
- **Interview:** Vice President, Clinical Applications; EHR Technical Director; Chief Nursing Officer; Chief Medical Information Officer; Director of Security Operations; Director of Identity and Access Management; Director of Clinical Engineering; Vice President, Emergency Management; General Counsel; CFO; COO; CISO; 20 randomly selected nurses and ED staff.
- **Test:** access tests with test accounts; a deletion attempt on the log archive; credential tests on device integration gateways (with vendor approval, after hours); a reachability test from the H-08 network; a detection test with an audit-owned device on two device segments; TLS scans; malformed HL7 messages in the test environment; a restore observation; an end-to-end trace of 60 laboratory results.

## 4. Rules of engagement
- No testing could affect patient care. Device gateway tests ran in maintenance windows with clinical engineering and a charge nurse present, and the Chief Nursing Officer's approval.
- Malformed message tests ran only in the test environment.
- The detection test used an audit-owned laptop with no ePHI, pre-approved by the CISO and the hospital presidents.
- No ePHI left the system's environment. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor passwords on 2 device integration gateways (reported 2026-07-29; passwords changed 2026-08-05).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-06-22 | Kickoff; document requests |
| 2026-06-29 to 2026-07-31 | Fieldwork (examine, interview, test) |
| 2026-08-03 to 2026-08-07 | Finding validation with control owners |
| 2026-08-14 | Report issued to the COO, CISO, and Vice President, Clinical Applications |
| 2026-09-15 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (289 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 250 |
| Other than satisfied | 39 |
| **Total** | **289** |

**Controls with at least one Other than satisfied statement: 25 of 46:** AC-2, AC-2(3), AC-17, AT-3, AU-6, CM-3, CM-6, CM-8, CP-2, CP-4, CP-10, IA-5, IA-8, IR-8, MA-4, PS-4, PS-7, RA-5, SA-9, SA-22, SC-4, SC-7, SI-2, SI-4, SI-7.

**Fully Other than satisfied:** IA-8 (single determination statement).

**Themes:**
1. **Recovery and downtime at scale** drive the contingency findings: the cyber restore misses its target (CP-10), and the plan and tests do not cover several hospitals in downtime with diversion decisions (CP-2, CP-4, AT-3).
2. **Identity hygiene outside employees:** service accounts (AC-2, IA-5), agency staff (AC-2, PS-4, PS-7), and affiliate users (AC-2(3), IA-8).
3. **Medical devices and vendors:** unsupported devices (SA-22, CM-6), inventory (CM-8), vendor remote tools (AC-17, MA-4), and default credentials on device gateways (IA-5).
4. **H-08:** network reachability (SC-7) and missing monitoring (AU-6, SI-4).
5. **Record integrity:** emergency build changes (CM-3), result reconciliation (SI-7), and Part 2 flagging (SC-4).
6. **Disclosure readiness:** the materiality step is not tuned for H-08 or connected to hospital incident command (IR-8).

**Strengths:** privileged access and MFA (AC-6, IA-2, IA-2(1)), separation of build and migration (AC-5), signatures and audit generation (AU-10, AU-12), immutable logs and backups (AU-9, CP-9), encryption at rest and in transit (SC-28, SC-8), malware protection (SI-3), and message validation (SI-10) were all Satisfied.

**New finding during testing:** default vendor passwords on 2 of 16 device integration gateways (IA-05e.). Added to the risk register as R-056 and to POAM-010.

## 7. POA&M summary
`poam.csv` holds 24 items: 18 from this assessment (POAM-001 to POAM-017, and POAM-021, which also closes P03 gaps), and 6 carried from the P03 gap analysis, the P01 register, or P10 (POAM-018 to POAM-020 and POAM-022 to POAM-024), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 13 |
| Moderate | 11 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

## 8. Conclusion
Internal Audit concludes that the ECIS control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, backup, encryption, and malware protection operate effectively. The exceptions concentrate in cyber recovery, downtime and diversion readiness at scale, identities that sit outside the employee lifecycle, medical devices, and H-08. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
