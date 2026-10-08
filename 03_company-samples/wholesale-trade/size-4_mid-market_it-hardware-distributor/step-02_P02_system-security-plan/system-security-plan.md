# System Security Plan: Distribution Operations Platform (DOP)

**Organization:** Cris Santos Company, Inc. (PE-backed IT hardware and software wholesale distributor) | **Tier:** Mid-Market | **Vertical:** Wholesale Trade
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Distribution Operations Platform (**DOP**), identifier CSC-DOP-01. The DOP is the company's major system. It comprises SYS-01 to SYS-14 in `../00_company-facts.md`. The Federal Integration Enclave (SYS-09) is a subsystem with its own enclave SSP (version 1.0, 2025-11); this plan replaces that document's boundary and role sections and references its configuration detail.

## 2. System Overview
The DOP supports every process in the BIA (P05): order capture from resellers and federal channel customers, the reseller portal and order API, EDI, purchasing, receiving and authenticity inspection, fulfillment at DC-1 and DC-2, transportation, the commercial Integration Center, and the Federal Integration Lab (FIL). It serves 850 workforce members, about 9,600 reseller portal users, the MSSP, and the DC automation integrator.

The DOP also contains the company's **CMMC Level 2 assessment scope** under 32 CFR 170.19(c): the Federal Integration Enclave and the FIL, which hold the CUI that Prime A, Prime B, and Prime C provide, and the security protection assets that serve them.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | ERP: order-to-cash, procure-to-pay, inventory, finance | Vendor SaaS; SOC 2 Type 2 |
| SYS-02 | WMS with 420 RF handhelds | Company-managed in the workloads account (IaaS) |
| SYS-03 | Reseller portal and order API | Vendor SaaS; SOC 2 Type 2 |
| SYS-04 | EDI service | Vendor SaaS |
| SYS-05 | Transportation management system | Vendor SaaS |
| SYS-06 | Corporate identity provider (SSO, MFA, conditional access) | SaaS |
| SYS-07 | Corporate productivity suite | Vendor SaaS, commercial tier |
| SYS-08 | Cloud landing zone: security, shared services, workloads, data, and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-09 | Federal Integration Enclave: government-community productivity and identity tenant, enclave cloud account (virtual desktops, configuration build server, image repository) | Government community cloud (FedRAMP Moderate and High authorized services) |
| SYS-10 | Networks: HQ, DC-1, DC-2 on SD-WAN; warehouse Wi-Fi; FIL network | On-premises; SD-WAN managed service |
| SYS-11 | 880 laptops and desktops, 22 FIL workstations, 420 handhelds, 160 printers | Company-managed |
| SYS-12 | DC automation: conveyor, sortation, vertical lift controls | On-premises at DC-1; integrator-maintained |
| SYS-13 | Physical security: badges, 310 cameras, FIL cage | On-premises |
| SYS-14 | Security tooling: EDR, SIEM (MSSP), privileged access broker, vulnerability scanner | SaaS and cloud |

The forecasting platform (SYS-15), other AI tools (SYS-16), and third parties (SYS-17) connect as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the DOP |
|---|---|---|---|
| N42-R03 | DFARS Safeguarding Covered Defense Information and Cyber Incident Reporting | 48 CFR 252.204-7012 (Prime A, B, C subcontracts) | SP 800-171 Rev. 2 for every system that holds CUI; FedRAMP Moderate equivalency for cloud services holding CUI; 72-hour reporting; image preservation |
| N42-R02 | CMMC Program: Level 2 (C3PAO) requested by the primes from 2027-06-01 (suspended with CMMC Phase 2; still prepared for); Level 1 (Self) for the FCI stream | 32 CFR Part 170; DFARS 252.204-7021 | Assessment scope and asset categories (170.19); POA&M limits (170.21); annual affirmation (170.22) |
| N42-R04 | FAR Basic Safeguarding of Covered Contractor Information Systems | 48 CFR 52.204-21 | 15 safeguarding requirements for systems holding FCI (ERP, WMS, EDI, TMS, email) |
| N42-R05 | Section 889 covered telecommunications and video surveillance prohibition | 48 CFR 52.204-25 | Screening of products on federal orders and of the company's own systems; 1-business-day report |
| FAR | FASCSA orders prohibition | 48 CFR 52.204-30 | SAM.gov search for FASCSA orders; 3-business-day report |
| DFARS | Sources of Electronic Parts; Counterfeit Electronic Part Detection and Avoidance System | 48 CFR 252.246-7008 (all CUI subcontracts); 252.246-7007 (Prime A, through paragraph (e)) | Sourcing order, authenticity inspection, traceability, GIDEP reporting (SR controls) |
| DFARS | NIST SP 800-171 DoD Assessment requirements | 48 CFR 252.204-7019 and 252.204-7020 | Current SPRS score for each covered system |
| CUI | CUI Basic is categorized at no less than moderate confidentiality | 32 CFR 2002.14(g) | Sets the confidentiality floor in section 6 |
| N42-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) | Reasonable security for employee and reseller-contact personal information and accurate security statements to customers |
| State | State breach notification laws (Florida as the worked example) | Fla. Stat. 501.171 and other states' laws | Breach notification (P08) |
| Contract | Reseller agreements with 3 national resellers | Contract | SOC 2 Type 2 report on the Partner Commerce Platform (P09) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

