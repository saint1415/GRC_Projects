# Security Assessment Plan and Report: Cris Santos Company | Construction | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor) |
| System assessed | Project Delivery and Payment Platform (PDPP), CSC-SYS-PDPP-001, per the SSP (P02), including the enterprise common controls it inherits (CCP-01 to CCP-09) |
| Tier / Vertical | Enterprise / Construction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The GRC team and the CMMC Program Office (second line) supported scoping only and did not assess. Co-sourced CMMC specialists were not used for this system because the PDPP is outside the Level 2 scope |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Annual independent assessment for the PDPP authorization decision (P02 section 4.2; POL-01 4.9); evidence for the enterprise FCI scope Level 1 self-assessment due 2027-01-30 (FAR 52.204-21, 32 CFR 170.15); SOX IT general control reliance for ERP access and change (coordinated with the SOX program, not duplicated) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 8, AT 2, AU 4, CA 1, CM 3, CP 4, IA 5, IR 4, PS 1, RA 2, SA 1, SC 3, SI 5, SR 1), 263 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 for payments and the PDPP (R-001, R-002, R-003, R-006, R-009, R-042, R-051);
- cover the FAR 52.204-21 requirements behind the enterprise Level 1 affirmation (P03 G-111 to G-125), because Level 1 allows no POA&M;
- protect payment integrity: the High-baseline supplements documented in P02 (AU-10, AC-2(12)) and the Moderate controls that carry payment integrity (SI-7, SI-7(1), SI-10, AC-5, IA-12);
- are common controls the PDPP inherits that no other assessment covered this year (identity, SOC, cloud landing zone, HR).

