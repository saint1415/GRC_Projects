# System Security Plan: Building Systems Operations Platform (BSOP)

**Organization:** Cris Santos Company, LLC (facilities support contractor operating government buildings, NAICS 561210) | **Tier:** Micro | **Vertical:** Government Services and Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Building Systems Operations Platform (**BSOP**), identifier CSC-SYS-001.

## 2. System Overview
The BSOP is how a 7-person company runs other people's buildings. It supports alarm monitoring and emergency response for 7 county and city buildings, the county's managed access control and video service, BAS operation and maintenance, dispatch, and the engineering records behind them. It holds cardholder records for about 1,050 county employees, contractors, and volunteers.

The company owns almost no infrastructure. Two vendor SaaS platforms do the heavy lifting, 7 small gateways connect them to the customers' building networks, and a managed service provider (MSP) runs the office IT. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** managed access control and video service: the company's tenant in a vendor's cloud platform, serving 4 county buildings (16 county-owned door controllers, 52 readers, 38 entrance cameras), including the face verification pilot (SYS-12)
- **SYS-02:** BAS monitoring and alarm service (vendor SaaS) for 4 county and 3 city buildings; remote write for county buildings, read-only for city buildings
- **SYS-03:** 7 company-owned site gateways with outbound encrypted tunnels to SYS-02 and a technician VPN
- **SYS-04:** productivity suite (email, files, chat)
- **SYS-05:** CMMS (work orders and assets)
- **SYS-06:** 6 laptops, 3 rugged tablets, 7 company phones
- **SYS-07:** office network (firewall, staff and guest Wi-Fi)
- **SYS-08:** SaaS-to-SaaS backup of the productivity suite, operated by the MSP

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | How it reaches the company |
|---|---|---|
| CT-C | County security exhibit: NIST SP 800-53 Rev. 5 Moderate controls for systems the vendor hosts for the county and for privileged vendor accounts; MFA; 24-hour incident notice; annual questionnaire | Contract (the county adopted its standards under Fla. Stat. 282.3185(4)(a)) |
| CT-M | City cybersecurity standards (NIST CSF-based); named accounts and city MFA; 24-hour incident notice | Contract |
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558): GSA's BAS at the federal building is a GSA system under GSA's authorization; the company follows GSA IT policies through the BTTRG v3.0 | Indirectly, through the CT-F subcontract. No company system operates on GSA's behalf |
| FAR | 52.204-21 (FCI safeguarding), 52.204-23, 52.204-25, 52.204-30, 52.204-9 | CT-F subcontract flow-downs |
| CUI | 32 CFR Part 2002 and GSA Order PBS 3490.3 CHGE 1 (CUI drawings) | CT-F statement of work |
| State | Fla. Stat. 501.171 (reasonable security, third-party agent notice, disposal); 119.0701 (contractor public records); 119.071(3) (exempt security system plans and building plans) | Direct |
| Internal | POL-02, POL-03, POL-04 (P06) | Approved 2026-08-31 |

Not applicable: IRS Pub. 1075 (C-GOVERNMENT-R02, no FTI), CJIS Security Policy (R03, no criminal justice buildings in scope), VVSG 2.0 (R04), FERPA (R05), SLCGP (R07). CIRCIA (R06) is a proposed rule only. GovRAMP (R08) is not required of the company by any customer.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the owner accepted continued operation of the BSOP, on condition that the POA&M items in P07 are completed by their dates and the 4 High risks in P01 (R-001, R-002, R-005, R-010) are treated by 2026-12-31. A summary of this plan and the POA&M goes to the county with the questionnaire answer by 2026-09-30.

### 4.3 System Operational Status
Operational. Planned changes by 2026-12-31: named SYS-02 accounts with MFA (R-001), MFA on the gateway VPN (R-004), an engineering repository inside the backed-up suite (R-006), MSP-managed endpoint detection and response (R-005), and an MSP security addendum (R-010).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts Moderate and higher risk; approves this plan, policies, and spending |
| Information Security Officer | Office and Compliance Manager | Day-to-day security; maintains this plan, the risk register, and the POA&M; CUI program lead; supplier screening |
| SYS-01 administrator | Security Systems Technician | Tenant configuration, cardholders, door schedules, face pilot |
| SYS-02 and SYS-03 administrator | Lead Controls Technician | Monitoring service, alarm rules, gateways, technician VPN |
| IT operations | MSP | Laptops, office network, suite administration on request, SYS-08 backup |
| Independent assessor | Building systems security consultant | Annual control assessment (P07) |

