# Business Impact Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Small

**Organization:** Cris Santos Company, LLC (live event venue operator with ticketing) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the Director of Ticketing, Operations Director, Food and Beverage Manager, and Controller | **Approved:** General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- PCI DSS v4.0.1 Requirement 12.10 (the incident response plan must cover business recovery and continuity) (N71-R04).

## 2. System and business description
The company runs one Florida venue building with two rooms, about 260 shows a year on about 200 event days, and about 400,000 attendees. Ticketing runs on a vendor SaaS platform with the company as merchant of record. Food, beverage, and merchandise sales are card-only through a cloud POS with validated P2PE readers. See `../00_company-facts.md` sections 1 and 3.

**What makes a venue different:** the most time-critical window is not the business day but **the 60 to 90 minutes before doors**, when thousands of people arrive at once. An outage then is a crowd safety problem before it is a revenue problem. The same outage on a dark day costs almost nothing.

## 3. Impact categories and values
Dollar values are scaled to $24.0 million in annual revenue. An average Hall show brings in about $95,000 on the night (tickets sold on the night, food and beverage, merchandise commission).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (a cancelled Hall show with refunds) | $30,000 to $150,000 | Less than $30,000 |
| Operations | A show cannot open doors or must stop | One service (bars, box office, one room) stops | Staff slowed but working |
| Contractual and regulatory | Missed card brand, acquirer, or breach notice duty; breach of an artist agreement | Late settlement or late filing | Internal policy deviation |
| Safety | Crowd pressure at the doors or loss of emergency communications | Reduced monitoring covered by extra staff | None |
| Reputation | Regional media coverage, artist or promoter lost | Patron complaints and social media | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Event entry and access control | High | 1 h | 0.5 h | 0 h |
| BP-02 Venue safety and security operations | High | 4 h | 2 h | 24 h |
| BP-03 Food, beverage, and merchandise sales | High | 2 h | 1 h | 0 h |
| BP-04 Box office sales and phone orders | Moderate | 8 h | 4 h | 1 h |
| BP-05 Online ticket sales and on-sales | High | 12 h | 4 h | 1 h |
| BP-06 Show settlement and artist payments | Moderate | 24 h | 12 h | 24 h |
| BP-07 Production and show operations | Moderate | 1 h | 0.5 h | 24 h |
| BP-08 Marketing and patron communications | Moderate | 24 h | 8 h | 24 h |
| BP-09 Booking, holds, and venue rentals | Low | 72 h | 48 h | 24 h |
| BP-10 Finance, accounts payable, and payroll | Low | 120 h | 72 h | 24 h |

The MTD values for BP-01, BP-03, and BP-07 apply **during an event**. On a dark day the same processes can wait until the next event.

**What drives the values:**
- **Attendee safety** drives BP-01 and BP-02. The manual entry procedure (printed manifests and wristbands) is the real recovery strategy, because no IT recovery is fast enough during doors. It is not written yet (P01 R-034).
- **Revenue in a short window** drives BP-03. Most bar sales happen in about 2 hours per show, and the venue is cashless.
- **Artist agreements** drive BP-05 and BP-06. Many agreements fix the on-sale time and require settlement on show night.
- **An RPO of 0** for BP-01, BP-03, and BP-05 is met by the vendors (the ticketing platform, the POS vendor, and the payment partner keep the transactions), not by company backups.

**Key findings:**
1. The ticketing vendor's stated recovery commitments (RTO 4 hours, RPO 15 minutes in its SOC 2 system description, P09) meet BP-04 and BP-05, but **not BP-01**. BP-01 depends on scanners working offline from a manifest downloaded before doors. That download is not yet a checklist step.
2. Whether the P2PE solution allows offline card acceptance is unknown. The P2PE Instruction Manual governs it. The Food and Beverage Manager must confirm with the POS vendor before relying on it for BP-03.
3. The settlement app's backups (BP-06) sit in the same cloud account as production and have **never been restore-tested**, so the 12-hour RTO is unproven (P01 R-010). The spreadsheet workaround is the realistic recovery path until then.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Ticketing platform (SaaS) | Sales, box office app, scanning manifests, reports | BP-01, BP-04, BP-05, BP-06, BP-08 |
| SYS-02 Payment partner and box office readers | Ticket payments for MID-T | BP-04, BP-05 |
| SYS-03 POS and P2PE readers | Food, beverage, and merchandise sales for MID-F | BP-03, BP-06 |
| SYS-04 Box office PCs | Window sales and phone orders | BP-04 |
| SYS-05 Cloud tenant | Settlement app, patron marketing database, backups | BP-06, BP-08 |
| SYS-06 Identity provider | Sign-in to email, cloud, accounting | BP-06, BP-08, BP-09, BP-10 |
| SYS-08 Venue network and internet | Two ISPs, one firewall, Wi-Fi for scanners | BP-01, BP-02, BP-03, BP-04 |
| SYS-09 Scanners and PCs | 24 scanners; 48 PCs and laptops | BP-01, BP-04, BP-06 |
| SYS-10 CCTV and door access | Monitoring and staff doors | BP-02 |
| SYS-11 Website and email service | Event calendar and patron notices | BP-05, BP-08 |
| SYS-13 Production systems | Standalone consoles | BP-07 |
| People | Door staff and security supervisors (staffing contractors), box office, bar staff, Controller's settlement staff, IT Manager and technician | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual entry procedure for BP-01 | Immediate | Printed manifests and wristbands at every door (to be written and drilled; R-034) |
| 2 | SYS-10 radios, door access, CCTV | 2 h | Extra guards; manual keys |
| 3 | SYS-08 internet and Wi-Fi for scanners and POS | 1 h | Cellular failover (funded, P01); scanners offline mode |
| 4 | SYS-03 POS | 1 h | Vendor support line; offline mode only if the P2PE manual allows |
| 5 | SYS-01 ticketing platform (vendor) | 4 h | Vendor recovery; printed will-call lists |
| 6 | SYS-04 box office PCs and readers | 4 h | Two spare PCs; after the P2PE change, standalone devices need no PC |
| 7 | SYS-06 identity provider and break-glass admin access | 4 h | Two break-glass accounts stored offline (to be created) |
| 8 | SYS-05 settlement app | 12 h | Spreadsheet settlement from ticketing and POS reports |
| 9 | SYS-11 website and email service | 8 h | Ticketing platform buyer emails; social posts |
| 10 | SYS-12 finance and payroll | 72 h | Repeat the prior payroll |
