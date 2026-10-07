# Security Assessment Plan and Report: Cris Santos Company | Chemical | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded specialty chemical formulator and packager) |
| System assessed | Gulf Coast Complex Process Control and Batch Management System (GC-PCBMS), CSC-SYS-OT-PL01, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Chemical |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, two IT auditors, and an OT audit specialist under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls, and none has regularly assigned cybersecurity duties at PLT-01, so the work also meets the independence test for MTSA Cybersecurity Plan audits (33 CFR 101.630(f)(4)). The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork; OT testing at PLT-01 on 2026-08-11 to 2026-08-13 during a planned ammonia unit outage); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the GC-PCBMS authorization (P02 section 4.2); input to the PLT-01 MTSA Cybersecurity Assessment (101.650(e)(1)) and to the RMP and PSM compliance audits (40 CFR 68.79; 29 CFR 1910.119(o)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **42 controls (AC 5, AT 2, AU 2, CA 1, CM 5, CP 4, IA 2, IR 3, MA 2, MP 1, PE 1, PL 1, PS 1, RA 2, SA 2, SC 2, SI 4, SR 2), 334 determination statements.** Every determination statement of each selected control was assessed. Controls were selected because they:
- address the Very High and High risks in P01 (shared OT services, the integrator-account intrusion scenario, SIS integrity, changes outside MOC, KEVs, OT recovery);
- cover MTSA measures in 101.650 with gaps in P03;
- protect the safety and integrity of the process (SI-7, SC-24, MA-2, CM-3);
- are common controls the GC-PCBMS inherits (gateway, vault, SOC, identity) that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-001; R-036; 101.650(a)(6)-(7) | Comprehensive | Comprehensive | 412 OT directory accounts; 61 integrator accounts with PLT-01 targets on the gateway; 118 PLT-01 leavers with OT access (2026-01 to 2026-06) | 100% of accounts (data analytic); 25 leavers (random) | 23 / 3 |
| AC-3 | R-001; R-016 | Focused | Focused | 5 DCS role levels; 412 accounts | 25 accounts (random) tested against role privileges | 1 / 0 |
| AC-4 | R-002; R-026 | Focused | Comprehensive | OT DMZ flows (order relay, historian replication) | 100% of OT DMZ rules for these flows; reverse-path test from Cloud provider A | 1 / 0 |
| AC-6 | R-016 | Focused | Focused | 22 engineer and administrator accounts | 100% | 1 / 0 |
| AC-17 | R-001; R-011; 101.650(a)(4), (f)(3) | Comprehensive | Comprehensive | Remote access paths into PLT-01 OT; 1,940 gateway sessions (2026-01-01 to 2026-06-30) | 100% of paths (firewall review); 60 sessions (random) | 4 / 0 |
| AT-2 | R-015; 101.650(d) | Focused | Comprehensive | 3,540 PLT-01 employees and contractors with IT or OT access | 100% (learning system analytic); content reviewed | 9 / 1 |
| AT-3 | 101.650(d)(2); 49 CFR 172.704(a)(5) | Focused | Focused | 64 key personnel; 310 operators | 100% of key personnel; 25 operators (random) | 9 / 0 |
| AU-2 | R-006; 101.650(c)(1) | Focused | Focused | STD-01.6 event list | 6 event types generated in test during the ammonia unit outage | 6 / 0 |
| AU-6 | R-006; R-001; 101.650(h)(2) | Comprehensive | Comprehensive | 26 weeks of SOC OT review records; SIEM use case list | 5 weeks (random); 100% of OT use cases | 2 / 1 |
| CA-7 | Continuous monitoring | Focused | Basic | 6 monthly OT metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-004; 101.650(b)(1) | Focused | Comprehensive | Baselines for DCS servers, EWS, operator stations, OT DMZ servers, terminal PLCs | 100% | 4 / 1 |
| CM-3 | R-004; 40 CFR 68.75 | Comprehensive | Comprehensive | 1,326 PLT-01 DCS change log entries (2026-01 to 2026-06) | 40 changes (random) traced to MOC records | 7 / 3 |
| CM-5 | R-016 | Focused | Focused | 6 EWS; SIS key log | 100% | 6 / 0 |
| CM-7 | R-008; R-031; 101.650(b)(2) | Focused | Comprehensive | 50 OT hosts (6 server pairs, 38 operator stations, 6 EWS) | 100% (allowlisting console analytic); port scans of 10 hosts | 5 / 1 |
| CM-8 | R-009; 101.650(b)(3)-(4) | Comprehensive | Comprehensive | OT asset inventory; 64 PLCs | 100% of PLCs; 40 assets traced from the floor to the inventory | 4 / 2 |
| CP-2 | R-007; 101.650(g) | Comprehensive | Focused | PLT-01 OT contingency plan v2 | Plan examined; 4 interviews (Plant Manager, Controls Engineering Manager, CySO, shift supervisor) | 22 / 2 |
| CP-4 | R-007; 101.650(g)(4) | Focused | Comprehensive | Restore tests 2025-2026 | 100% | 4 / 1 |
| CP-9 | R-061; 101.650(g)(4) | Focused | Focused | 182 daily backup jobs | 25 jobs (random); 1 restore of a recipe set observed | 5 / 1 |
| CP-10 | R-007 | Focused | Focused | Restore tests | 100% | 0 / 2 |
| IA-2 | R-001 | Focused | Comprehensive | 412 OT accounts; gateway accounts | 100% (analytic); 25 logons | 2 / 0 |
| IA-5 | R-014; 101.650(a)(2) | Focused | Comprehensive | 76 OT devices with web or login interfaces | 100% (tested during the outage with vendor approval) | 9 / 1 |
| IR-4 | R-002; 101.650(g)(2) | Focused | Focused | 38 OT-related security incidents (2026-01 to 2026-06) | 25 (random) | 13 / 0 |
| IR-6 | 33 CFR 6.16-1 | Basic | Focused | 38 incidents; 20 staff | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-012; Form 8-K Item 1.05 | Comprehensive | Focused | IR plan v5; materiality playbook | Plan examined; interviews with General Counsel, CFO, CISO | 14 / 3 |
| MA-2 | 40 CFR 68.73 | Focused | Focused | Proof tests and DCS maintenance work orders | 40 (random) | 9 / 0 |
| MA-4 | R-013 | Focused | Focused | Vendor sessions | 60 sessions (same sample as AC-17) | 8 / 0 |
| MP-7 | R-032; 101.650(i)(2) | Focused | Comprehensive | 6 EWS; 38 operator stations | 100% | 1 / 1 |
| PE-3 | 101.650(i)(1) | Basic | Focused | Control room and rack room badge events | 40 events (random); walkthrough 2026-08-11 | 12 / 0 |
| PL-2 | P02 SSP | Focused | Basic | GC-PCBMS SSP v2.0 | Plan examined | 38 / 0 |
| PS-4 | R-036; 101.650(a)(7) | Comprehensive | Comprehensive | 118 PLT-01 leavers with OT access | 25 (same sample as AC-2) | 3 / 2 |
| RA-3 | P01; 40 CFR 68.67 | Focused | Basic | 2026 risk analysis; PHA records | Documents examined | 7 / 1 |
| RA-5 | R-005; 101.650(e)(3) | Focused | Comprehensive | 412 open vulnerability findings on PLT-01 OT | 100% (analytic) | 8 / 1 |
| SA-9 | R-013; 101.650(f)(2) | Focused | Comprehensive | 9 OT suppliers serving PLT-01 | 100% | 5 / 1 |
| SA-22 | R-031 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-034; 101.650(h)(1) | Comprehensive | Comprehensive | 212 OT DMZ firewall rules | 100%; reachability tests from the business network | 4 / 2 |
| SC-24 | Process safety | Focused | Focused | SIS and controller failure modes | Communication loss test on one controller pair during the outage | 1 / 0 |
| SI-2 | R-005; 101.650(e)(3)(i) | Focused | Focused | 86 OT patches released (2026-01 to 2026-06) | 25 (random) | 8 / 2 |
| SI-3 | R-008 | Focused | Focused | 50 OT hosts; media kiosk | 100% (console); test file at the kiosk | 8 / 0 |
| SI-4 | R-006; 101.650(h)(2) | Focused | Focused | OT monitoring coverage; SIEM use cases | Coverage map; 2 test events | 10 / 2 |
| SI-7 | R-003; R-061 | Comprehensive | Focused | SIS programs; recipe store | Comparison records 2025-2026 | 4 / 2 |
| SR-6 | R-013 | Focused | Comprehensive | 6 DCS and PLC integrators | 100% | 0 / 1 |
| SR-11 | R-030 | Focused | Focused | Controllers and SIS cards received in 2026 | 15 receipts (all) | 5 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key controls, large populations, zero deviations expected:** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-17 and MA-4 (gateway sessions).
- **Controls where walkthroughs showed deviations were likely:** a smaller random sample (40 for CM-3, 25 for the AC-2 and PS-4 leaver test) to estimate the deviation rate. When the sample already showed deviations well above the 5% tolerable rate (7 of 40; 3 of 25), the statement was concluded Other than satisfied without extending the sample.
- **Configuration-enforced and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AT-3, CP-9, IA-2, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual or one-time, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 412 OT accounts, all 61 integrator accounts, all 412 open OT vulnerability findings, all 212 OT DMZ firewall rules, and all 76 OT devices with a login interface for default credentials).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects a safety function or a PSM process (CM-3, SI-7, CP-2, SC-24) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), OT directory and gateway records, DCS change logs and MOC records, SIS comparison records, backup and restore test reports, the KEV report and patch staging records, firewall rule bases, monitoring coverage and SIEM use cases, vendor contracts and assessments, the incident response plan and materiality playbook, disclosure committee charter and minutes, training records.
- **Interview:** PLT-01 Plant Manager; PLT-01 Controls Engineering Manager; PLT-01 CySO; PLT-01 Facility Security Officer; Process Safety Manager, PLT-01; 3 shift supervisors; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Third-Party Risk Management; General Counsel; CFO; CISO; 20 randomly selected PLT-01 staff.
- **Test:** test logons against DCS roles; a reverse-path test from Cloud provider A toward the OT DMZ; default-credential tests on OT devices; USB device tests on EWS and operator stations; generation of 6 audit event types and a test alarm limit change on a non-safety tag; a communication-loss test on one controller pair; reachability tests from the business network.

