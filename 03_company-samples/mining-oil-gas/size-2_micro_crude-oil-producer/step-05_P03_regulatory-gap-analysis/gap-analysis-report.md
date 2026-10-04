# Regulatory Gap Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent crude oil producer, one field, NAICS 211120) |
| Tier / Vertical | Micro / Mining, Quarrying, and Oil and Gas Extraction |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to OT with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (September 2023). **Voluntary benchmark: no binding federal sector cybersecurity rule applies** (section 1) |
| Secondary regulation | Florida Information Protection Act, Fla. Stat. 501.171 (binding): data security, breach notice, and third-party agent duties for royalty owner and employee personal information |
| Assessment dates | 2026-07-20 to 2026-07-31 (field walkthrough 2026-07-22). Rows G-055 (PR.AA-03) and G-071 (PR.IR-01) updated 2026-08-12 with the P07 remote desktop finding |
| Assessors | Office Manager (Security Coordinator) and Field Superintendent, with the MSP lead technician; applicability reviewed with the insurer's panel counsel |
| Approved | 2026-08-31 by the Owner |
| Workbook | `gap-analysis.csv` (116 rows) |
| Regulatory driver label | `N21-BM` in the other deliverables points to this benchmark (see `../00_company-facts.md` section 5) |

## 1. Applicability
The vertical's research names three candidate federal requirements (`02_industry-rules/mining-oil-gas/requirements.csv`). **None of them applies to this company.** Each was checked against the rule text and recorded as a Not applicable row in `gap-analysis.csv` (G-113 to G-116).

| Requirement | Applicability test (rule text) | Decision for Cris Santos Company |
|---|---|---|
| **N21-R01** USCG Cybersecurity in the Marine Transportation System, 33 CFR Part 101, Subpart F | 101.605(a): owners and operators of U.S.-flagged vessels, facilities, and OCS facilities required to have a security plan under 33 CFR parts 104, 105, and 106. No size threshold | **Not applicable.** One onshore field in the Florida Panhandle. No vessel, no MTSA-regulated waterfront facility, no OCS facility, so no security plan under parts 104 to 106 |
| **N21-R02** TSA Security Directive Pipeline-2021-02G | Owners and operators of hazardous liquid and natural gas pipelines or LNG facilities that TSA has notified are critical | **Not applicable.** The company operates no pipeline. Crude leaves in the purchaser's tank trucks, and associated gas is burned on the lease. TSA has not notified the company |
| **N21-R03** CIRCIA, proposed 6 CFR Part 226 | Proposed 226.2: an entity in a critical infrastructure sector that exceeds the SBA size standard for its NAICS code, or meets a sector-based criterion | **Not applicable, and not in effect.** The final rule had not been published as of 2026-09-25. Even as proposed, 7 employees is far below the 1,250-employee standard for NAICS 211120 (13 CFR 121.201), and the company meets none of the sector criteria that could reach an oil producer (MTSA or OCS facility, TSA-identified pipeline). Voluntary reporting to CISA is planned in P08 |

**Other federal rules screened and excluded (G-116):**
- **PHMSA hazardous liquid pipeline safety, 49 CFR Part 195:** Part 195 does not apply to transportation "through onshore production (including flow lines)" facilities (195.1(b)(8)) or by tank truck (195.1(b)(9)(i)). All of the company's piping is production facility piping and flow lines.
- **PHMSA gas pipeline safety, 49 CFR Part 192:** onshore gathering is outside Part 192 unless it is a regulated onshore gathering line (192.1(b)(4)), and gathering cannot begin upstream of the end of the production operation (192.8(a)(1)). The company's associated gas is used as lease fuel in the heater-treater and never leaves the production operation, so it has no gathering line.
- **BSEE** (offshore oil and gas) does not reach onshore operations. **MSHA** has no cybersecurity rules. **DOE** is the sector risk management agency and issues guidance, not rules.
- **EPA and state spill rules** matter only where a SCADA failure could cause a release. The oil discharge notice (40 CFR 110.6) is carried into the P08 notification matrix; it is not analyzed row by row here.

**Why a voluntary benchmark at this size.** With no binding sector rule, the company's cybersecurity duties come from Florida law, its contracts (the cyber insurance policy, the seismic data license, the joint operating agreements), and its own safety and environmental duties. The company chose NIST CSF 2.0 because the larger partner's questionnaire and the insurer's application follow it, and SP 800-82 Rev. 3 for the OT side: architecture (section 5), OT program content (section 3), and OT guidance for each framework category (section 6). For a 7-person company the benchmark is applied in proportion: most remediation actions are one-page procedures, MSP settings, or one small firewall, not new systems.

