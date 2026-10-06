# System Security Plan: Hosted Case Management Service (HCMS)

**Organization:** Cris Santos Company, LLC (GovTech systems integrator) | **Tier:** Micro | **Vertical:** Public Administration
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-08-31

## 1. System Name and Identifier
Hosted Case Management Service (**HCMS**), identifier CSC-SYS-001.

## 2. System Overview
The HCMS is the set of case management applications that the company configures, hosts, and supports for 4 Florida local agencies: pretrial supervision for a sheriff's office (AC-01), the county-funded Emergency Assistance Program for a county human services department (AC-02), and code enforcement and constituent requests for two cities (AC-03, AC-04). About 38,000 people have records in it, and about 75 agency staff use it (about 30 at AC-01, 9 at AC-02, 20 at AC-03, and 15 at AC-04).

The company owns almost no infrastructure. The applications run in the company's tenant on a licensed low-code case management platform (SaaS/PaaS), and the only server the company runs is one integration virtual machine in a government-community IaaS region. A managed service provider (MSP) runs the laptops and the productivity suite. This plan therefore says, for each control, what the company does itself, what the MSP does for it, and what it inherits from the platform vendor or the IaaS provider.

**Major components:**
- **SYS-01:** the platform tenant: 4 agency workspaces and a developer sandbox
- **SYS-02:** the integration server and export storage: one Linux virtual machine that pulls the sheriff's nightly file and loads it into AC-01, and one object storage bucket that holds nightly exports of all 4 workspaces
- **SYS-09:** the AI eligibility pre-screening pilot in the AC-02 workspace (the platform vendor's AI add-on)

Supporting services that administer the system: the productivity suite identity service (SYS-03), the helpdesk (SYS-04), the source code repository (SYS-05), and the administrator laptops in SYS-06.

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the company |
|---|---|---|---|
| Contract | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline | SP 800-53B Moderate baseline | AC-02 contract; AC-03 and AC-04 contracts by reference |
| N92-R02 | FBI CJIS Security Policy | CJISSECPOL v6.1 (06/25/2026); 28 CFR 20.33(a)(7) | CJIS Security Addendum in the AC-01 contract |
| N92-R01 | IRS Publication 1075 (FTI safeguards) | 26 U.S.C. 6103(p)(4); Pub. 1075 (Rev. 11-2021), Exhibit 7 | SC-01 subcontract. **FTI is outside this boundary**: it stays in the revenue agency's virtual desktop (SYS-10). The rule reaches this system only through the 2 laptops that connect and the ban on FTI in company systems |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2) and (6) | Directly, as a third-party agent of each agency |
| State | Florida public records law for contractors | Fla. Stat. 119.0701(2)(b) | Directly, through the public records clause in each agency contract |
| State | Local Government Cybersecurity Act | Fla. Stat. 282.3185 | Binds the county and city customers (12-hour ransomware reports); the company supplies facts (P08) |
| N92-R08 | GovRAMP (formerly StateRAMP) | GovRAMP program (not law) | The platform vendor is listed as verified; the company itself is not (P09) |
| Internal | Security policies POL-02, POL-03, POL-04 | P06 | Company policy |

Not applicable:
- HIPAA Security Rule (N92-R03): no customer has designated the company a business associate.
- Medicaid safeguards (N92-R04): the AC-02 program is county-funded and is not Medicaid, SNAP, or TANF.
- Driver's Privacy Protection Act (N92-R05): no data from motor vehicle records.
- SLCGP (N92-R06): no grant funds pay for the service.
- CIRCIA (N92-R07): proposed rule only.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the owner on 2026-08-31.

### 4.2 System Authorization Decision
The company is not a federal agency, so there is no formal authorization. The equivalent internal decisions on 2026-08-31:
- The owner accepted continued operation of the HCMS on the condition that the POA&M items in P07 are completed by their dates and the High and Very High risks in P01 are treated on the dates set there.
- The owner confirmed that the Implementation and Support Analyst stays out of the AC-01 workspace until fingerprint-based checks and the Security Addendum certification are complete (support role narrowed on 2026-08-12).
- AC-01 and AC-02 will receive this SSP summary, the P07 results, and the POA&M by 2026-10-30, with the AC-02 renewal questionnaire (P09).

### 4.3 System Operational Status
Operational. Planned changes: FIPS mode for the sheriff file transfer by 2026-09-18 (SC-13), MFA for AC-04 by 2026-09-30, 1-year log retention by 2026-10-31 (AU-11), immutable exports in a separate account by 2026-11-30 (CP-9), and SSH access through an MFA-protected session service by 2026-12-31 (IA-2(1)).

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner and risk acceptor | Owner | Overall accountability; accepts risk; approves this plan, policies, and spending |
| Security and Compliance Officer | Operations Manager | Day-to-day program; maintains this plan, the risk register, and the POA&M; agency and prime notices; screening paperwork |
| System administrator | Lead Platform Engineer | Platform tenant administration; SYS-02; technical controls |
| Configuration | Platform Developers (2) | Application changes in the sandbox and promotion to production |
| Support | Implementation and Support Analyst | Agency user support through the helpdesk |
| IT operations | MSP | Laptops, suite administration, office network |
| Agency counterparts | AC-01 LASO; AC-02 IT security liaison; AC-03 and AC-04 IT managers | Approve agency users; receive notices; AC-01 holds the Security Addendum certifications |
| Independent assessor | Outside security consultant | Annual control assessment (P07) |

**Where roles overlap.** The owner, who accepts risk, also holds a platform administrator account, and the Lead Platform Engineer both runs and checks the technical controls. The company compensates with the independent assessor (P07), the vendor evidence reviewed in P09, and a monthly review of administrator activity by the Operations Manager, who holds no administrator rights.

## 6. System Information Types and System Categorization
Information types were modeled on the mission-based categories in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199 and were discussed with the AC-01 and AC-02 contacts.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Criminal justice supervision records (CJI, including CHRI) for AC-01 | Moderate | Moderate | Moderate | Disclosure harms supervisees and breaches 28 CFR Part 20 terms; wrong conditions or violation data could lead to a wrongful arrest or a missed violation; officers can work about 2 days on paper (P05 MTD 48 h) |
| Emergency assistance applicant records for AC-02 | Moderate | Moderate | Moderate | Social Security numbers and income documents; errors or delays affect households facing eviction or shutoff (P05 MTD 48 h) |
| Constituent service records for AC-03 and AC-04 | Low | Low | Low | Names, addresses, some driver license numbers; paper workaround for 5 days |
| System and security information (credentials, keys, logs, exports) | Moderate | Moderate | Moderate | Compromise gives access to every workspace |
| **HCMS category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Baseline:** the NIST SP 800-53B Moderate baseline, as the AC-02, AC-03, and AC-04 contracts require. The P03 gap analysis rates all 177 Moderate base controls. This plan documents the **46 controls** the company operates itself or shares with a provider (see `control-implementation.csv`). The other Moderate controls are handled one of two ways:
- **Inherited** from the platform vendor's and the IaaS provider's FedRAMP Moderate authorizations (data center physical and environmental controls, platform patching and vulnerability management, platform network protection, platform backups). Evidence: the FedRAMP Marketplace listings (checked June 2026) and the platform vendor's SOC 2 Type 2 report (reviewed in P09).
- **Rated in P03 only,** where the company's part is small (for example, program-level controls run once for the whole company). These are tracked as gaps in P03, not tailored out, because the contracts require the full baseline.

Where the CJIS Security Policy sets a stricter value for the AC-01 workspace (for example, 5 failed sign-ins in 15 minutes for AC-7, a 30-minute device lock for AC-11, 1-year log retention for AU-11, FIPS 140-3 modules for SC-13), the stricter value governs the whole tenant.

## 7. Authorization Boundary Description
- **Inside:** the company's platform tenant and its configuration (SYS-01), SYS-02 and its bucket, the AI pre-screening configuration (SYS-09), and the company accounts, keys, and laptops used to administer them.
- **Outside (external services, interconnected):**
  - the platform vendor's and the IaaS provider's own infrastructure (inherited controls);
  - the sheriff's identity provider and file drop;
  - the MSP's remote management platform (SYS-08);
  - the productivity suite, helpdesk, and repository vendors' platforms;
  - the AI add-on's model subprocessor;
  - the revenue agency's virtual desktop (SYS-10), which is the revenue agency's FTI system and is governed by its own Pub. 1075 safeguards.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system or party | Direction | Data | Agreement |
|---|---|---|---|
| Sheriff's file drop (AC-01) | Inbound to SYS-02 nightly | New bookings and criminal history summaries (CJI) | AC-01 contract with the CJIS Security Addendum |
| Sheriff's identity provider (AC-01) | Inbound federation | User identities and MFA assertions | AC-01 contract |
| County payment system (AC-02) | Outbound weekly file sent by AC-02 staff from the platform | Approved payment requests (payee, amount) | AC-02 contract |
| Platform vendor AI add-on (SYS-09) | Outbound documents, inbound suggestions | AC-02 applicant documents and data | Platform subscription terms; **AI add-on terms not reviewed (gap; P10)** |
| Helpdesk vendor (SYS-04) | Inbound tickets | Agency user requests, sometimes screenshots with CJI | Standard terms; **no CJIS Security Addendum (gap)** |
| MSP remote management (SYS-08) | Inbound administrative access to laptops | Device management | MSP service contract (**no incident notice term**) |
| Revenue agency virtual desktop (SYS-10) | Outbound session from 2 approved laptops | FTI displayed inside the agency session only | SC-01 subcontract with Exhibit 7 terms; agency CISO device approval |

## 9. System Component Inventory
| Component | Type | Location or provider | Owner |
|---|---|---|---|
| Platform tenant: 4 workspaces and sandbox (SYS-01) | SaaS/PaaS | Platform vendor, U.S. government-community regions | Lead Platform Engineer |
| Integration virtual machine and bucket (SYS-02) | IaaS | IaaS provider, U.S. government-community region | Lead Platform Engineer |
| AI pre-screening configuration (SYS-09) | SaaS feature | Platform vendor and its model subprocessor | Owner |
| Suite identity service (SYS-03) | SaaS | Productivity suite vendor | Operations Manager (MSP operates) |
| Helpdesk (SYS-04) | SaaS | Helpdesk vendor | Implementation and Support Analyst |
| Repository (SYS-05) | SaaS | Repository vendor | Lead Platform Engineer |
| Administrator laptops (5 of 8 in SYS-06) | Endpoint | Office and staff homes | Operations Manager (MSP operates) |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv`. Summary of 46 controls:
- Implemented: 7
- Partially implemented: 28
- Planned: 11
- Not applicable: 0

By responsibility: 19 system-specific (the company alone) and 27 hybrid (the company with the platform vendor, the IaaS provider, the MSP, or an agency). Fully inherited controls are not listed in the CSV; they are rated in P03.

### 10.2 Inherited and MSP-provided controls
| Provider | What the company relies on | Evidence | What the company must still do |
|---|---|---|---|
| Platform vendor | Data centers (PE family), platform patching and scanning (SI-2, RA-5), encryption at rest and in transit (SC-28, SC-8, SC-13), workspace separation (AC-3, SC-4), platform backups (CP-9), audit log generation (AU-2) | FedRAMP Moderate authorization; SOC 2 Type 2 report reviewed 2026-08-21 (P09); August 2026 letter on FIPS 140-3 | Complementary user entity controls: user provisioning and removal, role design, MFA settings, log export and review, timely notice of incidents to agencies |
| IaaS provider | Physical security, hypervisor, default disk and bucket encryption, network isolation | FedRAMP Moderate authorization of the services used | Everything on the virtual machine: patching, hardening, SSH, logging, bucket policies |
| MSP | Laptop patching (SI-2), antivirus (SI-3), encryption (SC-28), screen lock (AC-11), suite account administration (AC-2), office firewall (SC-7) | Monthly MSP report (July 2026); P07 evidence requests | Direct the work, review reports monthly, approve exceptions, and add security terms to the contract (P01 R-012) |
| AC-01 and the revenue agency | Fingerprint-based checks and CJIS training (AC-01); background investigations, disclosure awareness training, and device approval (revenue agency) | Agency confirmations | Keep the access lists matched to screening; recertify on time |

**Inherited does not mean done.** Two of the platform vendor's complementary user entity controls are open gaps at the company: user access review (AC-2) and log review (AU-6).

### 10.3 Control assessment status
Assessed 2026-08-17 to 2026-08-19 by an independent consultant. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
Staff sign in to the platform and the suite with a password and a second factor (authenticator codes or push). This is appropriate for administrator access to Moderate data. SYS-02 SSH access is key-only and will move behind an MFA-protected session service (P01 R-009). Agency users sign in with platform-local accounts with MFA (AC-02, AC-03), the sheriff's identity provider with sheriff-enforced MFA (AC-01), or a password only (AC-04, a gap closing 2026-09-30). For the AC-01 workspace, the CJIS Security Policy requires MFA (IA-2(1), IA-2(2)), which the sheriff's identity provider supplies.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), BIA (P05), cloud control map (P04), risk register (P01), gap analysis (P03), policies (P06), assessment and POA&M (P07), incident response runbook (P08), SOC 2 readiness and platform vendor report review (P09), AI assessment (P10).

## 13. Acronym List and Glossary
- **CHRI:** criminal history record information
- **CJI:** criminal justice information
- **FTI:** federal tax information
- **HCMS:** Hosted Case Management Service
- **LASO:** local agency security officer
- **MFA:** multi-factor authentication
- **MSP:** managed service provider
- **POA&M:** plan of action and milestones
- **SFTP:** secure file transfer protocol

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 2026-08-31 | Initial plan | Operations Manager (Security and Compliance Officer) |
