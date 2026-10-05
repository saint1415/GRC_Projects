# Regulatory Gap Analysis: Cris Santos Company | Dams | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project, Florida) |
| Tier / Vertical | Micro / Dams |
| Primary program analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (March 30, 2016), as applied to a **Security Group 3** dam. Source: https://www.ferc.gov/sites/default/files/2020-04/security.pdf |
| Secondary regulation | 18 CFR Part 12, Safety of Water Power Projects and Project Works: incident reporting (12.10) and the related records, EAP, warning device, gate testing, and Owner's Dam Safety Program duties (eCFR version 2026-09-23) |
| Also checked | NERC CIP applicability (BES definition, Inclusion I2); Part 12 Subpart D triggers |
| Assessment dates | 2026-07-13 to 2026-07-24 (voluntary Section 9 screen on 2026-07-16) |
| Assessors | Office and Compliance Administrator and Plant Superintendent, with the Controls and Electrical Technician |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Applicability
**The FERC Security Program applies, but lightly, because this is a Security Group 3 dam.** The company is a FERC licensee, and 18 CFR Part 12 applies to projects licensed under Part I of the Federal Power Act (12.1(a)(1)). The Security Program is D2SI guidance that FERC engineers apply during dam safety inspections. It has no employee or revenue threshold: duties depend on the Security Group FERC assigns from consequence, vulnerability, and likelihood of attack. FERC placed this dam in **Group 3** (January 2010 regrouping letter to the prior licensee, confirmed at the 2025-11-04 inspection). For Group 3 the program says:

| Duty | Group 3 position (Rev. 3A) | Rows |
|---|---|---|
| General licensee responsibilities (awareness, walk-downs, training, contacts, reporting suspicious activity and incidents) | Apply to all licensees (3.2) | G-001 to G-010 |
| Security Assessment and Security Plan | "No security document requirements"; both "highly recommended" (3.3.3) | G-011, G-012 |
| Cyber security plan | "All Security Groups should consider having cyber security plans if they utilize cyber/SCADA assets" (3.3.3) | G-013 |
| Vulnerability Assessment | Only to justify a permanent facility closure (3.3.3, 3.3.4) | G-015: Not applicable |
| Group 1 and 2 Security Plan sub-elements and the Annual Security Compliance Certification Letter | Group 1 and 2 only | G-016, G-017: Not applicable |
| Threat notification and communications | All licensees (4.1 to 4.3) | G-018 to G-022 |

**Section 9 (Computer Security and SCADA) does not apply as an obligation.** Only Group 3 dams that are interconnected to operational or critical cyber assets of Group 1 or 2 dams are subject to it (9.1 note). This plant is not interconnected to any other dam (G-023). The company ran the Form 3 screen voluntarily on 2026-07-16: Questions 1 to 3 Yes (remote data acquisition, remote generation control, and remote control of the spillway gates), Question 4 No. Every Table 9.1c consequence value is at or below its threshold, and 4.4 MW of generation is Non-critical (under 100 MW, Table 9.1c note 3). Had Section 9 applied, the plant would sit at the baseline level (9.1.1.2). **The company adopts the Table 9.3a baseline measures as its benchmark** (G-024 to G-041), because remote control of the gates since 2021 is exactly the risk the FERC engineer raised at the 2025 inspection. Those rows are marked "Voluntary benchmark" in `gap-analysis.csv` and are not presented as FERC requirements.

**Size and form do not change the binding Part 12 duties.** The dam is Significant hazard (12.3(b)(13)(ii)) and has an EAP with no exemption under 12.21. A "condition affecting the safety of a project" includes misoperation of a gate (12.3(b)(4)(ii)) and "security incidents (physical and/or cyber)" (12.3(b)(4)(xi)), so a cyber event on the gate or unit controls must be reported to the Regional Engineer "as soon as practicable after that condition is discovered, preferably within 72 hours" (12.10(a)(1)). That is the most important binding rule in this analysis and the clock behind the P08 runbook.

