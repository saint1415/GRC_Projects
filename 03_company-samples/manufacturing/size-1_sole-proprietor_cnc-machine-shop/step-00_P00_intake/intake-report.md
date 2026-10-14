# Intake Report: Cris Santos Company | Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop, one leased Florida bay) |
| Intake window | 2026-08-03 to 2026-08-07 |
| Collected by | Owner-machinist (owner, security lead and CMMC affirming official) |
| Approved | Owner-machinist, 2026-09-04 |

## 1. Purpose and scope
Intake collected the shop's own records before the self-assessment began on 2026-08-10. A one-person machine shop has no HR system, asset database or internal audit, so the systems of record are the SaaS admin consoles, the accounting reports, bank and card statements, the email inbox, the signed agreements folder, the customer portals, the laptop and phone settings, the router app, the machine controller, the insurance agent's portal, and a walk-through of the bay. Intake covers the organization, the systems that hold customer drawings, programs and Federal contract information (FCI), the vendors and processors that touch them, and the rules and contract terms that may bind the shop. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Productivity suite | EV-001 to EV-003 | Suite admin console; provider terms and trust portal | 2026-08-03 |
| Accounting and business volume | EV-004 to EV-007 | Accounting SaaS settings and reports; tax files; bank and card statements | 2025-12-31 to 2026-08-04 |
| Devices and network | EV-008 to EV-010 | Laptop and phone settings screens; internet provider's router app | 2026-08-05 |
| Bay, machines and programs | EV-011 to EV-014 | Bay walk-through; lease and alarm agreement; VMC controller and builder notice; Jobs folder and travelers | 2023-06-01 to 2026-08-06 |
| Customers and contract terms | EV-015 to EV-019 | Signed agreements folder; customer portals; inbox; SAM.gov search | 2026-06-15 to 2026-08-06 |
| Documents | EV-020 | Owner's files | 2026-08-06 |
| Contractors, processors and visitors | EV-021 to EV-025 | Sent items and POs; signed agreements folder; inbox | 2025-01-15 to 2026-08-07 |
| Insurance and fraud attempt | EV-026, EV-027 | Insurance agent portal; inbox | 2026-01-01 to 2026-05-14 |
| Website and AI tools | EV-028, EV-029, EV-004 | Website builder settings; AI assistant account; accounting settings | 2026-08-04 to 2026-08-06 |
| Vendor assurance (intake follow-up) | EV-030 | Productivity suite provider trust portal | 2026-03-31 (received 2026-08-13) |

## 3. Observations by area
**Productivity suite.** The business plan has one user, the owner, as administrator. MFA is on with text-message codes sent to the owner's phone, the only registered second factor. The provider keeps sign-in and sharing history, and no saved review of it exists (EV-001). New sharing links default to "anyone with the link" with no expiry. Deleted items and file versions are kept 30 days. The Jobs folder, which holds drawings, CAM files, NC programs, inspection reports and quotes, syncs to the laptop, and the activity history shows no restore (EV-002). The provider publishes a SOC 2 Type 2 report on its trust portal, and the shop had no copy (EV-003).

**Accounting and business volume.** The accounting SaaS has the owner's administrator account, which signs in with a password only, and the bookkeeper's named accountant login, which signs in through the CPA firm's account with MFA. Card payments go through the provider's hosted payment page, and automatic transaction categorization is on (EV-004). About 12 business customers and no consumers: three medical device OEMs about 65% of receipts, the aerospace supplier about 20%, and about eight local customers about 15% (EV-005). Gross receipts were about $180,000 in 2025, with no wages paid (EV-006). Statements show recurring payments to 9 suppliers, monthly payments to the CPA firm, hourly payments to the IT technician, payments to the three outside processors and the machine tool dealer, and a laptop bought in 2025. No payment appears for a backup service, cyber insurance, a security course, or the AI assistant (EV-007).

**Devices and network.** The laptop has one local account with administrator rights, used for all work. Full-disk encryption, built-in antivirus, automatic updates and the host firewall are on. The CAM software is two releases behind. A shared folder feeds programs to the VMC, the IT technician's remote-support tool is installed with unattended access on, and nothing backs up the laptop except the sync client (EV-008). The phone is encrypted, updates automatically, and receives the suite's MFA codes (EV-009). The router is the internet provider's. It runs one Wi-Fi network with no guest network, the laptop, phone, VMC, alarm panel and several unnamed devices are connected, and the owner holds no record of an admin password change or firmware update (EV-010).

