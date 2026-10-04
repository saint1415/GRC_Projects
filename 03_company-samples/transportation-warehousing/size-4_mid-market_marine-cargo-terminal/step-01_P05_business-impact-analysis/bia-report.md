# Business Impact Analysis: Cris Santos Company | Transportation and Warehousing | Mid-Market

**Organization:** Cris Santos Company, Inc. (marine cargo terminal operator, NAICS 488320) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager (alternate CySO) with the vCISO, the process owners named in `bia.csv`, and both FSOs | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-15 (presented to the audit committee the same day)
**Handling:** Contains details of critical systems that will feed the Cybersecurity Plan. Handle as sensitive security information (SSI) under 49 CFR part 1520 (33 CFR 101.630(b); POL-04).

## 1. Overview and purpose
This BIA covers every business unit: Terminal 1 (container), Terminal 2 (breakbulk, project cargo and vehicles), the off-dock depot, the commercial group and corporate support. It rates 17 business processes and quantifies what an outage costs in money, operations, regulatory exposure and safety.

The results feed:
- the resilience measures in the USCG cyber rule: backups of critical IT and OT systems that are protected and tested frequently (33 CFR 101.650(g)(4)) and the Cyber Incident Response Plan (101.650(g)(2));
- the designation of critical IT and OT systems that the CySO must make in the Cybersecurity Plan (101.615; 101.650(b)(3));
- the "key facility operations that are important to protect" in each Facility Security Assessment report (33 CFR 105.305(d)(1)(v));
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment (P09).

## 2. System and business description
The company runs two terminals at two Florida ports and an off-dock depot. T1 handles about 620,000 container moves a year from 9 carrier services. T2 handles about 900,000 tons of breakbulk and project cargo and 160,000 vehicles a year. Together the gates process about 4,000 truck transactions a day. Operations run on the Terminal Operations and Gate Platform (TOGP) described in the SSP (P02): the TOS in the cloud landing zone, gate automation at three gates, EDI and integration, the identity provider, the SD-WAN and terminal networks, operations endpoints, security monitoring and the customer portal. Cranes and yard equipment run on their own controllers (OT) and take job instructions from the TOS. See `../00_company-facts.md` sections 1, 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual revenue over about 363 operating days: about $209,000 a day at T1, $50,000 at T2 and $16,500 at the depot.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $150,000 of lost revenue and extra cost, or a carrier contract penalty | $30,000 to $150,000 | Less than $30,000 |
| Operations | A terminal cannot work vessels, or a gate stops | One berth, some gate lanes or one yard block slowed to manual working, or throughput down by more than 30% | Staff slowed but working |
| Regulatory | A transportation security incident, a failure of FSP access control, a container released while on a customs hold, or a cyber incident not reported under 33 CFR 6.16-1 | A missed record, drill or reporting timeliness requirement | Internal policy deviation |
| Safety | Plausible injury: unsafe crane or RTG motion, a heavy or hazardous unit mis-stowed, or responders unable to locate hazardous cargo | Unsafe conditions controlled by stopping work | None |
| Reputation | A carrier moves a service to another terminal, the carrier alliance does not renew, or regional media coverage | Complaints from carriers, trucking companies or a port authority | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered, plus longshore standby and overtime, plus extra staff, over the process MTD. Recovery assumptions came from the process owners: carriers recover most throughput on later shifts, but about 20% of T1 vessel revenue in the outage window is lost to omitted calls and productivity penalties, and longshore standby and overtime cost about $5,000 an hour for each vessel being worked. For billing (BP-12) the loss is collection delay and interest; the delayed cash is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-04 Security, access control and hazardous cargo control | Both terminals | High | 4 | 2 | 1 | $5,000 |
| 2 | BP-01 Container vessel operations | T1 | High | 8 | 4 | 1 | $90,000 |
| 3 | BP-02 Container truck gate processing | T1 | High | 6 | 3 | 1 | $35,000 |
| 4 | BP-05 Crane and equipment maintenance and OT support | Both terminals | High | 8 | 4 | 24 | $25,000 |
| 5 | BP-03 Yard, equipment dispatch and reefer monitoring | T1 | High | 8 | 4 | 1 | $40,000 |
| 6 | BP-06 Breakbulk, project cargo and vehicle vessel operations | T2 | High | 12 | 6 | 1 | $30,000 |
| 7 | BP-08 Customs status and EDI exchange | Both terminals | Moderate | 12 | 8 | 4 | $20,000 |
| 8 | BP-10 Customer portal and truck appointments | Commercial | Moderate | 12 | 6 | 1 | $12,000 |
| 9 | BP-07 Truck gate and vehicle processing | T2 | Moderate | 12 | 8 | 1 | $8,000 |
| 10 | BP-17 Longshore labor ordering and gang timekeeping | Both terminals | Moderate | 12 | 8 | 4 | $20,000 |
| 11 | BP-16 IT and security operations | Corporate | Moderate | 24 | 8 | 24 | $5,000 |
| 12 | BP-09 Vessel, berth and yard planning | Both terminals | Moderate | 24 | 12 | 4 | $15,000 |
| 13 | BP-11 Empty container and chassis depot operations | Depot | Moderate | 24 | 12 | 4 | $10,000 |
| 14 | BP-15 Carrier and partner communications | Commercial | Moderate | 24 | 8 | 24 | $5,000 |
| 15 | BP-12 Billing, demurrage and collections | Commercial | Low | 72 | 48 | 24 | $15,000 (plus about $825,000 of invoicing delayed) |
| 16 | BP-13 Payroll, HR and timekeeping | Corporate | Low | 120 | 72 | 24 | $10,000 |
| 17 | BP-14 Finance, procurement and accounts payable | Corporate | Low | 120 | 72 | 24 | $5,000 |

