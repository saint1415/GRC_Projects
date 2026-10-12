# Intake Report: Cris Santos Company | Financial Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent property and casualty insurance agency, Florida home office) |
| Intake window | 2026-07-27 to 2026-07-31 |
| Collected by | Owner-agent (owner, licensed agent, information security coordinator) |
| Approved | Owner-agent, 2026-09-14 |

## 1. Purpose and scope
Intake collected the agency's own records before the self-assessment began on 2026-08-03. A one-person agency has no HR system, asset database or internal audit, so the systems of record are the AMS and the other vendors' admin settings and reports, the device and router settings screens, the inbox and file storage, the signed agreements folder, bank and card statements, the accounting SaaS, the tax files, the Department of Financial Services licensee records, the E&O insurer's portal, and the lead insurer's security questionnaire. Intake covers the organization, the systems that hold or move client personal information and premium money, the vendors and insurers that touch them, and the rules and contracts that may bind the agency. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (the BIA worksheet, the risk walk-through, the gap analysis self-review, the control tests, the AI use review) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| AMS accounts, settings and book of business | EV-001 to EV-004 | AMS admin settings, reports and release notes | 2026-06-30 to 2026-07-27 |
| Email and files | EV-005 to EV-008 | Email and file suite admin console and terms; mailbox; AMS activity notes | 2026-07-08 to 2026-07-28 |
| Portals and e-signature | EV-009, EV-010 | Insurer, rater and partner portals; e-signature account | 2026-07-28 to 2026-07-29 |
| Devices, home office and network | EV-011 to EV-015 | Laptop and phone settings; printer-scanner menu and lease; walk-through; router admin page | 2026-07-29 |
| Banking and accounting | EV-016 to EV-019 | Online banking; bank and card statements; accounting SaaS | 2026-06-30 to 2026-07-30 |
| Contracts and the questionnaire | EV-020 to EV-022 | Signed agreements folder; inbox | 2026-06-15 to 2026-07-30 |
| Documents, licensing, revenue and insurance | EV-023 to EV-026 | Owner's files; licensee records and CE transcript; tax files; E&O insurer portal | 2025-12-31 to 2026-07-31 |
| Vendor assurance | EV-027 | AMS vendor (under NDA) | 2026-03-31 |
| AI tools | EV-004, EV-028, EV-029 | AMS settings; chatbot account and terms | 2026-04-06 to 2026-07-30 |

## 3. Observations by area
**AMS accounts, settings and book of business.** The AMS has one user, the owner's administrator account. The vendor enforces an authenticator app code at every sign-in, the owner's phone is the only registered authenticator, and no backup sign-in method is set up. The activity log records sign-ins and record changes, and the report history shows no activity report run or exported (EV-001). The client upload portal is included in the subscription and turned off, and no export has ever been run (EV-002). The book of business shows about 640 client accounts (about 510 households and about 130 small businesses), about 1,150 policies, about 60 agency-billed commercial policies, and about 1,900 individuals named, about 60 of them with a primary address outside Florida. The lead insurer is about 40% of the book, and AMS records begin in 2022 (EV-003). An AI assistant arrived in the 2026-06 release, turned on by default (EV-004).

**Email and files.** The business plan email suite has one user, who is also the tenant administrator. The second step at sign-in is a text message code, turned on in 2025. Forwarding to outside addresses is allowed, no alert exists for new mailbox rules, and no record shows a sign-in history review. No forwarding rules are present, and the 30-day sign-in history lists only the owner's laptop and phone. Deleted items and file versions are kept 30 days, with no backup service (EV-005). The terms include the vendor's data protection addendum (EV-006). The mailbox holds applications, loss runs, payroll reports and bank draft forms as attachments, some with driver license and Social Security numbers. Invoices for agency-billed policies carry the premium trust account's bank details, and no message tells clients that bank details never change by email (EV-007). On 2026-07-08 a client forwarded a fake renewal invoice for an $18,400 workers compensation deposit premium from a lookalike domain, and called the owner before paying (EV-008).

**Portals and e-signature.** 7 of the 9 insurer portals require a second factor. 2 insurer portals offer password sign-in only, and the comparative rater offers MFA that is turned off (EV-009). E-signature links go to the client's email on file (EV-010).

