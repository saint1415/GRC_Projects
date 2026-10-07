# System Security Plan: Associate Payroll and Applicant Tracking Platform (APATP)

**Organization:** Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) | **Tier:** Mid-Market | **Vertical:** Administrative and Support and Waste Management and Remediation Services
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-22

## 1. System Name and Identifier
Associate Payroll and Applicant Tracking Platform (**APATP**), identifier CSC-APATP-01. The APATP is the firm's major system. Its scope is defined in `../00_company-facts.md` section 3.

## 2. System Overview
The APATP supports the firm's cycle from applicant to paycheck in every business unit: recruiting and AI-assisted screening, onboarding (tax forms, direct deposit, Form I-9, background checks, drug screens, E-Verify), Healthcare credentialing, time capture and client approval, weekly associate payroll for about 3,600 associates, and client invoicing. It is used by the 600 internal staff at HQ, 14 branches, and 6 on-site programs, by associates (self-service and timekeeping), and by client supervisors and hospital compliance staff.

**Major components:**
| ID | Component | Hosting and service model |
|---|---|---|
| SYS-01 | Staffing ATS and front-office platform (career site, onboarding with the electronic Form I-9 module, associate portal and mobile app, client portal, texting) | Vendor SaaS; SOC 2 Type 2 |
| SYS-02 | Payroll, billing, and back-office platform | Vendor SaaS; SOC 2 Type 2 and SOC 1 Type 2 |
| SYS-03 | Identity provider with SSO, number-matching push MFA, and conditional access | SaaS |
| SYS-04 | Cloud landing zone (security and identity, shared services, workloads, backup accounts): integration platform, data warehouse, document archive, BI | Public cloud IaaS/PaaS, vendor-agnostic (P04) |
| SYS-06 | Timekeeping app (GPS geofence) and 12 fingerprint time clocks at the on-site programs | Vendor SaaS; on-premises clocks |
| SYS-10 | Healthcare credentialing platform with client compliance portal | Vendor SaaS (no SOC 2 report) |
| SYS-13 | Networks at HQ, 14 branches, and 6 on-site offices on SD-WAN, with 42 lobby kiosks | On-premises; managed SD-WAN |
| SYS-14 | 640 laptops, 230 smartphones, 60 multifunction devices | Company-managed |
| SYS-15 | SIEM and EDR console operated by the MSSP | SaaS |

The screening provider (SYS-07), E-Verify (SYS-08), the AI tools (SYS-09), and the VMS (SYS-11) connect to the APATP as external services (section 8).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it affects the APATP |
|---|---|---|---|
| N56-R03 | Form I-9 retention, inspection, and electronic I-9 standards | 8 CFR 274a.2(b)(2)-(4), (e)-(i) | The I-9 module and archive must meet the electronic system, documentation, records security, and audit trail standards |
| E-Verify | E-Verify MOU for Employers | MOU Art. II.A (access, tutorial, timing, safeguarding, breach notice to DHS) | User access, credential safeguarding, immediate breach notice |
| State | Florida E-Verify statute | Fla. Stat. 448.095(2) | Use of E-Verify; 3-year retention of documentation and verifications; outage documentation |
| N56-R02 | FCRA employment background checks | 15 U.S.C. 1681b(b); 1681m(a) | Disclosure, authorization, adverse action workflow in SYS-01 and SYS-07 |
| N56-R01 | FACTA Disposal Rule | 16 CFR 682.3 | Disposal of consumer report information and media |
| State | Florida Information Protection Act | Fla. Stat. 501.171 | Reasonable security measures; breach notice; disposal. Personal information here includes SSNs, ID numbers, medical information, biometric data, and geolocation |
| Federal | ADA medical examination and inquiry records | 29 CFR 1630.14(b)(1), (c)(1) | Clinician health records in SYS-10 must be kept on separate forms, in separate medical files, as confidential medical records |
| State | Health care services pool registration | Fla. Stat. 400.980(2), (3), (5) | Level 2 screening and verified credential documentation before placement |
| State | Florida Security of Communications Act | Fla. Stat. 934.03(2)(d) | All-party consent for recorded recruiting calls (SYS-12 interface) |
| Federal | Title VII, ADEA, ADA selection rules | 42 U.S.C. 2000e-2(b), (k); 29 U.S.C. 623(b); 42 U.S.C. 12112(b)(6) | AI screening tools connected to SYS-01 (P10) |
| Contract | MSP client agreements | Contract | 48-hour incident notice; SOC 2 Type 2 report (P09) |
| Benchmark | NIST CSF 2.0 (voluntary; label N56-BM) | P03 | Target profile for the program |
| Internal | Security policies POL-01 to POL-05 and standards STD-01 to STD-10 | P06 | Policy basis for every control |

