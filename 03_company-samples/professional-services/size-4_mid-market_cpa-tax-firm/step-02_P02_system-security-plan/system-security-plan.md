# System Security Plan: Tax and Client Data Platform (TCDP)

**Organization:** Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm) | **Tier:** Mid-Market | **Vertical:** Professional, Scientific, and Technical Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-22

## 1. System Name and Identifier
Tax and Client Data Platform (**TCDP**), identifier CSC-TCDP-01. The TCDP is the Company's major system for customer information. It comprises SYS-01 to SYS-06 and SYS-10 to SYS-12 in `../00_company-facts.md`.

## 2. System Overview
The TCDP supports the tax practice end to end: client document intake and scanning, return preparation and review (including the offshore preparation program and AI-assisted data entry), e-signature of Forms 8879, IRC 7216 consents, electronic filing through the tax software vendor, return delivery, and storage of prior-year files. It also provides the shared identity, email, endpoint, network, cloud, and monitoring services that the CAS platform (SYS-08) and the Attest Firm's engagement platform (SYS-09) rely on. It serves 600 workforce members, about 130 seasonal staff and interns, about 30 offshore vendor staff, and clients filing about 47,400 returns a year.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Professional tax preparation and e-file software, including the AI document extraction feature (AI-001) | Vendor-hosted SaaS; vendor SOC 2 Type 2; vendor is an Authorized IRS e-file Provider |
| SYS-02 | Client portal with e-signature and secure file exchange | Vendor SaaS |
| SYS-03 | Document management system (DMS) | Company-managed servers in the workloads account |
| SYS-04 | Cloud landing zone: management and security, shared services, workloads, restricted data enclave, and backup accounts | Public cloud IaaS and PaaS, vendor-agnostic (P04) |
| SYS-05 | Identity provider with SSO, MFA, and conditional access; privileged access broker for cloud | SaaS |
| SYS-06 | Productivity suite (email, files, chat), including the enterprise AI assistant (AI-002) | SaaS |
| SYS-10 | Networks at 6 offices on SD-WAN | On-premises; SD-WAN managed service |
| SYS-11 | 640 laptops, 110 desktops, 26 multifunction printers, 18 high-volume scanners, about 520 enrolled phones | Company-managed |
| SYS-12 | Security tooling: EDR, SIEM operated by the MSSP, email security gateway, vulnerability scanner, SaaS discovery | SaaS and cloud |

The CAS platform (SYS-08), the audit and SOC engagement platform (SYS-09), and the AI tools outside SYS-01 and SYS-06 connect to the TCDP as external or adjacent systems (section 8). They inherit the TCDP's common controls (identity, endpoints, network, logging, incident response, personnel security), which is why P09 reuses this plan as evidence.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the TCDP |
|---|---|---|---|
| N54-R01 | FTC Standards for Safeguarding Customer Information (Safeguards Rule) | 16 CFR Part 314 | Primary control requirement. Applies in full: the Company is a financial institution under 314.2(h)(2)(viii) and holds customer information on about 205,000 consumers, so the 314.6 exception does not apply |
| N54-R02 | Disclosure or use of tax return information by preparers | 26 U.S.C. 7216; 26 CFR 301.7216-1 to -3 | Limits who can see return data, including offshore preparers (301.7216-2(c)(2); 301.7216-3(b)(4)) and contractors (301.7216-2(d)(2)) |
| N54-R03 | IRS data security expectations and e-file provider rules | IRS Pub. 4557; Pub. 5708; Pub. 1345 (Rev. 12-2025), including next-business-day reporting of security incidents | E-signature identity checks, Form 8879 retention, incident reporting to the IRS |
| N54-R06 | HIPAA Security Rule and breach notice, as a business associate | 45 CFR 164.302-164.318; 164.410 | Applies to the ePHI from 44 health care clients stored in the DMS and workpapers |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security (501.171(2)), disposal (501.171(8)), breach notification (P08); other states handled generically |
| Contract | CAS client agreements and BAAs | Contracts | CAS availability and confidentiality commitments (P09); BAA terms for PHI |
| Internal | Security policies POL-01 to POL-05 and the standards index | P06 | Policy basis for every control |

