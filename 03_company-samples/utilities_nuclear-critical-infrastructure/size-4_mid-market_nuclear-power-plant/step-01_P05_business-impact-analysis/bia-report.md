# Business Impact Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

**Organization:** Cris Santos Company, Inc. (single-unit nuclear electric generating station) | **Tier:** Mid-Market (850 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Security Manager with the vCISO, the process owners named in `bia.csv`, the Cyber Security Program Manager, and the Outage Manager | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Site Vice President, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit at the Station and the EOF: Operations, Work Management, Engineering, Radiation Protection and Chemistry, Security, Emergency Preparedness, Regulatory Affairs, Training, Supply Chain, Energy Marketing, Finance, Human Resources, and enterprise IT. It rates 18 business processes and quantifies what an outage of the business systems costs in money, operations, regulatory exposure, and safety.

**What this BIA does not cover.** Reactor control, reactor protection, the balance-of-plant control system, and the security systems run on Level 3 and Level 4 critical digital assets (CDAs) under the NRC-approved cyber security plan (CSP). They do not depend on the business network, and their availability is governed by the technical specifications and the CSP, not by this BIA. This BIA asks a narrower question: **what happens to the plant's people and processes when the business network and its applications are lost?**

The results feed:
- the FIPS 199 availability rating and contingency controls in the SSP for the Plant Business Network and Work Management System (P02);
- the cloud recovery account and disaster recovery design (P04);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria for the generation data service (P09).

## 2. System and business description
The company owns and operates one pressurized water reactor rated about 1,020 MW net. It sells all output under two wholesale power purchase agreements (PPA-1 with a regional utility, PPA-2 with a technology company's energy subsidiary). Business work runs on the PBN-WMS described in the SSP (P02):
- the work management system (WMS) with its clearance and tagging module;
- the corrective action program (CAP) and electronic document management system (EDMS);
- identity services, the productivity suite, and the ERP;
- the business network at the Station and the EOF, with about 1,370 endpoints;
- a 4-account cloud landing zone (analytics, the generation data and settlement reporting application, recovery);
- the historian replica fed one way from Level 3;
- the RWP and dose tracking system;
- the access authorization records enclave.

See `../00_company-facts.md` sections 3, 4, and 7.

## 3. Impact categories and values
Dollar values use about $450 million of annual revenue. When the unit is online, the business network can be lost without losing generation, because the CSP keeps Levels 3 and 4 independent. During a refueling outage, every day of extension costs about $2.03 million: $1.23 million of lost generation plus about $0.8 million of contractor standby.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of disruption) | More than $1,000,000 (for example, a day of refueling outage extension) | $100,000 to $1,000,000 | Less than $100,000 |
| Operations | Critical-path outage work stops, or a process the license depends on cannot be performed | One work group stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | A 10 CFR 73.77 notification or 24-hour recording missed, an emergency plan commitment missed, unescorted access granted improperly, or a NERC CIP violation | A record late or incomplete; a CAP condition | Internal procedure deviation |
| Safety | Plausible worker injury or radiological dose above an administrative limit; delayed emergency response | Increased error likelihood with independent checks still in place | None |
| Reputation | NRC or regional media attention, or loss of a PPA buyer's confidence | Buyer or contractor complaints | Internal only |

**How loss at MTD was estimated.** Loss is the extra labor plus outage extension cost (outage-sensitive processes are rated in outage conditions, their worst case) plus contract penalties, over the MTD. Process owners estimated how much work slows without each system. For example, outage work control runs at about 50% productivity on paper, and about half of the critical path needs a new or changed clearance in any shift.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-08 Emergency response organization (ERO) callout and EOF readiness | Emergency Preparedness | High | 1 | 1 | 24 | $5,000 |
| 2 | BP-10 Generation dispatch, telemetry, and scheduling with the Balancing Authority | Energy Marketing | High | 4 | 2 | 0.25 | $25,000 |
| 3 | BP-02 Equipment clearance and tagging (tagouts) | Work Management | High | 8 | 4 | 0.25 | $340,000 |
| 4 | BP-06 Radiation work permits and dose tracking | Radiation Protection and Chemistry | High | 12 | 6 | 1 | $200,000 |
| 5 | BP-03 Work order planning, scheduling, and refueling outage control | Work Management | High | 24 | 8 | 1 | $1,000,000 |
| 6 | BP-01 Shift operations support | Operations | High | 24 | 8 | 1 | $15,000 |
| 7 | BP-04 Corrective action program (CAP) entry, screening, and 73.77(b) recording | Regulatory Affairs | High | 24 | 8 | 1 | $20,000 |
| 8 | BP-16 Business communications (email, chat, files) | Enterprise | Moderate | 24 | 8 | 4 | $40,000 |
| 9 | BP-07 Access authorization and outage in-processing | Security | High | 24 | 12 | 4 | $250,000 |
| 10 | BP-05 Procedure and document control | Engineering | High | 24 | 12 | 4 | $60,000 |
| 11 | BP-13 Parts issue, procurement, and quality records for safety-related items | Supply Chain | Moderate | 24 | 12 | 4 | $120,000 |
| 12 | BP-18 Security force scheduling and program administration | Security | Moderate | 24 | 12 | 4 | $10,000 |
| 13 | BP-09 Design change and configuration management | Engineering | Moderate | 72 | 24 | 4 | $30,000 |
| 14 | BP-11 Generation data and settlement reporting (GDSR) for PPA-2 | Energy Marketing | Moderate | 72 | 24 | 1 | $30,000 |
| 15 | BP-17 Regulatory reporting and NRC correspondence (non-emergency) | Regulatory Affairs | Moderate | 72 | 24 | 4 | $5,000 |
| 16 | BP-12 PPA invoicing, payables, and cash management | Finance | Low | 120 | 72 | 24 | $20,000 |
| 17 | BP-15 Payroll, HR, and time keeping | Human Resources | Low | 120 | 72 | 24 | $25,000 |
| 18 | BP-14 Training and qualification records | Training | Low | 168 | 72 | 24 | $5,000 |

**Summary:** 9 High, 6 Moderate, and 3 Low processes (18 in total). The sum of estimated losses at each process's MTD is $2,200,000. Three outage-sensitive processes (BP-02, BP-03, BP-07) account for $1,590,000 of it.

**Enterprise-wide scenario.** If the whole PBN-WMS were down for 72 hours:
- **while the unit is online:** generation continues. Labor, workarounds, and late data credits cost about $250,000. The main exposure is regulatory (BP-04, BP-07, BP-08), not financial;
- **during a refueling outage:** work control, clearances, RWPs, and in-processing all slow at once. Process owners estimate about 1.5 days of outage extension, about $3.0 million. Incident response costs come on top (P01 R-002).

**What drives the values:**
- **Safety** drives BP-02 (worker protection through clearances), BP-06 (radiological dose), and BP-08 (emergency staffing). These have the shortest MTDs.
- **Outage economics** drive BP-03, BP-07, and BP-13. They are Moderate or Minimal while online and Severe during an outage, so the BIA rates them in outage conditions.
- **Regulatory clocks** drive BP-04 (73.77(b) 24-hour recording), BP-07 (73.56), BP-08 (emergency plan), and BP-10 (Balancing Authority coordination and CIP-003-9).

## 5. Key findings
1. **The CSP isolation works in the BIA's favor.** No process that keeps the reactor safe depends on the business network. This is the most important result, and it must stay true. Any change that makes a Level 3 or Level 4 function depend on Level 2 must go through the CST (P03; P01 R-006).
2. **Recovery of the most critical business applications is unproven.** The WMS (including the clearance and tagging module) and the CAP/EDMS have a cloud pilot-light disaster recovery design that has never been failover-tested (gap 5). Their RTOs of 4 to 12 hours are targets, not demonstrated capabilities (P01 R-010; P07 CP-4).
3. **The clearance and tagging module is both critical and legacy.** It runs on 2 servers with an out-of-support operating system (gap 10), and its RPO is 15 minutes. Today's backups are daily, so a restore could lose a day of clearance status changes. Action: database log shipping every 15 minutes to the recovery account and a paper clearance drill before the 2027 outage (P01 R-018, R-019).
4. **There is no written fallback for the 73.77(b) 24-hour CAP recording.** A cyber attack that takes down CAP is exactly the event that must be recorded within 24 hours. Action: paper CAP intake procedure (P01 R-011; P03).
5. **The ERO callout service has a 1-hour MTD and was never evaluated by the CST.** The printed call tree works but takes about 45 minutes instead of 5 (P01 R-007; gap 3).
6. **Outage timing multiplies impact.** The same 72-hour event costs about 12 times more during a refueling outage. The next outage starts 2027-03-08, so recovery testing must finish before then.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 WMS and clearance and tagging module | On-premises; 2 legacy servers for the clearance module | BP-01 to BP-03, BP-09, BP-13 |
| SYS-02 CAP and EDMS | On-premises; CAP is the 73.77(b) record system | BP-01, BP-04, BP-05, BP-09, BP-17 |
| SYS-03 Identity services | Directory, cloud identity provider (SSO and MFA), privileged access broker | All |
| SYS-04 Productivity suite (SaaS) | Email, files, chat | BP-08, BP-10, BP-16, BP-17 |
| SYS-05 ERP and applicant tracking (SaaS) | Finance, supply chain, HR, payroll, training records | BP-12 to BP-15, BP-18 |
| SYS-06 Business network and endpoints | Station and EOF LANs, site data center, about 1,370 endpoints | All |
| SYS-07 Cloud landing zone | GDSR application, analytics, backup vault, pilot-light DR for SYS-01 and SYS-02 | BP-11; recovery of SYS-01 and SYS-02 |
| SYS-08 Security tooling (SIEM, EDR, scanner) | MSSP-operated SIEM | Recovery validation |
| SYS-09 Historian replica and one-way device receive server | Level 2 copy of plant data | BP-01, BP-11 |
| SYS-10 RWP and dose tracking | On-premises | BP-06 |
| SYS-11 Access authorization records | Restricted enclave | BP-07 |
| SYS-14 ERO callout service (SaaS) | Outside the SSP boundary | BP-08 |
| SYS-15 Dispatch RTU and metering | Separate dispatch network (NERC low impact) | BP-10, BP-11 |
| Third parties | WMS vendor, identity provider, productivity suite vendor, ERP vendor, cloud provider, MSSP, ERO callout vendor, industry shared access data system, Balancing Authority | As listed in `bia.csv` |
| People and facilities | Work control center, outage control center, RCA access point, badging office, document control desk, EOF | As listed in `bia.csv` |

## 7. Regulatory linkage
The BIA ties business downtime to the rules that set the clocks:

| Rule | What it requires (verified text, summarized) | Processes | Status |
|---|---|---|---|
| 10 CFR 73.77(b) | Record cyber security program vulnerabilities, weaknesses, failures, and deficiencies, and 73.77(a) notifications, in the site corrective action program within 24 hours of discovery | BP-04 | Gap: no manual fallback (finding 4) |
| 10 CFR 73.54(a)(1)(iii)-(iv) | Protect systems associated with emergency preparedness functions, including offsite communications, and support systems that, if compromised, would adversely impact safety, security, or EP functions | BP-08 | Gap: callout service not evaluated (finding 5) |
| 10 CFR 73.54(e)(2)(iv) | The CSP must describe how the licensee will restore systems affected by cyber attacks | BP-01 to BP-08 (where they support the CSP) | CDA restoration is in the CSP; business-side restoration is not tested |
| 10 CFR 73.56 | Only a licensee grants unescorted access, after the access authorization process is complete | BP-07 | No paper path for unescorted access; escorted access is the fallback |
| NERC CIP-003-9 Attachment 1 Section 4 | Cyber Security Incident response plan for low-impact BES Cyber Systems, including E-ISAC notification determination | BP-10 | In place since 2026-03; joint test planned (P08) |
| PPA-2 (contract) | Daily hourly data; service credit of $10,000 per late day | BP-11 | MTD 72 hours set from the contract |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | ERO callout service (vendor) and printed call tree | 1 h | Printed call tree at the control room and security; EOF dedicated EP phones |
| 2 | Identity services and break-glass accounts | 1 h | Two break-glass accounts per critical system, sealed offline |
| 3 | Business network core, Station and EOF LANs | 2 h | Isolate infected segments; EOF LAN can run standalone |
| 4 | Dispatch telemetry path (separate network) | 2 h | Recorded phone line to the Balancing Authority |
| 5 | Clean endpoints for the work control center, RCA access point, and outage control center | 2 h | 40 pre-imaged spare laptops in the IT cage |
| 6 | SYS-01 clearance and tagging module | 4 h | Paper clearance process with pre-printed tags |
| 7 | SYS-10 RWP and dose tracking | 6 h | Paper RWPs; manual dosimeter logging |
| 8 | SYS-01 WMS (work orders and outage schedule) | 8 h | Printed look-ahead schedule and staged work packages |
| 9 | SYS-02 CAP | 8 h | Paper CAP intake forms (to be written; finding 4) |
| 10 | SYS-08 SIEM feeds and EDR console | 8 h | MSSP platform; needed to validate a clean recovery |
| 11 | SYS-04 productivity suite access | 8 h | Phones, radios, printed contact lists |
| 12 | SYS-11 access authorization enclave | 12 h | Escorted access only |
| 13 | SYS-02 EDMS | 12 h | Controlled hard copies; document control desk |
| 14 | SYS-05 ERP (supply chain first) | 12 h (outage), 72 h (online) | Paper issue tickets |
| 15 | SYS-07 GDSR application | 24 h | Spreadsheet with second reviewer |
| 16 | SYS-09 historian replica | 24 h | Level 3 control room displays; backfill from the plant historian through the one-way device |
| 17 | SYS-05 payroll and training records | 72 h | Repeat prior payroll; printed qualification matrix |