**Not applicable:**
- **HIPAA (N56-R04).** Placed clinicians work under the direct control of the client facility and are its workforce (45 CFR 160.103), and the firm creates, receives, maintains, or transmits no PHI on behalf of a covered entity. Reasoning in P03 G-152.
- **PCI DSS (N56-R06), FAR 52.204-21 (N56-R07), NYC Local Law 144 (N56-R08), TCPA/TSR (N56-R05), PHMSA security plans (N56-R09).** Reasons in P03 section 1.

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Chief Operating Officer (system owner) on 2026-09-22, after the control assessment (P07) and before the audit committee meeting the same day.
### 4.2 System Authorization Decision
The firm is not a federal agency, so there is no formal authorization to operate. The equivalent internal decision:
- **Decision:** operation of the APATP accepted with conditions, 2026-09-22.
- **Authorizing official equivalent:** Chief Executive Officer for High and Very High risks; Chief Operating Officer for Moderate and below (P01 acceptance authorities).
- **Conditions:** the exposed payroll API key is rotated and moved to the secrets service by 2026-10-15 (POAM-004); the High-risk POA&M items in P07 meet their milestones; the audit committee receives POA&M status each quarter; re-decision by 2027-09-30 or after a major change (for example, an acquisition or a new AI tool that ranks candidates).
### 4.3 System Operational Status
Operational. Major modifications planned:
- Associate portal sign-in with app-based or passkey authentication and a hold on new bank accounts (due 2026-12-31)
- SaaS audit logs (ATS, payroll, VMS, credentialing) into the SIEM with payroll fraud alerts (due 2027-01-31)
- Removal of full SSNs and bank account numbers from the data warehouse (due 2026-12-31)
- Kiosk segmentation at Branches 6-14 (due 2027-03-31)

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | Chief Operating Officer | Accountable for the APATP; accepts Moderate risk; executive sponsor of the security program |
| Authorizing official equivalent (High risk) | Chief Executive Officer | Accepts High risk; approves the risk appetite |
| Oversight | Board audit committee | Quarterly cyber risk reporting |
| Program strategy | vCISO (part-time contractor) | Strategy, risk method, board reporting, SSP review |
| Information Security Officer | Security Manager | Day-to-day control owner; maintains this plan; manages the MSSP |
| IT operations and recovery | IT Director | Infrastructure, identity, cloud landing zone, recovery |
| Privacy and records compliance | Director of Compliance and Privacy | Form I-9, E-Verify, FCRA, ADA medical files, retention, breach determinations with the General Counsel |
| Legal | General Counsel | Breach notice decisions, vendor terms, AI legal review |
| Payroll process owner | Director of Payroll and Billing | Payroll users, bank-change controls, payroll continuity |
| Recruiting process owner | Director of Recruiting Operations | ATS recruiting workflow and the recruiting AI tools |
| Healthcare credentialing | Credentialing Manager | Credential files, AHCA screenings, client compliance portal |
| Business unit owners | VP Light Industrial; VP Office and Professional; VP Healthcare Staffing; VP Managed Workforce Solutions | Access approvals and downtime procedures for their units |
| Independent assessment | Co-sourced internal audit firm | Annual IT audit; P07 assessment |
| Monitoring | MSSP | 24x7 EDR and SIEM monitoring |

