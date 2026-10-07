# Security Assessment Plan and Report: Cris Santos Company | Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer) |
| System assessed | Device Software Factory and Manufacturing Execution System (DSF-MES), CSC-SYS-DSF-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Manufacturing (NAICS 334510) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors, and one auditor with OT experience under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. An outside OT testing firm, engaged by Internal Audit, supervised the plant station tests |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork; MN-1 plant testing 2026-08-11); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also satisfies | Annual assessment for the DSF-MES authorization (P02 section 4.2); evidence for the section 524B(b)(2) processes (P03 G-005) and for the Item 106 description of third-party assessment |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **45 controls (AC 5, AT 2, AU 4, CA 1, CM 8, CP 3, IA 4, IR 3, PS 1, RA 2, SA 4, SC 3, SI 3, SR 2), 270 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 on the code-to-device path (build and signing integrity, the legacy signing workstation, MN-1 stations);
- protect release integrity (the High-baseline and non-baseline integrity supplements in P02 section 6);
- cover the section 524B(b)(2) processes that P03 found partially met;
- are common controls DSF-MES inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-012; R-021; R-055 | Comprehensive | Comprehensive | 1,410 repository, build, signing, and MES account events (2026-01-01 to 2026-06-30); 318 contractor departures with repository access; 400 MN-1 operators on shared logins | 60 account events (random); 60 contractor departures (random); MN-1 shared account register examined in full | 23 / 3 |
| AC-3 | R-002 | Focused | Focused | 2,600 repositories; artifact repository permissions | 25 device firmware repositories (random); release repository permissions in full | 1 / 0 |
| AC-5 | R-010; R-027 | Comprehensive | Comprehensive | 12 signing approvers; 1 legacy signing workstation; 184 releases | 100% of approver assignments; 25 signing events (random) | 1 / 1 |
| AC-6 | R-011 | Focused | Comprehensive | All cloud runner and build service credentials (46) | 100% (credential inventory analytics) | 0 / 1 |
| AC-17 | R-054 | Focused | Comprehensive | 5 remote access paths into DSF-MES | 100% | 3 / 1 |
| AT-2 | R-026 | Basic | Focused | About 3,400 DSF-MES users (engineering, release, plant supervisors) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-058 | Focused | Focused | 1,100 device software engineers; 12 signing approvers; 6 HSM administrators; 40 plant OT engineers | 60 engineers (random); all approvers, HSM administrators, and OT engineers | 8 / 1 |
| AU-2 | R-002; R-027 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-010; R-027 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 31 DSF-MES log sources | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-10 | R-010; R-027 | Focused | Focused | 184 signing events (2026 H1), 9 on the legacy workstation | 25 events (random) plus all 9 legacy events | 0 / 1 |
| AU-12 | R-002 | Basic | Focused | n/a (configuration) | Repository tenant, build orchestrator, signing portal, HSMs, artifact repository, FL-1 and TX-1 MES | 3 / 0 |
| CA-7 | SEC Item 106 (continuous monitoring described) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-020; R-023 | Focused | Comprehensive | 67 servers and nodes (64 build nodes, 3 MES) | 100% | 4 / 1 |
| CM-3 | R-002; 21 CFR 820.10(c) | Comprehensive | Comprehensive | 184 firmware and cloud releases (2026-01-01 to 2026-06-30) | 40 releases (random) | 8 / 2 |
| CM-3(1) | R-002 | Focused | Focused | n/a (configuration) | Promotion gate tested for each of 7 product lines | 5 / 1 |
| CM-5 | R-020 | Focused | Focused | 184 releases; 3 MES servers | 10 changes traced to PAM sessions; MN-1 local administrator list in full | 5 / 1 |
| CM-6 | R-020; R-062 | Focused | Comprehensive | About 420 stations; 67 servers and nodes | 40 settings checked on 30 stations (10 per plant, random) and all servers | 4 / 2 |
| CM-7 | R-020 | Focused | Focused | About 420 stations | 30 stations (10 per plant, random) | 5 / 1 |
| CM-8 | R-013; 524B(b)(3) | Comprehensive | Comprehensive | About 490 DSF-MES components; 7 released SBOMs; 38 third-party firmware modules | 60 physical components traced to the CMDB (20 per plant, random); all SBOMs; all modules | 4 / 2 |
| CM-14 | R-022 | Focused | Comprehensive | About 420 stations | Unsigned test image presented to 30 stations (10 per plant) | 1 / 1 |
| CP-4 | R-014 | Focused | Focused | Annual DSF-MES recovery test program | 2026-05 test report and HSM failover history | 4 / 1 |
| CP-9 | R-023 | Focused | Focused | 181 nightly backup jobs per system (2026 H1) | 25 jobs (random) across systems; restore records | 5 / 1 |
| CP-10 | R-014 | Focused | Focused | 1 recovery test | 100% | 1 / 1 |
| IA-2 | R-021; R-026 | Basic | Focused | About 3,400 DSF-MES users | 25 sign-ins (random); MN-1 shared account register | 1 / 1 |
| IA-2(1) | R-027 | Focused | Comprehensive | 58 privileged accounts (build, HSM, MES) | 100% | 1 / 0 |
| IA-3 | R-022 | Focused | Focused | 330 programming stations at FL-1 and TX-1 | 25 stations (random) | 1 / 0 |
| IA-5 | R-062 | Focused | Comprehensive | 90 MN-1 fixtures and stations; 330 FL-1 and TX-1 stations | 100% default-credential test (after hours, with plant director approval) | 9 / 1 |
| IR-4 | R-002; R-010 | Focused | Focused | 37 security incidents touching DSF-MES (2026 H1) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-015; 21 CFR 806.10 | Basic | Focused | 61 PSIRT cases closed with a field update | 25 cases (random) | 1 / 1 |
| IR-8 | R-017 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with General Counsel, CFO, CISO, VP Product Security, CQRO | 15 / 2 |
| PS-4 | R-055 | Comprehensive | Comprehensive | 1,640 terminations of staff with DSF-MES access (212 at MN-1) | 60 (stratified: 35 enterprise, 25 MN-1) | 4 / 1 |
| RA-5 | R-013 | Focused | Focused | 2,210 vulnerability findings on DSF-MES components | 60 findings (random); scan coverage analytics | 8 / 1 |
| RA-5(11) | 524B(b)(1) | Basic | Focused | n/a (program) | Published CVD policy examined | 1 / 0 |
| SA-9 | R-033 | Focused | Comprehensive | 9 external services supporting DSF-MES | 100% | 5 / 1 |
| SA-11 | R-051; 524B(b)(2) | Focused | Focused | 184 releases | 25 releases (random) | 9 / 0 |
| SA-15 | R-002 | Focused | Focused | n/a (process) | Toolchain standard and 25 builds examined | 8 / 1 |
| SA-22 | R-023 | Focused | Comprehensive | Unsupported component register | 100% | 1 / 1 |
| SC-7 | R-020 | Comprehensive | Focused | n/a (architecture) | Reachability tests from the MN-1 and FL-1 office networks to MES and stations | 4 / 2 |
| SC-8 | R-056 | Basic | Focused | All DSF-MES interfaces | 100% (TLS scan; MN-1 packet capture) | 0 / 1 |
| SC-12 | R-010 | Focused | Comprehensive | Key inventory (27 keys) | 100% | 1 / 1 |
| SI-2 | R-020 | Focused | Focused | 318 patches for DSF-MES components | 25 patches (random) | 9 / 1 |
| SI-4 | R-020; R-027 | Focused | Focused | 3 plants; data center segments | Monitoring coverage examined; test alerts generated | 11 / 1 |
| SI-7 | R-022; R-002 | Comprehensive | Focused | n/a | Integrity verification at stations, repository, and devices examined | 5 / 1 |
| SR-3 | R-013 | Focused | Focused | 38 third-party firmware modules | 100% | 3 / 1 |
| SR-11 | R-033 | Focused | Focused | 2 contract manufacturers | 100% | 4 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic or a small population allowed testing every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, AT-2, AT-3, CM-8, PS-4, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (184 releases).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-5, AU-10, CP-9, IA-2, IA-3, IR-4, IR-6, SA-11, SA-15, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 46 pipeline credentials, all 27 keys, all 420 stations for default credentials).
- **Plant station tests:** 30 stations, 10 per plant, selected at random from each plant's station list, so the acquired plant (MN-1, 21% of stations) got a third of the sample.
- **Stratification:** terminations were stratified so MN-1 (13% of the population) got 25 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key integrity control (AC-5, AU-10, CM-3, CM-14, SC-12, SI-7) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, signing portal and HSM audit logs, key ceremony records, PLM release records and promotion logs, SBOM service reports, backup and DR test reports, vulnerability scans, supplier assessments, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Chief Technology Officer; Director of Build and Release Engineering; Vice President, Manufacturing Systems; MN-1 plant director; VP Product Security; CQRO; Director of Identity and Access Management; Director of Security Operations; General Counsel; CFO; CISO; 20 randomly selected engineers and plant supervisors.
- **Test:** access tests with auditor test accounts; a signing request observed end to end; token scope tests; an unsigned test image presented to 30 programming stations; default-credential tests on MN-1 fixtures and stations; reachability tests from the MN-1 and FL-1 office networks to MES; TLS scans and a packet capture on the MN-1 MES segment; generated audit events.

