# Business Impact Analysis: Cris Santos Company | Dams | Mid-Market

**Organization:** Cris Santos Company, Inc. (owner and operator of 4 FERC-licensed hydroelectric projects, with Hydro Services) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** vCISO and GRC Manager with the Vice President of Generation Operations, the Chief Dam Safety Engineer, the ROC Manager, and the process owners named in `bia.csv` | **Fieldwork:** 2026-06-29 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: Generation Operations (the Remote Operations Center and 4 projects), Dam Safety, Hydro Services (field services and Remote Monitoring and Operations Services, RMOS), Recreation and Lands, Corporate Security, License and NERC compliance, Data Analytics, and corporate functions. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and public safety.

The results feed:
- the Rapid Recovery of Essential Services sub-element of the Blackwater Bend (Group 1) Security Plan and the Internal Emergency Response sub-elements for Blackwater Bend, Cedar Shoals, and Pine Hollow (FERC Security Program Rev. 3A 7.4.1 and 7.4.2);
- the Section 9 baseline measure "plan and prepare for the restoration and recovery of control systems" with annual testing (Rev. 3A Table 9.3a) and Form 3 Question 20 (identify essential systems and processes);
- the CIP-012-2 R1 Parts 1.2 and 1.3 methods for loss and recovery of the ICCP link (BP-05);
- the FIPS 199 availability ratings and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability commitments in the RMOS SOC 2 readiness work (P09).

## 2. System and business description
The company owns and operates 4 hydroelectric projects in north Florida (300 MW, 12 units, 20 spillway gates). Three dams are High hazard potential and one is Significant. A 24x7 Remote Operations Center (ROC) at headquarters supervises and controls all 4 projects and, under contract, 6 small hydro projects owned by 4 client companies. The control system is the Hydro Control and Dam Monitoring System (HCDMS) described in the SSP (P02): ROC SCADA, plant and gate controls, dam safety instrumentation and sirens, the OT wide-area network, remote access, and OT monitoring (SYS-01 to SYS-07). Corporate IT, the cloud landing zone, and SaaS services support the business (SYS-08 to SYS-16). See `../00_company-facts.md` sections 1 and 3.

**What is different about a dam operator.** For most processes the question is "how long until we lose money." For BP-01, BP-02, BP-08, and BP-18 it is "how long until someone downstream, or a public water supply, could be harmed." The company can always fall back to **manual local control**: operators at the 20 gate panels and the unit panels, and technicians reading instruments by hand. The MTDs below measure how long the company can run on those workarounds safely, not how long a dam can go uncontrolled. A dam is never left uncontrolled.

