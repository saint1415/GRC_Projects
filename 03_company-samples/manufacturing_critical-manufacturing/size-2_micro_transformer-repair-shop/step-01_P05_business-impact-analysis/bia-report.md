# Business Impact Analysis: Cris Santos Company | Critical Manufacturing | Micro

**Organization:** Cris Santos Company, LLC (transformer repair and remanufacturing shop, Florida) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Security Coordinator) with the Owner, the Shop Manager, the Field Service and Test Technician, the Lead Winder, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** Owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the shop, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Availability criteria in the SOC 2 self-assessment (P09).

No regulation requires this shop to keep a contingency plan. The drivers are business ones: utilities buy rebuilt transformers from stock to restore power after storms, the federal purchase order and utility orders require a test report with every unit, and the G&T cooperative's Vendor Cyber Security Exhibit expects coordinated response to incidents. The CSF 2.0 benchmark (P03) covers this under GV.OC-04, ID.IM-04, and RC.RP-02.

**Values are rated for hurricane season** (June 1 to November 30), the worst case. Outside the season, most MTDs could double.

## 2. System and business description
One leased building in Florida with 7 employees, repairing and remanufacturing about 35 distribution transformers a month. Office work runs on SaaS: the job-shop ERP with its scheduling board (SYS-01) and the productivity suite (SYS-02), backed up by the MSP (SYS-08). On site are 6 computers and 2 tablets (SYS-03), one flat network (SYS-04), the test bay and its test PC (SYS-05), the vacuum drying oven and oil rig (SYS-06), and the coil winding machine (SYS-07). The MSP runs IT; the oven OEM and the test set vendor support their equipment. See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,200 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $12,000 (about 3 working days) or a lost storm order | $4,000 to $12,000 | Less than $4,000 |
| Operations | No units can be built, tested, or shipped | One function stops; output slowed | Staff slowed but working |
| Regulatory and contractual | Missed federal delivery, missed cooperative exhibit notice, or breach notice duty | Late report or record to a customer | Internal policy deviation |
| Safety | Oven or test bay operated outside safe limits; a unit ships without valid tests | Work stopped safely with some risk during shutdown | None |
| Reputation | A utility cannot restore customers because the shop cannot ship, or the cooperative suspends the shop as a vendor | Customer complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Job scheduling and work orders | High | 24 h | 8 h | 4 h |
| BP-02 Repair and rewind production | High | 48 h | 24 h | 24 h |
| BP-03 Vacuum drying and oil processing | High | 24 h | 12 h | 168 h |
| BP-04 Final testing and test reports | High | 24 h | 8 h | 24 h |
| BP-05 Shipping, storm-stock sales, and customer communication | High | 24 h | 8 h | 4 h |
| BP-06 Field service and oil sampling | Moderate | 72 h | 24 h | 24 h |
| BP-07 Purchasing and receiving | Moderate | 72 h | 48 h | 24 h |
| BP-08 Billing, payroll, and bookkeeping | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Testing (BP-04) is the bottleneck.** Every unit ships with a test report from the test PC. If the test PC is down, nothing ships, including storm stock that is already built.
- **Storm demand sets the 24-hour MTDs** for scheduling, testing, and shipping. After a hurricane, utilities buy from whichever shop can ship first.
- **Safety drives BP-03.** A drying cycle in progress must be finished or stopped safely, and units cannot be filled with oil until they are dried.
- **Billing (BP-08) tolerates 5 days** because payroll runs through an outside service and the shop holds a cash reserve of about 45 days.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 ERP (SaaS) | Jobs, schedule board, inventory, purchasing, invoicing, accounting, customer portal | ERP vendor's backups (SOC 2 report states RTO 8 h, RPO 1 h; see P09). **The shop holds no export of its own data** | BP-01, BP-05, BP-07, BP-08 |
| SYS-02 Productivity suite (SaaS) | Email, shared drive (rewind data sheet library, test report copies, FCI, HR files) | Vendor resilience; daily SaaS-to-SaaS backup (SYS-08), 1-year retention. **Never restore-tested** | BP-02, BP-05, BP-06, BP-08 |
| SYS-03 Endpoints | 3 desktops, 2 laptops, shop-floor PC, 2 tablets | No local data by design except unsynced desktop files; MSP reimages | All |
| SYS-04 Network and internet | Firewall, one Wi-Fi network, one cable line | MSP holds the firewall configuration; phone hotspots as a fallback | All SaaS functions |
| SYS-05 Test PC and test set | Unsupported operating system; vendor software; local test database | **No backup.** Reinstall needs the vendor's media and license key, which the shop has not located | BP-04 |
| SYS-06 Drying oven PLC and HMI | Recipes only in the PLC; OEM cellular modem | **No copy of recipes or HMI project.** OEM can reload from its records (not confirmed) | BP-03 |
| SYS-07 Winding machine | Programs on USB sticks | Lead Winder's USB stick; partial copies in the shared drive | BP-02 |
| People | Owner, Office Manager, Shop Manager, Lead Winder, 2 Repair Technicians, Field Service and Test Technician | Cross-training: the Shop Manager can run tests; the Owner can quote and ship; only the Lead Winder knows the winding machine well | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| ERP vendor | BP-01, BP-05, BP-07, BP-08 | SOC 2 Type 2 report reviewed 2026-08-20 (P09); RTO 8 h and RPO 1 h meet this BIA |
| MSP | Recovery of every managed computer, the network, and the suite backup | No written recovery commitment; contract has only a 4-business-hour response time |
| Productivity suite vendor | BP-02, BP-05, BP-06, BP-08 | Vendor service commitments (standard terms) |
| Test set vendor | BP-04 (software reinstall, license, calibration) | None. Support by phone in business hours only |
| Drying oven OEM | BP-03 (controls support, recipe reload) | None. Remote support through its own modem; no written terms |
| Internet provider | Every SaaS function | None; single line |
| Payroll service | BP-08 | Vendor service commitments |

