# Business Impact Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Micro

**Organization:** Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Security Coordinator) with the Owner and General Manager, the Irrigation and Equipment Technician, the Field Supervisor, and the MSP technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner and General Manager, 2026-08-31
**Sources:** process owner interviews 2026-07-20 to 2026-07-23 (EV-040), FY2025 accounts with receipts by crop, harvest-day value and cash (EV-028), the grower agreement (EV-024), the Technician's intake interview (EV-035), the backup job report (EV-015), the MSP service contract (EV-017), the irrigation dealer's agreement and reply (EV-018, EV-020), and the FMIS vendor SOC 2 report (EV-052). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the Owner and General Manager.

## 1. Overview and purpose
This BIA lists every business function of the farm, how long each can be down, and how much data each can lose. It supports:
- the availability rating of the Farm Management and Irrigation Control Platform (FMICP) in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08);
- CSF 2.0 subcategories ID.AM-05 (assets prioritized by criticality) and RC.RP-01 to RC.RP-03 in the gap analysis (P03).

No law requires this farm to have a contingency plan. The drivers are the crop itself, the record duties of the Produce Safety Rule and the H-2A program, and the packer-shipper's grower agreement.

## 2. System and business description
The farm grows watermelons, peanuts, and cotton on about 420 acres in two parcels, with 7 employees and about $1.1 million in receipts. Watermelons bring about 40% of receipts in an 8-week harvest from late May to mid-July. Field work, irrigation, and records run on the FMICP: the farm management software with its irrigation module (SYS-01), the productivity suite (SYS-02), 8 devices (SYS-03), the shop network (SYS-04), the pump station and pivots (SYS-05), and the MSP-run cloud backup (SYS-08). See the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

**What is different about a farm:** the largest losses come from **time-critical physical work**, not from data. A day without water on drip-irrigated watermelons in a hot, dry spell, or a day of ripe fruit left unharvested, cannot be made up later. Every High process therefore has a manual workaround, and the real question is how long people can keep it up. At this farm one person knows how to run the irrigation by hand.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts and about $9,000 per watermelon harvest day (EV-028).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (about 3 harvest days, or loss of a watermelon field) | $5,000 to $25,000 | Less than $5,000 |
| Operations | Irrigation or harvest stops on a whole parcel | One crop, crew, or delivery slowed or stopped | Staff slowed but working |
| Regulatory | Produce Safety or H-2A records cannot be produced or are unreliable; water permit exceedance; reportable breach | Late or incomplete record that can be corrected | Internal procedure deviation |
| Safety | Worker injury or chemical exposure (fertigation or spray equipment misbehaving) | Unsafe condition caught before harm | None |
| Reputation | Loss of the packer-shipper's grower agreement or local media coverage | Buyer complaint or escalation | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Irrigation and fertigation | High | 24 h | 8 h | 24 h |
| BP-02 Watermelon harvest and load dispatch | High | 24 h | 8 h | 24 h |
| BP-03 Daily hours and Produce Safety records | High | 48 h | 24 h | 4 h |
| BP-04 Peanut and cotton harvest and delivery | Moderate | 72 h | 48 h | 24 h |
| BP-05 Precision field operations | Moderate | 72 h | 48 h | 168 h |
| BP-06 Payroll, H-2A records, and HR | Moderate | 72 h | 48 h | 24 h |
| BP-07 Accounting, USDA programs, crop insurance, and water use reporting | Low | 240 h | 120 h | 24 h |
| BP-08 Crop scouting, drone imagery, and yield forecasting | Low | 168 h | 120 h | 168 h |

Counts: 3 High, 3 Moderate, 2 Low.

