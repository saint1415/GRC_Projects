# Regulatory Gap Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system, NAICS 211120) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to OT with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023). **Voluntary benchmark: no binding federal sector cybersecurity rule applies** (section 1) |
| Binding rules analyzed | 49 CFR Part 195 for the gathering system (regulated rural gathering line requirements in 195.11 and the Subpart B reporting duties, cyber-relevant parts); Fla. Stat. 501.171 as the state law worked example; other states' breach laws generically |
| Assessment dates | 2026-07-06 to 2026-07-31 (walkthroughs: Panhandle and OCC 2026-07-14 and 2026-07-15; South Florida 2026-07-16; Alabama and BCC 2026-07-17); evidence refreshed with P07 results through 2026-08-21 |
| Assessors | GRC Analyst and Security Manager, with the OT Security Engineer and the Pipeline Compliance Manager; applicability reviewed by the General Counsel; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-16 |
| Workbook | `gap-analysis.csv` (125 rows) |
| Regulatory driver labels | `N21-BM` points to the benchmark rows and `N21-P195` to the Part 195 rows (see `../00_company-facts.md` section 5) |

## 1. Applicability
**Primary business line:** crude oil production in 3 onshore operating areas, with a Panhandle gathering system that carries the company's and 5 shippers' crude to a third-party transmission pipeline.

The vertical's research names three candidate federal cyber requirements (`02_industry-rules/mining-oil-gas/requirements.csv`). **None of them applies to this company today.** Each was checked against the rule text; the result is recorded as a Not applicable row in `gap-analysis.csv` (G-122 to G-124).

| Requirement | Applicability test (rule text) | Decision for Cris Santos Company |
|---|---|---|
| **N21-R01** USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F | 101.605(a): owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106. No size threshold | **Not applicable.** All operations are onshore in Florida and Alabama. No vessel, no MTSA-regulated waterfront facility, no OCS facility |
| **N21-R02** TSA Security Directive Pipeline-2021-02G | Owners and operators of hazardous liquid and natural gas pipelines or LNG facilities that TSA has notified are critical | **Not applicable today.** The company does operate a crude gathering system, so this is a live question at this size, unlike the smaller samples. TSA has not notified the company, and General Counsel confirmed on 2026-07-22 that no notice was received. A notice would make the directive apply; the quarterly regulatory watch (G-003) checks for one |
| **N21-R03** CIRCIA, proposed 6 CFR Part 226 | Proposed 226.2: a critical infrastructure entity that (a) exceeds the SBA size standard for its NAICS code, or (b) meets a sector-based criterion | **Not applicable, and not in effect.** No final rule as of 2026-09-25. As proposed: 850 employees is below the 1,250-employee standard for NAICS 211120 (13 CFR 121.201), so the size test is not met, and no sector criterion that could reach an oil producer is met (MTSA facility, (b)(15); TSA-identified pipeline, (b)(14)(iv); NERC CIP or OE-417 reporting, (b)(6)). Growth past 1,250 employees or a TSA notice would change this |

**Binding rule that does apply: 49 CFR Part 195 for the gathering system.** Part 195 covers onshore gathering lines used to transport petroleum when they are regulated rural gathering lines (195.1(a)(4)(ii)), and requires every other gathering line to meet the Subpart B reporting requirements (195.1(a)(5), 195.15). The text was verified on eCFR (2026-09-23 version):
- **Regulated rural gathering line (195.11(a)):** an onshore gathering line in a rural area with a nominal diameter from 6 5/8 to 8 5/8 inches, located in or within one-quarter mile of an unusually sensitive area (195.6), operating above 20% of specified minimum yield strength (or above 125 psi gage where the stress level is unknown). The company's **14-mile 8-inch trunk line** meets all three criteria because it runs within one-quarter mile of a drinking water unusually sensitive area.
- **Requirements that apply to it (195.11(b)):** written procedures; segment identification; design and construction rules for lines changed after July 3, 2009; Subpart B reporting; MOP under 195.406; line markers; public education (195.440); damage prevention (195.442); corrosion control; an internal corrosion program; and operator qualification processes (195.505). Record retention follows 195.11(d).
- **Reporting-regulated-only lines (195.15):** the other **78 miles** must meet the annual, accident, and safety-related condition reporting requirements of Subpart B, except the immediate telephone notice (195.52) and certain other reports (195.15(c)(2)).
- **What does not apply:** 195.11(b) does not list control room management (195.446) or the procedural manual (195.402), and the gathering lines are not transmission lines. Production facilities and flow lines (195.1(b)(8)) and tank truck movements (195.1(b)(9)(i)) are excluded. The company applies parts of 195.446 and 195.402(e) voluntarily (G-125).

