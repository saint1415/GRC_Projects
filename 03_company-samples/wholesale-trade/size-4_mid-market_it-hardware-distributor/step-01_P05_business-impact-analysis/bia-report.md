# Business Impact Analysis: Cris Santos Company | Wholesale Trade | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Director of Information Technology with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: sales and order management, distribution operations at DC-1 and DC-2, supply chain, the commercial Integration Center, the Federal Integration Lab (FIL), federal programs, finance, customer service, and HR. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, mission and worker safety, and reputation.

No regulation sets recovery times for an IT distributor. The drivers are revenue, reseller and prime contracts, and the federal reporting clocks that keep running during an outage. The results feed:
- the contingency plan and recovery standard (SP 800-53 CP-2, CP-4, CP-9, CP-10; P06 STD-07);
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company ships about 3,600 shipments and 9,800 order lines per shipping day to about 4,200 reseller accounts and 7 federal channel customers, from DC-1 (about 80% of units, with conveyor, sortation, and vertical lift automation) and DC-2. Work runs on the Distribution Operations Platform (DOP) described in the SSP (P02): the SaaS ERP, the WMS in the cloud landing zone, the reseller portal and order API, EDI, the TMS, the identity provider, the networks, endpoints, DC automation, and the Federal Integration Enclave used by the FIL. See `../00_company-facts.md` sections 1, 3, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $820 million in annual revenue over 250 shipping days: about $3.28 million of revenue and $344,000 of gross profit per shipping day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (at the MTD) | More than $50,000 of lost gross profit and extra cost, or more than $5 million of cash delayed | $15,000 to $50,000 | Less than $15,000 |
| Operations | A distribution center cannot ship, or orders cannot be taken | One channel, site, or service stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Missed DFARS 252.204-7012 72-hour report, FAR 52.204-25 1-business-day report, or FAR 52.204-30 3-business-day report; CUI mishandled; covered equipment delivered | Late notice to a prime; sourcing or inspection records incomplete | Internal policy deviation |
| Safety (mission and worker) | Counterfeit, tampered, or misconfigured equipment reaches a DoD installation network; injury risk from manual conveyor operation | Defective equipment reaches a commercial customer | None |
| Reputation | Loss of a DoD prime, a national reseller, or the federal channel | Reseller complaints; SOC 2 questions from customers | Internal only |

**How loss at MTD was estimated.** Estimated loss is the gross profit on orders that are not recovered plus extra labor, expedite, detention, and chargeback costs, over the MTD. The process owners estimated that about 25% of orders that miss the shipping cutoff during a 12-hour outage are lost to competing distributors (30% for portal orders, 20% for EDI and DC-2), at the 10.5% gross margin. For billing (BP-12), the loss is overtime and interest on the revolving credit line; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-11 Government contract compliance and incident reporting | Federal programs | High | 24 | 8 | 24 | $0 (regulatory) |
| 2 | BP-04 DC-1 fulfillment and shipping | Distribution operations | High | 12 | 8 | 0.5 | $79,000 |
| 3 | BP-01 Order capture and order management | Sales and order management | High | 12 | 6 | 1 | $68,000 |
| 4 | BP-02 Reseller portal and order API | Sales and order management | High | 12 | 4 | 1 | $38,000 |
| 5 | BP-06 Transportation management and carrier labeling | Distribution operations | High | 12 | 4 | 1 | $50,000 |
| 6 | BP-03 EDI order, ship notice, and invoice exchange | Sales and order management | High | 24 | 8 | 1 | $32,000 |
| 7 | BP-05 DC-2 fulfillment, returns, and RMA | Distribution operations | Moderate | 24 | 12 | 1 | $22,000 |
| 8 | BP-14 Customer service and technical support | Customer service | Moderate | 24 | 12 | 4 | $15,000 |
| 9 | BP-07 Receiving, authenticity inspection, and inventory control | Distribution operations | Moderate | 48 | 24 | 1 | $24,000 |
| 10 | BP-09 Integration Center | Integration services | Moderate | 48 | 24 | 24 | $40,000 |
| 11 | BP-08 Purchasing and replenishment | Supply chain | Moderate | 72 | 24 | 4 | $30,000 |
| 12 | BP-10 Federal Integration Lab | Integration services | Moderate | 72 | 48 | 24 | $25,000 |
| 13 | BP-12 Credit, billing, collections, and cash application | Finance | Moderate | 72 | 48 | 4 | $35,000 (plus $9.8 million cash delayed) |
| 14 | BP-13 Supplier payments and bank-detail changes | Finance | Moderate | 72 | 48 | 4 | $20,000 |
| 15 | BP-15 Import and customs filing | Supply chain | Low | 120 | 72 | 24 | $10,000 |
| 16 | BP-16 Payroll, HR, and recruiting | Human resources | Low | 120 | 72 | 24 | $10,000 |
| 17 | BP-17 Analytics and reporting | Finance | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 6 High, 8 Moderate, and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $503,000.

**Enterprise-wide scenario.** If ransomware stopped the WMS, integration services, and DC automation for 72 hours while the SaaS ERP and portal stayed up, DC-1 would ship in manual mode at about 40% of capacity and DC-2 would stop. About $5.9 million of revenue would be delayed; at a 25% loss rate that is about $1.48 million of lost revenue, or about $155,000 of gross profit, plus about $400,000 of overtime, expedites, detention, and reseller credits. Incident response and any notification costs come on top (P01 R-001 and R-002).

