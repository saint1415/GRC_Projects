# Security Assessment Plan and Report: Cris Santos Company | Information Technology | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) |
| System assessed | Hosting Control Plane and Customer Portal, Government Region (HCP-G), CSC-SYS-HCPG-001, per the SSP (P02), including the enterprise common controls it inherits |
| Purpose | Class D readiness assessment for the SL-2 upgrade, and the annual internal assessment of HCP-G. It does not replace the FedRAMP independent assessment by a FedRAMP Recognized assessment service (FRC-APP-FIA; IVV-CSO-FIA) |
| Tier / Vertical | Enterprise / Information Technology |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`), assessed against Class D parameter values where Class D sets them |
| Assessor(s) and independence | Internal Audit (third line): an IT audit director, two IT audit managers, and four IT auditors under the Chief Audit Executive, who reports functionally to the audit committee. Two auditors hold U.S.-person status for G1 fieldwork. None of the assessors designs or operates the controls, and none worked in G1 engineering in the last 2 years. The GRC team and the FedRAMP compliance group (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk and technology committee on 2026-09-10 |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **48 controls (AC 5, AT 1, AU 5, CA 2, CM 6, CP 3, IA 2, IR 3, MA 1, MP 1, PE 1, PL 1, PS 1, RA 2, SA 2, SC 5, SI 4, SR 3), 306 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (provider tooling compromise, tenant isolation, G1 recovery, Class D certification);
- carry Class D additions or FedRAMP rule gaps from P03;
- are common controls HCP-G inherits that no other assessment covered this year;
- were not tested in the 2026-03 FedRAMP independent assessment, or were tested there with findings.

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-008; R-022; FRC-CSF-BSL AC-2 | Comprehensive | Comprehensive | 2,940 G1 account events (2026-01-01 to 2026-06-30); 412 terminations of staff and contractors with G1 roles | 60 account events (random); 60 terminations (stratified: 45 employees, 15 contractors); 100% of G1 privileged grants (data analytic) | 24 / 2 |
| AC-3 | R-004 | Focused | Focused | 1,186 operator access requests to tenant resources | 25 requests (random) | 1 / 0 |
| AC-5 | R-001; FRC-CSF-BSL AC-5 | Comprehensive | Comprehensive | 214 G1 channel releases (2026-01-01 to 2026-06-30): 196 host, 18 guest-agent | 100% (data analytic) | 1 / 1 |
| AC-6 | R-008 | Focused | Focused | 8,420 PAM elevation sessions to G1 | 25 sessions (random) | 1 / 0 |
| AC-17 | R-007 | Focused | Comprehensive | 3 remote access paths into G1 management | 100% | 4 / 0 |
| AU-2 | R-021 | Focused | Focused | n/a (configuration) | 6 event types generated in test on control plane, host, and KMS components | 6 / 0 |
| AU-6 | R-019; P10 AI-001 | Comprehensive | Comprehensive | About 46,000 G1 alerts auto-closed by AI triage (2026-01-01 to 2026-06-30); 26 weeks of hunt records | 60 auto-closed alerts (random); 5 weeks of hunt records (random) | 2 / 1 |
| AU-9 | R-021 | Basic | Focused | n/a (configuration) | Write-once settings inspected; deletion attempt by a test administrator tested | 2 / 0 |
| AU-10 | R-001; FRC-CSF-BSL AU-10 (Class D) | Focused | Comprehensive | 214 G1 channel releases | 100% (data analytic) | 0 / 1 |
| AU-12 | R-021 | Basic | Focused | 212 G1 log sources | 100% (latency analytic) | 2 / 1 |
| CA-2 | FRC-CSF-BSL CA-2; IVV-CSO-FIA | Focused | Basic | n/a | 2026 assessment examined | 11 / 0 |
| CA-7 | R-014; CCM-OCR-AVL | Focused | Basic | 6 monthly continuous monitoring packages | 3 months (random) | 10 / 1 |
| CM-2 | R-005 | Focused | Focused | n/a (configuration) | Baselines for 5 component types examined | 5 / 0 |
| CM-3 | R-001; R-005; FRC-CSF-BSL CM-3(1) | Comprehensive | Comprehensive | 1,380 G1 change records (2026-01-01 to 2026-06-30); 18 guest-agent channel releases | 60 changes (random); 100% of guest-agent releases | 9 / 1 |
| CM-5 | R-001 | Focused | Focused | 1,380 changes | 25 changes traced to pipeline or PAM sessions | 5 / 1 |
| CM-6 | R-009 | Focused | Comprehensive | About 9,000 G1 hosts | 25 hosts (random) inspected against baseline | 5 / 1 |
| CM-7 | R-063 | Basic | Focused | n/a (configuration) | Host image and 10 hosts scanned | 6 / 0 |
| CM-8 | R-033 | Comprehensive | Comprehensive | About 9,600 G1 components (hosts, switches, arrays, spares) | 60 physical components traced to the inventory (random, both sites) | 5 / 1 |
| CP-4 | R-011 | Focused | Focused | 1 annual G1 test | 100% | 5 / 0 |
| CP-9 | R-062 | Focused | Focused | 181 daily G1 backup jobs | 25 jobs (random); 1 restore observed | 6 / 0 |
| CP-10 | R-011 | Focused | Focused | 1 G1 recovery test | 100% | 1 / 1 |
| IA-2 | R-015 | Basic | Focused | About 300 workforce identities with G1 roles | 25 sign-ins (random) | 2 / 0 |
| IA-5 | R-020 | Focused | Comprehensive | 148 G1 network and out-of-band devices | 100% (credential test with change approval) | 9 / 1 |
| IR-4 | R-001; R-023 | Focused | Focused | 96 G1 security incidents | 25 incidents (random) | 13 / 0 |
| IR-6 | R-013; IEC-CSO-IIR | Focused | Comprehensive | 2 reportable incidents and 3 drills since 2026-08-03 | 100% | 1 / 1 |
| IR-8 | R-013; R-018 | Comprehensive | Focused | n/a (plan) | Plan examined; 4 interviews | 15 / 2 |
| MA-4 | R-028 | Focused | Comprehensive | 214 nonlocal maintenance sessions in G1 | 100% (data analytic) | 7 / 1 |
| PE-3 | R-031 | Basic | Focused | 2,104 badge events at G1 data hall doors in one week | 25 events (random); walkthrough of both sites | 12 / 0 |
| PS-4 | R-022 | Comprehensive | Comprehensive | 412 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | FRC-CSF-BSL RA-3 | Focused | Basic | n/a | 2026 assessment examined | 8 / 0 |
| RA-5 | R-006; VDR-TFR-PVR | Focused | Focused | 3,912 G1 vulnerability findings closed 2026-02 to 2026-07 | 60 findings (random) | 8 / 1 |
| SA-9 | R-030; MAS-CSO-TPR | Focused | Comprehensive | 14 external services supporting G1 | 100% | 5 / 1 |
| SA-10 | R-001; R-027 | Focused | Focused | 214 G1 channel releases | 25 releases (random) | 10 / 1 |
| SC-7 | R-007 | Comprehensive | Focused | n/a (architecture) | Rule review against approved flows; reachability test | 5 / 1 |
| SC-8 | R-003 | Basic | Focused | All G1 external endpoints | 100% (TLS scan) | 1 / 0 |
| SC-12 | R-026 | Focused | Focused | 4 key ceremonies in 2026 | 100% | 2 / 0 |
| SC-13 | R-012; CMU-CSO-UVM | Focused | Comprehensive | 52 FR-2 services | 100% | 1 / 1 |
| SC-28 | R-034 | Basic | Focused | n/a (configuration) | Volume, object, and backup encryption inspected | 1 / 0 |
| SI-2 | R-006; VDR-TFR-KEV | Focused | Focused | 14 KEVs affecting G1 in 2026 | 100% | 9 / 1 |
| SI-3 | R-038 | Basic | Focused | 312 G1 host management servers | 25 servers (random) | 8 / 0 |
| SI-4 | R-019; P10 AI-001 | Focused | Focused | 61 automated host isolations in G1 (2026-01-01 to 2026-06-30) | 100% | 11 / 1 |
| SI-7 | R-001; FRC-CSF-BSL SI-7(5) | Comprehensive | Focused | n/a | Integrity monitoring and response design examined | 5 / 1 |
| SR-3 | R-031 | Focused | Focused | n/a | Procedures examined; receiving observed at G1-A | 3 / 1 |
| SR-6 | R-030 | Focused | Comprehensive | 14 G1 suppliers | 100% | 0 / 1 |
| SR-11 | R-027 | Focused | Focused | n/a | Mirror configuration examined; 10 builds traced | 5 / 0 |
| AT-2 | R-039 | Basic | Focused | About 300 workforce with G1 roles | 25 training records (random); phishing results for 6 months | 10 / 0 |
| PL-2 | FRC-CSF-BSL PL-2; SDR rules | Focused | Basic | n/a (plan) | Plan examined | 8 / 0 |
| MP-6 | R-034 | Basic | Focused | 1,860 drives retired from G1 in 2026 | 25 drives (random) | 4 / 0 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic could test every item.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AU-6, CM-3, CM-8, and RA-5.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CM-5, CM-6, CP-9, IA-2, IR-4, PE-3, SA-10, SI-3, AT-2, and MP-6.
- **Data analytics on the full population:** release approvals (AC-5, AU-10), privileged grants (AC-2), log source latency (AU-12), nonlocal maintenance sessions (MA-4), automated host isolations (SI-4), KEVs (SI-2), cryptographic modules (SC-13), and G1 suppliers (SA-9, SR-6).
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Stratification:** terminations were stratified so contractors (about 20% of the population) got 15 of 60 items, because contractor terminations follow a different process.
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control on the release path (AC-5, AU-10, CM-3, CM-5, SA-10, SI-7) makes the statement Other than satisfied, because one bad release can reach every enrolled customer VM.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP and Class D delta (P02), identity governance and PAM records, release approvals and signing logs, change records, drift and inventory reports, backup and contingency test reports, vulnerability and KEV records, the cryptographic module inventory, vendor register and SOC report reviews, the incident response plan and materiality worksheet, FedRAMP incident reports and drill records.
- **Interview:** Senior Vice President, Government Cloud; Director of Government Cloud Engineering; Vice President, Software Supply Chain; Vice President, Control Plane Engineering; Director of Security Operations; Director of Identity and Access Management; Director of Key Management and PKI; Director of FedRAMP Compliance; General Counsel; Chief Financial Officer; CISO.
- **Test:** data analytics over release, grant, session, and alert populations; a deletion attempt on the log archive; a reachability test from the corporate jump zone; a credential test on G1 network and out-of-band devices (with change approval); TLS scans; physical traces of 60 components at both G1 sites; a restore observation.

## 4. Rules of engagement
- No test could change production or customer resources. Data analytics ran on read-only exports. The reachability test used an audit-owned host in the jump zone with the CISO's written approval.
- The credential test on out-of-band devices ran in an approved change window with a G1 network engineer present.
- No customer content or federal data left G1. Workpapers hold redacted exports only; G1 workpapers are stored in the G1 partition.
- Critical exposures were reported to the CISO within 24 hours. Two were: default credentials on 2 out-of-band console servers (reported 2026-08-05; fixed 2026-08-29) and the over-broad jump zone rule (reported 2026-08-11; narrowed 2026-09-12).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test) at headquarters, G1-A, and G1-B |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the Chief Technology Officer, CISO, and Senior Vice President, Government Cloud |
| 2026-09-10 | Presented to the audit committee and the risk and technology committee |

Deliverables: this plan and report, `assessment-results.csv` (306 rows), and `poam.csv` (29 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 278 |
| Other than satisfied | 28 |
| **Total** | **306** |

**Controls with at least one Other than satisfied statement: 26 of 48:** AC-2, AC-5, AU-6, AU-10, AU-12, CA-7, CM-3, CM-5, CM-6, CM-8, CP-10, IA-5, IR-6, IR-8, MA-4, PS-4, RA-5, SA-9, SA-10, SC-7, SC-13, SI-2, SI-4, SI-7, SR-3, SR-6.

**Fully Other than satisfied:** AU-10, SR-6 (each has a single determination statement).

**Themes:**
1. **The release path is the main weakness.** Six findings across AC-5, AU-10, CM-3, CM-5, SA-10, and SI-7 share one root cause: the guest-agent channel of fleet automation can be authored, approved, and promoted by one team, approvals are not bound to a person by signature, and nothing halts a rollout on an integrity alert (POAM-001). This is the path in the P08 scenario.
2. **Class D readiness.** Recovery time (CP-10), cryptographic module validation (SC-13), vulnerability timeframes (RA-5, SI-2), and 15-minute incident reporting (IR-6, IR-8) meet Class C but not Class D.
3. **AI in the SOC.** AI triage auto-closes some alerts and isolates G1 hosts without human review (AU-6, SI-4; POAM-013; P10).
4. **Hygiene at the edges of G1.** BMC drift (CM-6), spare servers outside the inventory (CM-8), default credentials on out-of-band devices (IA-5), vendor sessions without recording (MA-4), and an over-broad firewall rule (SC-7).
5. **Disclosure readiness.** The materiality worksheet does not address a multi-tenant incident (IR-8; POAM-011).

**Strengths:** identity and privileged access (IA-2, AC-6, AC-17), operator access to tenant resources (AC-3), log protection (AU-9), backups (CP-9), key management (SC-12), encryption (SC-8, SC-28), physical access (PE-3), media sanitization (MP-6), and component authenticity (SR-11) were all Satisfied.

## 7. POA&M summary
`poam.csv` holds 29 items: 18 from this assessment (POAM-001 to POAM-019, except POAM-016) and 11 carried from the P02 Class D delta, the P03 gap analysis, the P05 BIA, the P01 register, and the P10 inventory (POAM-016, POAM-020, POAM-021, POAM-022, POAM-023, POAM-024, POAM-025, POAM-026, POAM-027, POAM-028, POAM-029), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 9 |
| Moderate | 18 |
| Low | 2 |

| Status | Items |
|---|---|
| In progress | 21 |
| Open | 8 |

## 8. Conclusion
Internal Audit concludes that the HCP-G control environment is **effective with exceptions** at the Class C level and **not yet ready** for the Class D independent assessment. Enterprise common controls for identity, logging, backup, key management, and physical security operate effectively. The exceptions concentrate on the release path and on the Class D-specific parameters. Management accepted all findings and committed to the POA&M dates; the Chief Technology Officer used this report for the conditional decision in P02 section 4.2. Internal Audit will retest POAM-001, POAM-009, and POAM-010 in 2027-01 before the Class D assessment.
