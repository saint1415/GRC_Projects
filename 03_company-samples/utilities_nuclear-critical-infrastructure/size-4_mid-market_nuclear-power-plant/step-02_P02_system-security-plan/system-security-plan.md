# System Security Plan: Plant Business Network and Work Management System (PBN-WMS)

**Organization:** Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) | **Tier:** Mid-Market | **Vertical:** Nuclear Reactors, Materials, and Waste
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Plant Business Network and Work Management System (**PBN-WMS**), identifier CSC-PBN-01. It comprises SYS-01 to SYS-11 in `../00_company-facts.md`. It is the company's major non-safety system: every business process in the BIA (P05) runs on it, and it borders the CSP's protected levels.

## 2. System Overview
The PBN-WMS supports work control, clearances, the corrective action program, document control, radiation work permits, access authorization records, business communications, finance, supply chain, HR, and the generation data service. It serves about 1,150 accounts (about 2,150 during a refueling outage) at the Station and the EOF.

**Where it sits in the CSP defensive architecture.** The CSP allocates CDAs to Levels 3 and 4. The PBN-WMS is the Level 2 business network and the systems below it (the cloud and the internet). Data moves only one way, from Level 3 to Level 2, through a one-way deterministic device. Nothing on the PBN-WMS can initiate a connection to Level 3 or Level 4. This plan covers Level 2 and below. The CSP covers Levels 3 and 4.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Work management system (WMS) with the clearance and tagging module | On-premises, site data center |
| SYS-02 | Corrective action program (CAP) and electronic document management system (EDMS) | On-premises, site data center |
| SYS-03 | Directory, cloud identity provider (SSO and MFA), cloud privileged access broker | Hybrid (SaaS identity provider) |
| SYS-04 | Productivity suite (email, files, chat) | SaaS |
| SYS-05 | ERP (finance, supply chain, HR, payroll, training records) and applicant tracking | SaaS |
| SYS-06 | Business network at the Station and the EOF, site data center, about 90 servers, 1,150 workstations and laptops, 220 rugged field tablets | On-premises |
| SYS-07 | Cloud landing zone: identity and security, shared services, workloads, recovery accounts | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-08 | SIEM (MSSP-operated), EDR, vulnerability scanner | SaaS and on-premises |
| SYS-09 | Historian replica and one-way device receive server | On-premises (Level 2 side) |
| SYS-10 | RWP and dose tracking system | On-premises |
| SYS-11 | Access authorization records system | Restricted enclave on the business network |

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the PBN-WMS |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber security rule and the approved CSP | 10 CFR 73.54 | The PBN-WMS is not a CDA, but it is the lower level that the CSP boundary protects against. Changes that create a data path to or from Level 3 need the CST's evaluation under 73.54(d)(3) (P03) |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | CAP (SYS-02) is the record system for 24-hour recordable events (73.77(b)); business network detections may start a 73.77(a) clock |
| C-NUCLEAR-R04 | NERC CIP low impact | CIP-003-9 Attachment 1 | The dispatch network is separate, but its vendor remote access and transient asset controls share IT processes with the PBN-WMS |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | **Proposed only.** Tracked in P03; not a current obligation |
| C-NUCLEAR-S01 | Safeguards Information | 10 CFR 73.21-73.22 | SGI must never be stored or processed on the PBN-WMS; it stays on stand-alone computers (73.22(g); SYS-16) |
| C-NUCLEAR-S02 | Access authorization | 10 CFR 73.56 | Personnel with electronic access that could adversely impact safety, security, or EP must be in the program (73.56(b)(1)(ii)); SYS-11 holds the program's records |
| C-NUCLEAR-S04 | Florida breach notification | Fla. Stat. 501.171 | Employee, contractor, and access authorization personal information |
| C-NUCLEAR-S05 | PPA-2 data service | Contract | SOC 2 Type 2 on the generation data and settlement reporting service (P09) |
| C-NUCLEAR-S06 | NIST SP 800-53 Rev. 5 Moderate baseline and CSF 2.0 | Voluntary | Control baseline for this plan |
| Internal | Policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable: SEC cybersecurity disclosure rules (private company); 10 CFR 73.110 (not a Part 53 licensee); HIPAA (not a covered entity).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Site Vice President (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the PBN-WMS accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Site Vice President for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the CST must complete the 73.54(d)(3) evaluations of the 3 unevaluated changes by 2026-11-30; WMS failover must be tested before the 2027-03-08 refueling outage; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.

### 4.3 System Operational Status
Operational. Major modifications planned:
- Server segmentation of the business network (due 2027-02-28)
- Privileged access management for directory, database, and WMS administrators (due 2027-01-31)
- Upgrade of the clearance and tagging module off Windows Server 2012 R2 (due 2027-06-30, after the outage)
- Onboarding of WMS, EDMS, CAP, and the one-way device receive server to the SIEM (due 2026-12-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Site Vice President | Accountable for the PBN-WMS; accepts Moderate risk; NERC CIP Senior Manager |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Information system security officer | IT Security Manager | Day-to-day control owner; MSSP oversight |
| Technical owner | IT Director | Operations of SYS-01 to SYS-11 |
| CSP boundary authority | Cyber Security Program Manager | Decides whether a change touches 73.54 scope; owns the one-way device and everything above it |
| Business owners | Director of Work Management (SYS-01), Regulatory Affairs Manager (CAP), Director of Engineering (EDMS), Radiation Protection Manager (SYS-10), Director of Security (SYS-11), Energy Marketing and Settlements Manager (GDSR) | Access approvals and downtime procedures for their systems |
| GRC | Compliance and GRC Lead | Risk register, POA&M, NERC evidence |
| Independent assessment | Co-sourced internal audit firm with Nuclear Oversight | Annual assessment (P07) |
| Monitoring | MSSP | 24x7 SIEM and EDR monitoring of the PBN-WMS |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Energy supply and production management (work orders, clearances, outage schedule, plant data replica) | Moderate | Moderate | Moderate | Disclosure of work schedules and plant data aids an attacker's planning; altered clearance data could injure a worker, but every tag is independently verified in the field; outage processes have an 8 to 24 hour MTD (P05) |
| Security-Related Information (CAP security entries, cyber assessments, drawings marked SRI) | Moderate | Moderate | Low | Not SGI (SGI is never on this system); disclosure would help an adversary but would not by itself defeat the CDA protections |
| Personnel identity and authentication; access authorization records | Moderate | Moderate | Low | Background investigation and fitness-for-duty records for about 2,000 people; harm to individuals and to the 73.56 program if disclosed |
| Financial management and contract (PPA settlement, invoicing) | Moderate | Moderate | Low | Settlement data integrity matters to buyers (P09); MTD 72 to 120 hours |
| Radiation protection records (RWPs, dose) | Low | Moderate | Moderate | Dose records must be accurate; RCA work stops without RWPs (MTD 12 hours) |
| System and network monitoring | Moderate | Moderate | Low | Needed to detect a pivot toward the CSP boundary |
| **PBN-WMS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** A tampered clearance could contribute to a worker injury. The team kept integrity at Moderate because clearances are verified in the field by a second qualified person, and because the clearance module cannot operate plant equipment. To compensate, the plan adds integrity tailoring: CM-3 routes WMS changes through the change advisory board, SI-7 adds integrity monitoring, and AC-5 enforces separation of duties for clearance approval.

**Why the PBN-WMS is not a CDA.** The CSP's 73.54(b)(1) analysis (CST, 2017, updated 2023) concluded that no safety, security, or EP function depends on the PBN-WMS. That conclusion is sound for the 2023 design. It must be re-checked for 3 later changes (gap 3): the cloud analytics feed, the predictive maintenance gateway, and the ERO callout service.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the WMS and its clearance and tagging module;
- CAP and EDMS;
- the directory, the identity provider tenant, and the privileged access broker;
- the company's productivity suite and ERP tenants;
- the business network at the Station and the EOF, the site data center, and about 1,370 endpoints;
- all 4 cloud accounts and their workloads;
- the company's SIEM tenant, EDR, and scanner;
- the historian replica and the one-way device receive server;
- the RWP and dose tracking system;
- the access authorization records enclave.

**Outside the boundary:**
- Level 3 and Level 4 CDAs, including the one-way device itself and the plant historian (SYS-12; CSP);
- security systems (SYS-13; CSP);
- EP systems, ERDS, and the ERO callout service (SYS-14);
- the dispatch network and its NERC low-impact BES Cyber Systems (SYS-15; CIP-003-9);
- SGI stand-alone computers (SYS-16; 73.22(g));
- vendors' platforms (cloud provider, identity provider, productivity suite, ERP, MSSP, ERO callout service).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Level 3 plant historian (through the one-way deterministic device) | Inbound only | Plant process data | CSP (no agreement needed; internal) |
| Cloud landing zone | Bidirectional (site-to-cloud VPN) | Analytics copy of plant data, GDSR, backups | Cloud provider terms |
| PPA-2 buyer data portal | Outbound (mutual TLS) | Hourly generation and attribute data | PPA-2 data exhibit |
| MSSP | Inbound logs; remote response actions | Security logs | MSSP contract; SOC 2 Type 2 |
| WMS vendor | Inbound remote support (VPN) | WMS configuration and data | Support contract; **no interconnection terms; shared account (gap 4)** |
| Predictive maintenance vendor (AI-001) | Outbound from the gateway to the vendor cloud; vendor VPN for support | Vibration and temperature data from balance-of-plant equipment | Pilot agreement; **no security addendum (P10)** |
| Industry shared access data system | Bidirectional | Access authorization status | Industry participation agreement |
| Background screening vendor and fitness-for-duty laboratory | Bidirectional | Personal information | Contracts with confidentiality terms |
| ERO callout service | Outbound roster; inbound responses | Names and phone numbers | Vendor terms; not evaluated by the CST |
| Banks | Bidirectional | Payments | Bank agreements |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| WMS application and database servers | Virtual machines | Site data center | Director of Work Management |
| Clearance and tagging module (2 servers, Windows Server 2012 R2) and tag printers | Physical servers | Site data center; work control center | Director of Work Management |
| CAP and EDMS servers | Virtual machines | Site data center | Regulatory Affairs Manager; Director of Engineering |
| Directory domain controllers (4) | Virtual machines | Site data center (2), EOF (1), cloud shared services (1) | IT Director |
| Identity provider and privileged access broker tenants | SaaS | Identity vendor | IT Security Manager |
| Productivity suite and ERP tenants | SaaS | Vendors | IT Director; Chief Financial Officer |
| Core switches, internet edge firewalls, VPN appliance, Wi-Fi | Network | Station and EOF | IT Director |
| Workstations and laptops (1,150), rugged field tablets (220) | Endpoint | Station and EOF | IT Director |
| Historian replica and one-way device receive server | Physical servers | Site data center | Cyber Security Program Manager (receive server); IT Director (replica) |
| RWP and dose tracking servers | Virtual machines | Site data center | Radiation Protection Manager |
| Access authorization enclave (2 servers, restricted VLAN) | Virtual machines | Site data center | Director of Security |
| Cloud accounts (4) | IaaS/PaaS | Public cloud | IT Director |
| SIEM tenant, EDR console, vulnerability scanner | SaaS and virtual machine | MSSP; site data center | IT Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The PBN-WMS uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 135 controls** in `control-implementation.csv`. They cover the Moderate controls that address the risks in P01 (privileged access, segmentation, vendor access, recovery, monitoring, supply chain) and the controls that support the CSP boundary, 73.77(b) recording, and the PPA-2 data service.
- **Selected by tailoring (added, 3):** CA-8 (penetration testing, a High-baseline control) because the business network borders the CSP boundary, and PM-1 and PM-9 for the program plan and risk strategy.
- **Integrity tailoring:** AC-5, CM-3, and SI-7 statements cover clearance approval, WMS changes, and integrity monitoring (section 6).
- **Inherited without separate statements:** the remaining Moderate physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, inherited from the cloud provider, identity provider, productivity suite and ERP vendors, and the MSSP, and evidenced by their SOC 2 Type 2 reports (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 135 documented controls:**
| Status | Count |
|---|---|
| Implemented | 64 |
| Partially implemented | 67 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 135 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 102 | Company |
| Hybrid | 17 | Identity provider, MSSP, cloud provider, EDR vendor, ERP vendor, VPN appliance vendor |
| Common/Inherited | 16 | Station physical protection program (PE-1, PE-2, PE-3, PE-6), access authorization program (PS-1, PS-3), identity provider (AC-2(1), AC-7, AC-12, IA-2(8)), MSSP (AU-6(1), IR-7), cloud provider (CP-6, SC-12), productivity suite vendor (SI-8), internet service providers (SC-5) |

The Partially implemented statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. Two of the common control providers are internal programs (physical protection and access authorization), which is typical at a nuclear station: the business network inherits the site's physical and personnel security.

### 10.2 Control assessment status
The co-sourced internal audit firm, with Nuclear Oversight, assessed 33 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce and contractors.** All users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Outage contractors receive accounts with an end date tied to the outage.
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-01-31 (P01 R-004). Until then, cloud administration goes through the privileged access broker with just-in-time elevation; on-premises administration remains a gap.
- **Vendors.** The 2 shared vendor VPN accounts will be replaced by named, time-limited accounts with MFA and session recording by 2026-11-30 (P01 R-008).
- **External parties.** The PPA-2 buyer uses its own data portal; no buyer accounts exist on the PBN-WMS.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10). The CSP, the CDA inventory, and the defensive architecture drawings are Security-Related Information held by the CST and are referenced, not reproduced.

## 13. Acronym List and Glossary
- **CAP:** corrective action program
- **CDA:** critical digital asset (73.54 scope)
- **CSP:** cyber security plan (NRC-approved license condition)
- **CST:** cyber security team
- **EDMS:** electronic document management system
- **EOF:** emergency operations facility
- **ERO:** emergency response organization
- **GDSR:** generation data and settlement reporting
- **Level 2, 3, 4:** security levels of the CSP defensive architecture; Level 2 is the business network
- **PMMD:** portable media and mobile devices
- **RWP:** radiation work permit
- **SGI:** Safeguards Information (10 CFR 73.21-73.22)
- **SRI:** Security-Related Information (company marking for sensitive security information that is not SGI)
- **WMS:** work management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | IT Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Site Vice President | IT Security Manager with the vCISO |
