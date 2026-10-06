# System Security Plan: Service Ticketing and Point-of-Sale Platform (STPP)

**Organization:** Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) | **Tier:** Mid-Market | **Vertical:** Other Services (except Public Administration)
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Service Ticketing and Point-of-Sale Platform (**STPP**), identifier CSC-STPP-01. The STPP is the company's major system. It comprises SYS-01, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07, SYS-09, SYS-10, and SYS-11 in `../00_company-facts.md`.

## 2. System Overview
The STPP runs every step of a repair across 34 Florida stores, the Depot, the contact center, and the digital channel: intake and consent at the counter, diagnostics and repair at the bench, data recovery at the Depot lab, protection plan claims from Partners P1 and P2, mail-in orders and checkout, payment, and release. It serves 600 workforce members, about 1,000 tickets a business day, and about 1.9 million customer records.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Ticketing and POS platform: tickets, customer records, POS, invoicing, inventory, status portal, SMS and email | Vendor SaaS (enterprise tier); vendor SOC 2 Type 2 |
| SYS-03 | Identity provider with SSO, MFA, and conditional access | SaaS |
| SYS-04 | Cloud landing zone: security and identity, shared services, workloads, and backup accounts | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-05 | Company-built mail-in portal (with the checkout page) and partner integration API | Containers in the workloads account |
| SYS-06 | Data recovery lab: storage array (about 95 TB used), 14 imaging workstations | On-premises at the Depot |
| SYS-07 | 238 technician bench workstations | On-premises at stores and the Depot |
| SYS-09 | Site networks at 34 stores, the Depot, and the corporate office on SD-WAN | On-premises; SD-WAN managed service |
| SYS-10 | 260 office endpoints and 120 counter tablets | Company-managed |
| SYS-11 | EDR and SIEM operated by the MSSP | SaaS |

The payment processor's P2PE terminals and payment gateway (SYS-02), the manufacturer portals (SYS-08), the contact center platform (SYS-12), and the AI services (SYS-13) connect to the STPP as external services (section 8).

**What the system protects beyond its own data.** Customer devices under repair connect to bench PCs for diagnostics and data transfer. Their content (photos, messages, health and location data, saved credentials) is not stored in the STPP by design, but it passes through it, and recovered data is stored in the lab. The plan therefore treats bench PCs, the lab, and device handling as part of the system.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the STPP |
|---|---|---|---|
| N81-R01 | FTC Act Section 5: unfair or deceptive practices | 15 U.S.C. 45(a)(1), 45(n) | Reasonable security for customer devices and data; privacy and AI claims must be true |
| N81-R02 | State breach and data security laws; Florida as the worked example | Fla. Stat. 501.171(2) to (6), (8) | Reasonable measures, breach notice, third-party agent duties, disposal of customer records |
| N81-R03 | PCI DSS v4.0.1 (contractual), validated on SAQ P2PE and SAQ A | Merchant agreement; acquirer letter 2026-04-15 | Keeps card data out of the STPP; checkout page script protection; terminal custody |
| N81-R04 | FTC Disposal Rule, for background check reports only | 16 CFR 682.3 | Disposal of consumer reports in SYS-14 (outside the boundary; noted) |
| N81-BM | NIST CSF 2.0 (voluntary benchmark); NIST SP 800-88 Rev. 2 for sanitization | NIST CSWP 29; SP 800-88r2 (September 2025) | Benchmark for the gap analysis (P03); sanitization method |
| Contract | Manufacturer A and B program agreements | Program agreements (fictional terms) | Named MFA accounts, consent-limited access, 24-hour incident notice |
| Contract | Partner P1 and P2 agreements | Partner agreements (fictional terms) | Claim data use limits, 48-hour breach notice, SOC 2 Type 2 from 2027 (P09) |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

