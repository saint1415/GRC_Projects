# Security Assessment Plan and Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company) |
| System assessed | Associate Lifecycle and Payroll Platform (ALPP), CSC-SYS-ALPP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Administrative and Support and Waste Management and Remediation Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. Internal Audit did not rely on the SOX program's IT general control testing of the payroll engine; where both tested the same control, the results agreed |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also satisfies | Annual assessment for the ALPP authorization (P02 section 4.2); the inspection and quality assurance evidence for the electronic I-9 system (8 CFR 274a.2(e)(1)(iii)) for the controls tested here; independent assessment under POL-01 4.9 |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 6, AT 2, AU 3, CA 2, CM 4, CP 4, IA 5, IR 3, MP 1, PS 1, RA 2, SA 2, SC 3, SI 5, SR 1), 280 determination statements.** Every determination statement for each selected control was tested. Controls were selected because they:
- address the Very High and High risks in P01 (ransomware during the payroll window, associate account takeover, pay rule and pay file integrity, mass data theft, ACQ-1, client integrations);
- protect the records the law requires the firm to keep (Form I-9 audit trail and retention, E-Verify access, consumer report disposal);
- cover the High-baseline supplement for account takeover (AC-2(12)) from P02 section 6;
- are common controls the ALPP inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-008; R-057; R-007; E-Verify MOU Art. II.A.3 | Comprehensive | Comprehensive | 2,310 ALPP account events (2026-01-01 to 2026-06-30); 2,900 enterprise and 160 ACQ-1 terminations; about 1,100 E-Verify accounts; about 400 client integrations | 60 account events (random); 60 enterprise and 40 ACQ-1 terminations (stratified); 100% of E-Verify accounts and integrations (analytics) | 21 / 5 |
| AC-2(12) | R-001; R-013 | Focused | Comprehensive | About 41,000 associate and 1,900 staff bank changes (2026 H1) | 100% (analytics); 60 flagged associate changes reviewed | 1 / 1 |
| AC-3 | R-016; 8 CFR 274a.2(g)(1)(i) | Focused | Focused | About 9,800 workforce users | 25 users (random); 4 test accounts | 1 / 0 |
| AC-5 | R-018 | Comprehensive | Comprehensive | 38 users with the payroll configuration administrator role | 100% | 1 / 1 |
| AC-6 | R-048 | Focused | Focused | 2,640 PAM sessions to payroll engine servers and database | 25 sessions (random) | 1 / 0 |
| AC-17 | R-025 | Focused | Comprehensive | 3 remote access paths; 6 vendor support accounts | 100% | 4 / 0 |
| AT-2 | R-022 | Basic | Focused | 12,000 internal employees (about 9,800 ALPP users) | 60 training records (random); 6 months of simulation results | 10 / 0 |
| AT-3 | R-013; 8 CFR 274a.2(g)(1)(iii) | Focused | Focused | About 380 Associate Service Center agents; 650 onboarding specialists; 420 payroll staff | 25 records per group (random); 10 mystery-shopper calls | 7 / 2 |
| AU-2 | R-016; 8 CFR 274a.2(g)(1)(iv) | Focused | Focused | n/a (configuration) | 8 event types generated in test (bank change, pay rule change, release, export, I-9 change) | 6 / 0 |
| AU-6 | R-003; R-004; R-016 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 148 tier-1 log sources | 5 weeks (random); 100% of log sources | 1 / 2 |
| AU-12 | R-017; 8 CFR 274a.2(g)(1)(iv) | Focused | Comprehensive | 11 ALPP components | 100% | 2 / 1 |
| CA-2 | Annual assessment requirement (POL-01 4.9) | Basic | Focused | n/a | 2025 and 2026 assessments | 11 / 0 |
| CA-7 | Continuous monitoring (P02) | Focused | Basic | 6 monthly packages | 3 months (random) | 11 / 0 |
| CM-2 | R-002 | Focused | Focused | 6 payroll engine servers | 100% | 5 / 0 |
| CM-3 | R-018; R-032 | Comprehensive | Comprehensive | About 1,150 payroll configuration changes and 96 releases (2026 H1) | 40 configuration changes (random); 25 releases (random) | 8 / 2 |
| CM-6 | R-060 | Focused | Comprehensive | Payroll engine servers (6); on-site time clocks (140) | 100% of servers; 25 time clocks (random, 9 sites) | 5 / 1 |
| CM-8 | R-060 | Comprehensive | Comprehensive | About 15,650 endpoints; 140 time clocks | 60 devices traced (random, 6 sites) | 5 / 1 |
| CP-2 | R-005; R-002 | Comprehensive | Focused | n/a (plan) | Plan examined; 4 interviews | 22 / 2 |
| CP-4 | R-005 | Focused | Focused | 1 annual DR test | 100% | 5 / 0 |
| CP-9 | R-002; 8 CFR 274a.2(g)(1)(ii) | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-005 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-023 | Basic | Focused | About 9,800 workforce users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-023 | Focused | Comprehensive | 64 privileged ALPP accounts | 100% | 1 / 0 |
| IA-5 | R-007; R-060 | Focused | Comprehensive | About 400 integration keys; 140 time clocks | 100% of keys (analytics); 25 time clocks (with site approval) | 7 / 3 |
| IA-8 | R-001; R-062 | Focused | Comprehensive | About 310,000 associate accounts | 100% (configuration and analytics) | 0 / 1 |
| IA-12 | R-045; 8 CFR 274a.2(b)(1)(ii) | Focused | Focused | About 118,000 new associates (2026 H1) | 25 onboarding records (random) | 5 / 0 |
| IR-4 | R-002; R-004 | Focused | Focused | About 8,400 SOC cases; 5 ACQ-1 incidents (2026 H1) | 25 cases (random) plus all 5 ACQ-1 incidents | 12 / 1 |
| IR-6 | E-Verify MOU Art. II.A.16; state breach laws | Basic | Focused | About 8,400 cases; 20 staff interviews | 25 cases; 20 staff | 2 / 0 |
| IR-8 | R-010; SEC 8-K 1.05 | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 15 / 2 |
| MP-6 | 16 CFR 682.3; FAR 52.204-21(b)(1)(vii) | Basic | Focused | About 2,100 devices retired (2026 H1) | 25 devices traced to certificates | 4 / 0 |
| PS-4 | R-057 | Comprehensive | Comprehensive | 2,900 enterprise and 160 ACQ-1 terminations | 100 (same sample as AC-2) | 4 / 1 |
| RA-3 | Annual risk assessment (POL-01 4.3) | Focused | Basic | n/a | Assessment examined | 8 / 0 |
| RA-5 | R-049 | Focused | Focused | About 3,800 critical and high findings on ALPP and shared components | 60 findings (random) | 8 / 1 |
| SA-9 | R-006; R-015; R-021 | Focused | Comprehensive | 14 external services supporting the ALPP | 100% | 4 / 2 |
| SA-22 | R-011 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-012 | Comprehensive | Focused | n/a (architecture) | Test from a lobby kiosk at 2 legacy branches | 5 / 1 |
| SC-8 | R-019 | Basic | Focused | All ALPP interfaces | 100% | 1 / 0 |
| SC-28 | R-003 | Basic | Focused | n/a (configuration) | Configuration inspected | 1 / 0 |
| SI-2 | R-002 | Focused | Focused | 214 patches (2026 H1) | 25 patches (random) | 10 / 0 |
| SI-4 | R-003; R-001 | Focused | Focused | n/a | Bulk export test; rule review | 10 / 2 |
| SI-7 | R-019 | Comprehensive | Focused | n/a | Test alteration of a copy of a paycard funding file in the test environment | 4 / 2 |
| SI-10 | R-053 | Focused | Focused | 20 test SL-2 intake files | 100% in the test environment | 0 / 1 |
| SI-12 | R-020; 8 CFR 274a.2(b)(2)(i)(A); 16 CFR 682.3 | Focused | Comprehensive | SYS-01, SYS-02, and data platform records | 100% (queries) | 2 / 2 |
| SR-6 | R-021 | Focused | Comprehensive | 220 vendors with personal information | 100% (analytics) | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 (account events and enterprise terminations), AT-2, CM-8, RA-5, and the flagged bank changes for AC-2(12).
- **Key manual controls, populations of 50 to 250, or a stratum:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3 (pay rule changes, drawn from the population of about 1,150) and the ACQ-1 termination stratum.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AT-3 (per group), CP-9, IA-2, IA-12, IR-4, IR-6, MP-6, SI-2, and the time clock test for CM-6 and IA-5.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all E-Verify accounts against HR records, all client integration keys by age, all bank changes for anomaly scoring, all record ages against the retention schedule).
- **Stratification:** terminations were stratified so ACQ-1 (5% of the population, but the least controlled environment) got 40 items on top of 60 enterprise items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key payroll integrity control (AC-5, CM-3, SI-7) or a legally required records control (AU-12 for Form I-9) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

