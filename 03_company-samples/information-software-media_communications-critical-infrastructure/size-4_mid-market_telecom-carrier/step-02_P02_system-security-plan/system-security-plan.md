# System Security Plan: Network Operations and Customer Billing Platform (OSS/BSS)

**Organization:** Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) | **Tier:** Mid-Market | **Vertical:** Communications
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Network Operations and Customer Billing Platform (**OSS/BSS**), identifier CSC-OSSBSS-01. It is the company's major system and comprises SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-09, SYS-13, SYS-16, and SYS-18 in `../00_company-facts.md`.

## 2. System Overview
The OSS/BSS runs customer and network operations for about 205,000 accounts in parts of 11 Florida counties: customer accounts and billing, CPNI approvals, call detail and toll rating, service provisioning, trouble tickets and dispatch, the customer portal and app, and management of the voice and broadband network. It supports the High-criticality processes BP-01 to BP-05, BP-08, and BP-09 in the BIA (P05), directly or through the management plane.

Users: about 700 workforce members (care agents, retail, billing, NOC, engineering, provisioning, IT, management, and field technicians who receive dispatches on tablets), 35 agents of the overflow call center vendor, and customers who use the portal and app.

**Major components (inside the boundary):**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Billing and customer care system (BSS): accounts, CPNI approval flags, account passwords, bills, agent desktop | Vendor SaaS; vendor SOC 2 Type 2 |
| SYS-02 | OSS: inventory, provisioning, trouble tickets, dispatch | Company-managed application in the production account of the landing zone |
| SYS-03 | Voice mediation and rating with the 36-month CDR archive | Production account (virtual machines and object storage) |
| SYS-04 | Customer portal and app back end, API gateway, web application firewall | Production account (PaaS) |
| SYS-05 | Identity provider (workforce single sign-on and MFA; backs TACACS+) | SaaS |
| SYS-09 | Network management plane: NOC monitoring and alarm correlation, element managers, TACACS+, syslog, configuration backups, jump hosts | On-premises at CO-1 and CO-4 |
| SYS-13 | Cloud landing zone: management, security and log archive, network hub, production, and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-16 | SIEM, monitored 24x7 by the MDR provider | SaaS |
| SYS-18 | Legacy CLEC billing system (about 6,800 business accounts until 2027-06-30) | On-premises at POP-A |

**Interconnected, outside the boundary:** the voice core (SYS-07) and IP/MPLS and access network (SYS-08), which the platform manages and which feed CDRs to SYS-03; the contact center platform (SYS-11); the AI chatbot (SYS-12); and the Business Services platform (SYS-15, covered by the P09 SOC 2 system description). The lawful-intercept system (SYS-10) is excluded and governed by the CALEA SSI plan.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the OSS/BSS |
|---|---|---|---|
| C-COMMUNICATIONS-R01 | FCC CPNI rules | 47 U.S.C. 222; 47 CFR 64.2001-64.2011 | Primary. SYS-01, SYS-03, SYS-04, and SYS-18 hold CPNI for the voice services: approvals (64.2007-64.2009), customer authentication and change notices (64.2010), breach notice (64.2011). "Reasonable measures" (64.2010(a)) are benchmarked to CSF 2.0 |
| C-COMMUNICATIONS-R02 | FCC outage reporting | 47 CFR Part 4 (4.9, 4.11, 4.18) | SYS-09 and SYS-02 support outage detection, PSAP notice, and NORS and DIRS filings |
| 911 reliability | Covered 911 service provider duties | 47 CFR 9.19-9.20 (as amended by FCC 26-39, 91 FR 42794, effective 2026-08-10) | SYS-09 provides the monitoring of covered 911 facilities; the OSS circuit inventory holds the tags for legacy 911 circuits (9.19(a)(9)); records must be kept 2 years (9.20(e)) |
| C-COMMUNICATIONS-R03 | CALEA system security and integrity | 47 U.S.C. 1001-1010; 47 CFR 1.20000-1.20008 | SYS-10 is outside the boundary but shares the management network path today (SC-7 gap); compromise reporting (1.20003(c)) is in P08 |
| Call authentication | STIR/SHAKEN and robocall mitigation | 47 CFR 64.6301-64.6305 | SYS-03 CDRs answer traceback requests within 24 hours (64.6305(a)(2)) |
| Supply chain | Secure Networks Act reporting | 47 CFR 1.50007 | CM-8 and SR-3 support the no-covered-equipment certification |
| C-COMMUNICATIONS-R05 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Tracked only. No final rule as of 2026-10-05 |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Breach notice for personal information in SYS-01, SYS-04, and SYS-18 (P08); other states' laws for seasonal residents |
| Benchmark | NIST CSF 2.0 and CISA Cross-Sector CPGs (voluntary) | P03 rows G-059 to G-072 | Measure of "reasonable measures" under 64.2010(a) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

