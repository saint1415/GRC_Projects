# Security Assessment Plan and Report: Cris Santos Company | Public Administration | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator) |
| System assessed | Agency Case Management Cloud (ACMC), CSC-SYS-ACMC-001, per the SSP (P02), including the integration hub and its DC-1 edge, and the enterprise common controls ACMC inherits |
| Tier / Vertical | Enterprise / Public Administration |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and three IT auditors under the Chief Audit Executive, who reports functionally to the audit committee, with a co-sourced firm for network and cryptography testing. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only. This corrects the 2025 assessment, which the GRC team performed itself (POAM-012) |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the board risk committee on 2026-09-10 |
| Also satisfies | Annual assessment for the ACMC authorization (P02 section 4.2; CA-2, CA-7); evidence for agency CJIS audits and IRS safeguard reviews; SOC 2 readiness evidence (P09) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **46 controls (AC 6, AT 2, AU 5, CA 2, CM 5, CP 4, IA 4, IR 3, MP 1, PS 3, RA 2, SA 1, SC 5, SI 2, SR 1), 283 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (ransomware, the AQ-1 peering, FTI exposure to the help desk subcontractor, CJIS screening and cryptography);
- carry CJIS or Pub. 1075 values that agencies audit (AC-7, AU-11, IA-2(1), IR-6, PS-3, SC-13);
- are common controls ACMC inherits that no other assessment covered this year;
- protect tenant isolation and recovery, the core service promises in the SOC 2 report (P09).

