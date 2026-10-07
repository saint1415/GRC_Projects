# System Security Plan: Project Delivery and Payment Platform (PDPP)

**Organization:** Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) | **Tier:** Mid-Market | **Vertical:** Construction
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Project Delivery and Payment Platform (**PDPP**), identifier CSC-PDPP-01. It has one documented subsystem, the **CUI Project Enclave (CPE)**, identifier CSC-PDPP-01-CPE. The PDPP comprises SYS-01, SYS-02, SYS-04, SYS-05, SYS-06 (except the MBSS account), SYS-07, SYS-08, SYS-09, and SYS-12 in `../00_company-facts.md`.

This plan serves three purposes:
- the company's system security plan for its major system, on the NIST SP 800-53B Moderate baseline with tailoring;
- the **FCI scope** description for FAR 52.204-21 (corporate PDPP);
- the **NIST SP 800-171 Rev. 2 system security plan** required by requirement 3.12.4 for the CPE, which is the proposed CMMC Level 2 assessment scope (32 CFR 170.19(c)).

## 2. System Overview
The PDPP supports how the company wins, builds, bills, and pays for work: estimating and bid submission, drawings, RFIs, submittals, and daily logs for 22 active jobsites, monthly progress payment applications (pay apps) to owners (about $7.8 million a month), and payments to about 450 subcontractors and suppliers (about $5.2 million a month). It serves about 610 workforce accounts and about 2,600 external users of the project platform.

The CPE supports one contract, FC-4, the Army Corps of Engineers design-build project. It holds CUI-marked Government drawings and the A&E subcontractor's CUI design packages (covered defense information under DFARS 252.204-7012(a)).

**Major components:**
| ID | Component | Hosting and service model | Scope |
|---|---|---|---|
| SYS-01 | Construction project management platform (drawings, RFIs, submittals, daily logs, safety module, pay app workflow, subcontractor portal) | Commercial vendor SaaS; SOC 2 Type 2 | Corporate (FCI) |
| SYS-02 | Construction ERP (job cost, billing, accounts payable, vendor master, ACH files) | Commercial vendor SaaS; SOC 2 Type 2 | Corporate (FCI) |
| SYS-04 | Corporate identity provider (single sign-on, MFA, conditional access) | SaaS | Corporate |
| SYS-05 | Corporate productivity suite (email, files, chat) | Commercial SaaS | Corporate (FCI) |
| SYS-06 | Corporate cloud landing zone: security and identity, shared services, corporate workloads, and backup accounts | Commercial public cloud IaaS/PaaS, vendor-agnostic (P04) | Corporate (FCI) |
| SYS-07 | CUI Project Enclave: enclave identity tenant, CUI email and files, virtual desktops, 18 enclave laptops | Government-community cloud, FedRAMP authorized at Moderate or higher; CRM on file | CPE (CUI) |
| SYS-08 | Office, yard, and jobsite networks (SD-WAN; 22 jobsite cellular routers) | On-premises | Corporate |
| SYS-09 | Endpoints: 420 laptops and desktops, 380 smartphones, 150 rugged tablets, 12 commissioning laptops | Company-managed (40 tablets unmanaged) | Corporate; 26 FC-4 tablets hold CUI today (gap) |
| SYS-12 | SIEM and 24x7 MDR | MSSP-operated, commercial cloud | Corporate |

