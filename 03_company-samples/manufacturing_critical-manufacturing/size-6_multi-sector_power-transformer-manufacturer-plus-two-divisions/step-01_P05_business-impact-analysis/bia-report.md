# Business Impact Analysis: Cris Santos Company Holdings | Critical Manufacturing | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. (focus division: Transformer Manufacturing) | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity (SYS-G1), the SOC (SYS-G2), cloud and network (SYS-G3), the Group ERP and Production Scheduling Platform (GEPS, SYS-G4), HR and payroll (SYS-G5), and email and files (SYS-G6).
- **Division BIAs:** Transformer Manufacturing (focus), Electric Utility, and Grid Engineering. They are rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It feeds:
- the availability rating of the GEPS in the SSP (P02) and the impact ratings in the four risk registers (P01);
- the recovery order in the ransomware runbook (P08);
- the Electric Utility's CIP-009-6 recovery plans for the TCC (the BIA records their targets; it does not replace them);
- the FMS and project platform availability commitments in the SOC 2 scoping (P09);
- the voluntary benchmark outcomes GV.OC-04 (critical services) and ID.AM-05 (prioritization) in the gap analysis (P03).

## 2. System and business description
Corporate runs one GEPS instance for all three divisions (see `../00_company-facts.md` section 3). Transformer Manufacturing uses it for configure-to-order, bills of materials, export screening, and the APS schedule that releases work orders to the 8 plant MES through the integration hub. The Electric Utility uses it for storm stock, materials, and finance. Grid Engineering uses it for project accounting. Plant control systems (SYS-M2) and the Electric Utility's TCC and DCC (SYS-U1, SYS-U2) do not depend on the GEPS or on group identity while they run, which is why they recover on their own tracks.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Transformer Manufacturing about $26.3 million per day, Electric Utility about $16.4 million per day, and Grid Engineering about $6.6 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue (lost output, liquidated damages, restoration) | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (grid equipment, electric service, engineering deliverables), or more than one plant stops | One plant, line, or service stops | Staff slowed but working |
| Regulatory | Missed NERC or DOE report, reportable breach, SEC disclosure, or missed contract notice to a utility | Missed internal or non-statutory contractual deadline | Internal policy deviation |
| Safety | Plausible harm to workers (ovens, vacuum oil processing, test labs), crews, or the public (prolonged outages, unsafe units on the grid) | Delayed but safe operation | None |
| Reputation | National media, loss of utility customers or FMS subscribers, or regulator attention (SERC, FERC, state commission) | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 11 Transformer Manufacturing, 5 Electric Utility, and 4 Grid Engineering. 14 are High, 12 Moderate, and 1 Low. Rows are in recovery priority order.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-EU01 Transmission operations at the TCC | Electric Utility | High | 2 h | 1 h | 0 h |
| BP-EU02 Distribution operations and outage restoration | Electric Utility | High | 2 h | 1 h | 0 h |
| BP-EU05 Reliability and cyber incident reporting | Electric Utility | High | 1 h | 1 h | 24 h |
| BP-G01 Workforce identity and access | Group shared service | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, WAN, and plant connectivity | Group shared service | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group shared service | High | 8 h | 4 h | 1 h |
| BP-MF04 Plant process control | Transformer Manufacturing | High | 24 h | 12 h | 24 h |
| BP-G04 GEPS platform operations (ERP, APS, integration hub) | Group shared service | High | 24 h | 12 h | 1 h |
| BP-MF02 Production scheduling and work order release | Transformer Manufacturing | High | 48 h | 24 h | 1 h |
| BP-MF07 Storm-restoration orders and spare transformer release | Transformer Manufacturing | High | 24 h | 8 h | 1 h |
| BP-EU03 Storm materials and transformer logistics | Electric Utility | High | 24 h | 12 h | 1 h |
| BP-MF03 Plant production execution (MES) | Transformer Manufacturing | High | 24 h | 12 h | 4 h |
| BP-ES03 Client notices and contract duties | Grid Engineering | High | 24 h | 8 h | 24 h |
| BP-MF05 Testing and certified test reports | Transformer Manufacturing | High | 72 h | 24 h | 1 h |
| BP-MF06 Shipping, export screening, and logistics | Transformer Manufacturing | Moderate | 72 h | 24 h | 1 h |
| BP-MF01 Order entry, configuration, and engineering release | Transformer Manufacturing | Moderate | 72 h | 24 h | 1 h |
| BP-MF09 Fleet Monitoring Service for utilities | Transformer Manufacturing | Moderate | 24 h | 8 h | 1 h |
| BP-ES01 Client project delivery and document control | Grid Engineering | Moderate | 72 h | 24 h | 4 h |
| BP-ES02 Field commissioning and protection settings | Grid Engineering | Moderate | 48 h | 24 h | 24 h |
| BP-MF08 TMU firmware build, signing, and release | Transformer Manufacturing | Moderate | 120 h | 72 h | 24 h |
| BP-EU04 Customer service, metering, and billing | Electric Utility | Moderate | 72 h | 24 h | 4 h |
| BP-MF11 Procurement and supplier EDI | Transformer Manufacturing | Moderate | 72 h | 48 h | 1 h |
| BP-MF10 Field service, commissioning, and repair | Transformer Manufacturing | Moderate | 72 h | 24 h | 24 h |
| BP-G05 Financial close, SEC reporting, and treasury payments | Group shared service | Moderate | 72 h | 48 h | 1 h |
| BP-G07 Email, collaboration, and file services | Group shared service | Moderate | 24 h | 8 h | 24 h |
| BP-ES04 Federal contract delivery | Grid Engineering | Low | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group shared service | Moderate | 120 h | 72 h | 24 h |

