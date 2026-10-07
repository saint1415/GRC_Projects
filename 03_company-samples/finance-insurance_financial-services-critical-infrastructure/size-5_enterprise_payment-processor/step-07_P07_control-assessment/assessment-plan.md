# Security Assessment Plan and Report: Cris Santos Company | Financial Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor) |
| System assessed | Core Payment Processing Platform (CPPP), CSC-SYS-CPPP-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Financial Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit director and five IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. Internal Audit's co-source firm helped design the Cloud A landing zone guardrails in 2024, so it was **excluded** from testing CCP-03 controls and from the CM-2, CM-5, and SC-7 tests; it supported only the mainframe security manager review (AC-2, IA-5). The QSA firm did not take part, so the ROC stays independent of this work. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also satisfies | Annual assessment for the CPPP authorization (P02 section 4.2); FTC Safeguards Rule testing of safeguards (16 CFR 314.4(d)(1)); part of the Class A independent audit of the cybersecurity program for the payouts subsidiary (23 NYCRR 500.2(c)) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 5, AT 1, AU 4, CA 2, CM 6, CP 4, IA 4, IR 4, MA 1, PS 1, RA 2, SA 2, SC 4, SI 4), 277 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (card data theft, settlement ransomware, MFT exploitation, segmentation, legacy servers, embedded credentials);
- cover PCI DSS, Safeguards Rule, and Part 500 requirements with gaps in P03;
- are common controls the CPPP inherits and that no other assessment covered this year (identity, Cyber Fusion Center monitoring, third-party risk);
- were Partially implemented in the SSP (P02 section 10.1).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-027; R-058; PCI DSS 8.2.5 | Comprehensive | Comprehensive | 2,340 CPPP account events (2026-01-01 to 2026-06-30); 1,412 terminations of workforce with CDE access (1,180 employees, 232 contractors) | 60 account events (random); 60 terminations (stratified: 40 employees, 20 contractors) | 23 / 3 |
| AC-3 | R-044; PCI DSS 7.3.1 | Focused | Focused | About 2,300 workforce CPPP users | 25 users (random); 4 negative access tests | 1 / 0 |
| AC-5 | R-018; PCI DSS 3.7.6; 6.5.4 | Comprehensive | Comprehensive | 61 users able to create or release funding files; 18 key ceremonies | 100% | 2 / 0 |
| AC-6 | R-007; R-044 | Focused | Focused | 4,960 PAM elevation sessions to CPPP hosts | 25 sessions (random) | 1 / 0 |
| AC-17 | R-028; PCI DSS 8.2.7 | Focused | Comprehensive | 7 remote access paths into the CPPP | 100% | 3 / 1 |
| AT-2 | R-041; R-049; PCI DSS 12.6 | Basic | Focused | About 2,300 CPPP workforce members | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AU-2 | R-029; PCI DSS 10.2.1 | Focused | Focused | n/a (configuration) | 7 event types generated in test on a Cloud A host, a midrange server, and the mainframe | 6 / 0 |
| AU-6 | R-029; 23 NYCRR 500.14(b) | Comprehensive | Comprehensive | 26 weeks of Cyber Fusion Center review records; 58 log sources on the CPPP | 5 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-045 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-12 | R-029 | Basic | Focused | n/a (configuration) | 10 CPPP components (random across environments) | 3 / 0 |
| CA-7 | 16 CFR 314.4(d)(1); PCI DSS 12.4.2 | Focused | Basic | 6 monthly metric packages; 4 quarterly PCI DSS reviews | 3 months (random); 100% of quarterly reviews | 11 / 0 |
| CA-8 | R-025; PCI DSS 11.4 | Focused | Focused | 2026 penetration and segmentation tests | 100% | 1 / 0 |
| CM-2 | R-005 | Focused | Focused | 9 baseline documents | 100% | 5 / 0 |
| CM-3 | R-030; PCI DSS 6.5 | Comprehensive | Comprehensive | 236 settlement batch changes and 4,880 Cloud A CDE changes (2026-01-01 to 2026-06-30) | 40 settlement changes (random, including 12 emergency changes); 25 Cloud A changes (random) | 8 / 2 |
| CM-5 | R-007 | Focused | Focused | 4,880 Cloud A CDE changes | 10 changes traced to pipeline identities and PAM sessions | 6 / 0 |
| CM-6 | R-005 | Focused | Comprehensive | 46 midrange settlement servers | 100% (configuration scan) | 4 / 2 |
| CM-7 | PCI DSS 1.2.5 | Focused | Focused | 2,140 CDE firewall rules | 40 rules (random) | 6 / 0 |
| CM-8 | R-033; 23 NYCRR 500.13(a) | Comprehensive | Comprehensive | About 41,000 asset records; 3,960 CPPP components | 100% (data quality analytic); 60 physical components traced (random) | 5 / 1 |
| CP-2 | R-004; R-014 | Comprehensive | Focused | n/a (plan) | Plan v6 examined; 4 interviews | 22 / 2 |
| CP-4 | R-004 | Focused | Focused | 2026 authorization and settlement DR tests | 100% | 5 / 0 |
| CP-9 | R-050 | Focused | Focused | 181 daily backup jobs for CPPP databases | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-004; 23 NYCRR 500.16(a)(2) | Focused | Focused | 2026-04-25 settlement DR test | 100% | 0 / 2 |
| IA-2 | R-026 | Basic | Focused | About 2,300 CPPP workforce accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-006; PCI DSS 8.4.1 | Focused | Comprehensive | 212 privileged CPPP accounts | 100% (analytic) | 1 / 0 |
| IA-2(2) | R-026; 23 NYCRR 500.12 | Focused | Comprehensive | About 340 settlement operator accounts | 100% (analytic) | 0 / 1 |
| IA-5 | R-058; PCI DSS 8.6.2 | Focused | Comprehensive | 4,412 settlement job scripts; PAM vault | 100% (secret scan) | 9 / 1 |
| IR-3 | R-012; PCI DSS 12.10.2 | Focused | Focused | n/a (exercise records) | 2025 and 2026 exercise reports | 0 / 1 |
| IR-4 | R-001; R-002 | Focused | Focused | 388 security incidents involving the CPPP | 25 incidents (random) | 13 / 0 |
| IR-6 | R-013 | Basic | Focused | 388 incidents; contact register for 3 banks | 25 incidents; 100% of bank contacts | 1 / 1 |
| IR-8 | R-012; R-015 | Comprehensive | Focused | n/a (plan) | Plan examined; interviews with the General Counsel, CFO, CISO, and Chief Compliance Officer | 15 / 2 |
| MA-4 | R-028 | Focused | Comprehensive | 9 vendor remote maintenance paths | 100% | 6 / 2 |
| PS-4 | R-027 | Comprehensive | Comprehensive | 1,180 employee terminations | 40 (same sample as AC-2) | 5 / 0 |
| RA-3 | 16 CFR 314.4(b); 23 NYCRR 500.9 | Focused | Basic | n/a | 2026 risk assessment examined | 8 / 0 |
| RA-5 | R-031; PCI DSS 11.3 | Focused | Focused | 8,940 vulnerability findings on CPPP components | 60 findings (random) | 8 / 1 |
| SA-9 | R-011; PCI DSS 12.8.4 | Focused | Comprehensive | 14 external services supporting the CPPP | 100% | 5 / 1 |
| SA-22 | R-005 | Focused | Comprehensive | Unsupported component list | 100% | 0 / 2 |
| SC-7 | R-025; PCI DSS 11.4.6 | Comprehensive | Focused | n/a (architecture) | Reachability test from the DC-1 management subnet to Cloud A CDE subnets | 5 / 1 |
| SC-8 | R-032 | Basic | Focused | All CPPP data flows | 100% (TLS scan; packet capture inside DC-1) | 0 / 1 |
| SC-12 | R-022; PCI DSS 3.6, 3.7 | Focused | Focused | 18 key ceremonies; key inventory | 100% of ceremonies; 25 keys (random) | 2 / 0 |
| SC-28 | R-001; PCI DSS 3.5.1 | Basic | Focused | n/a (configuration) | Token vault and settlement database encryption inspected | 1 / 0 |
| SI-2 | R-031; PCI DSS 6.3.3 | Focused | Focused | 1,286 critical patches released for CPPP components | 60 patches (random) | 9 / 1 |
| SI-3 | R-002 | Focused | Focused | 2,960 CPPP hosts | 100% (coverage analytic); evaluation records for components not at risk | 8 / 0 |
| SI-4 | R-003; R-029 | Focused | Focused | Monitoring coverage map for the CPPP | 100% | 11 / 1 |
| SI-7 | R-001; PCI DSS 11.5.2; 11.6.1 | Comprehensive | Focused | n/a | FIM and payment page tamper-detection examined; 3 test changes | 6 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 account events and terminations, AT-2, CM-8 physical tracing, RA-5, and SI-2.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (settlement changes).
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CM-3 (Cloud A changes), CP-9, IA-2, IR-4, IR-6, and SC-12.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; quarterly, all 4; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 4,412 settlement job scripts for embedded secrets, all 46 midrange servers for baseline settings, all 41,000 asset records for required fields).
- **Stratification:** terminations were stratified so contractors (16% of the population) got 20 of 60 items, because contractor departures follow a different process.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a funding-integrity control (AC-5, CM-3 on the settlement platform) makes the statement Other than satisfied. Three contractor deviations in 20 made AC-2 Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, the mainframe security manager configuration, change tickets and library workflow records, scan and patch reports, segmentation test reports, DR test reports, the vendor register with AOCs and responsibility matrices, the incident response plan and materiality playbook, exercise reports, and disclosure committee materials.
- **Interview:** Senior Vice President, Core Payment Platforms; Director of Settlement Systems; Director of Authorization Platform Engineering; Director of Cryptographic Services; Director of Security Operations; Director of Identity and Access Management; Director of Data Center and Network Engineering; Senior Vice President, Settlement and Treasury Operations; General Counsel; CFO; CISO; Chief Compliance Officer.
- **Test:** negative access tests with test accounts; event generation for logging; secret scanning of job scripts; configuration scans; a reachability test from the DC-1 management subnet; TLS scans and a packet capture inside DC-1; payment page and FIM test changes; a restore observation.

