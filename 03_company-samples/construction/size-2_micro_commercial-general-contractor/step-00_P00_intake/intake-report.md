# Intake Report: Cris Santos Company | Construction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor, one Florida office and 4 active jobsites) |
| Intake window | 2026-07-06 to 2026-07-17 |
| Collected by | Office Manager, with the MSP lead technician for the MSP exports |
| Approved | Owner and President, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-20. It covers the organization, the systems that process, store or transmit Federal Contract Information (FCI), payment instructions and employee data, the suppliers that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, tests) to the same register, so one list backs every deliverable.

A 7-person contractor has no HR system, CMDB or accounts payable vendor master. Its systems of record are the vendor admin consoles (productivity suite, project management platform, accounting, payroll), the bank portal, SAM.gov, the MSP's exports and monthly report, the paper contracts and HR files, the card statements, the Office Manager's mailbox, and what can be seen in the office.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| People, access and payments | EV-001 to EV-009 | Payroll service; productivity suite, SYS-01 and SYS-02 admin consoles; domain registrar; bank portal; SAM.gov | 2026-06-30 to 2026-07-09 |
| Devices, network and backup | EV-010 to EV-018 | MSP device, policy and antivirus consoles; MSP monthly report; firewall documentation; backup console; MSP tickets; carrier account; device check | 2026-06-30 to 2026-07-15 |
| Suppliers and contracts | EV-019 to EV-032 | Card statements and invoices; contracts folder; vendor portals; SYS-01 submittal log; SAM.gov opportunities; Owner's inbox; AI vendor portal | 2025-01-01 to 2026-07-10 |
| Documents and records | EV-033 to EV-036 | Document request; office and HR files; Office Manager's mailbox | 2022-01-01 to 2026-07-10 |
| Payments and business volume | EV-037 to EV-040 | Accounting service; SYS-01 pay app workflow; Office Manager's and Project Manager's mailboxes | 2025-12-31 to 2026-07-10 |
| Office, field and people | EV-041 to EV-045 | Office walk-through; alarm company portal; intake interviews; staff survey | 2026-07-10 to 2026-07-15 |

## 3. Observations by area
**People, access and payments.** Payroll lists 7 employees and 1 termination from January to June 2026, a Superintendent whose last working day was in April 2026 (EV-001). The productivity suite has named accounts for the 5 staff who use email, each with push MFA, and a shared "bids" mailbox that signs in with a shared password, last changed in 2024, and no MFA (EV-002). External auto-forwarding is allowed and no alerts are set for new inbox or forwarding rules (EV-003). No DMARC record is published (EV-004). SYS-01 has about 60 external users, each limited to one project; the Project Manager and both Superintendents hold company administrator rights; MFA is available and not enforced; and no company export of project records appears in its history (EV-005). In SYS-02 the Office Manager's role can add vendors and edit their bank details with no approval step (EV-006). In the bank portal only the Owner can release ACH batches and wires, and the release screen does not show which payee bank details changed (EV-007). Payroll employees can change their own direct-deposit account (EV-008). The SAM registration holds the company's EFT information; its representations were renewed in March 2026; the Owner signs in with MFA through the government sign-in service; and the company has no SPRS account (EV-009). The account lists were compared with payroll during the risk analysis (EV-049).

**Devices, network and backup.** The MSP device list shows 4 laptops and the office desktop and nothing else (EV-010). The 4 laptops are encrypted and the desktop is not; screen lock, automatic patching and the MSP's remote agent cover all 5 computers, with 5 of 5 current (EV-011). The MSP's services do not include vulnerability scanning, 24x7 monitoring or phone and tablet management (EV-012). Antivirus runs on all 5 computers, and its alerts go by email to the MSP help desk in business hours (EV-013). The firewall exposes no services; one Wi-Fi network serves staff, visitors, the printer and the plotter; the firmware is 11 months old; and logs are kept 7 days (EV-014). The backup copies email and files daily with 30 days of retention, immutable retention off, one MSP administrator account and no restore jobs; SYS-01 to SYS-03 are outside its scope (EV-015). MSP tickets close the retirement of 3 laptops since 2024 with no wipe record (EV-016). The 5 phones and 2 tablets are not in device management, one tablet has no passcode, and both tablets stay signed in to SYS-01 as a Superintendent (EV-017). The office has one internet line (EV-018).

