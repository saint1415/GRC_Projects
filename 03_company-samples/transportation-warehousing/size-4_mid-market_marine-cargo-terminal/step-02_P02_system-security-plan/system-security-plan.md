# System Security Plan: Terminal Operations and Gate Platform (TOGP)

**Organization:** Cris Santos Company, Inc. (PE-backed marine cargo terminal operator, two Florida terminals) | **Tier:** Mid-Market | **Vertical:** Transportation and Warehousing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15
**Handling:** Contains network and security measure details that will become part of the Cybersecurity Plan. Handle as sensitive security information (SSI) under 49 CFR part 1520 (33 CFR 101.630(b); POL-04).

## 1. System Name and Identifier
Terminal Operations and Gate Platform (**TOGP**), identifier CSC-TOGP-01. The TOGP is the company's major system. It comprises SYS-01, SYS-02, SYS-04, SYS-05, SYS-07, the operations endpoints in SYS-08, SYS-10, SYS-13 and SYS-14 in `../00_company-facts.md`.

## 2. System Overview
The TOGP runs every cargo process in the BIA (P05) at Terminal 1 (container), Terminal 2 (breakbulk, project cargo and vehicles) and the off-dock depot: vessel and yard planning, equipment dispatch, three truck gates, customs release and hold status, EDI with carriers, trucking companies, two port community systems and the customs data exchange service, the customer portal and truck appointments, and billing. It supports about 20 vessel calls a week and about 4,000 truck gate transactions a day. Users are 600 employees, longshore labor who use vehicle-mounted terminals (VMTs), and about 1,200 trucking companies and cargo owners on the portal.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Terminal operating system (TOS), one instance for both terminals and the depot | Commercial software run by the company in the cloud workloads account (IaaS and managed database); TOS gate servers on premises |
| SYS-02 | Gate automation: OCR portals, TWIC readers, driver kiosks, gate transaction servers at three gates | On premises |
| SYS-04 | EDI gateway and integration services | Cloud workloads account (IaaS) |
| SYS-05 | Identity provider with SSO, MFA and conditional access | SaaS |
| SYS-07 | SD-WAN, internet firewalls, T1 OT zone firewall, T2 gate and yard network, VMT Wi-Fi, staff VPN | On premises and managed SD-WAN |
| SYS-08 | Operations endpoints: planner, superintendent and gate booth workstations, rugged tablets, VMTs | Company-managed |
| SYS-10 | Cloud landing zone: identity and security, shared services, workloads and backup accounts; standby region | Public cloud, vendor-agnostic (P04) |
| SYS-13 | SIEM operated by the MSSP; passive OT monitoring sensors at T1 | SaaS plus on-premises sensors |
| SYS-14 | Customer portal and truck appointment system (company-built) | Cloud workloads account (PaaS and IaaS) |

