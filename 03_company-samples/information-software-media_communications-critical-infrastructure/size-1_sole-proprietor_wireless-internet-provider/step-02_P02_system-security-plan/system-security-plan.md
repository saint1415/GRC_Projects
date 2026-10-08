# System Security Plan (short form): ISP Operations Systems Profile

**Organization:** Cris Santos Company (owner-operated wireless internet service provider) | **Tier:** Sole Proprietorship | **Vertical:** Communications
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
ISP Operations Systems Profile (**IOSP**), identifier CSC-SYS-001.

## 2. System Overview
The IOSP is everything the owner uses to run internet and home phone service for about 310 rural accounts: billing and the customer portal, the VoIP reseller portal, the cloud radio controller, email and files, accounting, the AI support assistant, the owner's laptop and phone, and the management plane of the owner-operated network (edge router, core switch, access points, and customer radios). One person, the owner-operator, uses and runs it. Components are SYS-01 to SYS-08 in `../00_company-facts.md` section 3.

The tier default for this size is "the owner's core SaaS stack". The boundary adds the network management plane because, for a WISP, the network is the service and the router is the most likely way into CPNI (P01 R-001). There is no server room and no IaaS. Most SaaS safeguards are **inherited from the vendors**; the owner is responsible for identities, data handling, devices, network devices, and vendor terms (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| C-COMMUNICATIONS-R01 | FCC CPNI rules (through the home phone add-on only) | 47 U.S.C. 222; 47 CFR 64.2001-64.2011 |
| C-COMMUNICATIONS-R03 | CALEA system security and integrity | 47 U.S.C. 1001-1010; 47 CFR 1.20000-1.20008 |
| C-COMMUNICATIONS-R02 | Outage reporting for interconnected VoIP; 911 special facility contacts | 47 CFR 4.9(g), (h); 4.18 |
| C-COMMUNICATIONS-R05 | CIRCIA (proposed, not in force) | Proposed 6 CFR Part 226. Tracked only |
| Other FCC | Broadband transparency and consumer labels; interconnected VoIP 911 service | 47 CFR 8.1; 47 CFR 9.11 (not security rules; noted for completeness) |
| State | Breach notification | Fla. Stat. 501.171 |
| Internal | Information Security Policy | POL-01 (P06) |

Not applicable: SEC rules (C-COMMUNICATIONS-R06), submarine cable rules (C-COMMUNICATIONS-R04), and CMRS-only CPNI rules (64.2010(h)). Broadband usage data is not CPNI while broadband is an information service (P03 section 1).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-operator on 2026-08-31.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner-operator accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-009) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: router firmware update and management filter rework (2026-09-15); encrypted VoIP signaling on all ATAs (2026-12-31); second upstream circuit under evaluation (2027).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, privacy lead, risk acceptor, CPNI certifying officer, CALEA senior officer | Owner-operator | Every role (designated in writing in POL-01 4.2) |
| Technical support | On-call network consultant (confidentiality and security terms since 2026-07-17) | Router and outage help on request, through the VPN, in sessions the owner approves |
| Field support | Tower and installation contractor | Climbs and radio installs; no CPNI access |
| Service providers | Billing platform vendor, wholesale VoIP provider, radio vendor, email provider, accounting SaaS vendor | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type | C | I | A | Rationale |
|---|---|---|---|---|
| CPNI and subscriber information (call detail, VoIP features, account and billing data) | Moderate | Moderate | Low | Disclosure triggers CPNI breach duties and harms customers; wrong data misbills customers; billing can wait days (P05 BP-04 MTD 120 h) |
| Network management and service delivery (router, radio, and 911 address configuration) | Moderate | Moderate | Moderate | Tampering can intercept or cut service; a wrong 911 registered address can misdirect help; outage over 8 hours passes the BP-01 and BP-02 MTD |
| **IOSP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

