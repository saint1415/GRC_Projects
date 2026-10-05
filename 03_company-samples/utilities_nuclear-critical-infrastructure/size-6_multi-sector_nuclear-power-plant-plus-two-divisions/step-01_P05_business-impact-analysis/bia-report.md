# Business Impact Analysis: Cris Santos Company Holdings | Nuclear Reactors, Materials, and Waste | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads and each station's emergency preparedness manager | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud, network and remote access, finance, HR).
- **Division BIAs:** Nuclear Generation (focus), Engineering and Radiation Services, and Radioactive Waste Management. They are rows in one workbook (`bia.csv`, `division` column), so cross-division dependencies are visible in one place.

**What this BIA does not cover.** Reactor safety functions and the CDAs that perform them (SYS-N4, SYS-N5) are not business processes with a recovery time objective. Their operability is governed by each unit's Technical Specifications, the emergency plan, and the station cyber security plan (CSP), which requires the capability to detect, respond to, and recover from cyber attacks (10 CFR 73.54(c)(2), (e)(2)). The units keep running safely if every system in this BIA is down. This BIA covers what the business, the regulators, and the customers need from the IT systems around the plants.

It supports:
- the station CSP incident response and recovery measures for the business-side systems that touch CDAs (the PMMD kiosk update path, the plant data replicas);
- the 73.77 and 50.72 notification capability (BP-NG02), which must work with every IT system down;
- the Part 37 security program at the Florida waste facility (37.49);
- the dosimetry and waste portal availability commitments in the SOC 2 work (P09);
- impact ratings in the registers (P01), the availability rating in the SSP (P02), and the recovery order in the runbook (P08).

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud, WAN, and remote access, and SYS-G4 ERP and HR. Nuclear Generation runs the plant business networks (SYS-N1) and the fleet work management system (SYS-N2) that together form the P02 system, plus the CAP system, the fleet operations center, the PMMD kiosks, and the predictive maintenance service. Engineering and Radiation Services runs engineering collaboration (SYS-E1), stand-alone SGI systems (SYS-E2), the dosimetry system (SYS-E3), and a DOE projects enclave (SYS-E4). Radioactive Waste Management runs waste tracking (SYS-W1), facility OT (SYS-W2), the Florida vault security systems (SYS-W3), and fleet telematics (SYS-W4). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Nuclear Generation about $9.9 million per day; Engineering and Radiation Services about $17 million per day; Radioactive Waste Management about $22 million per day. A lost outage day on a 1,150 MW unit costs about $1.7 million in lost generation.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10 million for the group, or more than 1 day of a division's revenue | $1 million to $10 million | Less than $1 million |
| Operations | A division cannot deliver its core service (outage execution, dosimetry, waste processing), or a refueling outage is extended | One site, line, or service stops | Staff slowed but working |
| Regulatory | Missed NRC, NERC, Agreement State, or SEC deadline; a CSP deficiency not recorded; a Part 37 monitoring loss without compensatory measures | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Plausible worker injury or radiation exposure control failure (clearances, dose results, vault monitoring) | Degraded but safe | None |
| Reputation | National media, NRC or regulator attention, loss of utility or dosimetry customers | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 31 processes: 5 group shared services, 12 Nuclear Generation, 7 Engineering and Radiation Services, and 7 Radioactive Waste Management. 15 are High, 13 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-NG02 NRC and offsite notifications | Nuclear Generation | High | 1 h | 1 h | 0 |
| BP-NG01 Fleet dispatch and grid communications | Nuclear Generation | High | 2 h | 1 h | 1 h |
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, WAN, and remote access | Group | High | 4 h | 2 h | 1 h |
| BP-WM03 Vault security monitoring (Florida facility) | Waste | High | 4 h | 2 h | 1 h |
| BP-WM04 Hazmat transport dispatch and tracking | Waste | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-NG03 Clearance and tagging | Nuclear Generation | High | 12 h | 4 h | 1 h |
| BP-NG04 Outage work execution and scheduling | Nuclear Generation | High | 24 h | 8 h | 1 h |
| BP-NG05 Site access processing for outage workers | Nuclear Generation | High | 24 h | 8 h | 4 h |
| BP-ER05 Contractor/vendor access authorization processing | Engineering | High | 24 h | 8 h | 4 h |
| BP-ER03 Outage engineering support to stations | Engineering | High | 24 h | 8 h | 4 h |
| BP-WM02 Manifests and waste tracking | Waste | High | 48 h | 12 h | 1 h |
| BP-WM01 Waste receipt, processing, and shipment | Waste | High | 48 h | 24 h | 4 h |
| BP-ER01 Dosimetry processing and dose reporting | Engineering | High | 48 h | 24 h | 4 h |
| BP-NG06 Corrective action program | Nuclear Generation | Moderate | 24 h | 8 h | 4 h |
| BP-NG08 Controlled documents on the business network | Nuclear Generation | Moderate | 24 h | 8 h | 24 h |
| BP-WM07 Reactor-site radwaste and decommissioning | Waste | Moderate | 48 h | 24 h | 24 h |
| BP-NG07 Online work management and maintenance | Nuclear Generation | Moderate | 72 h | 24 h | 4 h |
| BP-ER02 Dosimetry customer portal | Engineering | Moderate | 72 h | 24 h | 4 h |
| BP-ER07 DOE contract engineering | Engineering | Moderate | 72 h | 24 h | 24 h |
| BP-WM05 Waste customer portal and certificates | Waste | Moderate | 72 h | 24 h | 4 h |
| BP-WM06 DOE site remediation project operations | Waste | Moderate | 72 h | 24 h | 24 h |
| BP-G04 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-NG09 Plant data replica and engineering data | Nuclear Generation | Moderate | 72 h | 24 h | 24 h |
| BP-NG10 PMMD kiosk operations | Nuclear Generation | Moderate | 72 h | 24 h | 24 h |
| BP-ER04 Design and modification engineering | Engineering | Moderate | 120 h | 48 h | 24 h |
| BP-G05 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-ER06 SGI engineering work | Engineering | Low | 120 h | 72 h | 24 h |
| BP-NG11 SGI processing (Nuclear Generation) | Nuclear Generation | Low | 120 h | 72 h | 24 h |
| BP-NG12 Predictive maintenance analytics | Nuclear Generation | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Regulatory clocks** drive the shortest MTDs. NRC notifications (BP-NG02) are measured in hours from discovery and must work even when every IT system is down, so they rely on the Emergency Notification System and commercial telephone, not the business network (73.77(c)(1); 50.72(a)(2)).
- **Worker safety** drives clearance and tagging (BP-NG03) and dosimetry (BP-ER01). A paper clearance process exists and is drilled each outage, which is why its MTD is 12 hours and not 1.
- **Outage economics** drive outage work (BP-NG04, BP-NG05, BP-ER03, BP-ER05): about $1.7 million per lost unit-day, and badging delays cascade into the critical path.
- **Part 37 and DOT rules** drive the waste division's security monitoring and shipment tracking (BP-WM03, BP-WM04). Compensatory measures start at once; the MTD is how long the facility can rely on them.
- **Low availability, high confidentiality.** SGI work (BP-ER06, BP-NG11) and predictive maintenance (BP-NG12) can wait days. Their protection cannot (P02, P03).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every business process | A group identity outage stops business work in all three divisions at once. CDAs, the fleet operations center, and the security network do not use SYS-G1, by design |
| Contractor/vendor certifications (BP-ER05) | Engineering and Radiation Services | Nuclear Generation site access (BP-NG05) | Outage workers cannot be badged without them |
| Outage engineers and radwaste crews | Engineering and Radiation Services; Radioactive Waste Management | Nuclear Generation outages (BP-NG04) | About 1,900 cross-division accounts on the station networks and the work management system (scenario gap 1). The same accounts are an attack path (P01 GR-01; P08) |
| Work packages (SYS-N2) | Nuclear Generation | Engineering and waste crews | Crews execute from them; they also hold CDA details (scenario gap 2) |
| SOC facts (BP-G02) | Group | Station CSTs; every notice in P08 | 73.77 clocks start at discovery; the CST needs business-network evidence fast |
| Dry active waste processing (BP-WM01) | Radioactive Waste Management | Nuclear Generation outages | Outage waste must move off site; delays fill station storage |
| Kiosk update server on SYS-N1 (BP-NG10) | Nuclear Generation business network | PMMD kiosks protecting CDAs | A business-network compromise can reach the kiosks' update path (scenario gap 3; P08) |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); one kiosk update server for all 9 kiosks; one background investigation vendor for 80% of contractor/vendor files (P01 ER-012); the Florida vault security systems on the facility business network with no alternate path (P01 WM-002).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All business processes | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| SYS-N2 work management (provider A) | BP-NG03, BP-NG04, BP-NG07 | Database replica in provider B (15-minute lag); hourly immutable snapshots |
| SYS-N1 station file and print services | BP-NG08 | Nightly backups to the provider B vault; local snapshots |
| SYS-N6 kiosk update server | BP-NG10 | Golden image and signature sets held offline by the CST |
| SYS-E3 dosimetry system | BP-ER01, BP-ER02 | Database replica in provider B; reader raw data retained 90 days on the lab network |
| SYS-W1 waste tracking (SaaS) | BP-WM02, BP-WM05 | Vendor replication; nightly export to the group vault |
| SYS-W3 vault security systems | BP-WM03 | Local recording; compensatory guard post |
| People | All | Paper fallbacks drilled each outage; cross-trained work control staff |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, WAN, and remote access
3. SOC visibility (SIEM and EDR), so the CSTs and counsel can establish facts for notices
4. and 5. NRC notification capability and fleet dispatch (both independent of the business network; listed to confirm they are working)
6. to 10. Clearance and tagging, outage work, site access, contractor/vendor certifications, outage engineering
11. and 12. Vault security monitoring and shipment tracking at the waste division (compensatory measures start immediately; systems restored next)
13. to 15. Waste processing and manifests, dosimetry processing
16. to 31. CAP, controlled documents, radwaste services, online work, portals, DOE work, finance, plant data replicas, kiosks, design engineering, HR, SGI work, and predictive maintenance.

## 8. Key findings
1. **Plant safety does not depend on anything in this BIA**, which is the purpose of the CSP defensive architecture. The business risk is outage time, worker safety processes, and regulatory clocks, not reactor control.
2. **Shared identity is the group's largest single point of failure and its largest shared attack path.** The 1,900 cross-division station accounts (scenario gap 1) connect Engineering and Radiation Services and Radioactive Waste Management laptops to the station business networks.
3. **Notification capability is a process with its own recovery target** (BP-NG02, BP-G02). The ENS and telephone paths are independent of IT; the facts that feed them are not.
4. **The kiosk update server is a business-network asset with a CDA-protection role** (BP-NG10). Its availability is Moderate, but its integrity matters more than any other business-network server (P02, P08).
5. **The waste division's vault monitoring has no alternate path** (scenario gap 7), so its 4-hour MTD depends entirely on guards. P03 rates this as a Part 37 gap.
