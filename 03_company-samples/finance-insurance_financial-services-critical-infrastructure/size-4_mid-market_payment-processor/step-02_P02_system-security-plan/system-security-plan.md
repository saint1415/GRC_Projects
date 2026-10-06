# System Security Plan: Payment Processing Platform (PPP)

**Organization:** Cris Santos Company, Inc. (PE-backed payment processor serving merchants) | **Tier:** Mid-Market | **Vertical:** Financial Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

## 1. System Name and Identifier
Payment Processing Platform (**PPP**), identifier CSC-PPP-01. The PPP is the company's major system and its PCI DSS cardholder data environment (CDE), plus the connected-to and security-impacting systems that PCI DSS brings into scope. It comprises SYS-01 to SYS-07, SYS-09 to SYS-12, and SYS-16 in `../00_company-facts.md`, and the administrative access path from SYS-08.

## 2. System Overview
The PPP authorizes, clears, and settles card payments for about 31,000 merchants: about 820 million transactions and $38 billion a year. It serves 600 workforce members, about 64,000 core merchant portal users, about 15,000 Integrated Payments partner and merchant portal users, 420 ISV partners, and the consumers who pay on merchants' e-commerce sites.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Core payment platform: authorization switch, merchant API gateway, terminal gateway, token vault, recurring billing | Cloud A CDE accounts (primary and secondary region); containers, managed relational database, message queues (PaaS) |
| SYS-02 | Settlement and funding engine: clearing, reconciliation, merchant funding, chargebacks | On premises: primary colocation cage (Florida) and DR cage (outside Florida) |
| SYS-03 | Payment HSMs | Company-owned HSMs in both cages; Cloud A payment HSM service |
| SYS-04 | Merchant portal and virtual terminal (core) | Cloud A |
| SYS-05 | Hosted payment page and embedded payment form (core) | Cloud A, through a content delivery service |
| SYS-06 | Integrated Payments gateway (acquired 2025-11-03): partner API, hosted payment fields, token vault, partner portal | Cloud B, 3 accounts |

**Connected-to and security-impacting components:**
| ID | Component | Hosting |
|---|---|---|
| SYS-07 | Workforce identity provider and PAM vault | SaaS |
| SYS-09 | SIEM (monitored 24x7 by the MSSP), EDR, web application firewalls, network intrusion detection, file integrity monitoring, payment page tamper-detection | SaaS and cloud services |
| SYS-10 | Source code repositories and CI/CD pipelines (two instances) | SaaS |
| SYS-11 | Fraud-detection model (AI-001) | Cloud A |
| SYS-12 | Data platform: data warehouse and model training environment | Cloud A analytics account |
| SYS-16 | Bank connectivity: managed file transfer servers and treasury workstations | Colocation cages |
| SYS-08 (part) | Administrator laptops, as the administrative access path into PAM | Headquarters, acquired office, remote |

The cloud is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the PPP |
|---|---|---|---|
| Primary (contract) | PCI DSS v4.0.1, assessed as a service provider (Visa Level 1: annual ROC by a QSA) | PCI SSC, June 2024; required through both sponsor agreements and card brand rules | Main control requirement; mapped in `control-implementation.csv` |
| Federal | FTC Standards for Safeguarding Customer Information (Safeguards Rule) | 16 CFR Part 314 | Program elements, MFA, encryption, monitoring, service provider oversight, incident response plan, board report, FTC notice |
| C-FINANCIAL-R01 | Computer-Security Incident Notification Rule, bank service provider notice | 12 CFR 53.4 (Bank A, OCC); 12 CFR 304.24 (Bank B, FDIC) | Settlement, reconciliation, and funding files are covered services; a 4-hour disruption must be reported to each affected bank (P05 section 7; P08) |
| C-FINANCIAL-R02 | Interagency Guidelines Establishing Information Security Standards | 12 CFR 30 App. B (Bank A); 12 CFR 364 App. B (Bank B) | Bind the banks, not the company; reach the PPP through the sponsor agreements' security and audit terms |
| Contract | Bank Service Company Act examination clause | 12 U.S.C. 1867(c) | The banks' examiners may examine the settlement and funding services |
| State | Breach notification in each state where affected individuals reside; Florida as the worked example | Fla. Stat. 501.171 | Notices as a third-party agent for merchants and as a covered entity for merchant owner data (P08) |
| Card brand | Visa What To Do If Compromised (supplemental requirements, v10.0, effective 2026-06-25) and other brands' incident rules through the sponsor banks | Visa Core Rules and supplements | 3-calendar-day reporting clocks (P08) |
| Contract | ISV partner agreements; merchant agreements | Contracts | 99.95% availability; security schedules for the 20 largest partners (gap, CA-3) |
| Internal | Security policies POL-01 to POL-05 and supporting standards | P06 | Policy basis for every control |

