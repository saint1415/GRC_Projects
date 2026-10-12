# Intake Report: Cris Santos Company | Management of Companies and Enterprises | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company: Building Products, Home Services, Manufacturing, Finance, and Global Business Services; six states) |
| Intake window | 2026-04-06 to 2026-04-30 |
| Collected by | GRC team (second line), with system owners in GBS and each subsidiary, the Integration Management Office, and Internal Audit's prior workpapers |
| Approved | CISO and Chief Compliance Officer, 2026-04-30. Obligations register reviewed by the General Counsel's office, with outside securities counsel (EV-050) |

## 1. Purpose and scope
Intake collected the group's own records before the BIA, the enterprise risk assessment and the gap analysis began on 2026-05-04, and before Internal Audit's control assessment began on 2026-07-13. It covers the holding company, GBS, the four subsidiaries and the two acquired businesses (AQ-01 and AQ-02); the systems that hold financial reporting data, payments, personal information, Finance customer information, plan PHI or MNPI, or that support tier-1 processes; the vendors that touch them; and the rules that may bind the group and its two external service lines (SL-1 and SL-2). Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (BIA interviews, risk workshops, gap analysis samples, Internal Audit tests, AI tests) to the same register, so one list backs every deliverable.

At this size the sources are enterprise systems of record run by GBS and the subsidiaries: the identity platform, PAM and identity governance, the HRIS, the CMDB, the EDR and endpoint consoles, the cloud consoles and SIEM, the third-party risk register and the accounts payable vendor master, the contract repository, treasury and payment hub records, board and committee records, prior Internal Audit and SOX workpapers, and the group's SEC filings.

Each register row names the owning system of record and owner. The [asset inventory](asset-inventory.csv) reconciles the CMDB with the identity, endpoint, cloud, OT and AI records; the [vendor register](vendor-register.csv) reconciles the third-party risk register with the accounts payable vendor master and the contract repository.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Identity and access | EV-001 to EV-009 | Identity platform consoles; PAM; identity governance; HRIS; AQ legacy directories; SCSP application consoles; service desk records | 2026-03-31 to 2026-04-10 |
| Endpoints, network and OT | EV-010 to EV-014 | EDR and endpoint consoles; CMDB; network and firewall management; OT asset register; vulnerability scanner | 2026-03-31 to 2026-04-06 |
| Cloud, logging, backup and recovery | EV-015 to EV-020 | Cloud consoles and posture management; key management; backup accounts; DR records; SIEM; SOC case management | 2026-03-31 to 2026-04-25 |
| Governance, prior assurance and disclosure | EV-021 to EV-029, EV-063 | GRC platform; ERM register; board portal; Internal Audit and SOX files; EDGAR; General Counsel's office; SOC knowledge base | 2025-11-30 to 2026-04-06 |
| Workforce | EV-030, EV-059 | Learning system; HRIS and HR case management | 2026-03-31 |
| Finance and data | EV-031 to EV-034, EV-062 | Finance compliance files; loan platform; data catalog and warehouse; records office; privacy tracker | 2026-03-12 to 2026-04-06 |
| Third parties, contracts and service lines | EV-035 to EV-040, EV-058 | Third-party risk register; AP vendor master; contract repository; vendor portals; service auditor report; service line engineering records | 2025-12-31 to 2026-04-06 |
| Treasury and payments | EV-041, EV-053 | Treasury management system and payment hub; PCI program files | 2026-03-31 |
| Facilities and disposal | EV-042, EV-043 | Physical access system; facilities records; IT asset disposition | 2026-03-31 |
| Business volume and structure | EV-044 to EV-047, EV-061 | ERP financial reporting; operational reporting; legal entity register; Integration Management Office tracker; telecom records | 2025-12-31 to 2026-04-01 |
| AI | EV-048, EV-049, EV-057 | AI governance committee site; SSO application catalog and web proxy; productivity suite admin console | 2026-04-06 to 2026-04-15 |
| Obligations and regulatory status | EV-050 to EV-052 | General Counsel's office; benefits program files; insurance files | 2026-01-01 to 2026-04-24 |
| Other operating records | EV-054 to EV-056, EV-060 | Change management; threat intelligence; SCSP documentation; board portal | 2026-03-31 |

