# Intake Report: Cris Santos Company | Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer, one Florida facility) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Security Officer), with the Product Security Lead and the Compliance Manager (Privacy Officer) |
| Approved | COO, 2026-09-04 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the device cloud and the corporate, engineering and factory systems around it, the fielded PM-2 and PM-1 monitors, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walk-throughs, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; HR information system; IT service desk; cloud console; repository; portal administration; MES console | 2026-06-30 to 2026-07-07 |
| Endpoints, facility network and build | EV-009 to EV-013 | Endpoint and EDR consoles; network documentation; build server; source repository; badge system | 2026-06-26 to 2026-07-02 |
| Device cloud | EV-014 to EV-021 | Infrastructure code repository; cloud console; backup service; log analytics; scanner and CI pipeline; database reporting | 2026-06-30 to 2026-07-01 |
| Product security records | EV-022 to EV-030 | PLM; issue tracker; supplier correspondence; company website; ERP | 2023-10-31 to 2026-07-06 |
| Quality system and security program records | EV-031 to EV-040 | eQMS; security@ mailbox; shared drives; IT service desk; COO's files; learning records; HR files; compliance files; support ticketing | 2025-01-01 to 2026-07-06 |
| Suppliers and contracts | EV-041 to EV-045 | ERP payables; contract files; vendor portals | 2025-12-31 to 2026-07-06 |
| Business volume | EV-046 | ERP | 2025-12-31 |
| AI tools | EV-047, EV-048 | Engineering survey and web filter; PLM | 2026-07-06 to 2026-07-07 |

## 3. Observations by area
**Users and access.** Each employee on the HR roster has one named identity provider account with MFA registered, and disabled accounts are deleted after 30 days (EV-001). Single sign-on with MFA covers email, PLM, the repository, ERP, eQMS, VPN, the cloud console and the portal support views, with hardware keys for privileged roles. The MES server and test stations are not in the application list (EV-002). HR recorded 250 employees, 18 terminations and 9 transfers from January to June 2026 (EV-003). Each termination ticket was closed with account disablement on the last working day, and the transfer tickets have no step for device cloud production roles (EV-004). Fourteen support and DevOps engineers hold a standing production role covering all hospital tenants, and the same administrator roles manage the database and its backup copies (EV-005). Portal roles are tenant-scoped and the database enforces row-level security by tenant (EV-006). Twenty-eight hospitals use federation and 12 use local portal accounts with MFA (EV-007). MES and test station operators sign in with one shared account per line and no second factor (EV-008).

**Endpoints, facility network and build.** The endpoint consoles list 205 laptops and 30 desktops, all with EDR and full-disk encryption (EV-009). Lines 1 and 3 sit on separate VLANs behind the OT firewall. Line 2 and its 5 test stations sit on the office VLAN (EV-010). The firmware signing job reads a password-protected key file from the build server's disk. Six build engineers are local administrators, the job has no approval step, and no HSM is recorded (EV-011). Firmware release branches allow the author to approve, and firmware builds do not pin dependency versions (EV-012). The badge system lists holders by door group (EV-013).

**Device cloud.** The infrastructure code lists the components of the device cloud in one active region, with private subnets, a bastion for administration, and unrestricted outbound internet access from the processing services (EV-014). External listeners require TLS 1.2 or higher. PM-2 uses per-device certificates. PM-1 uses one shared API key per hospital, created in 2019 with no rotation record (EV-015). Data and backups are encrypted at rest with provider-managed keys, and service secrets rotate every 90 days (EV-016). Daily backups with point-in-time recovery are copied to a second region. No restore jobs ran from April to June 2026 (EV-017). Logs go to the log analytics service with 30-day retention. Application log fields include patient names and MRNs, and no alert rules or scheduled searches are configured (EV-018). Cloud workloads are scanned monthly and on every build. Firmware components are outside the scanner's scope (EV-019). Container images are not signed at deployment, and the update service distributes only signed PM-2 images (EV-020). The database holds records for about 380,000 patients, and a job deletes records older than 24 months (EV-021).

