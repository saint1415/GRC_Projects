# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc., its corporate shared services, and all subsidiaries in the Insurance and Health Care Services divisions |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-30, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12, SR-6 |
| CSF 2.0 | GV.OC-03, GV.OC-05, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.RM-03, GV.OV-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory drivers | N55-R01 (Item 106(b)-(c)); N55-R03; N55-R06 and N62-R01 (group health plan); N52-R07 (Model #668 sec. 4A, 4C, 4E, 4F); N62-R01 (164.308(a)(1), (a)(2), (a)(8), (b)(1); 164.316); Fla. Stat. 628.801(2) |
| Division supplements | Insurance supplement (v2025); Health Care Services supplement (v2023, re-issue due 2026-11-30); Group health plan sponsor procedures (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign accountability at group and division level, and give every other group policy and every division supplement its authority. The program protects employees', policyholders', claimants', and patients' information, the group's financial reporting and payments, and the systems that hold them.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its subsidiaries (employees, contractors, and independent adjusters), all systems and data the group owns or operates, and systems operated for the group by vendors. It covers the holding company's own services to its subsidiaries, the group health plan's PHI held by the plan sponsor, the insurers' nonpublic information, and Health Care Services' PHI.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Audit committee | Oversees internal control over financial reporting and group internal audit |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register, enterprise risk management roll-up, and the Fla. Stat. 628.801(2) enterprise risk report; co-accepts High risks |
| Group CIO | Owns the Shared Corporate Services Platform; accepts Moderate group risks |
| Group Chief Privacy Officer | Owns data classification and cross-division data sharing rules |
| Group General Counsel | Owns intercompany agreements, business associate agreements, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Insurance information security officer | Responsible for the insurers' information security program (Model #668 sec. 4C(1)); maintains the Insurance supplement |
| Health Care Services HIPAA Security and Privacy Officers | Designated for the covered entity (45 CFR 164.308(a)(2); 164.530(a)) |
| Group health plan security and privacy officials | Group security governance director and Group benefits director |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the HIPAA Security Rule for Health Care Services and the group health plan, and the insurance data security laws that bind the insurers. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each regulated entity must designate its own responsible officials in writing: the insurers' information security officer, Health Care Services' HIPAA Security and Privacy Officers, and the group health plan's security and privacy officials. (PM-2; GV.RR-02; Model #668 sec. 4C(1); 164.308(a)(2))

4.3 The group and each division must complete a risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that sit in shared services, cross divisions, or need a group decision must roll up to the group register. Group High risks that could affect the insurers must be included in the annual enterprise risk report. (RA-3; PM-9; ID.RA-01; GV.RM-03; Fla. Stat. 628.801(2))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead (for group risks, the group security governance director); Moderate, the division president (for group risks, the Group CIO); High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Patient-safety risks and risks to claimants' benefit payments rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.6 **Common controls.** Common control providers must maintain the common control catalog. Each division must document, for each system that holds regulated data, which controls it inherits and which remain with the division, including systems from acquisitions, within 90 days of closing. (PL-2; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm, and every sanction documented. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.8 **Intercompany services are third-party services.** When the holding company provides a service that stores, processes, or accesses a subsidiary's regulated information:
- (a) the intercompany agreement must include a security schedule (safeguards, incident notice within 24 hours of the group SOC's knowledge, audit rights, and return or destruction of data);
- (b) the receiving division must perform due diligence each year, which may rely on the SCSP affiliate assurance report (P09);
- (c) where the subsidiary is a HIPAA covered entity or plan, a business associate agreement must be in place before PHI is handled, and it must be reviewed when a new service (such as an AI feature) begins to handle that PHI.
(SA-9; SA-4; PM-30; GV.SC-05; GV.SC-06; Model #668 sec. 4F; 164.308(b)(1))

4.9 **Outside vendors.** No vendor may handle regulated information without a security review, contract security terms, and, for PHI, a business associate agreement. Tier 1 vendors are reviewed each year, including mapping of complementary user entity controls in their SOC reports. (SA-9; SR-6; GV.SC-07)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 164.308(a)(8); Model #668 sec. 4C(5))

4.11 **Board and regulated-entity reporting.** The Group CISO reports to the board risk committee each quarter. Each insurer's board receives an annual written report on its program, including its Third-Party Service Provider arrangements with the holding company. (PM-9; GV.OV-01; Model #668 sec. 4E(2); Item 106(c))

4.12 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the register, and limited to 12 months or less. (PL-1)

4.13 **Retention.** Security policies, risk assessments, and assessments must be kept at least 6 years (164.316(b)(2)(i)); cybersecurity event records at least 5 years (Model #668 sec. 5D); and SOX evidence as the retention schedule requires. (SI-12)

4.14 **AI systems.** No AI system that processes Restricted data or makes or supports decisions about employees, policyholders, claimants, or patients may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and quarterly access reviews.

## 6. Exceptions
Exceptions follow section 4.12.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10).
