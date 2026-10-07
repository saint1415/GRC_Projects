# Security Assessment Plan and Report: Cris Santos Company | Energy | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded interstate natural gas transmission company) |
| System assessed | Pipeline SCADA and Gas Control System (PSGCS), CSC-SYS-PSGCS-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Energy (natural gas pipeline) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, co-sourced with an independent OT assessment firm for field and control room testing. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork, including site visits to GCC-1, GCC-2, PS3-CR, and 6 compressor stations); report issued 2026-09-04; presented to the audit committee and the risk committee of the board on 2026-09-10 |
| Also satisfies | Annual assessment for the PSGCS authorization (P02 section 4.2); counts toward the SD Pipeline-2021-02G Section III.G.2.d schedule and feeds the annual report due to TSA by 2026-11-14 (Section III.G.4) |
| Handling | Workpapers that describe Critical Cyber System vulnerabilities are SSI (49 CFR 1520.5(b)(5)). This sample contains no SSI |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **45 controls (AC 7, AT 1, AU 3, CA 2, CM 4, CP 6, IA 4, IR 4, MA 1, MP 1, PE 1, PS 1, RA 2, SA 2, SC 2, SI 3, SR 1), 278 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware forcing a shutdown, OT pre-positioning, legacy station controls, PS-3 integration, vendor modems, unpatched OT);
- cover SD 02G measures with gaps in P03 (Sections III.B to III.F);
- support the control room management duties in 49 CFR 192.631 (change management, backup SCADA, training);
- are common controls the PSGCS inherits that no other assessment covered this year (SOC, third-party risk, physical security).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-007; R-034; SD 02G III.C.3, III.C.4.b | Comprehensive | Comprehensive | 412 OT account changes (2026-01-01 to 2026-06-30); 118 departures and transfers of station staff; 1,450 OT domain accounts | 60 account changes (random); 25 departures and transfers (random); 100% of accounts (data analytic) | 24 / 2 |
| AC-2(1) | R-005; SD 02G III.C.3 | Focused | Comprehensive | HR leaver events for staff with OT accounts (2026-01-01 to 2026-06-30) | 100% (data analytic) | 0 / 1 |
| AC-4 | R-001; SD 02G III.B | Focused | Focused | n/a (configuration) | DMZ firewall rules at both GCCs inspected; one-way transfer to the historian replica tested | 1 / 0 |
| AC-5 | SD 02G III.C.3; 49 CFR 192.631(b)(5) | Focused | Comprehensive | 64 users with SCADA configuration rights | 100% | 2 / 0 |
| AC-6 | R-021; SD 02G III.C.3 | Focused | Focused | 1,450 OT domain accounts | 25 accounts (random) | 1 / 0 |
| AC-6(9) | R-003 | Basic | Focused | n/a (configuration) | OT privileged access logs inspected for 5 days (random) | 1 / 0 |
| AC-17 | R-008; SD 02G III.B.1.b, III.C | Comprehensive | Comprehensive | About 210 vendor users; 2,316 gateway sessions (2026-01-01 to 2026-06-30); modem inventories at 96 stations | 25 sessions (random); 100% of modem inventories; 6 stations visited | 3 / 1 |
| AT-3 | R-038; 49 CFR 192.631(h) | Focused | Focused | About 150 GCC controllers; 18 PS-3 controllers; about 60 OT engineers | 25 controllers (random); all 18 PS-3 controllers; 25 OT engineers (random) | 8 / 1 |
| AU-6 | R-036; R-003; SD 02G III.D.3.a | Comprehensive | Comprehensive | 26 weeks of OT monitoring cell review records; about 1,180 expected OT log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-11 | R-036; SD 02G III.D.3.b | Basic | Comprehensive | About 1,180 OT log sources | 100% (retention settings) | 0 / 1 |
| AU-12 | R-036 | Basic | Focused | n/a (configuration) | 4 SCADA hosts, 2 gateway nodes, 2 OT domain controllers, and 4 station HMIs (2 legacy) | 2 / 1 |
| CA-2 | SD 02G III.G; POL-01 4.9 | Focused | Basic | n/a | Cybersecurity Assessment Plan; 2025 annual report; architecture design review 2025-04 | 11 / 0 |
| CA-7 | SD 02G III.D; III.G | Focused | Basic | 6 monthly OT security metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-005; R-004 | Focused | Focused | About 1,100 hosts and HMIs in the PSGCS | 25 components (random, stratified: 15 PS-1 and PS-2, 10 PS-3) | 4 / 1 |
| CM-3 | R-037; 49 CFR 192.631(c)(2), (f) | Comprehensive | Comprehensive | 184 SCADA display and point changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 9 / 1 |
| CM-6 | R-004 | Focused | Comprehensive | 96 compressor stations | 100% (configuration compliance report); 6 stations inspected | 5 / 1 |
| CM-8 | R-064; SD 02G III.A | Comprehensive | Comprehensive | About 6,900 field devices (about 1,300 on PS-3) | 60 devices traced from the field to the inventory (stratified: 40 PS-1 and PS-2, 20 PS-3); 25 inventory entries traced to the field | 5 / 1 |
| CP-2 | R-002; R-012; SD 02G III.F | Comprehensive | Focused | n/a (plan) | PSGCS contingency plan v6 examined; 4 interviews | 22 / 2 |
| CP-4 | R-012; 49 CFR 192.631(c)(3), (c)(4) | Focused | Focused | 2026 contingency tests | GCC-2 failover test 2026-04-22; manual operation test 2026-04; exercise 2026-03-18 | 4 / 1 |
| CP-7 | R-005 | Basic | Focused | n/a | GCC-2 readiness checklist; site visit | 3 / 1 |
| CP-8 | R-024 | Basic | Focused | n/a | Telecommunications design; carrier contracts | 0 / 1 |
| CP-9 | R-029; SD 02G III.F.1.c | Focused | Focused | 181 daily SCADA backup jobs | 25 jobs (random); 1 restore observed at GCC-2 | 5 / 1 |
| CP-10 | R-002; R-005 | Focused | Focused | n/a | Rebuild runbooks; restore observation | 1 / 1 |
| IA-2 | R-007; SD 02G III.C.4 | Basic | Focused | 1,450 OT domain accounts; PS-3 legacy SCADA accounts | 25 console sign-ins (random); PS-3 account list | 1 / 1 |
| IA-2(1) | R-003; SD 02G III.C.2 | Focused | Comprehensive | 64 privileged OT accounts | 100% | 1 / 0 |
| IA-2(2) | SD 02G III.C.2 | Focused | Comprehensive | Engineering and remote access paths; 3 control rooms | 100% | 0 / 1 |
| IA-5 | R-007; R-035; R-058; SD 02G III.C.1 | Focused | Comprehensive | About 1,450 OT accounts; 38 components that cannot be reset; 31 shared station accounts; PS-3 field devices | 100% (password age report); 25 departures (same sample as AC-2); 20 PS-3 field devices tested for default credentials | 7 / 3 |
| IR-3 | R-012; SD 02G III.F.1.e | Focused | Focused | 2026 exercises | Exercise 2026-03-18 report and attendance | 0 / 1 |
| IR-4 | R-060; SD 02G III.F.1.a, III.F.1.b | Focused | Focused | 167 security incidents (2025-09 to 2026-06) | 25 incidents (random) | 11 / 2 |
| IR-6 | R-014; SD 01G II.C | Basic | Comprehensive | 14 reports to CISA (2025-09 to 2026-08); 167 incidents | 100% of reports; 25 incidents (same sample as IR-4) for reportability decisions | 2 / 0 |
| IR-8 | R-013; SEC Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; interviews with the General Counsel, CFO, CISO, and Director of OT Security | 15 / 2 |
| MA-4 | R-008 | Focused | Comprehensive | Nonlocal maintenance paths: gateway and 7 modems | 100% | 6 / 2 |
| MP-3 | R-016; 49 CFR 1520.13 | Focused | Focused | About 640 records in the TSA submission library | 25 records (random) | 1 / 1 |
| PE-3 | R-023; SD 02G III.C.2 | Focused | Focused | 3 control rooms; 96 stations; badge logs | 3 control rooms visited; 6 stations visited; 30 days of badge logs at GCC-1 (5 days random) | 11 / 1 |
| PS-4 | R-007; SD 02G III.C.3 | Comprehensive | Comprehensive | 214 terminations of staff with OT access (2026-01-01 to 2026-06-30), 18 on PS-3 | 40 terminations (stratified: 30 PS-1, PS-2, and JV; 10 PS-3) | 4 / 1 |
| RA-3 | SD 02G II.B.1; Item 106 | Focused | Basic | n/a | 2026 enterprise risk analysis examined (P01) | 8 / 0 |
| RA-5 | R-006; SD 02G III.E | Focused | Focused | 1,236 applicable patch items; 96 stations | 60 vulnerability findings (random); scan coverage report | 8 / 1 |
| SA-9 | R-030; R-031; SD 02G II.A.3 | Focused | Comprehensive | 6 critical OT suppliers | 100% | 5 / 1 |
| SA-22 | R-004; SD 02G III.E.3 | Focused | Comprehensive | 22 stations with unsupported components | 100% | 1 / 1 |
| SC-7 | R-005; R-008; SD 02G III.B | Comprehensive | Focused | About 4,800 firewall rules; 96 stations | 60 rules (random); reachability tests at 2 PS-3 stations and 2 PS-1 stations | 4 / 2 |
| SC-8 | R-059; SD 02G III.B.2.b | Basic | Focused | All SCADA polling paths | 100% (network design review); packet capture on one PS-3 circuit | 0 / 1 |
| SI-2 | R-006; SD 02G III.E | Focused | Focused | 1,236 applicable patch items on OT hosts (2026-01-01 to 2026-06-30) | 60 items (random) | 8 / 2 |
| SI-4 | R-003; R-010; SD 02G III.D | Focused | Comprehensive | 96 stations; 3 control rooms | Sensor coverage report (100%); detection test at 2 stations | 9 / 3 |
| SI-7 | R-004; R-030 | Comprehensive | Focused | n/a | File integrity reports; PLC logic comparison reports for 3 months | 5 / 1 |
| SR-6 | R-031 | Focused | Comprehensive | 6 critical OT suppliers | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 account changes, CM-8 field devices, RA-5, SI-2, and SC-7 firewall rules.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's table for smaller populations. Used for CM-3 and PS-4.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated through the period. Used for AC-6, AC-17 sessions, CM-2, CP-9, IA-2, IR-4, and MP-3.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all OT domain accounts for password age, all 96 station modem inventories, all OT log sources).
- **Stratification:** PS-3 is about 19% of field devices and 8% of terminations but carries most integration risk, so it was over-sampled: 20 of 60 field devices, 10 of 25 baseline components, and 10 of 40 terminations.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects safe operation (CM-3 point-to-point verification, IA-5 shared accounts, AC-17 vendor access) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), the TSA-approved Cybersecurity Implementation Plan and Assessment Plan, OT account exports and workflows, the shared account register, firewall exports, zone diagrams, change and point-to-point records, backup and failover test reports, the contingency plan, the incident response plan and materiality playbook, vulnerability and patch reports, the supplier register, training records, and the SSI library.
- **Interview:** Vice President, Gas Control; Director of SCADA Engineering; Director of OT Security; Director of Security Operations; Director of Compression Engineering; Director of Network Engineering; Director of Third-Party Risk Management; General Counsel; CFO; CISO; 10 controllers and 12 station operators.
- **Test:** passive observation of network traffic at 2 stations; reachability tests from the business network and between station zones (read-only tools); a detection test with benign traffic at 2 monitored stations; default-credential checks on 20 PS-3 field devices using the vendors' own tools; a backup restore observation at GCC-2; a packet capture on one PS-3 polling circuit.