**Product security records.** The 2024 PM-2 510(k) included a threat model, a security risk assessment, a 2023 penetration test, a manual SBOM and a postmarket management plan section that names no monitoring sources, frequency or personnel (EV-022). The PM-2 threat model (2023) and security risk assessment (2024) have no later revision, and the device cloud threat model is a draft marked incomplete (EV-023). The 2023 PM-2 test is the only penetration test report on file (EV-024). The PM-2 SBOM is dated June 2024, and there is none for PM-1 or the device cloud (EV-025). Three PM-2 releases followed it. The latest is 11 months old, security fixes ship with feature releases, and field update adoption is not recorded (EV-026). PM-2 verifies firmware signatures at boot and before install, and its maintenance interface is enabled by default (EV-027). A supplier notice puts end of support for the PM-1 embedded operating system component in June 2027 (EV-028). The 2024 customer security guide has no end-of-support dates and lists the maintenance interface as disabled (EV-029). About 6,800 PM-2 and 2,100 PM-1 units are in the field at 40 Florida hospitals (EV-030).

**Quality system and security program records.** The complaint, MDR and correction and removal procedures contain no steps for cybersecurity events, and no CVD or product security incident procedure is listed (EV-031). No complaint record refers to the vulnerability reports received at security@ (EV-032). Two external vulnerability reports arrived at security@ in 2026, and one had no reply after 41 days. The website has no disclosure policy page (EV-033). The document request returned a 2024 corporate IT incident response plan, a draft recovery runbook and a hardening standard. It returned no CVD policy, advisory template, ISAO membership record, contingency plan, restore test record, device cloud penetration test, access review, log review, vendor oversight procedure or approved AI tools list (EV-034). A March 2026 phishing incident was handled with EDR isolation and reviewed afterward (EV-035). The IT Manager was designated HIPAA security official for the device cloud on 2026-07-01 (EV-036). Annual awareness training is assigned to every employee (EV-037). The handbook has a code of conduct (EV-038). The device cloud's SOC 2 Type 1 report covers Security as of 2026-03-31 (EV-039), and hospitals ask for a Type 2 report with Availability and Confidentiality (EV-040).

**Suppliers and contracts.** Payments go to the SaaS, cloud and MES vendors, the payroll provider and regulatory counsel. No ISAO fee or AI tool subscription appears (EV-041). BAAs are signed with all 40 hospitals, with notice terms that differ by hospital and no single register of them. Subcontractor BAAs are on file for the cloud provider and the ticketing vendor, and none for the log analytics vendor (EV-042). The 12 hospital VPN connections have no interconnection security terms (EV-043). The cloud provider's SOC 2 Type 2 report covers 2025-04-01 to 2026-03-31 (EV-044). The log analytics and ticketing vendors publish SOC 2 reports (EV-045).

**Business volume.** Revenue was $58 million across 250 business days in FY2025 (EV-046).

**AI tools.** Some engineers report pasting source code into public generative AI assistants, and the web filter shows engineering laptops reaching those sites. No approved-tools list was found (EV-047). AI-001 is in development on 14,200 de-identified images (Fitzpatrick I-II 48%, III-IV 39%, V-VI 13%), and its file index has no bias testing plan (EV-048).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of engineers using public AI assistants, and what they paste | VP Engineering | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Subcontractor BAA or security terms from the log analytics vendor | Compliance Manager (Privacy Officer) | 2026-07-06 | None on file at intake; carried into the P01 risk register (R-009) |
| Field adoption of the 3 PM-2 releases since June 2024 | VP Engineering | 2026-07-06 | No report exists; carried into P03 (G-019) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue (EV-046), installed base (EV-030), backup schedule (EV-017), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-005 to EV-007, EV-009 and EV-014 to EV-021 |
| P04 Cloud mapping | Cloud and SaaS components (EV-014, EV-041) and provider assurance (EV-044, EV-045) |
| P01 Risk register | Likelihood inputs from the configuration exports, the product security records (EV-022 to EV-029), the mailbox review (EV-033) and the incident records (EV-035) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document request response (EV-034) and the QMS procedures (EV-031) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-005) |
| P08 IR runbook | Notification duties from the obligations register; BAA terms (EV-042); contacts from the vendor register |
| P09 SOC 2 | The Type 1 report (EV-039), hospital requests (EV-040), and vendor assurance on file (EV-044, EV-045) |
| P10 AI governance | AI tools found (EV-041, EV-047, EV-048) |
