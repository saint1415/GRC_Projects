# Regulatory Gap Analysis: Cris Santos Company | Dams | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects; NERC-registered GO and GOP; Hydro Services) |
| Tier / Vertical | Mid-Market / Dams |
| Primary program analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (March 30, 2016), applied to 1 Group 1, 2 Group 2, and 1 interconnected Group 3 dam, including Section 9 and Form 3. Source: https://www.ferc.gov/sites/default/files/2020-04/security.pdf, with the FERC Security Program FAQ |
| Other rules for the primary business line | 18 CFR Part 12 (eCFR version 2026-09-23); NERC CIP-002-5.1a, CIP-003-9, CIP-012-2, and EOP-004-4 (NERC standard PDFs); CEII, 18 CFR 388.113; Fla. Stat. 501.171 for employee personal information; CIRCIA (proposed only) |
| Assessment dates | 2026-06-29 to 2026-07-31 (Section 9 re-determination 2026-07-14 to 2026-07-16); evidence refreshed with P07 results through 2026-08-28 |
| Assessors | GRC Manager and NERC Compliance Manager, with the Corporate Security Manager, OT Security Manager, and Chief Dam Safety Engineer; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** hydroelectric generation at 4 FERC-licensed projects (73% of receipts), with RMOS and field services as a second line.

| Rule | Applies? | Basis |
|---|---|---|
| FERC Security Program (Rev. 3A) | **Yes, by Security Group** | The company is a FERC licensee; 18 CFR Part 12 applies to licensed projects, and the Regional Engineer supervises project "safety, stability, security, and integrity". FERC assigned BWB to **Group 1**, CDS and PNH to **Group 2**, and SGR to **Group 3** (letters in 2019, confirmed at the 2025-11-04 inspection). Group criteria are not public (Rev. 3A 3.3.1 to 3.3.3). Size does not matter; the group does |
| Section 9 (Computer Security and SCADA) | **Yes, at the Critical level** | Form 3 Questions 1-4 are Yes for BWB, CDS, and PNH, including interconnection with other dams through the ROC. Gate control at all three exceeds the Table 9.1c threshold of more than 60 people within 3 miles. BWB generation (180 MW) alone would be Operational (100 MW or more, under 1,500 MW, Table 9.1c note 2). The ROC SCADA is one cyber system, so the higher consequence governs (FAQ Q1). SGR is an interconnected Group 3 dam and must have the same level of protection (9.1.1.2 note; FAQ Q10). Baseline and enhanced measures and Form 3 Questions 5-33 apply |
| 18 CFR Part 12 | **Yes** | 12.10 reporting of conditions affecting project safety, which include gate misoperation, unusual instrument readings, and "security incidents (physical and/or cyber)" (12.3(b)(4)); EAPs; gate testing; Owner's Dam Safety Program |
| NERC CIP-002-5.1a | **Yes** | Registered GO and GOP. BWB (4 units of about 50 MVA, 180 MW) and CDS (2 units of about 46 MVA, 84 MW) are BES under Inclusion I2 (units over 20 MVA, or a plant over 75 MVA, connected at 100 kV or above; NERC BES Definition Reference Document, version 3). PNH and SGR (69 kV) are not BES |
| NERC CIP-003-9 | **Yes, low impact** | The ROC (Control Center, criterion 3.1), BWB and CDS (generation resources, criterion 3.3) contain low impact BES Cyber Systems. Nothing is medium or high: 264 MW of BES generation is below the 1,500 MW lines in criteria 2.1 and 2.11, no criterion 2.3 designation exists, and neither plant is a Blackstart Resource. CIP-003-9 Attachment 1 Section 6 (vendor electronic remote access) took effect 2026-04-01 |
| NERC CIP-012-2 | **Yes** | The ROC is a GOP Control Center that sends real-time data to the BA/TOP Control Center over ICCP. The co-location exemption (4.2.3) does not apply, because the data is about BWB and CDS, which are not co-located with the ROC. CIP-012-2, with new Parts 1.2 and 1.3, took effect 2026-07-01 |
| NERC EOP-004-4 | **Yes** | GO and GOP report damage or destruction of their Facility from intentional human action, and physical threats or suspicious devices or activity at their Facility (Attachment 1) |
| NERC CIP-004 to CIP-011, CIP-013, CIP-015 | **No** | High and medium impact only. CIP-008 reporting does not apply; low impact incident response and E-ISAC notice come from CIP-003-9 Attachment 1 Section 4 |
| NERC CIP-014-3 | **No** | Transmission Owners and Operators only |
| CEII (18 CFR 388.113) | **Yes, for FERC filings** | Defines CEII and sets the justification and marking rules when the company asks FERC to protect filed information. Internal handling is a FERC Security Program duty (3.2 OPSEC; Form 1 Q22) |
| Fla. Stat. 501.171 and other state laws | **Yes, for employee data** | 850 employees, a few living in Georgia and Alabama; notice follows the law of each state where affected individuals reside, with Florida as the worked example. RMOS client data is mostly operational, not personal information |
| CIRCIA | **No (proposed only)** | Final rule not published as of 2026-09-25; tracked in section 6 |

