# Business Impact Analysis: Cris Santos Company | Other Services | Small

**Organization:** Cris Santos Company, LLC (electronics and device repair service) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the Operations Manager, the Store Managers, and the Data Recovery Lead | **Approved:** General Manager, 2026-09-04

## 1. Overview and purpose
This BIA identifies the business processes the company depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the contingency plan the company does not yet have (POA&M item POAM-006 in P07).

No law sets recovery times for a repair business. The drivers here are revenue, customer property in the company's custody, the manufacturer program agreements, and the confidentiality of customer data.

## 2. System and business description
Four Florida stores and the Depot handle about 200 repair tickets a business day. Everything runs through the Service Ticketing and Point-of-Sale Platform (STPP): the SaaS ticketing and POS system (SYS-01), P2PE payment terminals (SYS-02), the identity provider (SYS-03), a small cloud tenant (SYS-05), the data recovery lab (SYS-06), technician bench workstations (SYS-07), the site networks (SYS-09), and office endpoints and counter tablets (SYS-10). Warranty work also depends on the manufacturers' portals (SYS-08). See `../scenario-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to $20.4 million in annual revenue, about $78,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (about 2 business days of revenue) | $40,000 to $150,000 | Less than $40,000 |
| Operations | All stores cannot take in or release devices | One store, the Depot, or one service line stops | Staff slowed but working |
| Regulatory and contractual | Reportable breach (Fla. Stat. 501.171), loss of SAQ P2PE eligibility, or breach of a manufacturer program agreement | Missed contractual deadline (warranty claim window, business account turnaround) | Internal policy deviation |
| Safety | Not used: an IT outage at a repair shop does not create a plausible safety harm. Battery and electrical safety are handled by shop procedures outside this BIA | | |
| Reputation | Local media coverage, loss of authorized status, or loss of business accounts | Customer complaints or negative online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Device intake and check-in | High | 8 h | 4 h | 1 h |
| BP-02 Diagnostics and repair | High | 24 h | 8 h | 4 h |
| BP-03 Payment and device release | High | 8 h | 4 h | 1 h |
| BP-04 Manufacturer warranty claims | Moderate | 72 h | 24 h | 24 h |
| BP-05 Data recovery and data transfer | Moderate | 72 h | 48 h | 24 h |
| BP-06 Mail-in intake and return shipping | Moderate | 48 h | 24 h | 4 h |
| BP-07 Customer communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Business account service and invoicing | Moderate | 72 h | 48 h | 24 h |
| BP-09 Recycling drop-off and device sanitization | Low | 240 h | 120 h | 24 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Custody of customer property drives BP-01 and BP-03.** An 8-hour MTD equals one business day. Beyond that, devices pile up without tickets, and the risk of releasing a device to the wrong person rises. That is a data exposure as well as a lost-property problem.
- **Revenue drives BP-03.** P2PE terminals can run standalone, so card payments can continue for a while even if SYS-01 is down.
- **Data integrity, not time, drives BP-05.** Some failing drives can be read only once. If the lab storage loses an image, the customer's data may be gone for good, which is why its RPO of 24 hours must be backed by tested backups.
- **Contracts drive BP-04 and BP-08.** Warranty claims have submission windows, and business account contracts promise turnaround times.

## 5. Resource requirements
| Resource | Description | Supports | Backup or replication method |
|---|---|---|---|
| SYS-01 Ticketing and POS (SaaS) | System of record for tickets, customers, inventory, invoices | BP-01 to BP-04, BP-06 to BP-09 | Vendor-managed backups (SOC 2 system description states RPO 1 h, RTO 4 h; P09). **No company-held export** |
| SYS-02 P2PE terminals | Card payments | BP-03, BP-06 | Standalone mode; 2 spare terminals |
| SYS-03 Identity provider | Single sign-on and MFA | All | Vendor-managed |
| SYS-05 Cloud tenant | Recovered-data delivery, chatbot connector, backup vault | BP-05, BP-07 | Object versioning; backup vault in the **same account** (gap) |
| SYS-06 Data recovery lab storage | Customer device images and recovered files | BP-05 | Nightly backup to the cloud vault; **never restore-tested** |
| SYS-07 Bench workstations | Diagnostics, flashing, data transfer | BP-02, BP-05, BP-09 | Standard image held by the IT Support Technician; 2 spare bench PCs at the Depot |
| SYS-08 Manufacturer portals and tools | Warranty claims, parts pairing, diagnostics | BP-02, BP-04 | Manufacturer-operated |
| SYS-09 Site networks and internet | Firewalls, VPN, Wi-Fi | All | Single ISP per site; cellular hotspot at the Depot only |
| SYS-10 Office endpoints and counter tablets | Counter and office work | BP-01, BP-03, BP-08 | Spare tablets (1 per store) |
| People | Customer service advisors, technicians, Data Recovery Lead, IT Manager, IT Support Technician | All | Cross-trained counter staff at each store |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 Identity provider and emergency administrator access | 1 h | Two break-glass accounts (to be created; POAM-006) |
| 2 | SYS-09 Internet and network at the affected site | 2 h | Cellular hotspot kit per store (to be purchased) |
| 3 | SYS-10 Counter tablets and office PCs | 4 h | Spare tablet per store; paper intake forms |
| 4 | SYS-01 Ticketing and POS access | 4 h | Vendor-hosted; paper intake and release checklists; standalone terminals |
| 5 | SYS-07 Bench workstations | 8 h | Reimage from the standard image; spare bench PCs |
| 6 | SYS-08 Manufacturer portals | 24 h | Manufacturer-operated; queue claims |
| 7 | SYS-06 and SYS-05 Data recovery storage and delivery | 48 h | Restore from the cloud vault; pause new cases |
| 8 | SYS-11 Chatbot | 8 h target, lowest business need | Turn off with a website banner and phone number |
| 9 | Recycling and payroll | 72 to 120 h | Locked bins; repeat prior payroll |

## 7. Key findings
1. **The SYS-01 vendor's stated recovery objectives (RTO 4 h, RPO 1 h) meet BP-01 and BP-03,** but the company holds no export of its own. If the vendor account were compromised or closed, the company could not rebuild its customer and ticket records. A weekly encrypted export is recommended (P01 R-017).
2. **The data recovery lab's RPO is unproven.** The nightly backup has never been restore-tested and sits in the same cloud account as the delivery storage (P01 R-014; P04 finding 2).
3. **Single ISP at every store.** An internet outage stops BP-01 and BP-03 at that store except for standalone card payments (P01 R-020).
4. **Recovery must not spread exposure.** Restoring the lab storage or bench PCs must not bring back recovered customer data that should have been deleted. Retention rules (POL-04) must be applied before restores are used as a source.
