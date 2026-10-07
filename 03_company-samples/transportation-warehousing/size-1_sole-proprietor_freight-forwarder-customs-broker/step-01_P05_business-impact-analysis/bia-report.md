# Business Impact Analysis: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

**Organization:** Cris Santos Company (freight forwarder and customs broker) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-18, with the on-call IT consultant | **Adopted:** Owner, 2026-09-14

## 1. Overview and purpose
This one-page BIA lists the five business functions the brokerage depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the duty to make records available to CBP within 30 calendar days of a request (19 CFR 111.25(b)).

## 2. Business description
The owner is an individually licensed customs broker who also works as an FMC-licensed ocean freight forwarder from a home office in Florida. About 40 active clients send about 600 import entries and 250 export shipments a year. The customs and forwarding software (SYS-01) is vendor SaaS and is the system of record. Everything else runs on a laptop and a personal phone, a business email and file suite, an accounting SaaS, and online banking. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $720 per business day. Client money passing through the account (about $1.4 million a year) is counted in Cost because a misdirected payment must be made good.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week of revenue, or one freight wire) | $1,000 to $5,000 | Less than $1,000 |
| Operations | No entries can be filed or cargo is held | Filings or bookings slowed | Administrative delay only |
| Regulatory | CBP action against the license or permit, or a reportable breach | Missed filing or record deadline | Internal policy deviation |
| Safety | Not applicable: the business moves no cargo itself | | |
| Reputation | Clients move to another broker | Client complaints | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Import entry and ISF filing | High | 24 h | 8 h | 1 h |
| BP-02 Duty, freight, and client payments | High | 48 h | 24 h | 24 h |
| BP-03 Shipment coordination and client communications | Moderate | 24 h | 8 h | 24 h |
| BP-04 Export shipments and EEI filing | Moderate | 48 h | 24 h | 1 h |
| BP-05 Records, billing, and license administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** cargo drives BP-01. Containers arrive most business days, free time at the terminal is short, and every day of delay adds demurrage and storage charges that clients blame on the broker. ISF data is due 24 hours before the cargo is loaded at the foreign port (19 CFR 149.2(b)). BP-02 is rated High on cost, not time: one misdirected freight wire can exceed a month of revenue. The 1-hour RPO for BP-01 and BP-04 depends on the customs software vendor's backups (confirmed in its SOC 2 report, P09). The 24-hour RPO for BP-05 is **not supported today**: the scanned records archive syncs between the laptop and the cloud with no independent backup, so ransomware on the laptop would reach both copies (P01 R-003).

**Single-person dependency (the key finding).** The owner is the only licensed broker, the only person CBP can deal with, the only bank user, and the only holder of every credential. The customs software and email second factors are on the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 exceeds its 24-hour MTD on the first day, and no one else may lawfully transact customs business for these clients: another broker needs its own power of attorney from each client before acting (19 CFR 141.46). Actions (P01 R-005, due 2026-12-31):
1. Sign a written coverage agreement with the nearby backup broker, and offer clients a standby POA with that broker.
2. Store recovery codes for the customs software, email, and bank, with a one-page emergency sheet, in a sealed envelope held by the owner's attorney.
3. Name a records custodian in the emergency sheet so the notice required on permanent termination of the business can be given (111.30(e)).
4. Wipe and reinstall the 2019 laptop as a clean spare device (P07 POAM-008).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Customs and forwarding software (SaaS) | Entries, ISF, EEI, shipment files; vendor backups | BP-01, BP-04 |
| SYS-07 Mobile phone | Second factors; calls; chats with agents | BP-01, BP-02, BP-03 |
| SYS-06 Laptop | Main work device; synced archive | BP-01, BP-03, BP-04, BP-05 |
| SYS-08 Home network | Internet; phone hotspot is the fallback | BP-01, BP-03 |
| SYS-04 Business banking | Duty payments and freight wires | BP-02 |
| SYS-02 Email and file suite | Correspondence and records archive | BP-03, BP-05 |
| SYS-03 Accounting SaaS | Invoices and client ledgers | BP-02, BP-05 |
| SYS-05 CBP portals | Broker submissions and trade account | BP-01, BP-05 |
| People | Owner only; contract bookkeeper monthly | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and authenticator app | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet | 1 h | Phone hotspot |
| 3 | A clean access device | 4 h | Wiped spare laptop (after POAM-008); laptop reinstalled by the IT consultant |
| 4 | SYS-01 customs software access | 8 h (vendor-hosted) | Backup broker files urgent entries under its own POA |
| 5 | SYS-02 email | 8 h | Phone and carrier portals |
| 6 | SYS-04 business banking | 24 h | Bank business service line; branch visit |
| 7 | SYS-03 accounting and SYS-02 records archive | 72 h | Invoice from the customs software; rebuild files from SYS-01 and carrier portals |
