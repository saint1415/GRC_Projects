# Business Impact Analysis: Cris Santos Company | Wholesale Trade | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded IT hardware and software distributor serving commercial resellers and DoD customers) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the AQ-1 acquisition. It feeds:
- the enterprise contingency and disaster recovery program (SP 800-53 CP-2, CP-4, CP-10) and the OCFP contingency plan;
- the availability rating and recovery objectives in the OCFP System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the supplier compromise runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

No regulation sets recovery times for a wholesale distributor. The drivers are revenue, reseller contracts, the SL-1 availability commitment, and federal reporting clocks that keep running during an outage (DFARS 252.204-7012(c): 72 hours from discovery; FAR 52.204-25(d): 1 business day from identification).

**Results in one line:** 17 processes were analyzed; 7 are High criticality, 9 Moderate, and 1 Low. 5 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 10 of them single points of failure and 3 never tested.

## 2. System and business description
Cris Santos Company distributes IT hardware, software, and cloud subscriptions from 6 distribution centers (FL-2, GA-1, TX-1, OH-1, NV-1, and TX-2 from the AQ-1 acquisition) to about 9,500 reseller and integrator accounts, and sells directly to DoD through Federal Solutions. It has 12,000 employees and about $4.8 billion of revenue (about $19.2 million per shipping day). The technology estate is described in `../00_company-facts.md` section 3: the ERP (SYS-01) and WMS (SYS-02) on Cloud provider A, the reseller commerce platform (SYS-03) on Cloud provider B, EDI through two VANs (SYS-04), a SaaS TMS (SYS-05), distribution-center OT at 4 sites (SYS-06), the identity platform (SYS-07), the SOC (SYS-08), the network and two colocation data centers (SYS-09), the Federal Solutions CUI Enclave (SYS-10), the lifecycle services platform (SYS-11), and the AQ-1 legacy environment at TX-2 (SYS-15).

## 3. Impact categories and values
Dollar thresholds are scaled to about $1.36 million of gross profit per shipping day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated. The company reports quantified impact as lost gross profit plus extra cost, because most revenue in a distributor is passed through to suppliers; revenue at risk is shown separately where it matters for cash.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 per day, or more than $5 million cumulative | $100,000 to $500,000 per day | Less than $100,000 per day |
| Operations | Order capture or shipping stops enterprise-wide, or 2 or more distribution centers stop | One channel, one distribution center, or one service line stops | Staff slowed but working |
| Regulatory | Missed DFARS 72-hour or FAR 52.204-25 1-business-day report; covered equipment delivered; CUI mishandled; missed SEC filing | Late notice to a prime or contracting officer; late CCPA response | Internal policy deviation |
| Safety | Injury risk on automated material handling; counterfeit or tampered equipment reaches a DoD network | Defective equipment reaches a commercial customer | None |
| Reputation | Loss of a top-5 OEM authorization or a top-20 reseller; national media; analyst or ratings action | Reseller complaints; SOC 2 exception visible to customers | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Order capture and order management | High | 8 h | 4 h | 15 min | $1.10M |
| BP-02 Distribution-center fulfillment and shipping | High | 12 h | 4 h | 15 min | $1.25M |
| BP-03 Reseller commerce platform and order APIs (SL-1) | High | 8 h | 4 h | 15 min | $0.35M |
| BP-04 EDI and B2B integration | High | 12 h | 4 h | 1 h | $0.35M |
| BP-09 Transportation and carrier management | High | 12 h | 4 h | 1 h | $0.60M |
| BP-05 Federal order fulfillment and contract compliance | High | 24 h | 8 h | 1 h | $0.18M |
| BP-17 AQ-1 order-to-cash at TX-2 (legacy ERP and WMS) | High | 12 h | 8 h | 15 min | $0.12M |
| BP-08 Receiving, product authentication, and inventory control | Moderate | 24 h | 12 h | 1 h | $0.25M |
| BP-15 Customer service, returns (RMA), and technical support | Moderate | 24 h | 12 h | 4 h | $0.08M |
| BP-07 Purchasing and replenishment | Moderate | 48 h | 24 h | 4 h | $0.12M |
| BP-06 Federal configuration and integration (CUI) | Moderate | 72 h | 24 h | 4 h | $0.08M |
| BP-10 Lifecycle services: configuration and ITAD (SL-2) | Moderate | 72 h | 24 h | 4 h | $0.20M |
| BP-11 Credit, invoicing, cash application, and collections | Moderate | 72 h | 48 h | 4 h | $0.06M |
| BP-12 Supplier payments and treasury | Moderate | 72 h | 48 h | 4 h | $0.10M |
| BP-14 Payroll and HR, including temporary worker onboarding | Moderate | 72 h | 48 h | 24 h | $0.04M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.02M |
| BP-16 Import and customs entry for the private-label line | Low | 72 h | 48 h | 24 h | $0.03M |