Not applicable:
- **SEC cybersecurity disclosure (N42-R07):** the company is privately held.
- **CCPA/CPRA (N42-R08):** no California business today (counsel, 2026-06); revisit before the planned 2027 West Coast expansion.
- **CTPAT (N42-R06):** voluntary; membership under evaluation in 2027.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the DOP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High POA&M items in P07 meet their milestones; CUI is removed from the ERP and the commercial email tenant by 2026-11-30; the audit committee receives POA&M and CMMC readiness status each quarter; re-decision by 2027-09-30 or after a major change.
- **CMMC affirmation:** the Chief Operating Officer, as CMMC Affirming Official (32 CFR 170.22), will not affirm Level 2 compliance until every requirement that cannot be placed on a CMMC POA&M is met (P03).

### 4.3 System Operational Status
Operational. Major modifications planned:
- **CUI scope cleanup and enclave expansion** (Prime C onboarding into the enclave, ERP attachment block on federal order types, email purge, FIL print control), due 2026-11-30
- **DC-1 OT segmentation** with a remote access gateway and OT monitoring, due 2027-03-31
- **Privileged access broker extension** to ERP, WMS, and enclave tenant administrators, due 2027-01-31
- **SIEM onboarding** of ERP, WMS, portal, FIL firewall, and DC automation logs, due 2027-01-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the DOP; accepts Moderate risk; CMMC Affirming Official |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite and budget |
| Oversight | Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Program strategy | vCISO (part-time contractor) | Strategy, risk method, board reporting, SSP review |
| Security and IT lead | Director of Information Technology | Maintains this SSP; contingency planning; day-to-day control owner |
| Security operations and GRC | Security Manager and 2 security analysts | Monitoring oversight, vulnerability management, POA&M, GRC |
| CUI custodian | Federal Integration Lab Manager | Enclave and FIL access approvals; CUI handling |
| Federal contract compliance | Director of Federal Programs | SPRS entries, Section 889 and FASCSA screening, DIBNet reports |
| Supply chain risk lead | Vice President of Supply Chain | C-SCRM plan, approved supplier list, broker approvals |
| Product compliance | Director of Quality and Product Compliance | Counterfeit detection and avoidance system, inspection, GIDEP |
| Business unit owners | Vice President of Sales Operations; Director of Distribution Operations; Chief Financial Officer | Downtime procedures and access approvals for their systems |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP (External Service Provider, 32 CFR 170.19(c)(2)) | 24x7 EDR and SIEM monitoring, including enclave logs |

**Role overlaps.** The Director of Information Technology both runs IT and maintains this SSP, so the vCISO reviews the SSP and the co-sourced internal audit firm assesses the controls (P07). The Security Manager coordinates assessor access but does not select samples or rate findings.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| CUI configuration documents (prime network drawings, IP plans, configuration templates, hardened images) | Moderate | Moderate | Low | 32 CFR 2002.14(g) sets confidentiality at no less than moderate; altered configurations could harm DoD networks; FIL jobs tolerate days of delay (P05 MTD 72 h) |
| Goods acquisition, inventory control, and logistics (orders, purchase orders, inventory, shipments, FCI) | Moderate | Moderate | Moderate | Contract pricing and federal order data are sensitive; wrong inventory or ship-to data sends the wrong product; one shipping day is the MTD (P05) |
| Financial management (invoices, supplier bank details, credit) | Moderate | Moderate | Low | Bank-detail changes are a fraud target; billing tolerates 72 hours (P05) |
| Human resources (workforce identities, applicant data) | Moderate | Low | Low | Personal information of 850 employees in 12 states |
| System and network monitoring (security logs, Security Protection Data) | Moderate | Moderate | Low | Needed for DFARS 252.204-7012 investigations and image preservation |
| **DOP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High** for the FIL, because a tampered configuration could reach a DoD installation network. It stays Moderate because the primes verify configurations at installation and every FIL job uses a second-technician review, but the plan adds integrity-focused SR controls (SR-10, SR-11, SR-11(2)) to the baseline.

## 7. Authorization Boundary Description
The boundary is the DOP. Inside it, the CMMC Level 2 assessment scope uses the asset categories in 32 CFR 170.19(c).

