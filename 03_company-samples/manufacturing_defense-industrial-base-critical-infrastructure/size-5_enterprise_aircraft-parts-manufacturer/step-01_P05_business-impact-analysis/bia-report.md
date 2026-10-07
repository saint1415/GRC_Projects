# Business Impact Analysis: Cris Santos Company | Defense Industrial Base | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer; DoD prime contractor and subcontractor with CUI) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, the acquired KS-1 plant, and the new AZ-1 additive center. It feeds:
- the contingency plans for the CUI Engineering Enclave (CEE) and the Manufacturing Operations Zone (MOZ) (SP 800-53 CP-2 and CP-10, documented in the SSPs);
- the availability rating and recovery objectives in the CEE System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order and the reporting duties that must continue during an incident in the CUI exfiltration runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

SP 800-171 Rev. 2 has no contingency planning requirement, so this BIA rests on business need, the SEC's expectations for describing cybersecurity risk management (Regulation S-K Item 106), and two DFARS duties that continue during an outage: the 72-hour cyber incident report (DFARS 252.204-7012(c)) and preservation of images of affected systems for at least 90 days (252.204-7012(e)).

**Results in one line:** 17 processes were analyzed; 8 are High criticality, 8 Moderate, and 1 Low. 5 processes need recovery within 8 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 12 of them single points of failure and 3 never tested.

## 2. System and business description
Cris Santos Company makes structural assemblies, composite panels, actuation components, and additively manufactured parts at 8 sites in 6 states, and repairs components at its FL-3 MRO depot. It has 12,000 employees and about $4.8 billion in annual revenue, 56% from defense work. The technology estate is described in `../00_company-facts.md` section 3: the identity platform (SYS-01), the CUI collaboration suite and CEE cloud subscriptions in a government-community cloud (SYS-02, SYS-03), CAD/PLM (SYS-04), about 2,650 engineering endpoints (SYS-05), the Manufacturing Operations Zone with about 1,150 CNC machines and 36 metal additive printers (SYS-06), the enterprise and plant networks (SYS-07), the security operations platform (SYS-08), ERP (SYS-09), the commercial cloud platforms for the SL-1 and SL-2 service lines (SYS-11), the KS-1 legacy environment (SYS-12), and the stand-alone classified system (SYS-13).

## 3. Impact categories and values
Dollar values are scaled to about $19.2 million of shipments per production day (about $4.8 billion over about 250 production days) and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | A plant stops, or nothing can ship from two or more plants | One department, work cell, or service line stops | Staff slowed but working |
| Regulatory | Missed DFARS 72-hour report; unauthorized ITAR release; loss of CMMC status; missed SEC filing; missed NISPOM report | Missed contract quality or delivery notice to a prime | Internal policy deviation |
| Safety | A nonconforming flight part could reach an aircraft, or a wrong NC program or build file could injure a worker | Defect caught at inspection; rework or scrap | None |
| Reputation | Prime supplier rating downgrade, loss of source approval, national media, or analyst action | Corrective action request from a prime; regional media | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Production release and machining | High | 24 h | 8 h | 1 h | $7.30M |
| BP-02 Composite fabrication | High | 24 h | 12 h | 4 h | $2.60M |
| BP-05 Quality inspection and product acceptance | High | 24 h | 8 h | 1 h | $11.50M |
| BP-09 Shipping, receiving, and DoD spares delivery | High | 24 h | 8 h | 1 h | $17.50M |
| BP-10 Component MRO and the SL-1 customer portal | High | 24 h | 8 h | 1 h | $1.60M |
| BP-12 Contracts, export compliance, and DoD incident reporting | High | 24 h | 4 h | 24 h | $0.30M |
| BP-03 Final assembly and delivery of structural assemblies | High | 48 h | 24 h | 4 h | $4.00M |
| BP-08 CUI exchange with primes, DoD, and suppliers | High | 48 h | 12 h | 4 h | $2.20M |
| BP-11 Aircraft health monitoring analytics (SL-2) | Moderate | 24 h | 12 h | 4 h | $0.25M |
| BP-07 NC programming and build-file preparation | Moderate | 48 h | 24 h | 15 min | $0.90M |
| BP-17 KS-1 fabrication on legacy systems | Moderate | 48 h | 24 h | 24 h | $1.10M |
| BP-04 Additive manufacturing | Moderate | 72 h | 24 h | 24 h | $0.60M |
| BP-06 Engineering design and change control | Moderate | 72 h | 24 h | 15 min | $1.20M |
| BP-13 Supply chain, purchasing, and supplier quality | Moderate | 72 h | 24 h | 1 h | $1.80M |
| BP-15 Payroll and human resources | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-14 Financial close, government contract billing, and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.40M |
| BP-16 Classified program work (Program K) | Low | 120 h | 72 h | 24 h | $0.15M |