## 4. Rules of engagement
- No testing could affect authorization, clearing, or funding. Tests on the settlement platform ran outside the nightly batch window with the Director of Settlement Systems' approval.
- The reachability test used an audit-owned virtual machine in the DC-1 management subnet, pre-approved by the CISO; it sent connection probes only and carried no card data.
- No PAN or merchant data left company systems. Screenshots and exports in workpapers are masked.
- Critical exposures were reported to the CISO within 24 hours. One was: batch scheduler credentials in plain text in settlement job scripts (reported 2026-08-12; credentials vaulted and rotated 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-12 | Stop-and-notify finding to the CISO (embedded credentials) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Senior Vice President, Core Payment Platforms |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (277 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 247 |
| Other than satisfied | 30 |
| **Total** | **277** |

**Controls with at least one Other than satisfied statement: 21 of 44:** AC-2, AC-17, AU-6, CM-3, CM-6, CM-8, CP-2, CP-10, IA-2(2), IA-5, IR-3, IR-6, IR-8, MA-4, RA-5, SA-9, SA-22, SC-7, SC-8, SI-2, SI-4.

**Fully Other than satisfied:** CP-10, IA-2(2), IR-3, SA-22, SC-8.

**Themes:**
1. **The legacy settlement platform** drives most findings: unsupported servers (SA-22, CM-6), patch timing (SI-2, RA-5), embedded credentials (IA-5), password-only operator sign-in (IA-2(2)), emergency change approvals (CM-3), daily log forwarding (AU-6), vendor remote access (AC-17, MA-4), unencrypted internal transfers (SC-8), and recovery time (CP-10).
2. **Change at the edges of the environment:** the interconnect change created a segmentation path (SC-7); the Bank C program is not yet in the incident tooling (IR-6) or the plan (IR-8).
3. **Readiness of the people who decide:** the incident response capability has not been tested with the executive team and disclosure committee within 12 months (IR-3), and the NYDFS clock is not in the plan (IR-8).
4. **Third parties:** 3 services supporting the CPPP lack current PCI DSS assurance (SA-9); the MFT appliances have no file-level monitoring (SI-4).

**Strengths:** separation of duties for funding files and key ceremonies (AC-5, SC-12), phishing-resistant MFA for all privileged users (IA-2(1)), encryption of stored PAN (SC-28), immutable logs and backups (AU-9, CP-9), penetration testing (CA-8), Cloud A change control (CM-5), and payment page and file integrity monitoring (SI-7) were all Satisfied.

**Finding during testing:** plain-text batch scheduler credentials (IA-05g.), reported to the CISO on 2026-08-12. Added to the risk register as R-058 and to POAM-002.

## 7. POA&M summary
`poam.csv` holds 24 items: 17 from this assessment, 6 carried from the P03 gap analysis (POAM-014 and POAM-019 to POAM-021, POAM-023, POAM-024), and 1 from the P10 AI governance review (POAM-022), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 10 |
| Moderate | 13 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the CPPP control environment is **effective with exceptions**. Enterprise common controls for privileged identity, logging, backup, encryption, and key management operate effectively. The exceptions concentrate in the legacy settlement platform and in readiness for the regulatory notice and disclosure steps. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2, and the results feed the QSA's 2026 ROC fieldwork starting 2026-10-19.
