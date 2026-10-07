# Security Assessment Plan and Report: Cris Santos Company | Communications | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier) |
| System assessed | Customer Billing and Network Operations Platform (OSS/BSS), CSC-SYS-OSSBSS-001, per the SSP (P02), including the enterprise common controls it inherits from the identity platform, SOC, cloud landing zone, and network management plane |
| Tier / Vertical | Enterprise / Communications |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. A network specialist from an outside firm, engaged by Internal Audit, ran the element scans and reachability tests under Internal Audit supervision |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also supports | The CPNI certification evidence package (47 CFR 64.2009(e); PRC-01.4); the annual assessment for the OSS/BSS authorization (P02 section 4.2); the SOC 2 readiness evidence (P09) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **42 controls (AC 7, AT 2, AU 4, CA 2, CM 4, CP 4, IA 4, IR 4, PS 1, PT 1, RA 1, SA 2, SC 3, SI 3), 250 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (state-sponsored intrusion through the management plane, acquired-carrier networks, pretexting at care vendors, disclosure readiness);
- cover CPNI rules with gaps in P03 (customer authentication, approvals, training, breach notice);
- include High-baseline confidentiality supplements from the SSP (AC-6(3), CA-8, SI-4(20));
- are common controls the OSS/BSS inherits from the network management plane and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-005; 64.2010(a) | Comprehensive | Comprehensive | 2,940 OSS/BSS account events (2026-01-01 to 2026-06-30); 1,410 terminations of staff and vendor agents with BSS access (96 at AQ-02 and AQ-03) | 60 account events (random); 60 terminations (stratified: 45 enterprise and vendor, 15 AQ) | 22 / 4 |
| AC-2(3) | R-004 | Focused | Comprehensive | 12,400 workforce and vendor accounts | 100% (data analytic) | 4 / 0 |
| AC-3 | R-005; 64.2010(b) | Focused | Focused | 9,800 workforce BSS users | 25 users (random); CPNI screen access tested with 2 test accounts | 1 / 0 |
| AC-5 | R-031 | Focused | Comprehensive | 46 users with rating or bill-run roles | 100% | 2 / 0 |
| AC-6 | R-053; R-010 | Focused | Comprehensive | 12,400 accounts | 100% of bulk export entitlements (data analytic) | 0 / 1 |
| AC-6(3) | R-001; R-008 | Comprehensive | Focused | 6 element platform families | 100% of platform families; 1 test path | 1 / 1 |
| AC-17 | R-003; R-058 | Focused | Comprehensive | 4 remote access types; 9 AQ site VPN tunnels; 1 transition services provider | 100% | 3 / 1 |
| AT-2 | R-005; 64.2009(b) | Basic | Focused | 12,000 employees and 2,600 vendor agents | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-005; 64.2009(b) | Focused | Comprehensive | about 2,600 vendor agents; about 1,700 in-house agents; 420 network administrators | 100% (data analytic) for completion; 10 interviews | 7 / 2 |
| AU-2 | R-010; 64.2010(f) | Focused | Focused | n/a (configuration) | 6 event types generated in test (CPNI view, call detail display, export, password change, address change, approval flag change) | 6 / 0 |
| AU-6 | R-063; R-010 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 6 monthly AQ access reviews | 5 weeks (random); 100% of AQ reviews | 2 / 1 |
| AU-9 | 64.2011(d) | Basic | Focused | n/a (configuration) | configuration inspected; 1 deletion attempt | 2 / 0 |
| AU-12 | R-009 | Basic | Comprehensive | 38 OSS/BSS log sources | 100% | 2 / 1 |
| CA-7 | Program health | Focused | Basic | 6 monthly packages | 3 months (random) | 11 / 0 |
| CA-8 | R-001 | Basic | Focused | 1 annual test | 100% | 1 / 0 |
| CM-2 | R-002 | Focused | Comprehensive | 12 BSS servers and 9 container images | 100% | 5 / 0 |
| CM-3 | R-031; 64.2009(a) | Comprehensive | Focused | 312 changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 10 / 0 |
| CM-6 | R-049; R-008 | Focused | Comprehensive | about 2,900 AQ elements; 6 adapter hosts | SNMP and default credential scan of 100% of AQ-03 elements (with Chief Network Officer approval, maintenance window) | 4 / 2 |
| CM-8 | R-059 | Comprehensive | Comprehensive | about 41,000 network elements | 60 physical elements traced to the inventory (random, 6 offices) | 4 / 2 |
| CP-2 | R-016 | Comprehensive | Focused | n/a (plan) | plan examined; 3 interviews | 22 / 2 |
| CP-4 | R-016 | Focused | Focused | 1 annual test | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-016 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-021 | Basic | Focused | 12,400 accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-021 | Focused | Comprehensive | 64 privileged OSS/BSS accounts | 100% | 1 / 0 |
| IA-5 | R-008; R-049 | Focused | Comprehensive | about 41,000 network elements; 6 adapter accounts | 100% (data analytic) | 8 / 2 |
| IA-8 | R-005; R-006; 64.2010(b)-(e) | Comprehensive | Comprehensive | about 410,000 calls with call detail requests (2026 H1); AQ-02 portal | 240 recorded calls (60 in-house, 60 per vendor); 2 AQ-02 test accounts | 0 / 1 |
| IR-3 | R-014 | Focused | Focused | 2 exercises in the past 12 months | 100% | 0 / 1 |
| IR-4 | R-060; R-002 | Focused | Focused | 248 security incidents (9 at AQ sites) | 25 incidents (random) plus all 9 AQ incidents | 11 / 2 |
| IR-6 | R-001; 64.2011(b) | Basic | Focused | 248 incidents | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-014; R-011 | Comprehensive | Focused | n/a (plan) | plan examined | 15 / 2 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,410 terminations | 60 (stratified) | 4 / 1 |
| PT-4 | R-019; 64.2007 | Focused | Comprehensive | about 1.02 million voice accounts; 38 campaigns | 40 approvals (random); 38 campaigns | 0 / 1 |
| RA-5 | R-007; R-048 | Focused | Focused | about 3,900 critical and high network and OSS/BSS findings (2026 H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-023; R-040 | Focused | Comprehensive | 14 external services supporting the OSS/BSS (11 tier-1) | 100% | 4 / 2 |
| SA-22 | R-025 | Focused | Comprehensive | OSS/BSS components and their direct feeds | 100% | 1 / 1 |
| SC-7 | R-003; R-001 | Comprehensive | Focused | n/a (architecture) | 2 test paths | 5 / 1 |
| SC-8 | R-017 | Basic | Comprehensive | all OSS/BSS interfaces; 102 CDR feeds | 100% | 0 / 1 |
| SC-28 | R-022 | Basic | Focused | n/a (configuration) | configuration inspected | 1 / 0 |
| SI-2 | R-007 | Focused | Focused | 286 patches for OSS/BSS servers and network firmware (2026 H1) | 25 patches (random) | 9 / 1 |
| SI-4 | R-001; R-009 | Comprehensive | Focused | about 41,000 elements; 38 OSS/BSS log sources | coverage analytic 100%; 2 test locations | 10 / 2 |
| SI-4(20) | R-010; R-021 | Basic | Comprehensive | 64 privileged accounts | 100% | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items per stratum, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 and PS-4 terminations, CM-8, RA-5, AT-2, and for IA-8 call recordings (60 per care channel).
- **Key manual controls, populations of 250 to 500:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3 (312 changes) and PT-4 approvals.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, CP-9, IA-2, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences (all 6 for the AQ access reviews because of their risk); annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 12,400 accounts for inactivity, all bulk export entitlements, all AQ-03 elements for default credentials, all 38 log sources).
- **Stratification:** terminations were stratified so the acquired carriers (7% of the population) got 15 of 60 items; call recordings were stratified by channel (in-house, CV-1, CV-2, CV-3).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a CPNI authentication control (IA-8) or a lawful-intercept-adjacent control makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, BSS role matrix and audit trails, change tickets, TACACS+ coverage and authorization rules, backup and DR test reports, vulnerability scans, vendor register and SOC report reviews, the incident response plan and materiality playbook, campaign register and approval flags, call recordings.
- **Interview:** Vice President, OSS/BSS Platforms; BSS Application Manager; Director of Network Security Engineering; Director of Security Operations; Director of Identity and Access Management; Chief Customer Officer; Director of Outsourced Care; Vice President, Marketing; General Counsel; CFO; CISO; 20 randomly selected care agents (10 in-house, 10 vendor).
- **Test:** access tests with test accounts; a deletion attempt against the log archive; default-credential and SNMP scans of AQ-03 elements (approved by the Chief Network Officer, in a maintenance window); reachability tests from an AQ-02 site network and from the OSS adapter segment toward the lawful-intercept enclave; a rogue device test on management networks at two central offices; TLS scans and a protocol inventory of CDR feeds; AQ-02 portal reset tests with two test accounts.

