# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes such as a new payment channel, a new venue or managed venue, a ticketing platform change, or a significant incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CM-3, CM-7, CM-8, SI-7, SA-4, SA-9, SR-6, PT-5 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-06, GV.SC-07, ID.RA-01, ID.AM-03, PR.PS-01 |
| PCI DSS v4.0.1 (N71-R04) | 12.1, 12.3, 12.5, 12.8; 6.4.3, 6.5, 11.6.1 |
| Law (N71-R05 and others) | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n); Rule on Unfair or Deceptive Fees, 16 CFR Part 464; Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-09) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects patrons' card and account data, the systems the venues need to sell tickets and admit attendees safely, the company's money, and the services the company provides to the County Performing Arts Center.

## 2. Scope
All employees, temporary staff, and contractors with access to company systems, including the marketing agency, the web agency, the network and security integrator, the MSSP, and event-day workers supplied by staffing contractors. Covers headquarters, the Amphitheater, the Music Hall, the Club, and any venue the company manages (the County PAC from 2027-07-01); all payment channels (online, box office, phone, group and premium, bars and stands); and all systems and data, including systems that service providers run for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, PCI DSS status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks; signs the PCI DSS AOCs |
| Chief Operating Officer | Executive sponsor and TVOP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee; leads the SOC 2 program |
| Security Manager (Information Security Officer) | Runs the program day to day; owns the SSP, the PCI DSS scope document, and the standards index |
| Chief Financial Officer | Merchant agreements, QSA engagement, AOC evidence file |
| General Counsel (Privacy Officer) | Privacy notice, breach determinations, contract terms with service providers |
| Business owners (ticketing, marketing and digital, premium and group sales, venue operations, food and beverage) | Operate the controls in their areas, including the ticketing settings, the website and tag manager, and payment devices |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the standards in `standards-index.md`, and the System Security Plan. (PM-1; GV.PO-01; PCI 12.1)
4.2 The Security Manager is the designated Information Security Officer, responsible for PCI DSS compliance activities. The designation must be in writing. (PM-2; GV.RR-02; PCI 12.1.3)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Where PCI DSS lets the company set how often a control runs, a targeted risk analysis must record the choice and be reviewed every 12 months. (RA-3; PM-9; ID.RA-01; PCI 12.3.1)
4.4 Risk acceptance authority: the risk owner may accept Low and Very Low risks; the Chief Operating Officer, Moderate; the Chief Executive Officer, High. Very High risks may not be accepted. No technology risk that could contribute to crowd harm may be accepted above Low. (PM-9; GV.RM-01)
4.5 **PCI DSS scope** must be documented for each merchant account and payment channel, with card data-flow diagrams and the connected and security-impacting systems, and confirmed at least every 12 months and before any new payment channel, device type, managed venue, or checkout change goes live. No AOC or SAQ may be signed until every answer is backed by evidence in the CFO's file. (PL-2; CM-8; ID.AM-03; PCI 12.5.2)
4.6 Security policies and standards must be reviewed at least annually and after major changes or incidents. Every workforce member must acknowledge the policies at hire and annually. (PL-1; GV.PO-02; PCI 12.1.2)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less.
4.8 **Service providers.** Before a provider stores, processes, or transmits card data or patron data for the company, or can affect their security (including tag and script vendors and agencies with access to the website or the ticketing tenant), it must be on the service provider list with a written agreement that covers security duties, its acknowledgment of responsibility for the data, and breach notice. Providers that touch card data must supply a current PCI DSS AOC and a responsibility matrix; Tier 1 providers are reviewed every year (STD-03). (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI 12.8)
4.9 **Purchasing gate.** No software, SaaS service, AI feature, or third-party script may be purchased, enabled, or added without a security review by the Security Manager and, where patron data is involved, the General Counsel. (SA-4; GV.SC-06)
4.10 **Sanctions.** Workforce members and contractors who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, termination, or removal of contractor access. (PS-8; GV.RR-04)
4.11 **Prices and privacy claims.** Every ticket price the company shows or advertises (website, email, SMS, social media, signs, phone scripts) must show the total price including mandatory fees, more prominently than any other pricing information, and fee names must describe what the fee is. The privacy notice must match actual data practices, including scripts, bot detection, the chatbot, and marketing scoring. The Vice President of Marketing and Digital checks prices before publication; the General Counsel owns the privacy notice. (PT-5; GV.OC-03; 16 CFR 464.2 and 464.3; 15 U.S.C. 45(a))
4.12 **Change control.** Changes to ticketing checkout, pricing, and bot mitigation settings, tag manager containers, website releases, payment device configurations, and firewall rules must be requested, approved by the owner, recorded, and, for payment-related changes, reviewed for PCI DSS impact before they go live. (CM-3; PR.PS-01; PCI 6.5)
4.13 **Payment pages.** Every script that loads on a page that embeds the payment form must be on an inventory with its owner, written business justification, and authorization by the Vice President of Marketing and Digital, and must be integrity-checked. A change and tamper detection mechanism must check those pages at least weekly and alert the MSSP. Publishing to the tag manager requires two people. (CM-7; CM-8; SI-7; PR.PS-01; PCI 6.4.3; 11.6.1)
4.14 **AI.** AI tools and AI features in existing systems must pass the P10 governance process before use, and the inventory of AI use cases must be kept current. (SA-4; PM-9; GV.OC-03)
4.15 Security controls must be assessed at least annually by the co-sourced internal audit firm, which must not operate the controls it assesses, and after major changes. (CA-2; ID.IM-02)

## 5. Compliance and enforcement
Violations are handled under section 4.10. Compliance is checked through the annual independent assessment (P07), the PCI DSS ROC and SAQ, the SOC 2 examinations for the County PAC, and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved at the right level, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; `policy-control-map.csv`; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); PCI DSS v4.0.1; 16 CFR Part 464