**Overlapping roles.** The Information Security Officer also runs HR, billing, and contracts, and the Lead Controls Technician both changes and checks the gateways. With 7 people this cannot be avoided. Compensating checks: the owner approves every new administrator account, reviews the POA&M and the weekly log review results monthly, and an independent consultant assesses the controls each year.

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facility operations and maintenance (BAS alarms, schedules, setpoints, programs) | Low | Moderate | Moderate | Wrong setpoints or schedules can damage equipment or make a building unusable; field controllers keep running locally, so loss of the platform is not immediate (P05 MTD 4 h for alarm monitoring) |
| Physical security (access control, door schedules, video, security system layouts) | Moderate | Moderate | Moderate | Unauthorized door changes expose people and property; layouts are exempt public records (Fla. Stat. 119.071(3)(a)); door controllers keep the last cardholder list offline |
| Personal identity and authentication (cardholder records, badge photos, face templates) | Moderate | Moderate | Low | About 1,050 people; breach duties under Fla. Stat. 501.171 |
| Federal CUI building information (GSA drawings) and FCI | Moderate | Low | Low | CUI (Physical Security category) and work orders |
| **BSOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Physical security integrity was not rated High because every county door also has a mechanical key override, the county keeps its own security staff, and the administration building has local lockdown buttons that work without the cloud. The risk register still treats door manipulation as one of the most serious scenarios (R-002).

**Baseline:** the NIST SP 800-53B **Moderate** baseline, which the county exhibit requires. This plan documents **44 controls** in `control-implementation.csv`: the ones that carry the county exhibit's named requirements (MFA, incident notice, assessment), the High risks in P01, and the FAR clauses. All **177 base controls** are rated in the gap analysis (P03) with the same statements, so the two documents do not drift. Tailoring:
- **OT tailoring** follows NIST SP 800-82 Rev. 3: no active vulnerability scans of customer BAS networks without the customer's approval (RA-5), no malware agents on gateways (SI-3), and segmentation to compensate for unencrypted BACnet (SC-8).
- **Not applicable:** 4 developer controls (SA-3, SA-10, SA-11, SA-15). The company develops no software; its vendors' practices are reviewed under SA-9.
- **Inherited:** most physical and environmental controls come from the SaaS vendors' data centers and the office landlord. The SYS-01 vendor's SOC 2 report is the main evidence (P09).

CSF 2.0 subcategories come from NIST's official informative references where NIST lists one. 6 of the 44 controls (AC-21, MA-4, MP-4, PL-4, PS-3, PS-4) have no NIST reference, and their CSF entries are author mappings.

## 7. Authorization Boundary Description
- **Inside:** the company's SYS-01 tenant and its configuration (including SYS-12), the company's SYS-02 subscription and alarm rules, the 7 SYS-03 gateways, the suite tenant (SYS-04), the CMMS tenant (SYS-05), 16 company devices (SYS-06), the office network (SYS-07), the suite backup subscription (SYS-08), and the company's named administrator accounts on the city building systems (SYS-10).
- **Outside (interconnected):** the county-owned door controllers, readers, and cameras; the county and city BAS controllers and networks; the city BAS server and access control server (SYS-10); the vendors' platforms and data centers; the MSP's RMM platform; the payroll service (SYS-09); and GSA's systems at the federal building (SYS-11), reached only on GSA equipment.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| County BAS networks (through SYS-03) | Bidirectional | BACnet alarms, trends, schedule and setpoint writes | CT-C scope of work; no interconnection record yet (CA-3) |
| City BAS networks (through SYS-03) | Inbound to SYS-02 | BACnet alarms and trends (read-only) | CT-M scope of work |
| City VPN to SYS-10 | Bidirectional | Administration of city BAS and access control | City named accounts and city MFA |
| County security staff (SYS-01 operator accounts) | Bidirectional | Door status, lockdown, video | CT-C; named operator accounts with MFA |
| County HR and facilities (email) | Inbound | Badge requests and removals | CT-C |
| Prime contractor (email, suite sharing) | Bidirectional | Work orders (FCI), CUI drawings | CT-F subcontract |
| Mechanical subcontractor (email) | Outbound | Work orders, drawings | Subcontract with confidentiality clause only (PS-7) |
| MSP RMM platform | Inbound administrative access | Laptop management | MSP contract (no security terms yet) |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Access control and video tenant (SYS-01, with SYS-12) | SaaS | Access control vendor | Security Systems Technician |
| BAS monitoring subscription (SYS-02) | SaaS | BAS monitoring vendor | Lead Controls Technician |
| Site gateways (7) (SYS-03) | OT network appliance | County and city mechanical rooms | Lead Controls Technician |
| Productivity suite tenant (SYS-04) | SaaS | Suite vendor | Office and Compliance Manager (MSP administers) |
| CMMS tenant (SYS-05) | SaaS | CMMS vendor | Service Coordinator |
| Laptops (6), rugged tablets (3), phones (7) (SYS-06) | Endpoint | Office, vans, sites | Office and Compliance Manager (MSP operates laptops) |
| Firewall, staff Wi-Fi, guest Wi-Fi (SYS-07) | Network | Office network closet | Office and Compliance Manager (MSP operates) |
| Suite backup subscription (SYS-08) | SaaS | Backup provider (MSP subcontractor) | Office and Compliance Manager (MSP operates) |

