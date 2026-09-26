# System Security Plan: Business Operations and Records Platform (BORP)

**Organization:** Cris Santos Company, LLC (radioactive and hazardous waste processor) | **Tier:** Small | **Vertical:** Nuclear Reactors, Materials, and Waste
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Business Operations and Records Platform (**BORP**), identifier CSC-SYS-001.

## 2. System Overview
The BORP is the company's core business SaaS stack and its records. It runs customer onboarding, waste profiles, container tracking, manifests, certificates of processing, billing, HR, and the records the company must keep under its Florida radioactive materials license, 10 CFR Part 37, and its RCRA permit. It serves 60 workforce members and about 450 customer accounts.

**Major components:**
- **SYS-01:** a SaaS productivity suite (email, files, chat). It holds the Part 37 security plan, implementing procedures, and approved-individuals list
- **SYS-02:** an identity provider for single sign-on and MFA
- **SYS-03:** the waste tracking and customer portal SaaS (company configuration and users)
- **SYS-04:** accounting and billing SaaS
- **SYS-05:** HR and payroll SaaS
- **SYS-06:** a public-cloud tenant hosting the source inventory application, the records archive, and the backup vault
- **SYS-07:** the site business network and endpoints

The cloud tenant is described by service category and is vendor-agnostic (see P04).

**Why this system matters for radioactive material security.** The BORP holds information that Part 37 requires the company to protect: the security plan, implementing procedures, and the list of approved individuals (37.43(d)), and background investigation records (37.31). It also holds records that must be protected against tampering and loss (37.101). A breach of this system can become a Part 37 violation, and in the worst case help someone plan a theft.

## 3. Laws, Regulations, and Policies Affecting the System
Driver IDs are defined in `../scenario-facts.md` section 1.

| ID | Requirement | Citation |
|---|---|---|
| C-NUCLEAR-S01 | Physical protection of category 2 quantities, including protection of information and records | 10 CFR Part 37 (37.31, 37.43(d), 37.49(c), 37.101), imposed by the Florida license condition |
| C-NUCLEAR-S02 | Florida radiation control rules | Chapter 64E-5, F.A.C. |
| C-NUCLEAR-S03 | DOT hazmat transportation security plan | 49 CFR 172.800-172.804 |
| C-NUCLEAR-S04 | RCRA manifest system, operating record, and records retention | 40 CFR 264.71-264.74, through Chapter 62-730, F.A.C. |
| C-NUCLEAR-S05 | NIST CSF 2.0 (voluntary benchmark; SP 800-82 Rev. 3 for connected OT) | NIST CSWP 29; SP 800-82 Rev. 3 |
| C-NUCLEAR-S06 | Florida Information Protection Act (breach notification) | Fla. Stat. 501.171 |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable:
- 10 CFR 73.54 and 73.77 (C-NUCLEAR-R01, R03), because the company is not a power reactor licensee (P03 section 1).
- Safeguards Information rules (10 CFR 73.21), because the company holds no SGI.
- CIRCIA (C-NUCLEAR-R05), which is proposed only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the General Manager on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The General Manager accepted operation of the BORP on 2026-08-31, with the conditions in the P07 POA&M.
- The President accepted the High risks in P01 with dated treatment plans.
- **Condition:** the restricted library for Part 37 information must be in place by 2026-09-30 (POAM-001).
### 4.3 System Operational Status
Operational. Major modifications planned:
- a security VLAN that moves the PACS server, NVR, and cameras off the business network (P01 R-003), due 2026-12-15
- the backup redesign (P01 R-007), due 2026-12-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | General Manager | Overall accountability; risk acceptance up to Moderate; individual with overall responsibility for the Part 37 security program |
| Risk acceptor (authorizing official equivalent) | President (majority owner) | Acceptance of High and Very High risks |
| Cybersecurity lead | IT Manager | Day-to-day security; SSP owner |
| Part 37 information owner | Radiation Safety Officer | Decides who may see the security plan, procedures, and approved list; reviewing official |
| Records owner (RCRA and shipments) | Compliance and Transportation Manager | Manifests, operating record, shipment coordination records |
| Operations support | Managed service provider | Help desk, patching, EDR monitoring |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Security management (Part 37 security plan, procedures, approved list) | Moderate | Moderate | Low | Disclosure could help an adversary plan theft of category 2 material, which Part 37 guards against with need-to-know rules. Moderate rather than High: disclosure alone does not defeat the vault barriers, IDS, two-person entry, and armed LLEA response. It is not Safeguards Information |
| Personnel identity and authentication (background investigations, HR) | Moderate | Moderate | Low | Criminal history and identity documents; 37.31 and Fla. Stat. 501.171 |
| Regulatory compliance records (source inventory, manifests, operating record) | Low | Moderate | Moderate | Wrong or lost records can cause mis-shipment, a possession-limit error, or a license or permit violation. Paper fallback limits the availability impact (P05 MTD 24 h) |
| Customer services (waste profiles, container tracking, certificates) | Moderate | Moderate | Moderate | Receiving and shipping stop without it (P05 MTD 24 h) |
| Financial management (billing, payables) | Moderate | Moderate | Low | Fraud and cash flow; billing can wait (P05 MTD 72 h) |
| **BORP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 60-person company. The plan documents the 74 controls that cover the Part 37 information and records duties and core network hygiene (see `control-implementation.csv`). Every other Moderate-baseline control is treated as follows:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems.