**What drives the values:**
- **Revenue and reseller loyalty** drive BP-01 to BP-06. Resellers can buy the same SKUs from competing distributors, so an order that misses the cutoff is often lost.
- **Reporting clocks** make BP-11 High even though it needs little IT. The DFARS 252.204-7012(c) report is due within 72 hours of discovery, the FAR 52.204-25(d) report within 1 business day, and the FAR 52.204-30(c)(4) report within 3 business days. An outage caused by an incident starts those clocks at the worst time.
- **Mission safety** drives BP-07 and BP-10. Receiving is where counterfeit and tampered products are stopped, and the FIL configures equipment that goes onto DoD networks. During an outage the pressure to skip inspection rises, so the BP-07 workaround keeps every broker and private-label receipt in quarantine.
- **CUI handling rules** shape BP-10. Its MTD is long, but it has no workaround outside the enclave.

## 5. Key findings
1. **The ERP vendor's recovery commitment does not meet the BIA.** The ERP contract states an RTO of 24 hours; BP-01 needs 6 hours. The portal order queue keeps about 55% of order intake working during an ERP outage, but allocation, credit, and invoicing stop. Action: negotiate recovery terms at the 2027 renewal and test the queue-and-replay workaround (P01 R-014; P09 vendor review).
2. **WMS recovery is designed but not proven at scale.** The WMS database replicates every 15 minutes to a standby and is backed up daily to the write-once backup account, so the 30-minute RPO for BP-04 is achievable. A full rebuild was last tested in 2025-09 and took 14 hours against the 8-hour RTO (gap 6; P01 R-013; P07 CP-4).
3. **DC automation is a single point of failure.** Without the sortation controls, DC-1 runs at about 40% capacity. The control network is reachable from corporate VLANs and the integrator's remote access is always on (gap 4; P01 R-005).
4. **The TMS has no alternate.** Carrier web portals produce about 30% of normal label volume. Action: pre-registered carrier portal accounts at both DCs and a printed priority list (P01 R-016).
5. **The FIL can tolerate days, but only inside the enclave.** CUI may be restored only into the government community enclave. The enclave's recovery depends on the cloud provider's commitments, which are documented in its FedRAMP package and customer responsibility matrix (P04).
6. **The DIBNet reporting path has one person.** Only the Director of Federal Programs holds a medium assurance certificate. A second certificate is due by 2026-10-31 (gap 11; P01 R-022).
7. **HQ has one ISP.** HQ hosts customer service and the finance team; both can work from DC-1 if HQ loses connectivity.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 ERP (SaaS) | Orders, purchasing, inventory, finance | BP-01, BP-03, BP-05, BP-07, BP-08, BP-12, BP-13 |
| SYS-02 WMS (workloads account) | Picking, packing, receiving, bin locations; 420 RF handhelds | BP-04, BP-05, BP-07, BP-09 |
| SYS-03 Reseller portal and order API (SaaS) | Ordering, status, invoices | BP-02, BP-14 |
| SYS-04 EDI service (SaaS) | Purchase orders, ship notices, invoices | BP-03, BP-08 |
| SYS-05 TMS (SaaS) | Labels, tendering, tracking | BP-06 |
| SYS-06 Identity provider | Single sign-on and MFA | All |
| SYS-08 Landing zone | WMS, integration services, file services, data warehouse, backup account | BP-02, BP-04, BP-09, BP-17 |
| SYS-09 Federal Integration Enclave | CUI email and files, virtual desktops, build server | BP-10, BP-11 |
| SYS-10 Networks and SD-WAN | Dual ISP at DC-1 and DC-2; single ISP at HQ; FIL network | All |
| SYS-11 Endpoints | Laptops, FIL workstations, handhelds, label printers | All |
| SYS-12 DC automation | Conveyor, sortation, vertical lift controls | BP-04 |
| SYS-14 Security tooling | EDR, SIEM (MSSP), privileged access broker | Recovery validation |
| Third parties | ERP, portal, EDI, TMS, and identity vendors; cloud and government community cloud providers; DC automation integrator; MSSP; carriers; customs broker | As listed in `bia.csv` |
| People and facilities | DC-1, DC-2, HQ, the FIL cage; about 330 warehouse staff; 95 integration technicians; IT and security team | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, sealed offline |
| 2 | Clean device and certificate for DIBNet; out-of-band contact tree | 2 h | Reserved laptop kept offline at HQ; printed contacts (BP-11) |
| 3 | SYS-10 SD-WAN and DC-1 network | 2 h | Cellular failover at all sites; dual ISP at DC-1 and DC-2 |
| 4 | SYS-02 WMS (promote the standby, or restore from the backup account) | 8 h | Manual pick mode from printed pick lists (40% capacity) |
| 5 | SYS-05 TMS (vendor) | 4 h | Carrier web portals (30% capacity) |
| 6 | SYS-01 ERP access (vendor) and SYS-03 portal sync | 6 h (ERP), 4 h (portal) | Portal order queue; order form template |
| 7 | SYS-12 DC automation controls | 12 h | Manual lanes; integrator on site |
| 8 | SYS-04 EDI | 8 h | Secure email from trading partners |
| 9 | SYS-08 integration services and file services | 24 h | Manual uploads by the EDI and integration teams |
| 10 | SYS-09 enclave virtual desktops and build server | 48 h | FIL jobs paused; primes told of new dates |
| 11 | SYS-15 forecasting platform (AI-001) | 72 h | ERP reorder report; auto-release stays off until validated |
| 12 | Payroll SaaS and applicant tracking | 72 h | Repeat prior payroll |
| 13 | SYS-08 data warehouse | 120 h | ERP standard reports |
