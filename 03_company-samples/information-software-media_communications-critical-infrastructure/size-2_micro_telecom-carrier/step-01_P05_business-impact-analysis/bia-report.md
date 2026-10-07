# Business Impact Analysis: Cris Santos Company | Communications | Micro

**Organization:** Cris Santos Company, LLC (rural fiber broadband and voice carrier) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security and compliance lead) with the Network Operations Lead, both Customer Service Representatives, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner and General Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Availability criteria in the SOC 2 readiness check (P09), which the community bank branch asked about.

No FCC rule requires a carrier of this size to write a BIA or a contingency plan. The FCC outage rules (47 CFR Part 4) set **reporting** clocks, not recovery targets, but they shape this BIA: an outage must be noticed, measured against the thresholds, and reported on time (BP-03).

## 2. System and business description
One office building in a rural Florida town, one network hut about a mile away, about 140 route miles of passive fiber, and 7 employees. The company serves about 1,420 accounts: about 1,385 broadband subscribers, about 440 telephone numbers of interconnected VoIP voice, and 6 dedicated internet access circuits for local business and public customers. All internet traffic leaves over one leased 10 Gbps middle-mile circuit. Voice runs on a wholesale hosted voice platform; billing, the portal, and the AI assistant run on the BSS vendor's SaaS. The MSP runs office IT; the company runs its own network with help from a network engineering consultant. See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (credits, lost revenue, emergency repair) | $2,500 to $10,000 | Less than $2,500 |
| Operations | Most subscribers or all voice service down | One function stops; installs or billing delayed | Staff slowed but working |
| Regulatory | Missed FCC outage or breach clock; unlawful CPNI release; CALEA failure | Late or incomplete record or filing | Internal policy deviation |
| Safety | Customers cannot reach 911 from their lines | Delayed repair of a line used for medical or alarm purposes | None |
| Reputation | Local media coverage; loss of the town hall or bank circuit | Complaints and online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Broadband internet service delivery | High | 4 h | 2 h | 24 h |
| BP-02 Voice service and 911 calling | High | 2 h | 1 h | 24 h |
| BP-03 Network monitoring, repair, and outage response | High | 4 h | 2 h | 24 h |
| BP-04 Customer service and account support | Moderate | 24 h | 8 h | 1 h |
| BP-05 Service activation and changes | Moderate | 72 h | 24 h | 24 h |
| BP-06 Billing, payments, and collections | Moderate | 72 h | 48 h | 24 h |
| BP-07 Lawful intercept and law enforcement requests | Moderate | 24 h | 24 h | 24 h |
| BP-08 Office administration, payroll, and regulatory filings | Low | 72 h | 48 h | 24 h |