**What drives the values:**
- **The MES buffer drives manufacturing.** Each plant MES holds about 48 hours of released work orders, so production scheduling (BP-MF02) has an MTD of 48 hours. After that, all 8 plants stop for lack of released orders, at about $26.3 million of output per day.
- **Storm season shortens everything.** From June to November, storm orders and spare release (BP-MF07) and the Electric Utility's storm materials (BP-EU03) have a 24-hour MTD, because restoration crews cannot wait.
- **Safety, not revenue, drives plant process control** (BP-MF04). Ovens and vacuum oil processing must reach a safe state at once and restart only under control, from verified controller programs.
- **Reliability drives the Electric Utility.** The TCC and DCC (BP-EU01, BP-EU02) have 2-hour MTDs and recover through the backup control centers. Reporting (BP-EU05) is its own process because the DOE-417 Emergency Alert clock is 1 hour.
- **Integrity drives testing and firmware** (BP-MF05, BP-MF08). A few days of delay is tolerable; an altered test report or firmware image is not.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every IT process | A group identity outage stops order entry, scheduling, and project work at once. Plant OT DMZs and the TCC use separate local accounts, so control systems keep running |
| GEPS (SYS-G4) | Group | BP-MF01, MF02, MF06, MF07, MF11; BP-EU03; BP-G05 | One ERP instance means one outage stops manufacturing scheduling **and** the utility's storm stock **and** group finance. This is the single largest shared dependency |
| Transformers and spares (BP-MF07) | Transformer Manufacturing | Electric Utility (BP-EU03) | The utility buys all its large power transformer spares and about 35% of its distribution transformers from the affiliate. A manufacturing outage in storm season lengthens the utility's restoration |
| Engineering and commissioning (BP-ES02) | Grid Engineering | Electric Utility | About $310 million a year of design, settings, and commissioning work; 140 engineers hold TCC access |
| SOC facts (BP-G02) | Group | Every division's notices | Utility addenda clocks (24 and 48 hours), client contract clocks (24 to 72 hours), CIP-008-6, DOE-417, and Form 8-K all start from facts the SOC establishes |
| TMU data | Electric Utility (and 69 other subscribers) | FMS (BP-MF09) | Utilities push data one way; an FMS outage does not affect utility operations |

**Single points of failure found:**
- The GEPS integration hub (one cluster, 6 service accounts with standing access to all 8 MES). Mitigation in P01 GR-02 and POAM-002.
- The TMU firmware signing key on one build server (P01 MF-005).
- The P8 legacy MES server, which has no tested backup (P01 MF-003).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-G1 identity platform | Vendor multi-region SaaS; configuration exported daily | All IT processes |
| SYS-G3 landing zones and WAN | Infrastructure as code; dual carriers with cellular backup | All |
| SYS-G4 GEPS | Primary in provider A; database replication to provider B (RPO about 15 minutes); immutable daily backups in the provider B vault | BP-G04, BP-MF01, MF02, MF06, MF07, MF11, BP-EU03, BP-G05 |
| SYS-M1 plant MES | P1 to P7: application servers in the OT DMZ, nightly database backups to the plant backup appliance and the vault. P8: local disk only | BP-MF03 |
| SYS-M2 plant OT | Automated controller program backups at P1 to P7 (daily); ad hoc copies at P8 | BP-MF04 |
| SYS-M4 TDMS | Provider A with backups in the provider B vault; local results on test stations for 30 days | BP-MF05 |
| SYS-M5 firmware pipeline | Repositories (SaaS) and build servers in the group data center; release hashes in the download portal | BP-MF08 |
| SYS-M6 FMS; SYS-S1 project platform | Provider B, with a warm standby region | BP-MF09; BP-ES01 |
| SYS-U1 and SYS-U2 | Backup TCC and backup DCC with their own recovery plans (CIP-009-6 for the TCC) | BP-EU01, BP-EU02 |
| People | Cross-trained planners at every plant; storm desk; out-of-band crisis line | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1-3 | Electric Utility TCC, DCC, and reliability reporting (own track) | Within 1 hour (failover to the backup centers) | Backup TCC and DCC; printed reporting binder |
| 4-6 | Group identity, landing zones and WAN, SOC visibility | 1 to 4 hours | Break-glass accounts; retainer tooling |
| 7 | Plant process control (safe state at once; controlled restart) | 12 hours to restart | Manual shutdown procedures; controller backups |
| 8-12 | GEPS, production scheduling, storm orders, utility storm materials, plant MES | 8 to 24 hours | Reporting copy in provider B; printed lists; paper travelers (not at P8) |
| 13-16 | Client notices, testing, shipping, order entry | 8 to 24 hours | Printed contact lists; local test results; manual screening |
| 17-27 | FMS, project platform, commissioning, firmware, billing, procurement, field service, finance, email, federal work, payroll | 8 to 72 hours | Per `bia.csv` |

## 8. Key findings
1. **The GEPS is the group's widest single point of failure.** It is High for availability because one outage stops manufacturing scheduling, the utility's storm stock, and finance together (P02 categorization).
2. **The 24-hour GEPS recovery time is unproven.** Only the finance modules have been restored in a test; APS and the integration hub have not (P01 GR-02; POAM-004).
3. **P8 is outside the plant recovery design.** It has no paper production procedure, no tested MES backup, and only ad hoc controller backups, so it would recover last and slowest (P01 MF-003).
4. **Notification capacity is itself a process** (BP-G02, BP-EU05, BP-ES03). If the SOC or the contracts team is down during an incident, the clocks keep running. The P08 runbook uses out-of-band channels for this reason.
