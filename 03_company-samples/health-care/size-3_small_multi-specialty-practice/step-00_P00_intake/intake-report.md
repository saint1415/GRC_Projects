# Intake Report: Cris Santos Company | Health Care and Social Assistance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice, two Florida clinics) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Security Officer), with the Privacy Officer |
| Approved | Practice Administrator, 2026-08-31 |

## 1. Purpose and scope
Intake collected the practice's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that create, receive, maintain or transmit ePHI, the suppliers that touch them, and the rules that may bind the practice. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-005 | Identity provider; HR and payroll system; MSP ticketing; EHR admin console | 2026-06-30 to 2026-07-02 |
| Devices and network | EV-006 to EV-009 | MSP endpoint console; antivirus console; MSP network documentation; device walk-through | 2026-06-26 to 2026-07-08 |
| Cloud and backups | EV-010, EV-011 | Cloud provider console; backup service | 2026-06-30 to 2026-07-01 |
| Documents and records | EV-012 to EV-019 | Shared drive; HR files; learning records; MSP tickets and email; EHR reports | 2021-03-15 to 2026-07-06 |
| Suppliers and contracts | EV-020 to EV-024 | Accounting system; contracts folder; vendor portals | 2026-03-31 to 2026-07-06 |
| Facilities and disposal | EV-025 to EV-027 | Walk-through; badge system; vendor certificates and MSP tickets | 2026-06-30 to 2026-07-09 |
| Business volume | EV-028, EV-029 | Accounting system; EHR/PM reporting | 2025-12-31 to 2026-06-30 |
| Email and AI tools | EV-030, EV-031 | Productivity suite admin console; staff survey and identity provider app list | 2026-07-02 to 2026-07-08 |

## 3. Observations by area
**Users and access.** 60 active named workforce accounts, each with MFA registered; 41 disabled accounts are retained (EV-001). MFA is required for email, the EHR and the cloud console (EV-002). HR recorded 7 terminations from January to June 2026 (EV-003). Termination requests reach the MSP by email from HR, and each disable ticket has its own open and close date (EV-004). Four billing users hold the EHR report-writer role (EV-005).

**Devices and network.** The endpoint console lists 58 desktops, 12 laptops and 12 tablets. Patching is automatic and signature antivirus runs on all 70 computers. Disk encryption is reported on the 12 laptops and not on the 58 desktops. No endpoint detection and response agent is installed (EV-006). Antivirus alerts go to a shared mailbox (EV-007). Each clinic has one flat network holding workstations, medical devices and servers. The firewall firmware is 3 releases behind the vendor's current release, and Clinic B has a single ISP (EV-008). The X-ray modality workstation signs in with a shared local account and runs an operating system past its vendor's support end date. ECG carts and vital-sign monitors connect to the clinic network (EV-009).

**Cloud and backups.** The cloud tenant holds the imaging archive, the interface engine (a single VM) and the backup vault, which sits in the same region and account as production. Three administrator accounts have standing access (EV-010). Daily backups completed from April to June 2026. Vault immutability is off, and no restore jobs were run (EV-011).

**Documents and records.** The policy set is a 2019 template with no approval signature or review history. The request for an incident response plan, a contingency plan, downtime procedures and a records retention schedule returned none (EV-012). The last risk analysis is dated 2021-03-15 (EV-013). A Security Officer was designated on 2026-07-01 (EV-014). The 2024 handbook has a general discipline section and nothing on privacy or security violations (EV-015). Training records show the new-hire HIPAA module only, with content dated 2019 (EV-016). Fourteen security-related tickets in 12 months were handled by whoever was on call, with no incident numbers or post-incident notes (EV-017). The MSP states that no vulnerability scans are run (EV-018). EHR audit logging is on, but the access report has no runs in 2025 or 2026 (EV-019).

**Suppliers and contracts.** Payments go to 11 suppliers, including an AI scribe subscription with 3 seats from June 2026 (EV-020). BAAs are signed with the EHR vendor, clearinghouse, MSP and reference lab. None was located for the cloud fax or telehealth vendor, and the AI scribe BAA is a draft in legal review (EV-021). The EHR vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-022). The clearinghouse agreement covers standard electronic transactions (EV-024).

**Facilities and disposal.** Clinic A doors use badge readers. Clinic B uses keyed locks, the network closet key is held by several staff, and no key log was presented (EV-025, EV-026). Paper destruction certificates are on file. Drives were removed from 6 retired PCs in 2025 with no destruction record (EV-027).

**Business volume.** Revenue was $9.6 million across 250 clinic days in FY2025 (EV-028). There are about 18,000 active patients and about 240 visits per clinic day (EV-029).

**Email and AI tools.** Transport encryption is opportunistic, and no rule encrypts external messages that staff send to referring offices (EV-030). Three providers use the AI scribe pilot, and staff report using public chatbots to draft letters. No approved-tools list was found (EV-031).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they paste | Practice Administrator | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| MSP's own security assurance (SOC 2 or questionnaire) | MSP service manager | 2026-07-03 | Not provided; carried into the P01 risk register (R-022) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue and visit volume (EV-028, EV-029), backup schedule (EV-011), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-005 to EV-011 and EV-030 |
| P04 Cloud mapping | Cloud and SaaS components (EV-010, EV-020) and provider assurance (EV-022, EV-023) |
| P01 Risk register | Likelihood inputs from the ticket history (EV-017), scanning status (EV-018), configuration exports and the walk-throughs |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The existing 2019 template (EV-012) and the handbook (EV-015) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-004, EV-006) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register |
| P09 SOC 2 | Vendor assurance on file (EV-022, EV-023) |
| P10 AI governance | AI tools found (EV-020, EV-031) |
