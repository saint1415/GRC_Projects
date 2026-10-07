# Security Assessment Plan and Report: Cris Santos Company | Utilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility) |
| System assessed | Distribution Operations Platform (DOP), CSC-DOP-01, per the SSP (P02), including the common controls it inherits from the OT security program and the enterprise platform |
| Tier / Vertical | Enterprise / Utilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with two OT specialists from the co-sourced firm. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. The NERC compliance team observed the CIP-related tests but did not assess |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork; DCC and substation testing 2026-08-11 to 2026-08-13); report issued 2026-09-04; presented to the audit committee and the risk and reliability committee on 2026-09-10 |
| Also satisfies | Annual assessment for the DOP authorization (P02 section 4.2); OT-STD-01 independent assessment; supporting evidence for the CIP internal controls program where controls are shared with the EMS |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 7, AT 2, AU 4, CA 2, CM 5, CP 5, IA 4, IR 3, MA 1, MP 1, PE 1, PS 1, RA 1, SA 2, SC 2, SI 4, SR 1), 300 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (vendor remote access into the ADMS, nation-state intrusion, ADMS recovery, field device security);
- are common controls the DOP inherits from the OT security program, which also serves the CIP-scope EMS, and that no other assessment covered this year;
- cover the CIP-related findings that the P03 gap analysis found in shared processes (terminations, supply chain);
- support the SEC disclosure process (IR-8).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-019; R-014; OT-STD-01 account rules | Comprehensive | Comprehensive | 1,322 ADMS and OMS account events (2026-01-01 to 2026-06-30); 412 ADMS domain accounts | 60 account events (random); 412 accounts (data analytic) | 23 / 3 |
| AC-3 | R-024; switching order controls | Focused | Focused | 96 consoles; 4 ADMS roles | 4 roles tested with test accounts | 1 / 0 |
| AC-4 | R-025 | Comprehensive | Comprehensive | 486 DMZ rules | 486 (full rule review); 1 reachability test | 0 / 1 |
| AC-5 | R-024 | Focused | Focused | 19 privileged administrators | 19 (full) | 2 / 0 |
| AC-6 | R-039 | Focused | Focused | 2,140 OT PAM elevation sessions | 25 sessions (random) | 1 / 0 |
| AC-7 | R-020 | Basic | Focused | n/a (configuration) | 2 test accounts (engineering) and 1 console alert test | 2 / 0 |
| AC-17 | R-002 | Comprehensive | Comprehensive | 64 vendor remote access paths into OT; 3,410 remote sessions to the ADMS | 64 paths (full); 25 sessions (random) | 3 / 1 |
| AT-2 | R-020 | Basic | Focused | About 12,000 workforce (210 DCC staff) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-020; R-024 | Focused | Focused | 210 DCC operators and engineers | 40 operators (random) | 8 / 1 |
| AU-2 | R-007 | Focused | Focused | n/a (configuration) | 6 event types generated in the quality environment | 6 / 0 |
| AU-6 | R-002; R-007 | Comprehensive | Comprehensive | 26 weekly reviews; 58 ADMS and DMZ log sources | 5 weeks (random) plus the 2 migration weeks; 58 sources (full) | 2 / 1 |
| AU-9 | R-039 | Basic | Focused | n/a (configuration) | 1 deletion test | 2 / 0 |
| AU-12 | R-007 | Basic | Focused | 34 servers and hosts | 10 (random) | 3 / 0 |
| CA-2 | R-040 | Focused | Focused | 12 internal compliance checks | 12 (full) | 10 / 1 |
| CA-7 | R-007 | Focused | Basic | 6 monthly packages | 3 months (random) | 11 / 0 |
| CM-2 | R-024 | Focused | Focused | 118 ADMS servers and consoles | 25 (random) | 5 / 0 |
| CM-3 | R-024 | Comprehensive | Comprehensive | 164 ADMS changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 9 / 1 |
| CM-6 | R-021 | Focused | Comprehensive | 118 servers and consoles | 118 (data analytic) | 6 / 0 |
| CM-7 | R-025 | Focused | Focused | 118 servers and consoles | 10 (random) | 6 / 0 |
| CM-8 | R-007; R-023 | Comprehensive | Comprehensive | About 41,000 field devices and 418 substation gateways | 60 physical devices traced to the CMDB (random, 6 substations) | 4 / 2 |
| CP-2 | R-003; R-012 | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 22 / 2 |
| CP-4 | R-003 | Focused | Focused | 1 annual test | 1 (full) | 5 / 0 |
| CP-7 | R-003 | Focused | Focused | 1 alternate site | 1 (full) | 3 / 1 |
| CP-9 | R-004 | Focused | Focused | 182 daily ADMS backups; 26 weekly offline copies | 25 daily jobs (random); 5 weekly copies; 1 restore observed | 6 / 0 |
| CP-10 | R-003 | Focused | Focused | 1 test | 1 (full) | 0 / 2 |
| IA-2 | R-020 | Basic | Focused | About 4,800 users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-002; R-039 | Focused | Comprehensive | 19 privileged ADMS accounts; 63 vendor accounts | 100% | 1 / 0 |
| IA-3 | R-006 | Focused | Comprehensive | 418 substation gateways | 418 (inventory review); 2 captures | 0 / 1 |
| IA-5 | R-022 | Focused | Comprehensive | About 3,900 capacitor controls and line sensors on IP networks | 60 devices (random) | 9 / 1 |
| IR-4 | R-001; R-002 | Focused | Focused | 74 OT security incidents (2025-07-01 to 2026-06-30) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-001 | Basic | Focused | 74 incidents; 210 DCC staff | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-016 | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 16 / 1 |
| MA-4 | R-002 | Comprehensive | Comprehensive | 64 vendor paths; 3,410 sessions | 64 (full); 25 sessions (random) | 5 / 3 |
| MP-7 | R-057 | Basic | Focused | 96 consoles | 10 consoles tested with a test USB drive | 2 / 0 |
| PE-3 | R-010 | Focused | Focused | 2 control rooms; 6 server rooms | 8 doors tested | 12 / 0 |
| PS-4 | R-014 | Comprehensive | Comprehensive | 1,180 terminations (214 with CIP access) | 60 terminations (stratified: 40 with CIP access, 20 other) | 4 / 1 |
| RA-5 | R-023 | Focused | Focused | 2,210 open and closed vulnerability findings | 60 findings (random) | 8 / 1 |
| SA-9 | R-034; R-026 | Focused | Comprehensive | 9 external services | 9 (full) | 4 / 2 |
| SA-22 | R-021 | Focused | Comprehensive | 118 servers and consoles | 118 (full) | 1 / 1 |
| SC-7 | R-002; R-025 | Comprehensive | Focused | n/a (architecture) | Discovery scan at the DCC; reachability test from the data platform | 4 / 2 |
| SC-8 | R-006 | Basic | Focused | 418 substations | 418 (inventory); 2 captures | 0 / 1 |
| SI-2 | R-021; R-023 | Focused | Focused | 312 ADMS host patches; 41 field device firmware advisories | 25 patches (random); 41 advisories (full) | 9 / 1 |
| SI-3 | R-004 | Basic | Focused | 118 servers and consoles | 118 (data analytic) | 8 / 0 |
| SI-4 | R-001; R-007 | Focused | Focused | 418 distribution substations (247 without sensors) | 2 substations without sensors | 10 / 2 |
| SI-7 | R-011 | Focused | Focused | 22 ADMS servers | 22 (full) | 6 / 0 |
| SR-6 | R-030 | Focused | Comprehensive | 88 CIP-scope procurements | 25 (random; P03 sample reperformed) | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, CM-8, IA-5, PS-4, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for AT-3 and CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-6, AC-17 (sessions), CM-2, CP-9, IA-2, IR-4, IR-6, SI-2, and SR-6 (the P03 sample of 25, reperformed).
- **Recurring controls:** weekly, 5 occurrences (plus the two SIEM migration weeks, selected on purpose); monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 486 DMZ rules, all 412 ADMS domain accounts, all 418 substation gateways, all 64 vendor remote access paths).
- **Stratification:** terminations were stratified so individuals with CIP access (18% of terminations) got 40 of 60 items, because their revocation clock is 24 hours.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects grid safety or carries a NERC timeline (AC-17, MA-4, IA-5, PS-4 for CIP access) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), OT-STD-01, identity governance and OT PAM records, ADMS role tables, change tickets and impact analyses, backup and failover reports, vulnerability and firmware records, vendor contracts, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Distribution Operations; Director, Distribution Control Center; ADMS Platform Manager; OMS Application Manager; Director, OT Security; Director, OT Engineering; Director, Security Operations; General Counsel; CFO; CISO; 20 randomly selected DCC staff.
- **Test:** access tests with test accounts in the ADMS quality environment; lockout and alert tests; a network discovery scan at the DCC; a reachability test from the corporate data platform to the historian; default-credential tests on field devices; protocol captures at two legacy substations; a rogue device test at two substations without OT sensors; a restore observation.

