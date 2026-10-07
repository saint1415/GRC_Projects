# Business Impact Analysis: Cris Santos Company | Utilities | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded investor-owned electric utility; distribution and transmission in Florida and south Georgia) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and reliability committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties. It feeds:
- the CIP-009-6 recovery plans for the high and medium impact BES Cyber Systems (recovery objectives and activation conditions);
- the availability rating and recovery objectives in the Distribution Operations Platform System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the OT intrusion runbook (P08) and the quantitative factors in the SEC materiality worksheet;
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 19 processes were analyzed; 9 are High criticality and 10 Moderate. 8 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 28 dependencies: 13 are single points of failure, 1 is partly a single point of failure, and 3 have never been tested.

## 2. System and business description
Cris Santos Company delivers electricity to about 1.95 million meters in northern and central Florida and south Georgia over 3,380 distribution feeders and about 5,900 circuit miles of transmission. It has 12,000 employees and about $4.8 billion in annual revenue. It is registered with NERC as a Distribution Provider, Transmission Owner, and Transmission Operator. The technology estate is described in `../00_company-facts.md` section 3. The two control rooms that matter most are:
- the **Transmission Control Center (TCC)** at headquarters, with the backup TCC at Operations Center North (OCN). The energy management system (SYS-01) there is a high impact BES Cyber System under NERC CIP;
- the **Distribution Control Center (DCC)** at the Grid Operations Center, with the backup DCC at OCN. The ADMS (SYS-02) and OMS (SYS-03) there are outside CIP scope and protected to the company's OT security standard.

## 3. Impact categories and values
Dollar thresholds are scaled to about $12.5 million of retail revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated. In a utility, the cost of an outage of a control system is mostly restoration cost, customer credits, and regulatory exposure, not lost sales, because customers still buy the power once service returns.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Loss of real-time monitoring or control of the transmission or distribution system; more than 100,000 customers without service because of the event | One district, one service line, or one control function degraded with a workaround | Staff slowed but working |
| Regulatory | Potential violation of a NERC Reliability Standard; missed DOE-417 or EOP-004 report; missed SEC filing; breach notice to regulators | Missed contractual or documentation deadline | Internal policy deviation |
| Safety | Plausible harm to workers or the public (switching errors, downed wires not handled, medical-priority customers without service) | Delayed but safe response | None |
| Reputation | National media, state commission inquiry, rating agency comment, or loss of client contracts | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Transmission system real-time operations (TOP) | High | 2 h | 1 h | 5 min | $4.80M |
| BP-02 Distribution system operations (DCC) | High | 4 h | 2 h | 15 min | $3.60M |
| BP-03 Outage management and restoration dispatch | High | 4 h | 2 h | 15 min | $2.90M |
| BP-04 Customer contact center and IVR | High | 4 h | 2 h | 15 min | $0.90M |
| BP-05 Storm and emergency response | High | 4 h | 2 h | 1 h | $5.00M (storm day) |
| BP-06 Substation and field device communications | High | 8 h | 4 h | 1 h | $1.10M |
| BP-07 Physical security and access control | High | 4 h | 2 h | 15 min | $0.60M |
| BP-08 Wholesale power scheduling and load forecasting | High | 12 h | 6 h | 1 h | $1.50M |
| BP-14 Utility Services for client utilities (SL-1) | High | 24 h | 8 h | 15 min | $0.35M |
| BP-15 Fleet charging services (SL-2) | Moderate | 12 h | 4 h | 1 h | $0.25M |
| BP-09 Remote connect and disconnect (AMI) | Moderate | 24 h | 8 h | 1 h | $0.45M |
| BP-13 Customer portal and mobile app | Moderate | 24 h | 8 h | 15 min | $0.70M |
| BP-12 Payments, collections, and credit | Moderate | 48 h | 12 h | 15 min | $2.10M |
| BP-10 Meter data management and billing determinants | Moderate | 72 h | 24 h | 1 h | $0.35M |
| BP-11 Billing and bill delivery | Moderate | 72 h | 24 h | 15 min | $1.20M |
| BP-16 Work, asset, and supply chain management | Moderate | 72 h | 48 h | 24 h | $0.40M |
| BP-17 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.20M |
| BP-18 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-19 NERC and DOE event reporting and compliance | Moderate | 24 h | 8 h | 4 h | $0.10M |

