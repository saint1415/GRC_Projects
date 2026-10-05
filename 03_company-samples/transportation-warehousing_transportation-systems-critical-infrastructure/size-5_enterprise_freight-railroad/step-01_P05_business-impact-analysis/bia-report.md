# Business Impact Analysis: Cris Santos Company | Transportation Systems | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded holding company of 64 short line and regional freight railroads in 27 states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** board safety, security, and risk committee, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, the Class I and passenger partners, and the acquired railroads. It feeds:
- the Cybersecurity Incident Response Plan objectives and the isolation and backup measures required of the Covered Railroads (SD 1580-21-01E Sec. II.D);
- the definition of business critical functions and Critical Cyber Systems in the TSA-approved Cybersecurity Implementation Plan (SD 1580/82-2022-01E Sec. III.A and VII);
- the availability rating and recovery objectives in the TDPB System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 9 are High criticality and 8 Moderate. 7 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies: 9 are single points of failure and 2 more are partial ones, and 5 have never been tested by the company.

## 2. System and business description
Cris Santos Company owns 64 freight railroads (60 Class III and 4 Class II) with about 11,400 route miles in 27 states, plus a rail services segment (industrial switching, transload terminals, and two technology services sold to unaffiliated railroads). It has 12,000 employees and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3:
- the centralized dispatch system (SYS-01) and PTC back office (SYS-02) at the primary NOC and DC-1 in Florida, with standby at the backup NOC and DC-2 in Texas;
- CTC, wayside, and radio OT (SYS-03);
- the TMS and crew system in Cloud provider A (SYS-04, SYS-05);
- the identity platform (SYS-06), the multi-cloud estate (SYS-07), SD-WAN and operations networks (SYS-08), and about 14,000 endpoints plus locomotive onboard systems (SYS-09);
- about 1,100 vendors (SYS-11).

Six railroads were acquired in 2025-2026; three (AQ-04 to AQ-06) still run their own legacy dispatch systems.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Train movement stops or falls below half of normal on more than 5 railroads, or any host passenger segment stops | One region, up to 5 railroads, or one service line slowed | Staff slowed but trains run |
| Regulatory | Missed TSA 30-minute location answer, missed TSA or CISA report, FRA PTC violation, missed SEC filing | Missed contractual or documentation deadline | Internal policy deviation |
| Safety | Plausible conflicting movement authority, unprotected crossing, missed hot bearing or defect alarm, PIH release | Delayed but safe operation | None |
| Reputation | National media, regulator action, Class I or passenger partner escalation, loss of SL-1 or SL-2 customers | Regional media; customer complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-06 TSA and hazmat security obligations | High | 0.5 h | 0.5 h | 4 h | $0.05M (penalty allowance) |
| BP-01 Train dispatching and movement authority | High | 8 h | 2 h | 0 | $7.20M |
| BP-03 CTC signal control and wayside monitoring | High | 4 h | 2 h | 1 h | $1.10M |
| BP-02 PTC operations on host and tenant territory | High | 8 h | 4 h | 15 min | $2.60M |
| BP-04 Crew calling and hours-of-service recordkeeping | High | 12 h | 4 h | 15 min | $2.40M |
| BP-11 SL-1 hosted PTC back office service | High | 8 h | 4 h | 15 min | $0.35M |
| BP-12 SL-2 dispatch and car management platform | High | 8 h | 4 h | 15 min | $0.25M |
| BP-05 Car management, waybilling, and interchange EDI | High | 24 h | 8 h | 15 min | $1.80M |
| BP-16 Dispatch on acquired railroads AQ-04 to AQ-06 | High | 8 h | 8 h | 24 h | $0.45M |
| BP-17 Safety and regulatory reporting | Moderate | 24 h | 12 h | 4 h | $0.02M (penalty allowance) |
| BP-07 Customer portal, car ordering, and shipment tracking | Moderate | 48 h | 24 h | 1 h | $0.40M |
| BP-09 Mechanical inspections, telematics, onboard PTC maintenance | Moderate | 72 h | 24 h | 24 h | $0.30M |
| BP-10 Rail services: industrial switching and transload | Moderate | 48 h | 24 h | 24 h | $0.60M |
| BP-08 Track, bridge, and signal inspection records | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-14 Payroll, timekeeping, and HR | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-13 Revenue accounting, billing, and interline settlement | Moderate | 120 h | 72 h | 24 h | $0.50M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |

