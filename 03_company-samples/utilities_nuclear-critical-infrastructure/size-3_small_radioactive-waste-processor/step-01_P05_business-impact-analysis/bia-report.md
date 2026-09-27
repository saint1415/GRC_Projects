# Business Impact Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

**Organization:** Cris Santos Company, LLC (radioactive and hazardous waste processor) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager with the Radiation Safety Officer, Operations Manager, and Compliance and Transportation Manager | **Approved:** General Manager, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the company depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan due 2026-12-31 (POAM-004);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

It also documents how the company keeps meeting two Part 37 duties when systems fail: monitoring and detection "without delay" (10 CFR 37.41(b), 37.49(a)(1)) and records protected against loss (37.101).

## 2. System and business description
The company runs one Florida site (the Plant) with 60 employees and about 450 customer accounts. Business work runs on the Business Operations and Records Platform (BORP): SaaS for email and files, waste tracking, accounting, and HR; an identity provider; a cloud tenant (source inventory, records archive, backups); and the site business network. Plant processing runs on the OT network. The sealed source vault is protected by the IDS, the PACS, and video. See `../00_company-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $28.2 million in annual receipts, about $113,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $300,000 (about 3 business days) | $50,000 to $300,000 | Less than $50,000 |
| Operations | Receiving or processing stops for the whole Plant | One line or service slows or stops | Staff slowed but working |
| Regulatory | Violation of the license, Part 37, or the RCRA permit; a reportable event | Missed record or timeliness requirement | Internal procedure deviation |
| Safety | Plausible radiation exposure or release, or a window for theft of category 2 material | Degraded but controlled safety or security margin | None |
| Reputation | Customer loss, State enforcement publicity, or loss of a reactor customer | Customer complaints | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Part 37 security monitoring and access control | High | 4 h | 2 h | 24 h |
| BP-02 Radiation safety and effluent monitoring | High | 8 h | 4 h | 1 h |
| BP-03 Waste receiving and radiological survey | High | 24 h | 8 h | 4 h |
| BP-04 Storage and inventory control | High | 24 h | 12 h | 4 h |
| BP-05 Processing operations | Moderate | 72 h | 48 h | 24 h |
| BP-06 Outbound shipping and manifesting | Moderate | 72 h | 24 h | 4 h |
| BP-07 Customer pickups and field services | Moderate | 48 h | 24 h | 24 h |
| BP-08 Customer service and portal | Moderate | 48 h | 24 h | 4 h |
| BP-09 Regulatory records and reporting | Moderate | 72 h | 48 h | 24 h |
| BP-10 Billing and accounts receivable | Low | 120 h | 72 h | 24 h |
| BP-11 HR, payroll, and access authorization records | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Security and safety drive BP-01 and BP-02, not money.**
  - The vault IDS keeps working on its own battery and cellular path, so detection is never fully lost.
  - Badge control and video are a different matter. They sit on the business network today, so a network outage removes them.
  - The workaround is direct control of the vault by approved individuals (37.47(c)(2)). Staff can sustain that for a shift, not for days. That sets the 4-hour MTD.
- **Regulatory records drive BP-04, BP-06, and BP-09.** Inventory, manifest, and shipment records are license, Part 37, and RCRA permit duties, so data loss matters more than downtime (RPO 4 hours for inventory and manifests).
- **Processing (BP-05) can wait three days.** Incoming containers can be stored unopened. That makes it Moderate, even though it is where the revenue comes from.

**Key findings:**
- **BP-01's 2-hour RTO cannot be met today.** In a ransomware event on the business network, the PACS server and NVR would be down along with office systems. They would be restored in the same queue, with no separate recovery path (P01 R-003; P03 G-046, G-047).
- **The 4-hour RPO for BP-04 is not assured.** The source inventory application is backed up once a day, to a vault in the same account, and has never been restored (P01 R-007; POAM-003, POAM-004). The daily printed inventory export is the interim workaround.
- **The waste tracking vendor's commitments meet the BIA** (P09): RTO 8 hours and RPO 1 hour for SYS-03, against the 8-hour RTO and 4-hour RPO for BP-03.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-10 Physical security systems | Vault IDS with dual-path communicator; PACS server and door controllers; NVR and 22 cameras | BP-01 |
| SYS-09 Radiation monitoring | Area, portal, and stack monitors; monitoring workstation | BP-02, BP-03 |
| SYS-02 Identity provider | Single sign-on and MFA for all SaaS and the cloud console | BP-03 to BP-11 |
| SYS-07 Site network and internet | Firewall, switches, Wi-Fi, single internet provider | All (and BP-01 today) |
| SYS-03 Waste tracking and customer portal | System of record for containers, manifests, certificates | BP-03, BP-04, BP-06, BP-07, BP-08 |
| SYS-06 Source inventory application | Source and radionuclide inventory; sum-of-fractions; weekly verification | BP-04 |
| SYS-06 Records archive and backup vault | License, RCRA, training, and Part 37 records; backups | BP-06, BP-09 |
| SYS-08 Plant OT network | PLCs, HMIs, historian | BP-02 (historian), BP-05 |
| SYS-11 EPA e-Manifest | Hazardous and mixed waste manifests | BP-06 |
| SYS-04 Accounting; SYS-05 HR and payroll | Billing; payroll; HR records | BP-10, BP-11 |
| People and facilities | RSO and 14 approved individuals; health physics technicians; operators; the vault; the Plant dock | All |
| Third parties | Alarm monitoring company, security system vendor, controls integrator, waste tracking vendor, cloud provider, MSP, exclusive-use carrier, county sheriff | As listed in `bia.csv` |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-10 IDS path check; PACS server and NVR | 2 h | Approved individuals keep direct control of the vault; IDS cellular path; the security VLAN (due 2026-12-15) separates these from business IT recovery |
| 2 | SYS-02 Identity provider and break-glass accounts | 1 h | Two break-glass accounts stored offline (to be created with POAM-003) |
| 3 | SYS-09 Radiation monitoring workstation | 4 h | Portable instruments and manual stack sampling |
| 4 | SYS-07 Site internet and business network | 4 h | Cellular hotspot kit for the dock and dispatcher |
| 5 | SYS-03 Waste tracking access and clean tablets | 8 h | Vendor-hosted; paper receiving log |
| 6 | SYS-06 Source inventory application | 12 h | Daily printed export; physical count |
| 7 | SYS-06 Records archive; SYS-11 e-Manifest access | 24 h | Paper binders; paper manifests where allowed |
| 8 | SYS-12 Fleet telematics | 24 h | Phone check-ins |
| 9 | SYS-08 Plant OT network (PLCs, HMIs, historian) | 48 h | Local hand control; restore PLC programs from backups (stale today; P03 G-077) |
| 10 | SYS-04 Accounting and billing | 72 h | Queue invoices |
| 11 | SYS-05 HR and payroll | 72 h | Repeat prior payroll |