**Key findings:**
1. **The test PC can stop the business.** It has no backup, an unsupported operating system, and no known reinstall path. A realistic rebuild today is 3 to 5 days against an RTO of 8 hours (risk R-002). Every shipment depends on it.
2. **The ERP vendor meets the BIA**, but the shop holds no copy of its own data. If the ERP account were deleted or the vendor failed, jobs, inventory, and receivables would be lost (risk R-011). Fix: the vendor's scheduled full export to the shop's shared drive.
3. **OT recovery depends on vendors.** Oven recipes and the HMI project exist only in the PLC, and winding programs sit on USB sticks (risk R-014).
4. **The internet line is a single point of failure** for scheduling, shipping, and email (risk R-013).
5. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time (risk R-009).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Shop safety: oven and test bay in a safe state (SYS-06, SYS-05) | Immediate | Stop or finish cycles locally; de-energize the test bay |
| 2 | Internet and network (SYS-04) | 2 h | Phone hotspots for the Owner's and Office Manager's laptops; cellular failover router once installed (R-013) |
| 3 | Clean office endpoints (SYS-03) | 4 h | Laptops checked by the MSP; desktops reimaged |
| 4 | Test PC and test set (SYS-05) | 8 h target; 3 to 5 days today | Paper test forms and a report template on a clean laptop, signed by the Shop Manager |
| 5 | ERP access (SYS-01) | 8 h | Vendor-hosted; confirm the shop's accounts are clean; printed schedule and stock list until then |
| 6 | Email and shared drive (SYS-02) | 8 h | Owner's cell phone for customer calls; printed rewind data sheets in the bay binder |
| 7 | Drying oven controls (SYS-06) | 12 h | Local HMI only with the modem unplugged; OEM printed recipe sheet |
| 8 | Winding machine programs (SYS-07) | 24 h | Lead Winder's USB stick |
| 9 | Field service tools (field laptop, SYS-10) | 24 h | Paper field forms |
| 10 | Billing and payroll | 72 h | Payroll service repeats the prior payroll |