Only the **cyber-relevant** Part 195 duties are analyzed (G-107 to G-114): segment identification, MOP, operator qualification, the 1-hour telephone notice and release estimate, accident and annual reports, and record retention. Line markers, public education, damage prevention, and corrosion control are pipeline safety programs with no cyber dependency and are audited by the Pipeline Compliance Manager's own program.

**State law.** The company is a "covered entity" under Fla. Stat. 501.171(1)(b) and holds personal information of about 14,000 royalty owners (names with Social Security or taxpayer numbers, bank account numbers) and 850 employees (Social Security, driver license, and health plan numbers, and vehicle location history). Subsections (2) to (6) apply (G-115 to G-119). Subsection (8), disposal of "customer records", does not apply because the company has no consumer customers (501.171(1)(c)); the same disposal rules are applied voluntarily through POL-04 (G-120). Owners live in more than 40 states, so the law of each state where affected individuals reside also applies; it is handled generically with Florida as the worked example (G-121).

**Other rules screened and excluded:** BSEE (offshore) does not reach onshore operations; MSHA has no cybersecurity rules; DOE is the sector risk management agency and issues guidance, not rules. EPA and state oil discharge, spill, and air rules are operational duties; the one that bears on cyber-physical safety, the oil discharge notice (40 CFR 110.6), is handled in the P08 notification matrix.

