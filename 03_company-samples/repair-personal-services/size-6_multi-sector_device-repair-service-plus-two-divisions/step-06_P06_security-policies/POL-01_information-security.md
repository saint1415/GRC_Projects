# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Device Repair, Electronics Retail, IT Support Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-3, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory drivers | N81-R01 (15 U.S.C. 45); N81-R02 (Fla. Stat. 501.171(2)); N81-R03 and N44-45-R01 (PCI DSS v4.0.1 Req. 12.1, 12.4, 12.8); N54-R06 (45 CFR 164.308(a)(1), (a)(2), (a)(8), (b)(1); 164.316) for IT Support; N52-R08 |
| Division supplements | Device Repair supplement (v2024, re-alignment due 2026-11-30); Electronics Retail supplement (v2026); IT Support supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers' information and devices, cardholder data, managed customers' systems and data, and the systems that hold them.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff), all systems and data the group owns or operates, customer devices in the group's custody, and systems operated for the group by vendors, service providers, and subcontractors.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber, privacy, and AI risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G4; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Owns data classification, purposes, retention, and the customer data access standard |
| Group General Counsel | Owns contracts, the notification matrix, and external notices |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads (Device Repair CISO, Electronics Retail CISO, IT Support security and compliance lead) | Maintain division supplements and registers; own their division's PCI DSS, HIPAA, and SOC 2 duties; accept Low risks |
| IT Support HIPAA Security Official and Privacy Official | Designated in writing for the division's business associate services (45 CFR 164.308(a)(2)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that also meets PCI DSS v4.0.1 for both merchants and the HIPAA Security Rule for IT Support's business associate services. (PM-1; GV.PO-01; PCI DSS 12.1; 164.316)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead, and IT Support must designate its HIPAA Security Official and Privacy Official in writing. Executive responsibility for each merchant's PCI DSS compliance must be assigned in writing. (PM-2; GV.RR-02; PCI DSS 12.4; 164.308(a)(2))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks that would expose customer device content or card data at scale must be treated, not accepted, when rated High. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. Where a division operates inside another division's sites (the in-store repair counters), the supplement must say which division's rules apply to what. (PL-1; GV.PO-02; PCI DSS 12.1.2)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each system and site that holds customer, card, or managed customer data, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; CA-2; GV.RR-02; PCI DSS 12.8.5)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm. Misuse of a customer's device or its content is a serious violation. HR must document every sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.8 **No terms, no data, no code.** No vendor, service provider, or subcontractor may handle customer data, cardholder data, or managed customers' data, and **no third-party software may run on bench workstations, counter devices, or managed customer endpoints**, until the vendor has signed security terms (including breach notice, data use, and, for software, update integrity) and passed a security review proportionate to its access. Vendors that handle ePHI for IT Support must sign a business associate (subcontractor) agreement first. (SA-4; SA-9; SR-3; GV.SC-05; GV.SC-06; PCI DSS 12.8.2; 164.308(b)(1))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 164.308(a)(8))

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a PCI DSS requirement for an in-scope system or a HIPAA required specification. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))

4.12 **AI systems.** No AI system that processes customer data or device data, interacts with customers, or acts on customer systems may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, the QSA ROCs, the IT Support SOC 2 examination, and quarterly access certifications.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10).