## 3. Impact categories and values
Dollar values are scaled to $186.0 million in annual revenue (about $509,600 per day). Generation is about $350,700 per day at average output (Blackwater Bend $203,400, Cedar Shoals $98,200, Pine Hollow $31,600, Sawgrass Run $17,500). Field services earn about $118,000 per working day (250 days) and RMOS about $31,500 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $500,000 (about one day of total revenue) | $50,000 to $500,000 | Less than $50,000 |
| Operations | Gates or units at a project cannot be controlled even locally; the ROC and the backup ROC are both lost; or a business unit cannot deliver its core service | One project, one client, or one service line runs only on manual workarounds | Staff slowed but working |
| Regulatory | Condition reportable under 18 CFR 12.10, EAP activation, a FERC directive, or a possible NERC violation (EOP-004-4, CIP-003-9, CIP-012-2) | Missed internal, contract, or client deadline | Internal policy deviation |
| Safety | Plausible harm to people downstream, to recreation users, or to a public water supply (uncontrolled release, missed warning, reservoir below an intake) | Worker safety exposure during manual operation | None |
| Reputation | Regional or national media coverage; loss of a PPA offtaker, an RMOS client, or community confidence | Complaints from clients, recreation users, or the county | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered plus extra labor over the MTD. Assumptions from the process owners: local control keeps about half of normal BES output during the first 12 hours; Sawgrass Run stops when ROC control is lost; RMOS service credits follow the standard contract (10% of the monthly fee per day of outage, capped at 30%); field crews keep about 85% of productivity on printed packets for 3 days. Regulatory exposure (for example a missed EOP-004-4 report) is not given a dollar value.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Reservoir and spillway gate operations | Generation Operations | High | 4 | 2 | 1 | $25,000 |
| 2 | BP-02 Dam safety monitoring and EAP early warning | Dam Safety | High | 8 | 4 | 1 | $8,000 |
| 3 | BP-05 ROC supervision and ICCP data exchange | ROC | High | 4 | 2 | 0.25 | $15,000 |
| 4 | BP-08 RMOS client monitoring and control | Hydro Services | High | 4 | 2 | 1 | $40,000 |
| 5 | BP-03 Generation and unit control, BES plants | Generation Operations | High | 12 | 6 | 24 | $95,000 |
| 6 | BP-07 Physical security monitoring | Corporate Security | Moderate | 8 | 4 | 24 | $12,000 |
| 7 | BP-18 Cedar Shoals raw-water intake level | Generation Operations | Moderate | 24 | 12 | 1 | $3,300 |
| 8 | BP-04 Generation and unit control, non-BES plants | Generation Operations | Moderate | 24 | 12 | 24 | $24,600 |
| 9 | BP-11 Regulatory reporting | Legal and Compliance | Moderate | 24 | 12 | 24 | $0 (regulatory exposure only) |
| 10 | BP-06 Energy scheduling and settlement | Generation Operations | Moderate | 24 | 8 | 4 | $20,000 |
| 11 | BP-13 Corporate communications and mass notification | Corporate IT | Moderate | 24 | 8 | 24 | $10,000 |
| 12 | BP-10 Field services delivery | Hydro Services | Moderate | 72 | 24 | 24 | $53,000 |
| 13 | BP-09 RMOS client portal and reporting | Hydro Services | Moderate | 72 | 24 | 4 | $6,000 |
| 14 | BP-12 Maintenance management and spares | Generation Operations | Moderate | 72 | 48 | 24 | $15,000 |
| 15 | BP-14 Engineering records and CEII control | Dam Safety | Moderate | 48 | 24 | 24 | $5,000 |
| 16 | BP-15 Recreation reservations | Recreation and Lands | Low | 48 | 24 | 24 | $8,000 |
| 17 | BP-16 Finance, payroll, and HR | Corporate | Low | 120 | 72 | 24 | $20,000 |
| 18 | BP-17 Dam safety analytics and AI | Data Analytics | Low | 168 | 72 | 24 | $2,000 |

**Summary:** 5 High, 10 Moderate, and 3 Low processes (18 in total). The sum of estimated losses at each process's MTD is $361,900.

**Enterprise-wide scenarios.**
- **OT-wide cyber event (ROC SCADA and the OT WAN untrusted for 72 hours, all 4 projects in local control).** Unrecovered generation revenue about $552,300 (BES plants $452,400 at half output; Pine Hollow at half output and Sawgrass Run stopped $99,900), RMOS revenue and service credits about $381,500, and overtime for round-the-clock local staffing about $150,000: **about $1.08 million**, before response costs. The bigger exposure is safety: 20 gates in local control during a flood needs more qualified operators than the company has on its call-out list (finding 3).
- **Ransomware in corporate IT that forces IT/OT separation for 72 hours.** Field services, scheduling and settlement, the RMOS portal, recreation, and corporate functions run on workarounds (about $107,000 of unrecovered revenue and labor, the sum of the BP-06, BP-09, BP-10, BP-15, and BP-16 losses at MTD). The ROC keeps running, but separation also cuts the identity provider that supplies MFA to the OT jump hosts (finding 5). If RMOS client data is stolen, response and client notice costs come on top (P01 R-003; P08 `ir-runbook-ransomware.md`).

**What drives the values:**
- **Public safety** drives BP-01, BP-02, BP-08, and BP-18. Gate operations have the shortest MTD (4 hours) because all-local operation needs 20 people at 4 dams.
- **Revenue** drives BP-03, BP-04, and BP-10. A day without the BES plants costs about $301,600.
- **Regulatory clocks** drive BP-05 (CIP-012-2, the BA/TOP agreement) and BP-11 (EOP-004-4 reports within 24 hours or by the end of the next business day; FERC security incident reports usually within one working day).

