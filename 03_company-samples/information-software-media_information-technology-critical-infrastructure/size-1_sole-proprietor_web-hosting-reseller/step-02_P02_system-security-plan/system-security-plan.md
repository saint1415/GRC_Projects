# System Security Plan (short form): Hosting Control Plane and Customer Portal

**Organization:** Cris Santos Company (web hosting reseller) | **Tier:** Sole Proprietorship | **Vertical:** Information Technology
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-28

## 1. System Name and Identifier
Hosting Control Plane and Customer Portal (**HCP**), identifier CSC-SYS-001.

## 2. System Overview
The HCP is everything the owner uses to sell, run, and support hosting for about 150 small business customers: about 270 websites, 410 mailboxes, and 230 domains. It is the "control plane" of a one-person reseller. Whoever controls it can create, suspend, or delete any customer's hosting account, change any domain's DNS, sign in to any customer control panel, and push code to the 120 care-plan sites.

Components are SYS-01 to SYS-07 in `../00_company-facts.md` section 3:
- the customer portal and billing automation (SaaS), which stores the API credentials for the reseller console and the registrar;
- the upstream provider's reseller console and customer control panels;
- the registrar reseller account and DNS;
- the site management dashboard (SaaS);
- the website security and uptime service (SaaS);
- email, file storage, and the password manager;
- the owner's laptop and phone.