The crane and yard equipment controllers (SYS-03), CCTV and PACS (SYS-09), the ERP and HR SaaS (SYS-11) and the scheduling optimization service (SYS-12) connect to the TOGP as interconnected systems (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the TOGP |
|---|---|---|---|
| N48-49-R01 | USCG Cybersecurity in the Marine Transportation System | 33 CFR Part 101, Subpart F (101.600-101.670); 90 FR 6298 | Primary control requirement. The TOGP contains critical IT systems and connects to critical OT systems as defined in 101.615. Mapped in `control-implementation.csv` |
| MTSA | Facility security (FSPs, FSAs, TWIC access control, drills, records, audits) | 33 CFR Part 105 (105.220, 105.225, 105.305, 105.405, 105.415) | The FSA report must describe computer systems and networks (105.305(d)(2)(v)); PACS reader records are SSI (105.225(c)) |
| Reporting | Cyber incident reporting to the FBI, CISA and the COTP; MTSA reporting to the NRC | 33 CFR 6.16-1; 33 CFR 101.305 | Detection and logging must support immediate reporting (P08) |
| SSI | Protection of sensitive security information | 49 CFR 1520.9 | The Cybersecurity Plan is SSI (101.630(b)); this SSP is handled as SSI |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (4), (8) | Reasonable measures for driver and employee personal information held in the TOS gate module and the portal; breach notice (P08) |
| Shipping Act | Marine terminal operator duties | 46 U.S.C. 41106 | Berth windows and appointment slots must not give undue or unreasonable preference (relevant to SYS-12, P10) |
| Safety | OSHA marine terminal standards | 29 CFR part 1917 | Relevant to OT and the scheduling service (P10) |
| Contract | Carrier alliance agreement | Contract | SOC 2 Type 2 report on the portal and EDI services before the 2027-12-31 renewal (P09) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable: TSA rail, pipeline and aviation Security Directives (N48-49-R02 to R04); CMMC (N48-49-R07, no DoD contracts); SEC disclosure (N48-49-R08, privately held). CTPAT (N48-49-R05) is voluntary; the company is not a partner. PCI DSS: card payments use a hosted payment page run by a payment service provider, outside the TOGP (noted, not assessed).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-15, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the TOGP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change.
- **Coast Guard approval.** The approval that matters for the regulator is approval of the Cybersecurity Plan by the cognizant COTP for each terminal (101.630(d)). The company targets submission by 2027-05-28, ahead of the 2027-07-16 deadline (101.655).
### 4.3 System Operational Status
Operational. Major modifications planned:
- An OT zone and industrial firewall at T2, matching T1 (P01 R-002), due 2027-03-31
- Vendor remote access consolidated on the privileged remote access service for all 27 vendors with access (P01 R-003, R-018), due 2026-12-31
- A tested failover of the TOS to the standby region (P01 R-004), first test 2026-11-07
- Replacement of the T2 OCR servers and 2 T2 crane HMIs (P01 R-010), due 2027-03-31
- Privileged access management for directory, identity provider and TOS administrators (P01 R-009), due 2027-03-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the TOGP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Program strategy, board reporting, SSP review |
| Cybersecurity Officer (CySO) | Director of IT and Cybersecurity | CySO for both terminals (designated 2026-03-02); day-to-day control owner; Subpart F duties in 101.625 |
| Alternate CySO; security operations and GRC | Security Manager, 2 security analysts (one OT-focused), GRC analyst | Vulnerability management, MSSP liaison, GRC |
| Facility Security Officers | Director of Port Security (T1); T2 Security Lead (T2) | FSPs, TWIC and PACS, MTSA reporting, drills and records |
| Business process owners | Vice President, Terminal Operations; T1 and T2 General Managers; Depot Manager | TOS roles, gate procedures, manual release review |
| OT owner | Director of Maintenance and Engineering | Crane and yard equipment controllers; OEM access approvals |
| Application owners | TOS Application Manager; Director of Commercial and Customer Service (portal) | TOS configuration, portal development and releases |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment; future annual Plan audit (101.630(f)(4)) |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring of IT |
| Application support | TOS vendor | TOS support under contract |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Water transportation (vessel, yard and gate operations; container and vehicle location and status; hazardous cargo class and location) | Moderate | Moderate | Moderate | Wrong status or location data could release a held container or misplace hazardous cargo. Loss stops a terminal, but manual procedures limit the effect to about one shift before severe disruption (P05 MTD 4 to 12 h) |
| Logistics management (EDI with carriers, trucking companies, port community systems and the customs data exchange) | Moderate | Moderate | Moderate | Bills of lading and customs release status are commercially sensitive; false releases enable cargo theft (P01 R-012, R-019) |
| Customer services (portal accounts, appointments, invoices) | Moderate | Moderate | Moderate | Trucking companies depend on appointments to reach the gate; carrier alliance availability commitments (P09) |
| Personal identity and authentication (driver names and license numbers, TWIC reader records, workforce identities) | Moderate | Moderate | Low | Florida personal information (Fla. Stat. 501.171); TWIC reader records are SSI (105.225(c)) |
| System and network monitoring (security logs, OT monitoring) | Moderate | Moderate | Low | Needed for investigations and for evidence to the Coast Guard (101.640) |
| Revenue collection (billing, demurrage) | Low | Moderate | Low | Invoicing can wait 72 h (P05) |
| **TOGP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Availability and integrity were considered for High.** A multi-day outage at a port can cause regional economic disruption, which is part of the definition of a transportation security incident (33 CFR 101.105), and altered hazardous cargo locations could hurt people. The team kept both at Moderate for three reasons: manual gate and vessel procedures exist; each terminal is one of several at its port; and crane safety interlocks and operators in the cabs remain independent of the TOS. To compensate, the baseline adds integrity and availability tailoring: CP-7 and CP-9 statements cover the standby region and write-once backups, SI-7 covers PLC program integrity, and CA-8 adds penetration testing.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the TOS application servers, TOS database, EDI gateway, integration services and customer portal in the cloud workloads account;
- the identity, shared services and backup accounts and the standby region;
- the TOS gate servers, OCR servers, gate transaction servers and driver kiosks at T1, T2 and the depot;
- the SD-WAN, internet firewalls, the T1 OT zone firewall (its IT-facing side), the T2 gate and yard network, VMT Wi-Fi and the staff VPN;
- the identity provider tenant;
- operations workstations, gate booth workstations, 140 rugged tablets and 130 VMTs;
- the company's SIEM tenant and the T1 OT monitoring sensors.

**Interconnected, outside the boundary:**
- crane and yard equipment controllers, the crane management system and reefer monitoring (SYS-03, owned by the Director of Maintenance and Engineering);
- CCTV and PACS (SYS-09, owned by the Director of Port Security);
- the scheduling optimization service (SYS-12);
- ERP and HR SaaS (SYS-11);
- the TOS vendor's support access, the MSSP's platform and the cloud provider's infrastructure;
- carrier, trucking, port community system and customs data exchange partners.

**Boundary weakness.** At T2, mobile harbor crane controllers and the PACS sit on the same flat network as the in-boundary gate servers, so the boundary is not enforced there. The T2 OT zone project (P01 R-002, due 2027-03-31) will enforce it. At T1 the OT zone firewall enforces it today.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Protection | Agreement |
|---|---|---|---|---|
| Ocean carriers and T2 customers (16) | Bidirectional EDI | Bay plans, load and discharge lists, container and vehicle status | AS2 or SFTP for 14; **plain FTP for 2 (gap)** | Terminal services agreements |
| Trucking companies and cargo owners (about 1,200) | Inbound via the customer portal | Appointments, driver and truck details, availability, invoices | TLS; web application firewall | Portal terms of use |
| Port community systems (2 port authorities) | Bidirectional API | Vessel schedules, gate status | TLS with API keys | Lease and data sharing terms; **no interconnection security terms (gap, CA-3)** |
| Customs data exchange service | Inbound | Release and hold status from U.S. Customs and Border Protection | SFTP | Service agreement |
| Crane management system and crane controllers, T1 (SYS-03) | Bidirectional through the OT zone firewall | Job instructions, completions, positions | Allow-listed flows; unencrypted OT protocols | Internal interface document |
| Mobile harbor crane controllers, T2 (SYS-03) | Bidirectional on the flat network | Job instructions, completions | **No flow control (gap)** | Internal |
| PACS (SYS-09) | Inbound to gates | TWIC validation results | T1 segmented; T2 flat (gap) | Internal |
| Scheduling optimization service (SYS-12) | Bidirectional API | Move history, schedules, recommended plans | TLS; scoped API key | Service agreement; **security terms pending (P10)** |
| ERP (SYS-11) | Outbound from the TOS | Billable events | TLS | ERP SaaS contract |
| MSSP | Inbound logs; remote response actions | Security logs | TLS; MFA for MSSP analysts | MSSP contract; SOC 2 Type 2 |
| Crane OEMs and other vendors with access (27) | Inbound remote access | Diagnostics and support | T1 OEM via privileged remote access service; **others not (gap)** | Service contracts; 14 without notice clauses |
| Payment service provider | Customer redirect from the portal | Payment confirmations only (no card data) | TLS | Payment services agreement |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| TOS application servers (4) and batch server | Cloud virtual machines | Workloads account | TOS Application Manager |
| TOS database and standby replica | Managed database service | Workloads account; standby region | Director of IT and Cybersecurity |
| EDI gateway and integration services | Cloud virtual machines | Workloads account | TOS Application Manager |
| Customer portal (web tier, API tier, database) | Container and managed database services | Workloads account | Director of Commercial and Customer Service |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Director of IT and Cybersecurity |
| Network hub, cloud firewall, privileged access broker, log forwarding | Network and management services | Shared services account | Director of IT and Cybersecurity |
| Cloud identity federation, guardrails, posture management | Identity and policy services | Identity and security account | Security Manager |
| Identity provider tenant | SaaS | Identity vendor | Director of IT and Cybersecurity |
| TOS gate servers (T1 4, T2 2, depot 1), gate transaction servers (3) | Physical servers | Gate server rooms | TOS Application Manager |
| OCR servers (T1 4, T2 2) and 18 OCR portals | Physical servers and camera controllers | Gate complexes | T1 and T2 General Managers |
| Driver kiosks (18) | Kiosk PCs | Gate lanes | T1 and T2 General Managers |
| Internet firewalls, SD-WAN edges, T1 OT zone firewall, switches, Wi-Fi controllers | Network | T1, T2, depot | Director of IT and Cybersecurity; OT network engineer |
| Operations workstations (about 210), gate booth workstations (24), rugged tablets (140), VMTs (130) | Endpoints | All sites | Director of IT and Cybersecurity |
| SIEM tenant; T1 OT monitoring sensors (3) | SaaS; appliances | MSSP; T1 OT zone | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The TOGP uses the NIST SP 800-53B **Moderate** baseline (287 controls and enhancements), tailored as follows:
- **Documented here: 123 controls** in `control-implementation.csv`. They cover every SP 800-53 control mapped to a Subpart F measure in the P03 gap analysis (an author mapping), plus the Moderate controls that address the risks in P01 (segmentation, privileged and vendor access, monitoring, recovery, secure development of the portal).
- **Selected by tailoring (added), 5 controls:** CA-8 (penetration testing is required at Plan renewal, 101.650(e)(2)), PM-1, PM-2 and PM-9 (Subpart F requires a designated CySO and a risk-based Plan), and PM-16 (threat information sharing, 101.650(e)(3)(iii)).
- **Integrity and availability tailoring:** CP-7 and CP-9 cover the standby region and write-once backups; SI-7 covers PLC program integrity; SI-10 covers EDI release and hold messages.
- **Inherited without separate statements:** the remaining Moderate-baseline physical and environmental controls for cloud and SaaS data centers (for example PE-9 to PE-17) and platform-level SA and SC controls. They are inherited from the cloud provider, the identity provider, the MSSP and the TOS vendor, evidenced by their SOC 2 reports, and reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred or out of scope for this tier:** Moderate controls whose purpose applies only to federal systems, and controls with no Subpart F mapping and no Moderate-or-higher risk in P01. They are recorded as tailoring decisions and reviewed each year.

CSF 2.0 subcategories in the CSV come from the NIST CSF 2.0 to SP 800-53 crosswalk (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); the column is blank where the crosswalk lists none.

**Status of the 123 documented controls:**
| Status | Count |
|---|---|
| Implemented | 33 |
| Partially implemented | 87 |
| Planned | 3 |
| Not applicable | 0 |

**Inheritance of the 123 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 81 | Company |
| Hybrid | 34 | Cloud provider, identity provider, MSSP, TOS vendor, crane OEMs, privileged remote access service vendor |
| Common/Inherited | 8 | Identity provider (for example AC-2(1), IA-2(2)), cloud provider (CP-6, SC-5), MSSP (IR-7) |

Most Partially implemented statements share one pattern: the control works at T1 and in the cloud, but not yet at T2 or for OT. They trace to the 15 gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv` and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance. Given the Moderate categorization and the Subpart F requirement for MFA on password-protected IT systems (101.650(a)(4)), this is acceptable for general users.
- **Administrators.** Administrators will move to phishing-resistant authenticators (FIDO2 security keys) by 2027-03-31 (P01 R-009). Until then, cloud administration goes through the privileged access broker with just-in-time elevation.
- **Gate booths.** Gate clerks sign in to the TOS gate module with named accounts. Badge tap plus PIN replaces the phone prompt at shift change, because gate throughput cannot absorb it. The TOS gate module local accounts move into the identity provider by 2027-01-31 (P01 R-013).
- **OT.** HMIs in crane cabs cannot support MFA. They must not be remotely accessible, and their compensating controls (physical access, OT zone, monitoring) will be documented in the Cybersecurity Plan, as 101.650(a)(4) allows.
- **Customers.** Trucking companies and cargo owners use email-verified portal accounts with optional MFA. MFA for portal administrator accounts at trucking companies becomes mandatory by 2027-03-31 (P09 CC6.1). Truck drivers do not sign in to the TOGP; they are identified at the gate by TWIC or driver license and appointment number, under the FSPs.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register and appetite statements (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); Facility Security Plans and Facility Security Assessments (SSI, held by the FSOs).

## 13. Acronym List and Glossary
- **COTP:** Captain of the Port
- **CySO:** Cybersecurity Officer (33 CFR 101.615)
- **EDI:** electronic data interchange
- **FSO / FSP / FSA:** Facility Security Officer / Plan / Assessment (33 CFR Part 105)
- **HMI:** human-machine interface
- **KEV:** Known Exploited Vulnerability
- **MSSP:** managed security service provider
- **NRC:** National Response Center
- **OCR:** optical character recognition
- **OT:** operational technology
- **PACS:** physical access control system
- **PLC:** programmable logic controller
- **RTG / STS:** rubber-tired gantry crane / ship-to-shore crane
- **SSI:** sensitive security information (49 CFR part 1520)
- **TOS:** terminal operating system
- **TWIC:** Transportation Worker Identification Credential
- **VMT:** vehicle-mounted terminal

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the risk assessment and gap analysis | Security Manager |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Director of IT and Cybersecurity (CySO) |
