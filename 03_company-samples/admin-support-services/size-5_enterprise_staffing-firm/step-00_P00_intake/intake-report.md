# Intake Report: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company: about 380 branches and 140 on-site offices in 38 states and DC; 12,000 internal employees; about 78,000 associates on assignment a week) |
| Intake window | 2026-05-04 to 2026-05-29 |
| Collected by | GRC team (second line), with system owners in each segment, the Integration Management Office and Internal Audit's prior workpapers |
| Approved | CISO and Chief Compliance Officer, 2026-05-29. Obligations register reviewed by the General Counsel's office, with outside securities counsel (EV-064) |

## 1. Purpose and scope
Intake collected the firm's own records before the enterprise risk analysis, the BIA and the gap analysis began on 2026-06-01, and before Internal Audit's control assessment began on 2026-07-13. It covers the organization (about 520 sites, the four segments, and the acquired firms ACQ-1 and ACQ-2), the systems that hold associate, candidate, client or pay data or support tier-1 processes, the vendors that touch them, and the rules that may bind the firm and its two client service lines (SL-1 and SL-2). Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (BIA interviews, risk workshops, gap analysis samples, Internal Audit tests, the AI portfolio review) to the same register, so one list backs every deliverable.

At this size the sources are enterprise systems of record across the segments: the identity platform and HCM system, the CMDB and EDR console, the cloud consoles and SIEM, the payroll engine and its integrations, the onboarding and Form I-9 platform, the third-party risk register and accounts payable vendor master, the contract repository, board and committee records, prior Internal Audit and SOX workpapers, and counsel's memos.

Each register row names the owning system of record and owner. The [asset inventory](asset-inventory.csv) reconciles the CMDB with the cloud account inventory, the EDR and endpoint consoles, the integration route inventory and the AI register; the [vendor register](vendor-register.csv) reconciles the third-party risk register with the accounts payable vendor master and the contract repository.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Identity and access | EV-001 to EV-009 | Identity platform (SSO, PAM, identity governance); HCM system; ACQ-1 directory; ALPP component consoles; associate app settings; E-Verify reports | 2026-04-30 to 2026-05-06 |
| Endpoints, devices and network | EV-010 to EV-015 | EDR and endpoint consoles; CMDB; network management; scanner | 2026-04-30 to 2026-05-04 |
| Cloud, data, logging, backup and recovery | EV-016 to EV-028 | Cloud consoles and posture management; backup accounts; key management; data catalog and data platform; SIEM; SOC case management; DR records; change and pipeline systems; integration platform; file transfer service; audit settings | 2026-04-30 to 2026-05-16 |
| Governance, prior assurance and disclosure | EV-029 to EV-034, EV-039 to EV-041 | GRC platform; ERM register; board portal; Internal Audit and SOX workpapers; General Counsel's office; SEC filing | 2025-12-31 to 2026-05-01 |
| Employment eligibility and screening | EV-035 to EV-038 | Onboarding and Form I-9 platform; DC-2 archive; ACQ-1 contract files; screening provider records | 2026-04-30 to 2026-05-08 |
| Workforce, associate service and fraud | EV-042 to EV-044 | Learning system; CCaaS and service desk records; payroll fraud tracker | 2025-12-31 to 2026-04-30 |
| Third parties, contracts and service lines | EV-045 to EV-050 | Third-party risk register; AP vendor master; contract repository; vendor portals; service auditor report; WMP and payrolling records | 2025-12-31 to 2026-05-01 |
| Facilities, disposal and retention | EV-051 to EV-053 | Physical access system; IT asset disposition; records management | 2026-04-30 to 2026-05-01 |
| Business volume and structure | EV-054 to EV-058 | ERP financial reporting; operational reporting; legal entity register; Integration Management Office tracker; ACQ-1 records | 2025-12-31 to 2026-05-15 |
| AI | EV-059 to EV-061 | AI governance council register; SaaS and AI feature discovery; AI-001 records | 2026-04-30 to 2026-05-20 |
| Obligations | EV-062 to EV-064 | General Counsel's office; outside counsel | 2026-04-17 to 2026-05-27 |
| Other operating records | EV-065 to EV-069 | Treasury; payroll tax files; threat intelligence; Privacy Office; insurance files | 2026-01-01 to 2026-04-30 |

## 3. Observations by area
**Identity and access.** Internal staff sign in through SSO with MFA; the about 900 ACQ-1 staff use the ACQ-1 legacy directory, which is not federated and where ACQ-1 IT enters disable dates by hand (EV-001, EV-006). MFA is required for every SSO application, FIDO2 keys for privileged roles, and lockout follows 10 failed attempts (EV-002). The 64 privileged ALPP accounts are vaulted in PAM with just-in-time elevation and session recording (EV-003). Joiner, mover and leaver events flow from the HCM system, and 4 quarterly certification campaigns closed in the last 12 months; the ACQ-1 directory and E-Verify are not connected to the workflows (EV-004). HCM holds about 12,000 internal employees, and ACQ-1 terminations reach ACQ-1 IT through a weekly report (EV-005). About 9,800 workforce users work in the ALPP components; the 38 payroll configuration administrators also hold the payroll release permission, and bulk export rights sit with 14 roles (EV-007). About 310,000 associates sign in to the app with a password and an SMS code and change bank accounts there with no out-of-band confirmation configured (EV-008). About 1,100 named E-Verify accounts are managed in E-Verify outside SSO, reviewed quarterly, and E-Verify is not on the HR termination checklist (EV-009).

