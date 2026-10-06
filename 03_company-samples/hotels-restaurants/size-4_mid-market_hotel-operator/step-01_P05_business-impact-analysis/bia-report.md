# Business Impact Analysis: Cris Santos Company | Accommodation and Food Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and GRC Analyst with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 (walkthroughs at all 6 hotels, 2026-07-13 to 2026-07-24) | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Resort 1, Resort 2, the 4 franchised select-service hotels (Hotels 3 to 6), the central reservations office (CRO), and the corporate shared services. It rates 16 business processes and puts a dollar value on what an outage costs, along with its operational, regulatory, guest safety, and reputational effects.

The results feed:
- the incident response plan, which PCI DSS v4.0.1 Requirement 12.10.1 expects to include business recovery and continuity procedures;
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment for the REIT management agreement (P09);
- the IT sections of the hotels' hurricane plans (section 7).

## 2. System and business description
The company runs 1,160 rooms in 6 Florida hotels, about 147,000 stays a year, and about 1.05 million card transactions a year under 10 merchant accounts. Guest-facing and payment work runs on the Property Management and Point-of-Sale Platform (PMPS) described in the SSP (P02): the resort PMS (SaaS), payment gateways and devices, the resort outlet POS systems, the SD-WAN and property networks, 520 PCs and 180 tablets and phones, the door lock systems, the identity provider, the 4-account cloud landing zone, and the MSSP-operated SIEM. Hotels 3 to 6 also depend on the franchisor's PMS, central reservation system, and loyalty platform (SYS-02), which the company does not control (see `../00_company-facts.md` sections 3, 4, and 7).

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue, about $274,000 a day: Resort 1 about $114,000 (rooms $82,000; food, beverage, and other $32,000), Resort 2 about $91,000 (rooms $66,000; other $25,000), and Hotels 3 to 6 about $69,000 together.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 of lost revenue or extra cost | $20,000 to $100,000 | Less than $20,000 |
| Operations | A hotel cannot check guests in, issue keys, or take payments | One outlet, one channel, or one hotel's back office stops | Staff slowed but working |
| Regulatory | Card compromise notice to the acquirer and card brands, reportable breach, or a franchise or management agreement default | Missed contractual or record-keeping duty (for example, the Fla. Stat. 509.101(2) guest register) | Internal policy deviation |
| Guest safety | Guests cannot secure or reach their rooms, or cannot be accounted for during an evacuation | Delayed service with a safe workaround | None |
| Reputation | Regional media, a wave of online reviews, loss of online travel agency ranking, or franchisor or REIT intervention | Individual complaints and reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra cost (guest compensation, walked guests, overtime, and security staffing) over the process's MTD. The process owners supplied the recovery assumptions: about 30% of bookings missed during a distribution outage and about 40% of lost CRO and outlet sales are not recovered. Payments delayed by an outage are shown as revenue at risk, not as loss, because most are collected later.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-02 Room access and key management | All 6 hotels | High | 2 | 1 | 24 | $15,000 |
| 2 | BP-01 Guest arrival and check-in | All 6 hotels | High | 4 | 2 | 1 | $45,000 |
| 3 | BP-10 Guest safety and security operations | All 6 hotels | High | 4 | 2 | 4 | $5,000 |
| 4 | BP-03 Guest payments and folio settlement | All 6 hotels | High | 8 | 4 | 1 | $20,000 |
| 5 | BP-04 Reservations and distribution | Resorts and Hotels 3 to 6 | High | 8 | 4 | 1 | $21,000 |
| 6 | BP-05 Central reservations phone sales | CRO | Moderate | 8 | 4 | 1 | $5,000 |
| 7 | BP-06 Resort food, beverage, spa, and retail | Resorts | Moderate | 8 | 4 | 4 | $8,000 |
| 8 | BP-09 Housekeeping, room status, and maintenance | All 6 hotels | Moderate | 12 | 8 | 4 | $10,000 |
| 9 | BP-16 Guest Wi-Fi and in-room entertainment | All 6 hotels | Moderate | 12 | 6 | 24 | $12,000 |
| 10 | BP-08 Night audit, accounting, and card settlement | All 6 hotels and corporate | Moderate | 24 | 12 | 24 | $6,000 |
| 11 | BP-12 Guest communications and marketing | Corporate | Moderate | 24 | 8 | 24 | $8,000 |
| 12 | BP-07 Group sales, catering, and events | Resorts | Moderate | 72 | 24 | 24 | $25,000 |
| 13 | BP-11 Revenue management and rate publishing | Corporate | Low | 72 | 48 | 24 | $15,000 |
| 14 | BP-13 Payroll, timekeeping, and HR | Corporate | Low | 120 | 72 | 24 | $10,000 |
| 15 | BP-14 Procurement and accounts payable | Corporate | Low | 120 | 72 | 24 | $3,000 |
| 16 | BP-15 Financial reporting and owner and lender reporting | Corporate | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 5 High, 7 Moderate, and 4 Low processes (16 in total). The sum of estimated losses at each process's MTD is $213,000.

