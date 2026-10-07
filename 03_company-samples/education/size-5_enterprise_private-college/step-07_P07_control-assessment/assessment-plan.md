# Security Assessment Plan and Report: Cris Santos Company | Educational Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company operating a private, for-profit college) |
| System assessed | Student Records and Learning Platform (SRLP), CSC-SYS-SRLP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Educational Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the board risk committee on 2026-09-10 |
| Also satisfies | Regular testing of key controls (16 CFR 314.4(d)(1)); annual assessment for the SRLP authorization (P02 section 4.2); input to the Qualified Individual's annual report (314.4(i)(2)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **45 controls (AC 9, AT 2, AU 5, CA 2, CM 4, CP 4, IA 4, IR 3, PS 1, PT 1, RA 2, SA 2, SC 3, SI 3), 268 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware, refund fraud, help desk MFA resets, FAFSA data use, legacy imaging, recovery time);
- cover Safeguards Rule elements and FERPA requirements with gaps in P03;
- include the High-baseline supplements and tailored additions in P02 section 6 (AC-2(12), CA-8, PT-3);
- are common controls the SRLP inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-005; 314.4(c)(1)(i); 99.31(a)(1)(ii) | Comprehensive | Comprehensive | 3,940 SRLP account events; 1,410 adjunct separations and 2,860 other separations of staff with SRLP access (2026-01-01 to 2026-06-30) | 60 account events (random); 60 adjunct separations (random); 25 other separations (random) | 22 / 4 |
| AC-2(3) | R-005 | Focused | Comprehensive | About 9,400 workforce SRLP accounts | 100% (data analytic) | 3 / 1 |
| AC-2(12) | R-017; R-002 | Focused | Focused | SIEM use cases for SRLP accounts | Use case catalog in full; 1 test export of 50,000 records | 1 / 1 |
| AC-3 | R-009 | Focused | Focused | About 9,400 workforce SRLP accounts | 25 users (random) | 1 / 0 |
| AC-4 | R-008; HEA section 483 | Comprehensive | Comprehensive | 34 SRLP integration routes | 100% | 0 / 1 |
| AC-5 | 314.4(c)(1); 34 CFR 668.16(c)(2) | Comprehensive | Comprehensive | 640 financial aid and 210 student finance users | 100% (data analytic) | 2 / 0 |
| AC-6 | R-009; 99.31(a)(1)(ii) | Comprehensive | Comprehensive | 2,100 enrollment advisor accounts | 100% (data analytic) | 0 / 1 |
| AC-6(9) | R-040 | Focused | Focused | 2,240 PAM sessions to SIS servers and database | 25 sessions (random) | 1 / 0 |
| AC-17 | R-040; 314.4(c)(5) | Focused | Comprehensive | 3 remote access paths; 14 SIS vendor support sessions | 100% | 4 / 0 |
| AT-2 | R-062; 314.4(e)(1) | Basic | Focused | 12,000 workforce | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-018; 314.4(e)(1) | Focused | Comprehensive | 640 financial aid staff with Department access; 11 SIS security administrators; 9 disclosure committee members | 100% (data analytic) | 8 / 1 |
| AU-2 | R-017; 314.4(c)(8) | Focused | Focused | 5 event types | 5 event types generated in test | 6 / 0 |
| AU-6 | R-054; 314.4(c)(8) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 41 SRLP-related log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | R-057 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-054 | Basic | Focused | 6 SIS servers; 2 SAIG servers; portal back end | 100% | 3 / 0 |
| CA-7 | 314.4(d)(1) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CA-8 | 314.4(d)(2)(i) | Focused | Focused | 1 annual test | 100% | 1 / 0 |
| CM-2 | R-024 | Focused | Focused | 6 SIS servers; 2 SAIG servers; portal images | 100% | 5 / 0 |
| CM-3 | R-024; 314.4(c)(7) | Comprehensive | Comprehensive | 212 SRLP changes (2026-01-01 to 2026-06-30), 58 emergency | 40 emergency changes (random) | 8 / 2 |
| CM-6 | R-021; R-007 | Focused | Comprehensive | 8 SRLP servers; 31 processing-center scanners; imaging system | 100% | 5 / 1 |
| CM-8 | R-021; 314.4(c)(2) | Comprehensive | Comprehensive | About 1,950 SRLP-related components | 60 components traced (random) | 5 / 1 |
| CP-2 | R-010; R-011; 314.4(h) | Comprehensive | Focused | n/a (plan) | Plan examined; 4 interviews | 22 / 2 |
| CP-4 | R-010 | Focused | Focused | 1 annual DR test | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-010 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-004 | Basic | Focused | About 9,400 workforce SRLP accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-040 | Focused | Comprehensive | 34 privileged SRLP accounts | 100% | 1 / 0 |
| IA-5 | R-004; R-021 | Focused | Comprehensive | 2,950 help desk MFA resets (2026-01 to 2026-06); 31 scanners | 25 resets (random); 100% of scanners | 8 / 2 |
| IA-8 | R-003; 314.4(c)(5) | Focused | Comprehensive | About 285,000 student accounts | 100% (configuration) | 0 / 1 |
| IR-4 | R-060 | Focused | Focused | 212 incidents (2025-07 to 2026-06), 38 vendor-originated | 25 vendor-originated incidents (random); 15 other incidents (random) | 11 / 2 |
| IR-6 | R-055; 314.4(j) | Basic | Focused | 212 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-013; 314.4(h) | Comprehensive | Focused | n/a (plan) | Plan examined; 4 interviews | 15 / 2 |
| PS-4 | R-005 | Comprehensive | Comprehensive | 1,410 adjunct separations; 2,860 other separations | 60 adjunct and 25 other separations (same samples as AC-2) | 4 / 1 |
| PT-3 | R-008; HEA section 483 | Comprehensive | Comprehensive | 17 data platform data sets with student data | 100% (catalog analytic) | 4 / 2 |
| RA-3 | 314.4(b) | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-023; 314.4(d)(2)(ii) | Focused | Focused | 1,212 vulnerability findings on SRLP hosts (2026-01 to 2026-06) | 60 findings (random) | 8 / 1 |
| SA-9 | R-012; 314.4(f) | Focused | Comprehensive | 14 external services supporting the SRLP; enterprise register of 260 vendors with student data | 100% of the 14 services; register analytic | 4 / 2 |
| SA-22 | R-007 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-019 | Comprehensive | Focused | n/a (architecture) | Test from the integration subnet | 5 / 1 |
| SC-8 | 314.4(c)(3) | Basic | Focused | All SRLP interfaces | 100% (TLS scan) | 1 / 0 |
| SC-28 | 314.4(c)(3) | Basic | Focused | n/a (configuration) | Settings inspected | 1 / 0 |
| SI-2 | R-023 | Focused | Focused | Security patches for SRLP hosts (2026-01 to 2026-06) | 25 patches (random) | 9 / 1 |
| SI-4 | R-017 | Focused | Focused | SIEM use case catalog | Catalog in full; 1 test export | 11 / 1 |
| SI-12 | R-020; 314.4(c)(6) | Focused | Comprehensive | SIS records of about 3.4 million former students | 100% (data analytic) | 2 / 2 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (58 emergency changes).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6(9), CP-9, IA-2, IA-5 (help desk resets), IR-4 (vendor-originated incidents), IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 9,400 workforce accounts for inactivity, all 2,100 enrollment advisor role assignments, all 17 data platform data sets, all 31 scanners for default credentials).
- **Stratification:** separations were split into adjunct contract ends (60 items) and other separations (25 items), because the adjunct process is different and higher risk.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key control over student funds or customer information (AC-5, IA-8, AC-4, PT-3) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, SIS role matrix and audit trails, integration route field lists, the data platform catalog and data use register, change tickets, backup and DR test reports, vulnerability scans and patch records, vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Enterprise Applications; SIS Application Manager; University Registrar; Vice President, Financial Aid; Vice President, Student Finance; Chief Data and Analytics Officer; Director of Academic Technology; Director of Security Operations; Director of Identity and Access Management; General Counsel; CFO; CISO; 20 randomly selected staff.
- **Test:** access tests with audit test accounts; a bulk report export test (50,000 test records); a refund bank-change flow test with an audit test student account; default-credential tests on scanners (with vendor approval, after hours); a reachability test from the integration subnet to the SAIG servers; TLS scans; a log deletion attempt; a restore observation.

