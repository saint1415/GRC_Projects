# Intake Report: Cris Santos Company | Finance and Insurance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank, six Florida branches; subsidiary of Cris Santos Company, a bank holding company) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Officer), with the Compliance Officer |
| Approved | President and CEO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the bank's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that store, process or transmit customer information, the service providers that touch them, and the rules that may bind the bank and its holding company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-011 | Identity provider; HR information system; IT help desk tickets; core security administration; online banking admin console; wire platform; customer service procedures | 2024-03-01 to 2026-07-02 |
| Devices and network | EV-012 to EV-016 | Device management and EDR consoles; IT build records and token register; network documentation; MSSP portal and agreement | 2025-01-01 to 2026-07-01 |
| Cloud and backups | EV-017 to EV-019 | Cloud provider console; backup service; credit decisioning service logs | 2026-06-30 to 2026-07-01 |
| Governance and program documents | EV-020 to EV-029 | Board portal; ISO files; HR; policy library; core processor portal; internal audit and penetration test reports | 2023-04-14 to 2026-06-30 |
| People, training and procedures | EV-030 to EV-036 | Learning management system; HR files; IT change log; deposit operations and treasury files; wire platform reporting; BSA case system; online banking fraud queue | 2024-09-01 to 2026-06-30 |
| Suppliers, contracts and charter | EV-037 to EV-043 | Accounts payable system; contracts folder; vendor management files; provider portals; corporate records | 2025-12-31 to 2026-07-06 |
| Facilities and disposal | EV-044 to EV-047 | Walk-through; badge system; ATM vendor reports; shredding certificates and IT tickets | 2026-06-30 to 2026-07-08 |
| Business volume | EV-048 to EV-050 | General ledger; core and online banking reporting; loan origination system | 2025-12-31 to 2026-06-30 |
| Email and AI tools | EV-051 to EV-053 | Productivity suite admin console; model file and model inventory; staff survey and identity provider app list | 2026-07-02 to 2026-07-08 |

## 3. Observations by area
**Users and access.** 120 active named workforce accounts, each with MFA registered; administrators use hardware keys (EV-001). MFA is required for email, remote access, the cloud console, the admin console and the wire platform. Push approval without number matching is allowed for non-privileged users, and sign-in logs are kept at the 30-day default (EV-002). HR lists 120 employees by department and every separation in the 12 months to June 2026 (EV-003). Disable tickets for the identity provider, admin console and wire platform close 1 to 3 business days after the last working day, and the ticket template has no core banking step (EV-004). Five core accounts hold the bank-level super user role (EV-005). The last core entitlement review is dated 2025-05-20 and does not include super user roles (EV-006). Three IT staff hold the full administrator role in the admin console (EV-007). Customer MFA is set to optional and is enabled by 31% of consumer and 58% of business users. Adding a wire beneficiary asks for a second factor only from users who have enabled MFA, and no alert rules are set for beneficiary or limit changes (EV-008). The wire platform requires a second user to approve every outgoing wire; the 2 approvers also hold the template maintenance role (EV-009). Admin console and wire platform logging is on, with no saved reports or report runs in 2025 or 2026 (EV-010). Phone resets of customer passwords are verified with knowledge questions (EV-011).

**Devices and network.** The device console lists 110 workstations and laptops, including 34 teller workstations, 2 payments workstations and 5 wire-room PCs. EDR reports on all of them, patches install within 14 days, and laptops report full-disk encryption (EV-012). The payments workstations run a hardened image with an allow-list, and a spare is recorded at Branch 4 (EV-013). Payments workstations sit on an isolated segment; teller and back-office devices share one segment at each branch; firewall firmware is updated quarterly (EV-014). The MSSP monitors EDR, firewall and cloud management alerts 24x7; the admin console, wire platform, identity provider and core are not among its sources (EV-015). Vulnerability scanning is not in the MSSP's service scope (EV-016).

**Cloud and backups.** The cloud tenant holds 4 workloads in one account, with 2 named administrators who manage both production and backups. No configuration baseline or posture monitoring service is enabled, and identity and admin console logs are not forwarded to the log archive (EV-017). Daily backups completed from April to June 2026. Vault immutability is off, the vault is in the production account, and no restore jobs were run (EV-018). The credit model's version is pinned and hashed at each release, and every scoring request is logged with its reason codes (EV-019).

