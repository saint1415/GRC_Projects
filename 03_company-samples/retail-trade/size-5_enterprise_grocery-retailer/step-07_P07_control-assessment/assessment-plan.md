# Security Assessment Plan and Report: Cris Santos Company | Retail Trade | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional supermarket chain; 112 stores in FL, GA, AL, SC, TN; online ordering) |
| System assessed | Omnichannel Commerce and Payments Platform (OCPP) per the SSP (P02), including the enterprise common controls it inherits (CCP-01 to CCP-09) |
| Tier / Vertical | Enterprise / Retail Trade |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors from the 6-person IT audit team under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team and the PCI Program Manager (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee of the board on 2026-09-10 |
| Also satisfies | Annual independent assessment for the OCPP authorization (P02 section 4.2; POL-01 4.14); evidence the QSA can reuse for the 2026 ROC where the PCI DSS testing procedures allow (fieldwork 2026-10-19 to 2026-11-20). This assessment is **not** a PCI DSS assessment and does not replace the ROC |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 6, AT 1, AU 5, CA 1, CM 6, CP 4, IA 4, IR 3, MA 1, PS 1, RA 2, SA 1, SC 4, SI 4, SR 1), 279 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware, e-commerce skimming, store OT, third parties, disclosure);
- cover PCI DSS requirements with partially met rows in P03 that sit inside the OCPP boundary (payment pages, logging review, change control, TPSP oversight, inventory);
- test the hybrid controls the OCPP shares with the store network, identity, and security operations providers;
- are common controls the OCPP inherits that no other assessment covered this year.