**Overlap and compensation.** The Security Manager both operates and reports on many controls. The vCISO reviews the Security Manager's work, and the co-sourced internal audit firm, which designs and operates no control, performs the annual assessment and reports directly to the audit committee.

## 6. System Information Types and System Categorization
Information types come from NIST SP 800-60 Vol. 2 Rev. 1. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Personnel records and employment eligibility (applicant, associate, I-9, consumer report, screening data) | Moderate | Moderate | Moderate | SSNs and identity documents of about 168,000 people: disclosure causes identity theft and multi-state breach duties; altered I-9 records are a violation (8 CFR 274a.2(g)(2)); onboarding can run on paper for days, but Healthcare credential verification has a 12-hour MTD (P05) |
| Payroll management and expense reimbursement (associate pay, bank accounts, tax) | Moderate | Moderate | Moderate | Diverted or wrong pay harms associates directly; payroll must run weekly (P05 MTD 48 h) |
| Health-related employment records (clinician immunizations, TB tests, physicals, drug screens) | Moderate | Moderate | Low | Medical information of about 2,600 current and former clinicians; ADA confidentiality; loss of availability is covered by the credential status export |
| Customer services (client job orders, timesheet approvals, invoices; MSP supplier data) | Moderate | Moderate | Moderate | MSP client and supplier rates are contract-confidential; wrong time or invoices cause disputes and SOC 2 Processing Integrity exceptions |
| System and network monitoring (security logs) | Moderate | Moderate | Low | Needed for breach investigations and inspections |
| **APATP category (high-water mark)** | **Moderate** | **Moderate** | **Moderate** | |

**Confidentiality was considered for High.** A theft of the full associate register would expose SSNs and bank accounts of about 168,000 people. The team kept confidentiality at Moderate because the harm, while serious, is limited to identity theft and financial loss that notice, credit monitoring, and recovery can contain, and it does not threaten the firm's ability to operate at all. To compensate, the plan adds data minimization (SI-12(1)) and monitoring of bulk exports (AU-6(1)).

## 7. Authorization Boundary Description
**Inside the boundary:**
- the firm's ATS tenant configuration, roles, I-9 module settings, and associate portal settings;
- the payroll platform users, roles, and settings;
- the identity provider tenant;
- the timekeeping tenant settings and the 12 fingerprint clocks;
- the credentialing tenant configuration and client portal settings;
- all 4 cloud accounts and their workloads (integration platform, data warehouse, document archive, BI, backups);
- the networks at HQ, 14 branches, and 6 on-site offices, including 42 kiosks;
- 640 laptops, 230 smartphones, and 60 multifunction devices;
- the firm's SIEM tenant and its use cases.

**Outside the boundary (external services, interconnected):**
- the ATS, payroll, timekeeping, credentialing, VMS, and contact center vendors' platforms;
- the cloud provider's infrastructure;
- the MSSP's platform;
- the background screening provider and drug testing administrator;
- E-Verify (DHS);
- the AI vendors (P10);
- the payroll vendor's bank and the credit line lender.