## 4. Rules of engagement
- **Safety first.** No active test touched a running process. OT tests ran only during the planned ammonia unit outage (2026-08-11 to 2026-08-13), on equipment released by the PLT-01 Plant Manager under a work permit, with a controls engineer and the shift supervisor present. The test alarm limit change used a non-safety tag in the outage area and was reversed under MOC.
- No active scanning of controllers or SIS logic solvers; vulnerability data came from passive monitoring and vendor-approved methods.
- Default-credential tests were approved by the DCS and PLC vendors.
- SSI (network maps, Cybersecurity Plan drafts) was reviewed in the FSO's SSI repository and not copied into workpapers.
- Critical exposures were reported to the CISO and the CySO within 24 hours. One was: default vendor passwords on the tank gauging server and two truck rack PLC web interfaces (reported 2026-08-12; changed 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); OT testing at PLT-01 on 2026-08-11 to 2026-08-13 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, Director of OT Security, and PLT-01 Plant Manager |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (334 rows), and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 296 |
| Other than satisfied | 38 |
| **Total** | **334** |

**Controls with at least one Other than satisfied statement: 24 of 42:** AC-2, AT-2, AU-6, CM-2, CM-3, CM-7, CM-8, CP-2, CP-4, CP-9, CP-10, IA-5, IR-8, MP-7, PS-4, RA-3, RA-5, SA-9, SA-22, SC-7, SI-2, SI-4, SI-7, SR-6.

