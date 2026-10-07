# Security Assessment Plan and Report: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded independent crude oil producer) |
| System assessed | Field SCADA and Production Accounting System (FSPA), CSC-SYS-FSPA-001, per the SSP (P02), including the enterprise common controls it inherits; AQ-MC legacy SCADA tested where it connects to the FSPA or the enterprise network |
| Tier / Vertical | Enterprise / Mining, Quarrying, and Oil and Gas Extraction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`); OT test methods follow NIST SP 800-82 Rev. 3 cautions for operational systems |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors, and a contracted OT security specialist under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also serves | Annual assessment for the FSPA authorization decision (P02 section 4.2); evidence for SOC 2 readiness (P09) and the Item 106 description |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 2, AU 3, CA 2, CM 5, CP 5, IA 3, IR 3, MA 1, PE 1, PS 1, RA 2, SA 2, SC 2, SI 4, SR 1), 300 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware reaching OT, AQ-MC integration, vendor paths into the field, integrity of control, failover);
- cover High gaps in P03 (identity, remote access, segmentation, change control, recovery, disclosure);
- protect integrity and recovery (the High-baseline supplements in P02 section 6);
- are common controls the FSPA inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-006; P03 PR.AA-01 | Comprehensive | Comprehensive | 1,412 terminations of staff and contractors with OT access (2026-01-01 to 2026-06-30); 2,310 OT domain and local SCADA accounts | 60 terminations (stratified: 45 Permian and IOC, 8 Florida, 7 AQ-MC; reperformed and extended from the P03 sample); 100% of OT accounts by directory analytic | 21 / 5 |
| AC-2(3) | R-006 | Focused | Comprehensive | 2,310 OT accounts | 100% (directory analytic) | 3 / 1 |
| AC-3 | R-029 | Focused | Focused | 2,310 OT accounts; SCADA role matrix | 25 accounts (random) | 1 / 0 |
| AC-4 | R-001; R-002 | Comprehensive | Comprehensive | Firewall rule sets at the IOC, BCC, and Florida IT/OT boundaries | 100% of rules (rule analytic) | 0 / 1 |
| AC-5 | R-010; R-012 | Comprehensive | Comprehensive | 96 users with controller programming rights; 140 hydrocarbon accounting users | 100% (role analytic) | 1 / 1 |
| AC-6 | R-029; R-055 | Focused | Focused | 2,960 PAM elevation sessions to OT DMZ and SCADA servers | 25 sessions (random) | 1 / 0 |
| AC-17 | R-003; R-002 | Comprehensive | Comprehensive | 6 remote access paths into OT; 210 vendors with remote access | 100% of paths | 2 / 2 |
| AT-2 | R-013; R-014 | Basic | Focused | 12,000 workforce; phishing simulation results | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-036 | Focused | Comprehensive | 840 staff in OT roles | 100% (learning system analytic) | 7 / 2 |
| AU-2 | R-057 | Focused | Focused | n/a (configuration) | 6 event types generated in test at the IOC | 6 / 0 |
| AU-6 | R-016; R-057 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 412 expected log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-12 | R-057 | Basic | Focused | n/a (configuration) | 6 IOC and BCC SCADA servers; 2 Florida servers | 2 / 1 |
| CA-2 | Program requirement (POL-01 4.9) | Focused | Basic | n/a | 2026 assessment plan and prior report examined | 11 / 0 |
| CA-7 | Program requirement | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-004; R-010 | Focused | Comprehensive | SCADA platform components at the IOC, BCC, Florida, and AQ-MC | 100% of baseline documents | 4 / 1 |
| CM-3 | R-010; R-004 | Comprehensive | Comprehensive | 612 OT changes (2026-01-01 to 2026-06-30) | 40 changes (random; reperformed and extended from the P03 sample) | 7 / 3 |
| CM-5 | R-004; R-029 | Focused | Focused | 9,300 controllers on the enterprise platform | 60 controllers (random; configuration read) | 5 / 1 |
| CM-6 | R-004 | Focused | Focused | 9,300 controllers; 140 HMIs | 60 controllers and 25 HMIs (random) | 5 / 1 |
| CM-8 | R-018 | Comprehensive | Comprehensive | About 11,000 field controllers | 60 physical devices traced to the inventory at 12 sites (random) | 4 / 2 |
| CP-2 | R-005; R-009 | Comprehensive | Focused | n/a (plan) | FSPA contingency plan v3 examined; 4 interviews | 22 / 2 |
| CP-4 | R-005; R-019 | Focused | Focused | Contingency tests for the IOC, BCC, Florida, and AQ-MC | 100% of 2026 tests | 4 / 1 |
| CP-7 | R-005 | Focused | Focused | n/a | BCC site inspection; failover test report | 3 / 1 |
| CP-9 | R-019; R-050 | Focused | Focused | 181 daily tier-1 backup jobs; OT program backups by region | 25 jobs (random); 1 restore observed; OT backups by region | 4 / 2 |
| CP-10 | R-005 | Focused | Focused | 1 failover test | 100% | 1 / 1 |
| IA-2 | R-023 | Focused | Comprehensive | 140 HMIs; 2,310 OT accounts | 100% of HMI logon configurations | 1 / 1 |
| IA-2(1) | R-055 | Focused | Comprehensive | 184 privileged OT and OT DMZ accounts | 100% | 1 / 0 |
| IA-5 | R-061 | Focused | Comprehensive | 16 LACT flow computers; 410 AQ-MC cellular modems | 100% (credential test, with operations approval) | 8 / 2 |
| IR-4 | R-001; R-060 | Focused | Focused | 212 security incidents (4 at AQ-MC) | 25 incidents (random) plus all 4 AQ-MC incidents | 13 / 0 |
| IR-6 | R-001 | Basic | Focused | 212 incidents; 20 field staff interviews | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-008; SEC Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan v5 and PRC-03.2 examined; interviews with the General Counsel, CFO, COO, and CISO | 15 / 2 |
| MA-4 | R-003 | Focused | Comprehensive | 1,180 gateway vendor sessions (2026 H1); ESP vendor cloud | 25 gateway sessions (random); ESP vendor path examined | 5 / 3 |
| PE-3 | R-033 | Basic | Focused | IOC, BCC, Florida control room; 12 field sites | 4 control rooms and 12 field sites visited | 12 / 0 |
| PS-4 | R-006 | Comprehensive | Comprehensive | 1,412 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | Program requirement | Focused | Basic | n/a | 2026 risk assessment examined | 8 / 0 |
| RA-5 | R-030 | Focused | Focused | 2,240 open OT vulnerability findings | 60 findings (random; reperformed and extended from the P03 sample) | 7 / 2 |
| SA-9 | R-031; R-003 | Focused | Comprehensive | 210 vendors with remote access | 100% (tracker analytic); 10 contracts examined | 4 / 2 |
| SA-22 | R-015 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-001; R-002; R-017 | Comprehensive | Focused | n/a (architecture) | Reachability tests from the AQ-MC network and from the internet | 4 / 2 |
| SC-8 | R-059 | Basic | Focused | About 6,500 cellular modems | 100% (carrier APN report) | 0 / 1 |
| SI-2 | R-030; R-022 | Focused | Focused | 212 IT patches; 48 OT patches | 25 IT and 25 OT patches (random) | 9 / 1 |
| SI-4 | R-016 | Focused | Focused | OT sites by monitoring coverage | Coverage report; detection test at 2 Permian facilities | 10 / 2 |
| SI-7 | R-012; R-010 | Comprehensive | Focused | n/a | Integrity tools and volume controls examined; 25 run ticket edits (random) | 3 / 3 |
| SI-7(1) | R-012 | Focused | Focused | n/a | Integrity check logs examined (3 months) | 2 / 1 |
| SR-6 | R-003; R-020 | Focused | Comprehensive | Tier-1 OT suppliers | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 and PS-4 (terminations), CM-5 and CM-6 (controller configuration), CM-8 (device trace), and RA-5.
- **Key manual controls, populations of 50 to 250, or high-risk populations:** 40 items, random selection. Used for CM-3 (612 OT changes; 40 chosen because changes at AQ-MC and Florida carry higher risk).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, IR-4, IR-6, MA-4, SI-2, and SI-7.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 2,310 OT accounts for inactivity, all 16 LACT flow computers and 410 AQ-MC modems for default credentials, all 6,500 modems for APN status).
- **Stratification:** terminations were stratified so Florida and AQ-MC (about 11% of the population) got 15 of 60 items.
- **Reuse of P03 samples:** where the P03 gap analysis had already drawn a sample from the same population (terminations, OT changes, OT vulnerability findings, controller configuration, device trace), Internal Audit reperformed those items and extended them rather than drawing a second sample.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key integrity control (CM-3, CM-5, AC-5, SI-7) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02) and OT tailoring register, identity governance, OT directory, and PAM records, firewall rule sets, OT change tickets and program repository logs, controller configurations, backup and failover test reports, the OT vulnerability register, vendor register and contracts, the IR plan and materiality procedure, disclosure committee minutes, run ticket audit trails and reconciliations.
- **Interview:** Chief Operating Officer; Vice President, Operations Technology and Automation; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; Vice President, Production and Revenue Accounting; General Counsel; CFO; CISO; regional operations leads at Florida and AQ-MC; 20 randomly selected Production Controllers and field staff.
- **Test:** credential tests on LACT flow computers and AQ-MC modems (with operations approval); reachability tests from the AQ-MC network and from the internet; controller mode reads through the SCADA platform (read-only); detection tests at 2 Permian facilities; a restore observation; failover test evidence review.

## 4. Rules of engagement (OT safety first)
- No test could change a setpoint, controller logic, or safety function. Controller tests were read-only and ran through the SCADA platform, not directly against devices.
- Credential tests on LACT flow computers ran only during scheduled proving windows with the Vice President, Midstream and Water's approval and a measurement technician present; modem tests were limited to the management interface.
- No active scanning of field devices. OT vulnerability data came from passive monitoring and vendor-approved tools (tailoring TR-04).
- The Production Controller on shift could stop any test at any time; none was stopped.
- No owner personal information left company systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO and the Director of OT Security within 24 hours. One was: default credentials on 37 internet-exposed AQ-MC modems and 3 LACT flow computers (reported 2026-08-12; interim fix 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests; rules of engagement signed by the COO |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including visits to the IOC, BCC, Florida control room, AQ-MC control room, and 12 field sites |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Operations Technology and Automation |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (300 rows), and `poam.csv` (23 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 246 |
| Other than satisfied | 54 |
| **Total** | **300** |

**Controls with at least one Other than satisfied statement: 33 of 44:** AC-2, AC-2(3), AC-4, AC-5, AC-17, AT-3, AU-6, AU-12, CM-2, CM-3, CM-5, CM-6, CM-8, CP-2, CP-4, CP-7, CP-9, CP-10, IA-2, IA-5, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SI-7, SI-7(1), SR-6.

**Fully Other than satisfied:** AC-4, SC-8, SR-6 (each has a single determination statement).

**Themes:**
1. **AQ-MC integration** drives the boundary (SC-7, AC-4), remote access (AC-17, MA-4), identity (AC-2, PS-4, IA-2), default credential (IA-5), change control (CM-3), and monitoring (AU-6, SI-4) findings.
2. **Florida legacy:** no OT DMZ (AC-4, SC-7), unsupported operating system (SA-22), same-room backups and untested recovery (CP-9, CP-4), no baseline (CM-2), and short local log retention (AU-12).
3. **Integrity of control and volumes:** change approvals and program compare outside the Permian (CM-3, CM-5, CM-6, AC-5, SI-7) and volume reconciliation (SI-7, SI-7(1)).
4. **Field device visibility and vendors:** inventory and firmware tracking (CM-8, SI-2), public APN modems (SC-8), and vendor assurance (SA-9, SR-6).
5. **Recovery and disclosure:** failover time (CP-10, CP-7, CP-2) and the OT scenario in the materiality playbook (IR-8).

**Strengths:** AC-3, AC-6, AT-2, AU-2, CA-2, CA-7, IA-2(1), IR-4, IR-6, PE-3, RA-3 were Satisfied. The IOC and BCC environment, privileged access through PAM, the SOC's incident handling, awareness training, and the risk and assessment program operate effectively.

**New finding during testing:** default credentials on AQ-MC modems and LACT flow computers (IA-05e.). Added to the risk register as R-061 and to POAM-008.

## 7. POA&M summary
`poam.csv` holds 23 items: 18 from this assessment and 5 carried from the P03 gap analysis and the P10 portfolio review (POAM-019, POAM-020, POAM-021, POAM-022, POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 7 |
| Moderate | 13 |
| Low | 3 |

| Status | Items |
|---|---|
| In progress | 18 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the FSPA control environment is **effective with exceptions**. Enterprise common controls for identity, privileged access, logging at the control centers, backup of IT workloads, monitoring, and incident handling operate effectively. The exceptions concentrate where enterprise controls have not yet reached (AQ-MC, the Florida control room, cellular field sites, and vendor-operated paths) and in OT change and volume integrity outside the Permian. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