**Why a voluntary benchmark as the primary structure.** With no binding sector cyber rule, the company's cybersecurity obligations come from general law (state breach laws, the FTC Act for any security representations), Part 195's safety and reporting duties for the gathering system, and its contracts (gathering agreements, bank group, insurer, partners). NIST CSF 2.0 is sector-neutral, and the bank group's and insurer's questionnaires are organized around it. SP 800-82 Rev. 3 supplies the OT practices: segmentation and architecture (section 5), OT program content (section 3), and OT guidance for each framework category (section 6).

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core. Part 195 rows follow the sections of the rule; state rows follow the statute's subsections.
2. **OT guidance.** Each CSF row cites the SP 800-82 Rev. 3 section used to judge the OT side (column `sp800_82r3_reference`). SP 800-82 Rev. 3 organizes its framework guidance by CSF 1.1 categories (section 6), so the link from each CSF 2.0 subcategory to an SP 800-82 section is an **author mapping**.
3. **Crosswalk.** SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of the key controls from that official list. Part 195 and state rows use an author mapping.
4. **Evidence.** Interviews (COO, VP Operations, VP IT, Security Manager, OT Security Engineer, SCADA and Automation Manager, Control Room Manager, Pipeline Compliance Manager, Measurement Supervisor, Production Accounting Director, HR Director, General Counsel, the 3 Field Superintendents, 4 Production Controllers, 6 automation technicians, and the SCADA integrator's lead engineer), document review, firewall and account exports, and walkthroughs of the OCC, the BCC, the South Florida office, the Panhandle Central Facility and pump station, 4 tank batteries, 2 injection plants, 2 compression stations, and 6 well pads.
5. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, using the co-sourced internal audit firm's attribute sampling table (25 items for a control that operates many times a year, 15 for weekly or monthly controls). Each `evidence` cell names the sample and its result:
   - terminations: 25 of 96 (4 still active in SCADA local accounts);
   - new hires: 25 of 110 (all background-checked);
   - Panhandle CAB changes: 15 of 44 (all approved);
   - South Florida and Alabama controller changes from work orders: 20 of 58 (13 without a change record);
   - contracts with system or data access: 20 of 64 (9 with security terms);
   - privileged accounts: 25 of 38 (all with MFA);
   - jump host sessions in July 2026: 25 of 212 (all recorded and approved);
   - backup job days: 31 of 31 (July 2026);
   - incidents: 10 of 31 (all triaged);
   - OT devices at 6 sampled pads: 41 found, 12 missing from the area spreadsheets;
   - OQ qualification records: 15 (all current).
6. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| GOVERN (GV) | 13 | 18 | 0 | 0 | 31 |
| IDENTIFY (ID) | 5 | 16 | 0 | 0 | 21 |
| PROTECT (PR) | 4 | 18 | 0 | 0 | 22 |
| DETECT (DE) | 1 | 10 | 0 | 0 | 11 |
| RESPOND (RS) | 5 | 8 | 0 | 0 | 13 |
| RECOVER (RC) | 2 | 6 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **30** | **76** | **0** | **0** | **106** |
| 49 CFR Part 195 (gathering system, cyber-relevant) | 5 | 3 | 0 | 0 | 8 |
| Fla. Stat. 501.171 | 1 | 4 | 0 | 1 | 6 |
| Other states' breach laws (generic) | 0 | 1 | 0 | 0 | 1 |
| Applicability screen | 0 | 0 | 0 | 4 | 4 |
| **Total** | **36** | **84** | **0** | **5** | **125** |

**Gap risk ratings (84 rows Partially met):** 1 Very High, 11 High, 40 Moderate, 32 Low.

**Reading the pattern.** The company has a defined program: governance, risk management, MFA, EDR with 24x7 MDR, isolated cloud backups, and an OT DMZ are in place, so most GOVERN rows are Met and no row is Not met. Almost every gap is a **gap in scale**: a control that works at the OCC and in the Panhandle but not at the South Florida office, the BCC, Alabama field sites, or vendor paths. DETECT has the weakest result because OT monitoring covers only 2 locations and only business hours. The Part 195 duties that do not depend on systems are Met; the two that depend on SCADA data and on recognizing a cyber-caused event (the 1-hour notice and the release estimate) are not yet fully supported.

## 4. Priority gaps
| Gap | Benchmark or rule reference | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| BCC and South Florida reach the OCC around the OT DMZ; vendor gateways outside any boundary | PR.IR-01 (G-071); SP 800-82r3 5.2.3 | Very High | Extend the OT DMZ pattern; close vendor paths | OT Security Engineer | 2027-03-31 |
| Packager gateways and flow computer modem without MFA or logging; 2 reachable from the internet | PR.AA-03 (G-055), DE.CM-06 (G-078); SP 800-82r3 6.2.10 | High | Block internet access; all vendor access through the jump host | OT Security Engineer | 2026-10-31 (block), 2026-11-30 (jump host) |
| Shared engineering account on South Florida and BCC HMIs | PR.AA-01 (G-053); SP 800-82r3 6.2.1 | High | Named accounts from the OT directory | SCADA and Automation Manager | 2027-03-31 |
| Offline SCADA images reachable from the network; image restore never tested | PR.DS-11 (G-064), RC.RP-03 (G-101); SP 800-82r3 6.2.4, 6.5.1 | High | Second offline set with no network path; quarterly image restore | SCADA and Automation Manager | 2027-01-31 |
| BCC failover never fully tested; no OT or crisis management exercises | PR.IR-03 (G-073), ID.IM-02 (G-050); SP 800-82r3 5.3.2 | High | Failover test twice a year; OT and crisis management tabletops | Control Room Manager; Security Manager | 2027-04-30 |
| Field controller and flow computer changes not controlled | ID.RA-07 (G-045); SP 800-82r3 6.2.4 | High | Extend the CAB and repository to all areas | SCADA and Automation Manager | 2027-03-31 |
| Unsupported OS at the BCC and South Florida | PR.PS-02 (G-066); SP 800-82r3 6.2.11 | High | Upgrade with the SCADA vendor | SCADA and Automation Manager | 2027-03-31 |
| No OT monitoring outside the Panhandle; OT alerts not watched after hours | DE.CM-01 (G-075), DE.AE-02 (G-080); SP 800-82r3 6.3.1, 6.3.2 | High | Sensors at 3 locations; OT in the MDR contract | OT Security Engineer; Security Manager | 2027-06-30 |
| Cyber-caused events not linked to the 1-hour notice; release estimate depends on SCADA data | 49 CFR 195.52(a)-(d) (G-110, G-111) | Moderate | Cross-reference the runbooks and emergency procedure; manual fallback for the estimate | Pipeline Compliance Manager | 2026-12-31 |
| Owner deck copy with Social Security numbers in the data platform; tax files by email | Fla. Stat. 501.171(2) (G-115); PR.DS-01 (G-063) | Moderate | De-identified extract; secure transfer | Production Accounting Director | 2026-12-31 |
| OT vendors unassessed; gathering agreements without data terms | GV.SC-04 to GV.SC-08 (G-025 to G-029) | Moderate | Tier and assess OT vendors; amend agreements | General Counsel; GRC Analyst | 2027-06-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Close the doors** | 2026 Q4 | Packager gateways off the internet and behind the jump host; flow computer modem removed; owner deck copy de-identified; tabletops (OT, crisis management, pipeline notice); interim rule reduction at the BCC and South Florida | PR.AA-03, DE.CM-06, PR.DS-01, ID.IM-04, G-110, Fla. Stat. 501.171(2) |
| **2. Extend the Panhandle model** | 2027 Q1 | OT DMZ at the BCC and South Florida; upgrade of the BCC server and South Florida HMIs; named HMI accounts; CAB and repository for all areas; offline image vault and first image restore | PR.IR-01, PR.PS-02, PR.AA-01, ID.RA-07, PR.DS-11, RC.RP-03 |
| **3. Prove recovery and see everything** | 2027 Q2 | First full BCC failover test (before hurricane season); OT sensors in South Florida, Alabama, and the BCC with 24x7 MDR coverage; complete OT inventory; SOC 2 observation period starts 2027-04-01 (P09) | PR.IR-03, ID.IM-02, DE.CM-01, DE.AE-02, ID.AM-01 |
| **4. Sustain** | 2027 Q3 to Q4 | Annual risk assessment (July 2027); OT vendor assessments; gathering agreement amendments; repeat this benchmark review | GV.SC-04 to GV.SC-08, GV.OV-03 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met to Met.

## 6. Pending regulatory changes
None of these is a current obligation. The `pending_rule_change` column flags the affected rows.
- **CIRCIA final rule (N21-R03).** Not published as of 2026-09-25. If the final rule keeps the proposed size test and sector criteria, the company stays outside it unless it grows past 1,250 employees or receives a TSA notice. If it applied, the company would face 72-hour incident reports and 24-hour ransom payment reports to CISA. General Counsel rechecks when the final rule is published (GV.OC-03).
- **TSA surface cyber risk management rule** (NPRM Nov. 7, 2024; not final) and **a TSA notice under the pipeline security directives.** Either would bring the company's gathering system into TSA's cybersecurity requirements. The roadmap above (segmentation, vendor access, monitoring, recovery testing) moves in the same direction as those requirements, so a notice would mostly change deadlines and documentation.
- **Business changes that would change applicability:** a new unusually sensitive area along the gathering system (195.11(c) gives 6 months to comply for a newly regulated segment), larger-diameter or transmission pipe, acquisitions of offshore or waterfront assets (USCG Subpart F), or growth past 1,250 employees (the proposed CIRCIA size test).
