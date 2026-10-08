# Regulatory Gap Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded diversified precision-agriculture crop farm, NAICS 111998; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Agriculture, Forestry, Fishing and Hunting |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**, with NIST SP 800-82 Rev. 3 (September 2023) applied to OT |
| Binding rules analyzed | SEC Form 8-K Item 1.05 and Reg S-K Item 106; FDA Produce Safety Rule records (21 CFR 112, Subpart O); FDA Food Traceability Rule (21 CFR 1, Subpart S, readiness); H-2A earnings records and statements (20 CFR 655.122(j)-(k)); EPA Worker Protection Standard records (40 CFR 170.311(b)); FAA Part 107 and Part 137; state data security, breach notice, and disposal laws (Florida worked example); PCI DSS by contract; 21 CFR Part 121 (N11-R01) and the farm-status condition that would trigger it |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Chief Food Safety and Quality Officer; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |
| Workbook | `gap-analysis.csv` (145 rows) |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv), with counsel's review (EV-077); the Part 121 conclusion was confirmed in the 2026-07 applicability memo (EV-088). This section restates the results for the rules analyzed here.

**No binding sector-specific federal cybersecurity rule applies to the company.** Each candidate was checked:

| Candidate | Applies? | Basis |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (vertical requirement **N11-R01**) | **No** | Part 121 applies to facilities required to register under FD&C Act section 415 (21 CFR 121.1). Farms do not register (21 CFR 1.226(b)). The 48 farms are primary production farms and the 3 hubs are secondary activities farms under 21 CFR 1.227, and farm activities subject to the Produce Safety standards are exempt anyway (121.5(d)). The very small business exemption (121.5(a)) does **not** help at this size, so farm status is the condition that matters (row G-145) |
| Farm status of the hubs (21 CFR 1.227) | **Yes, as a monitored condition** | A hub stays a secondary activities farm only while company farms grow the majority of the raw agricultural commodities it packs and holds. Hub 2 is at 31% third-party produce and the grower services plan would pass a majority in 2027, which would require FDA registration and bring Part 121 and Part 117 into scope |
| Reportable Food Registry, 21 U.S.C. 350f | **No** | The duty falls on the responsible party that registers a food facility; the company registers none. Kept in the P08 matrix for coordination with buyers |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company. Item 106 defines information systems to include physical infrastructure controlled by them, so irrigation and packing OT are in scope (17 CFR 229.106(a)) |
| Produce Safety Rule, 21 CFR Part 112 | **Yes** | Covered farm: produce sales far exceed the inflation-adjusted $25,000 threshold (112.4(a)), and all food sales far exceed the $500,000 qualified exemption limit (112.5). Only the Subpart O record requirements are a cybersecurity concern; the growing standards are outside this analysis |
| Food Traceability Rule, 21 CFR 1.1300-1.1465 | **Yes (enforcement from 2028-07-20)** | The company grows, cools, and initially packs foods on the Food Traceability List (tomatoes, peppers, cucumbers, melons). The farm alternative to the sortable spreadsheet in 1.1455(c)(3)(iii)(A) (no more than $250,000 a year) does not apply |
| H-2A program, 20 CFR 655.122(j)-(k) | **Yes** | About 5,600 H-2A workers under about 60 labor certifications a year |
| Worker Protection Standard, 40 CFR 170.311(b) | **Yes** | Agricultural employer applying pesticides on its establishments |
| FAA Part 107 | **Yes** | About 140 company drones flown by about 58 certificated remote pilots |
| FAA Part 137 | **No** | The company flies no application aircraft; contracted applicators must hold Part 137 certificates (14 CFR 137.11), checked at vendor onboarding |
| State data security, breach notice, and disposal laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example. Seasonal and H-2A workers add home-country addresses to the residence analysis |
| PCI DSS | **By contract** | Acquirer agreement for the produce box (hosted payment page; self-assessment questionnaire) |
| HIPAA | **No** | Not a covered entity; the employee group health plan is a separate covered entity outside these deliverables |
| FAR 52.204-21, -23, -25 | **No** | No federal prime contracts or subcontracts since 2024 |
| State comprehensive consumer privacy laws | **Not analyzed further** | None enacted in Georgia, South Carolina, or North Carolina according to the repository's cross-sector register (as of 2026-09-25). Florida's Digital Bill of Rights is reported to reach only businesses with more than $1 billion in revenue that also meet further criteria; that threshold was **not verified** here and is flagged for counsel |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25. As proposed, it would cover the company through the size criterion, because it exceeds the SBA size standard for NAICS 111998 ($2.5 million, 13 CFR 121.201) |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll (SYS-11) are tested by the SOX program and not repeated here |

