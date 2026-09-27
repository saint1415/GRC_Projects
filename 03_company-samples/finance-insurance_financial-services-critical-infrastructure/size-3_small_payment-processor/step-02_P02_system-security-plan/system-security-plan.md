# System Security Plan: Payment Processing Platform (PPP)

**Organization:** Cris Santos Company, LLC (payment processor serving merchants) | **Tier:** Small | **Vertical:** Financial Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Payment Processing Platform (**PPP**), identifier CSC-SYS-001. The PPP is also the company's PCI DSS cardholder data environment (CDE) plus the connected-to and security-impacting systems that PCI DSS brings into scope.

## 2. System Overview
The PPP authorizes, clears, and settles card payments for about 4,200 merchants: about 95 million transactions and $6.8 billion a year. It serves 60 workforce members, about 11,500 merchant portal users, and the consumers who pay on about 1,600 merchants' e-commerce sites.

**Major components (all in one public cloud tenant unless noted):**
- **SYS-01:** payment processing platform: authorization switch, merchant API gateway, terminal gateway, token vault, settlement and funding engine (containers, managed relational database, message queue)
- **SYS-02:** payment HSM service (FIPS 140-3 Level 3 validated), provided by the cloud provider
- **SYS-03:** merchant portal and virtual terminal
- **SYS-04:** hosted payment page and embedded payment form, served through a content delivery service

**Connected-to and security-impacting components:**
- **SYS-05:** identity provider (SaaS)
- **SYS-07:** SIEM service, EDR console, web application firewall
- **SYS-08:** source code repository and CI/CD pipeline (SaaS)
- **SYS-09:** fraud-detection model (licensed, hosted in the tenant)
- **SYS-13:** cloud data warehouse
- the administrative path from office laptops (SYS-06) through the bastion

The cloud is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| Primary (contract) | PCI DSS v4.0.1, assessed as a service provider (Visa Level 1: annual ROC by a QSA) | PCI SSC, June 2024; required through the sponsor agreement and card brand rules |
| Federal | FTC Standards for Safeguarding Customer Information (Safeguards Rule) | 16 CFR Part 314 |
| C-FINANCIAL-R01 | Computer-Security Incident Notification Rule, bank service provider notice | 12 CFR 53.4 (OCC-supervised sponsor bank). 12 CFR 304.24 (FDIC) applies once the second sponsor agreement is signed |
| C-FINANCIAL-R02 | Interagency Guidelines Establishing Information Security Standards | 12 CFR 30 App. B. Binds the sponsor bank, not the processor; reaches the PPP through the sponsor agreement's security and audit terms |
| Contract | Bank Service Company Act examination clause | 12 U.S.C. 1867(c): the sponsor bank's examiners may examine the settlement and funding services |
| State | Breach notification in each state where affected individuals reside; Florida as the worked example | Fla. Stat. 501.171 |
| Card brand | Visa What To Do If Compromised (supplemental requirements, v10.0, effective 2026-06-25) and other brands' incident rules through the sponsor bank | Visa Core Rules and supplements |
| Internal | Security policies POL-01 to POL-05 | P06 |

Not applicable (see `../00_company-facts.md` section 1 and P03):
- NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05): no New York license, registration, or charter.
- SEC Regulation SCI (C-FINANCIAL-R04): not an SCI entity.
- NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03): not a credit union and serves none.
- CIRCIA (C-FINANCIAL-R06): proposed only; no final rule. Tracked, not applied.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the COO on 2026-08-31.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions:
- The COO accepted continued operation of the PPP on 2026-08-31, with the conditions in the P07 POA&M.
- The majority owner and CEO accepted the High risks in P01 on 2026-08-31, each with a dated treatment plan.
- External validation: the QSA's 2025 AOC ("Compliant", 2025-12-01). The 2026 ROC fieldwork is 2026-11-02 to 2026-11-13.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Payment page script controls (R-001), due 2026-10-31
- 24x7 monitoring and egress intrusion detection (R-003), due 2026-12-31
- Second-region warm standby (R-006), due 2027-03-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CTO | The platform, engineering, and change management |
| Executive owner and risk acceptor (Moderate) | COO | Security and compliance program; PCI DSS responsibility (12.4.1); accepts Moderate risks |
| Risk acceptor (authorizing official equivalent) | Majority owner and CEO | Acceptance of High and Very High risks |
| Information Security Lead and Qualified Individual | IT Manager | Day-to-day security and PCI DSS lead; 16 CFR 314.4(a) designee |
| Platform operations | Platform Engineering Lead | Cloud tenant, pipeline, logging, key management operations |
| Compliance | Compliance and Risk Manager | Sponsor bank and card brand compliance, service providers, notices |
| Key custodians | 2 platform engineers and the Platform Engineering Lead | Dual control for HSM key ceremonies |
| Independent assessor | External QSA firm | Annual ROC |

## 6. System Information Types and System Categorization
Information types were matched to NIST SP 800-60 Vol. 2 Rev. 1 where a close type exists; key material and security logs are company-defined types. Impact levels follow FIPS 199 and were set by the company for its own context.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments (account data: PAN, expiry, cardholder name; transaction and settlement records) | High | Moderate | Moderate | Bulk PAN disclosure would harm millions of cardholders and could end the sponsor relationship (severe to catastrophic). Wrong settlement data is caught by daily reconciliation. Authorization MTD is 4 hours (P05) |
| Cryptographic key material (company-defined) | High | High | Moderate | Keys protect all stored PAN; altered keys would stop decryption |
| Merchant owner information (SSNs, bank accounts) | Moderate | Moderate | Low | Identity data for about 4,200 merchant owners; onboarding can wait days (P05 MTD 120 h) |
| Security logs and monitoring data (company-defined) | Moderate | Moderate | Moderate | Needed to detect and investigate attacks; PCI DSS requires 12 months of retention |
| **PPP category (high-water mark)** | **High** | **High** | **Moderate** | |

