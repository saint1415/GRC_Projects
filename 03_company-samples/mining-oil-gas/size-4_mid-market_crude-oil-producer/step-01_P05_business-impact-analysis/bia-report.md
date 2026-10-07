# Business Impact Analysis: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Mid-Market

**Organization:** Cris Santos Company, Inc. (independent crude oil producer with a Panhandle gathering system) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with the OT availability considerations of NIST SP 800-82 Rev. 3 (sections 3.3.9 and 5.3.2)
**Prepared by:** GRC Analyst and Security Manager with the process owners named in `bia.csv`, the SCADA and Automation Manager, the Control Room Manager, and the 3 Field Superintendents | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-16 (field-operations values agreed by the VP Operations; presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: field operations in the 3 operating areas (Panhandle, South Florida, Southwest Alabama), the control room (OCC and BCC), gathering and measurement, production accounting, finance, engineering and field services, and corporate support. It rates 16 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and safety and environmental harm.

The results feed:
- the contingency and recovery planning that the benchmark calls for (CSF 2.0 RC.RP; SP 800-82 Rev. 3 section 3.3.9);
- the availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the gathering system linkage to the Part 195 reporting duties (section 7 and P03);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

For an oil producer, "downtime" has two layers. SCADA can be down while the wells keep running, because field controllers work on local logic and the safety shutdowns are hardwired. The real limit is how long people can run the fields and the gathering system by hand before wells must be shut in or the trunk line shut down. The values below reflect that.

## 2. System and business description
The company operates 640 wells and 24 facilities in 3 operating areas, producing about 9,800 barrels of oil per day and reinjecting or disposing of about 340,000 barrels of produced water per day. Field controllers report over licensed radio, microwave, and cellular links to the SCADA servers at the 24x7 Operations Control Center (OCC) in the Panhandle, with a Backup Control Center (BCC) at the Alabama field office. In the Panhandle, crude moves through the company's 92-mile gathering system to 6 LACT units and a third-party transmission pipeline; in South Florida and Alabama it leaves by purchaser trucks. Daily volumes flow through the cloud landing zone to the production accounting SaaS, which pays about 14,000 royalty owners and bills 22 partners each month. See `../00_company-facts.md` sections 1 to 4.

## 3. Impact categories and values
Dollar values are scaled to about $265 million in annual revenue: about $660,000 of crude oil sales per day (Panhandle $375,000, South Florida $140,000, Alabama $140,000), about $36,000 per day of gas and liquids, and about $16,000 per day of gathering fees.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 of lost or deferred sales or extra cost | $25,000 to $100,000 | Less than $25,000 |
| Operations | An operating area shut in, the gathering trunk line shut down, or water handling stopped | One facility stops, or throughput drops by more than 20% | Staff slowed but production continues |
| Regulatory | Reportable pipeline accident or oil discharge, permit violation, or breach notice to regulators | Late state production report or missed contract deadline | Internal policy deviation |
| Safety and environment | Plausible injury, H2S exposure, or a release of oil or produced water | Degraded safety monitoring with compensating patrols | None |
| Reputation | Regional media, loss of a shipper, purchaser, lender, or partner's confidence, or royalty owner complaints to regulators | Owner, shipper, or partner complaints | Internal only |

**How loss at MTD was estimated.** Estimated loss is extra labor (overtime and contract crews) plus production deferred or lost during the MTD, valued at the full sales price. The values are conservative: most deferred barrels are produced later, but restarts, flush production limits, and well damage make some of it a true loss. Cash that is only delayed (royalty and partner billing cycles) is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Emergency alarm call-out, H2S monitoring, and release reporting | Field operations | High | 4 | 2 | 24 | $25,000 |
| 2 | BP-02 Produced water injection and disposal | Field operations | High | 8 | 4 | 24 | $60,000 |
| 3 | BP-03 Well monitoring and remote control | Control room | High | 24 | 12 | 24 | $160,000 |
| 4 | BP-04 Gathering system operation and pipeline safety monitoring | Gathering and measurement | High | 8 | 4 | 24 | $15,000 |
| 5 | BP-05 Custody transfer measurement and shipper volume statements | Gathering and measurement | High | 48 | 24 | 1 | $40,000 |
| 6 | BP-06 Truck custody transfer: tank gauging and run tickets | Field operations | High | 72 | 24 | 4 | $30,000 |
| 7 | BP-07 Associated gas compression and sales | Field operations | Moderate | 24 | 12 | 24 | $60,000 |
| 8 | BP-08 Production allocation and state production reporting | Production accounting | Moderate | 120 | 72 | 24 | $25,000 |
| 9 | BP-09 Royalty and revenue distribution and joint interest billing | Production accounting | Moderate | 120 | 72 | 24 | $40,000 (plus about $23 million a month of payments and billings delayed) |
| 10 | BP-10 Well servicing and maintenance dispatch | Engineering and field services | Moderate | 72 | 48 | 24 | $45,000 |
| 11 | BP-11 Pipeline compliance records and reporting | Gathering and measurement | Moderate | 120 | 72 | 24 | $5,000 |
| 12 | BP-12 Treasury, payables, and crude sales settlement | Finance | Low | 120 | 72 | 24 | $10,000 |
| 13 | BP-13 Payroll and HR | Corporate support | Low | 120 | 72 | 24 | $15,000 |
| 14 | BP-15 Water and fluid hauling dispatch | Field operations | Moderate | 24 | 12 | 24 | $20,000 |
| 15 | BP-16 Email, collaboration, and document management | Corporate support | Moderate | 48 | 24 | 24 | $10,000 |
| 16 | BP-14 Reservoir and geoscience analysis | Engineering and field services | Low | 240 | 120 | 24 | $5,000 |

**Summary:** 6 High, 7 Moderate, and 3 Low processes (16 in total). The sum of estimated losses at each process's MTD is $565,000.

**Enterprise-wide scenario.** If ransomware reached both the OCC and the BCC and SCADA plus business IT were down for 72 hours, the company would run all 3 areas by hand. About 15% of production would be lost on day 1 and about 40% on days 2 and 3 as the 180 cellular sites and then the gathering trunk line are shut in, for about $630,000 of deferred crude sales, plus about $180,000 of overtime and contract crews and about $90,000 of well restart and repair costs. Incident response, legal, and breach notification costs come on top (P01 R-001 and R-002).

**What drives the values:**
- **Safety and environment** drive BP-01 and BP-04. Hardwired shutdowns work without SCADA, but remote call-out and trunk line pressure monitoring are how people learn about a release. A release on the regulated trunk line carries a 1-hour telephone notice (section 7).
- **Water, not oil,** drives BP-02. Storage fills in about 8 hours at full rate, and then every producing well in that area must be shut in.
- **Measurement integrity** drives BP-05 and BP-06. These are the only processes with short RPOs (1 and 4 hours), because LACT tickets and run tickets are the basis for sales, shipper statements, and royalties.
- For SCADA-based processes (BP-01 to BP-04, BP-07), the RPO is the age of the last good copy of the SCADA configuration and controller programs. Process data from an outage period cannot be recovered and is rebuilt from field logs.

## 5. Key findings
1. **The BCC is not yet a proven recovery site.** The BIA assumes the BCC can take over BP-03 and BP-04 within the 12-hour and 4-hour RTOs. The last failover test (2023) was partial, and the BCC standby server runs an unsupported operating system on a network without an OT DMZ (gaps 1, 4, 6 in `../00_company-facts.md`). Until a full failover test passes, the RTOs for BP-03 and BP-04 are targets, not demonstrated capabilities (P01 R-003, R-014; P07 CP-4, CP-7).
2. **A ransomware event that reaches the BCC could destroy the offline SCADA images.** The weekly offline images are stored at the BCC, which connects to the corporate network through broad site firewall rules. A second copy must be stored where no network can reach it (P01 R-003).
3. **The gathering system has an 8-hour MTD for monitoring, not for flow.** Hardwired high-pressure shutdowns keep the trunk line below MOP without SCADA, but the company's own procedure shuts the trunk line down if pressure and flow monitoring cannot be restored or staffed within 8 hours. After the 2-day storage buffer, Panhandle production (about $375,000 per day) stops.
4. **Measurement and shipper commitments depend on systems outside the OT DMZ.** The shipper portal and measurement data service run in the cloud; flow computers hold their own records, which makes the 1-hour RPO achievable for tickets but not for the portal statements. The largest shipper has asked for SOC 2 assurance over this service (P09).
5. **The production accounting vendor's commitments meet BP-08 and BP-09.** Its SOC 2 report states an RTO of 24 hours and an RPO of 1 hour, inside the 72-hour and 24-hour targets (P09 vendor review).
6. **Compression depends on a vendor path.** The compressor packager's always-on cellular gateways (gap 3) are the support path for BP-07; removing them needs a jump host alternative so that vendor support is not lost.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 SCADA control centers | Primary server pair, historian, 12 HMIs, and 4 engineering workstations at the OCC; 3 HMIs at the South Florida office; standby server and 4 HMIs at the BCC | BP-01 to BP-05, BP-07 |
| SYS-02 Field devices and communications | About 610 RTUs and PLCs, 130 ESP drives, 260 flow meters, 6 LACT flow computers, pump station PLC, licensed radio, 180 cellular modems, 2 microwave links | BP-01 to BP-07 |
| SYS-08 Corporate and OT networks | SD-WAN, OT DMZ at the OCC, site firewalls at the field offices and BCC | All |
| SYS-12 OT remote access | Jump host with MFA and session recording; packager and flow computer vendor exceptions | BP-03, BP-05, BP-07 (support) |
| SYS-14 Measurement and shipper services | Measurement data service and shipper portal | BP-05 |
| SYS-05 Identity provider | Single sign-on and MFA for SaaS, cloud, and the jump host | BP-05, BP-06, BP-08 to BP-16 |
| SYS-04 Cloud landing zone | OT data account, business workloads account (field data capture app, volume integration, shipper portal, data platform, ML workspace), backup account | BP-05, BP-06, BP-08, BP-10, BP-11, BP-14 |
| SYS-09 Rugged tablets and smartphones | 240 tablets for gauging and run tickets; smartphones for drivers | BP-06, BP-15 |
| SYS-03 Production accounting SaaS | Allocations, royalties, joint interest billing, shipper invoicing | BP-06, BP-08, BP-09 |
| SYS-06 ERP SaaS | Work orders, payables | BP-10, BP-12 |
| SYS-10, SYS-11 HR and payroll; telematics | Payroll; driver dispatch and hours | BP-13, BP-15 |
| SYS-13 Security tooling | SIEM and MDR, OT sensors | Recovery validation |
| Third parties | SCADA integrator, compressor packager, flow computer vendor, cellular carrier, electric utilities, transmission pipeline, crude purchasers, shippers, production accounting vendor, cloud provider, MDR provider | As listed in `bia.csv` |
| People and facilities | Production Controllers at the OCC and BCC, lease operators, gathering operators, injection plant operators, automation technicians, HSE on-call | BP-01 to BP-07 |

## 7. Gathering system linkage (49 CFR Part 195)
The gathering system is the only part of the business with a binding federal pipeline safety rule (P03 section 1). The BIA supplies the availability values that the pipeline emergency procedures and the reporting duties depend on.

| Part 195 duty (verified on eCFR, 2026-09-23 version, summarized) | Applies to | What this BIA supplies | Status |
|---|---|---|---|
| 195.11(b)(5): establish the MOP of a regulated rural gathering line under 195.406 | 14-mile trunk line | The hardwired high-pressure shutdown switches and the SCADA pressure setpoints are the controls that keep operation at or below MOP; BP-04 records the 8-hour monitoring limit | MOP established; cyber protection of setpoints in P02 (CM-3, CM-5) |
| 195.52: telephone notice to the National Response Center at the earliest practicable moment, no later than 1 hour after confirmed discovery, for accidents meeting the listed criteria | Regulated trunk line (195.15(c)(2) exempts reporting-regulated-only lines from 195.52) | BP-01 and BP-04 call-out paths; printed NRC contact sheets at the OCC and pump station | Linked to cyber events in P08 |
| 195.50 and 195.54: accident report within 30 days of discovery for releases meeting 195.50 | Regulated trunk line and reporting-regulated lines (195.15) | BP-11 records and BP-04 volume data needed to estimate the release | Procedure exists; data sources depend on SYS-14 |
| 195.49: annual report | All 92 miles | BP-08 and BP-11 | Filed each June |
| 195.11(d): record retention (life of pipe for segment identification and internal corrosion records) | Regulated trunk line | BP-11 RPO 24 hours; records in SYS-07 and the data platform are backed up to the backup account | Restore never tested for these records (P07 CP-4) |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Field safety call-out (HSE on-call phone tree, roving patrols, line riders for the trunk line) | Immediate | Printed HSE and pipeline emergency binders at each field office, the OCC, and the pump station |
| 2 | Gathering pump station and injection plant controllers on local panels | 2 h (pump station), 4 h (plants) | Local operation by station and plant operators; hardwired high-pressure shutdowns |
| 3 | SCADA servers and OCC HMIs from a clean, verified image (or failover to the BCC if it is clean) | 12 h (target; full restore and BCC failover untested) | Manual operations; shut-in order set by the Field Superintendents |
| 4 | Field communications (radio, microwave, cellular private network) | 12 h | Manual operations |
| 5 | Identity provider and break-glass accounts | 4 h, in parallel with priorities 2 to 4 | Break-glass accounts sealed offline |
| 6 | LACT flow computers and measurement data service | 24 h | Paper tickets from flow computer front panels |
| 7 | Compression station controllers | 12 h | Local panel operation; curtail high gas-oil-ratio wells |
| 8 | Field data capture app and tablets | 24 h | Paper run tickets |
| 9 | Shipper portal | 24 h | Statements by email from the Measurement Supervisor |
| 10 | Volume integration service and production accounting | 72 h | Rebuild volumes from tickets and meter data |
| 11 | ERP, payroll, finance, telematics | 72 h | Whiteboard dispatch; repeat prior payroll; manual payments with call-back |
| 12 | Data platform and ML workspace | 120 h | Defer analysis |

Recovery priority 3 depends on an image that is isolated from every network and has been restore-tested, and on a BCC failover test. Until POAM-004 and POAM-005 (P07) close, the company cannot rely on meeting it.