**Bay, machines and programs.** The bay and office doors are keyed and the alarm is monitored. The Wi-Fi password is posted on the office wall, drawings on the bench are in view of the entrance, and no visitor sheet or escort notice is at the door. Travelers and inspection records are in a locked cabinet. Unlabeled USB sticks at the turning center are mixed with personal sticks, and the laptop retired in 2025 sits in the office drawer with used sticks (EV-011). The landlord keeps a master key (EV-012). The VMC controller dates from 2012 and no longer receives software updates, and it keeps no log of edits made at the panel. The turning center takes programs by USB stick only (EV-013). About 180 released OEM programs sit in the Jobs folder, editable from the laptop, with no read-only copy or hash, and the sampled travelers record no controller edits (EV-014).

**Customers and contract terms.** NDAs are signed with all four main customers and SQAs with two OEMs. The third OEM uses PO quality clauses. The terms include 10-year record retention, prior written approval of program changes to released parts, and notice within 5 business days of unauthorized access to OEM confidential information (EV-015). Aerospace POs since 2025-03 flow down FAR 52.204-21 and FAR 52.204-25 and require incident notice within 72 hours (EV-016). The customer's letter of 2026-06-15 requires a Final CMMC Level 1 (Self) status and an SPRS affirmation before the December 2026 award, and states that its drawings carry FCI but no CUI or ITAR-controlled data (EV-017). The aerospace portal enforces MFA on the shop's named account (EV-018). The shop has no SAM.gov registration, CAGE code, or SPRS account (EV-019).

**Documents.** No written security policy, risk assessment, incident plan or contact list, FAR 52.204-21 review, approved external systems list, retention rule, disposal record, emergency access sheet, device list, or training certificate was found (EV-020).

**Contractors, processors and visitors.** POs to the heat treater, anodizer and calibration lab carry no confidentiality or FAR 52.204-21 terms, and no processor has an NDA. Email threads with the anodizer include aerospace drawing attachments and open sharing links (EV-021). The IT technician signed an NDA on 2026-08-07. Earlier invoices include remote sessions on the laptop under no written security terms (EV-022). The bookkeeper works under an engagement letter (EV-023). The machine tool dealer's technician connected his own service laptop to the VMC at the annual service (EV-024). Two OEM supplier audits in the past 12 months included visits to the bay (EV-025).

**Insurance and fraud attempt.** The general liability declarations list no cyber coverage (EV-026). In 2026-05 an OEM received a spoofed request to pay the shop at "new bank details", checked by phone, and paid nothing (EV-027).

**Website and AI tools.** Only the owner's account can publish to the website, which is hosted on the builder's platform (EV-028). The consumer AI assistant account, opened in 2026-03 on a free plan, lists about 40 chats on quotes, emails, GD&T callouts and G-code, and the setting that lets the vendor use chats to improve its models is on (EV-029). The accounting SaaS categorizes transactions automatically (EV-004).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Productivity suite provider's SOC 2 Type 2 report | Productivity suite provider (trust portal) | 2026-08-03 | Received 2026-08-13 (EV-030, intake follow-up); reviewed in P09 |
| Does the general liability policy cover any cyber event? | Insurance agent | 2026-08-04 | Not answered at intake; P08 carries it as an owner action |
| Does the IT technician use MFA on the remote-support tool account? | On-call IT technician | 2026-08-07 | Not confirmed at intake; carried into the P01 risk register (R-007) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Receipts and customer mix (EV-005, EV-006), program storage (EV-013, EV-014), single-person access (EV-001), the suite's retention (EV-002), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-014 |
| P04 Cloud mapping | SaaS components and settings (EV-001 to EV-004, EV-028, EV-029) and provider assurance (EV-030) |
| P01 Risk register | Likelihood inputs from the account, device and network reviews (EV-001, EV-004, EV-008, EV-010), the bay walk-through (EV-011), the program records (EV-013, EV-014), contractor and processor records (EV-021, EV-022, EV-024), the fraud attempt (EV-027) and the AI account (EV-029) |
| P03 Gap analysis | The obligations register (which rules and contract terms apply) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-020): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the suite and accounting accounts (EV-001, EV-004), the laptop and network (EV-008, EV-010), the about 180 released OEM programs (EV-014), and the external systems and processors (EV-021, EV-029) |
| P08 IR runbook | Notice terms from the obligations register (EV-015, EV-016); contacts from the vendor register; insurance status (EV-026) |
| P09 SOC 2 | Vendor assurance on file (EV-030) |
| P10 AI governance | AI tools found (EV-029, EV-004) |