| Asset category | Assets |
|---|---|
| CUI Assets | SYS-09 enclave (CUI email and library, virtual desktops, build server, image repository); SYS-10 FIL network; SYS-11 FIL workstations; **and, until cleanup closes, the places CUI was found:** SYS-01 ERP (37 orders), SYS-07 commercial email tenant (212 messages), and printed sheets at Integration Center benches |
| Security Protection Assets | Enclave identity tenant; SYS-14 SIEM tenant and EDR console (MSSP, External Service Provider); FIL firewall and VPN appliance; SYS-13 FIL cage badge system |
| Contractor Risk Managed Assets | None designated. The corporate environment is out of CMMC scope once the CUI cleanup is complete; enclave virtual desktop clients on corporate laptops are configured so CUI cannot leave the session |
| Specialized Assets | None in the CMMC scope. DC automation (SYS-12) is OT but holds no CUI and is outside the CMMC scope |
| Out of CMMC scope, inside this plan | SYS-02 WMS, SYS-03 portal, SYS-04 EDI, SYS-05 TMS, SYS-06 corporate IdP, SYS-08 landing zone, SYS-12 DC automation. These hold FCI and are in the FAR 52.204-21 and CMMC Level 1 scope |

- **Inside the boundary:** the company's ERP, portal, EDI, and TMS tenant configurations; the WMS and handhelds; the IdP tenant; all 5 landing zone accounts; the enclave tenant and account; site networks and SD-WAN edges; endpoints; DC automation; physical security systems; and the company's SIEM tenant, EDR console, and access broker.
- **Outside the boundary (external services, interconnected):** the SaaS, cloud, and government community cloud providers' platforms; the MSSP platform; primes' secure file exchanges; the forecasting platform and other AI vendors; carriers; the customs broker; the bank.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Prime A, Prime B, Prime C | Inbound CUI through the primes' secure file exchanges into the enclave; outbound configured equipment | CUI configuration documents | Subcontracts with DFARS 252.204-7012, -7019/-7020, 252.246-7008 (and -7007 for Prime A), FAR 52.204-21, -25, -30 |
| Federal channel customers (7), through SYS-04 EDI | Bidirectional | Purchase orders, ship notices, invoices (FCI) | Subcontract purchase orders with FAR 52.204-21, -25, -30 and DFARS 252.204-7021 (Level 1) |
| 140 trading partners (SYS-04) | Bidirectional | Purchase orders, ship notices, invoices | EDI trading partner agreements |
| Reseller portal and order API (SYS-03) | Bidirectional sync with the ERP | Catalog, contract pricing, orders, invoices | Portal vendor contract; SOC 2 Type 2 (P09) |
| Forecasting platform (SYS-15) | Outbound order history; inbound purchase orders | Order history, **including federal channel orders (FCI)** | Vendor terms; **no FAR 52.204-21 terms (gap, P10)** |
| TMS and carriers (SYS-05) | Outbound | Ship-to addresses (FCI for federal orders) | Vendor and carrier terms |
| MSSP (SYS-14) | Inbound logs; remote response actions | Security Protection Data, including enclave logs | MSSP contract; SOC 2 Type 2; **no customer responsibility matrix (gap, SA-9)** |
| DC automation integrator | Inbound remote maintenance | Control configurations | Service contract; **no security terms or interconnection terms (gap, CA-3)** |
| Bank | Outbound | Supplier payments | Bank agreement with dual approval |
| Customs broker | Bidirectional | Commercial invoices, entry data | Customs broker agreement |
| AI vendors (AI-002 to AI-005) | Varies | See P10 | Vendor terms (P10) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ERP tenant | SaaS | ERP vendor (SOC 2 Type 2; no FedRAMP authorization) | Chief Operating Officer |
| WMS application and database servers, standby replica | Cloud virtual machines and managed database | Workloads account | Director of Distribution Operations |
| Integration services (order APIs, middleware), file services | Cloud virtual machines and managed file shares | Workloads account | Director of Information Technology |
| Data warehouse | Managed database | Data account | Chief Financial Officer |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Director of Information Technology |
| Network hub, cloud firewall, VPN, log pipeline | Network and management services | Shared services account | Director of Information Technology |
| Organization guardrails, posture management, privileged access broker | Identity and policy services | Security account | Security Manager |
| Enclave tenant (CUI email and library, enclave identity) | Government community SaaS (FedRAMP High) | Government community cloud provider | Federal Integration Lab Manager |
| Enclave account (virtual desktops, build server, image repository, enclave vault) | Government community IaaS and PaaS (FedRAMP Moderate) | Government community cloud provider | Federal Integration Lab Manager |
| Portal, EDI, TMS tenants | SaaS | Vendors | Vice President of Sales Operations; Director of Distribution Operations |
| IdP tenant | SaaS | Identity vendor | Director of Information Technology |
| SD-WAN edges, firewalls, switches, Wi-Fi (3 sites); FIL firewall and VPN appliance | Network | HQ, DC-1, DC-2, FIL | Director of Information Technology |
| Laptops and desktops (880); FIL workstations (22); handhelds (420); printers (160) | Endpoint | All sites | Director of Information Technology |
| Conveyor and sortation controllers, 2 sorter control servers (unsupported OS), 2 operator workstations, vertical lift modules | OT | DC-1 | Director of Distribution Operations |
| Badge system, 310 cameras, recorders, FIL cage | Physical security | All sites | Director of Distribution Operations |
| SIEM tenant, EDR console, vulnerability scanner | SaaS | MSSP and security vendors | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The DOP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 117 controls** in `control-implementation.csv`. They cover every SP 800-53 control that implements the 110 SP 800-171 Rev. 2 requirements and the 15 FAR 52.204-21 requirements (taken from the P03 crosswalk), the SR controls that carry the DFARS 252.246-7007/-7008 and FAR 52.204-25/-30 duties (applied with NIST SP 800-161 Rev. 1), and the Moderate controls that treat the P01 risks (recovery, OT, privileged access).
- **Selected by tailoring (added):** PM-9 and PM-30. They are not in the Moderate baseline but are needed for the risk appetite (P01) and the C-SCRM strategy.
- **How the SR controls are applied.** SP 800-53 writes the SR controls for the components of an organization's own systems. As an author decision, the company also applies them to the products it distributes on federal orders, because those products become components of DoD systems.
- **Inherited without separate statements:** the remaining Moderate physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17 at provider sites) and platform-level SA and SC controls. They are inherited from the cloud, government community cloud, and SaaS providers and evidenced by FedRAMP packages or SOC 2 Type 2 reports (P04, P09).
- **Deferred:** other Moderate controls with no SP 800-171 or FAR mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software). Recorded as tailoring decisions and reviewed yearly.

