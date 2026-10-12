# Intake Report: Cris Santos Company | Information | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher; online booking and appointment reminders for small appointment-based businesses) |
| Intake window | 2026-08-17 to 2026-08-21 |
| Collected by | Owner-developer (owner, developer, administrator, and security and privacy lead) |
| Approved | Owner-developer, 2026-09-25 |

## 1. Purpose and scope
Intake collected the company's own records before the self-assessment began on 2026-08-24. A one-person software business has no HR system, asset database or internal audit, so the systems of record are the vendors' consoles and admin pages, the product's own admin console and database reports, the repository and CI service, bank and card statements, the payment processor's reports, the email inbox, the signed agreements and vendor terms folders, the company website, the laptop and phone, and the insurance broker's quote. Intake covers the organization, the Multi-tenant Booking Platform and the services it depends on, the vendors that receive subscriber data, the AI tools in use, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (the BIA worksheet, walk-throughs, self-reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Platform and product | EV-001 to EV-007 | Hosting console; product admin console; framework configuration; database report; booking pages; feature flags | 2026-08-17 to 2026-08-18 |
| Code, monitoring and support | EV-008 to EV-012 | Repository and CI service; error and uptime monitoring; status page; help desk | 2026-08-17 to 2026-08-18 |
| Back office and devices | EV-013 to EV-017 | Back office consoles and password manager; laptop and phone settings; home office walk-through; inbox | 2025-03-18 to 2026-08-19 |
| Contracts and vendors | EV-018 to EV-022 | Website terms; signed agreements folder; sub-processor page; vendor terms folder | 2026-08-20 |
| Business volume | EV-023, EV-024 | Bank and card statements; payment processor dashboard | 2026-07-31 |
| Public statements and questionnaires | EV-025 to EV-028 | Company website; answer document; inbox | 2025-11-30 to 2026-08-20 |
| Assurance, insurance and documents | EV-029 to EV-031 | Hosting provider trust portal; broker's email; owner's files | 2026-03-31 to 2026-08-21 |
| AI tools | EV-007, EV-032, EV-033 | Feature flags and prompt template; model provider console; coding assistant plan terms | 2026-08-18 to 2026-08-21 |

## 3. Observations by area
**Platform and product.** The product runs in one region on a managed application platform, a managed database and one photo storage bucket. Every public endpoint is HTTPS only, and the provider encrypts the database, backups and storage at rest. The database has daily backups kept 7 days and 7-day point-in-time recovery, in the same provider account. Photo storage has versioning off and no copy, and the backup activity shows one backup export in April 2026 and no restore to a separate instance (EV-001). The owner is the only console member, with MFA. One full-scope hosting API token, created in 2024 with no expiry and never rotated, is used by CI; the database password and the messaging and model API keys have not been rotated. The audit log keeps 30 days, with no export or alert (EV-002). The product's admin console has one super-admin account, signs in with a password only, can open and export any subscriber account, and keeps no record of actions; the owner states that the support contractor uses this account (EV-003). Subscriber passwords are salted and hashed with an 8-character minimum, subscriber staff have no MFA option, and sign-in is rate limited at 10 failed attempts per account per 15 minutes (EV-004). The database holds about 240 active subscribers in 11 states, about 520 staff accounts and about 88,000 end-client records (about 61,000 in Florida), plus the records and photos of 31 closed accounts (EV-005). Booking pages collect contact details, a home address only for home services, pet names and optional photos, and no government ID, card or health fields (EV-006). Smart Replies went to 30 opt-in beta subscribers on 2026-06-15; 6 have auto-send on, and the prompt carries the client's full service notes (EV-007).

**Code, monitoring and support.** The owner is the only member of the private product repository and the public demo repository, with MFA. CI deploys with the hosting token stored as a CI secret. Secret scanning and push protection are off, dependency alerts are on with no triage notes, about 1,100 tests run on every push with none covering tenant isolation, authorization, export or deletion, and the framework is updated about monthly (EV-008). Error events include some client names and phone numbers and are kept 90 days, with scrubbing off (EV-009). Measured availability was 99.82% over the 12 months ending 2026-08-17 (EV-010). The 14-hour outage on 2026-03-11 after a failed migration is the only major outage in that period, and 3 subscribers cancelled because of it, about $2,300 a year of revenue (EV-011). The help desk has named accounts for the owner and the support contractor, with MFA available and not enforced (EV-012).

