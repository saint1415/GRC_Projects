# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Live Venues, Hotels and Restaurants, Ticketing and Streaming Technology) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, SA-4, SA-9, CA-2, CA-7, CM-3, SI-12 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| PCI DSS v4.0.1 | Requirements 12.1, 12.3, 12.4, 12.5, 12.8, 12.9 (N71-R04; N72-R01) |
| Division supplements | Live Venues supplement (v2026); Hotels and Restaurants supplement (v2024, re-alignment due 2026-11-30); Ticketing and Streaming supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects patrons', guests', subscribers', and clients' information and the systems that hold it, and supports the group's three PCI DSS roles.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and event-day contractor workers), all systems and data the group owns or operates, including newly acquired businesses from the day the acquisition closes, and systems operated for the group by service providers. It covers card data, patron, guest, and subscriber personal information, client data processed by the ticketing platform, and all other group information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); co-accepts High risks; chairs the group AI council |
| Group Chief Privacy Officer | Owns data classification, purposes, and minimization across divisions and the patron data platform |
| Group General Counsel | Owns client and vendor contract terms, the notification matrix, and the price display standard |
| Group PCI program director | Owns PCI DSS scope documents, provider lists, and assessor relationships for all three PCI roles |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that meets PCI DSS for every merchant and service provider role in the group. (PM-1; GV.PO-01; PCI DSS 12.1)

4.2 The Group CISO is accountable for the program. The Group PCI program director must be named in writing as responsible for PCI DSS compliance across the group, with a named lead in each division. (PM-2; GV.RR-02; PCI DSS 12.4)

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1, and a targeted risk analysis for each PCI DSS requirement that allows the entity to set its own frequency. Division risks that cross divisions, sit in shared services or the ticketing platform, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; PCI DSS 12.3)

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Crowd-safety and guest-safety risks rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems in PCI DSS scope, which controls it inherits and which remain with the division, and must confirm that documentation every year before signing any ROC or SAQ. (PL-2; CA-2; GV.RR-02; PCI DSS 12.5)

4.7 **Sanctions.** Workforce members who violate security or privacy policies must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04)

4.8 **Service providers.** No vendor or intercompany service may store, process, or transmit card data, or run code on a payment page, without a security review, written PCI DSS responsibility terms, and current evidence (an AOC or equivalent). The Ticketing and Streaming division must give every client, including the other divisions, a written acknowledgment of its PCI DSS responsibilities and a responsibility matrix. (SA-9; SA-4; GV.SC-05; PCI DSS 12.8, 12.9)

4.9 **Acquisitions.** An acquired business must be added to the group PCI DSS scope documents, the SOC, and the risk registers within 30 days of closing, with an interim plan for any card channel that does not meet group standards. (PL-2; CA-7; PCI DSS 12.5)

4.10 **Evaluation.** Group internal audit must assess common controls at least annually and sample each division's controls. Results feed the POA&M and the risk registers. (CA-2; CA-7; ID.IM-01)

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.12 **Price displays.** Every ticket and room price that a division offers, displays, or advertises, in any channel, must show the total price, including mandatory fees, more prominently than other pricing information, and must describe fees accurately (16 CFR 464.2, 464.3). The Group General Counsel maintains the price display standard. (PL-4; GV.OC-03)

4.13 **Payment page changes.** Any change to content on a payment page, including tags added by a tenant, a division, or a client, must be authorized, inventoried with a business justification, and covered by change-and-tamper detection. Tags are not permitted in any checkout step. (CM-3; CM-8; SI-7; PCI DSS 6.4.3, 11.6.1)

4.14 **AI systems.** No AI system that sets prices, controls access to purchases or venues, uses patron, guest, or subscriber data, or makes or supports decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.15 Security policies, procedures, risk analyses, assessments, and required actions must be retained for at least 6 years. Incident records follow POL-03. (SI-12)

## 5. Compliance and enforcement
Violations are handled under 4.7. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, PCI DSS validations, and access reviews.

## 6. Exceptions
Exceptions follow section 4.11. No exception may permit a price display without the total price or a tag in a checkout step.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); PCI DSS v4.0.1; 16 CFR Part 464.
