# System Security Plan: Facility Operations Technology Platform (FOTP)

**Organization:** Cris Santos Company, LLC (facilities support contractor operating government buildings) | **Tier:** Small | **Vertical:** Government Services and Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Facility Operations Technology Platform (**FOTP**), identifier CSC-SYS-001.

## 2. System Overview
The FOTP is how the company monitors and operates the building systems of its state and county customers from the Remote Operations Center (ROC) and in the field. It supports:
- HVAC and building automation (BAS) supervision, trending, and alarm response for about 1,150 customer-owned BACnet controllers
- access control administration (badges, door schedules, alarms) and video management for 118 door controllers, about 520 readers, about 610 cameras, and 9 NVRs
- remote and on-site engineering access for 4 BAS controls technicians, 2 security systems technicians, and the access control and video integrator

**Major components:**
- **SYS-01:** BAS supervisory platform (supervisory server and trend historian on virtual machines)
- **SYS-02:** access control and video platform tenants for the state and county (vendor SaaS, administered by the company), including the face verification pilot module (SYS-12)
- **SYS-03:** remote access gateway (jump host with session recording)
- **SYS-04:** public cloud tenant (IaaS/PaaS) hosting SYS-01, SYS-03, file storage for drawings and controller program backups, and the backup vault
- **SYS-05:** company-managed edge firewalls, VPN gateways, and 5 engineering workstations at the state and county sites
- **SYS-09 (part):** 6 ROC workstations and the technicians' laptops

The cloud tenant is described by service category and is vendor-agnostic (see P04).

**Not part of the FOTP:** the BAS at the federal building. It runs on GSA servers on the GSA Building Systems Network under a GSA FISMA Moderate ATO. Company staff reach it only through GSA's virtual desktop with PIV cards (SYS-10). GSA owns its security plan; the company's duties there are the personnel, PIV, and conduct rules in section 3 and in POL-02.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the FOTP |
|---|---|---|---|
| Contract (CT-S) | State cybersecurity exhibit: SP 800-53 Rev. 5 Moderate controls, 24-hour incident notice, annual independent assessment | Required by Fla. Stat. 282.318(4)(h) for state agency IT service contracts | Binding |
| Contract (CT-C) | County security addendum: county cybersecurity standards (NIST CSF-based under Fla. Stat. 282.3185(4)), 24-hour incident notice, background checks | County contract | Binding |
| C-GOVERNMENT-R01 | FISMA, through GSA policies for contractor staff on GSA systems | 44 U.S.C. 3554; GSA BTTRG v3.0; GSA CIO 2100.1 | Applies to company staff conduct on SYS-10, not to the FOTP itself |
| FAR (CT-F) | Basic safeguarding of covered contractor information systems | FAR 52.204-21 | Applies to FOTP components that hold federal contract information (file storage, laptops) |
| FAR (CT-F) | Section 889, Kaspersky, FASCSA prohibitions; PIV of contractor personnel | FAR 52.204-25, 52.204-23, 52.204-30, 52.204-9; GSAR 552.204-9 | Equipment and personnel |
| CUI (CT-F) | Handling of GSA building drawings marked CUI | 32 CFR Part 2002; GSA Order PBS 3490.3 CHGE 1 | File storage (SYS-04) |
| State | Breach notice and reasonable security for personal information, including biometric data | Fla. Stat. 501.171 | Cardholder records and face templates in SYS-02 and SYS-12 |
| State | Contractor public records duties; exemptions for security system plans | Fla. Stat. 119.0701; 119.071(3) | State and county records held by the company |
| Internal | Security policies POL-01 to POL-05 | P06 | All components |

