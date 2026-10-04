# Security Assessment Plan and Report: Cris Santos Company | Transportation and Warehousing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded multi-port marine cargo terminal operator) |
| System assessed | Enterprise Terminal Operating and Gate Platform (ETOP), CSC-SYS-ETOP-001, per the SSP (P02), including the enterprise common controls it inherits and the OT and T-08 interfaces in its risk scope |
| Tier / Vertical | Enterprise / Transportation and Warehousing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors and two co-sourced OT specialists under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls, and none has regularly assigned cybersecurity duties at the terminals, which is the independence test the Cybersecurity Plan audits will need (33 CFR 101.630(f)(4)). The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the ETOP authorization (P02 section 4.2); evidence for the Cybersecurity Assessment (101.650(e)(1)) and the first Plan audits; SOC 2 readiness evidence for SL-2 (P09) |
| Handling | Workpapers with network and OT details are sensitive security information (49 CFR part 1520) and stay in the Internal Audit SSI repository |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **45 controls (AC 6, AT 2, AU 5, CA 2, CM 4, CP 4, IA 3, IR 3, MA 1, MP 1, PS 1, RA 2, SA 2, SC 3, SI 5, SR 1), 289 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (multi-terminal ransomware, TOS recovery, OT exposure, OEM remote access, T-08 integration, disclosure and reporting);
- implement Subpart F measures with gaps in P03 (101.650(a), (b), (c), (d), (e)(3), (f), (g)(4), (h), (i));
- protect the integrity of customs holds, releases and hazardous cargo data (the High-baseline supplements in P02 section 6);
- are common controls ETOP inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-033; R-034; R-035; 101.650(a)(7) | Comprehensive | Comprehensive | 2,140 ETOP account events (2026-01-01 to 2026-06-30); 1,018 terminations of staff with ETOP or T-08 legacy TOS access (31 at T-08); about 1,150 SL-2 client accounts | 60 account events (random); 60 terminations (stratified: 50 enterprise, 10 T-08); 100% of client accounts (data analytic) | 22 / 4 |
| AC-2(3) | R-034 | Focused | Comprehensive | About 4,750 accounts (about 3,600 workforce; about 1,150 SL-2 client) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-018; R-019 | Focused | Focused | About 3,600 workforce ETOP users; 4 SL-2 client environments | 25 users (random); tenant isolation test from one client account in each SL-2 environment | 1 / 0 |
| AC-5 | R-019; CTPAT | Comprehensive | Comprehensive | 212 users with release override, gate supervisor or billing adjustment roles | 100% (role conflict analytic) | 1 / 1 |
| AC-6 | R-035; R-046 | Focused | Focused | 2,310 PAM elevation sessions to ETOP servers and databases; 22 vendor support accounts | 25 sessions (random); 100% of vendor accounts | 0 / 1 |
| AC-17 | R-004; 101.650(e)(3)(v), (f)(3) | Focused | Comprehensive | 4 OEMs and the TOS vendor; zero-trust workforce access | 100% of vendor remote access paths | 2 / 2 |
| AT-2 | R-020; 101.650(d)(1), (d)(4) | Basic | Focused | 12,000 employees; 1,140 new hires in the period | 60 employee records (random); 60 new hires (random); phishing results for 6 months | 9 / 1 |
| AT-3 | R-027; 101.650(d)(1)(v), (d)(2), (d)(3) | Focused | Comprehensive | Key personnel (412); maintenance contractors (380); 6 hiring halls | 25 key personnel records (random); 100% of contractor records; 6 of 6 hiring hall arrangements | 8 / 1 |
| AU-2 | R-009; R-019 | Focused | Focused | n/a (configuration) | 6 event types generated in test (override, hold change, hazardous cargo edit, role change, admin login, configuration change) | 6 / 0 |
| AU-6 | R-041; 101.650(c)(1) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 58 log sources on the ETOP path | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-051 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | R-041; 101.640 | Basic | Comprehensive | All ETOP log sources | 100% retention settings | 0 / 1 |
| AU-12 | R-041 | Basic | Focused | n/a (configuration) | 4 TOS servers, 2 database instances and 3 gate servers (one at T-07) | 3 / 0 |
| CA-2 | 101.630(f)(4) | Focused | Basic | n/a | Assessment plan and independence statements examined | 11 / 0 |
| CA-7 | 101.625(d)(2) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-007; 101.650(b)(4) | Focused | Focused | 11 TOS environments; OT devices that exchange data with ETOP at 5 container terminals | Baselines for 11 environments; OT configuration records at T-03, T-06 and T-07 | 4 / 1 |
| CM-3 | R-036; CTPAT | Comprehensive | Comprehensive | 196 ETOP change records (2026-01-01 to 2026-06-30) | 40 changes (random) | 9 / 1 |
| CM-7 | R-039; 101.650(b)(1)-(2) | Focused | Focused | 58 gate servers at T-01 to T-07 | 10 gate servers (random, including 2 at T-07) | 5 / 1 |
| CM-8 | R-007; 101.650(b)(3) | Comprehensive | Comprehensive | About 4,430 OT devices (estimate); about 1,900 IT components of ETOP | 60 physical OT devices traced to the inventory (random, 4 terminals); 25 ETOP components traced | 5 / 1 |
| CP-2 | R-008; 101.650(g)(4) | Comprehensive | Focused | n/a (plan) | Plan v3 examined; 4 interviews | 22 / 2 |
| CP-4 | R-008; R-025 | Focused | Focused | 1 annual DR test | 100% | 4 / 1 |
| CP-9 | R-050; 101.650(g)(4) | Focused | Focused | 181 daily backup jobs for 11 databases | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-008 | Focused | Focused | 1 DR test | 100% | 0 / 2 |
| IA-2 | R-045 | Basic | Focused | About 3,600 workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-045 | Focused | Comprehensive | 64 privileged ETOP and cloud accounts | 100% | 1 / 0 |
| IA-5 | R-007; 101.650(a)(2)-(4), (a)(6) | Focused | Comprehensive | About 340 OT devices without password controls; RTG HMIs at 4 terminals | 60 OT devices tested for default credentials (with OEM approval, at night with no vessel at berth); 100% of the device-class list | 7 / 3 |
| IR-4 | R-001; R-013 | Focused | Focused | 246 security incidents (11 affecting SL-2 environments; 5 at T-08) | 25 incidents (random) plus all 11 SL-2 and 5 T-08 incidents | 11 / 2 |
| IR-6 | R-012; 6.16-1 | Basic | Focused | 4 reportable events (2025-07 to 2026-07); 20 staff interviews | 100% of reportable events; 20 staff | 1 / 1 |
| IR-8 | R-012; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, CISO and CySO | 15 / 2 |
| MA-4 | R-004; 101.650(f)(3) | Focused | Comprehensive | Nonlocal maintenance by the TOS vendor and 4 OEMs | 100% of paths; 25 gateway sessions (random) | 5 / 3 |
| MP-7 | R-039; 101.650(i)(2) | Focused | Focused | 58 gate servers; OT HMIs at 8 terminals | 10 gate servers and 12 HMIs (random) | 1 / 1 |
| PS-4 | R-033; 101.650(a)(7) | Comprehensive | Comprehensive | 1,018 terminations (31 at T-08) | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | 101.650(e)(1) | Focused | Basic | n/a | 2026 risk analysis examined | 8 / 0 |
| RA-5 | R-006; R-042; 101.650(e)(3)(i), (vi) | Focused | Focused | 2,480 vulnerability findings on ETOP and OT components; 37 open OT KEVs | 60 findings (random); 100% of open KEVs | 7 / 2 |
| SA-9 | R-010; R-011; 101.650(f)(2) | Focused | Comprehensive | 14 external services supporting ETOP | 100% | 4 / 2 |
| SA-22 | R-026 | Focused | Comprehensive | Lifecycle register for ETOP components | 100% | 1 / 1 |
| SC-7 | R-002; 101.650(h)(1) | Comprehensive | Focused | n/a (architecture) | Reachability tests from the T-07 gate VLAN, from an SL-2 client spoke and from the T-08 site link | 5 / 1 |
| SC-8 | R-048 | Basic | Focused | All ETOP interfaces | 100% (TLS scan; EDI protocol review) | 1 / 0 |
| SC-28 | R-016 | Basic | Focused | n/a (configuration) | Database and backup encryption inspected | 1 / 0 |
| SI-2 | R-006 | Focused | Focused | 236 patches and firmware updates | 25 (random) | 9 / 1 |
| SI-3 | R-003 | Focused | Focused | EDR console (all sites) | Coverage report; 25 endpoints (random); T-08 sample of 25 | 7 / 1 |
| SI-4 | R-042; 101.650(h)(2) | Focused | Focused | 8 terminals | OT sensor coverage reviewed; test connection from the T-07 gate VLAN to an RTG controller | 11 / 1 |
| SI-7 | R-009; R-036 | Comprehensive | Focused | n/a | File integrity monitoring and table checksums examined; 25 hold reconciliation reports | 6 / 0 |
| SI-10 | R-048 | Focused | Focused | 20 malformed test messages | 100% in the test environment | 1 / 0 |
| SR-6 | R-014 | Focused | Focused | 210 tier-1 and tier-2 vendors | 25 (random) | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8 and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AT-3 (key personnel), CP-9, IA-2, IR-4, MA-4, SI-2, SI-3 and SR-6.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all SL-2 client accounts for inactivity, all role assignments for conflicts, all open OT KEVs).
- **Stratification:** terminations were stratified so T-08 (3% of the population) got 10 of 60 items, and OT devices were drawn from 4 terminals (T-01, T-03, T-07, T-08) to cover each OEM and the legacy estate.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key control for holds, releases or OT safety (AC-5, CM-3, IA-5 default credentials) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, the ETOP role matrix and override logs, change tickets and test evidence, backup and DR test reports, vulnerability scans and the KEV tracker, the OT inventory, the vendor register and contracts, the incident response plan and materiality playbook, 6.16-1 reporting records, disclosure committee minutes.
- **Interview:** Vice President, Terminal Technology; TOS Platform Manager; Director of Maritime Cybersecurity (CySO); 3 Terminal OT Security Leads; Director of OT Engineering; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Vice President, Labor Relations; General Counsel; CFO; CISO; 20 randomly selected terminal staff.
- **Test:** access tests with test accounts; tenant isolation tests from SL-2 spokes; default-credential tests on 60 OT devices (with OEM approval); reachability tests from the T-07 gate VLAN and the T-08 site link; a USB port test on gate servers and HMIs; an OT monitoring alert test at T-07; malformed EDI messages in the test environment; a restore observation.

