# Business Impact Analysis: Cris Santos Company Holdings | Chemical | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level, with OT recovery guidance from NIST SP 800-82 Rev. 3
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads, the Group Process Safety Director, and the Group ERC manager | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity and the OT remote access gateway (SYS-G1), the SOC and OT desk (SYS-G2), cloud and WAN (SYS-G3), the ERP that produces every division's hazmat shipping papers (SYS-G4), and the 24x7 Group Emergency Response Center (ERC).
- **Division BIAs:** Specialty Chemicals (focus, with Plant C1 in detail), Distribution, and Hazmat Transport. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Plant C1 emergency response program and the release notification path (40 CFR 68.95; 40 CFR 302.6; 40 CFR 355.40 to 355.43);
- the Terminal T1 Facility Security Plan and the backup requirement in the USCG cyber rule (33 CFR 101.650(g)(4));
- the emergency response telephone duty on shipping papers (49 CFR 172.604);
- the availability commitments the managed inventory service will make in its first SOC 2 report (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services SYS-G1 to SYS-G7. Division systems are SYS-C1 to SYS-C9 (Specialty Chemicals: the Plant C1 control systems, the other 15 plants, the LIMS, the central engineering hub, and the AI-001 service), SYS-D1 to SYS-D4 (Distribution: Terminal T1 automation, branches, the managed inventory service, and terminal access control), and SYS-T1 to SYS-T4 (Hazmat Transport: TMS, telematics and ELDs, driver records, and maintenance records). See `../00_company-facts.md` sections 3 and 7.

**What makes this BIA different from an IT-only BIA.** At a chemical plant the worst outcome of an outage is not lost revenue. It is losing the ability to see and control a toxic inventory. Plant C1 can hold 360,000 lb of chlorine on its unloading manifold. The BIA therefore separates the **safety functions** that must never wait (the SIS, gas detection, release notification, the ERC number) from the **production functions** that can stop safely and restart later.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Specialty Chemicals about $31.2 million per day, Distribution about $15.3 million per day of third-party sales, and Hazmat Transport about $2.7 million per day of third-party revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot make, store, or move product, or a water utility customer runs out of treatment chemical | One plant, terminal, or region stops | Staff slowed but working |
| Regulatory | Missed release notice, an MTSA security plan measure not maintained, a hazmat shipment without valid shipping papers or a monitored emergency number, or SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible toxic release, fire, or harm to workers, responders, or the public; loss of en route security for a hazmat load | Degraded safeguards with compensating measures in place | None |
| Reputation | National media, regulator attention, or loss of utility or major customers | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 33 processes: 11 group shared services, 10 Specialty Chemicals, 6 Distribution, and 6 Hazmat Transport. 17 are High, 13 Moderate, and 3 Low. The table is in recovery priority order.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-SC02 Safety instrumented functions and chlorine gas detection at Plant C1 | Specialty Chemicals | High | 2 h | 1 h | 24 h |
| BP-SC09 Release notification and emergency response coordination | Specialty Chemicals | High | 1 h | 15 min | 24 h |
| BP-G06 Emergency response telephone service (Group ERC) | Group | High | 1 h | 30 min | 24 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G04 Cloud landing zones, WAN, and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G03 Security monitoring, incident response, and the OT desk | Group | High | 8 h | 4 h | 1 h |
| BP-HT03 En route security monitoring of hazmat loads | Hazmat Transport | High | 4 h | 2 h | 1 h |
| BP-SC01 Plant C1 chlorine unloading and hypochlorite production | Specialty Chemicals | High | 48 h | 24 h | 1 h |
| BP-SC04 Plant C1 tank farm, loading rack, and outbound shipping | Specialty Chemicals | High | 24 h | 12 h | 1 h |
| BP-DS04 Managed inventory service (telemetry and automatic replenishment) | Distribution | High | 24 h | 8 h | 1 h |
| BP-DS01 Terminal T1 marine transfers and bulk tank storage | Distribution | High | 24 h | 12 h | 1 h |
| BP-DS02 Terminal T1 truck and rail loading racks | Distribution | High | 24 h | 12 h | 1 h |
| BP-G05 ERP order-to-cash, inventory, and hazmat shipping paper data | Group | High | 24 h | 8 h | 1 h |
| BP-HT01 Dispatch, load planning, and electronic shipping papers | Hazmat Transport | High | 12 h | 4 h | 1 h |
| BP-SC07 Production at the other 15 Specialty Chemicals plants | Specialty Chemicals | High | 48 h | 24 h | 4 h |
| BP-SC03 Batch execution and recipe management | Specialty Chemicals | High | 48 h | 24 h | 4 h |
| BP-DS06 Terminal T1 access control and CCTV | Distribution | Moderate | 8 h | 4 h | 24 h |
| BP-DS03 Branch warehousing, repackaging, and order fulfillment | Distribution | High | 48 h | 24 h | 4 h |
| BP-HT02 Hours of service and ELD records | Hazmat Transport | Moderate | 72 h | 24 h | 1 h |
| BP-G09 Email, files, and chat | Group | Moderate | 24 h | 8 h | 4 h |
| BP-SC05 Quality release and certificates of analysis | Specialty Chemicals | Moderate | 48 h | 24 h | 4 h |
| BP-DS05 Customer portal (orders, SDS, certificates) | Distribution | Moderate | 48 h | 24 h | 4 h |
| BP-HT06 Customer load tracking and freight billing | Hazmat Transport | Moderate | 48 h | 24 h | 4 h |
| BP-SC08 Central process control engineering and configuration repositories | Specialty Chemicals | Moderate | 72 h | 48 h | 24 h |
| BP-SC06 Process historian and OT DMZ at Plant C1 | Specialty Chemicals | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Product stewardship and SDS authoring | Group | Moderate | 72 h | 24 h | 24 h |
| BP-HT05 Fleet maintenance and cargo tank inspection records | Hazmat Transport | Moderate | 72 h | 48 h | 24 h |
| BP-G02 OT remote access gateway | Group | Moderate | 72 h | 24 h | 24 h |
| BP-G10 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G11 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-HT04 Driver qualification and drug and alcohol testing records | Hazmat Transport | Low | 120 h | 72 h | 24 h |
| BP-G08 Group data platform and process analytics | Group | Low | 168 h | 72 h | 24 h |
| BP-SC10 AI-001 process-optimization advisory | Specialty Chemicals | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Life safety and release response** drive the first three rows. The SIS and gas detection run on their own network and power, so they do not wait for any group service. Release notices are due immediately (40 CFR 302.6(a); 355.43(a)), and the ERC number must be monitored whenever a group hazmat shipment is in transportation (49 CFR 172.604(a)(1)). The RPO of 24 hours for these rows covers reference data (the approved SIS program, call lists, and product hazard data), not transactions.
- **Water utility supply** drives Plant C1 production (BP-SC01, BP-SC04) and the managed inventory service (BP-DS04). Utilities hold 7 to 14 days of hypochlorite, so Plant C1 itself can stop for 48 hours. But a utility whose automatic replenishment fails may not notice until a tank is low, which is why BP-DS04 has the shorter RTO (8 hours).
- **Hazmat transport rules** drive dispatch and en route security (BP-HT01, BP-HT03). A load cannot move without shipping papers, and the carrier security plan relies on telematics alerts for large bulk quantities of hydrogen peroxide and Class 3 solvents.
- **MTSA security** drives Terminal T1 access control (BP-DS06). It is Moderate only because guards can check TWICs by hand while the system is down.
- **Revenue more than time** drives branches, billing, LIMS, and finance. Customers hold stock and certificates can be issued by hand.
- **Plant C1 control systems use RPO differently.** For the DCS, SIS, and recipes, the recovery point is the last **approved** configuration or recipe, not the last backup. Restoring a newer but unverified copy could restore an attacker's change (P08).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| ERP shipping paper data (SYS-G4) | Group | Every hazmat shipment of all three divisions | One ERP outage stops order release and shipping papers everywhere at once. Pre-printed papers for the top 500 products are the fallback (P08 scenario) |
| Group ERC number (SYS-G7 and telephony) | Group | Shipping papers of all three divisions | One number for every group shipment; the backup ERC site is tested twice a year |
| OT remote access gateway (SYS-G1) | Group | 16 plants and Terminal T1 | Moderate for availability but carries the top group risk: one stolen integrator credential can reach many sites (P01 GR-01) |
| Central engineering hub (SYS-C8) | Specialty Chemicals | All 16 plants | Source of clean configuration and recipe copies for a cyber restore, and also a standing path into every plant |
| Plant C1 hypochlorite | Specialty Chemicals | Distribution managed inventory customers (about 640 utilities) | About 30% of division volume is sold through Distribution |
| Hazmat Transport capacity | Hazmat Transport | Specialty Chemicals and Distribution | About 55% of the two divisions' bulk outbound loads |
| Terminal T1 raw materials | Distribution | Specialty Chemicals plants | Caustic soda and solvents for production |
| SOC facts (SYS-G2) | Group | Every notice in P08 | Release notices do not wait for the SOC, but breach, SEC, and Coast Guard reporting depend on what the SOC establishes |

**Single points of failure found:**
1. **ERP shipping paper data** for all three divisions (P01 GR-03). The pre-printed paper fallback covers 500 products, not all 11,000.
2. **The central engineering hub** is the only source of verified recipe masters for the 15 plants other than Plant C1 (P01 SC-002).
3. **One chlorine rail supplier** for Plant C1 (accepted; supply contract has a second origin plant).
4. **The Group ERC** is mitigated by a tested backup site and automatic call routing.

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SIS program and gas detection configuration | BP-SC02 | Approved program copy held offline by Controls Engineering; checksum recorded at each proof test |
| Plant C1 DCS and batch configuration | BP-SC01, BP-SC03, BP-SC04 | Weekly configuration export to an offline, write-protected copy at the plant and to SYS-C8; restore tested at the 2026-08-12 turnaround (P07 CP-9) |
| Recipe library (SYS-C8) | BP-SC03, BP-SC07 | Versioned repository; nightly copy to the immutable vault in provider B |
| Legacy plant control systems (SYS-C6) | BP-SC07 | **Not reliable.** No tested backups at 5 of the 7 legacy plants (P01 SC-004) |
| SYS-G1, SYS-G3, SYS-G4 integration services | IT processes | Vendor multi-region services; infrastructure as code; immutable backups in provider B |
| SYS-D1 Terminal T1 automation | BP-DS01, BP-DS02 | Nightly configuration backup on site; offline copy monthly (USCG 101.650(g)(4) test frequency not yet defined, P03) |
| SYS-D3 managed inventory platform | BP-DS04, BP-DS05 | Database replicas and a warm standby region in provider A |
| SYS-T1 TMS and SYS-T2 telematics (vendor SaaS) | BP-HT01 to BP-HT03 | Vendor replication per contract; daily export of open loads |
| People | All | Cross-trained operators; ERC backup site staff; on-call integrators for on-site work |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. to 3. **Safety first:** SIS and gas detection at Plant C1, release notification, and the Group ERC. None of these depends on IT recovery.
4. to 6. Identity, cloud and WAN, and SOC visibility.
7. En route security monitoring of hazmat loads already on the road.
8. to 12. Plant C1 production and loading, the managed inventory service, and Terminal T1 transfers and racks.
13. and 14. ERP and Hazmat Transport dispatch (shipping papers).
15. to 33. Other plants, recipes, Terminal T1 access control, branches, ELDs, email, quality, portal, billing, the engineering hub, historian, SDS authoring, maintenance records, the OT remote access gateway, finance, HR, driver records, the data platform, and AI-001.

**Safety gates come before speed.** A plant or terminal control system restored after a cyber incident restarts only after a pre-startup review confirms setpoints, alarm limits, interlocks, and recipes against the process safety information (P08 section 8). The OT remote access gateway is restored near the end, and only after every integrator account has been re-issued.

## 8. Key findings
1. **Safety functions do not depend on IT, and that is by design.** The SIS, gas detection, and release notification work with the business network down. The 2025-10-08 field exercise confirmed the notification path; the 2026 notification exercise will run with the business network simulated down (P07 CP-4).
2. **The ERP is the hidden single point of failure for hazmat shipping.** Every division's shipping papers come from ERP product data. The P08 scenario uses exactly this dependency.
3. **The OT remote access gateway is Moderate for availability and the top risk for integrity.** Its recovery can wait; its protection cannot (P02, P01 GR-01).
4. **Legacy plant RTOs are unproven.** Five of the 7 legacy plants have no tested OT backups, so the 24-hour RTO for BP-SC07 is a target, not a capability (P01 SC-004; POAM in P07).
5. **Water utilities connect two divisions' outages into a public health issue.** A combined outage of Plant C1 and the managed inventory service longer than about a week could leave utilities short of disinfectant. The P08 recovery order puts both ahead of branch and billing systems.