**Suppliers and contracts.** The card statements and invoices show the SaaS vendors, the MSP (including a resold backup), the internet and cellular providers, the website host, the cyber insurer, and an AI estimating subscription from June 2026 (EV-019). The MSP contract has business-hours response, no recovery time commitment and no incident notice term, and renews 2026-12-31 (EV-020). SYS-01, accounting and payroll run on click-through terms (EV-021). The SYS-01 vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 4 hours and an RPO of 1 hour, with a bridge letter through 2026-06-30 (EV-022). FC-1 carries FAR 52.204-21, 52.204-25, 52.222-8, 52.232-27 and 52.232-33 (EV-023). The 2023 subcontract template has a one-line clause requiring compliance with the prime contract; 6 FC-1 subcontractors signed it (EV-024). The submittal log has no field for the equipment manufacturer; the FC-1 camera and recorder submittal was approved on 2026-06-10 (EV-025). A DoD pre-solicitation notice expects to require CMMC Level 1 (Self) (EV-026). The cyber policy's $25,000 social engineering sublimit applies only with a recorded call-back (EV-027). The medical office owner's contract limits sharing of its drawings (EV-028). The printer lease has no storage wipe clause (EV-029). The website is vendor-hosted (EV-030). A hospital system's security questionnaire is due 2026-10-15 (EV-031). The AI estimating trial started on 2026-06-01 under terms that allow model training, with MFA off and FC-1 change-order drawings uploaded (EV-032).

**Documents and records.** The request for policies, a risk assessment, incident response and contingency plans, a system security plan, an FCI scope, an inventory, a CMMC self-assessment, training and call-back records, a Section 889 inquiry record and a retention rule returned none, and no security lead is designated in writing (EV-033). The handbook has a short conduct section only (EV-034). The departed Superintendent's termination file records no account removal or key return (EV-035). Staff accounts trace to the Owner's emailed hiring approvals; SYS-01 subcontractor users are added on emailed requests (EV-036).

**Payments and business volume.** Revenue was about $1.1 million in FY2025, about $4,400 per business day (EV-037). About $92,000 is billed a month, the largest pay app in 2026 was $78,000, and about $55,000 a month goes to about 25 subcontractors and suppliers, mostly by ACH (EV-038). June pay apps went out as PDFs from the Project Manager's mailbox with the company's bank details on the cover page (EV-039). In May 2026 a spoofed supplier email asked for a bank change, which was not entered after the supplier's representative happened to call (EV-040).

**Office, field and people.** The office has keyed entry with an alarm, a locked tool room and a locked network closet; visitors receive the Wi-Fi password; and 6 keys have been issued with no key list (EV-041). The alarm uses one shared code, unchanged since 2022 (EV-042). The Office Manager describes bank changes entered from email with no call-back, terminations without a checklist, no log review, no call-back records, the insurer's hotline number not at hand, and certified payrolls for about 40 workers held in her mailbox (EV-043). The Superintendents forward drawings, including FC-1 drawings, to personal email for printing, and the Project Manager uploads drawings to the AI trial (EV-044). The staff survey found the AI trial and mentions of public chatbots (EV-045).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Number of staff using public chatbots, and what they enter | Office Manager (staff survey follow-up) | 2026-07-16 | Not established at intake; P10 treats it as unknown |
| MSP technician list and evidence of MFA on the remote management platform | MSP lead technician | 2026-07-09 | Not provided; asked again for P07 on 2026-08-10 and not received by fieldwork end (EV-061); carried into the P01 risk register (R-014) and POAM-004 |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-001, EV-043), revenue and billing volume (EV-037, EV-038), the FC-1 payment and payroll clauses (EV-023), the backup schedule (EV-015), vendor recovery figures (EV-020, EV-022), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-002 to EV-017 |
| P04 Cloud mapping | SaaS components and the MSP-operated backup (EV-002 to EV-008, EV-015, EV-019) and provider documentation (EV-021, EV-022) |
| P01 Risk register | Likelihood inputs from the console and MSP exports, the bank portal and SAM records, the contracts folder, the May 2026 email (EV-040) and the intake interviews (EV-043, EV-044) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document request (EV-033) and the handbook (EV-034) |
| P07 Control assessment | Populations to test from (EV-001, EV-002, EV-005, EV-006, EV-010, EV-025) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the cyber policy (EV-027) |
| P09 SOC 2 | Vendor assurance on file (EV-021, EV-022) and the hospital system's questionnaire (EV-031) |
| P10 AI governance | AI tools found (EV-019, EV-032, EV-044, EV-045) |

The asset inventory in this folder is the assessment's list, built from the evidence above. It is not a company-maintained inventory; the SSP (CM-8) and the P03 remediation plan call for one.
