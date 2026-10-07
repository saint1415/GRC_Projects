# Business Impact Analysis: Cris Santos Company | Utilities | Micro

**Organization:** Cris Santos Electric Cooperative, Inc. (small electric distribution cooperative) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office and Finance Manager (Security Coordinator) with the Line Superintendent, the General Manager, the Meter and Service Technician, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** General Manager, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the cooperative, how long each can be down, and how much data each can lose. It supports:
- the RUS Emergency Restoration Plan (ERP), whose Business Continuity Section must cover business systems such as computer and financial systems (7 CFR 1730.28(c)(4)); that section does not exist today (P03);
- the Vulnerability and Risk Assessment (VRA), which must identify external system impacts and interdependencies (7 CFR 1730.27(c)(4));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

The cooperative is not NERC-registered, so no NERC recovery plan standard applies. RUS 7 CFR Part 1730 is the binding driver.

## 2. System and business description
One headquarters site, one distribution substation (Substation 1), 128 miles of line on 3 feeders, about 820 meters, and 7 employees. The cooperative buys all of its power from the G&T and owns nothing at 100 kV or above. Almost every system is vendor SaaS: the hosted SCADA service (SYS-01), the AMI and load management head-end (SYS-03), the utility business suite with outage management (SYS-04), and the productivity suite (SYS-05). On site are the substation and field control devices (SYS-02), the office network and 9 computers and tablets (SYS-06). The MSP runs the office IT and the cloud backup vault (SYS-07). See `../00_company-facts.md` sections 3 and 7.

**The grid keeps running when the computers stop.** Reclosers and regulators act on their own. Losing SCADA, AMI, or the business suite does not by itself cut power to members. It takes away visibility and remote control, slows restoration, and moves work onto 4 field staff. The exception is a cyber attack that uses those systems to operate field devices (P01 R-001, R-002, R-003; P08).

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $3,000 a day. Lost electricity sales during an outage are small; the costs that matter are overtime, contractors, demand charges, and damage.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $15,000 | $4,000 to $15,000 | Less than $4,000 |
| Operations | Members lose power with no way to find or fix faults quickly | One function stops; restoration or billing slowed | Staff slowed but working |
| Regulatory | DOE-417 report missed, or an RUS loan or review finding | Late RUS record or certification | Internal policy deviation |
| Safety | Plausible injury to the public or a crew, or loss of power to a medical-needs member or the water plant for many hours | Delayed but safe restoration | None |
| Reputation | Local media coverage or a member petition to the Board | Member complaints or social media posts | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Outage response and service restoration | High | 4 h | 2 h | 1 h |
| BP-02 SCADA monitoring and remote control | High | 24 h | 8 h | 24 h |
| BP-03 Outage reporting and member communication | High | 4 h | 2 h | 1 h |
| BP-04 Metering, remote connect and disconnect, and load control | Moderate | 72 h | 24 h | 24 h |
| BP-05 Billing, payments, and member accounts | Moderate | 72 h | 48 h | 24 h |
| BP-06 Wholesale power, peak management, and G&T coordination | Moderate | 24 h | 8 h | 24 h |
| BP-07 Accounting, payroll, and vendor payments | Low | 72 h | 48 h | 24 h |
| BP-08 Engineering records, mapping, and compliance records | Low | 168 h | 72 h | 168 h |

