# System Security Plan (short form): Building Systems Support Environment

**Organization:** Cris Santos Company (facilities support contractor operating government buildings, NAICS 561210) | **Tier:** Sole Proprietorship | **Vertical:** Government Services and Facilities
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Building Systems Support Environment (**BSSE**), identifier CSC-SYS-001.

## 2. System Overview
The BSSE is everything the owner uses to operate and maintain customer building systems: one laptop with the BAS engineering software, one phone, a business productivity suite, a remote-desktop subscription, an accounting service, the home office network, and a consumer AI chatbot (SYS-01 to SYS-07 in `../00_company-facts.md` section 3). It also includes the owner's **administrator accounts and access paths into the city's building systems** (SYS-08): the city VPN, the city identity provider sign-in to the cloud access control tenant, the remote-desktop agent on the city hall BAS engineering workstation, and the shared BAS supervisory administrator account.

It supports the five business processes in the BIA (P05): city building operations (BP-01), city access control administration (BP-02), federal building BAS support (BP-03), billing (BP-04), and communications and records (BP-05). One person, the owner, uses and runs it.

**Why this boundary and not the registry default.** The registry default system is "Physical access control and building automation system." Those systems belong to the customers: the city owns its BAS controllers and its access control tenant, and GSA owns the federal building BAS. A one-person contractor cannot write the security plan for a customer's system. What the owner controls, and what an attacker would use to reach those systems, is the owner's own devices, accounts, and access paths. That is the BSSE.

There is no server and no IaaS. Most platform safeguards are inherited from the SaaS providers. The owner is responsible for identities, data, devices, the home network, and how the access paths into the city's systems are used (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the BSSE |
|---|---|---|---|
| Contract CT-C | City security exhibit: SP 800-53 Rev. 5 **Moderate** safeguards for contractor devices and accounts that administer city building systems or store city data; MFA for remote access; incident notice within 24 hours; background check; annual training; return or destruction of data | City contract (the city adopted its cybersecurity standards under Fla. Stat. 282.3185(4)(a)) | **Binding.** The basis for the control set in section 10 |
| Contract CT-F | Basic safeguarding of covered contractor information systems | FAR 52.204-21 (NOV 2021), flowed down under 52.204-21(c) | Laptop, phone, and productivity suite hold FCI (work orders, point lists) |
| Contract CT-F | Kaspersky, Section 889, and FASCSA prohibitions and reporting; PIV accountability | FAR 52.204-23, 52.204-25 (without (b)(2)), 52.204-30 (without (c)(1)), 52.204-9 | Parts the owner supplies for the federal building; the owner's PIV card |
| C-GOVERNMENT-R01 | FISMA, through GSA policies for contractor staff on GSA systems | 44 U.S.C. 3554; GSA BTTRG v3.0 (section 1.6.1 incident reporting) | Owner conduct on SYS-09 and the duty to report incidents involving GSA data or credentials immediately. GSA's BAS is not part of the BSSE |
| CUI (CT-F) | Safeguarding of GSA drawings marked CUI | 32 CFR 2002.14; GSA Order PBS 3490.3 CHGE 1 | Three drawing sets in the productivity suite and on the laptop |
| State | Contractor public records duties; exempt building plans and security system plans | Fla. Stat. 119.0701(2)(b); 119.071(3)(a) and (b) | City drawings, BAS riser diagrams, door hardware schedules, cardholder exports |
| State | Reasonable security and third-party agent breach notice | Fla. Stat. 501.171(2) and (6)(a) | City cardholder exports (treated as personal information; counsel to confirm, facts section 7) |
| Internal | Information Security Policy (consolidated) | POL-01 (P06) | All components |

