# Business Impact Analysis: Cris Santos Company | Food and Agriculture | Sole Proprietorship

**Organization:** Cris Santos Company (custom-exempt meat processing shop) | **Tier:** Sole Proprietorship (owner-operator only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-operator, 2026-07-28, with the on-call IT technician | **Adopted:** Owner-operator, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the shop depends on, how long each can be down, and how much data it can lose. It feeds:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order and the cold-chain steps in the incident runbook (P08);
- the contingency section of POL-01 (P06).

No regulation requires a BIA from a custom-exempt shop. It is done because the shop holds other people's meat: a cooler failure is a loss to customers, not only to the business.

## 2. Business description
One owner-operator cuts, cures, smokes, and packages about 180 beef, 260 hogs, and 40 lambs and goats a year for the animals' owners, under the custom exemption (9 CFR 303.1(a)(2)). A separate mobile slaughter operator delivers the carcasses. The shop's systems are a cold-chain monitoring service (SYS-01), a smokehouse controller and app (SYS-02), a shop laptop with the label printer (SYS-03, SYS-04), a consumer email and file account (SYS-05), the owner's phone (SYS-06), a booking form (SYS-07), accounting and payments (SYS-08), the shop Wi-Fi (SYS-09), and a public AI chatbot (SYS-10). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 a year in processing fees, or about $3,500 a week in season. Customers' meat is valued at replacement cost.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (for example, one cooler of customers' beef) | $1,000 to $5,000 | Less than $1,000 |
| Operations | No product can be stored safely or processed | Processing slowed or rescheduled | Administrative delay only |
| Regulatory | Product adulterated, or a custom exemption condition not met (labels, records) | Records incomplete or late | Internal policy deviation |
| Safety | Plausible illness (temperature-abused or wrongly cured product reaches a household) | Product held and checked; safe outcome | None |
| Reputation | Loss of livestock owners or the slaughter operator's referrals | Complaints or online reviews | None outside the shop |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Cold storage of carcasses and customer product | High | 4 h | 1 h | 12 h |
| BP-02 Cutting, grinding, and packaging to the cut sheet | High | 48 h | 24 h | 24 h |
| BP-03 Curing and smoking | High | 48 h | 24 h | 24 h |
| BP-04 Scheduling, customer communication, and pickup | Moderate | 72 h | 24 h | 24 h |
| BP-05 Custom records, invoicing, and payments | Moderate | 120 h | 72 h | 24 h |

**What drives the values.** Product safety and customers' property drive BP-01: a closed walk-in holds temperature for only a few hours without power or a working unit, so the shop has about 4 hours to act. The RTO of 1 hour is not for the SaaS dashboard; it is the time to get *some* form of temperature watch running again, either the alerts or hourly manual readings. BP-03 is High because a wrong cure amount or an altered cook program is the one way a data error becomes a food safety problem (9 CFR 424.21(c), applied through 303.1(b)(1)). BP-05 can wait days, but its records cannot be lost: they must be kept for 2 years after the end of the transaction year (9 CFR 320.3(a)).

**RPOs that are not supported today:**
- BP-03 and BP-05 (24 h): the cook programs, the cure sheet, and the custom records spreadsheet have no backup or version history (P01 R-004).
- BP-01: alerts stop entirely when the gateway loses power or internet. The gateway buffers 12 hours of readings, so the record survives, but **nobody is told in real time** (P01 R-003).

**Single-person dependency (the key finding).** The owner is the only person who cuts, cures, smokes, labels, answers alerts, and holds the passwords. Cold-chain alerts go to one phone. If the owner is ill, injured, asleep through an alert, or without the phone, BP-01 exceeds its 4-hour MTD with nobody aware of it. Actions (P01 R-009 and R-003, due before the 2026-10-15 busy season):
1. Add a second alert contact in SYS-01: a neighboring custom processor, under a written reciprocal agreement that also offers emergency cooler space.
2. Turn on the vendor's "gateway offline" notice and put the gateway and router on a battery backup.
3. Keep a sealed envelope with the SYS-01 recovery codes, the refrigeration contractor's number, and a one-page "cooler emergency" sheet with a trusted family member.
4. Get a quote for a generator transfer switch for the two condensing units (hurricane season, P01 R-010).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| Walk-in cooler and freezer with two condensing units | Product storage; maintained by the refrigeration contractor | BP-01 |
| SYS-01 Cold-chain monitoring (sensors, gateway, vendor SaaS) | Temperature alerts and history | BP-01 |
| SYS-06 Phone | Only alert recipient; kill sheet photos; card reader; customer texts | BP-01, BP-04, BP-05 |
| SYS-09 Shop Wi-Fi and internet | Carries the gateway, smokehouse controller, and laptop traffic | BP-01, BP-02, BP-03 |
| SYS-03 Laptop and SYS-04 scale and label printer | Cut sheets, label templates, cure sheet, synced custom records | BP-02, BP-03, BP-05 |
| SYS-02 Smokehouse controller and app | Cook programs | BP-03 |
| SYS-05 Email and files; SYS-07 booking form | Cut sheets, bookings, custom records spreadsheet | BP-02, BP-04, BP-05 |
| SYS-08 Accounting, banking, card reader | Invoicing and payments | BP-05 |
| People | Owner-operator only; refrigeration contractor on call | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Temperature watch on the walk-ins | 1 h | Hourly dial thermometer readings on the paper log |
| 2 | Power and refrigeration | 4 h | Refrigeration contractor's 24-hour line; emergency cooler space (planned); generator (quote planned) |
| 3 | Owner access: phone and SYS-01 account | 2 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 4 | Internet in the shop | 2 h | Phone hotspot for the laptop; the gateway buffers 12 hours of readings |
| 5 | A clean laptop with label software and templates | 24 h | Preprinted "Not for Sale" labels written by hand |
| 6 | Smokehouse cook programs and cure sheet | 24 h | Panel operation from printed programs; supplier's printed cure chart |
| 7 | Booking form and email | 72 h | Phone calls and texts; paper appointment book |
| 8 | Accounting and custom records spreadsheet | 72 h | Paper receipt book; rebuild from kill sheet photos and cut sheets |
