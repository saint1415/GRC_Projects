# Business Impact Analysis: Cris Santos Company | Transportation and Warehousing | Micro

**Organization:** Cris Santos Company, LLC (freight forwarding and customs brokerage office) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office and Compliance Manager with the owner, the Licensed Customs Broker (Entry Supervisor), the Accounting Specialist, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the office, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the customs broker duties that depend on records and systems being available: keeping records for 5 years in a form that can be readily examined (19 CFR 111.23(b), 111.25(a)), producing them within 30 days of a request (111.25(b)), paying the Government on time (111.29(a)), and keeping a working copy and a backup copy of records held in electronic form (163.5(b)(2)(vi)).

No contingency planning rule applies to the company directly. The USCG maritime cyber rule (33 CFR Part 101 Subpart F) covers facilities and vessels with security plans, which the company does not have (see P03). The BIA is still the base for every later step.

## 2. System and business description
One Florida office suite, 7 employees, about 180 active clients, about 4,500 entries, 4,000 ISFs, and 1,200 export shipments a year. Almost everything runs in SaaS: the customs brokerage and forwarding platform (SYS-01), the productivity suite (SYS-02), accounting (SYS-03), and online banking (SYS-04). On site are 9 computers and a printer (SYS-06) and the office network (SYS-07). The MSP runs IT and the suite backup (SYS-08). See `../00_company-facts.md` section 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 (about 3 business days of revenue, or one diverted wire) | $4,000 to $15,000 | Less than $4,000 |
| Operations | Entries or ISFs cannot be filed | One function stops; work slowed | Staff slowed but working |
| Regulatory | CBP penalty, license action, or missed 72-hour breach notice | Missed 10-day or 30-day CBP update; records not produced on time | Internal policy deviation |
| Safety | Not applicable: the office handles no cargo or equipment | | |
| Reputation | Loss of a major client or CTPAT client relationship | Client complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Import entry filing and cargo release | High | 8 h | 4 h | 1 h |
| BP-02 Importer Security Filing (ISF) | High | 8 h | 4 h | 1 h |
| BP-03 Duty, fee, and carrier and agent payments | High | 24 h | 8 h | 24 h |
| BP-04 Client communications | High | 8 h | 4 h | 4 h |
| BP-05 Ocean import and export forwarding | Moderate | 24 h | 8 h | 4 h |
| BP-06 Export EEI filing | Moderate | 24 h | 8 h | 4 h |
| BP-07 Client onboarding and customs records management | Moderate | 72 h | 48 h | 24 h |
| BP-08 Billing, collections, and accounting | Low | 72 h | 48 h | 24 h |
| BP-09 CBP license administration | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- An MTD of 8 hours is one business day. Past that, client containers begin to run past terminal free time, and ISFs tied to vessel loading abroad start to fall late.
- Payments (BP-03) tolerate 24 hours because CBP payment due dates are known in advance. The bigger payment risk is not downtime but fraud: a wire sent to the wrong account (P01 R-001).
- Records management (BP-07) tolerates 72 hours because CBP allows 30 calendar days to produce records (111.25(b)). Losing archive data, by contrast, is a regulatory failure, so its RPO is 24 hours.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Customs platform (SaaS) | Entries, ISF, EEI, client and POA files, shipment documents | Vendor backups and replication (vendor SOC 2 report states RPO 1 hour, RTO 8 hours; see P09) | BP-01, BP-02, BP-05, BP-06, BP-07 |
| SYS-02 Productivity suite (SaaS) | Email and the Client Records Archive | Vendor service resilience; daily copy to SYS-08 | BP-02, BP-04, BP-07 |
| SYS-08 Suite backup (SaaS) | Daily copy of mail and files, 1-year retention | **Never restore-tested** | BP-04, BP-07 |
| SYS-03 Accounting SaaS | Invoices, ledgers, payables | Vendor backups (standard terms) | BP-03, BP-08 |
| SYS-04 Online banking | ACH and wires | Bank systems | BP-03 |
| SYS-06 Endpoints | 6 desktops, 3 laptops, printer | No local data by design; MSP reimages | All |
| SYS-07 Office network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-09 Carrier and terminal portals | Bookings and container status | Carrier-operated | BP-05 |
| People | 2 licensed brokers, 2 Entry Writers, coordinator, accounting, office manager | Cross-training: the Entry Supervisor can file ISFs and EEI; the owner can release wires | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Contract terms | Evidence of recovery capability |
|---|---|---|---|
| Customs platform vendor | BP-01, BP-02, BP-06, and part of BP-05 and BP-07 | SaaS subscription; U.S. hosting stated | SOC 2 Type 2 report reviewed (P09); RTO 8 h and RPO 1 h. **The RTO is longer than the 4-hour target for BP-01 and BP-02** |
| MSP | Recovery of every on-site system; operates the backup | 4-business-hour response; no recovery commitment | None in writing |
| Productivity suite vendor | BP-04, BP-07, part of BP-02 | Standard business terms | Vendor service commitments |
| Backup service (MSP subcontractor) | Restore of mail and files | Through the MSP | None until the first restore test |
| Bank | BP-03 | Commercial account agreement | Bank operations |
| Internet provider | Every SaaS function | Business line | None; single line |
| Overseas agents and ocean carriers | BP-02 data and BP-05 | Agency agreements; carrier terms | Not assessed |

**Key findings:**
1. **The customs platform does not fully meet the BIA.** Its stated RTO (8 hours) is longer than the 4-hour RTO for entries and ISFs. The workaround is to file from another location through the vendor's web interface, which only helps when the vendor itself is up. For a vendor outage, a standby arrangement with another licensed broker is the only real alternate (P01 R-007).
2. **The suite backup is unproven.** SYS-08 has never been restored, so the 24-hour RPO for the Client Records Archive is an assumption (R-006). It is also the "back-up copy" that 163.5(b)(2)(vi) expects.
3. **The internet line is a single point of failure** for every High function (R-008).
4. **The MSP contract has no recovery commitment.** The 4-business-hour response time is not a recovery time (R-014).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and office network (SYS-07) | 2 h | Cellular failover router (to be installed by 2026-11-30); staff work from home on company laptops until then |
| 2 | Clean endpoints for the brokers and Entry Writers (SYS-06) | 4 h | The 3 company laptops; MSP reimages desktops |
| 3 | Customs platform access (SYS-01) | 4 h (vendor RTO 8 h) | Vendor-hosted; standby broker for urgent entries |
| 4 | Email (SYS-02) | 4 h | Phone; temporary mailbox on a clean device |
| 5 | Banking (SYS-04) | 8 h | Owner releases urgent wires after call-back |
| 6 | Carrier and terminal portals (SYS-09) | 8 h | Carrier sales offices by phone |
| 7 | Accounting (SYS-03) | 48 h | Queue invoices |
| 8 | Client Records Archive restore (SYS-08 to SYS-02) | 48 h | Request copies from clients or the customs platform's document store |