**Summary:** 6 High, 8 Moderate and 3 Low processes (17 in total). The sum of estimated losses at each process's MTD is $350,000.

**Enterprise-wide scenario.** If the TOS and the gates were down at both terminals for 72 hours (for example, ransomware), unrecovered revenue would be about $195,000 (T1 about $157,000, T2 about $23,000, depot about $15,000), and longshore standby and overtime would add about $600,000, for a total of about $0.8 million. About $825,000 of invoicing would also be delayed. Incident response, legal and recovery costs come on top (see P01 R-001), as does the risk that the carrier alliance does not renew in 2027 (P01 R-043).

**What drives the values:**
- **Safety and security drive BP-04.** The FSOs and emergency responders must be able to find hazardous cargo at any time. Today that list exists only in the TOS. A printed list at every shift change makes the 4-hour MTD achievable (P01 R-030).
- **The berth window drives BP-01, BP-05 and BP-06.** Past about one shift of manual working at T1, carriers miss their windows. T2 breakbulk tolerates paper working longer, so its MTD is 12 hours.
- **Road congestion and customs holds drive the gates.** T1 trucks back up onto port roads within about 90 minutes, so BP-02 has the shortest operational MTD after security.
- **Partners can resend data, which drives BP-08.** Carriers and the customs data exchange can resend 24 hours of messages, so a 4-hour RPO is enough. Timeliness matters more than data loss.
- **The OT RPO means a program version, not hours of data.** PLC programs and HMI settings change rarely. The 24-hour RPO means the last approved version must be held by the company, not only by an OEM.

## 5. Key findings
1. **The TOS recovery targets are not yet demonstrated.** BP-01 to BP-04 need the TOS back in 2 to 4 hours with no more than 1 hour of data lost. The 2026-04-22 restore test took **6.5 hours**, and failover to the warm standby in the second region has never been tested (gap 5). If an attacker corrupted the primary database and the change replicated to the standby, the fallback would be the daily write-once backup, an RPO of up to 24 hours. Action: tested failover runbook and hourly isolated snapshots (P01 R-004; P07 CP-4).
2. **T2 cannot be rebuilt within its RTOs.** T2 gate server images are not backed up, and T2 PLC programs are held only by the mobile harbor crane OEM. A rebuild would take days of vendor work (P01 R-010, R-017).
3. **T1 gate capacity in manual mode is about 25% of normal.** At peak, a manual gate cannot keep trucks off port roads. A printed release list and pre-staged paper interchange forms are needed at all 12 lanes (P01 R-031).
4. **Single points of failure:** the T2 internet and SD-WAN circuit (P01 R-016), the customs data exchange service (P01 R-019), the identity provider (P01 R-034), and the T1 gate server room for hurricanes (P01 R-015).
5. **Reefer monitoring loss is labor-intensive.** Manual checks of 1,200 plugs every 4 hours need about 8 extra technicians a shift. The reefer monitoring vendor's remote access is not controlled (gap 2; P01 R-018).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Identity provider | Single sign-on and MFA for the TOS, portal, email and cloud administration | BP-01 to BP-04, BP-06 to BP-10, BP-12 to BP-16 |
| SYS-07 Networks and SD-WAN | Internet firewalls, T1 OT zone firewall, T2 flat gate and yard network, VMT Wi-Fi, SD-WAN to the cloud (dual circuits at T1, single at T2) | All |
| SYS-10 Cloud landing zone | TOS application and database, EDI gateway, integration services, portal; backup account; standby region | BP-01 to BP-12 |
| SYS-01 TOS | System of record for containers, vehicles, locations, holds and hazardous cargo | BP-01 to BP-09, BP-11, BP-12, BP-17 |
| SYS-02 Gate automation | OCR portals, TWIC readers, kiosks, gate transaction servers at three gates | BP-02, BP-04, BP-07, BP-11 |
| SYS-03 Crane and yard equipment OT | STS, RTG and mobile harbor crane controllers, crane management system, reefer monitoring, VMTs | BP-01, BP-03, BP-05, BP-06 |
| SYS-04 EDI and integration | Carriers, trucking companies, two port community systems, customs data exchange | BP-01, BP-02, BP-07, BP-08 |
| SYS-08 Endpoints | Operations and gate booth workstations, rugged tablets, VMTs | BP-01 to BP-03, BP-06, BP-07 |
| SYS-09 Security systems | CCTV, perimeter video analytics, PACS and TWIC readers | BP-04 |
| SYS-13 Security monitoring | SIEM (MSSP) and T1 OT monitoring sensors | BP-16; recovery validation |
| SYS-14 Customer portal | Appointments, availability, invoices | BP-10, BP-02 |
| SYS-11 ERP and HR SaaS | Finance, billing, procurement, payroll | BP-12 to BP-14 |
| SYS-12 Scheduling optimization (AI-001) | Advisory berth and yard plans | BP-09 (not required for recovery) |
| People and facilities | Planners, superintendents, clerks, security officers, mechanics, longshore labor, IT and security staff, MSSP; gate server rooms and crane electrical houses | All |