**Not applicable** (reasons in P03 section 1): SEC cybersecurity disclosure (C-COMMUNICATIONS-R06; privately held); submarine cable rules (C-COMMUNICATIONS-R04; no cable landing); CMRS-only CPNI rules (64.2010(h)); EAS rules (no video or broadcast service). Broadband usage data is not CPNI after *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025), but POL-04 protects the whole customer account record to the CPNI standard.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the OSS/BSS accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the chatbot "verify me" fallback stays disabled (done 2026-07-24) until P10 conditions are met; the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (SYS-18 retirement, SBC replacement).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Management plane hardening: named TACACS+ accounts with MFA on all element types, POP segmentation, vendor access through the access broker (due 2027-03-31)
- SIEM onboarding of network element logs, CDR archive reads, and SYS-18 (due 2027-01-31)
- Migration of the 6,800 CLEC accounts from SYS-18 to SYS-01 (due 2027-06-30)
- SBC upgrades before end of support (due 2026-12-15)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the OSS/BSS; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Technical owner | Chief Technology Officer | Network, NOC, and IT; 911 reliability certifying official |
| Security operations and GRC | Security Manager, 2 security analysts, GRC analyst | Day-to-day control owner; vulnerability management; MDR oversight; this SSP |
| CPNI compliance officer | Vice President of Regulatory Affairs | CPNI certification; breach determinations with counsel |
| CALEA senior officer | Vice President of Network Operations | SYS-10 and the SSI plan; compromise reports |
| Component owners | IT Director (SYS-05, SYS-13); NOC Director and Director of Network Engineering (SYS-09); Billing Director (SYS-01, SYS-03, SYS-18); Director of Customer Operations (SYS-04) | Role assignments, access reviews, procedures |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MDR provider | 24x7 SIEM and EDR monitoring |

## 6. System Information Types and System Categorization
Information types are the closest matches in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer account and CPNI records (closest type: Customer Services) | Moderate | Moderate | Moderate | Disclosure of call detail harms customers and triggers 64.2011; wrong approval flags cause unlawful CPNI use; care can run on offline reports for up to 24 h (P05 BP-09 MTD) |
| Call detail and rating (closest type: Collections and Receivables) | Moderate | Moderate | Low | 36 months of calling history for about 74,000 lines; switches buffer CDRs for 72 h (P05 BP-13 MTD 120 h) |
| Network operations, configuration, and outage records (closest types: System and Network Monitoring; IT Infrastructure Maintenance) | Moderate | Moderate | Moderate | Topology and configurations are sensitive (NORS filings are presumptively confidential, 4.2); altered configurations can cause outages; the NOC needs the management plane within 30 minutes to meet PSAP clocks (P05 BP-04) |
| Workforce identities (closest type: Human Resources Management) | Moderate | Moderate | Low | Credentials give access to all of the above |
| **OSS/BSS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability was considered for High.** BP-02 (911 facilities) has a 1-hour MTD. The team kept availability at Moderate because 911 call completion depends on the voice core and access network (SYS-07, SYS-08), which are outside this boundary and have their own redundancy (two core nodes, diverse 911 circuits, generators). Loss of the OSS/BSS slows outage response and care but does not by itself stop calls. To compensate, the tailoring adds the NOC failover to CO-4 and the PSAP notification procedure as contingency controls (CP-2, CP-7).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the BSS tenant configuration, user roles, and CPNI flags;
- the identity provider tenant;
- all 5 cloud accounts and their workloads (OSS, mediation and CDR archive, portal back end, API gateway, data warehouse, backup vault, log archive);
- the network management plane at CO-1 and CO-4 (monitoring, element managers, TACACS+, syslog, configuration backups, jump hosts);
- the SIEM tenant and its use cases;
- SYS-18 at POP-A;
- the endpoints of users who administer these components.

