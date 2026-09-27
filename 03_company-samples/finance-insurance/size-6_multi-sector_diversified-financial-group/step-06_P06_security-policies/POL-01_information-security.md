# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Banking, Financial Software and Data Services, Commercial Real Estate) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Holding company board risk committee (2026-09-10); adopted as the bank's information security program by the bank board risk committee (2026-09-10) |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-6, CA-2, CA-2(1), CA-7, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-01 |
| Regulatory basis | 12 CFR 30 App. B II and III (bank); 12 CFR 225 App. F II and III (holding company and nonbank subsidiaries); 12 CFR 30 App. D (risk governance framework); 12 CFR 53.3, 53.4, 225.302 |
| Division supplements | Banking supplement (v2026); Financial Software supplement (v2025, aligned); Commercial Real Estate supplement (the acquired company's 2023 policies, **re-issue due 2026-11-30**). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers' information, client institutions' data, and the integrity of payments.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its subsidiaries (employees, contractors, and temporary staff), all systems and data the group owns or operates, and systems operated for the group by service providers, **including affiliates that provide services to one another** (for example, the Financial Software division's platform for the bank).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Holding company board risk committee | Approves this policy and the group program (12 CFR 225 App. F III.A); accepts Very High risks |
| Bank board risk committee | Adopts the program as the bank's (12 CFR 30 App. B III.A); approves the bank's risk governance framework and risk appetite (App. D) |
| Group CISO | Owns the program and group policies; operates common controls (SYS-G1 to SYS-G4); serves as the bank's information security officer; co-accepts High risks |
| Group Chief Risk Officer | Leads independent risk management; owns the group risk register and roll-up; co-accepts High risks |
| Head of Technology and Cyber Risk | Second-line challenge of cyber, technology, and third-party risk |
| Chief Audit Executive | Independent assessment of common controls and division samples |
| Group General Counsel | Contracts, intercompany agreements, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads (including the Financial Software division CISO) | Maintain division supplements and registers; accept Low risks |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one written information security program aligned to NIST CSF 2.0 that meets 12 CFR 30 App. B for the bank and 12 CFR 225 App. F for the holding company and every nonbank subsidiary. Each subsidiary is covered by including it in this program (App. F II.A). (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. The bank board designates the bank's information security officer; the Financial Software division, which issues SOC reports to clients, has its own CISO reporting to the Group CISO. (PM-2; GV.RR-02; App. B III.A.2)

4.3 Each division and corporate must complete a risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; App. B III.B; App. F III.B)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the holding company board risk committee (and the bank board risk committee for bank risks); Very High, the board risk committee only. High risks to payment integrity or customer harm must be treated, not accepted. Every acceptance is compared to the bank's risk appetite statement. (PM-9; GV.RM-01; App. D II.E)

4.5 **Three lines.** First-line owners assess and treat their risks. The Head of Technology and Cyber Risk independently challenges High ratings, acceptances, and authorizations. Group internal audit must not design or operate the controls it assesses. (CA-2(1); GV.RR-02; App. D I.E.7-8)

4.6 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.7 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems that holds customer information or supports a critical process, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.8 **Service providers, including affiliates.** No service provider may access customer information, client institution data, or payment systems, or perform services the bank depends on, without: due diligence before selection; a written contract with security measures, incident notice to the group SOC within 24 hours, and audit or assurance rights; and monitoring at least annually (review of SOC reports or equivalent, exception follow-up, and mapping of complementary user entity controls). **Affiliates providing services to the bank are treated as critical vendors** under this statement, with the same files and reviews as outside vendors. Each bank service provider that serves the bank must hold the bank's designated point of contact for 12 CFR 53.4 notices. (SA-9; SA-4; SR-6; GV.SC-05; GV.SC-07; App. B III.D.1-3; Supplement A II.A.2)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; App. B III.C.3; App. F III.C.3)

4.10 **Board reporting.** The Group CISO must report to the holding company board risk committee and the bank board risk committee at least annually on the program's status, covering risk assessment, risk decisions, service provider arrangements (including affiliates), testing results, security events and responses, and recommended changes. (PM-9; GV.OV-01; App. B III.F; App. F III.F)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less.

4.12 **Records.** Security policies, risk assessments, assessments, incident records, and required actions must be retained for at least 5 years, or longer where a regulation or the group records schedule requires. (SI-12)

4.13 **AI and models.** No AI system or model that uses customer information or client data, or that makes or supports decisions about customers or applicants, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). Models used in credit decisions must also pass independent validation by model risk management and fair lending review before production use and after any material change. (RA-3; PL-2; GV.RM-01)

4.14 **Acquisitions.** Every acquired business must be brought under this policy within 12 months: identity and email, policies and supplement, payment controls, data retention, and control inheritance. (CA-7; ID.IM-03; App. F III.E)

4.15 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Violations are handled under 4.15. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); 12 CFR 30 App. B and App. D; 12 CFR 225 App. F.