**Decision: NIST CSF 2.0 as the benchmark, with SP 800-82 Rev. 3 for OT.** This follows the vertical profile: primary agricultural production has no binding federal cybersecurity regulation, and CSF 2.0 is the sector-neutral baseline. SP 800-82 Rev. 3 predates CSF 2.0, so its OT guidance is applied to the matching CSF 2.0 subcategories (author mapping, column `ot_application_sp800_82r3`). CSF ratings measure the company against its Target Profile, not against a legal duty. The binding rows (G-107 to G-145) are legal or contractual duties.

## 2. Method
1. **Decompose.** The 106 CSF 2.0 subcategories and outcome text come from `00_universal-framework/frameworks/csf2_core.csv`. Binding rules were broken into citation-level duties from the eCFR text current as of 2026-09-23 (21 CFR 112.161-112.166; 21 CFR 1.1315-1.1340 and 1.1455; 20 CFR 655.122; 40 CFR 170.311; 14 CFR 107.7, 107.9, 107.12, 137.11; 17 CFR 229.106), the SEC's Form 8-K instructions for Item 1.05, and the 2026 Florida statute. PCI DSS rows list only the questionnaire type; the standard's text is not reproduced.
2. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53) in `nist_official_sp800_53r5`; the `sp800_53_controls` column is a key-control subset chosen by the author. Binding-rule rows are author mappings and are labeled that way.
3. **Target Profile.** Each subcategory has a priority (High 51, Medium 53, Low 2), set by the CISO and the Chief Risk Officer from the risk register (P01) and BIA (P05).
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and populations under 250 used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random, stratified by region where noted. **35 rows were tested by sampling or full-population analytics; 19 found exceptions.** Current state was established from the intake evidence (exports, documents and records from the enterprise systems of record, EV-001 to EV-078 and EV-093), gap analysis interviews with control owners (EV-083), the samples and analytics (EV-084 to EV-087), the Part 121 applicability memo (EV-088), the 2026 third-party food safety audit reports (EV-089), and, where Internal Audit had already tested a control, its P07 results (for example EV-CM-6 and EV-IA-5). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Rate.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. High gaps are in the P01 register and the P07 POA&M.

**CSF Tier.** Current: **Tier 3 (Repeatable) for IT and Tier 2 (Risk Informed) for OT.** Target: Tier 3 for OT by 2027-12, once OT vendor access, change control, and monitoring coverage are closed.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CSF 2.0 Govern | 22 | 9 | 0 | 0 | 31 |
| CSF 2.0 Identify | 13 | 8 | 0 | 0 | 21 |
| CSF 2.0 Protect | 9 | 13 | 0 | 0 | 22 |
| CSF 2.0 Detect | 7 | 4 | 0 | 0 | 11 |
| CSF 2.0 Respond | 11 | 2 | 0 | 0 | 13 |
| CSF 2.0 Recover | 5 | 3 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **67** | **39** | **0** | **0** | **106** |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Reg S-K Item 106 | 4 | 0 | 0 | 0 | 4 |
| Produce Safety records, 21 CFR 112 Subpart O | 6 | 1 | 0 | 0 | 7 |
| H-2A earnings records and statements, 20 CFR 655.122(j)-(k) | 3 | 1 | 0 | 0 | 4 |
| Worker Protection Standard, 40 CFR 170.311(b) | 1 | 0 | 0 | 0 | 1 |
| Food Traceability Rule (readiness) | 2 | 6 | 0 | 0 | 8 |
| FAA Part 107 and Part 137 | 2 | 0 | 0 | 1 | 3 |
| State data security, breach, and disposal laws (Florida worked example) | 3 | 3 | 0 | 0 | 6 |
| PCI DSS (contractual) | 1 | 0 | 0 | 0 | 1 |
| 21 CFR Part 121 (N11-R01) and farm status | 0 | 1 | 0 | 1 | 2 |
| **Total** | **90** | **53** | **0** | **2** | **145** |

