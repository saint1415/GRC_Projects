# Security Assessment Plan and Report: Cris Santos Company | Government Services and Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings) |
| System assessed | Integrated Building Operations Platform (IBOP), CSC-SYS-IBOP-001, per the SSP (P02), including the enterprise common controls it inherits and the AQ-1 and AQ-2 components that still reach IBOP-managed devices |
| Tier / Vertical | Enterprise / Government Services and Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors, and one OT specialist auditor under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. Field device tests were witnessed by the Director of OT Security's staff but performed and recorded by Internal Audit |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | The annual independent assessment required by the 5 state cybersecurity exhibits (SP 800-53 CA-2); the annual assessment for the IBOP authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 6, AT 2, AU 4, CA 2, CM 5, CP 4, IA 4, IR 3, MA 1, PE 1, PS 2, RA 2, SA 2, SC 3, SI 4, SR 1), 307 determination statements.** Every determination statement for each selected control was assessed. Controls were selected because they:
- address the Very High and High risks in P01 (multi-building intrusion, AQ-1 remote access, default credentials, OT monitoring, supply chain, disclosure);
- cover High and Very High gaps in P03;
- protect door and setpoint integrity (the High-baseline supplements AC-2(12), AU-10, and CM-3(1) in P02 section 6);
- are common controls the IBOP inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-003; R-028; G-002 | Comprehensive | Comprehensive | 2,140 IBOP account events (2026-01-01 to 2026-06-30); 486 terminations of staff with IBOP accounts (61 AQ-1); 4,800 customer console accounts | 60 events (random); 60 terminations (stratified: 48 enterprise, 12 AQ-1); 100% of console accounts (analytic) | 22 / 4 |
| AC-2(12) | R-028; High-baseline supplement | Focused | Focused | 6 atypical-use rules (PACS-01 to PACS-06) | 100% of rules; 10 alerts traced (random) | 2 / 0 |
| AC-3 | R-028 | Focused | Focused | 1,360 company IBOP accounts | 25 accounts (random) | 1 / 0 |
| AC-5 | R-028; G-005 | Focused | Focused | 1,140 access-level and schedule changes | 25 changes (random) | 2 / 0 |
| AC-6 | R-054 | Focused | Focused | 2,610 PAM elevation sessions; 3 AQ-2 legacy instances | 25 sessions (random); 100% of AQ-2 instances | 0 / 1 |
| AC-17 | R-001; R-002; G-012 | Comprehensive | Comprehensive | About 1,480 sites; 3 remote access paths (gateway, vendor support through the gateway, AQ-1 legacy tool) | 100% of paths; 25 gateway sessions (random) | 2 / 2 |
| AT-2 | R-026 | Basic | Focused | 12,000 staff | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-031; G-020; CJIS AT-3 | Focused | Focused | 412 technicians assigned to public safety buildings | 40 records (random) | 8 / 1 |
| AU-2 | R-051; G-024 | Focused | Focused | 186 IBOP log sources | 100% of sources (SIEM inventory) | 5 / 1 |
| AU-6 | R-051; R-028 | Comprehensive | Focused | 26 weeks of OT change report reviews | 5 weeks (random) | 2 / 1 |
| AU-10 | R-054; High-baseline supplement | Focused | Focused | 1,140 door schedule and program changes | 25 changes (random) | 0 / 1 |
| AU-12 | R-051 | Basic | Focused | 186 IBOP log sources | 10 components tested | 2 / 1 |
| CA-2 | State exhibits (annual independent assessment) | Focused | Basic | n/a (program) | 2026 assessment plan examined | 11 / 0 |
| CA-7 | R-011; G-038 | Focused | Focused | 6 monthly metric packages; OT sensor coverage report | 3 months (random) | 10 / 1 |
| CM-2 | R-002; R-054 | Focused | Focused | 38 BAS servers, 24 PACS servers, 6 alarm servers; about 1,480 edge gateways | 100% of servers; 25 gateways (random, including 6 AQ-1) | 4 / 1 |
| CM-3 | R-021; R-010 | Comprehensive | Comprehensive | 1,140 IBOP and program changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 10 / 0 |
| CM-3(1) | R-010; High-baseline supplement | Focused | Focused | Pipeline gate configuration | 3 test pushes without tickets | 6 / 0 |
| CM-6 | R-004; R-058; G-045 | Comprehensive | Comprehensive | About 73,550 field devices (controllers, door controllers, recording servers) | 60 devices at 6 sites (stratified, including AQ-1 and AQ-2), tested with customer approval | 5 / 1 |
| CM-8 | R-011 | Comprehensive | Comprehensive | About 73,550 field devices | 60 physical devices traced at 6 sites | 4 / 2 |
| CP-2 | R-009; R-013 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; 4 interviews | 22 / 2 |
| CP-4 | R-010 | Focused | Focused | 1 annual regional failover test | 100% | 4 / 1 |
| CP-9 | R-010 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 5 / 1 |
| CP-10 | R-009; G-060 | Focused | Focused | 1 regional failover test | 100% | 1 / 1 |
| IA-2 | R-003; R-054 | Basic | Focused | 1,360 company IBOP accounts; AQ-2 instances | 25 sign-ins (random); 100% of AQ-2 accounts | 1 / 1 |
| IA-2(1) | R-040; R-026 | Focused | Comprehensive | 64 privileged IBOP and cloud accounts | 100% | 1 / 0 |
| IA-5 | R-004; R-058 | Comprehensive | Comprehensive | About 73,550 field devices; PAM vault | 60 devices (same sample as CM-6); vault configuration | 8 / 2 |
| IA-8 | R-028 | Focused | Comprehensive | 4,800 customer console accounts | 100% (analytic) | 0 / 1 |
| IR-4 | R-060; R-001 | Focused | Focused | 318 security incidents (14 at AQ sites) | 25 incidents (random) plus 6 AQ incidents | 11 / 2 |
| IR-6 | R-024 | Basic | Focused | 318 incidents; 30 staff interviews | 25 incidents; 30 staff (ROC and field) | 1 / 1 |
| IR-8 | R-025; G-078 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, CISO | 15 / 2 |
| MA-4 | R-002; R-022 | Comprehensive | Comprehensive | Gateway sessions (2026-01-01 to 2026-06-30); AQ-1 legacy tool | 25 gateway sessions (random); AQ-1 tool examined | 5 / 3 |
| PE-3 | R-064 | Focused | Focused | 3 ROCs | Inspection at all 3 ROCs; 25 badge events (random) | 12 / 0 |
| PS-3 | CJIS PS-3; R-031 | Basic | Focused | 486 hires assigned to IBOP roles | 25 hires (random) | 3 / 0 |
| PS-4 | R-003; R-032 | Comprehensive | Comprehensive | 486 terminations of staff with IBOP accounts; 214 departures from federal contracts | 60 terminations (same sample as AC-2); 25 federal departures (random) | 3 / 2 |
| RA-3 | P01 | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-011; R-036 | Focused | Focused | 2,330 findings on IBOP components; OT advisory tracker | 60 findings (random) | 7 / 2 |
| SA-9 | R-019 | Focused | Comprehensive | 23 external services supporting the IBOP; 38 subcontractors with gateway accounts | 100% | 5 / 1 |
| SA-22 | R-036 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-001; R-005 | Comprehensive | Focused | n/a (architecture) | Tests from 2 customer IT networks and 1 AQ-1 site | 4 / 2 |
| SC-8 | R-059 | Basic | Focused | All IBOP interfaces; 6 sites | 100% (TLS scan); packet capture at 2 sites | 0 / 1 |
| SC-28 | R-007; R-008 | Basic | Focused | n/a (configuration) | Database, file store, and backup encryption inspected | 1 / 0 |
| SI-2 | R-027 | Focused | Focused | 1,920 edge firmware updates; 214 IBOP server patches | 25 firmware updates (random); 25 server patches (random) | 9 / 1 |
| SI-3 | R-006 | Basic | Focused | About 15,500 endpoints and servers | EDR coverage report; 25 endpoints (random) | 8 / 0 |
| SI-4 | R-011; G-161 | Focused | Focused | 1,420 buildings (550 without OT sensors) | Rogue device test at 2 buildings without sensors and 2 with sensors | 10 / 2 |
| SI-7 | R-010 | Comprehensive | Focused | n/a | File integrity monitoring and nightly hash comparison examined; 1 tampered test schedule | 6 / 0 |
| SR-3 | R-017; G-171 | Focused | Focused | 9,400 purchase lines; AQ-1 inventory | 60 purchase lines (random); AQ-1 process walkthrough | 3 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4 (terminations), CM-6, CM-8, IA-5, RA-5, and SR-3.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 and AT-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-5, AC-6, IA-2, IR-4, IR-6, PS-3, PS-4 (PIV returns), SI-2, and SI-3.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 4,800 customer console accounts for inactivity and shared use, all 64 privileged accounts for MFA, all 186 log sources).
- **Stratification:** field device and termination samples were stratified so AQ-1 and AQ-2 sites, which hold most known weaknesses, were represented (12 of 60 terminations; 2 of the 6 field device sites).
- **Field device testing:** credential and configuration tests on customer-owned devices ran only with written customer approval, in maintenance windows, with the building engineer present (section 4).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a door or setpoint integrity control (CM-3, CM-3(1), AU-10, AC-5) or a remote access control (AC-17, MA-4) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, IBOP role matrix and audit trails, FSP change tickets and approvals, backup and failover test reports, vulnerability scans, OT sensor reports, the vendor register and SOC report reviews, screening logs, the incident response plan and materiality playbook, disclosure committee minutes, customer clearance rosters.
- **Interview:** Vice President, Building Technology Platforms; Vice President, Remote Operations; IBOP Platform Manager; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Vice President, Government Contracts Compliance; General Counsel; CFO; CISO; 30 randomly selected ROC operators and field technicians.
- **Test:** access tests with test accounts; atypical-use alert tests; pipeline gate tests with unapproved pushes; credential tests on 60 field devices; device tracing at 6 sites; network reachability tests from 2 customer IT networks and an AQ-1 site; rogue device tests at 4 buildings; TLS scans and packet captures at 2 sites; a tampered test door schedule in a test tenant; a backup restore observation.

