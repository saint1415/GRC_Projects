# System Security Plan: Integrated Facility Operations Platform (IFOP)

**Organization:** Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) | **Tier:** Mid-Market | **Vertical:** Government Services and Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Integrated Facility Operations Platform (**IFOP**), identifier CSC-IFOP-01. The IFOP is the company's major system. Its components are listed in `../00_company-facts.md` section 3.

## 2. System Overview
The IFOP is how the company monitors and operates the building systems of its state, county, and city customers, around the clock, from the Remote Operations Center (ROC) and in the field. It supports the processes the BIA (P05) rated highest: remote alarm monitoring (BP-01), access control administration (BP-02), critical environment support at the County A Emergency Operations Center and the state data center building (BP-03), BAS supervision (BP-05), and controller program engineering (BP-09). It serves the 46 state, county, and city sites, about 41,000 cardholders, and about 9,800 BACnet controllers, and it carries remote access to the school district's BAS.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | BAS supervisory platform: 8 supervisory clusters and trend historians | Virtual machines in the OT workloads account of the landing zone (IaaS) |
| SYS-02 | Access control and video tenants for CT-S, CT-C1, CT-C2, and CT-M, administered by the company | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-03 | Privileged remote access broker with vault, per-session approval, and recording | Virtual machines in the shared services account (IaaS) |
| SYS-04 | Cloud landing zone: 5 accounts (management and identity, security and logging, shared network services, OT workloads, backup) | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-05 | 46 site edge firewalls and VPN gateways, 38 engineering workstations, passive OT sensors at 12 sites | On-premises at customer sites |
| SYS-13 | Face verification module (County A, 6 readers, 1,150 enrolled) | Feature of the SYS-02 vendor platform |
| SYS-14 | Primary ROC and backup ROC | On-premises (HQ and north regional office) |
| SYS-15 | Video analytics module (4 state sites) | Feature of the SYS-02 vendor platform |
| SYS-09 (part) | 40 ROC workstations and the laptops and tablets of the Building Technology and ROC staff | Company-managed |

The identity provider (SYS-06), CMMS (SYS-08), and SIEM (SYS-12) are external services the IFOP depends on (section 8).

**Not part of the IFOP:** the BAS at the 5 federal buildings. It runs on GSA servers on the GSA Building Systems Network under a GSA FISMA Moderate ATO. Company staff reach it only through GSA's virtual desktop with PIV cards (SYS-10). GSA owns its security plan; the company's duties there are the personnel, PIV, and conduct rules in section 3 and in POL-02. The school district's BAS server is also outside the boundary; only the broker connection to it is inside.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the IFOP |
|---|---|---|---|
| Contract (CT-S) | State cybersecurity exhibit: SP 800-53 Rev. 5 Moderate controls, 24-hour incident notice, annual independent assessment, SOC 2 Type 2 by 2028-06-30 | Required by Fla. Stat. 282.318(4)(h) for state agency IT service contracts | Binding for components that store or process state agency data |
| Contract (CT-C1) | County A security addendum: county cybersecurity standards (NIST CSF-based under Fla. Stat. 282.3185(4)), notice within 6 hours for suspected ransomware and 24 hours otherwise, background checks, SOC 2 or equivalent; Supervisor of Elections annex | County contract | Binding for County A tenants, cluster, and sites |
| Contract (CT-C2, CT-M, CT-K) | County B and City addenda (24-hour notice; local standards under Fla. Stat. 282.3185(4)); school district terms (48-hour notice) | Customer contracts | Binding for each customer's components |
| C-GOVERNMENT-R01 | FISMA, through GSA policies for contractor staff on GSA systems | 44 U.S.C. 3554(a)(1)(A)(ii); GSA BTTRG v3.0; GSA CIO 2100.1 | Applies to company staff conduct on SYS-10, not to the IFOP itself |
| FAR (CT-F) | Basic safeguarding of covered contractor information systems | FAR 52.204-21 | Applies to IFOP components that hold federal contract information (file storage, laptops) and to the CMMS |
| FAR (CT-F) | Section 889, Kaspersky, and FASCSA prohibitions; PIV of contractor personnel | FAR 52.204-25, 52.204-23, 52.204-30, 52.204-9; GSAR 552.204-9 | Equipment, software, and personnel |
| CUI (CT-F) | Handling of GSA building drawings marked CUI | 32 CFR Part 2002; GSA Order PBS 3490.3 CHGE 1 | CUI library in SYS-04 |
| State | Breach notice and reasonable security for personal information, including biometric data | Fla. Stat. 501.171 | Cardholder records and face templates in SYS-02 and SYS-13 |
| State | Contractor public records duties; exemption for security system plans | Fla. Stat. 119.0701; 119.071(3) | Customer records held by the company |
| C-GOVERNMENT-R08 | GovRAMP | GovRAMP program (not law) | Not required by any contract today; relevant to the access control SaaS vendor and to the 2028 state rebid |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | All components |