**What drives the values:**
- **Safety sets the shortest MTDs.** A dispatcher must never lose an authority already in effect, so BP-01 has a zero RPO (synchronous replication to DC-2). Without CTC and wayside monitoring (BP-03), crossing and detector alarms stop reaching the NOC, so its MTD is 4 hours.
- **Regulation sets BP-06.** TSA can ask for RSSM car locations at any hour and the answer is due within 30 minutes (49 CFR 1580.203(d)), so the fallback must always be ready rather than recovered.
- **PTC sets BP-02.** Without the back office, host territory runs under the restricted-speed rules for en route failures (49 CFR 236.1029(b)) and 22 tenant railroads cannot initialize trains for Class I PTC lines (236.1006(a)).
- **Revenue concentrates in BP-01.** About 60% of the $11.5 million of daily rail operations revenue is deferred or lost when the NOC dispatches on paper.
- **Contracts set the service lines.** SL-1 and SL-2 customers have 4-hour RTO and 15-minute RPO commitments (P09).
- **SEC deadlines tighten BP-15** in the quarter-end window, when its MTD drops to 48 hours.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **PTC back office recovery (DEP-02, DEP-25).** In the 2026-04-25 DR test the CAD failed over to DC-2 in 1.6 hours (RTO 2 hours), but the PTC back office took 9.5 hours against its 4-hour RTO. The failover is manual, needs the PTC vendor on the bridge, and depends on two key custodians. The same platform serves SL-1 customers (BP-11), so the gap is also a contract risk. This is P01 risk R-004 and POA&M item POAM-006.
2. **Acquired railroads (DEP-18).** AQ-04 to AQ-06 dispatch on single legacy servers with nightly backups, so their real RPO is 24 hours and their vendors commit to next-business-day support. AQ-05 (CR-10) carries RSSM in an HTUA, so an outage there also tests the 30-minute TSA duty. Migrations to SYS-01 are due 2026-12-15, 2027-02-28, and 2027-05-31.
3. **Crew calling telephony (DEP-10).** One hosted provider places all automated crew calls, and the fallback (manual calls by company mobile phone) has never been tested for a full shift.
4. **Industry dependencies (DEP-04, DEP-15, DEP-16).** The interoperable train control messaging network, the Class I railroads, and the passenger operators are dependencies the company cannot remove. The workarounds are procedural and agreed in the interchange and operating agreements.
5. **Crossing monitor vendor (DEP-17).** About 310 monitored crossings in 2 regions report through a vendor's cellular modems that sit outside PAM and outside the OT asset inventory.
6. **Backhaul (DEP-06).** 14 tower sites on CTC territory have a single backhaul route.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 CAD | Centralized dispatch, DC-1 primary and DC-2 hot standby | BP-01, BP-12 |
| SYS-02 PTC back office | Host and tenant PTC office segment; SL-1 tenants | BP-02, BP-09, BP-11 |
| SYS-03 CTC and wayside OT | CTC code servers, field code units, wayside interface units, detectors, crossing monitors, radio | BP-01, BP-02, BP-03 |
| SYS-04 TMS (Cloud provider A) | Car management, waybills, consists, RSSM data | BP-05, BP-06, BP-07, BP-12 |
| SYS-05 Crew system (Cloud provider A) | Crew calling and hours of service | BP-04, BP-14 |
| SYS-06 Identity platform | SSO, MFA, PAM, OT directory | All |
| SYS-08 Networks | SD-WAN, NOC operations zone, industrial DMZ, field networks | All site-based processes |
| SYS-10 ERP, revenue, payroll, HR | SaaS | BP-13, BP-14, BP-15 |
| Immutable backups | Separate backup accounts with write-once retention; weekly offline copy in DC-2 | Recovery of all |
| People | Dispatchers, crew callers, signal maintainers, train control team, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 identity platform, OT directory, and break-glass accounts | 1 h | Sealed break-glass accounts; OT directory independent of the cloud identity provider |
| 2 | NOC operations zone network, industrial DMZ, radio and backhaul, DNS | 1 h | Cellular backup; satellite phones |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-01 CAD (and SL-2 dispatch tenants) | 2 h | Paper track warrants; hot standby in DC-2 |
| 5 | SYS-03 CTC code servers and wayside monitoring | 2 h | Local control by signal maintainers; patrols |
| 6 | RSSM location data for TSA (offline extract) | Ready at all times | Printed list every 4 hours; standby laptop |
| 7 | SYS-02 PTC back office (company and SL-1 tenants) | 4 h target (9.5 h demonstrated) | 236.1029(b) restricted operation; hold tenant trains |
| 8 | SYS-05 crew system and crew calling telephony | 4 h | Printed crew boards; manual calls |
| 9 | SYS-04 TMS and interchange EDI | 8 h | Paper waybills; consist exports |
| 10 | Legacy dispatch at AQ-04 to AQ-06 | 8 h target (24 h per vendor terms) | Paper track warrants |
| 11 | Safety reporting, customer portal, rail services systems | 12 to 24 h | Phone and paper |
| 12 | Mechanical and engineering applications | 24 to 48 h | Paper records |
| 13 | ERP, revenue accounting, payroll, HR | 48 to 72 h | Repeat prior payroll; manual invoices |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| PTC back office failover 9.5 h against 4 h RTO; 2 key custodians | P01 R-004; P02 CP-10; POAM-006 |
| Acquired railroads on single legacy dispatch servers (RPO 24 h) | P01 R-003 and R-015; POAM-001 |
| Manual dispatch fallback for CTC territory exercised at 2 of 11 signaled railroads | P01 R-013; P03 G-021; POAM-020 |
| No tested fallback for the TSA 30-minute RSSM location duty | P01 R-014; P03 G-038; POAM-019 |
| Crew calling telephony provider untested fallback | P01 R-022; POAM-021 |
| Crossing monitor vendor modems outside PAM and inventory | P01 R-010; POAM-008 |
