# Business Impact Analysis: Cris Santos Company | Energy | Micro

**Organization:** Cris Santos Company, LLC (small intrastate natural gas transmission pipeline operator) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (security program coordinator) with the Operations Manager, the Gas Scheduler, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** Owner, 2026-09-15

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the recovery order and the operate-or-shut-in decision in the incident response runbook (P08);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the emergency plan (49 CFR 192.615) and the abnormal operation procedures for loss of communications (192.605(c)(1)(iii)).

**What does not drive this BIA.** 49 CFR 192.631(c)(3) and (c)(4) (annual tests of manual operation and backup SCADA) do not bind this company: its control room is limited to transmission without a compressor station, so 192.631(a)(1)(ii) limits its procedures to paragraphs (d), (i), and (j) (see P03). The company plans for manual operation anyway, because the emergency plan and the abnormal operation procedures need it.

## 2. System and business description
The company moves natural gas through about 26 miles of intrastate transmission line in Florida, from one tap on an interstate pipeline to 3 delivery stations: a municipal gas system serving about 9,000 homes and businesses, a ceramic tile plant, and a food processing plant. There is no compressor station. Delivery pressure is held by mechanical regulators at each station.

Seven people run the company. The SCADA host is a hosted service run by the SCADA vendor (SYS-01). Controllers reach it from 2 gas control desk workstations in the office (SYS-02) or, after hours, from their company laptops. The 7 field sites report over one cellular carrier (SYS-04). The MSP runs office IT. See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 per day. For this company, safety and supply to the municipal system matter far more than lost revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25,000 (contract claims, relight costs for the municipal system, or emergency contractor costs) | $5,000 to $25,000 | Less than $5,000 |
| Operations | Deliveries to the municipal gas system interrupted or curtailed | Deliveries continue under manual operation or with estimated data | Staff slowed but working |
| Regulatory | Reportable incident under 49 CFR Part 191, or an FPSC enforcement action | Missed compliance record or interval | Internal procedure deviation |
| Safety | Plausible harm to the public or workers (undetected release, overpressure, loss of gas to homes followed by unsafe relighting) | Degraded monitoring covered by field staff | None |
| Reputation | Regional media coverage; loss of the municipal contract | Customer complaints; escalation by the upstream pipeline | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Gas control (SCADA monitoring and control) | High | 8 h | 2 h | 1 h |
| BP-02 Emergency response and public safety communication | High | 1 h | 15 min | 0 |
| BP-03 Gas scheduling and nominations | Moderate | 24 h | 8 h | 4 h |
| BP-04 Gas measurement and customer volume reporting | Moderate | 72 h | 48 h | 24 h |
| BP-05 Field O&M, corrosion control, and compliance records | Moderate | 72 h | 48 h | 24 h |
| BP-06 Customer billing and accounting | Low | 120 h | 72 h | 24 h |
| BP-07 Payroll and HR | Low | 120 h | 72 h | 24 h |
| BP-08 Leak-detection anomaly alerts (trial, advisory) | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Public safety drives BP-01 and BP-02.** Controllers must see pressures and alarms to detect a rupture and act. Emergency communication cannot pause: 49 CFR 191.5 requires notice within one hour after confirmed discovery of an incident.
- **The 8-hour MTD for gas control is a staffing limit.** The company has 4 field-qualified people. Two pairs can man the receipt station and the municipal gate station for about one shift. After that, the Operations Manager would reduce pressure and ask the municipal system to prepare for curtailment.
- **Measurement and billing are not time-critical.** Flow computers keep about 35 days of hourly data, and invoices are monthly.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Hosted SCADA service | SCADA host, historian, alarm callout, web client | Vendor replication between two data centers; vendor SOC 2 report states RPO 15 minutes and RTO 4 hours (see finding 2) | BP-01, BP-04, BP-08 |
| SYS-02 Gas control desk | 2 office workstations | None needed (no local data); rebuilt by the MSP | BP-01 |
| SYS-03 Field devices | 7 RTUs, 4 flow computers, RCV actuators | Flow computers keep 35 days locally; RTU programs only on the Operations Manager's laptop (**no second copy**) | BP-01, BP-04 |
| SYS-04 Cellular telemetry | 7 gateways, one carrier | None; carrier outage stops all telemetry | BP-01 |
| SYS-05 Laptops and tablets | Controller laptops for after-hours SCADA | No local data by design | BP-01, BP-03, BP-05 |
| SYS-06 Office network | Firewall, Wi-Fi, one fiber line | Firewall configuration backed up by the MSP | BP-01 (in business hours), BP-03 |
| SYS-07 and SYS-09 Productivity suite and its backup | Email, shared drive with records and maps | Nightly backup, 30 days of versions; **never restore-tested** | BP-03, BP-05 |
| SYS-08 Accounting SaaS and payroll service | Billing, payables, payroll | Vendor resilience | BP-06, BP-07 |
| SYS-11 Interstate pipeline portal | Nominations | Operated by the interstate pipeline | BP-03 |
| People | 3 qualified controllers; 4 field-qualified staff; Office Manager; Gas Scheduler | Cross-training: the Operations Manager covers scheduling; the Office Manager covers customer calls | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Hosted SCADA vendor | BP-01, BP-04, BP-08 | SOC 2 Type 2 report reviewed for the first time in 2026 (P09): RTO 4 h and RPO 15 min. **The RTO does not meet the 2-hour BIA target** |
| Cellular carrier | BP-01 (all field telemetry) | Standard business terms; no restoration commitment |
| MSP | Recovery of the gas control desk and office IT; operates the suite backup | No recovery commitment; the contract has a 4-business-hour response time only |
| Internet provider | BP-01 from the gas control desk; BP-03 | None; single line. Controller laptops on phone hotspots are the fallback |
| Productivity suite vendor and backup service | BP-03, BP-05 | Vendor service terms; backup never restore-tested |
| Upstream interstate pipeline | Gas supply; BP-03 | Interconnect operating agreement; its gas control desk is reachable by phone 24x7 |

