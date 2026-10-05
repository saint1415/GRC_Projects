# Security Assessment Plan and Report: Cris Santos Company | Transportation Systems | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 freight railroads) |
| System assessed | Train Dispatching and PTC Back Office Platform (TDPB), CSC-SYS-TDPB-001, per the SSP (P02), including the enterprise common controls it inherits and the field and acquired railroad conditions that affect it |
| Tier / Vertical | Enterprise / Transportation Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors, and two co-sourced OT security specialists under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork: NOC walkthrough 2026-07-22; DC-2 and backup NOC 2026-07-29; CR-07 wayside and PTC field visit and Central region field tests 2026-08-05); report issued 2026-09-04; presented to the board safety, security, and risk committee and the audit committee on 2026-09-10 |
| Also satisfies | Assessments counted toward the 2026-2027 year of the TSA Cybersecurity Assessment Plan (SD 1580/82-2022-01E Sec. III.F.2.d); annual assessment for the TDPB authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 4, AT 2, AU 5, CA 3, CM 4, CP 6, IA 3, IR 4, MA 1, PE 1, PS 1, RA 2, SA 1, SC 3, SI 4), 297 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware, OT access paths, PTC recovery, acquired railroads, manual operations);
- implement CIP measures in SD 1580/82-2022-01E Sec. III.B to III.E and CIRP objectives in SD 1580-21-01E Sec. II.D that had gaps in P03;
- protect TDPB integrity and availability (the High-baseline supplements in P02 section 6 rest on CM-3, CP-2, CP-10, SI-7);
- are common controls the TDPB inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied. In the "why selected" column, SD-2022 means SD 1580/82-2022-01E and SD-21 means SD 1580-21-01E.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-063; R-006; SD-2022 III.C.3-4 | Comprehensive | Comprehensive | 1,212 TDPB account events (2026-01-01 to 2026-06-30); 1,318 terminations of staff with TDPB or corporate access (96 at AQ-04 to AQ-06) | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AQ) | 22 / 4 |
| AC-3 | R-002; SD-2022 III.C.3 | Focused | Comprehensive | OT directory groups and permissions on 38 TDPB servers | 100% (permission analytic) | 0 / 1 |
| AC-6 | R-062; SD-2022 III.C.3 | Focused | Focused | 2,140 PAM elevation sessions to TDPB servers | 25 sessions (random) | 1 / 0 |
| AC-17 | R-010; R-038; SD-2022 III.C | Focused | Comprehensive | 5 remote access paths to Critical Cyber Systems; 14 OT vendors | 100% | 3 / 1 |
| AT-2 | R-018; SD-2022 III.D.1.a | Basic | Focused | 12,000 employees (520 network operations) | 60 training records (random); phishing results for 6 months | 10 / 0 |
| AT-3 | R-034; SD-21 II.D.3.b | Focused | Comprehensive | 310 dispatchers and supervisors; 46 train control staff | 100% (learning system analytic) | 8 / 1 |
| AU-2 | R-008; R-012 | Focused | Focused | n/a (configuration) | 6 event types generated in test (authority issue, territory table change, PTC key event, privileged logon, configuration change, failed logon) | 6 / 0 |
| AU-6 | R-008; SD-2022 III.D.3.a | Comprehensive | Comprehensive | 26 weeks of SOC and CAD/PTC exception reviews; 214 OT log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-008 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested with a test account | 2 / 0 |
| AU-11 | R-008; SD-2022 III.D.3.b | Basic | Comprehensive | n/a (configuration); 83 uncollected OT sources | Retention settings inspected for all TDPB sources | 0 / 1 |
| AU-12 | R-008 | Basic | Focused | 38 TDPB servers | 10 servers (random) | 3 / 0 |
| CA-2 | SD-2022 III.F; POL-01 4.9 | Focused | Basic | n/a (plan) | 2026 CAP and assessment plans examined | 11 / 0 |
| CA-7 | SD-2022 III.F.1 | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CA-8 | R-001; SD-2022 III.F.2.c | Basic | Focused | 2026 penetration test and purple team exercise | 100% | 1 / 0 |
| CM-2 | R-035; R-012 | Focused | Focused | 38 TDPB servers; 148 consoles | 10 servers and 25 consoles (random) | 5 / 0 |
| CM-3 | R-011; 49 CFR 236.1023(c) | Comprehensive | Comprehensive | 226 CAD and PTC change records (2026-01-01 to 2026-06-30), 40 of them emergency | All 40 emergency changes (100% of that stratum) and 25 standard changes (random) | 8 / 2 |
| CM-6 | R-035; SD-2022 III.D.1.d | Focused | Comprehensive | 148 dispatch consoles; 38 servers | 100% (configuration analytic) | 4 / 2 |
| CM-8 | R-009; SD-2022 III.A; IV.C.2.a | Comprehensive | Comprehensive | About 3,900 TDPB and OT field devices in 2 regions | 60 physical devices traced to the CMDB (random, 6 sites) | 5 / 1 |
| CP-2 | R-004; R-013; R-014; R-022 | Comprehensive | Focused | n/a (plan) | TDPB contingency plan v6 examined; 4 interviews | 22 / 2 |
| CP-4 | R-013; SD-21 II.D.3 | Focused | Comprehensive | 1 annual DR test; 11 signaled railroads | 100% | 4 / 1 |
| CP-7 | R-029; R-031 | Focused | Focused | DC-2 and the backup NOC | Site visit 2026-07-29 | 4 / 0 |
| CP-8 | R-028; R-022 | Basic | Comprehensive | About 380 tower and field sites; crew calling telephony | 100% (carrier inventory analytic) | 0 / 1 |
| CP-9 | R-050; SD-21 II.D.1.b | Focused | Focused | 181 daily backup jobs (CAD and PTC) | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-004; 49 CFR 236.1033(f) | Focused | Comprehensive | 1 DR test (CAD and PTC) | 100% | 0 / 2 |
| IA-2 | R-006; SD-2022 III.C.4 | Focused | Comprehensive | 1,912 accounts on Critical Cyber Systems | 100% (analytic) | 1 / 1 |
| IA-2(1) | R-062; SD-2022 III.C.2 | Focused | Comprehensive | 31 TDPB administrators | 100% | 1 / 0 |
| IA-5 | R-007; R-006; SD-2022 III.C.1 | Focused | Comprehensive | About 640 detector modems and 41 field code unit gateways | 60 detector modems (random) plus all 41 gateways, tested in maintenance windows with signal engineering approval | 8 / 2 |
| IR-3 | SD-21 II.D.3 | Basic | Focused | 1 annual exercise (2026-03-18) | 100% | 1 / 0 |
| IR-4 | R-001; SD-2022 III.D.2.d | Focused | Focused | 212 security incidents (2026-01-01 to 2026-06-30) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-054; SD-21 II.C; 49 CFR 1570.203 | Basic | Focused | 212 incidents; 2 CISA reports; 20 staff interviews | 25 incidents; 2 reports; 20 staff | 2 / 0 |
| IR-8 | R-017; R-054; SD-21 II.D.1-2 | Comprehensive | Focused | n/a (plan) | CIRP v5 and materiality playbook examined; interviews with the General Counsel, CFO, CISO | 15 / 2 |
| MA-4 | R-038 | Focused | Focused | 312 vendor maintenance sessions to CAD and PTC | 25 sessions (random) | 8 / 0 |
| PE-3 | R-058; SD-2022 III.C.6 | Basic | Focused | NOC floors, DC-1 and DC-2 data halls | 3 site visits; 25 badge events (random) | 12 / 0 |
| PS-4 | R-063 | Comprehensive | Comprehensive | 1,318 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | SD-21 II.E; POL-01 4.3 | Focused | Basic | n/a | 2026 risk analysis examined (P01) | 8 / 0 |
| RA-5 | R-037; SD-2022 III.E.2.b | Focused | Focused | 1,904 vulnerability findings on TDPB components; field segment coverage map | 60 findings (random); coverage map in full | 8 / 1 |
| SA-9 | R-026; SD-2022 II.A.2 | Focused | Comprehensive | 12 external services supporting the TDPB | 100% | 5 / 1 |
| SC-7 | R-003; R-010; SD-2022 III.B.2.a | Comprehensive | Focused | 11 zone boundaries | Reachability tests from an AQ-06 site network and from the crossing monitor vendor network (2026-08-05) | 4 / 2 |
| SC-8 | R-036; SD-2022 III.B.2.b | Basic | Comprehensive | All TDPB and code line circuits on 11 signaled railroads | 100% (TLS scan; packet capture on leased circuits) | 0 / 1 |
| SC-12 | 49 CFR 236.1033(b)-(d) | Focused | Focused | PTC key management procedure; HSMs in DC-1 and DC-2 | Key ceremony records for 2 rotations | 2 / 0 |
| SI-2 | R-005; SD-2022 III.E | Focused | Focused | 212 patches for TDPB components | 25 patches (random) | 9 / 1 |
| SI-3 | R-001; SD-2022 III.D.1.d | Basic | Focused | 38 TDPB servers; 148 consoles | 10 servers and 25 consoles (random) | 8 / 0 |
| SI-4 | R-037; R-008; SD-2022 III.D.2.b | Focused | Focused | 11 NOC and DMZ monitoring points; field segment coverage | All monitoring points; rogue connection test at the backup NOC | 11 / 1 |
| SI-7 | R-012 | Focused | Focused | n/a | File integrity monitoring and territory table checksum examined; test change in the CAD lab | 6 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, and RA-5.
- **High-risk strata:** where a stratum carried most of the risk, it was tested in full. CM-3 tested all 40 emergency changes plus 25 random standard changes; IA-5 tested all 41 field code unit gateways plus 60 random detector modems.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-6, CP-9, IR-4, IR-6, MA-4, PE-3, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 1,912 accounts on Critical Cyber Systems for shared accounts, all 148 consoles for configuration, all 214 OT log sources for collection).
- **Stratification:** terminations were stratified so the acquired railroads (7% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects movement authority or OT access (AC-3, CM-3, IA-2, IA-5, SC-7) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references). Workpapers that contain SSI are kept in the SSI library.

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), the CIP, CAP, and CIRP, identity governance and PAM records, OT directory and server permissions, change tickets and change board minutes, backup and DR test reports, vulnerability and patch reports, vendor register and SOC report reviews, the materiality playbook, disclosure committee minutes, CISA report confirmations.
- **Interview:** Vice President, Network Operations; Director of Train Control Systems; CAD Application Manager; PTC Back Office Manager; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Assistant Vice President, Rail Security; Vice President, Crew Management; General Counsel; CFO; CISO; 20 randomly selected NOC and train control staff.
- **Test:** access tests with test accounts; default-credential tests on detector modems and field code unit gateways (in maintenance windows, with signal engineering approval); reachability tests from an AQ-06 site network and from the crossing monitor vendor network; a rogue connection test at the backup NOC; TLS scans and packet captures on leased code line circuits; a test change in the CAD lab to trigger integrity alerts; a restore observation.

