# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (GovTech Integration, IT Consulting, Government Software Products) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), after major changes, acquisitions, or incidents, and within 60 days of a new CJIS Security Policy version |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-3, PS-7, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Agency and federal drivers | CJISSECPOL v6.1 (Security Addendum sec. 3.01; PS-3; SA-9); Pub. 1075 Exhibit 7 and sec. 2.C.3; DFARS 252.204-7012(b) and 32 CFR Part 170; 45 CFR 164.308(a)(1), (a)(2), (b); 18 U.S.C. 2721 |
| Division supplements | GovTech Integration supplement (v2026); IT Consulting supplement (v2024, re-issue due 2026-11-30); Government Software Products supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and division supplement its authority. The program protects the agency, federal, and customer data the group holds and the systems that hold it, and it is how the group meets the security terms agencies and federal customers place in their contracts.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and subcontractor staff), including staff who joined through acquisitions; all systems and data the group owns or operates; systems operated for the group by service providers; and agency-owned systems that group staff use under contract.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and AI risk; approves this policy, POL-03, and the Group AI Standard; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group General Counsel | Owns contracts, flowdowns, and the group notification matrix |
| Group public sector compliance director | Owns the agency contract obligations register (Security Addendum, Exhibit 7, DPPA, state contract terms) and checks each new CJIS Security Policy version |
| Group Chief Privacy Officer | Owns data classification, privacy, and state breach laws |
| Division presidents | Accept Moderate risks; the IT Consulting president is the CMMC Affirming Official |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| GovTech HIPAA Security Official; IT Consulting security and compliance lead | HIPAA Security Officials for their divisions' business associate work (45 CFR 164.308(a)(2)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents within 1 hour |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 and built on the NIST SP 800-53 Rev. 5 Moderate baseline, so that every system that holds agency or federal data can meet the baseline its contracts require. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division that acts as a HIPAA business associate must designate a Security Official in writing, and the IT Consulting president must act as CMMC Affirming Official for the division's CAGE codes. (PM-2; GV.RR-02; 164.308(a)(2); 32 CFR 170.22)

4.3 Each division and corporate must complete a risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. A risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or DFARS 252.204-7012 term must not be accepted at any level; it must be treated or the regulated data removed. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and must cover acquired staff from the date of the acquisition. Each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog (P02). Each division must document, for each system that holds agency, federal, or customer regulated data, which controls it inherits and which remain with the division, and must confirm that documentation every year and before any external assessment (CSA audit, IRS review, CMMC, FedRAMP, GovRAMP, or SOC 2). (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Screening before access, wherever the person works.** No one, including corporate shared-service staff and subcontractor staff, may receive access to an environment holding CJI, FTI, CUI, or motor vehicle records until the screening, training, and signed agreements that the governing contract requires are complete for every state or program involved. The group screening register is the single record of this status. (PS-3; PS-6; PS-7; GV.RR-04; CJISSECPOL v6.1 PS-3, SA-9; Pub. 1075 Exhibit 7 I(2))

4.8 **Sanctions.** Workforce members who violate security policies, or who look up or disclose records without a business need, must be sanctioned in proportion to intent and harm. Agencies must be told when a sanction involves their data. (PS-8; GV.RR-04)

4.9 **Flowdown before data.** No vendor, subcontractor, or intercompany service provider may receive agency, federal, or customer regulated data until the group has confirmed the security review and the contract terms the governing agreement requires: the CJIS Security Addendum, IRS approval and unchanged Exhibit 7 terms for FTI work, DFARS 252.204-7012 flowdown for covered defense information, business associate or subcontractor terms for PHI, and U.S.-only processing where required. For FTI, the agency's IRS notification must name the service before it receives FTI. (SA-9; SA-4; GV.SC-05; Pub. 1075 Exhibit 7 I(8), Exhibit 6; DFARS 252.204-7012(m); 164.308(b)(2))

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a contract or legal requirement. (PL-1)

4.12 **Retention.** Security policies, assessments, and incident records must be kept for at least 7 years, which covers the Pub. 1075 audit record period and the 6-year HIPAA documentation period. (SI-12; Pub. 1075 sec. 4 AU-11; 164.316(b)(2)(i))

4.13 **AI systems.** No AI system that processes agency, federal, or customer regulated data, or that makes or supports decisions about people, may be deployed, released to a beta, or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under 4.8. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, the screening register, and agency and federal assessments.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); group notification matrix (P08).
