# Security Assessment Plan and Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company; four stations, seven units) |
| System assessed | Fleet Work Management System and Plant Business Networks (WMS-PBN), CSC-SYS-WMS-001, per the SSP (P02), including the enterprise common controls it inherits (CCP-01 to CCP-09). The CDA side of the one-way data transfer devices (CCP-10 and the station CSPs) is out of scope |
| Tier / Vertical | Enterprise / Nuclear Reactors, Materials, and Waste |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. Station cyber teams escorted walkdowns but did not assess |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork and validation); report issued 2026-09-04; presented to the audit committee, the risk committee of the board, and the nuclear safety oversight committee on 2026-09-10 |
| Also satisfies | Annual assessment for the WMS-PBN authorization decision (P02 section 4.2); POL-01 4.9 independent annual assessment of tier-1 systems and common control providers; input to the Nuclear Oversight 73.55(m) review and the Item 106 disclosure |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 2, AU 5, CA 1, CM 5, CP 4, IA 3, IR 3, MP 1, PS 2, RA 2, SA 1, SC 2, SI 5, SR 1), 283 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (fleet ransomware during an outage, the pivot toward CDAs, Station 4 integration, sensor gateways, WMS record integrity, disclosure readiness);
- cover the P03 gaps that sit in business systems (73.54(c)(2) outer defensive level, 73.77 coordination, 73.56(m) information handling);
- protect clearance and surveillance record integrity (the High-baseline supplements in P02 section 6);
- are common controls WMS-PBN inherits that no other assessment covered this year. Identity and ERP controls already tested by the SOX program were relied on only where the SOX tests covered WMS-PBN.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-003; 73.56(m) context | Comprehensive | Comprehensive | 2,840 WMS and business-network account events (2026-01-01 to 2026-06-30); 2,310 departures of people with WMS or business-network access (1,880 outage contractors, 430 employees) | 60 account events (random); 60 departures (stratified: 40 outage contractors from Stations 2 and 3, 20 employees) | 22 / 4 |
| AC-2(3) | R-004 | Focused | Comprehensive | 11,640 enabled WMS and business-network accounts at fieldwork | 100% (data analytic) | 3 / 1 |
| AC-3 | R-006 | Focused | Focused | 9,500 named WMS users | 25 users (random) | 1 / 0 |
| AC-5 | R-007; 50.36(c)(3) | Comprehensive | Comprehensive | 412 users holding clearance writer or clearance approver roles (fleet) | 100% | 1 / 1 |
| AC-6 | R-029 | Focused | Focused | 2,150 PAM elevation sessions to WMS servers and the database | 25 sessions (random) | 1 / 0 |
| AC-17 | R-003; R-030 | Focused | Comprehensive | 4 remote access paths (zero-trust gateway; PAM vendor gateway; Station 4 prior-owner VPN; M&D vendor support channel) | 100% | 3 / 1 |
| AC-20 | R-018 | Focused | Focused | Contractor network segments at 4 stations | Configuration at 4 stations; connection test with an audit laptop at Station 2 | 3 / 0 |
| AT-2 | R-001; R-055; 73.54(d)(1) | Basic | Focused | 12,000 employees and 2,710 contractors with accounts | 60 training records (random); phishing simulation results for 6 months | 10 / 0 |
| AT-3 | 73.54(d)(1) | Basic | Focused | 640 role-based training assignments (WMS administrators, SOC analysts, privileged users) | 25 assignments (random) | 9 / 0 |
| AU-2 | R-006 | Focused | Focused | n/a (configuration) | 6 event types generated in test (clearance edit, clearance approval, surveillance date change, role change, failed sign-in, export) | 6 / 0 |
| AU-6 | R-040; R-006 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 128 log sources in the WMS-PBN boundary | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-10 | R-008; 50.36(c)(3) | Focused | Comprehensive | About 21,600 clearance approvals (2026-01-01 to 2026-06-30); 1,140 approvals in the Station 2 outage control center during the spring outage | 25 approvals (random) plus 100% of the Station 2 outage control center approvals (data analytic) | 0 / 1 |
| AU-12 | R-006 | Basic | Focused | n/a (configuration) | 6 WMS application servers and 3 edge servers | 3 / 0 |
| CA-7 | 73.54(e)(2) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-039 | Focused | Focused | 9 WMS servers (6 application, 3 edge) | 100% | 5 / 0 |
| CM-3 | R-009; 50.36(c)(3) | Comprehensive | Comprehensive | 212 WMS change records (2026-01-01 to 2026-06-30), of which 96 changed surveillance scheduling rules or clearance workflows | 40 scheduling rule and clearance workflow changes (random) | 8 / 2 |
| CM-5 | R-009 | Focused | Focused | 212 changes | 10 changes traced to PAM sessions | 6 / 0 |
| CM-7 | R-039 | Focused | Focused | 9 WMS servers | 100% (port and service scan) | 6 / 0 |
| CM-8 | R-005; R-036 | Comprehensive | Comprehensive | About 11,300 business network devices at the four stations | 60 physical devices traced to the CMDB (random, walkdowns at Stations 1 to 4) | 5 / 1 |
| CP-2 | R-010; R-001 | Comprehensive | Focused | n/a (plan) | WMS contingency plan v5 examined; 4 interviews | 22 / 2 |
| CP-4 | R-010 | Focused | Focused | 1 annual DR test | 100% | 4 / 1 |
| CP-9 | R-050; R-026 | Focused | Focused | 181 daily WMS backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-010 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-003 | Basic | Focused | 9,500 WMS accounts; about 1,000 Station 4 accounts | 25 sign-ins (random); comparison of Station 4 directory to identity governance (100%) | 1 / 1 |
| IA-2(1) | R-029 | Focused | Comprehensive | 22 privileged WMS-PBN accounts | 100% | 1 / 0 |
| IA-5 | R-036 | Focused | Comprehensive | 140 network-attached business devices in walkdown areas at Stations 3 and 4 | 100% (default credential test) | 9 / 1 |
| IR-4 | R-001; R-002 | Focused | Focused | 188 security incidents (2026-01-01 to 2026-06-30), 9 with a station link | 25 incidents (random) plus all 9 station-linked incidents | 13 / 0 |
| IR-6 | R-014; R-015; 73.77(a)(2)(iii); 73.77(b)(1) | Basic | Focused | 188 incidents; 25 cyber program deficiencies discovered by corporate staff; 20 staff interviews | 25 incidents; 25 deficiencies; 20 staff | 1 / 1 |
| IR-8 | R-013; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan v7 examined; interviews with the General Counsel, CFO, CISO, and Director, Nuclear Cyber Security | 15 / 2 |
| MP-7 | R-002; R-037 | Focused | Focused | Kiosk logs at 4 stations; 8 protected area entry points and 4 warehouses | Observation at 12 locations; 25 kiosk log entries (random) | 1 / 1 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 2,310 departures | 60 (same sample as AC-2) | 4 / 1 |
| PS-7 | R-004 | Focused | Comprehensive | 14 contracts with outage and service contractors whose staff hold company accounts | 100% | 4 / 1 |
| RA-3 | 73.54(d)(2) | Focused | Basic | n/a | 2026 enterprise risk analysis examined | 8 / 0 |
| RA-5 | R-039 | Focused | Focused | 3,420 vulnerability findings on WMS-PBN components | 60 findings (random); scan coverage report (100%) | 8 / 1 |
| SA-9 | R-020 | Focused | Comprehensive | 16 external services supporting WMS-PBN | 100% | 4 / 2 |
| SC-7 | R-002; R-003; R-005; 73.54(c)(2) | Comprehensive | Focused | n/a (architecture) | Reachability test from the Station 4 business network; one-way device direction test observed with the Station 2 cyber team from the business side | 4 / 2 |
| SC-8 | R-031 | Basic | Focused | All WMS interfaces | 100% (TLS scan) | 1 / 0 |
| SI-2 | R-039 | Focused | Focused | 236 patches for WMS-PBN components | 25 patches (random); 100% of edge server patch records for the spring outage | 9 / 1 |
| SI-3 | R-001; R-040 | Focused | Focused | About 9,800 station endpoints | EDR coverage report (100%); 25 endpoints (random) | 7 / 1 |
| SI-4 | R-040; R-002 | Focused | Focused | 4 station business networks | Rogue device tests at the Station 2 contractor segment and the Station 4 business network | 10 / 2 |
| SI-7 | R-006; 50.36(c)(3) | Comprehensive | Focused | n/a | Clearance record checksum job and nightly WMS-to-edge-server reconciliation examined | 6 / 0 |
| SI-7(1) | R-006 | Focused | Focused | n/a | Integrity check logs for 3 months | 3 / 0 |
| SR-6 | R-019; R-057 | Focused | Comprehensive | 38 tier-1 suppliers | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (96 scheduling rule and clearance workflow changes).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AT-3, AU-10 (random part), CP-9, IA-2, IR-4, IR-6, MP-7, SI-2, and SI-3.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 11,640 enabled accounts for expiry and inactivity, all 1,140 Station 2 outage control center clearance approvals for shared logins, all 140 walkdown-area devices for default credentials).
- **Stratification:** departures were stratified so outage contractors at Stations 2 and 3 (the stations with spring 2026 outages) got 40 of 60 items; CMDB tracing covered all four stations, weighted to Stations 3 and 4.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects clearance or surveillance record integrity (AC-5, AU-10, CM-3) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, WMS role matrix and audit trails, kiosk sign-in records, change tickets and test records, backup and DR test reports, vulnerability scans, the CMDB, vendor register and SOC report reviews, contractor contracts, the incident response plan v7 and materiality playbook, SOC external report log, station CAP entries.
- **Interview:** Vice President, Fleet Work Management; WMS Application Manager; Plant Managers (Stations 2 and 3); outage contractor coordinators; Director, Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Endpoint Engineering; Director, Nuclear Cyber Security and the Site Cyber Security Program Managers; Corrective Action Program Manager (fleet); General Counsel; CFO; CISO; 20 randomly selected station staff.
- **Test:** access tests with test accounts; inactivity and expiry analytics; a default credential test on business network devices in walkdown areas; a reachability test from the Station 4 business network; rogue device tests at the Station 2 contractor segment and the Station 4 business network; a one-way device direction test observed from the business side; TLS scans; a restore observation; generation of WMS audit events.

