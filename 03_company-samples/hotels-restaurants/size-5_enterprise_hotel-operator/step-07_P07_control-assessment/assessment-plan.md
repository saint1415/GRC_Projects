# Security Assessment Plan and Report: Cris Santos Company | Accommodation and Food Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner: 750 hotels, 110 company-operated) |
| System assessed | Property and Payment Platform (PPP), CSC-SYS-PPP-001, per the SSP (P02), including the enterprise common controls it inherits from CCP-01 to CCP-09 |
| Tier / Vertical | Enterprise / Accommodation and Food Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of them designs or operates the controls. The co-source firm's specialists performed only the network reachability test and the packet captures (SC-7, SC-8); every test of PAM (AC-6, IA-2(1), MA-4) was performed in house, because the co-source firm's consulting arm configured the PAM tool in 2025. The CA-2(1) conclusion was reviewed by the audit committee chair, because Internal Audit cannot judge its own independence alone. The GRC team (second line) supported scoping only. The QSA took no part |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee of the board on 2026-09-10 |
| Also satisfies | Annual assessment for the PPP operating decision (P02 section 4.2); evidence for the PCI DSS 12.4.2 quarterly reviews and the 2026 merchant ROC preparation; SOC 2 readiness evidence for SL-1 (P09) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **42 controls (AC 5, AT 1, AU 5, CA 2, CM 5, CP 4, IA 3, IR 3, MA 1, PS 1, RA 2, SA 2, SC 4, SI 3, SR 1), 256 determination statements.** This is the same control set marked "Yes" in the P06 `policy-control-map.csv` column `assessed_in_P07`. Controls were selected because they:
- address the Very High and High risks in P01 (POS and reservation compromise through vendor remote access, legacy POS, the hub rule, franchisee credentials, resort integration, lock servers);
- cover PCI DSS requirements with gaps in P03 for both the merchant and the service provider assessments;
- are partially implemented in the SSP (P02 section 10.1), so their status needed independent confirmation before the operating decision;
- are common controls the PPP inherits that no other 2026 assessment covered (identity, logging, backup, incident response).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-006; R-020; PCI DSS 8.2 | Comprehensive | Comprehensive | About 36,500 PMS tenant accounts; 2,210 account events on PPP components (2026-01-01 to 2026-06-30); 1,318 terminations of staff with PPP access (96 at the 9 resorts) | 60 account events (random); 60 terminations (stratified: 50 company-operated hotels and offices, 10 resorts) | 22 / 4 |
| AC-2(3) | R-020; PCI DSS 8.2.6 | Focused | Comprehensive | About 36,500 PMS tenant accounts (about 8,900 company-operated hotel staff, 26,400 franchisee staff, 1,200 corporate and support) and 46 vault administrator accounts | 100% (data analytic) | 3 / 1 |
| AC-3 | R-019; R-006 | Focused | Focused | About 36,500 PMS tenant accounts; 6 service accounts allowed to detokenize | 25 PMS users (random) tested for access outside their hotel; detokenization attempted from 3 unapproved service identities | 1 / 0 |
| AC-6 | R-019; PCI DSS 7.2 | Focused | Comprehensive | About 36,500 PMS accounts; 1,640 PAM elevation sessions to the vault (2026-01-01 to 2026-06-30) | 100% of PMS permissions (analytic); 25 PAM sessions (random) | 0 / 1 |
| AC-17 | R-003; R-001; PCI DSS 8.4.2 | Focused | Comprehensive | 14 property-system vendors; 3 remote access paths (zero-trust gateway, PAM vendor gateway, hotel firewall rules) | 100% | 3 / 1 |
| AT-2 | R-064; R-023; PCI DSS 12.6 | Basic | Focused | 12,000 workforce (about 5,600 POS users) | 60 training records (random); 6 months of phishing simulation results | 10 / 0 |
| AU-2 | R-052; PCI DSS 10.2 | Focused | Focused | n/a (configuration) | 6 event types generated in test (vault access, administrator action, failed sign-in, log change, card display, detokenization) | 6 / 0 |
| AU-6 | R-052; R-001; PCI DSS 10.4 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 312 PPP log sources; 26 weeks of local legacy POS report reviews at 41 hotels | 5 weeks of SOC records (random); 100% of log sources; 25 weeks of local reviews (random) | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested with an audit test account | 2 / 0 |
| AU-11 | PCI DSS 10.5.1 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-052 | Basic | Focused | n/a (configuration) | 6 components (vault database, tokenization service, gateway connector, PMS tenant audit, cloud POS, 1 legacy POS server) | 3 / 0 |
| CA-2(1) | R-055; P03 G-102 | Focused | Comprehensive | 6 assurance engagements in 2025-2026 (Internal Audit, co-source firm, two QSA firms, segmentation tester) | 100% | 0 / 1 |
| CA-8 | R-051; P03 G-055; PCI DSS 11.4.6 | Focused | Focused | 3 required tests (2025 annual, 2025 H2 service provider segmentation, 2026 H1 annual and segmentation) | 100% | 0 / 1 |
| CM-2 | R-048; PCI DSS 2.2 | Focused | Comprehensive | 6 component types; 25 components compared to baseline | 100% of types; 25 components (random) | 3 / 2 |
| CM-3 | R-030; PCI DSS 6.5 | Comprehensive | Comprehensive | 212 changes to PPP components (2026-01-01 to 2026-06-30) | 40 changes (random) | 10 / 0 |
| CM-6 | R-009; R-048; PCI DSS 2.2 | Focused | Comprehensive | 1,150 front desk PCs; 110 hotel firewall pairs; 41 legacy POS servers; 31 lock servers | 100% (configuration compliance scans) | 4 / 2 |
| CM-8 | R-036; PCI DSS 9.5.1; 12.5.1 | Comprehensive | Comprehensive | About 1,900 P2PE devices, 640 front desk terminals, 470 legacy POS workstations | 60 physical devices traced to the inventory (random, 8 hotels); terminal lists compared for all 41 legacy hotels | 5 / 1 |
| CM-12 | R-011; PCI DSS 12.5.2 | Focused | Comprehensive | Data discovery results for 1,180 sales, events, and reservation mailboxes (about 61 million emails), file shares, chat transcripts, and the warehouse | 100% of scan results; scan re-performed on 10 mailboxes | 5 / 2 |
| CP-2 | R-004; R-002 | Comprehensive | Focused | n/a (plan) | PPP contingency plan v3 examined; 4 interviews | 22 / 2 |
| CP-4 | R-029 | Focused | Focused | 1 annual DR test (2026-04-25) | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs (2026-01-01 to 2026-06-30) | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-004 | Focused | Focused | 1 DR test; resort transition services terms | 100% | 1 / 1 |
| IA-2 | R-006 | Basic | Focused | About 36,500 PMS accounts; workforce, franchisee, and vendor identities | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-021 | Focused | Comprehensive | 64 privileged accounts (vault, PMS tenant administration, hub firewalls) | 100% | 1 / 0 |
| IA-5 | R-038; PCI DSS 2.2.2; 8.3; 8.6 | Focused | Comprehensive | 41 legacy POS servers; password and authenticator settings | 100% (default-credential test with vendor approval, after outlet hours) | 8 / 2 |
| IR-4 | R-001; R-060 | Focused | Focused | 286 security incidents involving PPP components or hotels (2026-01-01 to 2026-06-30) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-001 | Basic | Focused | 286 incidents; 20 hotel staff | 25 incidents; 20 staff interviews at 4 hotels | 2 / 0 |
| IR-8 | R-015; P03 G-098; G-099 | Comprehensive | Focused | n/a (plan) | Plan v6 and materiality playbook v2 examined; interviews with General Counsel, CFO, CISO, Director of Payments and PCI Compliance, Director of Franchise Technology Compliance | 14 / 3 |
| MA-4 | R-003; PCI DSS 8.4.2 | Focused | Comprehensive | 14 property-system vendors; 1,420 PAM vendor sessions (2026-01-01 to 2026-06-30) | 100% of vendors; 25 PAM sessions (random) | 5 / 3 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,318 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | PCI DSS 12.3.1 | Focused | Basic | n/a | 2026 enterprise risk analysis and targeted risk analyses examined | 8 / 0 |
| RA-5 | R-049; PCI DSS 6.3.3; 11.3.1 | Focused | Focused | 1,860 vulnerability findings on PPP components (2026-01-01 to 2026-06-30) | 60 findings (random) | 8 / 1 |
| SA-9 | R-006; R-018; P03 G-068 | Focused | Comprehensive | 86 card-data and personal-data vendors; franchise AOC tracker for 640 hotels | 100% | 4 / 2 |
| SA-22 | R-009; R-048 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-007; R-059; PCI DSS 1.2; 1.3 | Comprehensive | Focused | 2,340 hub and hotel firewall rules; network configurations at 41 legacy hotels | 100% (rule analytics); reachability test from a franchised hotel segment in the network lab | 5 / 1 |
| SC-8 | R-059; PCI DSS 4.2 | Basic | Focused | All PPP interfaces | 100% (TLS scan); packet capture at 2 legacy hotels using test cards | 0 / 1 |
| SC-12 | R-022 | Focused | Focused | Key ceremonies and rotations (2025-07 to 2026-06) | 100% | 2 / 0 |
| SC-28 | R-022 | Basic | Focused | n/a (configuration) | Vault database and backup encryption inspected | 1 / 0 |
| SI-2 | R-049 | Focused | Focused | 238 patches for PPP components (2026-01-01 to 2026-06-30) | 25 patches (random) | 9 / 1 |
| SI-4 | R-005; R-003 | Focused | Focused | Coverage map; EDR coverage for about 21,000 endpoints | 100% of coverage map; SOC alert test on 2 hotels | 10 / 2 |
| SI-7 | R-008; R-005; PCI DSS 11.5.2; 11.6.1 | Comprehensive | Focused | 4 payment pages; vault, tokenization, and legacy POS components | 100% | 4 / 2 |
| SR-9 | R-036; PCI DSS 9.5.1 | Focused | Focused | 52 weeks of inspection logs at legacy outlets | 25 weeks (random) | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and tested the full population where a data analytic could check every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated through the period. Used for AC-3, AC-6 (PAM sessions), CP-9, IA-2, IR-4, IR-6, MA-4 (PAM sessions), and SI-2.
- **Recurring controls performed at hotels:** weekly controls with a history of exceptions (legacy outlet device inspections, local legacy POS log reviews) used 25 weeks; low-risk weekly controls used 5 weeks (SOC review records); annual controls used the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 36,500 PMS accounts for inactivity and card display permission, all 2,340 firewall rules, all 41 legacy POS servers for default credentials).
- **Stratification:** terminations were stratified so the 9 resorts (7% of the population) got 10 of 60 items, because their directory is not federated.
- **Evaluation:** a deviation in a sample is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key card data control (IA-5, SC-7, AC-17, SR-9) makes the statement Other than satisfied.
- **Shared samples:** for terminations (PS-4, AC-2), legacy POS vulnerabilities (RA-5), device inspections (SR-9), and local log reviews (AU-6), Internal Audit selected the samples and the GRC team used the same selections for the P03 rows G-024, G-032, G-042, and G-046, so the populations were not tested twice.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies, standards, and brand technology standards (P06), the SSP (P02), identity governance and PAM records, PMS permission reports, franchise portal exports, change tickets, baselines and configuration scans, backup and DR test reports, vulnerability scans and penetration test reports, firewall rule sets, data discovery reports, vendor register and AOC reviews, the franchise AOC tracker, the incident response plan and materiality playbook, disclosure committee minutes, the internal audit charter, and QSA selection records.
- **Interview:** Vice President, Hotel Technology; Director of Payments and PCI Compliance; PMS Tenant Administration Manager; Payments Platform Engineering Manager; POS Operations Manager; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; Director of Franchise Technology Compliance; Vice President, Integration Management Office; General Counsel; CFO; CISO; two hotel general managers; 20 randomly selected hotel staff at 4 hotels.
- **Test:** cross-hotel access tests with test accounts in the PMS; detokenization attempts from unapproved identities; default-credential tests on the 41 legacy POS servers; a reachability test from a franchised hotel segment in the network lab; TLS scans and packet captures at 2 legacy hotels; a log deletion attempt; generation of 6 test event types; a restore observation; SOC alert tests at 2 hotels.