**What drives the values:**
- **Reliability and safety** set the shortest MTDs. Transmission operations (BP-01) must move to the backup TCC within the hour; distribution switching and clearances (BP-02) protect line workers; hazard calls (BP-04) protect the public.
- **Storms multiply everything.** A cyber event during a hurricane would hit BP-02 to BP-05 at their peak load. BP-05 is valued on a storm day, when about 3,000 mutual assistance workers may be on standby.
- **Cash, not time,** drives billing and payments (BP-11, BP-12). Bills and payments can be delayed for days, but each day defers about $12.5 million of billed revenue.
- **Regulation** drives physical security (BP-07, CIP-006-6 alarm and logging requirements) and reporting (BP-19, 1-hour DOE-417 and CIP-008 clocks, which are met by phone and paper when systems are down). Financial close (BP-18) tightens to 48 hours in the quarter-end window because of SEC filing deadlines.
- **Contracts** set the Utility Services (BP-14) and fleet charging (BP-15) objectives, because external clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **ADMS recovery and the vendor path (DEP-04, DEP-05).** The ADMS failed over to the backup DCC in 5 hours 20 minutes on 2026-04-21 against a 2-hour RTO. During P07 testing, the ADMS vendor's remote support appliance was found holding a persistent tunnel outside the jump hosts (POAM-001, POAM-005). This is P01 risk R-002 and R-003.
2. **OMS at storm volume (DEP-06, DEP-23).** The OMS warm standby has only been switched over at normal load, and the May hurricane exercise did not include a cyber-degraded OMS (POAM-027).
3. **ICCP diversity (DEP-03).** The backup ICCP path to the Reliability Coordinator shares a carrier entrance with the primary at the backup TCC, which matters for the new CIP-012-2 availability parts (POAM-024).
4. **Single-vendor platforms.** The EMS, ADMS, OMS, AMI head-end, private LTE core, contact center platform, payment processor, and charging management SaaS are each single points of failure that cannot be removed quickly. The response is contract terms, tested fallbacks, and CIP-013 vendor risk management.
5. **AMI bulk disconnect (DEP-09).** One command can disconnect up to 50,000 meters with a single approver; misuse would create a self-inflicted outage across both the company's and the Utility Services clients' meters (POAM-018).
6. **Untested fallbacks (DEP-15, DEP-17, DEP-24).** The weather data feed for load forecasting, the charging management SaaS, and the credit and collection service providers have no tested fallback or documented oversight.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 EMS (TCC and backup TCC) | High impact BES Cyber Systems; ICCP | BP-01; BP-08 |
| SYS-02 ADMS (DCC and backup DCC) | Distribution SCADA, DMS, FLISR | BP-02; BP-03; BP-05 |
| SYS-03 OMS, GIS, mobile workforce | Outage prediction, dispatch, maps | BP-03; BP-04; BP-05 |
| SYS-04 and SYS-05 substation and field networks | Telemetry and control paths; BES Cyber Systems at substations | BP-01; BP-02; BP-06 |
| SYS-06 AMI and MDM | Meter reads, outage events, remote connect and disconnect | BP-03; BP-09; BP-10; BP-14 |
| SYS-07 CIS, portal, IVR, contact center | Customer account, billing, payments, calls | BP-04; BP-11; BP-12; BP-13 |
| SYS-08 identity (enterprise and OT domains) | SSO, MFA, PAM; separate EMS and ADMS domains | All |
| SYS-09 Cloud providers A and B; DC-1 and DC-2 | Customer and analytics workloads; ERP; PACS servers; backup copies | BP-07 to BP-18 |
| SYS-12 OT DMZs and Intermediate Systems | The only approved path for remote OT access | BP-01; BP-02 |
| SYS-13 security operations | Detection and clean-room validation during recovery | All |
| SYS-14 and SYS-15 service line platforms | Utility Services and fleet charging | BP-14; BP-15 |
| People | TCC and DCC operators, field crews, contact center agents, SOC | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | EMS at the backup TCC (transfer) | 1 h | Field staffing of key substations; RC monitoring |
| 2 | OT identity domains, OT PAM, sealed emergency accounts | 1 h | Local emergency accounts at each control center |
| 3 | ADMS at the DCC or backup DCC | 2 h target (5 h 20 min demonstrated) | Paper switching orders; field operation by radio |
| 4 | OMS and mobile dispatch | 2 h | Paper trouble tickets; radio dispatch |
| 5 | Contact center platform, IVR, direct DCC hazard line | 2 h | Overflow contact center |
| 6 | Storm command tools | 2 h | Paper incident command forms; satellite phones |
| 7 | PACS and alarm monitoring | 2 h | Guards and manual logs |
| 8 | Substation and field communications | 4 h | Crew staffing of substations |
| 9 | Enterprise identity platform, network core, SIEM and EDR consoles | 4 h | Break-glass accounts; MSSP tooling |
| 10 | Fleet charging management | 4 h | Charger offline authorization (72 h) |
| 11 | Load forecasting and scheduling | 6 h | Prior-day schedule adjusted for weather |
| 12 | Customer portal, app, AMI connects, Utility Services | 8 h | Contact center; field connects; clients defer billing |
| 13 | Payments | 12 h | Lockbox and agents |
| 14 | MDM, CIS billing | 24 h | Estimated reads; delayed bill runs |
| 15 | ERP, payroll, financial close | 48 to 72 h | Repeat prior payroll; manual journals |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| ADMS failover 5 h 20 min against a 2 h RTO | P01 R-003; P02 CP-10; POAM-005 |
| ADMS vendor remote support tunnel outside the jump hosts | P01 R-002; P02 MA-4; POAM-001 |
| OMS standby never tested at storm volume | P01 R-012; POAM-027 |
| ICCP backup path shares a carrier entrance | P01 R-031; P03 CIP-012-2; POAM-024 |
| AMI bulk disconnect with one approver | P01 R-005; POAM-018 |
| Weather feed and charging SaaS without tested fallback | P01 R-045 and R-051; POAM-028; P09 SL-2 |
