# System Security Plan: Property Management and Point-of-Sale Platform (PMPS)

**Organization:** Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) | **Tier:** Mid-Market | **Vertical:** Accommodation and Food Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Property Management and Point-of-Sale Platform (**PMPS**), identifier CSC-PMPS-01. The PMPS is the company's major system. It comprises SYS-01, SYS-03, SYS-04, SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, and SYS-12 in `../00_company-facts.md`, including the company-managed property side of the 4 franchised hotels.

## 2. System Overview
The PMPS supports every guest-facing and payment process in the BIA (P05): reservations and distribution, central reservations, check-in, key issuance, folios and payments, outlet service, night audit and settlement, guest safety, and guest communications. It serves 600 employees and about 260 contracted workers, about 147,000 stays a year, and about 1.05 million card transactions a year under 10 merchant accounts.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Resort PMS with the vendor's card vault, used by Resorts 1 and 2 and the CRO | Vendor SaaS; vendor PCI DSS service provider AOC and SOC 2 Type 2 |
| SYS-03 | Payment gateways; 14 validated P2PE devices at the resort front desks; 12 brand-mandated chip terminals at Hotels 3 to 6 | Service providers plus on-premises devices |
| SYS-04 | Resort outlet POS: Resort 1 cloud POS with 64 P2PE devices; Resort 2 legacy on-premises POS server, 38 workstations, 30 readers | Vendor SaaS (Resort 1); on-premises (Resort 2) |
| SYS-06 | SD-WAN and property networks at 7 sites | On-premises; SD-WAN managed service; brand-managed firewalls at Hotels 3 to 6 |
| SYS-07 | 520 PCs and laptops; 180 tablets and phones | Company-managed (brand image on 90 PCs at Hotels 3 to 6) |
| SYS-08 | Door lock systems (resort lock servers; cloud lock service at Hotels 3 to 6) | On-premises and vendor SaaS |
| SYS-09 | Identity provider with SSO and MFA | SaaS |
| SYS-10 | Cloud landing zone: identity and security, shared services, workloads, and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-12 | SIEM operated by the MSSP | SaaS |

The franchisor's platform (SYS-02), the booking engine and channel manager (SYS-05), email (SYS-11), and the AI and HR systems (SYS-13 to SYS-16) connect to the PMPS as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the PMPS |
|---|---|---|---|
| N72-R01 | PCI DSS v4.0.1 (contractual). The company validates with an SAQ D for Merchants, supported by a QSA firm, for 2026 | PCI SSC standard; merchant agreement; acquirer letter 2026-05-18 | Primary control requirement; mapped in `control-implementation.csv` |
| N72-R02 | FTC Act Section 5 and the FTC Rule on Unfair or Deceptive Fees | 15 U.S.C. 45(a), (n); 16 CFR Part 464 | Reasonable security for card and guest data; accurate privacy statements; total price in rate displays fed by the PMPS |
| N72-R03 | FTC Disposal Rule | 16 CFR 682.3 | Disposal of background-check reports |
| N72-R04 | State breach notification; Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security (501.171(2)), disposal (501.171(8)), and breach notice (P08) |
| State | Florida guest register | Fla. Stat. 509.101(2) | The PMS and brand PMS keep the register; at least 2 years must be available |
| State | FACTA receipt truncation | 15 U.S.C. 1681c(g) | POS and PMS receipts print no more than the last 5 digits |
| Contract | Franchise agreements (Hotels 3 to 6) | Contract | Brand IT and PCI standards; 24-hour notice of suspected compromise; brand access to property firewalls |
| Contract | REIT hotel management agreement (from 2027-01-01) | Contract | SOC 2 Type 2 on the hotel management platform (P09); 48-hour incident notice |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable:
- **CIRCIA (N72-R06).** Proposed only. If finalized as proposed, the company would likely be covered because it exceeds the SBA size standard (P03).
- **Illinois BIPA (N72-R05).** No Illinois operations or employees.
- **SEC cybersecurity disclosure rules.** Privately held.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the PMPS accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the CFO signs the 2026 SAQ D only with evidence for every answer; the audit committee receives POA&M and PCI status each quarter; re-decision by 2027-09-30 or after a major change.
### 4.3 System Operational Status
Operational. Major modifications planned:
- removal of stored card data from mailboxes and call recordings, with pause-and-resume recording in the CRO (due 2026-12-31);
- a PCI DSS responsibility matrix with the franchisor and segmentation of the Hotels 3 to 6 staff networks (due 2027-03-31);
- replacement of the Resort 2 legacy POS with a validated P2PE cloud POS (due 2027-06-30);
- replacement of the Resort 2 lock server (due 2027-03-31);
- SIEM onboarding of lock servers, the Resort 2 POS, and Hotels 3 to 6 (due 2027-01-31).

