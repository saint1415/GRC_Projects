# Intake Report: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings, one Florida home office) |
| Intake window | 2026-07-06 to 2026-07-10 |
| Collected by | Owner (system owner, security lead and CMMC Affirming Official) |
| Approved | Owner, 2026-08-31 |

## 1. Purpose and scope
Intake collected the business's own records before the self-assessment began on 2026-07-13. A one-person business has no HR system, asset database or internal audit, so the systems of record are the SaaS admin consoles, the Prime A portal and contract file, SPRS and SAM.gov, bank and card statements, the email inbox, the signed agreements folder, the laptop and phone settings screens, the internet service provider's account app, and the insurance agent's portal. Intake covers the organization, the systems that process, store or transmit CUI and FCI, the suppliers that touch them, and the rules that may bind the business. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Contract, customer and federal records | EV-001 to EV-008 | Signed agreements folder; inbox; SPRS; SAM.gov; owner's files; Prime A portal | 2025-05-20 to 2026-07-07 |
| Cloud services | EV-009 to EV-011 | Productivity suite admin console, terms and storage | 2026-07-07 |
| Devices, network and home office | EV-012 to EV-016 | Laptop and phone settings screens; backup tool; internet service provider account app; home office photos | 2026-07-08 |
| Accounting and business volume | EV-017 to EV-019 | Accounting SaaS; tax files | 2025-12-31 to 2026-07-09 |
| Suppliers and agreements | EV-020 to EV-023 | Bank and card statements; inbox; CAD vendor portal; signed agreements folder | 2026-06-30 to 2026-07-09 |
| Documents, insurance and customer requests | EV-024 to EV-026 | Owner's files; insurance agent portal; inbox | 2026-01-01 to 2026-07-09 |
| AI tools | EV-020, EV-027 | Card statements; chatbot account page | 2026-06-30 to 2026-07-09 |

## 3. Observations by area
**Contract, customer and federal records.** The Prime A master purchase order was awarded 2025-06-02 for two years. It lists DFARS 252.204-7012, 252.204-7019 and 252.204-7020, FAR 52.204-21 and FAR 52.204-25, does not list DFARS 252.204-7021, and pays invoices in 30 days (EV-001). Prime A's notice of 2026-06-15 says the follow-on subcontract will require CMMC Level 2 (Self) (EV-002). SPRS holds one Basic Assessment score of 110 dated 2025-05-20 and no CMMC status (EV-003). The SAM.gov registration is active, with a CAGE code assigned in 2025-04 (EV-004). The 2025 SSP is a generic template that names none of the owner's systems, and the score worksheet marks all 110 requirements implemented with no evidence attached (EV-005). Prime A verified the owner's U.S. citizenship at onboarding (EV-006). The Prime A portal requires a password and an authenticator app code (EV-007). The owner completed Prime A's 30-minute supplier cybersecurity briefing in 2025 (EV-008).

**Cloud services.** The productivity suite is a commercial business plan with 1 user. MFA with an authenticator app is on, browser sessions stay signed in for 90 days, audit records are kept 180 days with no saved searches or exports, and files have 30-day version history (EV-009). The plan terms do not mention FedRAMP or DFARS 252.204-7012, and the provider manages the keys (EV-010). The synced CUI project folder holds about 320 files marked CUI, some with an ITAR warning, and the same folder holds a password spreadsheet and the laptop disk recovery key (EV-011).

**Devices, network and home office.** On the laptop, full-disk encryption, real-time antivirus, the host firewall and automatic updates are on. The screen locks after 5 minutes, no lockout threshold is set, and the owner's daily account is an administrator. No record of the encryption module's FIPS validation was found (EV-012). The phone is encrypted and locked by passcode and biometric, holds the authenticator app, opens CUI attachments in its email app, and backs up to a personal cloud account (EV-013). A weekly full backup goes to a USB drive with the encryption option not selected, and the drive sits in an unlocked drawer (EV-014). One WPA2 Wi-Fi network with one passphrase serves the laptop, the printer, household devices, guests and a smart TV. The router firmware was last updated in 2024 (EV-015). The office door locks and a cross-cut shredder stands next to the printer. No visitor log is kept, and household members and the cleaning service enter when the door is unlocked (EV-016).

**Accounting and business volume.** The accounting SaaS signs in with a password only (MFA available and off) and holds client and billing records, Prime A task orders and invoices: about 14 task orders in the last 12 months (EV-017). 2025 revenue was about $180,000, about 70% from Prime A (EV-018), and the Schedule C shows no wages paid (EV-019).

**Suppliers and agreements.** The statements show payments to 8 recurring suppliers plus the IT consultant by the hour and the accountant once a year, and no payment for cyber insurance, a vulnerability scanner, a password manager or a medium assurance certificate (EV-020). The IT consultant's invoices list on-site visits only, including setup of the current laptop in 2025-05 (EV-021). The CAD licenses are node-locked to the laptop, and the installed release is two releases behind the current one (EV-022). Commercial customers' drawings are held under nondisclosure agreements, and the commercial aerospace agreements carry an EAR export-control clause (EV-023).

**Documents, insurance and customer requests.** Apart from the 2025 template, no security policy, incident plan or contact list, contingency plan, baseline, change log, visitor log, log review record, scan report, sanitization record or other training certificate was found, and there is no medium assurance certificate (EV-024). The professional liability declarations do not say whether cyber events are covered (EV-025). A commercial customer sent a security questionnaire on 2026-07-07 (EV-026).

**AI tools.** The card statements show a monthly individual plan for a commercial generative AI chatbot (EV-020). The account page shows 1 user and the model training control on, and the owner states it is used for report drafting and engineering questions. No approved-tools list exists (EV-027).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Does the professional liability policy cover cyber events? | Insurance agent | 2026-07-09 | Not answered at intake; P08 carries it as an owner action |
| What content has been entered into the AI chatbot? | Owner (review of the conversation history) | 2026-07-09 | Not established at intake; reviewed in P03 fieldwork on 2026-07-16 (EV-032) |
| Is the encryption module on the laptop FIPS-validated, and in which mode? | Owner (laptop vendor documentation) | 2026-07-08 | Not established at intake; tested in P07 (EV-SC-13) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and its split (EV-018, EV-019), payment terms (EV-001), CAD licenses (EV-022), version history and backups (EV-009, EV-014), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-007, EV-009 to EV-017; the 2025 template (EV-005) |
| P04 Cloud mapping | SaaS components and terms (EV-009, EV-010, EV-017, EV-020) |
| P01 Risk register | Likelihood inputs from the account, device and network reviews (EV-009 to EV-015), the SPRS record and template (EV-003, EV-005) and the contract notice (EV-002) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with NIST SP 800-171 Rev. 2 and the clauses |
| P06 Policies | The document search (EV-005, EV-024): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the SaaS services (EV-009, EV-017, EV-020, EV-027), the laptop, phone, backup drive, router and printer (EV-012 to EV-015) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-025) |
| P09 SOC 2 | The customer questionnaire (EV-026) |
| P10 AI governance | AI tools found (EV-020, EV-027) |