**What drives the values:**
- **Competition, not contracts,** sets the shortest MTDs. Resellers can buy the same SKU from another distributor within hours, so order capture (BP-01) and the reseller platform (BP-03) lose business for good after about one shipping day.
- **Carrier cutoffs** drive fulfillment (BP-02) and transportation (BP-09). WMS edge servers let each distribution center keep picking for up to 8 hours, but labels and manifests depend on the TMS.
- **Federal clocks** make BP-05 High even though it needs little IT. A cyber incident that disrupts systems also starts the DFARS 72-hour and FAR 52.204-25 1-business-day reporting clocks, so the reporting path (offline laptop with a medium assurance certificate) must work on day one.
- **CUI rules remove workarounds.** Federal configuration work (BP-06) has a long MTD but no workaround: CUI may be restored only inside the FSCE.
- **Authentication under pressure.** During an outage, receiving (BP-08) is the step most likely to be rushed. The workaround sends every open-market and suspect lot to quarantine until systems return.
- **Regulation** tightens financial close (BP-13) to 48 hours in the quarter-end window because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:
1. **EDI concentration (DEP-08).** The primary VAN carries 72% of EDI documents (about 800,000 a month) and failover to the secondary VAN has never been tested end to end. A multi-day VAN outage would push about a third of order lines to email and manual entry. This is P01 risk R-010 and POA&M item POAM-019.
2. **ERP recovery time (DEP-01).** The 2026-05-09 tier-1 DR test recovered the ERP in 5.5 hours against its 4-hour RTO; the WMS central instance and the reseller platform met their objectives. The delay came from manual database and interface reconfiguration steps (P01 R-012; POAM-010).
3. **AQ-1 at TX-2 (DEP-21, DEP-22).** The legacy ERP and WMS are backed up nightly to local storage, so the real RPO is 24 hours against a 15-minute target, and the restore has never been tested. The site-to-site VPN that carries AQ-1 EDI traffic also reaches the enterprise EDI translator and ERP integration layer, so a compromise at TX-2 can spread (P01 R-007, R-008; POAM-002).
4. **TMS (DEP-10).** The TMS vendor's contract RTO is 8 hours against the 4-hour BIA RTO. Carrier web portals cover only about 15% of normal volume (P01 R-033).
5. **Workforce and logistics third parties (DEP-12, DEP-18).** The 4 staffing agencies that supply up to 1,500 temporary workers and the 2 overflow 3PL warehouses are outside third-party risk tiering, although agency workers receive WMS accounts and handhelds (P01 R-031).
6. **Supply sources (DEP-14 to DEP-16).** The top 5 OEMs account for about 47% of revenue. Brokers (1.9% of spend) and drop-ship partners (22% of federal order lines) are the main product-integrity exposures; they feed the P08 scenario.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-07 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-09 Network, SD-WAN, COLO-1 and COLO-2 | Site connectivity, network core, offline backup copy | All |
| SYS-08 Security operations platform | EDR console and SIEM for clean-room validation | Recovery of all |
| SYS-01 ERP (Cloud provider A) | Orders, purchasing, inventory, finance | BP-01, BP-05, BP-07, BP-08, BP-11 to BP-13, BP-16 |
| SYS-02 WMS (Cloud provider A and edge servers) | Picking, packing, receiving, inventory locations | BP-02, BP-08, BP-17 (after cutover) |
| SYS-03 Reseller commerce platform (Cloud provider B) | Portal, quoting, APIs, subscriptions | BP-03, BP-15 |
| SYS-04 EDI translator and VANs | Order and invoice documents | BP-01, BP-04, BP-07 |
| SYS-05 TMS | Labels, manifests, tracking | BP-02, BP-09 |
| SYS-06 Distribution-center OT | Conveyors, sortation, automated storage | BP-02 |
| SYS-10 FSCE | CUI work for DoD configuration jobs | BP-06 |
| SYS-11 Lifecycle services platform | Imaging, ITAD tracking, sanitization records | BP-10 |
| SYS-15 AQ-1 legacy environment | AQ-1 orders and fulfillment until cutover | BP-17 |
| Offline federal reporting kit | Laptop with a DoD-approved medium assurance certificate; offline covered-manufacturer list | BP-05 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to COLO-1 | RPO for all cloud workloads |
| People | Sales desk, distribution staff, SOC, IT operations, Federal Solutions contracts staff | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-07 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at distribution centers |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Security operations runbooks on the offline kit |
| 4 | Offline federal reporting kit (BP-05) | 2 h | Second certificate holder at FL-1 |
| 5 | SYS-01 ERP and SYS-04 EDI translator | 4 h (5.5 h achieved in the 2026-05-09 test) | Sales desk spreadsheets; VANs queue documents |
| 6 | SYS-02 WMS central instance; SYS-05 TMS connections | 4 h | WMS edge servers (up to 8 h); carrier web portals |
| 7 | SYS-03 reseller commerce platform | 4 h | EDI and sales desk |
| 8 | SYS-06 OT warehouse control systems | 8 h | Manual sortation at reduced speed |
| 9 | SYS-15 AQ-1 legacy ERP and WMS | 8 h target (24 h or more achievable) | Paper pick lists; enterprise sales desk |
| 10 | Receiving and authentication functions (ERP, WMS, serial validation services) | 12 h | Receive to quarantine only |
| 11 | Contact center and RMA | 12 h | Order status exports |
| 12 | SYS-10 FSCE and configuration lab | 24 h | None for CUI; notify primes and contracting officers |
| 13 | SYS-11 lifecycle services platform | 24 h | Hold devices in secure cages |
| 14 | Forecasting platform (AI-001) and purchasing | 24 h | ERP reorder reports |
| 15 | Credit, invoicing, supplier payments | 48 h | Manual credit overrides; bank portal wires |
| 16 | Payroll and HR | 48 h | Repeat prior payroll |
| 17 | Financial close tools; import filings | 72 h | Last extracts; customs broker files from emails |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| ERP recovered in 5.5 h against a 4 h RTO | P01 R-012; P02 CP-10; POAM-010 |
| Primary VAN concentration and untested failover | P01 R-010; P03 (contingency rows); POAM-019 |
| AQ-1 RPO 24 h and RTO above 24 h against BIA targets; VPN reach into the EDI translator | P01 R-007, R-008; POAM-002 |
| TMS contract RTO 8 h against 4 h BIA RTO | P01 R-033 |
| Staffing agencies and 3PLs outside third-party risk tiering | P01 R-031; POAM-017 |
| No generators at OH-1, NV-1, TX-2 | P01 R-036 (accepted with volume shifting) |
