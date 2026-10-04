# Business Impact Analysis: Cris Santos Company | Utilities | Sole Proprietorship

**Organization:** Cris Santos Company (independent utility engineering consultant) | **Tier:** Sole Proprietorship (owner-engineer only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-engineer, 2026-07-21, with the on-call IT technician (under NDA) | **Adopted:** Owner-engineer, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the consultancy depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the clients' expectations: Client A and Client B both require incident notice within 24 hours (SSA-A (5), VAA-B (5)), so communications must come back within a day.

## 2. Business description
One licensed engineer works from a home office in Florida and visits client substations. There are no employees. A part-time drafting subcontractor updates drawings. All work runs on a business email and file suite (SYS-01), one engineering laptop (SYS-02), a personal phone (SYS-03), USB drives (SYS-05), an accounting SaaS (SYS-04), and named accounts on two client-operated systems (SYS-06). Clients are four small utilities and an engineering firm. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $3,500 a week.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (about three weeks of receipts, or loss of a client) | $2,000 to $10,000 | Less than $2,000 |
| Operations | A client's substation work or event analysis stops | Study or settings deadlines slip | Administrative delay only |
| Regulatory and contract | Missed contractual incident notice or exposure of a client's BCSI or CEII | Late deliverable under a contract | Internal policy deviation |
| Safety | A wrong or late relay setting could lead to a misoperation on a client's system | Delayed but safe work | None |
| Reputation | A client ends the contract or warns other utilities | Client complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Field support: commissioning and event analysis | High | 24 h | 8 h | 24 h |
| BP-02 Client communications and incident notices | High | 24 h | 8 h | 24 h |
| BP-03 Protection and control engineering | Moderate | 72 h | 24 h | 24 h |
| BP-04 Planning and interconnection studies | Moderate | 120 h | 72 h | 24 h |
| BP-05 Billing and business administration | Low | 168 h | 72 h | 24 h |

**What drives the values:** client operations drive BP-01, because Client B waits on the event analysis before it returns a line or feeder to normal. Contract notice duties drive BP-02: an incident at the consultant must reach Client A and Client B within 24 hours, so email and the phone must work within a day. Project deadlines drive BP-03 and BP-04. The 24-hour RPO for BP-03 is **not supported today**: the local settings databases and software license files on the laptop have no backup (P01 R-011).

**Single-person dependency (the key finding).** The owner-engineer is the only engineer, the only person who seals work, the only person Client A has authorized to see its BCSI, and the only holder of every password and second factor. The SMS codes and the Client B MFA push go to one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-02 exceed their MTD at once, and nobody can tell the clients. A backup engineer cannot simply step in: Client A must authorize any person by name before that person sees Client A BCSI (SSA-A (2)). Actions (P01 R-010, due 2026-12-31):
1. Sign a standby arrangement with another independent engineer for Client B and Client C urgent work, with an NDA. Ask Client A to pre-authorize that engineer, or record that Client A work waits.
2. Keep the recovery codes for the email suite and accounting SaaS and a one-page emergency sheet (client contacts, insurer hotline) in a sealed envelope held by the owner's attorney.
3. Give each client a second contact (the attorney) who will tell them if the owner is unavailable.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Mobile phone | SMS codes, Client B MFA push, client calls | BP-01, BP-02 |
| SYS-02 Engineering laptop | Settings software, studies, CEII archive, Client B gateway client | BP-01, BP-03, BP-04 |
| SYS-01 Email and file suite | Client correspondence and project files | BP-02, BP-03, BP-05 |
| SYS-06 Client A portal and Client B gateway | Client-operated; named accounts | BP-01, BP-02, BP-03 |
| SYS-05 USB drives | Carry settings files to sites | BP-01 |
| SYS-07 Home network | Internet for the home office; phone hotspot is the fallback | All |
| SYS-04 Accounting SaaS | Invoices and books | BP-05 |
| Third parties | Relay manufacturers' and analysis software vendors (licenses), drafting subcontractor, insurer, tax accountant | BP-03, BP-04, BP-05 |
| People | Owner-engineer only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and second factors | 2 h | Recovery codes in the sealed envelope; replacement phone and SIM from the carrier |
| 2 | Client contact by phone and email (BP-02) | 4 h | Phone calls; client portals from the phone; printed contact sheet |
| 3 | A clean device for client work | 8 h | Spare clean laptop (planned, P01 R-002); laptop reinstalled by the IT technician |
| 4 | Engineering software licenses and settings databases | 24 h | Reinstall from vendor portals; settings from the last files delivered to the clients |
| 5 | Project files (BP-03, BP-04) | 24 h | File suite version history (30 days) |
| 6 | Accounting SaaS (BP-05) | 72 h | Invoice templates by email |
