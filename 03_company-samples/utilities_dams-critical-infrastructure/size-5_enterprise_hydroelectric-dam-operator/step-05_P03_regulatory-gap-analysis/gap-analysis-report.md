# Regulatory Gap Analysis: Cris Santos Company | Dams | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded hydroelectric generation company: 31 FERC licenses, 46 developments, 63 dams, 8,640 MW; NERC-registered Generator Owner and Generator Operator) |
| Tier / Vertical | Enterprise / Dams |
| Primary program analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (March 30, 2016), for a fleet with **4 Group 1, 19 Group 2, and 40 Group 3 dams**. Source: https://www.ferc.gov/sites/default/files/2020-04/security.pdf, with the FERC FAQ and the Revision 3/3A change notice (retrieved 2026-09-26) |
| Also analyzed | NERC CIP-002-5.1a to CIP-014-3 for a medium and low impact GO/GOP (C-DAMS-R03); NERC EOP-004-4; 18 CFR Part 12 (C-DAMS-R02 and related sections) and 18 CFR 388.113; Form DOE-417; SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example) |
| Versions checked | eCFR text for 18 CFR Part 12 and 388.113 (version 2026-09-23); NERC standard texts and the NERC BES Definition Reference Document (version 3, April 30, 2026); CIP effective dates from 02_industry-rules (NERC bulletin, 2026-08-31 to 2026-09-07); Form DOE-417 instructions (OMB 1901-0288) |
| Assessment dates | 2026-06-01 to 2026-07-31 (Section 9 determinations refreshed 2026-07-08; evidence sampling completed 2026-08-14) |
| Assessors | GRC team and NERC compliance team (second line) with the Chief Compliance Officer; sampling reperformed by Internal Audit for 12 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the safety, risk, and reliability committee of the board, 2026-09-10 |
| Handling | Rows describing Section 9 and CIP gaps are BCSI and "Privileged - Security Sensitive Material"; this sample is fictional |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FERC Security Program (C-DAMS-R01) | **Yes** | FERC licensee; 18 CFR Part 12 applies to projects licensed under Part I of the Federal Power Act (12.1(a)(1)). The program is D2SI guidance enforced through inspections under the Regional Engineer's authority. **Size does not matter; Security Group does.** Group 1 duties (Vulnerability Assessment, Rapid Recovery, Security Plan exercise every 5 years) apply to 4 dams; Group 2 duties to 19; Group 3 dams have no document duties, but those interconnected with Group 1 and 2 projects must be protected (Sec. 3.3.3) |
| Section 9 (cyber and SCADA) | **Yes, Critical** | All 23 Group 1 and 2 dams answered Yes to remote operation (Form 3 Q1-4). The HOC fleet SCADA controls more than 1,500 MW through one cyber asset, which Table 9.1c note 1 makes Critical; gate control at the Group 1 and 2 dams exceeds the population-at-risk thresholds. Baseline **and enhanced** measures apply, with a plan and schedule for each negative Form 3 answer |
| NERC CIP (C-DAMS-R03) | **Yes, medium and low impact** | Registered GO and GOP (SERC). Under the BES definition (Inclusion I2: units over 20 MVA or plants over 75 MVA, connected at 100 kV or above) 34 developments are BES. CIP-002-5.1a criterion 2.11 makes the HOC BES Cyber Systems **medium impact** (GOP Control Centers for 1,500 MW or more in one Interconnection). No high impact: no plant reaches 1,500 MW (criterion 2.1) and no criterion 2.3, 2.6, or 2.9 designation exists, so criterion 1.4 is not met. 34 plants contain low impact BES Cyber Systems (criterion 3.3; Blackstart Resources also 3.4). Note: the README summary row for this vertical describes a 3,000 MW high impact threshold; that figure belongs to Balancing Authority and Transmission Operator criteria, not to a Generator Operator, and is not used here |
| CIP-012-2 | **Yes** | Applies to GOPs with Control Centers; real-time data moves between HOC-A, HOC-B, and the Balancing Authority and Transmission Operator Control Centers |
| CIP-013-2 | **Yes, medium impact only** | Applies to medium impact BES Cyber Systems and their EACMS and PACS. The company applies the same terms to all OT procurement by its own standard (STD-01.3), which is how the OEM gap is rated |
| CIP-014-3 | **No** | Transmission Owners and Operators only |
| Section 9 and CIP overlap | **Both, coordinated** | FERC FAQ Question 12 (hub and spoke) and Rev. 3A 9.4: the HOC hub meets CIP and the Security Plan references the CIP standards met; each plant is evaluated under Section 9 |
| NERC EOP-004-4 | **Yes** | GO and GOP are applicable entities |
| 18 CFR Part 12 | **Yes** | 12.10 (C-DAMS-R02): security incidents (physical and/or cyber) and gate misoperation are conditions affecting safety (12.3(b)(4)(ii), (xi)). Also EAPs, gate testing, records, the Owner's Dam Safety Program (38 High hazard dams, so a Chief Dam Safety Engineer is required, 12.62(a)), and the 5-year independent audit (12.65) |
| 18 CFR 388.113 | **Yes, for filings** | CEII submitted to FERC needs a request and justification; internal handling follows POL-04 |
| Form DOE-417 | **To be confirmed** | Clocks verified from the form and instructions. The OMB abstract names utilities that operate a Balancing Authority or Reliability Coordinator and other electric utilities as appropriate; the company is neither a BA nor an RC, so its own filer role is being confirmed with DOE and the Balancing Authorities (row G-227) |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | Each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25; reporting is voluntary |
| FAR clauses | **No** | No federal contracts |

