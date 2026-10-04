# Business Impact Analysis: Cris Santos Company | Retail Trade | Mid-Market

**Organization:** Cris Santos Company, Inc. (regional grocery retailer: 5 supermarkets, online ordering, a distribution center, and a support center) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, and the Distribution Center Director | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the 5 stores, e-commerce (website, app, picking, pickup, and delivery), the distribution center (DC) and transportation, and the support center functions. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory and contract exposure, food safety, and reputation.

The results feed:
- the FIPS 199 availability rating and contingency controls in the SSP for the E-commerce and Point-of-Sale Platform (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the supplier offers service (P09);
- the incident response plan that PCI DSS v4.0.1 Requirement 12.10 expects, which must include business recovery and continuity procedures (P03).

## 2. System and business description
The company runs 5 supermarkets in two neighboring Florida counties, online ordering with curbside pickup and home delivery, deli and bakery catering, and a DC that ships to the stores every day. Sales and payments run on the E-commerce and Point-of-Sale Platform (EPP) described in the SSP (P02): the SaaS e-commerce platform, the payment processor's services, the store POS system (65 registers, 65 PIN pads, 5 store servers, and the POS head-office application), the 4-account cloud landing zone, the identity provider, the 6 site networks on SD-WAN, about 465 endpoints, and the MSSP-operated SIEM. The ERP and WMS, the refrigeration and building systems, about 85 vendors, and the AI tools connect to it (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual sales over 364 trading days: about $48,400 a day per store (about $242,000 across 5 stores) and about $33,000 a day online. About $22,000 of daily store sales are paid with SNAP EBT.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $50,000 in lost sales, spoiled product, or extra labor | $10,000 to $50,000 | Less than $10,000 |
| Operations | All stores, the DC, or online ordering cannot serve customers | One store or one channel stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory and contract | Card data compromise, breach notice, loss of SNAP authorization, or a food safety violation | Missed contract or reporting deadline (acquirer, supplier) | Internal policy deviation |
| Safety (food and customer) | Plausible illness from temperature-abused food, or harm to customers or staff | Delayed but safe service | None |
| Reputation | Regional media coverage, loss of a national supplier program, or a visible loss of customers | Complaints and online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is sales that are not recovered, plus spoiled product and extra labor, over the MTD. The process owners supplied the recovery assumptions: about 40% of store baskets lost during a checkout outage are not recovered, about 60% of online orders lost in a long outage are not recovered, and about half of SNAP purchases delayed beyond 8 hours are lost. For settlement and supplier payments (BP-13, BP-14), the loss is fees, overtime, and supplier holds; delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 In-store checkout and card payments | Stores | High | 4 | 2 | 0.25 | $26,000 |
| 2 | BP-08 Refrigeration monitoring and food safety | Stores and DC | High | 4 | 2 | 1 | $15,000 |
| 3 | BP-02 SNAP EBT acceptance | Stores | High | 8 | 4 | 0.25 | $6,000 |
| 4 | BP-03 Online ordering and payment | E-commerce | High | 12 | 4 | 1 | $10,000 |
| 5 | BP-06 Store replenishment and warehouse operations | DC | High | 24 | 12 | 4 | $60,000 |
| 6 | BP-04 Order picking, pickup, and delivery | E-commerce and stores | Moderate | 24 | 8 | 1 | $15,000 |
| 7 | BP-09 Loyalty program and digital offers | E-commerce and stores | Moderate | 24 | 8 | 1 | $12,000 |
| 8 | BP-05 Pricing, item file, and promotions | Support center | Moderate | 24 | 12 | 24 | $8,000 |
| 9 | BP-16 Fleet dispatch and delivery routing | DC | Moderate | 24 | 12 | 4 | $9,000 |
| 10 | BP-12 Customer service | Support center | Moderate | 24 | 8 | 24 | $3,000 |
| 11 | BP-07 Supplier purchasing and receiving | Support center | Moderate | 48 | 24 | 24 | $20,000 |
| 12 | BP-11 Catering and service-desk orders | Stores | Low | 48 | 24 | 24 | $4,000 |
| 13 | BP-13 Payment settlement and reconciliation | Support center | Moderate | 72 | 48 | 24 | $10,000 |
| 14 | BP-10 Supplier offers and retail media service | Support center | Moderate | 72 | 24 | 4 | $15,000 |
| 15 | BP-14 Accounts payable and supplier payments | Support center | Moderate | 72 | 48 | 24 | $8,000 |
| 16 | BP-15 Payroll, scheduling, timekeeping, and HR | Enterprise | Moderate | 72 | 48 | 24 | $12,000 |
| 17 | BP-18 CCTV, physical security, and loss prevention | Stores and DC | Low | 72 | 48 | 24 | $3,000 |
| 18 | BP-17 Analytics, forecasting, and reporting | Support center | Low | 120 | 72 | 24 | $5,000 |

**Summary:** 5 High, 10 Moderate, and 3 Low processes (18 in total). The sum of estimated losses at each process's MTD is $241,000.

**Enterprise-wide scenario.** If ransomware stopped the store POS servers, the integration platform, and the WMS for 72 hours, unrecovered sales would be about $430,000 (stores about $350,000 after offline mode runs out at 24 hours, online about $60,000, SNAP about $20,000), and spoiled or written-off product about $150,000. About $5.7 million of card settlements and supplier payments would be delayed. Incident response, forensics, and any breach notice come on top (see P01 R-002 and R-001).

**What drives the values:**
- **Checkout continuity** drives BP-01 and BP-02. Offline mode on the store POS servers carries card sales for up to 24 hours, but only if registers and store servers are healthy. SNAP EBT has no offline option, so BP-02 has a short MTD despite lower revenue.
- **Food safety** drives BP-08 and the DC (BP-06). Temperature-abused product must be discarded, and an undetected case failure can put unsafe food on the shelf within hours.
- **Card data protection** drives how BP-03 recovers. Online card payments must not reopen until the checkout page is verified clean (P08 skimming runbook).
- **Contracts** drive BP-10 (supplier SOC 2 and billing accuracy) and the acquirer terms behind BP-01 and BP-03.

## 5. Key findings
1. **Store resilience depends on the store POS servers.** Offline mode protects sales for 24 hours, but it runs on the same store servers that a ransomware attack would target. The servers are backed up locally only, and POS vendor technicians reach them through 3 shared accounts with standing access (gap 3). Action: off-site, immutable backups of store server images and named, brokered vendor access (P01 R-001, R-006; P07 CP-9, AC-17).
2. **Cloud workload recovery is unproven.** The loyalty and CDP database (BP-09), the integration platform (BP-03, BP-05, BP-07), and the POS head-office application (BP-01) have never been restore-tested (gap 7). Their RTOs of 2 to 12 hours are targets, not demonstrated capabilities (P01 R-014, R-015; P07 CP-4).
3. **The ERP vendor's recovery commitment does not meet the BIA.** The ERP vendor's SOC 2 system description states an RTO of 24 hours. BP-05 needs 12 hours to publish a price file. The workaround (run on the last good price file) is acceptable for 24 hours only. Action: negotiate the recovery term at the 2027 renewal and keep a daily price file export in the cloud backup account (P01 R-016; P09 vendor review).
4. **The DC has the largest single loss.** A 24-hour WMS or DC network outage costs about $60,000, mostly in spoiled fresh product and empty shelves. The WMS is SaaS, but the DC network, RF handhelds, and cold-room controls are company-run (P01 R-018).
5. **Refrigeration monitoring has no cyber resilience plan.** Controllers and sensors at Stores 4 and 5 share the corporate VLAN (gap 4), and the contractor's remote tool is always on. A compromise or network outage would silence temperature alarms. Manual 2-hour temperature checks are written into store procedures but have not been drilled (P01 R-008).
6. **Card data must not leak into workarounds.** Catering staff write full card numbers on paper (gap 8), and during outages staff have taken card numbers by phone. Workarounds in this BIA use pay-at-pickup on PIN pads instead.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 E-commerce platform (SaaS) | Website, app back end, customer accounts, order management | BP-03, BP-04, BP-09, BP-12 |
| SYS-02 Payment processor services | Store encryption service, hosted fields and SDK, tokens, virtual terminal, merchant portal | BP-01, BP-02, BP-03, BP-11, BP-13 |
| SYS-03 Store POS system | 65 registers, 65 PIN pads, 5 store servers (offline mode), POS head-office application | BP-01, BP-02, BP-09 |
| SYS-04 Landing zone: loyalty and CDP database, loyalty API | Member lookups, offers, purchase history | BP-03, BP-09, BP-10 |
| SYS-04 Landing zone: integration platform | Price file, orders, EDI hand-offs, offers engine feeds | BP-03, BP-05, BP-07 |
| SYS-04 Landing zone: data warehouse and reporting portal | Supplier reporting, forecasting, dashboards | BP-10, BP-17 |
| SYS-04 Landing zone: backup account | Daily immutable backups, 35-day retention | Recovery of SYS-03 head office and SYS-04 workloads |
| SYS-05 ERP and WMS (SaaS) | Item and price files, purchasing, finance, warehouse operations | BP-05, BP-06, BP-07, BP-13, BP-14 |
| SYS-06 Identity provider | Single sign-on and MFA for workforce | All support-center processes |
| SYS-07 Site networks and SD-WAN | 6 sites; dual ISP at the DC campus, single ISP plus cellular failover at stores | All |
| SYS-08 Endpoints | PCs, laptops, handhelds, tablets; 5 service-desk PCs | All |
| SYS-09 SIEM (MSSP) | Detection and investigation | Recovery validation |
| SYS-10 Operational technology | Refrigeration controllers and sensors, cold rooms, CCTV | BP-06, BP-08, BP-18 |
| Third parties | Payment processor, EBT processor, POS vendor, e-commerce platform vendor, ERP and WMS vendors, cloud provider, MSSP, refrigeration contractor, delivery marketplace, offers engine vendor | As listed in `bia.csv` |
| People and facilities | Store teams, DC and transportation staff, e-commerce team, IT and security team, MSSP | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, stored offline |
| 2 | SYS-07 SD-WAN and store networks (POS VLANs first) | 2 h | Cellular failover at each store; offline mode on store servers |
| 3 | SYS-03 store POS servers and registers | 2 h | Offline mode up to 24 hours; cash-only lanes; rebuild servers from the vendor image |
| 4 | SYS-10 refrigeration monitoring | 2 h | Manual temperature checks every 2 hours; contractor on site |
| 5 | SYS-02 processor connectivity (cards and EBT) | 2 h (cards), 4 h (EBT) | Processor's backup connection path; EBT processor outage procedure |
| 6 | SYS-01 e-commerce checkout (after integrity check) | 4 h | Pay-at-pickup on PIN pads; phone orders for vulnerable customers |
| 7 | SYS-04 integration platform and loyalty API | 8 h | Last good price file; standard member discount at registers |
| 8 | SYS-05 WMS and DC network | 12 h | Paper pick lists; direct-store delivery from key suppliers |
| 9 | SYS-09 SIEM and EDR console | 8 h | MSSP works from its own platform; needed to validate clean recovery |
| 10 | SYS-05 ERP (pricing, purchasing) | 12 h (pricing), 24 h (purchasing) | Phone and email orders to top 40 suppliers |
| 11 | SYS-04 reporting portal and data warehouse | 24 h (portal), 72 h (warehouse) | Manual redemption summaries to suppliers |
| 12 | Payroll and HR SaaS | 48 h | Repeat prior payroll |
