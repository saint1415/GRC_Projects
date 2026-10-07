# Business Impact Analysis: Cris Santos Company | Manufacturing | Mid-Market

**Organization:** Cris Santos Company, Inc. (connected medical device manufacturer, NAICS 334510) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, the Plant Manager, and the VP QA/RA | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the Connected Care Cloud (CCC), product security, quality and regulatory, engineering, the four plant lines, supply chain, customer support and field service, and enterprise support functions. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure, and patient safety.

The results feed:
- the CCC contingency plan and the HIPAA contingency plan standard for the CCC as a business associate (45 CFR 164.308(a)(7)), including the applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the FIPS 199 availability rating and the contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company designs, builds, and services the VM-7 and legacy VM-5 vital-signs monitors, the IP-4 infusion pump, and the AI-001 skin-image analysis function for about 290 hospitals in 24 states. The CCC gives clinicians remote viewing and secondary alarm notifications, manages pump drug libraries and EHR-integrated pump programming, runs AI-001, and distributes signed firmware. Production runs at the Florida plant on four lines managed by the MES. Engineering, quality, and business systems are mostly SaaS. See `../00_company-facts.md` sections 1 to 3.

A design fact bounds the safety impact of a CCC outage: **primary alarms always sound at the bedside monitor or pump, and pumps keep running on their last drug library.** A CCC outage removes remote visibility, secondary notifications, and auto-programming. It does not silence a device or stop an infusion.

## 3. Impact categories and values
Dollar values are scaled to about $240 million in annual revenue over about 250 business days, or about $960,000 a day: monitors $472,000, pumps $248,000, subscriptions $136,000, and service $104,000 (facts section 7).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $100,000 of loss at the MTD, or more than $250,000 of revenue at risk per day | $25,000 to $100,000, or revenue protected by inventory buffers | Less than $25,000 |
| Operations | Remote monitoring or pump programming down for hospitals, or two or more lines stopped | One line, one CCC service, or one support channel down | Staff slowed but working |
| Regulatory | Missed FDA reporting deadline (21 CFR 803 or 806), missed business associate breach notice (164.410 or a BAA term), or loss of the FDA enforcement-discretion path for a vulnerability | Records gap found in an audit or inspection; late customer communication inside the legal limit | Internal procedure deviation |
| Patient safety | Plausible patient harm from a device or CCC failure (delayed response to an alarm, wrong-dose risk) | Clinicians lose remote tools but bedside functions work | None |
| Reputation | Public advisory or media coverage naming a product; loss of a health system or group purchasing contract | Complaints from several hospitals | Internal only |

**How loss at MTD was estimated.** Estimated loss is unrecovered revenue, service credits, overtime and expediting, and quarantine or retest costs, over the MTD. The process owners supplied the recovery assumptions: finished goods buffers (3 weeks of monitors, 2 weeks of pumps) protect shipments, overtime recovers about 3 days of lost output per line, and CCC outages longer than the 99.9% monthly commitment earn service credits of up to 25% of monthly fees. For shipping (BP-13), revenue is delayed rather than lost, so the delayed value is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-01 Remote patient monitoring and secondary alarm notification | CCC | High | 4 | 2 | 0.25 | $150,000 |
| 2 | BP-02 IP-4 drug library management and EHR-integrated pump programming | CCC | High | 8 | 4 | 1 | $60,000 |
| 3 | BP-06 Complaint handling, MDR, and correction and removal reporting | Quality and regulatory | High | 48 | 24 | 4 | $25,000 |
| 4 | BP-05 Vulnerability monitoring, PSIRT, and coordinated disclosure | Product security | High | 24 | 8 | 24 | $20,000 |
| 5 | BP-14 Customer support, clinical support line, and field service | Customer support | Moderate | 24 | 8 | 4 | $25,000 |
| 6 | BP-03 AI-001 skin-image analysis service | CCC | Moderate | 24 | 8 | 4 | $15,000 |
| 7 | BP-12 Device history records and product release (MES) | Plant and quality | High | 72 | 24 | 1 | $75,000 |
| 8 | BP-13 Order fulfillment, shipping, and UDI traceability | Supply chain | Moderate | 72 | 24 | 4 | $50,000 (plus $2.16 million of shipments delayed) |
| 9 | BP-04 Firmware and software update distribution | CCC | Moderate | 48 | 24 | 24 | $10,000 |
| 10 | BP-07 Software build and code signing | Engineering | Moderate | 72 | 24 | 24 | $40,000 |
| 11 | BP-11 Infusion pump assembly, flow calibration, and test (Line 3) | Plant | Moderate | 72 | 48 | 24 | $90,000 |
| 12 | BP-10 Monitor final assembly and test (Line 2) | Plant | Moderate | 72 | 48 | 24 | $120,000 |
| 13 | BP-09 Printed circuit board assembly (Line 1) | Plant | Moderate | 72 | 48 | 24 | $60,000 |
| 14 | BP-17 Supplier management, purchasing, and incoming inspection | Supply chain | Low | 120 | 72 | 24 | $25,000 |
| 15 | BP-15 Service and refurbishment depot (Line 4) | Service | Low | 120 | 72 | 24 | $30,000 |
| 16 | BP-16 Finance, payroll, and HR | Enterprise | Low | 120 | 72 | 24 | $20,000 |
| 17 | BP-08 Design controls, PLM, and regulatory submissions | Engineering and regulatory | Low | 168 | 72 | 24 | $20,000 |