## 4. Rules of engagement
- No testing could affect voice, 911, or broadband service. Element scans ran only in approved maintenance windows with the NOC on the bridge, and the NOC could stop any test.
- The reachability test toward the lawful-intercept enclave was limited to connection attempts; no assessor accessed intercept content or records. The Director, Lawful Intercept Compliance, approved and observed it.
- Call recordings were reviewed in the quality tool; no CPNI left company systems. Screenshots and exports in workpapers are redacted.
- Portal tests used company-owned test accounts, not customer accounts.
- Critical exposures were reported to the CISO within 24 hours. One was: default credentials on 8 AQ-03 elements (reported 2026-08-21, fixed 2026-08-27).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, OSS/BSS Platforms |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (250 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 213 |
| Other than satisfied | 37 |
| **Total** | **250** |

**Controls with at least one Other than satisfied statement: 25 of 42:** AC-2, AC-6, AC-6(3), AC-17, AT-3, AU-6, AU-12, CM-6, CM-8, CP-2, CP-10, IA-5, IA-8, IR-3, IR-4, IR-8, PS-4, PT-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4.

**Fully Other than satisfied:** AC-6, IA-8, IR-3, PT-4, SC-8 (each has a single determination statement).

**Themes:**
1. **Acquired-carrier integration** drives the identity (AC-2, PS-4), remote access and network boundary (AC-17, AC-6(3), SC-7), monitoring (AU-6, AU-12, IR-4), and CPNI approval (PT-4) findings.
2. **The network management plane** is the main common-control weakness: shared local accounts on legacy elements (IA-5), defaults at AQ-03 (CM-6, IA-5), incomplete inventory (CM-8), monitoring coverage (SI-4), and patching of AQ-02 SBCs and edge routers (RA-5, SI-2).
3. **CPNI authentication at the edges of care:** one care vendor and the AQ-02 portal (IA-8), and vendor agents trained after access (AT-3).
4. **Disclosure readiness:** the plan and playbook do not cover the 64.2011 hold or Item 1.05(d), and the disclosure committee has not been exercised (IR-3, IR-8).

**Strengths:** BSS access enforcement (AC-3, AC-5), privileged MFA and monitoring (IA-2(1), SI-4(20)), change management for CPNI logic (CM-3), immutable logs and backups (AU-9, CP-9), encryption at rest (SC-28), training for the in-house workforce (AT-2), continuous monitoring (CA-7), penetration testing (CA-8), and CPNI breach reporting (IR-6) were all Satisfied. The lawful-intercept enclave was not reachable from the OSS adapter segment.

**New finding during testing:** vendor-default SNMP community strings on 6 AQ-03 cabinet switches and a default administrator password on 2 OLT shelf controllers (CM-06b., IA-05e.). Added to the risk register as R-049 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 24 items: 17 from this assessment and 7 carried from the SSP (POAM-016), the P03 gap analysis (POAM-019 to POAM-022, POAM-024), and the P10 AI assessment (POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 9 |
| Moderate | 14 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 4 |

**Scope note:** the AQ-02 and AQ-03 legacy billing systems are outside the SSP boundary, so their backups and restores were not tested here (P05 DEP-20, DEP-21); the untested restore is carried as P01 R-051.

## 8. Conclusion
Internal Audit concludes that the OSS/BSS control environment is **effective with exceptions**. Enterprise controls for identity, change management, logging, backup, and encryption of CPNI operate effectively. The exceptions concentrate in the network management plane the OSS/BSS depends on, in the acquired carriers, and in authentication at one care vendor. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2, and the Chief Compliance Officer will use it in the evidence package for the 2027 CPNI certifications.