## 3. Observations by area
**Identity and access.** The identity platform holds about 14,500 workforce identities and about 3,100 service accounts. Every workforce account has MFA registered. About 62% of the about 1,180 privileged accounts have a FIDO2 key registered; the rest use push MFA. AQ-01 and AQ-02 users sign in through their own directories (EV-001). MFA is required for every SCSP sign-in, FIDO2 keys are required for treasury approvers and payment releasers, and lockout follows 10 failed attempts (EV-002). Privileged access is vaulted and recorded through PAM, and about 1,900 service accounts are vaulted (EV-003). 410 service accounts have non-expiring passwords; the tiering design sets 6 domain administrator accounts, and the tiering project plan shows that work open (EV-004). Joiner, mover and leaver events flow from the HRIS, and quarterly certifications for the SOX applications closed in each of the last 4 quarters (EV-005). The HRIS holds 12,000 employees in 6 employer entities; the about 2,500 contractors are not HRIS records (EV-006). At AQ-01 and AQ-02, accounts are disabled by hand after HR emails local administrators, and neither directory forwards logs to the group SIEM (EV-007). About 2,900 named users hold SCSP application roles, and the ERP conflict report lists Home Services branch users who maintain small-vendor records and release local payments (EV-008). The outsourced service desk verifies callers with knowledge-based questions before password and MFA resets, including for administrators, and performed about 61% of resets in 2026 Q1 (EV-009).

**Endpoints, network and OT.** The group runs about 15,800 endpoints and about 1,900 servers. EDR reports on about 97% of endpoints, including about 70% of AQ-01 endpoints (EV-010). About 420 virtual machines from every subsidiary run on the shared virtualization layer at DC-1 and DC-2 (EV-011). The SD-WAN covers about 140 sites. AQ-01 and AQ-02 connect by site VPNs whose rules permit the site subnets to reach the integration platform subnet (EV-012). Plants 1 and 2 sit behind IT/OT firewalls and an industrial DMZ; Plant 3 runs one flat network (EV-013). Scans run weekly against a 15-day critical timeframe, and the integration middleware has been out of mainstream support since 2025-12, under extended support (EV-014).

**Cloud, logging, backup and recovery.** Both clouds use account vending, guardrails as code and daily posture scans (EV-015). Keys are customer-managed, and bank files travel over SFTP with PGP (EV-016). Backups sit in separate accounts with write-once retention and a weekly offline copy at DC-2 (EV-017). In the 2026-04-25 tier-1 DR test the identity platform met its 1-hour objective, and the ERP recovered in 9.5 hours against an 8-hour RTO (EV-018). The SIEM does not list the AQ-01 and AQ-02 directories, the plant MES servers or the integration platform administration logs as log sources (EV-019). The SOC runs 24x7 with MSSP overflow and records cases by subsidiary, with no field linking related cases across subsidiaries (EV-020).

**Governance, prior assurance and disclosure.** The program is aligned to CSF 2.0, with a GRC team of 11, a BISO in each subsidiary and a three lines model (EV-021). POL-01 to POL-05 are in their 2025 versions, with standards, procedures and an exception register (EV-022). The 2025 enterprise risk assessment rolled into 8 enterprise risks (EV-023), and the board approved the risk appetite in 2026-02 (EV-024). The audit plans show the identity platform's non-SOX controls last assessed by Internal Audit in 2023 (EV-025). The FY2025 10-K includes Item 1C, management's ICFR report and an unqualified auditor ICFR opinion (EV-026). The 2024 materiality playbook routes incidents that start at the holding company, does not describe incidents that start in a subsidiary or at a shared-services vendor or how related incidents are combined, and was last exercised with the disclosure committee in 2025-03 (EV-027). AQ-01 and AQ-02 trial balances reach consolidation by manual upload (EV-028). The 2026-03-19 tabletop used a payment fraud scenario without the disclosure committee (EV-029).

**Workforce.** Annual training, role-based modules and monthly phishing simulations are recorded (EV-030). Background checks, code of conduct attestation and a sanctions log are on file (EV-059).

**Finance and data.** WISP v4 (2026-02) covers Finance and the services GBS provides; the Qualified Individual was designated in 2024-01 and reported to Finance's board on 2026-03-12 (EV-031). Finance holds about 210,000 loans and customer information on about 520,000 consumers, and about 9,800 dealer portal accounts are created by dealer administrators (EV-032). Finance customer data copied to the warehouse includes full SSNs, and declined-application records from 2022 and 2023 are in the warehouse (EV-033).

**Third parties, contracts and service lines.** The vendor register lists about 2,300 vendors, 420 with access to sensitive data or systems; 18 of 64 tier-1 vendors are past their annual reassessment date, and the outsourced service desk is tiered as tier 2 (EV-035). Home Services branches pay small vendors through local payables (EV-036). The service desk contract sets no identity-verification standard and no audit rights; the intercompany services agreement requires GBS to tell an affected subsidiary of a breach within 10 days (EV-037). The service desk provider's SOC 2 Type 2 report lists two exceptions on reset verification (EV-038). SL-1 issued its 2025 SOC 2 Type 2 report with no exceptions (EV-039). SL-1 and SL-2 agreements commit to 99.9% and 99.5% monthly availability and 72-hour customer notice (EV-040). SL-2 units shipped before 2024 share device certificates per model (EV-058).

