# Business Impact Analysis: Cris Santos Company | Arts, Entertainment, and Recreation | Micro

**Organization:** Cris Santos Company, LLC (live event venue operator with ticketing; one music club) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Venue Manager (Security and Privacy Lead) with the Owner and General Manager, the Box Office and Ticketing Manager, the Bar Manager, the Bookkeeper, and the MSP account technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner and General Manager, 2026-08-31

**Sources:** process owner interviews 2026-07-13 to 2026-07-17 (EV-044), FY2025 financial statements and show settlement summary (EV-036), ticket sales and attendance reports (EV-007), the Owner's description of settlements and payments (EV-037), suite backup job report (EV-025), MSP service contract (EV-018), and the venue walk-through (EV-040). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the Owner and General Manager.

## 1. Overview and purpose
This BIA lists every business function of the club, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- PCI DSS v4.0.1 Requirement 12.10, which expects the incident response plan to cover business recovery and continuity (N71-R04).

No law sets contingency planning duties for a privately held music club. The drivers are the merchant agreements, artist agreements, attendee safety, and the cost of a cancelled show.

## 2. System and business description
One leased Florida building with one room (650 standing), about 150 shows a year on about 140 event nights, and about 42,000 attendees. Nearly everything runs in vendor SaaS: the ticketing platform (SYS-01) and its payment partner (SYS-02), the bar POS (SYS-03), the productivity suite (SYS-05), the website (SYS-07), and email marketing (SYS-08). On site are 5 office computers, 2 door tablets, and 3 scanners (SYS-04), the venue network (SYS-06), CCTV (SYS-10), and standalone production consoles (SYS-12). An MSP runs the office computers, network, and suite. See `../00_company-facts.md` and the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

**What makes a club different:** the critical window is not the business day but **the hour after doors open**, when several hundred people arrive at once. An outage then is a crowd safety problem before it is a revenue problem. The same outage on a dark night costs almost nothing.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $7,300 per show (tickets, fees, and bar) (EV-036).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about two cancelled shows with refunds) | $3,000 to $15,000 | Less than $3,000 |
| Operations | A show cannot open doors or must stop | One service (bar, door sales, online sales) stops | Staff slowed but working |
| Contractual and regulatory | Missed acquirer, card brand, or breach notice duty; breach of an artist agreement | Late settlement or late filing | Internal policy deviation |
| Safety | Crowd pressure at the door or loss of radios and guard coordination | Reduced monitoring covered by extra guards | None |
| Reputation | Local media coverage, or an agent stops routing artists to the club | Patron complaints and social media | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Event entry and ticket scanning | High | 1 h | 0.5 h | 0 h |
| BP-02 Venue safety and security operations | High | 4 h | 2 h | 24 h |
| BP-03 Bar and merchandise sales | High | 2 h | 1 h | 0 h |
| BP-04 Online ticket sales and on-sales | High | 12 h | 4 h | 1 h |
| BP-05 Door sales, will-call, and phone orders | Moderate | 4 h | 2 h | 1 h |
| BP-06 Show settlement and artist payments | Moderate | 24 h | 12 h | 24 h |
| BP-07 Production and show operations | Moderate | 1 h | 0.5 h | 24 h |
| BP-08 Marketing and patron communications | Moderate | 24 h | 8 h | 24 h |
| BP-09 Booking, holds, and room rentals | Low | 72 h | 48 h | 24 h |
| BP-10 Bookkeeping and payroll | Low | 120 h | 72 h | 24 h |

The values for BP-01, BP-02, BP-03, and BP-07 apply **during an event**. On a dark night the same functions can wait until the next show.

