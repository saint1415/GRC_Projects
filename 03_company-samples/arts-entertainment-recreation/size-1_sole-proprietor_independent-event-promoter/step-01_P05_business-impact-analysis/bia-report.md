# Business Impact Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

**Organization:** Cris Santos Company (independent event promoter with one leased room) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-07-28, with the on-call IT consultant | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the incident response policy section on continuity (P06, POL-01 section 11);
- the recovery order in the incident runbook (P08).

## 2. Business description
The owner promotes about 60 public shows a year in the Room, a leased 280-person room in Florida, and rents it for about 15 private events. The business has no employees. Tickets are sold on a ticketing platform (SYS-01) with an integrated payment processor (SYS-02). Marketing runs on a website builder (SYS-03), email, and social media, with a freelance marketing assistant. Door staff come from a crowd management contractor. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in gross receipts, or about $2,500 in tickets per show.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about two shows) | $1,000 to $5,000 | Less than $1,000 |
| Operations | A show cannot open its doors or an on-sale fails | Sales or announcements delayed by a day or more | Administrative delay only |
| Regulatory and contractual | Card data compromise (processor notice; card brand rules; breach notices) | Missed processor, tax, or fee-display requirement | Internal policy deviation |
| Safety | Crowd count unknown at capacity (fire code) | Slow or crowded entry | None |
| Reputation | Fans or agents stop buying or booking | Complaints or poor reviews | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Show-night operations | High | 2 h | 1 h | 0 |
| BP-02 Ticket sales and on-sales | High | 24 h | 4 h | 0 |
| BP-03 Marketing and patron communications | Moderate | 72 h | 24 h | 24 h |
| BP-04 Booking and artist settlement | Moderate | 72 h | 24 h | 24 h |
| BP-05 Finance and administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** a show cannot be moved once doors are set, so BP-01 has the shortest limit. The scanner app works offline with the attendee list downloaded before doors, which is why a 1-hour RTO is achievable even if the internet fails. The RPO of 0 for BP-01 and BP-02 depends on the ticketing vendor, which holds every order and payment; its SOC 2 report states its recovery commitments (P09). On-sale days are the exception inside BP-02: an outage of more than 2 hours on an on-sale day loses most first-day sales, so the owner postpones and re-announces rather than letting fans fail at checkout.

**Single-person dependency (the key finding).** The owner is the only person who can run settlement, the guest list, pricing, payouts, refunds, and the processor portal. Every credential and the only authenticator app are on the owner's phone, and the marketing assistant works today only because it shares the owner's own logins (a gap, P01 R-001). If the owner is ill, injured, or without the phone on a show night, BP-01 exceeds its MTD within hours and nobody else can settle with the artist or refund fans. Actions (P01 R-009, due 2026-12-31):
1. Create named SYS-01 sub-users with limited roles for the marketing assistant and the door contractor's lead, so another person can run doors without the owner's login (2026-09-15).
2. Keep recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney (done 2026-07-31 for email, the processor portal, and accounting; add the ticketing platform and website after MFA is on).
3. Write a one-page show-night card for the door contractor's lead: download the attendee list before doors, print it, hand count at capacity, and whom to call.
4. Agree with a trusted fellow promoter to run settlement and refunds for up to two weeks if the owner cannot, with a sub-user account and written limits.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Ticketing platform | Event pages, checkout, scanner app, patron records, payouts; vendor backups | BP-01, BP-02, BP-03 |
| SYS-02 Payment processor | Merchant account, settlements, chargebacks, PCI portal | BP-02, BP-05 |
| SYS-07 Owner's phone | Authenticator app; calls; email; scanner backup | All |
| SYS-07 Scanning phones and laptop | Door scanning; office work | BP-01, BP-04 |
| SYS-08 The Room's internet and Wi-Fi | Internet for doors and the office; phone hotspot is the fallback | BP-01, BP-02 |
| SYS-03, SYS-05 Website, email marketing, social | Announcements and the checkout widget | BP-02, BP-03 |
| SYS-04 Email and files | Contracts, settlement sheets, fan email | BP-04, BP-05 |
| SYS-06 Accounting SaaS | Books and payments | BP-04, BP-05 |
| Contractors | Door and security contractor, marketing assistant, sound engineer, bookkeeper, IT consultant | BP-01, BP-03, BP-05 |
| People and place | The owner; the Room (lease) | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and authenticator | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Door scanning (SYS-01 scanner app) | 1 h on show nights | Offline attendee list; printed list and hand count |
| 3 | Internet in the Room | 1 h | Phone hotspot for the scanning phones |
| 4 | SYS-01 and SYS-02 sales and payouts | 4 h (vendor-hosted) | Postpone the on-sale; pause walk-up sales |
| 5 | SYS-04 email and files | 24 h | Phone agents; copies of contracts in cloud storage |
| 6 | SYS-03 and SYS-05 website, email marketing, social | 24 h | Ticketing platform event pages; the owner's personal social account |
| 7 | SYS-06 accounting | 72 h | Bank and processor portals |
