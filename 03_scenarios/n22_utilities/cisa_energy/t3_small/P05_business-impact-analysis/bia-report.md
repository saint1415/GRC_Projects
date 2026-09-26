# Business Impact Analysis: Cris Santos Company | Energy | Small

**Organization:** Cris Santos Company, LLC (intrastate natural gas transmission pipeline operator) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Gas Control Manager, Field Operations Manager, Commercial Manager, and Finance Manager | **Approved:** President, 2026-09-24

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the recovery and isolation objectives in the cybersecurity incident response plan (P06 POL-03 and the P08 runbook);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the manual operation and backup SCADA duties in 49 CFR 192.631(c)(3) and (c)(4), and the emergency plan in 192.615.

## 2. System and business description
The company moves natural gas through about 185 miles of intrastate transmission line in Florida, from one receipt interconnect to 14 delivery points serving 2 local distribution companies (LDCs), a power plant, and 6 industrial plants. Six gas controllers run the pipeline 24x7 from the Gas Control Center through the Pipeline SCADA and Gas Control System (PSGCS). A backup control room sits at Compressor Station 1. Business IT (email, ERP, nominations portal, and the cloud-hosted measurement application) is separate from OT behind a firewall pair and DMZ. See `../scenario-facts.md` sections 3 and 4.

## 3. Impact categories and values
Dollar values are scaled to $24.9 million in annual revenue, about $68,000 per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $200,000 (about 3 days of revenue), or contract penalties and imbalance charges above that | $50,000 to $200,000 | Less than $50,000 |
| Operations | Deliveries to an LDC or the power plant interrupted or curtailed | Deliveries continue but with manual operation, reduced pressure, or estimated data | Staff slowed but working |
| Regulatory | Reportable incident under 49 CFR Part 191, or FPSC enforcement | Missed compliance record or interval (for example a 15-month interval under 192.631) | Internal procedure deviation |
| Safety | Plausible harm to the public or workers (overpressure, undetected release, loss of gas supply to homes during cold weather) | Degraded monitoring with compensating field coverage | None |
| Reputation | Regional media coverage; loss of an LDC or power plant customer | Customer complaints; upstream pipeline escalation | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Gas control (SCADA monitoring and control) | High | 8 h | 2 h | 1 h |
| BP-02 Compressor station operation | High | 12 h | 4 h | 24 h |
| BP-03 Emergency response and public safety communication | High | 1 h | 15 min | 0 |
| BP-04 Gas scheduling and nominations | High | 24 h | 12 h | 4 h |
| BP-05 Gas measurement and custody transfer data | Moderate | 72 h | 48 h | 24 h |
| BP-06 Leak detection analytics (advisory) | Moderate | 72 h | 24 h | 24 h |
| BP-07 Customer billing and gas accounting | Low | 120 h | 72 h | 24 h |
| BP-08 Field O&M, integrity, and compliance records | Moderate | 72 h | 48 h | 24 h |
| BP-09 Payroll, HR, and finance | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Public safety drives BP-01 and BP-03.** Controllers must see pressures and alarms to detect a rupture and act. The 8-hour MTD for gas control is how long field staff can hold the line safely in manual operation. After that, the company would reduce pressure and curtail deliveries. Emergency communication cannot pause because 49 CFR 191.5 requires notice within one hour of confirmed discovery of an incident.
- **Customer supply drives BP-02 and BP-04.** Nominations run on the gas day. Missing a nomination cycle creates imbalance charges and puts next-day deliveries at risk.
- **Billing is not time-critical.** BP-07 can stop for 5 days. Measurement data is safe in the flow computers for about 35 days.

**Key finding: a billing or business IT outage alone does not justify shutting down the pipeline.** Gas control (BP-01) can run without any business IT system. The only business IT dependencies that matter within the first day are email and phones for emergency communication (BP-03) and the nominations portal (BP-04), and both have manual workarounds. A precautionary shutdown is justified only when the company cannot confirm that OT is isolated and trustworthy (see P08). Today it cannot confirm that quickly, because it has no OT network monitoring (gap 6) and the jump host is shared (gap 4).

**Second finding: the SCADA recovery objectives are unproven.** The backup control room failover was tested in November 2025, which supports the 2-hour RTO for BP-01 if the backup host is clean. But SCADA server backups sit on a storage device inside the OT network and have never been restored to new hardware (gap 7). If ransomware reached OT, the 2-hour RTO could not be met (risk R-004 in P01).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 SCADA hosts, HMI consoles, historian | Primary gas control | BP-01, BP-02, BP-05, BP-06 |
| SYS-02 Backup SCADA host and backup control room | Warm standby at Compressor Station 1 | BP-01 |
| SYS-03 Field RTUs, PLCs, flow computers | Field data and remote control; local measurement archive | BP-01, BP-02, BP-05 |
| SYS-04 Radio and cellular telecommunications | SCADA polling; 9 sites are cellular-only | BP-01, BP-03 |
| SYS-05 IT/OT DMZ | Historian replica, patch staging, remote access jump host | BP-05, BP-06 |
| SYS-07 Identity provider and SYS-08 productivity suite | Email, files, sign-in for business systems | BP-03, BP-04, BP-08 |
| SYS-09 Cloud tenant | Measurement application, leak analytics, backup vault | BP-05, BP-06, BP-07 |
| SYS-10 ERP and payroll SaaS | Billing, accounting, payroll | BP-07, BP-09 |
| SYS-11 Nominations portal | Daily nominations and confirmations | BP-04 |
| People | 6 controllers plus the Gas Control Manager as relief; 26 field staff for manual operation; SCADA Engineer; IT Manager and MSP | All |
| Facilities | Gas Control Center (HQ), Compressor Station 1, two field offices | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency communications (phones, radio, printed contact lists) | 15 min | Personal cell phones and radio; printed lists at each site |
| 2 | SYS-01 or SYS-02 SCADA (clean host) and SYS-04 telecommunications | 2 h | Manual operation plan with field technicians at key sites |
| 3 | SYS-03 compressor station control | 4 h | Local panel operation |
| 4 | SYS-11 nominations portal and SYS-08 email | 12 h | Phone nominations and spreadsheet; phone confirmation with the upstream pipeline |
| 5 | SYS-09 measurement application | 48 h | Flow computer archives downloaded on site |
| 6 | SYS-06 business endpoints for field records | 48 h | Printed maps and paper work orders |
| 7 | SYS-09 leak analytics | 24 h after historian replica is clean | SCADA alarms and line-pack trending |
| 8 | SYS-10 ERP and billing | 72 h | Estimated invoices |
| 9 | Payroll | 72 h | Repeat prior payroll |

Leak analytics (priority 7) has a shorter RTO than billing but is restored after the measurement application, because it depends on a clean historian replica in the DMZ and must be revalidated before controllers rely on it again (P10).
