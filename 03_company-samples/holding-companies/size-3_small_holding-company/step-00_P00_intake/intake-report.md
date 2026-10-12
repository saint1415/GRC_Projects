# Intake Report: Cris Santos Company | Management of Companies and Enterprises | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries at three Florida sites) |
| Intake window | 2026-08-03 to 2026-08-14 |
| Collected by | IT Manager (Qualified Individual for Finance), with the CFO and the Controller |
| Approved | CEO, 2026-09-25 |

## 1. Purpose and scope
Intake collected the group's own records before any assessment work began on 2026-08-17. It covers the holding company and its three subsidiaries (Supply, Home Services, and Finance), the shared systems and the subsidiary systems that connect to them, the suppliers that touch them, and the rules that may bind the group. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement or a CSF 2.0 outcome is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-012 | Identity provider; HRIS; help desk tickets; ERP; bank portals; loan servicing and field-service systems | 2026-07-31 to 2026-08-05 |
| Devices and network | EV-013 to EV-019 | Device management; EDR console; MSP firewall consoles, documentation, remote tool and patch reports | 2024-10-31 to 2026-08-06 |
| Cloud and backups | EV-020 to EV-024 | Cloud provider console; backup service; SFTP server; deployment log; close files | 2026-07-31 to 2026-08-05 |
| Email, files and AI | EV-025 to EV-029 | Productivity suite and identity admin consoles; event record | 2026-08-05 to 2026-08-13 |
| Documents and governance | EV-030 to EV-042 | Document request list; Finance and group board records; HR files; training platform; IT files; CFO and CEO files | 2023-05-31 to 2026-08-06 |
| Suppliers and contracts | EV-043 to EV-050 | ERP payables and card statements; contracts folder; purchase approvals; vendor and provider portals | 2022-01-01 to 2026-08-07 |
| Facilities and disposal | EV-051, EV-052 | Badge system and key log; destruction certificates and wipe reports | 2026-06-30 to 2026-08-03 |
| Business, ownership and legal status | EV-053 to EV-058 | ERP consolidation; loan servicing reports; corporate records; Finance and CFO files; HR benefits files | 2025-12-31 to 2026-08-07 |

One item arrived after the window: Finance's notice letter and counsel's memo on the 2026-08-12 event (EV-059, intake follow-up).

## 3. Observations by area
**Users and access.** The identity provider holds named accounts for all 60 employees and for MSP technicians, each with push MFA (number matching) registered (EV-001). Policies require MFA for every single sign-on application, the cloud console and the VPN. No policy checks whether the device is managed (EV-002). Seven accounts hold the global administrator role with standing assignment, 2 of them MSP accounts, and there are no break-glass accounts (EV-003). Identity risk detections are emailed to the IT team, and most have no review note (EV-004). HR recorded 60 employees (holding company 14, Supply 22, Home Services 15, Finance 9), 13 terminations and 3 transfers between subsidiaries in the year to July 2026 (EV-005). Employees can change direct deposit details in the HRIS with no waiting period or out-of-band notice (EV-006). Disable tickets for subsidiary leavers were opened on average 3 business days after the last working day (EV-007). The ERP separates vendor master maintenance from payment release (EV-008). Vendor bank-detail changes are entered from emailed forms, with no callback record (EV-009). The bank enforces dual approval for wires and ACH batches and runs positive pay on all operating accounts. New wire payee setups carry no callback record (EV-010). Every Finance role in the loan servicing system can bulk-export (EV-011). The field-service system uses local accounts with no MFA, outside single sign-on (EV-012).

**Devices and network.** Device management lists 50 laptops, 10 desktops and 16 tablets. All 60 computers have full-disk encryption and automatic OS and browser updates. Tablets have a PIN, encryption and remote wipe (EV-013). EDR runs on all 60 computers. Alerts go to the IT team mailbox with no after-hours routing (EV-014). Firewalls protect all three sites, with a site-to-site VPN to the cloud tenant and a separate guest Wi-Fi. The Home Services firewall firmware is two major versions behind, and each site has one internet circuit (EV-015). The MSP's network device list was last updated 2024-10-31 (EV-016). The MSP's remote tool reaches every endpoint, accepts connections from any address, and does not log sessions (EV-017). The MSP patches cloud VMs monthly (EV-018). The MSP states that no vulnerability scanning or penetration testing has been run (EV-019).

**Cloud and backups.** The cloud tenant runs four workloads: the integration service, the reporting database, the SFTP server and the backup vault. Three named administrator roles also administer backups (EV-020). Daily backups completed from May to July 2026, kept 30 days in the production account and region, with immutability off and no restore jobs (EV-021). ACH collection files are kept on the SFTP server with no deletion job, and every IT administrator can read them (EV-022). Integration jobs and ACH scripts change with no review record (EV-023). The Controller reconciles subsidiary feeds to the ERP by hand each month (EV-024).

