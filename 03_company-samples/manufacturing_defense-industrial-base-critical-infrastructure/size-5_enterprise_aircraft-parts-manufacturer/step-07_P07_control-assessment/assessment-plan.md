# Security Assessment Plan and Report: Cris Santos Company | Defense Industrial Base | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer) |
| System assessed | CUI Engineering Enclave (CEE), CSC-SYS-CEE-001, per the SSP (P02), including the enterprise common controls it inherits and the AZ-1 segments added on 2026-05-18 |
| Tier / Vertical | Enterprise / Defense Industrial Base |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit director and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls. The CMMC Program Office (second line) supported scoping only. The C3PAO that certified the company in 2026-03 was not involved |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |
| Also satisfies | SP 800-171 Rev. 2 requirements 3.12.1 and 3.12.3 (annual assessment); input to the 2027-03-20 CMMC affirmation; annual assessment for the CEE authorization (P02 section 4.2) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 6, AT 2, AU 4, CA 3, CM 6, CP 1, IA 4, IR 4, MA 1, MP 2, PE 2, PS 1, RA 2, SA 1, SC 2, SI 2, SR 1), 259 determination statements.** Controls were selected because they:
- address the High and Very High risks in P01 (CUI exfiltration, export attribute failures, AZ-1 and KS-1 integration, supply chain);
- cover SP 800-171 requirements worth 5 points in the CMMC score, and requirements that can never be on a CMMC POA&M (3.1.20, 3.10.3, 3.10.4);
- test the Level 3 requirements most at risk (penetration testing, threat hunting, device authentication, inventory, supplier risk);
- are common controls the CEE inherits and that no other assessment covered this year.

