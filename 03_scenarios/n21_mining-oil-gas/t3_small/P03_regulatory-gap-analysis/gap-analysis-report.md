# Regulatory Gap Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, NAICS 211120) |
| Tier / Vertical | Small / Mining, Quarrying, and Oil and Gas Extraction |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to OT with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023). **Voluntary benchmark: no binding federal sector cybersecurity rule applies** (section 1) |
| Secondary regulation | Florida Information Protection Act, Fla. Stat. 501.171 (binding): data security, breach notice, and third-party agent duties for royalty owner and employee personal information |
| Assessment dates | 2026-07-13 to 2026-07-24 (OCC and field walkthroughs 2026-07-15 and 2026-07-16) |
| Assessors | IT Manager with the SCADA and Automation Supervisor; applicability reviewed with outside counsel |
| Workbook | `gap-analysis.csv` (116 rows) |
| Regulatory driver label | `N21-BM` in the other deliverables points to this benchmark (see `../scenario-facts.md` section 5) |

## 1. Applicability
The vertical's research names three candidate federal requirements (`02_verticals/n21_mining-oil-gas/requirements.csv`). **None of them applies to this company today.** Each was checked against the rule text; the result is recorded as a Not applicable row in `gap-analysis.csv` (G-113 to G-116).

| Requirement | Applicability test (rule text) | Decision for Cris Santos Company |
|---|---|---|
| **N21-R01** USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F | 101.605(a): "the owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106." There is no size threshold | **Not applicable.** All operations are onshore in Florida. The company owns no vessel, no MTSA-regulated waterfront facility, and no Outer Continental Shelf facility, so it has no security plan under parts 104 to 106. The related duty to report cyber incidents to the Coast Guard (33 CFR 6.16-1) concerns vessels, harbors, ports, and waterfront facilities and does not reach inland well sites either |
| **N21-R02** TSA Security Directive Pipeline-2021-02G | Applies to owners and operators of hazardous liquid and natural gas pipelines or LNG facilities that TSA has notified are critical | **Not applicable.** The company operates no pipeline. Crude is sold at the lease and leaves in the purchaser's tank trucks, and gas is sold at the lease meter into a third party's gathering system. TSA has not notified the company |
| **N21-R03** CIRCIA, proposed 6 CFR Part 226 | Proposed 226.2: an entity in a critical infrastructure sector that (a) exceeds the SBA size standard for its NAICS code, or (b) meets a sector-based criterion | **Not applicable, and not in effect.** The final rule had not been published as of 2026-09-25, so there is no current duty. Even as proposed: the company has 250 employees against the 1,250-employee standard for NAICS 211120 (13 CFR 121.201), so it does not exceed the standard; and it meets none of the sector criteria that could reach an oil producer (MTSA facility, (b)(15); TSA-identified pipeline, (b)(14)(iv); NERC CIP or OE-417 reporting, (b)(6)). Voluntary reporting to CISA is planned in P08 |

**Other federal rules screened and excluded:**
- **PHMSA pipeline safety, 49 CFR Part 195**, including control room management (195.446): Part 195 excludes transportation through "onshore production (including flow lines)" facilities (195.1(b)(8)) and transportation by tank truck (195.1(b)(9)(i)). The company's piping is all production facility piping, so its SCADA control room is not a pipeline control room under 195.446(a).
- **BSEE** (offshore oil and gas) does not reach onshore operations. **MSHA** has no cybersecurity rules. **DOE** is the sector risk management agency and issues guidance, not rules.

**Why a voluntary benchmark.** With no binding sector rule, the company's cybersecurity obligations come from general law (the Florida statute below, and the FTC Act for any security representations the company makes), its contracts (lender, insurer, partners), and its own safety and environmental duties. The company chose NIST CSF 2.0 as the structure because it is sector-neutral and because the reserve-based lender's and the cyber insurer's security questionnaires are organized around it. SP 800-82 Rev. 3 supplies the OT-specific practices: segmentation and architecture (section 5), OT program content (section 3), and OT guidance for each framework category (section 6).

