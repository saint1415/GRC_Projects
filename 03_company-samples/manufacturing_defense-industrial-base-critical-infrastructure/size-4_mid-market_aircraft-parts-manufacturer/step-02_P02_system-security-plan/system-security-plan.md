# System Security Plan: CUI Engineering Enclave (CEE)

**Organization:** Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) | **Tier:** Mid-Market | **Vertical:** Defense Industrial Base
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 4.0, 2026-09-17 (replaces v3.0 of 2025-05-30)
**Requirement set:** NIST SP 800-171 Rev. 2 (110 requirements), as required by DFARS 252.204-7012(b)(2) and CMMC Level 2 (32 CFR 170.14(c)(3)); SP 800-53 Rev. 5 Moderate baseline used for control design, with tailoring

## 1. System Name and Identifier
CUI Engineering Enclave (**CEE**), identifier CSC-CEE-01. The CEE is the company's major system. It comprises SYS-01 to SYS-08, the company side of SYS-12, and the MSSP services in SYS-13 in `../00_company-facts.md`. This SSP satisfies SP 800-171 requirement 3.12.4 and is the SSP named in SPRS submissions under DFARS 252.204-7019 and 252.204-7020.

## 2. System Overview
The CEE is where the company receives, creates, stores, and uses controlled technical information (CTI) for its DoD subcontracts and the controlled technical data of its commercial customers: drawings, 3D models, specifications, NC programs, additive build files, test procedures, and the travelers and inspection records built from them. It supports engineering, manufacturing engineering, quality, testing, the services line, and shop-floor production at both plants. About 290 named users hold enclave accounts; about 500 production workers see CUI through MES terminals and printed drawings.

**Major components:**
| ID | Component | Hosting and service model | CMMC asset category |
|---|---|---|---|
| SYS-01 | Enclave identity provider (single sign-on, MFA, device compliance) | Government-community cloud SaaS | Security Protection Asset |
| SYS-02 | Enclave collaboration suite (CUI email, file storage, chat) | Government-community cloud SaaS | CUI Asset |
| SYS-03 | 4-account landing zone: security and identity, shared services (network hub, VPN gateways, virtual desktops, MFT gateway), workloads (PLM, CAD license servers, build preparation, test data repository), backup | Government-community cloud IaaS and PaaS (P04) | CUI Assets and Security Protection Assets |
| SYS-04 | CAD/PLM, about 165,000 controlled documents | CAD on SYS-05; PLM in SYS-03 | CUI Asset |
| SYS-05 | 120 CAD workstations and 110 enclave laptops | Company-managed | CUI Assets |
| SYS-06 | MES and DNC at Plant 1 (40 terminals) and Plant 2 (20 terminals) | On-premises | CUI Assets |
| SYS-07 | 90 CNC machines, 12 CMMs, 6 additive printers, 6 test stands, machine-vision cell | On-premises | Specialized Assets |
| SYS-08 | Plant enclave networks, enclave firewalls, SD-WAN, site-to-cloud VPN | On-premises and provider gateways | Security Protection Assets |
| SYS-12 (company side) | MFT gateway, VPN and SD-WAN tunnels, virtual desktop access to the Prime A portal | Mixed | CUI Assets |
| SYS-13 | SIEM and 24x7 managed detection and response | MSSP, government-community cloud region | Security Protection Assets (External Service Provider) |

The cloud services are described by service category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the CEE |
|---|---|---|---|
| C-DIB-R01 | DFARS 252.204-7012 (MAY 2024) | 48 CFR 252.204-7012 | SP 800-171 on covered contractor information systems; FedRAMP Moderate-equivalent cloud; 72-hour reporting; malware to DC3; 90-day image preservation; flowdown |
| C-DIB-R02 | CMMC Program and DFARS 252.204-7021 (NOV 2025) | 32 CFR Part 170; 48 CFR 252.204-7021 | Level 2 (C3PAO) status needed for prime solicitations from Phase 2 (2026-11-10); scoping per 170.19(c), including External Service Providers per 170.19(c)(2); scoring per 170.24; POA&M limits per 170.21; affirmation per 170.22 |
| C-DIB-R03 | DFARS 252.204-7019 and 252.204-7020 (NOV 2023) | 48 CFR 252.204-7019, 252.204-7020 | Current SP 800-171 DoD Assessment score in SPRS; Government assessment access; subcontractor assessments |
| C-DIB-R04 | FAR 52.204-21 (NOV 2021) | 48 CFR 52.204-21 | Basic safeguarding for FCI (also on corporate systems and ERP outside this boundary) |
| C-DIB-R05 | ITAR | 22 CFR Parts 120-130 | Release of technical data to foreign persons is an export (22 CFR 120.56); U.S.-person access; encrypted-data carve-out conditions (22 CFR 120.54(a)(5)) |
| C-DIB-R06 | EAR | 15 CFR Parts 730-774 | Same principles for EAR-controlled technology on commercial parts (15 CFR 734.18(a)(5)) |
| CUI program | CUI Basic safeguarding | 32 CFR 2002.14 | CUI Basic protected at no less than moderate confidentiality (2002.14(a)(3)) |
| Contract | Additive and engineering services agreements | Contract | Confidentiality and turnaround commitments; SOC 2 Type 2 report by 2027-12-31 (P09) |
| Internal | Security policies POL-01 to POL-05 and the standards index | P06 | Policy basis for every control |

