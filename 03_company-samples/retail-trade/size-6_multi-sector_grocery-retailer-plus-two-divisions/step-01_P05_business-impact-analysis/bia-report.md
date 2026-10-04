# Business Impact Analysis: Cris Santos Company Holdings | Retail Trade | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud, data centers and network, the digital front door, ERP, HR).
- **Division BIAs:** Grocery Retail (focus), Grocery Wholesale, and Financial Services. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the availability rating of the E-commerce and Point-of-Sale Platform in the SSP (P02) and the cloud placement of recovery controls (P04);
- impact ratings in the group and division risk registers (P01);
- PCI DSS v4.0.1 Requirement 12.10.1, which expects business recovery and continuity procedures in the incident response plan;
- the Financial Services incident response plan under the FTC Safeguards Rule (16 CFR 314.4(h)) and its Reg Z servicing duties;
- the wholesale division's ability to produce food records within 24 hours of an FDA request (21 CFR 1.361);
- the Availability commitments planned for the Retailer Services Portal SOC 2 report (P09) and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and the two colocation data centers, SYS-G4 the digital front door (content delivery, web application firewall, tag management, customer sign-in), and SYS-G5 ERP and HR. Division systems are SYS-D1 (the E-commerce and Point-of-Sale Platform, including the payment switch), SYS-D2 (loyalty, CDP, and pricing), SYS-D3 (store infrastructure and refrigeration), SYS-D4 (distribution systems and OT), SYS-D5 (Retailer Services Portal), and SYS-D6 (card and lending platform). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Grocery Retail about $42.7 million a day (about $38.9 million in stores and $3.8 million online), Grocery Wholesale about $4.9 million a day from independent grocers (plus every group store's supply), and Financial Services about $1.6 million a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (selling in stores, supplying stores, servicing cards) | One region, channel, or distribution center stops | Staff slowed but working |
| Regulatory | Reportable breach, missed acquirer, FTC, FDA, or SEC deadline, or loss of SNAP authorization | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible harm to customers or workers (unsafe food, recall not executed, driver safety) | Product loss without safety effect | None |
| Reputation | National media, regulator attention, or loss of independent grocer customers | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 28 processes: 7 group shared services, 8 Grocery Retail, 7 Grocery Wholesale, and 6 Financial Services. 13 are High, 12 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-RT01 In-store checkout and card authorization | Grocery Retail | High | 2 h | 1 h | 0 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G05 Digital front door | Group | High | 4 h | 2 h | 1 h |
| BP-RT07 SNAP EBT acceptance | Grocery Retail | High | 4 h | 2 h | 0 h |
| BP-RT06 Store refrigeration monitoring and food safety | Grocery Retail | High | 4 h | 2 h | 1 h |
| BP-WD06 Distribution center cold chain monitoring | Grocery Wholesale | High | 4 h | 2 h | 1 h |
| BP-G04 Data centers and wide-area network | Group | High | 8 h | 4 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-RT02 Online ordering and checkout | Grocery Retail | High | 8 h | 4 h | 1 h |
| BP-WD01 Distribution center picking and shipping | Grocery Wholesale | High | 12 h | 6 h | 1 h |
| BP-WD02 Transportation dispatch and routing | Grocery Wholesale | High | 12 h | 8 h | 4 h |
| BP-FS03 Cardholder service and lost or stolen card reporting | Financial Services | High | 12 h | 4 h | 1 h |
| BP-FS01 Rewards Card authorization | Financial Services | Moderate | 8 h | 4 h | 0 h |
| BP-RT03 Pickup and delivery fulfillment | Grocery Retail | Moderate | 24 h | 8 h | 4 h |
| BP-RT04 Item and price file to stores | Grocery Retail | Moderate | 24 h | 12 h | 4 h |
| BP-WD03 Retailer Services Portal | Grocery Wholesale | Moderate | 24 h | 8 h | 4 h |
| BP-WD05 Traceability and recall records | Grocery Wholesale | Moderate | 24 h | 12 h | 4 h |
| BP-RT08 Store ordering and receiving | Grocery Retail | Moderate | 24 h | 12 h | 4 h |
| BP-FS02 Credit applications and decisioning | Financial Services | Moderate | 24 h | 8 h | 4 h |
| BP-FS04 Payments posting and statements | Financial Services | Moderate | 48 h | 24 h | 4 h |
| BP-RT05 Loyalty, customer data platform, and offers | Grocery Retail | Moderate | 48 h | 24 h | 24 h |
| BP-WD04 Supplier EDI | Grocery Wholesale | Moderate | 48 h | 24 h | 4 h |
| BP-G06 ERP finance, merchandising, and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-WD07 Wholesale invoicing and customer payments | Grocery Wholesale | Low | 72 h | 48 h | 24 h |
| BP-FS05 Collections and recoveries | Financial Services | Low | 72 h | 48 h | 24 h |
| BP-FS06 Installment loan servicing | Financial Services | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Revenue per hour** drives in-store checkout (BP-RT01). About $1.6 million of in-store sales an hour stops when lanes cannot tender. Store-and-forward authorization within the processor's floor limits buys time, but only for brand cards and only within those limits. An RPO of 0 means no completed sale may be lost: each lane journals to the store controller.
- **Food safety** drives refrigeration and cold chain monitoring (BP-RT06, BP-WD06). Controllers keep cooling without the monitoring service, but nobody sees a failing case. Hourly manual rounds are the fallback.
- **Store supply** drives the distribution centers (BP-WD01, BP-WD02). Perishables on store shelves last 24 to 48 hours, so a 12-hour MTD keeps every store stocked.
- **Regulatory clocks** set three values that revenue alone would not: SNAP households must be able to buy food with benefits (BP-RT07; stores are authorized SNAP retailers under 7 CFR 278.1), cardholders must be able to report a lost or stolen card (BP-FS03; 12 CFR 1026.12(b)), and the wholesale division must produce food records within 24 hours of an FDA request (BP-WD05; 21 CFR 1.361).
- **Integrity matters more than uptime online** (BP-RT02). Online checkout can wait 8 hours, because customers can pay at pickup. A tampered checkout page cannot run for 8 minutes (P08).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops administration in all three divisions. Cashier sign-on is cached at store controllers, so lanes keep selling |
| Digital front door and tag management (SYS-G4) | Group | Retail checkout; wholesale portal; cardholder portal | One tag management container serves all three divisions' sites. It is a shared availability dependency and a shared integrity risk (P01 GR-01; P08) |
| Payment switch (SYS-D1, in group data centers) | Grocery Retail | Financial Services (Rewards Card authorization) | The retail switch routes store card authorizations; a switch outage stops Rewards Card purchases too |
| Rewards Card field on the retail checkout | Grocery Retail | Financial Services | Financial Services customer information is captured on a retail page (P03; P08) |
| Distribution centers (BP-WD01) | Grocery Wholesale | All 380 group stores | Wholesale is the supply chain for the focus division |
| Rewards Card data to the CDP | Financial Services | Grocery Retail marketing (BP-RT05) | Routine affiliate data flow; opt-outs must follow the data (P03; P10) |
| SOC facts (SYS-G2) | Group | Acquirer notice, FTC notice, state notices, wholesale customer notices, SEC filing | Every notice clock in P08 depends on the SOC establishing what happened |
| ERP (SYS-G5) | Group | Price files to stores; recall records; SEC reporting | Merchandising master data and the general ledger are shared |

**Single points of failure found:**
- SYS-G4 tag management, a single container for all divisions (P01 GR-01; POAM-001).
- The legacy store gateway that connects the 46 acquired stores to the payment switch (P01 RT-004).
- The central WMS instance for the two automated distribution centers, whose restore has never been tested at full volume (P01 WD-003).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| Payment switch (two data centers) | BP-RT01, BP-RT07, BP-FS01 | Active-active; transaction journals replicated synchronously |
| Store controllers and lanes | BP-RT01 | Lane journals at the controller; nightly polling to the data center |
| EPP storefront and order services | BP-RT02, BP-RT03 | Managed database replicas; warm standby in provider B |
| WMS (central instance and distribution center servers) | BP-WD01, BP-WD05 | Database log shipping to the secondary data center; nightly immutable backups |
| Card processing platform (vendor SaaS) | BP-FS01, BP-FS03, BP-FS04 | Vendor replication (RPO 15 minutes per contract; SOC 2 Availability report) |
| CDP and pricing engine | BP-RT05 | Daily snapshots; vendor engine restored from configuration |
| People | All | Cross-trained store and distribution center staff; remote work for cardholder service agents |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. Digital front door (only after integrity is confirmed, P08)
4. Data centers and wide-area network
5. SOC visibility (SIEM and EDR)
6. to 8. In-store checkout and card authorization, SNAP EBT acceptance, store refrigeration monitoring
9. Online ordering and checkout
10. to 12. Distribution center cold chain, picking and shipping, transportation dispatch
13. Cardholder service and lost or stolen card reporting
14. to 28. Rewards Card authorization, fulfillment, price files, the wholesale portal, traceability records, store ordering, credit decisioning, payments posting, loyalty and offers, supplier EDI, ERP and SEC reporting, payroll, wholesale invoicing, collections, and installment loan servicing.

## 8. Key findings
1. **Shared services set the floor.** Group identity, the cloud hub, and the digital front door have RTOs of 1 to 2 hours, shorter than any division process that depends on them. The identity RTO of 1 hour was met in two tests in 2026; the digital front door has never been tested as a whole (POAM-012).
2. **The digital front door is both an availability and an integrity dependency.** Restoring it fast is not enough. A compromised tag must not be restored with it, so the P08 runbook restores a known-good container before re-opening checkout pages.
3. **Regulatory clocks set some MTDs that revenue would not.** SNAP acceptance, lost or stolen card reporting, and FDA record requests are short because of the rules behind them, not because of the money.
4. **The acquired stores are the weakest recovery path.** The 46 stores depend on a legacy store gateway with no tested failover (P01 RT-004), until their migration in 2027.
5. **Notification capacity is itself a process** (BP-G02, BP-G06, BP-FS03). If the SOC, the disclosure committee's records, or the cardholder service line is down during an incident, notice clocks keep running. The P08 runbook uses out-of-band channels for this reason.