Not applicable (reasons in `../00_company-facts.md` section 1):
- FAR 52.204-21 and DFARS 252.204-7012 with CMMC (N54-R04, N54-R05): no federal contracts.
- ABA Model Rules (N54-R07): not a law firm.
- CIRCIA (N54-R09): proposed rule only.
- AICPA Code of Professional Conduct (N54-R08): noted, not assessed.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (executive sponsor and system owner for shared services) and the National Tax Practice Leader (business owner) on 2026-09-22, after the control assessment (P07) and before the audit committee meeting the same day.

### 4.2 System Authorization Decision
The Company is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the TCDP accepted with conditions on 2026-09-22.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the High-risk POA&M items in P07 must meet their milestones, and every treatment marked "before filing season" must be live by 2027-01-15. The audit committee receives POA&M status each quarter. Re-decision is due by 2027-09-30 or after a major change (for example, an acquisition, P01 R-046).

### 4.3 System Operational Status
Operational. Major modifications planned:
- Phishing-resistant MFA for administrators, partners, and finance and CAS payroll staff, and device compliance for mail access (due 2027-01-15)
- Mandatory client MFA on the portal (due 2027-01-15)
- SIEM onboarding of tax software, portal, DMS, and CAS platform activity (due 2027-01-15)
- SSN masking in scanned documents for the offshore pool, and an offshore-only DMS view (due 2026-12-15)
- PHI moved from the general DMS to the restricted data enclave (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner (business) | National Tax Practice Leader | Business owner of the tax practice and the TCDP's tax services |
| System owner (shared services) | Chief Operating Officer | Executive sponsor of the security program; accepts Moderate risk |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; oversees the Qualified Individual |
| Governing body | Board of directors and its audit committee | Receives the Qualified Individual's annual written report (314.4(i)) and quarterly reporting |
| Qualified Individual and HIPAA Security Officer | Director of Information Security | Oversees, implements, and enforces the program (314.4(a)); day-to-day control owner |
| Technology owner | Chief Information Officer | Infrastructure, cloud, endpoints, and SaaS administration |
| Risk and compliance | GRC Manager and GRC Analyst | Risk register, POA&M, vendor reviews, evidence |
| Privacy and legal | General Counsel and Privacy Officer | IRC 7216 consents, breach determinations, BAAs, contracts |
| IRS e-file Responsible Official | Director of Tax Operations | E-file program, Pub. 1345 duties, offshore program |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Taxation management (client tax return information, SSNs, bank account numbers) | Moderate | Moderate | Moderate | Disclosure enables identity theft refund fraud and triggers FTC, IRS, and state duties for up to 205,000 consumers; altered data leads to wrong returns and diverted refunds; outages near a deadline cause late filings (P05 MTD 24 h in season) |
| Financial audit (attest workpapers, client general ledgers, PHI samples from health care audits) | Moderate | Moderate | Low | Confidential client financial data and some ePHI; engagements can slip a few days (P05 MTD 120 h) |
| Customer services (portal accounts, engagement letters, IRC 7216 consents, client communications) | Moderate | Moderate | Moderate | Account data; consents must be accurate and signed before disclosure; clients depend on the portal to sign Forms 8879 in season |
| Human resources management (workforce and seasonal identities) | Moderate | Low | Low | Account data; limited harm if briefly unavailable |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed to establish discovery dates and scope in breach investigations |
| **TCDP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Confidentiality was considered for High.** A breach of the whole DMS would affect about 205,000 consumers plus about 90,000 other individuals. The team kept confidentiality at Moderate because the harm to each person is financial and largely recoverable (IRS Identity Protection PINs, credit monitoring, corrected returns), which fits the FIPS 199 "serious adverse effect" description, and because the Company would survive such an event. To compensate for the volume, the plan adds tailoring aimed at bulk exposure: SA-9(5) for processing location, CA-8 for annual penetration testing, and AU-6(1) for bulk-export detection.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the Company's tax software tenant configuration, user roles, and AI feature settings;
- the client portal tenant;
- the DMS servers and storage;
- all 5 cloud accounts and their workloads, including the virtual desktop pool and the log archive;
- the identity provider and productivity suite tenants;
- 6 office networks;
- 776 managed endpoints and devices, and enrolled phones;
- the Company's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the tax software vendor's platform and its AI sub-processor, and the IRS and state e-file systems (reached only through the vendor);
- the portal vendor's platform and the cloud provider's infrastructure;
- the CAS platform services (SYS-08), the practice management service (SYS-07), and the HR and applicant tracking service (SYS-13);
- the audit and SOC engagement platform (SYS-09), which shares the landing zone but has its own owner (Attest Firm Managing Partner);
- the MSSP's platform, the offshore preparation support vendor, and about 85 other service providers.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| IRS and state e-file systems (through the tax software vendor) | Outbound returns; inbound acknowledgments | Returns, acknowledgments, rejects | IRS e-file rules (Pub. 1345); vendor contract |
| Tax software vendor's AI sub-processor | Outbound documents; inbound extracted data | Scanned source documents | Vendor contract amendment 2025 (U.S. processing, no training); **sub-processor not independently assessed (gap)** |
| Offshore preparation support vendor (virtual desktops) | Bidirectional within firm-hosted desktops | Tax return information; **SSNs visible in scanned documents (gap)** | Vendor contract; IRC 7216 consent per client (301.7216-3) |
| Clients (portal) | Bidirectional | Source documents, Forms 8879, engagement letters, consents, returns | Portal terms; engagement letter |
| Clients (email) | Bidirectional | Documents emailed by clients; returns emailed on request | **Encryption not enforced (gap)** |
| Client lenders and advisers (on request) | Outbound | Copies of returns | Signed IRC 7216 consent |
| CAS platform services (SYS-08) | Bidirectional (staff access through SSO; payroll and bill-pay local accounts) | Client ledgers, payroll, payments | Vendor contracts; **local accounts outside SSO (gap)** |
| Health care clients (attest and CAS) | Inbound | PHI samples and payroll data | 44 BAAs |
| MSSP | Inbound logs; remote response actions | Security logs (may include customer information fragments) | MSSP contract with security terms; SOC 2 Type 2 |
| Software vendors (2) with their own remote tools | Inbound management | Server administration | **No per-session approval (gap)** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Tax preparation and e-file tenant | SaaS | Tax software vendor | National Tax Practice Leader |
| Client portal tenant | SaaS | Portal vendor | Director of Tax Operations |
| DMS application and database servers (4) and file storage | Virtual machines and managed file storage | Workloads account | Chief Information Officer |
| Virtual desktop pool (offshore vendor and remote seasonal staff) | Managed virtual desktop service | Workloads account | Director of Tax Operations |
| Restricted data enclave (audit analytics, PHI staging) | Virtual machines and object storage | Enclave account | Attest Firm Managing Partner |
| Network hub, cloud firewall, VPN and desktop gateways, privileged access broker | Network and management services | Shared services account | Chief Information Officer |
| Organization guardrails, posture management, locked log archive | Security services | Management and security account | Director of Information Security |
| Backup vault | Backup service with write-once retention | Backup account (second region) | Chief Information Officer |
| Identity provider tenant | SaaS | Identity vendor | Chief Information Officer |
| Productivity suite tenant | SaaS | Productivity vendor | Chief Information Officer |
| SD-WAN edges, firewalls, switches, Wi-Fi | Network | Offices 1-6 | Chief Information Officer |
| Laptops (640), desktops (110) | Endpoint | All offices and remote | Chief Information Officer |
| Multifunction printers (26) and high-volume scanners (18) | Leased devices | All offices; 12 scanners at the document processing center | Director of Tax Operations |
| EDR, SIEM tenant, email security gateway, scanner, SaaS discovery | Security tooling | SaaS and cloud; SIEM operated by the MSSP | Director of Information Security |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The TCDP uses the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 120 controls** in `control-implementation.csv`. They cover every control the Company maps to a Safeguards Rule element (author mapping in P03), the controls that support IRC 7216 and the HIPAA Security Rule standards, and the Moderate controls that address the risks in P01 (identity, privileged access, monitoring, vendors, recovery).
- **Selected by tailoring (added, 5):** CA-8 (penetration testing, required by 314.4(d)(2)(i) without continuous monitoring), PM-1, PM-2, and PM-9 (program, Qualified Individual, and risk strategy for 314.3(a), 314.4(a), (b), and (i)), and SA-9(5) (processing location, because 26 CFR 301.7216-3(b)(4) restricts SSN disclosure outside the United States).
- **Inherited without separate statements:** the remaining physical and environmental controls for cloud and SaaS data centers and platform-level SA and SC controls. These are inherited from the tax software vendor, the portal vendor, the identity vendor, the productivity vendor, the cloud provider, and the MSSP, and are evidenced by their SOC 2 Type 2 reports, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Deferred:** other Moderate controls with no Safeguards Rule, IRC 7216, or HIPAA mapping and no Moderate-or-higher risk in P01 (for example SA-11 developer testing and SA-15 development process, because the Company develops no software). They are recorded as tailoring decisions and reviewed yearly.

**Status of the 120 documented controls:**
| Status | Count |
|---|---|
| Implemented | 50 |
| Partially implemented | 68 |
| Planned | 2 |
| Not applicable | 0 |

**Inheritance of the 120 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 69 | Company |
| Hybrid | 37 | Identity vendor, tax software vendor, portal vendor, cloud provider, MSSP, CAS platform vendors |
| Common/Inherited | 14 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12), SaaS vendors (AC-12, SI-7), MSSP and insurer panel (IR-7) |

