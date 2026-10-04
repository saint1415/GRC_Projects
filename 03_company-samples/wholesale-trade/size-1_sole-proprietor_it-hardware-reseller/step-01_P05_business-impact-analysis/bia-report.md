# Business Impact Analysis: Cris Santos Company | Wholesale Trade | Sole Proprietorship

**Organization:** Cris Santos Company (IT hardware reseller) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-04, with the on-call IT consultant | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the owner's promise to the prime contractor that DoD deliveries can continue after a disruption.

## 2. Business description
One person quotes, buys, stages, delivers, and bills from a home office and an attached garage in Florida. About 45 small-business customers and 3 managed service providers buy network equipment, mostly drop-shipped by two authorized distributors. One DoD prime contractor buys staged and asset-tagged equipment for a DoD installation (about 23% of receipts). The order management system is an accounting and inventory SaaS (SYS-01). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $720 per business day (about $160 of gross margin).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (more than a month of gross margin) | $1,000 to $5,000 | Less than $1,000 |
| Operations | No orders can be quoted, bought, or delivered | Orders delayed or partly rescheduled | Administrative delay only |
| Regulatory and contract | A missed FAR or DFARS clause duty, or loss of eligibility for the prime's orders | A missed delivery date or report the prime must chase | Internal policy deviation |
| Safety | Not applicable: the business sells office network equipment and does no installation work | | |
| Reputation | Loss of the prime or of a managed service provider customer | Customer complaints or lost quotes | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Quoting and order entry | High | 48 h | 24 h | 24 h |
| BP-02 Purchasing and receiving | High | 48 h | 24 h | 24 h |
| BP-03 DoD staging and delivery for the prime | High | 72 h | 48 h | 8 h |
| BP-04 Invoicing, collections, and supplier payments | Moderate | 120 h | 72 h | 24 h |
| BP-05 Customer support, returns, and warranty | Moderate | 72 h | 48 h | 24 h |

**What drives the values:** lost sales drive BP-01 and BP-02, because small-business customers buy elsewhere when a quote or a drop shipment is late. Contract duties drive BP-03: the prime's building schedule allows about 3 business days of slack, and the serial-to-tag spreadsheet is both the delivery record and Federal Contract Information (FCI). The 24-hour RPO for BP-01, BP-02, and BP-04 matches the accounting SaaS vendor's stated RPO (SOC 2 system description, reviewed 2026-08-05; P09). The **8-hour RPO for BP-03 is not supported today**: the spreadsheet is often saved only on the laptop, and the laptop has no backup (P01 R-014).

**Single-person dependency (the key finding).** The owner is the only buyer, staging technician, bookkeeper of record, and the only holder of every password and second factor. If the owner is ill, injured, or without the phone, every function exceeds its MTD at once. Nobody else can reach the accounting SaaS, the distributors, or the prime, and the prime will buy elsewhere. Actions (P01 R-011, due 2026-12-31):
1. Write a one-page emergency sheet: whom to call (prime, distributors, top 10 customers) and what to tell them. It holds no passwords.
2. Store the recovery codes for email, the accounting SaaS, and the bank in a sealed envelope held by the owner's attorney, for use only to wind down or hand over open orders.
3. Ask both distributors to note on the account that open drop shipments may be released on a call from the attorney.
4. Agree with the prime in writing that it may source open orders elsewhere if the owner is unavailable for more than 3 business days. Household members do not receive access to FCI or business accounts.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Accounting and inventory SaaS | Quotes, orders, stock, serials, invoices; vendor backups | BP-01, BP-02, BP-03, BP-04 |
| SYS-02 Email and file storage | Customer and supplier email; asset tag spreadsheets | BP-01, BP-03, BP-04, BP-05 |
| SYS-03 Distributor and OEM portals | Pricing, ordering, drop shipments, serial lookup, warranty | BP-01, BP-02, BP-05 |
| SYS-05 Laptop | Every business task; console staging | BP-01, BP-03 |
| SYS-06 Phone | Second factor for email; calls; photos of serial labels | BP-01, BP-05 |
| SYS-07 Home network | Internet; phone hotspot is the fallback | All |
| SYS-08 Garage bench and cabinet | Stock and staged DoD equipment | BP-02, BP-03 |
| SYS-09 Bank and card | Payments in and out | BP-04 |
| People | Owner only (bookkeeper read-only; IT consultant on call) | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factors | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the home office | 1 h | Phone hotspot |
| 3 | A clean laptop | 8 h | One old laptop, wiped and rebuilt by the IT consultant as the spare (P07 POAM-004) |
| 4 | SYS-02 Email and files (vendor-hosted) | 4 h | Web access from the spare laptop or phone |
| 5 | SYS-01 Accounting and inventory SaaS | 8 h | Spreadsheet quotes and paper order log |
| 6 | SYS-03 Distributor portals | 24 h | Phone orders to distributor account representatives |
| 7 | SYS-08 Bench and stock (BP-03) | 48 h | Paper serial sheets; tell the prime the same day |
| 8 | SYS-09 Bank | 72 h | Branch visit; pay distributors on terms |
