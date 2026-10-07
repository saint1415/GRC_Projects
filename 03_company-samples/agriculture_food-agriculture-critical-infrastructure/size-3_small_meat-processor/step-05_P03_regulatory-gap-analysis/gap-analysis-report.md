# Regulatory Gap Analysis: Cris Santos Company | Food and Agriculture | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Tier / Vertical | Small / Food and Agriculture (NAICS 311612) |
| Primary regulation | FSMA Intentional Adulteration rule, 21 CFR Part 121 (C-FOOD-AG-R01), text read from eCFR (point-in-time 2026-09-23) |
| Secondary regulation | FSIS HACCP and recall rules where they touch electronic CCP monitoring and records (9 CFR 417.2-417.5, 418.2-418.3), with the parallel seafood HACCP record rule (21 CFR 123.9(f)) |
| OT control benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (voluntary) |
| Assessment dates | 2026-07-13 to 2026-07-24 (plant walkthrough 2026-07-15) |
| Assessors | FSQA Manager (qualified individual under 121.4(c)) and IT Manager, with the Controls Engineer |

## 1. Applicability

### 1.1 Does Part 121 apply to a meat processing plant?
**Usually not, but it does here.** Part 121 applies to "the owner, operator or agent in charge of a domestic or foreign food facility that manufactures/processes, packs, or holds food for consumption in the United States and is required to register under section 415 of the Federal Food, Drug, and Cosmetic Act, unless one of the exemptions in § 121.5 applies" (21 CFR 121.1). The facility definition in 121.3 points to the registration rule in 21 CFR Part 1, Subpart H.

The registration rule exempts "Facilities that are regulated exclusively, throughout the entire facility, by the U.S. Department of Agriculture under the Federal Meat Inspection Act" (21 CFR 1.226(g)). A plant that made only FSIS-inspected meat products would not register with FDA and **would not be covered by Part 121**. FDA's own compliance policy guide states the jurisdictional split: USDA has exclusive jurisdiction over a meat product up to the time it leaves a USDA-inspected plant (FDA CPG Sec. 565.100).

Cris Santos Company lost the 1.226(g) exemption in 2023, when it opened the smoked seafood room. Finfish is FDA-regulated food, so the plant registered with FDA in February 2023 (21 CFR 1.225) and is now a covered facility.

### 1.2 Size and exemptions (21 CFR 121.5)
| Exemption | Result | Reason |
|---|---|---|
| 121.5(a) very small business | **Does not apply** | 121.3 defines a very small business as averaging less than $10,000,000, adjusted for inflation, per year over the prior 3 years in human food sales plus the market value of food held without sale. The company's human food sales are about $148 million a year. No reasonable inflation adjustment closes that gap |
| 121.5(b) holding | **Partly** | Storage of finished product in coolers and the freezer warehouse is exempt holding. The seafood brine tank is a liquid storage tank, which the exemption expressly keeps in scope |
| 121.5(c) intact-container packing | **Partly** | Resale of sealed packages at the outlet store is exempt; processing is not |
| 121.5(d) produce farms; (e) alcoholic beverages; (g) on-farm eggs and game meats | Do not apply | The company is not a farm and makes no alcoholic beverages |
| 121.5(f) animal food | **Partly** | Inedible fish trim sold to a renderer is outside the rule |

**Small business.** Under 121.3 a small business employs fewer than 500 full-time equivalent employees. The company has 242 FTE (250 employees), so it is a small business. FDA's rule page gives small businesses four years after publication of the final rule (81 FR 34219, May 27, 2016) to comply. That period ended in 2020, before the company registered. **The rule applied in full from the day the seafood room began production.**

### 1.3 Scope decision
Part 121 is an FDA rule and FDA's jurisdiction over the FSIS-inspected meat products is limited while they are in the plant (CPG Sec. 565.100). The plan therefore covers:
- **In scope:** every point, step, and procedure of the smoked seafood process (receiving, brining, smoking, dip mixing, packaging), and **every shared system that can reach that food**: the brine and cure dosing skid, the CIP valve manifold, the recipe and batch system that sends formulations and setpoints, the seafood smokehouse controller, and the ammonia refrigeration controls.
- **Voluntarily in scope:** the General Manager directed that the same vulnerability method be applied to the meat lines. FSIS describes functional food defense plans as voluntary in FSIS-regulated establishments (text from fsis.usda.gov search results; the page itself returned HTTP 403 when fetched on 2026-09-26). No food defense plan requirement appears in 9 CFR Parts 416-418, which were read on eCFR. The meat-line work is **not** scored as Part 121 compliance in this analysis.
- **Open question for counsel:** whether FDA expects the vulnerability assessment at a mixed FDA and FSIS facility to cover the FSIS-inspected products. The regulatory text requires an assessment "for each type of food manufactured, processed, packed, or held at your facility" (121.130(a)) and was not found to address mixed-jurisdiction plants. The company is covering both, so the answer changes documentation, not controls.

