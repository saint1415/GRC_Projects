# Intake Report: Cris Santos Company | Information Technology | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider, 7 employees, one Florida office and two racks at the DC-1 colocation facility) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Lead Systems Engineer (Information Security Lead), with the Operations Manager (Compliance Coordinator) for payroll, HR, contracts and billing records |
| Approved | Owner, 2026-09-15 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that hold or reach customer data (the hosting platform at DC-1, the cloud tenant, and the SaaS tools that run the business), the suppliers behind them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person hosting provider has no HR system, CMDB or accounts payable vendor master. Its systems of record are the admin consoles of the tools it runs (identity provider, RMM tool, hypervisor manager, firewalls, storage array, backup software, cloud tenant, PSA, DNS account, password vault, MDR console), the payroll service, the portal's billing module and the card statements, the contracts folder, the Lead Systems Engineer's hardware spreadsheet, the ticket history, and the inboxes of the Owner and the Operations Manager.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005 | Payroll service; identity provider; firewall VPN; RMM vendor portal; hypervisor manager | 2026-06-30 to 2026-07-08 |
| Hosting platform and backups | EV-006 to EV-010, EV-019 | Hypervisor manager and BMCs; hardware spreadsheet; storage array; backup console; cloud provider console; firewall management | 2026-06-30 to 2026-07-09 |
| Portal, PSA, vault and DNS | EV-011 to EV-014 | Portal admin console; PSA admin console; password manager; DNS provider console | 2026-07-09 to 2026-07-10 |
| Monitoring and tickets | EV-015 to EV-018 | MDR console and contract; PSA ticket history | 2025-11-01 to 2026-07-08 |
| Business volume and customers | EV-020, EV-021 | Portal billing module; bank statements; customer records | 2026-06-30 to 2026-07-07 |
| Contracts and insurance | EV-022 to EV-028 | Contracts folder; bank contact file; colocation correspondence | 2024-06-30 to 2026-07-07 |
| Documents and records | EV-029 to EV-034 | Shared files and document request; Owner's files; HR files; training portal; team chat; Owner's inbox | 2025-12-31 to 2026-07-10 |
| Suppliers, vendor documentation, capacity, AI and customer requests | EV-035 to EV-039 | Card statements and invoices; vendor websites and portals; capacity worksheet; staff survey; Operations Manager's inbox | 2026-06-30 to 2026-07-14 |

## 3. Observations by area
**People and access.** Payroll lists 7 people and 1 termination from January to June 2026, a Support Engineer whose last working day was 2026-03-13 (EV-001). The identity provider has 7 named accounts with push-approval MFA and number matching off. It signs staff in to the suite, PSA ticketing, the MDR console and the VPN, but not to the RMM tool, the hypervisor manager or the cloud tenant. The Owner's everyday account holds the global administrator role (EV-002). The VPN is the only path to the management network, requires identity provider MFA, and has 8 enabled user accounts (EV-003). The RMM tool reaches about 310 servers of 22 customers, including 8 Bank A and 9 Bank B servers. It has 3 named technician accounts, one of them the Owner's administrator account, and 2 shared support accounts whose one-time codes come from a seed in the team vault. Any technician account can act on all 22 customers, the script approval workflow is off, sign-in is allowed from any address, and audit logs are kept 30 days (EV-004). The hypervisor manager has one shared administrator account with lockout off, and the portal's service account holds its full administrator role. The 6 BMCs share one password, and device logs roll over in about 7 days (EV-005).

**Hosting platform and backups.** The hosts run two minor releases behind the vendor's current release, and BMC firmware has not changed since the 2022 purchase (EV-006). The hardware spreadsheet lists the DC-1 equipment and nothing else: no SaaS, cloud resources or laptops, and no record of where bank customer information sits (EV-007). Array volumes, including Bank A's 6 VMs, are not encrypted at rest (EV-008). Nightly backups cover the 145 add-on VMs, kept 14 days on the appliance and 30 days in the cloud copy, with nightly configuration and portal database backups. The repository is not encrypted, and no job is recorded as a restore test (EV-009). The cloud tenant is one account in one region holding the portal and the backup copy. Object lock and versioning are off, the Owner's user holds full administrator rights, console sign-in is open to any address, and the audit trail keeps the provider default of 90 days (EV-010). Tenants are on separate VLANs. The BMCs and the backup appliance sit on the management VLAN that every VPN user reaches, and firewall firmware is updated quarterly (EV-019).

**Portal, PSA, vault and DNS.** About 180 customer users include 72 customer administrators, 15 of whom use the optional MFA. Lockout and rate limiting are off, and portal updates follow vendor releases by about 30 days (EV-011). The PSA vault holds customer server passwords, including both banks', readable by all 7 staff. The vendor's AI ticket-summary feature is off (EV-012). The team vault's shared folder holds the shared RMM credentials and seed, the DNS MFA seed, and the hypervisor and BMC passwords. The BMC entry was last changed in 2022 and the shared RMM entry not after 2026-03-13 (EV-013). The DNS account holds about 190 zones under one administrator login with MFA, with no zone export and no log retention (EV-014).

