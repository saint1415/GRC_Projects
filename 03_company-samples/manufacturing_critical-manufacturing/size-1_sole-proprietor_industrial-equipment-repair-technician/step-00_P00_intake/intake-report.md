# Intake Report: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service, Florida home office and service van) |
| Intake window | 2026-08-17 to 2026-08-21 |
| Collected by | Owner-technician (owner, security lead and contract compliance) |
| Approved | Owner-technician, 2026-09-11 |

## 1. Purpose and scope
Intake collected the business's own records before the self-assessment began on 2026-08-24. A one-person repair business has no HR system, asset database or internal audit, so the systems of record are the SaaS admin consoles and portals, the accounting reports, bank and card statements, the email inbox, the signed agreements folder, the job tickets, the laptop, phone and field kit themselves, the router maker's portal, the insurance agent's portal, and a walk-through of the home office and the service van. Intake covers the organization, the systems that hold or carry customer machine programs and other confidential customer data, the vendors that touch them, and the rules and contract terms that may bind the business. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Productivity suite and the Customer Machine Library | EV-001 to EV-004 | Suite admin console; sync client; library folder; cloud storage | 2026-08-17 |
| Accounting | EV-005 | Accounting SaaS settings | 2026-08-18 |
| Laptop, virtual machine, phone and field kit | EV-006 to EV-009 | Device settings screens; field kit in the van | 2026-08-19 |
| Home office, van and home network | EV-010, EV-011 | Walk-through; internet provider's router app | 2026-08-19 |
| Router at Customer B | EV-012, EV-013 | Router maker's cloud portal; inbox; expense records | 2026-08-18 |
| Customer contracts and access | EV-014 to EV-017 | Signed agreements folder; Customer A gateway | 2025-09-30 to 2026-08-20 |
| Field records | EV-018 to EV-020 | Job tickets; firmware files; sent mail and inbox | 2026-08-19 to 2026-08-20 |
| Documents and training | EV-021, EV-022 | Owner's files; certificates folder | 2026-08-20 |
| Insurance | EV-023, EV-024 | Insurance agent portal | 2026-08-18 |
| Business volume and purchase orders | EV-025 to EV-028 | Bank and card statements; tax files; accounting reports; POs | 2025-12-31 to 2026-07-31 |
| AI tools | EV-029, EV-030, EV-008 | Vibration analytics account and terms; phone app review | 2026-05-04 to 2026-08-19 |
| Contracted services and vendor assurance | EV-031 to EV-033 | Signed agreements folder; inbox; suite provider trust portal | 2026-06-30 to 2026-08-20 |

## 3. Observations by area
**Productivity suite and the Customer Machine Library.** The business plan has one user, the owner, as administrator. MFA is on with an authenticator app on the owner's phone, the only registered second factor. The provider keeps sign-in and sharing history, and no saved review of it exists (EV-001). The library folder on the laptop syncs to cloud storage, deleted files and prior versions are kept 30 days, and the activity history shows no restore. The sharing report lists 3 "anyone with the link" links to customer program folders, created in 2025 and 2026 (EV-002). The library holds about 2,400 files for about 70 machines at 10 customer sites, saved with the visit date in the file name, with no index, no record of the current version, and no hash values (EV-003). An ordinary spreadsheet with no file protection lists about 140 customer machine passwords for 10 sites (EV-004).

**Accounting.** The owner's administrator account signs in with a password only, although MFA is offered. The bookkeeper's accountant-role login signs in through the CPA firm's account with MFA (EV-005).

**Laptop, virtual machine, phone and field kit.** The laptop has one local account with administrator rights, used for email, web, quotes and engineering work. Full-disk encryption, built-in antivirus, automatic updates and the host firewall are on. Engineering software from 5 automation makers is installed, the IT consultant's remote-support tool is installed with unattended access off, and nothing backs up the laptop except the sync client (EV-006). The legacy engineering virtual machine runs an operating system that no longer receives updates, has no malicious code protection, and is bridged to whatever network the laptop is on (EV-007). The phone has a passcode, encryption and remote wipe. It holds the only MFA app, the vibration analytics app and a consumer generative AI assistant, and its camera roll of equipment photos syncs to the owner's personal photo cloud (EV-008). The field kit holds 8 unencrypted USB sticks with program files for more than one customer (EV-009).

**Home office, van and home network.** The old laptop, replaced in 2025, is in a desk drawer with a library copy and no wipe record. Paper records are in a locked cabinet. The van locks and has an alarm, and the laptop is kept in the home office overnight (EV-010). The home Wi-Fi is shared with family laptops, a smart TV and a game console, and a guest network is available and off (EV-011).