Not applicable (see P03 section 1.2): IRS Pub. 1075, CJIS Security Policy, VVSG 2.0, FERPA, SLCGP, and CIRCIA (proposed only).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The IFOP is a contractor system, not a federal system, so there is no federal ATO. The equivalent internal decision:
- **Decision:** operation of the IFOP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** R-001 (subcontractor remote access) treated by 2026-12-31 with weekly interim checks; the High-risk POA&M items in P07 meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.
- **Customer review:** this SSP and the POA&M go to the state agency by 2026-10-31 under the contract exhibit (CA-6), and to County A with the SOC 2 readiness summary (P09).
### 4.3 System Operational Status
Operational. Major modifications planned:
- All subcontractor remote access moved to the broker (due 2026-12-31)
- OT segmentation at the 17 flat sites (due 2027-06-30)
- OT logs and sensors onboarded to the SIEM (due 2027-01-31 for logs; 2027-06-30 for sensors at all sites)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the IFOP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Information Security Officer | IT Director | Day-to-day control owner; SSP and contingency planning for IT |
| Security operations and GRC | Security Manager, 2 security analysts, GRC analyst | MSSP oversight, vulnerability management, SSP and POA&M maintenance |
| OT security | OT Security Engineer | OT monitoring, hardening, and remote access policy |
| Platform owners | Director of Building Technology; Controls Engineering Manager (SYS-01); Security Systems Manager (SYS-02, SYS-13, SYS-15) | Platform security, roles, and change control |
| Operations | VP Operations; ROC Manager (SYS-14) | Building safety in incidents; ROC continuity |
| Contract, CUI, and supply chain | Contracts Director | Customer terms, FAR clauses, CUI handling, supplier and subcontractor screening |
| Legal | General Counsel | Breach determinations and notices |
| Customer liaison | Program managers | Customer notices; manual-mode procedures |
| Independent assessment | Co-sourced internal audit firm (with an OT specialist) | Annual assessment (P07) |
| Monitoring | MSSP | 24x7 MDR and SIEM |

**Where roles overlap.** The IT Director is both Information Security Officer and the owner of IT operations, so the vCISO reviews the SSP and the co-sourced internal audit firm assesses the controls. The Security Manager coordinated P07 access but did not select samples or rate findings.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facility operations and maintenance (BAS control, setpoints, schedules, alarms) | Low | Moderate | Moderate | Wrong setpoints can damage equipment or make a building unusable; controllers keep running locally, so loss of the supervisory layer is not immediate (P05 MTD 24 h) |
| Critical facility environmental control (EOC and data center building cooling and power monitoring) | Low | Moderate | Moderate | Considered for High (see below); local operator workstations and on-site engineers carry the 4-hour MTD |
| Physical security (access control, door schedules, video, security system layouts) | Moderate | Moderate | Moderate | Unauthorized door changes expose people and property; layouts are exempt public records (Fla. Stat. 119.071(3)(a)); controllers cache credentials 72 h |
| Personal identity and authentication (cardholder records, badge photos, face templates) | Moderate | Moderate | Low | About 41,000 people plus 1,150 face templates; breach notice under Fla. Stat. 501.171 and other states' laws |
| Federal CUI building information (GSA drawings in the CUI library) | Moderate | Low | Low | CUI Basic is categorized at no less than Moderate confidentiality (32 CFR 2002.14(g)) |
| System and network monitoring (OT sensor data, session recordings, logs) | Moderate | Moderate | Low | Needed for investigations and customer notices |
| **IFOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability and integrity were considered for High.** Loss of BAS control at the County A EOC during a hurricane activation, or at the state data center building, could have severe effects. The team kept Moderate because both buildings have local operator workstations that run without the IFOP, on-site engineers can run equipment in hand mode, and controllers keep their last programs. To compensate, the baseline adds tailoring for those two sites (section 10.1) and the BIA gives them the shortest MTD. Door integrity was kept at Moderate because every door has a mechanical key override, customers keep their own security staff, and doors fail to their programmed locked state. The risk register still treats door manipulation as the most serious scenario (R-001).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the 8 BAS supervisory clusters (SYS-01);
- the company's administration and configuration of the 4 access control and video tenants, the face verification module, and the video analytics module (SYS-02, SYS-13, SYS-15);
- the remote access broker (SYS-03);
- all 5 landing zone accounts and their workloads (SYS-04);
- the 46 site edge firewalls, 38 engineering workstations, and 12 sets of passive OT sensors (SYS-05);
- the primary and backup ROC (SYS-14), the 40 ROC workstations, and Building Technology and ROC laptops and tablets.