Information types follow the intent of NIST SP 800-60; the security categorization uses FIPS 199 impact levels.

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the CPNI "reasonable measures" duty (64.2010(a)) and the network security practices that matter most for a one-person ISP (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the billing vendor's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's accounts and settings in SYS-01, SYS-02, SYS-03, SYS-04, SYS-07, and SYS-08; the laptop and phone; the edge router, core switch, access points, backhaul radios, customer radios, and ATAs, as far as their management and configuration go; paper sign-up forms in the home office.
- **Outside (external services):** the vendors' platforms, the upstream fiber network, the wholesale VoIP switching and 911 routing, the payment processor, the site landlords' premises, and customers' own home networks.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Wholesale VoIP provider | Line orders, 911 registered addresses, CDRs, porting requests | Wholesale reseller agreement (covers 911 and lawful intercept support; **no security terms or review**) |
| Billing platform vendor | Subscriber accounts, invoices with home phone toll detail, text-line and chat transcripts | SaaS terms; SOC 2 Type 2 report reviewed 2026-07-23 |
| AI support assistant (billing vendor add-on and its model provider) | Customer messages; account data it reads | Add-on terms; **turned on without a review (P10)** |
| Payment processor | Card and bank details on its hosted pages | Merchant agreement |
| Bookkeeper | Monthly billing summaries | Engagement letter |
| Network consultant | Router configuration and traffic seen during support | Confidentiality and security terms (2026-07-17) |
| Upstream fiber provider | All subscriber traffic in transit | Service agreement |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Billing platform tenant (SYS-01) | SaaS | Owner-operator |
| VoIP reseller portal account (SYS-02) | SaaS | Owner-operator |
| Email and files (SYS-03) | SaaS | Owner-operator |
| Cloud radio controller tenant (SYS-04) | SaaS | Owner-operator |
| Edge router, core switch, 4 sites of access points and backhaul, about 310 customer radios, 52 ATAs (SYS-05) | Network devices | Owner-operator |
| Laptop and phone (SYS-06) | Endpoints | Owner-operator |
| Accounting tenant (SYS-07) | SaaS | Owner-operator |
| AI support assistant (SYS-08) | SaaS add-on | Owner-operator |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 4
- Partially implemented: 21
- Planned: 3

Inheritance: 14 hybrid (a vendor operates the mechanism and the owner configures or uses it correctly) and 14 the owner's alone (AC-17, AT-2, AU-6, CA-2(1), CM-3, CM-6, CP-2, IA-5, IR-6, IR-8, RA-3, RA-5, SA-9, SC-7). None is fully inherited, because the owner always keeps identities, data, and the network.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 with written CPNI and CALEA officer designation; vendor terms (SA-9) |
| Identify | Risk assessment (RA-3); BIA (P05); advisory tracking and port checks (RA-5, planned) |
| Protect | MFA (IA-2(1), gap on the VoIP portal); customer authentication for CPNI (IA-8); management filtering (SC-7); firmware (SI-2) |
| Detect | SaaS sign-in logs (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Network intrusion runbook and CPNI breach notice (IR-8, IR-6) |
| Recover | Vendor backups and router configuration copies (CP-9); emergency access envelope (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-07-20 to 2026-07-24 with the network consultant. See P07.

## 11. Digital Identity Acceptance Statement
The owner's email, billing platform admin, and radio controller accounts require a password and a second factor on the owner's phone, which is appropriate for administrative access to CPNI at a Moderate categorization. The VoIP reseller portal uses a password only until MFA is turned on (2026-09-15). Customers authenticate to the portal with passwords set through a link to the email of record, which meets 47 CFR 64.2010(c) and (e). The AI support assistant may show CPNI only inside an authenticated portal session (POL-01 7.8).

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **ATA:** analog telephone adapter (connects a home phone to the VoIP service)
- **CALEA:** Communications Assistance for Law Enforcement Act
- **CDR:** call detail record
- **CPNI:** customer proprietary network information (47 U.S.C. 222(h)(1))
- **IOSP:** ISP Operations Systems Profile
- **MFA:** multi-factor authentication
- **WISP:** wireless internet service provider

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-operator |
