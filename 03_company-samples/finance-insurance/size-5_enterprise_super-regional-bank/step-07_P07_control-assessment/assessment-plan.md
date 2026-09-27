# Security Assessment Plan and Report: Cris Santos Company | Finance and Insurance | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company); Cris Santos Bank, N.A. |
| System assessed | Core Banking and Digital Channels Platform (CBDC), CSB-SYS-CBDC-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Finance and Insurance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): a technology audit director and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee (12 CFR 30 App. D I.E.8). None of the assessors designs or operates the controls. The GRC team and Technology and Operational Risk (second line) supported scoping only |
| Assessment window | 2026-06-15 to 2026-08-14 (fieldwork); report issued 2026-09-04; presented to the audit committee and the board risk committee on 2026-09-15 |
| Also satisfies | Regular testing of key controls by independent parties (12 CFR 30 App. B III.C.3); part of Internal Audit's risk-based audit plan (App. D II.C.3.(b)); annual assessment for the CBDC authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 8, AT 2, AU 5, CA 2, CM 3, CP 4, IA 5, IR 3, PS 1, RA 2, SA 1, SC 3, SI 4, SR 1), 269 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (payments fraud, destructive attack, mainframe privilege, third parties);
- cover App. B III.C.1 measures with gaps in P03;
- are Partially implemented in the SSP (P02 section 10.1);
- are common controls the CBDC inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-025; R-027; App. B III.C.1.a | Comprehensive | Comprehensive | 1,410 terminations of staff with core access (2026-01-01 to 2026-06-30); 2,860 account events on CBDC components | 60 terminations (random); 60 account events (random) | 21 / 5 |
| AC-2(3) | R-027 | Focused | Comprehensive | 9,800 workforce accounts and 214 service accounts on CBDC components | 100% (data analytic) | 3 / 1 |
| AC-3 | R-053 | Focused | Focused | 9,800 workforce users; business entitlement model | 25 users (random); 12 authorization test cases | 1 / 0 |
| AC-5 | R-020; App. B III.C.1.e | Comprehensive | Comprehensive | 310 users with payment or template roles | 100% | 2 / 0 |
| AC-6 | R-007 | Focused | Comprehensive | 2,410 PAM elevations to CBDC servers; 41 standing mainframe privileged IDs | 25 elevations (random); 100% of mainframe privileged IDs | 0 / 1 |
| AC-6(9) | R-007 | Basic | Focused | Privileged sessions | 10 sessions (random) | 1 / 0 |
| AC-7 | R-003 | Basic | Focused | n/a (configuration) | 2 test accounts per channel | 2 / 0 |
| AC-17 | R-019 | Focused | Comprehensive | 3 remote access paths; 14 vendors with remote support | 100% | 4 / 0 |
| AT-2 | R-001; App. B III.C.2 | Basic | Focused | 12,000 workforce | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-005; R-035 | Focused | Focused | About 640 commercial client service staff; 310 privileged users; 190 payments staff | 25 from each group (random) | 7 / 2 |
| AU-2 | R-026 | Focused | Comprehensive | 214 tier-1 log sources | 100% of sources | 5 / 1 |
| AU-6 | R-026; App. B III.C.1.f | Comprehensive | Focused | 26 weeks of Cyber Defense Center review records | 5 weeks (random) | 2 / 1 |
| AU-9 | R-002 | Basic | Focused | n/a (configuration) | Settings inspected; 1 deletion attempt | 2 / 0 |
| AU-10 | R-001 | Focused | Focused | About 21 million digital payment instructions (2026-01 to 2026-06) | 25 records (random) | 1 / 0 |
| AU-12 | R-026 | Basic | Focused | n/a (configuration) | 6 component types | 3 / 0 |
| CA-2 | App. D II.C.3 | Focused | Basic | n/a | 2025 assessment examined | 11 / 0 |
| CA-7 | R-046 | Focused | Basic | 6 monthly packages | 3 months (random) | 11 / 0 |
| CM-3 | App. B III.C.1.d | Comprehensive | Comprehensive | 2,310 changes to tier-1 systems (2026-01 to 2026-06) | 40 changes (random) | 10 / 0 |
| CM-5 | R-007 | Focused | Focused | CBDC production environments | 10 changes traced to PAM sessions | 6 / 0 |
| CM-6 | R-031 | Focused | Comprehensive | 48 core middleware servers | 100% | 4 / 2 |
| CP-2 | R-022; R-028 | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 22 / 2 |
| CP-4 | R-029 | Focused | Focused | 2 annual tests | 100% | 5 / 0 |
| CP-9 | R-002 | Focused | Focused | 4,380 backup jobs | 25 jobs (random); 1 restore observed | 5 / 1 |
| CP-10 | R-029 | Focused | Focused | 1 test | 100% | 2 / 0 |
| IA-2 | R-005 | Basic | Focused | 9,800 workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-007 | Focused | Comprehensive | 351 privileged accounts (310 distributed and cloud, 41 mainframe) | 100% | 1 / 0 |
| IA-5 | R-027 | Focused | Comprehensive | 214 service accounts on CBDC components | 100% (data analytic) | 9 / 1 |
| IA-8 | R-003 | Focused | Comprehensive | 2.4 million consumer users | 100% (data analytic) | 0 / 1 |
| IA-11 | R-034 | Focused | Focused | n/a (configuration) | 6 test scenarios | 0 / 1 |
| IR-4 | R-015; 12 CFR 53.3 | Focused | Focused | 388 security incidents (2026-01 to 2026-06) | 25 incidents (random) | 12 / 1 |
| IR-6 | R-015 | Basic | Focused | 388 incidents; 20 staff | 25 incidents; 20 staff | 2 / 0 |
| IR-8 | R-014; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 16 / 1 |
| PS-4 | R-025 | Comprehensive | Comprehensive | 1,410 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | App. B III.B | Focused | Basic | n/a | Assessment examined | 8 / 0 |
| RA-5 | R-032 | Focused | Focused | 6,120 critical and high findings | 60 findings (random) | 8 / 1 |
| SA-9 | R-023; App. B III.D.3 | Focused | Comprehensive | 41 critical third parties | 100% | 5 / 1 |
| SC-7 | R-019 | Comprehensive | Focused | n/a (architecture) | 1 reachability test | 6 / 0 |
| SC-8 | App. B III.C.1.c | Basic | Focused | All CBDC interfaces | 100% (TLS scan) | 1 / 0 |
| SC-28 | App. B III.C.1.c | Basic | Focused | n/a (configuration) | Settings inspected | 1 / 0 |
| SI-2 | R-032 | Focused | Focused | 1,240 patches applied | 25 patches (random) | 9 / 1 |
| SI-4 | R-017 | Focused | Focused | Treasury and digital channels | 2 test scenarios; 60 new-beneficiary wires (from P03) | 11 / 1 |
| SI-7 | R-007 | Comprehensive | Focused | n/a | 20 business days (random) | 6 / 0 |
| SI-10 | R-053 | Focused | Focused | 20 malformed requests | 100% in the test environment | 1 / 0 |
| SR-6 | R-024 | Focused | Comprehensive | 41 critical third parties | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, and RA-5.
- **Key controls, populations of 50 to 250, and changes:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AU-10, CP-9, IA-2, IR-4, IR-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; daily, 20 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 214 service accounts for password age and inactivity, all 48 core middleware servers against the baseline, and all 2.4 million consumer users for authenticator type).
- **Stratification:** AT-3 used 25 items from each of three role groups so the commercial client service staff were tested on their own.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects payment release or privileged access (AC-2 terminations, AC-5, AC-6, PS-4) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, mainframe entitlement exports, SIEM source inventory and review records, change tickets, backup and DR test reports, vulnerability data, vendor register and SOC report reviews, the incident response plan and materiality playbook, case management records.
- **Interview:** Head of Core Banking Technology; Head of Digital Banking Technology; Director of Identity and Access Management; Director of Data Center and Mainframe Operations; Director of Cyber Defense; Director of Enterprise Resilience; Head of Payments Operations; Director of Third-Party Risk Management; BSA/AML Officer; General Counsel; CISO; 20 randomly selected operations and branch staff.
- **Test:** lockout and step-up tests with test customer accounts; a new-beneficiary-plus-wire test in the treasury test environment; service account attribute analytics; a deletion attempt against the log archive; a reachability test from a branch network to core ports; TLS scans; malformed API requests in the test environment; a restore observation.

