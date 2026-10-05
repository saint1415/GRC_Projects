# Business Impact Analysis: Cris Santos Company Holdings | Construction | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's continuity team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-15

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, SOC, cloud and network, the payment factory, email, payroll, financial close, and the CUI enclave).
- **Division BIAs:** Commercial Construction (focus), Commercial Property, and Architecture and Engineering (A&E). They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

It supports:
- the availability rating of the Project Delivery and Payment Platform (PDPP) in the SSP (P02);
- impact ratings in the group and division risk registers (P01);
- the recovery order and notice priorities in the incident runbook (P08);
- the availability commitments of the two services in SOC 2 scope (P09: the TSSI managed service and the A&E digital twin service).

## 2. System and business description
Corporate shared services run SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and network, SYS-G4 ERP and payment factory, SYS-G5 commercial email and files, and SYS-G6, the CUI enclave. The PDPP is the shared project management and pay application platform used by all three divisions. Division systems are SYS-D1 and SYS-D2 (Construction field systems and TSSI tools), SYS-D3 and SYS-D4 (Property management platform and building systems), SYS-D5 (A&E design platform), and SYS-D6 (AI estimating and bid assistant). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 1: Construction about $39 million of billings a day, Property about $5.8 million a day, and A&E about $4.7 million a day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20 million for the group, a diverted payment above $5 million, or more than 1 day of a division's revenue | $1 million to $20 million | Less than $1 million |
| Operations | A division cannot deliver its core service (build, operate buildings, design) or jobsites stop | One region, project group, or property stops | Staff slowed but working |
| Regulatory | DoD cyber incident report, loss of a CMMC status or SPRS eligibility, state breach notices, or SEC disclosure | Missed contract deadline or late certified payroll | Internal policy deviation |
| Safety | Plausible injury to workers, tenants, or the public (superseded structural drawings, failed life-safety interface, no permits) | Delayed but safe work | None |
| Reputation | National media, loss of federal work, or owner or tenant loss of trust after a payment fraud | Regional media or client complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 30 processes: 9 group shared services, 10 Construction, 6 Property, and 5 A&E. 12 are High, 15 Moderate, and 3 Low.

| Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|
| BP-G01 Workforce identity and access | Group | High | 4 h | 1 h | 1 h |
| BP-G03 Group cloud platform, WAN, and jobsite connectivity | Group | High | 4 h | 2 h | 1 h |
| BP-G02 Security monitoring and incident response | Group | High | 8 h | 4 h | 1 h |
| BP-G04 Payment factory: disbursements and vendor master | Group | High | 24 h | 8 h | 4 h |
| BP-C01 Project document control | Construction | High | 8 h | 4 h | 1 h |
| BP-C05 Jobsite safety management | Construction | High | 8 h | 4 h | 4 h |
| BP-P01 Building operations and BAS | Property | High | 8 h | 4 h | 4 h |
| BP-P02 Access control and video at owned properties | Property | High | 8 h | 4 h | 4 h |
| BP-C02 Pay application processing | Construction | High | 72 h | 24 h | 4 h |
| BP-G09 CUI enclave services | Group | High | 24 h | 8 h | 4 h |
| BP-A02 Federal CUI design production | A&E | High | 48 h | 24 h | 4 h |
| BP-C10 TSSI managed service for clients | Construction | High | 12 h | 4 h | 1 h |
| BP-C04 Field operations and daily reporting | Construction | Moderate | 24 h | 12 h | 4 h |
| BP-C03 Subcontractor management and compliance | Construction | Moderate | 72 h | 24 h | 24 h |
| BP-G05 Billing and cash application | Group | Moderate | 72 h | 24 h | 24 h |
| BP-P03 Rent billing and collections | Property | Moderate | 72 h | 24 h | 24 h |
| BP-G07 Email and collaboration | Group | Moderate | 24 h | 8 h | 4 h |
| BP-G06 Payroll and certified payroll | Group | Moderate | 72 h | 48 h | 24 h |
| BP-A01 Commercial design production | A&E | Moderate | 48 h | 24 h | 4 h |
| BP-A03 Design review, quality control, and sealing | A&E | Moderate | 48 h | 24 h | 4 h |
| BP-A04 Digital twin facility data service | A&E | Moderate | 48 h | 12 h | 4 h |
| BP-P05 Parking operations and card payments | Property | Moderate | 24 h | 8 h | 24 h |
| BP-P04 Tenant service requests and portal | Property | Moderate | 48 h | 24 h | 24 h |
| BP-C06 Estimating and bidding | Construction | Moderate | 72 h | 24 h | 24 h |
| BP-C08 Federal contract compliance operations | Construction | Moderate | 72 h | 48 h | 24 h |
| BP-G08 Financial close and SEC reporting | Group | Moderate | 72 h | 48 h | 24 h |
| BP-C09 TSSI installation and commissioning | Construction | Moderate | 72 h | 24 h | 24 h |
| BP-P06 Leasing and lease administration | Property | Low | 120 h | 72 h | 24 h |
| BP-A05 A&E project accounting and invoicing | A&E | Low | 120 h | 72 h | 24 h |
| BP-C07 Equipment fleet and telematics | Construction | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **Safety** drives the 8-hour MTDs for document control, jobsite safety, and building operations. Crews start at 6 a.m. and must not build from superseded structural or life-safety drawings. Building life-safety interfaces stay under local control, which is why the BAS front ends can be down for hours without harm.
- **Money integrity more than availability** drives pay applications (BP-C02) and the payment factory (BP-G04). A pay application can wait 3 days. A wrong remittance instruction cannot be undone, and on federal jobs the subcontractor must still be paid within 7 days of the Government's payment (FAR 52.232-27(c)(1)). The RPO of 4 hours protects the vendor-master change log, the evidence trail for any fraud.
- **Federal rules, not convenience,** drive the CUI enclave (BP-G09). If the enclave is down there is no lawful workaround: CUI may not move to commercial email or the PDPP (DFARS 252.204-7012(b)(2)(ii)(D); 252.204-7021(d)(2)). Federal design work pauses instead.
- **Client commitments** drive the TSSI managed service (BP-C10, 4-hour response to critical alarms at hospitals and federal sites) and the digital twin service (BP-A04, 99.5% monthly availability).

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all three divisions at once. Break-glass accounts per critical system are the fallback |
| PDPP document control and pay applications | Construction (platform business owner) | A&E design-build revisions; Property tenant improvement and capital projects | The divisions exchange drawings and approve intercompany pay applications in one platform |
| CUI enclave (BP-G09) | Group | A&E federal design (BP-A02); Construction DoD field use | CUI drawings must flow from A&E to the field through the enclave gateway, not the PDPP. The current workaround breaks this rule (gap 1) |
| Payment factory (BP-G04) | Group | Construction and A&E payments | Bank-change verification is strong here. Property accounts payable runs outside it (gap 3) |
| SOC facts (BP-G02) | Group | All divisions; DoD report; SEC decision | Every notice clock in P08 depends on the SOC establishing what happened |
| TSSI installations | Construction | Property access control and video at 12 properties | Same Section 889 screening should apply to both; it does not today (gap 5) |
| Digital twin service (BP-A04) | A&E | Property facility data for 22 owned buildings | Property maintenance planning depends on A&E's service |
| Email (BP-G07) | Group | Owner, tenant, and subcontractor correspondence | The main fraud channel (P08) |

