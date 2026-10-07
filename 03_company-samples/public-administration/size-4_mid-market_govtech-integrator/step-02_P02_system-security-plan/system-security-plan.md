# System Security Plan: Agency Case Management Cloud (ACMC)

**Organization:** Cris Santos Company, Inc. (PE-backed GovTech systems integrator) | **Tier:** Mid-Market | **Vertical:** Public Administration
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-17

## 1. System Name and Identifier
Agency Case Management Cloud (**ACMC**), identifier CSC-ACMC-01. The ACMC is the company's major system and its largest business line. It comprises SYS-01, SYS-02, SYS-03, SYS-05, SYS-06, SYS-08, SYS-09, and SYS-14 in `../00_company-facts.md`, with the supporting services that administer them.

## 2. System Overview
The ACMC is a multi-tenant case management service that the company builds, hosts, and supports for 43 live agencies in Florida, State B, and State C, with a Colorado county contracted for 2027. Agency staff use it for pretrial, probation, and jail program supervision (AG-02, AG-39), statewide benefits intake and verification (AG-03), tax compliance casework (AG-01), motor vehicle title and registration casework (AG-04), and constituent services and permitting for 38 cities and counties. About 3.1 million individuals have records in it.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Application tier: managed container service, message queue, document object storage | Production account, U.S. region A, 3 zones (PaaS) |
| SYS-02 | Data tier: regulated-tier cluster (AG-02, AG-03, AG-04, AG-39), shared municipal cluster, and the AG-01 instance in the separate **FTI enclave** account; read replicas in region B | Managed relational database (PaaS) |
| SYS-03 | Integration hub: managed file transfer, API gateway, message-switch connectors, motor vehicle feed | Production account (PaaS and containers) |
| SYS-05 | Agency user sign-in: federation with 5 agency identity providers; platform-local accounts for municipal tenants | Part of SYS-01 |
| SYS-06 | Cloud landing zone: 8 accounts (management, security tooling and log archive, shared services, production, FTI enclave, staging, development, backup) | Public cloud, vendor-agnostic (P04) |
| SYS-08 | Analytics and agency reporting service | Managed data warehouse, production account |
| SYS-09 | AI eligibility assistant (feature of SYS-01) | Production account plus the provider's managed model service |
| SYS-14 | Backups: point-in-time recovery and a write-once vault in region B | Backup account |

**Supporting services that administer the system (inside the boundary as configured by the company):** the workforce identity provider and privileged access management service (SYS-04), the repositories and CI/CD pipeline (SYS-07), the SIEM operated with the MDR provider (SYS-12), and the 120 administrator and support laptops in SYS-11.

**Not part of this system:** the managed services remote management platform (SYS-10) and the agency-hosted systems it reaches. They are a separate business line with their own risks (P01 R-001, R-008, R-050). Their only allowed connection to the ACMC is being removed (section 7).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it reaches the company |
|---|---|---|---|
| Contract | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline | SP 800-53B Moderate baseline | All agency contracts |
| N92-R02 | FBI CJIS Security Policy | CJISSECPOL v6.1 (06/25/2026); 28 CFR 20.33(a)(7) | CJIS Security Addendum in the AG-02 contract and, through the State B CJIS Systems Agency, in the AG-39 contract |
| N92-R01 | IRS Publication 1075 (FTI safeguards) | 26 U.S.C. 6103(p)(4); 26 CFR 301.6103(n)-1; Pub. 1075 (Rev. 11-2021) | Exhibit 7 language in the AG-01 contract |
| N92-R04 | Medicaid applicant and beneficiary safeguards | 42 CFR 431.300-431.307 | AG-03 contract confidentiality terms (with SNAP, 7 CFR 272.1(c)) |
| N92-R05 | Driver's Privacy Protection Act | 18 U.S.C. 2721-2725 | AG-04 contract, which applies the state motor vehicle agency's data-access terms |
| State | Florida Cybersecurity Standards | Rule 60GG-2, F.A.C.; Fla. Stat. 282.318(4)(h) | Security terms in the AG-01, AG-03, and other Florida state agency contracts |
| State | Florida Information Protection Act | Fla. Stat. 501.171(2), (6), and (8) | Directly, as a third-party agent |
| State | Other states' laws | Law of each state where the agency sits or affected individuals reside | AG-39 to AG-43 contracts; counsel confirms |
| State | Colorado SB26-189 (automated decision-making technology) | C.R.S. 6-1-1701 to -1709 as reenacted; effective 2027-01-01 | AG-44 contract, for AI-001 (P10) |
| N92-R08 | GovRAMP (formerly StateRAMP) | GovRAMP program (not law) | State B procurement policy; Authorized status required by 2027-06-30 |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Company policy |