## 2. Method
1. **Decompose.** FERC rows follow the program's own structure: section 3.2 licensee responsibilities, the Group 1 and Group 2 duties (3.3.1, 3.3.2, Table 3.3.8), sections 4 to 8 including each Group 1 statement in the certification letter, every line of the Section 9 baseline and enhanced measures (Tables 9.3a and 9.3b), the Form 3 questions not already covered, the FAQ items that matter for a fleet (Question 10 interconnection, Question 12 hub and spoke), and three Form 1 items. NERC rows follow each standard's requirements and parts. FERC and NERC documents and CFR text are public; short phrases are used where the wording matters.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **All mappings are author mappings**: NIST has published no mapping for the FERC program or NERC CIP. The FERC program's own tables cite NIST SP 800-82, so SP 800-82 Rev. 3 and its overlay were the bridge.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller or lower-risk populations used 25 to 40 items; small populations (dams, plants, quarters) and configuration data were tested in full. **44 rows were tested by sampling or full-population analytics; 24 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and has an owner and date. High and Very High gaps are in the P01 register and the P07 POA&M. The plan and schedule FERC asks for under Section 9.1.1.3 is the POA&M filtered to the Section 9 rows.
5. **Scope.** The `scope_entities` column says which part of the fleet each row covers (for example, the 4 Group 1 dams, the 34 low impact BES plants, or HOC-A and HOC-B).

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FERC Sec. 3.2 and 3.4 Licensee responsibilities | 8 | 3 | 0 | 0 | 11 |
| FERC Sec. 3.3, 5, 6, 7 Group requirements, assessments, Security Plans | 9 | 7 | 0 | 0 | 16 |
| FERC Sec. 4 Threat notification and communications | 3 | 0 | 0 | 0 | 3 |
| FERC Sec. 8 Annual certification letter | 3 | 4 | 0 | 0 | 7 |
| FERC Sec. 9, Form 3, and FAQ (cyber and SCADA) | 19 | 15 | 0 | 0 | 34 |
| FERC Appendix A Form 1 (physical checklist) | 1 | 2 | 0 | 0 | 3 |
| 18 CFR Part 12 and CEII | 7 | 2 | 0 | 0 | 9 |
| NERC CIP-002 | 6 | 0 | 0 | 0 | 6 |
| NERC CIP-003 | 8 | 7 | 0 | 0 | 15 |
| NERC CIP-004 | 15 | 2 | 0 | 2 | 19 |
| NERC CIP-005 | 12 | 0 | 0 | 0 | 12 |
| NERC CIP-006 | 13 | 0 | 0 | 1 | 14 |
| NERC CIP-007 | 19 | 0 | 0 | 1 | 20 |
| NERC CIP-008 | 12 | 0 | 0 | 0 | 12 |
| NERC CIP-009 | 9 | 0 | 0 | 1 | 10 |
| NERC CIP-010 | 10 | 0 | 0 | 4 | 14 |
| NERC CIP-011 | 3 | 1 | 0 | 0 | 4 |
| NERC CIP-012 | 4 | 1 | 0 | 0 | 5 |
| NERC CIP-013 | 9 | 0 | 0 | 0 | 9 |
| NERC CIP-014 | 0 | 0 | 0 | 1 | 1 |
| NERC EOP-004-4 | 2 | 0 | 0 | 0 | 2 |
| Form DOE-417 | 0 | 1 | 0 | 0 | 1 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **181** | **48** | **0** | **10** | **239** |

