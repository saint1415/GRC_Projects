# Security Assessment Plan and Report: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage) with Cris Santos Title and Escrow, LLC |
| System assessed | Transaction Management and Closing Communications System (TMCC), CSC-SYS-TMCC-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Real Estate and Rental and Leasing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee and administratively to the CFO. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also satisfies | Regular testing of key controls under 16 CFR 314.4(d)(1); input to the Qualified Individual's annual report (314.4(i)); annual assessment for the TMCC authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **48 controls (AC 8, AT 2, AU 4, CA 3, CM 4, CP 4, IA 6, IR 3, PS 2, RA 2, SA 2, SC 3, SI 4, SR 1), 294 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (funds diversion through BEC, agent identity, acquired firms, bank channel secrets, disclosure);
- cover Safeguards Rule elements with gaps in P03;
- protect funds integrity (the High-baseline supplements in P02 section 6);
- are common controls the TMCC inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-012; R-016; 314.4(c)(1)(i) | Comprehensive | Comprehensive | 9,100 contractor agent departures and 1,310 employee terminations (2025-07-01 to 2026-06-30); 4,820 TMCC staff account events (2026 H1); 28,600 external Hub accounts | 60 agent departures (stratified: 50 enterprise, 10 AQ-06 to AQ-08); 60 employee terminations (random); 60 account events (random); 28,600 external accounts (100% data analytic) | 22 / 4 |
| AC-2(3) | R-012; R-016 | Focused | Comprehensive | 4,120 workforce TMCC accounts; 28,600 external Hub accounts | 100% (data analytic) | 2 / 2 |
| AC-3 | R-013; 314.4(c)(1)(ii) | Focused | Focused | About 41,000 transactions open in the Hub at fieldwork | 25 cross-transaction access attempts with audit test accounts (random transactions) | 1 / 0 |
| AC-5 | R-002; R-007; Fla. Stat. 626.8473(4) | Comprehensive | Comprehensive | About 190,000 trust account disbursements (2026 H1); 312 users with Disbursement Hub approval roles | 60 disbursements (random); 312 users (100%) | 2 / 0 |
| AC-6 | R-011 | Focused | Focused | 1,460 PAM elevation sessions to TMCC production (2026 H1) | 25 sessions (random) | 1 / 0 |
| AC-6(1) | R-010 | Focused | Comprehensive | 6 holders of the Hub configuration administrator role | 100% | 4 / 0 |
| AC-17 | R-021 | Focused | Comprehensive | 3 remote access types (administrator, vendor support, contractor agent browser access) | 100% | 4 / 0 |
| AC-20 | R-021; R-053 | Focused | Focused | 38,000 contractor agents using their own devices | Session replay test with an audit-owned device; conditional access policy examined | 2 / 1 |
| AT-2 | R-054; 314.4(e)(1) | Basic | Focused | 12,000 employees; 38,000 contractor agents | 60 employee records and 60 agent records (random); 6 months of phishing simulation results | 9 / 1 |
| AT-3 | R-002; R-064 | Focused | Focused | About 1,400 closers, payoff specialists, and escrow accounting staff | 40 staff (random) | 9 / 0 |
| AU-2 | R-007; R-010 | Focused | Focused | n/a (configuration) | 6 event types generated in test (payee change, approval, payment file creation, document download, role change, configuration change) | 6 / 0 |
| AU-6 | R-005; 314.4(c)(8) | Comprehensive | Comprehensive | 26 weeks of SOC review records; 47 log sources on the funds path | 5 weeks (random); 47 log sources (100%) | 2 / 1 |
| AU-9 | R-007 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-10 | R-007; R-002 | Focused | Focused | About 190,000 disbursements and 3,400 payee changes (2026 H1) | 25 approvals (random) | 1 / 0 |
| CA-2 | 314.4(d)(1); Item 106(b) | Focused | Basic | Assessments of the TMCC and the 9 common control providers | This assessment plan and 3 provider assessments | 11 / 0 |
| CA-7 | 314.4(d)(1) | Focused | Basic | 6 monthly continuous monitoring packages (2026 H1) | 3 months (random) | 11 / 0 |
| CA-8 | 314.4(d)(2) | Focused | Focused | 1 annual penetration test (2026-04) | 100% | 1 / 0 |
| CM-3 | R-010; 314.4(c)(7) | Comprehensive | Comprehensive | 212 TMCC changes (2026-01-01 to 2026-06-30), of which 58 were emergency changes | 40 emergency changes (random) and 25 normal changes (random) | 8 / 2 |
| CM-5 | R-010 | Focused | Focused | 1,180 production deployments (2026 H1) | 25 deployments (random) | 6 / 0 |
| CM-6 | R-015 | Focused | Comprehensive | 9 TMCC cloud accounts | 100% (posture data) | 6 / 0 |
| CM-8 | R-015 | Focused | Comprehensive | TMCC components in the 9 accounts | 100% (inventory compared with cloud tags) | 6 / 0 |
| CP-2 | R-033; R-025; 314.4(h) | Comprehensive | Focused | n/a (plan) | Contingency plan v3 examined; 4 interviews | 22 / 2 |
| CP-4 | R-025 | Focused | Focused | 1 annual DR test (2026-05-16) | 100% | 5 / 0 |
| CP-9 | R-031 | Focused | Focused | 181 daily backup jobs (2026 H1) | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-025 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-053 | Basic | Focused | About 52,000 identities | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-011 | Focused | Comprehensive | 64 privileged TMCC accounts | 100% | 1 / 0 |
| IA-2(2) | R-053; R-001; 314.4(c)(5) | Focused | Comprehensive | About 41,300 non-privileged SYS-01 and SSO accounts | 100% (data analytic) | 0 / 1 |
| IA-5 | R-011 | Focused | Comprehensive | 38 TMCC pipelines; secrets vault inventory | 100% | 8 / 2 |
| IA-8 | R-016; 314.4(c)(5) | Focused | Comprehensive | 28,600 external professional accounts; about 212,000 consumer accounts | 100% (data analytic) | 0 / 1 |
| IA-12 | R-003; R-016 | Focused | Focused | About 61,000 seller and payee verifications (2026 H1) | 60 verifications (random); buyer onboarding flow examined | 4 / 1 |
| IR-4 | R-047; 314.4(h)(2) | Focused | Focused | 212 security incidents (2026 H1), 7 at the legacy tenants | 25 incidents (random) plus all 7 legacy-tenant incidents | 11 / 2 |
| IR-6 | R-047; 314.4(j)(2) | Basic | Focused | 31 funds-related cases (2026 H1); 20 closing office staff | 31 cases (100%); 20 staff interviews | 1 / 1 |
| IR-8 | R-044; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | IR plan, BEC runbook, and materiality playbook examined; interviews with the General Counsel, CFO, CISO, and President of Title and Escrow | 15 / 2 |
| PS-4 | R-012 | Comprehensive | Comprehensive | 1,310 employee terminations; 9,100 agent departures | 60 employee terminations; 60 agent departures (same samples as AC-2) | 4 / 1 |
| PS-7 | R-012; R-057 | Focused | Focused | 38,000 contractor agents | 25 agent files (random) | 5 / 0 |
| RA-3 | 314.4(b); Item 106(b) | Focused | Basic | n/a | 2026 risk assessment examined | 8 / 0 |
| RA-5 | R-032; 314.4(d)(2) | Focused | Focused | 1,640 internet-facing critical and high findings (2026 H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-035; 314.4(f)(3) | Focused | Comprehensive | 11 external services supporting the TMCC | 100% | 5 / 1 |
| SA-11 | R-032 | Focused | Focused | 74 TMCC releases (2026 H1) | 25 releases (random) | 9 / 0 |
| SC-7 | R-011; R-015 | Comprehensive | Focused | n/a (architecture) | Inbound scan of the payments account from the internet; egress test to an unlisted destination | 6 / 0 |
| SC-8 | R-013 | Basic | Comprehensive | All TMCC endpoints and bank channels | 100% (TLS scan) | 1 / 0 |
| SC-28 | R-015 | Basic | Focused | n/a (configuration) | Database, document store, and backup encryption inspected | 1 / 0 |
| SI-4 | R-005; R-001 | Focused | Focused | 47 log sources on the funds path | Forwarding-rule test in an enterprise test mailbox and in an AQ-07 test mailbox; use case list examined | 11 / 1 |
| SI-7 | R-002; R-009; Fla. Stat. 626.8473(4) | Comprehensive | Focused | About 190,000 disbursements (2026 H1), about 26,600 verified by manual callback | Verification coverage report (100%); 60 manual callbacks (random) | 4 / 2 |
| SI-8 | R-005 | Focused | Focused | 1 enterprise tenant and 3 legacy tenants | Configuration inspected (100%); look-alike domain test message | 3 / 2 |
| SI-12 | R-014; 314.4(c)(6) | Focused | Focused | n/a (document review) | Retention schedule, Hub deletion job, and legacy file inventory examined | 3 / 1 |
| SR-6 | R-035 | Basic | Comprehensive | 11 TMCC suppliers | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, AC-5, PS-4, AT-2, RA-5, IA-12, and the manual callback test in SI-7.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for the 58 emergency changes in CM-3 and for AT-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, AU-10, CM-5, CP-9, IA-2, IR-4, PS-7, and SA-11.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 28,600 external Hub accounts for inactivity, all 41,300 non-privileged accounts for authentication methods, all 38 pipelines for secrets).
- **Stratification:** agent departures were stratified so the acquired firms AQ-06 to AQ-08 (about 8% of the population) got 10 of 60 items.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key funds control (AC-5, AU-10, SI-7, CM-3 for wire-instruction templates) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, Disbursement Hub role matrix and signed approvals, payee verification and callback records, change tickets and pipeline logs, backup and DR test reports, vulnerability scans, vendor register and SOC report reviews, the incident response plan, materiality playbook, and disclosure committee minutes.
- **Interview:** President of Title and Escrow; Vice President, Escrow Accounting; Executive Vice President, Brokerage Operations; Director of Closing Platform Engineering; Director of Security Operations; Director of Identity and Access Management; General Counsel; CFO; CISO; 20 randomly selected closing office staff.
- **Test:** cross-transaction access tests with audit test accounts; a session token replay test from an audit-owned device; forwarding-rule and look-alike domain tests in enterprise and AQ-07 test mailboxes; an inbound scan of the payments account and an egress test; TLS scans; a pipeline variable scan; a log deletion attempt; a backup restore observation.