## 5. Key findings
1. **OT recovery is proven only at Blackwater Bend** (gap 7). A restore test passed at Blackwater Bend in 2025. Configuration backups for Cedar Shoals, Pine Hollow, and Sawgrass Run are incomplete, and the governor settings for 5 units are held only by the OEMs. The RTOs of 2 to 12 hours for BP-01, BP-03, BP-04, and BP-05 are targets, not demonstrated capabilities (P01 R-008; P07 CP-4 and CP-10).
2. **The backup ROC is not independent of a cyber event.** It sits on the same flat OT WAN and in the same SCADA domain as the primary ROC (gap 2). It protects against loss of the building, not against an attacker in the SCADA. The Blackwater Bend Rapid Recovery sub-element does not cover recovery of the ROC SCADA after a cyber attack (Rev. 3A 7.4.2).
3. **All-local operation is thin during a flood.** Running all 20 gates locally needs 20 people at once, and the call-out list has 22 qualified gate operators across 4 sites. A flood that forces local control at night would leave almost no relief. Action: cross-train 12 more plant staff on local gate operation by 2027-03-31 (P01 R-018).
4. **RMOS handback is not fully written down.** Operating orders for 2 of the 4 client projects the ROC operates do not state how fast client staff must take local control when the ROC cannot. The BIA assumes 4 hours (BP-08). Action: add handback terms to all operating orders and the new client security schedule (P03 G-118; P09).
5. **Identity is a hidden OT dependency.** The corporate identity provider supplies MFA for the OT jump hosts (SYS-06, SYS-09). A ransomware event that forces IT/OT separation also removes staff remote access to OT. That is acceptable for safety (the ROC operates locally) but slows vendor support during recovery. Action: break-glass MFA for the jump hosts that does not depend on the corporate identity provider (P01 R-027).
6. **The ICCP link has no written loss or recovery method** (gap 11). The BA/TOP accepts voice updates for about 4 hours (BP-05). CIP-012-2 R1 Parts 1.2 and 1.3 require those methods in the plan from 2026-07-01 (P03).
7. **Cedar Shoals has a water supply mission.** Undetected full flows could draw the reservoir below the county intake within about 30 hours (BP-18). That makes "loss of other missions" in Rev. 3A Table 9.1b a live consequence for Cedar Shoals and supports its Critical designation in the Section 9 re-determination.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 ROC SCADA (primary and backup ROC) | Supervisory control and alarms for 4 projects and 6 RMOS client projects; ICCP server | BP-01 to BP-05, BP-08, BP-18 |
| SYS-02 Plant control | 12 unit PLCs, governors, exciters, plant HMIs | BP-03, BP-04, BP-18 |
| SYS-03 Spillway gate control | Gate PLCs, 20 local panels, hoists, standby generators | BP-01, BP-18 |
| SYS-04 Instrumentation and early warning | 410 instruments, 9 river gauges, 23 sirens | BP-01, BP-02, BP-18 |
| SYS-05 OT WAN and site networks | Fiber and microwave, site OT firewalls, OT DMZ, OT backup server | BP-01 to BP-05, BP-08 |
| SYS-06 Remote access | OT jump hosts with MFA; RMOS client tunnels; 2 OEM direct VPNs (gap 3) | BP-04, BP-08, recovery support |
| SYS-07 OT monitoring | Passive sensors at the ROC and BWB; MSSP alerts | Recovery validation |
| SYS-08, SYS-09, SYS-10 | Corporate endpoints, identity provider (also jump host MFA), productivity suite | BP-06, BP-10, BP-11, BP-13, BP-14, BP-16 |
| SYS-11 Cloud landing zone | 6 accounts, including the backup account | BP-09, BP-17, recovery of cloud workloads |
| SYS-12 Business SaaS | ERP and EAM, HR and payroll, scheduling and settlement, reservations | BP-06, BP-10, BP-12, BP-15, BP-16 |
| SYS-13 SIEM (MSSP) | Detection and investigation | Recovery validation |
| SYS-14 Dam safety data platform | Data lake, dashboards, AI-001 and AI-002 | BP-17 |
| SYS-15 RMOS client portal | Client dashboards and reports | BP-09 |
| SYS-16 Physical security systems | Cameras, card access, intrusion detection | BP-07 |
| People | ROC staff (36), plant operators, 22 call-out gate operators, dam safety technicians, controls engineering and I&C (24), OT Security Manager and 3 OT security engineers | All |
| Third parties | SCADA platform vendor, governor and turbine OEMs, BA/TOP, cooperative, RMOS clients, MSSP, cloud and SaaS providers, county emergency management | As listed in `bia.csv` |