### What each test could show
The 2026 revisions of POL-01 to POL-05 (P06) were drafts during fieldwork; they were approved on 2026-09-10 and take effect on 2026-10-01. Internal Audit therefore tested each control as it operated under the 2025 policy set, which was in force (EV-029), and reviewed the draft 2026 statements for design only. Any statement the 2026 revision adds has not operated yet; its operation is tested at the 2027-03 follow-up. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control was in force during the period and was tested on samples, full populations or live systems | 277 (240 Satisfied, 37 Other than satisfied) |
| Design | The control is new (a draft 2026 policy statement); only its design was reviewed. Operation is tested at the 2027-03 follow-up | 0 (the draft statements were reviewed against the policy text, not scored as determination statements) |
| Not implemented | Nothing existed to test: integrity verification of bank and paycard files on the SFTP staging server (SI-07a.[03]), a defined action for an altered pay file (SI-07b.[03]), and a retention or purge rule for data platform extracts (SI-12[04]) | 3 |
| **Total** | | **280** |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each sample was drawn from. Populations came from the intake exports where the period allowed (for example identity governance and HCM records, EV-004 and EV-005, the change records, EV-025, and the vendor register, EV-045) and were refreshed to 2026-06-30 at kickoff.

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, E-Verify user lists, integration key inventory, payroll role matrix, change tickets and approvals, DR test report, backup reports, vulnerability scans, vendor register and SOC report reviews, retention schedule and record-age queries, the incident response plan and disclosure playbook, disclosure committee minutes.
- **Interview:** Senior Vice President, Payroll and Associate Services; Vice President, Payroll Technology; Payroll Engine Application Manager; Vice President, Employment Compliance; Director of Employment Eligibility Compliance; Vice President, Associate Service Center; Treasurer; Director of Security Operations; Director of Identity and Access Management; Director of Network and Endpoint Engineering; General Counsel; CFO; CISO; 20 randomly selected payroll, onboarding, and branch staff.
- **Test:** access tests with audit test accounts; an audit test export of 5,000 associate records (synthetic records in a test tenant mirrored to production monitoring); 10 mystery-shopper calls to the Associate Service Center using audit-owned test associate identities; a reachability test from lobby kiosks at 2 legacy branches; a default-credential test on 25 on-site time clocks (with site approval); alteration of a copy of a paycard funding file in the test environment; malformed SL-2 intake files in the test environment; a restore observation.

