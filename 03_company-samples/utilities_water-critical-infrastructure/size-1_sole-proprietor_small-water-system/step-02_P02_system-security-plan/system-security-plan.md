# System Security Plan (short form): Water System Operations Profile

**Organization:** Cris Santos Company (small community water system) | **Tier:** Sole Proprietorship | **Vertical:** Water and Wastewater Systems
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Water System Operations Profile (**WSOP**), identifier CSC-WSOP-001.

## 2. System Overview
The WSOP is everything the owner-operator uses to make and deliver safe drinking water to 138 homes (330 persons) and to run the business: the treatment control panel in the well house (SYS-01), the cellular router and cloud remote access portal that reach it (SYS-02), the billing SaaS (SYS-03), email and file storage (SYS-04), the laptop (SYS-05), the phone (SYS-06), the home office network (SYS-07), and the portal's anomaly alert feature (SYS-08). See `../00_company-facts.md` section 3.

**Why this is the "Water treatment SCADA" at this size.** There is no SCADA server or control room. The control system is one PLC panel with a touchscreen HMI, and the "SCADA" layer is the vendor's cloud portal on the owner's phone. That portal is also the main attack path (P08). Most IT safeguards are **inherited from SaaS vendors**; the owner is responsible for identities, the panel and router settings, devices, and contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status for this system |
|---|---|---|---|
| C-WATER-R01 | SDWA section 1433 risk and resilience assessment and ERP | 42 U.S.C. 300i-2 | **Not applicable**: serves 330 persons, not more than 3,300 (P03 G-001, G-002). Its elements are used as a voluntary benchmark |
| C-WATER-R02 | CIRCIA reporting | 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **Proposed only**; tracked, not an obligation (P03 G-003) |
| NPDWR | Public notification rule | 40 CFR Part 141, Subpart Q (141.201-141.205) | Applies (community water system) |
| NPDWR | Ground Water Rule compliance monitoring, treatment technique, reporting | 40 CFR 141.403(b)(3), 141.404(c), 141.405 | Applies (4-log treatment notified to the state) |
| NPDWR | Reporting and record maintenance | 40 CFR 141.31, 141.33 | Applies |
| State | Customer data security, breach notice, disposal | Fla. Stat. 501.171 | Applies to customer portal credentials held by the billing vendor |
| Internal | Information Security Policy | POL-01 (P06) | Adopted 2026-08-31 |

Benchmarks (voluntary): NIST CSF 2.0 and NIST SP 800-82 Rev. 3 for the control panel; EPA's small-system resources listed on its AWIA section 2013 page.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-operator on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private water system. Equivalent decision: the owner-operator accepted continued operation on 2026-08-31, on condition that the two High risks in P01 are treated by their due dates (R-001 portal MFA by 2026-09-15; R-002 integrator access by 2026-10-31, with its account disabled between approved sessions from 2026-09-15) and the plant stays able to run by hand.
### 4.3 System Operational Status
Operational. Planned changes: MFA and named accounts on the portal (2026-09-15); router firmware update (2026-09-15); PLC and HMI password change with the integrator (2026-11-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, licensed operator, security lead, risk acceptor | Owner-operator | Every role (designated in POL-01) |
| Relief operation | Licensed relief operator (contractor) | Runs the plant on the owner's days off; daily grab sample |
| Control system support | Controls integrator (contractor) | Panel programming and remote support through the portal |
| Technical support | On-call IT technician (confidentiality agreement since 2026-07-15) | Laptop, phone, and home network help; no standing access |
| Service providers | Portal vendor, billing SaaS vendor, email and file provider | Operate inherited controls |

## 6. System Information Types and System Categorization
Information types are named by the owner and rated with the FIPS 199 impact definitions.

| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Treatment control (PLC logic, setpoints, portal commands) | Low | **Moderate** | **Moderate** | A wrong setpoint can stop disinfection for hundreds of people (P05 BP-01 MTD 4 h). The pump's mechanical stroke cap and the daily grab sample keep the worst case short of catastrophic |
| Compliance records (residual log, lab results, notices) | Low | Moderate | Low | Wrong or lost records cause violations; deadlines are days, not hours |
| Customer information (names, addresses, contacts, portal credentials) | Moderate | Low | Moderate | Portal credentials are personal information under Fla. Stat. 501.171; contacts are needed for 24-hour notices |
| **WSOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 25 controls that a one-person water system can run (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the portal vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program.

## 7. Authorization Boundary Description
- **Inside:** the control panel and alarm dialer, the cellular router, the owner's portal, billing, email, and file accounts and their settings, the laptop, the phone, the home network, and paper records at the well house and home office.
- **Outside (external services):** the portal vendor's cloud platform and relay, the billing SaaS platform, the payment processor, the email and file platform, the certified laboratory's portal, the state reporting portal, the integrator's own systems, and the cellular carrier.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Remote access portal vendor | Panel screens, setpoint commands, process history | Subscription terms; SOC 2 reviewed |
| Controls integrator | Remote support sessions; PLC program copies | Service agreement **with no security terms (gap)** |
| Billing SaaS vendor and payment processor | Customer accounts, usage, portal credentials; payments on the processor's page | Subscription terms; SOC 2 not yet requested (gap) |
| Certified laboratory | Sample results | Lab contract |
| State primacy agency | Monthly operating reports, notices, certifications | Regulatory |
| Anomaly alert feature (SYS-08) | Process data | **Click-through terms allow model training (gap; P10)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| PLC, HMI, analyzer, flow meter, alarm dialer (SYS-01) | OT, on premises | Owner-operator |
| Cellular router (SYS-02) | Network device | Owner-operator |
| Remote access portal and app (SYS-02, SYS-08) | SaaS | Owner-operator (tenant) |
| Billing SaaS (SYS-03); email and files (SYS-04) | SaaS | Owner-operator (tenant) |
| Laptop (SYS-05); phone (SYS-06); home router (SYS-07) | Endpoints and network | Owner-operator |

Model, firmware, and network address are not yet recorded for the panel components (CM-8 gap).

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 25 controls:
- Implemented: 5
- Partially implemented: 15
- Planned: 5

Inheritance: 1 fully inherited from the SaaS vendors (AU-2), 11 hybrid (vendor runs the mechanism, the owner configures or uses it), and 13 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); first inventory (CM-8) |
| Protect | Portal MFA (IA-2(1), gap); default passwords (IA-5, gap); integrator access (MA-4, AC-17); hand-off-auto switches and mechanical stroke cap |
| Detect | Process alarms through the dialer and anomaly alerts (SI-4); portal log review (AU-6, planned) |
| Respond | HMI remote-access runbook (IR-8); notice clocks (IR-6) |
| Recover | Manual operation; PLC program backup (CP-9, gap); restore steps (CP-10, planned) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the IT technician; tests on 2026-07-23. See P07.

## 11. Digital Identity Acceptance Statement
The portal can change treatment setpoints, so it needs the strongest sign-in the vendor offers: app-based MFA on every account, one account per person (2026-09-15). Email uses a text-message code today; the owner moves it to an authenticator app when the portal change is made. Customers use the billing vendor's portal and its identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **HMI:** human-machine interface (the touchscreen on the panel)
- **MFA:** multi-factor authentication
- **NPDWR:** national primary drinking water regulations (40 CFR Part 141)
- **PLC:** programmable logic controller
- **WSOP:** Water System Operations Profile

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-operator |
