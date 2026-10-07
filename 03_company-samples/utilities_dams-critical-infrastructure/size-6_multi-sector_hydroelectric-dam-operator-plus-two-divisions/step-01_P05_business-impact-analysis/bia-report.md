# Business Impact Analysis: Cris Santos Company Holdings | Dams | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees; Hydro, Constructors, Engineering) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division security and compliance leads and the Chief Dam Safety Engineer | **Fieldwork:** 2026-05-01 to 2026-07-31 | **Approved:** board safety, risk, and reliability committee, 2026-09-10

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services that the divisions depend on (identity, security operations, cloud, network, payroll and HR, finance, procurement).
- **Division BIAs:** Hydro (focus), Constructors, and Engineering, kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the Hydro **Rapid Recovery** sub-element required in the Security Plans of the 6 Group 1 dams and the Section 9 restoration and recovery measure (FERC Security Program Rev. 3A, 7.4 and Table 9.3a);
- the **CIP-009-6 recovery plans** for the medium impact BES Cyber Systems at HOC-A and HOC-B;
- the EAP and Owner's Dam Safety Program (18 CFR 12.20 to 12.25 and 12.60 to 12.65), which this BIA does not replace;
- the DSMS availability commitments that the SOC 2 readiness work tests (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

## 2. System and business description
Corporate runs SYS-G1 (identity), SYS-G2 (security operations), SYS-G3 (cloud platform on providers A and B), SYS-G4 (ERP, HR, payroll), SYS-G5 (network and endpoints), and SYS-G6 (productivity suite). Hydro runs the fleet SCADA at two Hydro Operations Centers (SYS-H1), plant and gate control (SYS-H2, SYS-H3), dam safety instrumentation (SYS-H4), and the OT network and identity domain (SYS-H5). Constructors runs its project platform (SYS-C1), the Federal Projects Enclave (SYS-C2), and jobsite technology (SYS-C3). Engineering runs the Dam Safety Monitoring Service (SYS-E1) and its design environment (SYS-E2). See `../00_company-facts.md` section 3.

**One design choice shapes the whole BIA:** Hydro OT does not depend on corporate identity or corporate networks. The OT identity domain does not trust SYS-G1, and gates and units can run in local control. That is why Hydro's safety-critical processes can recover before, and in parallel with, the group shared services.

## 3. Impact categories and values
Dollar values use the fictional revenue in `../00_company-facts.md` section 7: Hydro about $17.0 million per day, Constructors about $25.5 million per day, and Engineering about $6.8 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (generation and water control, construction, DSMS monitoring) | One plant, region, project group, or service stops | Staff slowed but working |
| Regulatory | Missed FERC, NERC, DOE, DoD, or SEC duty, or a reportable condition under 18 CFR 12.10 | Missed contractual or internal deadline | Internal policy deviation |
| Safety | Plausible harm to people downstream of a dam, workers, or the public | Degraded but safe operation | None |
| Reputation | National media, regulator action, or loss of major clients or federal work | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists **27 processes**: 9 Hydro, 7 group shared services, 6 Constructors, and 5 Engineering. **13 are High, 10 Moderate, and 4 Low.**

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-H02 Spillway gate operation and reservoir management | Hydro | High | 4 h | 2 h | 1 h |
| BP-H03 Dam safety monitoring and EAP early warning | Hydro | High | 4 h | 2 h | 1 h |
| BP-H01 Real-time fleet operations at the HOCs | Hydro | High | 4 h | 2 h | 1 h |
| BP-H07 Physical security monitoring and dispatch | Hydro | High | 4 h | 1 h | 1 h |
| BP-H06 Blackstart readiness and restoration support | Hydro | High | 4 h | 2 h | 24 h |
| BP-H04 Unit control and generation at plants | Hydro | High | 8 h | 4 h | 24 h |
| BP-G01 Workforce identity and access (IT) | Group | High | 4 h | 1 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Cloud landing zones and hub networks | Group | High | 8 h | 4 h | 1 h |
| BP-E01 DSMS data collection and alerting | Engineering | High | 8 h | 4 h | 1 h |
| BP-H05 Energy scheduling, trading, and settlements | Hydro | High | 12 h | 4 h | 1 h |
| BP-E04 Emergency engineering support to dam owners | Engineering | High | 8 h | 4 h | 24 h |
| BP-C01 Project execution and field operations | Constructors | High | 48 h | 24 h | 4 h |
| BP-G03 Corporate network, WAN, and jobsite connectivity | Group | Moderate | 24 h | 8 h | 4 h |
| BP-H08 NERC, FERC, and DOE event and compliance reporting | Hydro | Moderate | 24 h | 8 h | 4 h |
| BP-C02 Federal Projects Enclave and CUI work | Constructors | Moderate | 72 h | 24 h | 4 h |
| BP-C03 Pay applications, subcontractor payments, and progress billing | Constructors | Moderate | 72 h | 48 h | 24 h |
| BP-E02 AI anomaly detection (AI-001) | Engineering | Moderate | 24 h | 12 h | 24 h |
| BP-C04 Commissioning and testing at owner sites | Constructors | Moderate | 72 h | 24 h | 24 h |
| BP-C05 Estimating and bidding | Constructors | Moderate | 48 h | 24 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 96 h | 48 h | 24 h |
| BP-G05 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-E03 Engineering design and sealed deliverables | Engineering | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Procurement and vendor payments | Group | Low | 120 h | 72 h | 24 h |
| BP-E05 Field inspections and imagery processing | Engineering | Low | 120 h | 72 h | 24 h |
| BP-H09 Recreation reservations and public information | Hydro | Low | 120 h | 72 h | 24 h |
| BP-C06 Equipment telematics and fleet maintenance | Constructors | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Public safety** drives the Hydro 4-hour MTDs for gate operation, dam safety monitoring, and HOC operations. During a flood, loss of remote gate control is tolerable for only about 1 hour, which is why every gated dam has a local control procedure and on-call crews.
- **Grid obligations** drive HOC operations and blackstart readiness. The 2026-06-13 failover from HOC-A to HOC-B took 2.6 hours against the 2-hour RTO (P01 HY-005).
- **Client commitments** drive the DSMS (BP-E01). 61 external clients use its alerts in their own dam safety programs, and their contracts commit to 99.5% availability.
- **Money more than time** drives Constructors. Project execution is High because a day of idle crews costs about $25.5 million of revenue, but jobsites can work from printed drawings for 2 days.
- **The AI model is not on the critical path, but practice has put it there.** BP-E02 is Moderate because rules-based thresholds keep running without AI-001. However, 31 Hydro dams moved to monthly manual readings in 2026 on the strength of AI-001 alerts. If the model is down, those dams must go back to weekly readings until it returns (P10).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | All IT processes in every division | A group identity outage stops the DSMS, the FPE, scheduling, and project platforms at once. Break-glass accounts per critical system are the fallback. **Hydro OT is not affected** (separate OT identity domain) |
| SOC facts (SYS-G2) | Group | Hydro NERC and FERC reports; Constructors DFARS reports; SEC filing | Every reporting clock in P08 depends on the SOC establishing what happened |
| Cloud platform (SYS-G3) | Group | DSMS (Engineering), FPE (Constructors and Engineering), scheduling (Hydro) | One provider-level incident can affect three divisions' services |
| DSMS analysis (SYS-E1) | Engineering | Hydro dam safety teams (68 dams) | Hydro's alarms run locally, but trend analysis, AI-001 alerts, and reporting come from the DSMS |
| Historian data to the DSMS | Hydro | Engineering | 17 plants use two-way replication, which also gives the DSMS a network path toward Hydro OT DMZs (P01 GR-03) |
| Commissioning and rehabilitation work (BP-C04) | Constructors | Hydro plants (7 active projects) | Construction connections into gate and unit control networks during commissioning (gap 1) |
| Emergency engineering (BP-E04) | Engineering | Hydro Chief Dam Safety Engineer | Breach and inundation analysis during floods and incidents |
| Terminations (BP-G06) | Group | Hydro CIP access removal | CIP-004-7 Part 5.1 requires removal of unescorted physical access and Interactive Remote Access within 24 hours of a termination action |
| CIP-013 procurement (BP-G07) | Group | Hydro OT purchases | The 2025 OEM renewal skipped the CIP-013 terms (gap 9) |

**Single points of failure found:**
- **HOC-A**, mitigated by HOC-B; the failover is slower than the RTO (POAM-008).
- **One governor and excitation OEM** for 55% of Hydro units (P01 GR-08).
- **Cloud provider A** for the DSMS. A warm standby region exists, but a provider-wide identity incident would stop it (accepted at Low, EN-014).
- **One payroll provider** for weekly craft payroll (accepted at Low, GR-16).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-H1 fleet SCADA (HOC-A and HOC-B) | BP-H01, BP-H02 | Real-time replication between HOCs; nightly offline backups at both HOCs; quarterly restore test |
| SYS-H2 and SYS-H3 PLC logic, governor and HMI configurations | BP-H02, BP-H04, BP-H06 | Offline copies after each change; **12 plants have logic backups older than 12 months** (POAM-010) |
| SYS-H4 instrumentation data | BP-H03 | Local data loggers keep 30 days; replicated to the DSMS |
| SYS-G1 identity platform (SaaS) | All IT processes | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs, backup vault | DSMS, FPE, scheduling | Infrastructure as code; immutable backups in provider B |
| SYS-E1 DSMS | BP-E01, BP-E02 | Database replicas; warm standby region on provider A; immutable backups in provider B |
| SYS-C2 FPE | BP-C02 | Provider B government-community region backups; restore tested twice a year |
| People | All | Cross-trained HOC shifts; on-call crews at each gated dam; remote work for most Engineering staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. Spillway gate operation (local control first)
2. Dam safety monitoring and EAP early warning
3. HOC fleet operations (or failover to HOC-B)
4. Physical security monitoring
5. Blackstart readiness
6. Unit control and generation
7. to 10. Group identity, the SOC, the cloud landing zones, and the DSMS
11. to 13. Energy scheduling, emergency engineering support, and Constructors project execution
14. to 27. Corporate network, compliance reporting, the FPE, pay applications, AI-001, commissioning, estimating, payroll, financial close, engineering design, procurement, field inspections, recreation, and telematics.

Steps 1 to 6 do not wait for steps 7 to 10, because Hydro OT does not depend on them.

## 8. Key findings
1. **Hydro's safety-critical processes are independent of corporate IT, and should stay that way.** Two links weaken that independence: the two-way DSMS replication at 17 plants and the Constructors commissioning connections (P01 GR-01, GR-03).
2. **The HOC failover is 30 minutes slower than its RTO.** The 2.6-hour failover in June 2026 needed a manual ICCP restart (POAM-008).
3. **AI-001 has crept onto the dam safety critical path** without being rated as such. The P10 decision restores weekly manual readings until the model passes its conditions.
4. **Reporting capacity is itself a process.** If the SOC or email is down during an incident, the 1-hour CIP-008 clock and the 72-hour DFARS clock keep running. The P08 runbook uses out-of-band channels and a printed contact list for that reason.