**Summary:** 5 High, 8 Moderate, and 4 Low processes (17 in total). The sum of estimated losses at each process's MTD is $835,000. Direct revenue tied to specific processes totals $960,000 a day.

**Enterprise-wide scenarios.**
- **Plant OT ransomware, 5 business days (P08 `ir-runbook-plant-ransomware.md`).** Lines 1 to 4 and the MES stop. Finished goods protect shipments for about 2 weeks, so revenue is mostly deferred, not lost. The cost is about $800,000: overtime and expediting to rebuild inventory (about $450,000), quarantine and retest of lots with incomplete device history records (about $150,000), and revalidation of rebuilt test and calibration stations (about $200,000). If the outage passes 2 weeks, pump shipments stop and about $248,000 of revenue a day is deferred. Incident response costs come on top (P01 R-005).
- **CCC outage, 24 hours.** Service credits of up to about $700,000 (25% of one month of subscription fees), plus contract and reputational exposure with health systems. Patient safety is protected by bedside alarms, but hospitals that rely on remote viewing lose it (P01 R-006).

**What drives the values:**
- **Patient safety** drives BP-01 and BP-02. Remote viewing and secondary notifications support how hospitals staff their units, and manual pump programming raises the chance of a dosing error.
- **Regulatory clocks** drive BP-05 and BP-06. They run whether or not systems are up (section 7).
- **Records integrity** drives BP-12. Without complete device history records no lot can be released, and lost records force quarantine and retest.
- **Revenue with buffers** drives the plant lines. Finished goods make them Moderate rather than High.

## 5. Key findings
1. **The CCC's 2-hour RTO is not demonstrated.** The 2025 regional failover test took 6 hours (gap 11). The 15-minute RPO is supported by point-in-time recovery with a 5-minute log interval. Action: automate failover and rerun the test quarterly (P01 R-016; P07 CP-4).
2. **The MES cannot meet its 1-hour RPO.** The MES database is backed up nightly to a plant file server on the same OT network. A ransomware event could destroy both the database and its only backup, and up to a day of device history records (P01 R-021).
3. **Every firmware fix depends on the signing keys, and key recovery has never been tested.** The HSM-backed keys for current products have a documented recovery procedure that has never been exercised. The VM-5 legacy key has one backup copy on media in the same safe (gap 3; P01 R-012).
4. **One plant event can stop both pump production and board supply.** Line 1 and Line 3 share a flat OT segment with a persistent vendor VPN (gap 4). Line 1 feeds all products, so the 3-day board buffer becomes the real limit (P01 R-005, R-020).
5. **Regulatory clocks do not stop during an outage.** The eQMS vendor's stated RTO of 24 hours and RPO of 4 hours meet BP-06, but the paper fallback for complaints has never been exercised (P08).
6. **Traceability supports targeted field actions.** The ERP vendor's stated RPO of 1 hour meets BP-13, which matters because 806.10(c) reports need device identifiers and counts.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Connected Care Cloud | Gateway, container services, database, object storage, key management | BP-01 to BP-04 |
| SYS-02 Landing zone | Production, backup, build and signing, and shared network accounts | BP-01 to BP-04, BP-07 |
| SYS-03 Identity provider | SSO and MFA for all workforce systems | All except plant floor stations |
| SYS-04 Repositories, CI/CD, and signing service | Source, builds, SBOM store, HSM-backed signing; VM-5 legacy key offline | BP-04, BP-05, BP-07 |
| SYS-05 PLM | Design history and risk management files, threat models | BP-08 |
| SYS-06 eQMS | Complaints, MDR, 806 records, CAPA, CVD queue | BP-05, BP-06, BP-14 |
| SYS-07 MES and plant OT | MES, 52 test and calibration stations, SMT and AOI equipment, provisioning server, PLCs, historian | BP-09 to BP-12, BP-15 |
| SYS-08 Endpoints | 780 laptops and 140 desktops | All |
| SYS-09 SIEM and EDR (MSSP) | Detection and investigation | Recovery validation |
| SYS-10 ERP | Orders, shipping, UDI and serial traceability | BP-13, BP-15, BP-17 |
| SYS-11 Productivity suite and ticketing | Email (security@), support tickets, field service apps | BP-05, BP-06, BP-14 |
| Backups | CCC point-in-time recovery and daily write-once snapshots in the backup account; MES nightly backup to a plant file server only | BP-01 to BP-04, BP-12 |
| Third parties | Cloud provider, SaaS vendors, MSSP, line equipment vendors, component suppliers, freight carriers, the ISAO | As listed in `bia.csv` |
| People and facilities | Florida campus (plant, labs, offices, distribution center); 64 field service engineers | All |

