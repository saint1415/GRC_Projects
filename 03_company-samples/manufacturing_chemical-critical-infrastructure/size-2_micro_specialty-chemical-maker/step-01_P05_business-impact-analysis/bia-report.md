# Business Impact Analysis: Cris Santos Company | Chemical | Micro

**Organization:** Cris Santos Company, LLC (specialty chemical maker) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, with OT recovery considerations from NIST SP 800-82 Rev. 3 (sec. 6.2.4.3 Backups; sec. 6.5.1 Recovery Planning)
**Prepared by:** Office Manager (Security Coordinator) with the Owner, the Operations Manager, the QC Technician, the Warehouse and Shipping Lead, the MSP lead technician, and the control system integrator, 2026-07-13 to 2026-07-24 | **Approved:** Owner and President, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the recovery and contingency expectations of CFATS RBPS 8 guidance and NIST CSF 2.0 (RC.RP), used here as a voluntary benchmark (P03);
- immediate release reporting (40 CFR 302.6; 355.43) and the DOT duty to keep a monitored emergency response telephone number on shipping papers (49 CFR 172.604);
- the FIPS 199 availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No federal rule requires this company to have a contingency plan. EPA RMP and OSHA PSM do not apply (`../00_company-facts.md`, threshold math), and CFATS is lapsed. The BIA is done because the company cannot ship without its systems, and because its largest customer asked about continuity of supply (P09).

## 2. System and business description
One Florida unit with 7 employees blends about 4 batches a day and ships 2 to 4 LTL loads a day. Batching runs on one PLC with an HMI and recipe PC (SYS-01, SYS-02), supported remotely by the control system integrator through a cellular gateway and cloud portal (SYS-03). The business runs on SaaS: the productivity suite (SYS-06), the accounting and inventory service (SYS-07), and the SDS and label service (SYS-08). The MSP runs the office network, endpoints, and the cloud backup (SYS-04, SYS-05, SYS-09). See `../00_company-facts.md` sections 1 to 3.

**Safety comes before recovery time.** If the HMI or PLC cannot be trusted, the first objective is a safe state: dosing pumps off, the T-1 heater off, and any partial batch held. The hardwired emergency stop and high-temperature cutout work without the PLC. Restarting automatic dosing of hydrogen peroxide on an untrusted HMI is not an acceptable workaround.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue, about $4,400 of shipments per production day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $13,000 (about 3 production days) | $4,000 to $13,000 | Less than $4,000 |
| Operations | Blending or all shipping stops | One function stops; work slowed | Staff slowed but working |
| Regulatory | Late release notice, or hazmat offered without correct shipping papers or a working emergency number | Missed record or training deadline | Internal procedure deviation |
| Safety | Plausible chemical burn, exothermic reaction, fire, or release affecting workers or neighbors | Degraded safeguards with manual measures in place | None |
| Reputation | Loss of the private-label customer, or local news coverage of a release | Late deliveries or customer complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Batch blending (T-1 and T-2) | High | 48 h | 24 h | 24 h |
| BP-02 Packaging and labeling | Moderate | 72 h | 24 h | 24 h |
| BP-03 Order entry, inventory, and invoicing | Moderate | 48 h | 24 h | 1 h |
| BP-04 Hazmat shipping | High | 24 h | 8 h | 24 h |
| BP-05 Quality control and certificates of analysis | Moderate | 48 h | 24 h | 24 h |
| BP-06 Formulation, recipe, and SDS management | Moderate | 72 h | 48 h | 24 h |
| BP-07 Emergency notification and release reporting | High | 1 h | 0.5 h | 24 h |
| BP-08 Purchasing and receiving raw materials | Low | 72 h | 48 h | 24 h |
| BP-09 Payroll, HR, and bookkeeping | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **BP-07 has the shortest MTD** even though it earns nothing. Release notices are due immediately, and today the only call list lives in the office phone system, which runs over the office network. If ransomware takes that network down, the company needs a printed list and cell phones within the hour.
- **BP-04 drives revenue.** Finished goods on the shelf can ship for about 3 days without blending, but only if shipping papers can be produced and the ERI provider holds current SDS information.
- **BP-01 is limited by recipes and configuration, not hardware.** A replacement panel PC can be bought in 2 days. What cannot be replaced quickly is a clean, verified copy of the PLC program, HMI project, and 85 recipes.