**Single points of failure found:** SYS-G1 (mitigated by break-glass accounts, tested quarterly); one project management SaaS vendor for all project records (mitigated by a nightly export to the group cloud, P01 CON-012); one parking technology service provider for all 18 garages (accepted, P01 PRP-014).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-G3 landing zones, keys, logs | Cloud-hosted processes | Infrastructure as code; immutable backups in provider B |
| PDPP project management SaaS tenant | BP-C01, BP-C02, BP-C04 | Vendor replication; nightly full export of project records to the group cloud (independent copy) |
| PDPP integration and payment-instruction services | BP-C02, BP-G04 | Infrastructure as code; database backups every 4 hours to the provider B vault |
| SYS-G4 ERP and payment factory (SaaS) | BP-G04, BP-G05, BP-G08 | Vendor replication; daily extracts; bank files retained 7 years |
| SYS-G6 CUI enclave | BP-G09, BP-A02 | Provider backups inside the authorized boundary; restore tested twice a year |
| SYS-D4 building controllers | BP-P01, BP-P02 | Controller configuration backups held by integrators (not by Property; P01 PRP-004) |
| People | All | Cross-trained project accountants; on-site building engineers at every property |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. Cloud landing zone, WAN, and jobsite connectivity
3. SOC visibility (SIEM, EDR, email security)
4. Payment factory, with the vendor master frozen until verified
5. to 8. Project document control, jobsite safety, building operations, and building access control
9. Pay application processing
10. and 11. CUI enclave services and federal CUI design production
12. TSSI managed service for clients
13. to 30. Field reporting, subcontractor compliance, billing, rent collection, email, payroll, A&E design and review, the digital twin service, parking, tenant services, estimating, federal compliance operations, financial close, TSSI installation, leasing, A&E invoicing, and fleet telematics.

Email (BP-G07) is deliberately not first. In a payment fraud incident, restoring email before identity is secured hands the channel back to the attacker (P08).

## 8. Key findings
1. **RTOs for shared services are shorter than any division's**, as they must be. The group identity RTO of 1 hour was met in two tests in 2026.
2. **The PDPP depends on one SaaS vendor.** The nightly independent export (added in 2025) has been restore-tested once. A second test with the project teams is planned for 2026-12 (P01 CON-012).
3. **The CUI enclave has no lawful workaround.** Its availability target is set by contract schedules, and the BIA records that field teams must not fall back to commercial tools. Today they do so even when the enclave is up (gap 1), which is a confidentiality failure, not an availability one.
4. **Property building systems recover locally, but nobody else can see them.** Their controller backups are held by integrators, not by Property, and the group SOC cannot see them (gap 4). Recovery after a ransomware event at an integrator is unproven.
5. **Notification capacity is itself a process** (BP-G02, BP-C08, BP-G08). If the SOC or the compliance office is down during an incident, the DoD 72-hour clock keeps running. The P08 runbook uses out-of-band channels for this reason.