Systems outside the ACMC boundary (IES, legacy hosting servers, the AQ-1 platform itself) were rated in the P03 gap analysis, not tested here; the AQ-1 peering and the AQ-1 engineers with integration hub access were tested because they reach ACMC.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-051; R-003; CJISSECPOL AC-2 | Comprehensive | Comprehensive | 1,412 workforce terminations and 96 subcontractor terminations (2026-01-01 to 2026-06-30); 2,860 ACMC account events | 60 workforce terminations (random); 20 subcontractor terminations (random); 60 account events (random) | 23 / 3 |
| AC-3 | R-017; DPPA 2721(a) | Focused | Focused | 132 tenants | Cross-tenant tests from 25 test accounts in 5 tenants | 1 / 0 |
| AC-6 | R-018; CJISSECPOL AC-6 | Focused | Comprehensive | All 412 ACMC support and administrator role assignments | 100% (data analytic) | 0 / 1 |
| AC-7 | R-023; CJISSECPOL AC-7 | Basic | Focused | n/a (configuration) | Lockout tested with 3 test accounts (workforce, local agency, federated) | 2 / 0 |
| AC-17 | R-039; CJISSECPOL AC-17 | Focused | Comprehensive | 4 remote administration paths | 100% | 4 / 0 |
| AC-21 | R-007; Pub. 1075 Exhibit 7 | Focused | Comprehensive | About 52,000 tickets from FTI tenants (2026-H1) | 100% (keyword and image scan) | 1 / 1 |
| AT-2 | R-022; CJISSECPOL AT-2 | Basic | Focused | About 12,000 workforce members (3,400 with CJI access) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | R-057; Pub. 1075 sec. 2.D | Focused | Focused | About 1,900 staff with FTI access | 60 (random) | 8 / 1 |
| AU-2 | R-038; CJISSECPOL AU-2 | Focused | Focused | n/a (configuration) | 6 event types generated in test | 6 / 0 |
| AU-6 | R-018; R-057; Pub. 1075 sec. 4 AU-6 | Comprehensive | Comprehensive | 26 weeks of FTI tenant reviews; 41 ACMC log sources | 13 weeks (random); 100% of log sources | 2 / 1 |
| AU-9 | R-001 | Basic | Focused | n/a (configuration) | Archive settings inspected; deletion attempt tested | 2 / 0 |
| AU-11 | CJISSECPOL AU-11; Pub. 1075 sec. 4 AU-11 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-038 | Basic | Focused | n/a (configuration) | 8 ACMC components | 3 / 0 |
| CA-2 | R-030; 17 CFR 229.106(b)(1)(ii) | Focused | Focused | n/a (process) | 2025 and 2026 assessments examined; interviews | 10 / 1 |
| CA-7 | Contract (SP 800-53 Moderate) | Focused | Basic | 12 monthly monitoring packages | 3 months (random) | 11 / 0 |
| CM-2 | R-045 | Focused | Focused | 14 ACMC image and template baselines | 100% | 5 / 0 |
| CM-3 | R-053; CJISSECPOL CM-3 | Comprehensive | Comprehensive | 412 ACMC changes (2026-01-01 to 2026-06-30), 48 emergency | 40 changes (random, 12 emergency) | 9 / 1 |
| CM-5 | R-053 | Focused | Focused | 412 changes | 10 changes traced to pipeline and PAM records | 6 / 0 |
| CM-6 | R-046 | Focused | Comprehensive | All ACMC accounts | 100% (posture scan) | 6 / 0 |
| CM-8 | Contract (SP 800-53 Moderate) | Focused | Focused | About 2,300 ACMC cloud resources and 14 DC-1 edge devices | 60 resources traced to the CMDB (random) | 6 / 0 |
| CP-2 | R-020; R-031 | Comprehensive | Focused | n/a (plan) | Plan v5 examined; 3 interviews | 24 / 0 |
| CP-4 | R-020 | Focused | Focused | 1 annual failover test | 100% | 5 / 0 |
| CP-9 | R-001 | Focused | Focused | 181 daily backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-020 | Focused | Focused | 1 failover test | 100% | 2 / 0 |
| IA-2 | R-022; CJISSECPOL IA-2 | Basic | Focused | About 4,800 workforce accounts with ACMC access | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-049; CJISSECPOL IA-2(1) | Focused | Comprehensive | 412 privileged ACMC role assignments | 100% (data analytic) | 1 / 0 |
| IA-5 | R-058; CJISSECPOL IA-5 | Focused | Comprehensive | 14 DC-1 edge devices; 212 service credentials | 100% (default credential test; secrets manager report) | 9 / 1 |
| IA-8 | R-023 | Focused | Comprehensive | About 31,000 agency user accounts | 100% (data analytic) | 1 / 0 |
| IR-4 | R-001; CJISSECPOL IR-4 | Focused | Focused | 236 security incidents (2026-H1) | 25 incidents (random) | 13 / 0 |
| IR-6 | R-019; CJISSECPOL IR-6; Pub. 1075 sec. 1.8.4 | Comprehensive | Focused | 41 incidents involving CJI or FTI tenants (2026-H1); 20 staff interviews | 25 incidents (random); 20 staff | 1 / 1 |
| IR-8 | R-010; SEC Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, and CISO | 15 / 2 |
| MP-6 | R-027; Pub. 1075 Exhibit 7 I(5) | Focused | Comprehensive | 9 contract ends (2025-07 to 2026-06); DC-1 media disposal records | 100% | 3 / 1 |
| PS-3 | R-004; CJISSECPOL PS-3 | Comprehensive | Comprehensive | About 3,400 staff with CJI access; 12 AQ-1 engineers with integration hub access | 60 (random); 12 (100%) | 2 / 1 |
| PS-4 | R-051 | Comprehensive | Comprehensive | 1,412 workforce terminations | 60 (same sample as AC-2) | 5 / 0 |
| PS-7 | R-008; R-051; Pub. 1075 Exhibit 7 | Comprehensive | Comprehensive | 41 subcontractors with FTI or CJI access | 100% contracts; 20 terminations (random) | 3 / 2 |
| RA-3 | Contract (SP 800-53 Moderate) | Focused | Basic | n/a | 2026 risk assessment examined | 8 / 0 |
| RA-5 | R-045 | Focused | Focused | 2,214 critical and high findings on ACMC (2026-H1) | 60 findings (random) | 8 / 1 |
| SA-9 | R-007; R-013; Pub. 1075 sec. 3.3.1 | Focused | Comprehensive | 11 external services supporting ACMC | 100% | 4 / 2 |
| SC-7 | R-003; CJISSECPOL SC-7 | Comprehensive | Focused | n/a (architecture) | Reachability test from an AQ-1 host to hub subnets; firewall rule review | 5 / 1 |
| SC-8 | R-006; CJISSECPOL SC-8 | Basic | Comprehensive | All ACMC endpoints and 31 VPN tunnels | 100% (TLS scan; appliance certificate review) | 0 / 1 |
| SC-12 | Pub. 1075 sec. 3.3.1(e) | Focused | Focused | 6 FTI tenant keys | 100% | 2 / 0 |
| SC-13 | R-006; CJISSECPOL SC-13 | Focused | Comprehensive | Cryptographic modules on CJI and FTI paths | 100% | 1 / 1 |
| SC-28 | CJISSECPOL SC-28 | Basic | Focused | n/a (configuration) | Database, storage, and backup encryption inspected | 1 / 0 |
| SI-2 | R-045; R-016 | Focused | Focused | 198 ACMC patch releases | 25 (random) | 10 / 0 |
| SI-4 | R-001; R-002 | Focused | Focused | n/a | Simulated exfiltration and privilege misuse in a test tenant | 12 / 0 |
| SR-6 | R-013; R-052 | Focused | Comprehensive | 11 suppliers supporting ACMC | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-3, PS-4, AT-2, AT-3, CM-8, and RA-5.
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3, stratified so emergency changes (12% of the population) got 12 of 40 items.
- **Smaller populations:** 20 to 25 items, or the full population when under 25. Used for subcontractor terminations (20 of 96), CJI and FTI tenant incidents (25 of 41), backup jobs, sign-ins, and patch releases.
- **Recurring controls:** weekly, 13 occurrences from 26 (the FTI review); monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 412 privileged role assignments, all 31,000 agency accounts for MFA, all 52,000 FTI tenant tickets for FTI content, all 14 edge devices for default credentials).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects CJI or FTI under an agency contract term (PS-3, IR-6, AC-21, SC-13) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, ACMC role catalog and audit logs, change records, backup and DR test reports, scanner reports, vendor and subcontract registers, agency IRS notifications and CJIS certification lists, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, ACMC Platform Operations; ACMC Security Lead; Director of Regulated Data Compliance; Director of Security Operations; Director of Identity and Access Management; Director of Network and Data Center Operations; Director of Third-Party Risk Management; General Counsel; CFO; CISO; 20 randomly selected staff with CJI access.
- **Test:** cross-tenant access tests with test accounts; lockout tests; a default-credential test of every DC-1 edge device (with the network team present, in a maintenance window); a reachability test from an AQ-1 test host to integration hub subnets; TLS scans and appliance certificate review; a full scan of FTI tenant tickets; simulated exfiltration and privilege misuse in a test tenant; an observed restore.