**Secondary regulation: Fla. Stat. 501.171 applies.** The company is a "covered entity" (a commercial entity that "acquires, maintains, stores, or uses personal information", 501.171(1)(b)). It holds personal information of about 2,300 royalty owners (names with Social Security numbers) and 250 employees (Social Security numbers, driver license numbers, health plan identifiers, and vehicle location history, which the 2026 statute lists as "information regarding an individual's geolocation"). Subsections (2) to (6) apply. Subsection (8), disposal of "customer records", does not apply because the company has no consumer customers (501.171(1)(c)); the same disposal rules are applied voluntarily through POL-04.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core. The Florida rows follow the statute's subsections.
2. **OT guidance.** Each CSF row cites the SP 800-82 Rev. 3 section used to judge the OT side (column `sp800_82r3_reference`). SP 800-82 Rev. 3 organizes its framework guidance by CSF 1.1 categories (section 6), so the link from each CSF 2.0 subcategory to an SP 800-82 section is an **author mapping**.
3. **Crosswalk.** SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of the key controls from that official list. Florida rows use an author mapping.
4. **Evidence.** Interviews (CFO, VP Operations, IT Manager, SCADA and Automation Supervisor, Network Administrator, Production Accounting Manager, HR Manager, 4 Production Controllers, 2 automation technicians, the SCADA integrator's lead engineer), document review, the IT/OT firewall rule export, SCADA account lists, and walkthroughs of the OCC, 2 tank batteries, the injection plant, and 3 well pads.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| GOVERN (GV), 31 subcategories | 5 | 18 | 8 | 0 |
| IDENTIFY (ID), 21 | 3 | 9 | 9 | 0 |
| PROTECT (PR), 22 | 3 | 17 | 2 | 0 |
| DETECT (DE), 11 | 0 | 7 | 4 | 0 |
| RESPOND (RS), 13 | 0 | 11 | 2 | 0 |
| RECOVER (RC), 8 | 1 | 5 | 2 | 0 |
| **CSF 2.0 subtotal (106)** | **12** | **67** | **27** | **0** |
| Fla. Stat. 501.171 (6) | 0 | 4 | 1 | 1 |
| Applicability screen (4) | 0 | 0 | 0 | 4 |
| **Total (116)** | **12** | **71** | **28** | **5** |

Of the 99 unmet or partially met rows, 6 are rated High, 44 Moderate, 47 Low, and 2 Very Low.

**Reading the pattern.** Governance and risk assessment are now documented (the 2026 work created them), but the company has almost no OT-specific protection, detection, or recovery capability. The corporate side is in better shape than the SCADA side: MFA, EDR, and patching exist in IT, while the OT side has shared accounts, an unsupported operating system, no monitoring, and backups in the same room as the servers.

## 4. Priority gaps and roadmap
| Gap | Benchmark reference | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Vendor remote access without MFA or logging; shared SCADA accounts | PR.AA-01, PR.AA-03, DE.CM-06; SP 800-82r3 6.2.1, 6.2.10 | High | Jump host with named accounts, MFA, and session recording; named HMI accounts | IT Manager; SCADA and Automation Supervisor | 2026-11-30 |
| Weak IT/OT segmentation; internet-exposed modems | PR.IR-01; SP 800-82r3 5.2.3 | High | OT DMZ; firewall rule clean-up; retire the dual-homed workstation; private network for all modems | SCADA and Automation Supervisor | 2027-01-31 (modems 2026-09-30) |
| Backups not isolated or tested | PR.DS-11, RC.RP-03; SP 800-82r3 6.2.4, 6.5.1 | High | Offline SCADA copies; separate immutable cloud backups; quarterly restore test | SCADA and Automation Supervisor | 2026-12-31 (first restore test 2026-10-30) |
| No OT change control | ID.RA-07, PR.PS-01; SP 800-82r3 6.2.4 | Moderate | Change requests, peer review, program repository | SCADA and Automation Supervisor | 2026-12-31 |
| No monitoring of the SCADA network; short log retention | DE.CM-01, PR.PS-04, DE.AE-03; SP 800-82r3 6.3.2 | Moderate | Passive OT monitoring sensor; central logs with 1-year retention; 24x7 MDR | IT Manager | 2027-03-31 |
| Unsupported SCADA operating system | PR.PS-02, ID.AM-08; SP 800-82r3 6.2.11 | Moderate | Upgrade with the integrator | SCADA and Automation Supervisor | 2027-03-31 |
| No OT asset inventory or network diagram | ID.AM-01 to ID.AM-03; SP 800-82r3 6.1.1 | Moderate | OT inventory from passive monitoring and site survey; IT/OT data flow diagram | SCADA and Automation Supervisor | 2027-01-31 |
| Incident plan untested and not tied to manual operations | ID.IM-04, RS.MI-01; SP 800-82r3 3.3.8 | Moderate | Joint tabletop; practice SCADA isolation | IT Manager | 2026-11-30 |
| No supplier security terms | GV.SC-01, GV.SC-02, GV.SC-05; Fla. Stat. 501.171(6) | Moderate | Security schedule and breach notice clause at renewal | CFO | 2027-03-31 |
| Royalty owner data unprotected in exports | PR.DS-01; Fla. Stat. 501.171(2) | Moderate | Secure transfer; remove exports from the shared area | Production Accounting Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Sequencing.** The first quarter is spent on the access path (remote access and modems) and the way back (backups), because those close the three High risks in P01 for the least money. Segmentation and monitoring follow in 2027 Q1, because the OT DMZ design depends on the network diagram and asset inventory.

## 5. Pending regulatory changes
None of these is a current obligation. The `pending_rule_change` column flags the affected rows.
- **CIRCIA final rule (N21-R03).** Not published as of 2026-09-25. If the final rule keeps the proposed size test and sector criteria, the company stays outside it. If CISA adds an oil and gas production criterion or changes the size test, the company would face 72-hour incident reports and 24-hour ransom payment reports to CISA. The IT Manager rechecks when the final rule is published (GV.OC-03).
- **TSA surface cyber risk management rule** (NPRM Nov. 7, 2024; not final). Relevant only if the company ever acquires or operates a pipeline that TSA designates.
- **Business changes that would change applicability:** buying a gathering or transmission pipeline (PHMSA Part 195 and possibly TSA), acquiring offshore or waterfront assets (USCG Subpart F), or growing past 1,250 employees (the proposed CIRCIA size test).