The payroll and HR system (SYS-03), bank portal (SYS-10), federal portals (SYS-14), and the AI estimating and bid assistant (AI-001) connect as external services (section 8). The MBSS platform (SYS-13) has its own boundary and is covered by the SOC 2 readiness work (P09).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the PDPP |
|---|---|---|---|
| N23-R01 | FAR 52.204-21 Basic Safeguarding | 48 CFR 52.204-21 (NOV 2021). In FC-1 to FC-4 | 15 basic safeguarding requirements for every system that holds FCI (corporate PDPP and CPE) |
| N23-R02 | FAR 52.204-25 Section 889 prohibition | 48 CFR 52.204-25 (NOV 2021). In FC-1 to FC-4 | No covered telecommunications or video surveillance equipment provided or used; 1-business-day reporting |
| N23-R03 | DFARS 252.204-7012 Safeguarding Covered Defense Information | 48 CFR 252.204-7012 (MAY 2024). In FC-3 and FC-4; triggered on FC-4 because CDI is held | NIST SP 800-171 on every covered contractor information system (7012(b)(2)(i)); FedRAMP Moderate equivalent cloud (b)(2)(ii)(D); 72-hour reporting (c); flowdown (m). Mapped in P03 G-001 to G-119 |
| N23-R03 | DFARS 252.204-7019 and 252.204-7020 | 48 CFR 252.204-7019, 252.204-7020. In FC-3 and FC-4 | Current NIST SP 800-171 DoD Assessment score in SPRS; subcontractor assessment checks |
| N23-R04 | CMMC Program and DFARS 252.204-7021 | 32 CFR Part 170; 48 CFR 252.204-7021 (NOV 2025) | Level 2 (C3PAO) expected for the follow-on MATOC (2027); scoping by asset category (170.19(c)) |
| Payment terms | FAR 52.232-5, 52.232-27, 52.232-33 | 48 CFR Part 52 | Progress payments; subcontractors paid within 7 days of receipt; EFT to the SAM bank account |
| Payroll | FAR 52.222-8 | 48 CFR 52.222-8 | Weekly certified payrolls; payroll records kept 3 years after the work |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Breach notification for employee personal information (P08) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **NISPOM (32 CFR Part 117):** no facility clearance and no classified information.
- **HIPAA and PCI DSS:** no PHI is held for clients; no card payments are accepted.
- **SEC cyber disclosure rules:** the company is privately held.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and on the day of the audit committee meeting. The CPE section replaces the 2025 enclave plan (v0.3, 2025-02-10), which did not describe field use of CUI.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the PDPP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** CUI removed from SYS-01 and unmanaged tablets by 2026-10-31; corrected SPRS score posted by 2026-09-30; High-risk POA&M items meet their milestones; the audit committee receives POA&M and CMMC readiness status each quarter; re-decision by 2027-09-30 or after a major change.
- **CMMC affirmation:** the CEO, as Affirming Official (32 CFR 170.22), will not affirm any CMMC status until the C3PAO assessment result supports it.

