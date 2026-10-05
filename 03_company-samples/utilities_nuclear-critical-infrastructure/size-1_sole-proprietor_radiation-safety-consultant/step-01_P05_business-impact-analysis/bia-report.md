# Business Impact Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

**Organization:** Cris Santos Company (independent radiation safety consultant) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-consultant, 2026-07-21, with the on-call IT technician (under NDA since 2026-07-14) | **Adopted:** Owner-consultant, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the consultancy depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the notice clocks the two main clients set by contract (Client A 8 hours under CSR-A (5); Client B 24 hours under CSIA-B (4)), which make communications a time-critical function even though no regulation sets a recovery time for this business.

## 2. Business description
One health physicist works from a home office in Florida and on client sites. About 55% of receipts come from radiation protection support at Client A, a two-unit nuclear power plant, mostly during refueling outages. Client B, a hospital with a category 2 cesium-137 blood irradiator, buys the annual radiation protection program review and support for its Part 37 security program review. The rest is shielding and survey work. Everything runs on a business email and file suite, a main laptop, a phone, an older field laptop for survey meter data, an accounting SaaS, and the clients' own portals. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, about $3,500 a week, and about $1,500 a day while on site at Client A.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (lost outage days or a lost client) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Cannot support an outage or deliver surveys | Deliverables late by days | Administrative delay only |
| Regulatory and contractual | Client A access suspended, a contract notice missed, or a client finding traced to the consultant's work | Late deliverable that a client must explain to its regulator | Internal deviation only |
| Safety | Wrong or missing survey or dose data could expose workers to unplanned dose | Survey repeated or work delayed, no exposure | None |
| Reputation | Loss of Client A or Client B (a small industry where references matter) | Client complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Outage and field radiation protection support | High | 24 h | 12 h | 4 h |
| BP-02 Analysis and report production | High | 72 h | 48 h | 24 h |
| BP-03 Client communications and secure document exchange | Moderate | 24 h | 8 h | 24 h |
| BP-04 Instrument management and survey data | Moderate | 72 h | 48 h | 24 h |
| BP-05 Billing and administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** BP-01 is set by Client A's outage schedule. A contractor who misses more than a day is replaced, and survey or dose errors can affect workers. BP-03 has a short MTD only because the two client contracts set 8-hour and 24-hour notice clocks; if email is down the phone is the fallback. BP-02 is measured in days because client reports are due in weeks. The 24-hour RPO for BP-04 is **not supported today**: raw survey data on the field laptop has no backup (P01 R-006).

**Single-person dependency (the key finding).** The owner is the only health physicist, the only person who signs reports, the only person on Client B's information access list, and the only holder of every credential. The email second factor and the Client A portal authenticator are both on the owner's one phone. If the owner is ill, injured, or without the phone during an outage, BP-01 and BP-03 pass their MTD at once. Client A can cover outage work with its own staff, so the plant is not at risk, but the business would miss its contract notice clocks and could lose the client. Actions (P01 R-010, due 2026-12-31):
1. Agree in writing with a qualified peer health physicist (a sole proprietor who already holds Client A access) to cover urgent outage work, with Client A's consent under CSR-A (10).
2. Keep email and accounting recovery codes and a one-page contact sheet in a sealed envelope held by the owner's attorney. The sheet tells the attorney to notify Client A and Client B, not to open client files.
3. Give the per-diem technician a short script: whom to call at Client A if the owner cannot report for a shift.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Email and file suite | Correspondence, project folders, report drafts; 30-day version history | BP-02, BP-03, BP-05 |
| SYS-02 Main laptop | Calculations and reports; encrypted | BP-02 |
| SYS-03 Mobile phone | Calls and texts on site; email MFA codes; Client A portal authenticator | BP-01, BP-03 |
| SYS-04 Field laptop and survey instruments | Survey meter data download; six instruments | BP-01, BP-04 |
| SYS-05 Accounting SaaS | Invoices, receivables, W-9 copy | BP-05 |
| SYS-06 Client A portal and Client B share | Work packages, survey maps, dose reports; Client B security information | BP-01, BP-02, BP-03 |
| SYS-07 Home network | Internet for the home office; phone hotspot is the fallback | BP-02, BP-03 |
| SYS-08 Calibration-tracking SaaS | Calibration due dates and certificates | BP-04 |
| People | Owner-consultant; per-diem technician for surveys at Client A only | BP-01 |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone, email second factor, Client A authenticator | 2 h | Recovery codes in the sealed envelope; replacement phone from the carrier; Client A contractor coordinator resets the portal authenticator after identity check |
| 2 | Communications with Client A and Client B | 4 h | Phone calls; printed contact list (P08) |
| 3 | A clean device for client portals | 8 h | Phone browser for short tasks; main laptop reinstalled by the IT technician |
| 4 | Field data path (field laptop, instruments) | 12 h during an outage | Client A workstations and client-owned instruments on site; paper field notebook |
| 5 | SYS-01 Email and file suite | 24 h (vendor-hosted) | Client portals; working copies restored from version history |
| 6 | SYS-08 Calibration-tracking SaaS | 48 h | Calibration certificates in email; instrument labels |
| 7 | SYS-05 Accounting SaaS | 72 h | Invoice template in the email suite |
