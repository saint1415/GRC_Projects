# Intake Report: Cris Santos Company | Construction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor, home office in Florida) |
| Intake window | 2026-07-06 to 2026-07-10 (one late answer received 2026-07-14) |
| Collected by | Owner (owner, security lead, risk acceptor and SAM Entity Administrator) |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before the self-assessment began on 2026-07-13. A one-person general contractor has no HR system, asset database or internal audit, so the systems of record are the vendors' admin consoles (the project management and pay application SaaS, the accounting SaaS, the email and file account, online banking, the domain registrar, the router app, the AI bid assistant, the website builder), SAM.gov, bank and card statements, the email inbox, the signed agreements file cabinet, the phone carrier and insurance agent portals, the device settings screens, and the owner's calendar. Intake covers the organization, the systems that process, store or transmit federal contract information (FCI), payment details or subcontractors' personal information, the vendors and contractors that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Project management and pay applications | EV-001 to EV-003 | SYS-01 admin settings; the vendor's SOC 2 report and bridge letter | 2026-06-30 to 2026-07-06 |
| Accounting and business volume | EV-004 to EV-006 | Accounting SaaS settings and reports; 2025 Schedule C | 2025-12-31 to 2026-07-07 |
| Email, domain and payment correspondence | EV-007 to EV-010 | Email admin console; registrar DNS records; inbox; phone call log | 2026-03-18 to 2026-07-08 |
| Contracts and federal work | EV-011 to EV-014, EV-028 | Signed agreements file cabinet; contract file; inbox; SAM.gov | 2026-03-09 to 2026-07-07 |
| Banking and statements | EV-015, EV-016 | Online banking settings; bank and card statements | 2026-06-30 to 2026-07-07 |
| Devices and network | EV-017 to EV-020 | Carrier portal; laptop and phone settings screens; router app | 2026-07-08 |
| AI tools | EV-021, EV-022 | AI bid assistant account and terms | 2026-07-09 |
| Public content | EV-023, EV-024 | Social media page; website builder account | 2026-07-08 to 2026-07-09 |
| Insurance and contractors | EV-025 to EV-027, EV-031 | Insurance agent portal; agreements; inbox | 2026-06-30 to 2026-07-14 |
| Documents and records | EV-029, EV-030 | Owner's files (laptop, file storage, email, file cabinet); owner's calendar | 2026-07-10 |

## 3. Observations by area
**Project management and pay applications.** The owner's account is the only SYS-01 administrator. There are 23 external portal users, subcontractor staff and client representatives, each invited by the owner, and the FC-1 project lists 6 subcontractor companies. No user list review is on record (EV-001). The administrator signs in with a password only; MFA is offered for all users and turned off. The default subcontractor template shows the whole project folder, including other subcontractors' pricing. The export history lists no project data export (EV-002). The vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, with an unqualified opinion and no exceptions, and a bridge letter runs through 2026-06-30. Its system description states RTO 4 hours, RPO 1 hour, and encrypted backups kept in a separate location, and it lists the customer controls the company must run (EV-003).

**Accounting and business volume.** The accounting SaaS has one login, the owner's, with a password only and MFA off. The password was last changed in 2023, and the sign-in history shows sign-ins from a second computer during the bookkeeper's monthly sessions. Vendor records hold bank details, alerts on bank-detail changes are off, and 1099 tracking holds the W-9 forms of the 8 subcontractors who are sole proprietors (EV-004). About $15,000 is billed and about $9,000 paid out in a typical month, to about 14 trade subcontractors and 6 suppliers in 2026. No card payments are received (EV-005). Gross receipts were about $180,000 in 2025, with no wages paid (EV-006).

**Email, domain and payment correspondence.** The business email account (1 licensed user) uses 2-step verification by text message code, turned on in 2024. The provider keeps a sign-in history and a record of forwarding and inbox rules, with no record of a review, and it scans attachments (EV-007). The domain publishes SPF only, with no DKIM or DMARC record and no look-alike domain monitoring (EV-008). Pay apps, lien waivers, invoices and payment correspondence go by email. Earlier subcontractor bank-detail changes were requested and confirmed by email, with no record of a call-back. W-9 forms sit as attachments, and subcontractors send drawings through free file-transfer links (EV-009). In March 2026 an email appearing to come from the electrical subcontractor asked for a bank change. The real subcontractor phoned that day about another matter and said it had not changed its account (EV-010).

