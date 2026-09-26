# Business Impact Analysis: Cris Santos Company | Wholesale Trade | Small

**Organization:** Cris Santos Company, LLC (IT hardware and software wholesale distributor) | **Tier:** Small (62 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Warehouse and Logistics Manager, Sales Operations Manager, Purchasing and Supplier Manager, Configuration Lab Lead, and Controller | **Approved:** Chief Operating Officer, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan and backup redesign (SP 800-53 CP-2, CP-9, CP-10), which the company does not have today;
- the availability rating in the SSP (P02) for the Order-to-Fulfillment Platform (OFP);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Availability criteria in the reseller portal SOC 2 readiness assessment (P09).

No regulation sets recovery times for a wholesale distributor. The drivers are revenue, customer contracts, and the DoD reporting clocks that must still be met during an outage.

## 2. System and business description
The company distributes IT hardware and software from one Florida building that holds the offices, a 60,000 sq ft distribution center, and a caged configuration lab. It ships about 220 shipments and 650 order lines per shipping day to about 380 reseller accounts and three DoD prime contractors. Orders, inventory, fulfillment, and the reseller portal run on the Order-to-Fulfillment Platform (OFP): a SaaS ERP, a WMS on servers in the company's cloud tenant, the reseller portal, the identity provider, the network, and endpoints. See `../scenario-facts.md` sections 1 to 3 and the SSP (P02).

## 3. Impact categories and values
Dollar values are scaled to $54 million in annual revenue: about $216,000 of revenue and $24,000 of gross profit per shipping day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (lost gross profit, expedite fees, penalties) | $25,000 to $150,000 | Less than $25,000 (about one day of gross profit) |
| Operations | The company cannot take orders or ship | One channel or process stops (portal, receiving, lab) | Staff slowed but working |
| Regulatory | Missed DFARS 72-hour report or FAR 52.204-25 1-business-day report; CUI mishandled; covered equipment delivered | Late notice to a prime; sourcing rule not documented | Internal policy deviation |
| Safety (mission) | Counterfeit, tampered, or misconfigured equipment reaches a DoD installation network | Defective equipment reaches a commercial customer | None |
| Reputation | Loss of a DoD prime or a top-20 reseller | Reseller complaints; SOC 2 questions from customers | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Order capture and order management | High | 24 h | 8 h | 1 h |
| BP-02 Warehouse fulfillment and shipping | High | 24 h | 8 h | 4 h |
| BP-03 Reseller ordering portal | High | 24 h | 8 h | 1 h |
| BP-09 Government contract compliance and incident reporting | High | 24 h | 8 h | 24 h |
| BP-05 Receiving, inspection, and inventory control | Moderate | 48 h | 24 h | 4 h |
| BP-04 Purchasing and replenishment | Moderate | 72 h | 24 h | 4 h |
| BP-06 DoD configuration and kitting | Moderate | 72 h | 48 h | 24 h |
| BP-07 Customer service, returns, and RMA | Moderate | 48 h | 24 h | 4 h |
| BP-08 Billing, collections, and supplier payments | Moderate | 72 h | 48 h | 4 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

Counts: 4 High, 5 Moderate, 1 Low (10 processes).

**What drives the values:**
- Revenue and customer loyalty drive BP-01 to BP-03. Resellers can buy the same products from competing distributors, so orders that cannot ship within one shipping day are often lost for good.
- BP-09 is High even though it needs little IT. The DFARS 252.204-7012(c) report is due within 72 hours of discovery and the FAR 52.204-25(d) report within 1 business day, and an outage caused by a cyber incident starts those clocks at the worst time.
- BP-06 has a long MTD because Prime B schedules allow several days, but it has **no workaround**: CUI may be restored only to the controlled CUI share and lab workstations, never to a personal device or an unapproved cloud service.
- BP-05 is where authenticity checks happen. During an outage, pressure to skip inspection rises, so the workaround requires that all broker receipts stay in quarantine until systems return.

**Key findings:**
1. **The WMS cannot meet its RPO.** BP-02 and BP-05 need a 4-hour RPO for bin locations, picks, and receipts. The WMS database and file server are backed up **nightly**, so the achievable RPO is 24 hours. The backups have **never been restore-tested** and sit in the same cloud account, with the same administrator roles, as production. The 8-hour RTO for BP-02 is unproven (risk R-008 in P01; R-007 for ransomware).
2. **The ERP contract states 99.9% monthly availability but no RTO or RPO.** BP-01 depends on the ERP vendor meeting an 8-hour RTO and a 1-hour RPO. The Controller will request recovery commitments at the 2027 renewal and review the ERP vendor's SOC 2 Type 2 report for them (R-016).
3. **The portal vendor's commitments meet the BIA.** Its SOC 2 Type 2 report states an RTO of 4 hours and an RPO of 1 hour, which meets BP-03 (see P09 `vendor-soc2-review.csv`).
4. **One building, no alternate site.** A hurricane or long power loss that closes the building for more than 1 day exceeds the MTD for BP-01 and BP-02 (R-033). The alternate strategy is drop-shipping from the three largest authorized distributors and taking orders remotely through the SaaS ERP.
5. **The DIBNet reporting path does not exist yet.** The company has no DoD-approved medium assurance certificate, so BP-09 cannot meet its 8-hour RTO today (R-019).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Identity provider | Single sign-on and MFA for email, ERP, VPN, and the cloud console | All except the WMS handhelds |
| SYS-08 Network and internet | One firewall, one fiber ISP (no failover today), corporate, scanner, and guest Wi-Fi | All |
| SYS-01 ERP (SaaS) | Orders, purchasing, inventory, finance | BP-01, BP-02, BP-04, BP-05, BP-07, BP-08 |
| SYS-07 Cloud tenant: WMS servers | WMS application and database | BP-02, BP-05 |
| SYS-02 Handheld scanners | 40 handhelds on warehouse Wi-Fi | BP-02, BP-05 |
| SYS-11 Shipping and carrier label service | Rates, labels, tracking | BP-02 |
| SYS-03 Reseller portal (SaaS) | Reseller self-service ordering | BP-03 |
| SYS-04 EDI service | Purchase orders, ship notices, invoices with 22 suppliers and 18 resellers | BP-01, BP-04 |
| SYS-07 Cloud tenant: file server (CUI share) | Prime B configuration documents | BP-06 |
| SYS-09 Endpoints | 58 laptops and desktops, 6 lab workstations, 12 label and shipping printers | All |
| SYS-06 Productivity suite | Email and chat with customers and suppliers | All |
| SYS-10 Lab cage and badge system | Physical control of CUI work area | BP-06 |
| SYS-12 Forecasting add-on | Suggested purchase orders (not required to buy) | BP-04 |
| People | Sales, warehouse, purchasing, lab technicians, IT Manager, Systems Administrator, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and break-glass accounts | 1 h | Two break-glass administrator accounts stored offline (to be created; POL-02 4.8) |
| 2 | SYS-08 Firewall and internet | 2 h | Cellular failover router (to be purchased) |
| 3 | Clean laptop with the medium assurance certificate for BP-09 | 4 h | Spare laptop kept offline in the Chief Operating Officer's safe (certificate to be obtained) |
| 4 | SYS-01 ERP access | 8 h (vendor) | Order log spreadsheet; ERP is vendor-hosted and may be unaffected |
| 5 | SYS-07 WMS servers and database | 8 h | Rebuild from image and restore the latest clean backup (achievable RPO 24 h until backups improve) |
| 6 | SYS-02 Handhelds and scanner Wi-Fi; SYS-11 label service | 8 h | Paper pick tickets; carrier web portal labels |
| 7 | SYS-03 Portal and SYS-04 EDI | 8 h (vendors) | Email and phone orders; EDI partners resend |
| 8 | SYS-09 Clean endpoints for sales, customer service, and purchasing | 8 h | 4 pre-imaged spare laptops |
| 9 | SYS-07 File server CUI share and lab workstations | 48 h | None for CUI; notify Prime B of schedule impact |
| 10 | SYS-12 Forecasting add-on | 72 h | ERP reorder report |
| 11 | Payroll SaaS | 72 h | Repeat prior payroll |
