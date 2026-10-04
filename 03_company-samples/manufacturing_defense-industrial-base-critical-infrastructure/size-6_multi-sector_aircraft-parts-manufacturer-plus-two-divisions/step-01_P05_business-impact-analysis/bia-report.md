# Business Impact Analysis: Cris Santos Company Holdings | Defense Industrial Base | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board audit and risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC and DoD reporting, cloud and network, ERP, the CUI collaboration suite, export compliance, finance, HR).
- **Division BIAs:** Aircraft Parts (focus), Engineering Services, and Defense Software and Data Services. They are rows in the same workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the contingency plans for the GCEE (P02) and for each plant enclave (SP 800-53 CP-2);
- the availability rating in the SSP (P02) and the impact ratings in the risk registers (P01);
- the recovery order and the reporting duties that must continue during an incident (P08);
- the Availability commitments in the industry edition's SOC 2 report (P09) and the service levels in DoD edition contracts.

NIST SP 800-171 Rev. 2 has no contingency planning requirement, so continuity is a business need rather than a CMMC requirement. Two DFARS duties still depend on it: the 72-hour cyber incident report (252.204-7012(c)) must be filed while systems may be down, and images of affected systems must be preserved for at least 90 days from the report (252.204-7012(e)) before they are rebuilt. DFARS 252.239-7010(f) sets the same 90-day preservation duty for the DoD edition.

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 ERP, and SYS-G5 CUI collaboration. Aircraft Parts and Engineering Services share one CAD/PLM environment, the Group CUI Engineering Enclave (GCEE), which is the SSP system in P02. Division systems are SYS-D1 (plant MES, DNC, machines, and plant networks), SYS-D2 (Engineering Services HPC, test, and field systems), SYS-D3 and SYS-D4 (the two editions of the sustainment analytics platform), and SYS-D5 (the software factory). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Aircraft Parts about $45.6 million of shipments per production day, Engineering Services about $19.2 million of billable work per working day, and Defense Software about $4.9 million per calendar day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $40 million for the group, or more than 1 day of a division's revenue | $5 million to $40 million | Less than $5 million |
| Operations | A division cannot deliver its core output (parts, engineering, platform service) | One plant, center, or service line stops | Staff slowed but working |
| Regulatory | Missed DFARS 72-hour report, unauthorized ITAR release, loss of CMMC eligibility, or SEC disclosure | Missed contractual notice to a prime or customer | Internal policy deviation |
| Safety | A nonconforming flight part could reach an aircraft, wrong readiness data could ground or release an aircraft, or a wrong NC program could injure an operator | Defect caught at inspection; rework or scrap | None |
| Reputation | Prime supplier rating downgrade, loss of source approval, national media, or DoD program office escalation | Corrective action request or customer complaint | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 27 processes: 9 group shared services, 8 Aircraft Parts, 5 Engineering Services, and 5 Defense Software. 13 are High, 12 Moderate, and 2 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones and hub network | Group | High | 4 h | 2 h | 1 h |
| BP-G04 Wide-area network and site connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring, incident response, and DoD reporting | Group | High | 8 h | 4 h | 1 h |
| BP-DS01 DoD edition availability (SYS-D3) | Defense Software | High | 8 h | 4 h | 1 h |
| BP-DS02 Industry edition availability (SYS-D4) | Defense Software | High | 8 h | 4 h | 1 h |
| BP-ES02 Test and evaluation data acquisition | Engineering Services | High | 12 h | 4 h | 1 h |
| BP-AP01 Shop-floor release and production | Aircraft Parts | High | 24 h | 12 h | 4 h |
| BP-AP03 Engineering design and change control (GCEE PLM) | Aircraft Parts (shared) | High | 24 h | 8 h | 1 h |
| BP-AP08 Contracts, prime notices, and DoD reporting liaison | Aircraft Parts | High | 24 h | 8 h | 24 h |
| BP-G06 Orders, purchasing, and cost accounting (ERP) | Group | High | 24 h | 12 h | 4 h |
| BP-AP02 Quality inspection and product acceptance | Aircraft Parts | High | 48 h | 24 h | 4 h |
| BP-AP06 Shipping and delivery of DoD spares and production parts | Aircraft Parts | High | 48 h | 24 h | 4 h |
| BP-G05 CUI collaboration suite | Group | Moderate | 24 h | 8 h | 4 h |
| BP-DS03 Customer support and incident notices | Defense Software | Moderate | 24 h | 8 h | 4 h |
| BP-AP04 NC programming and additive build preparation | Aircraft Parts | Moderate | 48 h | 24 h | 4 h |
| BP-G07 Export compliance and U.S.-person verification | Group | Moderate | 48 h | 24 h | 24 h |
| BP-ES01 Engineering analysis and design deliverables | Engineering Services | Moderate | 72 h | 24 h | 4 h |
| BP-ES04 On-site engineering support at customer sites | Engineering Services | Moderate | 72 h | 24 h | 24 h |
| BP-AP05 CUI exchange with primes, DoD, and suppliers | Aircraft Parts | Moderate | 72 h | 24 h | 24 h |
| BP-AP07 Supplier quality and outside processing | Aircraft Parts | Moderate | 72 h | 48 h | 24 h |
| BP-G09 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-DS04 Software factory (CI/CD and code signing) | Defense Software | Moderate | 72 h | 24 h | 4 h |
| BP-ES03 HPC simulation | Engineering Services | Moderate | 120 h | 48 h | 24 h |
| BP-G08 Payroll and human resources | Group | Moderate | 120 h | 72 h | 24 h |
| BP-DS05 Predictive maintenance model scoring | Defense Software | Low | 72 h | 24 h | 24 h |
| BP-ES05 Engineering proposals and deliverable submissions | Engineering Services | Low | 120 h | 72 h | 24 h |

