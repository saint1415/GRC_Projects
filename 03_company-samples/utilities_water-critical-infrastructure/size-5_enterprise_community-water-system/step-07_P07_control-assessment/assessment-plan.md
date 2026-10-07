# Security Assessment Plan and Report: Cris Santos Company | Water and Wastewater Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of state-regulated community water utilities) |
| System assessed | Gulf Coast Regional Water Treatment SCADA System (GCR-WTSS), CSC-OT-GCR-001, per the SSP (P02), including the enterprise common controls it inherits (OT remote access gateway, OT monitoring, identity, SOC, network, third-party risk) |
| Tier / Vertical | Enterprise / Water and Wastewater Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`), applied to OT with NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and two IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, co-sourced with an independent OT assessment firm (two OT assessors) that has no other engagement with the Gulf Coast Regional System. None of the assessors designs or operates the controls. This is the company's **first independent OT assessment**: the 2025 OT control review was a self-assessment by the OT security team that operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the safety, environmental, and risk committee on 2026-09-10 |
| Also satisfies | Evidence for the cyber element of the Gulf Coast Regional System RRA and ERP (42 U.S.C. 300i-2(a)(1)(A)(ii), (b)(1)); annual assessment for the GCR-WTSS authorization (P02 section 4.2); Internal Audit testing behind the Item 106 description of third-party assessors (17 CFR 229.106(b)(1)(ii)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 4, AT 2, AU 4, CA 2, CM 6, CP 5, IA 3, IR 3, MA 2, PE 2, PS 2, RA 2, SA 2, SC 3, SI 3, SR 1), 313 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (remote access to OT, PLC logic integrity, unsupported components, telemetry exposure, recovery, disclosure);
- cover High gaps in the cyber element benchmark in P03;
- protect the integrity and availability of treatment and chemical feed control (the GCR-WTSS is categorized High);
- are common controls the GCR-WTSS inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-016; R-015; POL-02 4.5 | Comprehensive | Comprehensive | 1,042 OT domain account events for GCR (2026-01-01 to 2026-06-30); 1,318 terminations of staff with OT domain access enterprise-wide (204 Florida region) | 60 account events (random); 60 terminations (stratified: 45 enterprise, 15 Florida region) | 23 / 3 |
| AC-3 | R-004; POL-02 4.2 | Focused | Focused | About 280 GCR OT domain users | 25 users (random); engineer role list in full | 1 / 0 |
| AC-6 | R-032; POL-02 4.8 | Focused | Focused | 1,560 PAM elevation sessions to GCR OT hosts | 25 sessions (random) | 1 / 0 |
| AC-17 | R-001; R-017; P03 G-028, G-029 | Comprehensive | Comprehensive | 1,214 GCR vendor sessions (2026-01-01 to 2026-06-30); remote access paths at all 126 systems | 25 sessions (random); 100% of systems for path coverage | 2 / 2 |
| AT-2 | R-057; POL-05 4.2 | Basic | Focused | 12,000 workforce | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-022; P03 G-031 | Focused | Focused | About 3,400 OT-role staff (operators, SCADA technicians, OT engineers) | 60 (random) | 8 / 1 |
| AU-2 | R-037 | Focused | Focused | n/a (configuration) | 6 event types generated in test (sign-in, setpoint change, logic download, mode change, gateway session, firewall deny) | 6 / 0 |
| AU-6 | R-037; R-013 | Comprehensive | Comprehensive | 26 weekly GCR OT log reviews; 38 GCR log sources | 13 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-032 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-12 | R-037 | Focused | Comprehensive | 64 operator HMIs, 22 panel HMIs, servers, and firewalls in the GCR-WTSS | 100% of HMI log sources | 2 / 1 |
| CA-2 | POL-01 4.9; P03 G-047 | Focused | Basic | n/a | 2026 assessment plan and prior self-assessment examined | 11 / 0 |
| CA-7 | POL-01 4.12 | Focused | Basic | 6 monthly OT metrics packages | 3 months (random) | 11 / 0 |
| CM-2 | R-008 | Focused | Focused | GCR OT hosts (servers, HMIs, engineering workstations) | 15 hosts (random) | 5 / 0 |
| CM-3 | R-004; P03 G-034 | Comprehensive | Comprehensive | 186 GCR PLC and SCADA change records (2026-01-01 to 2026-06-30) | 40 changes (random) | 8 / 2 |
| CM-5 | R-004 | Focused | Focused | 186 changes | 10 changes traced to key switch logs and download alerts | 6 / 0 |
| CM-6 | R-006; P03 G-034 | Focused | Comprehensive | 124 GCR private LTE site gateways; 15 OT hosts | 100% of gateways (external exposure scan and configuration export); 15 hosts | 5 / 1 |
| CM-7 | R-064 | Focused | Focused | GCR OT hosts | 15 hosts (random) | 6 / 0 |
| CM-8 | R-035; P03 G-023 | Comprehensive | Comprehensive | About 4,100 GCR components in the OT inventory | 60 physical field devices traced to the inventory (random, 8 sites) | 5 / 1 |
| CP-2 | R-010; P03 G-014 | Comprehensive | Focused | n/a (plan) | GCR-WTSS contingency annex and ERP examined; 4 interviews | 24 / 0 |
| CP-4 | R-010 | Focused | Focused | 2026-05-12 transfer exercise; 6 plant drills | 100% | 5 / 0 |
| CP-7 | R-010; P05 DEP-01 | Focused | Comprehensive | 1 transfer exercise | 100% | 3 / 1 |
| CP-9 | P03 G-033 | Focused | Focused | 412 GCR PLCs with offline backups | 40 controllers (random) | 5 / 1 |
| CP-10 | R-010 | Focused | Focused | 1 transfer exercise; 1 annual restore test | 100% | 1 / 1 |
| IA-2 | R-015; P03 G-027 | Basic | Comprehensive | About 280 GCR OT domain accounts; 22 TP-C panel HMIs | 100% (account analytic) | 1 / 1 |
| IA-2(1) | R-032 | Focused | Comprehensive | 31 privileged OT accounts | 100% | 1 / 0 |
| IA-5 | R-006; P03 G-027 | Focused | Comprehensive | 124 site gateways; 412 PLCs and 166 RTUs (credential capability) | 100% (exposure scan and vault reconciliation) | 9 / 1 |
| IR-4 | R-002; R-014 | Focused | Focused | 148 security incidents with OT relevance (2025-07-01 to 2026-06-30) | 25 incidents (random) | 13 / 0 |
| IR-6 | P03 G-048, G-056 | Basic | Focused | 148 incidents; 20 operator interviews | 25 incidents; 20 operators | 2 / 0 |
| IR-8 | R-007; P03 G-059, G-060 | Comprehensive | Focused | n/a (plan) | IR plan and materiality playbook examined; interviews with the General Counsel, CFO, CISO, and COO | 15 / 2 |
| MA-4 | R-017; R-005 | Focused | Comprehensive | 1,214 GCR vendor sessions | 25 (same sample as AC-17) | 7 / 1 |
| MA-5 | R-005 | Focused | Comprehensive | 23 integrators with remote access; GCR site visitor logs | 100% of integrators; 25 site visits (random) | 3 / 1 |
| PE-3 | R-023; R-047 | Focused | Focused | GCR ROCC, 3 plants, 28 boosters, 37 tanks | Badge reports for 25 days (random); 10 sites inspected | 12 / 0 |
| PE-6 | R-024; P03 G-030 | Focused | Comprehensive | 28 GCR booster stations | 100% (door alarm test) | 4 / 1 |
| PS-4 | R-016 | Comprehensive | Comprehensive | 1,318 terminations | 60 (same sample as AC-2) | 4 / 1 |
| PS-7 | R-005 | Focused | Comprehensive | 23 integrators with remote access | 100% | 4 / 1 |
| RA-3 | POL-01 4.3 | Focused | Basic | n/a | 2026 enterprise risk analysis and GCR RRA review examined | 8 / 0 |
| RA-5 | R-036; P03 G-035 | Focused | Focused | 2,960 open OT vulnerability findings enterprise-wide (612 at GCR) | 60 findings (random) | 8 / 1 |
| SA-9 | R-005; P03 G-021 | Focused | Comprehensive | About 140 OT vendor contracts | 100% | 4 / 2 |
| SA-22 | R-008; P03 G-046 | Focused | Comprehensive | Unsupported component list for the GCR-WTSS | 100% | 1 / 1 |
| SC-7 | R-003; P03 G-037 | Comprehensive | Focused | n/a (architecture) | OT penetration test of the GCR OT DMZ and gateway; reachability test from the AQ-05 site network | 5 / 1 |
| SC-8 | R-012 | Basic | Focused | 138 GCR telemetry endpoints | 100% (protocol capture at the radio master and LTE core) | 0 / 1 |
| SC-24 | R-021; P03 G-015 | Focused | Focused | 3 GCR plants | Hardwired limits and alarms tested at TP-A, TP-B, and TP-C during drills | 1 / 0 |
| SI-2 | R-036; R-008 | Focused | Focused | 212 GCR patches (2026-01-01 to 2026-06-30) | 25 patches (random) | 9 / 1 |
| SI-4 | R-013; R-014; P03 G-039 | Focused | Focused | GCR monitoring sensors; enterprise coverage | Detection tests at the ROCC and TP-A (rogue device, program download, unusual protocol); coverage report | 11 / 1 |
| SI-7 | R-004 | Comprehensive | Focused | n/a | File integrity monitoring and PLC logic integrity controls examined | 5 / 1 |
| SR-6 | R-005; P03 G-045 | Focused | Comprehensive | 23 integrators | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic or a full test could cover every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-3, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250, and OT controls where each item needs a field check:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 and CP-9.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AC-17, MA-4, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 13 occurrences for the GCR OT log review (raised from the usual 5 because it is a key detective control at a High system); monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 124 site gateways for default credentials and internet exposure, all 28 booster station door alarms, all 23 integrators).
- **Stratification:** terminations were stratified so the Florida region, whose OT domain serves the GCR-WTSS, got 15 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key public-safety control (CM-3, CM-5, CP-9, SC-24) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP and tailoring record (P02), identity governance and PAM records, the Florida OT domain export, SCADA role matrix, change records and CAB minutes, PLC key switch logs, OT monitoring alerts, backup logs and fire safe contents, the contingency annex and ERP, exercise reports, vulnerability findings, vendor contracts and rosters, the incident response plan and materiality playbook, disclosure committee charter and minutes.
- **Interview:** Vice President, Gulf Coast Regional Operations; GCR SCADA Manager; two ROCC shift supervisors; Director of OT Security; Director of OT Engineering; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; Vice President, Resilience and Emergency Management; General Counsel; CFO; CISO; COO; 20 randomly selected operators.
- **Test:** access tests with test accounts; detection tests at the ROCC and TP-A (rogue device, program download to a test-rack PLC mirrored on the monitored network, unusual protocol); an OT penetration test of the GCR OT DMZ and gateway; a reachability test from the AQ-05 site network; an external exposure scan of telemetry addresses; protocol captures at the radio master and LTE core; door alarm tests at all 28 booster stations; hardwired limit and alarm checks during the scheduled plant drills; a restore observation on the TP-B test rack.

## 4. Rules of engagement
- No test could change a setpoint, a PLC program, or the state of any process. Tests touching OT ran in scheduled windows approved by the Vice President, Gulf Coast Regional Operations, with a licensed operator and the GCR SCADA Manager present, and every test had a stop condition.
- PLCs and RTUs were never actively scanned. Vulnerability evidence for controllers came from passive monitoring and the inventory. The program download test used a PLC on the TP-B test rack.
- The penetration test was limited to the OT DMZ, the gateway, and the boundary from the AQ-05 site network; it did not cross into control zones.
- No Restricted information (RRA, ERP, diagrams) left company systems; workpapers reference documents by ID and are stored in the restricted repository.
- Critical exposures were reported to the CISO within 24 hours. One was: default web administration on 9 site gateways reachable from the internet (reported 2026-08-12, fixed 2026-08-20).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests; rules of engagement signed |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Gulf Coast Regional Operations |
| 2026-09-10 | Presented to the audit committee and the safety, environmental, and risk committee |

Deliverables: this plan and report, `assessment-results.csv` (313 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 279 |
| Other than satisfied | 34 |
| **Total** | **313** |

**Controls with at least one Other than satisfied statement: 28 of 46:** AC-2, AC-17, AT-3, AU-6, AU-12, CM-3, CM-6, CM-8, CP-7, CP-9, CP-10, IA-2, IA-5, IR-8, MA-4, MA-5, PE-6, PS-4, PS-7, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SI-7, SR-6.

**Fully Other than satisfied:** SC-8 and SR-6 (each has a single determination statement).

**Themes:**
1. **PLC logic integrity** is the main system-specific weakness: no automated comparison of running logic with approved versions, missing post-change verification, and stale offline backups (CM-3, SI-7, CP-9).
2. **Remote and third-party access:** sessions approved after they started (AC-17, MA-4); integrator contracts, rosters, and attestations (SA-9, SR-6, MA-5, PS-7). At enterprise level, 29 systems are still outside the gateway, including AQ-04 to AQ-06 (AC-17, SC-7).
3. **Identity:** manual OT domain disablement (AC-2, PS-4) and shared TP-C panel accounts (IA-2).
4. **Exposure and legacy:** default credentials on internet-reachable site gateways (CM-6, IA-5), 4 unsupported hosts (SA-22), unauthenticated radio telemetry (SC-8), and OT findings past SLA (RA-5, SI-2).
5. **Recovery:** the backup control center transfer missed its 2-hour target (CP-7, CP-10), although a full restore from offline images met the 8-hour RTO.
6. **Disclosure readiness:** the materiality playbook has no OT or public health scenario and no operations member (IR-8).

**Strengths:** least privilege and privileged access (AC-3, AC-6, IA-2(1)), protected logs (AU-9), the zone architecture and OT DMZ at GCR (the penetration test did not reach a control zone), detection at monitored plants (all test events detected within 15 minutes), physical access (PE-3), incident handling (IR-4, IR-6), and the engineered safeguards (SC-24: hardwired limits and alarms worked with SCADA disconnected at all three plants) were Satisfied.

**New finding during testing:** default web administration credentials on 9 internet-reachable site gateways (CM-06b., IA-05e.). Added to the risk register as R-006 and to POAM-009.

## 7. POA&M summary
`poam.csv` holds 23 items: 18 from this assessment (POAM-001 to POAM-018) and 5 carried from the P03 gap analysis, the risk register, and the AI assessment (POAM-019 to POAM-023), so leadership tracks one list. POAM-020 (monitoring coverage) was also confirmed by this assessment (SI-04c.01).

| Risk level | Items |
|---|---|
| High | 8 |
| Moderate | 13 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 18 |
| Open | 5 |

## 8. Conclusion
Internal Audit and the co-sourced OT firm conclude that the GCR-WTSS control environment is **effective with exceptions**. The engineered safeguards, the OT DMZ and zone architecture, privileged access, and detection at monitored plants operate effectively. The exceptions concentrate in PLC logic integrity, third-party access discipline, and recovery timing at GCR, and in enterprise common controls that depend on integrating the acquired systems. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