## 4. Rules of engagement
- No test could affect vessel, gate or equipment operations. OT tests ran at night with no vessel at berth, with the Terminal General Manager's approval, an OEM technician present, and the equipment in a safe state.
- Malformed message tests ran only in the staging environment.
- Reachability and USB tests used an audit-owned laptop with no company data, pre-approved by the CISO and the CySO.
- No SSI or personal information left company systems. Screenshots and exports in workpapers are redacted and stored as SSI.
- Critical exposures were reported to the CISO and the CySO within 24 hours. One was: manufacturer default passwords on 3 OT devices (reported 2026-08-13; changed by 2026-08-20).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); OT tests on nights at T-01, T-03, T-07 and T-08 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, CySO and Vice President, Terminal Technology |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (289 rows) and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 245 |
| Other than satisfied | 44 |
| **Total** | **289** |

**Controls with at least one Other than satisfied statement: 30 of 45:** AC-2, AC-2(3), AC-5, AC-6, AC-17, AT-2, AT-3, AU-6, AU-11, CM-2, CM-3, CM-7, CM-8, CP-2, CP-4, CP-10, IA-5, IR-4, IR-6, IR-8, MA-4, MP-7, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-3, SI-4.

**Fully Other than satisfied:** AC-6 and AU-11 (one determination statement each) and CP-10 (both statements).

