# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Specialty Chemicals, Distribution, Hazmat Transport) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents, or a change in the status of CFATS or CIRCIA |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, CM-3, CM-4, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.RA-07, ID.IM-01 |
| Regulatory basis | CFATS RBPS 8 (voluntary benchmark, C-CHEMICAL-R01); 40 CFR Part 68 (68.15, 68.67, 68.75); 33 CFR 101.620 and 101.630 (Terminal T1, C-CHEMICAL-R02); 49 CFR 172.802; Reg S-K Item 106 (N42-R07) |
| Division supplements | Specialty Chemicals (v2026); Distribution (v2026, with the Terminal T1 Cybersecurity Plan annex due 2027-05-31); Hazmat Transport (v2023, re-alignment due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for IT and OT across the group, assign who is accountable at group, division, and facility level, and give every other group policy and every division supplement its authority. The program protects people, communities, and the environment around group facilities, as well as the group's information and the systems that control chemical processes, terminals, and fleets.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and integrator and vendor personnel with access), all IT and OT systems and data the group owns or operates, and systems operated for the group by service providers. OT includes distributed control systems, safety instrumented systems, PLCs, terminal automation, gas detection, telematics, and the networks that connect them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and process safety risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group OT Security Director | Owns the group OT security standard, the OT remote access gateway design, OT monitoring, and the SOC OT desk |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Process Safety Director | Owns PHA and MOC methods; makes sure process safety programs consider cyber causes |
| Group General Counsel | Owns intercompany agreements and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Very Low and Low risks |
| Facility regulator-facing roles | RMP qualified person at each covered plant (40 CFR 68.15(b)); Terminal T1 Facility Security Officer and Cybersecurity Officer (33 CFR 101.620(b)(3)); the senior management official for each hazmat security plan (49 CFR 172.802(b)(1)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents and unexplained process behavior immediately |

**Where roles overlap.** The Group OT Security Director designs the gateway and also runs the OT desk that monitors it. Group internal audit, which reports to the board audit committee, assesses the gateway each year, and the OT desk's alerts go to the Group SOC director as well.

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that covers IT and OT. OT is protected under the group OT security standard, built on NIST SP 800-82 Rev. 3, with RBPS 8 used as a voluntary benchmark while CFATS is lapsed. (PM-1; GV.PO-01; C-CHEMICAL-R01)

4.2 The Group CISO is accountable for the program, and the Group OT Security Director for the OT standard. Regulator-facing facility roles (4.14) are named in writing by each division and are not delegated to corporate. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. **Process safety and public safety risks rated High must be treated, not accepted.** (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or regulator-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog (P02). Each division must document, for each of its systems, which controls it inherits and which remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR documents every sanction. Contractors who violate them lose access. (PS-8; GV.RR-04)

4.8 **Third parties.** No integrator, OEM, or service provider may access group OT or Restricted data without a contract that includes the group security addendum: named accounts, training, background checks for personnel with access, notice of cybersecurity vulnerabilities and incidents without delay (33 CFR 101.650(f)(2) for Terminal T1 vendors), and the right to audit. Contractors doing work on or adjacent to an RMP-covered process are also evaluated under the contractor program (40 CFR 68.87). (SA-4; SA-9; SR-8; GV.SC-05)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Audits of the Terminal T1 Cybersecurity Plan must be done by people independent of the measures they audit (33 CFR 101.630(f)(4)). Results feed the POA&M and the risk registers. (CA-2; CA-2(1); CA-7; ID.IM-01)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. An exception may never extend a legal deadline or remove a safety function. (PL-1)

4.11 **Retention.** Security policies, risk analyses, assessments, and required actions must be kept at least 6 years. Where a regulation sets a different period, keep the longer one: RMP records 5 years (40 CFR 68.200), PHAs for the life of the process (68.67(g)), MTSA records at least 2 years (33 CFR 105.225), and hazmat training records for 3 years of training plus 90 days after employment ends (49 CFR 172.704(d)). (SI-12; GV.PO-02)

4.12 **AI systems.** No AI system may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). **No AI system may write to a control system, change a setpoint, or change an alarm limit** unless the Group AI council has approved it as a High-tier use case and the change has passed plant MOC under 4.13. (RA-3; CM-3; GV.RM-01)

4.13 **Process safety and cyber together.** At every plant with an RMP- or PSM-covered process, any change to control system logic, setpoints or alarm limits outside the operating envelope, recipes, remote access paths, network connections, or AI operating modes is a change under MOC (40 CFR 68.75), with an OT security reviewer on the MOC and a cybersecurity screening question. PHAs and hazard reviews must consider control system compromise as a cause. MOC must also enforce Plant C1's inventory limits: hydrogen peroxide bought below 52% by weight, and flammable liquids under 10,000 lb in any one process location, so that no second PSM-covered process is created. (CM-3; CM-4; RA-3; ID.RA-07)

4.14 **Regulator-facing roles.** Each covered plant names its RMP qualified person; Terminal T1 names its Facility Security Officer and its Cybersecurity Officer (with alternates) in writing; each division names the senior management official for its hazmat security plan. Changes to these roles are reported as the rules require (for example, a CySO change within 96 hours, 33 CFR 101.630(e)(4)). (PM-2; GV.RR-02)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, MOC audits, and the RMP compliance audits.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; group OT security standard (2025); common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 40 CFR Part 68; 33 CFR Part 101 Subpart F; 49 CFR 172.800 to 172.804.
