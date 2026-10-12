# Intake Report: Cris Santos Company | Communications | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier, Florida) |
| Intake window | 2026-06-15 to 2026-07-02 |
| Collected by | GRC analyst and the Security Manager, with the vCISO and the Vice President of Regulatory Affairs |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-06. It covers the organization, the systems that hold CPNI and subscriber personal information or run the voice and broadband network, the suppliers that touch them, and the rules that may bind the company. At this size the sources are systems of record: the identity provider, the HR system, the endpoint and EDR consoles, the OSS network inventory, the TACACS+ and firewall configurations, the cloud organization console, the SIEM and MDR portal, the BSS and SYS-18 consoles, the accounts payable vendor master, the vendor access register and contract register, FCC filing records, NOC and 911 reliability files, internal audit reports, scan results and the incident log. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-007 | Identity provider; HR system; access review campaigns; privileged access tools; BSS, contact center and SYS-18 consoles | 2026-02-27 to 2026-06-30 |
| Devices and network | EV-008 to EV-016 | Endpoint, EDR and mobile device consoles; OSS network inventory; TACACS+, syslog and configuration backup servers; firewalls; scanner; advisory tracker; lifecycle register; configuration repository; change system | 2026-06-15 to 2026-06-30 |
| Cloud, backups and monitoring | EV-017 to EV-021 | Cloud organization console; backup service; test records; MDR portal and SIEM | 2026-06-24 to 2026-06-30 |
| Programs and documents | EV-022 to EV-029 | Intranet library; security team library; incident tracker; learning management system; HR files; internal audit; executive files; NOC procedures | 2025-10-31 to 2026-06-30 |
| CPNI and customer channels | EV-030 to EV-035 | Regulatory affairs files and FCC filing record; BSS console; campaign tool; mailing vendor reports; overflow vendor files; portal and chatbot configuration | 2025-05-31 to 2026-06-30 |
| Regulatory records for the network | EV-036 to EV-041 | CALEA room safe and filing history; NOC and FCC NORS and DIRS records; 911 reliability files; facilities maintenance system; RMD record and traceback log; purchasing procedures | 2025-10-15 to 2026-06-30 |
| Suppliers and contracts | EV-042 to EV-048 | ERP accounts payable; vendor access register; vendor portals; contract register; sales proposal files; insurance policy | 2026-03-31 to 2026-06-30 |
| Facilities and media | EV-049, EV-050 | Badge and alarm systems; destruction certificates | 2026-06-30 |
| Business volume and customer commitments | EV-051 to EV-053 | ERP general ledger; BSS, OSS and contact center reporting; website and legal files | 2025-12-31 to 2026-06-30 |
| Business Services and AI tools | EV-054, EV-055 | Hosted voice and SD-WAN consoles; identity provider app list, accounts payable and department heads survey | 2026-06-29 to 2026-06-30 |

## 3. Observations by area
**Users and access.** The identity provider holds named accounts for the 850 employees on the HR roster plus contractor, vendor agent and service accounts, and every active user account has MFA registered. Cloud and identity administrators use hardware security keys; 40 field supervisors still have SMS as a fallback factor (EV-001). Conditional access requires MFA for email, single sign-on applications, the VPN and the cloud console (EV-002). HR recorded 142 terminations and 77 internal transfers in the 12 months to 2026-06-30 (EV-003). Access reviews run twice a year; the February 2026 campaign covered identity provider groups and BSS roles (EV-004). There are 118 privileged accounts across all administration planes. TACACS+ with MFA covers core routers, broadband network gateways and internet edge routers. OLTs, DSLAMs, cabinet switches, CLEC metro switches and SBCs are administered with shared local accounts without MFA, and privileged access management covers Windows servers and the cloud accounts (EV-005). 61 users hold the BSS bulk export right, and 188 BSS accounts were created in the 12 months (EV-006). SYS-18 bills about 6,800 CLEC business accounts with shared administrator accounts, no account-change notices and no forwarding of logs to the SIEM (EV-007).

