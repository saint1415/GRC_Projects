# System Security Plan: Network Operations and Customer Billing Platform (OSS/BSS)

**Organization:** Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) | **Tier:** Small | **Vertical:** Communications
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-04

## 1. System Name and Identifier
Network Operations and Customer Billing Platform (**OSS/BSS**), identifier CSC-SYS-001.

## 2. System Overview
The OSS/BSS runs the company's customer and network operations for about 64,000 accounts in three Florida counties: customer accounts and billing, CPNI approvals, call detail and toll rating, service provisioning, trouble tickets and field dispatch, the customer portal and app, and management of the voice and broadband network. Users are the workforce (care agents, billing, NOC, engineering, provisioning, IT, management, and field technicians who receive dispatches on tablets), the overflow call center vendor's agents, and the customers who use the portal and app.

**Major components (inside the boundary):**
- **SYS-01:** billing and customer care system (BSS), vendor SaaS; the system of record for accounts, CPNI approval flags, account passwords, and bills
- **SYS-02:** OSS (inventory, provisioning, trouble tickets, dispatch) in the cloud tenant
- **SYS-03:** voice mediation and rating, with the 36-month CDR archive, in the cloud tenant
- **SYS-04:** customer portal and mobile app (PaaS web app behind an API gateway)
- **SYS-05:** identity provider (workforce single sign-on and MFA; also backs TACACS+)
- **SYS-09:** network management plane at CO-1 (NOC monitoring, element managers, TACACS+, syslog, configuration backups, jump hosts)
- **SYS-13:** cloud tenant (IaaS/PaaS) hosting SYS-02, SYS-03, SYS-04, the API gateway, the reporting data warehouse, and the backup vault

**Interconnected, outside the boundary:** the voice core (SYS-07) and IP/MPLS and access network (SYS-08), which the platform manages and which feed CDRs to SYS-03; the contact center platform (SYS-11); and the AI chatbot (SYS-12). The lawful-intercept system (SYS-10) is excluded and governed by the CALEA SSI plan. The cloud tenant is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it touches this system |
|---|---|---|---|
| C-COMMUNICATIONS-R01 | FCC CPNI rules | 47 U.S.C. 222; 47 CFR 64.2001-64.2011 | Primary. SYS-01, SYS-03, and SYS-04 hold CPNI for the voice services; authentication (64.2010), approvals (64.2007-64.2009), breach notice (64.2011) |
| C-COMMUNICATIONS-R02 | FCC outage reporting | 47 CFR Part 4 (4.9, 4.18) | SYS-09 and SYS-02 support outage detection, PSAP notice, and NORS and DIRS filings |
| C-COMMUNICATIONS-R03 | CALEA system security and integrity | 47 U.S.C. 1001-1010; 47 CFR 1.20000-1.20008 | SYS-10 is outside the boundary, but it shares the management network path today (SC-7 gap); compromise reporting (1.20003(c)) is in the P08 runbook |
| C-COMMUNICATIONS-R05 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Tracked only. No final rule as of 2026-09-25 |
| State | Florida Information Protection Act (breach notice) | Fla. Stat. 501.171 | Applies to personal information in SYS-01 and SYS-04 (for example, online credentials); other states' laws for seasonal residents |
| Benchmark | NIST CSF 2.0 and CISA Cross-Sector CPGs (voluntary) | P03 rows G-047 to G-060 | Used as the measure of "reasonable measures" under 64.2010(a) |
| Internal | Security policies POL-01 to POL-05 | P06 | All components |