Not applicable:
- **HIPAA Security Rule (N92-R03):** no customer has designated the company a business associate. AG-03 placed its eligibility functions outside its health care component (45 CFR 164.105).
- **FTI in the AG-03 tenant:** prohibited by contract, because human services agencies may not disclose FTI to contractors (Pub. 1075 section 2.C.11.2).
- **CIRCIA (N92-R07):** proposed rule only. **SLCGP (N92-R06):** no grant funds pay for company services.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Technology Officer (system owner) on 2026-09-17, after the control assessment (P07) and the same day as the audit committee meeting.
### 4.2 System Authorization Decision
The company is not a federal agency and there is no formal federal authorization. The equivalent decisions:
- **Decision:** the Chief Technology Officer accepted continued operation of the ACMC on 2026-09-17, with the conditions in the P07 POA&M.
- **Risk acceptance:** the Chief Executive Officer accepted the Very High and High risks in P01 only with dated treatment plans, and directed that the 15 staff with pending CJIS screening and the 3 with pending Pub. 1075 investigations lose access to CJI and FTI until screening is complete.
- **Agency reliance:** AG-01, AG-02, AG-03, AG-04, and AG-39 receive this SSP, the P07 results, and the POA&M by 2026-12-31 (CA-6). The SOC 2 Type 2 report (P09) and GovRAMP Authorized status (N92-R08) are the planned independent assurance for all customers.
- **Re-decision:** by 2027-09-30, or after a major change such as the planned 2027 acquisition.
### 4.3 System Operational Status
Operational. Major modifications planned:
- FIPS 140-3 certified modules on the AG-02 and AG-39 message-switch connectors by 2026-09-21 (SC-13)
- Application audit events for the regulated tenants sent to the SIEM, with weekly access analytics (AU-2, AU-6), by 2027-01-31
- Document storage added to the write-once vault and a region B failover exercise (CP-6, CP-7), by 2027-06-30
- Removal of SYS-10 access paths into the landing zone (AC-17), by 2026-12-31

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Technology Officer | Accountable for the ACMC; approves this SSP; accepts operation |
| Executive sponsor | Chief Operating Officer | Security program sponsor; accepts Moderate risk |
| Risk acceptor (authorizing official equivalent) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Strategy and audit committee reporting |
| Information Security Officer | Director of Information Security | Day-to-day security; security contact named in agency contracts |
| Security operations | Security Operations Manager and 3 security engineers | Monitoring with the MDR provider; vulnerability management; incident command |
| GRC | GRC Manager and 2 GRC analysts | SSP, risk register, gap analysis, POA&M, SOC 2 and GovRAMP evidence |
| Privacy and contract compliance | Director of Contracts and Compliance | Agency security terms; notices to agencies |
| System operations | Director of Cloud Operations | Landing zone, backups, logging, patching |
| Development | VP of Engineering | Code, pipeline, change management |
| AI feature owner | Director of Data and AI | SYS-09 (P10) |
| Personnel security | HR Director with the Personnel Security Coordinator | Screening for CJI, FTI, and motor vehicle positions |
| Independent assessment | Co-sourced internal audit firm | Annual assessment (P07) |
| Agency counterparts | AG-01 disclosure officer; AG-02 local agency security officer; AG-03 information security manager; AG-04 records custodian; AG-39 terminal agency coordinator | Receive notices; approve agency users; hold Security Addendum certifications |

## 6. System Information Types and System Categorization
Information types were modeled on the mission-based categories in NIST SP 800-60 Vol. 2 Rev. 1. Impact levels are the company's FIPS 199 determinations, agreed with the regulated customers.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Criminal justice supervision records (CJI, including CHRI) for AG-02 and AG-39 | Moderate | Moderate | Moderate | Disclosure harms supervisees and is restricted by 28 CFR Part 20; wrong conditions or violation data could lead to a wrongful arrest; each sheriff can run one shift on paper (P05 MTD 12 h) |
| Taxation management records with FTI for AG-01 | Moderate | Moderate | Low | Unauthorized inspection or disclosure carries criminal and civil penalties (IRC 7213, 7213A, 7431); the agency tax system keeps collections running (P05 MTD 48 h) |
| Benefits application records for AG-03 (SNAP, TANF, Medicaid) | Moderate | Moderate | Moderate | Social Security numbers and income data; errors or delays affect food and medical assistance timeliness (P05 MTD 24 h) |
| Motor vehicle record personal information for AG-04 | Moderate | Moderate | Moderate | DPPA-restricted data including some photographs; offices cannot clear held cases without it (P05 MTD 24 h) |
| Constituent service records for municipal customers | Low | Low | Low | Names, addresses, some driver license numbers; paper workaround for 3 days |
| System and security information (credentials, logs, keys) | Moderate | Moderate | Moderate | Compromise gives access to all tenants |
| **ACMC category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**High was considered for confidentiality** because the ACMC holds about 3.1 million people's records across FTI, CJI, and benefits data. The team kept Moderate because each regulated data set is isolated (separate enclave for FTI; customer-managed keys for the regulated tier), the agency contracts specify Moderate, and the harm from any one tenant's disclosure is serious rather than severe or catastrophic. The P01 R-003 exposure estimate reflects the aggregate case.

