# Business Impact Analysis: Cris Santos Company | Critical Manufacturing | Small

**Organization:** Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) | **Tier:** Small (200 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager and Controls Engineer with the process owners, 2026-07-13 to 2026-07-22 | **Approved:** VP Operations, 2026-09-04

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data each can lose. It covers all 10 business processes, office and plant floor. It feeds:
- the availability rating in the SSP for the ERP and Production Scheduling Platform (P02);
- the impact ratings in the risk register (P01);
- the recovery objectives in the cloud control map (P04);
- the recovery order and the manual production procedures in the ransomware runbook (P08);
- the contingency plan and OT recovery procedures that the company does not yet have (P03 G-059, P07 POA&M).

No law requires this company to have a contingency plan. The BIA supports the CSF 2.0 benchmark (ID.AM-05, RC.RP-02) and the delivery commitments in utility supply agreements and the federal contract.

## 2. System and business description
The company builds liquid-filled distribution and power transformers for 38 Southeast utilities and one federal site, on one Florida campus with two production shifts. Revenue is $84 million a year, about $336,000 of shipments per production day. Utilities place emergency storm-restoration orders each hurricane season, and the company reserves production slots for them.

Work flows from the ERP and APS (SYS-01) through the integration service (SYS-03) to the MES and shop-floor kiosks (SYS-05), then to the plant control systems (SYS-06) and the high-voltage test bay (SYS-07). Designs live in the PLM vault (SYS-04). See `../scenario-facts.md` sections 3 and 4 and the SSP (P02).

## 3. Impact categories and values
Dollar values are scaled to $84 million in annual revenue (about $336,000 per production day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1,000,000 (about 3 production days of shipments) | $250,000 to $1,000,000 | Less than $250,000 |
| Operations | Bay A or Bay B stops, or storm-restoration orders slip | One work center or one support function stops | Staff slowed but working |
| Regulatory and contractual | Missed utility addendum notice, a certified test report whose data integrity is in doubt, or a federal contract issue | Missed contractual deliverable date or record-keeping requirement | Internal policy deviation |
| Safety | Plausible worker injury (heat, vacuum, hot oil, high voltage) or an unsafe product shipped | Safety control degraded, manual safeguards in use | None |
| Reputation | A utility suspends a supply agreement, or regional media coverage during a storm response | Customer complaints or a supplier scorecard downgrade | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Production scheduling and work order release | High | 48 h | 24 h | 4 h |
| BP-02 Core cutting and coil winding | High | 72 h | 48 h | 24 h |
| BP-03 Drying and oil processing | High | 24 h | 12 h | 24 h |
| BP-04 Tank fabrication and welding | Moderate | 120 h | 72 h | 24 h |
| BP-05 Final assembly, high-voltage testing, and certified test reports | High | 48 h | 24 h | 1 h |
| BP-06 Order entry, quoting, and design engineering | Moderate | 72 h | 48 h | 24 h |
| BP-07 Procurement, inventory, and supplier EDI | Moderate | 72 h | 48 h | 4 h |
| BP-08 Shipping and logistics | Moderate | 72 h | 48 h | 4 h |
| BP-09 Field service, TMU support, and storm response | Moderate | 48 h | 24 h | 24 h |
| BP-10 Finance, billing, payroll, and HR | Low | 120 h | 72 h | 24 h |

Totals: 4 High, 5 Moderate, 1 Low.

**What drives the values:**
- **Safety drives BP-03.** Every transformer passes through the drying ovens and the vacuum oil fill station. An interrupted drying cycle must restart, and a control system whose integrity is in doubt creates heat, vacuum, and hot oil hazards. Its 12-hour RTO is the shortest in the plant.
- **Product integrity drives BP-05.** No transformer ships without a certified test report signed by Quality. The 1-hour RPO reflects that losing test data means repeating tests that take hours.
- **Work-in-process buffers set the plant MTDs.** The MES holds about 2 shifts of released work orders (BP-01, 48 hours). About 3 days of cut cores and wound coils sit ahead of assembly (BP-02, 72 hours). The tank shop runs about a week ahead (BP-04, 120 hours).
- **Contract duties keep running during an outage.** BP-09 is rated Severe for regulatory and contractual impact because the 48-hour incident notice and the 1-business-day access notice under the utility addenda do not pause while systems are down.

**Key findings:**
1. **No backup has ever been restore-tested.** The 24-hour RTO for BP-01 relies on the ERP database point-in-time restore, and those backups sit in the same cloud account and region as production (P01 R-002).
2. **The 12-hour RTO for BP-03 cannot be met today if a PLC or HMI must be rebuilt.** Oven programs and recipes exist only as ad hoc copies on the Controls Engineer's laptop (P01 R-021). The ovens can run stored recipes from the local PLC, but only if the PLC itself is intact.
3. **There are no written manual production procedures.** The paper traveler kit and the printed 5-day schedule in the BP-01 and BP-02 workarounds are described by the process owners but not documented or exercised (P03 G-059, P08).
4. **The MES is a single point of failure between the office and the plant.** It serves BP-01, BP-02, BP-04, and BP-05, and it is dual-homed on both networks, so an office incident can take it down with the plant (P01 R-001).

## 5. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 ERP and APS (cloud tenant) | Orders, bills of materials, purchasing, inventory, shipping, finance, finite-capacity schedule, export screening records | BP-01, BP-06, BP-07, BP-08, BP-10 |
| SYS-02 Identity provider | Single sign-on and MFA for email, ERP, cloud console, and VPN | All office processes |
| SYS-03 Integration service | Work orders from the ERP to the MES and confirmations back; EDI exchange | BP-01, BP-07 |
| SYS-04 PLM vault and CAD workstations | Designs, electromagnetic calculations, winding specifications, customer drawings | BP-02, BP-06 |
| SYS-05 MES and 25 kiosks | Dispatch, electronic travelers, confirmations, test data collection | BP-01, BP-02, BP-04, BP-05 |
| SYS-06 Plant control systems | Core cutting lines, winding machines, ovens, oil fill, plasma cutter, weld cells, 18 HMI and engineering workstations | BP-02, BP-03, BP-04 |
| SYS-07 High-voltage test bay | Impulse, applied voltage, and loss measurement systems; 4 test PCs | BP-05 |
| SYS-08 Plant historian | Oven, winder, and test process records | BP-03, BP-05 |
| SYS-09 IT endpoints and network | 140 laptops and desktops, firewalls, site-to-site VPN, directory, file server, backup appliance | All |
| SYS-10 EDI network provider | Purchase orders, advance ship notices, invoices | BP-07, BP-08 |
| SYS-11 Productivity suite | Email, files, chat | BP-06, BP-07, BP-09, BP-10 |
| SYS-12 TMU firmware and configuration library | Firmware images, customer configurations, configuration tool | BP-05, BP-09 |
| Facilities | Plant server room, HQ server room, standby generators, Bays A and B, test bay | All plant processes |
| People | Controls Engineer (single OT expert), IT Manager, MSP, shift supervisors, test technicians, Quality Manager | All |

## 6. Recovery priorities
The order puts worker safety first, then the shared services everything else needs, then the processes with the shortest RTO.

| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-06 drying ovens and oil fill (BP-03): confirm safe state, run stored recipes from the local PLC | 12 h | Safe shutdown if HMI integrity is in doubt; reload verified PLC programs from the offline OT backup store (to be built; P01 R-021) |
| 2 | SYS-02 identity provider and break-glass accounts | 2 h | Two offline break-glass administrator accounts (to be created) |
| 3 | SYS-09 internet, firewalls, and VPN to the cloud tenant | 4 h | Second internet carrier (funded in P01 treatment plan); cellular hotspots for key staff |
| 4 | SYS-07 test bay PCs (BP-05) | 24 h | Test systems run offline and store results locally; Quality hand-signs reports from raw data printouts |
| 5 | SYS-01 ERP and APS (BP-01) | 24 h | Printed 5-day schedule; restore from backups in a separate account and region (to be built; P01 R-002) |
| 6 | SYS-05 MES and kiosks, rebuilt single-homed on the plant network | 24 h | Paper travelers from the traveler kit |
| 7 | SYS-03 integration service | 24 h | Manual work order release by the Production Planning Manager |
| 8 | SYS-12 TMU library and field laptops (BP-09) | 24 h | Verified offline copy on an encrypted drive held by the VP Engineering (known-good images with supplier hashes) |
| 9 | SYS-06 core cutting and winding HMIs (BP-02) | 48 h | Manual recipe entry from printed winding sheets with an engineering double-check |
| 10 | SYS-04 PLM vault (BP-06) | 48 h | Released drawings in the traveler kit; hold new designs |
| 11 | SYS-10 EDI connectivity (BP-07, BP-08) | 48 h | Phone and email orders to the top 10 suppliers; paper bills of lading |
| 12 | SYS-06 plasma cutter and weld cells (BP-04) | 72 h | Manual welding; outside tank fabricator |
| 13 | Payroll SaaS and ERP finance (BP-10) | 72 h | Repeat prior payroll through the payroll provider |

The recovery order is carried into the P08 runbook (Recover phase) and should be proved in the first restore tests (P07 POA&M).