**FERC Security Program:** 43 Met, 31 Partially met, 0 Not met (74 rows). **NERC CIP:** 120 Met, 11 Partially met, 10 Not applicable (141 rows; the Not applicable rows are the parts that apply only to high impact systems, plus CIP-014).

**Gap risk levels (Partially met rows):** Very High 5, High 18, Moderate 20, Low 5.

**The pattern.** The program is mature where it has been in place for years: the HOC medium impact CIP program (SERC audit 2025-03, findings mitigated), the Security Plans and Security Assessments, Part 12 reporting, EAPs, and the Owner's Dam Safety Program. The gaps cluster in four places:
- **Piedmont.** Every Very High row and most High rows trace to the 9 acquired developments: CIP-003-9 Attachment 1 Sections 3.1 and 6 at PD-02, PD-04, and PD-06 (potential noncompliance, self-reported 2026-09-30), uncontrolled remote access, shared accounts, and missing Security Plan and Section 9 documentation for PD-04 and PD-06.
- **Coverage below the HOC.** Section 9 enhanced measures (monitoring, vulnerability assessment) reach the HOC hub but not every spoke.
- **Statements to regulators.** The 2025 certification letter reported PD contact verification as complete when it was not (G-034). It is High because it concerns accuracy toward FERC.
- **Three potential CIP issues at the HOC level:** BCSI in a contractor-shared folder (CIP-011-3 R1.2), one late access removal (CIP-004-7 R5.1), and the PD low impact sections. All were self-reported on 2026-09-30.

