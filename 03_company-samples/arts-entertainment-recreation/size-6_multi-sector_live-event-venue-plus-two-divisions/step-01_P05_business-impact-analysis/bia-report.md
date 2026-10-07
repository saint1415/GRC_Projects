# Business Impact Analysis: Cris Santos Company Holdings | Arts, Entertainment, and Recreation | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the patron data platform, finance, HR).
- **Division BIAs:** Live Venues (focus), Hotels and Restaurants, and Ticketing and Streaming Technology. They are rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- PCI DSS v4.0.1 Requirement 12.10, which expects the incident response plan to cover business recovery and continuity, for all three PCI roles in the group (N71-R04, N72-R01);
- the Availability commitments in the ticketing platform's SOC 2 report and the 99.95% monthly availability term in the 2024 client agreement (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and the wide-area network, and SYS-G4 the patron data platform. Division systems are SYS-D1 (venue operations estate), SYS-D2 (hotel systems, with a vendor-hosted PMS), SYS-D3 (the ticketing platform in provider A, disaster recovery in provider B), and SYS-D4 (streaming, in provider B). See `../00_company-facts.md` sections 1, 3, and 7.

**What makes this group different:** the most time-critical window is not the business day. It is **the 60 to 90 minutes before doors** at a venue, and **the first minutes of a high-demand on-sale** on the ticketing platform. A platform outage at 10:00 on an on-sale morning hits the group's venues, its hotel packages, and 1,150 client venues at once.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Live Venues about $25.8 million per day on average (much higher on event weekends), Hotels and Restaurants about $16.7 million per day, and Ticketing and Streaming about $6.8 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (admit and serve patrons, host guests, sell tickets for all tenants) | One venue, hotel, or service line stops | Staff slowed but working |
| Contractual and regulatory | Missed card brand, client, or breach notice duty; SEC disclosure; breach of the client availability commitment | Missed internal or single-client deadline | Internal policy deviation |
| Safety | Crowd pressure at doors, loss of emergency communications, or guests unable to reach rooms at night | Reduced monitoring covered by extra staff | None |
| Reputation | National media, loss of ticketing clients, artist or promoter lost | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 8 Live Venues, 5 Hotels and Restaurants, and 7 Ticketing and Streaming. 14 are High, 12 Moderate, and 1 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 1 h | 1 h |
| BP-G04 Wide-area network and venue and hotel connectivity | Group | High | 4 h | 1 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-TS02 Payment orchestration and token vault | Ticketing and Streaming | High | 2 h | 1 h | 0.25 h |
| BP-TS01 Online ticket sales and hosted checkout | Ticketing and Streaming | High | 2 h | 1 h | 0.25 h |
| BP-TS03 Mobile ticket delivery and access control service | Ticketing and Streaming | High | 2 h | 1 h | 1 h |
| BP-LV01 Event entry and access control | Live Venues | High | 1 h | 0.5 h | 0.25 h |
| BP-LV04 Crowd safety, CCTV, and venue security systems | Live Venues | High | 2 h | 1 h | 24 h |
| BP-LV02 Box office and on-site ticket sales | Live Venues | High | 4 h | 2 h | 1 h |
| BP-LV03 Food, beverage, and merchandise sales | Live Venues | High | 4 h | 2 h | 1 h |
| BP-HO01 Front desk check-in, check-out, and room keys | Hotels and Restaurants | High | 4 h | 2 h | 1 h |
| BP-HO02 Reservations and central call center | Hotels and Restaurants | High | 8 h | 4 h | 1 h |
| BP-LV05 Event setup, pricing, and on-sale management | Live Venues | High | 8 h | 4 h | 1 h |
| BP-TS05 Live-concert streaming | Ticketing and Streaming | Moderate | 4 h | 1 h | 24 h |
| BP-LV08 Production and broadcast networks | Live Venues | Moderate | 4 h | 1 h | 24 h |
| BP-HO03 Restaurant and bar sales | Hotels and Restaurants | Moderate | 8 h | 4 h | 4 h |
| BP-LV07 Acquired theater ticketing and POS (legacy) | Live Venues | Moderate | 8 h | 4 h | 4 h |
| BP-HO05 Event-and-stay packages | Hotels and Restaurants | Moderate | 24 h | 8 h | 4 h |
| BP-TS06 Dynamic pricing and bot detection modules | Ticketing and Streaming | Moderate | 24 h | 8 h | 4 h |
| BP-TS04 Client support and incident notices | Ticketing and Streaming | Moderate | 24 h | 8 h | 4 h |
| BP-G05 Patron data platform marketing and analytics | Group | Moderate | 72 h | 24 h | 24 h |
| BP-LV06 Show settlement and promoter payments | Live Venues | Moderate | 72 h | 24 h | 4 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-TS07 Platform release pipeline | Ticketing and Streaming | Moderate | 72 h | 24 h | 4 h |
| BP-HO04 Guest Wi-Fi and in-room services | Hotels and Restaurants | Low | 24 h | 12 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |

