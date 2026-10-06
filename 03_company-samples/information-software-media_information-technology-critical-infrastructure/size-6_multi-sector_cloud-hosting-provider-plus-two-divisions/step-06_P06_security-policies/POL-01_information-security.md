# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Cloud Hosting, Managed IT and Consulting, Payment Processing) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, SR-6, CA-2, CA-7, SI-12, AC-4, CM-7 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory programs | FedRAMP Consolidated Rules for 2026 (G1); DFARS 252.204-7012 and CMMC (Managed IT); FTC Safeguards Rule 16 CFR 314.4 and PCI DSS v4.0.1 (Payment Processing); HIPAA business associate duties (Cloud Hosting, Managed IT); bank service provider rule; 28 CFR Part 202; SEC Item 106 |
| Division supplements | Cloud Hosting (v2026); Managed IT (v2024, re-alignment due 2026-11-30); Payment Processing (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers', clients', agencies', merchants', and consumers' information and the systems that hold or can reach it.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and interns), all systems and data the group owns or operates, systems operated for the group by vendors, and **services one division provides to another**.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and AI risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group Chief Privacy Officer | Owns data classification and vendor screening under 28 CFR Part 202 |
| Group General Counsel | Owns intercompany agreements, BAAs, ESP terms, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Cloud Hosting division CISO | Division security lead; FedRAMP senior security official for G1 |
| Managed IT division security and compliance lead | Division security lead; HIPAA Security Official for the division's business associate work; CMMC program owner |
| Payment Processing division CISO | Division security lead; **Qualified Individual** under 16 CFR 314.4(a); PCI DSS program owner |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents within 1 hour |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets every regulatory program that applies to a division (FedRAMP for G1; DFARS 252.204-7012 and CMMC for Managed IT; 16 CFR Part 314 and PCI DSS for Payment Processing; HIPAA for business associate work). (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must designate in writing: a division security lead; for Cloud Hosting, the FedRAMP senior security official who receives Emergency messages from the FedRAMP Security Inbox; for Payment Processing, the Qualified Individual (16 CFR 314.4(a)); for Managed IT, the HIPAA Security Official for its business associate work. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 16 CFR 314.4(b))

4.4 **Risk acceptance authority:** Very Low and Low, the division security lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. A High risk to federal customer data, CUI, cardholder data, or a bank's covered services must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security lead must attest alignment every year. Where a supplement conflicts with group policy, group policy governs. (PL-1; GV.PO-02; 45 CFR 164.316(b)(2)(iii))

4.6 **Common controls.** Common control providers must maintain the common control catalog. Each division must document, for each of its systems in a regulated scope (G1, the CDE, the CUI enclave, systems holding PHI), which controls it inherits and which remain its responsibility, and confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Intercompany services.** When one division provides a service that can reach another division's regulated data or systems (for example, SL-1 hosting of the CDE, RMM management of Payment Processing servers, or partner-operator access to managed-hosting tenants), the two divisions must treat it as a service provider relationship: a written intercompany agreement with security and incident notice terms, a responsibility matrix, and an annual assessment by the receiving division. This includes the terms required by 16 CFR 314.4(f) and PCI DSS Requirements 12.8 and 12.9, and BAAs or ESP terms where they apply. (SA-9; SA-4; GV.SC-05)

4.9 **External vendors.** Vendors must be tiered by the data and systems they can reach. Tier 1 vendors must accept incident notice within 24 hours and annual assurance review. Every vendor and contractor with access to bulk U.S. sensitive personal data or government-related data must be screened for covered-person status under 28 CFR Part 202 before access and every year. (SA-9; SR-6; GV.SC-06)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Each division must also complete its external assessments: the annual FedRAMP independent assessment for G1, the PCI DSS assessment for the CDE, and the CMMC assessment the DoD subcontracts require. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a legal or contractual deadline. (PL-1)

4.12 Security policies, procedures, risk analyses, assessments, and required actions must be retained for at least 6 years from creation or last effective date, or longer where a rule or contract requires. (SI-12)

4.13 **AI systems.** No AI system that processes customer, client, agency, merchant, or consumer data, or that makes or supports decisions about them or takes actions in their systems, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). No AI system may take automated actions in G1, the CDE, or the CUI enclave without the written approval of that environment's owner. (RA-3; PL-2; GV.RM-01)

4.14 **Regulated environment boundaries.** Tooling that can act on many systems at once (RMM, run-command, fleet automation, SOAR) may reach G1, the CDE, or the CUI enclave only if the environment's owner has approved that tool and it is inside the environment's documented scope (FedRAMP minimum assessment scope, PCI DSS scope, or CMMC assessment scope). (AC-4; CM-7; GV.PO-01)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and the external assessments in 4.10.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); intercompany agreement template (Group General Counsel).
