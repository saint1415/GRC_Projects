# Security Assessment Plan and Report: Cris Santos Company | Arts, Entertainment, and Recreation | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded live entertainment company) |
| System assessed | Ticketing and Venue Operations Platform (TVOP), CSC-SYS-TVOP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Arts, Entertainment, and Recreation |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team and the Director of Payments and PCI Compliance (second line) supported scoping only. This assessment does not replace the QSA's Reports on Compliance; the QSA may use its results as input |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the TVOP authorization (P02 section 4.2); input to PCI DSS Requirement 12.4 and the QSA's 2026 fieldwork |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 7, AT 1, AU 5, CA 1, CM 6, CP 4, IA 5, IR 3, PS 1, RA 2, SA 1, SC 4, SI 5, SR 1), 256 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (e-skimming on checkout pages, acquired venues, client and service accounts, card data in the contact center, venue OT and gate entry);
- cover PCI DSS requirements with gaps in the P03 pre-assessment;
- are common controls the TVOP inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-005; R-032; R-057; PCI DSS 7.2, 8.2 | Comprehensive | Comprehensive | 1,412 TVOP workforce account events (2026-01-01 to 2026-06-30); 1,236 terminations with TVOP access (88 at AV venues); about 9,400 client user accounts | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AV); client accounts 100% (data analytic) | 22 / 4 |
| AC-2(3) | R-005; PCI DSS 8.2.6 | Focused | Comprehensive | About 2,900 workforce and about 9,400 client accounts | 100% (data analytic) | 3 / 1 |
| AC-3 | R-054; PCI DSS 7.3 | Focused | Focused | About 340 client tenants | 25 cross-tenant access attempts with test accounts | 1 / 0 |
| AC-4 | R-001; PCI DSS 1.3 | Focused | Focused | CDE egress allow-list | Allow-list examined; 5 test connections to non-listed destinations | 1 / 0 |
| AC-6 | R-025; PCI DSS 7.2 | Focused | Focused | 1,940 PAM elevation sessions to CDE accounts | 25 sessions (random) | 1 / 0 |
| AC-6(9) | R-025 | Basic | Focused | 1,940 PAM sessions | Same 25 sessions | 1 / 0 |
| AC-17 | R-028; PCI DSS 8.4.3 | Focused | Comprehensive | 4 remote access paths to the TVOP | 100% | 4 / 0 |
| AT-2 | R-028; PCI DSS 12.6 | Basic | Focused | 12,000 workforce (about 2,900 with TVOP access) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AU-2 | R-001; PCI DSS 10.2 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-034; PCI DSS 10.4 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 168 log sources on TVOP paths | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050; PCI DSS 10.3 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | PCI DSS 10.5.1 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | PCI DSS 10.2 | Basic | Focused | n/a (configuration) | 10 TVOP services and the payment service | 3 / 0 |
| CA-8 | PCI DSS 11.4 | Focused | Focused | 2026-03 penetration test | 100% | 1 / 0 |
| CM-2 | R-037; PCI DSS 2.2 | Focused | Focused | Baseline repository for TVOP services | 100% | 5 / 0 |
| CM-3 | R-055; PCI DSS 6.5 | Comprehensive | Comprehensive | 212 payment service changes (2026-01-01 to 2026-06-30), 31 of them emergency changes | 40 changes (random, including 18 emergency changes) | 8 / 2 |
| CM-6 | R-031; R-037; PCI DSS 2.2 | Focused | Comprehensive | About 150 AV POS terminals; 12 festival kits; TVOP containers | 25 AV terminals (random); 12 kits (100%); container baselines 100% | 4 / 2 |
| CM-7 | PCI DSS 2.2.4 | Focused | Focused | CDE container images | 10 images (random) | 6 / 0 |
| CM-7(5) | R-001; PCI DSS 6.4.3 | Comprehensive | Comprehensive | About 340 client templates and the own-brand checkout | 212 client templates with sales in the last 30 days (100% of active templates); own-brand checkout | 1 / 2 |
| CM-8 | R-004; PCI DSS 9.5.1.1; 12.5.1 | Comprehensive | Comprehensive | About 2,900 P2PE devices; about 150 AV readers; about 7,500 scanners | 60 devices traced to the inventory (random, 6 venues); all AV readers | 5 / 1 |
| CP-2 | R-008; R-011; PCI DSS 12.10.1 | Comprehensive | Focused | n/a (plan) | Plan v3 examined; 4 interviews | 22 / 2 |
| CP-4 | R-015; PCI DSS 12.10.2 | Focused | Comprehensive | 36 venues; 1 regional failover test; 1 processor failover test | 100% | 4 / 1 |
| CP-9 | R-049 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-010 | Focused | Focused | 1 regional failover test | 100% | 1 / 1 |
| IA-2 | R-028; PCI DSS 8.2.1 | Basic | Focused | About 2,900 workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-025; PCI DSS 8.4.1 | Focused | Comprehensive | 312 privileged and CDE accounts | 100% | 1 / 0 |
| IA-3 | PCI DSS 9.5.1 | Basic | Focused | About 7,500 scanners and 2,900 P2PE devices | 25 devices (random) | 1 / 0 |
| IA-5 | R-014; R-024; PCI DSS 2.2.2; 8.6.3 | Focused | Comprehensive | About 900 turnstile controllers and access control devices at 36 venues; 127 client API keys; TVOP secrets | Default-credential test on 120 turnstile and access control devices at 6 venues (with vendor approval, between events); 100% of API keys | 8 / 2 |
| IA-8 | R-005; FTC Act Section 5 | Focused | Comprehensive | About 9,400 client user accounts | 100% (data analytic) | 0 / 1 |
| IR-4 | R-060; PCI DSS 12.10 | Focused | Focused | 241 security incidents (2026 H1), 9 at AV venues and festivals | 25 incidents (random) plus all 9 AV and festival incidents | 11 / 2 |
| IR-6 | R-020 | Basic | Focused | 241 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-018; R-064; PCI DSS 12.10.1; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with the General Counsel, CFO, CISO, and Director of Payments and PCI Compliance | 15 / 2 |
| PS-4 | R-032; R-057; PCI DSS 8.2.5 | Comprehensive | Comprehensive | 1,236 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | PCI DSS 12.3 | Focused | Basic | n/a | 2026 risk assessment and targeted risk analyses examined | 8 / 0 |
| RA-5 | R-023; PCI DSS 6.3.1; 11.3 | Focused | Focused | 1,904 critical and high findings on CDE and TVOP components (2026 H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-021; PCI DSS 12.8 | Focused | Comprehensive | 31 service providers with PCI DSS impact; 9 tag vendors on checkout templates | 100% | 4 / 2 |
| SC-7 | R-004; PCI DSS 1.3 | Comprehensive | Focused | n/a (architecture) | Reachability tests from an AV venue office network to POS terminals and to the enterprise hub | 5 / 1 |
| SC-8 | PCI DSS 4.2.1 | Basic | Focused | All TVOP interfaces carrying card or patron data | 100% (TLS scan) | 1 / 0 |
| SC-12 | PCI DSS 3.6 | Basic | Focused | n/a (configuration) | Key policies inspected | 2 / 0 |
| SC-28 | PCI DSS 3.5.1 | Basic | Focused | n/a (configuration) | Database and backup encryption inspected; card-number discovery scan of TVOP databases | 1 / 0 |
| SI-2 | R-029; PCI DSS 6.3.3 | Focused | Focused | 248 security patches for TVOP components | 25 patches (random) | 9 / 1 |
| SI-4 | R-001; R-003; PCI DSS 10.4; 11.5 | Focused | Focused | n/a | Monitoring use cases examined; simulated checkout script change on a test template | 11 / 1 |
| SI-7 | R-001; PCI DSS 11.5.2; 11.6.1 | Comprehensive | Focused | n/a | Integrity tools examined; simulated change on own-brand and client test pages | 4 / 2 |
| SI-10 | PCI DSS 6.2.4 | Focused | Focused | 20 malformed requests | 100% in the test environment | 1 / 0 |
| SI-12 | R-007; R-053; PCI DSS 3.2.1 | Focused | Comprehensive | About 6.5 million case notes; 1.1 million overflow recordings; data warehouse retention | 100% of notes (pattern scan); 60 recordings (random) | 2 / 2 |
| SR-6 | R-011; PCI DSS 12.8.4 | Basic | Focused | 5 critical payment service providers | 100% | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (212 changes; the sample deliberately included 18 of the 31 emergency changes).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-6, CM-6 (AV terminals), CP-9, IA-2, IA-3, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all client user accounts for inactivity and MFA, all 212 active client templates for scripts, all case notes for card numbers).
- **Stratification:** terminations were stratified so the acquired venues (7% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key card data control (CM-7(5), SI-7, SI-12) or a safety control (IA-5 on entry devices) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, client user exports, change tickets and pipeline approvals, backup and DR test reports, vulnerability scans and ASV reports, the vendor register and AOC reviews, the incident response plan and materiality playbook, browser captures of checkout templates, and data discovery results.
- **Interview:** President, Ticketing; Chief Technology Officer; Directors of Platform Engineering, Payments Engineering, Security Operations, and Identity and Access Management; Director of Payments and PCI Compliance; General Counsel; CFO; CISO; Vice President, Integration Management Office; 20 randomly selected box office and contact center staff.
- **Test:** cross-tenant access tests with test accounts; a simulated script change on own-brand and client test templates; reachability tests from an AV venue office network; default-credential tests on turnstile and access control devices (with vendor approval, between events); a deletion attempt on the log archive; malformed requests in the test environment; a restore observation; a listening sample of overflow center recordings.

### What each test could show
The 2026 revisions of POL-01 to POL-05 (P06) were drafts during fieldwork; they were approved on 2026-09-10 and take effect on 2026-10-01. Internal Audit therefore tested each control as it operated under the policy set in force (EV-024), and reviewed the draft 2026 statements for design only. Any statement the 2026 revision adds has not operated yet; its operation is tested at the 2027-03 follow-up. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control was in force during the period and was tested on samples, full populations or live systems | 254 (221 Satisfied, 33 Other than satisfied) |
| Design | The control is new (a draft 2026 policy statement); only its design was reviewed. Operation is tested at the 2027-03 follow-up | 0 (the draft statements were reviewed against the policy text, not scored as determination statements) |
| Not implemented | Nothing existed to test: integrity verification of scripts and headers on client checkout templates (SI-07a.[01]) and a defined response to unauthorized changes there (SI-07b.[01]) | 2 |
| **Total** | | **256** |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-AC-2 and so on), with the population each sample was drawn from. Populations came from the intake exports where the period allowed (for example identity governance and HR records, EV-004 and EV-005, and the payment service change records, EV-067) and were refreshed to 2026-06-30 at kickoff.

