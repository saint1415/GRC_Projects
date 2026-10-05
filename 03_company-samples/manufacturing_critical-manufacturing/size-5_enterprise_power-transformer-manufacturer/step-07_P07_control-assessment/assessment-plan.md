# Security Assessment Plan and Report: Cris Santos Company | Critical Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer) |
| System assessed | Enterprise ERP and Production Scheduling Platform (EPSP), CSC-SYS-EPSP-001, per the SSP (P02), including the enterprise common controls it inherits (identity platform, cloud landing zone, security operations, enterprise network and IT/OT boundary, endpoint engineering, third-party risk) |
| Tier / Vertical | Enterprise / Critical Manufacturing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors from the 6-person IT audit team under the Chief Audit Executive, who reports functionally to the audit committee, plus a co-sourced OT specialist from an external industrial control systems assessment firm for the plant tests. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. Internal Audit has no OT specialist on staff; the co-sourced specialist compensates for that, and building in-house OT audit skill is on the 2027 audit plan |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork, with OT tests in Saturday maintenance windows: P2 on 2026-08-08, AQ-01 on 2026-08-15, P4 on 2026-08-22); report issued 2026-09-04; presented to the audit committee and the risk committee of the board on 2026-09-10 |
| Also satisfies | Annual assessment for the EPSP authorization decision (P02 section 4.2); SOX IT general control testing evidence for the ERP (access, change, operations); the "assess and manage" activity described in the Reg S-K Item 106(b) disclosure (P03 G-137); testing of FAR 52.204-21 safeguards for FCI held in the ERP (P03 G-108 to G-122) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 6, AT 2, AU 5, CA 1, CM 5, CP 4, IA 4, IR 3, MA 1, PS 1, RA 2, SA 2, SC 3, SI 4, SR 1), 282 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware reaching plant OT, AQ-01 integration, unsupported OT assets, recovery time, OEM remote access);
- cover the binding obligations with gaps in P03 (utility addendum notices, the SEC materiality step, FAR 52.204-21 safeguards for FCI in the ERP);
- protect production scheduling and master data integrity (SOX-relevant change and access controls);
- are common controls the EPSP inherits that no other assessment covered this year, including the IT/OT boundary and the OEM remote access gateway.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-028; FAR 52.204-21(b)(1)(i) | Comprehensive | Comprehensive | 1,436 EPSP account events (2026-01-01 to 2026-06-30); 1,960 terminations of staff with EPSP access (90 at AQ-01) | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 AQ-01) | 23 / 3 |
| AC-2(3) | R-028 | Focused | Comprehensive | 6,020 accounts (5,600 ERP workforce; 420 supplier portal) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-027; 15 CFR Part 744 screening | Focused | Focused | 5,600 ERP users | 25 users (random) | 1 / 0 |
| AC-5 | R-027 | Comprehensive | Comprehensive | 5,600 ERP users | 100% (SoD analytic) | 1 / 1 |
| AC-6 | R-059 | Focused | Focused | 2,180 PAM elevation sessions to ERP, database, and MES servers | 25 sessions (random) | 1 / 0 |
| AC-17 | R-007; R-008; addendum sec. 6 | Focused | Comprehensive | 3 remote access paths into EPSP zones (zero-trust service, OT gateway, ERP vendor support) | 100%; scan of 48 engineering workstations in MES zones | 3 / 1 |
| AT-2 | R-001; R-026 | Basic | Focused | 12,000 workforce | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-006; R-033 | Focused | Focused | 412 staff in EPSP and OT security roles | 40 (random) | 7 / 2 |
| AU-2 | R-029 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-029; R-030 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 63 tier-1 log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | SOX retention | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-029 | Basic | Focused | n/a (configuration) | 6 ERP servers, 2 integration nodes, 4 MES servers | 3 / 0 |
| CA-7 | Continuous monitoring | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-027 | Focused | Focused | 12 EPSP servers | 100% | 5 / 0 |
| CM-3 | R-027 | Comprehensive | Comprehensive | 212 EPSP changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 8 / 2 |
| CM-5 | R-027 | Focused | Focused | 212 changes | 10 changes traced to PAM sessions | 6 / 0 |
| CM-6 | R-006 | Focused | Comprehensive | 12 servers and 1,100 kiosks | 12 servers (100%); 60 kiosks (random, P3 and P4) | 5 / 1 |
| CM-8 | R-006 | Comprehensive | Comprehensive | About 1,100 kiosks and scanners at P1 to P6 | 60 physical devices traced to the CMDB (random, P3 and P4) | 4 / 2 |
| CP-2 | R-005; R-015 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; 4 interviews | 23 / 1 |
| CP-4 | R-031; R-032 | Focused | Focused | 1 annual DR test; 6 MES instances | 100% | 4 / 1 |
| CP-9 | R-002; R-032 | Focused | Focused | 181 daily ERP backup jobs; 6 MES backup sets | 25 ERP jobs (random); 6 MES sets (100%); 1 restore observed | 5 / 1 |
| CP-10 | R-005 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-049 | Basic | Focused | 5,600 ERP users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-049 | Focused | Comprehensive | 64 privileged EPSP accounts | 100% | 1 / 0 |
| IA-5 | R-009 | Focused | Comprehensive | About 90 OT devices with web interfaces in zones adjacent to the MES at P2, P4, and AQ-01 | 100% (tested with OEM approval in maintenance windows) | 9 / 1 |
| IA-8 | R-028 | Focused | Comprehensive | 420 supplier portal accounts | 100% (data analytic) | 0 / 1 |
| IR-4 | R-001 | Focused | Focused | 248 security incidents (11 at AQ-01) | 25 incidents (random) plus all 11 AQ-01 incidents | 13 / 0 |
| IR-6 | R-011; R-012; addendum secs. 1, 3 | Comprehensive | Comprehensive | 41 access-revocation notices; 248 incidents; 20 staff | 41 notices (100%); 25 incidents; 20 staff interviews | 1 / 1 |
| IR-8 | R-016 | Comprehensive | Focused | n/a (plan) | Plan and materiality procedure examined; interviews with General Counsel, CFO, CISO, COO | 15 / 2 |
| MA-4 | R-007; R-008 | Focused | Comprehensive | OEM sessions to MES zones (P1 to P6) | 25 gateway sessions (random); workstation scan | 5 / 3 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,960 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | Annual risk analysis | Focused | Basic | n/a | 2026 analysis examined | 8 / 0 |
| RA-5 | R-033 | Focused | Focused | 214 applicable ICS advisories; 3,880 IT findings on EPSP components | 60 advisories (random); 60 IT findings (random) | 7 / 2 |
| SA-9 | R-024 | Focused | Comprehensive | 12 external services supporting the EPSP | 100% | 5 / 1 |
| SA-22 | R-006 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-003 | Comprehensive | Focused | n/a (architecture) | Test from the AQ-01 office network | 4 / 2 |
| SC-8 | Interfaces | Basic | Focused | All EPSP interfaces | 100% (TLS scan) | 1 / 0 |
| SC-28 | R-018 | Basic | Focused | n/a (configuration) | Database and backup encryption inspected | 1 / 0 |
| SI-2 | R-048 | Focused | Focused | 1,240 critical patches | 60 (random) | 9 / 1 |
| SI-3 | R-001 | Focused | Focused | 12 servers and 1,100 kiosks | 12 servers; 25 kiosks (random) | 8 / 0 |
| SI-4 | R-029; R-030 | Focused | Focused | 7 plants | Rogue device test at P4 and AQ-01; after-hours alert test at P2 | 10 / 2 |
| SI-7 | R-025 | Focused | Focused | n/a | Integrity monitoring records examined | 6 / 0 |
| SR-6 | R-022; R-023 | Focused | Focused | 46 Tier 1 and 312 Tier 2 suppliers | 46 Tier 1 (100%); 40 Tier 2 (random) | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-6 and CM-8 (kiosks and scanners), RA-5, and SI-2.
- **Other manual controls:** 40 items, random selection, from Internal Audit's methodology table for moderate-risk manual controls. Used for CM-3 (212 changes), AT-3 (412 staff in EPSP and OT roles), and SR-6 (312 Tier 2 suppliers).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, IA-2, IR-4, IR-6 (incidents), MA-4 (gateway sessions), CP-9 (ERP jobs), and SI-3 (kiosks).
- **Recurring controls:** weekly, 5 occurrences (AU-6); monthly, 3 occurrences (CA-7); annual, the single occurrence (CP-4, CP-10, RA-3).
- **Configuration and data-analytic tests:** 100% of the population (for example, all 6,020 accounts for inactivity, all 5,600 ERP users for separation-of-duties conflicts, all 41 utility access-revocation notices, all 46 Tier 1 suppliers, and all of about 90 OT devices with web interfaces for default credentials).
- **Stratification:** terminations were stratified so AQ-01 (90 of 1,960, about 5% of the population) got 10 of 60 items; kiosk and scanner samples were drawn from P3 and P4, the plants whose MES logs are missing from the SIEM.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key production-integrity or process safety control (AC-5, CM-3, IA-5 on OT devices, AC-17 and MA-4 on OT remote access) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, the ERP role matrix and separation-of-duties rule set, change tickets, backup and DR test reports, MES backup sets, vulnerability scans and the ICS advisory tracker, the vendor register and SOC report reviews, the OT remote access gateway session records, the incident response plan and materiality procedure, disclosure committee minutes, and the obligations register with the 41 utility access-revocation notices.
- **Interview:** Vice President, Enterprise Applications; ERP Platform Manager; Vice President, Manufacturing Engineering; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; Chief Compliance Officer; General Counsel; CFO; COO; CISO; the plant managers at P2, P4, and AQ-01; and 20 randomly selected plant and office staff.
- **Test:** access tests with test accounts; an export release attempt without the Trade Compliance role; a network reachability test from the AQ-01 office network toward the AQ-01 PLC network and the corporate domain; default-credential tests on OT device web interfaces (with OEM approval, in maintenance windows); a scan of 48 engineering workstations in MES zones for unapproved remote tools; rogue device tests at P4 and AQ-01; an after-hours OT alert test at P2; TLS scans of EPSP interfaces; and a restore observation.

