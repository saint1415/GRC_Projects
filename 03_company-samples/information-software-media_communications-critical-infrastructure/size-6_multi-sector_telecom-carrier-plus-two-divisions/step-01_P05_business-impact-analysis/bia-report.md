# Business Impact Analysis: Cris Santos Company Holdings | Communications | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud platform, ERP, payroll, and the legal notification function).
- **Division BIAs:** Telecom Carrier (focus), Network Engineering Services, and Tower and Fiber Infrastructure. They are rows in the same workbook (`bia.csv`, `division` column) so that cross-division dependencies are visible in one place.

It supports:
- the availability rating in the SSP (P02) and the common control catalog;
- impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08);
- the Availability commitments of Engineering's Managed Network Operations service (P09).

For this group, several downtime limits are set by **regulatory clocks, not revenue**. A 911-affecting outage must be reported to the affected PSAPs within 30 minutes and to the FCC within 120 minutes for wireline service (47 CFR 4.9(h)(4) and 4.9(f)). A tower obstruction light outage not corrected within 30 minutes must be reported to the FAA immediately (47 CFR 17.48(a)). Those clocks keep running during a cyber incident, including one where the group's own containment causes the outage.

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud platform, and SYS-G4 ERP. The Carrier runs the OSS and BSS (SYS-C1 to SYS-C5), the voice core and IP network (SYS-C6, SYS-C7), lawful intercept (SYS-C8), the contact center (SYS-C9), and the AI chatbot (SYS-C10). Engineering runs the Managed Network Operations platform (SYS-E1) and design systems (SYS-E2). Tower runs lease management (SYS-T1), lighting and site monitoring (SYS-T2), and fiber route records (SYS-T3). See `../00_company-facts.md` sections 3 and 7.

The single most important cross-division fact: **the Carrier's service assurance platform (part of SYS-C1) also hosts the Engineering Managed Network Operations tenant and the Tower Alarm Monitoring Center tenant.** It is shared infrastructure in practice, though it is owned by one division.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Carrier about $34 million per day, Tower about $9 million per day, and Engineering about $6.3 million per day of external revenue.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue (including SLA credits) | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (calling, broadband, managed operations, tower monitoring) across a region | One service, one region, or one department stops | Staff slowed but working |
| Regulatory | Missed FCC outage, 911, CPNI, CALEA, FAA lighting, or SEC duty | Late filing, documentation gap, or missed contractual notice | Internal policy deviation |
| Safety | 911 calling or tower obstruction lighting unavailable or unmonitored | Degraded but safe (calls complete through alternates; lights observed manually) | None |
| Reputation | National media, FCC or state commission inquiry, loss of wholesale or managed services customers | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 7 group shared services, 10 Carrier, 5 Engineering, and 5 Tower. 12 are High, 13 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-C01 Voice service and 911 call completion | Carrier | High | 2 h | 1 h | 24 h |
| BP-C04 Network monitoring, outage response, regulatory outage reporting | Carrier | High | 2 h | 1 h | 1 h |
| BP-E01 Managed Network Operations for external customers | Engineering | High | 2 h | 1 h | 1 h |
| BP-T01 Tower lighting monitoring and FAA notification | Tower | High | 4 h | 2 h | 1 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-C02 Broadband internet service delivery | Carrier | High | 4 h | 2 h | 24 h |
| BP-C03 Enterprise, government, and wholesale transport | Carrier | High | 4 h | 2 h | 24 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-C05 Lawful-intercept support (CALEA) | Carrier | High | 8 h | 4 h | 24 h |
| BP-G07 Legal and regulatory notification coordination | Group | High | 8 h | 4 h | 4 h |
| BP-C06 Customer care and account support | Carrier | High | 24 h | 8 h | 1 h |
| BP-C08 Field operations and repair dispatch | Carrier | Moderate | 24 h | 8 h | 4 h |
| BP-T02 Site access and tenant work authorization | Tower | Moderate | 24 h | 8 h | 4 h |
| BP-C10 Customer portal, app, and chatbot | Carrier | Moderate | 24 h | 12 h | 4 h |
| BP-C07 Service provisioning and activation | Carrier | Moderate | 48 h | 24 h | 4 h |
| BP-T04 Fiber route records and locate requests | Tower | Moderate | 48 h | 24 h | 24 h |
| BP-G04 ERP and procurement | Group | Moderate | 72 h | 24 h | 4 h |
| BP-E04 Construction management and field crews | Engineering | Moderate | 72 h | 24 h | 24 h |
| BP-E02 Engineering design and project delivery | Engineering | Moderate | 72 h | 48 h | 24 h |
| BP-G05 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-C09 Billing, mediation, and collections | Carrier | Moderate | 120 h | 72 h | 24 h |
| BP-E03 Federal contract delivery | Engineering | Moderate | 120 h | 72 h | 24 h |
| BP-T03 Lease administration and landowner payments | Tower | Moderate | 120 h | 72 h | 24 h |
| BP-G06 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-E05 Equipment procurement, staging, and covered equipment screening | Engineering | Low | 120 h | 72 h | 24 h |
| BP-T05 Tenant applications and colocation sales | Tower | Low | 168 h | 120 h | 24 h |