The diagram is in P04 `cloud-architecture.md`.

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| Background screening provider and drug testing administrator (SYS-07) | Bidirectional (ATS integration) | Candidate identifiers, SSN, authorization; consumer reports; drug test results; adverse action triggers | Screening services agreement with FCRA end-user certification and security terms (2024) |
| E-Verify (SYS-08) | Manual entry on the DHS website | Form I-9 data, photo matching | E-Verify MOU |
| AI screening vendor and recruiting assistant vendor (SYS-09) | Outbound resumes and applications; inbound scores and pre-screen answers | Candidate work history, application answers, phone numbers | ATS marketplace click-through terms. **No data use or security terms (gap, P10)** |
| Payroll platform (SYS-02) via the integration platform | Outbound new hires, rates, time; inbound pay confirmations | SSN, bank, pay, time | Payroll services agreement with security and breach notice terms |
| Timekeeping vendor (SYS-06) via the integration platform | Inbound punches | Time, GPS location, clock enrollment status | Subscription terms. **No breach notice or template retention terms (gap)** |
| Credentialing platform (SYS-10) | Bidirectional (ATS sync; client portal) | License data, health clearances, medical documents | Subscription terms with a confidentiality clause. **No SOC 2 report or breach notice term (gap)** |
| VMS (SYS-11) via the integration platform | Inbound MSP timesheets; outbound invoice data | Contingent worker names, hours, rates | VMS subscription; MSP client contracts |
| Client supervisors and hospital compliance staff | Bidirectional (client portal; credentialing client portal) | Timesheets; clinician compliance files | Client agreements |
| Payroll vendor's bank; credit line lender | Outbound ACH and pay card funding; draw requests | Payroll funding files | Payroll services agreement; credit agreement |
| Contact center platform (SYS-12) | Inbound and outbound calls | Recordings, call notes | Subscription terms |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| ATS and front-office tenant (I-9 module, associate portal, client portal) | SaaS | ATS vendor | Director of Recruiting Operations (recruiting); Director of Compliance and Privacy (onboarding) |
| Payroll, billing, and back-office tenant | SaaS | Payroll vendor | Director of Payroll and Billing |
| Identity provider tenant | SaaS | Identity vendor | IT Director |
| Timekeeping tenant and 12 fingerprint clocks | SaaS; on-premises devices | Timekeeping vendor; On-site Programs 1-6 | Director of Payroll and Billing |
| Credentialing tenant and client compliance portal | SaaS | Credentialing vendor | Credentialing Manager |
| Cloud organization guardrails, identity federation, posture tooling | Identity and policy services | Security and identity account | Security Manager |
| Network hub, cloud firewall, SD-WAN connection, secrets service, log bucket | Network and management services | Shared services account | IT Director |
| Integration platform (containers) | Container service | Workloads account | IT Director (code by the integration contractor) |
| Data warehouse and BI | Managed database | Workloads account | Chief Financial Officer |
| Document archive (scanned Forms I-9 2012-2021; legacy credential files) | Object storage | Workloads account | Director of Compliance and Privacy |
| Backup vault (30-day write-once, second region) | Backup service | Backup account | IT Director |
| SD-WAN edges, firewalls, switches, Wi-Fi | Network | HQ, Branches 1-14, On-site Programs 1-6 | IT Director |
| Laptops (640), kiosks (42), smartphones (230), multifunction devices (60) | Endpoint | All sites | IT Director |
| SIEM tenant | SaaS | MSSP | Security Manager |

## 10. Control Implementation Details
### 10.1 Control implementation status
**Baseline and tailoring.** The APATP uses the NIST SP 800-53B **Moderate** baseline, tailored as follows:
- **Documented here: 113 controls** in `control-implementation.csv`. They cover the controls that carry the firm's legal duties (I-9, E-Verify, FCRA, ADA medical files, Florida), the controls that address the High and Very High risks in P01 (identity, data minimization, monitoring, recovery, vendors), and the controls the MSP clients will test in the SOC 2 examination (P09).
- **Selected by tailoring (added):** PM-1 and PM-2 (not in any SP 800-53B baseline) and PM-9, PT-5, and SI-12(1) (in the privacy baseline). The program-level controls are needed because the program and this system share an owner; PT-5 and SI-12(1) carry the FCRA, AI notice, biometric notice, and SSN minimization duties.
- **Inherited without separate statements:** the remaining Moderate physical and environmental controls for SaaS and cloud data centers (for example PE-9 to PE-17) and platform-level SC and SA controls, evidenced by the vendors' SOC 2 Type 2 reports and reviewed in P09 `vendor-soc2-review.csv`.
- **Deferred:** other Moderate controls with no legal driver and no Moderate-or-higher risk in P01, recorded as tailoring decisions and reviewed yearly.

**Status of the 113 documented controls:**
| Status | Count |
|---|---|
| Implemented | 41 |
| Partially implemented | 68 |
| Planned | 4 |
| Not applicable | 0 |