**Outside the boundary (external services, interconnected):**
- the BSS vendor's platform, the identity vendor's platform, the cloud provider's infrastructure, and the MDR provider's platform (inherited controls);
- the voice core and access network (managed through SYS-09);
- the contact center platform and the chatbot (vendor SaaS that call the BSS API);
- the Business Services platform (P09);
- the CALEA TTP, the SS7 hub, the state NG911 system service provider, the bill print vendor, and the payment processor.

**Excluded:** the lawful-intercept system (SYS-10), covered by the CALEA SSI plan. **Boundary weakness:** SYS-10 is reachable over the same management network path (P01 R-005); the segmentation work will place it on an isolated path.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Voice core (SYS-07) to mediation (SYS-03) | Inbound over site-to-cloud IPsec | CDRs | Internal; service account with read and write rights (**gap**: scope to read-only pulls) |
| Network elements (SYS-08) and management plane (SYS-09) | Bidirectional | Configurations, alarms, syslog, provisioning commands | Internal |
| Contact center platform (SYS-11) | Bidirectional (screen-pop; IVR payments; agent assist transcripts) | Account data, call recordings, transcripts | Vendor contract (**gap**: no CPNI, no-training, or 24-hour incident notice terms) |
| AI chatbot (SYS-12) | Bidirectional (API to SYS-01) | Account data, CPNI, chat transcripts | Vendor contract (**gap**: no security review until P10; no-training clause missing) |
| Overflow call center vendor | Agents use the BSS agent desktop | Account data, CPNI | Vendor contract with confidentiality terms (**gap**: no CPNI training requirement) |
| Business Services platform (SYS-15) | Bidirectional (provisioning, billing usage) | Business customer configurations and usage | Internal |
| Payment processor | Outbound redirect and token return | Payment tokens only | Processor agreement |
| Bill print vendor | Outbound | Bill images, including toll call detail | Vendor contract with confidentiality terms |
| State NG911 system service provider | Outage coordination | Circuit and outage information | Interconnection agreement |
| FCC NORS and DIRS; CPNI breach reporting facility; RMD | Outbound (web portals) | Outage reports; breach reports; certifications | Regulatory filings |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| BSS tenant (SYS-01) | SaaS | BSS vendor | Billing Director |
| Identity provider tenant (SYS-05) | SaaS | Identity vendor | IT Director |
| OSS application (SYS-02) | Virtual machines and managed database | Production account | Vice President of Network Operations |
| Mediation and CDR archive (SYS-03) | Virtual machines and object storage | Production account | Billing Director |
| Portal and app back end (SYS-04); API gateway; web application firewall | PaaS web app; managed API gateway | Production account | Director of Customer Operations |
| Reporting data warehouse | Managed database | Production account | Marketing Director (data owner) |
| Backup vault | Backup service, write-once 35 days | Backup account (second region) | IT Director |
| Log archive; posture and threat detection | Write-once object storage; managed security services | Security account | Security Manager |
| Network hub, cloud firewall, site-to-cloud VPN | Network services | Network hub account | IT Director |
| Organization root, identity federation, guardrails | Identity and policy services | Management account | Security Manager |
| SIEM tenant (SYS-16) | SaaS | SIEM vendor, monitored by the MDR | Security Manager |
| NOC monitoring, element managers, syslog collectors, configuration backup servers, 2 TACACS+ servers, 4 jump hosts (SYS-09) | On-premises servers and virtual machines | CO-1 and CO-4 | NOC Director |
| Legacy CLEC billing system (SYS-18) | On-premises servers and database | POP-A | Billing Director |
| Administrator endpoints | Laptops and desktops (part of SYS-14) | All sites | IT Director |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The OSS/BSS uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 129 controls** in `control-implementation.csv`: 123 from the Moderate baseline; 3 privacy-baseline controls selected because the platform processes CPNI (PT-2, PT-4, PT-5); and 3 program controls selected by tailoring (PM-1, PM-2, PM-9). They cover every control that the P03 gap analysis maps to a CPNI, CALEA, outage, or 911 requirement, plus the Moderate controls that treat the risks in P01 (management plane, privileged and vendor access, monitoring, recovery).
- **Inherited without separate statements:** the remaining Moderate physical and environmental controls for the cloud and SaaS data centers, and platform-level SA and SC controls, inherited from the BSS vendor, the identity vendor, the cloud provider, the SIEM vendor, and the MDR provider. They are evidenced by SOC 2 Type 2 reports reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no regulatory mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, beyond the small OSS integration code). These are recorded as tailoring decisions and reviewed yearly.