**Devices and network.** The endpoint consoles list 860 laptops and desktops and 64 servers, all with EDR, and 420 field tablets under mobile device management (EV-008). The OSS inventory lists about 2,100 access elements, 268 cabinets and the 14 tagged legacy 911 circuit pairs. About 140 POP devices from the CLEC acquisition are in a separate spreadsheet (EV-009). Network element syslog and TACACS+ accounting are kept 90 days on local collectors, and element configurations are backed up nightly to CO-1 with a copy at CO-4 (EV-010). At POP-A and POP-B the management VLAN is routed to the corporate VLANs, and the lawful-intercept system is reached over the same management path (EV-011). Servers and cloud workloads are scanned monthly and internet-facing addresses quarterly, with 50 critical findings in the first half of 2026; network elements are not in the scan scope (EV-012). Two internet edge routers were patched after the 30-day target for critical advisories (EV-013). The TDM switches have been out of vendor support since 2024, and 2 SBCs reach end of support on 2026-12-31 (EV-014). Golden configurations exist for core routers and broadband network gateways only (EV-015). 412 changes were made in 2026 Q2; hosted voice platform changes are recorded in team chat (EV-016).

**Cloud, backups and monitoring.** The landing zone has 5 accounts with guardrails and company-managed keys. CDR archive object-level read logging is not enabled, and the mediation service account has read and write rights (EV-017). Daily backups go to a separate backup account in a second region with 35-day write-once retention and separate credentials (EV-018). Restore records exist for the OSS (2026-04) and the NOC failover to CO-4 (2026-03) only (EV-019). The SIEM receives identity provider, cloud, EDR, firewall, VPN and BSS audit logs; network element syslog, TACACS+ accounting, CDR archive reads, SYS-15 and SYS-18 are not connected. The MDR contract requires a call within 30 minutes of a high-severity alert (EV-020, EV-021).

**Programs and documents.** The library holds five policies adopted in 2024 and three standards; there is no configuration, logging, vendor risk, network element or AI standard (EV-022). The 2024 incident response plan's CPNI breach section sends notice to the FCC with a 30-day customer notice and has no 7-business-day hold. One IT-only tabletop was run in 2025 (EV-023). 41 security incidents were logged in the 12 months (EV-024). Annual awareness and CPNI training is 96% complete, and the June 2026 phishing click rate was 6.1% (EV-025). The sanctions policy names misuse of CPNI (EV-026). The 2025 internal IT audit was reported to the audit committee (EV-027). The CPNI compliance officer, CALEA senior officer, 911 certifying official and Security Manager are designated in writing (EV-028). The request for an IT contingency plan returned the NOC outage and storm plan only (EV-029).

**CPNI and customer channels.** The CPNI procedures (2024) name SYS-01, the care center and the stores. The calendar year 2025 certification was filed on 2026-02-27; its statement describes the chatbot authentication as compliant (EV-030). The BSS records approval flags with history, enforces a 33-day wait after an opt-out notice, holds per-account passwords and sends change notices for the four change types (EV-031). The campaign tool lists 14 campaigns that used CPNI in the 12 months (EV-032). The biennial notice was mailed in 2025-05 to SYS-01 accounts only (EV-033). 35 overflow agents use the BSS agent desktop, including the call detail screens, and the vendor's training records show no CPNI course (EV-034). Portal and app resets use a one-time code to the number or email of record; the chatbot's "verify me" fallback accepts the last 4 SSN digits and the service address (EV-035).

**Regulatory records for the network.** The ILEC CALEA SSI policies were filed in 2019, and nothing has been filed since, including after the 2025-07-01 merger (EV-036). The NOC filed 6 NORS reports in the 12 months; PSAP contacts for POP-served areas were last confirmed in 2024; hosted voice alarms go to Business Services, not the NOC (EV-037). Annual 911 reliability certifications were filed through 2025, and the 2025 diversity audit records 2 of 14 legacy 911 circuit pairs sharing one fiber segment (EV-038). The CO-6 generator failed its full-load test on 2026-05-14 (EV-039). The RMD certification still names a contact who left on 2026-04-10, and 16 of 18 traceback requests were answered within 24 hours (EV-040). Purchasing has no Covered List check for used or refurbished equipment (EV-041).

**Suppliers and contracts.** Accounts payable paid about 180 vendors (EV-042). 34 vendors have access to CPNI, subscriber PII or the network; 12 Tier 1 vendors have security review records and 22 have none. The chatbot and contact center contracts have no clause barring training on company data and no 24-hour incident notice term (EV-043). The BSS vendor's SOC 2 Type 2 report states RTO 12 hours and RPO 1 hour (EV-044). The cloud provider's SOC 2 report is on file (EV-045). Customer contracts carry 99.99% SLAs, and 320 enterprise contracts set CPNI authentication terms (EV-046). Seven Business Services customers ask for a SOC 2 Type 2 report (EV-047). The cyber insurance policy has a $15 million limit and a $500,000 retention (EV-048).