By division: group shared services 5 High and 4 Moderate; Aircraft Parts 5 High and 3 Moderate; Engineering Services 1 High, 3 Moderate, and 1 Low; Defense Software 2 High, 2 Moderate, and 1 Low.

**What drives the values:**
- **Production and flight safety** drive Aircraft Parts. Machines run loaded jobs for about one shift, so the MTD for shop-floor release (BP-AP01) is one production day. Integrity matters as much as availability: a restored NC program, build file, or inspection record that is one revision old can produce a nonconforming flight part. Recovery must check program and drawing revisions against PLM before release.
- **Shared PLM** (BP-AP03) is High even though engineering itself tolerates delay, because all 9 plants and Engineering Services wait on PLM releases and engineering changes from primes. Its RPO is 1 hour because about 4.8 million controlled documents change continuously.
- **Test events** drive Engineering Services (BP-ES02): ground and flight tests are booked with DoD ranges months ahead, so lost data means repeating a test.
- **Customer and DoD commitments** drive Defense Software: program offices use the DoD edition for daily readiness reporting, and the industry edition's SOC 2 report includes the Availability category.
- **Reporting clocks** drive BP-G02 and BP-AP08. The DoD report must be possible from outside the CUI environment: from a clean laptop with a DoD-approved medium assurance certificate (252.204-7012(c)(3)). Defense Software has no certificate holder today (scenario gap 8).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1 government-community tenant) | Group | Every CUI process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| WAN and the provider A hub | Group | 9 plants, 4 centers, both platform editions | Plants run released jobs but cannot pull new releases; Plant 9 has a single legacy circuit |
| GCEE PLM (BP-AP03) | Aircraft Parts (system owner: corporate) | Engineering Services design and test reports | One environment, two divisions: a GCEE incident is always a two-division incident (P08) |
| Industry edition (BP-DS02) | Defense Software | Aircraft Parts spares forecasting; Engineering Services engineers working in prime tenants | Aircraft Parts is a customer of its sister division. If the industry edition cannot show FedRAMP Moderate equivalency, Aircraft Parts' own DFARS 252.204-7012(b)(2)(ii)(D) position is affected (scenario gap 4) |
| SOC facts (BP-G02) | Group | DIBNet reports for all three divisions; customer notices; SEC filing | Every reporting clock in P08 depends on the SOC establishing what happened |
| ERP (BP-G06) | Group | Aircraft Parts shipping (BP-AP06) | Spares deliveries stop without shipping documents |
| Export compliance (BP-G07) | Group | All CUI onboarding; Aircraft Parts export shipments | U.S.-person verification gates every new CUI account |

**Single points of failure found:**
- SYS-G1, mitigated by break-glass accounts tested every quarter;
- Plant 9's single internet circuit and local file server, both outside the GCEE until migration (P01 AP-003);
- one MES vendor support contract covering all 9 plants (P01 AP-017).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS, two tenants) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backup vault in a second provider A region (CUI never leaves the government-community offering) |
| GCEE PLM vault and database | BP-AP03, BP-AP04, BP-ES01 | Continuous database replication to the paired region; hourly vault snapshots; restore tested twice a year |
| SYS-D1 MES and DNC (per plant) | BP-AP01, BP-AP02 | Nightly backups to the provider A vault for plants 1 to 8; Plant 9 backs up weekly to a local disk (P01 AP-003) |
| SYS-D2 test and evaluation systems | BP-ES02 | Local buffering, then transfer to the GCEE within 1 hour of capture |
| SYS-D3 and SYS-D4 | BP-DS01, BP-DS02 | Database replicas; warm standby region; daily immutable backups |
| SYS-G4 ERP (SaaS) | BP-G06 | Vendor replication; daily extract to the group data store |
| People | All | Cross-trained teams; 3 plants can absorb urgent DoD spares work from another plant |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones and hub network
3. WAN and site connectivity
4. SOC visibility (SIEM and EDR) and the DoD reporting capability
5. Shop-floor release at the plants
6. and 7. DoD edition and industry edition of the platform
8. GCEE PLM
9. Test and evaluation data acquisition
10. Contracts and DoD reporting liaison
11. to 27. ERP, quality, shipping, collaboration, platform support, NC programming, engineering deliverables, field support, CUI exchange, export compliance, supplier quality, financial close, software factory, model scoring, HPC, payroll, and proposals.

**Evidence before rebuild.** For any cyber incident affecting CUI, images of affected systems are captured before servers are wiped (252.204-7012(e)). This adds hours to recovery and is built into the P08 runbook.

## 8. Key findings
1. **Shared services have shorter RTOs than any division process**, as they must. The identity RTO of 1 hour was met in both 2026 tests.
2. **The GCEE is High for availability across two divisions.** A single PLM outage idles engineering in both CUI divisions and, after about one shift, new work at 9 plants (P01 GR-03).
3. **Plant 9 does not meet the BP-AP01 RPO of 4 hours.** Weekly local backups could lose up to a week of traveler status. It is outside the GCEE and the planned Level 2 assessment scope until 2027-03-31 (gap 1).
4. **Reporting capacity is itself a process** (BP-G02, BP-AP08, BP-DS03). If the SOC or the support desk is down, DoD and customer clocks keep running. Defense Software must name and equip its own certificate holders (POAM-012).
5. **A sister-division dependency is also a compliance dependency.** Aircraft Parts relies on the industry edition for sustainment data; its availability is High, and its FedRAMP Moderate equivalency is unresolved (gap 4).