The Partially implemented statements trace to the 15 known gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 34 controls from 2026-08-03 to 2026-08-21 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). The assessment supports 16 CFR 314.4(d)(1) (regular testing of key controls). It does not replace the annual penetration test and the vulnerability assessments every six months required by 314.4(d)(2). Weaknesses are tracked in the POA&M and reported quarterly to the audit committee.

## 11. Digital Identity Acceptance Statement
- **Workforce.** All workforce users authenticate through the identity provider with a password and push MFA with number matching, under conditional access. The Safeguards Rule requires MFA for any individual accessing any information system (314.4(c)(5)). Number matching resists push fatigue but not adversary-in-the-middle phishing, which is the P08 BEC path. Phishing-resistant security keys are therefore required for administrators, partners, finance staff, and CAS payroll staff by 2027-01-15 (P01 R-001, R-007).
- **Offshore vendor staff.** Named accounts in the identity provider with MFA and access only through the virtual desktop pool. Vendor staff cannot reach the tax software or DMS directly.
- **Clients.** Clients use the portal vendor's sign-in. MFA becomes mandatory for all client accounts by 2027-01-15 (P01 R-006). Clients who sign Forms 8879 electronically go through the identity verification that IRS Pub. 1345 requires for electronic signatures in remote transactions, provided by the tax software's e-signature module.
- **CAS platform local accounts.** The payroll and bill-pay services use local accounts with SMS codes. They move to SSO with phishing-resistant MFA by 2026-12-31 (P01 R-051).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **BAA:** business associate agreement
- **BEC:** business email compromise
- **CAS:** client accounting services
- **DMS:** document management system
- **EDR:** endpoint detection and response
- **EFIN:** Electronic Filing Identification Number
- **ERO:** Electronic Return Originator
- **MSSP:** managed security service provider
- **PTIN:** Preparer Tax Identification Number
- **Qualified Individual:** the person who oversees the information security program under 16 CFR 314.4(a)
- **TCDP:** Tax and Client Data Platform
- **WISP:** written information security program

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis; replaces the 2024 WISP system description | GRC Manager |
| 1.0 | 2026-09-22 | Updated with P07 results; approved by the Chief Operating Officer and the National Tax Practice Leader | Director of Information Security |