## 4. Rules of engagement
- No test could interrupt check-in, payments, or room access. Legacy POS tests ran after outlet closing, with the POS vendor and the POS Operations Manager present, and with the hotel general manager's approval.
- Packet captures used test cards only, during a scheduled test transaction window; captures were destroyed after the finding was confirmed. No real card data entered the workpapers.
- The reachability test ran from the network lab copy of a franchised hotel segment, never from a franchisee's live network.
- No guest or card data left company systems. Screenshots and exports in workpapers are masked.
- Critical exposures were reported to the CISO within 24 hours. One was: vendor default credentials on legacy POS back-office servers at 3 hotels (reported 2026-08-12; changed 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Operating Officer, CISO, and Vice President, Hotel Technology |
| 2026-09-10 | Presented to the audit committee and the risk committee of the board |

Deliverables: this plan and report, `assessment-results.csv` (256 rows), and `poam.csv` (22 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 215 |
| Other than satisfied | 41 |
| **Total** | **256** |

Other than satisfied statements by risk level: High 31, Moderate 10.

**Controls with at least one Other than satisfied statement: 26 of 42:** AC-2, AC-2(3), AC-6, AC-17, AU-6, CA-2(1), CA-8, CM-2, CM-6, CM-8, CM-12, CP-2, CP-10, IA-5, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4, SI-7, SR-9. These are the same 26 controls the SSP marks Partially implemented within this set; the 16 controls the SSP marks Implemented were all Satisfied.

**Fully Other than satisfied:** AC-6, CA-2(1), CA-8, SC-8, SR-9 (each has a single determination statement).

**Themes:**
1. **Legacy property systems** drive most findings: the legacy POS (SC-8, CM-2, SI-4, SI-7, RA-5, SI-2), default and hardcoded credentials (IA-5), lock servers (CM-6, SA-22), and device inspections (SR-9, CM-8).
2. **Vendor remote access** outside PAM at 37 hotels (AC-17, MA-4, SI-4) is the path the P08 scenario follows.
3. **Franchisor duties:** inactive franchisee accounts (AC-2, AC-2(3)), missing franchisee AOCs (SA-9), and the hub rule plus the missed service provider segmentation test (SC-7, CA-8). These are the *FTC v. Wyndham* themes.
4. **Resort integration:** terminations (PS-4, AC-2), logging (AU-6), and recovery (CP-2, CP-10) at the 9 resorts.
5. **Governance:** the materiality playbook (IR-8), card data in email (CM-12), card display permission (AC-6), and written assessor independence (CA-2(1)).

**Strengths:** the card vault and tokenization service (AC-3, SC-12, SC-28), privileged MFA (IA-2(1)), change control (CM-3), immutable logs and backups (AU-9, CP-9), DR testing (CP-4), training (AT-2), and risk analysis (RA-3) were all Satisfied. The QSA reached the same view of the vault in the 2026 service provider ROC.

**New finding during testing:** vendor default credentials on legacy POS back-office servers at 3 hotels (IA-05e.). Added to the risk register as R-038 and to POAM-010.

## 7. POA&M summary
`poam.csv` holds 22 items: 17 from this assessment and 5 carried from the P03 gap analysis and the P01 risk register (POAM-017, POAM-018, POAM-020, POAM-021, POAM-022), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 14 |
| Moderate | 7 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 15 |
| Open | 7 |

Items due before QSA fieldwork for the 2026 merchant ROC (starts 2026-10-19): POAM-010 (2026-09-30), and the first milestones of POAM-004, POAM-005, and POAM-006. The Director of Payments and PCI Compliance tracks them weekly with the QSA engagement plan.

## 8. Conclusion
Internal Audit concludes that the PPP control environment is **effective with exceptions**. The core card data controls (vault, tokenization, keys, privileged access) and the enterprise common controls for identity, logging, backup, and change operate effectively. The exceptions concentrate in legacy property systems, vendor remote access, franchisee oversight, and the resorts still on the seller's systems. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional operating decision in P02 section 4.2 (2026-09-14).
