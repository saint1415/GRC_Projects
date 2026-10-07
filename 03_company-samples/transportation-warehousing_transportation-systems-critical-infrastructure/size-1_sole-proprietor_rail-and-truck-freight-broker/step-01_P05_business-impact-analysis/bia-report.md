# Business Impact Analysis: Cris Santos Company | Transportation Systems | Sole Proprietorship

**Organization:** Cris Santos Company (freight broker arranging truck and rail shipments) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-10, with the on-call IT consultant | **Adopted:** Owner, 2026-09-08

## 1. Overview and purpose
This one-page BIA lists the five business functions the brokerage depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system security plan (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the owner's answer to the largest shipper's yearly security questionnaire (P09).

## 2. Business description
The owner books about 1,100 truckloads and coordinates about 260 rail carloads a year from a home office in northeast Florida. On a normal weekday 6 to 10 truckloads are in transit. The broker never touches the freight: motor carriers haul it, and railroads move the rail cars that the owner orders for 4 shippers through the railroads' customer portals. Everything runs on SaaS (the TMS, email and files, accounting, the bank portal, the load board, the carrier monitoring service, and the tracking app), one laptop, and one phone. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 of annual margin, or about $720 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week of margin, or one diverted carrier payment) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Loads cannot be booked or loads in transit cannot be followed | Booking or tracing slowed; some loads handed back to shippers | Administrative delay only |
| Regulatory | FMCSA broker authority suspended, or a breach notice duty missed | A registration update or record duty missed | Internal policy deviation |
| Safety | Cargo stolen or a driver put at risk because a load was not watched | Delayed response to a delivery problem | None |
| Reputation | Loss of a top shipper or a railroad's portal access | Carrier complaints on load boards; shipper complaints | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Load booking and carrier selection (truck) | High | 24 h | 8 h | 24 h |
| BP-02 In-transit tracking and exception handling | High | 8 h | 4 h | 4 h |
| BP-03 Rail carload coordination | Moderate | 24 h | 8 h | 24 h |
| BP-04 Billing, carrier pay, and collections | Moderate | 72 h | 48 h | 24 h |
| BP-05 Registration, compliance, and records | Moderate | 120 h | 72 h | 24 h |

**What drives the values:**
- **Loads in transit drive BP-02.** Freight moves around the clock. If nobody answers a driver or a receiver for one shift, appointments are missed and the shipper's trust goes with them. Watching loads is also how a fictitious pickup or cargo theft is caught.
- **The TMS vendor's recovery point does not meet BP-02.** The vendor states an RPO of 24 hours in its SOC 2 system description (P09). The BIA needs 4 hours for in-transit status. Until a better option exists, the owner downloads the in-transit list (driver, phone, appointment, consignee) at 7 a.m. and 2 p.m. each business day (P01 R-010).
- **Regulation drives BP-05 more than its daily volume suggests.** A surety claim or an FMCSA suspension notice must be answered within 7 business days (49 CFR 387.307(e)(1)(ii), (e)(5)-(6)). Losing broker authority would stop BP-01 for good. The 120-hour MTD leaves 2 business days of margin inside that window.
- **BP-03 data lives at the railroads.** The portals keep car orders and shipping instructions, so the owner's RPO is only the owner's own notes.

**Single-person dependency (the key finding).** The owner is the only person who books loads, talks to drivers, holds the railroad portal user IDs, sends carrier payments, and receives FMCSA and surety notices. The email MFA codes go by text to the owner's one phone. If the owner is ill, injured, or without the phone, BP-02 exceeds its MTD within 8 hours, loads in transit go unwatched, carriers go unpaid, and a bond claim could go unanswered. Actions (P01 R-009, due 2026-12-31):
1. Sign a written backup broker agreement with a registered broker who will follow loads in transit and tell shippers and carriers what is happening.
2. Keep a sealed emergency access sheet (recovery codes for email, TMS, and accounting; bank and surety contacts; the in-transit list procedure) with the transportation attorney.
3. Give the attorney a signed letter authorizing a response to any surety claim or FMCSA notice on the owner's behalf.
4. Register a second MFA method (a hardware security key) for email and the TMS and keep it in the sealed envelope.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 TMS (vendor SaaS) | Loads, carriers, rate confirmations, documents, invoices, payables; vendor backups (RPO 24 h) | BP-01, BP-02, BP-04, BP-05 |
| SYS-08 Phone and business line | Calls and texts with drivers and shippers; email MFA codes; TMS mobile app | BP-01, BP-02 |
| SYS-07 Laptop | Main workstation; synced carrier packet folders | BP-01, BP-03, BP-04 |
| SYS-02 Email and files | Tenders, rate confirmations, carrier packets, contracts | BP-01, BP-03, BP-05 |
| SYS-06 Tracking app | Driver location during loads | BP-02 |
| SYS-10 Railroad portals | Car orders, shipping instructions, tracing | BP-03 |
| SYS-03 and SYS-04 Accounting and bank | Invoices, payables ledger, ACH | BP-04 |
| SYS-05 Load board and carrier monitoring | Finding and checking carriers | BP-01 |
| SYS-11 FMCSA registration account | Broker authority record | BP-05 |
| People | Owner only; bookkeeper monthly; IT consultant on call | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone, business number, and email MFA | 1 h | Recovery codes in the sealed envelope; replacement phone and SIM from the carrier (port-out PIN set first) |
| 2 | In-transit list and contact with drivers | 1 h | Last downloaded in-transit list; tracking app web page; phone |
| 3 | Internet at the home office | 1 h | Phone hotspot |
| 4 | SYS-01 TMS access from a clean device | 4 h | TMS mobile app on the phone; new laptop bought the same day |
| 5 | SYS-10 Railroad portals | 8 h | Shipper's own traffic staff; railroad customer service by phone |
| 6 | SYS-02 Email and files | 8 h | Phone email app; vendor web portals |
| 7 | SYS-03 and SYS-04 Accounting and bank | 48 h | Hold the ACH batch; bank portal from the clean device |
