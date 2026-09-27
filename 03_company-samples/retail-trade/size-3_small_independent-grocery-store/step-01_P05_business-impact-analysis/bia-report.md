# Business Impact Analysis: Cris Santos Company | Retail Trade | Small

**Organization:** Cris Santos Company, LLC (independent grocery retailer) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the Store Manager, E-commerce and Marketing Manager, and Controller | **Approved:** General Manager, 2026-09-04

## 1. Overview and purpose
This BIA identifies which business processes the store depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the incident response plan that PCI DSS v4.0.1 Requirement 12.10 expects, which must cover business recovery and continuity.

## 2. System and business description
One supermarket in Florida, open 7:00 to 22:00 every day, with 60 employees, plus online ordering with curbside pickup and delivery in four zones. Card payments run on a validated P2PE solution in the store and on the processor's embedded payment form online. Online ordering and the loyalty program run on the E-commerce and Loyalty Platform (P02). Refrigeration and building systems are monitored by IoT sensors and a vendor dashboard. See `../00_company-facts.md` sections 1, 3, and 4.

## 3. Impact categories and values
Dollar values are scaled to $24.0 million in annual sales, about $66,000 per day and about $4,400 per open hour.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $100,000 (lost sales, spoiled stock, or incident costs) | $25,000 to $100,000 | Less than $25,000 |
| Operations | The store cannot sell, or refrigerated stock cannot be protected | One channel or department stops | Staff slowed but working |
| Contractual and regulatory | Card data compromise or reportable breach of personal information | Missed contractual or PCI DSS deadline | Internal policy deviation |
| Food safety | Unsafe food could reach customers | Product discarded as a precaution | None |
| Reputation | Local media coverage or lasting loss of shoppers | Complaints or poor online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 In-store checkout and card payments | High | 4 h | 2 h | 1 h |
| BP-02 Online ordering and payment | Moderate | 24 h | 8 h | 1 h |
| BP-03 Order fulfillment (picking, curbside, delivery) | Moderate | 12 h | 6 h | 1 h |
| BP-04 Refrigeration and food safety monitoring | High | 2 h | 1 h | 24 h |
| BP-05 Receiving, inventory, and pricing | Moderate | 48 h | 24 h | 24 h |
| BP-06 Loyalty program and personalized offers | Low | 72 h | 48 h | 24 h |
| BP-07 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-08 Accounting, supplier payments, and card settlement reconciliation | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Food safety drives BP-04.** Refrigerated and frozen stock is worth about $150,000. If monitoring is lost, staff must check temperatures by hand every 2 hours, so the monitoring system has a 2-hour MTD. The 24-hour RPO covers the temperature logs kept for food safety records.
- **Card acceptance drives BP-01.** About 85% of store sales are by card. After about 4 hours of cash-only trading, shoppers go elsewhere and lost sales pass the Moderate cost band. **The workaround must never be manual card entry on a register.** That would put card numbers into systems outside the P2PE solution and undo the scope reduction.
- **Online ordering (BP-02) can wait longer** because customers can shop in the store. The storefront vendor's stated 4-hour recovery time meets the 8-hour RTO (P09 vendor review), so the outage risk was accepted (P01 R-020).
- **The loyalty program (BP-06) is Low for availability but not for confidentiality.** Checkout works without it, but a breach of its data has contractual and reputational impact. The SSP (P02) rates its confidentiality separately.

**Key findings:**
1. The store has a **single internet connection** and no offline card mode, so an internet outage stops card acceptance (BP-01) and online ordering at once (P01 R-019). Cellular failover is funded for 2026 Q4.
2. The loyalty database backups have **never been restore-tested**, so the 48-hour RTO for BP-06 is unproven (P01 R-013).
3. Refrigeration alerts go to **one email address** (P01 R-018). Text alerts to two people are planned.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-08 Store network and internet | Firewall, switches, Wi-Fi, single internet connection (cellular failover planned) | All |
| SYS-05 POS system and P2PE PIN pads | 11 registers, back office server, vendor cloud journal (hourly) | BP-01, BP-05 |
| SYS-02 Payment processor | Authorization, P2PE decryption, embedded form, merchant portal | BP-01, BP-02, BP-08 |
| SYS-07 Refrigeration and building IoT | Sensors, controllers, alarms, vendor dashboard | BP-04 |
| SYS-01 Storefront (SaaS) | Online catalog, orders, customer accounts; vendor backups | BP-02, BP-03 |
| SYS-09 Identity provider | Single sign-on and MFA for office systems and the storefront admin console | BP-02, BP-05, BP-06, BP-08 |
| SYS-11 Handhelds and PCs | 18 handhelds for picking and receiving; 16 PCs | BP-03, BP-05, BP-08 |
| SYS-06 Back office and inventory (SaaS) | Items, prices, receiving; vendor backups | BP-05 |
| SYS-03 and SYS-04 Loyalty database (cloud tenant) | Daily managed backups in the same account (separate account planned) | BP-06 |
| SYS-12 Pricing and offers engine | Vendor SaaS; can be paused, with shelf prices used online | BP-06 |
| People and facilities | Cashiers, pickers, drivers, department leads, Store Manager, IT Manager; generator for refrigeration | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-08 Internet and store network | 1 h | Cellular failover on the firewall (to be installed) |
| 2 | SYS-07 Refrigeration monitoring and alarms | 1 h | Manual temperature checks every 2 hours; generator |
| 3 | SYS-05 Registers and P2PE PIN pads | 2 h | Cash-only lanes; POS vendor on-site support; spare PIN pad from the processor |
| 4 | SYS-09 Identity provider and administrator access | 2 h | Two break-glass accounts (to be created, POL-02) |
| 5 | SYS-01 Storefront | 4 h (vendor commitment; RTO 8 h) | Vendor-hosted; phone orders for pickup |
| 6 | SYS-11 Handhelds and pick lists | 6 h | Printed pick lists |
| 7 | SYS-06 Back office, inventory, and price file | 24 h | Keep yesterday's price file |
| 8 | SYS-03 and SYS-04 Loyalty database | 48 h | Honor member prices manually; credit points later |
| 9 | Payroll SaaS | 72 h | Repeat prior payroll |