**Baseline:** the NIST SP 800-53B High baseline, tailored for a 60-person processor. The plan documents the 73 controls that implement PCI DSS, the Safeguards Rule, and the bank service provider notice duty (see `control-implementation.csv`). Every other High-baseline control is treated in one of two ways:
- **Inherited** from the cloud provider, the payment HSM service, and the SaaS providers, as evidenced by their AOCs and SOC 2 reports (P09).
- **Out of scope for this tier**, recorded as a tailoring decision, where the control's purpose applies only to federal systems. Examples are most PM-series program controls other than PM-2 and PM-9.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of provider services:
- **Inside:**
  - the cloud tenant (SYS-01 to SYS-04, SYS-09, SYS-13, the bastion, and the network, IAM, logging, and key management configuration)
  - the identity provider tenant (SYS-05)
  - the SIEM, EDR, and web application firewall configuration (SYS-07)
  - the repository and pipeline configuration (SYS-08)
  - the 9 administrator laptops (SYS-06), as the administrative access path
- **Outside (external services, interconnected):**
  - the cloud provider's infrastructure and payment HSM hardware
  - the content delivery service
  - the card networks and the sponsor bank
  - the fraud analytics vendor's training environment
  - the SaaS productivity suite (SYS-10), CRM (SYS-11), and ticketing (SYS-12). Card numbers found in SYS-10 and SYS-12 are a gap to remove, not a reason to bring them in scope.

The diagram is in P04 `cloud-architecture.md`. PCI DSS scope must be reconfirmed by 2026-09-30 (12.5.2.1). This boundary is the proposed scope.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Card networks (through links under the sponsor bank's membership) | Bidirectional | Authorization messages, clearing files, settlement reports, disputes | Sponsor agreement; network rules |
| Sponsor bank | Outbound | Merchant funding ACH file; settlement reports | Sponsor agreement (2023, renewed 2026-01-01) |
| Merchant terminals | Inbound | Card-present authorizations (TLS) | Merchant agreement |
| Merchant e-commerce sites and consumers' browsers | Bidirectional | Hosted payment page, payment form, tokens | Merchant agreement; integration guide |
| Merchant portal users | Bidirectional | Reports, refunds, virtual terminal entries | Merchant agreement and portal terms |
| Fraud analytics vendor | Outbound | Quarterly training extract (tokens and transaction features) | License and data processing terms (**no use limits or deletion terms; gap**) |
| Content delivery service | Bidirectional | Payment page files; DDoS protection | Service terms (**AOC missing; gap**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Authorization switch, API gateway, terminal gateway | Containers | Cloud tenant, 3 zones in the primary region | CTO |
| Token vault and settlement database | Managed relational database | Cloud tenant; snapshots to second region | Platform Engineering Lead |
| Message queue | Managed service | Cloud tenant | Platform Engineering Lead |
| Payment HSM service | Dedicated HSM service | Cloud provider | Platform Engineering Lead |
| Merchant portal and virtual terminal | Web application (containers) | Cloud tenant | CTO |
| Hosted payment page and payment form script | Static files and scripts | Cloud tenant, delivered through the content delivery service | CTO |
| Bastion | Virtual machine | Cloud tenant | IT Manager |
| Web application firewall | Managed service | Cloud tenant | IT Manager |
| Fraud-detection model | Container | Cloud tenant | Risk and Fraud Manager |
| Data warehouse | Managed analytics service | Cloud tenant | Platform Engineering Lead |
| Identity provider | SaaS | Identity vendor | IT Manager |
| SIEM and EDR | SaaS | Security vendors | IT Manager |
| Repository and pipeline | SaaS | Code hosting vendor | Platform Engineering Lead |
| Administrator laptops (9 of 72) | Endpoint | Florida office and remote | IT Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 73 controls:
- Implemented: 27
- Partially implemented: 40
- Planned: 6 (AU-5, CP-2, CP-4, CP-7, CP-10, SI-7)
- Not applicable: 0

Inheritance: 55 system-specific, 12 hybrid, 6 common or inherited from providers.

### 10.2 Control assessment status
Internal control assessment 2026-08-03 to 2026-08-07. See P07 `assessment-results.csv` and `poam.csv`. Independent validation is the QSA's annual ROC.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through the identity provider with a password and push MFA. Number matching or phishing-resistant MFA for all users is planned (R-018).
- **Administrators** (9) use phishing-resistant hardware keys and reach the CDE only through the bastion. This meets PCI DSS 8.4.2 and is appropriate for the High categorization.
- **Merchant portal users** (customer users) sign in with a password only; MFA is optional. This does **not** meet PCI DSS 8.3.10.1 or the Safeguards Rule MFA element (16 CFR 314.4(c)(5)). MFA will be required for users with refund, funding account, or virtual terminal rights by 2026-10-31 (R-004, R-025).
- **Consumers** paying on the hosted payment page are not account holders and do not authenticate to the PPP. Card brand authentication programs run through the issuers.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), risk register (P01), BIA (P05), gap analysis (P03), cloud control map (P04), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness (P09), AI assessment (P10), 2025 AOC, 2026-01 penetration test report.

## 13. Acronym List and Glossary
- **AOC:** Attestation of Compliance
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **EDR:** endpoint detection and response
- **HSM:** hardware security module
- **MFA:** multi-factor authentication
- **PAN:** primary account number (card number)
- **POA&M:** plan of action and milestones
- **PPP:** Payment Processing Platform
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan after the cloud migration | IT Manager |