**How this maps to CMMC.** A C3PAO or DIBCAC assesses each SP 800-171 Rev. 2 requirement against the SP 800-171A (June 2018) objectives and each Level 3 requirement against SP 800-172A (32 CFR 170.14(d)), and a requirement is NOT MET if any objective is not satisfied (32 CFR 170.24(b)(2)). This assessment uses SP 800-53A because the SSP documents SP 800-53 controls and its statements are finer grained. The second column links each control to the SP 800-171 or Level 3 requirements whose objectives it covers (author mapping, from the SP 800-53 references NIST lists for each requirement). An "Other than satisfied" statement means the related requirement would be scored NOT MET today. The February 2027 readiness re-check will test all 110 requirements directly against the SP 800-171A objectives before the affirmation.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | SP 800-171 or CMMC requirement | Why selected (risk ID) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|---|
| AC-2 | 3.1.1; 3.5.6; 3.9.2 | R-003; R-013; 5-point requirement | Comprehensive | Comprehensive | 214 CEE account holders separated (2026-01-01 to 2026-06-30); 1,960 account events | 60 separations (random); 60 account events (random) | 23 / 3 |
| AC-2(3) | 3.5.6 | R-013 | Focused | Comprehensive | 3,600 CEE accounts | 100% (data analytic) | 4 / 0 |
| AC-3 | 3.1.2 | R-004 | Focused | Focused | 3,100 PLM users | 25 role assignments (random) | 1 / 0 |
| AC-4 | 3.1.3; AC.L3-3.1.3e | R-004; 22 CFR 120.56 | Comprehensive | Comprehensive | 2,860 PLM project folders | 100% (attribute analytic) | 0 / 1 |
| AC-17 | 3.1.12 to 3.1.15 | R-002 | Focused | Comprehensive | 2 remote access paths | 100% | 4 / 0 |
| AC-20 | 3.1.20; AC.L3-3.1.2e | R-005 | Focused | Focused | 38 external connections in the register | 100%; web category test to 6 public AI and file-sharing sites | 3 / 0 |
| AT-2 | 3.2.1; 3.2.3 | R-002; R-003 | Basic | Focused | 12,000 workforce (3,600 CEE users) | 60 training records (random); 6 months of phishing results | 10 / 0 |
| AT-3 | 3.2.2; AT.L3-3.2.2e | R-006 | Focused | Comprehensive | 412 privileged users | 100% (completion analytic) | 8 / 1 |
| AU-2 | 3.3.1 | R-049 | Focused | Comprehensive | 1,940 log sources in scope | 100% (source inventory compared with asset inventory) | 5 / 1 |
| AU-6 | 3.3.5 | R-002; R-046 | Comprehensive | Focused | 26 weeks of SOC review records | 5 weeks (random) | 3 / 0 |
| AU-9 | 3.3.8; 3.3.9 | R-006 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt by a test administrator | 2 / 0 |
| AU-12 | 3.3.1 | R-049 | Basic | Focused | n/a (configuration) | 12 component types | 2 / 1 |
| CA-5 | 3.12.2 | R-013 | Basic | Basic | n/a (document) | POA&M examined | 2 / 0 |
| CA-7 | 3.12.3 | R-013 | Focused | Basic | 6 monthly metric packages | 3 (random) | 11 / 0 |
| CA-8 | CA.L3-3.12.1e | R-014 | Basic | Basic | n/a | Test reports examined | 0 / 1 |
| CM-2 | 3.4.1 | R-043; R-047 | Focused | Comprehensive | About 2,960 CEE endpoints and servers | 100% (configuration scan) | 3 / 2 |
| CM-3 | 3.4.3; 3.4.4 | R-018 | Comprehensive | Comprehensive | 486 CEE change records (2026-01-01 to 2026-06-30) | 40 (random) | 9 / 1 |
| CM-6 | 3.4.2 | R-043 | Focused | Comprehensive | About 2,960 endpoints and servers | 100% (configuration scan) | 5 / 1 |
| CM-7(5) | 3.4.8 | R-010 | Focused | Focused | About 2,960 endpoints and servers | 25 (random); blocked-execution test | 3 / 0 |
| CM-8 | 3.4.1; CM.L3-3.4.1e | R-014 | Comprehensive | Comprehensive | About 4,200 CEE and MOZ components in the CMDB | 60 physical components traced to the CMDB (random, 7 sites) | 5 / 1 |
| CM-8(3) | CM.L3-3.4.2e; CM.L3-3.4.3e | R-014 | Focused | Focused | 7 sites | Rogue device test at 3 sites (FL-1, FL-3, AZ-1) | 4 / 2 |
| CP-9 | 3.8.9 | R-022 | Focused | Focused | 181 daily PLM backup jobs | 25 (random); 1 restore observed | 6 / 0 |
| IA-2 | 3.5.1; 3.5.2 | R-002 | Basic | Focused | 3,600 CEE accounts | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | 3.5.3 | R-006 | Focused | Comprehensive | 412 privileged accounts | 100% (authentication method report) | 1 / 0 |
| IA-3 | 3.5.2; IA.L3-3.5.1e | R-014 | Focused | Focused | 7 sites | Device authentication test at 3 sites | 0 / 1 |
| IA-5 | 3.5.7 to 3.5.10 | R-006 | Focused | Focused | About 3,700 security keys issued; 610 vaulted service secrets | 25 issuance records (random); 25 secrets (random) | 10 / 0 |
| IR-4 | 3.6.1; IR.L3-3.6.2e | R-052 | Comprehensive | Focused | 212 security incidents (2026-01-01 to 2026-06-30) | 25 (random) | 12 / 1 |
| IR-4(14) | IR.L3-3.6.1e | R-014 | Basic | Basic | n/a | Staffing rosters for 4 weeks | 2 / 0 |
| IR-6 | 3.6.2 | R-052 | Basic | Focused | 212 incidents; 20 staff | 25 incidents (same sample as IR-4); 20 staff interviews | 1 / 1 |
| IR-8 | 3.6.1 | R-050 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, CISO, Vice President, Contracts | 15 / 2 |
| MA-4 | 3.7.5 | R-027 | Focused | Comprehensive | 6 manufacturer remote access paths | 100% | 6 / 2 |
| MP-6 | 3.7.3; 3.8.3 | R-003 | Basic | Focused | 212 media items released (2026-01-01 to 2026-06-30) | 25 (random) | 3 / 1 |
| MP-7 | 3.8.7; 3.8.8 | R-023 | Basic | Focused | About 1,900 AZ-1 build-file transfers (2026-05-18 to 2026-07-31) | 25 (random) | 1 / 1 |
| PE-3 | 3.10.1; 3.10.3 to 3.10.5 | R-008 | Basic | Focused | 1,184 visitor entries at certified sites (2026-04-01 to 2026-06-30) | 60 (stratified: 10 per site); walkthroughs at 3 sites | 11 / 1 |
| PE-8 | 3.10.4 | R-008 | Basic | Focused | 1,184 visitor entries | 60 (same sample as PE-3) | 2 / 1 |
| PS-4 | 3.9.2 | R-003 | Comprehensive | Comprehensive | 214 separations | 60 (same sample as AC-2) | 4 / 1 |
| RA-5 | 3.11.2; 3.11.3 | R-010 | Focused | Focused | 3,412 critical and high findings on CEE assets (2026-01-01 to 2026-06-30) | 60 (random) | 8 / 1 |
| RA-10 | RA.L3-3.11.2e | R-014 | Basic | Basic | n/a | Hunt notes for 2026 examined | 2 / 1 |
| SA-9 | 252.204-7012(b)(2)(ii)(D); 252.204-7021(f) | R-029 | Focused | Comprehensive | 380 CUI suppliers; 14 external system services | 100% status tracker; 14 services reviewed | 5 / 1 |
| SC-7 | 3.13.1; 3.13.5; 3.13.6 | R-047 | Comprehensive | Focused | 7 sites | Reachability test from the corporate network at each site | 5 / 1 |
| SC-13 | 3.13.11 | R-001 | Focused | Comprehensive | 14 CUI paths | 100% | 2 / 0 |
| SI-2 | 3.14.1 | R-010 | Focused | Focused | 3,412 findings | 60 (same sample as RA-5) | 9 / 1 |
| SI-4 | 3.14.6; 3.14.7 | R-001; R-002 | Focused | Focused | n/a | Bulk download test; gateway transfer anomaly test | 12 / 0 |
| SR-6 | RA.L3-3.11.6e | R-029 | Focused | Focused | 380 CUI suppliers | 100% status tracker | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, RA-5, SI-2, CM-8, and the visitor records for PE-3 and PE-8.
- **Key manual controls, populations of 250 to 500:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AT-2, CM-7(5), CP-9, IA-2, IA-5, IR-4, IR-6, MP-6, and MP-7.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 2,860 PLM folders for export attributes, all 3,600 CEE accounts for inactivity, all 14 CUI paths for FIPS validation, all 412 privileged users for training).
- **Stratification:** visitor records were stratified 10 per certified site, so that a lapse at a single site would show.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control tied to a requirement that cannot be on a CMMC POA&M (PE-3, PE-8), to export control (AC-4), or to DoD reporting (IR-4, IR-6) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the CEE and MOZ SSPs (P02), identity governance and PAM records, PLM attribute data, change records, configuration and vulnerability reports, the cryptography register and CRM, visitor and badge records, sanitization records, the incident response plan and materiality playbook, DIBNet logs, supplier status tracker, penetration test reports.
- **Interview:** Vice President, Engineering; PLM Platform Manager; Vice President, Trade Compliance; Vice President, Contracts; Director of Security Operations; Director of Identity and Access Management; Director of OT Engineering; AZ-1 Site Director; General Counsel; CFO; CISO; 20 randomly selected CEE users.
- **Test:** sign-in from an unmanaged device; web category test to public AI and file-sharing sites; deletion attempt on archived logs; bulk download and gateway transfer anomaly tests; rogue device tests at FL-1, FL-3, and AZ-1; reachability tests from the corporate network at every site; allowlisting test; restore observation.