**Not applicable** (reasons in P03 section 1.4): SEC cybersecurity disclosure (C-COMMUNICATIONS-R06; privately held), submarine cable rules (C-COMMUNICATIONS-R04; no cable landing), CMRS-only CPNI rules (64.2010(h)), the EAS cybersecurity order (no video or broadcast service). Broadband usage data is not CPNI after *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025), but POL-04 protects the whole customer account record to the CPNI standard.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO (system executive owner and CPNI compliance officer) on 2026-09-04.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- The COO accepted continued operation of the OSS/BSS on 2026-09-04, with the conditions in the P07 POA&M.
- The Chief Executive Officer accepted the six High risks in P01 on 2026-09-04, only with the dated treatment plans and funding listed there.
- **Conditions:** the portal password reset must be replaced by 2026-11-30 (POAM-001), and the chatbot's quick help mode stays disabled until P10 conditions are met.
### 4.3 System Operational Status
Operational. Major modifications planned: management plane segmentation and TACACS+ expansion (by 2026-12-31), portal reset redevelopment (by 2026-11-30), backup isolation (by 2026-12-31), and managed detection and response (by 2027-01-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System executive owner | COO | Overall accountability; CPNI compliance officer; accepts Moderate risks |
| System owner (operations) | Vice President of Network Operations | OSS, management plane, and network interfaces; CALEA senior officer |
| Risk acceptor (authorizing official equivalent) | Chief Executive Officer | Accepts High and Very High risks |
| Security and compliance lead | IT Manager | Day-to-day security; maintains this SSP and the risk register; accepts Low risks |
| Privacy lead | Regulatory Affairs Manager | CPNI breach determinations with counsel; FCC filings |
| Business owners | Billing Manager (BSS, mediation); Director of Customer Operations (portal, contact center, chatbot) | Role assignments, access reviews, customer authentication procedures |
| Network element owner | Network Engineering Manager | Device configuration, patching, TACACS+ policy |

## 6. System Information Types and System Categorization
Information types are the closest matches in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer account and CPNI records (closest SP 800-60 type: Customer Services) | Moderate | Moderate | Moderate | Disclosure of call detail harms customers and triggers 64.2011; wrong approval flags cause unlawful CPNI use; care can run on offline reports for up to 24 h (P05 BP-05 MTD) |
| Call detail and rating (closest type: Collections and Receivables) | Moderate | Moderate | Low | 36 months of calling history for 23,400 lines; switches buffer CDRs for 72 h (P05 BP-08 MTD 120 h) |
| Network operations, configuration, and outage records (closest types: System and Network Monitoring; IT Infrastructure Maintenance) | Moderate | Moderate | Moderate | Network topology is sensitive; altered configurations can cause outages; the network keeps passing traffic, including 911, if the management plane is down, but outage response and PSAP notice need it within 1 h (P05 BP-03) |
| Workforce identities (closest type: Human Resources Management) | Moderate | Moderate | Low | Credentials give access to all of the above |
| **OSS/BSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why availability is not High.** 911 call completion depends on the voice core and access network (SYS-07, SYS-08), which are outside this boundary and have their own redundancy (second SBC at CO-2, generators with 72 hours of fuel). Loss of the OSS/BSS slows outage response and care but does not by itself stop calls.

**Baseline:** the NIST SP 800-53B Moderate baseline, tailored for a 250-employee carrier. The plan documents **78 controls** (`control-implementation.csv`): 72 from the Moderate baseline, 4 privacy-baseline controls selected because the platform processes CPNI (PM-9, PT-2, PT-4, PT-5), and 2 program controls selected by tailoring (PM-1, PM-2). Every other Moderate-baseline control is either:
- **Inherited** from the SaaS and cloud providers, as evidenced by their SOC 2 reports (P09 Part B and the P04 map), or
- **Out of scope for this tier**, recorded as a tailoring decision where the control's purpose applies only to federal systems.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of vendor services:
- **Inside:** the BSS tenant configuration, user roles, and CPNI flags; the identity provider tenant; the cloud tenant (OSS, mediation and CDR archive, portal and app back end, API gateway, data warehouse, backup vault); the network management plane at CO-1 (monitoring, element managers, TACACS+, syslog, configuration backup server, jump hosts); and the endpoints of users who administer these components.
- **Outside (interconnected):** the BSS vendor's platform and the cloud provider's infrastructure (inherited controls); the voice core and access network (managed through SYS-09); the contact center platform and the chatbot (vendor SaaS that call the BSS API); the CALEA TTP, the SS7 hub, the NG911 system service provider, the bill print vendor, and the payment processor.
- **Excluded:** the lawful-intercept system (SYS-10), covered by the CALEA SSI plan. **Boundary weakness:** SYS-10 is reachable over the same management network path (P01 R-013); the segmentation work will place it on an isolated path.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Voice core (SYS-07) to mediation (SYS-03) | Inbound over site-to-site VPN | CDRs | Internal; service account with read and write rights (**gap**: scope to read-only pulls) |
| Network elements (SYS-08) and management plane (SYS-09) | Bidirectional | Configurations, alarms, syslog, provisioning commands | Internal |
| Contact center platform (SYS-11) | Bidirectional (agent desktop screen-pop; IVR payments) | Account data, call recordings | Vendor contract (**gap**: no CPNI or 24-hour incident notice terms) |
| AI chatbot (SYS-12) | Bidirectional (API to SYS-01) | Account data, CPNI, chat transcripts | Vendor contract (**gap**: no security review; P10) |
| Overflow call center vendor | Agents use the BSS agent desktop | Account data, CPNI | Vendor contract with confidentiality terms (**gap**: no CPNI training requirement) |
| Payment processor | Outbound redirect and token return | Payment tokens only | Processor agreement |
| Bill print vendor | Outbound | Bill images, including toll call detail | Vendor contract with confidentiality terms |
| FCC NORS and DIRS; CPNI breach reporting facility | Outbound (web portals) | Outage reports; breach reports | Regulatory filings |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| BSS tenant (SYS-01) | SaaS | BSS vendor | Billing Manager |
| Identity provider tenant (SYS-05) | SaaS | Identity vendor | IT Manager |
| OSS application (SYS-02) | Cloud virtual machines and managed database | Cloud tenant | Vice President of Network Operations |
| Mediation and CDR archive (SYS-03) | Cloud virtual machine and object storage | Cloud tenant | Billing Manager |
| Portal and app back end (SYS-04); API gateway | PaaS web app; managed API gateway; web application firewall | Cloud tenant | Director of Customer Operations |
| Reporting data warehouse | Managed database | Cloud tenant | Billing Manager |
| Backup vault | Cloud backup service | Cloud tenant (same account and region, **gap**) | IT Manager |
| NOC monitoring, element managers, syslog, configuration backup server, TACACS+ server, 2 jump hosts (SYS-09) | On-premises servers and virtual machines | CO-1 | NOC Manager |
| Administrator endpoints | Laptops and desktops (part of SYS-14) | CO-1, CO-2, remote | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 78 controls:
- Implemented: 24
- Partially implemented: 46
- Planned: 8

By inheritance: 56 system-specific, 18 hybrid, 4 common or inherited from providers.

### 10.2 Control assessment status
An independent assessor tested 20 of these controls from 2026-08-10 to 2026-08-14. Results are in P07 `assessment-results.csv`, and every weakness is in P07 `poam.csv`.

## 11. Digital Identity Acceptance Statement
**Workforce users.** All workforce users authenticate through the identity provider with a password and a second factor (push approval with number matching planned). Cloud and identity administrators use hardware security keys. This fits a Moderate system with remote and privileged access to CPNI. **Exception until 2026-12-31:** administrators of OLTs, DSLAMs, cabinet switches, and SBCs still use shared local accounts without MFA (POAM-003).

**Customers.** Customers are non-organizational users of the portal and app. The CPNI rules set the minimum: authentication "without the use of readily available biographical information, or account information" before online access, then a password (47 CFR 64.2010(c), (e)). The current reset flow does not meet this. The target design, due 2026-11-30:
- enrollment and reset by a one-time code sent to the telephone number or email address of record;
- optional app-based second factor;
- immediate notice to the customer of any password, backup authentication, online account, or address-of-record change (64.2010(f)).

## 12. Referenced Artifacts
Scenario facts (`../scenario-facts.md`), risk register (P01), gap analysis (P03), cloud control map and diagram (P04), BIA (P05), policies POL-01 to POL-05 (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 self-benchmark and BSS vendor review (P09), chatbot AI assessment (P10), CALEA SSI policies (filed 2014; rewrite due 2026-10-30).

## 13. Acronym List and Glossary
- **BSS / OSS:** business support system (billing and care) / operations support system (network inventory, provisioning, tickets)
- **CALEA:** Communications Assistance for Law Enforcement Act
- **CDR:** call detail record
- **CPNI:** customer proprietary network information (47 U.S.C. 222(h)(1))
- **DIRS / NORS:** FCC Disaster Information Reporting System / Network Outage Reporting System
- **DSLAM / OLT:** DSL access multiplexer / optical line terminal
- **PSAP:** public safety answering point (a 911 special facility under 47 CFR 4.5(e))
- **SBC:** session border controller
- **SSI:** system security and integrity (CALEA)
- **TACACS+:** centralized authentication, authorization, and accounting for network devices
- **TTP:** CALEA trusted third party

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-21 | Draft after control assessment | IT Manager |
| 1.0 | 2026-09-04 | Approved | IT Manager; approved by the COO |