Not applicable (see P03 section 1.2): IRS Pub. 1075, CJIS Security Policy, VVSG 2.0, FERPA, SLCGP, and CIRCIA (proposed only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer on 2026-08-31.
### 4.2 System Authorization Decision
The FOTP is a contractor system, not a federal system, so there is no federal ATO. The equivalent internal decision:
- The COO accepted operation of the FOTP on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner accepted the Very High and High risks in P01 only with dated treatment plans. R-001 (remote access intrusion) must be treated by 2026-10-15.
- This SSP and the POA&M will be sent to the state agency by 2026-10-31 for its review under the contract exhibit (CA-6).
### 4.3 System Operational Status
Operational. Major modifications planned: remote access redesign (P01 R-001), due 2026-10-15; backup redesign (R-006), due 2026-12-31; OT segmentation at the county service centers (R-004), due 2027-01-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Overall accountability; risk acceptance up to Moderate |
| Risk acceptor (authorizing official equivalent) | Majority owner | Acceptance of High and Very High risks |
| Information Security Officer | IT Manager | Day-to-day security, SSP, POA&M |
| System administrator | IT/OT Systems Administrator | Cloud tenant, identity provider, edge firewalls, endpoints |
| BAS platform owner | Controls Engineering Manager | Supervisory platform, controller programs, BAS technicians |
| Access control and video administrator | Security Systems Supervisor | SYS-02 tenants, cardholder data, integrator oversight |
| Contract and CUI lead | Contracts Manager | Customer terms, FAR clauses, CUI handling, supplier screening |
| Customer liaison | Site Managers | Customer notice, manual-mode procedures |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facility operations and maintenance (BAS control, setpoints, schedules, alarms) | Low | Moderate | Moderate | Wrong setpoints or schedules can damage equipment or make a building unusable; controllers keep running locally, so loss of the supervisory layer is not immediate (P05 MTD 24 h) |
| Physical security (access control, door schedules, video, security system layouts) | Moderate | Moderate | Moderate | Unauthorized door changes expose people and property; layouts are exempt public records (Fla. Stat. 119.071(3)(a)); controllers cache credentials 72 h |
| Personal identity and authentication (cardholder records, badge photos, face templates) | Moderate | Moderate | Low | About 5,000 people; breach notice under Fla. Stat. 501.171 |
| Federal CUI building information (GSA drawings) | Moderate | Low | Low | CUI (Physical Security category) |
| **FOTP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

The physical security information type was not rated High for integrity because every door also has a mechanical key override, the county and state keep their own security staff on site, and doors fail to their programmed locked state when controllers lose power. The risk register still treats door manipulation as the most serious scenario (R-001).

**Baseline:** the NIST SP 800-53B **Moderate** baseline, which the state contract exhibit requires. All **177 base controls** are documented in `control-implementation.csv`, with their Moderate enhancements assessed inside each base control. Tailoring:
- **OT tailoring** follows NIST SP 800-82 Rev. 3, for example passive OT discovery in place of active scanning during operating hours, and segmentation to compensate for unencrypted BACnet.
- **No controls were tailored out.** Developer controls (SA-10, SA-11, SA-15) apply through the company's vendors.
- **PM (program management) controls** are not part of the SP 800-53B baselines. The program is defined by POL-01 and this SSP.

## 7. Authorization Boundary Description
- **Inside:** the SYS-01 virtual machines, the SYS-03 jump host, the SYS-04 cloud tenant (file storage, program backups, backup vault, network and logging services), the company's administration and configuration of the SYS-02 tenants, the SYS-12 pilot configuration, the company-owned SYS-05 edge firewalls and engineering workstations, the ROC workstations, and technician laptops.
- **Outside (interconnected):** customer-owned field devices and site networks, the access control SaaS vendor's platform, the cloud provider's infrastructure, the identity provider, the CMMS, the integrator's systems, and GSA's systems (SYS-10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| State agency site network (via edge firewall) | Bidirectional | BACnet control and alarm traffic | Contract exhibit only; **no interconnection agreement (gap, CA-3)** |
| County site networks (5 sites) | Bidirectional | BACnet and door controller traffic | Addendum only; **no interconnection agreement (gap)** |
| Access control and video SaaS | Bidirectional | Cardholder data, events, video, face templates | Vendor terms; SOC 2 Type 2 (P09) |
| Identity provider | Inbound authentication | Identities, MFA | Vendor terms |
| CMMS | Outbound work orders from alarms | Site and asset data | Vendor terms; SOC 2 on file |
| Access control and video integrator | Remote access | Device configuration | Subcontract **without security terms (gap)**; always-on remote-support tool at a county site (gap) |
| Mechanical subcontractors | Outbound | Drawings (including GSA CUI), work orders | Subcontract **without CUI terms or FAR flow-down (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| BAS supervisory server and historian | Cloud virtual machines | Cloud tenant | Controls Engineering Manager |
| Jump host | Cloud virtual machine | Cloud tenant | IT/OT Systems Administrator |
| File storage (drawings, CUI, program backups) | Cloud object storage | Cloud tenant | Contracts Manager (CUI); Controls Engineering Manager (programs) |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Manager |
| Access control and video tenants (state, county) | SaaS | Access control vendor | Security Systems Supervisor |
| Edge firewalls and VPN gateways (6) | Network | State complex and county sites | IT/OT Systems Administrator |
| Engineering workstations (5; 2 on an unsupported OS) | Endpoint | State and county sites | Controls Engineering Manager |
| ROC workstations (6) and technician laptops | Endpoint | ROC and field | IT/OT Systems Administrator |
| Customer field devices (reference only) | OT | Customer sites (customer-owned) | Customers; maintained by the company |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 177 controls:
- Implemented: 48
- Partially implemented: 93
- Planned: 36
- Not applicable: 0

By inheritance: 130 system-specific, 25 hybrid, 22 common or inherited (from the cloud provider, the SaaS vendors, operating system vendors, and the office landlord).

### 10.2 Control assessment status
22 controls were assessed 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Company users authenticate through the identity provider with a password and a second factor (a phone authenticator app; hardware security keys for the 2 cloud administrators). This fits the Moderate categorization for remote and privileged access. **Gap:** the BAS supervisory server still uses shared local accounts, and the integrator's remote-support tool has no MFA (POA&M items for AC-17 and IA-2).

Cardholders (state and county employees) use badges, not passwords. Face verification in the county pilot is a second factor with the badge, never a replacement (P10). At the federal building, company staff use GSA-issued PIV cards under FIPS 201, managed by GSA.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), risk register (P01), gap analysis (P03), cloud control map (P04), BIA (P05), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10), GSA BTTRG v3.0 (May 1, 2024).

## 13. Acronym List and Glossary
- **BACnet:** building automation and control network protocol
- **BAS:** building automation system
- **BSN:** GSA Building Systems Network
- **BTTRG:** GSA Building Technologies Technical Reference Guide
- **CUI:** controlled unclassified information
- **FCI:** federal contract information
- **FOTP:** Facility Operations Technology Platform
- **NVR:** network video recorder
- **OT:** operational technology
- **PIV:** personal identity verification (card)
- **ROC:** Remote Operations Center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | IT Manager |