## 4. Rules of engagement
- No test could move money or alter a live transaction. Disbursement Hub tests ran in staging with synthetic payees; production evidence was examined read-only.
- Mailbox tests used audit-owned test mailboxes created for the assessment and deleted afterward.
- The token replay test used an audit-owned agent test account with no client data, pre-approved by the CISO.
- No customer information left the company's systems. Screenshots and exports in workpapers are redacted.
- Critical exposures were reported to the CISO within 24 hours. One was: bank API client secrets in pipeline variables (reported 2026-08-06; management scheduled rotation for 2026-09-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and President of Title and Escrow |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (294 rows), and `poam.csv` (21 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 260 |
| Other than satisfied | 34 |
| **Total** | **294** |

**Controls with at least one Other than satisfied statement: 23 of 48:** AC-2, AC-2(3), AC-20, AT-2, AU-6, CM-3, CP-2, CP-10, IA-2(2), IA-5, IA-8, IA-12, IR-4, IR-6, IR-8, PS-4, RA-5, SA-9, SI-4, SI-7, SI-8, SI-12, SR-6.

**Fully Other than satisfied:** IA-2(2), IA-8, SR-6 (each has a single determination statement).

**Themes:**
1. **Contractor agent identity** drives the account management (AC-2, AC-2(3), PS-4), authentication (IA-2(2)), external system (AC-20), and training (AT-2) findings. Agents are most of the user base and the most common entry point for BEC.
2. **Acquired firms:** the three legacy email tenants are neither filtered (SI-8) nor monitored (AU-6, SI-4), and their incidents are handled outside the SOC (IR-4).
3. **Funds integrity:** payee verification coverage and callback discipline (SI-7) and emergency changes to wire-instruction templates (CM-3). Separation of duties (AC-5) and signed approvals (AU-10) inside the Disbursement Hub were Satisfied.
4. **Secrets:** bank API client secrets outside the vault and not rotated (IA-5).
5. **Disclosure readiness:** the materiality playbook has no fraud-loss scenario and no method for a series of related incidents (IR-8).
6. **Recovery:** the Disbursement Hub missed its RTO in the DR test (CP-10) and the plan has no multi-day SYS-01 strategy (CP-2).

**Strengths:** separation of duties and signed approvals for funds (AC-5, AU-10), privileged access (AC-6, AC-6(1), IA-2(1)), network boundary of the payments account (SC-7), encryption (SC-8, SC-28), immutable logs and backups (AU-9, CP-9), secure development and penetration testing (SA-11, CA-8), and role-based training for funds staff (AT-3) were all Satisfied.

**New finding during testing:** bank API client secrets stored as pipeline variables (IA-05g.). Added to the risk register as R-011 and to POAM-010.

## 7. POA&M summary
`poam.csv` holds 21 items: 17 from this assessment and 4 carried from the P03 gap analysis and the P10 AI assessment (POAM-005, POAM-019, POAM-020, POAM-021), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 11 |

| Status | Items |
|---|---|
| In progress | 17 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the TMCC control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, backup, network boundaries, and encryption operate effectively, and the Disbursement Hub's core funds controls (dual approval and signed approvals) work as designed. The exceptions concentrate in contractor agent identity, the unintegrated acquired firms, payee verification coverage, and disclosure readiness for fraud losses. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