**Devices, home office and network.** The laptop has full-disk encryption, automatic updates, built-in antivirus, the host firewall and a 5-minute screen lock. Its browser stores the agency portal passwords and flags some as reused, and its synced folders and downloads hold client documents (EV-011). The phone is encrypted with a passcode and a 30-second lock, and remote wipe is off. It is the only device for the AMS authenticator and the email and bank text codes. Its messages hold client driver license photos and bank codes forwarded to the bookkeeper (EV-012). The leased printer-scanner keeps scans on internal storage that is not encrypted, and goes back to the dealer on 2026-11-30 (EV-013). The agency room is locked when the owner is away, a cross-cut shredder is in use, the retired laptop is in a closet, and client files from 2014 to 2021 are in garage boxes open to the household (EV-014). The router's admin page opens with the default password, one Wi-Fi network serves the agency and family devices, and the firmware is the version from setup (EV-015).

**Banking and accounting.** Online banking has one user, the owner, with full rights on the operating and premium trust accounts and a text code at sign-in. Sub-users are available and none is set up (EV-016). About $240,000 of premium passed through the separate premium trust account in 12 months, by check and bank transfer, with a reconciliation for each month (EV-017). The accounting SaaS has two named users, the owner and the bookkeeper, whose role is limited to bookkeeping and reports, and keeps 7 years of records (EV-018). Statements show recurring payments to 9 suppliers, monthly payments to the bookkeeper, hourly payments to the IT consultant, and no payment to a backup service, password manager or card processor (EV-019).

**Contracts and the questionnaire.** The AMS contract has breach notice and data export terms. The IT consultant signed confidentiality and security terms on 2026-07-27, with no earlier written terms. The bookkeeper's engagement letter has no confidentiality or security terms, the e-signature and rater terms have no record of review, and no vendor list, breach counsel agreement, or emergency servicing arrangement was located (EV-020). 4 of the 9 agency agreements carry a data security addendum with an MFA requirement, a 72-hour incident notice and an annual questionnaire (EV-021). The lead insurer's questionnaire, received 2026-06-15 and due 2026-09-30, asks for a written program, a designated individual, a risk assessment, MFA and an incident response plan (EV-022).

**Documents, licensing, revenue and insurance.** No written security program, policy, risk assessment, incident plan, contact list, designation, vendor list, data location list, retention schedule, disposal or change record, or training record was found (EV-023). The owner is the only licensed person for the agency, holds Florida licenses only, and has continuing education on insurance topics only (EV-024). 2025 gross receipts were about $180,000 in commissions, with no wages paid (EV-025). The E&O policy has a cyber and social engineering endorsement with sublimits of $50,000 and $25,000, notice as soon as practicable, and panel vendors (EV-026).

**Vendor assurance.** The AMS vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, and its system description states RTO 4 hours and RPO 1 hour (EV-027).

**AI tools.** The AMS assistant's terms say customer data is not used to train shared models (EV-004). The consumer chatbot account holds chats from 2026-04-06 with pasted information for about 40 client accounts, including driver license numbers for 7 clients and no Social Security numbers, and its training setting is on (EV-028). The consumer terms let the vendor use chats to improve its models unless the user opts out (EV-029).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| What protects the bookkeeper's own computer (updates, antivirus, who else uses it)? | Outsourced bookkeeper | 2026-07-30 | Not answered at intake; carried into the P01 risk register (R-005) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue (EV-025), book of business and agency-billed volume (EV-003, EV-017), the AMS vendor's recovery objectives (EV-027), single-device access (EV-001, EV-012), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-018 |
| P04 Cloud mapping | SaaS components and terms (EV-001, EV-002, EV-005, EV-006, EV-009, EV-010, EV-016) and provider assurance (EV-027) |
| P01 Risk register | Likelihood inputs from the near miss (EV-008), the account, device and banking records (EV-005, EV-007, EV-009, EV-011, EV-012, EV-015, EV-016), the agreements (EV-020, EV-021) and the AI records (EV-028, EV-029) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-023): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the owner's accounts (EV-001, EV-005, EV-009, EV-016), the devices (EV-011 to EV-013), and the vendors in the vendor register |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; the E&O endorsement (EV-026) and the addenda's 72-hour clause (EV-021) |
| P09 SOC 2 | Vendor assurance on file (EV-027) and the questionnaire (EV-022) |
| P10 AI governance | AI tools found (EV-004, EV-028, EV-029) |
