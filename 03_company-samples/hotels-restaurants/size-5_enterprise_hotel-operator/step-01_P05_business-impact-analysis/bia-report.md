# Business Impact Analysis: Cris Santos Company | Accommodation and Food Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded hotel franchisor, manager, and owner: 750 hotels in 33 states and DC) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, franchisees, and the resorts acquired in 2025. It feeds:
- the availability rating and recovery objectives in the Property and Payment Platform (PPP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the PCI DSS incident response plan and business continuity requirements (PCI DSS 12.10.1) assessed in P03;
- the recovery order in the POS and reservation compromise runbook (P08);
- the Availability criteria and service commitments for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 7 are High criticality, 9 Moderate, and 1 Low. 8 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 15 of them single points of failure (overall or per hotel) and 9 never tested.

## 2. System and business description
Cris Santos Company franchises, manages, and owns 750 hotels (about 96,000 rooms) under four brands: 38 owned or leased, 72 managed for third-party owners, and 640 franchised. The 110 owned, leased, and managed hotels are company-operated and employ about 9,900 of the company's 12,000 employees. Annual revenue is about $4.8 billion, about $13.2 million per calendar day. The technology estate is described in `../00_company-facts.md` section 3: the central reservation system (SYS-01), the brand cloud PMS (SYS-02), the tokenization service and card vault (SYS-03), the POS estate (SYS-04), the managed property network (SYS-05), digital channels (SYS-06), loyalty (SYS-07), channel connectivity (SYS-08), and about 1,100 vendors (SYS-15). Fourteen resorts were acquired in 2025-06; nine are still on the seller's systems under a transition services agreement.

**What makes a hotel company different:** many of the processes below serve hotels the company does not own. A CRS or PMS outage hits 640 franchised hotels and 180 independent distribution clients at once, so service credits, franchisee claims, and brand reputation weigh as much as the company's own room revenue.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A system-wide service stops (all brands), or more than 50 hotels cannot check in guests or take payments | One brand, one region, or up to 50 hotels affected | Staff slowed but working |
| Regulatory and contractual | Reportable breach of card or personal data in several states; failed PCI DSS validation; missed SEC filing | Missed contractual deadline (franchise, management, or client agreement); breach in one state | Internal policy deviation |
| Safety | Plausible harm to guests or staff (room access failure, building systems in extreme heat) | Inconvenience with a safety workaround in place | None |
| Reputation | National media, analyst or ratings action, loss of franchisees or management contracts | Regional media; owner or franchisee complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Central reservations and distribution | High | 6 h | 2 h | 15 min | $4.20M |
| BP-03 Card payment authorization, tokenization, and settlement | High | 4 h | 2 h | 15 min | $3.10M |
| BP-02 Front desk operations (PMS) | High | 8 h | 4 h | 15 min | $2.60M |
| BP-04 Guest room access (door locks and key encoding) | High | 4 h | 2 h | 1 h | $0.60M |
| BP-08 Franchise technology services (SL-1) | High | 8 h | 4 h | 15 min | $1.20M |
| BP-06 Contact center reservations and guest service | High | 8 h | 4 h | 24 h | $0.80M |
| BP-17 Operations at the 9 resorts on the seller's legacy systems | High | 8 h | 8 h | 15 min | $0.85M |
| BP-05 Food and beverage outlet sales | Moderate | 12 h | 4 h | 1 h | $0.90M |
| BP-09 Independent hotel distribution services (SL-2) | Moderate | 8 h | 4 h | 15 min | $0.25M |
| BP-07 Loyalty program operations | Moderate | 24 h | 8 h | 15 min | $0.70M |
| BP-10 Digital guest services (website, app, mobile check-in, digital key) | Moderate | 24 h | 8 h | 1 h | $0.45M |
| BP-13 Building management integrations | Moderate | 12 h | 8 h | 24 h | $0.30M |
| BP-11 Revenue management and rate distribution | Moderate | 72 h | 24 h | 24 h | $0.35M |
| BP-12 Group sales, events, and catering | Moderate | 48 h | 24 h | 24 h | $0.40M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-15 Financial close, owner reporting, franchise fee billing, and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |
| BP-16 Guest Wi-Fi and in-room entertainment | Low | 48 h | 24 h | 24 h | $0.15M |

**What drives the values:**
- **Guest safety** sets the shortest MTD for room access (BP-04): guests must be able to reach their rooms and lost keys must be voided. Fire and life safety egress is mechanical and does not depend on the lock servers.
- **System-wide reach** drives the CRS (BP-01) and payments (BP-03). Online travel agencies close availability after about 4 hours of failed messages, and franchise agreements commit the CRS to 99.9% monthly availability (fictional term), which allows about 43 minutes of downtime a month.
- **Contracts** set the objectives for franchise technology services (BP-08) and the independent hotel distribution clients (BP-09), because both are external commitments reported on in SOC 2 (P09).
- **Regulation** tightens financial close (BP-15) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.
- **The acquisition** creates the only process whose actual recovery capability is far below its target: the transition services agreement for the 9 resorts (BP-17) states a 24-hour RTO and nightly backups.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Resort transition services (DEP-19, DEP-20).** The seller's PMS for the 9 resorts has a 24-hour contract RTO and a 24-hour real RPO against BIA targets of 8 hours and 15 minutes. Neither restore has been tested, and the seller's directory is not federated, so terminations at the resorts depend on manual tickets. Migration to the brand PMS and the company network is due 2027-03-31. This is P01 risk R-004 and POA&M items POAM-002 and POAM-003.
2. **Single gateway for CRS guarantees (DEP-04).** About 92% of card volume runs through one payment gateway. The secondary gateway covers front desk terminals only, so a gateway outage stops CRS guarantees and prepaid bookings. This is P01 risk R-028.
3. **Legacy property systems with vendor remote tools (DEP-06, DEP-15, DEP-22).** The legacy POS, door lock, and building management vendors reach their systems through vendor-managed remote tools outside the PAM gateway at 37 hotels. These are the paths the P08 scenario uses. 31 lock servers also run unsupported operating systems and have no tested recovery.
4. **Franchisee networks (DEP-26).** 230 franchised hotels run their own networks. Their outages do not reach company systems, but their compromises can reach the CRS and PMS through stolen franchisee credentials, and the company has no technical visibility into them.
5. **Revenue-management concentration (DEP-16).** One vendor sets recommended rates for 110 company-operated and 212 franchised hotels. Rates can be held for days, so the operational impact is small; the legal risk from its pooled benchmarking clause is assessed in P10.
6. **Strong core recovery (DEP-01, DEP-03, DEP-10, DEP-11).** The CRS, card vault, and identity platform met their RTOs in the 2026-04-25 disaster recovery test (CRS failover 1.6 hours, card vault restore 1.8 hours).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Central reservation system and guest profile hub | Company-built on Cloud provider A, active-passive across two regions | BP-01, BP-06, BP-07, BP-09, BP-10, BP-11 |
| SYS-02 Brand cloud PMS tenant | Vendor-hosted; company administers configuration, users, and interfaces | BP-02, BP-04, BP-08, BP-12, BP-15 |
| SYS-03 Tokenization service and card vault | Cardholder data environment account on Cloud provider A | BP-01, BP-02, BP-03, BP-09 |
| SYS-04 POS estate | Cloud POS with P2PE (153 outlets); legacy integrated POS (111 outlets) | BP-05 |
| SYS-05 Managed property network | SD-WAN, hotel firewalls, hubs in colocation DC-1 and DC-2 | BP-02, BP-04, BP-05, BP-08, BP-13 |
| SYS-07 Loyalty platform | Vendor SaaS | BP-07, BP-10 |
| SYS-09 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-11 Hotel building and guest-room technology | Lock servers, building management, guest Wi-Fi, IPTV | BP-04, BP-13, BP-16 |
| SYS-12 ERP, payroll, owner and franchise accounting | SOX-relevant | BP-14, BP-15 |
| SYS-13 Contact center platform | CCaaS with tone-masking card capture | BP-06 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all cloud workloads |
| People | Front office, reservations, payments, engineering, SOC, franchise technology services | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-09 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; second region |
| 2 | Network hubs, SD-WAN, DNS, and cloud connectivity | 2 h | Hotel failover to the other hub; cellular backup |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | Tokenization service and card vault; gateway connectivity | 2 h | Standby vault in second region; P2PE terminals authorize directly |
| 5 | CRS, booking engine, and channel connections | 2 h | Paper bookings; direct online travel agency connections |
| 6 | Door lock servers and key encoders | 2 h | Emergency master key procedure with security escort |
| 7 | PMS tenant access and interfaces | 4 h | Vendor read-only downtime service; printed reports |
| 8 | Contact center platform and tone-masking service | 4 h | Calls routed to hotels |
| 9 | POS (cloud POS first; legacy POS hotel by hotel) | 4 h | Paper checks and room charges |
| 10 | Franchise technology services help desk and SL-2 client access | 4 h | Backup telephony; client status page |
| 11 | Resorts on the seller's systems | 8 h target (24 h per transition services agreement) | Paper downtime |
| 12 | Loyalty platform, website, and app | 8 h | Contact center manual redemption |
| 13 | Building management integrations | 8 h | Manual operation by engineering |
| 14 | Revenue management, group sales, guest Wi-Fi and IPTV | 24 h | Manual rates; printed event orders; lobby connectivity |
| 15 | Payroll, ERP, and financial close | 48 to 72 h | Repeat prior payroll; manual journals |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Resort transition services RTO and RPO below BIA targets; untested | P01 R-004; POAM-002 |
| Single gateway for CRS guarantees | P01 R-028 |
| Vendor remote tools outside PAM for legacy POS, door locks, and building management | P01 R-003; P03 G-034 and G-035; POAM-005 |
| 31 unsupported lock servers with no tested recovery | P01 R-009; POAM-009 |
| No technical visibility into 230 franchisee-operated networks | P01 R-006; POAM-012 |
| Revenue-management vendor concentration and pooled benchmarking clause | P01 R-012; P10; POAM-020 |