**What drives the values:**
- **Shipments and prime ratings** drive production, inspection, and shipping (BP-01, BP-05, BP-09). Shipping is the largest single exposure because revenue is recognized at shipment: each day of outage defers about $17.5 million.
- **Integrity matters as much as availability.** A restored NC program, build file, or inspection record that is one revision old can produce a nonconforming flight part. Recovery of BP-01, BP-04, BP-05, and BP-07 includes a revision check against PLM before release.
- **Regulation** sets the shortest RTO: contracts, export compliance, and DoD incident reporting (BP-12, 4 hours), because the DFARS 72-hour clock and the NISPOM duty to report classified system incidents immediately (32 CFR 117.8(f)(1)) do not stop during an outage.
- **Contracts** set the service line objectives: MRO turnaround commitments for aircraft-on-ground orders (BP-10) and SL-2 availability commitments (BP-11, P09).
- **Financial close (BP-14)** tightens to a 48-hour MTD in the quarter-end window because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **One file transfer product, two instances (DEP-08, DEP-09).** The CUI exchange gateway in the CEE and the corporate file transfer instance run the same managed file transfer product. A single zero-day vulnerability could expose both CUI and corporate data, and the vendor has no contractual commitment to notify the company of vulnerabilities within a set time. This is the P08 incident scenario and P01 risk R-001.
2. **KS-1 legacy environment (DEP-20, DEP-21).** KS-1's file server and MES are backed up weekly to disk in the same building, so the real RPO is up to 7 days against a 24-hour target, and the restore has never been tested. Its legacy SFTP server exchanges CUI outside the certified scope. Both close with the KS-1 integration (P01 R-022; POAM-020).
3. **AZ-1 build files move by USB (DEP-22).** There is no network path from PLM to the 36 printers. Build files are copied to labeled drives, which adds handling time and integrity and malware risk (P01 R-023; POAM-006).
4. **Autoclave controllers (DEP-14).** The two GA-1 autoclaves run controllers on an unsupported operating system. They are isolated, but a failure would stop all composite cure capacity until a qualified supplier takes overflow (P01 R-044).
5. **Sole-source forgings (DEP-15).** One supplier provides about 70% of titanium forgings for Prime A parts, holds CUI drawings, and has provided no cyber assurance evidence (P01 R-035).
6. **SL-2 single region (DEP-17).** The aircraft health monitoring platform runs in one region of Cloud provider A; the estimated rebuild time of 18 hours exceeds its 12-hour RTO (P09).
7. **Enterprise platforms met their tests.** PLM recovered in 9.5 hours against a 24-hour RTO in the 2026-05-09 regional failover test, MES failed over to DC-2 in 6.5 hours against 8 hours on 2026-03-28, and the DIBNet reporting drill on 2026-04-15 met its 4-hour target.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Identity platform | SSO, MFA, PAM, identity governance; break-glass accounts | All |
| SYS-02 CUI collaboration suite | CUI email, file storage, chat | BP-06, BP-08, BP-12 |
| SYS-03 CEE cloud subscriptions | PLM tier, virtual desktops, CUI exchange gateway, backup vault, logs | BP-04 to BP-08 |
| SYS-04 CAD/PLM | About 2.4 million controlled documents | BP-01 to BP-07 |
| SYS-05 Engineering endpoints | About 2,650 workstations and laptops | BP-06, BP-07 |
| SYS-06 MOZ | MES, DNC, CNC machines, CMMs, printers, autoclaves, test cells | BP-01 to BP-05, BP-07, BP-09 |
| SYS-07 Networks | SD-WAN, plant segments, NAC, IPsec to SYS-03 | All site-based processes |
| SYS-08 Security operations platform | SIEM, EDR, SOC | Detection and clean recovery of all |
| SYS-09 ERP | Orders, purchasing, shipping, government accounting | BP-09, BP-10, BP-13, BP-14 |
| SYS-11 Commercial cloud platforms | SL-1 portal, SL-2 analytics | BP-10, BP-11 |
| SYS-12 KS-1 legacy environment | File server, MES, DNC, SFTP | BP-17 |
| SYS-13 Classified information system | Stand-alone, closed area | BP-16 |
| DoD reporting capability | 4 medium assurance certificates, 2 clean laptops, contact lists | BP-12 |
| People and facilities | Operators, inspectors, engineers, SOC, IT and OT engineering; 8 sites and 2 data centers | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | DoD reporting capability (clean endpoint, certificate, contacts) | 4 h | Second certificate holder; phone prime security contacts |
| 2 | SYS-01 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts at FL-1 and DC-2 |
| 3 | SYS-07 SD-WAN, plant segments, DNS | 2 h | Cellular failover for critical traffic |
| 4 | SYS-08 security tooling (EDR console, SIEM) for clean-room validation | 2 h | Second SOC location |
| 5 | SYS-09 ERP and shipping documents | 8 h | Downtime reports; manual shipping documents |
| 6 | MES, quality management system, and DNC (SYS-06) | 8 h | Failover to DC-2; printed job packets |
| 7 | SL-1 MRO portal (SYS-11) | 8 h | Second region; phone and email status |
| 8 | CUI exchange gateway (SYS-03) | 12 h | Prime portals from virtual desktops |
| 9 | SL-2 analytics platform (SYS-11) | 12 h target (about 18 h today) | Daily summary reports |
| 10 | PLM, virtual desktops, and CUI suite (SYS-02 to SYS-04) | 24 h | Second-region standby; local CAD work checked in later |
| 11 | Engineering endpoints (SYS-05) | 24 h | Virtual desktops while workstations are reimaged |
| 12 | AZ-1 build-prep workstations | 24 h | Reimage from baseline (once documented, POAM-004) |
| 13 | KS-1 legacy file server and MES (SYS-12) | 24 h target (up to 7 days of data loss today) | Printed job packets |
| 14 | Payroll and HR SaaS | 48 h | Repeat prior payroll |
| 15 | Financial close and consolidation | 72 h (48 h at quarter end) | Manual entries |
| 16 | Classified information system (SYS-13) | 72 h | Pause classified work; approved storage |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| One managed file transfer product for the CEE gateway and the corporate instance; no vendor notification commitment | P01 R-001 and R-033; P08 |
| KS-1 weekly backups in the same building; legacy SFTP outside the certified scope | P01 R-022 and R-046; P03 G-135; POAM-020 |
| AZ-1 USB-only path to printers | P01 R-023; POAM-006 |
| GA-1 autoclave controllers on an unsupported operating system | P01 R-044 |
| Sole-source forging supplier without cyber assurance evidence | P01 R-035; POAM-018 |
| SL-2 single-region recovery (18 h against a 12 h RTO) | P09 A1.2 and A1.3 |