**Which revision.** Revision 3A is the latest version this analysis could confirm on ferc.gov. **Action:** the Corporate Security Manager confirms the current revision with the Regional Engineer before the 2026-11-10 inspection.

**What the 12.10 duty means for cyber.** A cyber event on gate or unit controls is a reportable condition even if no water was released. The report goes to the Regional Engineer as soon as practicable after discovery, preferably within 72 hours (12.10(a)(1)). That clock drives the P08 runbooks.

## 2. Method
1. **Requirements.** Rows follow each rule's own structure: Rev. 3A section 3.2 licensee responsibilities, the Group 1, 2, and 3 duties (3.3.1 to 3.3.3, Table 3.3.8), sections 4 to 8, each line of Tables 9.3a and 9.3b, the Form 3 questions not already covered, and three Form 1 items; Part 12 by section and paragraph; NERC standards by requirement and part; Florida by subsection. FERC, eCFR, and NERC texts were read in the primary documents; short phrases are quoted where the wording matters.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **These are author mappings.** NIST has not published a mapping for the FERC program or for these NERC standards. Rev. 3A Tables 9.3a and 9.3b cite NIST SP 800-82 sections; the mapping uses SP 800-82 Rev. 3 as the bridge.
3. **Evidence and sampling.** Interviews with all control owners; document review (VA, SAs, Security Plans, certification letters 2022-2025, EAPs, ODSP, CIP-002 and CIP-003 records, CIP-012 plan, EOP-004 Operating Plan); configuration exports; walkthroughs at all 4 projects and the ROC. Where a control operates often, a sample was tested:
   - jump host vendor sessions: 25 of 212 (July 2026);
   - transient asset log entries: 20 of 64;
   - walk-down logs: 20 days per site;
   - training records: 25 of 850 staff;
   - FERC filings marked CEII: 5 of 5 (2025);
   - certification letters: 4 of 4 (2022-2025);
   - OT and client contracts: 14 OT vendors and 4 RMOS clients (all);
   - card access reviews: 4 of 4 quarters.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FERC Sec. 3 (responsibilities and Security Group duties) | 8 | 10 | 0 | 1 | 19 |
