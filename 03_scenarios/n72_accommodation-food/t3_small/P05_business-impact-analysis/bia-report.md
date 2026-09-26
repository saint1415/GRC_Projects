# Business Impact Analysis: Cris Santos Company | Accommodation and Food Services | Small

**Organization:** Cris Santos Company, LLC (independent 140-room beachfront hotel) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the Front Office Manager, Controller, Chief Engineer, and Food and Beverage Director | **Approved:** General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the hotel depends on, how long each can be down, and how much data it can lose. It supports:
- the incident response plan that PCI DSS v4.0.1 Requirement 12.10.1 expects to include business recovery and continuity procedures;
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the IT section to be added to the hotel's hurricane plan (P01 R-015).

## 2. System and business description
One independent full-service hotel on the Florida Gulf Coast: 140 rooms, about 45 arrivals and 45 departures a day, a restaurant, two bars, and meeting space. Work runs on the Property Management and Point-of-Sale Platform (PMPS): a SaaS PMS, a payment gateway with front desk terminals, a restaurant POS with P2PE devices, an on-premises door lock system, the staff network and endpoints, an identity provider, and a cloud tenant. See `../scenario-facts.md` sections 3 and 4.

## 3. Impact categories and values
Dollar values are scaled to $24.0 million in annual revenue, about $66,000 per day (about $48,000 rooms and $14,500 food and beverage).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $130,000 (about 2 days of revenue) | $30,000 to $130,000 | Less than $30,000 |
| Operations | Guests cannot check in or enter rooms | One outlet or one channel stops | Staff slowed but working |
| Regulatory | Card compromise notice to the acquirer and brands, or reportable breach | Missed contractual or record-keeping duty (for example, the Fla. Stat. 509.101(2) guest register) | Internal policy deviation |
| Safety | Guests cannot secure or reach their rooms, or cannot be accounted for during an evacuation | Delayed service with a safe workaround | None |
| Reputation | Regional media, online review wave, or loss of online travel agency ranking | Individual complaints and reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Guest arrival and check-in | High | 4 h | 2 h | 1 h |
| BP-02 Room access and key management | High | 2 h | 1 h | 24 h |
| BP-03 Guest payments and folio settlement | High | 8 h | 4 h | 1 h |
| BP-04 Reservations and distribution | High | 8 h | 4 h | 1 h |
| BP-05 Restaurant and bar service and payments | Moderate | 8 h | 4 h | 4 h |
| BP-06 Night audit, accounting and card settlement | Moderate | 24 h | 12 h | 24 h |
| BP-07 Guest communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Sales and events | Low | 72 h | 48 h | 24 h |
| BP-09 Revenue management and rate publishing | Low | 72 h | 48 h | 24 h |
| BP-10 Payroll, timekeeping and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Guest safety drives BP-02.** Existing key cards keep working when the lock server is down, but new arrivals cannot get keys and lost cards cannot be cancelled. Two hours is the longest the hotel can rely on escorted entry with mechanical override keys.
- **The arrival window drives BP-01.** Most arrivals come between 15:00 and 22:00. A four-hour outage in that window creates a lobby queue of 30 or more parties.
- **Overbooking drives BP-04's 1-hour RPO.** A lost hour of reservations can put two parties in one room, because online travel agencies keep selling from the last inventory they received.
- **BP-09 is Low.** The AI pricing system can be switched off for days; the Revenue Manager can set rates by hand. This also means turning it off is a safe response to a pricing problem (P10).

**Key finding:** the PMS vendor's contract has no recovery time or recovery point commitment. Its SOC 2 report states an RTO of 4 hours and an RPO of 15 minutes (P09 `vendor-soc2-review.csv`). That meets the 4-hour RTO for BP-03 and BP-04 but **not the 2-hour RTO for BP-01**, so paper arrival procedures and emergency key cards are required (P01 R-014). The lock server has no tested backup or rebuild procedure, so its 1-hour RTO is unproven (P01 R-015, R-017).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 PMS (SaaS) | Reservations, profiles, folios, card vault, interfaces | BP-01, BP-03, BP-04, BP-06, BP-08 |
| SYS-02 Payment gateway and front desk terminals | Card authorizations and settlement for MID-1 | BP-01, BP-03, BP-06 |
| SYS-03 Booking engine; SYS-04 Channel manager | Direct and online travel agency bookings | BP-04 |
| SYS-05 Restaurant POS and P2PE devices | Orders, payments, room charges | BP-05, BP-06 |
| SYS-06 Staff network and internet | Firewall, switches, single internet provider | All |
| SYS-07 Endpoints | 6 front desk PCs, 2 reservations PCs, back office PCs | BP-01, BP-03, BP-04, BP-06 |
| SYS-08 Door lock system | Lock server, 3 encoders, 160 locks | BP-01, BP-02 |
| SYS-09 Identity provider | Sign-in and MFA | All cloud systems |
| SYS-10 Cloud tenant | Reporting database, guest-marketing hub, chatbot integration, backups | BP-06, BP-07, BP-09 |
| SYS-11 Productivity suite | Email and files | BP-07, BP-08 |
| People and facilities | Front desk, night auditor, engineering, server room (ground floor) | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 Internet and staff network | 1 h | Cellular failover router (to be purchased; P01 R-016) |
| 2 | SYS-08 Door lock server and encoders | 1 h | Emergency key cards; mechanical override keys with an entry log |
| 3 | SYS-09 Identity provider and administrator access | 1 h | Two sealed break-glass accounts (to be created) |
| 4 | SYS-07 Front desk PCs | 2 h | 2 pre-imaged spare laptops in the Front Office Manager's safe |
| 5 | SYS-01 PMS access | 2 h (vendor states 4 h) | Printed arrivals and in-house lists from night audit |
| 6 | SYS-02 Front desk terminals and gateway | 4 h | Gateway portal for later authorization; no paper card numbers |
| 7 | SYS-03 and SYS-04 distribution | 4 h | Stop-sell through vendor portals |
| 8 | SYS-05 Restaurant POS | 4 h | Paper checks; P2PE offline mode |
| 9 | SYS-11 Email; SYS-13 chatbot | 8 h | Phones; website notice |
| 10 | SYS-10 Cloud tenant workloads; SYS-12 pricing | 48 h | Manual rates and reports |
| 11 | SYS-14 Payroll and timekeeping | 72 h | Paper time sheets |