## 7. Regulatory clocks that run during an outage
These deadlines do not pause while systems are down. The BIA sets BP-05, BP-06, and BP-14 so the company can meet them on paper if it must (verified against the eCFR 2026-09-23 version and the FDA guidance text).

| Clock | Deadline | Starts when | Process |
|---|---|---|---|
| MDR, 5-day | 5 work days | Company becomes aware that a reportable event needs remedial action to prevent an unreasonable risk of substantial harm (21 CFR 803.53) | BP-06 |
| MDR, 30-day | 30 calendar days | Any employee becomes aware of information that reasonably suggests a death, serious injury, or reportable malfunction (803.50; "become aware" in 803.3) | BP-06, BP-14 |
| Correction or removal report | 10 working days | The company initiates a correction or removal to reduce a risk to health (806.10(b)) | BP-06, BP-04 |
| Uncontrolled cybersecurity risk (FDA enforcement discretion, nonbinding) | Customer communication within 30 days; validated fix within 60 days | The company learns of the vulnerability (FDA postmarket guidance, December 2016, section VII.B) | BP-05, BP-04, BP-07 |
| Business associate breach notice | Without unreasonable delay, no later than 60 calendar days, or sooner under a BAA | Discovery of a breach of unsecured PHI in the CCC (164.410) | BP-01 to BP-03 |
| State third-party agent notice (Florida example) | No later than 10 days | Determination of a breach of a system the company maintains for a hospital (Fla. Stat. 501.171(6)(a)); other states vary | BP-01 to BP-03 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity provider and break-glass cloud accounts | 1 h | Two break-glass accounts per critical plane, stored offline |
| 2 | SYS-01 CCC viewing, notification, and ingestion services (BP-01) | 2 h | Redeploy from infrastructure code; database point-in-time restore; second-region failover (runbook being automated) |
| 3 | SYS-01 pump programming and drug library services (BP-02) | 4 h | Pumps run on last library; manual programming with double-check |
| 4 | Security@, CVD queue, eQMS, and support ticketing (BP-05, BP-06, BP-14) | 8 h | Phone and ISAO portal intake; paper complaint forms |
| 5 | SYS-01 AI-001 service (BP-03) | 8 h | Standard skin assessment; images queued |
| 6 | SYS-10 ERP (BP-13) | 24 h | Paper pick lists and shipping log |
| 7 | SYS-07 MES database and servers (BP-12) | 24 h | Paper travelers for 1 day; lots held |
| 8 | SYS-04 build pipeline and signing service (BP-07), then update service (BP-04) | 24 h | Rebuild runners from code; HSM key recovery procedure (untested); USB field updates for urgent fixes |
| 9 | SYS-07 Line 3, then Line 2, then Line 1 stations (BP-11, BP-10, BP-09) | 48 h | Ship from finished goods; rebuild stations from golden images and revalidate |
| 10 | SYS-09 SIEM and EDR console | 8 h (in parallel) | MSSP runs from its own platform; needed to validate clean recovery |
| 11 | Line 4, payroll SaaS, supplier systems, PLM (BP-15, BP-16, BP-17, BP-08) | 72 h | Loaners; repeat prior payroll; exported documents |

The recovery order in `bia.csv` (recovery_priority) ranks the processes. This table ranks the resources those processes need. Line 3 comes before Line 2 because pumps have the smaller finished goods buffer.
