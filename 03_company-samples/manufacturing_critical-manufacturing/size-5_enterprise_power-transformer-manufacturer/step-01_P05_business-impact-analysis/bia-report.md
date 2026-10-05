# Business Impact Analysis: Cris Santos Company | Critical Manufacturing | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer; 7 plants in 6 states) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired Ohio plant (AQ-01). It feeds:
- the availability rating and recovery objectives in the Enterprise ERP and Production Scheduling Platform (EPSP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the materiality worksheet and recovery order in the ransomware runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09);
- plant business continuity plans and the EPSP contingency plan.

**Results in one line:** 18 processes were analyzed; 11 are High criticality and 7 Moderate. 4 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 14 of them single points of failure (one only at AQ-01), and 1 that has never been tested (the AQ-01 legacy ERP and MES restore).

## 2. System and business description
Cris Santos Company designs, builds, tests, and services transformers for the electric grid. It runs 7 plants (P1 to P7) in Florida, Georgia, Tennessee, Texas, North Carolina, and Ohio, 9 service and repair centers, 3 spare transformer yards, and 2 colocation data centers. It has 12,000 employees, about 650 utility customers, and about $4.8 billion in annual revenue (about $16.7 million of shipments per production day). The technology estate is described in `../00_company-facts.md` section 3: a global ERP with an advanced planning and scheduling module (SYS-01), an identity platform (SYS-02), a multi-cloud estate across two public cloud providers plus two colocation data centers (SYS-03), an SD-WAN with IT/OT boundaries (SYS-04), MES at every plant (SYS-05), about 3,900 OT assets (SYS-06), test systems and the Test Data Management System (SYS-07), and two service lines offered to utilities: the Fleet Monitoring Service (SL-1, SYS-11) and the Spare Transformer Reserve Service (SL-2, SYS-12). The Ohio plant (AQ-01, acquired 2025-07) still runs its own legacy ERP and MES.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the materiality worksheet in P08 section 6. Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative (including liquidated damages) | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Two or more plants stop, or any plant stops for more than 2 days, or storm-restoration orders cannot be filled | One plant, one service line, or one function stops | Staff slowed but working |
| Regulatory and contractual | Missed SEC filing or Form 8-K deadline; missed utility addendum notice; export without screening; loss of DOE certification records | Missed internal or contractual reporting date with no penalty | Internal policy deviation |
| Safety | Plausible injury, fire, or release (drying ovens, vacuum oil systems, high-voltage test) | Degraded but safe operation | None |
| Reputation | National media; utility customers or STRS members move business; analyst or ratings action | Regional media; customer complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Ordered by recovery priority. Impacts overlap (for example, an MES outage drives the plant production losses), so the 24-hour figures are not added together.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-05 Power transformer production (P2, P4, and P5) | High | 72 h | 4 h | 24 h | $7.90M |
| BP-03 Work order release and shop-floor execution (MES) | High | 24 h | 4 h | 15 min | $8.40M |
| BP-12 Fleet Monitoring Service (SL-1) | High | 24 h | 4 h | 15 min | $0.65M |
| BP-18 Contractual and regulatory notices | High | 24 h | 4 h | 24 h | $0.05M |
| BP-02 Production planning and scheduling (APS) | High | 48 h | 8 h | 15 min | $3.10M |
| BP-13 Spare Transformer Reserve Service dispatch (SL-2) | High | 24 h | 8 h | 1 h | $0.40M |
| BP-11 Field service, commissioning, and storm response | High | 24 h | 8 h | 4 h | $1.50M |
| BP-04 Distribution transformer production (P1 and P3) | High | 48 h | 12 h | 24 h | $8.00M |
| BP-07 Testing, certified test reports, and DOE certification data | High | 72 h | 24 h | 1 h | $2.50M |
| BP-10 Shipping, heavy-haul logistics, and export screening | High | 48 h | 24 h | 15 min | $2.00M |
| BP-14 TMU firmware release and product security response | High | 72 h | 24 h | 1 h | $0.15M |
| BP-01 Order entry, configuration, and quoting | Moderate | 48 h | 24 h | 15 min | $0.60M |
| BP-09 Procurement, supplier collaboration, and EDI | Moderate | 72 h | 24 h | 15 min | $0.50M |
| BP-17 AQ-01 (P7) operations on legacy ERP and MES | Moderate | 48 h | 24 h | 1 h | $0.80M |
| BP-08 Engineering design and PLM | Moderate | 120 h | 48 h | 1 h | $0.70M |
| BP-15 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-06 Core and component production (P6) | Moderate | 120 h | 72 h | 24 h | $0.90M |
| BP-16 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.10M |

