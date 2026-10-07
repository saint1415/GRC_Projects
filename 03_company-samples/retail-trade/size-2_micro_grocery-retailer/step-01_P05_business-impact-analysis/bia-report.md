# Business Impact Analysis: Cris Santos Company | Retail Trade | Micro

**Organization:** Cris Santos Company, LLC (neighborhood grocery store with online ordering) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Store Manager (Security and PCI Lead) with the Owner, the Bookkeeper, and the MSP technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the store, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Availability criteria in the SOC 2 readiness check (P09).

No law requires a grocery store of this size to keep a contingency plan. PCI DSS v4.0.1 asks for an incident response plan (Requirement 12.10), not a business continuity plan. The BIA is here because the store loses most of its sales when card payments stop, and because hurricanes are a yearly risk in Florida.

## 2. System and business description
One Florida store of about 4,500 square feet, 7 employees, about $3,000 of sales a day, and about 5 online orders a day for curbside pickup or local delivery. Almost everything runs on one commerce platform from one provider: the POS app, the P2PE card terminals, card processing, the online store, and the loyalty directory (SYS-01 to SYS-03). Email and files are in a productivity suite (SYS-04). On site are the office PC, the Owner's laptop, 2 POS tablets, the store phone (SYS-05), the store network (SYS-06), temperature sensors (SYS-08), and cameras (SYS-09). The MSP runs the office IT. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual sales, about $3,000 a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $6,000 (about 2 days of sales) | $1,500 to $6,000 | Less than $1,500 |
| Operations | The store cannot sell or must close | One function stops; customers slowed | Staff slowed but working |
| Regulatory | Reportable breach or loss of SNAP authorization | Missed contractual or tax deadline | Internal policy deviation |
| Safety | Unsafe food could reach customers | Food discarded as a precaution | None |
| Reputation | Local news coverage or lasting loss of regular customers | Complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 In-store checkout and payments | High | 4 h | 2 h | 1 h |
| BP-02 Online ordering and online payment | Moderate | 24 h | 8 h | 1 h |
| BP-03 Order picking, curbside pickup, and delivery | Moderate | 24 h | 8 h | 4 h |
| BP-04 Refrigeration monitoring and food safety | High | 4 h | 2 h | 24 h |
| BP-05 Receiving, inventory, pricing, and markdowns | Moderate | 48 h | 24 h | 24 h |
| BP-06 Bookkeeping, supplier payments, and payroll | Moderate | 72 h | 48 h | 24 h |
| BP-07 Loyalty and customer communications | Low | 72 h | 48 h | 24 h |
| BP-08 Store security and loss prevention | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **Card payments drive BP-01.** About 75% of sales are by card or SNAP EBT. Cash-only trading keeps the doors open, but most shoppers leave, so half a day without cards costs more than a full day of most other outages.
- **Food safety drives BP-04.** A cooler failure that goes unnoticed overnight is the most expensive single event the store faces, and the only one that can harm customers. The RPO of 24 hours reflects the alert history, which is helpful but not essential.
- **Online orders tolerate a day (BP-02, BP-03)** because they are about 9% of sales and customers can be called and switched to in-store pickup.
- **Back office functions tolerate 72 hours (BP-06 to BP-08)** because payroll is biweekly, the cash reserve covers about 3 weeks, and the platform keeps the sales history.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Commerce platform (SaaS) | POS app, dashboard, card processing, customer directory | Provider's replication and backups (SOC 2 system description states RTO 4 h and RPO 1 h; see P09) | BP-01, BP-02, BP-05, BP-07 |
| SYS-02 Online store (SaaS) | Catalog, accounts, orders, provider-hosted checkout | Same provider platform | BP-02, BP-03 |
| SYS-03 Card terminals | 2 countertop P2PE terminals; 1 mobile reader | Provider ships replacement terminals; no local data | BP-01, BP-03 |
| SYS-04 Productivity suite (SaaS) | Email, shared orders mailbox, files | Vendor service resilience | BP-06, BP-07 |
| SYS-05 Endpoints | Office PC, Owner laptop, 2 POS tablets, store phone | Office PC files copied nightly to SYS-11; tablets and phone hold no data that is not in the platform | All |
| SYS-06 Store network and internet | Firewall and Wi-Fi; one internet line | MSP keeps a copy of the firewall configuration | BP-01, BP-02, BP-04 |
| SYS-07 Accounting SaaS and payroll service | Books and payroll | Vendor services | BP-06 |
| SYS-08 Temperature sensors | 6 sensors with a cloud app | Alerts only; paper log as the fallback | BP-04 |
| SYS-11 Cloud backup (MSP) | Nightly copy of the office PC, 30 days of versions | **Never restore-tested** | BP-05, BP-06 |
| People | Owner, Store Manager, Bookkeeper, 2 Cashiers, Stock and Produce Clerk, Order Picker and Delivery Driver | Cross-training: the Store Manager can run a register and pick orders; the Owner can do the Bookkeeper's urgent tasks | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Payment and commerce platform provider | BP-01, BP-02, BP-03, BP-05, BP-07 | SOC 2 Type 2 report (Security and Availability) reviewed 2026-08-25 (P09): stated RTO 4 h and RPO 1 h |
| Internet provider | BP-01, BP-02, BP-04 (alerts) | None; one line, no failover |
| MSP | Recovery of the office PC, laptop, firewall, and Wi-Fi; runs the backup | No written recovery commitment; 4-business-hour response time only |
| Productivity suite vendor | BP-06, BP-07 | Vendor service commitments (standard terms) |
| Sensor vendor | BP-04 alerts | None; manual checks are the fallback |
| Accounting SaaS vendor and payroll service | BP-06 | Vendor service commitments |

**Key findings:**
1. **One provider runs almost everything.** A platform outage stops card payments, online orders, and loyalty at the same moment (risk R-013). The store cannot buy its way out of this at its size; it relies on a cash-only procedure and the provider's assurance report.
2. **The provider's recovery time is longer than the store can wait.** The provider states an RTO of 4 hours; BP-01 needs card payments back within 2 hours. The gap is covered only by cash-only trading, which must be written down and practiced (R-013).
3. **The internet line is a single point of failure** for card authorization, online order alerts, and temperature alerts (R-014, R-015). A cellular failover router fixes all three.
4. **Refrigeration alerts fail silently.** If the internet or Wi-Fi drops at night, no alert is sent and nobody knows (R-015).
5. **The office PC backup is unproven.** SYS-11 has never been restored, so the 24-hour RPO for BP-05 and BP-06 is an assumption (R-021). The MSP contract has no recovery commitment.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and store network (SYS-06) | 1 h | Cellular failover router (to be installed by 2026-11-30); the store phone's hotspot for one terminal until then |
| 2 | Refrigeration alerts (SYS-08) | 2 h | Manual thermometer checks every 2 hours on a paper log |
| 3 | Card terminals and POS tablets (SYS-03, SYS-05) | 2 h | Cash only with the printed price list; replacement terminals shipped by the provider |
| 4 | Online store and order alerts (SYS-02) | 8 h | Phone orders paid at pickup; delivery paused |
| 5 | Picking and delivery (BP-03) | 8 h | Printed pick lists; prepaid orders only |
| 6 | Receiving and pricing (BP-05) | 24 h | Paper receiving log; handwritten markdown stickers |
| 7 | Email, accounting, and payroll (SYS-04, SYS-07) | 48 h | Payroll service repeats the prior payroll |
| 8 | Office PC restore (SYS-11 to SYS-05) | 48 h | Supplier spreadsheets rebuilt from emails and invoices |