### 1.4 Part 121 is not an IT rule
Part 121 regulates **intentional adulteration intended to cause wide-scale public health harm**. It never mentions computers, networks, or control systems. It becomes a cyber-physical rule at this plant because:
- **Attackers reach the product through equipment.** The dosing skid, CIP valves, and smokehouse controllers act on food. A person with HMI, PLC, or recipe-system access can add a contaminant (for example, route CIP chemical into brine) without touching the product. The assessment methods in 121.130(a)(2)-(3) and the inside-attacker duty in 121.130(b) must consider that path. Treating control-system access as "access to the product" is an **author interpretation**, recorded as such in the CSV. FDA's draft guidance also describes a Key Activity Types method whose types include liquid storage and handling and mixing and similar activities (FDA constituent update on the revised draft guidance; nonbinding). The brine tank and dip mixing steps fall in those types.
- **Mitigation strategies can be cyber controls.** A hardwired interlock, named logins, two-person recipe approval, and a gated remote-access path are "risk-based, reasonably appropriate measures" (121.3) for those steps.
- **Monitoring, verification, and records live in systems.** Monitoring records must be accurate, indelible, and created concurrently (121.305), which puts integrity controls on the records application and historian in scope.
- **Change triggers reanalysis.** A significant change in plant activities that creates a reasonable potential for a new vulnerability requires reanalysis (121.157(b)(1)). A new remote access path or a recipe-system release is such a change.

Part 121 does not ask for segmentation, EDR, backups, or incident response in general. Those come from the OT benchmark (section 1.6).

### 1.5 Secondary regulation: FSIS HACCP records
The most relevant binding secondary rule is FSIS HACCP (9 CFR Part 417), because the plant's CCPs (cooking, chilling, cold storage) are monitored and recorded by the historian, cold-chain sensors, and records application in the SSP boundary. Key texts:
- "The use of records maintained on computers is acceptable, provided that appropriate controls are implemented to ensure the integrity of the electronic data and signatures" (9 CFR 417.5(d)). The seafood HACCP rule has the same sentence (21 CFR 123.9(f)).
- A HACCP system may be found inadequate if records are not maintained as required or adulterated product is produced or shipped (9 CFR 417.6).
- An establishment must notify the FSIS District Office within 24 hours of learning or determining that adulterated or misbranded product has entered commerce (9 CFR 418.2).

**FSIS inspection context (verified items only).** The plant is an official establishment with FSIS inspection program personnel assigned. FSIS verifies HACCP plans by reviewing the plan, CCP records, corrective actions, and critical limits, and by direct observation and record review (9 CFR 417.8). Records must be available for official review and copying (9 CFR 417.5(f)). This analysis does not describe FSIS inspection frequency or food defense verification tasks, which were not verified.

### 1.6 OT benchmark: NIST CSF 2.0 and SP 800-82 Rev. 3
Neither rule sets technical security controls for OT. The 12 benchmark rows use CSF 2.0 outcomes, tailored with SP 800-82 Rev. 3 (OT asset inventory, zones and conduits, remote access, OT change management, monitoring, backups, incident response, suppliers). They are **voluntary**, and are scored so the roadmap can show which regulatory gaps depend on them.

### 1.7 Other vertical requirements considered
- **CIRCIA (C-FOOD-AG-R02):** proposed rule only; not in effect as of 2026-09-26. As proposed (226.2(a)), coverage for this sector depends on exceeding the SBA size standard. The company has 250 employees against a 1,000-employee standard, so it would not be covered unless the final rule changes. Tracked in the `pending_rule_change` column.
- **USCG MTS cyber rule (C-FOOD-AG-R03):** does not apply. The plant is not an MTSA-regulated facility.
- **Reportable Food Registry (21 U.S.C. 350f):** a notification duty for the seafood room, handled in P08.