## 4. Rules of engagement
- **No active scanning of OT.** Tests on SCADA, station, and field networks were passive or read-only, approved by the Vice President, Gas Control, and run with a controller informed and an OT engineer present.
- Default-credential checks used the device vendors' configuration tools during maintenance windows, with the station operator's approval; no setting was changed.
- No test could issue a command to a field device or change a display. Any test touching a control room was paused on the controller's request.
- The co-sourced firm used company-owned transient devices scanned at the OT media kiosk; its own laptops never connected to OT.
- Workpapers with network details were stored in the SSI library.
- Critical exposures were reported to the CISO within 24 hours. One was: default credentials on 6 PS-3 field devices (reported 2026-08-07; POAM-018).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests; rules of engagement signed by the Vice President, Gas Control and the CISO |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including site visits |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Gas Control |
| 2026-09-10 | Presented to the audit committee and the risk committee of the board |
| 2026-11-14 | Results included in the annual Cybersecurity Assessment Plan report to TSA |

Deliverables: this plan and report, `assessment-results.csv` (278 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 231 |
| Other than satisfied | 47 |
| **Total** | **278** |

**Controls with at least one Other than satisfied statement: 36 of 45:** AC-2, AC-2(1), AC-17, AT-3, AU-6, AU-11, AU-12, CM-2, CM-3, CM-6, CM-8, CP-2, CP-4, CP-7, CP-8, CP-9, CP-10, IA-2, IA-2(2), IA-5, IR-3, IR-4, IR-8, MA-4, MP-3, PE-3, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SI-7, SR-6.

**Fully Other than satisfied:** AC-2(1), AU-11, CP-8, IA-2(2), IR-3, SC-8, SR-6 (each has a single determination statement).

**Themes:**
1. **PS-3 integration** drives the most findings (POAM-016): flat station networks (SC-7), unencrypted polling (SC-8), shared local accounts and manual disablement (IA-2, AC-2(1), PS-4), PS3-CR console and floor controls (IA-2(2), PE-3), no alternate site, offline backup, or tested rebuild (CP-7, CP-9, CP-10), separate incident tools (IR-4), and incomplete baselines and inventory (CM-2, CM-8).
2. **Legacy and unmonitored compressor stations:** unsupported components (SA-22, CM-6, SI-7), late firmware patches (SI-2), no monitoring or log forwarding at 22 stations (SI-4, AU-6, AU-11, AU-12), and no credentialed scanning at 31 stations (RA-5).
3. **Vendors with OT reach:** always-on modems (AC-17, MA-4, SC-7, SI-4) and missing supplier terms and software bills of materials (SA-9, SR-6).
4. **Resilience and disclosure readiness:** no platform-wide SCADA failure scenario (CP-2), isolation untested at GCC-2 and PS3-CR (CP-4, IR-3), and no curtailment factors in the SEC materiality step (IR-8).

**Strengths:** IT/OT flow enforcement and the one-way historian path (AC-4), least privilege and separation of duties (AC-5, AC-6, AC-6(9)), MFA for privileged OT access (IA-2(1)), the assessment program (CA-2, CA-7), the risk analysis (RA-3), and on-time reporting to CISA (IR-6) were all Satisfied. GCC-1 and GCC-2 controls are strong; most exceptions sit at PS-3 and the 22 legacy stations.

**New finding during testing:** default credentials on 6 of 20 PS-3 field devices tested (IA-05e.). Added to the risk register as R-058 and to POAM-018.

## 7. POA&M summary
`poam.csv` holds 24 items: 21 from this assessment and 3 carried from the P03 gap analysis and the P10 portfolio review (POAM-019, POAM-022, POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 13 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

## 8. Conclusion
Internal Audit concludes that the PSGCS control environment is **effective with exceptions**. Controls at GCC-1 and GCC-2 and the enterprise common controls for identity, privileged access, assessment, and CISA reporting operate effectively. The exceptions concentrate in the PS-3 subsystem (scheduled to migrate by 2027-06-30 under the TSA-approved plan amendment), the 22 legacy and unmonitored compressor stations, and third-party remote access. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
