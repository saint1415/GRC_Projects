# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Grocery Retail, Grocery Wholesale, Financial Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, CM-3, SC-18, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01, PR.PS-05 |
| Regulatory drivers | PCI DSS v4.0.1 Req. 12.1, 12.3, 12.4 to 12.8 as they apply to a merchant (N44-45-R01); FTC Safeguards Rule 16 CFR 314.4(a), (b), (f), (g), (i) (N44-45-R03); FTC Act Section 5 (N44-45-R02) |
| Division supplements | Grocery Retail supplement (v2026); Grocery Wholesale supplement (v2026); Financial Services supplement (v2024, re-alignment due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects customers' card and account data, cardholders' financial information, independent grocers' business data, and the systems that keep stores and distribution centers running.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff), all systems and data the group owns or operates, and systems operated for the group by service providers. It covers payment card data, Rewards Card and other Financial Services customer information, SNAP EBT data, consumer report information, customer and loyalty data, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber, privacy, and AI risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G4; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks |
| Group Chief Privacy Officer | Owns data classification, permitted uses, and affiliate data sharing rules |
| Group General Counsel | Owns intercompany agreements, service provider terms, and the notification matrix |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Grocery Retail CISO | Responsible for information security for the retail merchant (PCI DSS 12.1.4) and the annual ROC |
| Financial Services CISO | Qualified Individual under 16 CFR 314.4(a); reports in writing to the Financial Services board at least annually (314.4(i)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets PCI DSS for every merchant account in the group and the FTC Safeguards Rule for Financial Services. (PM-1; GV.PO-01; PCI DSS 12.1)

4.2 The Group CISO is accountable for the program. The Grocery Retail CISO is responsible for information security for the retail merchant, and Financial Services must designate a Qualified Individual in writing. (PM-2; GV.RR-02; PCI DSS 12.1.3, 12.1.4; 16 CFR 314.4(a))

4.3 Each division and corporate must complete a written risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; PCI DSS 12.3.1; 16 CFR 314.4(b))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Risks rated High that could expose card data or Financial Services customer information must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02; 16 CFR 314.4(g))

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each system that holds card data, Financial Services customer information, or customer data, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; CA-2; GV.RR-02; PCI DSS 12.8.5 for shared responsibilities; 16 CFR 314.4(d)(1))

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm, and HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Service providers.** No service provider, including an affiliate inside the group, may store, process, transmit, or affect the security of card data or Financial Services customer information without a written agreement with security terms and a security review before use, and an annual review of its compliance status after that. Third-party service providers for card data must be listed with the PCI DSS requirements each one manages. (SA-9; SA-4; GV.SC-05; PCI DSS 12.8; 16 CFR 314.4(f))

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. The retail merchant is also validated each year by a QSA ROC. (CA-2; CA-7; ID.IM-01; 16 CFR 314.4(d)(1))

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. No exception may reduce a PCI DSS requirement without a compensating control reviewed by the QSA. (PL-1)

4.11 Security policies, procedures, risk analyses, assessments, and incident records must be retained for at least 6 years from creation or last effective date, whichever is later. (SI-12)

4.12 **AI systems.** No AI system that uses customer, cardholder, or workforce data, or that makes or supports decisions about customers' prices, credit, or treatment in stores, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Payment pages.** Any web or app page on which a customer enters card data, Rewards Card data, or bank account data is a payment page. No script may be added to a payment page, by any division or through the group tag management service, unless the page owner approves it, records its justification, and its integrity is checked. Every payment page must have change and tamper detection that alerts the group SOC. (CM-3; SC-18; PR.PS-05; PCI DSS 6.4.3, 11.6.1)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the QSA ROC, the Qualified Individual's annual report, and the annual supplement attestations.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); PCI scope document and responsibility matrix; Financial Services written information security program.
