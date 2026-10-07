# Security Assessment Plan and Report: Cris Santos Company | Other Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded national electronics and device repair chain) |
| System assessed | Service Ticketing and Point-of-Sale Platform (STPP), CSC-SYS-STPP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Other Services (except Public Administration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. The QSA's PCI DSS assessment is separate (fieldwork 2026-10-19 to 2026-11-20) |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also satisfies | Annual assessment for the STPP authorization (P02 section 4.2); HIPAA evaluation input for SL-2 common controls (45 CFR 164.308(a)(8)); evidence for the SOC 2 readiness work (P09) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 7, AT 1, AU 4, CA 2, CM 4, CP 3, IA 3, IR 3, MP 2, PE 1, PS 3, RA 1, SA 2, SC 3, SI 4, SR 1), 251 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 that touch the STPP (passcodes in records, technician access, payment pages, sanitization, materiality);
- carry PCI DSS requirements the QSA will test in the 2026 ROC, so weaknesses are found first;
- implement policy statements in P06 (37 of the 51 statements are tested through these controls);
- are common controls the STPP inherits and that no other assessment covered this year.

**Out of scope:** the 160 AC stores. They are outside the STPP boundary until conversion; their conditions were sampled in the P03 gap analysis (10 stores) and are tracked in the POA&M as P03-sourced items.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-064; R-028; PCI DSS 8.2 | Comprehensive | Comprehensive | About 41,000 STPP account events (2026-01-01 to 2026-06-30); about 5,900 terminations of staff with STPP access | 60 account events (random); 60 terminations (random) | 23 / 3 |
| AC-2(3) | R-064 | Focused | Comprehensive | About 9,800 STPP workforce accounts; 6 SL-1 client credentials | 100% (data analytic) | 4 / 0 |
| AC-3 | R-002; R-005; PCI DSS 7.2 | Focused | Comprehensive | 9,800 STPP accounts; 31 million tickets | 100% (role analytics); 25 test tickets | 0 / 1 |
| AC-5 | R-040 | Focused | Focused | About 1,120 store manager accounts with refund approval; production database access | 25 refunds over $500 (random); PAM approvals for 10 database sessions | 2 / 0 |
| AC-6 | R-005; R-047 | Focused | Focused | About 3,400 PAM elevation sessions to STPP components | 25 sessions (random) | 1 / 0 |
| AC-6(9) | R-047 | Basic | Focused | As AC-6 | 10 recordings (random) | 1 / 0 |
| AC-17 | R-004 | Focused | Comprehensive | 3 remote access paths into the STPP and store technology | 100% | 4 / 0 |
| AT-2 | R-020; PCI DSS 12.6 | Basic | Focused | 12,000 workforce | 60 training records (random); phishing results for 6 months | 10 / 0 |
| AU-2 | R-002 | Focused | Focused | n/a (configuration) | 8 event types generated in test (ticket view, passcode view, export, refund, role change, API call, sign-in, admin action) | 6 / 0 |
| AU-6 | R-005; R-002 | Comprehensive | Comprehensive | 26 weeks of SOC review records; STPP alert rules | 5 weeks (random); 100% of STPP rules | 2 / 1 |
| AU-9 | R-046 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-12 | R-002 | Basic | Focused | n/a (configuration) | 4 STPP services | 3 / 0 |
| CA-7 | PCI DSS 10.4 | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CA-8 | R-012; PCI DSS 11.4 | Focused | Comprehensive | 2026 penetration test; 2 segmentation tests | 100% | 1 / 0 |
| CM-3 | R-059 | Comprehensive | Comprehensive | About 2,900 STPP changes (2026-01-01 to 2026-06-30) | 40 changes (random) | 10 / 0 |
| CM-6 | R-030 | Focused | Comprehensive | About 60 STPP containers; managed database; front end | 100% (configuration scan) | 6 / 0 |
| CM-6(2) | R-008; PCI DSS 6.4.3, 11.6.1 | Focused | Comprehensive | Payment pages (main checkout; mobile web deposit page) | 100% | 0 / 1 |
| CM-8 | R-048; PCI DSS 9.5.1.1 | Comprehensive | Comprehensive | About 3,100 PIN pads; cloud components | Full reconciliation with the processor list; 25 cloud components traced | 5 / 1 |
| CP-4 | R-003 | Focused | Focused | 1 annual failover test | 100% | 5 / 0 |
| CP-9 | R-046 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-003 | Focused | Focused | 1 DR test | 100% | 2 / 0 |
| IA-2 | R-020 | Basic | Focused | About 9,800 workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-029 | Focused | Comprehensive | 34 privileged STPP and cloud accounts | 100% | 1 / 0 |
| IA-5 | R-057; PCI DSS 2.2.2 | Focused | Comprehensive | Password policy; secrets; 14 sanitization stations at 3 depots | 100% of stations (tested with vendor approval) | 9 / 1 |
| IR-4 | R-005 | Focused | Focused | About 2,600 SOC cases (14 technician access complaints) | 25 cases (random) plus all 14 complaints | 13 / 0 |
| IR-6 | PCI DSS 12.10.1 | Basic | Focused | About 2,600 cases; 20 staff interviews | 25 cases; 20 staff | 2 / 0 |
| IR-8 | R-009; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan and playbook examined; interviews with the General Counsel, CFO, and CISO | 15 / 2 |
| MP-6 | R-006; Fla. Stat. 501.171(8) | Comprehensive | Focused | About 1,900 retired counter tablets and laptops (2026-01 to 2026-06) | 25 devices (random, all depots) | 3 / 1 |
| MP-7 | R-005 | Focused | Focused | About 6,900 core bench workstations; registered transfer stations | 25 workstations (random) tested with a USB storage device | 2 / 0 |
| PE-3 | R-033; R-060 | Basic | Focused | About 1,120 store back rooms; 3 depot cages; lab | 25 badge reviews (random); 3 depot walkthroughs | 12 / 0 |
| PS-3 | PCI DSS 12.7; Manufacturer A agreement | Basic | Focused | About 4,100 hires (2026-01 to 2026-06) | 60 (random) | 3 / 0 |
| PS-4 | R-064 | Comprehensive | Comprehensive | About 5,900 terminations | 60 (same sample as AC-2) | 4 / 1 |
| PS-6 | R-005 | Focused | Focused | About 6,000 technicians | 60 (random) | 3 / 1 |
| RA-5 | R-014 | Focused | Focused | About 2,200 vulnerability findings on STPP components and tablets | 60 findings (random) | 9 / 0 |
| SA-9 | R-024; PCI DSS 12.8 | Focused | Comprehensive | 58 TPSPs | 100% | 4 / 2 |
| SA-11 | R-012; R-059 | Focused | Focused | 2026 STPP releases; penetration test findings | 10 releases (random); all high findings | 8 / 1 |
| SC-7 | R-004; PCI DSS 1.3 | Comprehensive | Focused | n/a (architecture) | Segmentation test from a core store bench VLAN and guest Wi-Fi to the POS VLAN and STPP | 6 / 0 |
| SC-8 | PCI DSS 4.2 | Basic | Focused | All STPP interfaces | 100% (TLS scan); P2PE listing check | 1 / 0 |
| SC-28 | R-002 | Basic | Focused | n/a (configuration) | Database, backups, and passcode field encryption inspected | 1 / 0 |
| SI-2 | R-014 | Focused | Focused | About 210 critical tablet and container updates | 25 (random) | 9 / 1 |
| SI-4 | R-002; R-045 | Focused | Focused | STPP and store monitoring rules | Bulk export test with a test account; 100% of STPP rules | 12 / 0 |
| SI-7 | R-008; PCI DSS 11.5.2, 11.6.1 | Comprehensive | Focused | n/a | File integrity and payment page integrity tools examined | 5 / 1 |
| SI-12 | R-002; PCI DSS 3.2.1; Fla. Stat. 501.171(8) | Comprehensive | Comprehensive | 31 million tickets | 100% (DLP scan) | 2 / 2 |
| SR-9 | R-048; PCI DSS 9.5.1.2 | Focused | Focused | About 49,900 core store-weeks of PIN pad inspections (2026) | 60 store-weeks (random) | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-3, PS-4, PS-6, AT-2, RA-5, and SR-9.
- **Key manual controls, populations of 50 to 250, or high-risk transaction tests:** 40 items. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-5, AC-6, IA-2, IR-4, IR-6, MP-6, MP-7, PE-3, CP-9, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (all 9,800 accounts for inactivity, the full STPP ticket table for passcode and card-number patterns, all 14 sanitization stations for default credentials, all 58 TPSPs).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects customer passcodes, card data, or sanitization (AC-3, SI-12, MP-6, IA-5 on sanitization stations, CM-6(2), SR-9) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, the STPP role matrix and audit logs, change records and pipeline reports, backup and DR test reports, vulnerability scans and the 2026 penetration test, the TPSP list and AOC tracker, sanitization records, PIN pad inventory and inspection logs, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Chief Digital Officer; STPP Engineering Manager; Vice President, Payments; PCI Program Manager; Director of Security Operations; Director of Identity and Access Management; Director of Sanitization and Asset Recovery; General Counsel; CFO; CISO; 6 store managers; 20 randomly selected store staff.
- **Test:** access tests with test accounts; a bulk export test; default-credential tests on sanitization stations (with vendor approval, outside production hours); USB storage tests on 25 bench workstations; a segmentation test from a core store bench VLAN and guest Wi-Fi; a test change to a staging payment page; TLS scans; re-test of 5 sanitized devices with forensic tools; a restore observation.

## 4. Rules of engagement
- No testing could affect store payments, intake, or release. Store tests ran before opening hours with the store manager present.
- Payment page tests ran only in staging. No live card data was used.
- Default-credential tests on sanitization stations used the vendor's documented accounts, with the Director of Sanitization and Asset Recovery's approval, outside production hours.
- No customer data left the company's systems. Screenshots and exports in workpapers are redacted; the DLP scan output was reviewed inside the STPP environment.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor passwords on 6 sanitization stations at Depot West (reported 2026-08-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Chief Digital Officer |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (251 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 230 |
| Other than satisfied | 21 |
| **Total** | **251** |

**Controls with at least one Other than satisfied statement: 16 of 44:** AC-2, AC-3, AU-6, CM-6(2), CM-8, IA-5, IR-8, MP-6, PS-4, PS-6, SA-9, SA-11, SI-2, SI-7, SI-12, SR-9.

**Fully Other than satisfied:** AC-3, CM-6(2), SR-9 (each has a single determination statement).

**Themes:**
1. **Passcodes and card numbers outside their controls.** The restricted passcode field works, but free-text notes hold passcode-like strings and card numbers, are visible to every role at a location, and are kept 7 years (AC-3, SI-12).
2. **Customer devices and sanitization.** Passcode views and bench sessions are reviewed only on alert (AU-6), some technicians have not re-signed the confidentiality agreement (PS-6), and Depot West cannot show sanitization for every retired device and still had vendor default passwords on its stations (MP-6, IA-5).
3. **Payments.** The mobile web deposit page is outside script change detection (CM-6(2), SI-7), and PIN pad inspections and spare inventory have gaps (SR-9, CM-8).
4. **Store terminations** depend on store managers entering HR events on time (AC-2, PS-4).
5. **Disclosure readiness:** the plan and materiality playbook have not been adapted for a card compromise with customer data exposure, or updated after the AC acquisition (IR-8).
6. **Third parties and development:** TPSP AOCs and responsibility matrices (SA-9); release testing missed an authorization flaw in the SL-1 claims API (SA-11).

**Strengths:** identity and privileged access (IA-2, IA-2(1), AC-6, AC-6(9), AC-17), immutable logs and backups (AU-9, CP-9), change management (CM-3), segmentation of core stores (SC-7), detection of bulk exports (SI-4), USB control on bench workstations (MP-7), and recovery (CP-4, CP-10) were all Satisfied.

**New finding during testing:** vendor default administrator passwords on 6 sanitization stations at Depot West (IA-05e.). Added to the risk register as R-057 and to POAM-006.

## 7. POA&M summary
`poam.csv` holds 24 items: 10 from this assessment, 12 carried from the P03 gap analysis (mostly the AC stores, which are outside the STPP boundary), and 2 from the P10 AI assessment, so leadership tracks one list.

| Risk level | Items |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 12 |
| Low | 3 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

## 8. Conclusion
Internal Audit concludes that the STPP control environment is **effective with exceptions**. Enterprise common controls for identity, logging, backup, change, and monitoring operate effectively. The exceptions concentrate where the repair business differs from other retailers (passcodes, technician access, sanitization) and in payment controls the QSA will test next (payment pages, PIN pads). Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
