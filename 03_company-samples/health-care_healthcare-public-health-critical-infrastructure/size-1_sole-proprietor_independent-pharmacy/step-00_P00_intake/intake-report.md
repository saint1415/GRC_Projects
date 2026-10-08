# Intake Report: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy, one Florida storefront) |
| Intake window | 2026-07-27 to 2026-07-31 |
| Collected by | Pharmacist-owner (owner, prescription department manager, Privacy Officer and Security Officer) |
| Approved | Pharmacist-owner, 2026-09-04 |

## 1. Purpose and scope
Intake collected the pharmacy's own records before the self-assessment began on 2026-08-03. A one-person pharmacy has no HR system, asset database or internal audit, so the systems of record are the vendors' admin portals and reports (the pharmacy management system, the email and file suite, the cloud fax portal, the wholesaler portal, the router app), the Florida Board of Pharmacy and DEA records, bank and card statements, the email inbox, the signed agreements folder, the devices themselves, and the insurance agent's portal. The owner collected everything alone; the on-call IT consultant signed a BAA on the last day of intake and took part only from 2026-08-03. Intake covers the organization, the systems that create, receive, maintain or transmit ePHI and controlled substance records, the vendors that touch them, and the rules that may bind the pharmacy. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, vendor reports, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| PMS accounts, sign-in, logs and vendor access | EV-001 to EV-005 | PMS admin settings; remote-support agent; agreements folder and inbox | 2026-07-27 to 2026-07-28 |
| PMS records and settings | EV-006 to EV-011 | PMS reporting and admin settings | 2026-06-30 to 2026-07-27 |
| Email, files and fax | EV-012, EV-013 | Email and file suite admin console; cloud fax portal | 2026-07-28 |
| Devices, network and store | EV-014 to EV-018 | Desktop, laptop and phone settings screens; router app; store walk-through; alarm company portal | 2026-07-29 |
| Vendors and contracts | EV-019 to EV-024 | Signed agreements folder; bank and card statements; inbox; PMS sign-in history; wholesaler portal | 2026-06-30 to 2026-07-31 |
| Licenses, registrations and payers | EV-025 to EV-027 | DEA registration portal; Florida Board of Pharmacy portal; Medicaid portal and PBM agreements | 2026-07-30 |
| Business volume and insurance | EV-028, EV-029 | Tax files; insurance agent portal | 2025-12-31 to 2026-01-01 |
| Documents and training | EV-030, EV-031 | Owner's files on every device and on paper; continuing education account | 2026-07-30 to 2026-07-31 |
| AI tools | EV-010, EV-032, EV-033 | PMS DUR settings; AI chatbot account and terms | 2026-03-02 to 2026-07-31 |

## 3. Observations by area
**PMS accounts, sign-in, logs and vendor access.** The PMS has one pharmacy user account, the owner's, with the administrator role, plus vendor support accounts. The role catalog includes a pharmacist role and a separate controlled substance annotation permission, and only the administrator role is assigned. No account exists for the relief pharmacist, and no user list review is on record (EV-001). MFA is enforced for web sign-in from outside the store, with the owner's phone as the only second factor. The store is a vendor-defined trusted location where a password alone is accepted, and the password was last changed in 2023 (EV-002). The PMS keeps an audit trail and 90 daily EPCS audit reports. Every retained report is marked unopened, and the sign-in report has no run on record (EV-003). The vendor's remote-support agent on the counter desktop has unattended access turned on, so a session can start with no prompt at the desktop (EV-004). The 2021 service agreement covers the e-prescribing network and claims switch through the vendor's subcontractors. EPCS was turned on at go-live in 2021, and no EPCS audit or certification report, or request for one, is in the inbox or the agreements folder (EV-005).

**PMS records and settings.** The pharmacy has about 650 active patients and about 2,400 patient records. It fills about 14 prescriptions a business day, about 15% of them controlled substances, and about 40 compounded prescriptions a month (EV-006). About 90% of prescriptions are adjudicated in real time with PBMs, and about 10% are cash (EV-007). The PMS sends the PDMP file automatically each business night (EV-008). About 10 prescriber offices send most prescriptions, and about 30 patients have addresses in other states (EV-009). DUR alerts use age, sex, pregnancy and lactation flags, allergies, medication history and dose as inputs (EV-010). Refill reminder texts carry no drug name, and the refill phone line asks for the prescription number only (EV-011).

**Email, files and fax.** The email and file suite is a business plan with MFA on since 2024. Its admin console offers the vendor's BAA, with the status not accepted. The inbox holds faxed prescriptions and refill requests, and file storage holds the master formulation records and compounding logs, with version history on. The sign-in history has no review on record (EV-012). The cloud fax portal supports MFA, and it is turned off. Every incoming fax is also sent to the inbox as a PDF (EV-013).