**Router at Customer B.** The router maker's portal account is the owner's and signs in with a password only. The router on Customer B's drying oven panel has been online since 2024-11, and sessions start with no approval step (EV-012). The owner bought it at the maintenance supervisor's request, and no approval from Customer B's plant management was found (EV-013).

**Customer contracts and access.** Customer A's agreement was renewed on 2025-09-30 with exhibit terms S1 to S8 (EV-014). Customer A's letters of the same date say that S4, S5 and S6 flow down CIP-013-2 R1.2 topics from its utility contracts, that the owner works escorted in substations, and that the work involves no FAR or DFARS clauses, FCI or CUI (EV-015). Customers B and C have mutual NDAs, and the seven local plants have no written security terms (EV-016). Customer A's gateway uses a named account, MFA, per-session approval and session recording (EV-017).

**Field records.** Customer A job tickets show about 6 night breakdown calls in 12 months and no field for media scanning (EV-018). Firmware was loaded on 4 substation cabinets in 2026, with Customer A's hash values received and no hash check recorded (EV-019). Program files and sharing links were emailed to OEM support desks, and no customer consent appears for those messages or for the vibration analytics trial (EV-020).

**Documents and training.** No written security policy, risk assessment, list of contract duties, incident plan or contact list, contingency plan, emergency access sheet, referral arrangement, software and license list, or disposal rule was found (EV-021). No security course certificate appears (EV-022).

**Insurance.** The general liability declarations list no cyber coverage (EV-023). The insurance equipment schedule lists the laptop, phone and instruments, and not the USB sticks, the router or the old laptop (EV-024).

**Business volume and purchase orders.** Statements show recurring payments to the suite, accounting, phone, internet and insurance providers, the CPA firm and the IT consultant, and no payment for cyber insurance, a backup service, a password manager or a security course (EV-025). Gross receipts were about $180,000 in 2025 with no wages paid (EV-026). About 10 business customers: Customer A about 45%, Customer B about 20%, Customer C about 15%, seven local plants about 20%. Breakdown calls are about 40% of receipts, and about $3,500 is invoiced per week (EV-027). No PO carries a FAR or DFARS clause, and every work site is in the United States (EV-028).

**AI tools.** The vibration analytics trial opened on 2026-05-04, with sensors on 6 motors at Customer A and 4 at one local plant, and uploads that include machine and plant names (EV-029). Its click-through terms let the vendor use uploaded data to improve its service (EV-030). A consumer generative AI assistant is on the phone (EV-008).

**Contracted services and vendor assurance.** The IT consultant signed the owner's NDA on 2026-08-20 and invoices hourly for remote-support sessions (EV-031). The bookkeeper works under an engagement letter (EV-032). The productivity suite provider's SOC 2 Type 2 report covers Security, Availability and Confidentiality for the 12 months ending 2026-06-30 (EV-033).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Media scanning station log for the owner's visits in the last 12 months | Customer A plant controls engineer | 2026-08-20 | Not received at intake; P02 and P03 cite it as requested |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Receipts and customer mix (EV-026, EV-027), library storage and retention (EV-002, EV-003), single-person access (EV-001), contract terms (EV-014, EV-016), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-013 |
| P04 Cloud mapping | SaaS components and settings (EV-001, EV-002, EV-005, EV-012, EV-029, EV-030) and provider assurance (EV-033) |
| P01 Risk register | Likelihood inputs from the account, device and network reviews (EV-001, EV-004 to EV-012), the field records (EV-018 to EV-020), the document search (EV-021) and the AI trial records (EV-029, EV-030) |
| P03 Gap analysis | The obligations register (which rules and contract terms apply) and every observation above, compared with CSF 2.0, SP 800-82 Rev. 3 and the contract terms |
| P06 Policies | The document search (EV-021): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the administrator accounts (EV-001, EV-005, EV-012), the laptop and virtual machine (EV-006, EV-007), the 8 USB sticks (EV-009), the 4 firmware loads (EV-019), and the 4 SaaS suppliers (EV-001, EV-005, EV-012, EV-029) |
| P08 IR runbook | Notice terms from the obligations register (EV-014, EV-016); contacts from the vendor register; insurance status (EV-023) |
| P09 SOC 2 | Vendor assurance on file (EV-033) |
| P10 AI governance | AI tools found (EV-008, EV-029, EV-030) |
