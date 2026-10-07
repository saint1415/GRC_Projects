# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Payment Processing, Payments Software Platform, Merchant Consulting) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO (Qualified Individual under 16 CFR 314.4(a)) |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after significant changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, CM-4, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory basis | 16 CFR 314.4(a), (b), (f), (g), (i); PCI DSS 12.1, 12.3, 12.4, 12.5, 12.8; SOC 2 CC1 to CC5 |
| Division supplements | Payment Processing supplement (v2026); Software division supplement (v2025, update due 2026-10-31); Merchant Consulting supplement (v2024 acquired-firm set, re-issue due 2026-11-30). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects cardholder data, merchants' and clients' information, and the systems that hold them.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff), all systems and data the group owns or operates, and systems operated for the group by service providers, including group affiliates that provide services to one another. It covers cardholder data in both cardholder data environments (the processor's and the gateway's), customer information under the FTC Safeguards Rule, merchant and client information, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks; receives the Qualified Individual's annual report |
| Group CISO | Owns the program and group policies; operates common controls (SYS-G1 to SYS-G5); Qualified Individual; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the Group AI council |
| Group General Counsel | Owns intercompany agreements, third-party contract terms, and the notification matrix |
| Division presidents | Accept Moderate risks; the presidents of the two financial-institution divisions are the senior members who direct and oversee the Qualified Individual (314.4(a)(2)); the Payment Processing president is the PCI DSS accountable executive |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks; lead each division's PCI DSS or SOC 2 program |
| Group internal audit | Independently assesses common controls once a year and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets the FTC Safeguards Rule for every group financial institution and PCI DSS for every group cardholder data environment. (PM-1; GV.PO-01; 16 CFR 314.4)

4.2 The Group CISO is the Qualified Individual. The president of each division that is a financial institution must be designated in writing as the senior member who directs and oversees the Qualified Individual, and intercompany agreements must require the holding company to maintain a program that protects that division (314.4(a)(1)-(3)). Each division with a cardholder data environment must keep a PCI DSS charter signed by its president as accountable executive. (PM-2; GV.RR-02; PCI DSS 12.4.1)

4.3 Each division and corporate must complete a written risk assessment at least annually and after significant change, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. Each PCI DSS requirement with a flexible frequency must have a targeted risk analysis. (RA-3; PM-9; ID.RA-01; 314.4(b); PCI DSS 12.3.1)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. A High risk of cardholder data compromise must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. **An acquired company must adopt group policy within 180 days of closing**, and its supplement must be re-issued in that time. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems and for its users of other divisions' systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. (PL-2; CA-2; GV.RR-02; PCI DSS 12.8.5)

4.7 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Service providers, including affiliates.** No service provider may access customer information, cardholder data, or a cardholder data environment without a written agreement that requires safeguards, states PCI DSS responsibilities, and sets incident notice terms, plus due diligence before access and a review at least every year. **A group division that provides services to another division is a service provider for this purpose** and is overseen in the same way. (SA-9; SA-4; GV.SC-05; 314.4(f); PCI DSS 12.8)

4.9 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Each cardholder data environment must have quarterly reviews confirming that personnel perform their security tasks. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01; 314.4(d)(1), (g); PCI DSS 12.4.2)

4.10 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.11 Security policies, procedures, risk assessments, assessments, and required actions must be retained for at least 5 years from creation or last effective date, whichever is later. (SI-12)

4.12 **AI systems.** No AI system that processes customer information or cardholder data, or that makes or supports decisions about cardholders, merchants, or clients, may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.13 **Significant change.** A significant change to a cardholder data environment, and any significant organizational change (including an acquisition), must trigger a documented review of PCI DSS scope and control applicability, reported to the division president. Scope must also be confirmed at least every six months for each service provider cardholder data environment. (CM-4; CM-8; PCI DSS 12.5.2.1; 12.5.3)

4.14 **Board reporting.** The Qualified Individual must report in writing to the board risk committee at least annually on the status of the program and its compliance with the Safeguards Rule, and on material matters including risk assessment, risk management decisions, service provider arrangements, testing results, security events and management's responses, and recommended changes. (PM-9; GV.OV-01; 314.4(i))

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), quarterly PCI DSS reviews, the annual supplement attestations, and the QSA and SOC examinations.

## 6. Exceptions
Exceptions follow section 4.10.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); PCI DSS charters; intercompany services agreements.