**Not in scope:** the 14 acquired-banner (AB) stores' legacy POS, store servers, and processor link, which are outside the OCPP boundary until conversion (P02 section 4.3). AB staff and events were tested only where they touch the OCPP (order management accounts, terminations, incident handling). AB gaps found by the P03 gap analysis are carried into the POA&M so leadership tracks one list.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-019; R-018; PCI DSS 8.2 | Comprehensive | Comprehensive | 2,310 OCPP account events (2026-01-01 to 2026-06-30); 2,140 terminations of staff with OCPP access (96 at AB stores) | 60 account events (random); 60 terminations (stratified: 50 core, 10 AB) | 23 / 3 |
| AC-2(3) | R-034; R-022 | Focused | Comprehensive | About 18,600 OCPP accounts (about 6,200 SSO accounts and about 12,400 POS operator IDs at core stores) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-008 | Focused | Focused | About 6,200 workforce users across order management, storefront admin, POS back office, and switch console roles | 25 users (random) | 1 / 0 |
| AC-5 | R-027; R-063 | Comprehensive | Comprehensive | 9 payment switch administrators; 14 storefront release managers; routing table approvers | 100% | 2 / 0 |
| AC-6 | R-021; R-035 | Focused | Focused | 2,900 PAM elevation sessions to store controllers, switch servers, and production containers | 25 sessions (random) | 1 / 0 |
| AC-17 | R-007 | Focused | Comprehensive | 5 remote access paths into store and OCPP networks; remote tool scan of the 98 core store networks | 100% | 3 / 1 |
| AT-2 | R-021; R-024; PCI DSS 12.6 | Basic | Focused | About 8,900 workforce members with OCPP access (including cashiers at core stores) | 60 training records (random); phishing results for 6 months | 10 / 0 |
| AU-2 | R-050; PCI DSS 10.2 | Focused | Focused | n/a (configuration) | 6 event types generated in test on a store controller, the switch, and the storefront admin console | 6 / 0 |
| AU-6 | R-002; R-003; PCI DSS 10.4 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 58 log sources on the OCPP card and order paths | 5 weeks (random); 100% of log sources | 1 / 2 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | PCI DSS 10.5.1 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-050 | Basic | Focused | n/a (configuration) | 10 components (4 store controllers at 2 stores, 2 switch servers, 4 container clusters) | 3 / 0 |
| CA-7 | R-054 | Focused | Basic | 6 monthly PCI DSS control metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-004 | Focused | Focused | 4 baseline sets (registers, store controllers, switch servers, container base images) | 100% | 5 / 0 |
| CM-3 | R-027; R-002; PCI DSS 6.5.1 | Comprehensive | Comprehensive | 96 payment switch changes and 314 other OCPP changes (2026-01-01 to 2026-06-30) | 40 switch changes (random); 25 payment page changes (random) | 8 / 2 |
| CM-5 | R-025 | Focused | Focused | 410 OCPP changes | 10 changes traced to PAM sessions and pipeline runs | 6 / 0 |
| CM-6 | R-028; PCI DSS 2.2 | Focused | Focused | 196 core store controllers | 25 store controllers (random) | 4 / 2 |
| CM-7 | R-004 | Focused | Focused | n/a (configuration) | 10 registers and 10 store controllers at 4 stores | 6 / 0 |
| CM-8 | R-024; PCI DSS 9.5.1.1 | Comprehensive | Comprehensive | About 2,780 PIN pads and 196 store controllers at core stores | 100% reconciliation (data analytic); 60 physical devices traced at 6 stores (random) | 5 / 1 |
| CP-2 | R-005 | Comprehensive | Focused | n/a (plan) | OCPP contingency plan v6 examined; interviews with the Vice President, Payments, the Payment Switch Manager, and 3 store leads | 23 / 1 |
| CP-4 | R-017; 7 CFR 274.3(c)(4) | Focused | Focused | 1 annual switch failover test (2026-05-09); manual voucher drill records for 112 stores | 100% | 3 / 2 |
| CP-9 | R-001 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-017 | Focused | Focused | 1 failover test | 100% | 1 / 1 |
| IA-2 | R-021 | Basic | Focused | About 6,200 workforce SSO accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-021 | Focused | Comprehensive | 64 privileged accounts for store controllers, the switch, and production | 100% | 1 / 0 |
| IA-5 | R-035; R-062 | Focused | Comprehensive | 140 vaulted service account secrets; ESL base stations at 40 stores | 100% of service accounts; ESL base stations at 12 stores (random), tested with vendor approval after store hours | 9 / 1 |
| IA-8 | R-009 | Focused | Comprehensive | Customer sign-in configuration (about 1.4 million online accounts) | Configuration tested with 4 test customer accounts | 1 / 0 |
| IR-4 | R-001; R-002 | Focused | Focused | 238 security incidents (2026-01-01 to 2026-06-30) plus 9 security events found in the AB help desk log | 25 incidents (random) plus all 9 AB events | 11 / 2 |
| IR-6 | R-024 | Basic | Focused | 238 incidents; 20 store staff interviews | 25 incidents; 20 cashiers and front-end leads at 5 stores | 2 / 0 |
| IR-8 | R-010 | Comprehensive | Focused | n/a (plan) | IR plan v5 and materiality playbook examined; interviews with the General Counsel, CFO, CISO, and Vice President, Payments | 15 / 2 |
| MA-4 | R-007 | Focused | Comprehensive | 1,120 vendor maintenance sessions through PAM; remote tool scan of 98 core store networks | 25 PAM sessions (random); 100% of scan results | 5 / 3 |
| PS-4 | R-019 | Comprehensive | Comprehensive | 2,140 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | R-053; PCI DSS 12.3.1 | Focused | Basic | n/a | 2026 risk assessment (P01) and the targeted risk analyses register (11 requirements that need one) examined | 7 / 1 |
| RA-5 | R-028; R-020 | Focused | Focused | 2,460 vulnerability findings on OCPP components | 60 findings (random) | 8 / 1 |
| SA-9 | R-006; PCI DSS 12.8 | Focused | Comprehensive | 71 TPSPs | 100% | 4 / 2 |
| SC-7 | R-007; R-029; PCI DSS 1.2 | Comprehensive | Focused | n/a (architecture); NAC coverage report for 98 core stores | Segmentation tests at 6 stores (3 with NAC, 3 without) | 4 / 2 |
| SC-8 | R-052; PCI DSS 4.2.1 | Basic | Focused | All OCPP external endpoints and store-to-switch and switch-to-processor links | 100% (TLS scan) | 1 / 0 |
| SC-12 | R-004 | Focused | Focused | Key inventory | 100% | 2 / 0 |
| SC-28 | R-008 | Basic | Focused | n/a (configuration) | Order and token database encryption inspected | 1 / 0 |
| SI-2 | R-028 | Focused | Focused | 318 patches on OCPP components | 25 patches (random) | 9 / 1 |
| SI-3 | R-001; R-004 | Focused | Focused | EDR coverage report for OCPP servers and store controllers | 100% | 8 / 0 |
| SI-4 | R-029 | Focused | Focused | 98 core stores (37 without NAC); SOC metrics | Rogue device tests at 3 stores (2 without NAC, 1 with NAC) | 11 / 1 |
| SI-7 | R-002; PCI DSS 6.4.3; 11.6.1 | Comprehensive | Comprehensive | 6 pages that host or lead to payment fields (main checkout, express checkout, cart); 47 scripts | 100% | 4 / 2 |
| SR-6 | R-006; R-051 | Focused | Comprehensive | 71 TPSPs (same population as SA-9) | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8 (physical trace), and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (96 switch changes).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CM-3 (payment page changes), CM-6, CP-9, IA-2, IR-4, IR-6, MA-4, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 18,600 OCPP accounts for inactivity, all 2,780 PIN pads against lane maps, all 71 TPSPs, and all 47 payment page scripts).
- **Stratification:** terminations were stratified so the AB staff with OCPP access (about 4% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key payment control (SI-7 payment page integrity, CM-3 switch changes, AC-5) makes the statement Other than satisfied.
- **Reuse by the QSA:** populations and sample sizes were aligned with the PCI DSS testing procedures where possible; the QSA decides what it can rely on.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, POS operator ID exports, change tickets, configuration compliance reports, the PIN pad inventory and lane maps, payment page script inventory and tamper detection reports, backup and failover test reports, vulnerability scans and ASV reports, the TPSP list and AOC tracker, the incident response plan and materiality playbook, and disclosure committee materials.
- **Interview:** Chief Digital Officer; Vice President, Payments; PCI Program Manager; Director of E-commerce Engineering; Director of Store Technology; Payment Switch Manager; Director of Identity and Access Management; Director of Security Operations; Director of Network Engineering; Director of Facilities Engineering; Director of Third-Party Risk Management; General Counsel; CFO; CISO; 20 cashiers and front-end leads at 5 stores.
- **Test:** access tests with test accounts; default credential tests on ESL base stations (with vendor approval, after store hours); segmentation tests at 6 stores; rogue device tests at 3 stores; TLS scans; a log deletion attempt; a remote tool scan of core store networks; a restore observation; test customer accounts on the storefront.

## 4. Rules of engagement
- No testing could affect checkout, online ordering, or SNAP EBT acceptance. Store tests ran between 23:00 and 05:00 local time with the store manager and the Director of Store Technology's on-call engineer present; no tests ran in the 5 days before a holiday.
- Nothing was tested on production payment pages; script and tamper detection tests ran against the pre-production storefront that mirrors production.
- The rogue device and segmentation tests used audit-owned laptops with no card or customer data, pre-approved by the CISO and the store operations regional vice presidents.
- No card data or customer personal information left the company's systems. Screenshots and exports in workpapers are masked to the last 4 digits or redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: default vendor credentials on ESL base stations at 3 stores (reported 2026-08-12; credentials changed at those stores by 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Digital Officer, the CFO, and the CISO |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee of the board |

Deliverables: this plan and report, `assessment-results.csv` (279 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 243 |
| Other than satisfied | 36 |
| **Total** | **279** |

**Controls with at least one Other than satisfied statement: 23 of 44:** AC-2, AC-2(3), AC-17, AU-6, CM-3, CM-6, CM-8, CP-2, CP-4, CP-10, IA-5, IR-4, IR-8, MA-4, PS-4, RA-3, RA-5, SA-9, SC-7, SI-2, SI-4, SI-7, SR-6. These are the controls the SSP records as Partially implemented (P02 section 10.1) that fall inside this assessment.

**Fully Other than satisfied:** SR-6 (a single determination statement).

**Themes:**
1. **Payment pages (e-commerce skimming risk).** The script controls that protect the main web checkout do not reach the express checkout and cart pages, and the tag manager can still inject scripts there (SI-7, AU-6). This is the P08 scenario and the top item before the QSA fieldwork.
2. **Store network and OT.** Refrigeration vendors' always-on remote tools (AC-17, MA-4), OT on the back-office VLAN and stores without NAC (SC-7, SI-4), and default ESL credentials (IA-5) are store network weaknesses the OCPP inherits.
3. **Acquired banner touchpoints.** AB staff accounts and terminations (AC-2, PS-4) and AB incident handling and logging (IR-4, AU-6) are the parts of the AB gap that already touch the OCPP.
4. **Operational discipline.** Emergency switch changes without approval (CM-3), store controller drift and patch delays (CM-6, RA-5, SI-2), inactive POS operator IDs (AC-2(3)), PIN pad inventory accuracy (CM-8), and missing targeted risk analyses (RA-3).
5. **Resilience and disclosure.** No extended processor outage procedure (CP-2), SNAP EBT routing untested in failover (CP-4, CP-10), and a materiality playbook not built for card incidents (IR-8).
6. **Third parties.** 9 TPSPs without a current AOC and 14 without a responsibility matrix (SA-9, SR-6).

**Strengths:** identity and privileged access (IA-2, IA-2(1), AC-6), separation of duties for the switch and payment pages (AC-5), immutable logs and backups (AU-9, AU-11, CP-9), encryption in transit and at rest with no stored card numbers (SC-8, SC-12, SC-28), anti-malware and allow-listing (SI-3, CM-7), customer authentication (IA-8), and workforce training including skimming awareness (AT-2) were all Satisfied.

**New finding during testing:** default vendor credentials on ESL base stations at 3 of 12 sampled stores (IA-05e.). Added to the risk register as R-062 (updated 2026-08-28) and to POAM-006.

## 7. POA&M summary
`poam.csv` holds 24 items: 16 from this assessment and 8 carried from the P03 gap analysis and the P01 risk register (POAM-001, POAM-008, POAM-017, POAM-019, POAM-020, POAM-021, POAM-022, POAM-023), so leadership tracks one list. The carried items cover the AB stores outside the OCPP boundary, privacy and retail media gaps, AI and pricing, and delivery concentration.

| Risk level | Items |
|---|---|
| High | 8 |
| Moderate | 15 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 22 |
| Open | 2 |

Items due before the QSA fieldwork (2026-10-19): POAM-002 and POAM-018 (both 2026-10-16). Management tracks the POA&M monthly at the executive risk committee; Internal Audit validates closure of every High item before it is marked Closed.

## 8. Conclusion
Internal Audit concludes that the OCPP control environment is **effective with exceptions**. Identity, privileged access, logging, backup, encryption, and anti-malware controls operate effectively, and in-store card data is protected by encryption at the PIN pad. The exceptions concentrate in payment page coverage for the newer checkout paths, the store network the OCPP shares with store OT, third-party assurance, and resilience procedures for processor and SNAP EBT outages. Management accepted all findings and committed to the POA&M dates. The CFO used this report for the conditional authorization in P02 section 4.2 on 2026-09-14.
