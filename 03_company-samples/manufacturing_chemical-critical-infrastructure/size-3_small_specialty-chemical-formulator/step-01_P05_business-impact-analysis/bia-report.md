# Business Impact Analysis: Cris Santos Company | Chemical | Small

**Organization:** Cris Santos Company, LLC (specialty chemical formulator and packager) | **Tier:** Small (162 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with OT recovery considerations from NIST SP 800-82 Rev. 3 (sec. 6.2.4.3 Backups; sec. 6.5.1 Recovery Planning)
**Prepared by:** IT Manager with the Plant Manager, EHS Manager, Controls Engineer, Quality Manager, and Controller | **Approved:** VP Operations, 2026-09-04

## 1. Overview and purpose
This BIA identifies the business processes the plant depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency and recovery plans that CFATS RBPS 8 guidance and NIST CSF 2.0 (RC.RP) expect, used here as a voluntary benchmark (P03);
- the RMP requirement for a working emergency notification mechanism at a non-responding stationary source (40 CFR 68.90(b)(3)) and immediate release reporting (40 CFR 302.6; 355.43);
- the FIPS 199 availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
One Florida plant with 162 employees blends about 35 batches a day and ships about 25 truckloads a day. Blend Hall A runs on the Process Control and Batch Management System (PCBMS): the DCS, the batch management system, the SIS, and the historian. Business processes run on a SaaS ERP, a cloud tenant (LIMS, order interface, file shares, backups), and SaaS email and HR. See `../00_company-facts.md` sections 1 to 3.

**Safety comes before recovery time.** In an OT outage the first objective is a safe state, not a fast restart. The SIS is independent of the DCS, so the ammonia and peroxide tanks can be held safe while the DCS is down. Restarting Blend Hall A on an untrusted DCS is not an acceptable workaround.

## 3. Impact categories and values
Dollar values are scaled to $74 million in annual revenue, about $296,000 of shipments per production day (250 production days).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $600,000 (about 2 production days) | $150,000 to $600,000 | Less than $150,000 |
| Operations | Blend Hall A stops, or all shipping stops | One line, one process, or one shift lost | Staff slowed but working |
| Regulatory | Late release notification, RMP reportable accident, or an enforcement action | Missed record or internal deadline under Part 68 | Internal procedure deviation |
| Safety | Plausible toxic release, fire, or injury to workers or the public | Degraded safeguards with compensating manual measures | None |
| Reputation | Community evacuation or shelter-in-place, media coverage, loss of a top customer | Customer complaints or late deliveries | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Controlled blending (Blend Hall A) | High | 24 h | 12 h | 24 h |
| BP-02 Process safety monitoring and emergency shutdown | High | 8 h | 4 h | 0 (logic must match the approved copy) |
| BP-03 Raw material receiving and tank farm | High | 24 h | 8 h | 24 h |
| BP-04 Recipe and formulation management | Moderate | 48 h | 24 h | 24 h |
| BP-05 Quality control and batch release | Moderate | 24 h | 8 h | 4 h |
| BP-06 Packaging | Moderate | 48 h | 24 h | 24 h |
| BP-07 Order management, shipping, and loading rack | High | 24 h | 8 h | 1 h |
| BP-08 Hazardous materials inventory and site security | Moderate | 24 h | 12 h | 1 h |
| BP-09 Emergency notification and regulatory reporting | High | 1 h | 0.5 h | 24 h |
| BP-10 Purchasing, payables, and receivables | Low | 72 h | 48 h | 24 h |
| BP-11 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **BP-09 has the shortest MTD** even though it produces no revenue. Release notices are due immediately, and the plant's notification path today depends on the VoIP phone system on the business network. If ransomware takes that down, the plant needs cellular phones and a printed call list within the hour.
- **BP-02 is safety, not throughput.** The SIS must be trusted. If the SIS logic cannot be verified against the approved copy, the tanks stay isolated and the EHS Manager decides when to empty them.
- **BP-01 is limited by recipes and configuration, not hardware.** Spare DCS hardware is on site. What cannot be replaced quickly is a clean, verified DCS configuration and the 420 master recipes.
- **BP-07 and BP-08 RPO of 1 hour** come from the ERP vendor's replication, which the SOC 2 report states (P09 Part B).

**Key finding: the 12-hour RTO for BP-01 is unproven.** DCS backups exist only on the engineering workstation and one USB drive in the control room. Both are on the same network as the DCS, and neither has ever been restored (gap 8; risk R-006; POAM-004 and POAM-005). A ransomware event that reaches the EWS could destroy the running system and its backups together. Until an offline copy exists and a restore has been tested on spare hardware, the realistic recovery time for Blend Hall A after a destructive attack is **measured in weeks** (rebuild by the DCS integrator from its own project files, which are two releases old).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 DCS and SYS-02 batch management | Redundant controllers and servers, 3 operator stations, 1 EWS; recipes | BP-01, BP-03, BP-04 |
| SYS-03 SIS | Independent safety controller, gas detectors, isolation valves, UPS | BP-02, BP-03 |
| SYS-05 Historian | Process data for reports and AI-001 | BP-01 (reporting only) |
| SYS-06 OT network and IT/OT firewall | Control and supervisory networks | BP-01 to BP-03 |
| SYS-04 Loading rack and packaging PLCs | Rack metering, ground verification, fillers | BP-03, BP-06, BP-07 |
| SYS-08 ERP (SaaS) | Orders, inventory, bills of materials, shipping papers | BP-04, BP-07, BP-08, BP-10 |
| SYS-09 LIMS and SYS-10 cloud tenant | QC results, certificates, file shares, order interface, backups | BP-04, BP-05, BP-07 |
| SYS-11 Identity provider | SSO and MFA for SaaS and cloud; VPN | BP-05, BP-07, BP-10, BP-11 |
| SYS-12 Productivity suite and VoIP phones | Email and phones | BP-07, BP-09 |
| SYS-14 Physical security systems | Badges, cameras, gate | BP-08 |
| Utilities | Grid power (UPS on DCS and SIS; no generator for the office), cellular service | All |
| People | Controls Engineer (single point of knowledge), I&E technicians, Shift Supervisors, DCS integrator | BP-01 to BP-04 |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency notification (BP-09) | 0.5 h | Cellular phones and printed call list in the control room and gatehouse (to be issued; POAM-011) |
| 2 | SIS verified and tanks in a safe state (BP-02) | 4 h | Manual isolation, portable detectors, standby watch |
| 3 | Tank farm level monitoring (BP-03) | 8 h | Manual gauging each shift; stop unloading |
| 4 | Clean DCS configuration and recipes (BP-04, BP-01) | 12 h target, **unproven** | Offline backup (POAM-004) and spare-hardware restore test (POAM-005); integrator rebuild as last resort |
| 5 | Blend Hall A restart (BP-01) | 12 h after step 4 | Blend Hall B for non-ammonia products |
| 6 | ERP access and loading rack (BP-07) | 8 h | Paper shipping papers; rack in local mode |
| 7 | LIMS (BP-05) | 8 h | Paper worksheets |
| 8 | Physical security systems (BP-08) | 12 h | 24-hour guard at the gate |
| 9 | Packaging lines (BP-06) | 24 h | Manual filling |
| 10 | Finance (BP-10) | 48 h | Queue invoices |
| 11 | Payroll (BP-11) | 72 h | Repeat prior payroll |

The historian (SYS-05) and AI-001 are **not** on the recovery path. Blend Hall A runs without them. They are restored after BP-07, from clean media only.