**Outside the boundary (interconnected):**
- customer-owned field devices and site networks;
- the access control SaaS vendor's platform;
- the cloud provider's infrastructure;
- the identity provider, CMMS, and SIEM services;
- the subcontractors' own systems and remote tools;
- the school district's BAS server and network;
- GSA's systems (SYS-10).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| State agency site networks (6 sites) | Bidirectional | BACnet control and alarm traffic | Interconnection security agreement (2025) |
| County A site networks (19 sites) | Bidirectional | BACnet and door controller traffic | Addendum only; **no interconnection agreement (gap, CA-3)** |
| County B and City site networks (21 sites) | Bidirectional | BACnet and door controller traffic | Addenda only; **no interconnection agreement (gap)**; flat networks at 17 sites |
| School district BAS (through the district VPN) | Bidirectional | BAS trend data and remote sessions | Contract terms; **no interconnection agreement (gap)** |
| Access control and video SaaS | Bidirectional | Cardholder data, events, video, face templates, analytics alerts | Vendor terms; SOC 2 Type 2 (P09) |
| Identity provider | Inbound authentication | Identities, MFA | Vendor terms; SOC 2 Type 2 |
| CMMS | Bidirectional | Work orders, change tickets, asset lists | Vendor terms; SOC 2 Type 2 |
| MSSP and SIEM | Outbound logs; inbound response actions | Security logs | MSSP contract; SOC 2 Type 2 |
| OT subcontractors SUB-1 to SUB-3 | Remote access through the broker | Device configuration | Security addendum signed |
| OT subcontractors SUB-4 to SUB-7 | Own remote-support tools at 11 sites | Device configuration | **No security terms (gap, SA-9)**; tools outside the broker (gap, AC-17) |
| Trades subcontractors at federal sites | Outbound | Drawings (including GSA CUI), work orders | FAR 52.204-21 flowed down in 5 of 9 subcontracts (gap) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| BAS supervisory clusters and historians (8) | Cloud virtual machines | OT workloads account | Controls Engineering Manager |
| Remote access broker and credential vault | Cloud virtual machines | Shared services account | OT Security Engineer |
| Hub firewall, site-to-cloud VPN, DNS | Network services | Shared services account | IT Director |
| Log pipeline and write-once log bucket | Logging services | Security and logging account | Security Manager |
| Cloud identity federation and organization guardrails | Identity and policy services | Management and identity account | IT Director |
| File storage, CUI library, controller program repository | Object storage | OT workloads account | Contracts Director (CUI); Controls Engineering Manager (programs) |
| Backup vault (30-day write-once, second region) | Backup service | Backup account | IT Director |
| Access control and video tenants (4), face verification, video analytics | SaaS | Access control vendor | Security Systems Manager |
| Edge firewalls and VPN gateways (46) | Network | Customer sites | OT Security Engineer |
| Engineering workstations (38; 9 on an unsupported OS) | Endpoint | Customer sites | Controls Engineering Manager |
| Passive OT sensors (12 sites) | Network sensor | CT-S and County A sites | OT Security Engineer |
| ROC workstations (40) and video walls | Endpoint | Primary and backup ROC | ROC Manager |
| Building Technology and ROC laptops and tablets | Endpoint | Field | IT Director |
| Customer field devices (reference only) | OT | Customer sites (customer-owned) | Customers; maintained by the company |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The IFOP uses the NIST SP 800-53B **Moderate** baseline. All **287 controls and enhancements** (177 base controls and 110 enhancements) are documented in `control-implementation.csv`, each with a status, an owner, its inheritance, and a statement. Tailoring decisions:
- **OT tailoring** follows NIST SP 800-82 Rev. 3: passive OT discovery and vulnerability identification instead of active scanning during operating hours (RA-5, CM-8); segmentation to compensate for unencrypted BACnet (SC-8, SC-7); broker-only management access to compensate for field devices without lockout or MFA (AC-7, IA-2).
- **Critical facility tailoring:** the County A EOC and the state data center building keep local operator workstations that work without the IFOP, are tested in each contingency exercise (CP-4), and get the first manual-mode procedures (CP-2).
- **Not applicable (3):** IA-2(12) and IA-8(1) (the IFOP has no federal users and does not accept PIV credentials) and SA-4(10) (no PIV-capable products are acquired for it).
- **Developer controls** (SA-10, SA-11, SA-15) apply through the company's vendors, because the company develops no software.
- **Program management (PM) controls** are not part of the SP 800-53B baselines. The program is defined by POL-01, the standards index, and this SSP.
- **CSF 2.0 mapping:** 137 rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0; 101 enhancement rows take the official mapping of their base control; 49 rows (43 base controls with no official reference, and their enhancements) use an author mapping, labeled as such in P03.