Not applicable:
- **NISPOM (C-DIB-R07, 32 CFR Part 117):** no facility clearance and no classified information.
- **CIRCIA (6 U.S.C. 681b):** the final rule is not published; nothing is required yet.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07). The Chief Executive Officer, as CMMC Affirming Official, reviewed it the same day. It was presented to the audit committee on 2026-09-17.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no authorization to operate. The equivalent internal decision:
- **Decision:** continued operation of the CEE accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; Plant 2 integration (separate network, named MES accounts, replacement servers) must be complete before the C3PAO assessment; the audit committee receives POA&M status each quarter.
- **External validation:** the CMMC Level 2 certification assessment, target window 2027-03-08 to 2027-03-19.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Plant 2 enclave firewall and shop-floor VLANs (due 2027-01-31)
- Plant 2 MES and DNC replacement with named sign-in through SYS-01 (due 2027-01-31)
- SIEM onboarding of MES, DNC, OT gateways, and Plant 2 firewalls, plus passive OT monitoring (due 2027-01-31)
- DNC serial gateway for the 8 USB-loaded CNC machines (due 2027-01-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the CEE; accepts Moderate risk; executive sponsor |
| Risk acceptor and CMMC Affirming Official | Chief Executive Officer | High and Very High risk acceptance; SPRS affirmations (32 CFR 170.22) |
| Oversight | Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Program strategy | vCISO (part-time contractor) | Strategy, risk appetite, board reporting, SSP review |
| Security lead | Security Manager | SSP and POA&M owner; incident commander; MSSP liaison |
| Security operations and GRC | 2 security analysts; GRC analyst | Monitoring with the MSSP; vulnerability management; evidence, risk register, SPRS score calculation |
| Infrastructure and recovery | IT Director | Landing zone, networks, backups, recovery |
| OT owner | Manufacturing Systems Manager | MES, DNC, CNC, CMM, additive, and test lab connectivity |
| CUI data owner | Director of Engineering | Decides what is CUI; approves access to engineering data |
| Printed CUI owner | Director of Quality | Drawing distribution, travelers, shop-floor document control |
| Contracts and export compliance | Director of Trade Compliance and Contracts (ITAR Empowered Official) | Flowdowns, SPRS submissions, DIBNet reporting, technology control plan |
| Plant owners | Vice President of Operations; Plant 1 and Plant 2 Managers | Shop-floor practices, visitor escort, production recovery |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring (ESP) | MSSP | 24x7 detection and response; SIEM |

**Where roles overlap.** The Security Manager both operates controls and owns the SSP. The independent check is the co-sourced internal audit firm, which selected samples and rated findings in P07 without operating any control, and the C3PAO assessment that follows.

## 6. System Information Types and System Categorization
Information types are from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199. CUI Basic cannot be protected below moderate confidentiality (32 CFR 2002.14(a)(3)).

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Controlled technical information (drawings, models, NC programs, build files, test procedures) | Moderate | Moderate | Moderate | Disclosure harms defense programs and violates export controls; a wrong dimension or program produces nonconforming flight parts; an outage stops production (P05 MTD 24 h) |
| Production, quality, and test records | Moderate | Moderate | Moderate | Records prove conformance to primes; shipments stop without them (P05 BP-03 MTD 24 h) |
| Services customer technical data | Moderate | Moderate | Low | Contractual confidentiality; turnaround can slip for 48 hours (P05 BP-08) |
| Identity and security data (accounts, logs) | Moderate | Moderate | Moderate | Protects the enclave itself; logs support DFARS preservation |
| **CEE category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Integrity was considered for High.** A silently altered drawing, NC program, or test result could lead to a flight safety event. The team kept integrity at Moderate because engineering release requires checker sign-off against the source model, first article inspection catches dimensional errors before production, and PLM keeps revision history. To compensate, the tailoring adds change control and revision checks on shop-floor systems (CM-3, CM-5) and a revision check before any restored program is released (P05).

## 7. Authorization Boundary Description
The boundary follows the CMMC Level 2 asset categories in 32 CFR 170.19(c)(1):

| Category | Assets in the CEE | Treatment |
|---|---|---|
| CUI Assets | SYS-02; SYS-03 workloads and backup accounts, virtual desktops, MFT gateway; SYS-04; SYS-05; SYS-06 at both plants; printed drawings, travelers, and test reports; company side of SYS-12 | Assessed against all 110 requirements |
| Security Protection Assets | SYS-01; SYS-03 security account and log pipeline; SYS-08 firewalls, VLAN switches, SD-WAN appliances, VPN gateways; EDR console; key management; SYS-13 MSSP services | Assessed against the requirements relevant to their function |
| Specialized Assets | SYS-07: 90 CNC machines, 12 CMMs, 6 additive printers, 6 test stands, machine-vision cell (operational technology and test equipment) | Inventoried, shown on the diagram, managed under risk-based practices (section 9); not assessed against other requirements |
| Contractor Risk Managed Assets | None designated | Not used |
| Out-of-Scope Assets | SYS-09 corporate network and endpoints; SYS-10 ERP (attachments disabled; drawing numbers only); SYS-11 payroll, HR, and applicant tracking | Separated by the enclave firewalls. **Exception at fieldwork:** the Plant 2 corporate segment is not separated from the Plant 2 shop floor, so it cannot be treated as Out-of-Scope until the Plant 2 firewall is in place (2027-01-31) |
| Flows under review | AI-003 predictive maintenance gateway on the Plant 1 shop-floor VLAN sending telemetry to a vendor commercial cloud; AI-001 assistant pilot in SYS-02; AI-004 corporate assistant receiving CUI text | Gateway to be moved to an OT DMZ with program names removed (2026-11-30); AI-001 off until boundary confirmation; AI-004 blocked for engineering content (P10) |

**External Service Providers (32 CFR 170.19(c)(2)).**
| ESP | Is it a CSP? | Handles | Treatment | CRM |
|---|---|---|---|---|
| Government-community cloud provider | Yes | CUI | Must meet the FedRAMP requirements in DFARS 252.204-7012; offering is FedRAMP authorized at Moderate or higher (Marketplace checked 2026-07-08) | On file; referenced here as 32 CFR 170.17(c)(5)(iii) requires |
| MSSP (SIEM and managed detection) | Service is hosted by the MSSP in a government-community cloud region | Security Protection Data | In the assessment scope; assessed as Security Protection Assets | **Not yet provided (gap; P03 G-128)** |

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Path | Agreement |
|---|---|---|---|---|
| Prime A supplier portal | Bidirectional | Drawings, models, quality data | Browser from enclave virtual desktops (prime-hosted) | Subcontract (DFARS 252.204-7012 flowed down) |
| Prime B and Prime C | Bidirectional | Drawings, models, NC programs, test procedures | MFT gateway (FIPS mode) | Subcontracts (DFARS 252.204-7012 flowed down) |
| Services customers (3) | Bidirectional | CAD and build files, build packages, reports | MFT gateway, per-customer folders | Services agreements with confidentiality terms |
| Suppliers and outside processors (22) | Outbound | Drawings needed for the process | MFT gateway; sealed paper copies with parts | Purchase orders. **9 without current DFARS terms (gap)** |
| Plant 1 and Plant 2 to cloud | Bidirectional | All CEE traffic from the plants | Site-to-cloud VPN (FIPS mode) | Internal |
| Plant 1 to Plant 2 | Bidirectional | MES data, NC programs | SD-WAN tunnel. **Plant 2 appliance in non-FIPS mode (gap)** | Internal |
| MSSP | Inbound logs; remote response actions | Security Protection Data | Log forwarders over TLS | MSSP contract; CRM pending |
| ERP (SYS-10) | Outbound from ERP to MES | Work order numbers, quantities, due dates (no drawings) | Scheduled file drop to MES | Internal |
| Predictive maintenance vendor (AI-003) | Outbound | Spindle and alarm telemetry with active program names | Gateway on Plant 1 shop-floor VLAN. **Not authorized (gap)** | Vendor subscription terms |
| Public generative AI services | Blocked | None allowed | Web filter | Prohibited (POL-05) |

## 9. System Component Inventory
| Component | Type | Location or provider | CMMC category | Owner |
|---|---|---|---|---|
| Identity provider tenant (318 accounts) | SaaS | Government-community cloud | Security Protection Asset | Security Manager |
| Collaboration suite tenant | SaaS | Government-community cloud | CUI Asset | IT Director |
| Security and identity account (guardrails, posture management, key management) | IaaS/PaaS | Landing zone | Security Protection Assets | Security Manager |
| Shared services account (hub, firewall, VPN gateways, virtual desktops for 120 sessions, MFT gateway, access broker, log pipeline) | IaaS/PaaS | Landing zone | CUI Assets and Security Protection Assets | IT Director |
| Workloads account (PLM application and database, CAD license servers, build preparation server, test data repository) | IaaS/PaaS | Landing zone | CUI Assets | Director of Engineering |
| Backup account (write-once vault, second region) | PaaS | Landing zone | CUI Asset | IT Director |
| CAD workstations (120), enclave laptops (110) | Endpoints | Engineering center; mobile | CUI Assets | IT Director |
| Plant 1 MES and DNC servers, 40 terminals | On-premises | Plant 1 shop-floor VLAN | CUI Assets | Manufacturing Systems Manager |
| Plant 2 MES and DNC servers (unsupported operating system), 20 terminals | On-premises | Plant 2 (flat network) | CUI Assets | Manufacturing Systems Manager |
| CNC machines (64 at Plant 1, 26 at Plant 2; 8 USB-loaded), CMMs (12), additive printers (6), test stands (6), vision cell | Operational technology | Both plants | Specialized Assets | Manufacturing Systems Manager |
| Enclave firewalls, VLAN switches, SD-WAN appliances | Network | Both plants | Security Protection Assets | IT Director |
| Shop-floor printers (6) | Output devices | Both plants (Plant 2 printer in an open aisle) | CUI Assets | Director of Quality |
| Printed drawings, travelers, test reports | Paper media | Cells, inspection rooms, test lab, shipping | CUI (media) | Director of Quality |
| SIEM and EDR console | ESP service | MSSP | Security Protection Assets | Security Manager |

**Specialized Asset treatment (SP 800-171 3.4.1; DFARS 252.204-7012(b)(3)).** CNC controllers, additive printers, CMMs, and test stand data acquisition PCs run vendor-embedded or vendor-locked software the company cannot patch or harden. Compensating measures: shop-floor VLANs with no internet route (Plant 2 after 2027-01-31); programs accepted only from DNC (82 machines) or, until 2027-01-31, from labeled and inventoried USB drives (8 machines); vendor remote support only through the company access broker (the additive printer vendor moves by 2026-10-31); inventory and diagram entries; passive network monitoring from 2027-01-31.

**Unsupported servers (SA-22).** The Plant 2 MES and DNC servers run an operating system past end of vendor support. Until replacement on 2027-01-31: EDR on a supported legacy agent, remote desktop and legacy file sharing closed (2026-11-30), access only from the Plant 2 shop-floor VLAN, and daily encrypted backups to the cloud backup account (2026-11-30).

**Cryptographic modules (SC-13; SP 800-171 3.13.11).**
| Path or store | Mechanism | FIPS validation |
|---|---|---|
| Cloud services (suite, identity, storage, key management, backup) | Provider-managed | Confirmed in the provider CRM |
| Virtual desktop gateway and MFT gateway | TLS 1.2 or higher; SSH | Confirmed: gateways run in FIPS mode |
| Site-to-cloud VPN from both plants | IPsec | Confirmed: firewall images run in FIPS mode |
| SD-WAN tunnel between the plants | IPsec | **Not confirmed: Plant 2 appliance in non-FIPS mode (fix by 2026-11-30)** |
| Enclave laptops and inventoried USB drives | Full-disk and hardware encryption | Confirmed (module certificates on file) |
| Plant 2 MES disks and local backups | None | **Not encrypted (fix by 2027-01-31)** |

## 10. Control Implementation Details
### 10.1 Baseline, tailoring, and implementation status
**Requirement set.** The binding requirement set is the 110 SP 800-171 Rev. 2 requirements. Each requirement's implementation statement is in `sp800-171-requirement-statements.csv` (110 rows, linked to the gap analysis in P03).

**Baseline and tailoring.** Controls are designed from the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 158 controls** in `control-implementation.csv`:
  - 120 controls and enhancements that NIST's SP 800-171 Rev. 3 CUI overlay maps to the 110 requirements (through the Rev. 2 to Rev. 3 change analysis);
  - 18 policy and procedure controls (the "-1" control in each family);
  - 20 controls added for this company's risks: contingency (CP-2, CP-4, CP-6, CP-10), inventory and data location (CM-8, CM-12), interconnections and authorization (CA-3, CA-6), supply chain (SA-4, SA-9, SR-2, SR-3), unsupported components (SA-22), incident plan (IR-8), maintenance (MA-2), rules of behavior and architecture (PL-4, PL-8), and program management.
- **Selected by tailoring (added, not in the Moderate baseline):** PM-1, PM-2, and PM-9, for the program plan, the designated program lead, and the risk management strategy.
- **Inherited without separate statements:** the provider's physical and environmental controls for its data centers (for example PE-9 to PE-17 for cloud facilities) and platform-level SA and SC controls, evidenced by the FedRAMP authorization and the CRM.
- **Deferred:** other Moderate controls with no SP 800-171 mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software for sale). They are recorded as tailoring decisions and reviewed yearly.