**Endpoints, devices and network.** EDR reports on 98% of about 15,650 endpoints; the endpoints without the agent are time clocks and legacy kiosks (EV-010). Laptops have full-disk encryption and remote wipe (EV-011). The CMDB lists the 140 on-site time clocks by site only, without firmware or administrator settings (EV-012). The time clock server in DC-1 runs an unsupported operating system on an isolated VLAN (EV-013). SD-WAN reaches about 520 sites; lobby kiosks at 46 legacy branches sit on the branch staff network; ACQ-1 connects through a restricted site VPN on an appliance patched outside the enterprise process (EV-014). Scans run weekly, and the 2026-04 penetration test report is on file (EV-015).

**Cloud, data, logging, backup and recovery.** About 180 cloud accounts are created by account vending with guardrails as code and daily posture scans (EV-016). Backups sit in separate accounts with write-once locks and a weekly copy to DC-2; the payroll database is restore-tested monthly (EV-017). Keys are customer-managed (EV-018). SSNs and bank numbers are tokenized inside the payroll engine, but the nightly extract carries them in full to the data platform for about 2.9 million people (EV-019), where 41 analytics users can query them (EV-020). The SIEM does not list the ACQ-1 systems or the DC-2 archive server as sending, and no use case covers bulk export or associate bank changes (EV-021). The SOC runs 24x7 with MSSP overflow; several ACQ-1 incidents have no SOC case (EV-022). In the 2026-05-16 DR test the payroll engine met its RPO and recovered in 9.5 hours against an 8-hour RTO, and the WMP met its 4-hour RTO (EV-023); contingency plan v3 predates that test (EV-024). Pay rule and tax table changes are approved inside payroll operations (EV-025). About 400 client VMS integrations use shared service accounts, and 63 API keys are older than 2 years (EV-026). Pay files are staged on SFTP with no hash comparison recorded between approval and transmission (EV-027). Bank changes, releases and file approvals are written as signed audit entries (EV-028).

**Governance, prior assurance and disclosure.** The 2025 policy set (POL-01 to POL-05) sits in the policy portal with standards, procedures and an exception register (EV-029). The board approved the security strategy and risk appetite in 2026-02; the CSF 2.0 current profile is Tier 3 for the enterprise and Tier 2 practices at ACQ-1 (EV-030, EV-032). The 2025 risk analysis rolled into enterprise risks under NIST IR 8286 (EV-031). Internal Audit's 2025 ALPP assessment and the FY2025 SOX ITGC testing are on file (EV-033). Common controls are published by 9 providers, with monthly metrics and a POA&M (EV-034). The disclosure committee has 7 members; the CFO and General Counsel joined in 2026, the minutes record no exercise of the materiality playbook since then, and the playbook has no method to estimate client contract and associate remediation costs (EV-039). The FY2025 10-K includes Item 1C (EV-040). The 2026-03-19 tabletop covered payroll diversion and data theft without the disclosure committee (EV-041).

**Employment eligibility and screening.** The firm holds the E-Verify MOU and Federal contractor enrollment, and SYS-02 enforces Section 2 deadlines, computes retention dates and keeps a permanent audit trail (EV-035). The DC-2 archive holds about 1.4 million scanned Forms I-9 (2009-2019); its server records no access events, and about 410,000 forms from 2009-2012 are not indexed (EV-036). ACQ-1's legacy system vendor contract, which holds about 38,000 ACQ-1 Forms I-9, has no export clause, and 9 ACQ-1 vendor contracts have no 72-hour notice term (EV-037). The ACQ-1 FCRA disclosure form includes a liability waiver, and screening provider 2's contract has no 72-hour notice term (EV-038).

**Workforce, associate service and fraud.** Training, role-based modules and monthly phishing simulations are recorded; the Associate Service Center curriculum has no bank-change social engineering module (EV-042). Agents verify callers with knowledge questions, and IT service desk resets rely on employee ID and manager name (EV-043). In 2025, 214 fraudulent associate bank changes diverted about $612,000, which the firm repaid; out-of-band confirmation and scoring apply only to internal staff changes (EV-044).

