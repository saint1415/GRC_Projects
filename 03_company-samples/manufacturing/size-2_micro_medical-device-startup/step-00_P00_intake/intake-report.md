# Intake Report: Cris Santos Company | Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup, one Florida office suite with a small engineering lab) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Operations Manager (Information Security Coordinator), with the Cloud Software Engineer for the repository and cloud exports and the MSP lead technician for the MSP exports |
| Approved | CEO, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that design, build, sign, test and distribute WM-1 software, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

A 7-person startup has no HR system, CMDB or accounts payable vendor master. Its systems of record are the SaaS admin consoles (productivity suite, repository, eQMS, cloud console), the payroll service, the MSP's exports and monthly report, the contracts folder, the card statements, the design history file in the eQMS, and what can be seen in the office and lab.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People and access | EV-001 to EV-005 | Payroll service; contracts folder; suite, repository and cloud admin consoles | 2026-06-30 to 2026-07-09 |
| Cloud and quality system | EV-006, EV-007 | Cloud console; eQMS admin console | 2026-07-07 to 2026-07-08 |
| Devices and network | EV-008 to EV-010 | MSP device, EDR and encryption exports; MSP monthly report; firewall documentation | 2026-06-30 to 2026-07-08 |
| Suppliers and contracts | EV-011 to EV-014 | Contracts folder; vendor websites and portals; eQMS supplier and pilot build records; suite sharing settings | 2026-06-15 to 2026-07-10 |
| Product design and engineering records | EV-015 to EV-021 | eQMS design history file; repository; engineering shared folder; email | 2026-07-08 to 2026-07-10 |
| Regulatory and program documents | EV-022 to EV-027 | eQMS regulatory file; document request list; training records; mailbox; contracts folder | 2026-04-15 to 2026-07-10 |
| Partner hospital and business volume | EV-028 to EV-031 | Contracts folder; email inbox; accounting SaaS; card statements | 2026-06-30 to 2026-07-09 |
| Office, people and AI | EV-032 to EV-036 | Walk-through; key list and lease; intake interview; staff survey; dataset license | 2026-07-10 to 2026-07-15 |

## 3. Observations by area
**People and access.** Payroll lists 7 active employees and 1 employee departure in 2025 (EV-001). The contract firmware developer's agreement has no security terms, named sponsor or account end date, and the engagement ended on 2026-03-13 (EV-002). The productivity suite has 7 named accounts with MFA enforced, single sign-on to the eQMS only, and shared folder links that open without sign-in and have no expiry by default (EV-003). The repository requires MFA for all members, every engineer has write access to every repository including the release scripts, main-branch changes need one approving review, and dependency alerts are on for the cloud code repositories only (EV-004). In the cloud tenant, the two engineers' named accounts hold the owner role, and a shared owner account has its MFA device on the CEO's phone and a password last changed in 2025 (EV-005). The shared owner password is known to the CEO and the Cloud Software Engineer, and repository and cloud accounts are added on request in chat (EV-034).

**Cloud and quality system.** One cloud tenant holds development and pre-production, with simulator and test data only. Activity logs are kept for the 90-day default. Database snapshots run daily, are kept 7 days in the same region, and have never been restored. Encryption at rest is on, no keys exist in the HSM-backed key tier, and resources are created in the console (EV-006). The eQMS holds the QMS manual and the procedures adopted in 2025 for design controls, risk management, document control and supplier control, with draft complaint and MDR procedures. No procedure mentions cybersecurity, and the company holds no export of its eQMS records (EV-007).

**Devices and network.** The MSP device list shows 7 laptops with full-disk encryption and EDR, and no lab workstations, network devices, units or cloud resources (EV-008). The MSP patches the laptops monthly and its report covers the laptops, the suite and the office network only (EV-009). The firewall exposes no inbound services and guest Wi-Fi is separate. Staff Wi-Fi, the laptops and the lab bench network share one subnet, and there is one internet line (EV-010).