## 2. Method
1. **Requirements.** Part 121 rows follow the rule's own structure at paragraph level: 121.1 and 121.4-121.5 (Subpart A), 121.126-121.157 (Subpart C), 121.305-121.325 (Subpart D). 121.401 (prohibited acts) is enforcement context, not a requirement row. FSIS and seafood HACCP rows are limited to the paragraphs that touch electronic monitoring, records, corrective actions for unforeseen deviations, reassessment, and notification.
2. **Crosswalk.** NIST has published no mapping for Part 121 or 9 CFR Part 417, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. Benchmark rows use the official NIST CSF 2.0 to SP 800-53 informative references (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`), showing a subset.
3. **Evidence.** Interviews (General Manager, FSQA Manager, Controls Engineer, Maintenance and Refrigeration Manager, IT Manager, Sanitation Supervisor, seafood room lead); review of the 2023 food defense plan, HACCP plans, monitoring and corrective action logs (12-week sample), training records, change history, firewall and VPN configuration; and the 2026-07-15 walkthrough.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Part 121 Subpart A (121.1, 121.4 qualifications, 121.5 exemptions) | 12 | 2 | 6 | 0 | 4 |
| Part 121 Subpart C (121.126-121.157, food defense measures) | 37 | 4 | 18 | 13 | 2 |
| Part 121 Subpart D (121.305-121.325, records) | 13 | 5 | 6 | 0 | 2 |
| **Part 121 subtotal** | **62** | **11** | **30** | **13** | **8** |
| FSIS HACCP (9 CFR 417) | 12 | 6 | 5 | 1 | 0 |
| FSIS recalls (9 CFR 418) | 2 | 1 | 1 | 0 | 0 |
| FDA seafood HACCP (21 CFR 123.9(f)) | 1 | 0 | 0 | 1 | 0 |
| NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 12 | 0 | 5 | 7 | 0 |
| **Total** | **89** | **18** | **41** | **22** | **8** |

The 63 unmet or partially met rows break down by gap risk as 1 Very High, 21 High, 35 Moderate, and 6 Low. For Part 121 alone, the 43 open rows are 12 High, 25 Moderate, and 6 Low.

**The pattern.** The 2023 plan is a sound physical food defense plan with no management layer behind it and no view of the control system:
- **Subpart C is where the gaps are.** All 13 Not met Part 121 rows are in Subpart C: no verification at all (121.150), and no reanalysis. The 3-year reanalysis under 121.157(a) was due by 2026-02-20 and is overdue.
- **The vulnerability assessment missed the equipment path.** The brine tank, dosing skid, and CIP manifold were evaluated only for a person with a jug of contaminant, not for someone at an HMI or on the integrator VPN (P01 R-002, R-003, R-004).
- **Records are the bridge between food rules and IT.** 121.305(c) and (f), 9 CFR 417.5(b) and (d), and 21 CFR 123.9(f) all fail for the same reason: shared accounts and a disabled audit trail.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Reanalysis overdue and changes made without reanalysis | 121.157(a), (b)(1)-(2), (c) | High | Start reanalysis now with P01 inputs; add food defense sign-off to OT changes | FSQA Manager | 2026-10-31 start; 2026-12-31 complete |
| Vulnerability assessment omits control-system paths and insiders with shared logins | 121.130(a), (a)(2)-(3), (b) | High | Reassess every automated step with the Controls Engineer | FSQA Manager | 2026-12-31 |
| No mitigation at the seafood brine tank for CIP routing | 121.135(a) | High | Hardwired CIP interlock; brine tank as an actionable process step | Maintenance and Refrigeration Manager | 2026-11-30 |
| Shared HMI and recipe logins; no two-person formulation approval | 121.135(a); CSF PR.AA-05 | High | Named accounts; role-based recipe approval with change alerts to FSQA | Controls Engineer | 2026-12-31 |
| Electronic CCP and food defense records lack integrity controls | 9 CFR 417.5(d); 21 CFR 123.9(f); 121.305(c), (f) | High | Enable audit trails; named accounts and e-signatures; record locking | IT Manager | 2026-12-31 |
| No verification of any mitigation strategy | 121.150(a)-(c) | Moderate | Monthly records review; quarterly interlock tests; log reviews | FSQA Manager | 2026-12-31 |
| No procedure for loss of CCP monitoring or suspected tampering | 9 CFR 417.3(b); 418.2 | High | Product hold, review, and notification decision in P08 | FSQA Manager | 2026-10-31 |
| Weak OT segmentation; MES dual-homed | CSF PR.IR-01 | Very High | OT DMZ; rule rebuild; remove dual-homing | IT Manager | 2027-03-31 |
| OT remote access without MFA | CSF PR.AA-03 | High | Remote access gateway with MFA and approval | IT Manager | 2026-10-31 |
| Food defense awareness lapsed for temporary workers | 121.4(b)(2) | Moderate | Training at hire and annually for every worker at an actionable step | HR Manager | 2026-10-31 |

**Housekeeping actions:** renew the FDA registration between 2026-10-01 and 2026-12-31 (21 CFR 1.230(b)); keep a controlled printed copy of the plan onsite (121.315(c)); have the General Manager sign every plan revision (121.310).

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **Part 121:** no proposed amendments were found. The most recent Federal Register document affecting Part 121 is a 2022-03-14 notice of availability of an FDA enforcement policy guidance on certain provisions of several FSMA rules; its content was not reviewed for this analysis.
- **CIRCIA:** the final rule was not published as of 2026-09-26. The Unified Agenda listed 09/2026. If the final rule keeps the NPRM's size-based criterion, the company stays out of scope. If it adds a Food and Agriculture sector criterion, the P08 notification matrix must add a 72-hour report to CISA.
- **FSMA 204 traceability rule** (21 CFR Part 1, Subpart S) may reach the seafood room's products if they are on FDA's Food Traceability List. FDA proposed extending the compliance date to July 20, 2028 (FR Doc. 2025-14967). Whether the extension was finalized was not confirmed. Not analyzed here; flagged for the FSQA Manager.

None of these is treated as a current obligation.
