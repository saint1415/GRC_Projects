# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Commercial Property, Construction, Hotels) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PL-8, PS-8, RA-3, SA-4, SA-9, SR-6, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.SC-05, GV.OV-01, ID.RA-01, ID.IM-01, PR.IR-01 |
| Regulatory drivers | CISA CPG 2.0 goals 1.A-1.E (voluntary, adopted); PCI DSS v4.0.1 Req. 12.1, 12.4, 12.8; FAR 52.204-21 and 32 CFR Part 170 (Construction); Reg S-K Item 106 |
| Division supplements | Commercial Property (v2026); Construction (v2025, BTI section due 2026-12-31); Hotels (v2025, building OT section due 2026-12-31). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, covering office IT and building operational technology (OT), assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects tenants, guests, workers, and the data and buildings the group is trusted with.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff); all systems and data the group owns or operates, including building automation, access control, and video systems; and systems operated for the group by suppliers, including **divisions that supply services to other divisions**.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy and POL-03; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group OT security lead | Owns the OT security standard, OT segmentation, OT monitoring, and OT vulnerability management |
| Group Chief Risk Officer | Owns the group risk register and the enterprise risk roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification, biometric and video rules, and state privacy compliance |
| Group General Counsel | Owns supplier and intercompany agreements and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions; the Construction president is the CMMC Affirming Official |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Hotels payment security lead; Commercial Property controller | Own PCI DSS compliance for their divisions |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0. The CISA CPG 2.0 goals, tailored with NIST SP 800-82 Rev. 3, are the group baseline for building OT. The program must also meet the binding duties of each division (PCI DSS, federal contract clauses) and of the group (SEC disclosure, state law). (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program, and the Group OT security lead for OT. Each division must name a security and compliance lead. Hotels must name a payment security lead. Construction must name its CMMC Affirming Official in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Life-safety risks rated High (heat, ventilation, egress, fire alarm interfaces) must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. For every system that holds Restricted or Confidential information or controls a building, the owning division must document which controls it inherits and which remain with it, and confirm that documentation every year. This includes systems one division runs for another. (PL-2; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, documented by HR. (PS-8; GV.RR-04)

4.8 **Internal suppliers.** A division that provides IT or OT services to another division (for example, the BTI unit's integrator services) must be treated as a supplier. It must have a written intercompany agreement with security terms (incident notice to the group SOC within 24 hours, access only through group identity and the OT remote access gateway, credentials held in the group vault, data handling, and the right to assess), and its tools must run inside the group landing zone. Group internal audit must assess it each year. (SA-4; SA-9; SR-6; GV.SC-05)

4.9 **External suppliers.** No supplier may access group systems or hold Restricted or Confidential information without the group security addendum (including incident notice within 72 hours) and a security review. A supplier may not enable a new analytics, biometric, or automated control feature in a group system without approval under 4.13. (SA-4; SA-9; GV.SC-05)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.12 Security policies, risk analyses, assessments, and required actions must be retained for at least 6 years, or longer where a contract or law requires. (SI-12)

4.13 **AI systems.** No AI system that processes Restricted or Confidential information, makes or supports decisions about people, or can change building operations may be deployed or materially changed (including a vendor enabling a feature) without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.14 **OT security standard.** Building automation, access control, and video systems must follow the group OT security standard (zones and conduits per NIST SP 800-82 Rev. 3). New and renovated buildings must meet it before occupancy. Existing buildings and hotels must meet it by the dates in the OT roadmap, and until then must operate under the compensating controls the Group OT security lead sets. (PL-8; PR.IR-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), annual supplement attestations, the OT program metrics, and the PCI DSS and CMMC assessments.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); OT security standard; CISA CPG 2.0.
