# System Security Plan (short form): Multi-tenant Booking Platform

**Organization:** Cris Santos Company (independent B2B SaaS software publisher) | **Tier:** Sole Proprietorship | **Vertical:** Information
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026), all headings kept with short answers | **Version:** 1.0, 2026-09-25

## 1. System Name and Identifier
Multi-tenant Booking Platform (**MBP**), identifier CSC-SYS-001.

## 2. System Overview
The MBP is the online booking and appointment-reminder service that about 240 small businesses (salons, barbershops, pet groomers, home-cleaning services) use to take bookings from about 88,000 end clients. One person, the owner-developer, builds, deploys, operates, and supports it, with a freelance support contractor for about 10 hours a week. Components are SYS-01 to SYS-09 in `../00_company-facts.md` section 3: the production platform on a managed application platform and managed database (PaaS), the source repository and CI/CD pipeline, messaging providers, a generative AI model API (Smart Replies), a payment processor, error and uptime monitoring, help desk and chat, back office SaaS (email, files, accounting, password manager, domain registrar), and one laptop and one phone. There are no servers, virtual machines, or networks to manage; the hosting provider runs the platform layer. The owner is responsible for the application code, identities, secrets, data, configuration, and vendor contracts (P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies |
|---|---|---|---|
| N51-R01 | FTC Act Section 5 | 15 U.S.C. 45(a) and 45(n) | Reasonable data security (unfairness) and truthful security and data-use statements (deception). No size threshold. Analyzed in P03 |
| Contract | Terms of Service and DPA with every subscriber; two negotiated DPAs | Customer contracts | Use limits, 72-hour (two customers: 48-hour) incident notice, 14-day sub-processor notice, 30-day deletion after closure |
| State | Florida breach notification, third-party agent duties | Fla. Stat. 501.171(6) | Notice to subscribers no later than 10 days after determination of a breach (P08). Other states: each state where affected individuals reside |
| Internal | Information Security Policy | POL-01 (P06) | Consolidated policy for a one-person business |

Checked and not applicable at this size (P03 section 1): CCPA (N51-R03; the company is not a "business" under Cal. Civ. Code 1798.140(d)), COPPA (N51-R02), DOJ Data Security Program (N51-R04), PADFA (N51-R05), FCC CPNI (N51-R06), FedRAMP (N51-R07), and SEC disclosure (N51-R08).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner-developer on 2026-09-25.
### 4.2 System Authorization Decision
No formal authorization applies to a private software business. Equivalent decision: the owner-developer accepted continued operation on 2026-09-25, on condition that the Very High and High risks in P01 (R-001, R-002, R-006) are treated by their due dates.
### 4.3 System Operational Status
Operational since 2023. Planned changes: secrets moved out of the laptop and rotated (2026-10-31); named support role with MFA in the admin console (2026-11-30); backups copied outside the production account (2026-12-31).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner, developer, administrator, security and privacy lead, risk acceptor | Owner-developer | Every role. Self-review is compensated by a contract security consultant's challenge every year (POL-01 4.5) |
| Support operator | Freelance support contractor | Help desk and chat; admin console access for setup help (shared login today; named support role planned) |
| Independent check | Contract security consultant | Secret scan, configuration review, restore test witness (2026-08-27). No standing access |
| Service providers | Hosting provider and SaaS vendors | Operate inherited controls under their terms |

## 6. System Information Types and System Categorization
| Information type (SP 800-60) | C | I | A | Rationale |
|---|---|---|---|---|
| Subscribers' end-client records (contact details, appointment history, service notes, photos) | Moderate | Moderate | Moderate | Disclosure triggers subscriber notice duties and state breach analysis; wrong appointments disrupt subscribers' businesses; loss beyond one day breaks the BIA (P05 MTD 24 h for BP-01) |
| Subscriber accounts and credentials | Moderate | Moderate | Low | Email and password pairs are personal information under Fla. Stat. 501.171(1)(g)1.b. if not secured; sign-in can wait for a restore |
| Billing and business records | Low | Moderate | Low | Held by the payment processor and accounting SaaS; BP-05 MTD 168 h |
| **MBP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** SP 800-53B Moderate, tailored to 25 controls that carry the safeguards a one-person software business can operate and check (`control-implementation.csv`). One control outside the Moderate baseline, IA-5(7), was added because the top risk (P01 R-001) is plaintext secrets on the laptop. Other Moderate controls are either inherited from the hosting provider (evidence: its SOC 2 Type 2 report, reviewed 2026-09-09 in P09) or tailored out because they assume staff, facilities, or a federal program.

## 7. Authorization Boundary Description
- **Inside:** the owner's hosting account (application, job worker, admin console, database, photo storage, settings), the source repository and CI configuration, the owner's accounts and settings in every SaaS service (SYS-03 to SYS-08), the domain and DNS records, the laptop and the phone, and the secrets that connect them.
- **Outside (external services):** the hosting provider's platform and data centers, the messaging providers, the AI model provider, the payment processor and its hosted checkout, the error monitoring and help desk platforms, and the subscribers' own devices and staff.

Diagram: P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Party | Data | Agreement |
|---|---|---|
| Subscribers (about 240) | Their end-client records, staff accounts, exports | Terms of Service and DPA; two negotiated DPAs |
| Email service and SMS provider | Client names, phone numbers, emails, appointment details | Standard terms; email service DPA; on the public sub-processor list |
| AI model provider | Client messages, first names, service notes (Smart Replies prompts) | **API terms only; no DPA; not on the sub-processor list (gap)** |
| Error monitoring | Request data in error reports (sometimes client names and phone numbers) | Standard terms; on the list |
| Help desk | Subscriber questions; incidental client details | Standard terms; on the list |
| Payment processor | Subscriber billing contacts; deposits through subscribers' own connected accounts | Processor terms; no card data reaches the MBP |
| Subscribers (exports) | CSV exports of client lists | **Sent as email attachments (gap)** |

## 9. System Component Inventory
| Component | Type | Owner |
|---|---|---|
| Production platform (SYS-01) | PaaS application, managed database, object storage | Owner-developer |
| Source repository and CI/CD (SYS-02) | SaaS | Owner-developer |
| Messaging providers (SYS-03) | SaaS | Owner-developer |
| AI model provider API (SYS-04) | SaaS | Owner-developer |
| Payment processor (SYS-05) | SaaS | Owner-developer |
| Error and uptime monitoring (SYS-06) | SaaS | Owner-developer |
| Help desk and chat (SYS-07) | SaaS | Owner-developer |
| Back office SaaS and domain registrar (SYS-08) | SaaS | Owner-developer |
| Laptop and phone (SYS-09) | Owner endpoints | Owner-developer |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 25 controls:
- Implemented: 4
- Partially implemented: 17
- Planned: 4

Inheritance: 12 hybrid (the provider operates the mechanism and the owner configures and uses it correctly) and 13 the owner's alone (AC-3, AC-6(5), AC-7, AT-2, AU-6, CP-2, CP-4, IA-5(7), IR-6, IR-8, RA-3, SA-9, SA-11). None is fully inherited, because even the hosting provider's encryption, edge, and backups depend on the owner's account settings and secrets.

**Key safeguards per CSF Function:**
| Function | Key safeguards |
|---|---|
| Govern | POL-01; sub-processor terms and DPAs (SA-9); owner holds all roles |
| Identify | Risk assessment (RA-3); BIA (P05); dependency alerts (RA-5) |
| Protect | MFA on administrator accounts (IA-2(1)); secrets out of plaintext (IA-5(7), planned); tenant isolation (AC-3); encryption at rest and in transit (SC-28, SC-8) |
| Detect | Hosting and application event logs (AU-2); monthly review (AU-6, planned) |
| Respond | Credential compromise runbook (IR-8); subscriber and Florida notice duties (IR-6) |
| Recover | Provider backups and point-in-time recovery (CP-9); restore test (CP-4); emergency access kit (CP-2) |

### 10.2 Control assessment status
Self-assessed 2026-08-24 to 2026-08-28, with tests on 2026-08-27 run with the contract security consultant. See P07.

## 11. Digital Identity Acceptance Statement
The owner's administrator accounts use a password plus an authenticator app, which suits remote administration of a Moderate system. Two exceptions remain until MFA is added: the domain registrar (2026-10-15) and the product's admin console (2026-11-30). Subscriber staff sign in with a password only; offering MFA to subscriber admins is planned with the admin console change. End clients do not sign in; they book through public booking pages.

## 12. Referenced Artifacts
Scenario facts, P01 risk register, P03 gap analysis, P04 cloud control map, P05 BIA, P06 POL-01, P07 assessment and POA&M, P08 runbook and notification matrix, P09 SOC 2 self-check and hosting provider report review, P10 AI use assessment.

## 13. Acronym List and Glossary
- **CI/CD:** continuous integration and continuous delivery (the build and deploy pipeline)
- **DPA:** data processing addendum
- **MBP:** Multi-tenant Booking Platform
- **MFA:** multi-factor authentication
- **PaaS / SaaS:** platform as a service / software as a service
- **Sub-processor:** a service provider that processes subscriber data for the company

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-09-25 | Initial short-form plan | Owner-developer |
