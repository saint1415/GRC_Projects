# Business Impact Analysis: Cris Santos Company | Transportation Systems | Small

**Organization:** Cris Santos Company, LLC (Class III short line freight railroad) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Vice President of Operations, Chief Dispatcher, Manager of Safety and Security, and Signal and Communications Supervisor | **Approved:** President and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the railroad depends on, how long each can be down, and how much data it can lose. It covers all 10 business processes. It feeds:
- the contingency plan for the dispatch platform, which does not exist yet (P03 G-043 and G-066; P07 POAM-005);
- the prioritized service restoration plan that 49 CFR 236.1033(f) expects the railroad "or its vendor or supplier" to have for PTC communication services (P03 G-027);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08).

## 2. System and business description
The railroad runs 186 route miles of non-signaled track in north-central Florida under track warrant control from one dispatch center at Central Yard, plus 26 miles of trackage rights over a Class I main line to reach interchange. It moves about 38,000 carloads a year, including about 600 PIH tank cars. Operations run 24 hours a day, 6 days a week.

The core IT and OT platform is the Train Dispatch and PTC Operations Platform (TDPO) in the SSP (P02): the computer-aided dispatch system (CAD), the PTC tenant components, the dispatch network and radio, the identity provider, and operations workstations. The TMS, crew management application, and office systems support it. See `../scenario-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to $36.4 million in annual revenue, about $117,000 per operating day (about 310 operating days a year).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $350,000 (about 3 operating days of revenue) | $50,000 to $350,000 | Less than $50,000 |
| Operations | No trains can move on company track or to interchange | One subdivision, the interchange, or one support function stops | Staff slowed but working |
| Regulatory | A missed TSA or FRA duty: the 30-minute RSSM location answer, the 24-hour TSA report, or a train on the PTC segment without an operative onboard unit | Late records or reports | Internal policy deviation |
| Safety | Plausible collision, derailment, grade crossing accident, or PIH release | Degraded but safe operations (manual procedures, reduced speed) | None |
| Reputation | The Class I or major shippers divert traffic; regional media coverage of a hazmat event | Shipper complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Train dispatching and movement authority | High | 24 h | 8 h | 1 h |
| BP-02 Crew calling and hours-of-service records | High | 24 h | 12 h | 4 h |
| BP-03 Interchange over the trackage-rights segment (PTC) | High | 48 h | 24 h | 4 h |
| BP-04 Car management, waybilling, and billing | Moderate | 72 h | 48 h | 24 h |
| BP-05 Track, bridge, and signal inspection and maintenance | Moderate | 72 h | 48 h | 24 h |
| BP-06 Detector and grade crossing health monitoring | High | 8 h | 4 h | 24 h |
| BP-07 Transload terminal operations | Moderate | 72 h | 48 h | 24 h |
| BP-08 Locomotive and car mechanical, onboard PTC | Moderate | 72 h | 48 h | 24 h |
| BP-09 TSA and hazmat security obligations | High | 0.5 h | 0.5 h | 4 h |
| BP-10 Payroll, HR, and finance | Low | 120 h | 72 h | 24 h |

Totals: 5 High, 4 Moderate, 1 Low.

**What drives the values:**
- **Safety drives BP-01 and BP-06.** Manual dispatch is the only safe way to keep trains moving without the CAD system, and nobody has practiced it since 2019. The 24-hour MTD for BP-01 reflects how long the dispatchers can sustain paper track warrants before fatigue and volume make a conflicting authority likely (P01 R-005).
- **A regulation drives BP-09.** TSA can ask for the location of RSSM cars at any hour and expects an answer within 30 minutes (49 CFR 1580.203(d)). The fallback therefore has to be ready at all times, not restored after an outage.
- **The host railroad drives BP-03.** A company train may not enter the Class I segment without an operative onboard PTC apparatus (236.1006(a)). Without the PTC back office service or current consist data, interchange stops.
- **Revenue drives BP-04 and BP-07** more than time does, because billing can wait and truck customers can be scheduled by phone for a few days.

**Key findings:**
1. **The 8-hour RTO for the CAD system is unproven.** The standby server sits in the same room as the primary, and the cloud backups share the production account and have never been restore-tested (P01 R-003 and R-019; P03 G-052 and G-067).
2. **The PTC back office contract has no restoration commitment.** The vendor promises 99.5% monthly availability but no recovery time, and the company has no fallback agreed with the host railroad (P01 R-013; P03 G-027). The vendor's SOC 2 report is reviewed in P09.
3. **The BP-09 fallback depends on the TMS and a working workstation** (P01 R-007). A printed RSSM car list and a clean standby laptop close this.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 CAD system | Primary and standby servers at HQ, 6 dispatch consoles and the chief dispatcher desk | BP-01, BP-05, BP-06 |
| SYS-02 PTC tenant components | Onboard units on 8 locomotives, PTC administration workstation, vendor-hosted back office | BP-03, BP-08 |
| SYS-03 TMS (SaaS) | Waybills, consists, car location, EDI, billing | BP-03, BP-04, BP-07, BP-09 |
| SYS-04 Operations network and radio | Dispatch VLAN, radio gateway and consoles, 7 tower sites, 3 detectors, 14 crossing monitors | BP-01, BP-06 |
| SYS-05 Identity provider | Single sign-on and MFA | BP-01 to BP-04, BP-10 |
| SYS-07 Corporate network | HQ firewall, VPNs to the yard offices and the cloud tenant | All |
| SYS-08 Endpoints | Operations workstations, crew tablets, office and shop PCs, standby laptop | All |
| SYS-09 Cloud tenant | Crew management application, file server, CAD backup vault | BP-01, BP-02, BP-04, BP-05 |
| SYS-10 Finance, payroll, and HR (SaaS) | Payroll, HR records, accounting | BP-10 |
| People | Dispatchers, crew callers, clerks, signal maintainers, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Manual fallbacks: paper track warrant kit, printed RSSM car list, standby laptop, TSOC phone number | Within 30 minutes of any outage | Kept ready at the dispatch center (to be completed by 2026-12-31) |
| 2 | Dispatcher radio (SYS-04 radio gateway, consoles, tower sites) | 2 h | Fallback repeater and handheld radios at dispatch |
| 3 | SYS-05 Identity provider and break-glass administrator accounts | 2 h | Two break-glass accounts stored offline (to be created; P06 POL-02) |
| 4 | SYS-07 and SYS-04 dispatch VLAN, isolated from the office LAN; detector and crossing alarm path | 4 h | Signal maintainer patrols of monitored crossings |
| 5 | SYS-01 CAD system restored to clean servers from verified backup | 8 h | Manual dispatch continues until restored |
| 6 | SYS-09 crew management application | 12 h | Paper crew board and on-duty forms |
| 7 | SYS-02 PTC administration workstation (rebuilt) and access to the PTC back office portal | 24 h | Hold interchange traffic; ask the Class I to move interchange cars |
| 8 | SYS-03 TMS access from clean endpoints | 24 h | Daily consist export; paper waybills |
| 9 | Office endpoints, productivity suite, and file server | 48 h | Personal phones for voice; paper forms |
| 10 | SYS-10 finance, payroll, and HR | 72 h | Repeat the prior payroll |