| FERC Sec. 4 (threat notification and communications) | 1 | 2 | 0 | 0 | 3 |
| FERC Sec. 5 and 6 (Vulnerability and Security Assessments) | 1 | 2 | 0 | 0 | 3 |
| FERC Sec. 7 (Security Plans) | 3 | 4 | 0 | 0 | 7 |
| FERC Sec. 8 (annual certification letter) | 4 | 0 | 1 | 0 | 5 |
| FERC Sec. 9 and Form 3 (Computer security and SCADA) | 8 | 25 | 0 | 0 | 33 |
| FERC Appendix A Form 1 (physical checklist) | 0 | 3 | 0 | 0 | 3 |
| 18 CFR Part 12 | 3 | 4 | 0 | 0 | 7 |
| NERC CIP-002-5.1a | 2 | 0 | 0 | 0 | 2 |
| NERC CIP-003-9 | 9 | 2 | 0 | 1 | 12 |
| NERC CIP-012-2 | 1 | 2 | 2 | 0 | 5 |
| NERC EOP-004-4 | 2 | 0 | 0 | 0 | 2 |
| NERC CIP not applicable (CIP-004 to CIP-015) | 0 | 0 | 0 | 2 | 2 |
| CEII (18 CFR 388.113) | 1 | 0 | 0 | 0 | 1 |
| State breach law (Fla. Stat. 501.171) | 0 | 3 | 0 | 0 | 3 |
| CIRCIA (proposed) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **43** | **57** | **3** | **5** | **108** |

Of the 60 unmet or partially met rows, 1 is rated Very High, 25 High, 24 Moderate, and 10 Low. The FERC Security Program alone has 73 rows (25 Met, 46 Partially met, 1 Not met, 1 N/A).

**Reading the results.** This is a defined program with gaps in scale:
- **Physical security and the paperwork FERC inspects are largely sound.** Key control, law enforcement relations, Security Plan updates, VA and SA cycles, Part 12 reporting of physical conditions, and gate testing are met.
- **Section 9 is where the gaps cluster:** 25 of the 33 Section 9 and Form 3 rows are unmet or partially met. The jump hosts, ROC monitoring, and BWB recovery show the program works where it was applied; it was not extended to CDS, PNH, SGR, the OEMs, or the RMOS clients.
- **NERC low impact compliance is mostly met, with 6 gaps:** CIP-003-9 Section 3.1 at the ROC (client tunnel rules), Section 6.3 at CDS (new in 2026), and CIP-012-2 Parts 1.2 to 1.5 (new in 2026). The General Counsel decides on self-reporting the possible noncompliance by 2026-10-15.
- **The most sensitive finding concerns statements to FERC.** The 2024 and 2025 certification letters stated Section 9 compliance although the determinations had not been re-evaluated (G-035). The plan and schedule sent on 2026-09-30 includes a clarifying statement.

