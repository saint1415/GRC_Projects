# Business Impact Analysis: Cris Santos Company | Other Services (except Public Administration) | Micro

**Organization:** Cris Santos Company, LLC (independent electronics and device repair shop) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Shop Manager (Security and Privacy Lead) with the Owner, the Senior Technician, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the shop, how long each can be down, and how much data each can lose. No law requires a repair shop to have a BIA or contingency plan. The shop does it because:
- the risk register (P01) needs impact ratings tied to real business loss;
- the SSP (P02) needs an availability rating;
- the incident response runbook (P08) needs a recovery order;
- the property management account's security questionnaire asks how fast the shop can recover (P09);
- NIST CSF 2.0, the shop's benchmark, expects recovery priorities (ID.AM-05, RC.RP-02).

## 2. System and business description
One Florida storefront with 7 employees, about 22 repair tickets a business day, and about 60 customer devices in its custody at any time. Almost every business record lives in SaaS: the ticketing and POS platform (SYS-01), the payment processor's P2PE solution (SYS-02), and the productivity suite (SYS-03). In the shop are 4 office endpoints (SYS-04), 4 bench workstations (SYS-05), the bench storage (SYS-06), and the shop network (SYS-07). The MSP runs the office endpoints, the network, and the cloud backup (SYS-08). See `../00_company-facts.md` sections 3 and 7.