**Backup and replication behind the RPOs:** historian replication to the OT DMZ and to the cloud data lake (BP-01 to BP-05); data logger buffers (BP-02); monthly PLC and HMI configuration backups to the OT backup server and quarterly offline copies (complete only for BWB and the ROC today); immutable corporate backups in the cloud backup account (BP-06, BP-09 to BP-16); SaaS provider backups.

## 7. FERC Security Program linkage
The BIA supplies the recovery content that the Security Plans and Section 9 expect. Text checked against Rev. 3A (ferc.gov PDF).

| Rev. 3A requirement (summarized) | What this BIA supplies | Status |
|---|---|---|
| 7.4.2 Rapid Recovery of Essential Services (required for Group 1: Blackwater Bend): pre-planned actions to continue or quickly restore generation, including spare parts, equipment, and contractors | BP-03 and BP-12 values; recovery order in section 8; spare parts dependency | Sub-element exists but omits ROC SCADA recovery after a cyber attack (gap 7). Update due 2026-12-15 |
| 7.4.1 Internal Emergency Response (Groups 1 and 2: BWB, CDS, PNH): hand-off between a security incident and emergency notification and response | BP-01, BP-02, BP-07 workarounds; trigger to EAP | Cyber triggers missing (gap 8); added through P08 by 2026-11-30 |
| Table 9.3a: plan for timely restoration and recovery of control systems; review and test the plan annually | RTO and RPO for every HCDMS-dependent process | Tested only at BWB (2025). Annual tests at all 4 projects from 2027 (P07 POA&M) |
| Form 3 Question 20: identify the systems, assets, information, and processes essential to the mission | The 18 processes and their dependencies in `bia.csv` | Met by this BIA; review each year |
| Table 9.1b item 3: loss of other missions such as water supply | BP-18 (Cedar Shoals raw-water intake) | Used in the 2026-07-16 Section 9 re-determination |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Local manual control of gates and units at all 4 projects | Immediate: 15 minutes at staffed sites; 60 to 90 minutes at Sawgrass Run and at night | Call-out list; radio; roving operator |
| 2 | Sirens and instrument data acquisition | 4 h | Manual readings every 4 hours; local siren activation |
| 3 | ROC SCADA from a verified state, or the backup ROC once confirmed clean | 2 h (target; unproven after a cyber event) | Plant control rooms keep local control |
| 4 | OT WAN and site firewalls, restored site by site with segmented routes | 2 h per site | Sites run independently |
| 5 | ICCP link to the BA/TOP | 2 h | Voice updates every 30 minutes |
| 6 | RMOS client control, one client tunnel at a time after validation | 4 h | Client staff take local control under operating orders |
| 7 | Plant control through SCADA (BES plants, then PNH and SGR) | 6 h and 12 h | Local unit control; SGR shut down and spilling |
| 8 | Physical security systems | 4 h | Posted officers; patrols |
| 9 | Identity provider and jump host MFA (break-glass path) | 4 h | On-site support only |
| 10 | Email and mass notification | 8 h | Personal phones; printed lists; radios; satellite phones |
| 11 | Scheduling and settlement | 8 h | Phone schedules |
| 12 | ERP and EAM; field services | 24 to 48 h | Paper |
| 13 | RMOS client portal | 24 h | Emailed PDF reports |
| 14 | Historian replica and the dam safety data platform (one-way feed) | 72 h | Local historian; manual trend review |
| 15 | Reservations; payroll | 24 h and 72 h | Walk-in registration; repeat prior payroll |

Priority 1 is not a system: it is people at panels. Every OT recovery step in P08 starts by putting gates and units in local control and confirming their physical positions before any system is restored.
