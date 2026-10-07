# Security Assessment Plan and Report: Cris Santos Company | Wholesale Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded IT hardware and software distributor) |
| System assessed | Order-to-Cash and Fulfillment Platform (OCFP), CSC-SYS-OCFP-001, per the SSP (P02), including the enterprise common controls it inherits and the supply chain controls (SR family) that the SSP applies to distributed products |
| Tier / Vertical | Enterprise / Wholesale Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with a co-sourced audit firm for the OT review that fed POAM-008 and POAM-009. None of the assessors designs or operates the controls. **Independence safeguard:** two IT auditors administered the ERP until 2025; under the 24-month cooling-off rule (POL-01 4.9) they did not test ERP access, change, or segregation-of-duties controls (AC-2, AC-3, AC-5, CM-3, CM-5), which were tested by the audit manager and the other two auditors. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the OCFP authorization (P02 section 4.2); evidence for the SL-1 SOC 2 readiness (P09); input to the 2027-01-15 Level 1 (Self) self-assessment for the enterprise FCI scope |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 2, AU 5, CA 1, CM 5, CP 4, IA 4, IR 3, PS 1, RA 2, SA 1, SC 3, SI 3, SR 3), 270 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (ransomware, AQ-1 integration, product integrity, reseller fraud);
- cover FAR 52.204-21 requirements for the enterprise FCI scope (the OCFP holds FCI for every DoD order);
- protect OCFP availability (the contingency controls behind the SSP availability supplements);
- are common controls the OCFP inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-024; R-058; 52.204-21(b)(1)(i) | Comprehensive | Comprehensive | 2,940 OCFP account events (2026-01-01 to 2026-06-30); 1,610 separations of staff and agency workers with WMS or ERP access (1,020 agency workers) | 60 account events (random); 60 separations (stratified: 30 employees, 30 agency workers) | 23 / 3 |
| AC-2(3) | R-024 | Focused | Comprehensive | About 13,000 workforce OCFP accounts; about 38,000 reseller users | 100% (data analytic) | 4 / 0 |
| AC-3 | R-023; R-027 | Focused | Focused | About 6,800 ERP users | 25 users (random) | 1 / 0 |
| AC-5 | R-025 | Comprehensive | Comprehensive | About 6,800 ERP users | 100% (segregation of duties analytic) | 1 / 1 |
| AC-6 | R-001 | Focused | Focused | 2,210 PAM elevation sessions to OCFP servers and databases | 25 sessions (random) | 1 / 0 |
| AC-7 | R-011 | Basic | Focused | n/a (configuration) | SSO and reseller platform lockout tested with 2 test accounts | 2 / 0 |
| AC-17 | R-001; R-021 | Focused | Comprehensive | 4 remote administration paths to the OCFP | 100% | 4 / 0 |
| AT-2 | R-022; R-011 | Basic | Focused | 12,000 workforce plus about 1,000 active agency workers | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-003; R-016; R-011 | Focused | Focused | About 2,300 staff in role-based training groups | 40 records (random, stratified by role) | 8 / 1 |
| AU-2 | R-011; R-023 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-007; R-050 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 47 log sources on the OCFP order path and its interconnections | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-051 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | R-020 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-023 | Basic | Focused | n/a (configuration) | 8 ERP servers, 4 WMS servers, 4 edge servers, API gateway | 3 / 0 |
| CA-7 | 17 CFR 229.106(b) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-045 | Focused | Focused | 16 OCFP servers and edge servers in sample frame | 100% of the frame | 5 / 0 |
| CM-3 | R-048; R-049 | Comprehensive | Comprehensive | 212 OCFP change records (2026-01-01 to 2026-06-30), including 31 emergency changes | 40 changes (random, all 31 emergency changes eligible) | 9 / 1 |
| CM-5 | R-048 | Focused | Focused | 212 changes | 10 changes traced to pipeline and PAM sessions | 6 / 0 |
| CM-6 | R-021; R-026 | Focused | Comprehensive | 16 servers in sample frame | 100% | 6 / 0 |
| CM-8 | R-046 | Comprehensive | Comprehensive | About 4,800 handhelds and 28 servers | 60 physical devices traced to the CMDB and MDM (random, 3 distribution centers) | 5 / 1 |
| CP-2 | R-012; R-010 | Comprehensive | Focused | n/a (plan) | Plan v3 examined; 3 interviews | 24 / 0 |
| CP-4 | R-012 | Focused | Focused | 1 annual DR test | 100% | 5 / 0 |
| CP-9 | R-051 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-012 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-058; 52.204-21(b)(1)(v) | Comprehensive | Comprehensive | About 6,100 WMS accounts and about 6,800 ERP accounts | 100% (data analytic for shared or generic accounts); 25 sign-ins (random) | 1 / 1 |
| IA-2(1) | R-022 | Focused | Comprehensive | 74 ERP technical administrators and 31 platform administrators | 100% | 1 / 0 |
| IA-5 | R-013; R-058 | Focused | Comprehensive | About 430 reseller API keys; 3 kiosk accounts | 100% (data analytic) | 8 / 2 |
| IA-8 | R-011 | Focused | Comprehensive | About 38,000 reseller users | 100% (data analytic) | 1 / 0 |
| IR-4 | R-001; R-004 | Focused | Focused | 184 security incidents (2026 H1) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-019; R-005 | Basic | Focused | 184 incidents; 20 staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-017; R-004 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with the General Counsel, CFO, CISO, and Chief Supply Chain Officer | 15 / 2 |
| PS-4 | R-024 | Comprehensive | Comprehensive | 1,610 separations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | 17 CFR 229.106(b) | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-045; R-021 | Focused | Focused | 2,416 vulnerability findings on OCFP components (2026 H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-031; R-033; R-010 | Focused | Comprehensive | 14 external services supporting the OCFP (including 4 staffing agencies) | 100% | 4 / 2 |
| SC-7 | R-007 | Comprehensive | Focused | n/a (architecture) | Reachability test from the AQ-1 network at TX-2 to OCFP integration hosts | 4 / 2 |
| SC-8 | R-002 | Basic | Focused | All OCFP external interfaces | 100% (TLS scan) | 1 / 0 |
| SC-28 | R-002 | Basic | Focused | n/a (configuration) | Database, storage, and backup encryption inspected | 1 / 0 |
| SI-2 | R-045 | Focused | Focused | 236 patches applied to OCFP components (2026 H1) | 25 patches (random) | 9 / 1 |
| SI-4 | R-011; R-013 | Focused | Focused | n/a (monitoring design); 14 fraud cases (2026 H1) | Use case catalog examined; all 14 fraud cases traced | 11 / 1 |
| SI-10 | R-049 | Focused | Focused | 20 malformed test documents and API calls | 100% in the test environment | 1 / 0 |
| SR-3 | R-005; R-037 | Comprehensive | Comprehensive | About 5,700 drop-ship federal order lines with substitutions (2026 H1) | 60 (random) | 3 / 1 |
| SR-10 | R-003; R-040 | Comprehensive | Focused | About 4,900 open-market receipt lines (2026 H1) | 60 receipt lines (random, stratified: 30 federal, 30 commercial) | 0 / 1 |
| SR-11 | R-003; R-039 | Comprehensive | Focused | n/a (procedures); 31 suspect lots (2026 H1) | Procedure examined; all 31 suspect lots traced | 4 / 1 |
## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, RA-5, SR-3, and SR-10.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (212 changes). AT-3 also used 40 items, stratified by role, as a lower-risk control with a larger population.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CP-9, IA-2 (sign-ins), IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all OCFP accounts for inactivity and shared accounts, all reseller API keys for age, all ERP users for segregation-of-duties conflicts).
- **Stratification:** separations were stratified so agency workers (63% of the population) got 30 of 60 items; open-market receipts were stratified 30 federal and 30 commercial, because the inspection rules differ.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key product-integrity or federal compliance control (SR-3, SR-10, SR-11, IA-2 for FCI access) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, ERP role catalog and segregation-of-duties reports, change tickets, backup and DR test reports, vulnerability scans, the vendor register and SOC report reviews, the incident response plan and materiality playbook, drop-ship order records, Product Authentication Lab records.
- **Interview:** Vice President, Enterprise Applications; ERP Platform Manager; Vice President, Distribution Operations; Vice President, E-commerce; Director of Security Operations; Director of Identity and Access Management; Chief Supply Chain Officer; Director, Product Authentication Lab; Director, Government Contracts; General Counsel; CFO; CISO; 20 randomly selected distribution-center staff.
- **Test:** access tests with test accounts; lockout tests; a data analytic for shared and generic accounts; a reachability test from the AQ-1 network at TX-2; a deletion attempt against the log archive; TLS scans; malformed EDI documents and API calls in the test environment; a restore observation; a physical trace of handhelds at 3 distribution centers.

## 4. Rules of engagement
- No testing could interrupt order capture, picking, or shipping. Tests that touched production ran outside shift peaks with the system owner's approval.
- Malformed document tests ran only in the test environment.
- The AQ-1 reachability test used an audit-owned laptop, pre-approved by the CISO and the Vice President, Integration Management Office, and stopped at connection attempts (no exploitation).
- No customer data, FCI, or CUI left company systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: shared dock kiosk accounts at OH-1 with access to DoD ship-to data (reported 2026-08-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Enterprise Applications |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (270 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 245 |
| Other than satisfied | 25 |
| **Total** | **270** |

**Controls with at least one Other than satisfied statement: 19 of 44:** AC-2, AC-5, AT-3, AU-6, CM-3, CM-8, CP-10, IA-2, IA-5, IR-8, PS-4, RA-5, SA-9, SC-7, SI-2, SI-4, SR-3, SR-10, SR-11.

**Fully Other than satisfied:** SR-10 (a single determination statement).

**Themes:**
1. **Product integrity** is the main distributor-specific weakness: tamper inspection of commercial open-market receipts (SR-10), detection means for counterfeits (SR-11), and screening of drop-ship substitutions (SR-3).
2. **Workforce and third-party identity:** agency worker separations (AC-2, PS-4), shared kiosk accounts (IA-2, IA-5, AC-2), and untiered staffing agencies (SA-9).
3. **AQ-1 integration** drives the network (SC-7) and monitoring (AU-6) findings.
4. **Reseller channel fraud:** static API keys (IA-5) and missing detection of fraudulent ship-to patterns (SI-4).
5. **Disclosure readiness:** the plan and materiality playbook do not cover supplier-compromise events (IR-8).

**Strengths:** privileged access and phishing-resistant MFA for administrators (AC-6, IA-2(1)), reseller MFA (IA-8), immutable logs and backups (AU-9, CP-9), encryption (SC-8, SC-28), input validation (SI-10), and the contingency plan and test process (CP-2, CP-4) were all Satisfied.

**New finding during testing:** 3 shared dock kiosk accounts in the WMS at OH-1 that reach DoD ship-to data (IA-02[01], IA-05i., AC-02f.[01]). Added to the risk register as R-058 (and R-018 for the Level 1 affirmation), to the gap analysis rows G-115 and G-116, and to POAM-003.

## 7. POA&M summary
`poam.csv` holds 23 items: 16 from this assessment and 7 carried from the P03 gap analysis, the P05 BIA, and the co-sourced OT review (POAM-007, POAM-008, POAM-009, POAM-019, POAM-020, POAM-021, POAM-022), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 9 |
| Low | 3 |

| Status | Items |
|---|---|
| In progress | 17 |
| Open | 6 |

## 8. Conclusion
Internal Audit concludes that the OCFP control environment is **effective with exceptions**. Enterprise common controls for privileged identity, logging, backup, encryption, and recovery planning operate effectively. The exceptions concentrate in product-integrity controls, workforce and third-party identity, the AQ-1 connection, and reseller channel fraud. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
