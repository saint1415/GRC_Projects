# Intake Report: Cris Santos Company | Professional, Scientific, and Technical Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm, two Florida offices) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Qualified Individual), with the Firm Administrator |
| Approved | Firm Administrator, 2026-08-31 |

## 1. Purpose and scope
Intake collected the firm's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that store, process or transmit customer information and tax return information, the suppliers that touch them, and the rules that may bind the firm. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, scans, samples, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-010 | Identity provider; payroll and HR SaaS; IT ticketing; HR files; tax software and portal admin consoles | 2025-11-01 to 2026-07-02 |
| Email and logging | EV-011, EV-012 | Productivity suite admin console; audit settings in each system | 2026-07-02 |
| Devices and network | EV-013 to EV-018 | Device management and EDR consoles; MSP remote management and network documentation; MSP scanning tool | 2025-03-14 to 2026-07-03 |
| Cloud and backups | EV-019 to EV-021 | Cloud provider console; backup service; IT Manager's files | 2025-09-18 to 2026-07-01 |
| Documents and records | EV-022 to EV-029 | Shared drive and document request; Managing Partner's files; HR and learning records; MSP and IT tickets; DMS | 2024-01-01 to 2026-07-06 |
| Suppliers and contracts | EV-030 to EV-036 | Accounts payable records; contracts folder; vendor portals; insurance file | 2026-01-01 to 2026-07-06 |
| Clients and tax program | EV-037 to EV-041 | Risk and Quality Partner's files; IRS e-Services and PTIN records; Client Services files; tax software client list; practice management | 2025-12-31 to 2026-07-06 |
| Facilities and disposal | EV-042 to EV-044 | Walk-through; badge system; shredding certificates and printer-scanner lease | 2026-06-30 to 2026-07-09 |
| AI tools | EV-045 | Identity provider app list; productivity suite license report; tax software settings | 2026-07-07 |

## 3. Observations by area
**Users and access.** The identity provider holds 60 active named workforce accounts, each with push MFA and number matching off, plus 4 shared service mailbox accounts, including the shared intake mailbox. The 2026 seasonal preparer accounts are disabled (EV-001). Push MFA is required for staff on every federated system and for every administrator role. Legacy authentication is allowed for the 4 shared service mailboxes, and sign-ins are limited to the United States (EV-002). Three partners hold the global administrator role on their everyday productivity suite accounts (EV-003). Legacy-protocol sign-ins appear on the 4 shared service mailboxes (EV-004). HR lists 60 employees and 6 seasonal preparers from January to April 2026 (EV-005). Disable tickets for the seasonal preparers closed an average of 6 business days after their season end dates (EV-006). The HR checklist has HR email IT on the last day, with no step to confirm that access was removed (EV-007). Confidentiality agreements do not mention IRC 7216 or 6713, and the 2026 seasonal preparers signed on their first day (EV-008). The tax software has 4 roles, a PTIN on every preparer account, and the AI extraction feature turned on for 8 preparers since June 2026 (EV-009). Client portal MFA is optional, and about 38% of individual clients use it (EV-010).

**Email and logging.** Automatic forwarding to external addresses is allowed, no alert fires on new inbox rules, and no rule encrypts outbound attachments (EV-011). Every system generates audit events, but they stay in each system, and no alert rules are set, including none for bulk exports (EV-012).

**Devices and network.** Device management lists 62 laptops and 12 desktops. Full-disk encryption is reported on all 62 laptops and none of the 12 desktops. Screen lock excludes 4 seasonal stations at the Branch office. The 4 printer-scanners are not listed (EV-013). The EDR agent runs on all 74 computers and the cloud VMs, with alerts in the MSP's business-hours queue (EV-014). Firewall and VPN gateway firmware is updated on no set schedule (EV-015). The MSP remote management tool reaches every endpoint with no source restriction (EV-016). Both offices have firewalls with no inbound services. Staff and guest Wi-Fi are separate, and the Branch office has a single ISP (EV-017). The last vulnerability scan is dated 2025-03-14, and no penetration test report was provided (EV-018).

