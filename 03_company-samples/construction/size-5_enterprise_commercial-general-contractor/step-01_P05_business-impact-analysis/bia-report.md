# Business Impact Analysis: Cris Santos Company | Construction | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded commercial and institutional building general contractor) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the two acquired businesses (AQ-1 and AQ-2). It feeds:
- the availability rating and recovery objectives in the Project Delivery and Payment Platform (PDPP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the business email compromise runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09);
- the incident response and recovery requirements for the Federal Programs CUI Enclave (SP 800-171 R2 3.6.1, assessed in P03).

**Results in one line:** 17 processes were analyzed; 10 are High criticality, 6 Moderate, and 1 Low. 6 processes need recovery within 8 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 16 of them single points of failure and 6 never tested.

## 2. System and business description
Cris Santos Company builds for health care, higher education, civic, federal and defense, aviation, data center, and commercial office clients from a Florida headquarters and nine regional offices in eight states. It runs about 300 active projects at about 140 jobsites (16 on military installations), two prefabrication and equipment yards, and two colocation data centers. It has 12,000 employees and about $4.8 billion in annual revenue. Money moves in two large monthly streams: about $400 million of owner pay apps in, and about $300 million of subcontractor and supplier payments out. The technology estate is described in `../00_company-facts.md` section 3. Two businesses were acquired recently: AQ-1 (Texas MEP contractor, 2025-10) still runs its own ERP and email; AQ-2 (Virginia federal builder, 2026-03) still holds FCI on legacy systems.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative, or a single diverted payment above $1 million | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | Work stops at more than 20 jobsites, or payments to subcontractors stop company-wide | One region, one business unit, or up to 20 jobsites affected | Staff slowed but working |
| Regulatory and contract | Breach of a federal clause that affects award eligibility (CMMC, DFARS 252.204-7012); missed SEC filing; missed prompt payment duty | Missed contractual notice or documentation deadline | Internal policy deviation |
| Safety | Plausible injury (work from superseded drawings, loss of safety reporting, client security systems unmonitored) | Delayed but safe work | None |
| Reputation | National media, analyst or rating action, loss of a federal customer or major owner | Regional media; owner or subcontractor complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-11 BTS managed monitoring for clients (SL-1) | High | 4 h | 2 h | 1 h | $0.25M |
| BP-05 Treasury cash management and wires | High | 24 h | 4 h | 15 min | $0.90M |
| BP-01 Field execution and document control | High | 24 h | 8 h | 1 h | $4.60M |
| BP-08 Federal CUI project delivery | High | 24 h | 8 h | 4 h | $1.80M |
| BP-07 Estimating and bid submission | High | 24 h (4 h on bid day) | 8 h | 4 h | $2.00M |
| BP-13 Safety management and incident reporting | High | 24 h | 8 h | 4 h | $0.20M |
| BP-12 Capital Program Portal for owners (SL-2) | Moderate | 48 h | 12 h | 1 h | $0.15M |
| BP-16 Jobsite access control and time capture | Moderate | 24 h | 12 h | 4 h | $0.50M |
| BP-03 Subcontractor and supplier payments | High | 72 h | 24 h | 1 h | $1.20M |
| BP-04 Payee and bank-account verification | High | 48 h | 24 h | 15 min | $0.40M |
| BP-02 Owner progress billing (pay apps) | High | 72 h | 24 h | 4 h | $13.20M (deferred) |
| BP-06 Payroll and certified payroll | High | 72 h | 24 h | 24 h | $1.60M |
| BP-09 Design coordination, BIM, and VDC | Moderate | 48 h | 24 h | 4 h | $0.60M |
| BP-10 Procurement and subcontract management | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-17 AQ-1 project accounting, billing, and AP | Moderate | 72 h | 48 h | 24 h | $0.80M |
| BP-14 Equipment, fleet, and prefabrication yards | Low | 72 h | 48 h | 24 h | $0.25M |
| BP-15 Financial close and SEC reporting | Moderate | 120 h (48 h at quarter-end) | 72 h | 24 h | $0.10M |

