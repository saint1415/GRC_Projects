# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Cloud Software, Technology Consulting, Payments and Payroll) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, RA-8, SA-4, SA-9, CA-2, CA-3, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-01 |
| Regulatory anchors | FTC Act Section 5 (N51-R01); 16 CFR 314.4(a), (b), (f), (i) for Payments and Payroll (N52-R03); 48 CFR 52.204-21 for consulting's federal work (N54-R04); 45 CFR 164.308(a)(1), (a)(8), (b) for consulting's business associate work (N54-R06); PCI DSS 12; Reg S-K Item 106 (N51-R08) |
| Division supplements | Cloud Software (v2026); Technology Consulting (v2023, re-alignment due 2026-12-31); Payments and Payroll (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers', workers', clients', merchants', and the group's own information and the systems that hold it.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and interns), including the consulting firm acquired in 2025; all systems and data the group owns or operates; and systems operated for the group by service providers, sub-processors, and affiliates.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and AI risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification, data-use limits, and privacy impact assessments across divisions |
| Group General Counsel | Owns customer, client, intercompany, and sub-processor agreements and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads (division CISOs where they exist) | Maintain division supplements and registers; accept Low risks |
| Payments and Payroll division CISO | The **Qualified Individual** for the division's information security program (16 CFR 314.4(a)); reports to the division board at least annually (314.4(i)) |
| Technology Consulting security and compliance lead | HIPAA Security Official for the division's business associate work |
| Technology Consulting federal contracts compliance officer | FAR 52.204-21 safeguarding and flowdown |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that also meets each division's binding requirements: FTC Act Section 5 and SOC 2 commitments (Cloud Software), FAR 52.204-21 and HIPAA business associate duties (Technology Consulting), and the FTC Safeguards Rule and PCI DSS (Payments and Payroll). (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Payments and Payroll must designate its Qualified Individual in writing, and Technology Consulting must designate its HIPAA Security Official in writing. (PM-2; GV.RR-02; 16 CFR 314.4(a); 45 CFR 164.308(a)(2))

4.3 Each division and corporate must complete a written risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. The assessment must cover the division's data wherever it is held, **including data held for it by another division**. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 16 CFR 314.4(b))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks rated High that could leave workers unpaid or expose payroll, payment, or health data must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm, with HR documenting every sanction. (PS-8; GV.RR-04)

4.8 **Service providers, sub-processors, and affiliates.** No vendor, sub-processor, or affiliate may store, process, or access another party's customer, client, payroll, payment, or health data for a division without (a) a security review before access, (b) a written agreement with security, notice, and audit terms, and (c) periodic reassessment based on risk. **An affiliate division providing a service is a service provider for this purpose.** Cloud Software must not add a sub-processor until legal has confirmed the DPA notice period has run. (SA-4; SA-9; CA-3; GV.SC-05; GV.SC-07; 16 CFR 314.4(f); 45 CFR 164.308(b))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. Divisions must also maintain their external assurance (SOC 2, SOC 1, PCI DSS Report on Compliance, ISO/IEC 27001) on schedule. (CA-2; CA-7; ID.IM-01; 45 CFR 164.308(a)(8))

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 Security policies, procedures, risk assessments, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. (SI-12)

4.12 **AI systems.** No AI system that processes customer, worker, client, applicant, or payment data, or that makes or supports decisions about people, may be deployed or materially changed without registration in the group AI inventory, a privacy impact assessment, and approval under the Group AI Standard (P10). (RA-3; RA-8; GV.RM-01)

4.13 **Public and contractual statements.** Every security, privacy, or AI statement on the trust center, product pages, questionnaires, DPAs, or SOC 2 system description must have a named owner and supporting evidence, and must be reviewed each quarter against assessment results. A statement found untrue must be corrected within 10 business days. (PL-4; GV.OC-03; N51-R01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and quarterly statement reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); notification matrix (P08).