Not applicable: the FTC Safeguards Rule (no consumer credit), COPPA (not directed to children), HIPAA (not a covered entity; policy declines business associate work), and the Florida Digital Bill of Rights (revenue threshold). Reasons are in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-17, after the control assessment (P07) and at the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the STPP accepted with conditions, 2026-09-17.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (a new region, an acquisition, or a new partner integration).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Standard bench image (session recording, USB blocking, EDR) at the remaining 14 stores (due 2027-03-31)
- Bench and customer-device VLAN at the 12 older stores (due 2027-06-30)
- SYS-01, lab storage, and portal logs into the SIEM with bulk export alerts (due 2027-01-31)
- Script inventory and change detection for the mail-in checkout page (due 2026-11-30, before the SAQ A attestation)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the STPP; accepts Moderate risk; executive sponsor |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Strategy, board reporting, SSP review |
| Information Security Officer | IT Director | Day-to-day control owner; contingency planning |
| Security operations and GRC | Security Manager, security analyst, GRC Analyst | Monitoring, vulnerability management, MSSP oversight, risk register, POA&M, vendor reviews |
| Privacy | Privacy and Compliance Manager | Retention, privacy notices, breach determinations with the General Counsel |
| Application owner (SYS-05) | Digital Engineering Manager | Secure development and change control for the portal and partner API |
| Data custodian (recovered data) | Data Recovery Manager | Lab storage, retention, and deletion of recovered data |
| Business unit owners | Director of Retail Operations; Depot Director; Director of Partner Programs; Director of Customer Experience | Device custody, PIN pad inspections, partner terms, downtime procedures |
| PCI DSS and contracts | Chief Financial Officer | Merchant agreement, SAQ attestations, vendor contracts with the General Counsel |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types were chosen as the closest matches in NIST SP 800-60 Vol. 2 Rev. 1 (customer services, collections and receivables, personal identity and authentication, and system and network monitoring), adapted to a private business. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Customer records and repair tickets (names, contact details, device identifiers, passcodes until purged) | Moderate | Moderate | Moderate | Exposure of passcodes and credentials enables account takeover and is a breach under Fla. Stat. 501.171; wrong records mean devices released to the wrong person; intake and release stop within one store day (P05 MTD 8 h) |
| Customer device content in custody and recovered data | Moderate | Moderate | Low | Serious, not catastrophic, harm to each individual if exposed; recovery work can pause (P05 BP-08 MTD 72 h) |
| Protection plan claims and repair outcomes | Moderate | Moderate | Moderate | Claim data is personal information held as the partners' agent; outcomes drive partner settlement, so errors cause financial harm; acknowledgement expected within 4 business hours (P05 BP-05) |
| Payment and invoicing (truncated card data, business account ACH details) | Moderate | Moderate | Moderate | Card data stays in P2PE terminals and the gateway; ACH details enable payment fraud |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations and partner notices |
| **STPP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Why not High confidentiality.** A bulk exposure of customer records or recovered data would be serious for the company and harmful to individuals, but it would not threaten life, critical services, or the company's existence in FIPS 199 terms. The company compensates with the extra technician access controls (AC-6, MP-7, PS-6, AT-2(2)) this plan adds.

**Why not High integrity for partner outcomes.** Partners reconcile outcomes against their own claim records and pay weekly, so errors are caught before money moves in most cases. To compensate, SI-7 and SI-10 statements cover message validation and a daily outcome reconciliation (planned).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the SYS-01 tenant configuration, roles, fields, and audit settings;
- the identity provider tenant;
- all 4 cloud accounts and their workloads (portal, partner API, delivery storage, chatbot connector, reporting database, backups);
- the lab storage array and imaging workstations;
- 238 bench workstations, 260 office endpoints, and 120 counter tablets;
- site networks at 34 stores, the Depot, and the corporate office;
- the company's SIEM tenant and EDR configuration.

**Outside the boundary (external services, interconnected):**
- the SYS-01 vendor's platform and its subservice providers;
- the cloud provider's infrastructure;
- the payment processor's P2PE solution, terminals, and payment gateway (SYS-02);
- the Manufacturer A and B portals and tools (SYS-08);
- the contact center platform (SYS-12) and AI services (SYS-13);
- Partners P1 and P2, the recycler, and the courier.

