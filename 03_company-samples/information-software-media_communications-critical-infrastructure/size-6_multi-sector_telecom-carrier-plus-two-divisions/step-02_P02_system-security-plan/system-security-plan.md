# System Security Plan: Network Operations and Customer Billing Platform (OSS/BSS)

**Organization:** Cris Santos Company Holdings, Inc. (Telecom Carrier division, with tenants from the Network Engineering Services and Tower and Fiber Infrastructure divisions) | **Tier:** Multi-Sector | **Vertical:** Communications
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the Carrier's **OSS/BSS**, because it holds the group's largest CPNI stores (BSS, CDR store), it manages the network that carries 911 calls, and its service assurance platform is in practice a **shared system**: the Engineering Managed Network Operations tenant (SYS-E1) and the Tower Alarm Monitoring Center tenant (SYS-T2) run on it. It inherits most of its controls from corporate (SYS-G1 to SYS-G3). Engineering's SYS-E1 and Tower's SYS-T2 keep division plans that inherit from the same common control catalog (`common-control-catalog.csv`).

## 1. System Name and Identifier
Network Operations and Customer Billing Platform (**OSS/BSS**), identifier CSCH-SYS-C1-C5. It covers SYS-C1 to SYS-C5 in `../00_company-facts.md`.

## 2. System Overview
The OSS/BSS runs the Carrier's customer and network operations in 14 states:
- **Customers:** accounts, billing, CPNI approval flags, and account passwords for about 4.9 million mass-market accounts and about 41,000 enterprise, government, and wholesale accounts (SYS-C2); online access through the portal and app (SYS-C4).
- **Call detail:** mediation and rating of CDRs for about 1.9 million voice lines, with 24 months online (SYS-C3).
- **Network operations:** inventory, provisioning and activation, field workforce management, and the service assurance platform (fault monitoring, alarm correlation, trouble ticketing) (SYS-C1).
- **Network management:** element management systems, AAA (TACACS+ and RADIUS), jump hosts, configuration backups, and syslog collectors in 6 regional NOC data centers (SYS-C5).

Users: about 6,800 in-house care agents, about 2,100 outsourced agents at two U.S.-based vendors, NOC and engineering staff, billing and provisioning staff, about 9,000 field technicians (dispatch only), customers using the portal and app, and **tenant operators from the other two divisions** (about 410 Engineering Managed Network Operations operators and about 60 Tower Alarm Monitoring Center operators).

**Major components:**
- **SYS-C1 OSS:** network inventory, provisioning, workforce management (provider A); service assurance platform with three tenants: Carrier NOC, Engineering MNO, Tower alarm center (provider A, disaster recovery copy in provider B)
- **SYS-C2 BSS:** licensed billing and CRM platform operated by the Carrier in provider A; the 2 acquired operating companies stay on a legacy billing system until 2027
- **SYS-C3 mediation and CDR store:** collectors in the regional NOCs; rating and object storage in provider A
- **SYS-C4 portal, app, and API gateway:** PaaS web tier and managed API gateway in provider A; also the gateway the AI chatbot (SYS-C10) calls
- **SYS-C5 management plane:** on premises in 6 regional NOC data centers

The cloud components are described by service category and are vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to the OSS/BSS |
|---|---|---|---|
| C-COMMUNICATIONS-R01 | FCC CPNI rules | 47 U.S.C. 222; 47 CFR 64.2001-64.2011 | **Primary.** The BSS, CDR store, and portal hold CPNI for the voice services. Authentication (64.2010), approvals and notices (64.2007-64.2008), safeguards and certification (64.2009), breach notice (64.2011). Affiliate access on the shared platform is limited by 64.2005(a)(2) and 64.2007(b) |
| C-COMMUNICATIONS-R02 | FCC outage reporting | 47 CFR Part 4 (4.9, 4.18) | The service assurance platform and management plane support outage detection, PSAP and 988 notices, and NORS and DIRS filings |
| C-COMMUNICATIONS-R03 | CALEA system security and integrity | 47 U.S.C. 1001-1010; 47 CFR 1.20000-1.20008 | SYS-C8 is outside the boundary, but its management path runs through SYS-C5 in two regions; compromise reporting (1.20003(c)) is in P08 |
| Covered equipment report | Secure Networks Act reporting | 47 CFR 1.50007 | The Carrier certified it has no covered communications equipment; inventory in SYS-C1 supports the certification (P03) |
| C-COMMUNICATIONS-R05 | CIRCIA (pending rule) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Tracked only. No final rule as of 2026-10-05 |
| C-COMMUNICATIONS-R06 | SEC cybersecurity disclosure | Reg S-K Item 106; Form 8-K Item 1.05 | An OSS/BSS incident may be material to the group (P08) |
| State | State breach notification laws | Each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | Personal information in the BSS and portal (for example, online credentials, SSNs used for credit checks) |
| Contracts | Enterprise CPNI contracts; Engineering MNO customer contracts; outsourced contact center contracts | 47 CFR 64.2010(g); contracts | Enterprise authentication terms; tenant data of Engineering customers on the service assurance platform |
| Internal | Group policies POL-01 to POL-05 and the Carrier supplement | P06 | All components |