## 4. Rules of engagement
- No test could affect production, process safety, or test laboratory work. OT tests ran only in Saturday maintenance windows with the plant manager's written approval and a plant controls engineer present, who could stop any test.
- No active scanning or writes to PLCs, drives, or safety systems. OT tests were limited to HMI and engineering workstation web interfaces, passive traffic review, and the rogue device and alert tests.
- Default-credential tests used the OEM's published default list and were pre-approved by the OEM and the Vice President, Manufacturing Engineering.
- The rogue device tests used an audit-owned laptop with no company data, pre-approved by the CISO, the Director of OT Security, and the plant managers.
- No Restricted data (designs, customer drawings, FCI) left company systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. Two were: OEM default passwords on the web interface of 2 drying oven HMIs at AQ-01 (reported 2026-08-15) and 3 at P4 (reported 2026-08-22; the interface was blocked at the zone firewall on 2026-08-23); and the unapproved OEM remote tool on a P4 engineering workstation (reported 2026-08-22; removed 2026-08-24).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-22 | Fieldwork (examine, interview, test), including OT tests at P2 (2026-08-08), AQ-01 (2026-08-15), and P4 (2026-08-22) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners; risk register updated (R-008, R-009, R-027, R-028, R-032) |
| 2026-09-04 | Report issued to the COO, CISO, CIO, and Vice President, Enterprise Applications |
| 2026-09-10 | Presented to the audit committee and the risk committee of the board |
| 2026-09-14 | Used by the COO for the EPSP authorization decision (P02 section 4.2) |

