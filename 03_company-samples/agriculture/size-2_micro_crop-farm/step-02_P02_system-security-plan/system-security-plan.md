# System Security Plan: Farm Management and Irrigation Control Platform (FMICP)

**Organization:** Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) | **Tier:** Micro | **Vertical:** Agriculture, Forestry, Fishing and Hunting
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Farm Management and Irrigation Control Platform (**FMICP**), identifier CSC-SYS-001.

## 2. System Overview
The FMICP runs the farm's field work, irrigation, harvest records, and food safety records across about 420 acres in two parcels (Home Farm and River Tract). It supports crop plans and chemical application records, remote control of 5 center pivots, the pump station that feeds the watermelon drip and fertigation system, the harvest log and load records for the packer-shipper, the crew's daily hours (including 2 H-2A workers), and the Produce Safety records the farm must keep under 21 CFR Part 112. It serves 7 employees, the MSP, and the irrigation dealer.

The farm owns almost no IT infrastructure. Most of the FMICP is vendor SaaS, a managed service provider (MSP) runs the office computers, the firewall, and the backup, and the irrigation dealer services the pump station. This plan therefore says, for each control, what the farm does itself, what the MSP or a dealer does for it, and what it inherits from a SaaS vendor.

**Major components:**
- **SYS-01:** farm management software (FMIS, vendor SaaS) with web and mobile apps and the irrigation control module (farm-managed configuration)
- **SYS-02:** productivity suite (SaaS): email and the Office folder
- **SYS-03:** 1 office desktop, 2 laptops, 2 rugged tablets, 3 company phones
- **SYS-04:** shop network: MSP-managed firewall, shop Wi-Fi, wireless bridge to the pump station, one internet line
- **SYS-05:** irrigation OT: pump station controller, VFD well pump, fertigation injector, drip zone valves, the dealer's cellular remote-access gateway, 5 pivot panels with cellular modems, soil moisture probes, flow meters, and a weather station
- **SYS-08:** cloud backup of the productivity suite (SaaS, operated by the MSP)

The OT portion follows NIST SP 800-82 Rev. 3 guidance, scaled to a single pump station and five pivots.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for this system |
|---|---|---|---|
| Benchmark | NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (2024) | Voluntary benchmark (P03). No binding federal cybersecurity rule applies |
| Benchmark (OT) | Guide to Operational Technology Security | NIST SP 800-82 Rev. 3 (2023) | Voluntary guidance for SYS-05 |
| Binding | Produce Safety Rule, records | 21 CFR 112.161-112.167 | Applies (covered farm for watermelons). Produce Safety records are kept in SYS-01 |
| Binding | H-2A earnings records | 20 CFR 655.122(j) | Applies. Daily hours in SYS-01 are part of the earnings record |
| State | Florida Information Protection Act (data security, disposal, breach notice) | Fla. Stat. 501.171 | Applies to worker personal information in SYS-02 and to operator geolocation in SYS-06 |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Approved 2026-08-31 |

Not applicable:
- **N11-R01**, the FSMA intentional adulteration rule (21 CFR Part 121): it applies only to facilities that must register under FD&C Act section 415 (21 CFR 121.1), and farms are exempt from registration (21 CFR 1.226(b)). Its food defense approach is used only as a voluntary checklist for the fertigation risk (P01 R-008).
- **FAA Part 137:** the farm does no aerial application. Its one drone takes pictures and is flown under Part 107.
- **CIRCIA** (proposed 6 CFR Part 226): not final, and as proposed it would not cover a farm under the SBA size standard.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Owner and General Manager on 2026-08-31.

### 4.2 System Authorization Decision
The farm is not a federal agency, so there is no formal authorization. The equivalent internal decision: on 2026-08-31 the Owner and General Manager accepted continued operation of the FMICP on two conditions: the irrigation dealer's always-on remote access is replaced by on-request access (POAM-002, due 2026-10-31), and the three High risks in P01 are treated by their due dates.

