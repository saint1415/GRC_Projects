# Business Impact Analysis: Cris Santos Company | Communications | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier in Florida, Georgia, South Carolina, and North Carolina) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired carriers. It feeds:
- the availability rating and recovery objectives in the OSS/BSS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the CPNI intrusion runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09);
- the network contingency plans and storm procedures run by the NOCs.

For a carrier, the shortest downtime limits come from public safety and regulatory clocks, not only revenue. An outage that potentially affects a 911 special facility must be reported to the PSAP within 30 minutes of discovery and to the FCC within 120 minutes for wireline service (47 CFR 4.9(f), (h)). Those clocks keep running during a cyber incident.

**Results in one line:** 17 processes were analyzed; 10 are High criticality, 6 Moderate, and 1 Low. 9 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 13 of them single points of failure and 5 never tested.

## 2. System and business description
Cris Santos Company serves about 3.0 million accounts from 410 central offices and about 9,600 remote terminals and cabinets in four states: about 2.6 million broadband subscribers, about 1.15 million voice lines (520,000 copper and 630,000 interconnected VoIP), 110,000 business accounts, and 64 wholesale carrier customers. It has 12,000 employees and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: the converged BSS (SYS-01), the OSS (SYS-02), mediation and the CDR store (SYS-03), the portal and app (SYS-04), the identity platform (SYS-05), the voice core (SYS-06), the IP and access network (SYS-07), the management plane (SYS-08), the lawful-intercept platform (SYS-09), the contact center platform and chatbot (SYS-10), and a multi-cloud estate with two company data centers (SYS-11). Three carriers were acquired in 2025-2026; AQ-02 and AQ-03 are not yet integrated.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Service lost across a state or a tier-1 platform stops enterprise-wide | One service, one region, or one function stops | Staff slowed but working |
| Regulatory | Missed PSAP, NORS, CPNI breach, CALEA, or SEC duty; FCC enforcement exposure | Late filing or documentation gap | Internal policy deviation |
| Safety (public safety) | 911 calling unavailable for part of the service area; lawful intercept compromised | 911 degraded but calls complete through alternates | None |
| Reputation | National media, state commission or attorney general inquiry, analyst or ratings action, loss of large contracts | Regional media; customer complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Voice service and 911 call completion | High | 1 h | 0.5 h | 1 h | $2.60M |
| BP-03 Network surveillance, outage response, and regulatory outage reporting | High | 1 h | 0.5 h | 15 min | $1.10M |
| BP-05 Wholesale backhaul and SS7 signaling transport | High | 2 h | 1 h | 1 h | $2.20M |
| BP-09 Hosted unified communications and contact center (SL-2) | High | 2 h | 1 h | 15 min | $1.20M |
| BP-02 Broadband internet service delivery | High | 4 h | 2 h | 1 h | $9.40M |
| BP-04 Business transport and dedicated Ethernet | High | 4 h | 2 h | 1 h | $3.80M |
| BP-08 Managed network services (SL-1) | High | 4 h | 2 h | 1 h | $1.60M |
| BP-06 Lawful-intercept support (CALEA) | High | 8 h | 4 h | 24 h | $0.05M |
| BP-07 Customer care and account support | High | 12 h | 4 h | 15 min | $1.40M |
| BP-16 Operations at AQ-02 and AQ-03 | High | 12 h | 8 h | 15 min | $0.80M |
| BP-11 Field operations and repair dispatch | Moderate | 24 h | 8 h | 1 h | $0.70M |
| BP-13 Customer portal, app, and chatbot | Moderate | 24 h | 8 h | 1 h | $0.35M |
| BP-10 Service provisioning and activation | Moderate | 48 h | 24 h | 1 h | $0.90M |
| BP-14 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-12 Usage mediation, rating, billing, and collections | Moderate | 120 h | 72 h | 1 h | $0.60M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-17 Regulatory filings and lawful process response | Low | 72 h | 48 h | 24 h | $0.02M |