**Gap risk levels of the 53 partially met rows:** High 12, Moderate 33, Low 8.

**The pattern:** the program is defined and repeatable across Govern, Respond, and most of Identify. The gaps sit in three places. First, **OT third-party access and change control**: two integrators, the AQ-02 pivot cloud service, and some packing line vendors work outside the OT gateway, without contract terms or recorded sessions, at the same stations where change approvals and integrity checks are missing. Second, **acquired operations**: AQ-01 and AQ-02 still run legacy identity, flat networks, shared logins, and untested backups. Third, **disclosure under pressure**: the SEC materiality process has not been exercised with an OT outage or with the current committee. Food regulatory records are in good shape for the Produce Safety Rule; Food Traceability Rule readiness is the main records gap, with enforcement from 2028-07-20.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-026 | CSF 2.0 GV.SC-05 | INT-4, INT-5, the pivot manufacturer, and the 3 equipment dealers have no security terms | Amend agreements (POAM-004; POAM-002; POAM-016) | Director of Third-Party Risk Management | 2026-12-31 |
| G-045 | CSF 2.0 ID.RA-07 | 6 of 40 sampled OT changes lacked approval records, all at INT-4 and INT-5 stations | Enforce approval; block unapproved downloads (POAM-006) | SCADA Engineering Manager | 2027-01-31 |
| G-052 | CSF 2.0 ID.IM-04 | Materiality playbook has no OT outage or crop loss factors and has not been exercised with the current committee | Update and exercise the playbook (POAM-012) | General Counsel | 2026-11-30 |
| G-053 | CSF 2.0 PR.AA-01 | 412 seasonal FMIS accounts active more than 30 days after season end; AQ-01 shared tally logins; AQ legacy directories | POAM-003; POAM-023; POAM-001 | Director of Identity and Access Management | 2027-06-30 |
| G-055 | CSF 2.0 PR.AA-03 | AQ-02 pivot cloud service with shared logins and no MFA; 3 AQ-01 applications outside SSO | Interim MFA by 2026-11-15; migration (POAM-002); federation (POAM-001) | Director of Identity and Access Management | 2027-06-30 |
| G-071 | CSF 2.0 PR.IR-01 | AQ-01 farm offices flat; legacy VPN rule reached the R4 historian collector (removed 2026-09-04) | SD-WAN migration and segmentation (POAM-013) | Director of Network Engineering | 2027-03-31 |
| G-073 | CSF 2.0 PR.IR-03 | One carrier's private APN carries about 80% of field OT traffic | Second carrier for pivots in R1 and R3; radio expansion (POAM-024) | Director of Network Engineering | 2027-06-30 |
| G-078 | CSF 2.0 DE.CM-06 | 9 of 60 sampled vendor sessions outside the gateway and unrecorded | Gateway onboarding (POAM-004); dealer access on request (POAM-016) | Director of OT Security | 2026-12-31 |
| G-089 | CSF 2.0 RS.MA-04 | Escalation from SOC detection to a materiality decision never tested end to end | Tabletop 2026-11-17 (POAM-012) | General Counsel | 2026-11-30 |
| G-100 | CSF 2.0 RC.RP-02 | SCADA master restore took 9.5 hours against a 6-hour RTO | Pre-staged images, automated restore, retest (POAM-011) | SCADA Engineering Manager | 2027-01-31 |
| G-107 | Form 8-K Item 1.05(a); General Instruction B.1 | Four-business-day process not exercised with the current committee or an OT outage | Tabletop; brief new members (POAM-012) | General Counsel | 2026-11-30 |
| G-108 | Form 8-K, Instruction 1 to Item 1.05 | Materiality factors omit crop loss, missed harvest windows, and worker safety | Add OT and crop loss factors (POAM-012) | General Counsel | 2026-11-30 |

