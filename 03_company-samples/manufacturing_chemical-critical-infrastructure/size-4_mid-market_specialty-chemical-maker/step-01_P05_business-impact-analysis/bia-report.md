# Business Impact Analysis: Cris Santos Company | Chemical | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with OT recovery considerations from NIST SP 800-82 Rev. 3 (sec. 6.2.4.3 Backups; sec. 6.5.1 Recovery Planning)
**Prepared by:** GRC Analyst with the vCISO, the Information Security Manager, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-22 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the Port plant (including the marine terminal), the Inland plant, the Distribution center, the Tank Telemetry and Replenishment Service (TTRS), and corporate functions. It rates 18 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and process safety.

The results feed:
- the FIPS 199 availability rating and contingency controls in the SSP for the Process Control and Batch Management System (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the backup and resilience measures the USCG cybersecurity rule requires for critical IT and OT systems (33 CFR 101.650(g)(4)) and the Cybersecurity Assessment due 2027-07-16 (P03);
- the RMP emergency response program and exercises at the Port plant (40 CFR 68.95; 68.96), and immediate release reporting (40 CFR 302.6; 355.40-355.43);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the TTRS SOC 2 readiness assessment (P09).

## 2. System and business description
The company makes and delivers about $410 million a year of specialty chemicals from two Florida plants (see `../00_company-facts.md` sections 1 to 3).
- **Port plant:** about 70% of revenue. Its production runs on the Process Control and Batch Management System (PCBMS), described in the SSP (P02): the DCS, the batch management system, two SIS controllers, terminal and loading automation, and the historian. It is an MTSA-regulated facility, an RMP Program 3 stationary source, and a PSM site.
- **Inland plant:** about 22% of revenue. It runs a PLC and SCADA batch system on a nearly flat network.
- **Business systems:** a SaaS ERP, a 5-account cloud landing zone (LIMS, file services, data platform, TTRS), SaaS identity, email, HR, and fleet systems.

**Safety comes before recovery time.** In an OT outage the first objective is a safe state, not a fast restart. The SIS is independent of the DCS, so the Ammonia and Peroxide Units can be held safe while the DCS is down. Restarting a unit on an untrusted DCS is not an acceptable workaround.

## 3. Impact categories and values
Dollar values are scaled to about $410 million in annual revenue over 250 shipping days, about $1.64 million per shipping day. By process: Blend Hall 1 about $420,000, the Ammonia Unit about $260,000, the Peroxide Unit about $230,000, bulk acid and caustic resale about $240,000, and the Inland plant about $360,000 per shipping day. The remaining $130,000 is toll blending, terminal services, and TTRS fees (about $18,000).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $750,000 of lost shipments, or loss of more than $150,000 of margin | $150,000 to $750,000 of lost shipments | Less than $150,000 |
| Operations | A plant, a production unit, or all shipping stops | One line, one shift, or one service degraded by more than 30% | Staff slowed but working |
| Regulatory | Late release notification, RMP-reportable accident, MTSA breach of security or noncompliance with the FSP, or an enforcement action | Missed record, exercise, or internal deadline under Part 68, PSM, or the FSP | Internal procedure deviation |
| Process safety | Plausible toxic release, decomposition, fire, or injury that could reach workers or the public | Degraded safeguards with compensating manual measures | None |
| Reputation | Community shelter-in-place or evacuation, regional media, loss of a top-10 customer or a water utility contract | Customer complaints or late deliveries | Internal only |

**How loss at MTD was estimated.** Estimated loss is the share of lost shipments that is not recovered, plus extra costs (overtime, third-party supply, demurrage, service credits), over the MTD. The process owners supplied the recovery assumptions: about 30% of lost blended product, 20% of aqua ammonia, 25% of peroxide, 50% of bulk resale, and 30% of Inland output are not recovered, because customers buy elsewhere.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-10 Emergency response and release notification | Port plant (corporate support) | High | 1 | 0.5 | 24 | $0 (regulatory and safety) |
| 2 | BP-06 Process safety monitoring and emergency shutdown | Port plant | High | 8 | 4 | 0 | $76,000 |
| 3 | BP-02 Bulk tank farm, inventory control, and bulk resale | Port plant | High | 12 | 4 | 1 | $65,000 |
| 4 | BP-03 Ammonia Unit | Port plant | High | 24 | 12 | 24 | $92,000 |
| 5 | BP-16 Recipe and formulation management | Corporate | Moderate | 48 | 24 | 24 | $30,000 |
| 6 | BP-05 Blend Hall 1 controlled blending | Port plant | High | 24 | 12 | 24 | $146,000 |
| 7 | BP-15 Order management and customer service | Corporate | High | 24 | 8 | 1 | $82,000 |
| 8 | BP-08 Bulk truck loading and rail shipping | Port plant | High | 24 | 8 | 1 | $45,000 |
| 9 | BP-14 TTRS telemetry and automatic replenishment | Customer solutions | High | 24 | 8 | 1 | $75,000 |
| 10 | BP-04 Peroxide Unit | Port plant | High | 48 | 24 | 24 | $115,000 |
| 11 | BP-12 Inland blending and packaging | Inland plant | High | 48 | 24 | 24 | $216,000 |
| 12 | BP-09 Quality control and batch release | Port plant (both plants) | Moderate | 24 | 8 | 4 | $20,000 |
| 13 | BP-11 Maritime and site security | Port plant | Moderate | 12 | 4 | 24 | $8,000 |
| 14 | BP-13 Distribution and fleet dispatch | Distribution center | Moderate | 24 | 12 | 4 | $25,000 |
| 15 | BP-01 Marine terminal barge receipt | Port plant | Moderate | 72 | 24 | 24 | $45,000 |
| 16 | BP-07 Packaging (Port plant) | Port plant | Moderate | 48 | 24 | 24 | $30,000 |
| 17 | BP-17 Procurement, payables, and receivables | Corporate | Low | 72 | 48 | 24 | $10,000 |
| 18 | BP-18 Payroll and HR | Corporate | Low | 120 | 72 | 24 | $15,000 |

**Summary:** 10 High, 6 Moderate, and 2 Low processes (18 in total). The sum of estimated losses at each process's MTD is $1,095,000.

**Recovery priority is not the same as MTD.** BP-16 (recipes) has a 48-hour MTD but is restored fifth, because Blend Hall 1 and the Inland plant cannot restart without verified recipes. BP-04 has a longer MTD than the Ammonia Unit because pulp and paper customers hold more stock than water utilities.

**Two enterprise scenarios** (for P01 and P08):
- **Port plant OT intrusion, 7 days down** (Ammonia Unit, Peroxide Unit, Blend Hall 1, and the tank farm held safe; P08 runbook 1): unrecovered revenue about $2.5 million (Port production of about $1.15 million a day x 7 days x about 30% not recovered), plus about $400,000 of third-party aqua ammonia and peroxide bought to protect water utility and pulp customers. Forensics, rebuild, and regulatory costs come on top (P01 R-001, R-002).
- **Corporate ransomware, 72 hours** (identity provider, endpoints, file services, LIMS, and TTRS degraded; ERP vendor unaffected but unreachable without SSO; P08 runbook 2): both plants keep running in a safe state, but shipping drops to about 60% on paper. Unrecovered revenue about $590,000, plus about $150,000 of overtime and about $30,000 of TTRS service credits. Breach notification and incident response costs come on top (P01 R-003).

**What drives the values:**
- **Safety and regulation, not revenue,** drive BP-10 (1 hour) and BP-06 (8 hours). Release notices are due immediately. The Port plant emergency response team must be able to warn the community even if the business network is down.
- **Water utility customers** drive the 24-hour MTDs for the Ammonia Unit (BP-03), bulk loading (BP-08), and TTRS (BP-14). Utilities hold only 3 to 5 days of treatment chemicals, and TTRS is how the company knows which ones are running low.
- **Recipes and configuration, not hardware,** limit BP-05 and BP-12. Spare DCS hardware is on site at the Port plant. What cannot be replaced quickly is a clean, verified configuration, about 600 Port master recipes, and the Inland PLC programs.
- **The 1-hour RPOs** for BP-08, BP-14, and BP-15 come from the ERP vendor's replication (stated in its SOC 2 report, P09 Part B) and the TTRS database's point-in-time recovery.

## 5. Key findings
1. **The 12-hour RTO for the Ammonia Unit and Blend Hall 1 is unproven.** Weekly offline copies of the DCS, batch, and SIS configurations sit in the Port plant fire safe, which is a real strength. Only one operator station has ever been restored, and no full DCS restore has been tested (gap 5; P01 R-006; P07 CP-4, CP-10). Until a full restore is done on spare hardware, the realistic recovery time after a destructive attack is several days.
2. **The Inland plant could lose its PLC programs.** The only current copies of 14 PLC programs are on one controls engineer's laptop (gap 5; P01 R-007). If that laptop is lost or encrypted, the integrator would have to rebuild the programs from 2023 project files. That would take weeks, well beyond the 48-hour MTD for BP-12.
3. **Emergency notification depends partly on the business network.** The control room uses VoIP phones on the business network, and the community notification system is launched from a web console. Radios and cellular phones exist, but the printed call list is out of date (P01 R-014; P03 68.95 rows).
4. **TTRS has no tested failover.** The TTRS account runs in one cloud region. Its 99.5% availability commitment is not measured, and the manual workaround (phone readings for 160 water utility sites) has never been drilled (gap 11; P01 R-021; P09 A1.2, A1.3).
5. **ERP vendor objectives meet the BIA.** The ERP vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour, which meets BP-08, BP-13, and BP-15. The weak point is access: if the identity provider is down, nobody can sign in. Break-glass ERP accounts are needed (P01 R-020; P04).
6. **The historian, AI-001, and AI-003 are not on the recovery path.** The plants run without them. They are restored last, from clean media, after integrity checks (P10).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 DCS and SYS-02 batch management (Port) | 4 redundant controller pairs, redundant servers, 8 operator stations, 2 EWS; about 600 recipes | BP-02 to BP-05, BP-16 |
| SYS-03 SIS (Port) | Two safety controllers, gas and temperature detection, emergency shutdown valves, UPS | BP-03, BP-04, BP-06 |
| SYS-04 Terminal and loading automation | Dock transfer PLC and emergency shutdown, radar tank gauging, 6 loading bays | BP-01, BP-02, BP-08 |
| SYS-05 Historian and SYS-06 OT networks | OT DMZ, firewall pair, control and SIS networks | BP-02 to BP-06 |
| SYS-07 OT remote access gateway | Vendor and engineer remote sessions | Vendor support during recovery |
| SYS-08 Inland batch control | 14 PLCs, SCADA server, 4 HMIs | BP-12 |
| SYS-09 ERP (SaaS) | Orders, inventory, bills of materials, shipping papers | BP-08, BP-13, BP-15 to BP-17 |
| SYS-10 LIMS and SYS-11 landing zone | QC results, file services, data platform, backups | BP-09, BP-16 |
| SYS-12 TTRS | Telemetry, portal, replenishment engine, AI-004 | BP-14 |
| SYS-13 Identity provider | SSO and MFA for all IT and SaaS | All business processes |
| SYS-14 Productivity suite and VoIP | Email, chat, phones | BP-10, BP-15 |
| SYS-17 Physical security systems | Badge and TWIC readers, cameras | BP-11 |
| SYS-18 HR and payroll; SYS-19 fleet management | Payroll, terminations; dispatch and telematics | BP-13, BP-18 |
| Utilities | Grid power; UPS on the DCS, SIS, and control room; one generator at the Port plant for the control room and emergency lighting; cellular service | All |
| People | Controls Engineering Manager and 4 controls engineers (one at the Inland plant is a single point of knowledge), I&E technicians, emergency response team, DCS integrator, SIS vendor | BP-02 to BP-06, BP-12 |

## 7. Regulatory linkage
The BIA supplies inputs that several binding rules expect. The full analysis is in P03.

| Rule (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| 33 CFR 101.650(g)(4): back up critical IT and OT systems, with backups protected and tested frequently | The critical systems and recovery order below; RPO and RTO for each process | Port backups exist; testing gap (finding 1); Inland gap (finding 2) |
| 33 CFR 101.650(e)(1): Cybersecurity Assessment by 2027-07-16, analyzing the risk posed by each digital asset | Process criticality and dependent systems for every Port plant process | Input ready; assessment not started (P03) |
| 40 CFR 68.95(a)(1)(i) and (c): procedures to inform the public and response agencies, with timely release data | BP-10 MTD 1 hour, independent of the business network | Gap: printed call list out of date (finding 3) |
| 40 CFR 68.96(b)(2)(i): tabletop exercise before 2026-12-21 | Cyber-caused release scenario for the tabletop (P08 runbook 1) | Planned for 2026-11-17 |
| 40 CFR 68.73(a)(4)-(5); 29 CFR 1910.119(j)(1)(iv)-(v): emergency shutdown systems and controls are mechanical integrity equipment | BP-06 RPO 0 for SIS logic | SIS logic compare not routine (P07 CM-5) |
| 49 CFR 172.802(a)(3): en route security for 50% peroxide shipments | BP-08 and BP-13 dependencies (ERP shipping papers, telematics) | DOT plan update due (P03) |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency notification and response (BP-10) | 0.5 h | Radios, cellular and satellite phones, printed call lists in the control room, gatehouse, and response vehicle |
| 2 | SIS verified and units in a safe state (BP-06) | 4 h | Manual isolation, portable detection, standby watch |
| 3 | Tank farm level monitoring (BP-02) | 4 h | Manual gauging each shift; SIS high-level trips stay active |
| 4 | Ammonia Unit on a verified DCS (BP-03) | 12 h target, **unproven** | Ship from aqua ammonia in storage; third-party supply for water utilities |
| 5 | Clean DCS configuration and recipes (BP-16) | 24 h | Weekly offline copy; printed recipe cards for the top 60 formulations |
| 6 | Blend Hall 1 restart (BP-05) | 12 h after step 5 | Top 15 formulations at the Inland plant |
| 7 | Identity provider with break-glass accounts, then ERP access (BP-15) | 8 h | Paper orders from the last ERP extract |
| 8 | Loading bays and shipping papers (BP-08) | 8 h | Local mode with two-person verification; pre-printed papers |
| 9 | TTRS (BP-14) | 8 h | Daily phone readings for the 160 water utility tanks |
| 10 | Peroxide Unit (BP-04) | 24 h | Ship 50% product from storage |
| 11 | Inland batch control (BP-12) | 24 h target, **not achievable today** | Manual batching for the top 30 products |
| 12 | LIMS (BP-09) | 8 h | Paper worksheets and typed certificates |
| 13 | Physical security systems (BP-11) | 4 h | Guards at gates and the dock |
| 14 | Fleet dispatch (BP-13) | 12 h | Paper dispatch sheets |
| 15 | Dock transfer PLC (BP-01) | 24 h | Delay barges |
| 16 | Port packaging lines (BP-07) | 24 h | Manual filling |
| 17 | Finance (BP-17) | 48 h | Queue invoices |
| 18 | Payroll (BP-18) | 72 h | Repeat prior payroll |

The historian (SYS-05), the cloud data platform, AI-001, and AI-003 are restored after priority 18, from clean media, with one-way replication only.
