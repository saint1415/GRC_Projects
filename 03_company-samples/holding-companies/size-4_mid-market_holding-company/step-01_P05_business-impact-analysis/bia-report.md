# Business Impact Analysis: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager and the VP of Information Technology, with the vCISO and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-13 to 2026-08-07 | **Approved:** CFO, 2026-09-22 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit in the group: the holding company's shared services, Supply, Home Services (including Home Services North), Fabrication, and Finance. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and safety.

A holding company's BIA has one feature a single business does not: **one outage of the shared platform can stop work at every subsidiary at once.** The BIA therefore rates each subsidiary's processes against the shared systems they depend on, so recovery can be ordered across companies rather than inside each one.

The results feed:
- the availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the CSF 2.0 group profile outcomes for resilience and recovery (P03: GV.OC-04, PR.IR-03, RC.RP-01);
- Finance's incident response plan, which must cover recovery from security events affecting customer information (16 CFR 314.4(h));
- the contingency plan and applications and data criticality analysis for the group health plan's ePHI held by the sponsor (45 CFR 164.308(a)(7), including (7)(ii)(E));
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The group has 600 employees at 9 Florida sites: HQ (holding company and Finance), the Supply distribution center and 3 branches, 3 Home Services shops, and the Fabrication plant. Shared services run on the Shared Corporate Services Platform (SCSP) described in the SSP (P02): a cloud ERP, a hybrid identity service (on-premises directory synchronized to a cloud identity provider), one productivity suite, a 5-account cloud landing zone (integration service, reporting warehouse, bank file transfer server, invoice imaging, backups), the HRIS, the treasury system and bank portals, the board portal, endpoints, site networks on SD-WAN, on-premises servers at HQ and the plant, and the security operations stack. Each subsidiary also runs its own line-of-business system (SYS-12 to SYS-15). See `../00_company-facts.md` sections 3, 4, and 7.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in consolidated receipts over about 250 business days: about $216,000 of sales per day at Supply, $104,000 at Home Services, and $48,000 at Fabrication. Finance collects about $220,000 a business day, and treasury releases about $3.5 million of payments a business day for the group.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 of unrecovered revenue or extra cost, more than $1 million of cash delayed, or any single fraudulent payment over $250,000 (the crime policy's social engineering sublimit) | $20,000 to $100,000 | Less than $20,000 |
| Operations | A subsidiary cannot serve customers, or two or more subsidiaries are slowed at once | One process at one subsidiary stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Reportable event under the FTC Safeguards Rule (16 CFR 314.4(j)), the HIPAA Breach Notification Rule for the plan, or a state breach law; borrower account errors at Finance | Missed lender covenant or reporting date; missed Regulation B notice timing | Internal policy deviation |
| Safety | Plausible harm to a person (an elderly customer without cooling in summer heat; a gas-smell call without safety instructions; a tampered machine program) | Delayed but safe service | None |
| Reputation | Loss of the bank partner, a lender's confidence, a key supplier, or regional media coverage | Customer complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra labor, over the MTD. Recovery assumptions came from the process owners: about 40% of lost Supply counter sales, 35% of missed Home Services calls, and 25% of delayed Fabrication orders are not recovered. For Finance and treasury, the loss is fee reversals, manual posting overtime, and returned items; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-12 Call handling and dispatch, including emergency calls | Home Services | High | 8 | 4 | 1 | $35,000 |
| 2 | BP-09 Order-to-cash (counters, phone, contractor portal) | Supply | High | 12 | 4 | 1 | $90,000 |
| 3 | BP-01 Treasury, payments, and bank file transfer | Holding company | High | 24 | 8 | 4 | $25,000 |
| 4 | BP-16 Payment collections and servicing | Finance | High | 24 | 8 | 4 | $30,000 (plus $220,000 cash delayed per day) |
| 5 | BP-05 Group communications and collaboration | Holding company | High | 24 | 8 | 24 | $40,000 |
| 6 | BP-10 Warehouse receiving, picking, and delivery | Supply | High | 24 | 8 | 1 | $60,000 |
| 7 | BP-14 Production (nesting, CNC cutting, forming) | Fabrication | High | 24 | 12 | 24 | $40,000 |
| 8 | BP-13 Field service, invoicing, and payment | Home Services | Moderate | 24 | 8 | 4 | $25,000 |
| 9 | BP-17 Loan origination, decisioning, and funding | Finance | Moderate | 48 | 24 | 4 | $20,000 |
| 10 | BP-15 Order entry and shipping | Fabrication | Moderate | 48 | 24 | 4 | $10,000 |
| 11 | BP-02 Payroll for five employers | Holding company | Moderate | 72 | 24 | 24 | $15,000 |
| 12 | BP-11 Purchasing and inventory replenishment | Supply | Moderate | 72 | 24 | 24 | $15,000 |
| 13 | BP-06 HR onboarding, offboarding, and records | Holding company | Low | 72 | 48 | 24 | $5,000 |
| 14 | BP-18 Compliance reporting and complaint handling | Finance | Low | 72 | 48 | 24 | $2,000 |
| 15 | BP-03 Accounts payable and vendor master | Holding company | Moderate | 120 | 48 | 24 | $20,000 |
| 16 | BP-04 Month-end close, consolidation, and lender reporting | Holding company | Moderate | 120 | 72 | 24 | $10,000 |
| 17 | BP-07 Group health plan administration | Holding company | Low | 120 | 72 | 24 | $5,000 |
| 18 | BP-08 Board, sponsor reporting, and acquisitions | Holding company | Low | 168 | 72 | 24 | $5,000 |

**Summary:** 7 High, 7 Moderate, and 4 Low processes (18 in total). The sum of estimated losses at each process's MTD is $452,000.

**Group-wide scenario.** If the shared platform and identity were down for 72 hours (for example, ransomware), unrecovered revenue would be about $404,000 (Supply $259,000, Home Services $109,000, Fabrication $36,000), plus about $150,000 of extra labor. About $660,000 of Finance collections would be delayed, and treasury would have to release about $10.5 million of payments by hand through the bank portals. Incident response, notification, and legal costs come on top (P01 R-001 and R-002).

**What drives the values:**
- **Safety drives BP-12.** It has the shortest MTD (8 hours) because an elderly customer without cooling in a Florida summer, or a caller reporting a gas smell, needs an answer within hours. BP-13 and BP-14 also carry a safety element (gas appliance records; machine programs).
- **Customers drive BP-09 and BP-10.** Contractors buy elsewhere within hours, and delivery crews stand idle.
- **Cash, consumers, and fraud drive BP-01 and BP-16.** Positive pay and ACH files have daily bank cutoffs, borrower payments must post on the due date, and outages are when payment fraud succeeds.
- **Contract dates drive BP-02 and BP-04.** Payroll has a fixed provider deadline, and the credit agreement fixes reporting dates.

## 5. Key findings
1. **Identity is the single point of failure for almost every process.** Every SaaS system except Home Services North's field-service product signs in through the cloud identity provider, which is synchronized from the on-premises directory. Two break-glass accounts exist for the cloud identity provider and were tested in 2026-06, but **no one has ever practiced recovering the directory forest** (gap 7; P01 R-004).
2. **The Fabrication plant cannot meet its RPO.** BP-14 needs a 24-hour RPO, but the plant server is backed up weekly to a removable drive kept in the plant office. A ransomware event or fire would lose up to a week of nesting programs (gap 7; P01 R-016).
3. **The distribution system vendor's recovery commitment does not meet the BIA.** Its contract states a 24-hour RTO; BP-09 needs 4 hours and BP-10 needs 8 hours. The loan servicing vendor's SOC 2 system description (RTO 8 hours, RPO 1 hour) meets BP-16, and the ERP vendor's (RTO 12 hours, RPO 1 hour) meets BP-03, BP-04, and BP-15 (P09 `vendor-soc2-review.csv`; P01 R-019).
4. **Home Services North is outside the plan.** Its dispatch runs on a separate field-service product with local accounts, and its recovery depends on the seller's IT provider. Its share of BP-12 has no tested workaround (gap 2; P01 R-007).
5. **HQ on-premises servers have never been restore-tested.** The scanner management server (BP-10) and the legacy Supply shares (BP-11) are backed up nightly to a NAS in the same server room, which a ransomware attacker could reach (P01 R-001).
6. **The after-hours AI voice agent is now part of BP-12.** If it fails, calls roll to the on-call manager. Its emergency triage script is a safety control and is assessed in P10 (AI-005).

## 6. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-02 Hybrid identity | On-premises directory (3 domain controllers) and cloud identity provider; single sign-on and MFA | All processes except Home Services North dispatch | Directory: nightly system-state backup to the HQ NAS, never restore-tested; cloud identity provider: provider-managed with 2 break-glass accounts |
| SYS-03 Productivity suite | Email, files, chat, phones, device management | BP-05, BP-12, and all others | Provider retention plus third-party backup (daily) |
| SYS-06 Treasury system and bank portals | Wires, ACH, positive pay | BP-01, BP-02, BP-07, BP-16, BP-17 | Vendor- and bank-hosted |
| SYS-04 SFTP server | ACH collection and positive pay files | BP-01, BP-16 | Daily backup to the separate backup account (write-once, 35 days); restore tested 2026-03 |
| SYS-04 Integration service, reporting warehouse, invoice imaging | Subsidiary feeds to the ERP; consolidated reporting; invoice capture | BP-03, BP-04, BP-09 | Daily backup to the separate backup account; restore tested 2026-03 |
| SYS-01 Cloud ERP | General ledger, payables, consolidation, Fabrication order module | BP-03, BP-04, BP-15 | Vendor-managed (RTO 12 h, RPO 1 h per its SOC 2 system description) |
| SYS-05 HRIS and payroll | Payroll, HR records, benefits enrollment | BP-02, BP-06, BP-07 | Vendor-managed |
| SYS-10 HQ servers | File servers, scanner management server, print server | BP-10, BP-11 | Nightly to the HQ NAS; never restore-tested |
| SYS-10 and SYS-15 Plant server and machines | Nesting and scheduling software; machine controllers | BP-14 | Weekly removable drive (does not meet RPO) |
| SYS-12, SYS-13, SYS-14 | Subsidiary line-of-business SaaS | BP-09 to BP-13, BP-16 to BP-18 | Vendor-managed; distribution system RTO 24 h (does not meet BIA) |
| SYS-08 Endpoints | 430 laptops and desktops, 95 tablets, 120 scanners | All | Standard images; 12 pre-imaged spare laptops at HQ, 4 at each Home Services shop |
| SYS-09 Site networks | SD-WAN at 9 sites | All | Dual ISP at HQ and the distribution center; cellular failover at branches and shops; single ISP at the plant |
| SYS-11 Security operations | EDR, SIEM (MSSP), scanner | Recovery validation | MSSP platform outside the group's environment |
| People | IT team (14), security team (4), MSSP, treasury team, dispatchers, servicing staff | All | Cross-training: CFO can release payments; Central dispatch can cover South and North |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 cloud identity provider and administrator access | 1 h | Break-glass accounts stored offline |
| 2 | SYS-09 HQ, distribution center, and shop networks | 2 h | Cellular failover kits; mobile hotspots |
| 3 | SYS-08 clean endpoints for dispatch, counters, and treasury | 4 h | Pre-imaged spare laptops kept offline |
| 4 | SYS-03 phones and email | 4 h | Call forwarding to dispatchers' mobile phones; personal phones for the incident team |
| 5 | SYS-13 and SYS-12 through single sign-on | 4 h | Paper dispatch board; printed price lists |
| 6 | SYS-06 bank portals | 4 h | Bank hardware tokens; phone instructions with callback |
| 7 | SYS-11 EDR console and SIEM feeds | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 8 | SYS-04 SFTP server | 8 h | Upload ACH and positive pay files directly in the bank portal |
| 9 | SYS-14 through single sign-on | 8 h | Vendor phone payment line; manual posting |
| 10 | SYS-02 on-premises directory (forest recovery if compromised) | 12 h target, unproven | Cloud-only accounts for critical SaaS until the directory is clean |
| 11 | SYS-10 plant server and HQ scanner management server | 12 h | Repeat programs on machine controllers; paper pick lists |
| 12 | SYS-01 ERP (vendor-hosted; confirm integrity) | 24 h | Payments from the bank portal with CFO approval |
| 13 | SYS-05 HRIS and payroll | 24 h | Provider reruns the prior payroll |
| 14 | SYS-04 integration service and invoice imaging | 24 h | Manual journal entries from subsidiary reports |
| 15 | SYS-04 reporting warehouse | 72 h | Rebuild from ERP exports |
| 16 | SYS-07 board portal and data room | 72 h | Encrypted email to directors |