**Third parties, contracts and service lines.** The vendor register lists about 1,400 vendors, 220 with personal information; 31 of those have a last assessment older than the annual schedule, including the paycard program manager (EV-045, EV-046). Contract templates carry 72-hour notice terms; 37 hospital agreements carry BAAs; Government Solutions holds 34 federal and 21 state agency contracts (EV-047). SOC reports are on file for the clouds, colocation, the ATS, onboarding, time capture, screening and AI ranking vendors (EV-048). The SL-1 2025 SOC 2 Type 2 report had no exceptions (EV-049). SL-1 serves about 60 client programs; SL-2 serves about 340 clients, with its system description in draft (EV-050).

**Facilities, disposal and retention.** Payroll centers and colocation cages use badge plus PIN with quarterly reviews (EV-051). Certificates of destruction are on file (EV-052). Retention schedule STD-04.2 sets periods, and no purge is scheduled in SYS-01, SYS-02 or the data platform (EV-053).

**Business volume and structure.** FY2025 revenue was about $4.8 billion, about $13.2 million per calendar day, with about $65 million of associate pay each week (EV-054). About 78,000 associates are on assignment in an average week (EV-055). The firm runs about 520 sites in 38 states and DC (EV-056). ACQ-1 keeps its own directory, ATS, credentialing system and outsourced payroll until 2027-03-31; ACQ-2 identities were federated in 2026-05 (EV-057). ACQ-1's legacy ATS has no restore test record, and its payroll provider's contract states a 48-hour RTO (EV-058).

**AI.** The AI governance council register lists 8 use cases, 6 with completed review (EV-059). Feature discovery found 2 more outside the register, the branch redeployment ranking (AI-009) and timesheet anomaly flags (AI-010), for 10 in total (EV-060). AI-001 runs sort-only; its NYC bias audit (2026-02-09) covers NYC applicants, and its other fairness records cite vendor data (EV-059, EV-061). The council register records no workflow for Colorado SB26-189 deployer duties (EV-059).

**Obligations.** The firm is an SEC registrant (EV-040), the employer of record that completes Forms I-9 and runs E-Verify as a Federal contractor (EV-035), a user of consumer reports (EV-038), and a federal contractor holding federal contract information (EV-047). Counsel's view is that the firm is not a HIPAA business associate for clinician placements (EV-062). Counsel's state breach matrix is EV-063, and counsel's view on each candidate rule is in EV-064; the results are in [`obligations-register.csv`](obligations-register.csv).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Current SOC report from the paycard program manager | Director of Third-Party Risk Management | 2026-05-07 | Not received at intake; carried to P07 SA-9 and POAM-009 |
| Logs from the ACQ-1 directory, ATS, credentialing system and edge VPN | Vice President, Integration Management Office | 2026-05-07 | Not available at intake; P07 AU-6 and POAM-003 |
| ACQ-1 incident records kept by ACQ-1 IT | Vice President, Integration Management Office | 2026-05-12 | Partial; P07 sampled the 5 ACQ-1 incidents of 2026 H1 (IR-4) |
| 2026 Q2 E-Verify quarterly user review | Director of Employment Eligibility Compliance | 2026-05-06 | Due after intake; collected in P03 fieldwork (EV-078) |
| Record counts past the retention schedule in SYS-01, SYS-02 and the data platform | Vice President, Employment Compliance; Chief Data Officer | 2026-05-08 | Not established at intake; counted in P03 fieldwork (EV-082) |
| AI features embedded in vendor products beyond the discovery review | CIO | 2026-05-22 | Not established at intake; P10 treats further embedded features as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-005, EV-056), revenue, payroll and volumes (EV-054, EV-055), recovery records (EV-017, EV-023, EV-024), pay delivery (EV-065), ACQ-1 dependencies (EV-057, EV-058), and dependencies from the asset and vendor registers |
| P02 SSP | The ALPP boundary from the asset inventory (SYS-01 to SYS-04, SYS-03-SF, SYS-03-IP, SYS-04-TC, SYS-06-ARC); as-found configuration from EV-001 to EV-028 and EV-035, EV-036 |
| P04 Cloud mapping | Cloud components and guardrails (EV-016 to EV-021) and provider assurance (EV-048) |
| P01 Risk register | Likelihood inputs from threat intelligence (EV-067), fraud losses (EV-044), SOC case history (EV-022), coverage and configuration exports, the prior risk analysis (EV-031) and the risk appetite (EV-032) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2025 policy set and exception register (EV-029) |
| P07 Control assessment | Populations to sample from (EV-004, EV-005, EV-007, EV-009, EV-012, EV-015, EV-017, EV-022, EV-025, EV-026, EV-045) and prior Internal Audit workpapers (EV-033) |
| P08 IR runbook | Notification duties from the obligations register; disclosure committee records (EV-039); the state matrix (EV-063); contacts from the vendor register |
| P09 SOC 2 | Vendor assurance on file (EV-048), the SL-1 2025 report (EV-049) and service line records (EV-050) |
| P10 AI governance | AI tools found (EV-059, EV-060, EV-061) and AI subscriptions (EV-046) |