**Facilities and media.** Badge door groups, cameras and alarms cover the central offices, POP-A and the CO-1 data hall, and the CALEA room needs two-person entry (EV-049). Destruction certificates are on file for retired drives (EV-050).

**Business volume and customer commitments.** Annual receipts were $318 million in FY2025, about $871,000 per day (EV-051). The company serves about 205,000 accounts, about 197,000 broadband subscribers and about 74,000 voice lines, and handles about 9,500 customer contacts a day (EV-052). The recording notice on care calls does not mention AI transcription (EV-053).

**Business Services and AI tools.** The hosted voice cluster and its standby node share the CO-1 data hall, which has one cooling plant. Cluster configuration backups have no restore record, and new hosted voice tenants are onboarded with a manual checklist (EV-054). Four AI tools are in use: the chatbot, agent assist, NOC alarm correlation and the churn model. Agent assist, alarm correlation and the churn model have no security or CPNI review record. Staff report using public generative AI tools, and there is no approved-tools list (EV-055).

**Reconciliation across sources.**
- **Workforce.** The 850 employees on the HR roster each have an identity provider account (EV-001, EV-003).
- **Accounts.** About 198,000 accounts in SYS-01 plus about 6,800 in SYS-18 give the about 205,000 accounts in the volume report (EV-007, EV-052).
- **Network inventory.** The OSS count of access elements excludes the about 140 POP devices in the acquisition spreadsheet. That difference stays an open request.
- **Vendors.** About 180 vendors in accounts payable, 34 with access, 12 of them with review records (EV-042, EV-043). The named vendors and a summary row in [`vendor-register.csv`](vendor-register.csv) add up to the 34.
- **AI tools.** The chatbot, contact center and OSS vendors in accounts payable, plus the in-house churn model, give the 4 tools in [`asset-inventory.csv`](asset-inventory.csv). Public generative AI use comes from the survey only (EV-042, EV-055).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Load the about 140 POP devices from the acquisition spreadsheet into the OSS, with software versions | Director of Network Engineering | 2026-06-29 | Not done at intake; P07 counted POP-A devices (EV-CM-8) and POAM-008 carries it |
| How the 2025 CPNI certification statement was prepared and what evidence supported it | Vice President of Regulatory Affairs | 2026-06-23 | Answered in P03 fieldwork on 2026-07-08 (EV-058) |
| Current SOC 2 reports and bridge letters for the Tier 1 vendors | Security Manager | 2026-07-01 | Obtained for the P09 vendor review in 2026-08 and 2026-09 |
| Number of staff using public generative AI tools, and what they enter | vCISO with department heads | 2026-07-02 | Not established at intake; P01 R-040 and P10 treat it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Business units and owners (EV-003), revenue and volumes (EV-051, EV-052), BSS vendor recovery commitments (EV-044), backup design (EV-018), PSAP, outage and 911 records (EV-037, EV-038, EV-039), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-021 and EV-031, EV-035 |
| P04 Cloud mapping | Landing zone components (EV-017, EV-018) and provider assurance (EV-044, EV-045) |
| P01 Risk register | Likelihood inputs from the incident log (EV-024), scan and patch records (EV-012, EV-013), phishing results (EV-025), configuration exports, the regulatory records (EV-036 to EV-041) and the vendor register (EV-043) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements; sample populations (EV-031, EV-032, EV-036, EV-037, EV-038, EV-040, EV-046) |
| P06 Policies | The 2024 policies and standards (EV-022) and the 2024 incident response plan (EV-023) |
| P07 Control assessment | Populations to sample from: 142 terminations and 77 transfers (EV-003), 188 new BSS accounts (EV-006), 118 privileged accounts (EV-005), about 2,100 access elements and 268 cabinet switches (EV-009), 412 changes (EV-016), 41 incidents (EV-024), 50 critical findings (EV-012), 34 vendors with access (EV-043) |
| P08 IR runbooks | Notification duties from the obligations register; insurer terms (EV-048); PSAP contacts and NORS records (EV-037); vendor contacts from the vendor register |
| P09 SOC 2 | The customer requests (EV-047), the Business Services platform records (EV-054) and vendor assurance on file (EV-043 to EV-045) |
| P10 AI governance | AI tools found (EV-055) and their contracts (EV-043) |