**Status of the 287 documented controls and enhancements:**
| Status | Base controls | Enhancements | Total |
|---|---|---|---|
| Implemented | 74 | 45 | 119 |
| Partially implemented | 102 | 58 | 160 |
| Planned | 1 | 4 | 5 |
| Not applicable | 0 | 3 | 3 |
| **Total** | **177** | **110** | **287** |

**Inheritance of the 287:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 203 | Company |
| Hybrid | 62 | Identity provider vendor, cloud provider, access control SaaS vendor, MSSP, office landlords |
| Common/Inherited | 22 | Cloud provider (for example SC-12, SC-20), office landlords (PE-10, PE-12 to PE-15), identity provider vendor (IA-7), productivity suite vendor (SI-8) |

Inherited and hybrid controls rely on the providers' SOC 2 Type 2 reports and their complementary user entity controls, reviewed each year in P09 `vendor-soc2-review.csv`. The Partially implemented statements trace to the 14 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm, with an OT specialist subcontractor, assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. This fits the Moderate categorization for remote and privileged access.
- **Administrators.** Cloud and broker administrators use phishing-resistant hardware security keys. Access to site OT goes through the broker with per-session approval and credential injection, so technicians never see device passwords where the vault covers the site.
- **Gaps.** 3 BAS clusters still allow shared local engineer accounts, one subcontractor account in the County B tenant is shared, and 4 subcontractors use their own tools without company MFA (POA&M items for IA-2, AC-17, and IA-8).
- **Cardholders.** State, county, and city employees use badges, not passwords. Face verification at County A is a second factor with the badge, never a replacement (P10).
- **Federal sites.** Company staff use GSA-issued PIV cards under FIPS 201, managed by GSA, only on GSA systems.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); GSA BTTRG v3.0 (May 1, 2024); NIST SP 800-82 Rev. 3.

## 13. Acronym List and Glossary
- **BACnet:** building automation and control network protocol
- **BAS:** building automation system
- **BSN:** GSA Building Systems Network
- **BTTRG:** GSA Building Technologies Technical Reference Guide
- **CUI:** controlled unclassified information
- **EOC:** Emergency Operations Center
- **FCI:** federal contract information
- **IFOP:** Integrated Facility Operations Platform
- **MDR:** managed detection and response
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **NVR:** network video recorder
- **OT:** operational technology
- **PIV:** personal identity verification (card)
- **POA&M:** plan of action and milestones
- **ROC:** Remote Operations Center

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk assessment and gap analysis | Security Manager and GRC analyst |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (Information Security Officer) |