**Not applicable, with reasons (7 rows):**
- **Part 12 Subpart D and 12.65** (G-055): the dam is about 26 feet high and about 1,700 acre-feet, not High hazard, and the Regional Engineer has made no determination, so the 12.30 triggers are not met.
- **NERC CIP** (G-056): under the NERC BES definition (Reference Document version 3, April 30, 2026), a generating resource is included under I2 only when connected at 100 kV or above and over 20 MVA per unit or 75 MVA per plant. The 2 units are about 2.4 MVA each, connected at 12.47 kV, and none is a blackstart resource. The company is not NERC-registered.
- **Section 9 obligation** (G-023) and **Table 9.3b enhanced measures** (G-042): not triggered; the voluntary screen places the plant at the baseline level.
- **Vulnerability Assessment and Group 1 and 2 documents** (G-015 to G-017).

**Which revision.** Revision 3A is the latest version this analysis could confirm on ferc.gov. **Action:** the Plant Superintendent will confirm the current revision and the Group 3 status with the Regional Engineer before the next inspection (autumn 2027).

## 2. Method
1. **Requirements.** Rows follow the program's own structure: section 3.2 licensee responsibilities (bullet by bullet), the Group 3 provisions in 3.3.3 and Table 3.3.8, section 4, the Section 9 screen and each line of the Table 9.3a baseline measures, and four Form 1 physical checklist items the FERC engineer uses. Group 1 and 2 items are listed as Not applicable so the reader can see the line. Part 12 rows cite section and paragraph. FERC documents and the CFR are U.S. government works; short phrases are quoted where the wording matters.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has not published a mapping for the FERC program. Table 9.3a cites NIST SP 800-82; the mapping uses SP 800-82 Rev. 3 as the bridge.
3. **Documentary evidence.** Each status rests on a named record: the 2011 physical security checklist, the EAP and the 2026-02-17 drill record, the ODSP and its 2025 annual review, the 2024 and 2025 12.10 reports, the 2026 gate and generator test statement, the integrator's 2015 network drawing and firewall description, the remote desktop tool's user and connection settings, the suite sharing report (2026-07-15), the MSP campaign report, the walk-down sheet, and a site walkthrough on 2026-07-16. Interviews covered all 7 staff, the MSP, and the integrator.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since then (for example, the password change on 2026-08-12) are noted in the remediation column but do not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Sec. 3 Requirements and responsibilities | 3 | 7 | 4 | 3 | 17 |
| Sec. 4 Threat notification and communications | 1 | 2 | 2 | 0 | 5 |
| Sec. 9 Computer security and SCADA (voluntary benchmark) | 1 | 5 | 12 | 2 | 20 |
| Appendix A Form 1 (physical checklist) | 0 | 3 | 1 | 0 | 4 |
| 18 CFR Part 12 (secondary, binding) | 6 | 2 | 0 | 1 | 9 |
| NERC CIP (applicability) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **11** | **19** | **19** | **7** | **56** |

Of the 38 unmet or partially met rows, 11 are rated High, 16 Moderate, and 11 Low. None is Very High.

**The pattern.**
- **Dam safety paperwork is sound.** Six of the nine Part 12 rows are met: the EAP, warning devices, gate and standby power tests, permanent records, and 12.10 reporting for physical conditions all work. A small staff that drills its EAP every year does the dam safety basics well.
- **Cyber was never part of the program.** 17 of the 18 assessed Section 9 benchmark rows are unmet or partially met. The plant gained remote gate control in 2021 with one shared password and an always-on vendor link, and nobody treated that as a security change.
- **The binding gap is reporting.** G-047 (Partially met, High): 12.10 reporting works for a hoist motor failure or a rescue, but staff did not know a cyber event on the gates is a reportable condition. This is the one High gap against a mandatory regulation.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| One shared remote desktop password, no MFA, full gate and unit control from anywhere | 9.3a access control (benchmark); G-041 | High | One remote access path with named accounts, MFA, and view-only by default; integrator sessions approved and watched | Controls and Electrical Technician | 2026-11-30 (password changed 2026-08-12) |
| Firewall bypassed by the integrator router, an open office rule, and a dual-use laptop | 9.3a segregation (benchmark); G-039 | High | Firewall rebuild; router off except for watched sessions, then retired; OT-only engineering laptop | Controls and Electrical Technician | 2026-10-31 |
| Cyber events not recognized as 12.10 conditions | 18 CFR 12.10(a)(1); 12.3(b)(4)(xi); G-047, G-009 | High | POL-03 reporting rule; P08 runbook and matrix; training; ODSP communication section | Plant Superintendent | 2026-10-31 |
| Remote control of gates since 2021 with no cyber security plan | 3.3.3; G-013 | High | Adopt the P02 SSP as the cyber section of a site security plan; carry out its POA&M | Plant Superintendent | 2026-11-30 |
| Gate and unit controls cannot be rebuilt without the integrator | 9.3a restoration (benchmark); G-035 | High | Company-held copies after every change; written OT recovery procedure | Controls and Electrical Technician | 2026-12-31 |
| Unsupported, unpatched HMI PC | 9.3a configuration and patching (benchmark); G-033 | High | Replace the HMI PC; quarterly integrator version check | Owner and General Manager | 2027-03-31 |
| No annual security training; OPSEC not practiced | 3.2 (bullet 4); G-004 | High | Annual 1-hour session for all 7 staff; ICS course for the Controls and Electrical Technician | Office and Compliance Administrator | 2026-10-31 |
| No view of all connections into the control network | 9.3a network connections (benchmark); G-026 | High | List and review every connection with the OT inventory | Controls and Electrical Technician | 2026-10-31 |
| A remote intrusion would be noticed only if a gate moved | 9.3a intrusion detection (benchmark); G-037 | High | Phone alert at each remote session start; weekly session review; P08 runbook | Plant Superintendent | 2026-11-30 |
| CEII-type documents open to all staff and "anyone with the link" | Form 1 Q22; G-046 | Moderate | Restricted CEII folder with named guests; labels (POL-04) | Office and Compliance Administrator | 2026-09-30 |