**Fully Other than satisfied:** CP-10 (both statements) and SR-6 (single statement).

**Themes:**
1. **The cyber layer around the safety systems** is the main weakness: changes outside MOC (CM-3), manual SIS comparison (SI-7), no detection of alarm limit or keyswitch changes (AU-6, SI-4), and unproven OT recovery (CP-2, CP-4, CP-10).
2. **MTSA readiness at PLT-01:** KEVs without compensating controls (RA-5, SI-2), default passwords (IA-5), unscanned media on EWS (MP-7), contractor training (AT-2), and an incomplete inventory (CM-8, CM-2).
3. **Third parties:** shared integrator accounts on the gateway (AC-2) and missing supplier notification clauses (SA-9, SR-6).
4. **Disclosure readiness:** the materiality process does not cover OT incidents (IR-8).

**Strengths:** the one-way OT-to-cloud design (AC-4), remote access through the gateway with MFA, approval, and recording (AC-17, MA-4), DCS role enforcement and change restrictions (AC-3, AC-6, CM-5), physical security (PE-3), safe-state design (SC-24), proof testing (MA-2), incident handling and reporting (IR-4, IR-6), continuous monitoring metrics (CA-7), and the SSP itself (PL-2) were all Satisfied.

**New finding during testing:** default vendor passwords on the tank gauging server web interface and two truck rack PLC web interfaces (IA-05e.). Added to the risk register as R-014 and to POAM-013.

## 7. POA&M summary
`poam.csv` holds 25 items: 19 from this assessment and 6 carried from the P03 gap analysis and P10 (POAM-008, POAM-014, POAM-015, POAM-017, POAM-018, POAM-019), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 13 |
| Moderate | 12 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the GC-PCBMS control environment is **effective with exceptions**. The architecture (OT DMZ, one-way paths, central remote access, independent safety systems) and the enterprise common controls for identity, remote access, physical security, and incident handling operate effectively. The exceptions concentrate in the controls that connect cybersecurity to process safety (change control, SIS integrity, OT detections, and OT recovery) and in MTSA measures that must be in place before the Cybersecurity Plan is submitted. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