**What drives the values:**
- **Attendee safety** drives BP-01 and BP-02. The real recovery strategy for BP-01 is a manual door list and wristbands, because no IT recovery is fast enough during doors. That procedure is not written yet (P01 R-020).
- **Revenue in a short window** drives BP-03. Most bar sales happen in the 2 hours after doors, and about 85% are by card.
- **Artist agreements** drive BP-04 and BP-06. Many agreements fix the on-sale time and require settlement on show night.
- **An RPO of 0** for BP-01 and BP-03 is met by the vendors (the ticketing platform and the POS vendor keep the transactions), not by company backups.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Ticketing platform (SaaS) | Sales, box office app, scan manifests, reports, demand tools | Vendor replication and backups (SOC 2 system description states RTO 4 h and RPO 15 min; see P09) | BP-01, BP-04, BP-05, BP-06, BP-08 |
| SYS-02 Payment partner and 2 door readers | Ticket card payments for MID-T | Transactions held by the partner | BP-04, BP-05 |
| SYS-03 Bar POS and 4 P2PE readers | Bar and merchandise card payments for MID-F | Transactions held by the POS vendor | BP-03, BP-06 |
| SYS-04 Endpoints | Back-office PC, bar office PC, 3 laptops, 2 door tablets, 3 scanners | No unique data by design, except cached patron exports on 2 laptops | BP-01, BP-05, BP-06, BP-10 |
| SYS-05 Productivity suite and SYS-11 suite backup | Email, settlement workbooks, contracts, holds calendar | Daily SaaS backup, 30 days of versions; **excludes the 2 shared mailboxes and never restore-tested** | BP-06, BP-08, BP-09, BP-10 |
| SYS-06 Venue network and internet | Firewall, one staff Wi-Fi, guest Wi-Fi, one internet line | Firewall configuration backed up by the MSP | BP-01, BP-03, BP-05 |
| SYS-07 Website and SYS-08 email marketing (SaaS) | Event calendar with the checkout widget; patron email | Vendor service resilience | BP-04, BP-08 |
| SYS-10 CCTV | 16 cameras and an on-premises recorder | 21 days on the recorder; no copy | BP-02 |
| SYS-12 Production consoles | Standalone lighting and audio consoles | Show files on USB copies | BP-07 |
| People | Venue Manager, Box Office and Ticketing Manager, Bar Manager, Production Manager, Bookkeeper, Owner; about 20 contractor workers per show | Cross-training: the Venue Manager can run the door and the box office | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Ticketing vendor | BP-01 (manifests), BP-04, BP-05, BP-06 reports | SOC 2 Type 2 report reviewed (P09): RTO 4 h and RPO 15 min meet BP-04 and BP-05, not BP-01 |
| Payment partner | BP-04, BP-05 card payments | PCI DSS AOC requested 2026-08-14; no recovery figures |
| POS vendor | BP-03 | Vendor service commitments (standard terms) |
| MSP | Recovery of the office computers, network, and suite backup | **No written recovery commitment**; the MSP contract has only a 4-business-hour response time |
| Internet provider | BP-01 syncing, BP-03, BP-05, and every SaaS function | None; single line |
| Staffing contractors | BP-01, BP-02, BP-03 people | Contract staffing levels per show |

**Key findings:**
1. **The ticketing vendor meets online sales but not event entry.** Its 4-hour RTO is fine for BP-04 and BP-05. BP-01 cannot wait 4 hours, so it depends on scanners working offline from a manifest downloaded before doors. That download is not yet a checklist step (R-020).
2. **The internet line is a single point of failure on show nights.** It carries the bar POS, the door tablets, and scanner syncing (R-019).
3. **Whether the P2PE solutions allow offline card acceptance is unknown.** The P2PE instruction manuals govern it. The Bar Manager must confirm with the POS vendor before relying on it for BP-03.
4. **Settlement data recovery is unproven.** The settlement workbooks sit in the suite, and the backup has never been restore-tested (R-012). Rebuilding a settlement by hand from vendor reports is the realistic path until a restore test passes.
5. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time (R-015).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual door procedure for BP-01 | Immediate | Printed door list and wristbands at the door (to be written and drilled; R-020) |
| 2 | Radios, guard posts, and CCTV (SYS-10) | 2 h | Extra guards; manual key control |
| 3 | Internet and staff Wi-Fi (SYS-06) | 1 h | Cellular failover router (funded, due 2026-11-30); a staff phone hotspot until then; scanners in offline mode |
| 4 | Bar POS (SYS-03) | 1 h | Vendor support line; cash with a printed price list |
| 5 | Ticketing platform access (SYS-01) | 4 h | Vendor recovery; printed will-call list |
| 6 | Door tablets and readers (SYS-02, SYS-04) | 2 h | Cash at the door; walk-up buyers use the online checkout on their phones |
| 7 | Clean office computers and suite access (SYS-04, SYS-05) | 8 h | MSP reimages; staff use the web versions from a clean laptop |
| 8 | Settlement workbooks (SYS-05, restored from SYS-11) | 12 h | Settlement rebuilt by hand from ticketing and POS reports |
| 9 | Website and email marketing (SYS-07, SYS-08) | 8 h | Ticketing platform buyer emails; social media posts |
| 10 | Finance and payroll (SYS-09) | 72 h | Repeat the prior payroll |
