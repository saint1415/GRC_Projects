# SOC 2 Readiness Summary: Cris Santos Company Holdings | Retail Trade | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Retail Trade (focus division: Grocery Retail) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Grocery Wholesale **Retailer Services Portal** (`soc2-readiness.csv`). Grocery Retail and Financial Services are out of scope. A review of the vendor SOC reports Financial Services and the group rely on is in `vendor-soc2-review.csv` |
| Categories in scope | Security, Availability, Confidentiality (Retailer Services Portal) |
| Target report | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, issued by 2027-12-15 (meets the request from 140 independent grocers for a Type 2 report by the end of 2027) |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Grocery Wholesale security and compliance lead and the retailer services director |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build into their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Assurance relied on |
|---|---|---|---|---|---|
| Grocery Wholesale | Retailer Services Portal (SYS-D5): ordering, item and price files, promotions, invoices, and payments for about 1,100 independent grocers | **Yes.** Grocers rely on the portal for their purchasing, pricing, and payables, and 140 of the largest asked for a SOC 2 Type 2 report by the end of 2027 (P03 WD-G15) | **In scope.** First readiness assessment | Security, Availability, Confidentiality | SOC 2 (planned); SAQ for the division's merchant account |
| Grocery Wholesale | Distribution and transportation (SYS-D4) | No. Grocers buy goods and delivery, not a system they rely on for their own controls | Out of scope | n/a | Contracts; food safety records (P03) |
| Grocery Retail | Supermarkets and online ordering for consumers | **No.** Shoppers are consumers, not user entities | **Out of scope** | n/a | **PCI DSS Report on Compliance** by a QSA each year (Level 1 merchant); FTC Act Section 5 program (P03) |
| Financial Services | Rewards Card and installment loans to consumers | **No.** Cardholders are consumers. Financial Services is a *user* of a service organization (the card processing platform), not a provider | **Out of scope** | n/a | **FTC Safeguards Rule** program with a Qualified Individual and annual board report; Reg Z, Reg B, Reg P, FCRA, and Red Flags compliance (P03); the **card processor's SOC 1 and SOC 2 Type 2 reports** (`vendor-soc2-review.csv`) |

**Why Grocery Retail is out of scope:**
1. **No user entities.** Shoppers do not rely on the group's controls as part of their own control environment, which is what a SOC 2 report is for.
2. **The assurance its stakeholders ask for is PCI DSS.** The acquirer requires an annual ROC and AOC from a QSA (Level 1 merchant; 2026 ROC due 2026-12-15). That is the report the acquirer and the card brands rely on (vertical overlay: PCI DSS validation is the assurance alternative for card payments).
3. **Revisit trigger:** if Grocery Retail begins offering services to other businesses (for example, a retail media network or fulfillment for other brands), assess whether those customers need a SOC 2 or SOC 1 report.

**Why Financial Services is out of scope:**
1. **No user entities.** It lends to consumers. The warehouse credit facility lender receives financial reporting and covenant compliance, not a SOC report.
2. **Assurance comes from law and its own vendor oversight.** The Safeguards Rule requires a written program, a Qualified Individual, testing, and an annual written report to the board (16 CFR 314.4). The FTC and the CFPB enforce the consumer finance rules (P03 regulation-by-division matrix).
3. **It relies on SOC reports rather than issuing one.** The card processing platform's SOC 1 and SOC 2 reports are reviewed in `vendor-soc2-review.csv`. A SOC report does not by itself meet the Safeguards duty to oversee service providers (16 CFR 314.4(f)); it is evidence for that review (POAM-019).
4. **Revisit trigger:** if Financial Services starts servicing card or loan portfolios for other lenders, assess the need for a SOC 1 report.

**Other assurance options considered for the portal.** A completed security questionnaire per customer does not scale to 1,100 grocers, and the 140 largest asked for SOC 2 by name. PCI DSS validation covers only the invoice payment page, not ordering, pricing, or availability.