## 4. Rules of engagement
- **Nothing on the CDA side was touched.** All tests ran on business networks. No scan, connection attempt, or device was pointed at a one-way data transfer device, a CDA network, or plant equipment. The one-way device direction test was run by the Station 2 cyber team under their procedure, and Internal Audit observed.
- **No effect on plant work.** Tests at a station avoided outage critical-path windows and were approved by the Plant Manager and the Site Cyber Security Program Manager. Walkdowns in the owner-controlled area were escorted; no auditor entered a protected area for testing.
- **Portable media:** auditors used company-issued laptops scanned at a kiosk before each station visit; no auditor media was connected to station workstations.
- **Information handling:** no SGI was requested or collected; security-related information (network diagrams, CSP references) was viewed on site and summarized, not copied; export-controlled work package content and personal data were redacted from workpapers.
- **Critical exposures** were reported to the CISO within 24 hours and, where they could be cyber program weaknesses, to the Site Cyber Security Program Manager for entry in the station CAP within 24 hours (10 CFR 73.77(b)(1)). One was: default administrator passwords on 3 wireless sensor gateways at Station 4 (reported 2026-08-06; passwords changed 2026-08-07).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including station visits to Stations 2, 3, and 4 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Nuclear Officer, CISO, and Vice President, Fleet Work Management |
| 2026-09-10 | Presented to the audit committee, the risk committee of the board, and the nuclear safety oversight committee |
| 2026-09-14 | Used by the Chief Nuclear Officer for the WMS-PBN authorization decision (P02 section 4.2) |