Moderate gaps with regulatory consequences that are not High: Produce Safety and H-2A attribution at AQ-01 (G-115, G-121; POAM-023), Food Traceability Rule key data elements and the 24-hour sortable spreadsheet (G-128 to G-132; POAM-020), state residence tracking for breach notice (G-139), and hub farm status (G-145).

## 5. Compliance roadmap
| Quarter | Milestones | Requirements served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee tabletop with an OT outage and playbook update (POAM-012); default credentials removed (POAM-010); INT-4, INT-5, and packing vendors onto the gateway and agreements amended (POAM-004); interim MFA in the AQ-02 pivot service (POAM-002); OT training (POAM-018); AQ-01 backups into the enterprise service (POAM-017); cyber outage injection in the November freeze drill; residence-state field in the incident tracker | Item 1.05; CSF GV.SC-05, DE.CM-06, PR.PS-01, PR.AT-02, PR.DS-11, RC.RP-01; Fla. Stat. 501.171(4) | Tabletop report; gateway logs; signed amendments; drill report |
| 2027 Q1 | OT change enforcement (POAM-006); SCADA restore retest within 6 hours (POAM-011); seasonal account inactivity disablement (POAM-003); named AQ-01 tally accounts before the season (POAM-023); FMIS role split (POAM-007); AQ-01 SD-WAN migration (POAM-013); hub share automation | CSF ID.RA-07, RC.RP-02, PR.AA-01, PR.AA-05, PR.IR-01; 21 CFR 112.161(a)(4); 20 CFR 655.122(j)(1); 21 CFR 1.227 | Change reports; DR test report; account analytics; share report |
| 2027 Q2 | AQ-02 pivots onto company SCADA and AQ identity federation (POAM-002; POAM-001); OT monitoring expansion (POAM-005); second carrier (POAM-024); HMI replacement (POAM-014); pivot firmware (POAM-009); integrity checks at all stations (POAM-019) | CSF PR.AA-03, DE.CM-01, PR.IR-03, PR.PS-02, DE.CM-09 | Migration records; sensor coverage; carrier contract |
| 2027 Q3 | Traceability data service passes mock requests for all 4 FTL groups (POAM-020); annual risk analysis and gap reassessment | 21 CFR 1.1325-1.1340; 1.1455(c)(3)(ii) | Mock request report; updated P01 and P03 |

## 6. Pending regulatory changes (not current obligations)
- **Food Traceability Rule timing.** The original compliance date was 2026-01-20. FDA proposed to extend it to 2028-07-20 (90 FR 38084, 2025-08-07), and Pub. L. 119-37 directed FDA not to enforce the rule before 2028-07-20; FDA said it intends to comply (91 FR 31723, 2026-05-28). No final rule extending the compliance date was found in the Federal Register as of 2026-09-25. The company treats 2028-07-20 as the enforcement date and keeps its 2027-09-30 readiness target, because retail customers already ask for the data.
- **CIRCIA:** no final rule as of 2026-09-25. As proposed, it would cover the company through the size criterion. Reporting to CISA stays voluntary until a rule takes effect; P08 tracks it.
- **NIST SP 800-82 Rev. 4:** initial public draft with comments due 2026-11-30. Not used; OT rows note it in `pending_rule_change`.
- **H-2A rules:** the Department of Labor proposed on 2025-07-02 (90 FR 28919) to rescind parts of its 2024 farmworker protections rule that amended 20 CFR 655.122. No final rescission was found as of 2026-09-25. Whether the proposal would change the earnings record content in 655.122(j)(1) was not verified. The company follows the current text.
- **SEC:** no proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25.
- **Produce Safety Rule:** no pending change found after the 2024 agricultural water rule (89 FR 37448).

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can answer quickly an FDA records request or inspection, a Department of Labor H-2A audit, an EPA or state agency Worker Protection Standard inspection, a retailer audit, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- Produce Safety record retrieval drill results and the 2026 third-party audit reports for the 17 packing sites;
- the traceability plan draft, farm map, and mock request results;
- H-2A record production drill results and earnings statement samples;
- the disclosure committee charter, materiality playbook, and the annual report Item 1C workpapers;
- the hub third-party share reports and the farm-status analysis.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
