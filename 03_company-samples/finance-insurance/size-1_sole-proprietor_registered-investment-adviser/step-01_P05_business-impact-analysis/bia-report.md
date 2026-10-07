# Business Impact Analysis: Cris Santos Company | Finance and Insurance | Sole Proprietorship

**Organization:** Cris Santos Company (state-registered investment adviser) | **Tier:** Sole Proprietorship (owner-adviser only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-adviser, 2026-07-14, with the on-call IT consultant (under a services agreement since 2026-07-10) | **Adopted:** Owner-adviser, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the adviser depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the FTC Safeguards Rule duty to identify and manage data, devices, and systems "in accordance with their relative importance to business objectives" (16 CFR 314.4(c)(2));
- the Florida duty to keep books and records the OFR can examine and to produce them promptly on written request (Fla. Stat. 517.121).

## 2. Business description
One owner-adviser manages about $19 million for about 70 client households from a home office in Florida. There are no employees. Client assets sit at one qualified custodian, which the adviser reaches through the custodian's advisor portal (SYS-01). Everything else is SaaS: a portfolio and billing platform, a CRM, a business email and file suite, financial planning software, e-signature, and accounting, reached from one laptop and one phone over the home network. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual fees, or about $720 per business day. The `impact_safety` column in `bia.csv` is used for **client financial harm**, because no process here affects physical safety.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week and a half of revenue), including any amount the adviser repays a client | $1,000 to $5,000 | Less than $1,000 |
| Operations | No trading or client requests can be handled | Work slowed or partly deferred | Administrative delay only |
| Regulatory | Reportable breach; records not produced to the OFR; fiduciary breach | Missed internal deadline or filing correction | Internal policy deviation |
| Client financial harm | A client loses money (fraudulent payment, unhedged market loss, tax penalty) | Delay a client notices but that costs nothing | None |
| Reputation | Client households leave; referral sources stop | Client complaints | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Portfolio management and trading | High | 24 h | 8 h | 24 h |
| BP-02 Client money movement and service requests | High | 48 h | 24 h | 24 h |
| BP-03 Client communications and meetings | Moderate | 48 h | 24 h | 24 h |
| BP-04 Fee billing and performance reporting | Moderate | 168 h | 72 h | 24 h |
| BP-05 Compliance recordkeeping and regulatory filings | Low | 120 h | 72 h | 24 h |

**What drives the values:** market exposure drives BP-01, because clients stay invested with no one able to trade. BP-02 is rated High for **integrity, not speed**: a fraudulent or mistaken payment can cost a client tens of thousands of dollars in one step, while a one-day delay costs nothing. Positions of record are held by the custodian, so the RPOs mainly protect the owner's own notes, models, and documents. The 24-hour RPO for BP-05 is **not supported today**: the only independent copy of email and files is a weekly USB backup (about 168 hours), and the suite keeps only 30 days of file versions (P01 R-004 and R-011).

**Single-person dependency (the key finding).** The owner-adviser is the only person with trading authority, the only person who can submit fee instructions or money movement requests, and the only holder of every password. The custodian portal's second factor is on the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-02 pass their MTD within two days, and clients cannot get advice on their accounts. Clients can still reach the custodian directly for withdrawals, which limits the harm. Actions (P01 R-005, due 2026-12-31):
1. Sign a written arrangement with another Florida-registered adviser to serve clients if the owner is incapacitated, and describe it in the client agreement update.
2. Keep recovery codes for the custodian portal, email, and CRM, plus a one-page emergency access sheet, in a sealed envelope held by the owner's attorney.
3. Register a second MFA method (a hardware security key kept in the home safe) on the custodian portal and email.
4. Ask the custodian what it needs to let a designated adviser act for clients, and record the answer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Custodian advisor portal | Trading, fee instructions, money movement, statements of record | BP-01, BP-02, BP-04, BP-05 |
| SYS-02 Portfolio and billing platform | Models, rebalancing, performance, fee calculation | BP-01, BP-04 |
| SYS-03 CRM | Client contact data (including the phone numbers used for callbacks), notes, onboarding files | BP-02, BP-03, BP-05 |
| SYS-04 Email and file suite | Client correspondence and documents | BP-02, BP-03, BP-05 |
| SYS-06 E-signature service | Custodian forms and advisory agreements | BP-02, BP-05 |
| SYS-07 Laptop, phone, USB drive | Access devices; MFA app; weekly backup copy | All |
| SYS-08 Home network | Internet; the phone hotspot is the fallback | All |
| Contracted services | Custodian, platform vendors, IT consultant, compliance consultant | All |
| People | Owner-adviser only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA app | 1 h | Recovery codes in the sealed envelope; hardware key (planned); replacement phone from the carrier |
| 2 | Internet | 1 h | Phone hotspot |
| 3 | A clean access device | 4 h | Borrowed or new laptop; the IT consultant rebuilds the old one |
| 4 | SYS-01 custodian portal | 8 h (custodian-hosted) | Custodian's adviser service desk by phone |
| 5 | SYS-03 CRM (callback numbers) and SYS-04 email | 24 h | Printed client contact list in the locked file cabinet |
| 6 | SYS-02 portfolio and billing platform | 72 h | Spreadsheet fee calculation from custodian data |
| 7 | SYS-05, SYS-06, SYS-10 | 72 h | Paper forms; custodian's own e-signature path |
