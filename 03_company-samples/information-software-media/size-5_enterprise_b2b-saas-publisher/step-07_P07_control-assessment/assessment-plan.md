# Security Assessment Plan and Report: Cris Santos Company | Information | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher) |
| System assessed | Operations Cloud Production Platform (OCP), CSC-SYS-OCP-001, per the SSP (P02), including the enterprise common controls it inherits and the AQ-01 side of its export interconnection |
| Tier / Vertical | Enterprise / Information |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The two IT auditors who helped design the GRC control framework in 2025 were not assigned to controls in that framework's scope (AC, IA, CM). The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the cybersecurity and risk committee on 2026-09-10 |
| Also supports | Annual assessment for the OCP authorization (P02 section 4.2); SOC 2 readiness evidence (P09); CCPA cybersecurity audit readiness (P03 G-057) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 2, AU 6, CA 2, CM 4, CP 4, IA 3, IR 3, PS 1, RA 2, SA 1, SC 5, SI 4), 270 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (credential compromise, AQ-01 integration, support access, tenant isolation, secrets);
- test the commitments behind the deception gaps in P03 (support access, recording, deletion, notice);
- are common controls the OCP inherits and that no other assessment covered this year;
- support the SOC 2 service auditor's reliance and the CCPA cybersecurity audit components (Cal. Code Regs. tit. 11, 7123(c)).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-030; R-040 | Comprehensive | Comprehensive | 1,640 OCP account events (2026-01-01 to 2026-06-30); 1,312 contractor and vendor-agent departures; about 46,000 non-human identities | 60 account events (random); 60 departures (random); non-human identities 100% (access analyzer) | 22 / 4 |
| AC-2(3) | R-040 | Focused | Comprehensive | About 1,100 workforce accounts with OCP roles | 100% (data analytic) | 4 / 0 |
| AC-3 | R-004; R-005 | Comprehensive | Comprehensive | 41,200 tenant access sessions (2026 H1); isolation test suite | 60 sessions (random); isolation test with two auditor test tenants | 0 / 1 |
| AC-5 | R-004 | Focused | Comprehensive | Branch protection on 412 OCP repositories; tool approval rules | 100% (configuration analytic) | 2 / 0 |
| AC-6 | R-030; R-002 | Focused | Comprehensive | Non-human identities in OCP accounts; export bucket principals | 100% (access analyzer); export bucket policy | 0 / 1 |
| AC-6(9) | R-004 | Basic | Focused | 1,850 PAM elevations to OCP production | 25 elevations (random) | 1 / 0 |
| AC-17 | R-009 | Focused | Comprehensive | Remote access paths to production (zero-trust gateway only) | 100% | 4 / 0 |
| AT-2 | R-029; R-033 | Basic | Focused | 12,000 workforce | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-054 | Focused | Focused | About 4,300 engineers; about 600 support engineers with tenant access | 60 engineers (random); 25 support engineers (random) | 8 / 1 |
| AU-2 | R-001 | Focused | Focused | n/a (configuration) | 7 event types generated in test | 6 / 0 |
| AU-6 | R-002; R-051 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 63 OCP log sources; export bucket access logs | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-001 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested with an auditor role | 2 / 0 |
| AU-10 | R-004; R-020 | Focused | Comprehensive | 41,200 tenant access sessions | 100% (log analytic) | 0 / 1 |
| AU-11 | R-051 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-001 | Basic | Focused | n/a (configuration) | 6 OCP services, 2 data stores, the tenant access tool, and the export service | 3 / 0 |
| CA-3 | R-002; R-003 | Comprehensive | Comprehensive | 4 interconnections (Data Cloud, AQ-01, Government Edition, model providers) | 100% | 5 / 3 |
| CA-7 | N51-R08 (Item 106 continuous monitoring) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-3 | R-037 | Comprehensive | Comprehensive | 1,980 OCP production changes (2026 H1), 142 of them emergency changes | 40 normal changes (random); 40 emergency changes (random) | 8 / 2 |
| CM-5 | R-037 | Focused | Focused | 1,980 changes | 10 changes traced to pipeline roles and PAM | 6 / 0 |
| CM-6 | R-058; R-012 | Focused | Comprehensive | OCP accounts; AQ-01 accounts on the export interconnection | Benchmark reports for all OCP accounts; posture scan of the AQ-01 organization | 5 / 1 |
| CM-8 | R-056 | Comprehensive | Comprehensive | About 86,000 OCP cloud resources | 60 resources traced to the inventory (random) | 5 / 1 |
| CP-2 | R-016; R-041 | Comprehensive | Focused | n/a (plan) | Plan v7 examined; 3 interviews | 22 / 2 |
| CP-4 | R-008 | Focused | Focused | 14 cell DR tests (2026-05-16) | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs per cell (2026 H1) | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-008 | Focused | Focused | 14 cell DR tests | 100% | 1 / 1 |
| IA-2 | R-029 | Basic | Focused | About 1,100 workforce accounts with OCP roles | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-001 | Focused | Comprehensive | 214 privileged OCP roles | 100% | 1 / 0 |
| IA-5 | R-001; R-007 | Focused | Comprehensive | OCP pipeline credentials; OCP repositories | 100% (key inventory and secret scanning analytics) | 8 / 2 |
| IR-4 | R-001 | Focused | Focused | 184 security incidents touching the OCP (2026 H1) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-018; R-019 | Basic | Focused | 184 incidents; 20 staff interviews | 25 incidents; 20 staff | 1 / 1 |
| IR-8 | R-017; R-019; R-059 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, CISO, and Chief Customer Officer | 14 / 3 |
| PS-4 | R-040 | Comprehensive | Comprehensive | 1,312 contractor and vendor-agent departures; 418 employee terminations with OCP roles | 60 departures (random; same sample as AC-2); 25 employee terminations (random) | 4 / 1 |
| RA-3 | N51-R08 (Item 106(b)(1)) | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-035 | Focused | Focused | 2,410 critical and high findings on OCP images (2026 H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-014; R-031 | Focused | Comprehensive | 58 sub-processors | 100% | 4 / 2 |
| SC-4 | R-005; R-006 | Focused | Focused | Shared caches, queues, and the search cluster | Isolation tests run with auditor test tenants | 2 / 0 |
| SC-7 | R-042; R-048 | Comprehensive | Focused | n/a (architecture) | Edge inventory and external scan | 5 / 1 |
| SC-8 | R-001 | Basic | Focused | All external OCP endpoints | 100% (TLS scan) | 1 / 0 |
| SC-12 | R-055 | Focused | Focused | About 9,800 tenant keys plus service keys | 25 keys (random) | 1 / 1 |
| SC-28 | R-001 | Basic | Focused | n/a (configuration) | Database, object storage, and backup encryption inspected | 1 / 0 |
| SI-2 | R-035 | Focused | Focused | 2,410 findings (same population as RA-5) | 60 (same sample as RA-5) | 9 / 1 |
| SI-4 | R-001; R-002 | Focused | Focused | SIEM use cases; 5 OCP data stores; export path | Use case list; bulk-read simulation on the export path with an auditor role | 10 / 2 |
| SI-10 | R-026 | Focused | Focused | AI Assist prompt construction; 6 red-team findings | 20 injection test cases in the validation environment | 0 / 1 |
| SI-12 | R-023 | Comprehensive | Comprehensive | 412 tenants terminated in 12 months | 100% (data analytic) | 3 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, AC-3, AT-2, AT-3 (engineers), CM-8, PS-4, RA-5, and SI-2.
- **Change management:** 40 normal changes and 40 emergency changes, random selection, from Internal Audit's methodology table for the emergency change population (142) and as a second stratum for normal changes. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-6(9), CP-9, IA-2, IR-4, IR-6, and SC-12.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Data-analytic tests (100% of the population):** account inactivity (AC-2(3)), non-human identity permissions (AC-2, AC-6), recording coverage (AU-10), secret scanning and key inventory (IA-5), terminated tenant deletion (SI-12), and TLS (SC-8).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key tenant data control (AC-3, AU-10, SI-12) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, tenant access tool logs and recordings, change records, backup and DR test reports, vulnerability and secret scans, the vendor register and SOC report reviews, the interconnection register, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Platform Engineering; Vice President, Site Reliability Engineering; Vice President, Customer Support; Director of Identity and Access Management; Director of Security Operations; Director of Product Security; Director of Third-Party Risk Management; Chief Product Officer; General Counsel; CFO; CISO; Chief Customer Officer; 20 randomly selected engineers and support staff.
- **Test:** cross-tenant access attempts with two auditor test tenants; isolation tests on shared resources; a reachability test from a non-compliant device; a log deletion attempt; a bulk-read simulation on the export path; a posture scan of the AQ-01 organization; AI Assist injection tests in the validation environment; an external scan of the edge; a restore observation.

## 4. Rules of engagement
- No testing could affect customer tenants or production availability. Isolation and injection tests used auditor-owned test tenants in production and the validation environment; the bulk-read simulation used synthetic objects placed in the export bucket for the test.
- No customer data left the company's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: the publicly readable AQ-01 CI build log bucket with a static access key in one log (reported 2026-08-12; the key was revoked and the bucket made private on 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the CTO, CISO, and Vice President, Platform Engineering |
| 2026-09-10 | Presented to the audit committee and the cybersecurity and risk committee |

Deliverables: this plan and report, `assessment-results.csv` (270 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 234 |
| Other than satisfied | 36 |
| **Total** | **270** |

**Controls with at least one Other than satisfied statement: 24 of 44:** AC-2, AC-3, AC-6, AT-3, AU-6, AU-10, CA-3, CM-3, CM-6, CM-8, CP-2, CP-10, IA-5, IR-6, IR-8, PS-4, RA-5, SA-9, SC-7, SC-12, SI-2, SI-4, SI-10, SI-12.

**Fully Other than satisfied:** AC-3, AC-6, AU-10, SI-10 (each has a single determination statement).

**Themes:**
1. **The AQ-01 interconnection** is the weakest point: no agreement or requirements for the export (CA-3), no review of reads (AU-6, SI-4), and an unguarded cloud organization (CM-6).
2. **Credentials and secrets:** long-lived pipeline keys and live secrets in repositories (IA-5), and non-human identities without owners or certification (AC-2, AC-6).
3. **Support access:** sessions without the required ticket and an unrecorded legacy path (AC-2, AC-3, AU-10), which also make two trust page statements untrue (P03 G-032, G-033).
4. **Commitments:** deletion after termination (SI-12) and notice duties to banks, agencies, and customers with non-standard terms (IR-6, IR-8).
5. **Resilience:** Cell 4 recovery time (CP-10) and missing contingencies for DNS, the export path, and AI model providers (CP-2).

**Strengths:** tenant isolation held in all 40 cross-tenant attempts and in shared resources (AC-3 test, SC-4); phishing-resistant MFA and PAM (IA-2, IA-2(1), AC-6(9)); immutable logs and backups (AU-9, CP-9); separation of duties in code and tool approvals (AC-5); encryption (SC-8, SC-28); and workforce training (AT-2) were all Satisfied.

**New finding during testing:** a publicly readable AQ-01 CI build log bucket with a static access key in one log (CM-06b.). Added to the risk register as R-058 and to POAM-019. This is the same exposure path used in the P08 scenario.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment and 5 carried from the P03 gap analysis (POAM-020 to POAM-024), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 10 |
| Low | 3 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the OCP control environment is **effective with exceptions**. Tenant isolation, identity, logging, backup, and encryption controls operate effectively. The exceptions concentrate in the AQ-01 interconnection, credentials and secrets, support access, and the processes that keep the company's commitments to customers true. Management accepted all findings and committed to the POA&M dates. The CTO used this report for the conditional authorization in P02 section 4.2.
