# Business Impact Analysis: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board safety, security, and risk committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, network and cloud, the group integration platform, ERP payments, finance, HR).
- **Division BIAs:** Freight Railroad (focus), Transload and Wholesale, and Railside Industrial Real Estate. They are rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Cybersecurity Incident Response Plan the Covered Railroads must keep for their Critical Cyber Systems, including measures to reduce the risk of operational disruption (SD 1580-21-01E II.D), and the identification of Critical Cyber Systems and business critical functions in the CIP (SD 1580/82-2022-01E III.A);
- the PTC service restoration and mitigation plan for interruptions of service (49 CFR 236.1033(f));
- the CDS availability commitments that the SOC 2 report will cover (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 network, data centers, and cloud, SYS-G4 ERP, and SYS-G5 integration platform. Division systems are SYS-R1 to SYS-R5 (railroad dispatch, PTC, wayside OT, TMS, crew system), SYS-W1 to SYS-W4 (terminal operating system, terminal OT, wholesale commerce, fleet), and SYS-E1 to SYS-E3 (property management, building OT, right-of-way licensing). See `../00_company-facts.md` section 3. The SSP system in P02 is the Train Dispatching and PTC Back Office Platform (SYS-R1, SYS-R2, and the CTC office servers).

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Freight Railroad about $13.4 million per day, Transload and Wholesale about $33 million per day in sales (at a much lower margin), and Real Estate about $2.5 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 1 day of a division's operating income | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot deliver its core service (train movement, terminal throughput, building access) | One railroad, region, or terminal group stops | Staff slowed but working |
| Regulatory | Missed TSA, CISA, FRA, or SEC duty; reportable breach | Missed contractual or internal deadline | Internal policy deviation |
| Safety | Plausible harm to employees, passengers on hosted trains, or the public (movement authority, crossings, hazmat loading, building life safety) | Degraded but safe operation under restrictions | None |
| Reputation | National media, regulator attention, or loss of CDS customers or major shippers | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 10 Freight Railroad, 6 Transload and Wholesale, 4 Real Estate. 15 are High, 9 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Enterprise network, data centers, and cloud landing zones | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-R01 Train dispatching and movement authority | Freight Railroad | High | 4 h | 2 h | 15 min |
| BP-R03 CTC and wayside signal operations | Freight Railroad | High | 4 h | 2 h | 1 h |
| BP-R04 TSA RSSM location response and chain of custody | Freight Railroad | High | 30 min | 30 min | 4 h |
| BP-R02 PTC operations (host and tenant) | Freight Railroad | High | 4 h | 4 h | 1 h |
| BP-R09 Contract dispatching and car management service (CDS) | Freight Railroad | High | 4 h | 2 h | 15 min |
| BP-R07 Grade crossing and wayside detector monitoring | Freight Railroad | High | 4 h | 4 h | 1 h |
| BP-R06 Crew calling and hours of service | Freight Railroad | High | 8 h | 4 h | 1 h |
| BP-G04 Group integration platform (EDI and API hub) | Group | High | 8 h | 4 h | 1 h |
| BP-R05 Car management, waybills, and interchange (TMS) | Freight Railroad | High | 24 h | 8 h | 1 h |
| BP-W02 Hazmat truck loading and shipping papers | Transload and Wholesale | High | 8 h | 4 h | 1 h |
| BP-W01 Terminal operations (rail unloading, storage, truck loading) | Transload and Wholesale | High | 24 h | 8 h | 4 h |
| BP-E01 Building access control and life safety monitoring | Real Estate | High | 8 h | 4 h | 24 h |
| BP-W05 Fleet dispatch and driver hours | Transload and Wholesale | Moderate | 24 h | 12 h | 4 h |
| BP-W03 Order-to-cash | Transload and Wholesale | Moderate | 48 h | 24 h | 4 h |
| BP-G07 Accounts payable and treasury payments | Group | Moderate | 48 h | 24 h | 4 h |
| BP-E04 Building environmental controls (BAS) | Real Estate | Moderate | 24 h | 12 h | 24 h |
| BP-R08 Track and equipment inspection records | Freight Railroad | Moderate | 72 h | 24 h | 24 h |
| BP-W04 Procure-to-pay (product purchasing) | Transload and Wholesale | Moderate | 72 h | 48 h | 24 h |
| BP-G05 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-R10 Revenue accounting and demurrage billing | Freight Railroad | Moderate | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-E02 Lease administration and rent collection | Real Estate | Low | 120 h | 72 h | 24 h |
| BP-W06 Federal contract deliveries and records | Transload and Wholesale | Low | 120 h | 72 h | 24 h |
| BP-E03 Right-of-way licensing and engineering documents | Real Estate | Low | 168 h | 120 h | 24 h |

**What drives the values:**
- **Safety and movement authority** drive the rail values (BP-R01 to BP-R03). Trains can move safely without the CAD system, but only on manual authority at a fraction of normal capacity. The 15-minute RPO reflects real-time replication to DC-2: a dispatcher must never issue authority from a stale picture of the railroad.
- **A regulatory clock** drives BP-R04. TSA can ask for RSSM car locations at any hour and the answer is due within 30 minutes (49 CFR 1580.203(d)), so the workaround (printed lists and an offline extract) must be ready before any outage, not restored after it.
- **Passenger operators and Class I hosts** drive PTC (BP-R02). Without the back office, trains run under the en route failure restrictions of 49 CFR 236.1029 and new trips are delayed.
- **Customer commitments** drive the CDS (BP-R09): 11 short lines rely on group dispatchers, and their agreements set a 4-hour recovery commitment.
- **Throughput more than time** drives the terminals and wholesale processes (BP-W01, BP-W03). Product waits in cars and tanks for a day at some cost, but hazmat loading (BP-W02) stops at once without rack controls and correct shipping papers.
- **Life safety** drives building access and fire alarm monitoring (BP-E01); fire alarm monitoring has an independent central station path, which is why its RPO is not a constraint.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | The rail OT directory trusts the corporate directory one way (gap 4); a corporate identity compromise is a path toward dispatch |
| Integration platform (SYS-G5) | Group | Rail TMS, terminal TOS, ERP, property system | Car orders and car placement data for 41 terminals on group railroads pass through it; it also holds HR export files for all divisions. Not described in the CIP (gap 1) |
| Car switching (BP-R01, BP-R05) | Freight Railroad | Terminals (BP-W01) | A rail outage stops inbound product at 41 terminals within a day |
| Terminal car orders (BP-W01) | Transload and Wholesale | Rail car management (BP-R05) | Terminal outages leave cars unplaced and accrue demurrage |
| Real Estate sites | Real Estate | 22 terminals and 64 rail-served buildings | The wholesale division is a tenant at 22 sites; building access outages affect terminal staff |
| Right-of-way reviews (BP-E03) | Freight Railroad engineering | Real Estate licensing | Low time pressure |
| SOC facts (BP-G02) | Group | TSA, CISA, SEC, state, customer, and tenant notices | Every clock in P08 depends on it |
| Payments (BP-G07) | Group | All divisions' suppliers | Payment fraud controls (gap 6) |

**Single points of failure found:** SYS-G5 (one managed file transfer cluster in provider A; P01 GR-01); the hosted crew calling telephony provider (P01 RR-019); the PTC back office failover, which took 7.5 hours against a 4-hour RTO in the 2026-04-18 DR test (P01 RR-003).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) and rail OT directory | All | Vendor multi-region service; directory replicas at both NOCs |
| SYS-G3 data centers and landing zones | All | DC-1 to DC-2 replication; infrastructure as code; immutable backups in provider B |
| SYS-R1 CAD cluster | BP-R01, BP-R09 | Real-time replication to the DC-2 hot standby (failover 1.4 hours in the 2026-04-18 test; RTO 2 hours) |
| SYS-R2 PTC back office | BP-R02 | DC-2 standby (failover 7.5 hours in the test; RTO 4 hours) |
| SYS-R3 CTC office code servers | BP-R03 | Standby servers at the backup NOC |
| SYS-R4 TMS and SYS-R5 crew system | BP-R04 to BP-R06 | Provider A managed database replicas; immutable backups |
| SYS-G5 integration platform | BP-G04 | Single cluster; message store backed up hourly |
| SYS-W1 TOS and SYS-W2 terminal OT | BP-W01, BP-W02 | TOS replicas in provider A; rack controller configurations backed up only at 37 of 58 terminals |
| SYS-E2 building OT | BP-E01, BP-E04 | Vendor-held configurations (not verified) |
| People | All | Cross-trained dispatchers at both NOCs; regional terminal relief crews |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. Identity and break-glass access (SYS-G1)
2. Network, data centers, and landing zones (SYS-G3)
3. SOC visibility (SYS-G2)
4. to 10. Freight Railroad safety and movement processes: dispatching, CTC, the TSA RSSM response capability, PTC, the CDS customers, crossing and detector monitoring, crew calling
11. The group integration platform (needed for interchange and terminal car orders)
12. to 15. TMS, hazmat loading, terminal operations, building access and life safety
16. to 27. Fleet, order-to-cash, payments, building environmental controls, inspection records, purchasing, financial close, rail revenue accounting, payroll, leases, federal contract records, and right-of-way licensing.

## 8. Key findings
1. **The railroads recover first, but they do not recover alone.** Dispatch can run on manual authority, yet car management and terminal car orders stop when the integration platform stops. SYS-G5 is therefore High and must be named in the CIP's interdependency list (gap 1).
2. **The PTC back office RTO is not met.** A 7.5-hour failover against a 4-hour RTO (P01 RR-003; POAM-005).
3. **The 30-minute TSA location duty needs a workaround that is ready in advance.** It is (printed lists and an offline extract, tested twice in 2026), which is why BP-R04's workaround is the control, not its RTO.
4. **Terminal and building OT recovery is unproven.** Rack controller configurations are backed up at only 37 of 58 terminals, and building OT configurations are held by vendors (gaps 5 and 7).
5. **Notification capacity is itself a process.** If the SOC or the ERP is down, the TSA, CISA, SEC, and state clocks keep running. The P08 runbook uses out-of-band channels for this reason.
