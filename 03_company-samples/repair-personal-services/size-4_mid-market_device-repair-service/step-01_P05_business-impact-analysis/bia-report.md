# Business Impact Analysis: Cris Santos Company | Other Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (regional electronics and device repair chain) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the GRC Analyst, with the vCISO, the IT Director, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the 34 stores, the Depot, the digital channel (mail-in portal and partner integration API), partner programs, the contact center, business accounts, and corporate functions. It rates 16 business processes and quantifies what an outage costs in money, operations, and regulatory or contractual exposure.

No law sets recovery times for a repair business. The drivers here are revenue, customer property in the company's custody, the confidentiality of customer device data, the manufacturer program agreements, and the protection plan partner agreements.

The results feed:
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09);
- the contingency plan the company does not yet have (POA&M item POAM-007 in P07).

## 2. System and business description
About 1,000 repair tickets a business day run through the Service Ticketing and Point-of-Sale Platform (STPP) described in the SSP (P02): the SaaS ticketing and POS system (SYS-01), the identity provider (SYS-03), the 4-account cloud landing zone (SYS-04) with the company-built mail-in portal and partner integration API (SYS-05), the Depot data recovery lab (SYS-06), 238 bench workstations (SYS-07), the SD-WAN site networks (SYS-09), office endpoints and counter tablets (SYS-10), and the MSSP-operated EDR and SIEM (SYS-11). Card payments run on the payment processor's P2PE terminals and the gateway's hosted payment fields (SYS-02). Warranty work depends on the manufacturer portals (SYS-08). See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to $100.0 million in annual revenue over about 310 store business days, about $322,600 a day. The per-process revenue figures in `bia.csv` are rounded and add up to about $322,500.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $150,000 of lost revenue, or more than $500,000 of cash delayed | $30,000 to $150,000 | Less than $30,000 |
| Operations | All stores, the Depot, or the partner claims service cannot deliver its core service | One region, one service line, or the contact center stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory and contractual | Reportable breach (Fla. Stat. 501.171 or another state's law), loss of SAQ P2PE or SAQ A eligibility, or breach of a manufacturer or partner agreement | Missed contractual deadline (warranty claim window, partner acknowledgement time, business account turnaround) | Internal policy deviation |
| Safety | Not used: an IT outage at a repair business does not create a plausible safety harm. Battery and electrical safety are handled by shop procedures outside this BIA | | |
| Reputation | Regional media coverage, loss of authorized status, or loss of a protection plan partner | Customer complaints or negative online reviews in volume | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra labor and contract credits over the MTD. Recovery assumptions came from the process owners: about 40% of turned-away walk-in customers do not come back, about 20% of mail-in orders not placed during an outage are lost, partners reroute about 10% of claims during a long outage, and about 10% of delayed data recovery customers cancel. For warranty claims (BP-07) and partner billing (BP-14), the loss is overtime and interest; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-03 Payment and device release | Stores | High | 8 | 4 | 1 | $20,000 |
| 2 | BP-01 Device intake and check-in | Stores | High | 8 | 4 | 1 | $45,000 |
| 3 | BP-05 Protection plan claims intake and status | Partner programs | High | 12 | 8 | 1 | $15,000 |
| 4 | BP-02 Store diagnostics and repair | Stores | High | 24 | 8 | 4 | $35,000 |
| 5 | BP-06 Depot repair | Depot | Moderate | 24 | 12 | 4 | $18,000 |
| 6 | BP-04 Mail-in orders, checkout, and return shipping | Depot and digital | Moderate | 24 | 12 | 1 | $8,000 |
| 7 | BP-10 Contact center | Customer experience | Moderate | 24 | 8 | 24 | $6,000 |
| 8 | BP-07 Manufacturer warranty claims | Partner programs | Moderate | 72 | 24 | 24 | $6,000 (plus $164,400 of reimbursements delayed) |
| 9 | BP-08 Data recovery and data transfer | Depot | Moderate | 72 | 48 | 24 | $5,000 |
| 10 | BP-09 Customer communications | Customer experience | Moderate | 24 | 8 | 24 | $4,000 |
| 11 | BP-11 Business account service and invoicing | Business accounts | Moderate | 72 | 48 | 24 | $8,000 |
| 12 | BP-13 Parts purchasing and inventory | Corporate | Moderate | 72 | 24 | 24 | $12,000 |
| 13 | BP-14 Partner billing and claim settlement | Corporate | Moderate | 120 | 72 | 24 | $3,000 (plus about $258,000 of cash delayed) |
| 14 | BP-12 Recycling drop-off and sanitization | Depot and stores | Low | 240 | 120 | 24 | $1,000 |
| 15 | BP-15 Payroll, HR, and hiring | Corporate | Low | 120 | 72 | 24 | $10,000 |
| 16 | BP-16 Reporting and analytics | Corporate | Low | 168 | 120 | 24 | $2,000 |

**Summary:** 4 High, 9 Moderate, and 3 Low processes (16 in total). The sum of estimated losses at each process's MTD is $198,000.

**Enterprise-wide scenario.** If the whole STPP were down for 72 hours (for example ransomware, or a SYS-01 vendor outage combined with loss of the landing zone), unrecovered revenue would be about $227,000 (stores about $182,000, mail-in about $17,000, partner claims about $15,000, data recovery about $4,000, business account credits about $8,000), plus about $60,000 of overtime to clear backlogs. About $320,000 of warranty and partner cash would also be delayed. Incident response, notification, and partner credits come on top (see P01 R-003).

**What drives the values:**
- **Custody of customer property drives BP-01 and BP-03.** An 8-hour MTD is most of one store day. Beyond that, devices pile up without tickets, and the risk of releasing a device to the wrong person rises. That is a data exposure as well as a lost-property problem.
- **Revenue drives BP-03, and the P2PE design softens it.** The terminals run standalone, so card payments continue for a while even if SYS-01 is down.
- **Contracts drive BP-05, BP-07, and BP-11.** The partner agreements expect claim acknowledgement within 4 business hours, warranty claims have 5-business-day submission windows, and business account contracts promise turnaround times (all fictional terms).
- **Data integrity, not time, drives BP-08 and BP-14.** Some failing drives can be read only once, so the lab's RPO must be backed by tested backups. Partner billing depends on complete and accurate repair outcomes, which is why Partner P1 asked for Processing Integrity in the SOC 2 scope (P09).

## 5. Key findings
1. **The SYS-01 vendor's recovery objective does not meet the BIA for the stores.** The vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour. BP-01 and BP-03 need RTO 4 hours. Standalone P2PE terminals and paper intake make the 8-hour MTD survivable for one day, not longer. Action: recovery terms at the 2027 contract renewal and a tested store downtime kit (P01 R-010; P09 vendor review).
2. **Company-managed recovery is unproven.** The partner integration API (BP-05) and the mail-in portal (BP-04) run in the workloads account, and the lab storage (BP-08) is backed up to the backup account, but none has had a full restore or failover test (gap 9). Their RTOs of 8 to 48 hours are targets, not demonstrated capabilities (P01 R-006, R-011; P07 CP-4).
3. **The Depot is a single site for five processes.** Mail-in, Depot repair, partner claims repair, data recovery, and recycling all depend on one building. A hurricane or fire there would stop about $80,000 a day of revenue and leave thousands of customer devices in custody (P01 R-034, R-035).
4. **Recovery must not restore data that should be gone.** About 27 TB of recovered data is past its 90-day retention (gap 3). Restoring the lab storage from backup today would bring it back. Retention rules (POL-04) must be applied before backups are used as a recovery source.
5. **Contract clocks are shorter than outage tolerance.** Partners expect acknowledgement within 4 business hours. The partners' 72-hour replay window protects data (RPO), but not the service level. A partner outage notice template and a manual claims desk procedure are needed (P08 `ir-runbook-pos-compromise.md` section 7 and the contingency plan).

## 6. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-01 Ticketing and POS (SaaS) | System of record for tickets, customers, inventory, invoices, status portal | BP-01 to BP-11, BP-14 | Vendor-managed (stated RTO 8 h, RPO 1 h); weekly encrypted export to the backup account since 2026-03 |
| SYS-02 P2PE terminals and payment gateway | Card-present and e-commerce payments | BP-03, BP-04, BP-10 | Standalone terminal mode; 8 spare terminals; gateway operated by the provider |
| SYS-03 Identity provider | SSO, MFA, conditional access | All | Vendor-managed; 2 break-glass accounts (sealed) |
| SYS-04 Landing zone: workloads account | Mail-in portal, partner API, delivery storage, chatbot connector, reporting database | BP-04, BP-05, BP-08, BP-09, BP-16 | Daily backups to the backup account, 30-day write-once retention; **no failover test** |
| SYS-05 Mail-in portal and partner integration API | Company-built containers | BP-04, BP-05, BP-14 | Container images in the registry; infrastructure code in the repository; **no recovery test** |
| SYS-06 Data recovery lab | Storage array (about 95 TB used), imaging workstations | BP-08 | Nightly backup to the backup account; **never fully restore-tested** |
| SYS-07 Bench workstations | Diagnostics, flashing, data transfer | BP-02, BP-06, BP-08, BP-12 | Standard image (Depot and 20 stores); legacy image (14 stores); 6 spare bench PCs at the Depot |
| SYS-08 Manufacturer portals and tools | Warranty claims, parts pairing, diagnostics | BP-02, BP-06, BP-07 | Manufacturer-operated |
| SYS-09 Site networks and SD-WAN | 34 stores, Depot, corporate office | All | Cellular failover at every store; dual ISP at the Depot and corporate office |
| SYS-10 Office endpoints and counter tablets | Counter, contact center, and office work | BP-01, BP-03, BP-10, BP-11 | 2 spare tablets per region; pre-imaged spare laptops at the corporate office |
| SYS-11 EDR and SIEM (MSSP) | Detection and investigation | Recovery validation | MSSP platform |
| SYS-12 Contact center platform | Calls, queues, recordings | BP-10 | Vendor-managed; overflow answering service |
| SYS-16 ERP | Parts, purchasing, invoicing, payables | BP-11, BP-13, BP-14 | Vendor-managed |
| People and facilities | Store teams, Depot teams, data recovery specialists, IT and security team, MSSP, contact center | All | Cross-trained advisors at each store; second Depot shift |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity provider and break-glass accounts | 1 h | Two break-glass accounts stored sealed and offline |
| 2 | SYS-09 SD-WAN and store networks | 2 h | Cellular failover at each store |
| 3 | SYS-10 counter tablets and office endpoints for stores | 4 h | Spare tablets per region; paper intake and release kits |
| 4 | SYS-01 ticketing and POS access | 4 h target (vendor states 8 h) | Paper intake and release; standalone P2PE terminals |
| 5 | SYS-05 partner integration API | 8 h | Partners replay claims for 72 hours; manual claims desk |
| 6 | SYS-11 EDR and SIEM visibility | 8 h | MSSP runs from its own platform; needed to validate a clean recovery |
| 7 | SYS-07 bench workstations | 8 h (stores), 12 h (Depot) | Reimage from the standard image; spare bench PCs |
| 8 | SYS-12 contact center | 8 h | Overflow answering service; store phones |
| 9 | SYS-05 mail-in portal and checkout page | 12 h | Banner and phone bookings; phone payments on P2PE terminals |
| 10 | SYS-08 manufacturer portals | 24 h | Queue claims; manufacturer-operated |
| 11 | SYS-16 ERP | 24 h | Manual orders from the last stock report |
| 12 | SYS-06 and delivery storage | 48 h | Restore from the backup account after retention rules are applied; pause new cases |
| 13 | Partner billing, payroll, and reporting | 72 to 120 h | Hold invoices; repeat prior payroll; standard reports |
