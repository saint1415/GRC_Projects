# Business Impact Analysis: Cris Santos Company Holdings | Information Technology | Multi-Sector

**Organization:** Cris Santos Company Holdings, Inc. | **Tier:** Multi-Sector (45,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, applied at group and division level
**Prepared by:** Group Chief Risk Officer's resilience team with the three division continuity leads | **Fieldwork:** 2026-05-04 to 2026-07-31 | **Approved:** board risk committee, 2026-09-17

## 1. Overview and purpose
This BIA works at two levels:
- **Group BIA:** the corporate shared services every division depends on (identity, the SOC, the group landing zone and backup vault, notification coordination, finance, HR, and collaboration).
- **Division BIAs:** Cloud Hosting (focus), Managed IT and Consulting, and Payment Processing. They are kept as rows in one workbook (`bia.csv`, `division` column) so cross-division dependencies are visible in one place.

This group has an unusual shape: **the focus division is also the group's platform.** The Payment Processing cardholder data environment, the Managed IT RMM platform, and the DoD CUI enclave all run on the Cloud Hosting division's commercial cloud (SL-1). An SL-1 regional outage is therefore a group event, not a division event.

The BIA supports:
- the contingency planning controls of the HCP SSP (P02: CP-2, CP-4, CP-7, CP-9, CP-10) and the availability rating of the HCP;
- the FedRAMP Government Cloud's availability commitments, including the availability web service required for Class C (CDS-CSO-AVR, P03);
- the Availability category in the SL-1 SOC 2 report and the Managed IT readiness work (P09);
- business recovery in the Payment Processing incident response plan (PCI DSS Requirement 12.10.1) and the SOC 1 settlement controls;
- impact ratings in the risk registers (P01) and the recovery order in the incident runbook (P08).

## 2. System and business description
Corporate shared services run SYS-G1 (identity), SYS-G2 (SOC, SIEM, SOAR, EDR, and the AI triage service), SYS-G3 (the group landing zone on SL-1 and the backup vault at external provider X), and SYS-G4 (corporate SaaS). Division systems are SYS-H1 to SYS-H4 (Cloud Hosting), SYS-M1 and SYS-M2 (Managed IT), and SYS-P1 and SYS-P2 (Payment Processing). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values use the fictional revenue split in `../00_company-facts.md` section 7: Cloud Hosting about $27.9 million per day, Managed IT about $13.2 million per day, and Payment Processing about $8.2 million per day in net revenue (while it moves about $1.9 billion of merchant and biller funds per business day).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $25 million for the group, or more than 1 day of a division's revenue | $2 million to $25 million | Less than $2 million |
| Operations | A division cannot deliver its core service (hosting, managed operations, payments) | One region, service line, or client segment stops | Staff slowed but working |
| Regulatory | Reportable incident under FedRAMP, DFARS, the bank rule, HIPAA, or FTC Safeguards; card network or sponsor bank breach of terms; SEC disclosure | Missed internal or contractual deadline | Internal policy deviation |
| Safety | Not used for this group: no process has a direct physical safety effect. Customers' own safety-related workloads are covered by their own BIAs | | |
| Reputation | National media, loss of agency or bank customers, card network or regulator attention | Regional media or customer complaints | Internal only |

## 4. Process criticality and downtime
`bia.csv` lists 26 processes: 7 group shared services, 8 Cloud Hosting, 5 Managed IT, and 6 Payment Processing. 12 are High, 12 Moderate, and 2 Low. The table is in recovery order.

| Priority | Process | Division | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|---|---|
| 1 | BP-G01 Workforce identity and access | Group shared service | High | 4 h | 1 h | 1 h |
| 2 | BP-H04 Authoritative DNS, content delivery, and DDoS protection | Cloud Hosting | High | 2 h | 1 h | 1 h |
| 3 | BP-H01 Commercial compute, storage, and network data plane | Cloud Hosting | High | 2 h | 1 h | 0 h |
| 4 | BP-H03 Government Cloud (G1) services | Cloud Hosting | High | 4 h | 2 h | 1 h |
| 5 | BP-H08 Hypervisor and storage fleet operations | Cloud Hosting | High | 4 h | 2 h | 1 h |
| 6 | BP-H02 Hosting control plane and customer portal (HCP) | Cloud Hosting | High | 4 h | 2 h | 1 h |
| 7 | BP-G03 Group landing zone, keys, log archive, and backup vault | Group shared service | High | 4 h | 2 h | 1 h |
| 8 | BP-P01 Card authorization switch | Payment Processing | High | 2 h | 1 h | 0 h |
| 9 | BP-G02 Security monitoring and incident response | Group shared service | High | 8 h | 4 h | 1 h |
| 10 | BP-P02 Clearing, settlement, and merchant funding | Payment Processing | High | 24 h | 8 h | 1 h |
| 11 | BP-P03 ACH origination and consumer bill payment | Payment Processing | High | 24 h | 8 h | 1 h |
| 12 | BP-M01 Managed operations for clients | Managed IT | High | 24 h | 8 h | 4 h |
| 13 | BP-H06 Customer support and incident communications | Cloud Hosting | Moderate | 8 h | 4 h | 4 h |
| 14 | BP-G04 Incident notification coordination | Group shared service | Moderate | 24 h | 8 h | 4 h |
| 15 | BP-M03 Client service desk and incident notices | Managed IT | Moderate | 8 h | 4 h | 4 h |
| 16 | BP-G07 Corporate collaboration and IT service management | Group shared service | Moderate | 24 h | 8 h | 4 h |
| 17 | BP-H05 Fleet automation and software supply chain | Cloud Hosting | Moderate | 24 h | 8 h | 4 h |
| 18 | BP-M02 Managed hosting operations | Managed IT | Moderate | 24 h | 8 h | 4 h |
| 19 | BP-P05 Merchant and biller portals and reporting | Payment Processing | Moderate | 24 h | 12 h | 4 h |
| 20 | BP-P04 Merchant onboarding and risk scoring | Payment Processing | Moderate | 72 h | 24 h | 4 h |
| 21 | BP-M04 DoD subcontract delivery (CUI enclave) | Managed IT | Moderate | 72 h | 24 h | 24 h |
| 22 | BP-H07 Metering and billing | Cloud Hosting | Moderate | 72 h | 24 h | 1 h |
| 23 | BP-G05 Financial close and SEC reporting | Group shared service | Moderate | 72 h | 48 h | 24 h |
| 24 | BP-G06 Payroll and HR | Group shared service | Moderate | 120 h | 72 h | 24 h |
| 25 | BP-M05 Consulting and project delivery | Managed IT | Low | 120 h | 72 h | 24 h |
| 26 | BP-P06 Chargebacks and disputes | Payment Processing | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Customer SLAs and the bank rule** drive the hosting data plane and edge (BP-H01, BP-H04: 2-hour MTD). The multi-zone SLA is 99.99% a month, and about 260 banking organizations run covered services on SL-1. An outage that lasts 4 hours or more triggers bank notices under 12 CFR 53.4.
- **Real-time payments** drive card authorization (BP-P01: 2-hour MTD, RPO 0). Card network stand-in processing covers only some transactions, so merchants lose sales from the first minute.
- **Running workloads continue without the control plane.** That is why the HCP (BP-H02) has a 4-hour MTD and a Moderate availability rating in P02, while its confidentiality and integrity are High. Recovery of the HCP can wait a few hours. Its protection cannot.
- **Integrity before speed** drives the RMM (BP-M01) and the software supply chain (BP-H05). Both can reach thousands of systems at once. After a compromise they are restored only after integrity validation, so their RTOs (8 hours) assume a clean restore, not the incident case in P08.
- **File windows and cutoffs** drive settlement and ACH (BP-P02, BP-P03: 24-hour MTD). Missing one window is recoverable with sponsor bank approval; missing two is not.
- **Notification capacity is itself a process** (BP-G02, BP-G04, BP-H06, BP-M03). The FedRAMP Initial Incident Report for a G1 incident rated PAIN-3 to PAIN-5 is due within 1 hour, DFARS reports within 72 hours of discovery, and bank notices as soon as possible after the determination. Those clocks run even when the SOC or support tooling is down.

## 5. Cross-division dependencies and shared services
| Dependency | From | To | Why it matters |
|---|---|---|---|
| Sign-in (SYS-G1) | Group | Every process | A group identity outage stops all administration in all three divisions. Customer workloads keep running. Break-glass accounts per critical system are the fallback |
| SL-1 regions R1 and R3 | Cloud Hosting | Payment Processing (CDE active-active), Managed IT (RMM, SYS-M2), corporate workloads | A two-region failure would stop card authorization. The CDE was designed for one-region loss only |
| HCP partner-operator path | Cloud Hosting | Managed IT managed hosting (BP-M02) | About 1,900 engineers operate about 4,100 tenants through it; the same path is the top cross-division risk (P01 GR-01) |
| Edge services (SYS-H4) | Cloud Hosting | Payment gateways, merchant and biller portals, Managed IT client portals | DNS failure looks like a full outage for every division |
| RMM agents on division servers | Managed IT | Payment Processing settlement support (BP-P02); SYS-M2 enclave (BP-M04) | A malicious script through the RMM reaches the CDE connected-to segment and the CUI enclave (scenario gap 2) |
| SOC facts (SYS-G2) | Group | Every notice in P08; the SEC materiality decision | Every notice clock depends on the SOC establishing what happened, including what the AI triage service closed (P10) |
| Backup vault (external provider X) | Group | All divisions | The only copy outside SL-1; protects against a provider-wide compromise of SL-1 |

**Single points of failure found:**
1. **SYS-G1** (mitigated by break-glass accounts tested quarterly).
2. **One RMM tenant** for all clients and internal uses (P01 GR-02). It is a single point of compromise more than a single point of failure.
3. **Sponsor bank A** for card settlement (accepted: a second sponsor bank is a multi-year commercial decision; P01 PY-012).
4. **The CDE's two-region design.** It assumes R1 and R3 never fail together. A shared failure mode (control plane defect, fleet-wide bad update) would break that assumption (P01 CH-011).

## 6. Resource requirements
| Resource | Supports | RPO method |
|---|---|---|
| SYS-G1 identity platform (SaaS) | All | Vendor multi-region service; configuration exported daily |
| SYS-H1 HCP databases | BP-H02, BP-H03 | Synchronous replication across zones; point-in-time restore within 1 hour; immutable daily copies at external provider X |
| SYS-H2 storage clusters | BP-H01, BP-H03 | Three-way replication within a zone set (RPO 0 for durable storage); cross-region replication is a customer choice |
| SYS-H4 DNS zone data | BP-H04 | Replicated to all points of presence; group zones also at a secondary DNS provider |
| SYS-M1 RMM platform (SaaS) and script library | BP-M01, BP-M02 | Vendor-hosted; script library in version control; configuration export weekly |
| SYS-P1 CDE | BP-P01, BP-P02 | Active-active in R1 and R3; transaction journals replicated synchronously; tokenization vault keys in payment HSMs in both regions |
| SYS-P2 bill pay and ACH | BP-P03 | Database replicas in R3; nightly immutable backups at external provider X |
| SYS-G3 backup vault | All | Immutable, separate backup identity, separate provider |
| People | All | Follow-the-sun SOC in three sites; G1 staffed by U.S. persons only; cross-trained settlement team |

## 7. Recovery priorities
Recovery order across the group (full list in `bia.csv`, `recovery_priority`):
1. SYS-G1 identity and break-glass access
2. to 6. The hosting platform: edge and DNS, the commercial data plane, Government Cloud G1, fleet operations, and the HCP
7. The group landing zone, keys, logs, and backup vault
8. Card authorization
9. SOC visibility
10. and 11. Settlement and ACH, before their next file windows
12. Managed operations for clients (only after integrity validation)
13. to 26. Customer and client communications, notification coordination, collaboration, the supply chain, managed hosting, portals, onboarding, DoD subcontract work, billing, finance, HR, consulting, and disputes.

Edge and DNS come before the data plane because a healthy data plane that customers cannot resolve is still an outage. The SOC comes after card authorization because the SOC has its own fallback (native consoles and the retainer's tools), while merchants have none.

## 8. Key findings
1. **The focus division's availability is the group's availability.** Payment Processing and Managed IT inherit SL-1 availability. Their BIAs did not, until this year, list SL-1 as a dependency. Both now do.
2. **The CDE's 2-hour MTD relies on two SL-1 regions never failing together.** No test has ever simulated a shared failure mode such as a fleet-wide bad update (P01 CH-011; POAM-012).
3. **The fastest notice clock in the group is FedRAMP's.** A G1 incident rated PAIN-3 to PAIN-5 needs an Initial Incident Report within 1 hour. The SOC and G1 support teams must be able to reach FedRAMP and agency contacts without corporate email (P08).
4. **Tooling that can reach everything has the longest real RTO.** The RMM and the fleet automation service have 8-hour RTOs for a clean restore, but after a compromise they stay down until integrity is proven. The P08 runbook plans for days, not hours, and BP-M01's workaround (clients' own remote access) has never been tested at scale.