**Secondary regulation: Fla. Stat. 501.171 applies, but only in part at this size.** The company is a "covered entity" (a commercial entity that acquires, maintains, stores, or uses personal information, 501.171(1)(b)). It holds names with Social Security numbers and bank account numbers of about 140 royalty owners, and Social Security, driver license, and health plan numbers of 7 employees.
- **Applies:** (2) reasonable security measures; (4) notice to each affected Florida resident within 30 days of determination; (6) third-party agents (the production accounting vendor, the payroll service, and the MSP through the cloud backup) must notify the company within 10 days.
- **Not triggered at this size:** (3) Department of Legal Affairs notice needs 500 or more affected Floridians, and the company holds data on about 97; (5) consumer reporting agency notice needs more than 1,000 individuals notified at once.
- **Not applicable:** (8) disposal of "customer records", because the company has no consumer customers (501.171(1)(c)). The same disposal rules are applied voluntarily through POL-04.

## 2. Method
1. **Requirements.** Every CSF 2.0 subcategory (106) is one row, quoted from the CSF 2.0 core. The Florida rows follow the statute's subsections.
2. **OT guidance.** Each CSF row cites the SP 800-82 Rev. 3 section used to judge the OT side (column `sp800_82r3_reference`). SP 800-82 Rev. 3 organizes its framework guidance by CSF 1.1 categories (section 6), so the link from each CSF 2.0 subcategory to an SP 800-82 section is an **author mapping**, reused from the Small sample for this vertical.
3. **Crosswalk.** SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), kept in full in column `nist_official_sp800_53r5`. Column `sp800_53_controls` is the author's selection of the key controls from that list. Florida and screening rows use an author mapping.
4. **Documentary evidence.** Each status rests on a named document or record: the MSP device list, patch report, antivirus export, encryption report, and backup job report; the suite user export and sharing report; the production accounting role report; the SCADA account list and event log sample; the mobile viewer user list; the emergency response plan; the contracts and the insurance application; and the walkthrough of the field office, tank battery, SWD facility, and 3 well sites on 2026-07-22. Interviews covered all 7 staff, the MSP lead technician, and the SCADA integrator's technician.
5. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**, except the two rows updated on 2026-08-12. Actions completed later (policies and designations approved 2026-08-31, the SOC 2 review on 2026-08-20) are noted in the remediation column but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| GOVERN (GV), 31 subcategories | 3 | 8 | 20 | 0 |
| IDENTIFY (ID), 21 | 3 | 9 | 9 | 0 |
| PROTECT (PR), 22 | 1 | 15 | 5 | 1 |
| DETECT (DE), 11 | 0 | 3 | 8 | 0 |
| RESPOND (RS), 13 | 0 | 3 | 10 | 0 |
| RECOVER (RC), 8 | 0 | 3 | 5 | 0 |
| **CSF 2.0 subtotal (106)** | **7** | **41** | **57** | **1** |
| Fla. Stat. 501.171 (6) | 0 | 1 | 2 | 3 |
| Applicability screen (4) | 0 | 0 | 0 | 4 |
| **Total (116)** | **7** | **42** | **59** | **8** |

Of the 101 unmet or partially met rows, 4 are rated High, 39 Moderate, 57 Low, and 1 Very Low.

**Reading the pattern.** The only areas that score well are the ones this engagement created (the risk analysis and the BIA) and the ones the SaaS vendors supply (sign-in assertions, encryption, MFA where enforced). GOVERN scores worst because nothing was written down before August 2026: no named security role, no policies, no supplier terms. PROTECT is mostly "Partially met" because the office side has MFA, MSP patching, and encryption while the field side has a flat network, shared logins, and an unsupported SCADA host. DETECT, RESPOND, and RECOVER are mostly "Not met": there was no monitoring, no incident plan, and no tested restore.