## 2. System description (scope)
- **Services:** B2B ordering, item and price files, promotions, invoices, and card and ACH payments for about 1,100 independent grocers in 8 states.
- **Infrastructure and software:** SYS-D5 in cloud provider A (containers, managed database), with disaster recovery in provider B. Group common controls are **carved in** as internal shared services: identity (SYS-G1), SOC (SYS-G2), cloud platform (SYS-G3), and the digital front door with customer identity and tag management (SYS-G4).
- **Subservice organizations (carve-out):** cloud providers A and B; the payment processor (hosted payment fields for card payments); the tag management vendor.
- **People:** the portal product and engineering team, retailer services and customer support staff, plus group identity, SOC, cloud, and digital teams.
- **Data:** grocer account and contact data, order history, customer-specific prices and promotions (Confidential), invoices, and ACH bank details. Card data is entered only in the processor's hosted fields.
- **Complementary user entity controls:** each grocer names an administrator who creates and removes its store users, enables MFA, protects credentials, and reviews orders and invoices.

**The first deliverable is the system description itself (CC2.3).** The portal has no written service commitments, and its terms describe a stronger security model than practice (P03 WD-G13). The description must also say plainly which controls are inherited from group providers, which is why POAM-018 (inheritance matrices) is on the critical path.

## 3. Readiness results (Retailer Services Portal, `soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 21 | 9 | 3 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** the control environment, risk assessment, workforce access, network protection, and SOC criteria are met by group common controls that P07 assessed once (135 of 158 common statements satisfied).

**Not ready:**
- **CC2.3:** no system description, service commitments, or user entity responsibilities (above).
- **CC6.2:** about 30% of grocer accounts are shared among store staff, so users cannot be traced or removed one by one (POAM-023).
- **CC6.8:** the invoice payment page loads the shared "all pages" tag container (POAM-001). This is the same weakness behind the P08 scenario.

**Partially ready:** CC2.1 and CC4.1 (inheritance not documented or assessed, POAM-018), CC3.4 (group provider changes not assessed for portal impact), CC6.1 (customer MFA optional; cross-customer access checks not automated), CC7.1 and CC7.2 (no payment page change detection; alerts not to the SOC, POAM-002), CC7.4 (grocer notice steps not exercised, POAM-011), CC8.1 (tags bypass portal change control, POAM-001), CC9.2 (tag and script vendors not reviewed, POAM-003), A1.3 (digital front door never recovery-tested as a whole, POAM-013), C1.1 (account managers can download any customer's price files), and C1.2 (no retention or deletion schedule for departed customers).

**Processing Integrity** is not in scope for the first report because the portal makes no processing commitments today. It will be reconsidered for 2028, because grocers depend on accurate price files and invoices. **Privacy** is not in scope: the portal serves businesses, and the contact data it holds is covered by group privacy controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Work and evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.8, CC7.1, CC7.2, CC8.1, CC9.2 | Payments-only tag container, script inventory, payment page monitoring with SOC alerts, vendor reviews (POAM-001 to POAM-003); these also protect the 2026 wholesale self-assessment |
| 2026 Q4 | CC2.1, CC7.4 | SYS-D5 inheritance matrix (POAM-018); cross-division tabletop with grocer notices (POAM-011) |
| 2027 Q1 | CC2.3, CC3.4, CC4.1, CC6.1, CC6.2, A1.3, C1.1 | System description and commitments; named users and required MFA (POAM-023); group change review includes the portal; internal assessment of inherited controls; front door recovery test (POAM-013); download restrictions. **Type 1 as of 2027-03-31** |
| 2027 Q2 | C1.2 | Retention schedule and automated deletion |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30); report issued by 2027-12-15 |

**Communication:** the retailer services director sends the 140 requesting grocers a readiness letter with this timeline in 2026 Q4, together with the customer notice about named users and MFA (POAM-023). The service auditor will be engaged by 2027-01-31 for the Type 1 report.