**Key finding: the 24-hour RTO for BP-01 is unproven.** The only copies of the PLC program and HMI project are the integrator's 2023 files on its own laptop, and the newest recipe copy is a monthly USB export. Nothing has ever been restored (gap 4; risk R-005; POAM-004). After a destructive attack on the HMI PC, the realistic recovery time today is **1 to 2 weeks**: the integrator would rebuild from its 2023 files, and the Owner would re-enter changed recipes from the paper formulation binder.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Batch control PLC | PLC, load cells, dosing pumps, mixers, hot-water skid | Integrator's 2023 program copy (**never restore-tested**) | BP-01 |
| SYS-02 HMI and recipe PC | HMI, recipe module, batch records | Monthly recipe export to USB (**gap**; target daily, offline) | BP-01, BP-06 |
| SYS-03 Integrator gateway and portal | Remote support and the monitoring dashboard | Not needed to run batches | BP-01 (support only) |
| SYS-04 Office network and phones | Firewall, Wi-Fi, internet line, phone service | MSP keeps the firewall configuration | All; BP-07 call list |
| SYS-05 Endpoints | 4 laptops, 2 desktops, 1 tablet | No unique data by design; MSP reimages | All |
| SYS-06 Productivity suite | Email, shared drive, formulations folder | Vendor resilience plus daily copy to SYS-09 | BP-03, BP-05, BP-06 |
| SYS-07 Accounting and inventory service | Orders, lots, invoices, bills of lading | Vendor replication (SOC 2 report states RPO 1 h, RTO 8 h; see P09) | BP-03, BP-04, BP-08, BP-09 |
| SYS-08 SDS and label service | SDSs and labels for 85 products | Vendor backups; SDS PDFs also held by the ERI provider | BP-02, BP-04, BP-06 |
| SYS-09 Cloud backup (MSP-operated) | Daily copy of the suite, 30 days of versions | **Never restore-tested** | BP-06 |
| People | 7 employees; the Operations Manager is the only person who can run the HMI's engineering functions | Cross-training: the Owner can run simple batches; the integrator for anything else | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Control system integrator | Recovery of SYS-01 and SYS-02 | No written support commitment; the service agreement has no response or recovery time |
| MSP | Recovery of the office network and endpoints; operates the backup | Contract has a 4-business-hour response time and no recovery time commitment |
| Accounting and inventory service vendor | BP-03, BP-04, BP-08 | SOC 2 Type 2 report reviewed (P09); stated RTO 8 h and RPO 1 h meet this BIA |
| SDS and label service vendor | BP-02, BP-06 | Standard terms only |
| 24-hour ERI provider | BP-04 (legally required emergency number) | Contract; the provider must receive current SDS information before product is offered (172.604(b)(2)) |
| Internet and phone provider | Every SaaS function and the office phones | None; one line, no failover |
| Cellular carrier | BP-07 fallback; integrator gateway | Not contracted for availability |

**Key findings:**
1. **The batch control system has no tested recovery path** (risk R-005). This is the largest gap in the BIA.
2. **Release reporting depends on the office network** (R-014). Printed call lists and cell phones fix this for almost no cost.
3. **The accounting and inventory vendor meets the BIA.** Its stated RTO of 8 hours and RPO of 1 hour meet the targets for BP-03 and BP-04.
4. **Neither the integrator nor the MSP has a recovery commitment.** The P01 treatments add one to each contract (R-007, R-016).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Emergency notification (BP-07) | 0.5 h | Printed call list and staff cell phones (to be posted by 2026-09-30; POAM-012) |
| 2 | Safe state of T-1 and T-2 | Immediate | Hardwired emergency stop and high-temperature cutout; dosing tote valves closed by hand |
| 3 | Internet, office network, and clean endpoints for shipping (SYS-04, SYS-05) | 8 h | Owner's laptop on a phone hotspot; MSP reimages desktops |
| 4 | Hazmat shipping (BP-04) through the accounting service (SYS-07) | 8 h | Handwritten bills of lading from the shipping binder |
| 5 | Order entry and invoicing (BP-03) | 24 h | Paper order log |
| 6 | Clean HMI PC, PLC program, and recipes (SYS-01, SYS-02) | 24 h target, **unproven** | Offline backup and restore test (POAM-004); integrator rebuild as a last resort |
| 7 | Batch blending restart (BP-01) | After step 6 and a pre-start check | Manual non-peroxide batches with the portable mixer |
| 8 | Packaging and labels (BP-02), QC (BP-05) | 24 h | Pre-printed labels; paper QC worksheets |
| 9 | Formulation and SDS files (BP-06) from SYS-09 | 48 h | Owner's paper formulation binder |
| 10 | Purchasing (BP-08), payroll and bookkeeping (BP-09) | 48 to 72 h | Phone orders; repeat the prior payroll |

The integrator's cloud portal and the AI batch-optimization feature (SYS-03, SYS-12) are **not** on the recovery path. Batches run without them. The gateway stays powered off after an incident until the remote access fix in P01 (R-001) is in place.