**What drives the values:**
- **Public safety** sets the shortest MTDs: voice and 911 (BP-01), the NOC that detects outages and notifies PSAPs (BP-03), and the SS7 and backhaul services other carriers' 911 calls ride on (BP-05). For network elements, the RPO is the age of the last archived configuration; the archive captures every change.
- **Revenue and churn** drive broadband (BP-02). A day of enterprise-wide broadband loss costs about $9.4 million in credits, care surge, and churn, the largest single figure in the BIA.
- **Contracts** drive business transport (BP-04), SL-1 (BP-08), and SL-2 (BP-09). Most enterprise SLAs promise 99.95% monthly availability, about 22 minutes a month, so a 4-hour MTD is already a large credit event.
- **The law, not the clock,** drives lawful intercept (BP-06). The direct cost is small, but a failed or compromised intercept must be reported to the affected agencies (47 CFR 1.20003(c)).
- **Switch buffers** set mediation (BP-12). Switches hold CDRs for 72 hours; after that, toll records and the CPNI record customers can dispute are lost.
- **Regulation** tightens financial close (BP-15) at quarter end, when the MTD drops to 48 hours because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **BSS recovery (DEP-01).** The converged BSS recovered in 7.5 hours against its 4-hour RTO in the 2026-05-09 DR test, because the database failover still has manual steps. Care (BP-07) can run on the offline account report for about one shift. This is P01 risk R-016, P02 control CP-10, and POA&M item POAM-011.
2. **Acquired carriers (DEP-20 to DEP-22).** AQ-02 and AQ-03 bill on legacy systems with nightly backups, so their real RPO is 24 hours against a 15-minute target, and neither restore has been tested. Their management networks are flat and reach the enterprise over site VPNs, so a compromise there can spread to the enterprise management plane (P01 R-003, R-051; POAM-003).
3. **911 delivery (DEP-06).** Each state's NG911 system service provider is a single point of failure the company cannot remove. Only the Florida provider has done a joint failover test with the company (P01 R-042).
4. **Legacy voice (DEP-05).** 61 TDM switches serving about 520,000 copper lines are past vendor support and cannot fail over line by line. Spares come from a third-party maintenance contract (P01 R-025; POAM-009).
5. **Outsourced care (DEP-09).** Three vendors handle 35% of care calls; CV-2 alone handles 17%. The CV-2 site-loss tabletop showed the in-house overflow covers about half of its volume. CV-2 is also where the CPNI authentication exceptions were found (P01 R-005, R-040; POAM-005, POAM-014).
6. **Industry dependencies (DEP-23).** Number portability administration is an industry-wide service; the workaround is to queue port requests.
7. **Untested fallbacks (DEP-18, DEP-19).** The payment processor has no tested alternate (accepted, P01 R-047), and the second bill print vendor's dormant contract has never been exercised.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-06 Voice core | IMS core, SBC clusters, TDM switches, STP pairs, 911 trunks | BP-01, BP-05, BP-09 |
| SYS-07 IP and access network | Backbone, metro, OLTs, DSLAMs, cabinets, DNS and DHCP | BP-01, BP-02, BP-04, BP-05, BP-08 |
| SYS-08 Management plane | Surveillance, element managers, TACACS+, jump hosts, configuration archive | BP-01 to BP-05, BP-08, BP-11 |
| SYS-09 Lawful-intercept platform | Isolated enclave in DC-1 and DC-2 | BP-06 |
| SYS-01 BSS and SYS-03 mediation (Cloud A) | Accounts, billing, CPNI approvals, CDR store | BP-07, BP-10, BP-12, BP-13 |
| SYS-02 OSS (Cloud A) | Inventory, activation, service assurance, workforce management | BP-03, BP-10, BP-11 |
| SYS-04 Portal and app; SYS-10 CCaaS and chatbot | Customer channels | BP-07, BP-13 |
| SYS-05 Identity platform | SSO, MFA, PAM | All |
| SYS-11 Cloud B | SL-2 UCaaS platform; data and AI platform | BP-09, BP-13 |
| DC-1 and DC-2 | Management plane, lawful intercept, mediation collectors, offline backup copy | BP-03, BP-06, BP-12; recovery of all |
| Power | Central office generators (72 hours of fuel at most offices), cabinet batteries, data center generators (96 hours) | BP-01, BP-02, BP-04, BP-05 |
| People | NOC (about 180), SOC, field technicians, care agents, about 30 lawful-intercept authorized employees | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Voice core and 911 trunks | 0.5 h | Geo-redundant SBC and IMS failover; PSAP notification in parallel |
| 2 | Management plane (clean jump hosts, TACACS+, configuration archive) and NOC surveillance | 0.5 h | NOC-2 and DC-2; sealed break-glass console credentials |
| 3 | Identity platform and break-glass accounts | 1 h | Secondary region |
| 4 | STP pairs, backhaul, and SL-2 voice | 1 h | Mated STP failover; second Cloud B region |
| 5 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | SOC standby tenant |
| 6 | Broadband gateways, DNS and DHCP; business transport | 2 h | Reroute; anycast DNS |
| 7 | SL-1 orchestration | 2 h | Devices keep last configuration |
| 8 | BSS and CCaaS (care) | 4 h target (7.5 h demonstrated) | Offline account report; callback queue |
| 9 | Lawful-intercept platform | 4 h | Re-provision active orders from mediation records; trusted third party |
| 10 | AQ-02 and AQ-03 legacy systems | 8 h target (untested) | Paper; enterprise NOC bridge |
| 11 | Portal, app, and chatbot | 8 h | Phone channel; status page |
| 12 | OSS workforce management and dispatch | 8 h | Phone dispatch from regional garages |
| 13 | OSS activation | 24 h | Manual work orders |
| 14 | Payroll; mediation and billing; ERP | 48 to 72 h | Repeat prior payroll; switch CDR buffers |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| BSS recovery 7.5 h against 4 h RTO | P01 R-016; P02 CP-10; POAM-011 |
| AQ-02 and AQ-03 legacy billing RPO 24 h, restores untested | P01 R-051; P07 CP-9 scope note |
| AQ management networks reach the enterprise over site VPNs | P01 R-003; POAM-003 |
| NG911 joint failover tested only in Florida | P01 R-042 |
| TDM switches past vendor support | P01 R-025; POAM-009 |
| Care vendor concentration and CPNI authentication at CV-2 | P01 R-005, R-040; POAM-005; POAM-014 |
| 19 central offices without fixed generators | P01 R-015 |
