# Business Impact Analysis: Cris Santos Company Holdings | Accommodation and Food Services | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the Hotels, Attractions, and Vacation Ownership continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and network (SYS-G3), group payment services (SYS-G4), the guest identity and loyalty platform (SYS-G5), finance, and HR.
- **Division BIAs:** Hotels (focus), Attractions and Entertainment, and Resort Real Estate and Vacation Ownership. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It feeds:
- the group crisis plan and each division's continuity plans (hotel downtime procedures, park operations plans, owner services contingency plans);
- the incident response plan that PCI DSS Requirement 12.10.1 expects to include business recovery and continuity procedures (N72-R01);
- the availability commitments in the two SOC 2 service lines (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 payment services, SYS-G5 guest identity and loyalty, and SYS-G6 ERP and HR. Division systems are:
- **Hotels:** the cloud PMS tenant (SYS-H1), the CRS and contact center (SYS-H2), the POS estate (SYS-H3), property networks and door locks (SYS-H4), and revenue management and the chatbot (SYS-H5).
- **Attractions:** ticketing and gate access (SYS-A1), park POS (SYS-A2), the park app (SYS-A3), and ride and show control (SYS-A4).
- **Vacation Ownership:** sales (SYS-V1), loan origination and servicing (SYS-V2), owner services and association management (SYS-V3), and inventory forecasting (SYS-V4).

The SSP system (P02) is the Hotels division's Property Management and Point-of-Sale Platform (PMPS), which covers BP-H01, BP-H03, and the payment side of BP-H02. See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Hotels about $20 million per day, Attractions about $15 million per day (much higher on peak days), and Vacation Ownership about $14 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 1 day of a division's revenue | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot deliver its core service (rooms, park admission, owner stays) | One property, park, or channel stops | Staff slowed but working |
| Regulatory and contractual | Card brand compromise event, reportable breach, missed FTC or state deadline, or SEC disclosure | Missed internal, owner, or association deadline | Internal policy deviation |
| Safety | Plausible harm to guests, visitors, or riders (ride control failure, rooms not secured, crowd crush at gates) | Delayed but safe service | None |
| Reputation | National media, card brand action, or regulator attention | Regional media or owner complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 28 processes: 8 group shared services, 8 Hotels, 6 Attractions, and 6 Vacation Ownership. 15 are High, 11 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G05 Group payment services | Group | High | 2 h | 1 h | 1 h |
| BP-A01 Park admission and gate access | Attractions | High | 2 h | 1 h | 1 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, hubs, colocation | Group | High | 4 h | 2 h | 1 h |
| BP-G04 SD-WAN and property connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-A04 Ride and show control | Attractions | High | 4 h | 2 h | 1 h |
| BP-H04 Guest room access (door locks) | Hotels | High | 4 h | 2 h | 1 h |
| BP-H02 Central reservations and distribution | Hotels | High | 4 h | 2 h | 1 h |
| BP-A03 Park POS | Attractions | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-H01 Front desk and guest folios (PMS) | Hotels | High | 8 h | 4 h | 1 h |
| BP-H03 Hotel food and beverage POS | Hotels | High | 8 h | 4 h | 1 h |
| BP-A02 Online ticket and pass sales | Attractions | High | 8 h | 4 h | 1 h |
| BP-V01 Owner reservations and points | Vacation Ownership | High | 24 h | 8 h | 4 h |
| BP-V04 Loan servicing and payment processing | Vacation Ownership | High | 72 h | 24 h | 4 h |
| BP-H05 Reservations contact center | Hotels | Moderate | 24 h | 8 h | 4 h |
| BP-G06 Guest identity, loyalty, profile hub | Group | Moderate | 24 h | 8 h | 4 h |
| BP-A05 Park mobile app | Attractions | Moderate | 24 h | 8 h | 4 h |
| BP-V02 Sales tours and contracting | Vacation Ownership | Moderate | 48 h | 24 h | 4 h |
| BP-V03 Loan origination and credit decisions | Vacation Ownership | Moderate | 48 h | 24 h | 4 h |
| BP-H07 Managed hotel owner reporting and notices | Hotels | Moderate | 72 h | 24 h | 24 h |
| BP-H06 Revenue management and rate distribution | Hotels | Moderate | 72 h | 24 h | 24 h |
| BP-V06 Rental program and inventory forecasting | Vacation Ownership | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-V05 Association management and fee billing | Vacation Ownership | Moderate | 120 h | 72 h | 24 h |
| BP-G08 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-H08 Group sales and events | Hotels | Low | 120 h | 72 h | 24 h |
| BP-A06 Kids' club and park marketing | Attractions | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Gates and payments open every day.** Parks cannot admit visitors without ticket validation (BP-A01), and every division's online sales stop without group payment services (BP-G05). Both have a 2-hour MTD; their fallbacks (offline gate scanners, P2PE terminals authorizing directly) cover only a few hours.
- **Safety drives ride control and door locks.** A ride with a suspect control system stays closed until engineers verify it (BP-A04). Door locks keep working offline, but new keys cannot be encoded safely without the lock server (BP-H04).
- **Hotels run 24 hours.** Front desks can work from printed downtime reports for about 8 hours before arrivals, folios, and night audit become unmanageable (BP-H01).
- **Vacation Ownership runs on longer cycles.** Owner stays are booked weeks ahead, loan payments run in ACH cycles, and association billing is annual, so its MTDs are 24 to 120 hours. Its High rating comes from owners arriving at resorts (BP-V01) and the payment cycle with customer information under the FTC Safeguards Rule (BP-V04).
- **The guest profile hub is Moderate for availability but High for confidentiality.** Hotels and parks keep operating without loyalty recognition (BP-G06), but the hub holds 52 million profiles and owners' bank data (gap 2), so its protection cannot wait (P02, P01 GR-02).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Hotels, Attractions, corporate | A group identity outage stops two divisions at once. Vacation Ownership is outside SYS-G1 until 2027-03-31, which spares it in an outage but leaves it without group MFA and PAM (gap 3) |
| Group payment services (SYS-G4) | Group | All three divisions | One CDE account serves the CRS, ticket store, park app, and owner portal; all three PCI DSS validations include it |
| Legacy POS vendor | Hotels and Attractions | Both | The same legacy integrated POS and the same vendor remote support tool at 23 hotels and 2 Florida theme parks (gap 1). One vendor compromise reaches both divisions (P08) |
| Guest profile hub (SYS-G5) | Group | All three divisions | Loyalty lookups from PMS and POS, park app sign-in, owner portal sign-in, and tour marketing leads. Its payment preferences table holds owners' bank data (gap 2) |
| CRS (SYS-H2) | Hotels | Attractions (packages); Vacation Ownership (rentals) | Park packages and owner inventory rentals are sold through the CRS |
| Tour leads | Hotels and Attractions | Vacation Ownership sales (BP-V02) | About 46% of tours come from hotel guests and park visitors |
| SOC facts (BP-G02) | Group | Every notice | Card brand, FTC, state, owner, and SEC clocks all depend on the SOC establishing what happened |
| Florida destination resort | Hotels and Attractions | Both | 3 resort hotels sell room-linked park tickets; a PMS or gate outage affects both |

**Single points of failure found:**
- SYS-G1 (mitigated by break-glass accounts, tested quarterly).
- SYS-G4, the one tokenization and vault service for all divisions (mitigated by an active standby region; P2PE terminals authorize without it).
- The legacy POS vendor's remote support path into both divisions (P01 GR-01; POAM-001).
- One ACH bank for loan and maintenance-fee autopay (P01 VO-12, accepted until the 2027 bank review).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | Hotels, Attractions, corporate | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, hubs, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in Cloud provider B |
| SYS-G4 payment services | BP-G05 and every card channel | Active standby region; vault replication every 15 minutes; tokens are useless without the vault keys held in the key management service |
| SYS-G5 guest profile hub | BP-G06 and loyalty lookups | Database replicas; daily immutable backups |
| SYS-H1 cloud PMS (vendor SaaS) | BP-H01, BP-H04 interface | Vendor replication (RPO 15 minutes per contract); downtime reports every 4 hours |
| SYS-H3 and SYS-A2 POS | BP-H03, BP-A03 | Cloud POS vendor replication; legacy POS servers backed up nightly by the POS vendor (restore not tested by the group) |
| SYS-A1 ticketing and gates | BP-A01, BP-A02 | Vendor replication; offline ticket lists cached on handheld scanners each morning |
| SYS-A4 ride control | BP-A04 | Offline library of approved controller images and configurations, verified each quarter |
| SYS-V2 loan servicing (vendor SaaS) and origination | BP-V03, BP-V04 | Vendor replication; origination database backed up nightly in the legacy data center (migration to Cloud provider B in 2027) |
| SYS-V3 owner services | BP-V01, BP-V05 | Nightly backups in the legacy data center; restore tested once in 2025 |
| People | All | Cross-trained front office and gate staff; contact center overflow provider; remote work for owner services |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hubs
3. SD-WAN and property connectivity
4. Group payment services (SYS-G4)
5. SOC visibility (SIEM and EDR)
6. Ride and show control verification (rides stay closed until verified)
7. Park admission and gates
8. to 13. Hotel front desks, door locks, CRS, park POS, hotel POS, and online ticket sales
14. to 15. Owner reservations and loan servicing
16. to 28. Contact center, guest profile hub, park app, sales galleries, owner reporting, loan origination, revenue management, association billing, rental program, financial close, payroll, group sales, and the kids' club.

## 8. Key findings
1. **Shared services set the floor.** Group payment services (BP-G05) and identity (BP-G01) have shorter RTOs than any division process, as they must. Both met their RTOs in the 2026 failover tests.
2. **The legacy POS vendor is a shared single point of failure for two divisions.** It is also the top group risk for confidentiality (P01 GR-01).
3. **Vacation Ownership recovery is unproven.** SYS-V3 and the loan origination database sit in the legacy data center with one restore test in 2025 and none in 2026 (P01 VO-10; POAM-019).
4. **Ride control recovery is an engineering process, not an IT restore.** The offline image library works, but gap 9 means a park business network compromise could reach ride control at 2 parks. That is a safety risk, not only an availability risk (P01 ATT-02).
5. **Notification capacity is itself a process** (BP-G02, BP-H07, BP-G07). If the SOC, owner relations, or finance cannot work during an incident, card brand, owner, FTC, and SEC clocks keep running. The P08 runbook uses out-of-band channels for this reason.