**Gap:** this table is the first full list of company components. It does not yet list the customer devices each gateway reaches; P07 found 11 BACnet controllers at the city community center missing from the CMMS asset list (CM-8).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 44 controls:
- Implemented: 8
- Partially implemented: 22
- Planned: 14
- Not applicable: 0

By responsibility: 23 system-specific (the company), 19 hybrid (the company with a vendor or the MSP), 2 common/inherited (fully provided by SaaS vendors).

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Access control vendor (SYS-01) | Platform security, encryption, backups, lockout (AC-7), audit records (AU-2, AU-11), data center physical controls (PE-3) | SOC 2 Type 2 report reviewed 2026-08-20 (P09) | Complementary user entity controls: administrator provisioning and removal, MFA enforcement, review of administrator activity, notice to the vendor of a suspected compromise |
| BAS monitoring vendor (SYS-02) | Platform security, encryption in transit, audit log (90 days), lockout | Vendor documentation and service terms only; **no SOC report** | Named accounts, MFA, log export, alarm rule review; security questionnaire (SA-9) |
| Productivity suite vendor | Platform security, encryption (SC-8, SC-28), spam filtering (SI-8), audit logging | Vendor documentation | Sharing settings, MFA, log review |
| MSP | Laptop patching (SI-2), antivirus (SI-3), encryption (SC-28), firewall (SC-7), suite backup operation (CP-9) | Monthly MSP report; P07 evidence requests | Oversight: monthly report review, security addendum and yearly review (R-010) |
| Backup provider (MSP subcontractor) | Storage of suite backups (CP-9) | None yet; first restore test due 2026-10-31 | Confirm terms through the MSP |

**Inherited does not mean done.** The SYS-01 vendor's controls protect the county's cardholders only if the company removes administrators on time (AC-2, PS-4) and reviews administrator activity (AU-6). Both are open gaps.

### 10.3 Control assessment status
Assessed 2026-08-03 to 2026-08-06 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Company users sign in to the suite, the CMMS, SYS-01, and the named SYS-02 accounts with a password and a phone authenticator app, which fits the Moderate category for remote and privileged access. Number matching for push approvals is being turned on (R-002). **Gaps:** the shared SYS-02 "oncall" account and the gateway VPN use passwords only (POA&M items for IA-2(1) and AC-17).

Cardholders use badges, not passwords. Face verification in the county pilot is a second factor with the badge, never a replacement (P10). At the federal building, the 2 PIV holders use GSA-issued PIV cards under FIPS 201 on GSA equipment, managed by GSA.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **BACnet:** building automation and control networking protocol
- **BAS:** building automation system
- **BSN:** GSA Building Systems Network
- **BSOP:** Building Systems Operations Platform
- **BTTRG:** GSA Building Technologies Technical Reference Guide
- **CMMS:** computerized maintenance management system
- **CUI:** controlled unclassified information
- **FCI:** federal contract information
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **PIV:** personal identity verification
- **POA&M:** plan of action and milestones
- **RMM:** remote monitoring and management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office and Compliance Manager (Information Security Officer) |