**What drives the values:**
- **Safety sets the shortest RTO.** Vapor-phase drying ovens and vacuum oil systems at P2, P4, and P5 (BP-05) must be supervised from an HMI or held in a safe state. An interrupted drying cycle may have to restart, losing 2 to 5 days on a large power transformer, and liquidated damages of about 0.5% of contract value per week start on late units.
- **The MES is the choke point.** Paper travelers carry a plant through about one shift. After 24 hours untraceable work stops shipments, so BP-03 has the shortest MTD among production processes and a 15-minute RPO to keep traceability for test reports.
- **Storm season tightens distribution production.** BP-04 has a 48-hour MTD that falls to 24 hours when a hurricane watch covers a customer's service area.
- **Contracts set the service line objectives.** FMS subscribers are promised 99.5% monthly availability and advisories within 24 hours of a high-severity alert (BP-12); STRS members are promised a dispatch decision within 24 hours (BP-13).
- **Regulation and contract clocks set BP-18.** The shortest are the 24-hour incident notice in 27 utility addenda, 1 business day for access-revocation notices and FAR 52.204-25(d) reports, and 4 business days for Form 8-K Item 1.05 after a materiality determination. The process itself costs little to run; the exposure is breach of contract and disclosure risk.
- **Records drive BP-07 and BP-10.** No unit ships without a certified test report; DOE certification test data must be kept for DOE review (10 CFR 429.71); export records must be kept 5 years (15 CFR 762.6), and no export ships without screening.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **ERP recovery time (DEP-01).** The 2026-05-16 failover test met the 15-minute RPO (9 minutes of data lost) but took 11 hours against the 8-hour RTO, because database restore and integration cut-over are manual. Every EPSP-dependent process (BP-01, BP-02, BP-03, BP-09, BP-10, BP-13, BP-16) inherits that gap. This is P01 risk R-005 and POA&M item POAM-006.
2. **AQ-01 (DEP-04, DEP-15, DEP-20).** The Ohio plant runs on a legacy ERP and MES backed up nightly, so its real RPO is 24 hours against a 1-hour target, and no restore has ever been tested. It has one SD-WAN carrier and 5 always-on OEM cellular routers. Its two-way domain trust makes it a path into the enterprise (R-003; POAM-004).
3. **Supplier concentration (DEP-08, DEP-12, DEP-13).** One grain-oriented electrical steel supplier provides 68% of supply, and qualifying a third takes 6 to 9 months. The TMU electronics contract manufacturer is a sole source that has never been assessed for security and loads boot firmware (POAM-018). The EDI provider's SOC report expired in 2026-03 (POAM-014).
4. **OT recovery (DEP-15, DEP-16).** Controller program backups are automated at P1 to P6, but restores have been tested only at P1 and P5 (POAM-007). The OT-capable response firm on the insurer panel took part in the 2026-03 tabletop.
5. **Single facilities (DEP-21, DEP-22).** The P2 extra-high-voltage laboratory is the only place to test units above 345 kV. The spare yards hold 64 units; the Tennessee yard has no intrusion detection (POAM-023).
6. **Notices depend on one register (DEP-25).** The obligations register in the GRC platform holds the utility security contacts and deadlines. A printed copy in the incident binders is refreshed monthly. The 12 AQ-01 addenda are not yet loaded (POAM-016).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 ERP and APS | Single global instance on Cloud provider A; orders, schedule, purchasing, shipping, export screening, finance, STRS registry | BP-01, BP-02, BP-09, BP-10, BP-13, BP-16 |
| SYS-02 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-03 Cloud provider A workloads | ERP, integration platform, PLM, TDMS, STRS portal | BP-01 to BP-03, BP-07 to BP-10, BP-13 |
| SYS-03 Cloud provider B workloads | FMS, data platform and AI services, product build pipeline | BP-12, BP-14 |
| SYS-03 Colocation DC-1 and DC-2 | Network core, engineering compute cluster, offline backup copies | BP-08; recovery of all |
| SYS-04 Enterprise network | SD-WAN with two carriers per plant (one at AQ-01); IT/OT boundary firewalls | All site-based processes |
| SYS-05 MES (P1 to P6) | Application tier in each plant OT DMZ; about 1,100 kiosks | BP-03, BP-04, BP-05, BP-07 |
| SYS-06 Plant control systems | PLCs, CNC, winding machines, drying ovens, oil processing, HMIs | BP-04, BP-05, BP-06 |
| SYS-07 Test systems and TDMS | Test stations, high-voltage laboratories, certification data | BP-07 |
| SYS-10 Product pipeline and HSM | Firmware builds, signing, SBOMs, download portal | BP-14 |
| SYS-11 FMS; SYS-12 STRS | Service line platforms | BP-12; BP-13 |
| Immutable backups | Separate backup accounts with write-once retention in a second region; weekly offline copy at DC-2; automated controller program backups at P1 to P6 | RPO for all cloud workloads and plant OT |
| People | Plant operators and controls technicians, planners, test technicians, field technicians, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Plant safe states: drying ovens, vacuum and oil processing (P2, P4, P5) with verified programs | Immediate safe state; HMI supervision within 4 h | Local PLC operation under operator watch; safe-shutdown procedures |
| 2 | SYS-02 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 3 | Network core, SD-WAN, DNS, and IT/OT boundary firewalls (held closed) | 2 h | Cellular failover at P1 to P6 |
| 4 | Security tooling (EDR, SIEM, OT sensors) for clean validation | 2 h | MSSP tooling |
| 5 | MES application tier and kiosks at P1 to P6 | 4 h | Paper travelers for one shift |
| 6 | FMS (Cloud provider B) | 4 h | Reliability engineers call subscribers about high-risk units |
| 7 | Obligations register and out-of-band communications | 4 h | Printed register in the incident binders |
| 8 | ERP, APS, and integration platform | 8 h target (11 h demonstrated, POAM-006) | Printed 5-day schedules; paper orders |
| 9 | STRS portal and spare registry | 8 h | Printed registry; phone dispatch (fallback untested, POAM-024) |
| 10 | Field service tools and crew dispatch | 8 h | Printed rosters and job packets |
| 11 | Winding and core line HMIs at P1 and P3 | 12 h | Manual recipe entry with engineering double-check |
| 12 | TDMS and test stations | 24 h | Local station storage for 30 days; signed printouts |
| 13 | Shipping, export screening, and EDI | 24 h | Manual screening by Trade Compliance; email purchase orders |
| 14 | Firmware build pipeline and download portal | 24 h | Release freeze; advisories through the obligations register |
| 15 | AQ-01 legacy ERP and MES | 24 h target (untested) | Paper travelers; spreadsheet schedule |
| 16 | PLM and engineering compute cluster | 48 h | Released drawings cached on plant shares |
| 17 | Payroll and timekeeping | 48 h | Repeat prior payroll |
| 18 | P6 component production systems; financial close | 72 h | Outside purchase of cut cores; close from the last ERP extract |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| ERP failover 11 h against an 8 h RTO | P01 R-005; P02 CP-10; P03 G-073; POAM-006 |
| Controller program restores tested at 2 of 7 plants; P3 MES backup incomplete | P01 R-031, R-032; P03 G-064; POAM-007 |
| AQ-01 legacy systems: 24 h real RPO, untested restore, flat network, cellular routers | P01 R-003, R-007; P03 G-071; POAM-004, POAM-007, POAM-008 |
| Sole-source TMU contract manufacturer never assessed; EDI provider SOC report expired | P01 R-023, R-024; P03 G-048; POAM-014, POAM-018 |
| STRS manual dispatch fallback untested | P01 R-015; P02 CP-2; POAM-024 |
| Spare yard monitoring incomplete | P01 R-041; P03 G-058; POAM-023 |
| Materiality worksheet lacks production-loss values | P01 R-016; P03 G-094, G-135; POAM-011 (P08 section 6 now uses the values in section 4) |