## 4. Rules of engagement
- No testing could affect registration, aid processing, refunds, or SAIG transmissions. SAIG reachability tests used only management ports and ran outside transmission windows with the Vice President, Financial Aid's approval.
- The refund flow test used an audit test student account with no real bank details and no payment.
- The bulk export test used synthetic records in the validation environment and one production report limited to audit test accounts.
- No customer information or education records left the company's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor passwords on 4 scanners in the financial aid processing center (reported 2026-08-12; passwords changed 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Operating Officer, the CISO, and the Vice President, Enterprise Applications |
| 2026-09-10 | Presented to the audit committee and the board risk committee |

Deliverables: this plan and report, `assessment-results.csv` (268 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 232 |
| Other than satisfied | 36 |
| **Total** | **268** |

**Controls with at least one Other than satisfied statement: 25 of 45:** AC-2, AC-2(3), AC-2(12), AC-4, AC-6, AT-3, AU-6, CM-3, CM-6, CM-8, CP-2, CP-10, IA-5, IA-8, IR-4, IR-8, PS-4, PT-3, RA-5, SA-9, SA-22, SC-7, SI-2, SI-4, SI-12.

**Fully Other than satisfied:** AC-4, AC-6, IA-8 (each has a single determination statement).

**Themes:**
1. **Identity at the edges** drives the account management findings: adjunct contract ends (AC-2, AC-2(3), PS-4), help desk MFA resets (IA-5), student authentication and refund bank changes (IA-8), and enrollment advisor access (AC-6).
2. **Student financial data used outside its purpose:** ISIR-derived fields flow to the data platform (AC-4, PT-3), and former students' records are never disposed of (SI-12).
3. **Legacy and recovery:** the unsupported imaging system (SA-22), missing logs (AU-6), the SIS recovery time (CP-10, CP-2), and the LMS contingency gap (CP-2).
4. **Disclosure readiness:** the materiality playbook omits Title IV consequences and was not exercised with the current disclosure committee (IR-8).

**Strengths:** workforce SSO with MFA and privileged access (IA-2, IA-2(1), AC-6(9), AC-17), separation of awarding and disbursing (AC-5), immutable logs and backups (AU-9, CP-9), encryption (SC-8, SC-28), the annual independent penetration test (CA-8), continuous monitoring (CA-7), and the risk assessment (RA-3) were all Satisfied.

**New finding during testing:** default vendor administrator passwords on 4 scanners in the financial aid processing center (IA-05e.), with 3 scanners missing from the CMDB (CM-08a.02). Added to the risk register as R-021 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 24 items: 18 from this assessment (POAM-001 to POAM-018) and 6 carried from the P03 gap analysis, the P09 readiness review, and the P10 AI assessment (POAM-019 to POAM-024), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 12 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the SRLP control environment is **effective with exceptions**. Enterprise common controls for workforce identity, logging, backup, encryption, testing, and monitoring operate effectively. The exceptions concentrate in identity processes at the edges (adjuncts, students, help desk), in the use and retention of student financial data, and in legacy and recovery dependencies. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2.