**What drives the values:**
- **Crowd safety** drives event entry (BP-LV01) and venue security systems (BP-LV04). A queue of 20,000 people at an amphitheater is a safety problem within the hour, which is why scanners must work offline from manifests downloaded before doors.
- **On-sale economics and client commitments** drive the ticketing platform (BP-TS01, BP-TS02). Demand that cannot buy in the first hour moves to resale markets, and the 2024 client agreement commits 99.95% monthly availability.
- **Order integrity** drives the 15-minute RPO for checkout and payments. Seats sold but not recorded would be sold twice; authorizations without orders become refunds and chargebacks.
- **Revenue more than time** drives settlement, close, and the patron data platform (BP-LV06, BP-G07, BP-G05). These can wait days.
- **The pricing and bot modules are not needed to sell** (BP-TS06). On-sales can run on fixed prices. But a high-demand on-sale without bot protection is postponed, which is why the module is Moderate rather than Low.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process except the hotel PMS and the acquired theaters | A group identity outage stops ticketing administration, box offices, and the SOC console at once. Break-glass accounts per critical system are the fallback |
| Ticketing platform (BP-TS01 to BP-TS03) | Ticketing and Streaming | Live Venues sales and entry; hotel packages; streaming purchases; 1,150 clients | The group's largest single point of failure. Disaster recovery in provider B was failed over successfully in tests on 2026-02-11 and 2026-06-09 |
| Payment orchestration (BP-TS02) | Ticketing and Streaming | Live Venues, Hotels packages, streaming | Three merchant roles in the group depend on one service provider inside the group |
| WAN and cellular failover (BP-G04) | Group | All venues and hotels | Scanners and P2PE devices tolerate short outages only |
| SOC facts (BP-G02) | Group | Every notice in P08 | Card brand, client, state, and SEC clocks depend on the SOC establishing what happened |
| Broadcast feed (BP-LV08) | Live Venues | Streaming (BP-TS05) | A venue production outage ends a pay-per-view stream |
| PMS (SYS-D2) to patron data platform | Hotels and Restaurants | Group marketing (BP-G05) | Nightly export; carries identity document numbers no use case needs (P03, gap 3) |
| Client notices (BP-TS04) | Ticketing and Streaming | 1,150 client merchants | 24-hour notice for 186 clients; 72 hours for the rest |

**Single points of failure found:** the ticketing platform (mitigated by the provider B disaster recovery region, tested twice in 2026); SYS-G1 (break-glass accounts, tested quarterly); one P2PE solution provider for all integrated venues (accepted; contract has a 4-hour restoration term); the acquired theaters' legacy ticketing vendor (no group fallback beyond manual event setup on the TVOP, P01 LV-005).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-D3 ticketing platform | BP-TS01 to BP-TS03, BP-LV01, BP-LV02, BP-LV05, BP-HO05 | Synchronous database replicas in two provider A regions; asynchronous replica in provider B (lag target under 15 minutes) |
| Token vault and HSMs | BP-TS02 | HSM clusters in two regions; key ceremonies documented; vault replicated in provider B |
| SYS-D1 scanners and P2PE devices | BP-LV01 to BP-LV03 | Offline manifests; P2PE store-and-forward within the solution's limits |
| SYS-D2 PMS (vendor-hosted) | BP-HO01, BP-HO02 | Vendor replication (RPO 15 minutes per contract); local night-audit reports at each hotel |
| SYS-D4 streaming | BP-TS05 | Stateless delivery; subscriber database replicas in provider B |
| SYS-G4 patron data platform | BP-G05 | Daily immutable backups |
| People | All | Cross-trained box office and support teams; remote work for the hotel call center |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. WAN and venue and hotel connectivity
4. SOC visibility (SIEM and EDR)
5. to 7. Ticketing platform core: payment orchestration and token vault, hosted checkout, mobile tickets and access control
8. to 11. Live Venues event-day processes: entry, crowd safety systems, box office, food and beverage
12. and 13. Hotel front desk and reservations
14. to 27. On-sale management, streaming, production networks, restaurants, acquired theaters, packages, pricing and bot modules, client support, the patron data platform, settlement, financial close, release pipeline, guest Wi-Fi, and payroll.

## 8. Key findings
1. **The ticketing platform is the group's critical shared dependency**, more than any corporate service. Its RTO of 1 hour is supported by two tested failovers in 2026, but every division and 1,150 clients depend on it, so its confidentiality failures (P08) and its availability failures land on everyone.
2. **Event entry has the shortest MTD in the group (1 hour)** and survives a platform outage only because scanners work offline. Offline mode was last tested at 4 of 30 integrated venues (P01 LV-012).
3. **The acquired theaters are outside the recovery design.** They do not use SYS-G1, the WAN, or group backups, so their RTO of 4 hours depends on a vendor the group does not monitor (gap 2).
4. **Notification capacity is itself a process** (BP-TS04, BP-G02, BP-G07). If the SOC or client support is down during an incident, the 24-hour client clocks and the Visa 3-day clock keep running. The P08 runbook uses out-of-band channels for this reason.
