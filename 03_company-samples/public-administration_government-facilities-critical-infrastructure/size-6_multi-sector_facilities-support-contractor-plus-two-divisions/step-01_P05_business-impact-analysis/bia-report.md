# Business Impact Analysis: Cris Santos Company Holdings | Government Services and Facilities | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), the cloud platform and network (SYS-G3), payroll and finance (SYS-G4), and the Integrated Building Operations Platform (IBOP, SYS-G5).
- **Division BIAs:** Government Facilities Support (focus), Construction and Renovation, and Janitorial and Security Services. They are rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the contingency plans that state agency contracts require (SP 800-53 CP-2 under the Moderate baseline);
- building recovery (manual operation) procedures, which GSA requires at federal buildings (BTTRG v3.0 section 1.6.2) and the group extends to state, local, and education sites;
- the availability rating in the SSP (P02), impact ratings in the risk registers (P01), and the recovery order in the incident runbook (P08).

## 2. System and business description
Three divisions share corporate services. The one that matters most for this vertical is the **IBOP**, which hosts building automation supervision and access control administration for 296 state, local, and education sites, the central monitoring station for the Janitorial and Security division, and the commissioning workspace the Construction division uses before turnover. Division systems are SYS-F1 (CMMS), SYS-F2 (agency systems at federal buildings, outside the group's boundary), SYS-C1 to SYS-C3 (Construction), and SYS-J1 to SYS-J3 (Janitorial and Security). See `../00_company-facts.md` sections 3 and 7.

**A key property of building systems:** field controllers keep running their last programs and schedules, and door controllers cache credentials for up to 72 hours. Losing the IBOP does not stop the buildings at once. What stops first is **visibility** (alarms and video) and **change** (revocations, schedules). That is why alarm monitoring has the shortest MTDs in the group, while building automation supervision tolerates a day.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Facilities Support about $15 million per day, Construction about $26 million per day, and Janitorial and Security about $7.7 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (building operations, monitoring, project work) | One region, contract, or service stops | Staff slowed but working |
| Contract and regulatory | Missed legal or contract notice clock, default notice, loss of award eligibility (SPRS, CMMC, FAR 52.204-25), or SEC disclosure | Missed contract report or service credit | Internal deviation |
| Safety and physical security | People harmed or a government building left unsecured | Delayed response to a security or environmental alarm | None |
| Reputation | National media, loss of a state or federal customer, or regulator attention | Regional media or customer corrective action request | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 8 Facilities Support, 6 Construction, and 6 Janitorial and Security. 12 are High, 12 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G04 IBOP platform services | Group | High | 2 h | 1 h | 15 min |
| BP-JS01 Remote video and alarm monitoring | Janitorial and Security | High | 2 h | 1 h | 15 min |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and corporate network | Group | High | 4 h | 2 h | 1 h |
| BP-FS01 ROC alarm monitoring and dispatch | Facilities Support | High | 4 h | 2 h | 1 h |
| BP-FS07 Emergency response and hurricane operations | Facilities Support | High | 4 h | 2 h | 24 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-FS02 Access control administration | Facilities Support | High | 8 h | 4 h | 1 h |
| BP-FS04 Federal building operations and maintenance | Facilities Support | High | 24 h | 8 h | 24 h |
| BP-CN01 Project document control, RFIs, and submittals | Construction | High | 24 h | 8 h | 4 h |
| BP-JS03 Scheduling and time capture | Janitorial and Security | High | 24 h | 8 h | 4 h |
| BP-G05 Payroll and time processing | Group | High | 72 h | 24 h | 4 h |
| BP-FS03 Building automation supervision | Facilities Support | Moderate | 24 h | 12 h | 24 h |
| BP-CN03 Jobsite safety, access, and site monitoring | Construction | Moderate | 24 h | 8 h | 24 h |
| BP-JS02 Security officer post operations | Janitorial and Security | Moderate | 24 h | 8 h | 4 h |
| BP-CN02 DoD CUI project data | Construction | Moderate | 48 h | 24 h | 4 h |
| BP-CN05 Bid preparation and estimating | Construction | Moderate | 48 h | 24 h | 4 h |
| BP-FS05 Work orders and preventive maintenance | Facilities Support | Moderate | 72 h | 24 h | 4 h |
| BP-JS04 Hiring, background screening, and E-Verify | Janitorial and Security | Moderate | 72 h | 24 h | 24 h |
| BP-CN04 Commissioning and turnover | Construction | Moderate | 72 h | 24 h | 4 h |
| BP-FS06 Controller program engineering | Facilities Support | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Contract compliance reporting | Group | Moderate | 120 h | 72 h | 24 h |
| BP-CN06 Subcontractor payments and certified payroll | Construction | Moderate | 120 h | 72 h | 24 h |
| BP-FS08 Contract reporting and invoicing | Facilities Support | Low | 120 h | 72 h | 24 h |
| BP-JS05 Electronic security installation and service | Janitorial and Security | Low | 120 h | 72 h | 24 h |
| BP-JS06 Custodial operations and supply ordering | Janitorial and Security | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Physical security and safety** drive the monitoring processes (BP-JS01, BP-FS01) and the IBOP that hosts them. Monitoring contracts set alarm handling times in minutes, which is why BP-G04 has a 1-hour RTO and a 15-minute RPO even though controllers run locally.
- **Revocation integrity** drives BP-FS02's 1-hour RPO. A lost revocation leaves a former employee with access to a government building; county and university contracts require revocations within 4 hours.
- **Revenue and delay damages** drive Construction (BP-CN01). Field crews and about 1,900 subcontractors stop without current drawings.
- **Wage law and post coverage** drive payroll and scheduling (BP-G05, BP-JS03). About 37,000 hourly workers are paid weekly or biweekly; unpaid officers leave posts.
- **Legal clocks** drive the SOC (BP-G02) and contract compliance reporting (BP-G07): customer notices in 24 hours (12 hours under 9 county contracts), DoD in 72 hours, and FAR supply chain reports in business days.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops alarm consoles, revocations, and project documents at once. Break-glass accounts per critical system are the fallback |
| IBOP (SYS-G5) | Group | Facilities Support monitoring and access control; Janitorial and Security central monitoring; Construction commissioning | One platform outage or intrusion affects all three divisions and hundreds of customer contracts (P08) |
| ROC-2 | Group (shared facility) | Facilities Support ROC operators and the Janitorial and Security central monitoring station | A hurricane or facility loss at ROC-2 needs ROC-1 to absorb both workloads; tested in 2026-05 for Facilities Support only (P01 GR-09) |
| SOC facts (SYS-G2) | Group | Every customer notice, the DoD report, and SEC disclosure | Every notice clock in P08 depends on the SOC establishing what happened |
| Door schedules (BP-FS02) | Facilities Support | Janitorial and Security officers at 74 shared sites | Officers enforce the schedules the platform sets; a tampered schedule misleads the guard post too |
| Commissioning handover (BP-CN04) | Construction | Facilities Support (BP-FS03, BP-FS06) | Programs and drawings move into the operations repository at turnover; CUI drawings must not follow them (gap 5) |
| Gate officers (BP-JS02) | Janitorial and Security | Construction jobsites (BP-CN03) | Officers staff gates at 31 jobsites, using jobsite cameras that feed the IBOP |
| Time data (BP-JS03) | Janitorial and Security | Group payroll (BP-G05) | Payroll cannot run without time capture |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); ROC-2 hosting both monitoring workloads (P01 GR-09); one access control SaaS vendor for all 188 access control sites (P01 GR-08, accepted with contract terms and vendor SOC 2 review).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-G5 IBOP cloud services | BP-G04, BP-FS01 to BP-FS03, BP-JS01, BP-CN04 | Database replication to provider B every 15 minutes; daily immutable backups; failover tested for Facilities Support workloads only |
| Access control and video SaaS tenants | BP-FS02, BP-JS01 | Vendor replication (vendor SOC 2 states RTO 4 hours and RPO 15 minutes); weekly configuration exports by the group |
| Controller program repository | BP-FS06 | Versioned with hashes for 61% of sites; the rest only on technician laptops (P01 FS-007) |
| SYS-C1 and SYS-C2 | BP-CN01, BP-CN02 | Vendor and provider backups; SYS-C2 backups stay in the government community cloud |
| SYS-J1 workforce management | BP-JS03, BP-JS04 | Vendor backups; daily schedule export to branches |
| People | All | Two ROCs cross-trained for each other's alarms; regional storm teams |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and corporate network
3. IBOP platform services (monitoring module first, then access control administration, then supervision)
4. Remote video and alarm monitoring (central monitoring station)
5. ROC alarm monitoring and dispatch
6. SOC visibility (SIEM and EDR)
7. to 12. Emergency operations, access control administration, scheduling, project documents, federal building operations, and officer post operations
13. to 27. Building automation supervision, payroll, jobsite monitoring, CUI data, bidding, work orders, hiring, commissioning, controller programs, finance, compliance reporting, subcontractor payments, invoicing, installation services, and custodial ordering.

## 8. Key findings
1. **The IBOP is the group's most important shared dependency.** Its 1-hour RTO is set by the monitoring contracts, not by building automation. Failover to provider B has been tested for Facilities Support workloads, but **not for the central monitoring module** (P01 GR-09; POAM-014).
2. **ROC-2 is a shared single point of failure** for two divisions' monitoring. ROC-1 absorbed Facilities Support alarms in the 2026-05 exercise; the Janitorial and Security central monitoring station has never failed over to ROC-1.
3. **Restoring a tampered controller depends on the program repository**, which covers 61% of sites. At the other 39%, the 48-hour RTO for BP-FS06 is unproven (P01 FS-007).
4. **Building recovery procedures** exist for all 46 federal buildings and for 74% of state, local, and education sites. The rest are due by 2026-12-31 (POAM-016).
5. **Notification capacity is itself a process** (BP-G02, BP-G07). If the SOC or the contract management system is down during an incident, the 24-hour customer clocks keep running. The P08 runbook uses printed notice lists for this reason.
