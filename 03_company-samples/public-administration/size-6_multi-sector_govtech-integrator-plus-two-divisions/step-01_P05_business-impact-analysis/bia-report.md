# Business Impact Analysis: Cris Santos Company Holdings | Public Administration | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud landing zones and keys, the backup vault, the group notification desk, finance, and HR).
- **Division BIAs:** GovTech Integration (focus), IT Consulting, and Government Software Products. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the contingency planning that agency contracts require through the SP 800-53 Moderate baseline (CP-2, with RA-9 criticality analysis), and the CJISSECPOL v6.1 and Pub. 1075 contingency controls;
- the Availability commitments in the SOC 2 reports for the ACMP, the Civic Suite, and the RMS (P09);
- impact ratings in the risk registers (P01), the availability rating in the SSP (P02), and the recovery order in the incident runbook (P08).

As in every GovTech business, most of the downtime harm falls on **other organizations**: officers, caseworkers, tax collectors, and motor vehicle clerks who cannot reach their records. The contracts turn that harm into service credits, termination rights, and the group's reputation with state procurement offices.

## 2. System and business description
Three divisions share corporate services: SYS-G1 identity, SYS-G2 SOC, SIEM, and EDR, SYS-G3 cloud landing zones (provider A government-community, provider B commercial) with the backup vault, and SYS-G4 corporate SaaS. Division systems are SYS-D1 to SYS-D3 (GovTech: ACMP, IEP, MVSP), SYS-D4 and SYS-D5 (IT Consulting: delivery environment and CUI enclave), and SYS-D6 to SYS-D8 (Government Software Products: Civic Suite, RMS, Grants Management). See `../00_company-facts.md` sections 1 and 3.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: GovTech about $22 million per calendar day, IT Consulting about $17 million, and Government Software Products about $9.9 million.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue in credits, penalties, and response | $2 million to $25 million | Less than $2 million |
| Operations | Agencies cannot run a core program (supervision, benefits, tax collection, motor vehicle services, policing records) | One agency function or region slowed or on paper | Internal work slowed |
| Regulatory | An agency misses a CJIS, IRS, SNAP, or state reporting deadline because of the group; a breach of a Security Addendum, Exhibit 7, DPPA, or DFARS term; SEC disclosure | Contract notice or recovery term missed | Internal policy deviation |
| Safety | Plausible harm to a person (an officer without warrant information, a household without food benefits past the expedited deadline) | Delayed but safe service | None |
| Reputation | National media, state procurement action, or loss of a statewide contract | Agency complaints or regional media | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 25 processes: 7 group shared services, 9 GovTech Integration, 3 IT Consulting, and 6 Government Software Products. 12 are High, 10 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Cloud landing zones, network, and keys | Group | High | 4 h | 2 h | 1 h |
| BP-G05 Agency, customer, and regulator incident notifications | Group | High | 4 h | 1 h | 24 h |
| BP-SW01 Public Safety RMS service | Software | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Backup and recovery operations | Group | High | 8 h | 4 h | 1 h |
| BP-SW04 RMS connectors to state message switches and CAD | Software | High | 8 h | 4 h | 1 h |
| BP-GT01 Supervision and court case management (CJI) | GovTech | High | 12 h | 8 h | 1 h |
| BP-GT03 Integrated eligibility (SNAP, TANF, Medicaid) | GovTech | High | 24 h | 8 h | 1 h |
| BP-GT04 Agency data interfaces | GovTech | High | 24 h | 8 h | 1 h |
| BP-GT05 Motor vehicle services | GovTech | High | 24 h | 12 h | 1 h |
| BP-GT02 Tax compliance casework (FTI) | GovTech | High | 48 h | 8 h | 1 h |
| BP-SW02 Civic Suite service | Software | Moderate | 24 h | 8 h | 4 h |
| BP-SW05 SaaS customer support and notices | Software | Moderate | 24 h | 8 h | 4 h |
| BP-IC03 Managed application support for agency systems | IT Consulting | Moderate | 24 h | 12 h | 4 h |
| BP-GT06 Constituent services for local governments | GovTech | Moderate | 72 h | 24 h | 4 h |
| BP-GT09 ACMP release pipeline and emergency patching | GovTech | Moderate | 72 h | 24 h | 24 h |
| BP-IC02 DoD engagement delivery in the CUI enclave | IT Consulting | Moderate | 72 h | 24 h | 4 h |
| BP-SW03 Grants Management federal edition | Software | Moderate | 72 h | 24 h | 4 h |
| BP-IC01 Client engagement delivery | IT Consulting | Moderate | 72 h | 48 h | 24 h |
| BP-G06 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-G07 Payroll and HR | Group | Moderate | 120 h | 72 h | 24 h |
| BP-GT08 Implementation and data migration projects | GovTech | Low | 120 h | 72 h | 24 h |
| BP-GT07 AI eligibility assistant | GovTech | Low | 168 h | 72 h | 24 h |
| BP-SW06 RMS AI report-writing assist (beta) | Software | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **The notification desk (BP-G05) is a High process with a 1-hour RTO.** A suspected CJI incident must be reported within 1 hour (CJISSECPOL v6.1 IR-6), revenue agencies must report FTI incidents to TIGTA and the IRS Office of Safeguards within 24 hours (Pub. 1075 sec. 1.8), and Florida agencies must report ransomware within 12 hours (Fla. Stat. 282.318(3)(c)9.c.(I); 282.3185(5)(b)). These are agency clocks, but the agency can only meet them if the group tells it in time. The RPO of 24 hours reflects that the contact lists change slowly and are printed in every incident binder.
- **Public safety drives the shortest division MTD.** The RMS (BP-SW01) holds prior-contact and warrant information officers use in the field. Its MTD of 4 hours is shorter than the ACMP's, because supervision officers can run one shift on printed rosters (BP-GT01) and RMS users cannot.
- **SNAP timeliness drives the IEP** (BP-GT03). Expedited households must receive benefits by the 7th calendar day after filing (7 CFR 273.2(i)(3)), and others within 30 days (273.2(g)(1)). One day of downtime is survivable; several days push expedited cases past their deadline.
- **Revenue more than time drives tax casework** (BP-GT02). The revenue agencies' own tax systems keep collections running for 2 days, but the contracts set an 8-hour RTO and the FTI tenants carry the heaviest notice duties.
- **The AI features are Low** (BP-GT07, BP-SW06). Caseworkers and officers do the full work without them. This matters for P10: switching them off is always a safe fallback.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Sealed break-glass accounts per critical system are the fallback |
| Landing zones and keys (SYS-G3) | Group | ACMP, IEP, MVSP, RMS, Grants Management, CUI enclave | FTI tenants use customer-managed keys held in group key management; losing keys is losing the data |
| Backup vault (BP-G04) | Group | ACMP, IEP, RMS, Civic Suite | One backup design serves every regulated workload. A full ACMP restore has never been tested (section 8) |
| SOC facts (BP-G02) and notification desk (BP-G05) | Group | Every agency, customer, DoD, and SEC notice | Every clock in P08 depends on the SOC establishing what happened and the desk reaching the right contact |
| Shared-service staff with access to CJI and FTI environments | Group | GovTech and Software CJI and FTI tenants | About 860 corporate staff can reach these environments; screening is tracked by division, not for corporate (scenario gap 1) |
| Acquired consulting firm's identity provider and directory trust | IT Consulting | Group directory | A migration trust links an estate outside group EDR to the group directory (scenario gap 7; the P08 entry path) |
| GovTech consultants and IT Consulting managed services | GovTech; IT Consulting | Agency-owned systems | Both divisions' staff hold agency-issued accounts; an incident on group laptops can reach agency networks |
| RMS connectors (BP-SW04) | Software | State message switches | Same state CSAs as the ACMP CJI cluster; one CJIS incident can involve both divisions |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); the provider B vault as the only immutable copy for every regulated workload (accepted, because the vault account has a separate identity and deletion lock); one restore team in corporate serving all divisions (P01 GR-08).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | All hosted processes | Infrastructure as code; key backups in a separate key management account |
| SYS-D1 ACMP | BP-GT01, BP-GT02, BP-GT04, BP-GT06 | Database point-in-time recovery (5-minute granularity) plus hourly snapshots copied to the provider B vault |
| SYS-D2 IEP | BP-GT03, BP-GT07 | Same design as the ACMP |
| SYS-D3 MVSP | BP-GT05 | Same design; warm standby region in provider A |
| SYS-D7 RMS | BP-SW01, BP-SW04 | Database replicas across zones; hourly copies to the vault |
| SYS-D6 Civic Suite | BP-SW02 | Database replicas; 4-hourly copies to the vault |
| SYS-D5 CUI enclave | BP-IC02 | Daily backups inside provider A's government-community region |
| People | All | Cross-trained teams; remote work for most staff; restore runbooks per system |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zones, network, and keys
3. The group notification desk (printed contacts first; it runs while everything else is down)
4. SOC visibility (SIEM and EDR)
5. Backup vault access and restore tooling
6. to 10. GovTech: CJI supervision and court cases, integrated eligibility, interfaces, motor vehicle services, and tax casework
11. to 12. Software: the RMS and its connectors (they run in separate accounts, so they often recover in parallel with the ACMP)
13. to 25. Civic Suite, Software support, consulting managed services, constituent services, the ACMP pipeline, DoD engagements, Grants Management, consulting delivery, SEC reporting, implementations, payroll, and the two AI features.

## 8. Key findings
1. **Shared services set the floor.** Identity, landing zones, and the notification desk have RTOs of 1 to 2 hours, shorter than any division process, as they must. The identity RTO of 1 hour was met in both 2026 tests.
2. **The ACMP's 8-hour RTO is proven per tenant, not at scale.** The 2026 test restored 12 tenants in 6 hours. A ransomware event that reaches the whole CJI cluster or several FTI tenants would need about 430 tenant restores; the platform team estimates more than 30 hours (scenario gap 8; P01 GT-003; POAM-011).
3. **Notification capacity is a process in its own right** (BP-G05). If the SOC or the ticketing system is down during an incident, the 1-hour CJI and 12-hour Florida clocks keep running. The P08 runbook therefore uses printed contacts and out-of-band channels.
4. **The acquired consulting firm is outside the recovery design.** Its laptops and file shares are not in the group backup vault or EDR. A ransomware event there is unlikely to stop agency services but can expose CUI held outside the enclave (P01 IC-001, IC-002).