## 4. Rules of engagement
- No testing could delay or change a real payroll. File alteration and intake tests ran only in the test environment; the export test used synthetic records.
- Mystery-shopper calls used audit-owned test identities set up with the Senior Vice President, Payroll and Associate Services; no real associate account was changed, and test bank changes were reversed before any pay run.
- Time clock tests were run with the client site's approval during non-shift hours; settings were restored and the PIN issue was reported the same day.
- No associate or candidate personal information left the firm's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. Two were: default administrator PINs on 9 of 25 time clocks (reported 2026-08-06) and the undetected bulk export (reported 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Payroll Technology |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (280 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 240 |
| Other than satisfied | 40 |
| **Total** | **280** |

**Controls with at least one Other than satisfied statement: 25 of 44:** AC-2, AC-2(12), AC-5, AT-3, AU-6, AU-12, CM-3, CM-6, CM-8, CP-2, CP-10, IA-5, IA-8, IR-4, IR-8, PS-4, RA-5, SA-9, SA-22, SC-7, SI-4, SI-7, SI-10, SI-12, SR-6.

**Fully Other than satisfied:** IA-8, SI-10, SR-6 (each has a single determination statement).

**Themes:**
1. **Money moves on weak checks.** Associate authentication (IA-8), atypical-use monitoring (AC-2(12), SI-4), caller verification training (AT-3), separation of duties and change approval for pay rules (AC-5, CM-3), and pay file integrity (SI-7) all failed in ways that let wages be diverted. These map to four of the High risks in P01 (R-001, R-013, R-018, R-019).
2. **Detection gaps for data theft.** A 5,000-record test export went unnoticed (AU-6, SI-4), and records past retention enlarge what a thief could take (SI-12).
3. **Acquisition integration.** ACQ-1 drives the termination (AC-2, PS-4), logging (AU-6), and incident handling (IR-4) findings.
4. **Records the law requires.** The scanned I-9 archive has no audit trail (AU-12), and E-Verify access is outside the termination process (AC-2).
5. **Disclosure readiness.** The SEC materiality step has not been updated or exercised for the new disclosure committee members (IR-8).

**Strengths:** workforce and privileged authentication (IA-2, IA-2(1)), access enforcement for Form I-9 images and consumer reports (AC-3), identity proofing at onboarding (IA-12), backups (CP-9), the DR test program itself (CP-4), payroll engine patching (SI-2), encryption and tokenization inside the payroll engine (SC-28), media disposal (MP-6), and independent assessment and monitoring (CA-2, CA-7) were all Satisfied.

**New finding during testing:** the vendor default administrator PIN on 9 of 25 sampled on-site time clocks (IA-05e., CM-06b.). Added to the risk register as R-060 and to POAM-024.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment and 5 carried from the P03 gap analysis (POAM-004, POAM-014, POAM-021, POAM-022, POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 12 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

## 8. Conclusion
Internal Audit concludes that the ALPP control environment is **effective with exceptions**. Enterprise common controls for identity, logging infrastructure, backup, patching, and encryption operate effectively. The exceptions concentrate in the controls that stand between a criminal and an associate's paycheck, in detection of bulk data theft, and in controls that depend on integrating ACQ-1. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