**Governance and program documents.** The board approved the written program on 2025-11-18, designated the IT Manager as ISO, and receives an annual report each December. No risk appetite or tolerance statement appears in the minutes (EV-020). The December 2025 report has no sections on service provider oversight, testing results or security events (EV-021). The December 2025 risk assessment lists generic threats, does not list business email compromise, account takeover or service provider threats, and sets no tolerance thresholds (EV-022). The ISO also runs IT operations and reports to the COO (EV-023). The program document keeps its 2021 structure and does not mention 12 CFR Part 53 or the AI credit model (EV-024). The 2023 incident response plan has no OCC or Federal Reserve notice step and no definition of a notification incident (EV-025). The 2025 business continuity plan includes an alternate wire procedure, last tested in 2023, and names no alternate site for the wire room (EV-026). The bank took part in the core processor's 2025 disaster recovery test (EV-027). The 2025 IT audit and the 2025 external penetration test are on file (EV-028, EV-029).

**People, training and procedures.** Annual awareness training and two phishing simulations a year are recorded; content was last updated in 2024 and has no business email compromise or wire-fraud module (EV-030). Background checks were completed before start for every hire in the period, and 2026 ethics acknowledgments are signed (EV-031). The IT change log has no entries for admin console or wire platform settings (EV-032). The written callback standard requires a callback to the number on file for any wire request received by email or phone (EV-033). The wire platform sends about 35 outgoing wires a business day, about $4 million a day (EV-034). SARs are filed within 30 days, and payment-fraud cases are tracked in the BSA case system apart from IT incident records (EV-035). Online banking fraud alerts are worked in business hours (EV-036).

**Suppliers, contracts and charter.** Payments went to 17 suppliers, including an AI model vendor from May 2026 (EV-037). The core processor contract (2019, renewal due 2027) and the digital banking provider contract (2021) have confidentiality and security provisions and no incident notice time frame (EV-038). SOC reports are filed each year for the core processor, digital banking provider and card processor, with no review memo, CUEC mapping or bridge letter, and no provider has been given a 12 CFR 53.4 contact (EV-039). The core processor's SOC 1 and SOC 2 Type 2 reports cover the 12 months ending 2026-03-31 and state an RTO of 4 hours and an RPO of 15 minutes (EV-040). Provider SOC 2 reports for online banking, the cloud and the identity provider are on file (EV-041, EV-042). The bank holds an OCC national bank charter, and its holding company has no other operations (EV-043).

**Facilities and disposal.** Badge readers control the wire room, operations center and records room. The operations center and wire room share the main office building (EV-044). Nine people are on the wire room door group (EV-045). All 9 ATMs have anti-skimming hardware; no tamper alert devices are listed for the 3 off-site ATMs (EV-046). Paper destruction certificates are on file; drives and ATM disks were destroyed with no certificate (EV-047).

**Business volume.** Net revenue was about $20 million across 250 business days in FY2025, about $80,000 a business day, and total assets were $510 million (EV-048). The bank has about 13,800 consumer and 2,200 business deposit customers and 140 ACH originators (EV-049). About 350 small business loan applications arrive each year (EV-050).

**Email and AI tools.** Email uses TLS, and no rule encrypts outbound messages or attachments that carry loan documents (EV-051). The AI credit model has been in pilot at 3 branches since May 2026. Its file holds the vendor's documentation and no validation report, fair lending test or reason-code review, and the CFO's model inventory does not list it (EV-052). Staff report using public generative AI chatbots, and no approved-tools list was found (EV-053).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Payments service provider's current SOC 2 report | Deposit Operations Manager | 2026-07-06 | Received 2026-07-15 (EV-059, intake follow-up) |
| Number of staff using public chatbots, and what they paste | Chief Operating Officer | 2026-07-08 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue and volumes (EV-034, EV-048, EV-049, EV-050), the continuity plan and core recovery objectives (EV-026, EV-040), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-007 to EV-014 and EV-051 |
| P04 Cloud mapping | Cloud and SaaS components (EV-017, EV-037) and provider assurance (EV-040 to EV-042) |
| P01 Risk register | Likelihood inputs from the fraud records (EV-035, EV-036), configuration exports, the vendor files and the walk-through |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the Guidelines and 12 CFR Part 53 |
| P06 Policies | The program document (EV-024) and the 2023 incident response plan (EV-025) |
| P07 Control assessment | Populations to sample from (EV-003, EV-004, EV-005, EV-034) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register |
| P09 SOC 2 | Core processor reports and other provider assurance on file (EV-039 to EV-042) |
| P10 AI governance | AI tools found (EV-037, EV-052, EV-053) |
