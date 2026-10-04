# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (IT Distribution, Logistics and Warehousing, Online Retail) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board audit and risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PM-30, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, SI-12, SR-1, SR-2, SR-3, SR-5, SR-6 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-01, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01 |
| Regulatory drivers | N42-R03 (SP 800-171 R2 3.12.1 to 3.12.4); N42-R02 (32 CFR 170.22); N42-R05 (52.204-25); DFARS 252.246-7008; N44-45-R01 (PCI DSS v4.0.1 Req. 12.1, 12.4); N42-R07 (17 CFR 229.106) |
| Division supplements | IT Distribution supplement (v2026); Logistics supplement (v2024, re-alignment due 2026-11-30); Online Retail supplement (v2026). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers', clients', consumers', and the Government's information, and the integrity of the products the group distributes.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary agency workers), all systems and data the group owns or operates, including DC operational technology, and systems operated for the group by service providers. It covers CUI and FCI, cardholder data, consumer and seller personal information, 3PL client data, and all other group information, and the supply chain for products the group sells.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit and risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group CMMC program director | Owns the CMMC scope, SPRS entries, and assessment readiness |
| Group supply chain risk director | Owns the C-SCRM program, the approved supplier list, and the Section 889 screening list |
| Group Chief Privacy Officer | Owns data classification for personal information and the CCPA program |
| Group General Counsel | Owns contract flowdown, the notification matrix, and external notices |
| Division presidents | Accept Moderate risks; the IT Distribution president is the CMMC Affirming Official |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the contract, regulatory, and industry requirements of every division, including NIST SP 800-171 Rev. 2 for CUI and PCI DSS for cardholder data. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. Each division must name a security and compliance lead in writing. (PM-2; GV.RR-02)

4.3 Each division and corporate must complete a risk assessment at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; SP 800-171 R2 3.11.1)

4.4 **Risk acceptance authority:** Very Low and Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board audit and risk committee; Very High, the board audit and risk committee only. Risks that could cause worker injury or put covered or tampered equipment into a DoD system must be treated, not accepted, at High. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **System security plans.** Every system that stores, processes, or transmits CUI, FCI, or cardholder data must have a current security plan describing its boundary and how each requirement is met. (PL-2; SP 800-171 R2 3.12.4)

4.8 **Assessments and attestations.** Group internal audit must assess common controls at least annually and sample each division's controls. No SPRS score, CMMC affirmation, PCI DSS attestation, or SOC report assertion may be submitted unless a documented assessment of the full scope supports it. (CA-2; CA-7; ID.IM-01; 32 CFR 170.22)

4.9 **Service providers.** No service provider may store, process, or transmit CUI, FCI, cardholder data, or personal information for the group without a security review and contract terms that carry the group's obligations. Cloud services that would hold CUI must be FedRAMP Moderate authorized or have documented equivalency before use. (SA-9; SA-4; GV.SC-05; 252.204-7012(b)(2)(ii)(D); PCI DSS 12.8)

4.10 **Supply chain: sourcing.** Products for federal orders and integration jobs must come from the original manufacturer or its authorized suppliers first; other sources may be used only with written approval of the Group supply chain risk director and the notices the contract requires. No broker may be used for any stock until it passes the group broker assessment. (SR-5; SR-6; GV.SC-06; 252.246-7008(b))

4.11 **Supply chain: screening.** Every SKU must have a manufacturer of record before it can be sold. SKUs whose manufacturer is covered under FAR 52.204-25 must be blocked on all federal orders and on refurbished stock offered to resellers. (SR-3; RA-9; GV.SC-05; 52.204-25(b)(1))

4.12 **Supply chain: receiving.** Every DC must validate OEM serials and inspect for tampering on receipt, and must quarantine any item that fails until the Group supply chain risk director releases it. (SR-10; SR-11; GV.SC-07)

4.13 **Flowdown.** Contract clauses that require flowdown (including DFARS 252.204-7012, 252.204-7021, 252.246-7008, and FAR 52.204-25) must be included in the relevant subcontracts and supplier terms, and subcontractor CMMC status must be verified before award. (SA-4; SR-3; 252.204-7021(f))

4.14 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may waive a contract clause or a legal deadline. (PL-1)

4.15 Security policies, procedures, risk assessments, assessments, and records of actions taken must be retained for at least 6 years. (SI-12)

4.16 **AI systems.** No AI system that makes or influences purchasing, pricing, customer, worker, or seller decisions, or that processes CUI, FCI, cardholder data, or personal information, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled through the sanctions process: workforce members who violate security policies are sanctioned in proportion to intent and harm, and HR documents every sanction (PS-8; GV.RR-04). Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, quarterly access certification, the PCI DSS ROC, and the CMMC assessment.

## 6. Exceptions
Exceptions follow section 4.14.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); C-SCRM plan; Group AI Standard (P10).