**What drives the values:**
- **911 drives BP-02.** Home phone lines are how some older and rural customers call 911. The MTD of 2 hours reflects that risk, not revenue.
- **The dedicated circuits drive BP-01.** Their 99.9% monthly commitment allows about 43 minutes of downtime a month before credits. A full outage of more than 4 hours would also bring complaints from the town hall and the bank branch.
- **Outage reporting drives BP-03.** If the middle-mile circuit (about 64 OC3 equivalents at 10 Gbps) is down for 30 minutes, the outage reaches about 1,920 OC3 minutes, above the 667 OC3-minute threshold in 47 CFR 4.9(f)(2). The 120-minute NORS notification clock then runs from discovery. The voice thresholds are much harder to reach at this size: 900,000 user minutes across about 440 numbers would take about 34 hours of total loss (47 CFR 4.5(e), 4.7(e), 4.9(g)).
- **RPO of 24 hours for the network.** Router and OLT configurations change only with orders and maintenance. A nightly backup is enough, if it can be restored (see finding 2).

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-03 Fiber access network | 2 OLTs, about 1,420 ONTs, aggregation switch | Nightly configuration backup to the hut server; spare line cards and optics in the warehouse | BP-01, BP-02, BP-05 |
| SYS-04 Network core and management | Edge router, 2 hut servers (EMS, DHCP, DNS, RADIUS, configuration backups) | DHCP and RADIUS run on both servers; EMS and backups on one; **backups stay in the hut and were never restore-tested** | BP-01, BP-02, BP-03, BP-05 |
| SYS-02 Hosted voice platform | Softswitch, numbers, 911 routing, CDRs | Provider's platform resilience (no evidence reviewed) | BP-02, BP-04, BP-06, BP-07 |
| SYS-01 BSS and portal | Accounts, orders, bills, tickets | BSS vendor backups and replication (SOC 2 report states RPO 1 hour; see P09) | BP-04, BP-05, BP-06 |
| SYS-05 Monitoring service | Device and circuit alerts, paging | Vendor-hosted; configuration export kept by the Network Operations Lead | BP-03 |
| SYS-06 and SYS-09 | Productivity suite and its cloud backup | Nightly backup by the MSP | BP-08 |
| SYS-07 and SYS-08 | Office endpoints, tablets, office network | MSP rebuilds from its standard image; office internet is the company's own fiber | All |
| People | 7 employees | The Office Manager covers customer service; one Field Technician is trained on basic router checks; the consultant covers network engineering | All |
| Facilities | Office building; network hut | Hut batteries and propane standby generator (about 72 hours of fuel at full load) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Middle-mile and transit provider | BP-01, BP-02, BP-03 (the office loses internet too) | Contract states a 4-hour repair target; **single path, no diverse route** |
| Hosted voice platform provider | BP-02, BP-04 (office phones), BP-06 (CDRs), BP-07 (voice intercepts) | Contract states 99.99% platform availability; no SOC 2 or recovery evidence requested yet |
| BSS vendor (also runs the AI assistant) | BP-04, BP-05, BP-06 | SOC 2 Type 2 report on file (reviewed in P09): RTO 8 hours, RPO 1 hour |
| OLT and router vendors | BP-01, BP-05 | Support contracts with next-business-day parts |
| Network engineering consultant | BP-01 recovery of router configuration | Retainer with best-effort response; no time commitment |
| MSP | Office IT recovery | 4-business-hour response time; no recovery time commitment |
| CALEA trusted third party | BP-07 | Contract states it can deploy collection within 24 hours of a valid order |
| Answering service | BP-03, BP-04 after hours | Message-taking only |

**Key findings:**
1. **The middle-mile circuit is a single point of failure** for both High customer-facing functions and for the office itself (risk R-011). A diverse second path is the largest open availability gap.
2. **Network recovery is unproven.** Configuration backups sit on the same hut server they protect and have never been restored. A hut fire, flood, or theft would take out both the network and its backups (risk R-007).
3. **Voice and 911 depend on a provider the company has never reviewed.** The platform contract promises availability, but the company has no evidence of how the provider recovers (risk R-017).
4. **Office phones ride on the company's own voice service.** During a voice outage, customers cannot call in to report it. The answering service number is the fallback, and the website banner must say so.
5. **Outage reporting depends on one person.** Only the Network Operations Lead knows the NORS thresholds, and no one has the county 911 center's outage contacts (risk R-012).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Hut power and environment; edge router and middle-mile circuit (SYS-04) | 2 h | Generator; provider repair; spare router configuration from the consultant's copy (once the offline copy exists) |
| 2 | OLTs and aggregation switch (SYS-03); DHCP and RADIUS | 2 h | Spare line cards and optics; second server for DHCP and RADIUS |
| 3 | Voice service check with the platform provider; 911 test call (SYS-02) | 1 h after the network | Forward business numbers to mobile phones; customer 911 script |
| 4 | Monitoring and paging (SYS-05) | 2 h | Manual checks; answering service as alarm |
| 5 | Office network and endpoints (SYS-07, SYS-08) | 8 h | Technician phone hotspots; laptops |
| 6 | BSS and portal (SYS-01) | 8 h | Vendor-hosted; take messages and call back |
| 7 | EMS and provisioning (SYS-04) | 24 h | OLT command line with the consultant; reschedule installs |
| 8 | Billing run, productivity suite restore (SYS-01, SYS-06, SYS-09) | 48 h | Delay the bill run; repeat the prior payroll |

Lawful intercept (BP-07) is handled outside this order: if an order arrives during an outage, the General Manager contacts the TTP and the platform provider directly.