## 4. Priority gaps (Very High and High)
| Row | Citation | Risk | Gap | Action | Owner | Target |
|---|---|---|---|---|---|---|
| G-013 | Sec. 3.3.2; Sec. 7.2 (Information Technology/SCADA) | High | PD-04 and PD-06 cyber measures not documented to fleet standard | Add PD-04 and PD-06 to the fleet Cyber/SCADA Security Plan with the remote access redesign (POAM-001) | Director, OT Security | 2026-12-31 |
| G-034 | Sec. 8.0 (bullets 5-6) | High | Statement to FERC about PD contact verification was not supported | Correct the statement with the Regional Engineer and in the 2026 letter; evidence checklist for each letter statement (R-055) | Chief Compliance Officer | 2026-10-31 |
| G-040 | Sec. 9.1.1.3; Sec. 9.1.1.2 | High | PD-04 and PD-06 plan and schedule not yet filed | File PD-04 and PD-06 plan and schedule letters | Director, OT Security | 2026-09-30 |
| G-045 | Sec. 9.3 Table 9.3a (General: network connections) | High | Undocumented vendor paths | Remove the paths; add cellular discovery to the review (POAM-012) | Director, OT Network Engineering | 2026-11-30 |
| G-050 | Sec. 9.3 Table 9.3a (Coordination: acquisition standards) | High | Largest OT service contract (91 of 151 units) lacks security terms | Amend the OEM contract (POAM-014) | Director of Third-Party Risk Management | 2027-03-31 |
| G-052 | Sec. 9.3 Table 9.3a (System Lifecycle: configuration and patching); Form 3 Q15 | High | Unsupported operating systems at plants | Replacement program (POAM-005) | Director, Hydro Control Systems Engineering | 2027-12-31 |
| G-054 | Sec. 9.3 Table 9.3a (Restoration and Recovery); Form 3 Q16 | High | Logic copies stale at 14 plants; failover 3.4 h against 2 h | Refresh logic copies (POAM-008); retest failover (POAM-010) | Director, Hydro Control Systems Engineering | 2027-01-31 |
| G-055 | Sec. 9.3 Table 9.3a (Intrusion Detection and Response) | High | No network monitoring at 24 HOC-operated plants | Sensor rollout (POAM-003) | Director of Security Operations | 2027-06-30 |
| G-057 | Sec. 9.3 Table 9.3a (Access Control and Functional Segregation: firewalls); Form 3 Q11a-11b, Q22 | High | PD control networks reachable from the legacy VPN | Remote access redesign (POAM-001) | Vice President, Integration Management Office | 2026-12-31 |
| G-059 | Sec. 9.3 Table 9.3a (Access Control: remote and third-party connections); Form 3 Q12a-12c | Very High | PD remote and vendor access uncontrolled; cellular datalogger paths at 5 dams | POAM-001; POAM-012 | Vice President, Integration Management Office | 2026-12-31 |
| G-060 | Sec. 9.3 Table 9.3b (Access Control: enhanced); Form 3 Q18h, Q21 | High | Shared accounts at PD plants | Named accounts (POAM-002) | Vice President, Integration Management Office | 2027-01-31 |
| G-061 | Sec. 9.3 Table 9.3b (Vulnerability Assessment); Form 3 Q18i, Q31 | High | Assessment interval exceeded at 13 plants and all PD plants | Assessment program for all plants by 2027-06-30 (POAM-004) | Director, OT Security | 2027-06-30 |
| G-062 | Form 3 Q14a-14c | High | As for network monitoring | POAM-003 | Director of Security Operations | 2027-06-30 |
| G-093 | CIP-003-9 R2 | High | Plan not implemented at the 3 Piedmont BES plants | Implement Attachment 1 at PD-02, PD-04, and PD-06 (POAM-001; POAM-002) | Vice President, Integration Management Office | 2026-12-31 |
| G-096 | CIP-003-9 R2 Att. 1 Sec. 3.1 | Very High | Potential noncompliance at 3 Piedmont BES plants; self-reported to SERC 2026-09-30 | Gateway firewalls with documented rules; legacy VPN retired (POAM-001) | Vice President, Integration Management Office | 2026-12-31 |
| G-100 | CIP-003-9 R2 Att. 1 Sec. 6.1 | Very High | Potential noncompliance at PD-02, PD-04, PD-06 (Section 6 in effect since 2026-04-01); self-reported | POAM-001 | Vice President, Integration Management Office | 2026-12-31 |
| G-101 | CIP-003-9 R2 Att. 1 Sec. 6.2 | Very High | No reliable method at the PD plants before 2026-09-18 | POAM-001 | Vice President, Integration Management Office | 2026-12-31 |
| G-102 | CIP-003-9 R2 Att. 1 Sec. 6.3 | Very High | No detection at the PD plants | OT sensors at PD plants (POAM-001) | Director of Security Operations | 2026-12-31 |
| G-117 | CIP-004-7 R5 Part 5.1 | High | Potential noncompliance; self-reported to SERC 2026-09-30 | Daily contractor roster reconciliation; vendor notice enforcement (POAM-016) | Chief Human Resources Officer | 2026-12-31 |
| G-121 | CIP-004-7 R6 Part 6.1 | High | BCSI access provisioned outside R6 authorization (contractor folder) | POAM-006 | Director, NERC Compliance | 2026-11-30 |
| G-207 | CIP-011-3 R1 Part 1.2 | High | Potential noncompliance; self-reported to SERC 2026-09-30 | Remove the folder; review access history; BCSI DLP rules (POAM-006) | Director, NERC Compliance | 2026-11-30 |
| G-228 | Form 8-K Item 1.05; SEC Release 33-11216 | High | Process untested for the company's highest-consequence incident type | Tabletop 2026-11-18 with an OT and dam safety scenario; playbook update (POAM-013) | General Counsel | 2026-11-30 |
| G-229 | Form 8-K Item 1.05 (materiality determination) | High | Escalation timing untested end to end | POAM-013 | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q3 (by 2026-09-30) | Self-reports to SERC (PD CIP-003-9 Sections 3.1 and 6; CIP-004-7 R5.1; CIP-011-3 R1.2); plan and schedule letters for PD-04 and PD-06 to the Regional Engineer; correction of the PD contact statement | CIP-003-9; CIP-004-7; CIP-011-3; Rev. 3A 8.0 and 9.1.1.3 | Self-report filings; FERC letters |
| 2026 Q4 | PD remote access redesign and monitoring (POAM-001); BCSI cleanup (POAM-006); DEV-04 VA reprint and DEV-03 exercise (POAM-007); cellular datalogger paths removed (POAM-012); disclosure tabletop 2026-11-18 (POAM-013); PLC logic copies (POAM-008); PD-07 load test (POAM-023); 2026 certification letter by 2026-12-31 | CIP-003-9 Att. 1; CIP-011-3; Rev. 3A 3.3.1, 8.0, 9.3a; 18 CFR 12.54; SEC Item 1.05 | Firewall rule sets; session logs; VA reprint; exercise report; tabletop report; certification letter |
| 2027 Q1 | Named accounts at PD plants (POAM-002); HOC failover retest (POAM-010); OEM contract amendment (POAM-014); CEII cleanup (POAM-022); PD integration onto the HOC (2027-03-31) after a pre-connection assessment | Rev. 3A 7.4.2, 9.3b; CIP-009-6; company standard STD-01.3 | Failover report; amended contract; integration assessment |
| 2027 Q2 | OT sensors at all Group 1 and 2 gated plants, then Group 3 (POAM-003); OT vulnerability assessments at all plants (POAM-004); diverse telecom paths, first tranche (POAM-011) | Rev. 3A 9.3a, 9.3b; CIP-012-2 R1.2 | Coverage maps; assessment reports |
| 2027 Q3 to Q4 | Unsupported HMI and gate workstation replacement (POAM-005); annual reassessment; check NERC and FERC revisions | Rev. 3A 9.3a; all | Replacement records; updated P01 and P03 |

