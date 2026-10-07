# Business Impact Analysis: Cris Santos Company | Wholesale Trade | Micro

**Organization:** Cris Santos Company, LLC (IT hardware and software reseller) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (security and compliance lead) with the Owner, the Purchasing and Inventory Coordinator, the Bookkeeper, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- a short contingency plan (SP 800-53 CP-2), which the company does not have today;
- the availability rating in the SSP (P02) for the Reseller Operations Platform (ROP);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No regulation sets recovery times for an IT reseller. The drivers are revenue, customer delivery dates, and the federal reporting clocks that keep running during an outage. The FAR 52.204-25(d) report on covered equipment is due within 1 business day of identification, even if the email system is down.

## 2. System and business description
One Florida flex unit holds the office and a 2,000 sq ft stockroom with a setup bench. Seven people quote, buy, set up, and ship IT hardware and software to about 85 commercial accounts and to DoD end users (about 22% of revenue). Most products ship from distributor stock (drop-ship) or arrive the next day. Almost everything runs in SaaS: the ERP with its customer portal (SYS-01), the productivity suite (SYS-02), and the supplier portals (SYS-06). On site are 9 computers and the scanners and label printer (SYS-03), the network (SYS-04), and the stockroom security devices (SYS-09). The MSP runs IT. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue: about $4,400 of revenue and about $920 of gross profit per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (lost gross profit, expedite fees, a lost payment) | $2,000 to $10,000 | Less than $2,000 |
| Operations | The company cannot quote, buy, or ship | One function stops; orders slowed | Staff slowed but working |
| Regulatory | Missed FAR 52.204-25(d) report; covered equipment delivered on a DoD order; unsupported CMMC affirmation relied on | Late notice to a contracting officer or the Federal Prime; clause records incomplete | Internal policy deviation |
| Safety | Not used. A process outage does not harm people. Product integrity harm (counterfeit or tampered equipment reaching a DoD network) is rated in P01 | | |
| Reputation | Loss of the Federal Prime or a DoD contracting office as a customer | Customer complaints; questions on the supplier questionnaire | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Quoting and order entry | High | 24 h | 8 h | 1 h |
| BP-02 Purchasing and drop-ship ordering | High | 24 h | 8 h | 4 h |
| BP-03 Federal order administration and compliance reporting | High | 24 h | 8 h | 24 h |
| BP-04 Receiving, setup, and shipping | Moderate | 48 h | 24 h | 24 h |
| BP-05 Customer portal ordering | Moderate | 48 h | 24 h | 1 h |
| BP-06 Invoicing, collections, and supplier payments | Moderate | 72 h | 48 h | 4 h |
| BP-07 Customer service, returns, and warranty | Moderate | 48 h | 24 h | 24 h |
| BP-08 Payroll, HR, and office administration | Low | 120 h | 72 h | 24 h |

Counts: 3 High, 4 Moderate, 1 Low (8 processes).

**What drives the values:**
- An MTD of 24 hours is one business day. Commercial customers can buy the same products from many resellers, so a quote or order not confirmed within a day is often lost (BP-01, BP-02).
- BP-03 needs little IT but is High because of the 1-business-day Section 889 report and because DoD eligibility carries about 22% of revenue. It must work from any clean laptop with a printed contact list.
- BP-06 tolerates 72 hours because distributor terms allow 30 days and the cash reserve covers about 45 days. Its workaround forbids paying any new bank account without a call-back (the April 2026 diversion).

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 ERP with customer portal (SaaS) | Quotes, orders, purchasing, inventory, accounting, portal | ERP vendor backups and replication (SOC 2 report states RTO 4 h and RPO 1 h; see P09) | BP-01, BP-02, BP-04, BP-05, BP-06, BP-07 |
| SYS-02 Productivity suite (SaaS) | Email, shared files (including the "Orders" folder with customer equipment lists) | Vendor service resilience; nightly copy to SYS-05 | BP-01, BP-03, BP-04, BP-07, BP-08 |
| SYS-05 Suite backup (SaaS) | Nightly copy of mail and files, 30 days of versions | **Never restore-tested** | BP-08 and recovery of BP-03 records |
| SYS-06 Supplier portals | Pricing, ordering, drop-ship, returns | Supplier-hosted | BP-01, BP-02, BP-07 |
| SYS-07 Business banking and payment page | Supplier payments; customer card payments | Bank-hosted | BP-06 |
| SYS-03 Endpoints | 7 staff laptops, 1 spare laptop, setup bench desktop, scanners, label printer | Laptops hold no master data by design; the bench holds customer settings files and images | All |
| SYS-04 Network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All on-site work |
| People | 7 staff; the Owner and Operations Manager cover each other | Cross-training: the Owner can quote, buy, and pay | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| ERP vendor | BP-01, BP-02, BP-04 to BP-07 | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 1 h meet this BIA |
| National distributors (2) | BP-01, BP-02 (78% of purchase spend) | None obtained; each has its own portal and phone ordering |
| MSP | Recovery of every on-site system; operates the backup | No written recovery commitment; 4-business-hour response only |
| Productivity suite vendor | BP-03, BP-04, BP-07, BP-08 | Vendor service commitments (standard terms) |
| Backup service (through the MSP) | Restore of mail and files | None until the first restore test |
| Bank and payment processor | BP-06 | Bank service commitments |
| Internet provider | Every SaaS function from the office | None; single line. Staff can work from home |

**Key findings:**
1. **The ERP vendor meets the BIA.** Its stated RTO (4 h) and RPO (1 h) meet the targets for BP-01, BP-02, and BP-05.
2. **The suite backup is unproven.** SYS-05 has never been restore-tested, so the recovery of email and the shared folder (clause records, customer equipment lists, HR files) is an assumption (risk R-007).
3. **Federal reporting has no fallback today.** Nobody has a DIBNet account or a printed contact list, so BP-03 cannot meet its 8-hour RTO in an incident (R-019).
4. **The MSP contract has no recovery commitment.** The 4-business-hour response time is not a recovery time. A recovery term is added at renewal (R-010).
5. **Concentration on one distributor.** One national distributor carries most purchases. Its outage or a credit hold stops BP-02 even when every company system works (R-023).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | One clean laptop with the incident binder for BP-03 | 4 h | Spare laptop kept powered off in the Owner's office |
| 2 | Internet and office network (SYS-04) | 4 h | Work from home on laptops; phone hotspot |
| 3 | Suite access and email (SYS-02) | 8 h | Phones; vendor-hosted and usually unaffected |
| 4 | ERP access (SYS-01) | 8 h | Distributor portals and a spreadsheet order log |
| 5 | Supplier portals (SYS-06) with named logins | 8 h | Distributor phone ordering |
| 6 | Setup bench and label printer (SYS-03) | 24 h | Carrier web labels; delay setup orders |
| 7 | Banking (SYS-07) | 48 h | Hold payments; urgent payments only to known accounts after call-back |
| 8 | Shared folder restore (SYS-05 to SYS-02) | 72 h | Request equipment lists again from customers; payroll service repeats prior payroll |