**Enterprise-wide scenario.** If the whole PMPS were down for 72 hours (for example, ransomware that takes out the resort PMS interfaces, lock servers, and corporate systems), the unrecovered revenue and extra cost would be about $620,000: guest compensation and walked guests about $240,000, lost bookings about $190,000, overtime and added security staffing about $135,000, and resort outlet sales about $55,000. About $250,000 of card settlements a day would also be delayed until the gateways and night audit are back. Incident response, card brand, and notification costs come on top (see P01 R-001 and R-002).

**What drives the values:**
- **Guest safety drives BP-02 and BP-10.** Existing key cards keep working when a lock server is down, but new arrivals cannot get keys and lost keys cannot be cancelled. Two hours is the longest the hotels can rely on escorted entry. The in-house list must be current enough to account for guests during an evacuation.
- **The arrival window drives BP-01.** Most of the 400 daily arrivals come between 15:00 and 22:00.
- **Overbooking drives the 1-hour RPO for BP-04 and BP-05.** Online travel agencies keep selling from the last inventory they received, so a lost hour of reservations can put two parties in one room.
- **BP-11 is Low.** Rates can be set by hand for several days. This also means switching off the pricing AI is a safe response to a pricing problem (P10).
- **Contracts, not law, drive most regulatory ratings.** The merchant agreement, the franchise agreements, and (from 2027) the REIT management agreement carry the notice and recovery duties. The guest register (Fla. Stat. 509.101(2)) is the main statutory record.

## 5. Key findings
1. **The resort PMS vendor's recovery objectives are not in the contract.** Its SOC 2 report states RTO 4 hours and RPO 15 minutes. That meets the 4-hour RTO for payments and distribution (BP-03, BP-04) but **not the 2-hour RTO for check-in (BP-01)**. The printed lists every 4 hours and emergency key cards cover the difference. Action: write the objectives into the contract at renewal (P01 R-014; P09 vendor review).
2. **Hotels 3 to 6 depend on the franchisor for check-in, payments, and distribution.** The franchise agreements state no recovery objectives and give the company no say over recovery order. The brand's own continuity plan has not been shared (P01 R-016).
3. **Company-managed recovery is unproven.** The resort lock servers are backed up weekly to a local disk only and have never been restored. The data warehouse and CRM restores have never been tested. The RTOs for BP-02, BP-12, and BP-15 are targets, not demonstrated capabilities (P01 R-015, R-017; P07 CP-4).
4. **Resort 2's legacy POS has no tested fallback.** If its on-premises server fails, outlets fall back to paper checks with no way to take cards except loaner P2PE devices, which have not been set up (P01 R-019).
5. **IT is missing from the hurricane plans at Hotels 3 to 6.** The resorts' plans cover moving the lock server and network equipment; the select-service hotels' plans do not (P01 R-018).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Resort PMS (SaaS) | Reservations, profiles, folios, card vault, interfaces | BP-01 to BP-05, BP-07 to BP-10 (resorts and CRO) |
| SYS-02 Brand platform (franchisor) | PMS, central reservation system, loyalty for Hotels 3 to 6 | BP-01, BP-03, BP-04, BP-08, BP-09 (Hotels 3 to 6) |
| SYS-03 Payment gateways and devices | 14 P2PE devices at the resorts; 12 brand terminals at Hotels 3 to 6 | BP-01, BP-03, BP-08 |
| SYS-04 Outlet POS | Resort 1 cloud POS with P2PE; Resort 2 legacy on-premises POS | BP-06, BP-08 |
| SYS-05 Booking engine and channel manager | Direct and online travel agency bookings | BP-04 |
| SYS-06 SD-WAN and property networks | 7 sites; dual internet at the resorts and corporate office, single at Hotels 3 to 6 | All |
| SYS-07 Endpoints | 520 PCs and laptops; 180 tablets and phones; 2 pre-imaged spares per hotel | BP-01, BP-03, BP-05, BP-08, BP-09 |
| SYS-08 Door lock systems | Resort lock servers; cloud lock service at Hotels 3 to 6 | BP-01, BP-02 |
| SYS-09 Identity provider | SSO and MFA | All company-managed systems |
| SYS-10 Cloud landing zone | Data warehouse, CRM, integration services, websites, backup account | BP-08, BP-11, BP-12, BP-15 |
| SYS-12 SIEM (MSSP) | Detection and investigation | Recovery validation |
| SYS-15 CRO contact center | Calls, recording, call analytics | BP-05 |
| SYS-16 HR and payroll | Time clocks, payroll, applicant tracking | BP-13 |
| SYS-17 CCTV and building systems | Resort video management and building management | BP-10 |
| People and facilities | Front desks, night auditors, engineering, security officers (contracted), resort server rooms (ground floor at Resort 1, second floor at Resort 2) | All |