### 4.3 System Operational Status
Operational. Planned changes: on-request dealer access through the gateway (R-002), network separation of the pump station (R-020), backup redesign (R-004), and endpoint detection and response (R-001), all due by 2026-12-31.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner and General Manager | Overall accountability; accepts Moderate, High, and Very High risks; approves this plan, policies, and spending |
| Security Coordinator | Office Manager | Day-to-day security (about 3 hours a week); maintains this plan, the risk register, the inventory, and the vendor file; manages the MSP; accepts Low risks |
| OT operator and SYS-01 irrigation administrator | Irrigation and Equipment Technician | Operates SYS-05; approves pump station and pivot changes; runs hand operation; remote pilot for SYS-07 |
| Records owner | Field Supervisor | Daily hours and Produce Safety records in SYS-01 |
| IT operations | MSP | Office computers, firewall, Wi-Fi, productivity suite administration, SYS-08 backup |
| OT maintenance | Irrigation dealer | Pump station controller and gateway, pivot panels |
| Independent assessor | Contracted consultant with OT experience | Annual control assessment (P07) |

**Overlapping roles.** The Office Manager both runs and checks most security work, and the Technician is the only person who operates and changes the OT. The compensating checks are the Owner and General Manager's monthly review of the POA&M, the independent annual assessment (P07), and SYS-01 irrigation change alerts to two phones (P01 R-003, due 2026-09-30).

## 6. System Information Types and System Categorization
SP 800-60's information type catalog is built for federal missions and has no farm operations type. The types below are author-defined following the SP 800-60 method; impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Irrigation and fertigation control (schedules, setpoints, controller program) | Low | Moderate | Moderate | Wrong commands can stress or burn a crop, exceed the water permit, or expose workers to chemicals; hand operation keeps the availability impact to Moderate (P05 MTD 24 h) |
| Produce Safety and field records | Low | Moderate | Low | Records must be accurate and indelible (21 CFR 112.161(a)(3)); paper forms cover a short outage |
| Worker hours records (H-2A earnings records) and personnel files | Moderate | Moderate | Low | Names with hours, passport and visa numbers, and Social Security numbers; errors lead to wage disputes and program findings |
| Farm operational and yield data | Moderate | Low | Low | Commercially sensitive (yields, load commitments); little harm if briefly unavailable |
| **FMICP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 7-person farm. The plan documents 42 controls that carry the farm's main risks and basic cyber hygiene (see `control-implementation.csv`). All other Moderate-baseline controls are handled one of two ways:
- **Inherited** from the SaaS vendors (physical, platform, and application controls), with the FMIS vendor's SOC 2 report as the main evidence (P09).
- **Tailored out** for this tier, where the control addresses federal program management or organizations with IT staff and software development (for example, configuration change boards, separate development environments, and developer testing). These are recorded as tailoring decisions, not gaps.

## 7. Authorization Boundary Description
The boundary contains what the farm controls or pays someone to control on its behalf:
- **Inside:** the farm's SYS-01 tenant configuration and user roles, the productivity suite tenant and Office folder (SYS-02), 8 devices (SYS-03), the shop network (SYS-04), the pump station, gateway, pivot panels, probes, flow meters, and weather station (SYS-05), and the farm's backup subscription (SYS-08).
- **Outside (external services, interconnected):** the FMIS vendor's platform and the pivot manufacturer's connectivity service behind it, the cellular carriers, the MSP's remote management platform, the equipment dealer's telematics portal (SYS-06), the drone and imagery (SYS-07), and the agronomy analytics vendor (SYS-09, a pilot assessed in P10).
- **Outside and not interconnected:** accounting and payroll (SYS-10). Payroll exports and H-2A documents reach the Office folder by download, so the Office folder is inside the boundary.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Pivot manufacturer connectivity service (through SYS-01) | Bidirectional over the carrier's private cellular network | Start, stop, speed, and status | FMIS vendor terms; pivot service subscription |
| Irrigation dealer (cellular gateway) | Inbound remote sessions to the pump station controller | Full control and programming | Time-and-materials agreement with **no security terms (gap)** |
| Equipment dealer telematics (SYS-06) | Inbound to SYS-01 | As-applied maps, yield monitor data | Dealer portal terms; **no access or retention terms (gap)** |
| Agronomy analytics vendor (SYS-09) | Outbound imagery; inbound yield estimates | Drone images; field-level estimates | Click-through terms allowing secondary use (**gap**, P10) |
| Packer-shipper | Outbound by email | Harvest log, field and load records, food safety audit results | Grower agreement (24-hour notice term) |
| MSP remote management platform | Inbound administrative access | Office computer management | MSP contract |
| Payroll service and H-2A filing agent (SYS-10) | Outbound by upload; inbound reports | Hours, pay, passport and visa data | Service terms; **no breach contact registered (gap)** |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| SYS-01 FMIS tenant (records, labor, food safety, irrigation module) | SaaS | FMIS vendor | Owner and General Manager |
| Productivity suite tenant and Office folder (SYS-02) | SaaS | Productivity suite vendor | Office Manager (MSP administers) |
| Office desktop (1), laptops (2), rugged tablets (2), phones (3) (SYS-03) | Endpoint | Farm office and field | Office Manager (MSP operates the desktop and laptops) |
| Firewall, shop Wi-Fi, pump station bridge (SYS-04) | Network | Shop | Office Manager (MSP operates) |
| Pump station controller, VFD, fertigation injector, drip zone valves (6) (SYS-05) | OT | Pump station, Home Farm | Irrigation and Equipment Technician (dealer maintains) |
| Cellular remote-access gateway (SYS-05) | OT network | Pump station panel | Irrigation and Equipment Technician (dealer configures) |
| Center-pivot control panels (5) with cellular modems (SYS-05) | OT | Home Farm (3), River Tract (2) | Irrigation and Equipment Technician |
| Soil moisture probes (12), flow meters (2), weather station (1) (SYS-05) | IoT | Fields | Irrigation and Equipment Technician |
| Cloud backup subscription (SYS-08) | SaaS | Backup service (resold by the MSP) | Office Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 42 controls:
- Implemented: 6
- Partially implemented: 24
- Planned: 12
- Not applicable: 0