## 7. Authorization Boundary Description
**Inside the boundary:**
- the 8 landing zone accounts and their workloads: production (SYS-01, SYS-02 regulated tier and municipal cluster, SYS-03, SYS-08, SYS-09 components), the FTI enclave (AG-01 database and key), staging and development (masked data only), shared services (network hub, privileged access gateway), security tooling and log archive, backup (SYS-14), and management;
- the company's configuration of the identity provider and privileged access management service (SYS-04), the pipeline and its secrets (SYS-07), and the SIEM use cases (SYS-12);
- the 120 administrator and support laptops with production access.

**Outside the boundary (external services, interconnected):**
- the cloud provider's infrastructure and managed services (FedRAMP Moderate authorized);
- the managed large language model service used by SYS-09;
- the identity provider, repository, SIEM, MDR, and ticketing vendors' platforms;
- agency identity providers and agency systems at the other end of each interface;
- the managed services remote management platform (SYS-10). **Today SYS-10 can reach the shared services jump hosts from engineer laptops with push MFA** (gap, AC-17). That path is being removed by 2026-12-31; until then it is treated as an external connection under monitoring.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| AG-01 tax system | Inbound nightly file transfer; outbound case status | FTI and state tax data | Contract with Exhibit 7; interconnection security agreement; IRS 45-day notification (2022, updated 2025) |
| AG-02 message switch | Inbound criminal history summaries; outbound supervision status | CJI including CHRI | Contract with CJIS Security Addendum; interconnection security agreement |
| AG-39 message switch (State B) | Same as AG-02 | CJI including CHRI | Contract with CJIS Security Addendum through the State B CSA; **no interconnection security agreement (gap, CA-3)** |
| AG-03 eligibility system | Bidirectional API | Applicant and household data (no IRS or SSA income match fields) | Contract; interconnection security agreement |
| State motor vehicle data feed for AG-04 | Inbound | Motor vehicle record personal information | AG-04 contract and the state data-access terms |
| Agency identity providers (5) | Inbound assertions | User identity and roles | Federation terms in contracts |
| Managed model service (SYS-09) | Outbound prompts, inbound text | AG-03 applicant documents and extracted data | Provider standard terms; **signed data-use terms pending (gap, P03 PR-04)** |
| SIEM and MDR provider | Outbound logs | Cloud, identity, network, and endpoint logs | Contracts with security terms; SOC 2 reports |
| Analytics export (internal, production account) | Nightly copy from tenant databases to SYS-08 | Tenant data, FTI excluded by design | **AG-01 note fields carried FTI out of the enclave since 2025-04 (P03 PB-09); export stopped and copies being purged** |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| Web and application containers | Managed container service | Production account, region A, 3 zones | Director of Cloud Operations |
| Regulated-tier database cluster (customer-managed keys) | Managed relational database | Production account; replica in region B | Director of Cloud Operations |
| Shared municipal database cluster | Managed relational database | Production account; replica in region B | Director of Cloud Operations |
| AG-01 database instance and key | Managed relational database; key management | FTI enclave account | Director of Cloud Operations (enclave administrator group of 6) |
| Document storage | Object storage with versioning | Production account | Director of Cloud Operations |
| Integration hub | Managed file transfer, API gateway, containers | Production account | VP of Engineering |
| Analytics service | Managed data warehouse | Production account | VP of Engineering |
| AI eligibility assistant | Containers plus managed model service | Production account; provider AI service | Director of Data and AI |
| Network hub, cloud firewall, privileged access gateway | Network and management services | Shared services account | Director of Cloud Operations |
| Log archive (write-once, 7 years for cloud audit logs) | Object storage | Security tooling and log archive account | Security Operations Manager |
| Backup vault (write-once, 35 days) | Backup service | Backup account, region B | Director of Cloud Operations |
| Staging and development | Separate accounts with masked data | Cloud | VP of Engineering |
| Administrator and support laptops (120) | Endpoint | Offices and remote (U.S.) | IT Director |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The ACMC uses the NIST SP 800-53B **Moderate** baseline, as every agency contract requires: 177 base controls with 110 enhancements (287 in all). `control-implementation.csv` has one row per base control, and each statement covers that control's Moderate enhancements. Tailoring decisions:
- **Not applicable (4):** AC-18, MA-3, MP-5, SC-15, with the reason in each row.
- **Inherited or hybrid:** physical, environmental, and infrastructure controls are inherited from the FedRAMP Moderate authorized cloud provider (the PE family, SC-4, SC-39, and others). The company relies on the provider's authorization and its SOC 2 report, reviewed each year (P09 `vendor-soc2-review.csv`).
- **Overlay values:** where CJISSECPOL v6.1 or Pub. 1075 sets a stricter value, the stricter value governs. Examples: 3 failed logons in 120 minutes for FTI enclave access (Pub. 1075 AC-7) and 5 in 15 minutes elsewhere (CJIS AC-7); 7-year retention for FTI audit records (Pub. 1075 AU-11) and at least 1 year for CJI (CJIS AU-11); remediation of critical vulnerabilities within 15 days (CJIS RA-5 and SI-2); FIPS 140-3 certified modules for CJI in transit (CJIS SC-13). Recording all of them as organization-defined values is an open item (PL-11).
- IA-2(12) (acceptance of PIV credentials) has no effect because no users hold PIV credentials.