Not applicable (see `../00_company-facts.md` section 1 and P03):
- NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05): no New York license, registration, or charter.
- SEC Regulation SCI (C-FINANCIAL-R04): not an SCI entity; the company is not an SEC registrant.
- NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03): not a credit union and serves none.
- 12 CFR 225.303 (Federal Reserve bank service provider notice): no services for a Board-supervised banking organization.
- CIRCIA (C-FINANCIAL-R06): proposed rule only; no final rule. Tracked in P03, not applied.
- PCI PIN Security Requirements: the company does not acquire PIN transactions and holds no PIN keys.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer on 2026-09-15, after the control assessment (P07) and before the board audit committee meeting the same day. The CTO, as system owner, reviewed it.
### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decisions:
- **Decision:** continued operation of the PPP accepted with conditions, 2026-09-15.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High and Very High POA&M items in P07 must meet their milestones, and every item that would leave a PCI DSS requirement "not in place" must close or have an interim measure before ROC fieldwork starts on 2026-11-09. The audit committee receives POA&M status each quarter. Re-decision by 2027-09-30 or after a major change, including the migration of the Integrated Payments gateway into Cloud A.
- **External validation:** the QSA's 2025 AOC for the core platform ("Compliant", 2025-12-15) and the acquired gateway's 2025 AOC (2025-09-30). The combined 2026 AOC is due to both sponsor banks by 2026-12-15.
### 4.3 System Operational Status
Operational. Major modifications planned:
- Integrated Payments gateway onboarded to the SIEM, the MSSP, and PAM (due 2026-11-06), then migrated into the Cloud A landing zone (due 2027-09-30)
- MFA and dynamic risk analysis for Integrated Payments portal users (due 2026-10-30)
- Script controls and tamper-detection on the Integrated Payments hosted payment fields (due 2026-10-30)
- Replacement of the 4 unsupported settlement batch servers (due 2027-06-30)
- Automated authorization failover (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | CTO | Accountable for the PPP; engineering and change management for both platforms |
| Executive sponsor and risk acceptor (Moderate) | Chief Operating Officer | Security and compliance program; PCI DSS executive responsibility (12.4.1); accepts Moderate risks |
| Authorizing official equivalent (High and Very High) | Chief Executive Officer | Accepts High risks; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting; annual Qualified Individual report (16 CFR 314.4(i)) |
| Program strategy | vCISO (part-time contractor) | Program strategy, risk appetite, board reporting, SSP review |
| Qualified Individual and security lead | Director of Information Security | 16 CFR 314.4(a) designee; day-to-day control owner; PCI DSS program |
| Platform operations | VP Platform Engineering | Cloud A, colocation cages, key management operations, recovery |
| Acquired platform | Director of Integrated Payments Engineering | Cloud B gateway until migration |
| Settlement | Director of Settlement and Treasury Operations | Settlement, funding, bank connectivity |
| Compliance and third parties | Chief Risk and Compliance Officer | Sponsor bank and card brand compliance, service providers, model risk, notices |
| Key custodians | 6 named custodians (VP Platform Engineering, 3 site reliability engineers, 2 security engineers) | Dual control for HSM key ceremonies |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Independent assessor (PCI DSS) | External QSA firm | Annual ROC |
| Monitoring | MSSP | 24x7 SIEM and EDR monitoring |

## 6. System Information Types and System Categorization
Information types were matched to NIST SP 800-60 Vol. 2 Rev. 1 where a close type exists; key material and security logs are company-defined types. Impact levels follow FIPS 199 and were set by the company for its own context.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Payments (account data: PAN, expiry, cardholder name; transaction and settlement records) | High | High | Moderate | Bulk PAN disclosure from either token vault would harm millions of cardholders and could end both sponsor relationships (severe to catastrophic). Altered settlement or funding data could misdirect about $104 million of merchant funding a day; daily reconciliation catches errors, but not before funds move. Authorization MTD is 2 hours, but merchants keep offline floor limits and many have backup processors (P05) |
| Cryptographic key material (company-defined) | High | High | Moderate | Keys protect all stored PAN; altered or lost keys would stop decryption and settlement |
| Merchant owner information (SSNs, bank accounts) | Moderate | Moderate | Low | Identity data for about 31,000 merchant owners; onboarding can wait days (P05 MTD 120 hours) |
| Security logs and monitoring data (company-defined) | Moderate | Moderate | Moderate | Needed to detect and investigate attacks; PCI DSS requires 12 months of retention |
| **PPP category (high-water mark)** | **High** | **High** | **Moderate** | |

**Why High and not Moderate.** The Mid-Market tier guide expects a Moderate-impact major system. The PPP categorizes High for confidentiality and integrity for the same reasons as the Small sample, and more strongly at this volume: one compromise exposes card data across 31,000 merchants, and funding file integrity protects about $104 million a day. The plan therefore starts from the High baseline and tailors it, instead of starting from Moderate and adding controls.

## 7. Authorization Boundary Description
The boundary contains company-managed components and the company's configuration of provider services.

**Inside the boundary:**
- the Cloud A CDE production, CDE recovery, and non-CDE production accounts (SYS-01, SYS-04, SYS-05, SYS-11), the analytics account (SYS-12), and the network, IAM, logging, and key management configuration of the landing zone;
- the three Cloud B accounts (SYS-06);
- everything inside both colocation cages: settlement servers, databases, payment HSMs, firewalls, file transfer servers, tape library (SYS-02, SYS-03, SYS-16);
- the identity provider tenant and PAM vault (SYS-07);
- the SIEM, EDR, web application firewall, and tamper-detection configuration (SYS-09);
- the repository and pipeline configuration of both instances (SYS-10);
- the 136 administrator endpoints (SYS-08), as the administrative access path.

**Outside the boundary (external services, interconnected):**
- the Cloud A and Cloud B providers' infrastructure and the Cloud A payment HSM hardware;
- the colocation providers' buildings, power, cooling, and guards;
- the content delivery service and the MSSP's platform;
- the card networks and both sponsor banks;
- the 420 ISV partners' software;
- the SaaS productivity suite (SYS-15), onboarding and CRM (SYS-13), and support and contact center (SYS-14). Card data found in SYS-14 is a gap to remove, not a reason to bring it in scope.

The diagram is in P04 `cloud-architecture.md`. PCI DSS scope for the combined environment must be confirmed by 2026-10-16 (12.5.2.1, 12.5.3). This boundary is the proposed scope.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Card networks (links under the sponsor banks' memberships) | Bidirectional | Authorization messages, clearing files, settlement reports, disputes | Sponsor agreements; network rules |
| Bank A (OCC) | Outbound funding file; inbound settlement reports | Merchant funding ACH file; reconciliation data | Sponsor agreement (2017, renewed 2025) |
| Bank B (FDIC) | Outbound funding file; inbound settlement reports | Same, for Integrated Payments merchants | Sponsor agreement (2025-10-01) |
| Merchant terminals | Inbound | Card-present authorizations (TLS) | Merchant agreement |
| Merchant e-commerce sites and consumers' browsers | Bidirectional | Hosted payment page, payment form, tokens | Merchant agreement; integration guide |
| ISV partner software | Bidirectional | Partner API calls, hosted payment fields, tokens, reports | ISV partner agreement (**no security schedule for the 20 largest partners; gap**) |
| Cloud B gateway to core switch | Bidirectional | Authorization messages | Internal; private link (**not in the data-flow diagrams; gap**) |
| Data platform (SYS-12) | Inbound | Tokenized transactions for model training | Internal; PAN block on load |
| Vendor merchant risk scoring service | Outbound | Merchant owner and business data for onboarding scores | Contract and data processing terms |
| MSSP | Inbound logs; remote response actions | Security logs | Contract; SOC 2 Type 2 |
| Content delivery service | Bidirectional | Payment page files; DDoS protection | Service terms; AOC on file |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Authorization switch, API gateway, terminal gateway | Containers | Cloud A CDE accounts, 3 zones in the primary region; warm standby in the secondary region | CTO |
| Token vault database (core) | Managed relational database | Cloud A CDE accounts | VP Platform Engineering |
| Message queues | Managed service | Cloud A | VP Platform Engineering |
| Payment HSM service | Dedicated HSM service | Cloud A provider | VP Platform Engineering |
| Merchant portal and virtual terminal | Web application (containers) | Cloud A | CTO |
| Hosted payment page and payment form script | Static files and scripts | Cloud A, through the content delivery service | CTO |
| Integrated Payments gateway, hosted payment fields, partner portal | Containers | Cloud B production account | Director of Integrated Payments Engineering |
| Integrated Payments token vault | Managed relational database; provider general key management service | Cloud B | Director of Integrated Payments Engineering |
| Settlement and funding engine (batch servers, 4 out of support) and settlement database | Physical servers | Primary cage; DR cage | Director of Settlement and Treasury Operations |
| Payment HSMs (2 per cage) | Hardware appliances | Both cages | VP Platform Engineering |
| Managed file transfer servers and treasury workstations | Servers and endpoints | Both cages; headquarters treasury room | Director of Settlement and Treasury Operations |
| Cage firewalls, switches, private circuits | Network | Both cages | VP Platform Engineering |
| Fraud model serving | Containers | Cloud A | Head of Data Science |
| Data warehouse and training environment | Managed analytics service | Cloud A analytics account | Head of Data Science |
| Identity provider and PAM vault | SaaS | Identity and PAM vendors | IT Director |
| SIEM and EDR | SaaS | Security vendors; MSSP | Director of Information Security |
| Repositories and pipelines (2 instances) | SaaS | Code hosting vendor | CTO |
| Administrator endpoints (136 of about 720) | Endpoint | Headquarters, acquired office, remote | IT Director |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The PPP uses the NIST SP 800-53B **High** baseline (370 controls and enhancements), tailored as follows:
- **Documented here: 128 controls** in `control-implementation.csv`. They are every control that implements a PCI DSS requirement, a Safeguards Rule element, or the bank service provider notice duty, plus the controls that address the risks in P01 (acquisition integration, segmentation, privileged access, monitoring, recovery, key management).
- **Selected by tailoring (added):** PM-1, PM-2, PM-9, and PM-14. They are not in any baseline but are needed for 16 CFR 314.4(a)-(b) and PCI DSS 12.4.1 and 12.3.1.
- **Integrity tailoring:** because integrity is High, the SI-7 and SI-10 statements cover funding file validation and signing, and AC-5 covers dual control for funding file release.
- **Inherited without separate statements:** the remaining High-baseline physical and environmental controls (for example PE-9 to PE-18) for the cloud providers' data centers and the colocation buildings, and platform-level SA and SC controls for managed services. They are inherited from the Cloud A and Cloud B providers, the colocation providers, the identity provider, and the MSSP, and are evidenced by their AOCs and SOC 2 Type 2 reports, which are reviewed each year (P09 `vendor-soc2-review.csv`).
- **Out of scope for this tier, recorded as tailoring decisions:** controls whose purpose applies only to federal systems or to capabilities the company does not have, for example most PM-series program controls other than those listed above, and PE controls for facilities the company does not operate.

CSF 2.0 subcategories in the CSV come from `00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv` where it covers the control. For the controls it does not cover (for example AU-5, CP-3, MA-4, PS-3), the subcategories are an author mapping.

**Status of the 128 documented controls:**
| Status | Count |
|---|---|
| Implemented | 58 |
| Partially implemented | 69 |
| Planned | 1 (IR-3) |
| Not applicable | 0 |

**Inheritance of the 128 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 69 | Company |
| Hybrid | 54 | Cloud A and Cloud B providers, colocation providers, identity provider, MSSP, content delivery service, source code SaaS |
| Common/Inherited | 5 | Identity provider (AC-7, IA-2(8)), cloud and colocation time and visitor controls (AU-8, PE-8), content delivery service (SC-5) |

The Partially implemented statements trace to the 16 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. About half of them name the Integrated Payments gateway (Cloud B) as the reason, which is why its integration is the first condition in section 4.2.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 32 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee. Independent PCI DSS validation is the QSA's combined 2026 ROC.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance.
- **Administrators.** The 110 core administrators use phishing-resistant security keys and reach the CDE only through PAM. This meets PCI DSS 8.4.2 and is appropriate for the High categorization. The 26 Cloud B administrators use push MFA directly to the Cloud B console. That does **not** meet the company's authenticator standard; they move to PAM and security keys by 2026-11-06 (R-001, POAM-002).
- **Core merchant portal users** must use MFA for administrator, refund, funding account, and virtual terminal roles. Other core users (reporting only) sign in with a password, with dynamic risk analysis approved in writing by the Qualified Individual under PCI DSS 8.3.10.1.
- **Integrated Payments portal users** (about 15,000) sign in with a password only. This does **not** meet PCI DSS 8.3.10.1 or the Safeguards Rule MFA element (16 CFR 314.4(c)(5)). MFA will be required for all partner administrators and for merchant users with refund or funding account rights by 2026-10-30 (R-004, POAM-005).
- **Consumers** paying through the hosted payment page or hosted payment fields are not account holders and do not authenticate to the PPP. Card brand authentication programs run through the issuers.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10); 2025 AOCs; 2026-01 penetration test report.

## 13. Acronym List and Glossary
- **AOC:** Attestation of Compliance
- **ASV:** Approved Scanning Vendor
- **CDE:** cardholder data environment
- **DR:** disaster recovery
- **EDR:** endpoint detection and response
- **HSM:** hardware security module
- **ISV:** independent software vendor (software platform partner)
- **MFA:** multi-factor authentication
- **MSSP:** managed security service provider
- **PAM:** privileged access management
- **PAN:** primary account number (card number)
- **POA&M:** plan of action and milestones
- **PPP:** Payment Processing Platform
- **QSA:** Qualified Security Assessor
- **ROC:** Report on Compliance
- **SIEM:** security information and event management

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | Director of Information Security |
| 1.0 | 2026-09-15 | Updated with P07 results; approved by the Chief Operating Officer | Director of Information Security, reviewed by the CTO and the vCISO |
