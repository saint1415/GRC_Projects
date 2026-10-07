# Security Assessment Plan and Report: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm) |
| System assessed | Tax Engagement Platform (TEP), CSC-SYS-TEP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Professional, Scientific, and Technical Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit director and four IT auditors under the Chief Audit Executive, who reports functionally to the Audit and Risk Committee of the Partnership Board. None of the assessors designs or operates the controls. The firm's own assurance and SOC examination practices did not perform this work, so client-service independence rules are not engaged and Internal Audit stays separate from the engagement teams. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the Audit and Risk Committee on 2026-09-15 |
| Also satisfies | Regular testing of key controls under 16 CFR 314.4(d)(1); annual assessment for the TEP authorization (P02 section 4.2); the "results of testing" input to the Qualified Individual's report under 314.4(i) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 8, AT 2, AU 4, CA 2, CM 3, CP 4, IA 6, IR 4, MP 1, PS 1, RA 2, SA 1, SC 2, SI 4), 263 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware, business email compromise, portal takeover, insider access, offshore disclosure, acquired firms);
- cover Safeguards Rule elements with gaps in P03 (314.4(c)(1), (c)(5), (c)(8), (h));
- protect confidentiality (the High-baseline supplements in P02 section 6);
- are common controls the TEP inherits and that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-010; R-035; 314.4(c)(1)(i) | Comprehensive | Comprehensive | 2,940 TEP account events; 1,480 seasonal terminations; 12 privileged groups | 60 events (random); 60 terminations (random); all 12 groups | 22 / 4 |
| AC-2(3) | R-034 | Focused | Comprehensive | About 6,300 workforce and about 760,000 client accounts | 100% (data analytic) | 3 / 1 |
| AC-3 | R-007; 314.4(c)(1)(ii) | Comprehensive | Comprehensive | About 516,000 tax engagement repositories | 100% (permission analytic); 60 traced (random) | 0 / 1 |
| AC-5 | R-004; Pub. 1345 | Focused | Comprehensive | 58 tax application roles | 100%; 3 test accounts | 2 / 0 |
| AC-6 | R-007 | Focused | Comprehensive | Same as AC-3; PAM role catalog | 100% (analytic) | 0 / 1 |
| AC-17 | R-003 | Focused | Comprehensive | 3 remote access paths | 100% | 4 / 0 |
| AC-20 | R-001; R-009 | Focused | Focused | n/a (configuration) | Unmanaged-device sign-in tests | 2 / 1 |
| AC-21 | R-008; 301.7216-3 | Comprehensive | Comprehensive | About 21,000 offshore packages | 60 (random) | 0 / 2 |
| AT-2 | R-049; 314.4(e)(1) | Basic | Focused | About 13,500 workforce | 60 records (stratified 40/20); 6 months of phishing results | 9 / 1 |
| AT-3 | R-004 | Basic | Focused | About 1,900 role holders | 25 (random) | 7 / 2 |
| AU-2 | R-009; 314.4(c)(8) | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-009; 314.4(c)(8) | Comprehensive | Focused | 26 weekly reviews | 5 weeks (random) | 1 / 2 |
| AU-9 | R-002 | Basic | Focused | n/a (configuration) | Settings inspected; deletion attempt | 2 / 0 |
| AU-11 | R-016 | Basic | Basic | n/a (configuration) | Settings inspected | 1 / 0 |
| CA-7 | 314.4(d)(1) | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CA-8 | 314.4(d)(2)(i) | Basic | Basic | 1 annual test | 100% | 1 / 0 |
| CM-3 | R-027; 314.4(c)(7) | Comprehensive | Comprehensive | 186 TEP change records | 40 (random) | 9 / 1 |
| CM-6 | R-064 | Focused | Focused | 12 servers; about 140 printer-scanners | All servers; 60 devices (random) | 4 / 2 |
| CM-8 | 314.4(c)(2) | Focused | Focused | About 4,900 TEP cloud resources | 60 traced (random) | 4 / 2 |
| CP-2 | R-005; 314.4(h) | Comprehensive | Focused | n/a (plan) | Plan v3 examined; 2 interviews | 21 / 3 |
| CP-4 | R-031 | Focused | Focused | 1 annual DR test | 100% | 5 / 0 |
| CP-9 | R-002; R-050 | Focused | Focused | 4,344 hourly backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-031 | Focused | Focused | 1 DR test | 100% | 1 / 1 |
| IA-2 | R-024 | Basic | Focused | About 6,300 workforce TEP accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-021 | Focused | Comprehensive | 46 privileged accounts | 100% | 1 / 0 |
| IA-2(2) | R-001; 314.4(c)(5) | Focused | Comprehensive | About 13,800 workforce accounts | 100% (analytic) | 0 / 1 |
| IA-5 | R-064 | Focused | Focused | About 140 printer-scanners; authenticator policies | 60 devices (random) | 8 / 2 |
| IA-8 | R-006; 314.4(c)(5) | Focused | Comprehensive | About 760,000 client accounts | 100% (analytic) | 0 / 1 |
| IA-12 | R-037; Pub. 1345 | Focused | Focused | About 380,000 electronic Forms 8879 | 25 (random) | 5 / 0 |
| IR-3 | R-016; 314.4(h)(7) | Focused | Focused | Exercise records 2025-2026 | 100% | 0 / 1 |
| IR-4 | R-060 | Focused | Focused | 388 incidents (9 at AF-05 and AF-06) | 25 (random) plus all 9 AF incidents | 11 / 2 |
| IR-6 | R-019; Pub. 1345 | Basic | Focused | 388 incidents; 20 staff | 25 incidents; 20 interviews | 2 / 0 |
| IR-8 | R-016; R-018; 314.4(h) | Comprehensive | Focused | n/a (plan) | Plan examined; 3 interviews | 15 / 2 |
| MP-6 | R-029; 52.204-21(b)(1)(vii) | Basic | Focused | 412 disposed devices | 25 (random) | 4 / 0 |
| PS-4 | R-010 | Comprehensive | Comprehensive | 1,480 seasonal terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | 314.4(b)(1) | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-036; 314.4(d)(2)(ii) | Focused | Focused | 1,240 critical and high findings | 60 (random) | 8 / 1 |
| SA-9 | R-008; R-038; 314.4(f)(3) | Comprehensive | Comprehensive | 31 tier-1 and tier-2 TEP vendors; offshore packages | 100% of vendors; 60 packages | 3 / 3 |
| SC-8 | R-059; 314.4(c)(3) | Basic | Comprehensive | 14 external endpoints | 100% (TLS scan) | 0 / 1 |
| SC-28 | R-022; 314.4(c)(3) | Basic | Focused | n/a (configuration) | Settings inspected | 1 / 0 |
| SI-2 | R-036 | Focused | Focused | 318 patches | 25 (random) | 9 / 1 |
| SI-4 | R-009; 314.4(c)(8) | Comprehensive | Focused | n/a (detection) | Token replay purple-team test | 10 / 2 |
| SI-8 | R-001 | Basic | Focused | n/a (configuration) | 10 test messages | 5 / 0 |
| SI-12 | R-011; 314.4(c)(6) | Focused | Focused | Former-client folders | 60 (random) | 3 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AC-21, AT-2, RA-5, CM-6 (printer-scanners), CM-8, and SI-12.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AT-3, CP-9, IA-2, IA-12, IR-4, IR-6, MP-6, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 760,000 client accounts for MFA and inactivity, all 516,000 repositories for permissions).
- **Stratification:** training records were stratified so seasonal staff (about 11% of the workforce) got 20 of 60 items, and incidents at AF-05 and AF-06 were added in full.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key confidentiality control (AC-21, SA-9 consent and masking) or an IRC 7216 permission makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, DMS permission exports, offshore release records and IRC 7216 consents, change tickets, backup and DR test reports, vulnerability scans and the penetration test report, vendor register and SOC report reviews, the incident response plan, runbooks, and notification matrix.
- **Interview:** National Tax Leader; Director of Tax Technology; Director of e-file Operations; Director of Security Operations; Director of Identity and Access Management; Director of Endpoint Engineering; Director of Third-Party Risk Management; Chief Privacy Officer; General Counsel; CISO; 20 randomly selected tax staff.
- **Test:** access tests with test accounts; sign-in tests from an unmanaged device; a purple-team replay of a stolen session token against a test mailbox; default-credential tests on printer-scanners (with the Director of Endpoint Engineering's approval); TLS scans; a restore observation.

## 4. Rules of engagement
- No testing could affect client returns or e-file transmission. Tests ran outside the September 15 and October 15 deadline weeks.
- The token replay test used a test mailbox and a test DMS folder with synthetic data, pre-approved by the CISO; the SOC was not told in advance so detection could be measured.
- Printer-scanner tests changed nothing; auditors only checked whether the default password was accepted.
- No tax return information left the firm's systems. Screenshots and exports in workpapers are redacted, and auditors received the written IRC 7216 reminder at kickoff.
- Critical exposures were reported to the CISO within 24 hours. One was: default administrator passwords on 14 printer-scanners (reported 2026-08-06).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Operating Officer, the CISO, and the National Tax Leader |
| 2026-09-15 | Presented to the Audit and Risk Committee |

Deliverables: this plan and report, `assessment-results.csv` (263 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 220 |
| Other than satisfied | 43 |
| **Total** | **263** |

**Controls with at least one Other than satisfied statement: 27 of 44:** AC-2, AC-2(3), AC-3, AC-6, AC-20, AC-21, AT-2, AT-3, AU-6, CM-3, CM-6, CM-8, CP-2, CP-10, IA-2(2), IA-5, IA-8, IR-3, IR-4, IR-8, PS-4, RA-5, SA-9, SC-8, SI-2, SI-4, SI-12.

**Fully Other than satisfied:** AC-3, AC-6, AC-21, IA-2(2), IA-8, IR-3, SC-8.

**Themes:**
1. **Identity and sessions** drive the confidentiality findings: push MFA and legacy authentication (IA-2(2)), unmanaged-device email (AC-20), password-only client accounts (IA-8, AC-2(3)), and undetected token replay (SI-4, AU-6).
2. **Need-to-know at scale:** open DMS repositories (AC-3, AC-6).
3. **IRC 7216 in the offshore workflow:** consent and masking exceptions (AC-21, SA-9).
4. **Acquired firms and seasonal staff:** AF incident handling (IR-4), late seasonal terminations and training (AC-2, PS-4, AT-2).
5. **Readiness:** the business email compromise runbook has never been exercised (IR-3), the notice matrix is out of date (IR-8), and the transmitter scenario and RTO shortfall are not in the contingency plan (CP-2, CP-10).

**Strengths:** separation of duties for e-file release (AC-5), privileged MFA (IA-2(1)), e-signature identity verification (IA-12), logging and log protection (AU-2, AU-9, AU-11), the penetration test program (CA-8), backups (CP-9), encryption at rest (SC-28), and mail filtering (SI-8) were all Satisfied.

**New finding during testing:** default administrator passwords on 14 of 60 sampled processing hub printer-scanners, whose scan-to-email accounts could send mail that looks internal (IA-05e., IA-05g.). Added to the risk register as R-064 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment (POAM-001 to POAM-019) and 5 carried from the P03 gap analysis (POAM-020 to POAM-024), so leadership tracks one list. Several assessment items also close P03 rows (for example, POAM-008 closes G-048, G-050, and G-051). Each item names its related P01 risks.

| Risk level | Items |
|---|---|
| High | 9 |
| Moderate | 11 |
| Low | 4 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the TEP control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, backup, encryption, and penetration testing operate effectively. The exceptions concentrate in identity for non-privileged staff and clients, need-to-know in the DMS, the offshore IRC 7216 workflow, and the acquired firms. Management accepted all findings and committed to the POA&M dates. The Chief Operating Officer used this report for the conditional authorization in P02 section 4.2, and the CISO included its results in the 2026-09-17 report to the Partnership Board.