**Back office and devices.** MFA is on for the email and file suite, the password manager and the payment processor. The password manager shows a unique password for every login and no emergency access contact, and the accounting SaaS has two users, the owner and the CPA firm (EV-013). The laptop has full-disk encryption, automatic updates, antivirus and the firewall on, and is also used for personal purposes. Its project folder holds a plaintext `.env` file with the production secrets, and its development database holds a full copy of production data restored in April 2026 (EV-014). The phone is encrypted and holds the only authenticator for every account, with no second device, hardware key or offline recovery codes (EV-015). The home office in Florida is the only premises, with no paper or removable media holding client data (EV-016). The previous laptop was traded in factory reset on 2025-03-18 (EV-017).

**Contracts and vendors.** The click-through Terms of Service and DPA promise use only to provide the service, incident notice within 72 hours of confirmation, a public sub-processor list with 14 days' notice of changes, deletion within 30 days after closure, and export on request. They state no uptime service level (EV-018). Two larger subscribers signed negotiated DPAs with 48-hour notice and an annual questionnaire (EV-019). The public sub-processor list names five providers and not the AI model provider (EV-020). The hosting provider and the email service have DPAs. The other providers are on standard online terms, and the AI model provider on its standard API terms with no DPA (EV-021). The support contractor's agreement has a confidentiality clause and no security terms, and the consultant works under a nondisclosure agreement with no standing access (EV-022).

**Business volume.** Statements show recurring payments to 11 service providers and the coding assistant plan, monthly payments to the support contractor, payments to the CPA firm, and no payment for cyber insurance, counsel or training (EV-023). The payment processor billed about $180,000 in the 12 months to 2026-07-31, about $15,000 a month, from about 240 subscriptions (EV-024).

**Public statements and questionnaires.** The website security page states "bank-level 256-bit encryption", "automatic backups every day", "we never share your data with third parties" and "99.9% uptime". The Smart Replies release note states "your data is never used to train AI", and the site has no security contact or disclosure page (EV-025). The questionnaire answer document says every administrator has an individual account with MFA and that a SOC 2 report is planned (EV-026). About 6 questionnaires arrived in the last 12 months, and both negotiated-DPA subscribers asked for a SOC 2 report (EV-027). Export requests were answered by emailing CSV files, and no sub-processor change notice was sent in 2026 (EV-028).

**Assurance, insurance and documents.** The hosting provider's SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-03-31, lists complementary user entity controls, and notes one remediated exception (EV-029). A technology errors and omissions policy with a cyber endorsement was quoted on 2026-07-14 and not bought (EV-030). No written security policy, risk assessment, incident plan, contact list, restore steps, retention schedule, data inventory, vendor review, training certificate or counsel engagement was found (EV-031).

**AI tools.** Smart Replies is the one AI feature in the product (EV-007). The model provider account was opened in June 2026 on standard terms, with requests from 2026-06-15 and no DPA or signed terms (EV-032). The owner also uses a paid AI coding assistant whose plan terms say inputs are not used for training (EV-033).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| A DPA with no-training and retention terms, and written confirmation of the account's training setting | AI model provider | 2026-08-21 | Not answered at intake; carried into the P01 risk register (R-009) |
| Which device and network the support contractor uses to reach the admin console | Freelance support contractor | 2026-08-20 | Not answered at intake; covered in the P07 contractor interview on 2026-08-26 (EV-AC-6(5)) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue and subscriber counts (EV-024, EV-005), the March 2026 outage and cancellations (EV-011), backup settings (EV-001), the single authenticator phone (EV-015), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-015 |
| P04 Cloud mapping | PaaS and SaaS components and terms (EV-001, EV-002, EV-008, EV-021) and provider assurance (EV-029) |
| P01 Risk register | Likelihood inputs from the account, laptop and phone reviews (EV-002, EV-014, EV-015), the uptime and outage history (EV-010, EV-011), vendor records (EV-020, EV-021) and the Smart Replies settings (EV-007) |
| P03 Gap analysis | The obligations register (which rules apply), the public statements and contract promises (EV-018 to EV-020, EV-025, EV-026), and every observation above, compared with the FTC guidance |
| P06 Policies | The document search (EV-031): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the administrator accounts (EV-002, EV-003, EV-008, EV-013), the 2 devices (EV-014, EV-015), and the 6 service providers that receive subscriber data (EV-020, EV-021) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-023, EV-030) |
| P09 SOC 2 | The hosting provider's SOC 2 report (EV-029) and the subscribers' SOC 2 requests (EV-027) |
| P10 AI governance | AI tools found (EV-007, EV-032, EV-033) |
