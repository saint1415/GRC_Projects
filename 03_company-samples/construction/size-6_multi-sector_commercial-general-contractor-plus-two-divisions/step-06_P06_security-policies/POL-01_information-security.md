# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Construction, Property, A&E) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 (approved 2026-09-15) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, CMMC assessment results, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-5, SR-6, CA-2, CA-7, SI-12, AC-5, SC-7, MA-4 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-04, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory drivers | N23-R01 FAR 52.204-21; N23-R02 FAR 52.204-25; N23-R03 DFARS 252.204-7012; N23-R04 32 CFR Part 170 and DFARS 252.204-7021; N54-R05 (A&E); N53-R04 PCI DSS and N53-R05 SEC disclosure (Property and group) |
| Division supplements | Construction supplement (v2026); Property supplement (v2024, re-issue due 2026-12-31); A&E supplement (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects federal contract information (FCI), controlled unclassified information (CUI), payment instructions, personal information, client facility security details, and the building systems the group owns or installs.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, craft workers, contractors, and temporary staff), all systems and data the group owns or operates, systems operated for the group by service providers, and systems the group installs or manages for clients (the TSSI managed service). It covers both federal contracting entities (Cris Santos Construction, LLC and Cris Santos Design, Inc.) and every contractor information system they use to perform federal contracts.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy and POL-03; accepts Very High risks |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| Group CISO | Owns the program and group policies; operates common controls (SYS-G1 to SYS-G3, SYS-G5, SYS-G6); co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and the ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Financial Officer and Group Treasurer | Own the payment factory (SYS-G4) and the payment-instruction rules in 4.15 |
| Group General Counsel | Owns the notification matrix, contract and flowdown terms, and review of SPRS entries and affirmations |
| Director of Federal Contracts Compliance | Runs the CMMC program for both contracting entities: scoping, self-assessments, SPRS entries, subcontractor status checks |
| Division presidents | Accept Moderate risks. The Construction and A&E division presidents are the **CMMC Affirming Officials** for their entities (32 CFR 170.22(a)(1)) |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group internal audit | Independently assesses common controls once and samples division controls; reports to the board audit committee |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

**Overlapping roles and compensation.** The Director of Federal Contracts Compliance prepares the CMMC self-assessments that the division presidents affirm. Because the person who prepares the evidence also influences the score, no affirmation may rest on that evidence alone (4.9).

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the federal contract obligations of each contracting entity (FAR 52.204-21, FAR 52.204-25, DFARS 252.204-7012, and DFARS 252.204-7021) and the obligations of each division's regulators and customers. (PM-1; GV.PO-01; GV.OC-03)

4.2 The Group CISO is accountable for the program. Each federal contracting entity must designate its CMMC Affirming Official in writing. (PM-2; GV.RR-01; GV.RR-02; 32 CFR 170.22)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. High risks to life safety (jobsite safety systems, building life-safety interfaces) and to federal contract eligibility must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Third parties, subcontractors, and subconsultants.** No vendor, subcontractor, or subconsultant may receive FCI, CUI, payment data, or client facility security details without a security review and contract terms that carry the required flowdowns (FAR 52.204-21(c); FAR 52.204-25(e); DFARS 252.204-7012(m); DFARS 252.204-7021(f)(1)). **Before award**, procurement must confirm in SPRS that the subcontractor or subconsultant has a current CMMC status at the level appropriate for the information being flowed down (DFARS 252.204-7021(f)(2); 32 CFR 170.23). Without that status, CUI may be shared only by giving the subcontractor's named users enclave guest accounts. (SA-9; SA-4; SR-6; GV.SC-05; GV.SC-06)

4.9 **Evaluation and affirmations.** Group internal audit must assess common controls at least annually and sample each division's controls. A CMMC self-assessment score may be entered in SPRS, and an Affirming Official may affirm, only after the evidence binder has been independently tested by group internal audit or an outside assessor, and after the Group General Counsel has reviewed it. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 32 CFR 170.22)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may allow CUI outside the enclave or covered equipment under 4.14. (PL-1)

4.11 **Retention.** Security policies, risk analyses, assessments, and required actions must be kept for at least 6 years. CMMC assessment artifacts must be kept for 6 years from the CMMC status date (32 CFR 170.15(c)(2); 170.16(c)(4)). (SI-12; GV.PO-02)

4.12 **AI systems.** No AI system that processes FCI, CUI, bid pricing, personal information, or client data, or that supports decisions about people, subcontractors, designs, or building operations, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Building and installed systems.** Building automation, access control, video, and parking pay stations at owned properties, and client systems the TSSI unit manages, must follow the group building systems standard: segmented networks separated from corporate and payment networks, integrator and technician remote access only through group PAM with named accounts and session recording, default credentials changed before use, configuration backups held by the group, and logs sent to the group SOC. (SC-7; MA-4; SI-4; GV.SC-05)

4.14 **Section 889.** No division may procure, specify, install, or use covered telecommunications equipment or services, including video surveillance equipment from covered manufacturers or their subsidiaries and affiliates (FAR 52.204-25(b)). The Group Chief Risk Officer maintains a **group approved-manufacturer list** that every division uses, including for private-label products, A&E specifications, and Property procurement. A reasonable inquiry must be documented before each annual SAM representation (FAR 52.204-26). Covered equipment found in use must be reported under POL-03 4.7. (SR-5; GV.SC-04)

4.15 **Payment instructions.** A change to any bank or remittance detail (subcontractor, supplier, vendor, tenant refund, or the group's own remittance details) may be made only in the payment factory (SYS-G4), after a call-back to a phone number already on file and approval by a second person. Divisions must not keep separate vendor masters that bypass this rule. The group will never change its own remittance details by email, and every owner and tenant must be told so in writing. (AC-5; SI-10; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the CMMC self-assessments, the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); regulation-by-division matrix (P03); group building systems standard; group approved-manufacturer list; Group AI Standard (P10); FAR 52.204-21; FAR 52.204-25; DFARS 252.204-7012 and 252.204-7021; 32 CFR Part 170.
