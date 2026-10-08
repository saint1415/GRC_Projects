# System Security Plan (short form): Property Systems Profile

**Organization:** Cris Santos Company (owner-operator of one mixed-use commercial building) | **Tier:** Sole Proprietorship | **Vertical:** Commercial Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Property Systems Profile (**PSP**), identifier CSC-SYS-001.

## 2. System Overview
The PSP is everything the owner uses to run one 9,500 sq ft, 8-tenant building: door access, cameras, climate control, rent collection, leasing records, and tenant communication. One person, the owner, uses and administers all of it. Components are SYS-01 to SYS-09 in `../00_company-facts.md` section 3:
- **Building controls (the registry's "building automation and access control system" at this size):** cloud-managed access control with 4 door controllers (SYS-01), 6 cloud cameras (SYS-02), and 8 smart thermostats (SYS-03). Each has on-premises devices managed from a vendor cloud portal and phone app.
- **Network:** one ISP router with Wi-Fi in the utility room (SYS-04).
- **Business SaaS:** property management and accounting with the tenant portal (SYS-05), email and files (SYS-06), and a tenant screening service (SYS-09).
- **Devices:** the owner's laptop (SYS-07) and phone (SYS-08).

There is no server, no on-premises building automation controller network, and no IaaS. Most platform safeguards are **inherited from the vendors**; the owner is responsible for accounts, data handling, devices, the router, and contractor access (P04). The fire alarm panel and the elevator are outside the boundary, on their own cellular communicators.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| C-COMMERCIAL-FACILITIES-R05 | CISA Cross-Sector Cybersecurity Performance Goals 2.0 (voluntary) | CISA CPG 2.0 (December 2025) | Adopted by the owner on 2026-07-17 as the benchmark for "reasonable" security; tailored for building devices with NIST SP 800-82 Rev. 3 |
| C-COMMERCIAL-FACILITIES-R02 | FTC Act Section 5 | 15 U.S.C. 45(a) | No size threshold; unreasonable data security and misleading statements about data practices |
| State | Reasonable security, breach notice, and disposal of customer records | Fla. Stat. 501.171(2), (3) to (6), (8) | The owner is a "covered entity" (the definition names a sole proprietorship) that holds guarantor Social Security and driver license numbers |
| Federal | FTC Disposal Rule | 16 CFR 682.3(a) | Consumer credit reports on individual guarantors from SYS-09 |
| State | Interception of oral communications | Fla. Stat. 934.03 | Entrance camera audio (turned off 2026-07-21; P10) |
| Internal | Information Security Policy | POL-01 (P06) | |

Not applicable: PCI DSS (C-COMMERCIAL-FACILITIES-R01; no card acceptance), CCPA/CPRA (R03), SEC disclosure (R04), and CIRCIA (R06, proposed rule only). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-004) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: MFA on all building portals (2026-09-15); a business router with a separate network for building devices and an isolated guest network (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, privacy lead, administrator, risk acceptor | Owner | Every role (designated in writing in POL-01 4.2) |
| Technical support | On-call IT consultant | Router and laptop help on request; helped with the self-assessment; no standing access |
| Building device service | Access control and camera installer; HVAC service contractor | Hardware service. Today both hold administrator access they should not (P01 R-003, R-007) |
| Service providers | Access control, camera, thermostat, property management, email, and screening vendors | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Building access and physical security (door schedules, credentials, door history, video) | Moderate | Moderate | Moderate | Disclosure exposes tenant employees' movements; altered schedules leave the building open; loss beyond a day needs the owner on site (P05 MTD 24 h) |
| Building environmental control (thermostat schedules) | Low | Moderate | Moderate | Not sensitive; wrong settings or loss beyond a day stops tenants opening in summer (P05 MTD 24 h) |
| Guarantor and applicant personal information (SSNs, license copies, credit reports) | Moderate | Low | Low | Personal information under Fla. Stat. 501.171; rarely needed quickly (P05 MTD 120 h) |
| Tenant accounts and rent (lease terms, ACH bank details) | Moderate | Moderate | Low | Financial data; a week of delay is survivable (P05 MTD 120 h) |
| **PSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

The information types are described in plain terms; SP 800-60 has no building-operations type that fits a private landlord. **Baseline:** SP 800-53B Moderate, tailored to 26 controls a one-person landlord can run (`control-implementation.csv`). Other Moderate controls are either inherited from the SaaS vendors (evidence: the access control vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's administrator accounts and settings in SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, and SYS-09; the 4 door controllers and readers, 6 cameras, and 8 thermostats as devices on the building network; the router (SYS-04); the laptop and phone; the paper lease files.
- **Outside (external services):** the vendors' cloud platforms, the installer, HVAC contractor, IT consultant, janitorial contractor, CPA, the property management vendor's payment partner, the internet provider, the fire alarm and elevator systems, and every tenant's own network.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Access control and camera installer | Administrator access to SYS-01 and SYS-02 | Installation invoice only; **no security terms (gap)** |
| HVAC service contractor | Owner's thermostat login (shared); one building credential | Service agreement; **no security terms (gap)** |
| Outside CPA | Accountant role in SYS-05; shared link to the lease application folder | Engagement letter; the shared link is a gap |
| Property management vendor and its payment partner | Tenant ACH details and rent | Vendor terms of service |
| Tenant screening service | Applicant and guarantor identity data; consumer and business credit reports | Service terms with an FCRA end-user certification |
| Tenants | Employee names and contacts for credentials | Leases (no data clause) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Access control tenant and 4 door controllers (SYS-01) | SaaS plus OT devices | Owner |
| Cloud video tenant and 6 cameras (SYS-02) | SaaS plus OT devices | Owner |
| Thermostat platform account and 8 thermostats (SYS-03) | SaaS plus OT devices | Owner |
| ISP router and Wi-Fi (SYS-04) | Network device (ISP-supplied) | Owner (ISP owns the hardware) |
| Property management SaaS (SYS-05) | SaaS | Owner |
| Email and file suite (SYS-06) | SaaS | Owner |
| Laptop (SYS-07) | Endpoint | Owner |
| Phone (SYS-08) | Personal endpoint used for business | Owner |
| Tenant screening service (SYS-09) | SaaS | Owner |

Serial numbers, firmware versions, and locations are being added (CM-8, due 2026-10-31).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 6
- Partially implemented: 16
- Planned: 4

Inheritance: 2 fully inherited from the vendors (AU-2, AU-9), 10 hybrid (a vendor operates the mechanism, the owner configures or uses it correctly), and 14 the owner's alone (AC-5, AC-6, AT-2, AU-6, CA-2(1), CM-3, CM-8, CP-2, IA-5, IR-8, MP-6, RA-3, SA-9, SC-7).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; owner holds all roles; contractor terms (SA-9, gap) |
| Identify | Risk assessment (RA-3); BIA (P05); inventory (CM-8, partial) |
| Protect | MFA (IA-2(1), gap on building portals); unique logins (IA-2, IA-5); separate building network (SC-7, gap); laptop encryption (SC-28) |
| Detect | Vendor door and admin logs (AU-2, inherited); monthly review (AU-6, planned); antivirus (SI-3) |
| Respond | Runbook for ransomware reaching the building portals (IR-8) |
| Recover | Offline-capable door controllers and thermostats; manual procedures and backups (CP-2, CP-9, gaps) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT consultant. See P07.

## 11. Digital Identity Acceptance Statement
Administrator access to the building portals can unlock doors and change who can enter, so it needs a password and a phishing-resistant or app-based second factor. Today only the property management SaaS meets that; email uses text-message codes, and the access control, camera, and thermostat portals use a password only until MFA is turned on (2026-09-15). Tenant employees authenticate to doors with a fob or phone credential, which is a physical access credential managed in SYS-01, not a system account.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CPG:** CISA Cross-Sector Cybersecurity Performance Goals
- **MFA:** multi-factor authentication
- **OT:** operational technology (here, door controllers, cameras, and thermostats)
- **PSP:** Property Systems Profile
- **SaaS:** software as a service

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner |
