# Business Impact Analysis: Cris Santos Company Holdings | Commercial Facilities | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and the Group building technology director | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on: identity, the SOC, cloud and WAN, the Remote Building Operations Center (RBOC) with the central BAS supervisor, the enterprise access control and video platform, finance, and HR.
- **Division BIAs:** Commercial Property (focus), Construction and Tenant Build-Out, and Hotels. They are kept as rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the availability rating of the BAACS in the SSP (P02) and the recovery design in the cloud mapping (P04);
- impact ratings in the group and division risk registers (P01);
- the recovery order in the incident runbook (P08);
- CISA CPG 2.0 goals 3.O (backups and restoration) and 6.A (recovery plan, including degraded operations) in the gap analysis (P03);
- the availability commitments that the third-party property management service line must describe for SOC 2 (P09).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and WAN, SYS-G4 ERP and treasury, and SYS-G5, the Group Building Automation and Access Control System (BAACS). The BAACS runs HVAC and access control at 142 owned properties, 88 hotels, and 34 managed buildings. Division systems are SYS-D1 and SYS-D2 (Commercial Property), SYS-D3 to SYS-D5 (Construction, including the BTI unit's integrator tools), and SYS-D6 to SYS-D8 (Hotels). See `../00_company-facts.md` sections 3 and 7.

**The building systems behave differently from IT.** BAS field controllers keep running their last programs and schedules if the site supervisor or the central supervisor is lost, and door controllers keep working on cached credentials for up to 72 hours. So an outage of the central platform does not stop buildings at once. It removes **supervision** (alarms, schedule changes, badge revocation), and the risk grows by the hour. That is why the BAS processes have short RTOs but a 24-hour RPO: the data that matters (controller programs and site configurations) changes rarely, but losing it means a building cannot be rebuilt.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Construction about $30 million per day, Commercial Property about $10 million per day, and Hotels about $9 million per day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, or more than 1 day of a division's revenue | $2 million to $20 million | Less than $2 million |
| Operations | A division cannot deliver its core service (occupied buildings, guest stays, jobsites) | One region, property group, hotel group, or service line stops | Staff slowed but working |
| Regulatory and contractual | Reportable breach, missed DoD 72-hour report, SEC disclosure, or card brand action through the acquirer | Missed lease, owner, or contract notice deadline | Internal policy deviation |
| Safety | Plausible harm to tenants, guests, or workers (heat, ventilation, egress, uncontrolled access) | Discomfort or delay without harm | None |
| Reputation | National media, loss of anchor tenants or investor owners, or regulator attention | Regional media or tenant complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 28 processes: 7 group shared services, 9 Commercial Property, 5 Construction, and 7 Hotels. 14 are High, 9 Moderate, and 5 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and WAN | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Remote building operations and central BAS supervision | Group | High | 12 h | 4 h | 24 h |
| BP-CF01 Building HVAC and environmental control | Commercial Property | High | 8 h | 4 h | 24 h |
| BP-CF02 Physical access and lobby security | Commercial Property | High | 4 h | 2 h | 1 h |
| BP-CF03 Life-safety interfaces and emergency communications | Commercial Property | High | 4 h | 2 h | 24 h |
| BP-HO01 Front desk, check-in, and room keys | Hotels | High | 4 h | 2 h | 1 h |
| BP-HO04 Hotel building systems | Hotels | High | 8 h | 4 h | 24 h |
| BP-CN03 BTI integration and building systems service | Construction | High | 8 h | 4 h | 24 h |
| BP-G05 Enterprise access control and video administration | Group | High | 24 h | 8 h | 1 h |
| BP-HO03 Hotel card payments | Hotels | High | 8 h | 4 h | 1 h |
| BP-HO02 Reservations and booking engine | Hotels | High | 8 h | 4 h | 1 h |
| BP-CN01 Jobsite operations and project delivery | Construction | High | 24 h | 8 h | 4 h |
| BP-CF04 Tenant services, work orders, and tenant app | Commercial Property | Moderate | 24 h | 8 h | 4 h |
| BP-CF06 Third-party property management services | Commercial Property | Moderate | 48 h | 24 h | 4 h |
| BP-HO07 Housekeeping and maintenance workflow | Hotels | Moderate | 24 h | 12 h | 4 h |
| BP-HO05 Food and beverage operations | Hotels | Moderate | 24 h | 8 h | 4 h |
| BP-CN02 Federal CUI work in the enclave | Construction | Moderate | 72 h | 24 h | 4 h |
| BP-G06 Financial close, treasury, and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-CF05 Lease administration, billing, and collections | Commercial Property | Moderate | 72 h | 48 h | 24 h |
| BP-CN04 Subcontractor payments and pay applications | Construction | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 96 h | 72 h | 24 h |
| BP-CF07 Visitor management | Commercial Property | Low | 48 h | 24 h | 24 h |
| BP-HO06 Loyalty program and guest marketing | Hotels | Low | 72 h | 48 h | 24 h |
| BP-CF09 Parking operations | Commercial Property | Low | 72 h | 24 h | 24 h |
| BP-CN05 Bidding and estimating | Construction | Low | 120 h | 72 h | 24 h |
| BP-CF08 Event and amenity card payments | Commercial Property | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Safety drives the building processes.** Tenant server rooms, medical office tenants, hotel guest floors in summer heat, and kitchen ventilation make HVAC loss severe within hours (BP-CF01, BP-HO04). Doors must fail safe for egress and the lobby must stay controlled (BP-CF02).
- **Supervision, not control, drives the central platform.** BP-G04 has a 12-hour MTD because field controllers keep running. After that, unseen alarms and frozen schedules start to cause harm.
- **Revocation drives access control administration.** Door controllers work offline for up to 72 hours, but a terminated tenant employee keeps access until the platform is back. That is why BP-G05 is High with a 24-hour MTD and a 1-hour RPO (badge changes must not be lost).
- **Guests drive the hotel front desk.** Arrivals cannot wait, which gives BP-HO01 a 4-hour MTD.
- **Revenue more than time drives billing and payments** (BP-CF05, BP-CN04, BP-G06). Rent and pay applications can be billed late within contract terms.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops administration everywhere at once. Break-glass accounts for the BAACS, PMS, and ERP are the fallback |
| WAN and cloud hub | Group | All 264 building sites; hotel PMS | Site supervisors reach the central supervisor over the WAN. Cellular failover keeps sites reachable |
| Central BAS supervision (BP-G04) | Group | Commercial Property, Hotels, managed buildings | One platform supervises every building. It is a single point of failure for supervision, not for control |
| **BTI unit (BP-CN03)** | **Construction** | **BAACS restoration for Property and Hotels** | For about 40% of sites, controller programs and site configurations exist only in the BTI configuration repository (SYS-D5). The group cannot rebuild those sites without the Construction division (scenario gap 3) |
| Access control administration (BP-G05) | Group | Property lobbies, hotel back-of-house, group jobsites | Terminations in HR (BP-G07) must reach the access control platform |
| SOC facts (BP-G02) | Group | Every division's notices; SEC filing | Lease, owner, DoD, state, and SEC clocks depend on the SOC establishing what happened |
| Tenant build-out | Construction | Commercial Property leasing | About 22% of Construction volume is group tenant work; delays affect rent commencement |
| Treasury (BP-G06) | Group | Rent collection, subcontractor payments, hotel settlement | One payment platform for all divisions |

**Single points of failure found:**
- the central BAS supervisor (mitigated by local control at every site, but not by a standby supervisor; P01 GR-03);
- the BTI configuration repository as the only copy of many controller programs (P01 GR-02, CF-005);
- one access control platform vendor for all sites (accepted: the vendor's multi-region service and SOC 2 report; door controllers cache credentials);
- SYS-G1 (mitigated by break-glass accounts, tested quarterly).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| Central BAS supervisor and historian (provider A) | BP-G04, BP-CF01, BP-HO04 | Daily immutable backups to provider B; a standby supervisor is not yet built |
| Site supervisors and field controller programs | BP-CF01, BP-HO04 | **Gap:** about 60% of sites back up to the group vault after each change; the rest exist only in the BTI repository (SYS-D5) |
| Access control and video platform (vendor SaaS) | BP-G05, BP-CF02 | Vendor replication; door controllers cache credentials for 72 hours; NVRs keep 30 days locally |
| SYS-D1 property management platform | BP-CF04 to BP-CF06 | Vendor replication; nightly export to the group vault |
| SYS-D3 project delivery platform | BP-CN01 | Vendor replication; weekly export |
| SYS-D4 CUI enclave | BP-CN02 | Provider backups within the authorized boundary |
| SYS-D6 hotel PMS and CRS (vendor SaaS) | BP-HO01, BP-HO02 | Vendor replication; the 14 legacy on-premises PMS servers back up nightly to local disk only |
| People | All | RBOC staff can work from a secondary console room at headquarters; chief engineers trained in manual plant operation at about half the sites |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zone, hub network, and WAN
3. SOC visibility (SIEM, EDR, OT sensors)
4. Central BAS supervision and the RBOC
5. to 7. Commercial Property building HVAC, physical access, and life-safety interfaces (life-safety systems run independently; the priority is restoring their status display and fire watch)
8. Hotel front desk and room keys
9. Hotel building systems
10. BTI integration tools (needed to restore sites whose programs live only in SYS-D5)
11. Enterprise access control and video administration
12. to 28. Hotel payments and reservations, jobsite operations, tenant services, third-party management, housekeeping, food and beverage, the CUI enclave, financial close, rent billing, subcontractor payments, payroll, visitor management, loyalty, parking, estimating, and event payments.

**Note on item 10.** In a BAACS-wide incident the BTI tools are both a restoration resource and a possible attack path (P08). They must be confirmed clean before they are used to reload any site.

## 8. Key findings
1. **Supervision, not control, is what fails first.** Buildings keep running when the central platform is down, which buys hours, not days. Manual operating procedures exist at only some sites (scenario gap 3), so the 8-hour MTDs for HVAC are not yet supportable everywhere.
2. **The group cannot restore its own buildings without the Construction division.** About 40% of site configurations and controller programs live only in the BTI repository. This is a cross-division dependency that the intercompany services agreement does not address (scenario gap 4; P01 GR-02).
3. **The central BAS supervisor has no standby.** Its 4-hour RTO depends on rebuilding from the provider B backup, which has been tested once, in 2025, for a single virtual machine.
4. **Notification capacity is itself a process** (BP-G02, BP-G06). If the SOC or the disclosure process is down during an incident, the clocks keep running. The P08 runbook uses out-of-band channels for this reason.