## 4. Rules of engagement
- No test could change a door state, schedule, or setpoint in a live building. Integrity tests used a test tenant and a test schedule.
- Field device credential tests ran only with written customer approval, in scheduled maintenance windows, with the customer's building engineer present and a rollback plan.
- Rogue device tests used an audit-owned device with no customer data, pre-approved by the CISO, the Director of OT Security, and the customer's facilities director.
- No customer personal data left company systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: vendor default credentials on 5 field devices (reported and fixed 2026-08-14; customers informed the same day).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests; customer approvals for field tests requested |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Operating Officer, CISO, and Vice President, Building Technology Platforms |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (307 rows), and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 260 |
| Other than satisfied | 47 |
| **Total** | **307** |

**Controls with at least one Other than satisfied statement: 32 of 46:** AC-2, AC-6, AC-17, AT-3, AU-2, AU-6, AU-10, AU-12, CA-7, CM-2, CM-6, CM-8, CP-2, CP-4, CP-9, CP-10, IA-2, IA-5, IA-8, IR-4, IR-6, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SR-3.

**Fully Other than satisfied:** AC-6, AU-10, IA-8, SC-8 (each has a single determination statement).

**Themes:**
1. **Acquired businesses** drive the remote access (AC-17, MA-4, SC-7), identity (AC-2, PS-4, IA-2, AC-6, AU-10), logging (AU-2, AU-12), and incident handling (IR-4, IR-6) findings.
2. **The OT edge**: monitoring coverage (SI-4, CA-7, RA-5), default credentials (CM-6, IA-5), inventory (CM-8), segmentation and unencrypted BACnet (SC-7, SC-8), firmware and unsupported workstations (SI-2, SA-22).
3. **Recovery**: PACS administration RTO (CP-10, CP-2) and the untested program repository (CP-4, CP-9).
4. **Disclosure readiness**: the materiality step does not cover OT incidents with physical safety effects (IR-8).
5. **Supply chain scope**: screening does not reach AQ-1 offices and spares or subcontractor purchases (SR-3); 4 subcontractors with gateway access were unreviewed (SA-9).