## 4. Rules of engagement
- No testing could disturb production. Network tests at plants ran outside production hours with the Director of OT Engineering present; no test touched machine or printer controllers.
- No CUI left the CEE. Auditors worked from CEE virtual desktops and company-issued laptops, and screenshots with drawings were redacted.
- All auditors are U.S. persons, confirmed by Trade Compliance before access.
- Critical exposures were reported to the CISO within 24 hours. One was: the AZ-1 segment reachable from the corporate network (reported 2026-08-06; interim deny rules are due 2026-10-15 under POAM-005). The PLM export attribute gap was found by Trade Compliance analytics on 2026-08-11 and confirmed by Internal Audit.
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, and Vice President, Engineering |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (259 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 226 |
| Other than satisfied | 33 |
| **Total** | **259** |

**Controls with at least one Other than satisfied statement: 27 of 44:** AC-2, AC-4, AT-3, AU-2, AU-12, CA-8, CM-2, CM-3, CM-6, CM-8, CM-8(3), IA-3, IR-4, IR-6, IR-8, MA-4, MP-6, MP-7, PE-3, PE-8, PS-4, RA-5, RA-10, SA-9, SC-7, SI-2, SR-6.

**Fully Other than satisfied:** AC-4, CA-8, IA-3, SR-6 (each has a single determination statement).

**Themes:**
1. **AZ-1 was added faster than its controls.** Baselines (CM-2, CM-6), logging (AU-2, AU-12), segmentation (SC-7), removable media (MP-7), remote maintenance (MA-4), device authentication (IA-3, CM-8(3)), and inventory (CM-8) findings all trace to the new site.
2. **Operating drift in the certified sites:** contractor separations (AC-2, PS-4), TX-1 visitor escort and records (PE-3, PE-8), emergency change approvals (CM-3), sanitization records (MP-6), vulnerability SLAs (RA-5, SI-2), privileged training (AT-3), and reportability records (IR-4, IR-6).
3. **Export control inside the enclave:** missing ITAR attributes on migrated PLM folders (AC-4).
4. **Level 3 readiness:** penetration testing (CA-8), threat hunting (RA-10), and supplier risk (SA-9, SR-6).
5. **Disclosure readiness:** the materiality playbook does not cover a data-theft scenario or content review (IR-8).

**Strengths:** phishing-resistant MFA and privileged access (IA-2, IA-2(1), IA-5), remote access (AC-17), external connections (AC-20), inactivity disabling (AC-2(3)), log protection and review (AU-6, AU-9), allowlisting (CM-7(5)), backups (CP-9), FIPS-validated cryptography on all 14 CUI paths (SC-13), 24x7 SOC (IR-4(14)), and monitoring (SI-4) were all Satisfied.

**CMMC implications.** The PE-3 and PE-8 findings relate to 3.10.3 and 3.10.4, which can never be on a CMMC POA&M (32 CFR 170.21(a)(2)(iii)), so POAM-003 must be closed and verified before any assessment and before the 2027-03-20 affirmation.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment and 5 carried from the gap analysis (P03), the BIA (P05), and the risk register (P01) (POAM-020 to POAM-024), so leadership tracks one list. The `cmmc_poam_eligible` column shows whether each weakness could sit on a CMMC POA&M under 32 CFR 170.21; the company's plan is to close every Level 2 item before the affirmation regardless.

| Risk level | Items |
|---|---|
| High | 12 |
| Moderate | 11 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 20 |
| Open | 4 |

This POA&M is the SP 800-171 3.12.2 plan of action. It is not a CMMC POA&M, which exists only after a certification assessment and is limited by 32 CFR 170.21.

## 8. Conclusion
Internal Audit concludes that the CEE control environment is **effective with exceptions**. Enterprise common controls for identity, cryptography, logging, backup, and monitoring operate effectively. The exceptions concentrate in the AZ-1 site added after certification and in operating drift at the certified sites. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2, and the February 2027 readiness re-check will confirm closure before the affirmation.
