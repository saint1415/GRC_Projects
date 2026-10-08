# Intake Report: Cris Santos Company | Health Care and Social Assistance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice, one Florida exam suite) |
| Intake window | 2026-07-13 to 2026-07-17 |
| Collected by | Physician-owner (owner, Privacy Officer and Security Officer) |
| Approved | Physician-owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the practice's own records before the self-assessment began on 2026-07-20. A one-person practice has no HR system, asset database or internal audit, so the systems of record are the vendors' admin portals, the EHR's own reports, bank and card statements, the email inbox, the signed agreements folder, the phone, and the insurance agent's portal. Intake covers the organization, the systems that create, receive, maintain or transmit ePHI, the vendors that touch them, and the rules that may bind the practice. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| EHR accounts, sign-in and logs | EV-001 to EV-003, EV-025 | EHR/PM admin settings | 2026-07-13 to 2026-07-14 |
| Email, files and fax | EV-004 to EV-006 | Email and file account; provider terms; fax portal | 2026-07-14 |
| Devices | EV-007, EV-008 | Laptop, tablet and phone settings screens | 2026-07-15 |
| Office, network and paper | EV-009 to EV-012 | Building management notices; lease; suite walk-through | 2024-03-01 to 2026-07-15 |
| Vendors and contracts | EV-013 to EV-017 | Signed agreements folder; bank and card statements; inbox; answering service portal | 2026-06-30 to 2026-07-17 |
| Business volume | EV-018 to EV-020 | Billing company portal; tax files; EHR/PM reporting | 2025-12-31 to 2026-06-30 |
| Documents and training | EV-021 to EV-023 | Owner's files; CME tracking account; carrier portal | 2026-06-30 to 2026-07-16 |
| Vendor assurance and insurance | EV-024, EV-029 | EHR vendor (under NDA); insurance agent portal | 2026-01-01 to 2026-03-31 |
| AI tools | EV-025 to EV-028 | EHR settings; phone app store; AI scribe app and terms; EHR charts | 2026-07-06 to 2026-07-17 |

## 3. Observations by area
**EHR accounts, sign-in and logs.** The EHR has the owner's practice-administrator account and named billing-role accounts for billing company staff, each created by the owner, with no written request attached and no record of a user list review (EV-001). The vendor enforces MFA on every account. The owner's phone is the only registered second factor, and no backup sign-in method is set up (EV-002). Sign-in and record-access logging is on, and the report history shows no audit report run or export (EV-003).

**Email, files and fax.** Email and files sit in a personal consumer plan with two-step verification available and turned off. The mailbox and file storage hold patient documents, the plan keeps no file versions, and the junk folder holds recent phishing messages (EV-004). The provider offers a BAA only on its business plans (EV-005). The cloud fax portal supports two-step verification, and it is turned off (EV-006).

**Devices.** On the laptop, automatic updates, built-in antivirus and the host firewall are on. Full-disk encryption is off, the screen locks after 15 minutes, no backup is configured, the downloads folder holds patient documents, and the IT consultant's remote-support tool is installed. The tablet is encrypted and locks after 1 minute (EV-007). The phone is encrypted, has no remote wipe or backup set up, and holds clinical photos, patient text threads, the EHR second factor and the AI scribe app (EV-008).

**Office, network and paper.** The suite's Wi-Fi network name has its own password, and it runs on one shared building network (EV-009). The landlord controls building entry, holds a master key, and records lock repairs. The building provides a locked shredding bin (EV-010). The suite door is keyed, the chart cabinet is locked, and office practices are not written down (EV-011). Shredding certificates go to building management, and the notice does not cover electronic media (EV-012).

**Vendors and contracts.** BAAs are signed with the EHR vendor, billing company, cloud fax vendor and IT consultant (the last on 2026-07-17). None was located for the email and file provider, the answering service or the AI scribe app (EV-013). Statements show payments to 9 suppliers (8 recurring, plus the IT consultant by the hour) and no payment for a standalone cyber policy (EV-014). The IT consultant ran remote sessions on the laptop before the BAA (EV-015). The answering service texts after-hours messages, with patient names and call reasons, to the owner's phone under standard terms with no privacy terms (EV-016). The billing company submits the practice's claims electronically to Medicare, Florida Medicaid and commercial plans (EV-017).

**Business volume.** The billing company bills about $3,500 a week (EV-018). Gross receipts were about $180,000 in 2025, with no wages paid (EV-019). There are about 900 active patients and about 12 visits per clinic day, 4 days a week, about 200 clinic days a year (EV-020).

**Documents and training.** No written security policy, procedure, risk analysis, incident plan, contingency plan, contact list, Security Officer designation or device list was found (EV-021). CME records cover clinical topics only (EV-022). The previous phone was traded in on 2025-04-12 with no wipe confirmation kept (EV-023).

**Vendor assurance and insurance.** The EHR vendor's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, and its system description states RTO 4 hours and RPO 1 hour (EV-024). The professional liability declarations list no cyber endorsement (EV-029).

**AI tools.** The EHR's rule-based reminders use age, sex, problem list and medications as inputs (EV-025). The consumer AI scribe app was installed on 2026-07-06 under a free trial and lists about 96 recorded visits by 2026-07-17 (EV-026). Its click-through terms have no business associate terms and let the vendor keep recordings (EV-027). No recording consent note appears in the trial visits' charts (EV-028).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does the professional liability policy include a cyber endorsement? | Insurance agent | 2026-07-15 | Not answered at intake; P08 carries it as an owner action |
| Will the answering service sign a BAA, and what safeguards does it use? | Answering service | 2026-07-16 | Not answered at intake; carried into the P01 risk register (R-007) |
| Does the IT consultant use MFA on the remote-support tool account? | On-call IT consultant | 2026-07-17 | Not confirmed at intake; carried into the P01 risk register (R-008) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and visit volume (EV-018 to EV-020), the EHR vendor's recovery objectives (EV-024), single-person access (EV-002), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-012 |
| P04 Cloud mapping | SaaS components and terms (EV-004 to EV-006, EV-014) and provider assurance (EV-024) |
| P01 Risk register | Likelihood inputs from the device and account reviews (EV-004, EV-007, EV-008), vendor records (EV-013, EV-015, EV-016) and the AI scribe records (EV-026 to EV-028) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-021): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the accounts (EV-001), the 3 devices (EV-007, EV-008), and the 7 vendors that handle PHI (EV-013) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-029) |
| P09 SOC 2 | Vendor assurance on file (EV-024) |
| P10 AI governance | AI tools found (EV-025 to EV-028) |