### 4.3 System Operational Status
Operational. Major modifications planned:
- FC-4 CUI document control moved fully into the CPE, with field access to CUI drawings only through enclave virtual desktops on managed tablets (due 2026-12-31)
- CPE logs onboarded to a monitoring service hosted in the government-community cloud (due 2027-01-31)
- Phishing-resistant MFA for Project Managers, accounting staff, and executives (due 2026-12-31)
- Jobsite router baseline and central management (due 2027-01-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the PDPP; accepts Moderate risk; approves policies |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High and Very High risk; approves the risk appetite; CMMC Affirming Official |
| Oversight | Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, risk appetite, board reporting, SSP review |
| Security lead and SSP owner | Security Manager | Day-to-day control owner; incident commander; owner of this plan and the POA&M |
| Security operations and GRC | 2 security analysts; GRC analyst | Monitoring liaison, vulnerability management; risk register, evidence, SPRS score calculation |
| Infrastructure | IT Director | Cloud landing zone, networks, endpoints, recovery |
| CUI custodian | FC-4 Project Executive | CUI intake, distribution list, printed CUI at the FC-4 jobsite |
| Contract compliance | Director of Contracts and Compliance | Flowdowns, SAM, SPRS, Section 889 and DIBNet reports |
| Payment controls | Chief Financial Officer; Controller | Vendor master, billing, bank portal |
| Field operations | Vice President of Operations | Jobsite physical security and field devices |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment. Operates no control |
| Monitoring | MSSP | 24x7 MDR and SIEM for the corporate environment (not the CPE) |

**Where roles overlap.** The Security Manager writes this plan and also runs the controls it describes. The vCISO reviews it, and the co-sourced internal audit firm tests it (P07), so the person who wrote a control statement does not assess it. The GRC analyst calculates the SPRS score; the internal audit firm reperformed the calculation in P07.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1, plus two company-defined types. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Facilities, fleet, and equipment management (drawings, submittals, daily logs; FCI) | Moderate | Moderate | Moderate | Federal facility details must stay non-public; wrong drawings cause rework and safety exposure; jobsites run about 24 hours on offline and printed sets (P05 MTD 24 h) |
| CUI facility drawings and design packages (company-defined; FC-4 covered defense information) | Moderate | Moderate | Low | CUI is protected at no less than Moderate confidentiality; FC-4 can work from printed CUI sets for a day (P05 BP-04) |
| Payments; collections and receivables (pay apps, vendor bank details) | Moderate | **High** | Moderate | One altered bank record can divert a whole progress payment, averaging about $1.2 million (P01 R-001, R-002); billing tolerates 48 hours in billing week (P05) |
| Compensation management (payroll, certified payrolls) | Moderate | Moderate | Moderate | Social Security numbers and bank data for 600 employees; weekly payroll deadlines |
| Client facility security details (company-defined: installed security system layouts and credentials during installation and warranty) | Moderate | Moderate | Low | Disclosure could help an intruder at a client site |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for incident review under DFARS 252.204-7012(c)(1)(i) |
| **PDPP category (high-water mark)** | **Moderate** | **High** | **Moderate** | |

**Baseline decision.** Payment integrity rates High, so a strict FIPS 200 reading points to the High baseline for the whole PDPP. The company applies the **NIST SP 800-53B Moderate baseline**, tailored, and adds targeted integrity controls instead of the full High baseline:
- separation of duties on vendor-master changes and payment release (AC-5);
- replay-resistant MFA for payment roles (IA-2(8));
- daily review of vendor-master changes and positive pay (SI-7);
- call-back verification of bank changes to a number already on file (POL-01).

The CEO and COO approved this tailoring decision on 2026-09-17. The CPE uses the same Moderate baseline, which is also the basis of the SP 800-171 requirements.

## 7. Authorization Boundary Description
### 7.1 Corporate PDPP (FCI scope)
**Inside:** the SYS-01 and SYS-02 tenant configurations and roles; the identity provider and productivity suite tenants; the 4 corporate cloud accounts (security and identity, shared services, corporate workloads, backup); headquarters, regional office, and yard networks and the 22 jobsite cellular routers; 420 laptops and desktops, 380 smartphones, 150 rugged tablets, and 12 commissioning laptops; the company's SIEM tenant and use cases.

**Outside (external services, interconnected):** the vendors' platforms and the commercial cloud provider's infrastructure; payroll and HR (SYS-03); the bank portal (SYS-10); federal portals (SYS-14); the AI estimating and bid assistant (AI-001); the MSSP's platform; the MBSS account (SYS-13, separate boundary).

**Out of the FCI scope:** equipment telematics and jobsite technology services (SYS-11, no FCI by policy); client-installed security and building systems (client-owned); personal email and personal devices (prohibited for FCI and CUI by POL-04).

### 7.2 CUI Project Enclave (CMMC Level 2 scope)
The CPE is a separate tenant in a government-community cloud. There is no network path between corporate systems and the CPE. Users reach the enclave only through its virtual desktop gateway with phishing-resistant MFA, from enclave laptops or (from 2026-12) from managed tablets configured as virtual desktop clients only.

Asset categories under 32 CFR 170.19(c)(1), Table 3:

| Asset category | Assets (target state) | Treatment |
|---|---|---|
| CUI Assets | CPE collaboration suite (CUI email and files), virtual desktop pool, 18 enclave laptops | Assessed against all 110 requirements |
| Security Protection Assets | Enclave identity tenant; enclave endpoint protection and device management; CPE native log store; (planned) government-community cloud monitoring service | Assessed against the requirements relevant to the capability provided |
| Contractor Risk Managed Assets | None | |
| Specialized Assets | None. The company holds no Government-furnished equipment or OT on FC-4 | |
| Out-of-Scope Assets | Corporate PDPP (logically separated tenants); managed tablets configured as virtual desktop clients that allow only keyboard, video, and mouse traffic | Justification recorded; tablets qualify under the Table 3 virtual desktop client note |

**External Service Providers (32 CFR 170.19(c)(2)).** The government-community cloud provider stores and processes CUI and must meet FedRAMP requirements under DFARS 252.204-7012; its CRM is on file and mapped in P04. The MSSP does not handle CUI or Security Protection Data for the CPE today. If the planned monitoring service for the CPE is operated by the MSSP, its services enter the scope as Security Protection Assets and its CRM must be documented here first (P03 G-127).

**Known exceptions to fix before any CMMC assessment.** Today CUI is also in SYS-01 (1,140 items), on 26 FC-4 tablets, and in printed form in the FC-4 trailer. Those locations are CUI Assets in fact and fail several requirements (P03 G-003, G-019, G-064 to G-068, G-111). The target state above is valid only after the remediation in P03 section 4 is complete and verified.

The diagrams are in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Owners (private, state and local, federal) | Outbound pay apps; inbound payments | Pay apps, lien waivers, remittance details | Prime contracts. **Private owners have no agreed out-of-band method for remittance changes (gap 4)** |
| Subcontractors and suppliers (about 450) | Bidirectional via SYS-01 and email | Drawings (FCI), invoices, bank details | Subcontracts with FAR 52.204-21 and 52.204-25 substance (2025 templates) |
| FC-4 A&E subcontractor | Bidirectional through CPE guest accounts (8 users) | CUI design packages | Subcontract with DFARS 252.204-7012 |
| FC-4 trade subcontractors (14) | Outbound CUI drawings | CUI | **No DFARS 252.204-7012 flowdown (gap 3); CUI sent through SYS-01 (gap 1)** |
| Army Corps of Engineers | Bidirectional | CUI drawings, submittals, invoices | FC-4 contract |
| Payroll and HR SaaS (SYS-03) | Outbound hours; inbound certified payroll reports | Personal information, payroll | Vendor contract; SOC 2 on file |
| Bank portal (SYS-10) | Outbound ACH files from SYS-02 | Payment instructions | Treasury agreement; dual approval |
| AI estimating and bid assistant (AI-001) | Outbound bid documents; inbound estimates | FCI (federal bids), pricing | Enterprise terms since 2026-02 (no model training on customer data); CUI prohibited (P10) |
| Federal portals (SYS-14) | Bidirectional | SAM registration and EFT data, SPRS, invoices, DIBNet reports | Government terms |
| Design firms (file-transfer portal) | Bidirectional | Models and drawings (non-CUI) | Project agreements; **no security terms for 31 firms (CA-3)** |
| MSSP | Inbound logs; remote response actions | Corporate security logs | MSSP contract; SOC 2 Type 2 |

**CUI data flow (target).** Government and A&E CUI arrives in the CPE (email or file share from allow-listed domains). The FC-4 team works on it in enclave virtual desktops. Trade subcontractors receive CUI only through enclave guest accounts or their own systems, after flowdown and a verified SPRS score. Field crews view CUI drawings through the virtual desktop on managed tablets or use numbered printed sets from the locked plan cabinet. CUI never enters SYS-01, SYS-05, or personal accounts.

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Project management platform tenant | SaaS | Vendor | Vice President of Operations |
| ERP and accounting tenant | SaaS | Vendor | Chief Financial Officer |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Productivity suite tenant | SaaS | Productivity vendor | IT Director |
| Estimating database | Managed database | Corporate workloads account | Director of Preconstruction |
| BIM/CAD file servers and GPU virtual desktops | Virtual machines and block storage | Corporate workloads account | Director of VDC |
| File-transfer portal | Virtual machine, internet-facing | Corporate workloads account, public subnet | IT Director |
| Data warehouse | Managed database | Corporate workloads account | Chief Financial Officer |
| Network hub, VPN gateways, privileged access broker, log forwarding | Network and management services | Shared services account | IT Director |
| Cloud identity federation and guardrails | Identity and policy services | Security and identity account | Security Manager |
| Backup vault | Backup service, write-once retention | Backup account, second region | IT Director |
| CPE identity tenant | SaaS | Government-community cloud | Security Manager |
| CPE collaboration suite | SaaS | Government-community cloud | FC-4 Project Executive |
| CPE virtual desktop pool (40 sessions) | Virtual desktop service | Government-community cloud | IT Director |
| Enclave laptops (18) | Endpoint, FIPS mode | Headquarters FC-4 project office and FC-4 jobsite | IT Director |
| SD-WAN edges, firewalls, switches, Wi-Fi | Network | Headquarters, regional office, yard | IT Director |
| Jobsite cellular routers (22) | Network | Jobsite trailers | IT Director |
| Laptops and desktops (420), smartphones (380) | Endpoint (managed) | Offices and field | IT Director |
| Rugged tablets (150: 110 managed, 40 not) | Endpoint | Jobsites | Vice President of Operations |
| Commissioning laptops (12) | Endpoint (managed) | Technology and Security Systems group | Director of Technology and Security Systems |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Baseline, tailoring, and implementation status
**Baseline and tailoring.** The PDPP uses the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 124 controls** in `control-implementation.csv`. They include the SP 800-53 controls that NIST's SP 800-171 Rev. 3 tailoring maps to the SP 800-171 Rev. 2 requirements (through the Rev. 2 to Rev. 3 change analysis, an author route), the "-1" policy controls, the payment integrity controls in section 6, and controls for risks in P01 (contingency, interconnections, supply chain, Section 889). The `scope` column shows whether each control covers the corporate PDPP, the CPE, or both.
- **Selected by tailoring (added, not in the Moderate baseline):** PM-1, PM-2, and PM-9, for the program plan, the program lead, and the risk management strategy.
- **Inherited without separate statements:** the providers' physical and environmental controls for their data centers (for example PE-9 to PE-17) and platform-level SA and SC controls, evidenced by SOC 2 Type 2 reports (commercial providers) and the FedRAMP authorization and CRM (government-community cloud provider).
- **Deferred:** other Moderate controls with no SP 800-171 mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software for sale). They are recorded as tailoring decisions and reviewed yearly.

