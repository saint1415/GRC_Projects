# Intake Report: Cris Santos Company | Construction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor, one Florida main office and 8 active jobsites) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager, with the Accounting Manager and Contracts Administrator |
| Approved | CFO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that process, store or transmit Federal Contract Information (FCI) and payment data, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-009 | Identity provider; payroll and HR system; MSP ticketing; project management platform, ERP and bank portal admin consoles; file server | 2026-06-30 to 2026-07-02 |
| Devices and network | EV-010 to EV-014 | MSP device management, antivirus and patch consoles; MSP network documentation; commissioning laptop review | 2026-06-26 to 2026-07-08 |
| Cloud, backups and email | EV-015 to EV-017 | Cloud provider console; backup service; productivity suite admin console and public DNS | 2026-06-30 to 2026-07-02 |
| Documents and records | EV-018 to EV-024 | Document request list; SAM.gov and SPRS; HR files; MSP tickets; accounts payable walk-through; disposal spreadsheet | 2026-06-30 to 2026-07-07 |
| Facilities | EV-025 to EV-027 | Badge system; reception log book; VP Operations request response | 2026-07-01 to 2026-07-06 |
| Suppliers and contracts | EV-028 to EV-033 | ERP accounts payable; contracts folders; vendor portals; cyber policy | 2024-01-01 to 2026-07-06 |
| Business volume and other systems | EV-034 to EV-036 | ERP financial and billing reports; telematics portal; website content management system | 2025-12-31 to 2026-07-02 |
| AI tools and Section 889 sources | EV-037 to EV-039 | Staff survey, identity provider app list and AI vendor console; purchase records; submittal procedure and logs | 2026-06-30 to 2026-07-08 |

## 3. Observations by area
**Users and access.** Office and salaried field staff have named identity provider accounts with single sign-on to the project management platform, ERP, payroll system and productivity suite, and push-notification MFA. Six shared jobsite trailer accounts exist, and conditional access excludes them from MFA. The three administrators use security keys, and no sign-in risk policy or log review schedule is configured (EV-001, EV-002). HR lists 60 employees and the terminations from January to June 2026 (EV-003). Disable requests reach the MSP by email from HR, and field-staff disable tickets closed up to 10 business days after the last working day (EV-004). The project management platform has about 400 external users, each limited to assigned projects, and 212 external accounts whose projects are closed out. No scheduled export of project records exists (EV-005). One AP clerk holds vendor create, bank detail edit and ACH payment-file rights in the ERP (EV-006). In the bank portal, wires over $50,000 need two approvers, ACH batches need one, and checks use positive pay (EV-007). Employees can change their direct deposit in payroll self-service without a change notice (EV-008). The Client Systems and Estimating folders are readable by all staff (EV-009).

**Devices and network.** Device management lists 44 laptops and 12 desktops, all with full-disk encryption and a 10-minute screen lock, and 48 managed smartphones. The 20 rugged jobsite tablets and the 2 shared commissioning laptops are not enrolled, and the inventory has no manufacturer or FCI field (EV-010). Managed antivirus runs with automatic updates, real-time scanning and weekly full scans, and its alerts go to the MSP's shared inbox (EV-011). Operating system patches are 98% current on laptops and desktops, and cloud VMs are patched monthly (EV-012). The main office firewall publishes no inbound services. Its firmware is 14 months old, its logs have no review schedule, and the MSP remote management tool accepts connections from any source address. There is one internet circuit at the main office (EV-013). The commissioning laptops share one local login and have disk encryption off (EV-014).

**Cloud, backups and email.** The cloud tenant runs 4 workloads. The internet-facing file-transfer portal sits in the same subnet as the BIM/CAD file server, and backup administration uses the same roles as production (EV-015). Daily backups completed from April to June 2026. The vault is in the production account and region, immutability is off, and no restore was run (EV-016). Email has spam filtering and an external-sender banner. Automatic forwarding to external addresses is allowed, no alert exists for new inbox or forwarding rules, and DMARC is at p=none (EV-017).

**Documents and records.** The request for a security policy set, an SSP, an FCI scope, an asset inventory, a CMMC self-assessment, an incident response plan, a contingency plan and sanitization records returned none (EV-018). SAM representations were renewed in March 2026 with no inquiry record, and SPRS holds no assessment entry for the company (EV-019). Security awareness is a 15-minute segment of the annual safety meeting, with slides dated 2023 (EV-020). The HR checklist relies on an email to IT on the last day (EV-021). Security tickets carry no incident numbers or post-incident notes, and none exists for the March 2026 bank-change email (EV-022). About 120 subcontractors and suppliers are paid by ACH. Their bank-account changes arrive by email and one AP clerk enters them with no call-back, and the Accounting Manager states the March 2026 request was caught only by chance (EV-023). Nine retired laptops have no wipe record (EV-024).

**Facilities.** The main office uses badge access with 90-day logs and a reception visitor log (EV-025, EV-026). No trailer visitor log or key inventory was provided, and the yard gate combination was last changed in 2023 (EV-027).

**Suppliers and contracts.** Accounts payable shows the technology suppliers, including an AI estimating subscription with 4 seats from May 2026 (EV-028). The MSP agreement excludes 24x7 monitoring, log review and vulnerability scanning. The AI vendor's standard terms allow customer data to be used to improve its models (EV-029). SOC 2 reports are on file for the project management platform (12 months ending 2026-04-30), identity provider, payroll vendor and cloud provider (EV-030). FC-1, FC-2 and FC-3 all include FAR 52.204-21 and 52.204-25, FC-3 also includes DFARS 252.204-7012, and none includes DFARS 252.204-7021 (EV-031). The subcontract template incorporates FAR clauses by reference only (EV-032). The cyber policy has a $250,000 social engineering sublimit (EV-033).

**Business volume and other systems.** FY2025 revenue was $27.0 million, about 38% federal, with about $2.25 million billed a month (EV-034). Telematics tracks 35 pieces of equipment under one shared login (EV-035). The office manager is the only website publisher, with no approval workflow (EV-036).

**AI tools and Section 889 sources.** Four estimators use the AI bid assistant and have uploaded federal bid documents and FC-2 change-order drawings. Staff report using public chatbots. No approved-tools list exists in the documents provided (EV-037). Private-label products are invoiced under the distributor's brand (EV-038), and the submittal checklist has no manufacturer or Section 889 step (EV-039).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | CFO | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| MSP's own security assurance (SOC 2 or questionnaire) | MSP service manager | 2026-07-06 | Not provided; carried into the P01 risk register (R-028) and the P07 POA&M (POAM-019) |
| Trailer key inventory and trailer visitor logs | VP Operations | 2026-07-06 | None provided (EV-027) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue and billing volume (EV-034), payment volume (EV-023), backup schedule (EV-016), vendor recovery commitments (EV-030), and dependencies from the asset and vendor registers |
| P02 SSP | The FCI boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-005 to EV-017 |
| P04 Cloud mapping | Cloud and SaaS components (EV-015, EV-028) and provider assurance (EV-030) |
| P01 Risk register | Likelihood inputs from the accounts payable walk-through (EV-023), the ticket history (EV-022), configuration exports, the contract files and the AI tool review |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with FAR 52.204-21, FAR 52.204-25 and the CMMC program duties |
| P06 Policies | The document request response (EV-018) and the handbook (EV-021) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-005, EV-010, EV-039) |
| P08 IR runbook | Notification duties from the obligations register; insurer and vendor contacts from the vendor register (EV-033) |
| P09 SOC 2 | Vendor assurance on file (EV-030) |
| P10 AI governance | AI tools found (EV-028, EV-037) |