The FPCE (CMMC Level 2) was not in this assessment. Its 110 requirements were checked in the P03 internal readiness check and will be assessed by a C3PAO on 2027-01-25.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-031; R-043; 52.204-21(b)(1)(i) (G-111) | Comprehensive | Comprehensive | 2,412 workforce account events in the ERP and payment hub (2026-01-01 to 2026-06-30); about 41,000 external SYS-01 accounts; 1,108 terminations of staff with PDPP access (96 at AQ-1) | 60 workforce account events (random); 25 closed projects (random) for external accounts; external-account analytic (100%) | 22 / 4 |
| AC-2(3) | R-031; R-043 | Focused | Comprehensive | About 3,600 ERP accounts; about 9,200 workforce and about 41,000 external SYS-01 accounts | 100% (data analytic) | 3 / 1 |
| AC-2(12) | R-001; R-044 | Focused | Focused | Behavior analytics rules for payment-role and project manager accounts | All 14 rules examined; 5 test scenarios run | 1 / 1 |
| AC-3 | R-031; R-028 | Focused | Focused | About 9,200 workforce SYS-01 users; ERP role assignments | 25 users (random) traced to project and role assignments | 1 / 0 |
| AC-5 | R-003; R-004; R-052 | Comprehensive | Comprehensive | About 3,600 ERP users; 61 users with vendor master or payment release rights | 100% of users with vendor master or payment release rights (data analytic of conflicting role pairs) | 1 / 1 |
| AC-6 | R-064 | Focused | Focused | 1,512 PAM elevation sessions to ERP and payment hub servers (2026-01-01 to 2026-06-30) | 25 sessions (random) | 1 / 0 |
| AC-6(9) | R-064 | Basic | Focused | Same as AC-6 | Same 25 sessions traced to SIEM records | 1 / 0 |
| AC-17 | R-062; R-042 | Focused | Comprehensive | 4 remote access paths to PDPP administration (zero-trust access, PAM, payment gateway vendor support, ERP vendor support) | 100% | 4 / 0 |
| AT-2 | R-001; R-002 | Basic | Focused | 12,000 workforce (about 900 at AQ-1) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-001; R-003 | Focused | Focused | About 3,400 staff in payment-related roles (project managers, project accountants, AP, Payment Operations, Treasury) | 60 role-holders (random, stratified: 50 enterprise, 10 AQ-1) | 7 / 2 |
| AU-2 | R-034 | Focused | Focused | n/a (configuration) | Event types generated in test for SYS-01, ERP, and payment hub | 5 / 1 |
| AU-6 | R-044; R-001 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 37 log sources on the PDPP payment path | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-015 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-10 | R-003; R-008 | Focused | Focused | About 1,960 vendor master bank changes (2026-01-01 to 2026-06-30) | 60 changes (random) | 0 / 1 |
| CA-7 | 52.204-21; 17 CFR 229.106(b) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-3 | R-052; R-006 | Comprehensive | Comprehensive | 212 integration, payment mapping, and ERP change records (2026-01-01 to 2026-06-30) | 40 changes (random) | 9 / 1 |
| CM-6 | R-062 | Focused | Comprehensive | 24 PDPP components (ERP servers, integration services, gateway cluster) | 100% | 6 / 0 |
| CM-8 | R-032 | Comprehensive | Comprehensive | About 3,200 rugged jobsite tablets that reach SYS-01; 24 PDPP server components | 60 tablets (random, 6 jobsites) traced to device management; 100% of servers | 5 / 1 |
| CP-2 | R-010; R-009 | Comprehensive | Focused | n/a (plan) | Contingency plan v3 examined; 4 interviews | 24 / 0 |
| CP-4 | R-010 | Focused | Focused | 1 annual tier-1 DR test (2026-05-09) | 100% | 4 / 1 |
| CP-9 | R-015; R-009 | Focused | Focused | 181 daily ERP backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-010 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-002 | Basic | Focused | About 3,600 ERP and 9,200 workforce SYS-01 accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-064 | Focused | Comprehensive | 38 privileged PDPP accounts | 100% | 1 / 0 |
| IA-2(2) | R-002; R-001 | Focused | Comprehensive | About 12,000 non-privileged workforce accounts | 100% (conditional access analytic) | 1 / 0 |
| IA-5 | R-062 | Focused | Comprehensive | PDPP authenticators: 38 administrator accounts, 46 service account secrets, 6 appliance management consoles | 100% | 9 / 1 |
| IA-12 | R-003; R-004 | Focused | Focused | About 640 new payees activated (2026-01-01 to 2026-06-30) | 60 payees (random) | 5 / 0 |
| IR-3 | R-051 | Basic | Focused | 1 annual tabletop (2026-02-24) | 100% | 1 / 0 |
| IR-4 | R-003; R-001 | Focused | Focused | 184 security incidents (11 payment fraud attempts, 2 at AQ-1) | 25 incidents (random) plus all 11 payment fraud cases | 11 / 2 |
| IR-6 | R-023; R-053 | Basic | Focused | 184 incidents; 20 staff interviews | 25 incidents; 20 staff (random) | 2 / 0 |
| IR-8 | R-051 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; interviews with the General Counsel, CFO, and CISO | 15 / 2 |
| PS-4 | R-043 | Comprehensive | Comprehensive | 1,108 terminations of staff with PDPP access | 60 (same sample as AC-2, stratified: 50 enterprise, 10 AQ-1) | 4 / 1 |
| RA-3 | 17 CFR 229.106(b); 52.204-21 | Focused | Basic | n/a | 2026 enterprise risk analysis examined | 8 / 0 |
| RA-5 | R-017 | Focused | Focused | 1,286 vulnerability findings on PDPP components (2026-01-01 to 2026-06-30) | 60 findings (random) | 8 / 1 |
| SA-9 | R-036; R-037; R-035 | Focused | Comprehensive | 9 external services supporting the PDPP | 100% | 5 / 1 |
| SC-7 | R-042; R-017 | Comprehensive | Focused | n/a (architecture) | Reachability test from an AQ-1 site network to the integration platform | 5 / 1 |
| SC-8 | R-006 | Basic | Focused | All PDPP external connections, including 3 bank connections | 100% (TLS and SFTP configuration review) | 0 / 1 |
| SC-28 | R-028 | Basic | Focused | n/a (configuration) | Database, backup, and gateway storage encryption inspected | 1 / 0 |
| SI-2 | R-017 | Focused | Focused | 164 patches on PDPP components | 25 patches (random) | 10 / 0 |
| SI-4 | R-001; R-044 | Focused | Focused | BEC use cases and monitored sources | All use cases examined; 5 test scenarios | 11 / 1 |
| SI-7 | R-006 | Comprehensive | Focused | n/a | Payment file integrity controls for 3 banks examined | 5 / 1 |
| SI-7(1) | R-006 | Focused | Focused | Gateway integrity check logs | 30 days of logs | 2 / 1 |
| SI-10 | R-003; FAR 52.232-33(b) | Focused | Focused | Payment files from 2 sources (enterprise ERP and AQ-1 ERP); 1,960 bank changes | 60 bank changes (same sample as AU-10); 100% of file sources | 0 / 1 |
| SR-6 | R-035 | Basic | Basic | 6 tier-1 PDPP suppliers | 100% | 1 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-3, AU-10, SI-10, IA-12, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AC-6(9), CP-9, IA-2, IR-4, IR-6, SI-2, and the closed-project sample for AC-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all external SYS-01 accounts for inactivity, all users with vendor master or release rights for separation of duties, all appliance consoles for default passwords).
- **Stratification:** terminations and payment-role training were stratified so AQ-1 (about 8% of the population) got 10 of 60 items; tablets were sampled at 6 jobsites chosen to cover three regions.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key payment control (AC-5, AU-10, SI-10, IA-12) makes the statement Other than satisfied, because a single failure can send a payment to an attacker.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies, standards, and procedures (P06), the SSP (P02), identity governance and PAM records, ERP role catalog and SoD reports, vendor master change logs and call-back records, payment hub hashing and gateway logs, change tickets, backup and DR test reports, vulnerability scans, the vendor register and SOC report reviews, the incident response plan and materiality procedure (PRC-03.2), disclosure committee minutes of 2026-05-06, and the EV-2026-04 and EV-2026-06 case files.
- **Interview:** Vice President, Project Controls and Systems; Vice President, Treasury; Director of Payment Operations; Director of ERP Applications; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; General Counsel; CFO; CISO; the AQ-1 controller and AP manager; 20 randomly selected payment-role staff.
- **Test:** separation of duties analytics; external-account and inactivity analytics; test alerts for BEC use cases; a network reachability test from an AQ-1 site network to the integration platform; default-credential tests on appliance consoles (with the vendor present); TLS and SFTP configuration review of bank connections; a restore observation; tablet inventory tracing at 6 jobsites.

