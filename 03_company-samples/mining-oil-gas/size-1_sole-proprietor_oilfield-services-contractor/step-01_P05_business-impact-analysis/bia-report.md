# Business Impact Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

**Organization:** Cris Santos Company (owner-operated oilfield services contractor, NAICS 213112) | **Tier:** Sole Proprietorship (owner-operator only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-operator, 2026-07-21, with the on-call IT technician | **Adopted:** Owner-operator, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the contractor depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- CSF 2.0 GV.OC-04, ID.AM-05, and RC.RP subcategories in the voluntary benchmark (P03), and the business continuity questions in Customer A's annual security questionnaire.

## 2. Business description
One person pumps 34 wells for 4 small producers every day and programs and troubleshoots field controllers for 2 of them. The work is physical, but it now runs on a phone, a rugged laptop with licensed configuration software, a business email and file account, an accounting service, and two customer remote access paths. The owner has no SCADA of its own; the field equipment belongs to the customers. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000, or loss of Customer A (about 45% of receipts) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Rounds missed or a customer well or tank battery down because of the owner | Rounds late or service calls delayed | Administrative delay only |
| Regulatory and contract | Breach of Customer A's MSA security schedule, or a Florida breach notice | Missed contract deadline (for example the questionnaire) | Internal policy deviation |
| Safety and environment | Plausible release, overflow, or unsafe equipment state at a customer site | Delayed but safe operation | None |
| Reputation | Customer ends or does not renew an MSA | Customer complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Contract pumping rounds | High | 24 h | 8 h | 24 h |
| BP-02 Well-site automation service | High | 48 h | 24 h | 0 h (every approved program version) |
| BP-03 Customer reporting and communications | Moderate | 24 h | 8 h | 24 h |
| BP-04 Invoicing and payments | Moderate | 168 h | 72 h | 24 h |
| BP-05 Business administration | Low | 168 h | 72 h | 24 h |

**What drives the values:** safety and the environment drive BP-01 and BP-02. A tank battery that nobody checks for a day can overflow, and a controller left with a wrong or missing program can stop a well or upset a tank battery. Customers' hardwired high-level shutdowns limit the worst case, which is why BP-02 can wait 48 hours and not less. The RPO of 0 for BP-02 means that every program version a customer approved must be recoverable, because the owner may be the only one holding the current copy. **That RPO is not supported today**: program copies live only on the laptop and its synced folder, which ransomware or a sync error would damage at the same time (P01 R-007). BP-04 matters less than it looks, because customers pay monthly on 30-day terms, but a fake payment-change email could divert a month of receipts (P01 R-002).

**Single-person dependency (the key finding).** The owner-operator is the only pumper, the only programmer, the only person who knows each customer's equipment, and the only holder of every credential. Email MFA codes arrive on the one phone. If the owner is ill, injured on site, or without the phone, BP-01 exceeds its MTD the next morning and nobody can reach the customers' program copies or the accounts. Actions (P01 R-010, due 2026-12-31):
1. Turn the informal arrangement with the nearby contract pumper into a written mutual coverage agreement, and tell each customer who covers the rounds.
2. Keep a one-page route sheet per customer (well list, gauging order, who to call) in the truck and the home office.
3. Store account recovery codes and an emergency access sheet in a sealed envelope with a trusted family member, and record where the current program copies are (POL-01 7.6).
4. Give each automation customer a copy of its own current programs after each approved change, so the customer is not dependent on the owner's laptop (POL-01 8.5).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-04 Smartphone | Customer contacts; alarm viewer; MFA codes; hotspot; photos | BP-01, BP-02, BP-03 |
| SYS-03 Field laptop | Licensed configuration software; VPN and remote clients; program copies | BP-02, BP-03 |
| SYS-01 Productivity suite | Email; gauge sheets; program copies (synced) | BP-01, BP-02, BP-03, BP-05 |
| SYS-02 Accounting service | Invoices and payments | BP-04 |
| SYS-06 USB drives and cables | Program transfers on site | BP-02 |
| SYS-05 Customer remote access | Customer A VPN; Customer B remote-desktop tool | BP-02 |
| People and facilities | Owner-operator only; service truck; home office; nearby contract pumper (informal) | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner able to work, phone and customer contacts | 2 h | Replacement phone from the carrier; printed contact list and route sheets in the truck |
| 2 | Pumping rounds | 8 h | Paper gauge book; gauges by phone or text; coverage by the nearby pumper |
| 3 | Email access (SYS-01) | 8 h | Recovery codes in the sealed envelope; webmail from any clean device |
| 4 | A clean laptop with configuration software and customer program copies | 24 h | IT technician rebuilds or replaces the laptop and transfers licenses (about one working day); offline program copies (planned) |
| 5 | Customer remote access | 24 h | Customer A reissues VPN access; site visits instead of remote work |
| 6 | Accounting service | 72 h | Paper invoices from a template |
