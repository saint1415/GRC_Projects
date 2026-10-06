# Business Impact Analysis: Cris Santos Company | Other Services (except Public Administration) | Sole Proprietorship

**Organization:** Cris Santos Company (electronics and device repair service) | **Tier:** Sole Proprietorship (owner-technician only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-technician, 2026-07-20, with the independent security consultant | **Adopted:** Owner-technician, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the shop depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the CSF 2.0 outcomes GV.OC-04 (critical services understood) and ID.AM-05 (assets prioritized), checked in P03.

No law requires a BIA for a repair shop. It is done because one person runs everything, and a short outage of the wrong system stops all revenue.

## 2. Business description
One owner-technician runs a storefront repair shop in a Florida strip plaza, open Tuesday to Saturday. The shop handles about 6 repair tickets a day, plus data transfers, small data recovery jobs, and a free recycling drop-off. About 25 customer devices are in the shop at any time. The ticketing and POS platform (SYS-01) is vendor SaaS and is the system of record. Card payments go only through a P2PE terminal (SYS-02). Customer device data from transfers and recoveries sits on the bench PC and two external drives (SYS-06). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $720 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of revenue) | $700 to $3,500 | Less than $700 |
| Operations | No device can be released or repaired | Repairs slowed or partly rescheduled | Administrative delay only |
| Regulatory | Notifiable breach under Fla. Stat. 501.171, or loss of SAQ P2PE eligibility | Missed contract term (merchant agreement) | Internal policy deviation |
| Safety | Plausible injury (for example a swollen battery left half repaired) | Delayed but safe repair | None |
| Reputation | Public review or news story about customer data misuse | Individual complaints | None outside the shop |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Payment and device release | High | 24 h | 8 h | 1 h |
| BP-02 Diagnostics and repair | High | 24 h | 8 h | 24 h |
| BP-03 Device intake and check-in | Moderate | 48 h | 8 h | 24 h |
| BP-04 Data transfer and data recovery | Moderate | 72 h | 48 h | 0 h (open jobs) |
| BP-05 Customer communications and booking | Moderate | 48 h | 24 h | 24 h |

**What drives the values:** revenue drives BP-01, because nearly every dollar is collected when a device is released. BP-02 is High because customers are promised same-day or next-day work, and a half-finished battery repair is a safety risk. The 1-hour RPO for BP-01 depends on the ticketing vendor's backups (stated in its SOC 2 report, P09). **BP-04 has an RPO of zero while a job is open**: a recovered copy from a failing drive may be the only copy, and the bench PC and drives have no backup today. Once a job is delivered, the right answer is the opposite: the copy should be deleted (P01 R-002, POL-01 section 8).

**Single-person dependency (the key finding).** The owner-technician is the only technician, the only person at the counter, and the only holder of the SYS-01, email, bank, and processor credentials. The fill-in technician covers about 12 days a year, but only by using the owner's own login. If the owner is suddenly unavailable, about 25 customer devices are locked in the shop and nobody can legally and safely release them. Actions (P01 R-010, due 2026-12-31):
1. Give the fill-in technician a named SYS-01 account with limited rights and MFA, and a written agreement with confidentiality terms (also closes P01 R-001 and R-004 items).
2. Keep a one-page emergency access sheet and the recovery codes for SYS-01, email, and the processor portal in a sealed envelope held by the owner's designated emergency contact.
3. Write a device-return procedure: the fill-in technician releases devices against the paper intake tag, the SYS-01 ticket, and photo ID, and logs each release.
4. Print the list of devices in custody every Saturday evening and keep it in the locked cabinet.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Ticketing and POS (vendor SaaS) | Tickets, customer records, invoices, status texts; vendor backups | BP-01, BP-02, BP-03, BP-05 |
| SYS-02 P2PE terminal and processor | Card payments | BP-01 |
| SYS-07 Counter tablet | Intake, signatures, checkout | BP-01, BP-03 |
| SYS-06 Bench PC and transfer drives | Diagnostics, transfers, recoveries (no backup today) | BP-02, BP-04 |
| SYS-08 Owner phone | Business calls and texts, MFA codes, intake photos | BP-02, BP-03, BP-05 |
| SYS-09 Shop network and internet | Everything above; terminal falls back to cellular | All |
| SYS-03 and SYS-11 | Email, booking requests, website | BP-05 |
| Contracted help | Fill-in technician (no agreement yet); payment processor; parts suppliers | BP-01, BP-02 |
| People | Owner-technician only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA codes | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the shop | 1 h | Phone hotspot; the terminal falls back to cellular |
| 3 | SYS-02 card terminal | 4 h | Cash or check; processor sends a replacement terminal |
| 4 | SYS-01 ticketing and POS | 8 h (vendor-hosted) | Paper intake forms, paper tags, and the printed custody list |
| 5 | SYS-07 counter tablet | 8 h | Owner laptop in a browser |
| 6 | SYS-06 bench PC | 48 h | Stand-alone diagnostic tools; reschedule transfer and recovery jobs |
| 7 | SYS-03, SYS-11 email, booking, website | 24 h | Phone calls from the day list |