## 4. Rules of engagement
- No test could affect grid operations. Every field and DCC test was scheduled with the Director, Distribution Control Center, outside switching windows and storm watches, with an operator on the line and a stop word.
- Default-credential tests used read-only logons and stopped at the login banner; no setting was changed.
- The rogue device test used an audit-owned device with no company data, pre-approved by the CISO and the Director, OT Engineering, and was removed within 30 minutes.
- No test touched the EMS, its Electronic Security Perimeter, or any high or medium impact BES Cyber System. Shared controls were tested on the DOP side only.
- No customer data left company systems; screenshots in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: the ADMS vendor remote support tunnel (reported 2026-08-12, disabled 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); DCC and substation tests 2026-08-11 to 2026-08-13 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Distribution Operations |
| 2026-09-10 | Presented to the audit committee and the risk and reliability committee |

Deliverables: this plan and report, `assessment-results.csv` (300 rows), and `poam.csv` (29 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 266 |
| Other than satisfied | 34 |
| **Total** | **300** |

**Controls with at least one Other than satisfied statement: 24 of 46:** AC-2, AC-4, AC-17, AT-3, AU-6, CA-2, CM-3, CM-8, CP-2, CP-7, CP-10, IA-3, IA-5, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SR-6.

**Fully Other than satisfied:** AC-4, CP-10, IA-3, SC-8, and SR-6.

**Themes:**
1. **Vendor paths into OT.** The ADMS vendor's remote support appliance bypassed the jump hosts (AC-17, MA-4, SC-7), and two OT contracts lack security terms (SA-9). This is P01 risk R-002, the only Very High risk.
2. **The grid edge.** Legacy gateways cannot authenticate or protect commands (IA-3, SC-8), default passwords remain on field devices (IA-5), monitoring covers 41% of distribution substations (SI-4), and firmware and inventory lag (RA-5, SI-2, CM-8).
3. **Recovery.** The ADMS cannot yet fail over within its 2-hour RTO (CP-7, CP-10), and the OMS standby is untested at storm volume (CP-2).
4. **Governance.** The SEC materiality step has not been exercised with an OT scenario (IR-8), and internal CIP checks are done by the team that operates the controls (CA-2).

**Strengths:** least privilege and separation of duties in the ADMS (AC-3, AC-5, AC-6), MFA for privileged and vendor access through PAM (IA-2(1)), logging and log protection (AU-2, AU-9, AU-12), configuration baselines (CM-2, CM-6, CM-7), offline backups (CP-9), malware protection and integrity monitoring (SI-3, SI-7), and incident handling (IR-4, IR-6) were all Satisfied.

**New finding during testing:** the ADMS vendor remote support tunnel (AC-17b.). It was added to the risk register as the trigger for R-002 and to POAM-001.

## 7. POA&M summary
`poam.csv` holds 29 items: 17 from this assessment (POAM-001 to POAM-017), 8 carried from the P03 gap analysis (POAM-019 to POAM-026), and 4 from other sources (POAM-018 from the P01 risk register and P05 BIA, POAM-027 and POAM-028 from the P05 BIA, and POAM-029 from the P10 AI assessment), so leadership tracks one list. POAM-019 and POAM-027 were also confirmed by this assessment (SR-6 and CP-2).

| Risk level | Items |
|---|---|
| High | 13 |
| Moderate | 14 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 25 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the DOP control environment is **effective with exceptions**. The common controls the DOP inherits from the OT security program and the enterprise platform for identity, privileged access, logging, backup, and malware protection operate effectively. The exceptions concentrate at the boundaries: one unmanaged vendor path, legacy field equipment, recovery speed, and the independence of internal CIP checks. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2.