**Not applicable:** CMRS-only CPNI rules (64.2010(h); no wireless service); submarine cable rules (C-COMMUNICATIONS-R04; no cable landing); the EAS cybersecurity order (no video or broadcast service). Broadband usage data is not CPNI after *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025), but POL-04 protects the whole customer account record to the CPNI standard (P03 section 1).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the Carrier OSS/BSS platform vice president (system owner) on 2026-09-17, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-17, by the Group CISO and the Group Chief Risk Officer (acceptance authority for High risks), with the Carrier division president concurring.
- **Conditions:**
  1. Remove the cross-tenant read role from Engineering and Tower operators by 2026-11-30 and complete tenant partitioning by 2027-03-31 (POAM-008).
  2. Replace shared local administrator accounts in the acquired regions with named TACACS+ accounts and MFA by 2027-03-31; until then, all access from SYS-E1 tunnels to the acquired-region management plane is blocked except through group jump hosts (POAM-010, POAM-024).
  3. The chatbot account recovery feature stays disabled until a compliant design passes testing (POAM-012).
- **Reauthorization:** annually, or when tenant partitioning is complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** tenant partitioning of the service assurance platform (2027-03-31); management plane migration in the acquired regions (2027-03-31); legacy billing system retirement in the acquired regions (2027-09-30); SBC replacement (2027-01-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Carrier OSS/BSS platform vice president | Accountable for the OSS/BSS and this SSP |
| Authorizing official equivalent | Group CISO with the Group Chief Risk Officer | Authorization decision; High risk acceptance |
| Division concurrence | Carrier division president | Accepts Moderate risks for the Carrier |
| CPNI compliance officer | Carrier Senior Vice President, Regulatory and Compliance | CPNI approvals, certification, breach determinations |
| Network operations owner | Carrier NOC director | Service assurance platform operations; Part 4 notices |
| Tenant owners | Engineering MNO general manager; Tower site operations director | Their tenants' users, data, and use of the platform |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Privacy oversight | Group Chief Privacy Officer | CPNI purposes and affiliate access rules |
| Independent assessor | Group internal audit | Assesses common controls once and samples division controls (P07) |

## 6. System Information Types and System Categorization
Information types are the closest matches in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer account and CPNI records (closest type: Customer Services) | **High** | Moderate | Moderate | Provisional Moderate, raised to High for aggregation: disclosure of CPNI and PII for millions of accounts would have a severe effect (CPNI breach duties, state notices in 14 states, SEC materiality). Care can run on offline summaries for up to 24 hours (P05 BP-C06) |
| Call detail and rating (closest type: Collections and Receivables) | **High** | Moderate | Low | 24 months of calling history for about 1.9 million lines; a known target of nation-state intrusions into U.S. carriers. Switches buffer CDRs for 72 hours (P05 BP-C09) |
| Network operations, configuration, and outage records (closest types: System and Network Monitoring; IT Infrastructure Maintenance) | Moderate | **High** | **High** | Altered element configurations could cause regional outages including 911. Outage detection and PSAP notices need the platform within 1 hour (P05 BP-C04, RTO 1 hour) |
| Tenant data of other divisions (Engineering customers' network data; tower lighting alarms) | Moderate | Moderate | **High** | Tower lighting alarms support aviation safety (P05 BP-T01); Engineering customers rely on 30-minute outage notices (BP-E01) |
| Information security (AAA, keys, logs) | High | High | Moderate | Compromise would expose every component and the management plane |
| **OSS/BSS category (high-water mark)** | **High** | **High** | **High** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **134 controls** in `control-implementation.csv`:
- 127 from the High baseline;
- 5 from the privacy baseline (PM-9, PT-2, PT-3, PT-4, PT-5), added because CPNI approvals, notices, and purposes are the platform's main privacy duties;
- 2 program management controls not in any baseline (PM-1, PM-2).

Other High-baseline controls are either fully inherited from the cloud providers (for example, most PE controls for cloud-hosted components, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, AC-18 wireless access controls for which group endpoint standards apply).

## 7. Authorization Boundary Description
- **Inside:** SYS-C1 (OSS and the service assurance platform, including the platform layer under all three tenants), SYS-C2 (BSS, including the legacy billing system in the acquired regions), SYS-C3 (mediation and CDR store), SYS-C4 (portal, app back end, API gateway), and SYS-C5 (management plane in 6 regional NOC data centers).
- **Outside, inherited (common control providers):** SYS-G1 identity, SYS-G2 SOC, SYS-G3 landing zones, and the cloud providers' facilities and hardware.
- **Outside, interconnected:** SYS-C6 voice core and SYS-C7 IP and access network (managed through SYS-C5); SYS-C9 contact center; SYS-C10 AI chatbot and voice agent (vendor SaaS calling the API gateway); SYS-E1 remote access gateways and collectors (Engineering); SYS-T2 RMUs and smart locks (Tower); the NG911 system service providers, signaling hubs, bill print vendor, and payment processor.
- **Tenants inside the boundary:** the Engineering and Tower tenants on the service assurance platform are inside the boundary at the platform layer. Their users and data are governed by their divisions under a tenant agreement that does not yet exist (POAM-026).
- **Excluded:** SYS-C8 lawful intercept, governed by the CALEA SSI policies. **Boundary weakness:** in the 2 acquired regions, its management path shares SYS-C5 segments (P01 TC-013).

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-C6 voice core to SYS-C3 mediation | Inbound | CDRs | Internal; collectors in regional NOCs |
| SYS-C7 network elements and SYS-C5 | Bidirectional | Configurations, alarms, syslog, provisioning | Internal |
| SYS-C9 contact center | Bidirectional | Account data, call recordings, IVR payments (tokenized) | CCaaS contract with CPNI and 24-hour incident notice terms |
| Outsourced contact center vendors | Agents use the SYS-C2 agent desktop | Account data, CPNI | Vendor contracts (one lacks 24-hour incident notice terms; POAM-016) |
| SYS-C10 AI chatbot and voice agent | Bidirectional through the API gateway | Account data, CPNI, transcripts | Vendor contract (training exclusion and transcript deletion terms added 2026-06; P10) |
| SYS-E1 Engineering MNO | Tenant on service assurance; tunnels into SYS-C5 in the acquired regions | Customer network alarms and tickets; Carrier tickets readable through the legacy role (**gap**) | **No** intercompany CPNI or interconnection agreement (POAM-009, POAM-026) |
| SYS-T2 Tower alarm center | Tenant on service assurance | Lighting and site alarms | No tenant agreement (POAM-026) |
| SYS-G2 SOC | Outbound | Logs (may contain CPNI) | Group logging standard; purpose not yet documented (PT-3) |
| FCC NORS and DIRS; CPNI breach reporting facility | Outbound (web portals) | Outage reports; breach reports | Regulatory filings |
| Bill print vendor; payment processor | Outbound | Bill images; payment tokens | Contracts with confidentiality terms |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| OSS applications and service assurance platform (SYS-C1) | Containers and managed databases | Provider A; DR in provider B | Carrier OSS/BSS platform vice president |
| BSS (SYS-C2) | Licensed application on cloud virtual machines and a managed database | Provider A; DR in provider B | Carrier billing vice president |
| Legacy billing system (acquired regions) | Virtual machines | Provider A (lifted from the acquired company's data center in 2025) | Carrier billing vice president |
| Mediation collectors and CDR store (SYS-C3) | Appliances in regional NOCs; object storage | Regional NOCs; provider A | Carrier billing vice president |
| Portal, app back end, API gateway (SYS-C4) | PaaS web app; managed API gateway; WAF | Provider A | Carrier digital channels director |
| Element managers, AAA servers, jump hosts, configuration backup servers, syslog collectors (SYS-C5) | On-premises servers and virtual machines | 6 regional NOC data centers | Carrier NOC director |
| Administrator endpoints | Managed laptops | Workforce locations | Group end-user services |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (134 controls) and `common-control-catalog.csv` (102 group common controls).

| Status | Controls |
|---|---|
| Implemented | 112 |
| Partially implemented | 21 |
| Planned | 1 |
| Not applicable | 0 |
| **Total** | **134** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or the cloud providers) | 78 |
| Hybrid (group provides the mechanism; the Carrier configures or operates part) | 24 |
| System-specific | 32 |

**The 21 partially implemented controls** cluster in four places:
- **Management plane in the acquired regions** (scenario gaps 1, 3, and 7): AC-2, IA-2, AC-17, SC-7, SI-2, RA-5, AU-6, SI-4.
- **The shared service assurance platform and affiliate use of CPNI** (gap 2): AC-3, AC-6, AC-21, PT-2, PT-3, AT-3, CA-3.
- **Customer authentication and CPNI evidence** (gap 4 and P08 readiness): IA-8, AU-12.
- **Cross-division incident and supply chain governance** (gaps 8 and 10): IR-4, IR-8, CP-4, SR-3.

**The planned control** is CM-12 (information location): a CPNI data map across all platforms and tenants, due 2027-03-31.

### 10.2 Common control inheritance by division
The common control catalog lists 102 controls provided by corporate. Inheritance is **documented for the Carrier** (2025 inheritance matrix), **for Engineering** (2026-03 inheritance matrix, which also carves the group services into the planned SOC 2 report, P09), and for the OSS/BSS (this plan). It is **not documented for the Tower division** (scenario gap 9). Until POAM-021 closes, the Tower division cannot show which of its safeguards for SYS-T1 to SYS-T3 are met by group controls; P07 found its CA-2 statements other than satisfied for this reason.

### 10.3 Control assessment status
Common controls were assessed once, and OSS/BSS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce and outsourced agents** authenticate through SYS-G1 federated sign-in with MFA (number matching). **IT administrators** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High system with remote and privileged access to CPNI.
- **Network element administrators** authenticate through TACACS+ backed by SYS-G1 with MFA, except in the acquired regions (gap 1; exception until 2027-03-31 under authorization condition 2).
- **Tenant operators** (Engineering, Tower) authenticate through SYS-G1 like any workforce user. The issue is authorization (AC-3), not authentication.
- **Customers** are non-organizational users. The CPNI rules set the floor: authentication "without the use of readily available biographical information, or account information" before online access, then a password (47 CFR 64.2010(c), (e)), and immediate notice of changes to passwords, backup authentication, online accounts, or the address of record (64.2010(f)). The portal and app meet this; the chatbot account recovery pilot did not and is disabled (POAM-012). The target recovery design uses a one-time code sent to the telephone number or email address of record.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10), CALEA SSI policies (8 current; 2 being refiled).

## 13. Acronym List and Glossary
- **AAA:** authentication, authorization, and accounting (TACACS+ and RADIUS for network devices)
- **BSS / OSS:** business support system (billing and care) / operations support system (inventory, provisioning, assurance)
- **CDR:** call detail record
- **Common control:** a control provided once by corporate and inherited by several systems
- **CPNI:** customer proprietary network information (47 U.S.C. 222(h)(1))
- **MNO:** Engineering's Managed Network Operations service
- **NOC:** network operations center
- **PSAP:** public safety answering point
- **RMU:** remote monitoring unit (tower lighting)
- **SBC:** session border controller
- **Service assurance platform:** fault monitoring, alarm correlation, and ticketing; part of SYS-C1, shared by three tenants
- **SSI:** system security and integrity (CALEA)

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-31 | Draft after P07 fieldwork | Carrier OSS/BSS platform vice president |
| 1.0 | 2026-09-17 | Approved with authorization conditions | Group CISO |