**Strengths:** door and setpoint change control (CM-3, CM-3(1), AC-5), integrity monitoring (SI-7, which caught the tampered test schedule), privileged MFA (IA-2(1)), atypical-use alerts (AC-2(12)), encryption at rest (SC-28), ROC physical security (PE-3), screening of personnel (PS-3), risk assessment (RA-3), and the assessment program itself (CA-2) were all Satisfied.

**New finding during testing:** vendor default credentials on 5 of 60 sampled field devices (IA-05e.; CM-06b.). Added to the risk register as R-058 and to POAM-003.

## 7. POA&M summary
`poam.csv` holds 25 items: 19 from this assessment, 5 carried from the P03 gap analysis (POAM-011, POAM-015, POAM-020, POAM-022, POAM-023), and 1 from the P10 AI assessment (POAM-021), so leadership tracks one list.

| Risk level | Items |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 14 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the IBOP control environment is **effective with exceptions**. Enterprise common controls for identity, change control, integrity monitoring, backup, and encryption operate effectively, and the door and setpoint integrity supplements work as designed. The exceptions concentrate in components inherited from the acquisitions (AQ-1 remote access and identities, AQ-2 legacy instances) and at the OT edge. One weakness, the AQ-1 legacy remote-support tool, is rated Very High and is the subject of a condition in the authorization decision. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2, and the report serves as the 2026 annual independent assessment for the state customers.