**Email, files and AI.** One productivity suite tenant serves four email domains and 41 collaboration sites. Anonymous sharing links are allowed, and mail and files have no backup beyond the provider's retention (EV-025). Identity and email audit logs are kept 30 days under the current license, with no central collection (EV-026). On 2026-08-13, 3 of the 41 sites granted access to all group employees: Finance's loan-documents archive (about 2,100 files with customer information), the group HR site and the group accounting site (EV-027). The event record shows a Supply pilot user was shown a Finance loan document by the AI assistant on 2026-08-12, and all-employee access to the archive was removed on 2026-08-13 (EV-028). Finance sent a notice letter to the one affected consumer on 2026-08-21 (EV-059). The AI assistant pilot has 25 licensed users since 2026-07-06, with plugins, connectors and agent features off (EV-029).

**Documents and governance.** Finance's 2023 WISP was the only written security policy returned. Requests for group policies, an incident response plan, a contingency plan, a retention schedule, an AI use policy and SOC 2 review records returned none (EV-030). The WISP and Finance's risk assessment are dated 2023 and have not been revised, and the incident section has no test record (EV-031). The IT Manager was designated Finance's Qualified Individual in writing in 2023 (EV-032). Finance's board minutes record a Qualified Individual report in 2024 and none in 2025 (EV-033). The holding company's board minutes and management agendas have no cybersecurity item (EV-034). Three IT staff support the group, and the subsidiary Presidents' role descriptions list no cybersecurity duties (EV-035). HR runs background checks at hire and emails IT on the last day (EV-036). The handbook has no security sanctions statement (EV-037). 57 of 60 employees completed the annual training module in 2026 (EV-038). Two of the three IT staff have vendor training certificates (EV-039). IT notes cover one 2025 phishing incident, and no subsidiary raised an incident ticket (EV-040). A group cyber policy with a breach hotline runs from 2026-04-01 (EV-041).

**Suppliers and contracts.** The ERP vendor list has no criticality ranking. Spend shows 16 SaaS applications, 5 of them not known to IT (EV-043). The MSP contract has no security requirements, SaaS contracts have no data return or deletion terms, and the former payroll provider still holds employee data (EV-044). The intercompany services agreement lists services and fees with no service levels or security requirements (EV-045). SaaS purchase approvals carry no security review (EV-046). SOC 2 Type 2 reports are on file from the ERP, HRIS and loan servicing vendors (EV-047 to EV-049), and the suite and cloud providers publish theirs (EV-050).

**Facilities and disposal.** The HQ network closet is on badge access, and the site cabinets are locked with logged keys (EV-051). Retired drives have destruction certificates or wipe reports (EV-052).

**Business, ownership and legal status.** Consolidated FY2025 receipts were $27.3 million across about 260 business days (EV-053). Finance has about 3,300 active loans and customer records on about 8,600 consumers (EV-054). The company is a manager-managed LLC with 5 members of record and no SEC registration (EV-055). Finance holds a state consumer lending license and is funded by a bank line of credit; no group company is a bank (EV-056). The fully insured health plan has about 52 participants, and the sponsor receives only enrollment and summary health information (EV-057). Cards are taken only through the processor's encrypted terminals and hosted page (EV-058).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Distribution system vendor's recovery commitments (RPO) in the contract | Supply President | 2026-08-07 | Not provided; carried into the BIA (P05) as an action for the Supply President |
| Use of AI tools outside the pilot | IT Manager | 2026-08-07 | Not established at intake; the risk interviews (EV-062) and P10 follow it up |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Headcount and processes (EV-005), receipts (EV-053), loan volumes (EV-054), backup schedule (EV-021), the ERP vendor's recovery objectives (EV-047), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-026 |
| P04 Cloud mapping | Cloud and SaaS components (EV-020 to EV-025, EV-043) and provider assurance (EV-047, EV-050) |
| P01 Risk register | Likelihood inputs from the configuration exports, the event record (EV-028), incident records (EV-040), scanning status (EV-019) and the document request (EV-030) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the CSF 2.0 group profile and the Safeguards Rule |
| P06 Policies | Finance's 2023 WISP (EV-031) and the handbook (EV-037) |
| P07 Control assessment | Populations to sample from (EV-001, EV-005, EV-007, EV-027) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurer's hotline (EV-041) |
| P09 SOC 2 | Vendor assurance on file (EV-047 to EV-050) |
| P10 AI governance | The AI pilot (EV-029), the 2026-08-12 event (EV-028) and purchase approvals (EV-046) |