**Key findings:**
1. **An office IT outage does not, by itself, make the pipeline unsafe.** Gas keeps flowing and the regulators keep holding pressure. But the gas control desk sits on the flat office network (gap 3 in the company facts), so ransomware in the office also takes away the controllers' main SCADA screens. A clean spare laptop with a phone hotspot, kept off the office network, would restore the SCADA view in minutes. Today there is none (P01 R-001; P08).
2. **The SCADA vendor's stated RTO (4 hours) misses the 2-hour target for gas control.** Manual operation must cover hours 2 to 4 of any vendor outage. The company accepts this only with a tested manual operation call list (P01 R-019).
3. **One cellular carrier serves all 7 field sites.** A carrier outage removes all telemetry at once (P01 R-008). Second-carrier SIMs at the receipt station and the municipal gate station are planned.
4. **RTU programs exist only on one laptop.** If that laptop is lost or encrypted, a failed RTU cannot be restored quickly (P01 R-009).
5. **The MSP contract has no recovery time.** Its 4-business-hour response time is not a recovery commitment. The MSP contract amendment in P01 R-004 adds a recovery time for the gas control desk.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency communications (phones, printed contact list) | 15 min | Personal cell phones; printed lists in trucks and at home |
| 2 | Trusted SCADA view and control (SYS-01 through a clean device; SYS-04 telemetry) | 2 h | Clean spare laptop on a phone hotspot (to be set up by 2026-10-31); manual operation at the receipt station and municipal gate station |
| 3 | Nominations (SYS-11) and email (SYS-07) | 8 h | Phone confirmations with the interstate pipeline's scheduling desk |
| 4 | Measurement data (SYS-03 through SYS-01) | 48 h | Flow computer downloads on site |
| 5 | Records and maps (SYS-07, SYS-09) | 48 h | Printed O&M manual, emergency plan, and maps |
| 6 | Billing (SYS-08) | 72 h | Invoice from prior month's volumes |
| 7 | Payroll (SYS-08 and payroll service) | 72 h | Repeat prior payroll |
| 8 | Leak-detection alerts (SYS-01 module) | After revalidation | SCADA alarms and field methods (P10) |