**Requirement-level statements for the CPE.** The SP 800-171 Rev. 2 implementation description for each of the 110 requirements is the `current_state` column of P03 `gap-analysis.csv` (G-001 to G-110), maintained as part of this plan and updated at each POA&M milestone.

**Status of the 124 documented controls:**
| Status | Count |
|---|---|
| Implemented | 58 |
| Partially implemented | 64 |
| Planned | 2 |
| Not applicable | 0 |

**Scope of the 124 documented controls:**
| Scope | Count |
|---|---|
| Corporate PDPP and CPE | 102 |
| CPE only | 16 |
| Corporate PDPP (FCI scope) only | 6 |

**Inheritance of the 124 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 83 | Company |
| Hybrid | 30 | Government-community cloud provider (16), MSSP (13), identity provider vendor (6), commercial cloud provider (5), and one each for the ERP vendor, project platform vendor, and destruction vendor (a control can name more than one provider) |
| Common/Inherited | 11 | Government-community cloud provider (for example AC-12, SC-12), identity provider vendor (AC-7, IA-2(1)), commercial cloud provider (CP-6), MSSP (AU-3, AU-9) |

The Partially implemented and Planned statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. Most are partial because a control works in the corporate environment or the CPE, but not at the FC-4 jobsite or on field devices.

