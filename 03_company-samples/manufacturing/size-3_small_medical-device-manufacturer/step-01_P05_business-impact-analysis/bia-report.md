# Business Impact Analysis: Cris Santos Company | Manufacturing | Small

**Organization:** Cris Santos Company, LLC (connected medical device manufacturer) | **Tier:** Small (250 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Cloud Operations Lead and IT Manager, with the Director of Manufacturing Operations, VP QA/RA, and Customer Support Manager (interviews 2026-07-13 to 2026-07-24) | **Approved:** COO, 2026-09-04

## 1. Overview and purpose
This BIA covers every business process the company runs, from the device cloud to the factory floor. For each process it sets how long the process can be down and how much data it can lose. It feeds:
- the device cloud contingency plan and the HIPAA contingency plan standard for the device cloud as a business associate (45 CFR 164.308(a)(7)), including the applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the availability rating and the CP controls in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the Availability criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company designs, builds, and services the PM-2 wireless patient monitor (and supports the legacy PM-1) for 40 Florida hospitals. It runs the **Device Cloud Service (DCS)**, which gives clinicians remote viewing and secondary alarm notifications, sends results to hospital EHRs, and distributes signed PM-2 firmware (SSP, P02). Production runs on one Florida site with three lines managed by the MES. Engineering, quality, and business systems are mostly SaaS. See `../00_company-facts.md` sections 1 to 3.

A key design fact bounds the safety impact of a device cloud outage: **primary alarms always sound at the bedside monitor.** A DCS outage removes remote visibility and secondary notifications. It does not silence the monitor.

## 3. Impact categories and values
Dollar values are scaled to $58 million in annual revenue, about $232,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $500,000 (about 2 business days of revenue), or loss of a hospital contract | $100,000 to $500,000 | Less than $100,000 |
| Operations | Remote monitoring down for hospitals, or production stopped on Lines 1 and 2 | One line, one support channel, or one hospital interface down | Staff slowed but working |
| Regulatory | Missed FDA reporting deadline (21 CFR 803 or 806), missed business associate breach notice (164.410), or loss of a 524B element needed for a submission | Late internal record or a documentation gap found in an audit | Internal procedure deviation |
| Safety | Plausible patient harm from a device or device cloud failure (for example, a delayed response to an alarm) | Clinicians lose remote visibility but bedside alarms work | None |
| Reputation | Customer advisory or public vulnerability disclosure naming the company; loss of hospital trust | Complaints from several hospitals | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Remote patient monitoring and secondary alarm notification | High | 4 h | 2 h | 15 min |
| BP-02 Firmware update distribution | Moderate | 48 h | 24 h | 24 h |
| BP-03 Customer support and field service | Moderate | 24 h | 8 h | 4 h |
| BP-04 PM-2 production (Lines 1 and 2) | Moderate | 72 h | 48 h | 24 h |
| BP-05 Order fulfillment, shipping, and UDI traceability | Moderate | 72 h | 24 h | 4 h |
| BP-06 Complaint handling and regulatory reporting | High | 48 h | 24 h | 4 h |
| BP-07 Service and refurbishment (Line 3) | Low | 120 h | 72 h | 24 h |
| BP-08 Software engineering, build, and code signing | Moderate | 72 h | 48 h | 24 h |
| BP-09 Design controls and regulatory submissions | Low | 168 h | 72 h | 24 h |
| BP-10 Vulnerability intake and coordinated disclosure | Moderate | 24 h | 8 h | 24 h |
| BP-11 Finance, payroll, and HR | Low | 120 h | 72 h | 24 h |

Totals: 11 processes. 2 High, 6 Moderate, 3 Low.

**What drives the values:**
- **BP-01:** hospitals use remote viewing and secondary alarms to staff their units. Primary alarms stay at the bedside, and monitors buffer 72 hours of data, so an outage of up to 4 hours is tolerable with hospital downtime procedures. Data older than 15 minutes has little value for remote monitoring, which sets the 15-minute RPO.
- **BP-06:** the clocks are regulatory, not operational. FDA reports are due in 5 work days (803.53), 10 working days (806.10), or 30 calendar days (803.50). Business associate breach notice is due without unreasonable delay and within 60 days (164.410), and many BAAs are shorter. Losing complaint records would be a Severe regulatory impact, so the RPO is 4 hours.
- **BP-10 and BP-02:** they drive the response to an exploited vulnerability (P08). Intake must never stop for more than a day. A fix must be distributable within 24 hours of being signed, because 524B(b)(2)(B) expects out-of-cycle patches as soon as possible.
- **BP-04:** revenue drives this process. A two-week finished-goods buffer protects customers, which is why production is Moderate rather than High.

**Key findings:**
1. **The BIA's BP-01 targets are unproven.** The device cloud has daily backups with point-in-time recovery (5-minute log interval) copied to a second region. The 15-minute RPO is supported on paper. But no restore or failover test has ever been run, so the 2-hour RTO is not demonstrated (P01 R-016 and R-017).
2. **One key blocks every firmware fix.** BP-02 depends on BP-08, and BP-08 depends on a single copy of the code-signing key (P01 R-025). Until the key moves to an HSM with backup key shares, a disk failure on the build server would stop all PM-2 updates.
3. **Line 2 is exposed to the office network.** A ransomware event in the office could stop BP-04 (P01 R-005). The 48-hour RTO assumes an offline copy of the MES configuration, which does not exist yet.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Device cloud service | Ingestion, processing, portal, HL7 interface, update service, database, object storage | BP-01, BP-02 |
| SYS-02 Identity provider | Single sign-on and MFA for all SaaS and the cloud console | All except BP-04 and BP-07 floor stations |
| SYS-03 PLM | Design history and risk management files | BP-08, BP-09 |
| SYS-04 Repository and build/signing server | Source code, CI/CD, firmware signing key (single copy, no HSM) | BP-02, BP-08 |
| SYS-05 MES and 14 test stations | Production records, firmware loading, device certificates | BP-04, BP-07 |
| SYS-06 ERP | Orders, shipping, UDI and serial-number traceability | BP-04, BP-05, BP-07 |
| SYS-07 eQMS | Complaints, CAPA, MDR and correction/removal records | BP-06, BP-09, BP-10 |
| SYS-08 Endpoints | 205 laptops and 30 desktops | All |
| SYS-09 Productivity suite | Email (including security@), files, chat | BP-03, BP-05, BP-06, BP-09, BP-10, BP-11 |
| SYS-10 Log analytics | Device cloud application logs | BP-01 (investigations) |
| SYS-12 Support ticketing | Hospital tickets | BP-03 |
| Backup and replication | Database point-in-time recovery (5-minute log interval), daily snapshots copied to a second region; infrastructure as code for redeployment; disk mirroring only on the build server (the signing key has one copy) | BP-01, BP-02, BP-08 |
| Third parties | Cloud provider, SaaS vendors, hospital networks and EHRs, component suppliers, freight carriers, ISAO, CISA | As listed in `bia.csv` |
| People and facilities | Florida facility (factory floor, engineering server room, offices); remote work on laptops | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 Identity provider and break-glass cloud accounts | 1 h | Break-glass cloud administrator accounts, to be created with the contingency plan (SSP CP-2, due 2026-12-31) |
| 2 | SYS-01 device cloud: ingestion, portal, HL7 interface (BP-01) | 2 h | Redeploy from infrastructure code; restore the database to a point in time; second-region restore if the primary region is down (runbook not yet written) |
| 3 | Security@ mailbox, eQMS, and support ticketing (BP-10, BP-03, BP-06) | 8 h | Phone intake; paper and spreadsheet logs |
| 4 | SYS-01 update service and object storage (BP-02) | 24 h | USB updates by field service |
| 5 | SYS-06 ERP (BP-05) | 24 h | Paper shipping log |
| 6 | SYS-04 build server and signing key (BP-08) | 48 h | Rebuild the server from configuration scripts; if both mirrored disks fail, the key is lost and there is no alternate signing path until the HSM project closes |
| 7 | SYS-05 MES and test stations, Lines 1 and 2 (BP-04) | 48 h | Ship from finished goods; hold lots |
| 8 | SYS-05 Line 3, payroll SaaS, PLM (BP-07, BP-11, BP-09) | 72 h | Loaners; repeat prior payroll; exported documents |

The recovery order in `bia.csv` (recovery_priority) ranks the processes. This table ranks the resources those processes need.