## 4. Rules of engagement
- No test could initiate, alter, or delay a real payment. Payment hub tests ran in the test environment; production evidence was read-only.
- No testing during the pay app window (the 20th to the 25th) or on payment run days, except read-only data extracts.
- The reachability test used an audit-owned laptop at an AQ-1 office, pre-approved by the CISO and the Vice President, Integration Management Office.
- No FCI, bank account numbers, or Social Security numbers left company systems. Workpaper screenshots are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: the vendor default password on the payment file transfer gateway console (reported 2026-08-12, changed 2026-08-13).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), outside the 2026-07-20 to 2026-07-25 and 2026-08-20 to 2026-08-25 pay app windows for any test touching payment systems |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, CFO, and Vice President, Treasury |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (263 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 233 |
| Other than satisfied | 30 |
| **Total** | **263** |

**Controls with at least one Other than satisfied statement: 24 of 44:** AC-2, AC-2(3), AC-2(12), AC-5, AT-3, AU-2, AU-6, AU-10, CM-3, CM-8, CP-4, CP-10, IA-5, IR-4, IR-8, PS-4, RA-5, SA-9, SC-7, SC-8, SI-4, SI-7, SI-7(1), SI-10.

**Fully Other than satisfied:** AU-10, SC-8, SI-10 (each has a single determination statement).

**Themes:**
1. **AQ-1 is outside the enterprise payment and monitoring controls.** Its payee changes bypass Payment Operations (SI-10, AC-5), its mailboxes and ERP are not monitored (SI-4, AU-6, AC-2(12)), its staff were not trained (AT-3), its leavers are disabled late (PS-4), its network reaches the integration platform (SC-7), and its first payment fraud event never reached the SOC (IR-4). This is the same path that produced the 2026-04 loss.
2. **Payment integrity has three gaps:** call-back evidence is not attributable (AU-10), bank 3 files are not integrity-checked (SC-8, SI-7, SI-7(1)), and emergency changes to payment integrations skipped approval (CM-3).
3. **External users in SYS-01** are not removed after project closeout (AC-2, AC-2(3)), which also affects the FAR 52.204-21 Level 1 affirmation (POAM-024).
4. **Disclosure readiness:** the materiality procedure has no payment fraud scenario or related-occurrence rule (IR-8).

**Strengths:** identity and privileged access (IA-2, IA-2(1), AC-6, AC-6(9)), payee identity proofing for enterprise payees (IA-12), immutable logs and backups (AU-9, CP-9), configuration settings (CM-6), and workforce awareness (AT-2) were all Satisfied.

**Observation (not a finding):** IA-2(2) is Satisfied because every non-privileged account uses MFA. The company's own standard (STD-02.2) requires phishing-resistant authenticators for project management staff by 2027-03-31; that work is tracked as POAM-017 because adversary-in-the-middle phishing is the main BEC entry path (P01 R-002).

**New finding during testing:** the vendor default password on the payment file transfer gateway console (IA-05e.). Added to the risk register as R-062 and to POAM-007.

## 7. POA&M summary
`poam.csv` holds 24 items: 17 from this assessment, 1 carried from P01 and P02 (POAM-017), and 6 carried from the P03 gap analysis (POAM-019 to POAM-024), so leadership tracks one list for the PDPP, the FPCE, and the enterprise FCI scope.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 12 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 5 |

CMMC note: the POA&M here is the company's management plan. It is not a CMMC POA&M. POAM-020 and POAM-024 cover requirements that cannot be on a CMMC POA&M (32 CFR 170.21(a)), so they must be closed before the next self-assessment and affirmation, not carried.

## 8. Conclusion
Internal Audit concludes that the PDPP control environment is **effective with exceptions**. Enterprise common controls for identity, privileged access, logging, backup, and configuration operate effectively, and enterprise payee onboarding works as designed. The exceptions concentrate where AQ-1 connects to the PDPP and in end-to-end payment file integrity for one bank. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2 (2026-09-14).