**Monitoring and tickets.** The MDR covers 9 laptops (EDR, full-disk encryption reported on), the identity provider and the firewalls. It receives nothing from the hypervisor manager, BMCs, RMM tool, cloud tenant or DNS account. Its auto-close and automatic containment settings were set by the provider at onboarding in November 2025 (EV-015). The contract provides 24x7 monitoring, 12-month retention, and use of de-identified telemetry to improve the provider's models (EV-016). The June report records the automatic suspension of the on-call engineer's account on 2026-06-27 (EV-017). The ticket history shows a compromised customer VM in 2025 and a staff phishing click in 2026, both closed with no incident record. It also shows about 2 customer restores a month with no record of what was restored, 3 failed array drives returned under warranty, a 2025 host failure absorbed by the cluster, the 2026-06-27 lockout of about 50 minutes, and 3 abuse reports in 2026 (EV-018).

**Business volume and customers.** Revenue over the 12 months to June 2026 was about $1.1 million: about $3,000 a day and $92,000 a month. Cash on hand covers about 45 days of expenses (EV-020). There are about 70 business customers, including 2 community banks, about 260 VMs (about 145 on the backup add-on), 22 managed services customers with about 310 servers, about 190 DNS zones, and no federal agency customer (EV-021).

**Contracts and insurance.** Both bank contracts state that the services are subject to the Bank Service Company Act. They flow down the Interagency Guidelines and require notice within 24 hours of unauthorized access to customer information (EV-022). The bank contact file names a Bank A contact who left the bank in 2024 and has no Bank B entry (EV-023). The MSA sets 99.9% availability with credits and a 72-hour incident notice. It makes customers responsible for their own backups and guest patching unless they buy the add-ons, and it prohibits PHI, CUI and card data (EV-024). The RMM terms have no security or incident notice clause, and the folder has no vendor review records (EV-025). The newest colocation SOC 2 report in the folder covers the 12 months ending 2024-06-30 and was read in 2024 (EV-026). The last change request for the colocation authorized-person list is from 2024 (EV-027). A cyber policy with a breach hotline and panel vendors is in force (EV-028).

**Documents and records.** The only security document is a 2023 overview written for customer questionnaires. The request for policies, a risk assessment, response, recovery and notice plans, a termination checklist, change records, vendor reviews, scan reports, log reviews and restore tests returned none (EV-029). The Lead Systems Engineer was designated Information Security Lead in writing on 2026-06-15 (EV-030). The termination record for the former Support Engineer lists the laptop, badge, mailbox and tickets, and no steps for the VPN, RMM tool, colocation list or shared secrets (EV-031). All 7 staff completed the annual awareness module in 2025, with no phishing simulations (EV-032). Changes are announced in team chat with no approval or rollback steps (EV-033). The Owner declined a federal hosting inquiry in April 2026 (EV-034).

**Suppliers, vendor documentation, capacity, AI and customer requests.** Card statements show 16 recurring suppliers and no AI tool charges (EV-035). Vendor documentation describes encryption at rest for the PSA vault, TLS for RMM agent traffic, and the cloud provider's shared responsibility model (EV-036). Cluster capacity is checked monthly against one host down (EV-037). Staff report using public chatbots to draft emails and scripts (EV-038). Both banks' 2026 due diligence questionnaires are due 2026-10-30, and two prospects asked for a SOC 2 report (EV-039).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Current colocation SOC 2 report (the folder holds the 2024 copy) | Colocation provider account manager | 2026-07-08 | Received 2026-08-24 (EV-050, intake follow-up); reviewed in P09 on 2026-08-26 |
| Current colocation authorized-person list | Colocation provider account manager | 2026-07-08 | Not received at intake; obtained at the facility desk during P07 on 2026-08-18 (EV-AC-2) |
| Which staff use public chatbots, and what they enter | Operations Manager (staff survey follow-up) | 2026-07-15 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001), revenue and cash (EV-020), customer and VM counts (EV-021), MSA and bank terms (EV-022, EV-024), backup schedule (EV-009), DNS and MDR dependencies (EV-014, EV-016), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-015 and EV-019 |
| P04 Cloud mapping | Cloud and SaaS components (EV-002, EV-004, EV-010 to EV-015) and provider documentation (EV-025, EV-026, EV-036) |
| P01 Risk register | Likelihood inputs from the console exports, the ticket history (EV-018), the contracts folder and the document request (EV-029) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the bank contract measures and Fla. Stat. 501.171 |
| P06 Policies | The 2023 security overview and the document request (EV-029) and the designation letter (EV-030) |
| P07 Control assessment | Populations to test from (EV-001 to EV-005, EV-012, EV-031) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the bank contact file (EV-023) and the cyber policy (EV-028) |
| P09 SOC 2 | Vendor assurance on file (EV-026, EV-036, then EV-050) and the bank questionnaires (EV-039) |
| P10 AI governance | AI tools found (EV-012, EV-015, EV-016, EV-035, EV-038) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