Deliverables: this plan and report, `assessment-results.csv` (283 rows), and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 249 |
| Other than satisfied | 34 |
| **Total** | **283** |

**Controls with at least one Other than satisfied statement: 25 of 44:** AC-2, AC-2(3), AC-5, AC-17, AU-6, AU-10, CM-3, CM-8, CP-2, CP-4, CP-10, IA-2, IA-5, IR-6, IR-8, MP-7, PS-4, PS-7, RA-5, SA-9, SC-7, SI-2, SI-3, SI-4, SR-6.

**Fully Other than satisfied:** AU-10, SR-6 (each has a single determination statement).

These 25 controls are the in-scope controls that the SSP lists as Partially implemented (P02 section 10.1). The other two Partially implemented controls, AC-18 and CA-3, were not selected; their gaps are tracked through POAM-018 and POAM-022.

**Themes:**
1. **Station 4 integration** drives the identity (AC-2, IA-2), monitoring (AU-6, SI-3, SI-4), network (SC-7, AC-17), and vulnerability (RA-5) findings. Each has a dated plan and an approved exception with compensating controls.
2. **Work control record integrity** is the main system-specific weakness: dual clearance roles at Station 3 (AC-5), shared kiosk approvals at Station 2 (AU-10), and untested scheduling rule changes (CM-3). Field independent verification and weekly surveillance look-aheads limited the effect; no wrong clearance boundary or missed surveillance was found in the samples.
3. **Outage contractors:** account removal after early departures (AC-2, PS-4), bulk end-date extensions (AC-2(3)), and a missing contract clause (PS-7).
4. **Devices near plant equipment:** default passwords and missing inventory records on the Station 4 sensor gateways (IA-5, CM-8), and a cellular path around the boundary (SC-7).
5. **Notification and disclosure readiness:** the SOC-to-station link for 73.77 and the untested materiality step (IR-6, IR-8).
6. **Recovery time:** the WMS missed its RTO and outage mode is untested (CP-2, CP-4, CP-10).