## 4. Rules of engagement
- No testing could affect an on-sale, a live event, or gate entry. Device tests ran between events with the venue general manager's approval and an integrator present.
- Script change tests used test templates on a non-production client tenant; malformed request tests ran only in the test environment.
- The reachability test at AV-03 used an audit-owned laptop with no card or patron data, pre-approved by the CISO and the Vice President, Integration Management Office.
- No card or patron data left the company's systems. The recording listening sample was performed in the contact center with the Director of Payments and PCI Compliance present, and workpapers record only counts, never card numbers.
- Critical exposures were reported to the CISO within 24 hours. One was: vendor default credentials on turnstile controllers at 2 venues and a building management interface at a third venue (reported 2026-08-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Operating Officer, the CISO, and the President, Ticketing |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (256 rows), and `poam.csv` (26 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 221 |
| Other than satisfied | 35 |
| **Total** | **256** |

**Controls with at least one Other than satisfied statement: 22 of 46:** AC-2, AC-2(3), AU-6, CM-3, CM-6, CM-7(5), CM-8, CP-2, CP-4, CP-10, IA-5, IA-8, IR-4, IR-8, PS-4, RA-5, SA-9, SC-7, SI-2, SI-4, SI-7, SI-12.

**Fully Other than satisfied:** IA-8 (a single determination statement).

**Themes:**
1. **The payment page on client templates** is the most serious weakness: scripts are not identified or allow-listed (CM-7(5)), not integrity-checked (SI-7), and not monitored (SI-4). A simulated script change on a client test template went undetected.
2. **Acquired venues** drive the network (SC-7), inventory (CM-8), configuration (CM-6), identity (AC-2, PS-4), logging (AU-6), and incident handling (IR-4) findings.
3. **Non-workforce identities:** client users without MFA or reviews (IA-8, AC-2(3)) and client API keys never rotated (IA-5).
4. **Card data where it should not be:** card numbers and security codes in case notes and overflow recordings (SI-12).
5. **Resilience and disclosure readiness:** failover over its RTO (CP-10), untested edge provider fallback and offline drills (CP-2, CP-4), and an incident plan without the service provider path (IR-8).

**Strengths:** workforce identity and privileged access (IA-2, IA-2(1), AC-6, AC-6(9), AC-17), tenant isolation (AC-3), CDE network isolation (AC-4), log protection and retention (AU-9, AU-11), encryption (SC-8, SC-12, SC-28), backups (CP-9), penetration testing (CA-8), and training (AT-2) were all Satisfied.

**New finding during testing:** vendor default credentials on turnstile controllers at 2 venues (IA-05e.) and on a building management interface at a third venue. Added to the risk register as R-014 and to POAM-007.

## 7. POA&M summary
`poam.csv` holds 26 items: 16 from this assessment, 6 carried from the P03 gap analysis (POAM-005, POAM-021, POAM-022, POAM-023, POAM-025, POAM-026), and 4 from the risk register, BIA, and AI assessment (POAM-006, POAM-015, POAM-019, POAM-020), so leadership tracks one list.

| Risk level | Items |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 15 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the TVOP control environment is **effective with exceptions**. Enterprise common controls for identity, logging, encryption, backup, and testing operate effectively. The exceptions concentrate in the payment page on client templates, in the acquired venues, and in identities and data outside the workforce perimeter. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2, and the Director of Payments and PCI Compliance shared it with the QSA ahead of the 2026 fieldwork.
