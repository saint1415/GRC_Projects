# Security Assessment Plan and Report: Cris Santos Company | Commercial Facilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT) |
| System assessed | Building Automation and Access Control System (BAACS), CSC-SYS-BAACS-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Commercial Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`), with OT test practices from NIST SP 800-82 Rev. 3 |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. Because Internal Audit advised on the 2025 OT security standard, the OT standard areas (AC-17, AU-2, AU-12, CM-8, IA-5, MA-4, PL-8, RA-5, SI-4) were assessed by a co-sourced OT assessment firm under Internal Audit supervision. None of the assessors designs or operates the controls. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Also supports | CPG 2.0 goal 2.C, independent validation (C-COMMERCIAL-FACILITIES-R05); annual assessment for the BAACS authorization (P02 section 4.2); a rehearsal of the scope of the 2027 CPPA cybersecurity audit (11 CCR 7123) (C-COMMERCIAL-FACILITIES-R03) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **44 controls (AC 6, AT 2, AU 4, CA 3, CM 5, CP 4, IA 3, IR 3, MA 1, PE 1, PL 1, PS 1, RA 2, SA 2, SC 2, SI 3, SR 1), 317 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (portfolio-wide BAS ransomware, the acquired properties, recovery of Platforms B and C, platform vendor concentration, disclosure);
- cover CPG 2.0 goals with High or Moderate gaps in P03;
- cover the 11 CCR 7123(c) components most likely to be tested in the first CPPA cybersecurity audit (authentication, access, inventory, configuration, vulnerability management, logging, monitoring, segmentation);
- are common controls the BAACS inherits that no other assessment covered this year.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-004; R-016; CPG 3.D | Comprehensive | Comprehensive | 1,212 terminations of workforce members with BAACS access (2026-01-01 to 2026-06-30), 214 at Platform B and C properties; 2,940 BAACS account events | 60 terminations (stratified: 45 enterprise, 15 Platform B and C); 60 account events (random) | 23 / 3 |
| AC-2(3) | R-016; CPG 3.D | Focused | Comprehensive | About 212,000 tenant credentials and 3,600 workforce BAACS accounts | 100% (data analytic) | 3 / 1 |
| AC-3 | R-010 | Focused | Focused | About 3,600 workforce BAACS users | 25 users (random) | 1 / 0 |
| AC-5 | R-062 | Focused | Focused | About 1,900 credential issuance requests per business day | 40 issuance records (random) | 2 / 0 |
| AC-6 | R-045; R-010 | Focused | Comprehensive | 61 full administrators on the access control platform | 100% | 0 / 1 |
| AC-17 | R-003; CPG 1.E; 3.F | Comprehensive | Comprehensive | 9 integrators; 3 remote access paths (OT gateway, PAM, Integrator C tool) | 100% | 3 / 1 |
| AT-2 | R-041; R-062 | Basic | Focused | 12,000 workforce members | 60 training records (random); phishing results for 6 months | 10 / 0 |
| AT-3 | R-057; CPG 3.J | Focused | Focused | About 6,900 workforce members in OT roles (engineers, Building Technology Directors, RSOC staff) | 60 training records (random) | 8 / 1 |
| AU-2 | R-008; CPG 3.Q | Focused | Comprehensive | 41 OT log source types defined in STD-01.4 | 100% | 5 / 1 |
| AU-6 | R-008; R-001 | Comprehensive | Comprehensive | 26 weeks of Cyber Defense Center review records; 41 OT log source types | 5 weeks (random); 100% of source types | 2 / 1 |
| AU-9 | R-050 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt tested | 2 / 0 |
| AU-12 | R-008 | Basic | Focused | About 92 BAACS servers (Platform A cluster nodes, 57 Platform B, 19 Platform C) | 11 servers (4 Platform A cluster nodes, 4 Platform B, 3 Platform C) | 2 / 1 |
| CA-2 | CPG 2.C; 11 CCR 7122 | Focused | Basic | n/a (assessment process) | 2026 plan and report examined | 11 / 0 |
| CA-3 | R-026; R-039 | Focused | Comprehensive | 7 external information exchanges of the BAACS | 100% | 6 / 2 |
| CA-7 | CPG 1.B | Focused | Basic | 6 monthly OT metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-006 | Focused | Comprehensive | 9 BAACS host types | 100% | 4 / 1 |
| CM-3 | R-009; CPG 3.N | Comprehensive | Comprehensive | 212 Platform B program changes (2026-01-01 to 2026-06-30) | 40 (random) | 8 / 2 |
| CM-6 | R-006 | Focused | Comprehensive | About 300 OT Windows hosts | 60 (random, across Platforms A, B, and C) | 5 / 1 |
| CM-7 | R-044 | Focused | Focused | About 900 OT conduit rules | 20 rule sets (random) | 6 / 0 |
| CM-8 | R-007; CPG 2.A | Comprehensive | Comprehensive | About 85,300 field controllers plus about 7,500 door controllers and NVRs | 60 devices traced from the field to the inventory (6 properties) | 5 / 1 |
| CP-2 | R-012; CPG 6.A | Comprehensive | Focused | n/a (plan); 140 properties for degraded-mode procedures | Plan v3 examined; procedure inventory 100%; 5 interviews | 22 / 2 |
| CP-4 | R-011 | Focused | Focused | 1 Platform A failover test; 6 sampled Platform B restore tests; Platform C | 100% | 4 / 1 |
| CP-9 | R-011; CPG 3.O | Focused | Focused | About 2,400 backup jobs (2026-01 to 2026-06) | 25 jobs (random); 1 restore observed | 5 / 1 |
| CP-10 | R-011 | Focused | Focused | 1 observed Platform B restore | 100% | 1 / 1 |
| IA-2 | R-041 | Basic | Focused | About 3,600 workforce BAACS users | 25 sign-ins (random) | 2 / 0 |
| IA-2(1) | R-041 | Focused | Comprehensive | 140 privileged BAACS accounts | 100% | 1 / 0 |
| IA-5 | R-014; CPG 3.A | Focused | Comprehensive | About 7,500 NVRs and door controllers plus BACnet routers; shared site accounts at 19 Platform C properties | 60 devices (random, tested with the integrator present); 19 shared accounts | 8 / 2 |
| IR-4 | R-065; CPG 4.B | Focused | Focused | 214 OT-flagged cases (2026-01 to 2026-06); 61 OT events logged by acquired-property staff | 25 cases (random) plus 25 acquired-property events (random) | 11 / 2 |
| IR-6 | R-055 | Basic | Focused | 214 cases; 20 staff interviews | 25 cases; 20 staff | 2 / 0 |
| IR-8 | R-017; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with the General Counsel, CFO, and CISO | 15 / 2 |
| MA-4 | R-003; CPG 1.E | Comprehensive | Comprehensive | About 1,840 gateway maintenance sessions; 312 Integrator C tool sessions | 25 gateway sessions (random); 100% of Integrator C sessions | 5 / 3 |
| PE-3 | R-063 | Basic | Focused | About 420 OT closets and engineering rooms | 25 OT closets at 8 retail centers (random) | 11 / 1 |
| PL-8 | R-003; R-043 | Focused | Focused | n/a (architecture); 24 property walkthroughs | Architecture document; walkthroughs | 12 / 1 |
| PS-4 | R-004 | Comprehensive | Comprehensive | 1,212 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | CPG 1.B | Focused | Basic | n/a | 2026 risk assessment examined | 8 / 0 |
| RA-5 | R-056; CPG 2.B | Focused | Focused | About 300 OT Windows hosts; about 7,500 NVRs and door controllers | 60 Windows findings (random); 60 devices (random) | 7 / 2 |
| SA-9 | R-005; R-037 | Focused | Comprehensive | 48 tier-1 vendors; 9 integrators | 100% | 4 / 2 |
| SA-22 | R-006 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-003; CPG 3.I | Comprehensive | Focused | n/a (architecture) | Reachability test from a corporate VLAN at an acquired property; conduit review at 6 properties | 4 / 2 |
| SC-8 | R-048 | Basic | Focused | All BAACS interfaces | 100% (TLS scan; BACnet capture inside a zone) | 1 / 0 |
| SI-2 | R-056 | Focused | Focused | About 410 patches and firmware updates (2026-01 to 2026-06) | 25 (random) | 9 / 1 |
| SI-3 | R-006; CPG 4.A | Focused | Comprehensive | About 300 OT Windows hosts | 100% (EDR coverage report) | 7 / 1 |
| SI-4 | R-008; CPG 4.B | Focused | Focused | 140 properties | Sensor coverage 100%; rogue device test at 2 properties | 10 / 2 |
| SR-6 | R-037; CPG 1.E | Focused | Comprehensive | 48 tier-1 vendors | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2 and PS-4 (terminations), AT-2, AT-3, CM-6, CM-8 (field trace), IA-5 (device login tests), and RA-5 (device firmware).
- **Key manual controls, populations of 50 to 250:** 40 items, random selection, from Internal Audit's methodology table for smaller populations. Used for CM-3 (Platform B program changes) and AC-5.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, CP-9, IA-2, IR-4, IR-6, MA-4 (gateway sessions), PE-3, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Full-population tests:** for example, all 212,000 tenant credentials for inactivity, all 61 full administrators, all 9 integrators and remote paths, all 312 Integrator C sessions, and all 48 tier-1 vendors.
- **Stratification:** terminations were stratified so the Platform B and C properties (18% of the population) got 15 of 60 items, and OT events at the acquired properties were sampled separately (25 items) because their handling process differs.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a key occupant-safety control (CM-3, IA-5, MA-4) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, local OT account inventories, gateway session records, Integrator C tool console records, change tickets and integrator service reports, backup and restore test reports, vulnerability and firmware inventories, vendor register and SOC report reviews, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Executive Vice President, Property Operations; Senior Vice President, Engineering; 3 Building Technology Directors; 8 chief engineers; Vice President, Corporate Security; RSOC supervisors; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Network Engineering; Director of Third-Party Risk Management; General Counsel; CFO; CISO.
- **Test:** login tests on 60 OT devices (with the integrator present, outside business hours); a reachability test from a corporate VLAN at an acquired property; a rogue device test at two properties (one with a passive sensor, one without); a deletion attempt on the log archive; a restore observation of a Platform B site server; a TLS scan and a BACnet capture inside an OT zone; walkthroughs of OT closets at 8 retail centers.

## 4. Rules of engagement
- No testing could affect building operations or occupant safety. Device login tests and the restore observation ran outside business hours with the chief engineer present and the property in local hand control where needed.
- No test touched life-safety systems (SYS-13) or their relay points.
- Login tests on OT devices used read-only checks of the login prompt and stopped at successful authentication; no settings were changed.
- The rogue device test used an audit-owned laptop with no company data, pre-approved by the CISO and the Vice President, Corporate Security.
- Critical exposures were reported to the CISO within 24 hours. Two were: default passwords on 7 OT devices (reported 2026-08-06) and the reachability from a corporate VLAN to a Platform C server at an acquired property (reported 2026-08-13; interim access lists were applied to that property on 2026-08-15).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test), including walkthroughs at 8 properties |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, the CISO, and the Executive Vice President, Property Operations |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (317 rows), and `poam.csv` (25 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 271 |
| Other than satisfied | 46 |
| **Total** | **317** |

**Controls with at least one Other than satisfied statement: 32 of 44:** AC-2, AC-2(3), AC-6, AC-17, AT-3, AU-2, AU-6, AU-12, CA-3, CM-2, CM-3, CM-6, CM-8, CP-2, CP-4, CP-9, CP-10, IA-5, IR-4, IR-8, MA-4, PE-3, PL-8, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-3, SI-4, SR-6.

**Fully Other than satisfied:** AC-6, SR-6 (each has a single determination statement).

**Themes:**
1. **The acquired properties** drive the remote access (AC-17, MA-4), network (SC-7, PL-8), unsupported component (SA-22, CM-2, CM-6, SI-3), recovery (CP-4, CP-9), and incident handling (IR-4) findings.
2. **OT visibility at scale:** logging (AU-2, AU-6, AU-12), monitoring (SI-4), inventory (CM-8), and firmware currency (RA-5, SI-2) are in place at Platform A and the enterprise PACS but not across Platform B and the acquired properties.
3. **Identity at the edges:** local OT accounts outside identity governance (AC-2, PS-4), stale tenant credentials (AC-2(3)), excess platform administrators (AC-6), and default device passwords (IA-5).
4. **Third parties and disclosure:** vendor commitments and reassessments (SA-9, SR-6, CA-3), and a materiality process not yet exercised for a building outage (IR-8).

**Strengths:** privileged authentication (IA-2(1)), access enforcement and separation of duties (AC-3, AC-5), the log archive (AU-9), security awareness (AT-2), the assessment and monitoring program (CA-2, CA-7), conduit rules at integrated properties (CM-7), transmission protection (SC-8), incident reporting (IR-6), and the risk assessment (RA-3) were all Satisfied.

**New findings during testing:** default passwords on 7 of 60 sampled OT devices (IA-05e.), added to the risk register as R-014 and to POAM-009; and the reachability from a corporate VLAN to a Platform C server (SC-07a.[04]), which raised the likelihood in R-003.

## 7. POA&M summary
`poam.csv` holds 25 items: 18 from this assessment (POAM-001 to POAM-018) and 7 carried from the P03 gap analysis (POAM-019 to POAM-025), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 7 |
| Moderate | 16 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 6 |

## 8. Conclusion
Internal Audit concludes that the BAACS control environment is **effective with exceptions**. Enterprise common controls for identity, logging infrastructure, backup, and monitoring operate effectively at Platform A and the enterprise PACS. The exceptions concentrate in the 19 acquired properties, in OT visibility and recovery outside Platform A, and in third-party commitments. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