Deliverables: this plan and report, `assessment-results.csv` (282 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 245 |
| Other than satisfied | 37 |
| **Total** | **282** |

**Controls with at least one Other than satisfied statement: 26 of 44:** AC-2, AC-2(3), AC-5, AC-17, AT-3, AU-6, CM-3, CM-6, CM-8, CP-2, CP-4, CP-9, CP-10, IA-5, IA-8, IR-6, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-4, SR-6.

**Fully Other than satisfied:** IA-8, SR-6 (each has a single determination statement).

**Themes:**
1. **AQ-01 integration** drives the identity (AC-2, PS-4), boundary (SC-7), monitoring (AU-6, SI-4), and OT remote access (AC-17, MA-4) findings. The two-way domain trust and the dual-homed MES let the test reach both the corporate domain controllers and the AQ-01 PLC network from the office network.
2. **Recovery at scale** is unproven: the ERP failover missed the 8-hour RTO (CP-10), the P3 MES backup omitted its configuration database (CP-9), MES restores were tested at only 2 of 6 plants (CP-4), and the contingency plan lacks the manual scheduling and STRS dispatch procedures (CP-2).
3. **Production data integrity:** separation-of-duties conflicts (AC-5) and master data and scheduling rule changes without independent approval (CM-3).
4. **Legacy OT and OEM access:** unsupported kiosks and HMIs (SA-22, CM-6), inventory accuracy (CM-8), ICS advisory triage (RA-5), patching (SI-2), default OEM credentials (IA-5), and an OEM remote tool outside the gateway (AC-17, MA-4).
5. **Obligations to customers and investors:** late utility access-revocation notices and a single 48-hour clock where 27 addenda require 24 hours (IR-6), a materiality procedure with no production-loss method (IR-8), overdue supplier reviews and an unassessed TMU contract manufacturer (SR-6), and supplier portal accounts without MFA (IA-8).

**Strengths:** privileged access and MFA for workforce and administrators (IA-2, IA-2(1), AC-6), role-based access and export release controls (AC-3), immutable logs and backups (AU-9, ERP backup jobs under CP-9), malware protection (SI-3), integrity monitoring (SI-7), encryption (SC-8, SC-28), incident handling (IR-4), continuous monitoring (CA-7), and the annual risk analysis (RA-3) were all Satisfied. At P2 the OT DMZ, the deny-by-default IT/OT firewall rules, and gateway sessions operated as designed; the only P2 exception was after-hours alert routing (SI-4).

**New findings during testing:** OEM default passwords on the web configuration interface of 5 drying oven HMIs (IA-05e.), added to the risk register as R-009 and to POAM-012; and an OEM remote tool on a P4 engineering workstation (AC-17b.), added as R-008 under POAM-008.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment and 5 carried from the P03 gap analysis and the P10 AI review (POAM-019, POAM-020, POAM-021, POAM-022, POAM-023), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 9 |
| Moderate | 15 |

| Status | Items |
|---|---|
| In progress | 18 |
| Open | 6 |

## 8. Conclusion
Internal Audit concludes that the EPSP control environment is **effective with exceptions**. Enterprise common controls for identity, privileged access, logging integrity, backup immutability, malware protection, and incident handling operate effectively, and the OT boundary controls operated as designed at P2, the tested plant where they are fully built. The exceptions concentrate in controls that depend on integrating AQ-01, in recovery time, in production data integrity, and in the notice obligations owed to utilities and investors. Two of seven plants (P3 and P6) have still never had independent OT testing; Internal Audit has scheduled them for 2027. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