**What drives the values:**
- **Safety and field productivity** set the shortest field objectives. About 28,600 people work on company jobsites each day. Offline drawing caches on tablets last about one shift, so BP-01 has a 24-hour MTD and an 8-hour RTO.
- **Cash, not time,** drives owner billing (BP-02). Owners still pay late pay apps, so the MTD is 72 hours inside the pay app window, but each day of outage defers about $13.2 million of receipts.
- **Integrity, not availability,** drives payee verification (BP-04). Payments to changed accounts can be held for two days without harm, but the change log must be exact (RPO 15 minutes), because it is the evidence for a bank recall, an insurance claim, and the P08 runbook.
- **Contracts and regulation** set the federal objectives. FAR 52.232-27(c)(1) requires subcontractor payment within 7 days of a federal payment (BP-03), certified payrolls are weekly (BP-06), and CUI cannot move to commercial systems during an outage (BP-08), so the only workaround is printed sets in the controlled plan rooms.
- **Client commitments** set BTS monitoring (BP-11, 2-hour restoration) and the Capital Program Portal (BP-12, 12-hour restoration), because external clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Project management platform (DEP-01).** One SaaS platform carries every project's drawings, RFIs, and pay app workflow for about 50,000 users. The vendor's contract RTO is 24 hours, against a BIA RTO of 8 hours for BP-01, and the company has never restored its nightly export. This is P01 risk R-010 and POA&M item POAM-008.
2. **Payment hub (DEP-04, DEP-06).** All outbound payments pass through one file transfer gateway cluster. Files to one of the three banks carry no end-to-end integrity check (R-006, POAM-006). The bank account validation service has no tested fallback beyond call-back and no SOC report on file (POAM-012).
3. **AQ-1 (DEP-22, DEP-23).** The AQ-1 legacy ERP has nightly backups only (real RPO 24 hours), a 72-hour vendor RTO against a 48-hour BIA RTO, and no restore test. Its payment files enter the enterprise payment hub without enterprise payee verification, which is how the 2026-04 payment fraud loss happened (R-003, POAM-003). The AQ-1 email tenant has no SIEM feed (R-044, POAM-004).
4. **Federal enclave (DEP-09).** The FPCE depends on one government community cloud tenant. The 2026-04 restore test met the 8-hour RTO. The printed plan room sets are the workaround, which is why plan room controls matter for both availability and CUI protection (P03).
5. **Industry and government dependencies (DEP-17, DEP-18).** Bid portals and SAM are single points of failure the company cannot remove; the workarounds are procedural.
6. **Jobsite connectivity (DEP-10).** 40% of trailers rely on one cellular carrier. A second carrier is being added during the 2027 equipment refresh.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Project management platform | Vendor SaaS system of record for drawings, RFIs, daily logs, pay app workflow | BP-01, BP-02, BP-10 |
| SYS-02 ERP (Cloud provider A) | Project accounting, billing, AP, vendor master, payment files | BP-02 to BP-04, BP-10, BP-15 |
| SYS-03 Payroll SaaS | Weekly and certified payroll | BP-06 |
| SYS-04 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-05 Productivity suite | Email, files, chat | BP-01, BP-02, BP-07, BP-10 |
| SYS-06 Treasury and payment hub | Bank file transfer gateway, approvals, positive pay, bank account validation | BP-03 to BP-05 |
| SYS-07 Cloud provider A and B workloads; COLO-1 and COLO-2 | Estimating database, virtual desktops, Capital Program Portal, BTS platform, network core, offline backup copies | BP-07, BP-09, BP-11, BP-12; recovery of all |
| SYS-08 Enterprise and jobsite networks | SD-WAN; cellular routers at about 140 trailers | All site-based processes |
| SYS-09 Endpoints | Laptops, phones, rugged tablets, kiosks | BP-01, BP-13, BP-16 |
| SYS-10 FPCE | CUI collaboration, document control, virtual desktops, plan room plotters | BP-08 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to COLO-2 | RPO for all Cloud A and B workloads |
| People | Superintendents, project managers, Payment Operations, payroll, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at offices |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Managed security service provider tooling |
| 4 | BTS monitoring platform (SL-1) | 2 h | Client on-site consoles; technician dispatch |
| 5 | Treasury and payment hub, bank connectivity | 4 h | Bank portals with dual approval |
| 6 | Project management platform access (vendor SaaS) | 8 h target (24 h per vendor contract) | Offline tablet sync; printed sets |
| 7 | FPCE tenant and plan room plotters | 8 h | Printed CUI sets in plan rooms |
| 8 | Estimating database, bid tools, and productivity suite | 8 h | Laptop templates; phone bids |
| 9 | Safety management and badging services | 8 to 12 h | Paper forms; printed badge lists |
| 10 | Capital Program Portal (SL-2) | 12 h | Exports through the secure file-transfer portal |
| 11 | ERP billing, AP, and vendor master; payroll | 24 h | Bank portal payments for critical payees; repeat prior payroll |
| 12 | Virtual desktops for BIM and VDC | 24 h | Local model copies |
| 13 | AQ-1 legacy ERP | 48 h target (72 h per vendor contract) | Manual pay apps |
| 14 | Telematics, financial close tools | 48 to 72 h | Phone dispatch; last extracts |

During the pay app window (the 20th to the 25th of each month) and on payment run days, the incident commander may move the ERP billing and AP modules ahead of priority 8.

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Project management platform: vendor RTO 24 h against an 8 h BIA RTO; export never restored | P01 R-010; P02 CP-10; POAM-008 |
| Payment files to one bank without end-to-end integrity checks | P01 R-006; P02 SI-7(1); POAM-006 |
| AQ-1 payment files bypass enterprise payee verification; AQ-1 ERP RPO 24 h and RTO 72 h | P01 R-003; P07 SI-10; POAM-003 |
| AQ-1 email tenant without monitoring | P01 R-044; POAM-004 |
| Bank account validation and e-signature services without SOC report reviews | P01 R-036 and R-037; POAM-012 |
| Plan rooms are the only CUI workaround but are not in the FPCE SSP boundary | P03 G-087; POAM-020 |