**Strengths:** least privilege and privileged access (AC-3, AC-6, IA-2(1)), contractor segment isolation (AC-20), audit generation and protection (AU-2, AU-9, AU-12), baselines and change paths (CM-2, CM-5, CM-7), backups (CP-9), training (AT-2, AT-3), incident handling (IR-4), encryption in transit (SC-8), and integrity checks on clearance records (SI-7, SI-7(1)) were all Satisfied. The one-way data transfer devices passed traffic outward only.

**New finding during testing:** default administrator passwords on 3 wireless sensor gateways at Station 4 (IA-05e.). Added to the risk register as R-036 and to POAM-011.

## 7. POA&M summary
`poam.csv` holds 25 items: 17 from this assessment (POAM-001 to POAM-017) and 8 carried from the P03 gap analysis, the BIA, and the AI portfolio review (POAM-018, POAM-019, POAM-020, POAM-021, POAM-022, POAM-023, POAM-024, POAM-025), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 14 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 24 |
| Open | 1 |

## 8. Conclusion
Internal Audit concludes that the WMS-PBN control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, backup, and monitoring at Stations 1 to 3 operate effectively, and the defensive architecture at the CDA boundary worked as designed in every test. The exceptions concentrate in Station 4 integration, outage contractor access, and work control record integrity. Management accepted all findings and committed to the POA&M dates. The Chief Nuclear Officer used this report for the conditional authorization in P02 section 4.2.