**Status of the 117 documented controls:**
| Status | Count |
|---|---|
| Implemented | 42 |
| Partially implemented | 74 |
| Planned | 1 |
| Not applicable | 0 |

**Inheritance of the 117 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 79 | Company |
| Hybrid | 30 | Cloud and government community cloud providers, ERP and portal vendors, MSSP, SD-WAN provider |
| Common/Inherited | 8 | Identity vendors (AC-2(1), AC-7, IA-2(1), IA-2(2), IA-2(8)), cloud provider (CP-6), MSSP (AU-6(1)), cloud and SaaS providers (AU-8) |

The `regulatory_driver` column lists the SP 800-171 Rev. 2 requirements, FAR 52.204-21 paragraphs, and clauses each control implements. CSF 2.0 subcategories come from the official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference; the 19 controls with no entry in that reference are left blank rather than guessed.

**Relationship to SP 800-171 3.12.4.** SP 800-171 Rev. 2 requires a system security plan that describes how each requirement is implemented. This SSP, together with the requirement-level rows in P03 `gap-analysis.csv` (110 requirements, with current state and evidence), is that plan for the CMMC assessment scope.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the corporate IdP with a password and push MFA with number matching, under conditional access that checks device compliance. This is appropriate for the Moderate categorization.
- **Enclave users and all administrators.** The 64 enclave users and all 61 privileged accounts use phishing-resistant FIDO2 security keys.
- **Exceptions.** WMS handhelds use named badge-and-PIN sign-in without MFA (P07 IA-2(2); POAM-013), accepted until the handheld sign-in upgrade because handhelds hold no CUI. The 4 shared DC automation operator accounts are a gap (POAM-014).
- **Resellers.** Reseller users authenticate to the vendor portal with passwords; MFA is optional today and will be enforced for all accounts by 2027-01-31 (IA-8; POAM-026; P01 R-011).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); enclave SSP 1.0 (2025-11).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **CUI, FCI:** Controlled Unclassified Information; Federal Contract Information
- **DIBNet:** DoD's Defense Industrial Base network portal for cyber incident reports
- **DOP:** Distribution Operations Platform
- **ESP:** External Service Provider (32 CFR 170.4)
- **FASCSA:** Federal Acquisition Supply Chain Security Act
- **FIL:** Federal Integration Lab
- **GIDEP:** Government-Industry Data Exchange Program
- **MSSP:** managed security service provider
- **OT:** operational technology
- **SPRS:** Supplier Performance Risk System
- **TMS, WMS:** transportation management system; warehouse management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis; merges the enclave SSP 1.0 boundary | Director of Information Technology |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | Director of Information Technology |