**What drives the values:**
- **Public safety drives the 2-hour MTDs** for voice and 911 (BP-C01) and outage response (BP-C04). The RPO for network elements is the age of the last nightly configuration backup (24 hours).
- **Contracts that protect other carriers' safety clocks drive BP-E01.** Engineering must tell its carrier customers about a possibly reportable outage within 30 minutes so they can meet their own 911 and NORS duties.
- **Aviation safety drives BP-T01.** Without the automatic alarm system, the Tower division must observe each lit structure at least once every 24 hours (47 CFR 17.47(a)(1)) and report uncorrected outages to the FAA (17.48(a)). The 4-hour MTD is an internal limit set well inside that.
- **Notification capacity is itself a process (BP-G07).** If counsel, the matrix, or the regulator portals are unavailable, notice clocks keep running.
- **Revenue more than time drives billing (BP-C09) and lease payments (BP-T03).** The switches buffer CDRs for 72 hours, which sets the mediation RTO.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Service assurance platform (SYS-C1) | Carrier | Engineering BP-E01; Tower BP-T01 | One platform outage, or one Carrier containment action, stops Carrier outage response, Engineering's customer monitoring, and tower lighting alarms at once |
| Sign-in (SYS-G1) | Group | Every IT process | A group identity outage stops agents, NOC tools, and Engineering access. Network call processing continues |
| SOC facts (SYS-G2) | Group | Every notice in P08 | CPNI, SEC, CALEA, FAA, and customer contract clocks depend on the SOC establishing what happened |
| Persistent tunnels (SYS-E1) | Engineering | Carrier management plane in the acquired regions; 64 customer networks | A compromise of Engineering's gateways reaches the Carrier and its customers (gap 7; P08 scenario) |
| Dark fiber and route records (SYS-T3) | Tower | Carrier BP-C02, BP-C03 | Carrier backhaul and enterprise routes ride partly on Tower fiber; locate errors cut both |
| Construction crews (BP-E04) | Engineering | Carrier BP-C08; Tower sites | Storm restoration capacity is shared; a hurricane draws on the same crews |
| Covered equipment screening (BP-E05) | Engineering | Carrier (47 CFR 1.50007 certification); federal contracts | A screening failure becomes a Carrier filing problem and a FAR 52.204-25 report |
| Tower space and backhaul | Tower and Carrier | Wireless tenants | About 9,800 cell sites depend on Carrier backhaul, and many sit on Tower division structures |

**Single points of failure found:**
1. The shared service assurance platform (one production instance; the disaster recovery copy in provider B has not been failed over with all three tenants; P01 GR-02 and P07 CP-4).
2. The legacy RMU fleet's cellular backhaul from one cellular provider (P01 TF-003).
3. SYS-G1 (mitigated by break-glass accounts tested each quarter).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-C6 voice core and SYS-C7 network | BP-C01, BP-C02, BP-C03 | Geo-redundant SBCs and softswitches; nightly configuration backups to SYS-C5 and an offline copy (offline copy missing in the acquired regions; P01 TC-008) |
| SYS-C1 OSS and service assurance | BP-C04, BP-C07, BP-C08, BP-E01, BP-T01 | Database replication to provider B every 15 minutes |
| SYS-C2 BSS | BP-C06, BP-C09 | Database replication to provider B; immutable backups |
| SYS-C3 mediation and CDR store | BP-C09 | Switch buffers (72 hours); daily immutable backups |
| SYS-C5 management plane | BP-C01 to BP-C04 | Configuration backups nightly; AAA configuration exported daily |
| SYS-C8 lawful intercept | BP-C05 | Vendor appliance redundancy; order records with the trusted third party |
| SYS-E1 managed operations platform | BP-E01 | MNO tenant on SYS-C1; gateway configurations backed up nightly |
| SYS-T2 lighting monitoring | BP-T01 | RMU event history replicated with SYS-C1; vendor direct alerting for newer units |
| SYS-G1, SYS-G3 | All IT processes | Vendor multi-region service; infrastructure as code; immutable vault in provider B |
| People | All | Cross-trained NOC staff in 6 regional NOCs; remote work for care agents; mutual aid with Engineering crews |
| Facilities | BP-C01, BP-C04, BP-C05 | 6 regional NOC data centers with generators and 72 hours of fuel |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. Voice and 911 call completion (BP-C01)
2. Network monitoring and outage reporting (BP-C04), including the shared service assurance platform
3. Tower lighting monitoring and FAA notification (BP-T01)
4. Workforce identity (BP-G01)
5. to 8. Broadband, cloud landing zones, SOC visibility, enterprise and wholesale transport
9. to 12. Lawful intercept, Managed Network Operations, customer care, and the notification function
13. to 27. Provisioning, field dispatch, site access, portal and chatbot, construction, billing, fiber records, design, federal delivery, ERP, financial close, landowner payments, payroll, equipment staging, and tenant applications.

Unlike the IT-centric order in most groups, **identity is fourth**: network elements process calls without SYS-G1, and NOC staff can work from element consoles with break-glass access. Identity is still first for every IT recovery.

## 8. Key findings
1. **The service assurance platform is the group's hidden shared service.** It is owned by the Carrier but carries High processes for all three divisions. Its availability requirement (RTO 1 hour) is set by the strictest tenant, and its failover has never been tested with all three tenants.
2. **Containment can create safety clocks.** Isolating the platform or an SBC during an intrusion can stop 911 calls in a region or blind the tower Alarm Monitoring Center. P08 treats these as notice triggers, not side effects.
3. **The acquired regions have unproven RPOs.** Their network element configurations are backed up only to one server per region (P01 TC-008), so the 24-hour RPO for BP-C01 to BP-C03 there is not demonstrated.
4. **Tower lighting has no written manual fallback.** About 1,100 legacy RMUs lack vendor direct alerting, so a platform outage means daily visual observation by field crews, which is not yet planned (gap 6; POAM-019).
