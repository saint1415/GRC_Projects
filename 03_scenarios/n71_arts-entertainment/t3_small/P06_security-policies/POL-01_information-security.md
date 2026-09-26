# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | General Manager |
| Approved by | General Manager (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes such as a new payment channel or ticketing platform, or after incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CM-3, CM-7, CM-8, SI-7, SA-9, SR-6, PT-5 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, ID.RA-01, ID.AM-03, PR.PS-01 |
| PCI DSS v4.0.1 (N71-R04) | 12.1, 12.3, 12.5, 12.8; 6.4.3, 6.5, 11.6.1 |
| Law (N71-R05) | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n); Rule on Unfair or Deceptive Fees, 16 CFR Part 464 |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects patrons' card data and account data, the systems the venue needs to sell tickets and admit attendees safely, and the company's money.

## 2. Scope
All Cris Santos Company employees, owners, and temporary staff, and every contractor with access to company systems, including the marketing agency, the network and security integrator, and event-day workers from staffing contractors. Covers the venue building, all payment channels (online, box office, phone, bars and stands), and all systems and data, including systems that service providers run for the company (ticketing platform, payment partner, POS vendor, cloud provider).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks; signs the PCI DSS attestations |
| General Manager | Program owner; approves policies; accepts Moderate risks |
| IT Manager (Information Security Lead) | Runs the program day to day; maintains the risk register, SSP, and PCI DSS scope document |
| Controller | Merchant agreements, SAQ evidence file, service provider list |
| Director of Ticketing and Marketing Director | Own the ticketing platform settings and the checkout content respectively |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set and the System Security Plan. (PM-1; GV.PO-01; PCI 12.1)
4.2 The IT Manager is the designated Information Security Lead. The designation must be in writing. (PM-2; GV.RR-02)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Where PCI DSS lets the company set how often a control runs, a targeted risk analysis must record the choice. (RA-3; PM-9; ID.RA-01; PCI 12.3)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the General Manager, Moderate; the majority owner, High and Very High. Risks to attendee safety rated High may not be accepted. (PM-9; GV.RM-01)
4.5 **PCI DSS scope** must be documented for each merchant account and payment channel, with a card data-flow diagram, and confirmed at least annually and before any new payment channel, device, or checkout change goes live. Every SAQ answer must be backed by evidence in the Controller's file before anyone signs. (CM-8; PL-2; ID.AM-03; PCI 12.5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Every workforce member must acknowledge them at hire and annually. (PL-1; GV.PO-02; PCI 12.1)
4.7 Exceptions to any security policy must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less.
4.8 **Service providers.** Before a provider stores, processes, or transmits card data or patron data for the company, or can affect their security, it must be on the service provider list with a written agreement that covers security duties and breach notice. Providers that touch card data must supply a current PCI DSS AOC and a responsibility matrix, checked at least annually. (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI 12.8)
4.9 Security controls must be assessed at least annually (P07) and after major changes. (CA-2)
4.10 **Sanctions.** Workforce members and contractors who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, termination, or removal of contractor access. (PS-8; GV.RR-04)
4.11 **Prices and privacy claims.** Every ticket price the company shows or advertises (website, email, social media, signs, phone scripts) must show the total price including mandatory fees, as the FTC fee rule requires, and fee names must describe what the fee is. The privacy notice must match actual data practices. Both must be checked before publication by the Marketing Director. (PT-5; GV.OC-03; 16 CFR 464.2 and 464.3; 15 U.S.C. 45(a))
4.12 **Change control.** Changes to checkout settings, payment settings, pricing rules, bot mitigation settings, and firewall rules must be requested, approved by the owner named in section 3, and recorded before they go live. (CM-3; PR.PS-01; PCI 6.5)
4.13 **Payment pages.** No script, tag, or pixel may be added to ticketing checkout pages. Any script on event pages must be listed with its owner and business reason and approved by the Marketing Director. The company must obtain alerts from the ticketing vendor for any change to checkout settings. (CM-7; CM-8; SI-7; PR.PS-01; PCI 6.4.3; 11.6.1)

## 5. Compliance and enforcement
Violations are handled under section 4.10. Compliance is checked through the annual control assessment (P07), the annual SAQs, and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); PCI DSS v4.0.1; 16 CFR Part 464
