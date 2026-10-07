# Security Assessment Plan and Report: Cris Santos Company | Management of Companies and Enterprises | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries) |
| System assessed | Shared Corporate Services Platform (SCSP), CSC-SYS-SCSP-001, per the SSP (P02), including the group common controls it inherits and the network paths from acquired businesses and plants into it |
| Tier / Vertical | Enterprise / Management of Companies and Enterprises |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with two specialists from the co-source firm for identity and network testing. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. SOX ITGC testing by the external auditor is separate and was not relied on |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the joint session of the audit committee and the risk committee on 2026-09-17 |
| Also satisfies | Annual assessment for the SCSP authorization (P02 section 4.2); Finance's testing of key controls over customer information handled by GBS (16 CFR 314.4(d)(1)); evidence for the Item 106 statement that third parties assess the program (229.106(b)(1)(ii)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 8, AT 2, AU 5, CA 2, CM 4, CP 4, IA 3, IR 3, PS 1, RA 2, SA 2, SC 3, SI 4, SR 1), 275 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (shared-services ransomware, identity takeover through the service desk, payment fraud, acquisition integration);
- are key SOX IT general controls or Safeguards Rule elements with gaps in P03;
- protect financial and payment integrity (the High-baseline supplements in P02 section 6);
- are common controls the SCSP inherits that no other assessment covered this year (the identity platform's non-SOX controls had not been independently assessed since 2023).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-012; R-018; 16 CFR 314.4(c)(1)(i) | Comprehensive | Comprehensive | 2,214 SCSP account events (2026-01-01 to 2026-06-30); 1,412 terminations of workers with SCSP or SSO access (96 at AQ-01 and AQ-02) | 60 account events (random); 60 terminations (stratified: 50 core entities, 10 AQ) | 22 / 4 |
| AC-2(3) | R-018 | Focused | Comprehensive | About 17,600 accounts (14,500 workforce; 3,100 service) | 100% (data analytic) | 3 / 1 |
| AC-3 | R-009; R-010 | Focused | Focused | About 2,900 SCSP users | 25 users (random) tested for entity and function restrictions | 1 / 0 |
| AC-5 | R-003; R-050; N55-R03 | Comprehensive | Comprehensive | About 2,900 SCSP users | 100% (SoD conflict analytic) | 1 / 1 |
| AC-6 | R-018; R-046 | Comprehensive | Comprehensive | 1,180 privileged accounts | 100% (directory group export) | 0 / 1 |
| AC-6(9) | R-002 | Focused | Focused | 3,960 privileged sessions on SCSP servers | 25 sessions (random) | 1 / 0 |
| AC-7 | R-024 | Basic | Focused | n/a (configuration or document) | Identity provider lockout policy; 2 test accounts | 2 / 0 |
| AC-17 | R-014; R-007 | Focused | Comprehensive | 7 remote access paths into the SCSP and into plant networks that send data to the integration platform | 100% | 3 / 1 |
| AT-2 | R-024; 16 CFR 314.4(e)(1) | Basic | Focused | 12,000 employees | 60 training records (random); 6 months of simulation results | 10 / 0 |
| AT-3 | R-003; R-056 | Focused | Focused | 412 workers in payment, treasury, and administrator roles | 40 (random) | 8 / 1 |
| AU-2 | R-009; R-004 | Focused | Focused | n/a (configuration or document) | Logging matrix; 6 event types generated in test | 6 / 0 |
| AU-6 | R-047; 16 CFR 314.4(c)(8) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 54 log sources in the SCSP and connected systems | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-048 | Basic | Focused | n/a (configuration or document) | Archive retention locks inspected; deletion attempt tested | 2 / 0 |
| AU-10 | R-004; N55-R03 | Focused | Focused | About 41,000 payment approvals | 25 (random), plus the 3 local bank portals | 0 / 1 |
| AU-12 | R-047 | Basic | Focused | n/a (configuration or document) | SCSP components: 6 ERP servers, 2 hub servers, 4 middleware servers, integration service | 2 / 1 |
| CA-2 | N55-R01 (229.106(b)(1)(ii)) | Focused | Basic | n/a (configuration or document) | 2026 assessment plan and reports | 11 / 0 |
| CA-7 | 16 CFR 314.4(d)(1) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-3 | R-009; N55-R03 | Comprehensive | Comprehensive | 196 SCSP changes (2026-01-01 to 2026-06-30), 31 of them emergency | 40 changes (random, all types) | 8 / 2 |
| CM-5 | R-009 | Focused | Focused | 196 SCSP changes | 10 changes traced to PAM sessions or pipeline runs | 6 / 0 |
| CM-6 | R-028 | Focused | Comprehensive | 12 SCSP servers and 8 domain controllers | 100% | 6 / 0 |
| CM-8 | R-010; 16 CFR 314.4(c)(2) | Comprehensive | Comprehensive | About 310 components in or connected to the SCSP | 60 components traced both ways (random) | 5 / 1 |
| CP-2 | R-019; R-061 | Comprehensive | Focused | n/a (configuration or document) | SCSP contingency plan v5; interviews with the Director of ERP Platform, Treasurer, and Director of IAM | 23 / 1 |
| CP-4 | R-019 | Focused | Focused | n/a (configuration or document) | 2026-04-25 DR test report and corrective actions | 5 / 0 |
| CP-9 | R-048 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-019 | Focused | Focused | n/a (configuration or document) | 2026-04-25 DR test results | 1 / 1 |
| IA-2 | R-024 | Basic | Focused | About 2,900 SCSP users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-002; 16 CFR 314.4(c)(5) | Focused | Comprehensive | 1,180 privileged accounts | 100% | 0 / 1 |
| IA-5 | R-002; R-018; 16 CFR 314.4(c)(5) | Comprehensive | Comprehensive | 21,880 password and MFA resets (2026 H1), 61% by the outsourced service desk; 3,100 service accounts | 60 resets (random); 100% of service accounts (analytic); 2 test calls to the service desk approved by the CISO | 8 / 2 |
| IR-4 | R-063; R-065 | Focused | Focused | 212 security incidents (2025-07 to 2026-06) | 25 incidents (random) plus all 9 that started in a subsidiary plant or vendor | 12 / 1 |
| IR-6 | R-034 | Basic | Focused | n/a (configuration or document) | Case records; 20 staff interviews (random, all subsidiaries) | 2 / 0 |
| IR-8 | R-008; N55-R02 | Comprehensive | Focused | n/a (configuration or document) | Incident response plan, materiality playbook, disclosure committee minutes; interviews with the General Counsel, CFO, CISO, and 4 BISOs | 14 / 3 |
| PS-4 | R-012 | Comprehensive | Comprehensive | 1,412 terminations | 60 (same as AC-2) | 4 / 1 |
| RA-3 | 16 CFR 314.4(b); N55-R01 | Focused | Basic | n/a (configuration or document) | 2026 enterprise risk assessment (P01) | 8 / 0 |
| RA-5 | R-028; 16 CFR 314.4(d)(2) | Focused | Focused | 1,640 findings on SCSP components (2026 H1), 96 critical | 60 critical and high findings (random) | 8 / 1 |
| SA-9 | R-013; 16 CFR 314.4(f) | Focused | Comprehensive | 12 external services supporting the SCSP, including the outsourced service desk | 100% | 4 / 2 |
| SA-22 | R-029 | Focused | Comprehensive | SCSP components | 100% | 1 / 1 |
| SC-7 | R-007; R-011 | Comprehensive | Focused | n/a (configuration or document) | Network diagrams; firewall rules; reachability tests from an AQ-02 branch network and the Plant 3 network to the integration platform subnet | 5 / 1 |
| SC-8 | 16 CFR 314.4(c)(3) | Basic | Focused | n/a (configuration or document) | TLS scan of all SCSP interfaces; bank file encryption inspected | 1 / 0 |
| SC-28 | 16 CFR 314.4(c)(3) | Basic | Focused | n/a (configuration or document) | Database, storage, and backup encryption settings | 1 / 0 |
| SI-2 | R-028; R-029 | Focused | Focused | 288 patches on SCSP servers | 25 (random) | 9 / 1 |
| SI-4 | R-047 | Focused | Focused | n/a (configuration or document) | SOC metrics; identity threat detection rules | 12 / 0 |
| SI-7 | R-003; R-004 | Comprehensive | Focused | n/a (configuration or document) | Hub integrity logs; file integrity monitoring; payment files sent through the 3 local bank portals | 5 / 1 |
| SI-10 | R-010 | Focused | Focused | n/a (configuration or document) | 20 malformed journal and bank files in the test environment | 1 / 0 |
| SR-6 | R-027; 16 CFR 314.4(f)(3) | Focused | Comprehensive | 64 tier-1 vendors | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-8, IA-5 (resets), and RA-5.
- **Key manual controls, populations of 50 to 250 or a smaller role population:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3 and AT-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6(9), AU-10, CP-9, IA-2, IR-4, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 17,600 accounts for inactivity, all 1,180 privileged accounts for authenticator type, all SCSP users for SoD conflicts).
- **Stratification:** terminations were stratified so the acquired businesses (7% of the population) got 10 of 60 items; incidents included all 9 that started in a plant or at a vendor.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key payment-integrity or financial-reporting control (AC-5, AU-10, CM-3, SI-7) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, directory group exports, ERP SoD rules and role assignments, change tickets, payment hub integrity logs, backup and DR test reports, vulnerability scans, the vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Global Business Services; Treasurer; Director of ERP Platform; Director of Identity and Access Management; Director of Security Operations; Director of Third-Party Risk Management; Director of Enterprise Integration; General Counsel; CFO; CISO; the four subsidiary BISOs; 20 randomly selected staff.
- **Test:** lockout tests with test accounts; two social-engineering test calls to the outsourced service desk (pre-approved by the CISO and the provider's security lead, using a test administrator account); reachability tests from an AQ-02 branch network and the Plant 3 network to the integration platform subnet; malformed journal and bank files in the test environment; a restore observation; a log deletion attempt on the archive.

## 4. Rules of engagement
- No testing could affect payment release, the financial close, or plant production. Network tests ran outside close windows and plant shift changes, with the Treasurer and the plant manager informed.
- Social-engineering calls targeted only the test administrator account, which had no access to production data; the account was disabled immediately after each call.
- Malformed file tests ran only in the test environment.
- No customer, employee, or plan data left the group's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. Two were: the successful MFA reset test calls (reported 2026-07-29) and management-port reachability from the Plant 3 network (reported 2026-08-06).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the CFO, CISO, CIO, and Vice President, Global Business Services |
| 2026-09-17 | Presented to the joint session of the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (275 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 242 |
| Other than satisfied | 33 |
| **Total** | **275** |

**Controls with at least one Other than satisfied statement: 25 of 44:** AC-2, AC-2(3), AC-5, AC-6, AC-17, AT-3, AU-6, AU-10, AU-12, CM-3, CM-8, CP-2, CP-10, IA-2(1), IA-5, IR-4, IR-8, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-7, SR-6.

**Fully Other than satisfied:** AC-6, AU-10, IA-2(1), SR-6 (each has a single determination statement).

**Themes:**
1. **Identity recovery and privilege** is the most serious weakness: knowledge-based resets at the outsourced service desk (IA-5, SA-9), incomplete phishing-resistant MFA for administrators (IA-2(1)), oversized domain administrator membership (AC-6), and unowned service accounts (AC-2, AC-2(3), IA-5). Together these make the P08 scenario realistic.
2. **Payment integrity at the edges:** Home Services branch SoD conflicts (AC-5), training gaps (AT-3), and local bank portals outside the hub (SI-7, AU-10).
3. **Acquired businesses and plants:** manual AQ terminations (AC-2), CMDB gaps (CM-8), network reachability into the integration platform (SC-7), unmanaged vendor remote access (AC-17), and SIEM blind spots (AU-6, AU-12).
4. **Disclosure readiness across the group:** the incident plan and materiality playbook do not cover subsidiary, plant, or vendor-originated incidents or related incidents across subsidiaries (IR-8, IR-4).

**Strengths:** account provisioning and role-based access in the ERP (AC-3), privileged session recording (AC-6(9)), immutable logs and backups (AU-9, CP-9), encryption (SC-8, SC-28), input validation (SI-10), assessment and continuous monitoring (CA-2, CA-7), awareness training (AT-2), and the risk assessment (RA-3) were all Satisfied.

**Finding reported during testing:** both test calls to the outsourced service desk obtained an MFA reset for a test administrator account after knowledge-based questions only (IA-05a.). The CISO moved all privileged and treasury resets to the internal IAM team on 2026-07-30, ahead of the POA&M date (POAM-001).

## 7. POA&M summary
`poam.csv` holds 24 items: 20 from this assessment (POAM-001 to POAM-020) and 4 carried from the P03 gap analysis and the P10 AI assessment (POAM-021 to POAM-024), so leadership tracks one list. POAM-014 and POAM-016 also cover findings from the Manufacturing OT security review (2026-06), which Internal Audit confirmed during the CM-8 and AC-17 tests.

| Risk level | Items |
|---|---|
| High | 11 |
| Moderate | 12 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 3 |

## 8. Conclusion
Internal Audit concludes that the SCSP control environment is **effective with exceptions**. Core financial application controls, logging, backup, encryption, and monitoring operate effectively. The exceptions concentrate in identity recovery and privileged access, payment controls outside the hub, and controls that depend on integrating the acquired businesses and plants. Management accepted all findings and committed to the POA&M dates. The CFO used this report for the conditional authorization in P02 section 4.2.