The company runs no servers, so most infrastructure safeguards are **inherited from the upstream hosting provider**. The owner is responsible for identities, credentials, contractor access, customer-facing settings, backups beyond the provider's 7 days, and vendor oversight (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | Status here |
|---|---|---|---|
| FTC Act | Unfair or deceptive acts or practices (reasonable security; truthful security claims) | 15 U.S.C. 45(a), 45(n) | **Applies.** Main requirement set for P03 |
| State | Florida data security, third-party agent notice, disposal | Fla. Stat. 501.171(2), (6), (8) | **Applies** (company is a third-party agent for customers and a covered entity for its own data) |
| State | Other states' breach laws | Each state where affected individuals reside | Applies case by case (P08) |
| C-IT-R01 | FedRAMP | 44 U.S.C. 3607-3616 | Does not apply: no federal customer |
| C-IT-R02, C-IT-R03 | CMMC; DFARS 252.204-7012 | 32 CFR Part 170; 48 CFR 252.204-7012 | Do not apply: no DoD contracts |
| C-IT-R04 | DOJ Data Security Program | 28 CFR Part 202 | Does not apply on current facts (P03 section 1.3) |
| C-IT-R05 | Bank service provider notification | 12 CFR 53.4; 225.303; 304.24 | Does not apply: no bank customers |
| C-IT-R06 | CIRCIA (proposed only, not in force) | 6 U.S.C. 681b; proposed 6 CFR Part 226 | Tracked only |
| Contract | Terms of Service; payment processor merchant agreement (annual PCI DSS self-assessment) | Contracts | Applies |
| Internal | Information Security Policy | POL-01 (P06) | Adopted 2026-09-28 |

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-09-28.
### 4.2 System Authorization Decision
No formal authorization applies to a private reseller. Equivalent decision: the owner accepted continued operation on 2026-09-28, on condition that the Very High and High risks in P01 (R-001, R-002, R-004, R-009) are treated by their due dates, starting with MFA on the portal administrator login and every dashboard account by 2026-10-15.
### 4.3 System Operational Status
Operational. Planned changes: customer credentials moved into a shared password manager vault (2026-10-31); independent backups for all sites (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, security and privacy lead, risk acceptor | Owner | Every role (POL-01 section 3) |
| Contractor with privileged access | Freelance web developer | Care plan updates through the dashboard; no access to the portal, console, or registrar |
| Independent check | Contract security consultant | August 2026 tests; no standing access |
| Service providers | Upstream hosting provider, registrar, portal, dashboard, and security service vendors | Operate inherited controls |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Customer website and mailbox content (includes shopper accounts and rental applications with SSNs) | Moderate | Moderate | Moderate | Disclosure triggers customers' breach duties and the company's 10-day notice; altered sites harm customers' visitors; outage beyond a day loses customers (P05 MTD 24 h) |
| Control plane credentials and configuration (API credentials, DNS, account settings) | Moderate | Moderate | Moderate | Whoever holds them controls every customer service |
| Customer account and billing records | Moderate | Low | Low | Contact data and portal sign-ins; billing can wait 72 h (P05) |
| **HCP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 28 controls that carry the reasonable-security expectations for a one-person reseller (`control-implementation.csv`). Other Moderate controls are inherited from the upstream provider and the SaaS vendors (evidence: the upstream SOC 2 report, P09) or tailored out because they assume staff, owned networks, or a federal program. AC-5, AU-9, CM-3, and CA-2(1) are kept with compensating controls (see `control-implementation.csv`).

## 7. Authorization Boundary Description
- **Inside:** the owner's administrator accounts and settings in SYS-01 to SYS-06, the freelance developer's dashboard account, the customer password spreadsheet and password manager, and the owner's laptop and phone.
- **Outside (external services):** the upstream provider's servers, network, and data centers; the SaaS vendors' platforms; customers' own site content and site administrator accounts; the freelance developer's personal laptop (a gap: it reaches the dashboard but is outside the owner's control, P01 R-001).

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Direction | Data | Agreement |
|---|---|---|---|
| Upstream hosting provider | Both | Customer sites, databases, mailboxes; account provisioning through the API | Reseller terms (no security exhibit) |
| Registrar | Both | Domain contacts; nameserver changes through the API | Registrar reseller terms |
| Portal vendor | Both | Customer contacts, sign-ins, tickets, API credentials | Click-through terms |
| Dashboard vendor | Both | Administrator access to 120 sites; premium backups | Click-through terms; **data location not verified** |
| Security service vendor | Inbound | Site files, findings, visitor IP addresses | Click-through terms; **data location and AI data use not verified** |
| Freelance web developer | Outbound | Dashboard access; customer credentials by email | Freelance agreement (**no security terms**) |
| Customers | Both | Credentials, tickets, site content | Terms of Service (**no incident notice clause**) |
| Consumer AI chat assistant | Outbound | Pasted log excerpts and files | Consumer terms (**not approved; P10**) |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Customer portal (SYS-01) | SaaS | Portal vendor | Owner |
| Reseller console and control panels (SYS-02) | Managed hosting | Upstream provider, U.S. data centers | Owner (account level) |
| Registrar reseller account and DNS (SYS-03) | SaaS | Registrar | Owner |
| Site management dashboard (SYS-04) | SaaS | Dashboard vendor | Owner |
| Security and uptime service (SYS-05) | SaaS | Security service vendor | Owner |
| Email, files, password manager (SYS-06) | SaaS | Productivity suite vendor | Owner |
| Laptop and phone (SYS-07) | Endpoints | Home office | Owner |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 28 controls:
- Implemented: 6
- Partially implemented: 19
- Planned: 3

Inheritance: 3 fully inherited from the upstream provider (AC-3, PE-3, SC-7), 14 hybrid (the vendor provides the mechanism, the owner configures or uses it), and 11 the owner's alone (AT-2, AU-6, CA-2(1), CM-3, CP-2, IA-5, IR-6, IR-8, PS-7, RA-3, SA-9).

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; vendor oversight (SA-9); contractor terms (PS-7); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); vulnerability scanning of all sites (RA-5) |
| Protect | MFA on control plane tools (IA-2(1), gaps on the portal and the freelancer's dashboard account); credentials in a password manager (IA-5, gap); least privilege for the freelancer (AC-6, gap); site patching (SI-2) |
| Detect | Daily scans and uptime checks (SI-3, SI-4); weekly log review (AU-6, planned) |
| Respond | Provider tooling runbook (IR-8); Florida 10-day notice to customers (IR-6) |
| Recover | Upstream backups (CP-9, inherited) plus independent backups (planned); emergency access envelope (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-17 to 2026-08-21, with tests on 2026-08-19 run with the contract security consultant. See P07.

## 11. Digital Identity Acceptance Statement
- **Owner and freelancer (privileged users):** a password plus an authenticator app is required on every control plane tool. It is appropriate for administrators who can affect every customer. It is not yet in place on the portal administrator login or the freelancer's dashboard account (due 2026-10-15). Phishing-resistant authenticators (security keys) are planned for the portal, console, registrar, and dashboard by 2027-03-31, because these are the accounts an attacker would phish.
- **Customers:** a password with optional MFA in the portal and control panel. MFA will be required for customers who run online stores or hold mailboxes with Social Security numbers, and encouraged for the rest.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and upstream report review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **API:** application programming interface
- **CMS:** content management system
- **DNS:** Domain Name System
- **HCP:** Hosting Control Plane and Customer Portal
- **MFA:** multi-factor authentication
- **SFTP:** SSH File Transfer Protocol
- **Third-party agent:** under Fla. Stat. 501.171(1)(h), an entity contracted to maintain, store, or process personal information for a covered entity
- **Upstream provider:** the wholesale hosting provider whose servers and reseller program the company resells

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-28 | Initial short-form plan | Owner |