## 6. Pending regulatory changes
- **FERC Security Program:** Revision 3A is the latest revision this analysis could confirm on ferc.gov. The FERC program page refused automated access, so a newer revision could not be ruled out; the Vice President, Corporate Security will confirm with the Regional Engineers before the next inspections.
- **NERC CIP:** approved future versions are tracked per row in `pending_rule_change`: the virtualization revisions (CIP-002-8, CIP-003-10, CIP-004-8, CIP-005-8, CIP-006-7.1, CIP-007-7.1, CIP-008-7.1, CIP-009-7.1, CIP-010-5, CIP-011-4.1, CIP-013-3) effective 2028-07-01; CIP-015-1 internal network security monitoring effective 2028-10-01; CIP-003-11 effective 2029-07-01; CIP-015-2 effective 2029-10-01. FERC also directed further supply chain revisions. These are future obligations, not current ones.
- **Form DOE-417:** the current OMB approval expires 2027-05-31; check for a revised form.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect. The proposed rule has no dams-specific criterion; the company would likely be covered through its size or its NERC registration if the rule is finalized as proposed. Recheck when final.
- **SEC:** no proposal to amend or rescind Item 1.05 or Item 106 was found as of 2026-09-25.

## 7. Regulator-ready package
The GRC and NERC compliance teams keep an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a FERC dam safety or security inspection, a SERC audit or spot check, a DOE or E-ISAC inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the Cyber/SCADA Security Plan with its CIP cross-references (FERC FAQ Question 12), the Section 9 determinations, and the Form 3 answers for all 23 Group 1 and 2 dams;
- CIP evidence packages by standard, the self-reports, and mitigation plans;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- certification letters, 12.10 reports, EAP test records, and the Owner's Dam Safety Program annual reviews;
- retention: CIP evidence for the audit period required by NERC, and Part 12 permanent records under 18 CFR 12.12.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the safety, risk, and reliability committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, and before the Piedmont integration goes live.