G-001 (High) is the umbrella row for the licensee's security responsibility; it closes as the rows above close. The full list, with evidence, is in `gap-analysis.csv`. High gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are one-page procedures, settings in tools the company already pays for, or integrator labor. The budget approved on 2026-08-31 (about $21,000 one-time and $3,100 a year) is itemized in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Quick fixes | 2026-09-30 | Default passwords changed and data logger cabinet locked; hoist house lock changed and keys inventoried; restricted CEII folder; security checks on the walk-down sheet; FERC notices forwarded automatically; county weir contact and closure notice rule in the EAP and P08 contact sheets; P08 runbook in use for security breaches | G-002, G-007, G-014, G-018, G-019, G-025, G-044, G-046 |
| 2. Close the open doors | 2026-10-31 | Firewall rebuild; OT-only engineering laptop; no browsing on the HMI PC; OT inventory and connection list; change form with security questions; old HMI PC wiped; annual training; reporting rule taught | G-004, G-009, G-026, G-031, G-032, G-034, G-039, G-040, G-047 |
| 3. Remote access and detection | 2026-11-30 | One remote access path with named accounts and MFA; cellular paths evaluated; session alerts and weekly review; HSIN Dams portal access | G-003, G-013, G-021, G-027, G-037, G-041, G-043 |
| 4. Recovery and contracts | 2026-12-31 | Company-held OT copies and OT recovery procedure; Security Assessment from P01; ODSP updated for security; quarterly MSP and integrator call; security terms in vendor contracts; ICS course | G-011, G-029, G-030, G-035, G-038, G-054 |
| 5. Plans and replacement | 2027-02-28 to 2027-05-31 | EAP cyber trigger page; site security plan with threat-level actions; HMI PC replacement and first restore test; satellite messenger for the on-call phone | G-001, G-008, G-012, G-022, G-033, G-036, G-045 |
| 6. Annual cycle | 2027-07-31 | Review procedures and asset criticality with the risk register; repeat the Section 9 screen (G-024, already met) | G-028 |

**Progress check.** The Office and Compliance Administrator reports progress to the Owner and General Manager at a monthly 30-minute meeting, using the P07 POA&M as the tracker. The site security plan, Security Assessment, and POA&M will be ready to show the FERC engineer at the next inspection.

## 6. Pending regulatory changes
- **FERC Security Program:** no newer revision confirmed (section 1). Recheck with the Regional Engineer before each inspection. If FERC regrouped the dam, or if the plant were ever interconnected with a Group 1 or 2 dam, Section 9 would become mandatory and the benchmark rows would become requirements.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226): the final rule has not been published as of 2026-09-25, so reporting to CISA is voluntary. The proposed rule has no dams-specific criterion, and the company is far below the SBA size standard used in the proposed scope, so it would likely be outside the rule if finalized as proposed.
- **NERC CIP:** approved future revisions (effective 2028 and 2029) do not change BES inclusion, so they would not reach this 4.4 MW distribution-connected plant.

The `pending_rule_change` column in `gap-analysis.csv` records this per row. None of these is treated as a current obligation.