**By requirement** (`sp800-171-requirement-statements.csv`, 110 rows):
| Status | Count |
|---|---|
| Implemented | 64 |
| Partially implemented | 43 |
| Planned | 2 |
| Not applicable | 1 (3.13.14, no VoIP in the boundary) |

**By SP 800-53 control** (`control-implementation.csv`, 158 rows):
| Status | Count |
|---|---|
| Implemented | 86 |
| Partially implemented | 69 |
| Planned | 3 |

**Inheritance of the 158 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 99 | Company |
| Hybrid | 53 | Government-community cloud provider (37), MSSP (15), destruction vendor (1) |
| Common/Inherited | 6 | Government-community cloud provider (AC-12, AC-17(2), IA-2(8), SC-4, SC-23, CP-6) |

Hybrid and inherited statements rely on the provider's CRM and FedRAMP authorization package, and on the MSSP contract until its CRM is received. The Partially implemented statements trace to the 14 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. Most are partial because a control works in the cloud and at Plant 1 but not yet at Plant 2.

### 10.2 Assessment status and score
- Control assessment 2026-08-03 to 2026-08-21 by the co-sourced internal audit firm: see P07.
- Gap analysis: see P03. Recalculated score under 32 CFR 170.24 for the full scope (both plants): **-44**. For the cloud and Plant 1 alone it would be 40. The 2025 SPRS entry of 74 (Plant 1 scope) is withdrawn and will be corrected by 2026-09-30.
- Enduring exceptions: CNC, additive, CMM, and test stand controller patching and hardening (Specialized Assets, section 9).

