# Security Assessment Plan and Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm) |
| System assessed | Farm Management and Irrigation Control Platform (FMICP), CSC-SYS-FMICP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Agriculture, Forestry, Fishing and Hunting |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`); OT test methods follow NIST SP 800-82 Rev. 3 (passive first; active tests only in maintenance windows) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with a co-sourced OT assessment firm (two OT specialists) engaged by and reporting to Internal Audit. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. The OT firm has no other engagement with the company and is not one of the irrigation integrators |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the FMICP authorization (P02 section 4.2); evidence for the CSF 2.0 ID.IM-01 outcome (P03) and the Item 106 description of assessors (17 CFR 229.106(b)(1)(ii)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 2, AU 3, CA 1, CM 5, CP 5, IA 4, IR 3, MA 1, PS 1, RA 2, SA 2, SC 2, SI 6), 287 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware in season, OT vendor remote access, the AQ-02 pivot cloud service, fertigation change control, SCADA recovery, field network concentration, disclosure);
- cover CSF 2.0 subcategories rated High gap in P03;
- protect command integrity and safe operation (the High-baseline supplements in P02 section 6: CM-5(1), SI-6, SI-7 with SI-7(1));
- are common controls the FMICP inherits and that no other assessment covered this year (identity, logging, OT gateway, network).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-015; R-016; R-003; 20 CFR 655.122(j)(1) | Comprehensive | Comprehensive | About 2,100 FMIS and SCADA account events 2026-01-01 to 2026-06-30; about 740 terminations of year-round staff with FMIS or SCADA access (62 at AQ-01 and AQ-02) | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AQ) | 23 / 3 |
| AC-2(3) | R-015 | Focused | Comprehensive | 3,840 seasonal FMIS accounts (2025-26 season); 2,960 year-round FMIS and SCADA accounts | 100% (data analytic) | 2 / 2 |
| AC-3 | R-047 | Focused | Focused | About 6,800 FMIS users; about 420 SL-1 grower tenants | 25 users (random); 5 tenant isolation tests | 1 / 0 |
| AC-5 | R-006; R-037 | Comprehensive | Comprehensive | 19 users with the combined FMIS planner role; SCADA role matrix | 100% | 1 / 1 |
| AC-6 | R-057 | Focused | Focused | About 4,300 PAM elevation sessions to FMICP servers, SCADA masters, and cloud accounts | 25 sessions (random) | 1 / 0 |
| AC-17 | R-004; R-005 | Comprehensive | Comprehensive | 5 integrators; 4 packing line vendors; 1 pivot cloud service; the OT remote access gateway | 100% of remote access paths (network discovery scan and firewall review) | 2 / 2 |
| AC-19 | R-016; R-054 | Focused | Focused | About 6,500 rugged tablets and phones (about 260 at AQ-01) | 25 devices (random, 5 at AQ-01) | 3 / 1 |
| AT-2 | R-024; R-023 | Basic | Focused | About 6,600 workers required to train (2025-26) | 60 training records (random); 6 months of phishing exercise results | 10 / 0 |
| AT-3 | R-033 | Focused | Comprehensive | About 380 irrigation technicians and 34 engineers; INT-1 to INT-5 staff with OT access | 40 technicians and engineers (random); 100% of integrator attestations | 7 / 2 |
| AU-2 | R-027; R-006 | Focused | Focused | n/a (configuration) | 6 event types generated in test (PLC download, recipe change, setpoint change, gateway session, FMIS record edit, admin login) | 6 / 0 |
| AU-6 | R-013; R-058 | Comprehensive | Comprehensive | 26 weeks of SOC review records; about 1,420 log sources | 5 weeks (random); 100% of log sources (inventory reconciliation) | 2 / 1 |
| AU-9 | R-057 | Basic | Focused | n/a (configuration) | Write-once archive settings inspected; deletion attempt tested | 2 / 0 |
| CA-7 | 17 CFR 229.106(b)(1); P02 continuous monitoring | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-006; R-014 | Focused | Focused | Baselines for SCADA servers, HMIs, engineering workstations, and PLC programs | 100% of baseline documents; 10 components compared | 5 / 0 |
| CM-3 | R-006; R-014 | Comprehensive | Comprehensive | About 1,180 OT changes (PLC logic, setpoints, recipes) 2026-01-01 to 2026-06-30 | 40 changes (random) | 7 / 3 |
| CM-5(1) | R-014; R-006 | Focused | Comprehensive | About 410 pump stations | 100% (engineering access path review) | 1 / 1 |
| CM-6 | R-009; R-008 | Focused | Comprehensive | 48 HMIs; about 520 LoRaWAN gateways; pivot modems | 48 HMIs (full); 60 gateways (random); 25 pivot modems (random) | 5 / 1 |
| CM-8 | R-011 | Comprehensive | Comprehensive | About 45,500 OT and IoT devices | 60 field devices traced to the inventory (random, 3 regions) | 5 / 1 |
| CP-2 | R-012; R-007 | Comprehensive | Focused | n/a (plan) | FMICP contingency plan v3 and 3 regional freeze plans examined; 4 interviews | 24 / 0 |
| CP-4 | R-007; R-012 | Focused | Focused | 1 annual DR test; 6 November freeze drills | 100% | 4 / 1 |
| CP-8 | R-021 | Focused | Comprehensive | About 45,500 field devices; 410 pump stations | 100% (carrier and radio coverage review) | 0 / 1 |
| CP-9 | R-019; R-001 | Focused | Focused | About 180 daily backup jobs for FMICP components; AQ-01 farm servers | 25 jobs (random); 1 restore observed; AQ-01 backup configuration inspected | 4 / 2 |
| CP-10 | R-012 | Focused | Focused | 1 DR test | 100% | 0 / 2 |
| IA-2 | R-016; R-005 | Focused | Comprehensive | About 6,800 FMIS users; AQ-01 tally devices; AQ-02 pivot service accounts | 25 sign-ins (random); 100% of AQ-01 and AQ-02 account lists | 1 / 1 |
| IA-2(1) | R-057 | Focused | Comprehensive | About 290 privileged accounts for FMICP, SCADA, and cloud | 100% | 1 / 0 |
| IA-3 | R-008 | Focused | Focused | About 2,300 pivot panels | 25 panels (random) in a maintenance window | 0 / 1 |
| IA-5 | R-009; R-005 | Focused | Comprehensive | 48 HMIs; about 520 LoRaWAN gateways; vaulted OT service accounts; AQ-02 pivot service accounts | 100% of HMIs; 60 gateways (random); 100% of vaulted accounts | 8 / 2 |
| IR-4 | R-001; R-006 | Focused | Focused | About 230 security incidents 2026-01 to 2026-06 (4 OT-related) | 25 incidents (random) plus all 4 OT incidents | 13 / 0 |
| IR-6 | R-018 | Basic | Focused | About 230 incidents; 20 staff interviews | 25 incidents; 20 staff (including 6 control center operators) | 2 / 0 |
| IR-8 | R-017 | Comprehensive | Focused | n/a (plan) | IR plan v5 and materiality playbook examined; interviews with the General Counsel, CFO, CISO, and Vice President, Investor Relations | 15 / 2 |
| MA-4 | R-004; R-032 | Comprehensive | Comprehensive | About 2,900 vendor remote sessions 2026-04 to 2026-06 | 60 sessions (random) | 5 / 3 |
| PS-4 | R-015; R-003 | Comprehensive | Comprehensive | About 740 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | P01 method; 17 CFR 229.106(b)(1) | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-008; R-011 | Focused | Focused | About 3,400 open vulnerability findings on FMICP components (IT and OT) | 60 findings (random) | 8 / 1 |
| SA-9 | R-030; R-005; R-004 | Focused | Comprehensive | 14 external services supporting the FMICP | 100% | 4 / 2 |
| SA-22 | R-010 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-003; R-005 | Comprehensive | Focused | n/a (architecture) | Rule review of 6 control center OT firewalls; reachability test from an AQ-01 farm office network | 4 / 2 |
| SC-8 | R-008 | Basic | Focused | All FMICP interfaces and field links | 100% (TLS scan; APN segment capture in a maintenance window) | 0 / 1 |
| SI-2 | R-008; R-010 | Focused | Focused | About 610 OT patch tickets 2026-01 to 2026-06 | 60 tickets (random) | 9 / 1 |
| SI-3 | R-010; R-001 | Focused | Focused | SCADA servers, engineering workstations, and 48 HMIs | 100% (EDR coverage report) | 7 / 1 |
| SI-4 | R-013 | Focused | Focused | 6 control centers; 410 pump stations | Sensor coverage review; 2 test events at monitored stations | 11 / 1 |
| SI-6 | R-006 | Focused | Focused | About 140 fertigation and chemigation skids | 25 skids (random) checklists; 2 interlock tests observed | 6 / 1 |
| SI-7 | R-006; R-014 | Comprehensive | Focused | n/a | PLC program comparison process and 3 monthly comparison reports examined | 5 / 1 |
| SI-7(1) | R-006 | Focused | Focused | n/a | 3 monthly comparison runs | 2 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, MA-4, RA-5, and SI-2.
- **Key manual controls, populations of 50 to 250, or where the population is large but the test is costly in the field:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3 and AT-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AC-19, CP-9, IA-2, IA-3, IR-4, IR-6, and SI-6.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 6,800 FMIS and SCADA accounts for inactivity, all 48 HMIs for default credentials, all remote access paths by network discovery).
- **Stratification:** terminations were stratified so the acquired operations (about 8% of the population) got 10 of 60 items; field device traces were spread across 3 regions (R1, R3, R4).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key command-integrity or safety control (CM-3, CM-5(1), AC-5, SI-6, SI-7) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, FMIS and SCADA role matrices, OT change tickets and bench test records, PLC program comparison reports, seasonal interlock checklists, backup and DR test reports, vulnerability and OT monitoring reports, the vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Irrigation and Water Resources; Vice President, Digital Agronomy; SCADA Engineering Manager; FMIS Platform Manager; 3 Irrigation Control Center Managers (R1, R3, R4); Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; General Counsel; CFO; CISO; Vice President, Investor Relations; 20 randomly selected staff, including 6 control center operators.
- **Test:** access tests with test accounts; credential tests on HMIs, LoRaWAN gateways, and pivot panels in maintenance windows; a remote tool discovery scan of the OT DMZ and field segments; a reachability test from an AQ-01 farm office network; passive packet capture on an APN segment; observation of 2 fertigation interlock tests and 1 restore; generation of 6 event types to confirm logging.

## 4. Rules of engagement
- No test could affect irrigation, fertigation, freeze protection, or packing. OT tests ran only in scheduled maintenance windows, with the regional Irrigation Control Center Manager's written approval and an operator present who could stop the test at any time.
- No active scanning of live PLCs or pivot panels outside a maintenance window. Passive methods came first (SP 800-82 Rev. 3 section 6.1.3). Credential tests used read-only logins and changed no settings.
- Fertigation and chemigation skids were observed, never operated, by the assessors; interlock tests were run by the company's technicians.
- The AQ-01 reachability test used an audit-owned laptop with no company data, pre-approved by the CISO and the Vice President, Integration Management Office.
- No personal information left the company's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default credentials on 3 pump station HMIs and 11 LoRaWAN gateways (reported 2026-08-06; fixed 2026-08-20).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests; maintenance windows booked with the 6 control centers |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); OT tests in R1, R3, and R4 maintenance windows |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Irrigation and Water Resources |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (287 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 240 |
| Other than satisfied | 47 |
| **Total** | **287** |

**Controls with at least one Other than satisfied statement: 32 of 44:** AC-2, AC-2(3), AC-5, AC-17, AC-19, AT-3, AU-6, CM-3, CM-5(1), CM-6, CM-8, CP-4, CP-8, CP-9, CP-10, IA-2, IA-3, IA-5, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-3, SI-4, SI-6, SI-7, SI-7(1).

**Fully Other than satisfied:** CP-8, CP-10, IA-3, SC-8 (each has one or two determination statements).

**Themes:**
1. **OT third-party access** drives the remote access (AC-17), maintenance (MA-4), supplier (SA-9), and training (AT-3) findings: INT-4, INT-5, two packing line vendors, and the AQ-02 pivot cloud service work outside the OT gateway.
2. **Command integrity at the same stations:** changes without approval (CM-3), programming without PAM (CM-5(1)), the combined planner role (AC-5), integrity checks that skip 120 stations (SI-7, SI-7(1)), and paper-only interlock verification (SI-6).
3. **Acquired operations:** identity (AC-2, PS-4, IA-2, AC-19), logging (AU-6), network (SC-7), backups (CP-9), and shared pivot service credentials (IA-5).
4. **Field OT hygiene:** default credentials (IA-5, CM-6), the incomplete inventory (CM-8), pivot modem firmware and authentication (RA-5, SI-2, IA-3, SC-8), unsupported HMIs (SA-22, SI-3), and monitoring coverage (SI-4).
5. **Resilience and disclosure:** SCADA recovery time (CP-10), carrier concentration (CP-8), freeze drills without a cyber scenario (CP-4), and the materiality process (IR-8).

**Strengths:** privileged access (AC-6, IA-2(1)), access enforcement and SL-1 tenant isolation (AC-3), event logging and write-once archives (AU-2, AU-9), continuous monitoring (CA-7), baselines (CM-2), the contingency plan itself (CP-2), awareness training in English and Spanish (AT-2), incident handling and reporting (IR-4, IR-6), and the risk assessment (RA-3) were all Satisfied.

**New finding during testing:** default credentials on 3 pump station HMIs and 11 LoRaWAN gateways (IA-05e.). Added to the risk register as R-009 and to POAM-010.

## 7. POA&M summary
`poam.csv` holds 24 items: 21 from this assessment and 3 carried from other deliverables so leadership tracks one list: POAM-016 (dealer access, P03), POAM-020 (traceability readiness, P03), and POAM-021 (AI-001 bias testing and committee reviews, P10).

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 13 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

Items due before the 2026-27 freeze season (on or before 2026-12-31) are the conditions of the FMICP authorization (P02 section 4.2): POAM-010, POAM-004, and the POAM-002 interim milestone.

## 8. Conclusion
Internal Audit concludes that the FMICP control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, backup, training, and incident handling operate effectively. The exceptions concentrate in OT third-party access, command integrity at the stations those vendors support, and controls that depend on integrating the acquired operations. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