## 4. Rules of engagement
- No testing could affect train movement. Field tests ran only in signal maintenance windows with the Director of Train Control Systems' approval and a signal maintainer present; no test sent any control to a field code unit.
- Tests at the NOCs ran on non-production consoles or in the CAD and PTC labs; production consoles were inspected read-only.
- The rogue connection test used an audit-owned laptop with no company data, pre-approved by the CISO and the Director, Network Operations Center.
- SSI collected as evidence stayed in the SSI library. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. Two were: default credentials on 6 field devices (reported 2026-08-11) and vendor modems reaching a CTC field network (reported 2026-08-05; modems disconnected 2026-09-15).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including site visits on 2026-07-22, 2026-07-29, and 2026-08-05 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Network Operations |
| 2026-09-10 | Presented to the board safety, security, and risk committee and the audit committee |

Deliverables: this plan and report, `assessment-results.csv` (297 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 264 |
| Other than satisfied | 33 |
| **Total** | **297** |

**Controls with at least one Other than satisfied statement: 23 of 44:** AC-2, AC-3, AC-17, AT-3, AU-6, AU-11, CM-3, CM-6, CM-8, CP-2, CP-4, CP-8, CP-10, IA-2, IA-5, IR-8, PS-4, RA-5, SA-9, SC-7, SC-8, SI-2, SI-4.

**Fully Other than satisfied:** AC-3, AU-11, CP-8, and SC-8 (each has a single determination statement) and CP-10 (both statements).

**Themes:**
1. **OT access paths** are the main system weakness: the corporate-to-OT directory trust (AC-3), shared CTC accounts (IA-2, IA-5, AC-2), default credentials on field devices (IA-5), and the crossing monitor vendor's modems (AC-17, SC-7).
2. **Recovery and manual operations:** PTC back office recovery (CP-10, CP-2), manual CTC operations (CP-4), the RSSM fallback and crew calling (CP-2, CP-8).
3. **Acquired railroads** drive the termination (AC-2, PS-4) and boundary (SC-7) findings.
4. **OT visibility:** log collection and retention (AU-6, AU-11), field monitoring and inventory (SI-4, RA-5, CM-8).
5. **Disclosure readiness:** the SEC materiality and TSA/CISA steps are not integrated or exercised with the current disclosure committee (IR-8).

**Strengths:** privileged access through PAM with phishing-resistant MFA (AC-6, IA-2(1), MA-4), immutable and scanned backups (CP-9), audit record protection (AU-9), integrity monitoring of territory tables (SI-7), CAD recovery within its RTO, PTC key management (SC-12), the annual CIRP exercise (IR-3), and the TSA Cybersecurity Assessment Plan and independent testing (CA-2, CA-8) were all Satisfied.

**New findings during testing:** default vendor credentials on 6 field devices (IA-05e.) and vendor modems reaching a CTC field network (AC-17b.). Both were added to the risk register (R-007, R-010) and the POA&M (POAM-012, POAM-008).

## 7. POA&M summary
`poam.csv` holds 24 items: 20 from this assessment and 4 carried from the P03 gap analysis (POAM-002, POAM-022, POAM-023, POAM-024), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 12 |
| Moderate | 12 |

| Status | Items |
|---|---|
| In progress | 22 |
| Open | 2 |

## 8. Conclusion
Internal Audit concludes that the TDPB control environment is **effective with exceptions**. Enterprise common controls for privileged access, backup, logging protection, and incident handling operate effectively, and CAD meets its recovery objective. The exceptions concentrate in OT access paths, PTC back office recovery, manual operations readiness, and conditions at the acquired railroads. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2, and the CISO will include the results in the next annual Cybersecurity Assessment Plan report to TSA.