## 4. Priority gaps (Very High and High)
| Row | Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|---|
| G-058 | Two OEM paths outside control | Sec. 9.3 Table 9.3a (Access control: remote and third-party); Form 3 Q12a-12c | Very High | POAM-001 | OT Security Manager | 2026-11-30 |
| G-001 | Cyber program for OT matured only in 2026; Section 9 re-evaluation lapsed in 2024 and 2025 | Sec. 3.2 (bullet 1) | High | Adopt POL-01 to POL-05 and the SSP as the Cyber/SCADA Security Plan; add the annual Section 9 cycle to the compliance calendar | Vice President of Generation Operations | 2026-12-31 |
| G-008 | No link from a cyber event to EAP activation (gap 8) | Sec. 3.2 (bullet 10); Sec. 7.4.1 | High | Add cyber triggers to the 3 Internal Emergency Response sub-elements and 4 EAP flowcharts; joint exercise (POAM-008) | Chief Dam Safety Engineer | 2026-12-15 |
| G-020 | No cyber recovery content for the ROC SCADA that controls BWB | Sec. 3.3.1; Sec. 7.4.2; Table 3.3.8 | High | Add ROC SCADA and BWB control recovery after a cyber attack, using P05 and P08 (POAM-007) | Vice President of Generation Operations | 2026-12-15 |
| G-021 | SGR has no security documents and weak cyber measures although tied to Group 1 and 2 dams through the ROC | Sec. 3.3.3 | High | Light Security Assessment and Plan for SGR; cyber measures under Section 9 (POAM-001, POAM-003) | Corporate Security Manager | 2027-03-31 |
| G-035 | Section 9 compliance overstated in 2 letters | Sec. 8.0 (bullet 7) | High | Plan and schedule with a clarifying statement sent to the Regional Engineer 2026-09-30; accurate 2026 letter | Chief Dam Safety Engineer | 2026-12-31 |
| G-038 | Annual reassessment missed twice | Sec. 9.1.1; Table 9.1a; Form 3 Q1-4; FAQ Q8 | High | Annual Section 9 cycle each June in the compliance calendar (POAM-003) | OT Security Manager | 2027-06-30 |
| G-040 | No way to confirm client sites meet the baseline and enhanced measures; tunnels share the SCADA zone | Sec. 9.1.1.2 (note); Sec. 9.1.1.3; FAQ Q10 | High | Separate RMOS zone (POAM-002) and a client security schedule (POAM-009) | OT Security Manager | 2027-03-31 |
| G-041 | Measures not yet in place for the negative answers | Sec. 9.1.1.3; Form 3 Q5-33 | High | Execute the POA&M | OT Security Manager | 2027-09-30 |
| G-042 | Inventory incomplete at 3 projects (gap 1) | Sec. 9.2; Form 3 Q9a-9b, Q19a | High | Walkdowns and passive discovery at CDS, PNH, SGR (POAM-003) | OT Security Manager | 2026-12-31 |
| G-044 | Not all connections known or reviewed | Sec. 9.3 Table 9.3a (General: network connections) | High | Connection register for all sites, reviewed every 12 months (POAM-001) | OT Security Manager | 2026-11-30 |
| G-045 | Undocumented wireless path found (gap 13) | Sec. 9.3 Table 9.3a (General: wireless) and Table 9.3b (wireless); Form 3 Q13a-13b | High | Cellular signal survey at every panel; ban on cellular modems without approval (POAM-001) | OT Security Manager | 2026-11-30 |
| G-046 | Criticality review lapsed | Sec. 9.3 Table 9.3a (General: procedures and criticality review) | High | Covered by POAM-003 | OT Security Manager | 2027-06-30 |
| G-048 | External roles undefined | Sec. 9.3 Table 9.3a (Coordination: roles incl. outsourcers) | High | Security schedules for OEMs and clients (POAM-009) | GRC Manager | 2027-03-31 |
| G-050 | Flat WAN and shared SCADA zone (gap 2) | Sec. 9.3 Table 9.3a (System lifecycle: secure design) | High | OT zone architecture (POAM-002) | OT Security Manager | 2027-03-31 |
| G-051 | No OT patch cadence at the plants | Sec. 9.3 Table 9.3a (System lifecycle: configuration and patching); Form 3 Q15 | High | STD-07 OT patch standard; host replacement (POAM-006) | Manager of Controls Engineering | 2027-09-30 |
| G-053 | Recovery unproven at 3 plants and the ROC | Sec. 9.3 Table 9.3a (Restoration and recovery); Form 3 Q16 | High | POAM-007 | Manager of Controls Engineering | 2027-06-30 |
| G-054 | Monitoring and IR gaps (gaps 4 and 8) | Sec. 9.3 Table 9.3a (Intrusion detection and response) | High | POAM-005, POAM-008 | OT Security Manager | 2027-06-30 |
| G-056 | No segregation inside OT (gap 2) | Sec. 9.3 Table 9.3a (Access control and functional segregation: firewalls); Form 3 Q11a-11b, Q22 | High | POAM-002 | OT Security Manager | 2027-03-31 |
| G-059 | Shared and default credentials | Sec. 9.3 Table 9.3b (Access control: enhanced); Form 3 Q18h, Q21 | High | POAM-004, POAM-012, POAM-016 | OT Security Manager | 2026-12-31 |
| G-060 | 2 Critical sites never assessed | Sec. 9.3 Table 9.3b (Vulnerability assessment); Form 3 Q18i, Q31 | High | Assessments at CDS and PNH in 2026 Q4, then all Critical sites yearly (POAM-006) | OT Security Manager | 2026-12-31 |
| G-061 | 3 projects unmonitored | Form 3 Q14a-14c | High | POAM-005 | OT Security Manager | 2027-06-30 |
| G-071 | Electronic path into a gate PLC | Appendix A Form 1 Q6 | High | Modem removed; panel walkdowns (POAM-001) | OT Security Manager | 2026-10-31 |
| G-074 | Cyber events not recognized as reportable conditions (gap 8) | 18 CFR 12.10(a)(1); 12.3(b)(4)(ii), (viii), (xi) | High | Name cyber events in the ODSP, POL-03, and P08 (POAM-008) | Chief Dam Safety Engineer | 2026-10-31 |
| G-086 | ROC rules for client tunnels broader than necessary (possible noncompliance) | CIP-003-9 R2; Att. 1 Sec. 3.1 | High | Narrow client rules to client SCADA objects now; RMOS zone (POAM-002); General Counsel decides self-report by 2026-10-15 | NERC Compliance Manager | 2026-11-30 |
| G-092 | CDS vendor sessions not inspected (possible noncompliance) | CIP-003-9 R2; Att. 1 Sec. 6.3 | High | Extend inspection to CDS sessions; General Counsel self-report decision (POAM-001) | NERC Compliance Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01) and the POA&M (P07). The plan and schedule that Section 9.1.1.3 asks for is the P07 POA&M filtered to the Section 9 rows, sent to the Regional Engineer on 2026-09-30.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Contain** | 2026 Q4 | OEM VPNs moved to jump hosts; SGR modem removed and panels walked down; CDS vendor session inspection; client tunnel rules narrowed; CIP-012 plan updated; default passwords changed; restricted CEII library; accurate 2026 certification letter; cyber triggers in EAPs and Internal Emergency Response | G-008, G-035, G-044, G-045, G-058, G-071, G-072, G-073, G-074, G-086, G-092, G-096, G-097 |
| **2. Build** | 2027 Q1 | OT zone architecture with a separate RMOS zone; named HMI accounts; OEM and client security schedules; vulnerability assessments at CDS and PNH; Rapid Recovery update; SGR security documents | G-020, G-021, G-040, G-048, G-050, G-056, G-059, G-060 |
| **3. Prove** | 2027 Q2 | OT monitoring at CDS, PNH, SGR; restore tests at every plant and an ROC cyber recovery test; joint OT and EAP exercise with the FBI and county emergency management | G-053, G-054, G-061, G-066, G-078 |
| **4. Sustain** | 2027 Q3 onward | Annual Section 9 cycle each June; host replacement at PNH and SGR; SOC 2 Type 2 for RMOS; VA reprint by 2027-06-30 | G-011, G-038, G-046, G-051 |

Progress is reported to the audit committee each quarter as the count of rows moving to Met, and to the Regional Engineer as plan and schedule status at each inspection.

## 6. Pending regulatory changes
- **FERC Security Program:** no newer revision confirmed (section 1). Recheck before each inspection.
- **NERC CIP:** approved future revisions (from `requirements.csv`, NERC bulletin): virtualization revisions including CIP-002-8 and CIP-003-10 effective 2028-07-01 (FERC Order No. 919); CIP-003-11 effective 2029-07-01 (FERC Order No. 918); CIP-015-1 internal network security monitoring effective 2028-10-01, for high and medium impact only. None changes the low impact status of these assets as currently drafted; the NERC Compliance Manager tracks implementation plans.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226): final rule not published as of 2026-09-25, so reporting to CISA is voluntary. The proposed rule has no dams-specific criterion; the company exceeds the SBA size standard and is a NERC-registered entity, so it would likely be in scope if the rule is finalized as proposed. Recheck when the final rule appears.

The `pending_rule_change` column records this per row. None of these is treated as a current obligation.