## 7. Hurricane plan linkage
Both resorts sit on the coast and all 6 hotels are in Florida, so a hurricane is the most likely cause of a multi-day outage. The hotels' hurricane plans cover guests and buildings. This BIA supplies the IT content:

| Hurricane plan element | What this BIA supplies | Status |
|---|---|---|
| Accounting for guests | BP-10: printed in-house lists every 4 hours at the resorts and at night audit at Hotels 3 to 6 | Resorts in place; Hotels 3 to 6 at night audit only |
| Room access during power loss | BP-02: lock batteries keep existing keys working; emergency key cards; escorted entry log | In place |
| Protecting on-site equipment | Resort 1 server room is on the ground floor; move the lock server and core switch above flood level | Resort 1 relocation planned 2027 Q1 |
| Payments when networks are down | BP-03 and BP-06: P2PE standalone mode at the resorts; brand gateway portal at Hotels 3 to 6; no paper card numbers | Resort 2 outlets have no card fallback (finding 4) |
| Communicating with booked guests | BP-12: website banner and phone tree; chatbot hands hurricane questions to staff (P10) | In place at the resorts |
| Rates during a declared state of emergency | BP-11: AI-001 emergency mode (Fla. Stat. 501.160) | Due 2026-10-31 (P10) |
| IT recovery at Hotels 3 to 6 | Recovery priorities in section 8, coordinated with the franchisor | To be added by 2027-05-31 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 SD-WAN and internet (resorts first) | 1 h | Cellular failover at the resorts; cellular hot spots at Hotels 3 to 6 (to be purchased) |
| 2 | SYS-08 Door lock servers and encoders (resorts); confirm the cloud lock service (Hotels 3 to 6) | 1 h | Emergency key cards; mechanical override keys with an entry log |
| 3 | SYS-09 Identity provider and break-glass accounts | 1 h | Two sealed break-glass accounts per critical system |
| 4 | SYS-07 Clean front desk PCs | 2 h | 2 pre-imaged spare laptops per hotel |
| 5 | SYS-01 Resort PMS access; SYS-02 brand platform status from the franchisor | 2 h (vendor states 4 h) | Printed arrivals and in-house lists |
| 6 | SYS-17 CCTV recording | 2 h | Added security patrols |
| 7 | SYS-03 Payment devices and gateways | 4 h | P2PE standalone mode; gateway portals |
| 8 | SYS-05 Distribution; SYS-15 CRO contact center | 4 h | Stop-sell through vendor portals; route calls to front desks |
| 9 | SYS-04 Outlet POS (Resort 1 cloud, then Resort 2 server) | 4 h | Paper checks; loaner P2PE devices |
| 10 | SYS-12 SIEM feeds and EDR console | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 11 | SYS-11 Email; SYS-14 chatbot; websites | 8 h | Phones; website notice |
| 12 | SYS-10 Data warehouse, CRM, integration services; SYS-13 revenue management | 48 h | Manual rates and reports |
| 13 | SYS-16 Payroll and timekeeping | 72 h | Paper time sheets; repeat prior payroll |