Each change alters PCI scope and triggers a scope review (PCI DSS 12.5.2).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the PMPS; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk and PCI status reporting |
| PCI compliance owner | Chief Financial Officer | Merchant agreement and acquirer; signs the SAQ D; service provider files |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Technical lead | IT Director | Infrastructure; PCI DSS technical lead; contingency planning |
| Security operations | Security Manager and 1 security analyst | Vulnerability management, SIEM and MSSP oversight |
| GRC | GRC Analyst | Risk register, standards, vendor reviews, evidence |
| Privacy and legal | General Counsel | Breach determinations; franchise and management agreements |
| Business unit owners | Hotel General Managers; Resort Directors of Food and Beverage; Director of Central Reservations; Resort Chief Engineers | Downtime procedures, device inspections, and access approvals |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |
| External platform owner | Franchisor | SYS-02, brand gateway, and property firewalls at Hotels 3 to 6 |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 where a close match exists. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payment card data (account data under PCI DSS) | Moderate | Moderate | Moderate | Disclosure causes card fraud, card brand and acquirer costs, and notice duties; serious but not catastrophic to the company; P05 MTD 8 hours for payments |
| Guest records (profiles, ID scans, stay history, guest register) | Moderate | Moderate | Moderate | ID numbers are personal information under Fla. Stat. 501.171(1)(g); wrong room or folio data harms guests; P05 MTD 4 hours for check-in |
| Room access (lock system data) | Low | Moderate | Moderate | Integrity and availability affect guest safety; P05 MTD 2 hours with emergency key cards as fallback |
| Financial management (folios, settlement, owner reporting) | Moderate | Moderate | Low | Night audit can run late (P05 MTD 24 hours) |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for card compromise investigations and 12-month log retention |
| **PMPS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability was considered for High.** Room access affects guest safety. The team kept availability at Moderate because existing key cards keep working when lock servers fail, emergency key cards and escorted entry are in place at every hotel, and the MTD of 2 hours can be met with these workarounds. To compensate, the plan adds contingency tailoring for lock servers (CP-2, CP-4, CP-9 statements).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the SYS-01 tenant configuration, users, roles, and interfaces;
- the payment devices at all 6 hotels (physical custody and inspection);
- the Resort 1 POS tenant and P2PE devices, and the Resort 2 POS server, workstations, and readers;
- the SD-WAN edges, resort firewalls, switches, and staff Wi-Fi; the company-owned switches and PCs behind the brand firewalls at Hotels 3 to 6;
- 520 PCs and laptops and 180 tablets and phones;
- the resort lock servers and encoders, and the company's tenant of the cloud lock service;
- the identity provider tenant;
- all 4 cloud accounts and their workloads;
- the company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the franchisor's PMS, central reservation system, loyalty platform, gateway, and property firewall management (SYS-02);
- the SYS-01 vendor's platform and card vault; the payment gateways and P2PE solution providers;
- the booking engine and channel manager (SYS-05); the productivity suite (SYS-11);
- the revenue-management system, chatbot, contact center, and HR systems (SYS-13 to SYS-16);
- the guest Wi-Fi and TV networks; the cloud provider's infrastructure; the MSSP's platform.