**Inheritance of the 113 documented controls:**
| Inheritance | Count | Main providers |
|---|---|---|
| System-specific | 68 | Firm |
| Hybrid | 33 | ATS, payroll, identity, and credentialing vendors; cloud provider; MSSP; SD-WAN provider |
| Common/Inherited | 12 | Identity vendor (for example AC-7, IA-2(1)), cloud provider (CP-6, SC-12), MSSP (IR-7), SaaS vendors (AC-12, SC-13) |

The Partially implemented statements trace to the 15 numbered gaps in `../00_company-facts.md` section 4 and to the P07 findings.

### 10.2 Control assessment status
The co-sourced internal audit firm assessed 35 controls from 2026-08-17 to 2026-09-04 (P07 `assessment-plan.md`, `assessment-results.csv`, and `poam.csv`). Weaknesses are tracked in the POA&M and reported to the audit committee each quarter.

### 10.3 Electronic Form I-9 system description
8 CFR 274a.2(e)(5) requires a complete description of each electronic generation or storage system and its indexing system, available on request. This SSP gives the system-level description:
- **Generation and storage since 2021:** the ATS I-9 module. Forms are indexed by associate ID, name, hire date, and branch. Document images are stored with the form. Completed sections are locked, and changes are recorded in a per-form history.
- **Storage of scanned 2012-2021 paper forms:** the document archive in the workloads account, indexed by a spreadsheet of object names and associate IDs.
- **E-Verify case results:** case numbers are recorded in the I-9 module (MOU Art. II.A.7); case printouts are attached to the form.

The step-by-step business process documentation required by 274a.2(f)(1) (how forms are created, corrected, reverified, scanned, and kept, and how audit trails establish integrity) is due 2026-12-31 (POAM-023).

## 11. Digital Identity Acceptance Statement
- **Internal staff.** All staff authenticate through the identity provider with a password and number-matching push MFA, under conditional access that requires a managed device. That fits the Moderate categorization for general users. Push approvals can still be relayed by adversary-in-the-middle phishing kits, so payroll staff and administrators move to phishing-resistant authenticators by 2027-03-31 (P01 R-002, R-035).
- **Associates.** Associates sign in to the ATS associate portal and mobile app with the vendor's login and SMS one-time codes. That does **not** meet the firm's standard for an account that can change where pay is deposited (P01 R-001). Planned: app-based codes or passkeys, plus a verified hold on new bank accounts, by 2026-12-31. Associates' identity is proofed at hire through Form I-9 document examination and E-Verify (IA-12).
- **Client and supplier users.** Client supervisors, hospital compliance staff, and MSP suppliers use vendor-managed accounts in the client portal, the credentialing client portal, and the VMS. MFA is required in the VMS and is planned for the credentialing client portal (IA-8).

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`); BIA (P05); cloud architecture and control map (P04); risk register (P01); gap analysis and roadmap (P03); policies and standards index (P06); assessment and POA&M (P07); incident runbooks (P08); SOC 2 readiness and vendor reviews (P09); AI governance assessment (P10).

## 13. Acronym List and Glossary
- **AHCA:** Agency for Health Care Administration (Florida)
- **APATP:** Associate Payroll and Applicant Tracking Platform
- **ATS:** applicant tracking system
- **CRA:** consumer reporting agency (the background screening provider)
- **EDR:** endpoint detection and response
- **FCRA:** Fair Credit Reporting Act
- **MFA:** multi-factor authentication
- **MOU:** memorandum of understanding (E-Verify)
- **MSP:** managed service provider (contingent workforce program)
- **MSSP:** managed security service provider
- **POA&M:** plan of action and milestones
- **SD-WAN:** software-defined wide area network
- **VMS:** vendor management system

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-07 | Draft from the BIA, risk assessment, and gap analysis | Security Manager |
| 1.0 | 2026-09-22 | Updated with P07 results; approved by the Chief Operating Officer | Security Manager (Information Security Officer) |