By responsibility: 27 system-specific (the farm), 14 hybrid (the farm with a vendor, the MSP, or a dealer), 1 common/inherited (fully provided by the SaaS vendors).

### 10.2 Inherited, MSP-provided, and dealer-provided controls
| Provider | What the farm relies on | Evidence | What the farm must still do |
|---|---|---|---|
| FMIS vendor | Platform security, encryption, backups (CP-9), lockout (AC-7), audit trail (AU-2), the pivot connectivity service | SOC 2 Type 2 report received 2026-08-18 and reviewed (P09) | Complementary user entity controls: user provisioning and removal, MFA for every user, review of audit and change reports, protection of the devices that run the app |
| Productivity suite vendor | Platform security, encryption at rest and in transit (SC-8, SC-28), lockout (AC-7), audit logging (AU-2) | Vendor documentation | Accounts, MFA for every mailbox, forwarding and sharing settings, log review |
| MSP | Patching (SI-2), antivirus (SI-3), firewall and Wi-Fi (SC-7, AC-18), laptop encryption (SC-28), backup operation (CP-9) | Monthly MSP report; P07 evidence requests | Oversight: approve exceptions, read the monthly report, annual MSP review (P01 R-021) |
| Irrigation dealer | Pump station programming and gateway configuration (CM-2, MA-4) | Service invoices only | Approve each remote session; hold a copy of the program; security terms in the agreement (POAM-002, POAM-010) |
| Backup service (resold by the MSP) | Storage of suite copies (CP-9) | None until the first restore test (due 2026-09-30) | MFA on the console; immutable retention |

**Inherited does not mean done.** Two of the FMIS vendor's complementary user entity controls are open gaps at the farm: MFA for every user (IA-2(1); the Technician's account and the shared field login) and review of audit and change reports (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-10 to 2026-08-13 by an independent consultant, with OT tests on 2026-08-12. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Office users sign in to the productivity suite with a password and a phone authenticator app, which is appropriate for a Moderate system. Two exceptions are not acceptable and are on the POA&M: the Technician's SYS-01 administrator account, which can start and stop pivots, has no MFA (POAM-008), and the crew shares one SYS-01 login (POAM-001). Crew members will get named SYS-01 accounts with a short PIN on the managed field tablet, which is proportionate for entering hours and Produce Safety records on a farm-owned device.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and FMIS vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **FMICP:** Farm Management and Irrigation Control Platform
- **FMIS:** farm management (and irrigation) software
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **OT:** operational technology
- **PLC:** programmable logic controller (the pump station controller is a small PLC with a touchscreen)
- **POA&M:** plan of action and milestones
- **RTK:** real-time kinematic (GNSS correction for guidance)
- **VFD:** variable-frequency drive

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Office Manager (Security Coordinator) |
