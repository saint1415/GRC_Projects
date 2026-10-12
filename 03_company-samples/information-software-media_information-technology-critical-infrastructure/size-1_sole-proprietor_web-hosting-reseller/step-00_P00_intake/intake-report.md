# Intake Report: Cris Santos Company | Information Technology | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller; shared hosting, business email, domains and website care plans for about 150 small businesses) |
| Intake window | 2026-08-10 to 2026-08-14 |
| Collected by | Owner (owner, system administrator, support desk, and security and privacy lead) |
| Approved | Owner, 2026-09-28 |

## 1. Purpose and scope
Intake collected the company's own records before the self-assessment began on 2026-08-17. A one-person reseller has no HR system, asset database or internal audit, so the systems of record are the admin pages and reports of the customer portal, the upstream reseller console, the registrar account, the site management dashboard and the website security service, the upstream provider's terms and status page, bank and card statements, the email inbox and file storage, the signed agreements and vendor terms folders, the company website, the laptop and phone, and the insurance broker's quote. Intake covers the organization, the Hosting Control Plane and Customer Portal and the services it depends on, the vendors that touch customer data, the AI tools in use, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (the BIA worksheet, walk-throughs, self-reviews, customer calls, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Control plane tools | EV-001 to EV-008, EV-033 | Portal admin settings and reports; reseller console; upstream terms; registrar account; dashboard; security service | 2026-08-10 to 2026-08-14 |
| Incidents | EV-009, EV-010 | Email inbox; security service findings history; portal ticket history | 2025-03-12 to 2026-08-05 |
| Credentials, email and files | EV-011 to EV-013 | Productivity suite, password manager, payment processor and accounting SaaS admin pages; file storage; sent mail | 2026-08-12 |
| Devices and premises | EV-014 to EV-017 | Laptop and phone settings screens; home office walk-through; trade-in confirmation | 2025-06-20 to 2026-08-12 |
| Customer commitments and statements | EV-018 to EV-020 | Terms of Service; company website; inbox | 2026-08-12 to 2026-08-13 |
| Contracts and vendors | EV-021 to EV-024, EV-026 | Signed agreements folder; vendor terms folder; bank and card statements; payment processor account | 2026-07-31 to 2026-08-13 |
| Business volume and customer data | EV-025, EV-027, EV-031 | Portal billing reports; store CMS user reports; upstream status page | 2026-07-31 to 2026-08-14 |
| Insurance and documents | EV-028 to EV-030 | Broker's email; owner's files; file storage | 2026-08-07 to 2026-08-14 |
| AI tools | EV-007, EV-032 | Security service settings and findings report; consumer chat assistant account | 2026-08-11 to 2026-08-14 |

## 3. Observations by area
**Control plane tools.** The customer portal has one administrator account, the owner's, which signs in with a password only; MFA is available and off. The portal stores the API credentials for the reseller console and the registrar, and its modules can create, suspend and terminate hosting accounts and change nameservers. Customer MFA is optional, and the customer password minimum is 8 characters (EV-001). The portal lists about 150 active customers, about 85% in Florida and the rest in 5 other states, with about 190 portal sign-ins; 9% of customer accounts use MFA, and no customer has a security contact on record (EV-002). The reseller console holds about 270 websites and about 410 mailboxes, uses an authenticator app second factor, and can open any customer's control panel. 18 closed customers' accounts are suspended, not terminated, and 40 older accounts still allow plain FTP (EV-003). The upstream provider runs the servers, operating systems, hosting software, firewall and server-level malware scanning in U.S. data centers. Its nightly backups are kept 7 days with the provider and are deleted with a terminated account, a site can read its hosting account's files including mailbox files, and the program can change on 30 days' notice (EV-004). The registrar account holds about 230 domains on auto-renew with MFA on, and no DNS zone export is kept (EV-005). The dashboard connects 120 sites with administrator-level access. The owner's account has MFA; the freelance developer's administrator account over all 120 sites does not, and the dashboard does not enforce MFA. 35 premium sites have daily off-site backups kept 30 days, and weekly bulk updates go to all 120 sites in one run (EV-006). The security service scans all 270 sites daily and checks uptime every minute. The vendor turned on AI alert triage on 2026-05-04; in July 2026 it auto-dismissed 239 of 412 findings (58%), and uptime reports begin in August 2026 (EV-007). On 2026-08-14 the service flagged 64 hosting-only sites running a plugin with a known vulnerability, and no notice of findings to hosting-only customers appears (EV-008). The four control plane tools record sign-ins and administrative actions; the dashboard keeps 30 days, the portal records nothing for actions taken through its stored API credentials, and no export, review record or sign-in alert is set up (EV-033).

**Incidents.** On 2026-08-05 a customer reported spam pages. The owner found a web shell that the AI triage had auto-dismissed on 2026-07-21, cleaned the site and restored it from the upstream backup. No written record of the data involved or of a breach determination was kept (EV-009). On 2025-03-12 a hosting-only customer's site was defaced through an outdated plugin and restored from the upstream backup (EV-010).