## 7. Linkage to the Coast Guard rule and the FSPs
| Requirement (verified text, summarized) | What this BIA supplies | Status |
|---|---|---|
| 101.615 and 101.650(b)(3): inventory of network-connected systems with critical IT and OT systems designated by the CySO | Proposed critical systems in the `subpart_f_linkage` column: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-07, SYS-08 operations endpoints, SYS-10, SYS-13 and SYS-14; SYS-09 and SYS-12 for CySO decision | Proposal; CySO designation in the Plan due 2027-05-28 |
| 101.650(g)(4): back up critical IT and OT systems, sufficiently protected and tested frequently | RTO and RPO per process; recovery order in section 8 | Gap: T2 images and PLC programs; TOS RTO not met in test (findings 1 and 2) |
| 101.650(g)(2): develop, implement, maintain and exercise the Cyber Incident Response Plan | Recovery order and manual workarounds for both P08 runbooks | Runbooks approved 2026-09-15; not yet exercised |
| 105.305(d)(1)(v) and (d)(2)(v): the FSA report lists key facility operations important to protect and describes computer systems and networks | Processes BP-01 to BP-08 and their systems, for each terminal | To be added to both FSAs with the Cybersecurity Assessment |
| 101.635(b): cyber drills at least twice each calendar year, testing individual Plan elements | Drill topics: manual gate (BP-02), printed dangerous cargo list (BP-04), crane local mode (BP-05) | Second 2026 drill scheduled 2026-11-18 |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and break-glass administrator accounts | 1 h | Two break-glass accounts per critical system, sealed and stored offline at T1 and T2 |
| 2 | SYS-07 Firewalls, SD-WAN and core networks, with OT zones isolated | 2 h | Cellular backup routers at T2 and the depot; T1 dual circuits |
| 3 | SYS-09 PACS and TWIC readers; printed dangerous cargo lists | 2 h | PACS runs on its own servers; security officers check TWICs visually and log entries by hand |
| 4 | SYS-10 and SYS-01: TOS database and application servers | 4 h (target; 6.5 h demonstrated) | Fail over to the standby region; restore from isolated backups if the standby is corrupted |
| 5 | SYS-08 Clean operations endpoints and gate booth workstations | 4 h | Pre-imaged spare laptops: 10 at T1, 4 at T2 |
| 6 | SYS-03 Crane and RTG controllers verified clean and reconnected to the TOS | 4 h (T1); 1 to 3 days (T2 today) | Cranes in local mode with radio dispatch; T1 programs from the offline copies; T2 from the OEM |
| 7 | SYS-02 Gate automation at T1, then T2 and the depot | 3 h (T1); 8 h (T2) | Manual gate with printed release lists |
| 8 | SYS-04 EDI gateway and customs data exchange feed | 8 h | Customs data exchange web portal; carrier email |
| 9 | SYS-14 Customer portal and appointments | 6 h | Phone and email appointments |
| 10 | SYS-13 SIEM and EDR console | 8 h | MSSP runs from its own platform; needed to validate clean recovery |
| 11 | SYS-11 Finance, payroll and billing | 48 to 72 h | Queue invoices; repeat prior payroll |
| 12 | SYS-12 Scheduling optimization service | Not required; reconnect only after a security review | Manual planning |

The contingency plan update due 2026-12-31 will turn these priorities into tested procedures. A failover test of the TOS to the standby region is scheduled for 2026-11-07, with no vessel at berth at T1.