**PCI scope note.** Today the cardholder data environment (CDE) includes the Resort 2 outlet POS VLAN, the CRO PCs, the flat staff networks at Hotels 3 to 6, and every system that can reach them, including the shared mailboxes and the call recording store that hold card data. P03 section 1.2 shows how the 2027 changes shrink it. The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Franchisor platform (SYS-02) | Bidirectional (brand interfaces; brand-managed firewalls) | Reservations, guest and loyalty data, card authorizations at Hotels 3 to 6 | Franchise agreements; **no PCI DSS responsibility matrix or interconnection terms (gap, CA-3, SA-9)** |
| Resort payment gateway and P2PE solution provider | Bidirectional | Authorizations, tokens, settlement | Merchant agreement; gateway AOC 2026-03; P2PE Instruction Manual |
| Booking engine (SYS-05) | Inbound reservations and tokens | Direct bookings; payment form embedded in the resort websites | Contract; AOC 2026-01 |
| Channel manager (SYS-05) | Inbound reservations and virtual card numbers | Online travel agency bookings | Contract; **AOC dated 2025-04, more than 12 months old (gap)** |
| Revenue-management system (SYS-13) | Outbound stay data; inbound rates | Aggregated data; rates | Contract; SOC 2 Type 2 |
| Guest chatbot (SYS-14) | Bidirectional through the cloud integration | Availability, rates, guest questions | Contract; **no transcript retention or card-masking terms (gap, P10)** |
| CRO contact center (SYS-15) | Bidirectional; recordings stored in SYS-10 | Calls and recordings with spoken card data | Contract; **recordings hold card data (gap 2)** |
| Productivity suite (SYS-11) | Inbound email | Card authorization forms (**to be stopped**) | Service terms |
| Resort 2 POS vendor and lock vendor remote support | Inbound remote sessions | Administrative access | Service contracts; **no MFA or session approval (gap 5)** |
| MSSP | Inbound logs; remote response actions | Security logs | Contract; SOC 2 Type 2 |
| REIT-owned hotels (from 2027-01-01) | Bidirectional | Guest, reservation, and financial data for 2 managed hotels | Management agreement (P09) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| SYS-01 tenant | SaaS | SYS-01 vendor | Chief Operating Officer |
| Resort front desk P2PE devices (14) | Payment device | Resorts 1 and 2 | Chief Financial Officer |
| Brand chip terminals (12) | Payment device | Hotels 3 to 6 | Hotel General Managers |
| Resort 1 POS tenant and P2PE devices (64) | SaaS and payment devices | Resort 1 | Resort 1 Director of Food and Beverage |
| Resort 2 POS server, 38 workstations, 30 readers | On-premises server and devices | Resort 2 | Resort 2 Director of Food and Beverage |
| SD-WAN edges, firewalls, switches, staff Wi-Fi | Network | 7 sites | IT Director |
| PCs and laptops (520), tablets and phones (180) | Endpoint | All sites | IT Director |
| Resort lock servers (2) and encoders; cloud lock service tenant | Server, devices, SaaS | Resorts; lock vendor | Resort Chief Engineers |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Data warehouse, CRM, integration services, websites, call recording store | Managed database, object storage, serverless, containers | Workloads account | IT Director |
| Network hub, cloud firewall, VPN, privileged access broker, log pipeline | Network and management services | Shared services account | IT Director |
| Organization guardrails, posture and threat detection | Policy and security services | Identity and security account | Security Manager |
| Backup vault (second region, write-once) | Backup service | Backup account | IT Director |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The PMPS uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 154 controls** in `control-implementation.csv`. These cover every SP 800-53 control this plan maps to a PCI DSS v4.0.1 requirement for SAQ D (an author mapping), plus the Moderate controls that address the risks in P01 (segmentation, vendor access, logging, recovery, and supply chain).
- **Added by tailoring (2):** CA-8 (penetration testing, PCI DSS 11.4) and SR-9 (tamper resistance of payment devices, PCI DSS 9.5.1). Neither is in the Moderate baseline.
- **Program management (3):** PM-1, PM-2, and PM-9. They have no baseline but are needed for PCI DSS 12.1 and 12.3 and for the FTC reasonableness standard.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls. These are inherited from the SYS-01 vendor, payment providers, the identity vendor, the cloud provider, and the MSSP, and are evidenced by their AOCs and SOC 2 reports, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** the other Moderate controls with no PCI DSS mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the company does not develop software; the web agency's work is covered by SA-8). They are recorded as tailoring decisions and reviewed each year.
- **Franchised hotels.** At Hotels 3 to 6, controls on the brand PMS, brand gateway, and brand firewalls are the franchisor's. Until the responsibility matrix is signed (gap 3), the company treats them as Hybrid with the franchisor as provider and records the evidence gap.

**Status of the 154 documented controls:**
| Status | Count |
|---|---|
| Implemented | 51 |
| Partially implemented | 96 |
| Planned | 7 |
| Not applicable | 0 |

**Inheritance of the 154 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 101 | Company |
| Hybrid | 38 | SYS-01 vendor, identity vendor, payment gateways, MSSP, cloud provider, SD-WAN provider, franchisor |
| Common/Inherited | 15 | Identity vendor (for example AC-7, IA-2(8)), cloud provider (CP-6, SC-12), MSSP (IR-7, SI-4(2)), SYS-01 vendor (AC-12) |

The Partially implemented statements trace to the 13 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 32 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee. The QSA-supported PCI DSS assessment follows from 2026-10-05.

## 11. Digital Identity Acceptance Statement
- **Workforce.** Corporate, CRO, and resort users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Given the Moderate categorization and remote access to card and guest data, this meets the company's authenticator standard and PCI DSS 8.4.2 for SYS-01.
- **Administrators.** Administrator access to the cloud accounts and SYS-01 goes through the privileged access broker with just-in-time elevation. Administrators move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009).
- **Vendors.** The Resort 2 POS and lock vendors use shared logins on their own remote tools without MFA. This is not acceptable for access into the CDE (PCI DSS 8.4.3); the move to named accounts through the access broker is due 2026-11-30 (POAM-004).
- **Hotels 3 to 6.** Brand PMS users authenticate with brand-issued credentials and the franchisor's MFA. The company does not govern that identity system, and shared night-audit logins defeat it (POAM-002).
- **Guests.** Guests use the booking engine's and the brand's own accounts, which are outside this boundary.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis, SAQ scope, and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AOC:** attestation of compliance (PCI DSS)
- **ASV:** approved scanning vendor
- **CDE:** cardholder data environment
- **CRO:** central reservations office
- **EDR:** endpoint detection and response
- **MID:** merchant identification (merchant account)
- **MSSP:** managed security service provider
- **MTD, RTO, RPO:** maximum tolerable downtime, recovery time objective, recovery point objective
- **P2PE:** point-to-point encryption (PCI SSC validated solution)
- **PMPS:** Property Management and Point-of-Sale Platform
- **PMS:** property management system
- **POA&M:** plan of action and milestones
- **QSA:** Qualified Security Assessor
- **REIT:** real estate investment trust
- **SAQ:** self-assessment questionnaire
- **SD-WAN:** software-defined wide area network

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | GRC Analyst |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | IT Director |