## 4. Rules of engagement
- No testing could affect production or product quality. Station tests ran during scheduled changeovers with the plant director's approval, used a test image that could not be released, and every tested station was verified afterward by plant quality staff before production resumed.
- No test touched the HSM signing keys. The signing test used a dedicated test key partition.
- No test touched PHI or consumer data; DSF-MES holds none.
- Critical exposures were reported to the CISO and the Vice President, Manufacturing Systems within 24 hours. One was: default vendor passwords on 6 MN-1 programming fixture controllers (found and reported 2026-08-11; changed 2026-08-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); MN-1 plant testing on 2026-08-11 |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and CTO |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (270 rows), and `poam.csv` (26 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 228 |
| Other than satisfied | 42 |
| **Total** | **270** |

**Controls with at least one Other than satisfied statement: 35 of 45:** AC-2, AC-5, AC-6, AC-17, AT-3, AU-6, AU-10, CM-2, CM-3, CM-3(1), CM-5, CM-6, CM-7, CM-8, CM-14, CP-4, CP-9, CP-10, IA-2, IA-5, IR-6, IR-8, PS-4, RA-5, SA-9, SA-15, SA-22, SC-7, SC-8, SC-12, SI-2, SI-4, SI-7, SR-3, SR-11.

**Fully Other than satisfied:** AC-6, AU-10, SC-8 (each has a single determination statement).

**Why so many controls have an exception.** DSF-MES spans three plants, and one of them (MN-1) was acquired in 2024. MN-1 figures in 22 of the 42 Other than satisfied statements, across 20 controls; outside MN-1, most controls with an exception fail on one statement, usually the legacy signing path, the build pipeline, or a supplier. The enterprise build and signing core is sound.

**Themes:**
1. **The acquired plant (MN-1):** flat network, shared logins, vendor remote tools outside PAM, default fixture passwords, unsupported MES, missing baselines, late patches, untested backups, incomplete inventory and scanning, checksum-only stations, unencrypted station traffic, unconnected logs, and late terminations (SC-7, SI-4, IA-2, AC-2, AC-17, IA-5, SA-22, CM-2, CM-5, CM-6, CM-7, SI-2, CP-9, CM-8, RA-5, CM-14, SI-7, SC-8, AU-6, PS-4).
2. **The legacy signing path:** the IV-300 1.x workstation fails separation of duties, non-repudiation, key management, and log review (AC-5, AU-10, SC-12, AU-6).
3. **Build pipeline integrity:** runner token scope (AC-6), missing firmware provenance (SA-15), and releases promoted before approval (CM-3, CM-3(1)).
4. **Suppliers:** SBOM coverage and the CMO-2 assessment and PKI gap (CM-8, SR-3, SA-9, SR-11).
5. **Disclosure and reporting:** no fielded-device path in the materiality playbook (IR-8), and missing 806 decisions (IR-6).

**Strengths:** the HSM signing service and two-person approval for current lines, access enforcement in repositories (AC-3), privileged MFA (IA-2(1)), device certificates at FL-1 and TX-1 stations (IA-3), audit generation (AU-2, AU-12), security testing (SA-11), incident handling (IR-4), and the public CVD program (RA-5(11)) were all Satisfied.

**New finding during testing:** default vendor passwords on 6 MN-1 programming fixture controllers (IA-05e.). Added to the risk register as R-062 and to POAM-008.

## 7. POA&M summary
`poam.csv` holds 26 items: 20 from this assessment and 6 carried from the P03 gap analysis (POAM-021 to POAM-026), so leadership tracks one list.

| Risk level | Items |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 14 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the DSF-MES control environment is **effective with exceptions**. The HSM signing service, identity and privileged access, audit logging, security testing, and incident handling operate effectively for current product lines at FL-1 and TX-1. The exceptions concentrate in the acquired MN-1 plant, the legacy IV-300 signing path, firmware build provenance, and supplier software. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
