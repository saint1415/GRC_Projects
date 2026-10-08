# System Security Plan (short form): Shared Back-Office Platform

**Organization:** Cris Santos Company (the owner's management business for three wholly owned LLCs) | **Tier:** Sole Proprietorship | **Vertical:** Management of Companies and Enterprises
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Shared Back-Office Platform (**SBP**), identifier CSC-SYS-001.

## 2. System Overview
The SBP is the set of SaaS tools the owner uses to run the back office for four legal entities: the sole proprietorship and its three LLCs (Storage, Rentals, Laundry). It holds email and files for four domains, the books for four companies, four bank accounts, payroll for two employers, and the owner's administrator access to each LLC's own system. Components are SYS-01 to SYS-04, SYS-08, and SYS-10, plus the owner's administrator access to SYS-05 to SYS-07 and the site devices in SYS-09 (`../00_company-facts.md` section 3). There is no server and no IaaS.

**Why one system for four entities.** The LLCs are separate legal entities with separate bank accounts, books, and contracts, but they share one identity: the owner's email account is the administrator and recovery address for every system. A failure in the SBP is a failure in all three LLCs at once. That is the holding company risk at this size, and it is why the plan treats the shared platform, not each LLC, as the system. Most safeguards are **inherited from the SaaS vendors**; the owner is responsible for identities, data handling, devices, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation |
|---|---|---|
| State | Data security, breach notice, and disposal. Each LLC is a covered entity; the sole proprietorship is its third-party agent | Fla. Stat. 501.171(2)-(6), (8) |
| Federal (Rentals) | FCRA user duties for tenant screening; FTC Disposal Rule | 15 U.S.C. 1681b(f), 1681m(a); 16 CFR 682.3 |
| Federal (Rentals) | Fair Housing Act (tenant selection, including any AI use; P10) | 42 U.S.C. 3604 |
| Benchmark | NIST CSF 2.0 portfolio profile (voluntary) | NIST CSWP 29; P03 |
| Contract | Card processor merchant terms (Storage, Laundry) | Merchant agreements |
| Internal | Information Security Policy | POL-01 (P06) |

**Not applicable (vertical requirements):** N55-R01 to N55-R03 (SEC Regulation S-K Item 106, Form 8-K Item 1.05, SOX section 404): no securities registered and not an issuer. N55-R04 and N55-R05 (Federal Reserve): not a bank holding company. N55-R06 (HIPAA group health plan): no plan is sponsored. N55-R07 (CIRCIA): proposed only. Reasons in P03 section 1. Because none of the vertical requirement IDs applies, `regulatory_driver` columns cite Fla. Stat. 501.171, the Rentals rules, or the CSF 2.0 subcategory directly.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-manager on 2026-08-31, for the sole proprietorship and, as sole member and manager, for each LLC.
### 4.2 System Authorization Decision
No formal authorization applies to a private business. Equivalent decision: the owner accepted continued operation on 2026-08-31, on condition that the High risks in P01 (R-001, R-002, R-010) are treated by their due dates.
### 4.3 System Operational Status
Operational. Planned changes: password manager and app-based MFA (2026-09-15); backup service for the suite (2026-10-31); separate guest network at the laundromat (2026-10-31); successor access envelope (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security lead, risk acceptor, administrator | Owner-manager | Every role, for every entity |
| Day-to-day users | Storage facility manager; Laundry attendants (LLC employees) | Use their LLC's system; report problems to the owner |
| Contracted support | Outside bookkeeper; on-call IT technician (agreement signed 2026-07-24) | Bookkeeping; technical help on request, no standing access |
| Service providers | Productivity suite, accounting, payroll, storage, property management, and laundry platform vendors; the bank | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Personal identity and authentication (tenant, applicant, and employee SSNs and driver license numbers) | Moderate | Moderate | Low | Disclosure triggers Florida breach notices and identity theft risk; data can be re-requested if lost |
| Financial management, payments, and payroll | Moderate | Moderate | Moderate | Altered bank details cause direct loss; payroll every second Friday (P05 MTD 72 h) |
| Business operations and correspondence (email, contracts) | Moderate | Moderate | Moderate | Email is the recovery path for every system (P05 BP-01, MTD 24 h) |
| **SBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 26 controls a one-person back office can run (`control-implementation.csv`). Other Moderate controls are inherited from the SaaS vendors (evidence: the accounting service's SOC 2 report, P09) or tailored out because they assume staff, servers, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the suite tenant and its settings, the four accounting company files, the online banking profile, the payroll accounts, the owner's administrator access to the three LLC systems, the AI assistant add-on, the owner's laptop and phone, the Storage office desktop, the Laundry POS tablet, the routers at the three sites, the gate controller, and paper move-in forms.
- **Outside (external services):** the vendors' platforms and hosting, the bank, the payment processors, the consumer reporting agency behind the property management platform, the bookkeeper's and CPA firm's own systems, and the internet providers.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Outside bookkeeper | All four entities' books; payroll hours | Engagement letter only; **no confidentiality or security terms (gap)** |
| Outside CPA firm | Year-end files | Engagement letter; the firm's own portal |
| Bank | Payments; bank feeds to the accounting service | Online banking agreement |
| Consumer reporting agency (through SYS-06) | Applicant identity and screening reports | Platform terms and the landlord's user certification |
| Payment processors and laundry payment vendor | Card and app payments | Merchant agreements |
| On-call IT technician | Remote sessions the owner starts | Confidentiality and security agreement (2026-07-24) |
| AI assistant (SYS-10) | Prompts and anything the owner's account can open | Suite business terms; **no use rules until POL-01 9.5 (gap)** |

## 9. System Component Inventory
| Component | Type | Entity served |
|---|---|---|
| Productivity suite tenant (SYS-01) and AI assistant (SYS-10) | SaaS | All four |
| Accounting service (SYS-02) | SaaS | All four |
| Online banking (SYS-03) | Bank-hosted | All four |
| Payroll service (SYS-04) | SaaS | Storage, Laundry |
| Storage management system (SYS-05) | SaaS (owner administrator access) | Storage |
| Property management platform (SYS-06) | SaaS (owner administrator access) | Rentals |
| Laundry POS and payment platform (SYS-07) | SaaS (owner administrator access) | Laundry |
| Owner laptop and phone (SYS-08) | Endpoints | All four |
| Storage desktop, gate controller, POS tablet, three routers (SYS-09) | Site devices | Storage, Laundry, home office |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 26 controls:
- Implemented: 6
- Partially implemented: 18
- Planned: 2

Inheritance: 3 fully inherited from the SaaS vendors (AC-3, AU-2, AU-9), 12 hybrid (the vendor provides the mechanism and the owner configures or uses it), and 11 the owner's alone (AC-6, AT-2, AU-6, CA-2(1), CM-3, CM-8, CP-2, IR-8, MP-6, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01 covering all four entities; vendor terms (SA-9); owner holds every role |
| Identify | Risk assessment (RA-3); BIA (P05); inventory (CM-8, partial) |
| Protect | MFA (IA-2(1), IA-2(2), partial); password manager (IA-5, planned); laptop encryption (SC-28); bookkeeper role (AC-6) |
| Detect | Vendor sign-in logs and bank payment alerts (AU-2, inherited); monthly review (AU-6, planned) |
| Respond | Shared email takeover runbook with four-entity notification matrix (IR-8) |
| Recover | Vendor backups (CP-9, partial); successor access envelope (CP-2, planned) |

### 10.2 Control assessment status
Self-assessed 2026-07-27 to 2026-07-31 with the IT technician. See P07.

## 11. Digital Identity Acceptance Statement
The administrator accounts reach the Florida personal information of about 670 people (Storage about 610, Rentals applicants 47, LLC employees 8) and four bank accounts, so phishing-resistant or app-based MFA is appropriate. Today the accounting and payroll services enforce authenticator-app MFA, the suite and property management accounts use text-message codes, and the storage system and laundry platform use passwords only. Target by 2026-09-15: authenticator-app MFA everywhere, and a hardware security key for the suite and banking (a second key kept in the sealed envelope). Tenants and customers use each vendor's own portal and identity controls, outside this boundary.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 SaaS control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook, P09 SOC 2 self-check and vendor review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **LLC:** limited liability company (Storage, Rentals, and Laundry are single-member LLCs)
- **MFA:** multi-factor authentication
- **POS:** point of sale
- **SBP:** Shared Back-Office Platform
- **Third-party agent:** an entity contracted to maintain, store, or process personal information for a covered entity (Fla. Stat. 501.171(1)(h))

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial short-form plan | Owner-manager |