## 4. Rules of engagement
- No testing could move real money or affect customer service. Payment tests ran only in the treasury and digital test environments with synthetic accounts.
- Account analytics used extracts with account numbers masked; no customer information left the bank's systems, and workpaper screenshots are redacted.
- The branch reachability test used an audit-owned laptop with no customer data, pre-approved by the CISO and the branch manager.
- Critical exposures were reported to the CISO within 24 hours. One was: the enabled integration service account with a non-expiring password and query rights to the customer information file (reported 2026-08-13; disabled 2026-08-15).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-06-15 | Kickoff; document requests |
| 2026-06-22 to 2026-08-07 | Fieldwork (examine, interview, test) |
| 2026-08-10 to 2026-08-14 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Chief Risk Officer |
| 2026-09-15 | Presented to the audit committee and the board risk committee |

Deliverables: this plan and report, `assessment-results.csv` (269 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 242 |
| Other than satisfied | 27 |
| **Total** | **269** |

**Controls with at least one Other than satisfied statement: 20 of 44:** AC-2, AC-2(3), AC-6, AT-3, AU-2, AU-6, CM-6, CP-2, CP-9, IA-5, IA-8, IA-11, IR-4, IR-8, PS-4, RA-5, SA-9, SI-2, SI-4, SR-6.

**Fully Other than satisfied:** AC-6, IA-8, IA-11, SR-6 (each has a single determination statement).

**Themes:**
1. **The mainframe sits outside the enterprise identity controls.** Terminations (AC-2, PS-4), standing privileges (AC-6), and certification (AC-2j.) all fail on the mainframe while passing on distributed and cloud systems.
2. **Payment fraud detection has a blind spot.** Core maintenance events are not reviewed (AU-2, AU-6), and a new beneficiary paid under $100,000 raises no alert (SI-4). Customer step-up is skipped on trusted devices (IA-11), and 23% of consumers still use SMS (IA-8).
3. **Service identities are unmanaged.** A dormant integration account with a non-expiring password and customer information file access (IA-5, AC-2(3)) is the new finding.
4. **Resilience and third parties.** No isolated copy of core data (CP-9), plan assumptions that do not match the treasury vendor contract or manual screening capacity (CP-2), and late SOC reviews and missing contract terms (SA-9, SR-6).
5. **Process consistency.** Notification incident determination times missing in 2 of 25 incidents (IR-4), and no related-occurrence step for materiality (IR-8).

**Strengths:** separation of duties on payments (AC-5), privileged MFA (IA-2(1)), log protection (AU-9), payment non-repudiation (AU-10), change control (CM-3, CM-5), DR testing (CP-4, CP-10), encryption (SC-8, SC-28), and reconciliation and integrity checks (SI-7) were all Satisfied.

**New finding during testing:** the dormant integration service account (IA-05f.). Added to the risk register as R-027 and to POAM-013.

## 7. POA&M summary
`poam.csv` holds 24 items: 13 that originated in this assessment and 11 carried from the P03 gap analysis, so leadership tracks one list. Three of the P03 items (POAM-017, POAM-018, and POAM-020) were also confirmed by determination statements in this assessment.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 14 |

| Status | Items |
|---|---|
| In progress | 22 |
| Open | 2 |

## 8. Conclusion
Internal Audit concludes that the CBDC control environment is **effective with exceptions**. Enterprise common controls for workforce identity, change management, logging protection, encryption, and disaster recovery operate effectively. The exceptions concentrate in the mainframe's identity controls, payment fraud monitoring, service identities, isolation of core backups, and third-party oversight. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2.