**Devices, network and store.** The counter desktop signs in automatically to one shared local account with administrator rights. Its screen lock and full-disk encryption are off. Updates, antivirus and the host firewall are on. The CSOS certificate sits in the shared account's browser certificate store. The desktop holds scanned prescriptions, downloaded controlled substance reports and a 2025 mailing-list export of about 2,100 patients, and its browser history includes the AI chatbot and personal sites (EV-014). The laptop is encrypted and locks after 5 minutes. The phone is encrypted, locks after 1 minute, has no remote wipe set up, and holds the second factor for email and the PMS (EV-015). The router shows one network for the desktop, the camera recorder and customer phones, and the Wi-Fi password is the one printed at the counter (EV-016). In the walk-through, the prescription department is closed to the public, controlled substances and paper prescriptions are in locked cabinets, and the store has a monitored alarm, a camera and a cross-cut shredder. The desktop faces the counter with an open PMS session, a card with the PMS password is in the counter drawer, and the previous desktop sits in the back office with no wipe or disposal record. Store practices are not written down (EV-017). The alarm company lists 2 user codes, the owner's and the relief pharmacist's (EV-018).

**Vendors and contracts.** BAAs are signed with the PMS vendor (2021), the cloud fax vendor and the IT consultant (2026-07-31). None is on file for the email and file suite vendor or the AI chatbot vendor (EV-019). Statements show recurring payments to the PMS, email, fax, internet, alarm, phone, accounting and insurance suppliers and the card processor, drug purchases from the wholesaler, and payments to the IT consultant and the relief pharmacist, with no payment to an AI chatbot vendor, and no payment for a standalone cyber policy (EV-020). The relief pharmacist works about 2 business days a month under the owner's direction. The agreement has no confidentiality or security clause, no license verification record is kept, the relief pharmacist holds a key and the alarm code, and on relief days the PMS sign-in history shows the owner's account at the store (EV-021). The IT consultant set up the store network in 2021 and bills by the hour, with no recurring service (EV-022). Schedule II orders are signed with the owner's CSOS certificate, and confirmations go to the owner's email (EV-023). The card terminal runs on the processor's own cellular connection (EV-024).

**Licenses, registrations and payers.** The DEA registration covers Schedules II to V, and the only CSOS certificate is the owner's, with no power of attorney for anyone else (EV-025). The Florida community pharmacy permit is active, with the owner as prescription department manager (EV-026). The pharmacy is an enrolled Florida Medicaid provider with PBM network agreements for Medicare Part D and commercial plans, and none of its records lists a substance use disorder service (EV-027).

**Business volume and insurance.** Gross receipts were about $180,000 in 2025, with no wages paid (EV-028). The business owner's and professional liability declarations list no cyber endorsement and do not say whether business-interruption coverage reaches a computer outage (EV-029).

**Documents and training.** The owner's files hold the notice of privacy practices and a 2021 privacy policy template. No written security policy, procedure, risk analysis, incident plan, EPCS reporting procedure, contact list, downtime procedure, sanction rule, Security Officer designation, device list, disposal record, retention rule or transfer arrangement was found (EV-030). Continuing education covers pharmacy practice topics only, and there is no security training record for either pharmacist (EV-031).

**AI tools.** The PMS DUR alerts are rule-based (EV-010). The consumer AI chatbot is a free personal account used since 2026-03-02 for counseling sheet drafts, compounding calculation checks and drug questions. The model-training setting is on, and the owner states that some conversations included patient details (EV-032). The free plan's terms offer no BAA and allow the vendor to use chats to improve its models (EV-033).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| The PMS vendor's SOC 2 report and EPCS certification report | PMS vendor account manager | 2026-07-28 | Received 2026-08-05 during the self-assessment (EV-037, EV-038) |
| Does the business owner's or professional liability policy include cyber or business-interruption coverage for a computer outage? | Insurance agent | 2026-07-30 | Not answered at intake; P08 carries it as an owner action |
| How many chatbot conversations included patient details, and which details? | Pharmacist-owner (history review) | 2026-07-31 | Not established at intake; counted in the P10 review on 2026-08-12 (EV-040) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Prescription volume and receipts (EV-006, EV-007, EV-028), PDMP reporting (EV-008), single-person access (EV-002, EV-025), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-004 and EV-011 to EV-018 |
| P04 Cloud mapping | SaaS components and terms (EV-005, EV-012, EV-013, EV-020) and the vendor's remote-support path (EV-004) |
| P01 Risk register | Likelihood inputs from the PMS, desktop and network reviews (EV-001 to EV-004, EV-014, EV-016, EV-017), the relief-day records (EV-021), the vendor records (EV-012, EV-019) and the chatbot records (EV-032, EV-033) |
| P03 Gap analysis | The obligations register (which rules apply, including the DEA EPCS and CSOS duties) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-030): only a privacy notice and a 2021 privacy template existed to start from |
| P07 Control assessment | Populations to test: the PMS, email and fax accounts (EV-001, EV-012, EV-013), the 3 devices (EV-014, EV-015), the store network (EV-016), and the vendors in the vendor register (EV-019) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; prescriber offices and out-of-state patients (EV-009); insurance status (EV-020, EV-029) |
| P09 SOC 2 | The vendor assurance requested at intake and received on 2026-08-05 (EV-037, EV-038) |
| P10 AI governance | AI tools found (EV-010, EV-032, EV-033) |