**What drives the values:**
- Safety drives BP-01 and BP-03. During an outage the cooperative must find downed lines, call medical-needs members, and keep the water plant and fire station informed. Four hours is the longest the restoration process can run on paper and phone calls before outages grow longer for everyone.
- BP-02 tolerates 24 hours because reclosers protect the lines on their own and crews can operate devices at the device. After 24 hours a lineworker would have to stay at Substation 1, which a 4-person field staff cannot sustain in a storm.
- BP-06 is short in peak season. One missed coincident peak hour costs about $6,300 in demand charges.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Hosted SCADA (SaaS) | Master station, web HMI, historian, alarm texts | Vendor backups and a second hosting site (vendor SOC 2 report states RTO 4 h and RPO 1 h; see P09) | BP-02, BP-01 |
| SYS-02 Substation and field devices | RTU, recloser and regulator controls, cellular gateway and modems | Settings files on the Line Superintendent's laptop, last copied to the vault in February 2026. **Never restore-tested** | BP-02 |
| SYS-03 AMI and load management (SaaS) | Head-end, meter data, remote disconnect, load control, peak-forecasting add-on | Vendor service; meters store interval data for weeks. **No SOC 2 report requested yet** | BP-04, BP-01, BP-03, BP-06 |
| SYS-04 Utility business suite (SaaS) | CIS, billing, accounting, mapping, outage management, portal, IVR | Vendor backups (SOC 2 report states RPO 1 h); weekly CIS export to the vault | BP-01, BP-03, BP-05, BP-07, BP-08 |
| SYS-05 Productivity suite (SaaS) | Email and the shared drive | Vendor resilience; nightly copy of the shared drive to the vault | BP-03, BP-06, BP-07, BP-08 |
| SYS-06 Office network and endpoints | Firewall, Wi-Fi, 5 office computers, operations workstation, 3 truck tablets, 7 smartphones | No local data by design, except the Line Superintendent's laptop (settings files) | All |
| SYS-07 Cloud backup vault (IaaS) | Copies of the shared drive, CIS exports, and settings files | **Never restore-tested; not immutable** | BP-02, BP-05, BP-08 |
| People | 7 employees; 4 field staff on an on-call rotation | Cross-training: the Office and Finance Manager covers member services; the General Manager can run load control | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Security terms in contract | Evidence of recovery capability |
|---|---|---|---|
| Hosted SCADA vendor | BP-02 | None | SOC 2 Type 2 report reviewed 2026-08-20 (P09): RTO 4 h and RPO 1 h meet this BIA |
| Utility business suite vendor | BP-01, BP-03, BP-05, BP-07, BP-08 | Standard terms only | SOC 2 Type 2 report on file: RTO 4 h and RPO 1 h. RTO 4 h is longer than the 2-hour RTO for BP-01 and BP-03, covered by the paper workaround |
| AMI vendor | BP-04, BP-06, part of BP-01 and BP-03 | None | None; SOC 2 report requested 2026-08-14 |
| Cellular carrier | SCADA backhaul, line recloser modems, AMI collector backhaul, truck tablets | Not applicable | None; single carrier for all field links |
| MSP | Recovery of office computers; operates the backup vault | None | No recovery commitment; 4-business-hour response time only |
| G&T | All power supply; delivery point status; peak advisories | Wholesale power contract | G&T control center staffed 24x7 |
| After-hours call center | BP-03 after hours | Service agreement | Calls roll to the Line Superintendent's cell phone if the center is down |

**Key findings:**
1. **One carrier carries every field link.** SCADA, the line reclosers, the AMI collectors, and the truck tablets all ride the same cellular carrier. A carrier outage removes remote visibility and control at once (P01 R-011).
2. **Device settings are the weak recovery point.** If a recloser control or the RTU fails or is tampered with, the only reliable copy of its settings is on one laptop. The February 2026 copy in the vault has never been restored. The 24-hour RPO for BP-02 is therefore an assumption (P01 R-007).
3. **The ERP covers storms, not computers.** The 2021 ERP has no plan for losing SCADA, the AMI, or the business suite, and no cyber scenario. This BIA supplies the content for the missing Business Continuity Section (P03 G-030).
4. **The AMI vendor is an unknown.** It carries outage detection, remote disconnect, and load control, yet the cooperative has no evidence of how it protects or restores the service.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Field restoration: trucks, radios, cell phones, paper maps (BP-01) | Immediate | Already independent of IT |
| 2 | Outage call handling and the outage module (SYS-04) | 2 h | Office lines forwarded to the Line Superintendent; paper tickets; printed medical-needs list |
| 3 | SCADA visibility and control (SYS-01, SYS-02) | 8 h | Lineworker at Substation 1; local operation of reclosers |
| 4 | Clean endpoints: operations workstation and truck tablets (SYS-06) | 8 h | Line Superintendent's laptop; MSP reimages office computers |
| 5 | Peak management and load control (SYS-03) | 8 h in peak season | G&T peak advisory emails; manual load-control command |
| 6 | AMI reads and remote connect and disconnect (SYS-03) | 24 h | Field connects; estimated reads |
| 7 | Billing, payments, accounting (SYS-04) | 48 h | Processor hosted page and IVR for payments; delay billing run |
| 8 | Engineering records and settings library (SYS-07 to SYS-06) | 72 h | Paper maps; settings re-entered from device printouts |