**Contracts and federal work.** Every 2026 job has written subcontracts on the standard form. The form refers to "all applicable federal clauses" without setting out the substance of FAR 52.204-21 or 52.204-25, and the 6 FC-1 subcontracts use it. The client contract form and the pay app cover sheet say nothing about how remittance details change (EV-011). FC-1 is a VA firm-fixed-price contract of about $68,000, awarded 2026-03-09, that includes FAR 52.204-21, 52.204-23, 52.204-25, 52.222-8, 52.232-27 and 52.232-33 (EV-012). A prime contractor's request for proposal for a DoD subcontract of about $45,000 requires a current Final Level 1 (Self) status with an SPRS affirmation before award, expects no CUI, and includes a wireless door-access upgrade (EV-013). The SAM registration is active, the owner is the only Entity Administrator, and the representations were renewed in January 2026 with a "does not use" answer on covered telecommunications. The government sign-in service requires the authenticator app on the phone, and no SPRS account exists (EV-014). The private jobs include a dental office build-out with no patient information exchanged, a church hall renovation and small retail repairs (EV-028).

**Banking and statements.** Online banking has one user, the owner. The bank requires app approval for each new payee and each ACH batch, with a $30,000 daily ACH limit and no positive pay (EV-015). Statements show recurring payments to the project management, accounting and email vendors, the domain registrar, the website builder, the phone carrier, the internet provider, the storage facility and the general liability insurer; the AI bid assistant from 2026-03; the IT technician by the hour, the bookkeeper monthly and the CPA firm yearly; a laptop purchase in 2026-02; and no payment for cyber insurance (EV-016).

**Devices and network.** The carrier account holds the phone line and a carrier-branded mobile hotspot. The previous phone was traded in during 2025 with no wipe confirmation kept (EV-017). The laptop has one administrator login used by the owner and family members. Full-disk encryption, built-in antivirus, automatic updates and the host firewall are on. No backup is configured, and estimates, scanned lien waivers and W-9 forms are not copied anywhere else (EV-018). The phone has a passcode, biometric unlock and encryption. It receives the email codes and holds the bank app and the government sign-in authenticator, with no other second factor registered. Find-and-wipe is not turned on, and the camera roll, including FC-1 jobsite photos, syncs to a personal consumer cloud account (EV-019). The router runs one network shared with family phones, a game console, a smart TV and a doorbell camera, on firmware from 2021 with no update since setup (EV-020).

**AI tools.** The AI bid assistant is an individual subscription opened in 2026-03, used for about 20 bids and change orders. Its "use my content to improve the service" setting is on, and FC-1 change-order drawings were uploaded in 2026-06 (EV-021). The individual plan terms let the vendor use uploads to improve its service while the setting is on; a business plan offers no-training terms, deletion on request and MFA (EV-022).

**Public content.** Only the owner posts to the company's social media page. An April 2026 jobsite photo shows an FC-1 floor plan taped to a wall (EV-023). The website runs on a website builder with no integration with the company's other accounts (EV-024).

**Insurance and contractors.** The declarations list general liability and tool coverage and no cyber, funds transfer fraud or social engineering coverage (EV-025). The agent confirmed on 2026-07-14 that no such coverage exists (EV-031). The bookkeeper works about 6 hours a month under an engagement letter with no security or confidentiality terms; the previous bookkeeper's engagement ended in 2024 (EV-026). The IT technician is paid by the hour for on-site help, including setup of the router and the laptop, with no remote support plan (EV-027).

**Documents and records.** No written security policy, FCI scope, inventory, system security plan, risk assessment, CMMC self-assessment, Section 889 inquiry record, incident plan or contact list, wipe or disposal record, training certificate, stored recovery codes, retention rule or standby arrangement was found (EV-029). Old plan sets and bid documents go to a community shredding event twice a year, which gives no destruction record (EV-030).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does any policy cover cyber, funds transfer fraud or social engineering losses? | Insurance agent | 2026-07-09 | Answered 2026-07-14 (EV-031): no such coverage |
| How is the bookkeeper's own computer protected, and does anyone else use it? | Outside bookkeeper | 2026-07-09 | Not answered at intake; carried into the P01 risk register (R-004) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Billing and payout volume (EV-005), receipts (EV-006), FC-1 payment and payroll clauses (EV-012), the vendor's recovery objectives (EV-003), single-person access (EV-014, EV-015, EV-019), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-004, EV-007, EV-008 and EV-015 to EV-024 |
| P04 Cloud mapping | SaaS components and settings (EV-002, EV-004, EV-007, EV-008, EV-021) and provider assurance (EV-003) |
| P01 Risk register | Likelihood inputs from the account and device reviews (EV-004, EV-007, EV-018 to EV-020), the payment correspondence and the March 2026 email (EV-009, EV-010), the contract forms (EV-011), the prime's requirement (EV-013) and the insurance records (EV-025, EV-031) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the FAR, CMMC and Section 889 requirements |
| P06 Policies | The document search (EV-029): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the SaaS accounts (EV-001, EV-002, EV-004, EV-007), the laptop and phone (EV-018, EV-019), the router (EV-020) and the vendors in the vendor register |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-025, EV-031) |
| P09 SOC 2 | Vendor assurance on file (EV-003) |
| P10 AI governance | AI tools found (EV-021, EV-022) |