**Suppliers and contracts.** The MSP contract has a 4-business-hour response time, no recovery time commitment, and does not cover the lab workstations, the repository or the cloud tenant (EV-011). The eQMS contract states daily platform backups. No SOC 2 report is on file for the repository, eQMS or suite vendors (EV-012). The contract manufacturer quality agreement has no terms on firmware handling, provisioning secrets, test station security or security incident notice, and the approved supplier list does not include the software suppliers (EV-013). For the May 2026 pilot build of 30 sets, firmware images and the provisioning file, which contains the hub API key, went to the contract manufacturer through a shared folder link with no expiry. 22 sets are in the lab and 8 have been at the simulation center since 2026-06-15 (EV-014).

**Product design and engineering records.** The hub verifies a signature at boot and before installing an update, and the sensor bootloader verifies sensor images. The hub logs functional events only (EV-015). Every hub has the same maintenance password, the maintenance page is on by default and can change alarm limit defaults, hubs share one API key per environment, and sensor-to-hub pairing uses the "Just Works" method (EV-016). Design inputs hold no security requirements (EV-017). The only threat model is a spreadsheet for the radio link, and the safety risk file lists no security causes (EV-018). The component spreadsheet has no versions or support dates, and there is no SBOM (EV-019). Verification covers functional and performance requirements, with no static analysis, fuzzing or penetration test records (EV-020). A test lab quoted about $28,000 for a penetration test with one retest, planned for 2026-12 (EV-021). Images are signed on the Head of Engineering's laptop, with a USB copy of the key in the office safe, one signer, no HSM and no second approval (EV-034).

**Regulatory and program documents.** The regulatory consultant's strategy memo records WM-1 as a cyber device and sets a 2027-03-31 submission target (EV-022). The guidance checklist is about 20% complete (EV-023). The document request returned a two-page MSP "IT rules" sheet and no security policies, incident response plan, cybersecurity management plan, CVD policy, contingency plan or asset inventory (EV-024). Training records show the MSP onboarding video only (EV-025). Offboarding is an email to the MSP about the suite account (EV-026). A cyber liability policy with a 24x7 hotline and panel vendors was bought in April 2026 (EV-027).

**Partner hospital and business volume.** The development and evaluation agreement places 8 units on the simulation center's isolated, monitored test network, with test data only and 72-hour incident notice (EV-028). The hospital's vendor security questionnaire is due 2026-10-30 (EV-029). FY2025 receipts were about $1.1 million, monthly operating cost is about $190,000 (about $8,600 per business day), and cash runway is about 14 months (EV-030). The card statements show the SaaS, cloud, MSP, payroll, insurance, consultant and contract manufacturer payments, no AI tool charges and no ISAO fee (EV-031).

**Office, people and AI.** The walk-through counted 7 laptops and 2 lab workstations. The lab workstations use one shared local login, show no EDR agent, have disk encryption off, and hold test data and copies of the provisioning file (EV-032). Suite keys are held by the CEO and the Operations Manager (EV-033). Engineers report pasting code snippets into public chatbots through personal accounts (EV-035). The AI-001 dataset license covers video of 120 adult volunteers, and no counsel review of its terms is on file (EV-036).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Cloud provider SOC 2 Type 2 report (under NDA) | Cloud provider account team | 2026-07-10 | Received 2026-08-18 (EV-041); reviewed in P09 |
| How often engineers paste code into public chatbots, and what they paste | Head of Engineering (staff survey follow-up) | 2026-07-16 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Functions and owners (EV-001, EV-034), operating cost and runway (EV-030), snapshot settings (EV-006), vendor terms (EV-011, EV-012), the evaluation agreement (EV-028), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-003 to EV-020 and EV-032 |
| P04 Cloud mapping | SaaS and cloud components (EV-003 to EV-007, EV-031) and provider documentation (EV-012) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the design records, the contracts folder, the walk-through (EV-032) and the release process interview (EV-034) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The MSP IT rules sheet and the document request response (EV-024) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-003, EV-004, EV-005, EV-008, EV-014) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the insurance policy (EV-027) and evaluation agreement (EV-028) |
| P09 SOC 2 | The partner hospital questionnaire (EV-029) and vendor assurance (EV-012, EV-041) |
| P10 AI governance | AI tools and data found (EV-004, EV-016, EV-031, EV-035, EV-036) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) plans one by 2026-10-31.
