# System Security Plan (short form): Core Business SaaS Stack

**Organization:** Cris Santos Company (pipeline integrity engineering consultant) | **Tier:** Sole Proprietorship | **Vertical:** Energy
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-11

## 1. System Name and Identifier
Core Business SaaS Stack (**CBSS**), identifier CSC-SYS-001. This is the registry's "core business SaaS stack (email, files, client and billing records)".

## 2. System Overview
The CBSS is everything the consultancy uses to receive client pipeline data, analyze it, deliver sealed engineering reports, and bill for the work. One person, the engineer-owner, uses and runs it. Components are in `../00_company-facts.md` section 3: the productivity suite (SYS-01), the engineering laptop (SYS-02), the phone (SYS-03), removable media (SYS-04), the accounting SaaS (SYS-05), the AI anomaly-screening tool (SYS-07, trial stopped; see P10), the home office network (SYS-08), and paper client files in the home office. There is no server and no IaaS. Client A's integrity portal and Client B's file transfer site (SYS-06) belong to the clients and sit outside the boundary.

The system matters beyond its size because it holds **Client A's Sensitive Security Information** (an excerpt of its TSA-approved Cybersecurity Implementation Plan and a network zone drawing) and ILI and SCADA historian data for three pipeline operators. Most technical safeguards are **inherited from the SaaS providers**; the owner is responsible for identities, data handling, devices, media, and the terms with clients, subcontractors, and vendors (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | How it reaches this system |
|---|---|---|
| 49 CFR Part 1520 | Protection of Sensitive Security Information | **Binding.** The owner holds Client A's SSI as a covered person (1520.7(j) and (k)). Duties in 1520.9, 1520.11, 1520.13, 1520.19 |
| C-ENERGY-R03 | TSA SD Pipeline-2021-02G | **Not binding on the consultant.** Applies to Client A. Section IV.B requires Client A to store and transmit its plans and assessment results under Part 1520, which is why the plan excerpt is SSI. Client A flows its expectations down through the supplier addendum |
| C-ENERGY-R02 | TSA SD Pipeline-2021-01G | Not binding on the consultant. Client A reports its own cybersecurity incidents to CISA as soon as practicable and no later than 72 hours after identifying them; the consultant's 24-hour notice to Client A supports that |
| Contract | Client A Supplier Cybersecurity and Information Protection Addendum; Client B NDA | Binding by contract (sections listed in P03) |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) data security and (3) to (6) breach notice, for subcontractor W-9 data |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: C-ENERGY-R01 NERC CIP (no BES assets), C-ENERGY-R04 49 CFR 192.631 (no control room), C-ENERGY-R05 CIRCIA (proposed only; the consultant is also below the SBA size standard for NAICS 541330 and is not a pipeline Owner/Operator). See P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the engineer-owner on 2026-09-11.
### 4.2 System Authorization Decision
No formal authorization applies to a private consultancy. Equivalent decision: the engineer-owner accepted continued operation on 2026-09-11, on condition that the four High risks in P01 (R-001, R-003, R-004, R-005) are treated by their due dates and that no Client A data goes to any service Client A has not approved in writing.
### 4.3 System Operational Status
Operational. Planned changes: password manager and accounting MFA (2026-09-15); encrypted backup drive (2026-09-15); separate SSI folder and locked storage (2026-09-30); separate work network (2026-09-30).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, SSI custodian, risk acceptor | Engineer-owner | Every role, designated in POL-01 4.2 |
| Technical support | On-call IT support contractor (NDA since 2026-08-07) | Help on request; no standing access; never given SSI |
| Subcontractors | GIS and drafting; field NDE and corrosion | Use client data only as shared for a task; no SSI |
| Service providers | Productivity suite provider; accounting SaaS provider | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (organization-defined, SP 800-60 method) | C | I | A | Rationale |
|---|---|---|---|---|
| Client SSI (plan excerpt, zone drawing) | Moderate | Low | Low | Release to people without a need to know could help an attacker of Client A's leak-detection data path; the owner never edits it |
| Client engineering data (ILI results, GIS, historian exports, integrity records) | Moderate | Moderate | Low | Clients treat it as confidential; altered data could lead to a wrong dig or repair recommendation; clients can resend it (P05 MTD 72 h) |
| Draft and sealed deliverables | Low | Moderate | Moderate | Integrity of a sealed report matters for pipeline safety decisions; urgent findings have a 24 h MTD (P05 BP-01) |
| Business and subcontractor records (invoices, W-9s) | Moderate | Low | Low | Social Security numbers of 5 individuals (Fla. Stat. 501.171) |
| **CBSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 30 controls that carry the SSI duties, the Client A addendum, and basic hygiene for a one-person firm (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS providers (evidence: the suite provider's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal system. AC-5, AU-9, CM-3, and CA-2(1) assume a second person but are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's suite tenant and its settings, the laptop, the phone, the USB backup drive and any vendor drive while in the owner's custody, the accounting SaaS account, the AI tool trial account (being closed), the home office network as used for work, and paper client files in the home office.
- **Outside (external services and interfaces):** the suite and accounting providers' platforms, Client A's integrity portal and remote access gateway, Client B's file transfer site, the AI tool vendor's platform, ILI vendors, the subcontractors' own devices, and the ISP.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Client A | ILI results, GIS, historian exports, SSI records; deliverables back | MSA with supplier addendum; work order documents need to know for SSI |
| Client B | Integrity records, GIS; deliverables back | NDA (72-hour incident notice) |
| Client C | Distribution integrity data; deliverables back | Contract confidentiality clause |
| GIS subcontractor | Client GIS extracts; maps back | One-page NDA. **No security terms; not approved in writing by Client A (gap)** |
| Field subcontractor | Dig locations; field data sheets and photos back | One-page NDA. **No security terms (gap)** |
| AI tool vendor | Client A historian exports and one ILI feature list | **Click-through free-trial terms only; not approved by Client A (gap); use stopped** |
| Accounting SaaS provider | Invoices, W-9s, bank feed | Provider terms of service |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Productivity suite tenant (SYS-01) | SaaS | Engineer-owner |
| Engineering laptop (SYS-02) | Endpoint | Engineer-owner |
| Mobile phone (SYS-03) | Personal endpoint | Engineer-owner |
| USB backup drive; ILI vendor drives in custody (SYS-04) | Removable media | Engineer-owner (vendor drives belong to clients) |
| Accounting SaaS (SYS-05) | SaaS | Engineer-owner |
| AI anomaly-screening trial account (SYS-07) | SaaS | Engineer-owner |
| Home office network (SYS-08) | ISP router | Engineer-owner |
| Paper client files | Paper | Engineer-owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 30 controls:
- Implemented: 9
- Partially implemented: 15
- Planned: 6

Inheritance: 3 fully inherited from the suite provider (AU-2, AU-9, SC-5), 10 hybrid (a provider runs the mechanism, the owner configures or uses it correctly), and 17 the owner's alone.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; client and subcontractor terms (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); data retention (SI-12, gap) |
| Protect | Suite MFA (IA-2(1)); laptop encryption (SC-28); SSI marking and storage (MP-3, MP-4, gaps) |
| Detect | Suite logging (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Ransomware runbook (IR-8); reporting clocks (IR-6) |
| Recover | Provider version history (CP-9, inherited part); peer engineer arrangement (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-08-10 to 2026-08-14 with the on-call IT support contractor. See P07.

## 11. Digital Identity Acceptance Statement
The suite requires a password and an authenticator-app code on the owner's phone, which is appropriate for remote access to Moderate data held in SaaS. The accounting SaaS used a password only until MFA is turned on (2026-09-15). Client A's portal uses Client A's own identity controls, outside this boundary. Subcontractors will reach shared files only through named external accounts with a one-time sign-in code, not anonymous links (POL-01 7.4).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CBSS:** Core Business SaaS Stack
- **ILI:** in-line inspection (a tool run inside the pipe that records wall loss, dents, and cracks)
- **MFA:** multi-factor authentication
- **SSI:** Sensitive Security Information (49 CFR Part 1520)
- **TSA SD:** Transportation Security Administration Security Directive

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-11 | Initial short-form plan | Engineer-owner |