**Status of the 129 documented controls:**
| Status | Count |
|---|---|
| Implemented | 53 |
| Partially implemented | 74 |
| Planned | 2 |
| Not applicable | 0 |

**Inheritance of the 129 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 83 | Company |
| Hybrid | 36 | BSS vendor, identity vendor, cloud provider, MDR provider, network equipment vendors, upstream transit providers |
| Common/Inherited | 10 | Identity vendor (for example AC-2(1), AC-7, IA-2(2)), cloud provider (CP-6, SC-12), MDR provider (IR-7), BSS vendor (AC-12, AU-12) |

The Partially implemented statements trace to the 15 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls (234 determination statements) from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Cloud and identity administrators use hardware security keys. This meets the company's authenticator standard (STD-06) for a Moderate system with remote and privileged access to CPNI. **Exceptions until 2027-03-31:** administrators of access elements, SBCs, and SYS-18 use shared local accounts without MFA (POAM-002); 40 field supervisors still have SMS as a fallback factor.
- **Customers.** Customers are non-organizational users of the portal, the app, and the chatbot. The CPNI rules set the minimum: authentication "without the use of readily available biographical information, or account information" before online access, then a password (47 CFR 64.2010(c), (e)). The portal and app meet this with a one-time code to the telephone number or email of record. The chatbot fallback that accepted SSN4 and service address did not; it was disabled on 2026-07-24. SYS-18's business portal reset is being replaced (POAM-016). Account changes trigger notices under 64.2010(f) from SYS-01 but not from SYS-18.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); CALEA SSI policies (ILEC 2019; merged-entity amendment due 2026-10-30); NOC outage and storm plan.

## 13. Acronym List and Glossary
- **BSS / OSS:** business support system (billing and care) / operations support system (inventory, provisioning, tickets)
- **CALEA:** Communications Assistance for Law Enforcement Act
- **CDR:** call detail record
- **CLEC / ILEC:** competitive / incumbent local exchange carrier
- **CPNI:** customer proprietary network information (47 U.S.C. 222(h)(1))
- **DIRS / NORS:** FCC Disaster Information Reporting System / Network Outage Reporting System
- **MDR:** managed detection and response
- **OLT / DSLAM:** optical line terminal / DSL access multiplexer
- **PSAP:** public safety answering point (a 911 special facility under 47 CFR 4.5(e))
- **RMD:** Robocall Mitigation Database
- **SBC:** session border controller
- **SSI:** system security and integrity (CALEA)
- **TACACS+:** centralized authentication, authorization, and accounting for network devices
- **TTP:** CALEA trusted third party

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager; reviewed by the vCISO |