**Treasury and payments.** About $1.1 billion a week leaves through 6 banks, the primary bank carries 64% of payment value, approvals need two approvers in the hub and at the bank, and 3 local bank portals outside the hub carry about 6% of payment value (EV-041). Online card fields are hosted by the processor, and a separate PCI program assesses PCI DSS duties (EV-053).

**Facilities and disposal.** DC-1 sits on the Florida headquarters campus with badges, cameras and guards, and plant generators are sized for 24 hours (EV-042). Certificates of destruction are on file (EV-043).

**Business volume and structure.** FY2025 receipts were about $4.8 billion, about $13.2 million per calendar day (EV-044). Volumes per day and week are in EV-045. The group runs 72 branches and 4 distribution centers, 48 branches and 3 plants across six states, and no subsidiary is a bank or savings association (EV-046). AQ-01 and AQ-02 keep their own directories and ERPs, nightly backups only, and migrations planned for 2027 (EV-047).

**AI.** The AI governance committee register records reviews for AI-001 (assistant pilot), AI-002, AI-003, AI-004, AI-006, AI-007 and AI-009. The credit model (AI-002) was retrained in 2025-11, with no fairness test record after the retraining (EV-048). The assistant add-on is licensed for a pilot group, and web filtering blocks known public AI domains (EV-049). The tenant has about 9,800 collaboration sites, sharing with all employees is allowed, and a labeling project for sites holding Restricted data is open (EV-057).

**Obligations.** The group is a large accelerated filer (EV-026), Finance holds consumer lender licenses in six states and takes no deposits (EV-046), the self-insured health plan's sponsor receives PHI for appeals and stop-loss (EV-051), and the cyber policy requires insurer approval before any ransom payment (EV-052). Counsel's view on each candidate rule is in EV-050; the results are in [`obligations-register.csv`](obligations-register.csv).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| AI features turned on inside vendor products and team-level AI tools beyond the committee register | Chief Information Officer; Chief Data and Analytics Officer | 2026-04-17 | Not established at intake; passed to P03 and P10, which treat unregistered AI use as unknown until inventoried |
| OT asset discovery beyond the OT asset register, and the remote access paths into Plants 2 and 3 | Director of OT Security | 2026-04-14 | Not established at intake; the Manufacturing OT security review was scheduled for 2026-06; passed to P01 |
| Contractor end dates for the about 2,500 contractors | Chief Human Resources Officer | 2026-04-09 | Not held in the HRIS; passed to P07 for the termination sample |
| SOC 2 Type 2 report for the benefits third-party administrator | Director of Third-Party Risk Management | 2026-04-14 | Not received at intake; passed to P05 |
| Finance's 2026 written risk assessment | Finance Information Security Officer | 2026-04-14 | In progress at intake (due 2026-06); passed to P03 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Entities, sites and workforce (EV-006, EV-046), receipts and volumes (EV-044, EV-045, EV-032), recovery records (EV-017, EV-018), payment concentration (EV-041), contract RTOs (EV-037), AQ status (EV-047), and dependencies from the asset and vendor registers |
| P02 SSP | The SCSP boundary from the asset inventory (SYS-01 to SYS-04 and SYS-04-INT); prior SSP v2.0 and contingency plan v5 (EV-056); as-found configuration from EV-001 to EV-005, EV-008 to EV-012, EV-014 to EV-019 and EV-041 |
| P04 Cloud mapping | Cloud components and guardrails (EV-015 to EV-019) and provider assurance (EV-038) |
| P01 Risk register | Likelihood inputs from threat intelligence (EV-055), the SOC case history (EV-020), coverage and configuration exports, the 2025 enterprise risk assessment (EV-023) and the board's risk appetite (EV-024) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2025 policy set and exception register (EV-022) |
| P07 Control assessment | Populations to sample from (EV-005, EV-006, EV-008, EV-009, EV-011, EV-014, EV-017, EV-020, EV-054) and prior Internal Audit workpapers (EV-025) |
| P08 IR runbook | Notification duties from the obligations register; disclosure committee records (EV-027); contract notice terms (EV-037, EV-040); contacts from the vendor register |
| P09 SOC 2 | The SL-1 2025 report (EV-039), service line agreements (EV-040) and vendor assurance on file (EV-038) |
| P10 AI governance | AI tools found (EV-048, EV-049) and tenant sharing settings (EV-057) |