**What drives the values:**
- **BP-01 (irrigation):** the 24-hour MTD assumes the Irrigation and Equipment Technician runs pumps and pivots by hand. Hand operation of 5 pivots on two parcels 9 miles apart, plus the pump station, needs two people and cannot be kept up for more than a few days. If the Technician is away, nobody else has done it.
- **BP-02 (harvest):** ripe watermelons left in the field lose value within a day or two, and the packer-shipper plans trucks against committed loads. The grower agreement requires notice within 24 hours of anything that affects traceability or committed loads.
- **BP-03 (records):** regulation, not revenue, drives this. Daily hours are part of the H-2A earnings record (20 CFR 655.122(j)(1)), and Produce Safety records must be created at the time of the activity (21 CFR 112.161(a)(2)). The 4-hour RPO reflects that a lost morning of entries cannot be honestly re-created. Paper forms keep the records going during an outage.
- **BP-06 (payroll):** H-2A workers must receive an earnings statement on or before each payday (20 CFR 655.122(k)). The payroll service can repeat the prior week's run, so the farm tolerates 72 hours.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 FMIS (SaaS) | Field, labor, food safety, and application records; harvest log; irrigation module | Vendor backups (SOC 2 report states RPO 1 hour, EV-052; see P09). **No farm-held export ever made** (EV-006) | BP-01, BP-02, BP-03, BP-04, BP-05 |
| SYS-02 Productivity suite (SaaS) | Email; the Office folder with payroll exports and H-2A files | Vendor resilience; copied nightly to SYS-08 | BP-02, BP-06, BP-07 |
| SYS-08 Cloud backup (MSP-operated) | Nightly copy of mailboxes and the Office folder, 30 days of versions | **Never restore-tested** (EV-015) | BP-06, BP-07 |
| SYS-05 Irrigation OT | Pump station controller, pivot panels, probes, flow meters | Controller keeps running its last program; **the program is held only by the irrigation dealer** (EV-020) | BP-01 |
| SYS-04 Shop network and internet | Firewall, Wi-Fi, pump station bridge, one internet line | Firewall configuration backed up by the MSP | BP-01 (pump station alarms), BP-06, BP-07 |
| SYS-03 Endpoints | 1 desktop, 2 laptops, 2 tablets, 3 phones | Office computers rebuilt by the MSP; phones work on cellular | All |
| SYS-06 Telematics and guidance | Tractor displays, RTK subscription, dealer portal | Guidance lines stored on the displays | BP-04, BP-05 |
| SYS-10 Accounting and payroll (SaaS) | Payroll service, accounting, H-2A filing agent portal | Vendor-hosted | BP-06, BP-07 |
| People | Irrigation and Equipment Technician (only person who can run irrigation by hand), Field Supervisor (records), Office Manager (payroll) | Cross-training planned (POAM-004) | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| FMIS vendor (with the pivot manufacturer's connectivity service behind it) | BP-01 remote control, BP-02, BP-03 | SOC 2 Type 2 report received 2026-08-18: stated RTO 8 hours and RPO 1 hour (EV-052; P09). The RTO equals the BP-01 and BP-02 RTOs, so hand operation and paper carry the first hours of any vendor outage |
| Irrigation dealer | Rebuilding or reprogramming the pump station controller | None. Time-and-materials agreement with no response time (EV-018); the only copy of the controller program is on the dealer's laptop (EV-020) |
| MSP | Recovery of the office computers and the cloud backup | No written recovery commitment; the contract has only a 4-business-hour response time (EV-017) |
| Packer-shipper | BP-02 (it sends the harvest crew and trucks) | Not an IT dependency; phone contact works without systems |
| Payroll service | BP-06 | Vendor-hosted; can repeat the prior payroll |
| Cellular carrier and internet provider | Pivot remote control (cellular); office work (one fixed-wireless line) | None; no failover for the office line (EV-033) |

**Key findings:**
1. **Irrigation recovery depends on one person and one dealer.** Only the Irrigation and Equipment Technician has run the system by hand, and only the irrigation dealer holds the pump station program (risks R-007 and R-004).
2. **The backups are unproven.** SYS-08 has never been restore-tested and SYS-01 has never been exported, so the RPOs for BP-03 and BP-06 rest on assumptions (R-004).
3. **The FMIS vendor meets the RPO but leaves no margin on the RTO.** Its stated 8-hour RTO equals the targets for BP-01 and BP-02. Hand operation and paper forms must cover any outage.
4. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. A contract amendment is in P01 (R-021).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Hand operation of irrigation (people, not systems) | Immediate | Hand operation at each panel; fertigation off; written procedure and a second trained person by 2027-02-28 (POAM-004) |
| 2 | Productivity suite and SYS-01 administrator access from a clean device | 2 h | Owner and General Manager's phone; new passwords; MFA re-registered |
| 3 | SYS-01 irrigation module and harvest log | 8 h | Vendor-hosted; paper harvest log and load tickets |
| 4 | Pump station controller | 8 h | Controller runs its last program in local control; dealer reloads a farm-held copy of the program (to be created, POAM-003) |
| 5 | Field tablet and phones for daily hours and Produce Safety records | 24 h | Paper daily hours sheets and paper Produce Safety forms |
| 6 | Office desktop and laptops | 48 h | MSP rebuilds; payroll service portal from a clean phone or laptop |
| 7 | Payroll and the Office folder | 48 h | Repeat prior payroll; restore the Office folder from SYS-08 |
| 8 | Telematics, guidance, drone, and SYS-09 | 48 to 120 h | Manual steering; hand counts |

## 7. Approval
Approved by the Owner and General Manager on 2026-08-31. Review each January before the watermelon season, or after a major change such as new irrigation automation.