Not applicable (P03 section 1): IRS Pub. 1075 (R02), CJIS Security Policy (R03), VVSG 2.0 (R04), FERPA (R05), SLCGP (R07), GovRAMP (R08), FedRAMP, DFARS 252.204-7012 and CMMC. CIRCIA (R06) is a proposed rule only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-09-04.
### 4.2 System Authorization Decision
No formal authorization applies to a private contractor's own tools. Equivalent decision: the owner accepted continued operation on 2026-09-04, on condition that the three High risks in P01 (R-001 remote-desktop path, R-002 shared BAS administrator account, R-006 single-person dependency) are treated by their due dates. A summary of this plan and the owner's account list go to the city IT manager by 2026-09-30 (POL-01 7.8).
### 4.3 System Operational Status
Operational. Planned changes: remove the remote-desktop agent from the city hall BAS workstation (2026-09-30); standard user account for daily laptop work (2026-09-30); owner-owned router with a separate work network (2026-11-30); cloud backup folder for controller programs (2026-10-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security officer, CUI handler, incident handler, risk acceptor | Owner (building controls technician) | Every role. Designated in writing in POL-01 section 3 |
| Technical support | On-call IT technician (NDA signed 2026-08-03) | Laptop, phone, and router help on request; no standing access; sessions started and watched by the owner |
| Customer system owners | City IT manager; GSA (through the prime contractor) | Own SYS-08 and SYS-09, their VPN, identity provider, and logs; receive incident notices |
| Service providers | Productivity suite provider, remote-desktop provider, accounting SaaS provider, access control SaaS vendor (the city's vendor) | Operate inherited controls |

## 6. System Information Types and System Categorization
Impact levels follow FIPS 199.

| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| Building operations data (BAS programs, schedules, setpoints, point lists, riser diagrams) | Moderate | Moderate | Moderate | Exempt building plans (Fla. Stat. 119.071(3)(b)); a wrong program can create unsafe temperatures in an occupied public building; BP-01 MTD 24 h |
| Physical access data (cardholder exports, door schedules, door hardware schedules) | Moderate | Moderate | Moderate | Names with credential numbers and access history; security system plans (119.071(3)(a)); a wrong schedule leaves doors unlocked; BP-02 MTD 24 h |
| CUI (GSA drawings, Physical Security category) | Moderate | Low | Low | CUI Basic is categorized at no less than moderate confidentiality (32 CFR 2002.14(g)) |
| Federal contract information (work orders, point lists) | Low | Low | Low | FCI under FAR 52.204-21; BP-03 MTD 72 h |
| Business administration (invoices, contracts) | Low | Low | Low | BP-04 MTD 240 h |
| **BSSE category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, as the city security exhibit requires. All 177 Moderate base controls were assessed in the gap analysis (P03); 44 are not applicable to a one-person environment, with the reason given in each row. This plan documents the **31 controls** that carry the key safeguards (`control-implementation.csv`). The other applicable controls are covered in P03 with the same statements.

## 7. Authorization Boundary Description
- **Inside:** the laptop (SYS-01), the productivity suite tenant (SYS-02), the phone (SYS-03), the remote-desktop subscription account and its agent's configuration (SYS-04), the accounting tenant (SYS-05), the home office network equipment (SYS-06), the consumer AI chatbot account (SYS-07), the owner's accounts in the city VPN, identity provider, access control tenant, and BAS supervisory controller, and paper drawings in the van cabinet and home office.
- **Outside (customer and external systems):** the city BAS supervisory controller, field controllers, engineering workstation, VPN, identity provider, and access control tenant (SYS-08, the city's systems); GSA's BAS, BSN, and GSA-furnished workstation (SYS-09, GSA's system under GSA's authorization); and the SaaS providers' platforms.

The owner never connects the laptop to the GSA BSN, so no federal system is reached from the BSSE. Under 32 CFR 2002.14(h)(2), the owner's systems receive federal information only incidental to providing a service, so they are non-federal systems.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Path | Agreement |
|---|---|---|---|
| City (CT-C) | BAS commands and programs; cardholder and door schedule changes; monthly cardholder export; drawings | City VPN (city MFA); access control tenant through the city identity provider (city MFA); **remote-desktop agent (gap; removal 2026-09-30)**; email | City contract and security exhibit |
| Prime contractor (CT-F) | Work orders, point lists (FCI); CUI drawings | Email and cloud file sharing | Subcontract with FAR flow-downs |
| GSA (CT-F) | None from the BSSE. GSA's BAS is used only on GSA's workstation | On site only | Subcontract; GSA rules of behavior |
| On-call IT technician | Screen view during support sessions | Owner-started remote support session | NDA (2026-08-03) |
| Consumer AI chatbot provider | BAS point lists and a door schedule excerpt were pasted in June to August 2026 (P10) | Web chat | Click-through terms only (**gap**) |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| SYS-01 Business laptop | Endpoint | Owner |
| SYS-02 Productivity suite tenant | SaaS | Owner |
| SYS-03 Mobile phone | Personal endpoint | Owner |
| SYS-04 Remote-desktop subscription and agent | SaaS plus agent on city equipment | Owner (agent on city equipment) |
| SYS-05 Accounting tenant | SaaS | Owner |
| SYS-06 Home office router and Wi-Fi | Network (ISP-supplied) | Owner |
| SYS-07 Consumer AI chatbot account | SaaS (consumer) | Owner |
| Owner accounts in SYS-08 (VPN, identity provider, access control tenant, BAS supervisory controller) | Accounts in customer systems | City (the owner uses them) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 31 controls:
- Implemented: 8
- Partially implemented: 15
- Planned: 8

Inheritance: 15 hybrid (a SaaS provider, the device vendor, the city, or GSA operates part of the mechanism and the owner configures or uses it correctly) and 16 the owner's alone. None is fully inherited, because even where a provider runs the mechanism the owner still decides who gets access and where the data goes.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 (consolidated policy); contract security terms; supplier screening for the federal building (SR-3, planned) |
| Identify | Risk register (RA-3); BIA (P05); component and data location inventory (CM-8, partial) |
| Protect | MFA on the suite, VPN, and tenant (IA-2(1)); disk encryption (SC-28); standard account for daily work (AC-6, planned); remote access only through the city VPN (AC-17, gap) |
| Detect | Monthly review of the access control audit trail, remote session log, and suite sign-ins (AU-6, planned) |
| Respond | P08 runbook with the 24-hour, immediate, 1-business-day, and 10-day clocks (IR-6, IR-8) |
| Recover | Controller program and door schedule backups (CP-9, gap); manual operation sheets and backup technician (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the on-call IT technician; 10 controls tested 2026-08-18 to 2026-08-20. See P07.

## 11. Digital Identity Acceptance Statement
The productivity suite, accounting service, city VPN, and city access control tenant require a password and an authenticator app on the owner's phone, which is appropriate for remote and privileged access at a Moderate categorization. The remote-desktop account used a password only until 2026-08-18, when the owner turned on MFA during P07 testing; the agent is being removed. The BAS supervisory controller has no MFA and uses one shared built-in administrator account; the owner reaches it only after the city VPN's MFA once the agent is gone, and has asked the city for a named account (POAM-002). At the federal building the owner authenticates to GSA's workstation with a GSA-issued PIV card under GSA's own identity rules.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment, city contract and security exhibit, CT-F subcontract, GSA BTTRG v3.0.

## 13. Acronym List and Glossary
- **BAS:** building automation system (HVAC controls)
- **BSN:** GSA Building Systems Network
- **BSSE:** Building Systems Support Environment
- **BTTRG:** GSA Building Technologies Technical Reference Guide
- **CUI:** controlled unclassified information
- **FCI:** federal contract information
- **MFA:** multi-factor authentication
- **PIV:** personal identity verification (GSA-issued smart card)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-04 | Initial short-form plan | Owner |