The **OT overlay in SP 800-82 Rev. 3 Appendix F** is not applied to the BORP. It is the reference for the OT benchmark in P03 (G-066 to G-085).

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:**
  - the SYS-01 tenant, including the Radiation Safety and HR libraries
  - the identity provider tenant
  - the company's configuration, users, and roles in SYS-03, SYS-04, and SYS-05
  - the cloud tenant (3 workloads)
  - the site business network (firewall, switches, Wi-Fi) and 68 endpoints (44 laptops and desktops, 18 plant-floor tablets, 6 truck tablets)
  - **the PACS server, NVR, and 22 IP cameras, for as long as they sit on the business network.** They are owned by the Part 37 program but share this network today (P03 G-046).
- **Outside (external services):** the SaaS vendors' platforms, the cloud provider's infrastructure, EPA e-Manifest (SYS-11), fleet telematics (SYS-12), and the MSP's tools.
- **Outside (interconnected company systems):**
  - the plant OT network (SYS-08), which is reached today through the dual-homed historian
  - radiation monitoring (SYS-09)
  - the vault IDS panel and its communicator (SYS-10)
  - the predictive maintenance gateway (SYS-13)

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| EPA e-Manifest (SYS-11) | Bidirectional (web, named users) | Hazardous and mixed waste manifests | EPA terms of use; **one shared account (gap, P01 R-028)** |
| Fleet telematics (SYS-12) | Inbound | Truck locations | Vendor contract |
| Exclusive-use carrier | Bidirectional (email and carrier portal) | Category 2 shipment coordination and tracking | Carrier contract with tracking and signature terms |
| Receiving licensees | Bidirectional (email) | License verification, no-later-than arrival times | 37.71 and 37.75 records; **no retention rule (gap)** |
| Customers (portal) | Bidirectional | Waste profiles, pickup requests, certificates | Customer terms of service |
| Historian (SYS-08) | Inbound to business network | Process data for reports | **Undocumented dual-homed connection (gap)** |
| Alarm monitoring company | Outbound from IDS panel | Alarm and path supervision signals | Monitoring contract (outside boundary) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Productivity suite tenant | SaaS | Productivity vendor | IT Manager |
| Identity provider tenant | SaaS | Identity vendor | IT Manager |
| Waste tracking and customer portal | SaaS | Waste tracking vendor | Customer Service Manager |
| Accounting and billing | SaaS | Accounting vendor | Controller |
| HR and payroll | SaaS | HR vendor | HR Manager |
| Source inventory application | Cloud managed database and web app | Cloud tenant | Radiation Safety Officer |
| Records archive | Cloud object storage | Cloud tenant | Compliance and Transportation Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Manager |
| Site firewall, switches, Wi-Fi | Network | The Plant | IT Manager |
| Laptops and desktops (44), plant tablets (18), truck tablets (6) | Endpoint | The Plant and field | IT Manager |
| PACS server, NVR, 22 IP cameras | Physical security (on the business network, **gap**) | The Plant | Radiation Safety Officer |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 74 controls:
- Implemented: 31
- Partially implemented: 34
- Planned: 9
- Not applicable: 0

### 10.2 Control assessment status
Assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
All workforce users authenticate through the identity provider with a password and a second factor. Most use a phone authenticator app. The 2 cloud administrators and anyone granted access to the Part 37 restricted library use hardware security keys (from 2026-09-30). This meets the 37.43(d)(7) floor ("password protected") and is appropriate for a Moderate system holding security-related information.

Customers use the waste tracking vendor's portal with its own MFA. That is governed by the vendor and outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 self-benchmark and vendor review (P09), AI assessment (P10), Part 37 security plan Rev. 2 (restricted; not reproduced here).

## 13. Acronym List and Glossary
- **BORP:** Business Operations and Records Platform
- **EDR:** endpoint detection and response
- **IDS:** intrusion detection system
- **LLEA:** local law enforcement agency
- **MSP:** managed service provider
- **NVR:** network video recorder
- **OT:** operational technology
- **PACS:** physical access control system
- **POA&M:** plan of action and milestones
- **RSO:** Radiation Safety Officer
- **Security-related information:** in this plan, the Part 37 security plan, implementing procedures, and list of approved individuals (37.43(d))

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