**Status of the 177 base controls:**
| Status | Count |
|---|---|
| Implemented | 114 |
| Partially implemented | 59 |
| Planned | 0 |
| Not applicable | 4 |

**Inheritance of the 177 base controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 121 | Company |
| Hybrid | 31 | Cloud provider, identity provider vendor, MDR provider, agency identity providers |
| Common/Inherited | 25 | Cloud provider (PE family, SC-4, SC-39, CP-8), SIEM vendor (AU-7), productivity suite vendor (SI-8) |

The Partially implemented statements trace to the 12 known gaps in `../00_company-facts.md` section 4 and to the P07 findings. The largest clusters are access to regulated data (AC-2, AC-6, PS-3, PS-6), detection of misuse (AU-2, AU-6, SI-4), recovery (CP-2, CP-4, CP-6, CP-10), and cryptography on CJI paths (SC-8, SC-13, IA-7).

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 38 controls from 2026-08-03 to 2026-08-28 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). At the audit committee's request the assessment also covered the SYS-10 remote administration path, because of P01 R-001. The P03 gap analysis rated all 177 controls plus the CJIS, Pub. 1075, program confidentiality, DPPA, and Florida overlays.

## 11. Digital Identity Acceptance Statement
- **Workforce, general.** Every user signs in through the identity provider with a password and push MFA with number matching, under conditional access that checks device compliance and location (U.S. only). This meets CJISSECPOL IA-2(1) and IA-2(2) ([Priority 1]) and the Pub. 1075 multi-factor requirements.
- **Administrators.** The 40 cloud administrators use phishing-resistant security keys, and elevation is just in time. Support staff and managed services engineers who reach regulated data or agency systems will move to phishing-resistant keys by 2027-01-31 (IA-2 gap; P01 R-008).
- **Agency users.** AG-01, AG-02, AG-03, AG-04, and AG-39 users are authenticated by their agencies' identity providers, which enforce MFA; the agencies own identity proofing. Six municipal tenants still allow local accounts without MFA (IA-8 gap), which is acceptable only because those tenants hold no CJI, FTI, benefits, or motor vehicle data. MFA for them is due 2026-12-31.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); risk register (P01); gap analysis and roadmap (P03); cloud architecture and control map (P04); BIA (P05); policies and standards index (P06); assessment and POA&M (P07); incident runbooks and notification matrix (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **ACMC:** Agency Case Management Cloud
- **CHRI:** criminal history record information
- **CJI:** criminal justice information
- **CJISSECPOL:** FBI CJIS Security Policy
- **CSA:** CJIS Systems Agency
- **DPPA:** Driver's Privacy Protection Act
- **FTI:** federal tax information
- **MDR:** managed detection and response
- **MFA:** multi-factor authentication
- **POA&M:** plan of action and milestones
- **TIGTA:** Treasury Inspector General for Tax Administration

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-07-31 | Draft from the BIA, risk assessment, and gap analysis | GRC Manager |
| 1.0 | 2026-09-17 | Updated with P07 results; approved by the Chief Technology Officer; replaces the 2024 system description | Director of Information Security |