## 11. Digital Identity Acceptance Statement
- **Enclave users** authenticate to SYS-01 with a password and an app-based or phishing-resistant second factor on a compliant enrolled device. Given Moderate confidentiality and remote access to CUI, this meets SP 800-171 3.5.3 for network access. Phishing-resistant authenticators for all engineers are planned by 2027-01-31 (P01 R-002).
- **Administrators** use hardware security keys and just-in-time elevation through the access broker. Local administrator access to MES and DNC servers will move behind the broker with MFA by 2027-01-31.
- **Plant 1 operators** sign in to MES through SYS-01 with a badge tap plus PIN.
- **Exception until 2027-01-31:** Plant 2 MES terminals use shared logins. Compensating measures until then: terminals reachable only from the Plant 2 floor, supervisor sign-off on program changes, and camera coverage of the terminals (P07 POAM-003).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); requirement statements (`sp800-171-requirement-statements.csv`); risk register (P01); gap analysis, score, and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor assurance reviews (P09); AI governance assessment (P10); cloud provider CRM and FedRAMP Marketplace record (kept by the Security Manager).

## 13. Acronym List and Glossary
- **C3PAO:** CMMC Third-Party Assessment Organization
- **CDI:** covered defense information
- **CMMC:** Cybersecurity Maturity Model Certification
- **CRM:** customer responsibility matrix
- **CSP, ESP:** cloud service provider, External Service Provider
- **CTI:** controlled technical information
- **CUI:** Controlled Unclassified Information
- **DNC:** direct numerical control (NC program distribution)
- **FCI:** Federal contract information
- **MDR:** managed detection and response
- **MES:** manufacturing execution system
- **MFT:** managed file transfer
- **MSSP:** managed security service provider
- **OT:** operational technology
- **POA&M:** plan of action and milestones
- **SPRS:** Supplier Performance Risk System

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 3.0 | 2025-05-30 | Landing zone rebuild; Plant 1 scope | Security Manager |
| 3.9 | 2026-07-31 | Draft with Plant 2, MSSP as ESP, AI flows, and 110 requirement statements | Security Manager and GRC analyst |
| 4.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager |
