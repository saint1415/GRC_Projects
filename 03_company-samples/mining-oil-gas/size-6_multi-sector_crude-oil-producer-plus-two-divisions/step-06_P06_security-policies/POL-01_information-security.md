# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crude Oil Production, Power Generation, Crude Logistics) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee (2026-09-17) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SR-6, CA-2, CA-7, SI-12, CM-4 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory and benchmark drivers | NIST CSF 2.0 and SP 800-82 Rev. 3 (benchmark); NERC CIP-003-9 R1, R3 (Power Generation); 49 CFR 195.446(a) and 172.802(b) (Crude Logistics); Reg S-K Item 106 |
| Division supplements | Production supplement (v2026); Power Generation supplement (v2026, includes the CIP-003-9 low impact plans); Crude Logistics supplement (v2023, re-alignment due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, covering business IT and operational technology (OT), assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects people, the environment, and the reliability of production, generation, and transportation, as well as the group's information.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and integrator and vendor staff with access), all systems and data the group owns or operates, including field SCADA, plant control systems, and pipeline SCADA, and systems operated for the group by service providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group OT Security Director | Owns the OT security architecture, the OT DMZ standard, and the SOC OT desk for all divisions |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Owns intercompany agreements, regulator notices, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Power Generation CIP Senior Manager | Approves the CIP-003-9 policy and low impact plans (CIP-003-9 R3) |
| Crude Logistics Fleet Safety Director | Senior official for the hazmat security plan (49 CFR 172.802(b)(1)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0. OT systems must also follow NIST SP 800-82 Rev. 3 as the group's OT benchmark. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program and the Group OT Security Director for OT security across divisions. Each division must name a security and compliance lead in writing. Power Generation must name a CIP Senior Manager and Crude Logistics a senior official for the hazmat security plan. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; GV.RM-03)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Safety and environmental risks rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter or regulator-specific requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Safety first.** No security control, test, or response action may disable, bypass, or delay a safety instrumented function, hardwired shutdown, relief device, or alarm required by a safety or environmental rule. Security changes that could affect process safety must go through the division's management of change process. (CM-4; SI-17; PR.IR-03)

4.8 **Suppliers.** No OT supplier, integrator, or service provider may receive access or deliver software to OT until it has been assessed and its contract includes the group OT security schedule (security duties, incident notice, and remote access terms). (SA-4; SR-6; GV.SC-05; GV.SC-07)

4.9 **Acquisitions.** An acquired operation must not be connected to group networks until its OT is isolated, logged in the group SIEM, and its remote access is moved to group PAM, unless the Group CISO approves a dated exception. (CA-3; RA-3; ID.RA-01; GV.SC-06)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1; GV.PO-02)

4.12 Security policies, procedures, risk analyses, assessments, and compliance evidence must be retained for at least 6 years, or longer where a regulation or audit cycle requires (for example, NERC evidence since the last audit, and Part 195 records for the periods each section sets). (SI-12; GV.PO-02)

4.13 **AI systems.** No AI system that can change physical operations, or that makes or supports decisions about people, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). A model that writes setpoints to field or plant equipment also needs a safety management of change review. (RA-3; CM-4; PL-2; GV.RM-01; ID.RA-07)

4.14 Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Compliance is checked through the P07 assessment of common controls and division samples, the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may weaken a safety function or extend a legal notice deadline.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10).