**Customer devices** are outside the boundary but connect to bench PCs inside it. The rules for handling them are part of this plan (AC-6, MP-6, MP-7). The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Payment processor (SYS-02 terminals) | Terminal to processor (encrypted in the device) | Card data; the STPP receives only approval and truncated number | Merchant agreement; P2PE Instruction Manual |
| Payment gateway (hosted payment fields on the checkout page) | Customer browser to gateway | Card data entered in the gateway's frame; the portal receives a token and approval | Merchant agreement; gateway terms |
| Partners P1 and P2 (partner integration API) | Bidirectional, mutual TLS | Claims in; status, outcomes, and costs out | Partner agreements; **no technical interconnection schedule (gap, CA-3)** |
| Manufacturer A and B portals (SYS-08) | Bidirectional | Device serials, repair details, customer names for warranty claims | Program agreements |
| Contact center platform (SYS-12) | Bidirectional (ticket lookups) | Customer names, ticket status, call recordings | Vendor contract; **AI add-on has no data-use terms (gap)** |
| Chatbot service (SYS-13, AI-001) | Bidirectional through the connector function | Customer questions, first name, ticket status | **No data-use terms (gap)** |
| Diagnostics service (SYS-13, AI-002) | Outbound logs and photos, inbound suggestions | Diagnostic logs, damage photos | **No data-use terms (gap)** |
| MSSP (SYS-11) | Inbound logs; remote response actions | Security logs | MSSP contract; SOC 2 Type 2 |
| Business accounts | Outbound | Recovered data (links or encrypted drives), invoices | Service contracts |
| Courier | Physical | Mail-in devices | Shipping account terms only (**gap**) |
| Certified electronics recycler | Physical | Recycling lots and retired equipment | Service contract; **lot-level certificates only (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 tenant | SaaS | Ticketing and POS vendor | Chief Operating Officer |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Organization guardrails, cloud identity federation, posture service | Identity and policy services | Security and identity account | Security Manager |
| Network hub, cloud firewall, VPN to SD-WAN, log pipeline and locked log bucket | Network and management services | Shared services account | IT Director |
| Mail-in portal and checkout page; partner integration API; API gateway and web application firewall | Containers and managed gateway | Workloads account | Digital Engineering Manager |
| Recovered-data delivery storage | Object storage | Workloads account | Data Recovery Manager |
| Chatbot connector function | Serverless function | Workloads account | Director of Customer Experience |
| Reporting database | Managed database | Workloads account | Chief Financial Officer |
| Secrets service and key management | Managed services | Workloads account | Security Manager |
| Backup vault (30-day write-once) and SYS-01 weekly export | Backup service and object storage | Backup account (second region) | IT Director |
| Lab storage array and 14 imaging workstations | On-premises | Depot lab | Data Recovery Manager |
| Bench workstations (170 store, 68 Depot) | Endpoint | Stores and Depot | Depot Director (Depot); Director of Retail Operations (stores) |
| Office endpoints (260) and counter tablets (120) | Endpoint | All sites | IT Director |
| SD-WAN edges, firewalls, switches, Wi-Fi | Network | 34 stores, Depot, corporate office | IT Director |
| SIEM tenant and EDR console | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The STPP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 110 controls** in `control-implementation.csv`. They cover the controls that carry the company's legal and contractual duties (FTC Act Section 5, Fla. Stat. 501.171, PCI DSS, the manufacturer and partner agreements), the controls that address the Moderate-or-higher risks in P01, and core hygiene.
- **Selected by tailoring (added):** CA-8 (penetration testing; the company builds internet-facing software), PM-2, and PM-9 (program roles and risk strategy).
- **Device-handling emphasis:** AC-6, AC-20, AT-2(2), MP-6, MP-7, and PS-6 statements cover what technicians may do with customer devices, because that is the risk that sets this business apart.
- **Inherited without separate statements:** the remaining physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SC and SA controls, inherited from the SYS-01 vendor, the identity vendor, the cloud provider, the MSSP, and the payment processor, evidenced by their SOC 2 Type 2 reports or PCI DSS attestations (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no legal or contractual driver and no Moderate-or-higher risk (for example SA-15 development process standards beyond SA-11, and PT-series privacy controls handled by the privacy program). They are recorded as tailoring decisions and reviewed yearly.

**CSF 2.0 column.** The `csf2_subcategories` column comes from NIST's CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). For 15 controls that NIST's references do not map (for example AC-11, MP-6, PS-3), the column gives an author mapping and says so.

**Status of the 110 documented controls:**
| Status | Count |
|---|---|
| Implemented | 41 |
| Partially implemented | 64 |
| Planned | 5 |
| Not applicable | 0 |

**Inheritance of the 110 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 79 | Company |
| Hybrid | 24 | SYS-01 vendor, identity vendor, cloud provider, MSSP, payment processor |
| Common/Inherited | 7 | Identity vendor (AC-2(1), AC-7, IA-2(1), IA-2(2), IA-2(8)), SYS-01 vendor (AC-12), cloud provider (SC-12) |

The Partially implemented and Planned statements trace to the 13 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The 5 Planned controls are all contingency and exercise controls (CP-2, CP-3, CP-4, CP-10, IR-3).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 36 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All named users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Counter staff use badge tap plus PIN on managed counter tablets for named sessions inside a store, which the company accepts because the tablets are managed, fixed to the counter network, and lock after 2 minutes.
- **Exceptions.** Manufacturer portal and contact center accounts are local named accounts outside the identity provider (gap 7). They are accepted until 2027-03-31 only where the vendor's own MFA is enforced.
- **Administrators.** Administrators will move to phishing-resistant authenticators (security keys) by 2027-06-30 (P01 R-021). Until then, cloud administration uses just-in-time elevation.
- **Customers.** Customers use the status portal with a ticket number and a one-time code sent to the phone on file. Release requires photo ID or the one-time code. Business account delivery links will require a one-time code by 2026-12-31 (P01 R-024).
- **Partners.** Partner systems authenticate to the partner API with mutual TLS certificates and per-partner keys, rotated yearly.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **CUEC:** complementary user entity control (in a SOC 2 report)
- **EDR:** endpoint detection and response
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **P2PE:** point-to-point encryption
- **POA&M:** plan of action and milestones
- **SAQ:** self-assessment questionnaire (PCI DSS)
- **SD-WAN:** software-defined wide area network
- **STPP:** Service Ticketing and Point-of-Sale Platform

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Operating Officer | IT Director (Information Security Officer) |