**Themes:**
1. **OT at the edge of ETOP** drives most findings: OEM remote access (AC-17, MA-4), OT authenticators and default passwords (IA-5), OT KEVs (RA-5, SI-2), OT inventory and configuration records (CM-8, CM-2), removable media (MP-7) and monitoring (SI-4).
2. **TOS platform recovery** is the main system-specific weakness: the plan, the test and the demonstrated recovery time (CP-2, CP-4, CP-10).
3. **T-07 and T-08** concentrate the network and logging findings (SC-7, AU-6, AU-11, SI-3, IR-4) and the late terminations (AC-2, PS-4).
4. **Reporting and disclosure readiness:** the materiality playbook and multi-COTP reporting sequence (IR-8, IR-6) and the SL-2 client notice terms (IR-4).
5. **Third parties:** the customs data exchange service and the port community systems have no security terms (SA-9).

**Strengths:** identity and privileged access for ETOP (IA-2, IA-2(1)), immutable logs and backups (AU-9, CP-9), encryption (SC-8, SC-28), integrity of hold and hazardous cargo data (SI-7, SI-10), event logging (AU-2, AU-12), continuous monitoring and risk assessment (CA-7, RA-3) and supplier reviews (SR-6) were all Satisfied. Tenant isolation between SL-2 client environments and company terminals held in every test.

**New finding during testing:** manufacturer default passwords on 3 OT devices (IA-05e.). Added to the risk register under R-007 and to POAM-004.

## 7. POA&M summary
`poam.csv` holds 25 items: 19 from this assessment (POAM-001 to POAM-019) and 6 carried from the P03 gap analysis, the P05 BIA and the P10 AI assessment (POAM-020 to POAM-025), so leadership tracks one list. Testing confirmed two of the carried items (POAM-022 through SA-9 and POAM-023 through CM-7).

| Risk level | Items |
|---|---|
| High | 12 |
| Moderate | 12 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 18 |
| Open | 7 |

## 8. Conclusion
Internal Audit concludes that the ETOP control environment is **effective with exceptions**. Enterprise common controls for identity, logging, backup, encryption and cloud monitoring operate effectively. The exceptions concentrate in the OT controls at the edge of the platform, in recovery of the platform as a whole, and in the two terminals not yet at the enterprise standard (T-07 for segmentation, T-08 for everything). Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2, and the CySO will use it as input to the Cybersecurity Assessment.