**Credentials, email and files.** MFA is on for the business email, the password manager and the payment processor. The owner's own logins use unique generated passwords, no emergency access contact is set, file storage keeps version history, and the accounting SaaS has two users, the owner and the outside accountant (EV-011). A spreadsheet in file storage lists about 140 customer site administrator and SFTP passwords; passwords set before 2025 follow a pattern (EV-012). Sent mail holds customer and freelancer messages with passwords in the body, and site exports sent as attachments (EV-013).

**Devices and premises.** The laptop has full-disk encryption, automatic updates, built-in antivirus and the host firewall on, is also used for personal purposes, and holds full site backups with store shopper tables in its downloads folder (EV-014). The phone has a passcode and encryption, no remote wipe, and the only authenticator app for every account; recovery codes are not stored offline (EV-015). The business runs from one Florida home office with no paper records or removable media holding customer information (EV-016). The laptop replaced in 2025 was received factory reset with encryption on (EV-017).

**Customer commitments and statements.** The Terms of Service, adapted from a template in 2023, promise 99.9% uptime with a one-month service credit and confidentiality of account information. They have no incident notice clause, do not say who updates hosting-only sites, and do not mention health information (EV-018). The website states "Free daily backups kept for 30 days", "Enterprise-grade malware protection on every site", "Your data never leaves the USA" and "99.9% uptime guarantee", and gives no security contact (EV-019). The two law firms and the property management company sent security questionnaires in 2026. The owner answered them by email without an answer document, stating that MFA is required for all administrative access and that backups are kept 30 days (EV-020).

**Contracts and vendors.** The freelance developer is U.S.-based, works about 8 hours a week, and has an agreement with a confidentiality clause and no security terms (EV-021). The contract security consultant's engagement letter covers the August 2026 tests and a confidentiality agreement, with no standing access (EV-022). Every SaaS vendor is on click-through terms. The dashboard and security service terms do not state where data is stored, the security service terms are silent on model training with site files, and no vendor report or review is on file (EV-023). Statements show one upstream provider and the expected SaaS vendors, the freelancer and the accountant, and no payment for cyber insurance, counsel, training or a backup service (EV-024). The payment processor's merchant agreement requires an annual PCI DSS self-assessment, last attested in February 2026 (EV-026).

**Business volume and customer data.** The portal invoiced about $180,000 in the 12 months to 2026-07-31, about $15,000 a month or about $490 per calendar day, from 120 care plans (35 premium), hosting plans and domain renewals, and no service credit has been issued (EV-025). The 12 online stores hold about 38,000 shopper accounts, about 26,000 with a Florida address; 9 stores, with about 31,000 accounts, are on care plans, and card payments go through each store's own processor (EV-027). The upstream status page shows about 99.86% availability for the company's server cluster over 12 months (EV-031).

**Insurance and documents.** A technology errors and omissions policy with a cyber endorsement was quoted in August 2026; none was bought (EV-028). No written security policy, risk assessment, incident plan, customer security contact list, vendor review, retention rule, restore test record, emergency access or successor arrangement, or breach counsel engagement was found, and there is no security training record (EV-029). The site build checklist covers part of the CMS hardening guide (EV-030).

**AI tools.** The AI alert triage in the security service scores, explains and auto-dismisses findings in every category (EV-007). The owner's free consumer AI chat account holds pasted log excerpts with shopper emails and IP addresses, site files, and one configuration file with a database password; its terms allow use of inputs to improve the service (EV-032).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Where site files, findings and backups are stored, and whether site files are used to train the AI triage | Dashboard vendor and security service vendor | 2026-08-13 | Not answered at intake; carried into P03 (G-039) and POAM-006 |
| Which customers' sites and mailboxes hold Social Security numbers, financial or legal records | The property management company, one law firm and one online store | 2026-08-13 | Answered by phone during P03 fieldwork on 2026-08-18 (EV-037) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue (EV-025), customer and site counts (EV-002, EV-003, EV-006), the uptime promise and credits (EV-018), upstream backups (EV-004), the single authenticator phone (EV-015), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-008, EV-011 to EV-015 and EV-033 |
| P04 Cloud mapping | SaaS components and terms (EV-001, EV-003 to EV-007, EV-023) and the upstream backup and deletion rule (EV-004) |
| P01 Risk register | Likelihood inputs from the control plane exports (EV-001, EV-006, EV-033), the credential reviews (EV-012, EV-013), the vulnerability report and incidents (EV-008 to EV-010), the devices (EV-014, EV-015), the statements and questionnaires (EV-019, EV-020) and the AI records (EV-007, EV-032) |
| P03 Gap analysis | The obligations register (which rules apply), the public statements and contract promises (EV-018 to EV-020), and every observation above, compared with the FTC guidance and Fla. Stat. 501.171 |
| P06 Policies | The document search (EV-029): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the control plane accounts (EV-001, EV-003, EV-005 to EV-007, EV-011), the 270 sites and the 64 flagged hosting-only sites (EV-008), and the 5 vendors that hold customer data (EV-023) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance and counsel status (EV-024, EV-028, EV-029) |
| P09 SOC 2 | Vendor assurance status (EV-004, EV-023) and the customers' questionnaires (EV-020) |
| P10 AI governance | AI tools found (EV-007, EV-032) |