## 4. Rules of engagement
- No test could affect agency service. Edge device tests ran in the approved maintenance window, and VPN tunnels were never taken down.
- Cross-tenant and SOC simulation tests ran only in test tenants with synthetic data.
- No FTI, CJI, or DPPA data left company systems. Workpapers record ticket and record identifiers, never content. The 14 tickets with FTI were reported to the Director of Regulated Data Compliance the same day (2026-08-19) so agencies could be told.
- Critical exposures were reported to the CISO within 24 hours. Two were: default vendor passwords on 2 VPN appliances (reported 2026-08-12) and the AQ-1 peering reaching hub management ports (reported 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the President, State and Local Platforms, the CISO, and the Vice President, ACMC Platform Operations |
| 2026-09-10 | Presented to the audit committee and the board risk committee |

Deliverables: this plan and report, `assessment-results.csv` (283 rows), and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 259 |
| Other than satisfied | 24 |
| **Total** | **283** |

**Controls with at least one Other than satisfied statement: 19 of 46:** AC-2, AC-6, AC-21, AT-3, AU-6, CA-2, CM-3, IA-5, IR-6, IR-8, MP-6, PS-3, PS-7, RA-5, SA-9, SC-7, SC-8, SC-13, SR-6.

**Fully Other than satisfied:** AC-6, SC-8, SR-6 (each has a single determination statement).

**Themes:**
1. **The AQ-1 acquisition reaches ACMC.** The peering lets an AQ-1 host reach integration hub management ports (SC-7), AQ-1 engineers with hub access are managed outside the company directory (AC-2), and 5 of 12 of them were never fingerprinted (PS-3).
2. **The CJIS cryptography deadline.** 7 VPN tunnels on CJI paths still use FIPS 140-2 modules (SC-8, SC-13), and 2 of those appliances had default vendor passwords (IA-5).
3. **Regulated data and third parties.** The help desk subcontractor's overnight tier outside the United States could see FTI screenshots (AC-21, SA-9), 2 subcontractors with FTI access are outside the agencies' IRS notifications (PS-7), and supplier reviews are overdue (SR-6).
4. **Clocks and disclosure.** Agency notices for CJI incidents were late twice (IR-6), and the materiality playbook does not fit a GovTech incident (IR-8).
5. **Smaller process gaps:** standing support access to CJI tenants (AC-6), FTI review evidence (AU-6), emergency change reviews (CM-3), recertification timing (AT-3), deletion certificates (MP-6), and remediation timing (RA-5).

**Strengths:** tenant isolation (AC-3), MFA and phishing-resistant keys (IA-2, IA-2(1), IA-8), lockout (AC-7), logging and the write-once archive (AU-2, AU-9, AU-11, AU-12), ACMC recovery (CP-2, CP-4, CP-9, CP-10), encryption at rest and key co-control (SC-12, SC-28), monitoring (SI-4), and workforce terminations (PS-4) were all Satisfied.

**New finding during testing:** default vendor administrator passwords on 2 legacy VPN appliances (IA-05e.). Added to the risk register as R-058 and to POAM-007; the passwords were changed on 2026-09-04.

## 7. POA&M summary
`poam.csv` holds 25 items: 17 from this assessment and 8 carried from the P03 gap analysis (POAM-003, POAM-005, POAM-008, POAM-015, POAM-021, POAM-022, POAM-023, POAM-024), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 13 |
| Moderate | 10 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 4 |

## 8. Conclusion
Internal Audit concludes that the ACMC control environment is **effective with exceptions**. Tenant isolation, identity, logging, encryption, backup, and monitoring controls operate effectively. The exceptions concentrate where ACMC meets things outside it: the AQ-1 acquisition, the legacy VPN edge, and subcontractors. Management accepted all findings and committed to the POA&M dates. The President, State and Local Platforms used this report for the conditional authorization in P02 section 4.2.