**CSF 2.0 mapping.** The `csf2_subcategories` column uses NIST's CSF 2.0 to SP 800-53 Rev. 5 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`) at the base-control level. Where NIST lists no subcategory (AC-11, AC-12, MA-2, MA-4, PE-8, SA-22), the mapping is the author's.

### 10.2 Control assessment status and score
- The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`).
- Gap analysis with the recalculated score under 32 CFR 170.24: see P03. The 2025 SPRS entry of 71 (CPE scope, posted 2025-02-14) is not accurate and will be corrected by 2026-09-30.

## 11. Digital Identity Acceptance Statement
- **CPE users and all administrators** authenticate with phishing-resistant FIDO2 authenticators. This meets the CPE's need given CUI and remote access through the virtual desktop gateway.
- **Corporate workforce** users authenticate through SYS-04 with a password and push MFA with number matching, under conditional access that checks device compliance and sign-in risk. This is accepted for general users until 2026-12-31.
- **Payment roles** (Project Managers, billing, accounts payable, Controller, CFO) and executives are not adequately protected by push MFA, because an adversary-in-the-middle phishing page can relay the push and steal the session (P01 R-001). They move to phishing-resistant authenticators by 2026-12-31.
- **External users** of SYS-01 (about 2,600) authenticate with the vendor's sign-in and optional MFA, governed by the vendor and outside this boundary. Project permissions limit each external user to assigned projects. A&E guest users in the CPE use the enclave's phishing-resistant MFA.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis, SPRS score, and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **A&E:** architecture and engineering (the FC-4 design subcontractor)
- **CDI:** covered defense information (DFARS 252.204-7012(a))
- **CMMC:** Cybersecurity Maturity Model Certification
- **CPE:** CUI Project Enclave
- **CRM:** customer responsibility matrix
- **CUI:** Controlled Unclassified Information
- **EFT:** electronic funds transfer
- **FCI:** Federal Contract Information (FAR 52.204-21(a))
- **MATOC:** multiple-award task order contract
- **MBSS:** Managed Building Systems Services
- **MDR:** managed detection and response
- **MSSP:** managed security service provider
- **Pay app:** monthly progress payment application
- **PDPP:** Project Delivery and Payment Platform
- **POA&M:** plan of action and milestones
- **SAM:** System for Award Management
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.3 | 2025-02-10 | Enclave-only plan written for the FC-4 proposal and the 2025 SPRS score | IT Director |
| 0.9 | 2026-07-31 | Full PDPP plan drafted from the risk assessment and gap analysis | Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; CPE target scope and asset categories added; approved by the Chief Operating Officer | Security Manager |