**What makes a repair shop different.** The shop holds two kinds of data. Its own records (tickets, customers, invoices) live mostly in SaaS. Its customers' data sits on devices and on the bench storage while a job is open. The shop is not the system of record for customer device data: the device itself is the source. So the shop's own loss tolerance (RPO) for that data is about re-doing work, while its confidentiality duty is high (see P02 section 6).

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,600 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (about 3 business days) | $3,500 to $10,000 | Less than $3,500 |
| Operations | The shop cannot check in, repair, or release devices | One function stops; work slowed | Staff slowed but working |
| Regulatory | Reportable breach under Fla. Stat. 501.171, or loss of SAQ P2PE eligibility | Missed contract term or late notice | Internal policy deviation |
| Safety | Plausible injury (for example a damaged battery handled without the bench procedure) | Delayed but safe handling | None |
| Reputation | Local news coverage, a wave of one-star reviews, or loss of a business account | Customer complaints or a few poor reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Intake, check-in, and quoting | High | 8 h | 4 h | 1 h |
| BP-02 Diagnostics and repair | High | 24 h | 8 h | 1 h |
| BP-03 Payment and device release | High | 8 h | 4 h | 1 h |
| BP-04 Data transfer and data recovery | Moderate | 72 h | 24 h | 24 h |
| BP-05 Customer communications | Moderate | 24 h | 8 h | 24 h |
| BP-06 Parts ordering and inventory | Moderate | 72 h | 48 h | 24 h |
| BP-07 Business accounts, bookkeeping, and payroll | Low | 72 h | 48 h | 24 h |
| BP-08 Recycling drop-off and device wiping | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- An MTD of 8 hours is one business day. Past that, walk-in customers go elsewhere and about $3,600 of revenue is lost or delayed each day.
- Payment and release (BP-03) are High because no payment means no release, and a device released to the wrong person is a privacy incident. The P2PE terminals can take payments in standalone mode while SYS-01 is down.
- The 1-hour RPO for BP-01 to BP-03 applies to ticket data in SYS-01. Losing an hour of tickets means calling customers to re-create them.
- Data transfer and recovery (BP-04) has a 24-hour RPO because a lost staging copy can usually be copied again from the customer's device. The exception is a recovery from a failing drive, which may not survive a second attempt. Those jobs are flagged on the ticket and finished before the bench storage is touched.
- Recycling (BP-08) earns nothing and can wait a week. Its regulatory impact is Moderate because devices must not leave the shop unwiped (Fla. Stat. 501.171(8)).

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Ticketing and POS (SaaS) | Tickets, customers, inventory, invoicing, status texts | Vendor backups (the vendor's SOC 2 system description states hourly backups, a 1-hour recovery point, and an 8-hour recovery time target; see P09) | BP-01, BP-02, BP-03, BP-05, BP-06, BP-07 |
| SYS-02 P2PE terminals and merchant portal | 2 counter PIN pads and 1 spare | Processor-operated; standalone mode when SYS-01 is down | BP-03 |
| SYS-03 Productivity suite (SaaS) | Email, the shared repairs mailbox, files | Vendor service resilience; nightly copy to SYS-08 | BP-05, BP-07 |
| SYS-04 Office endpoints | 2 counter PCs, 2 laptops | No business data stored locally by design; MSP reimages | BP-01, BP-03, BP-06 |
| SYS-05 Bench workstations | 3 bench PCs, 1 data transfer station | No standard image; rebuilt by hand by the Senior Technician (gap) | BP-02, BP-04, BP-08 |
| SYS-06 Bench storage | 8 TB staging for transfers and recovery images | Nightly copy to SYS-08 (**never restore-tested**); re-copy from the customer's device | BP-04 |
| SYS-07 Shop network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-08 Cloud backup (MSP-operated) | Nightly backup of SYS-03 and SYS-06; 1-year retention | **Never restore-tested** | BP-04, BP-07 |
| People | Owner, Shop Manager, Senior Technician, 2 Repair Technicians, 2 Counter Associates | Cross-training: the Owner can do every job; only the Senior Technician does board-level work and data recovery (key-person risk, P01 R-022) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Data it holds for the shop | Evidence of recovery capability |
|---|---|---|---|
| Ticketing and POS vendor | BP-01, BP-02, BP-03 (release records), BP-05, BP-06 | All customer and ticket records | SOC 2 Type 2 report (Security only) reviewed 2026-08-18 (P09). States RPO 1 h and an RTO target of 8 h |
| Payment processor | BP-03 | Card data (processor side only) | PCI DSS validated service provider; P2PE listing; standalone terminal mode |
| MSP | Recovery of the office endpoints and network; operates the backup | Administrator access to SYS-03, SYS-04, SYS-07, SYS-08 | No written recovery commitment; the contract has a 4-business-hour response time only |
| Productivity suite vendor | BP-05, BP-07 | Email, files | Vendor service commitments (standard terms) |
| Cloud backup service (MSP's provider) | Restores of SYS-03 and SYS-06 | Copies of email, files, and customer data | None until the first restore test |
| Internet provider | Every SaaS function, including the terminals | None | None; single line |
| Outside data recovery lab; courier; e-waste recycler | BP-04 (severe cases); BP-08 | Customer drives and devices | Not time-critical; no contract terms (P01 R-018) |

**Key findings:**
1. **The ticketing vendor's recovery time does not meet the BIA.** Its stated 8-hour RTO target is longer than the 4-hour RTO for intake and payment. The shop closes the gap with paper intake forms and the terminals' standalone mode, which need to be printed, stocked, and practiced (P08 section 7).
2. **The internet line is a single point of failure for every High function**, including the payment terminals (P01 R-015).
3. **The backup is unproven.** SYS-08 has never been restored, so the 24-hour RPO for BP-04 and BP-07 is an assumption (P01 R-010).
4. **The MSP contract has no recovery commitment**, and the MSP does not touch the bench workstations, which have no standard image. A bench rebuild depends on one person, the Senior Technician.
5. **Hurricane season is the most likely full stop.** Customer devices in custody must be protected and tracked if the shop closes (P01 R-016).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and shop network (SYS-07) | 2 h | Cellular failover router (to be installed by 2026-11-30); a phone hotspot for one counter PC until then |
| 2 | Payment terminals (SYS-02) | 2 h | Standalone mode; spare terminal |
| 3 | Counter PCs (SYS-04) | 4 h | The Owner's and Shop Manager's laptops; MSP reimages |
| 4 | SYS-01 access | 4 h | Vendor-hosted; paper intake forms, paper tags, and a paper release log until restored |
| 5 | Email, repairs mailbox, and status texts (SYS-03, SYS-01) | 8 h | Call customers from the printed ticket list |
| 6 | Bench workstations (SYS-05) | 8 h | Rebuild from a documented standard image (to be created by 2026-12-31) |
| 7 | Bench storage (SYS-06) | 24 h | Re-copy from customer devices; restore open jobs only |
| 8 | Restores from the cloud backup (SYS-08) | 48 h | Payroll service repeats the prior payroll; invoices sent late |

**Hurricane plan (summary; full checklist due 2026-11-30 with the P08 tabletop):** 48 hours before a forecast landfall, stop intake, call customers to collect finished devices, move remaining devices into sealed bags in the locked parts cabinet or off site with the Owner (logged by ticket number), unplug and raise bench equipment, and confirm the last cloud backup.