**Cloud and backups.** The cloud tenant holds the DMS, the workpaper server, the VPN gateway and the backup vault, with 2 named IT administrators and a separate backup administrator role (EV-019). Daily backups completed from April to June 2026 to an immutable vault in a second region (EV-020). One DMS restore test was run in 2025, and no workpaper server restore is recorded (EV-021).

**Documents and records.** The written information security program is a 2023 adaptation of the IRS Pub. 5708 template with no later revision. The request for a written risk assessment, an incident response plan, a data theft procedure, a contingency plan, a change management procedure, a retention and disposal schedule, a service provider inventory, call-back verification procedures, configuration baselines, access review and log review records, and a penetration test report returned none (EV-022). The IT Manager was designated Qualified Individual on 2026-06-15 (EV-023). The Partner Group minutes for 2024 to 2026 contain no written security report (EV-024). Training is an annual December course, completed by all staff in December 2025. The 2026 seasonal preparers completed it after their start dates, and there are no phishing exercise records (EV-026). Phishing reports and malware alerts were handled by the IT Manager and the MSP with no incident numbers. Some changes were logged in tickets with no approval step (EV-028). The tax staff group can open every tax client folder in the DMS, and client folders go back to 2009 (EV-029).

**Suppliers and contracts.** Payments went to 14 suppliers, including an enterprise AI assistant add-on for 15 users from May 2026 (EV-030). The tax software, portal and cloud contracts include security terms. The tax software terms allow use of de-identified data and name no AI sub-processor, and there is no list of service providers (EV-031). The MSP agreement has no security requirements and no IRC 7216 notice (EV-032). The tax software vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-033). The cyber insurance policy includes a breach hotline and panel vendors (EV-036).

**Clients and tax program.** The engagement acceptance procedure declines work that requires PHI. There are no federal contracts and no public company audit clients (EV-037). Every preparer has a PTIN, the firm has one EFIN, and the Tax Partner is the Responsible Official (EV-038). The weekly PTIN check has no line for EFIN totals (EV-039). The firm prepared about 4,600 individual returns (about 7,400 consumers) and holds records on about 21,000 consumers. About 9% of individual clients live outside Florida for part or all of the year (EV-040). Receipts were $15.9 million in FY2025, about 55% of them billed from February to April (EV-041).

**Facilities and disposal.** Both offices use badge entry, and the Main office server and network closet has 3 key holders (EV-042, EV-043). Paper destruction certificates are on file. The printer-scanner lease has no drive wipe step, and the devices keep scanned images on an internal drive (EV-044).

**AI tools.** Two AI pilots were found: the tax software's extraction feature (8 preparers) and the productivity suite assistant (15 users). No list of approved AI tools was found (EV-045).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Name, location and security assurance of the AI sub-processor behind the tax software's extraction feature | Tax software vendor | 2026-07-07 | Not provided at intake; carried into P09 Part B and P10 |
| Staff use of public generative AI chatbots, and what was entered | Risk and Quality Partner | 2026-07-08 | Not established at intake. The gap analysis staff interviews found 3 cases (EV-049); P10 treats the wider count as unknown |
| MSP's own security assurance (SOC 2 report or questionnaire) | MSP account lead | 2026-07-03 | Not provided; carried into the P01 risk register (R-018) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners, receipts by day and season (EV-041), seasonal staffing (EV-005), backup schedule (EV-020), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-021 |
| P04 Cloud mapping | Cloud and SaaS components (EV-019, EV-030) and provider assurance (EV-033, EV-034, EV-035) |
| P01 Risk register | Likelihood inputs from the configuration exports, the ticket history (EV-028), the scan record (EV-018) and the document request response (EV-022) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the Safeguards Rule and IRC 7216 |
| P06 Policies | The 2023 WISP (EV-022), the handbook (EV-025) and the confidentiality agreement (EV-008) |
| P07 Control assessment | Populations to sample from (EV-001, EV-005, EV-006, EV-013) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber insurance policy (EV-036) |
| P09 SOC 2 | Vendor assurance on file (EV-033, EV-034) |
| P10 AI governance | AI tools found (EV-009, EV-030, EV-045) |