## 4. Priority gaps
| Gap | Benchmark reference | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Vendor and remote access without MFA; remote desktop exposed until 2026-08-11 | PR.AA-03, PR.IR-01; SP 800-82r3 6.2.10, 5.2.3 | High | Company-enabled vendor sessions with MFA; MFA on the mobile viewer and backup console; quarterly external scan | Field Superintendent | 2026-10-31 |
| Flat field office network | PR.IR-01; SP 800-82r3 5.2.3 | High | Small firewall separating the SCADA host and radio base; remove the remote desktop shortcut | Field Superintendent | 2026-11-30 |
| SCADA backup not isolated; never restore-tested | PR.DS-11, RC.RP-03; SP 800-82r3 6.2.4, 6.5.1 | High | Rotated encrypted drives, one off site; programs copied off the laptop; quarterly restore tests | Field Technician | 2026-12-31 |
| No named security role; no policies; no HR security steps | GV.RR-02, GV.PO-01, GV.RR-04 | Moderate | Designations and policies (done 2026-08-31); last-day checklist; acknowledgments | Owner; Office Manager | 2026-09-30 |
| No supplier security terms or due diligence (SCADA vendor write-back) | GV.SC-05, GV.SC-06, ID.RA-10; Fla. Stat. 501.171(6) | Moderate | Vendor checklist; security schedule at renewal | Owner | 2027-03-31 |
| No OT inventory, drawing, or change control | ID.AM-01 to ID.AM-03, ID.RA-07; SP 800-82r3 6.1.1, 6.2.4 | Moderate | OT inventory and drawing; OT change log | Field Technician; Field Superintendent | 2026-11-30 |
| Unsupported SCADA host; open USB and software installs | PR.PS-02, PR.PS-05, ID.AM-08; SP 800-82r3 6.2.11 | Moderate | Replacement host; standard user; USB blocked | Field Technician | 2026-12-31 |
| No incident plan, escalation path, or exercise | ID.IM-04, RS.MA-01, RS.MA-04, ID.IM-02 | Moderate | P08 runbook; tabletop with the MSP and integrator | Office Manager | 2026-11-30 |
| No training | PR.AT-01 | Moderate | Annual training with a field module; phishing exercises | Office Manager | 2026-12-31 |
| Owner data unprotected in email and on laptops; no breach procedure | PR.DS-01, PR.DS-02, ID.AM-07; Fla. Stat. 501.171(2), (4) | Moderate | Encrypted send; data list; notice template and counsel contact | Production Accountant; Office Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company. The MSP does the office work under the Office Manager's direction; the Field Technician and the integrator do the field work under the Field Superintendent's. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Access and accountability | 2026-09-30 to 2026-10-31 | Designations and policies (done 2026-08-31); acknowledgments; last-day checklist; gate code and shared passwords changed; MFA on the mobile viewer and backup console; company-enabled vendor sessions; reporting cards; call-back rule; Geology folder restricted; first MSP restore test | GV.RR-02, GV.RR-04, GV.PO-01, PR.AA-01 to PR.AA-03, PR.AA-05, PR.AA-06, RS.MA-02, GV.SC-10 |
| 2. Visibility and the field network | 2026-11-30 | OT inventory and network drawing; IT/OT firewall; OT change log; incident runbook and tabletop; storm checklist update; encryption of the field desktop and engineering laptop | ID.AM-01 to ID.AM-03, ID.AM-07, ID.RA-07, PR.IR-01, PR.IR-02, PR.DS-01, PR.DS-02, ID.IM-02, ID.IM-04, RS.MA-01, RS.MA-04, RS.MI-01, RC.RP-01 |
| 3. Recovery and detection | 2026-12-31 | Replacement SCADA host; rotated offline backups and immutable cloud copy; quarterly restore tests; EDR with after-hours alerts; training and phishing exercises; rebuild procedure | PR.DS-11, RC.RP-03, RC.RP-05, PR.PS-01, PR.PS-02, PR.PS-05, ID.AM-08, DE.CM-01, DE.CM-09, PR.AT-01, RS.MI-02 |
| 4. Suppliers | 2027-03-31 | Security schedule and breach notice terms at renewal (integrator, SCADA vendor, MSP, production accounting vendor); annual vendor review | GV.SC-01, GV.SC-02, GV.SC-05, GV.SC-07; Fla. Stat. 501.171(6) |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk analysis update (July); independent assessment and policy review (August) | GV.OV-01 to GV.OV-03, GV.PO-02, ID.IM-01 |

**Progress check.** The Office Manager reports progress to the Owner at a monthly 30-minute meeting with the Field Superintendent, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
None of these is a current obligation. The `pending_rule_change` column flags the affected rows.
- **CIRCIA final rule (N21-R03).** Not published as of 2026-09-25. If the final rule keeps the proposed size test and sector criteria, the company stays outside it by a wide margin. If CISA adds an oil and gas production criterion that applies regardless of size, the company would face 72-hour incident reports and 24-hour ransom payment reports to CISA. The Office Manager rechecks when the final rule is published (GV.OC-03).
- **TSA surface cyber risk management rule** (NPRM Nov. 7, 2024; not final). Relevant only if the company ever operates a pipeline that TSA designates.
- **Business changes that would change applicability:** selling associated gas through a new gas line (PHMSA Part 192 gathering classification), buying a crude gathering line (Part 195), or growing past 500 Florida residents in the owner and employee records (Fla. Stat. 501.171(3) Department notice).
