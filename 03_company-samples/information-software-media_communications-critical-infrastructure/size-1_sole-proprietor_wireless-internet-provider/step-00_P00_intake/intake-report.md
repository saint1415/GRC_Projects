# Intake Report: Cris Santos Company | Communications | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated fixed wireless internet service provider with a home phone add-on, one Florida county) |
| Intake window | 2026-07-13 to 2026-07-17 |
| Collected by | Owner-operator (owner, security lead and privacy lead) |
| Approved | Owner-operator, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before the self-assessment began on 2026-07-20. A one-person ISP has no HR system, asset database or internal audit, so the systems of record are the vendors' admin portals (billing platform, VoIP reseller portal, cloud radio controller, email, accounting), the router and switch configuration, the laptop and phone, bank and card statements, tax files, the signed agreements folder, the company website, the insurance agent's portal, and a walk-through of SITE-1 and the home office. Intake covers the organization, the systems that hold or carry CPNI and subscriber information, the vendors and contractors that touch them, and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (self-reviews, walk-throughs, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Billing platform, customer channels and AI assistant | EV-001 to EV-005 | Billing platform admin settings, tickets and add-on settings; add-on terms | 2026-05-04 to 2026-07-13 |
| Home phone (VoIP) service | EV-006 to EV-008 | VoIP reseller portal; signed agreements folder | 2023-02-15 to 2026-07-14 |
| Network and sites | EV-009 to EV-012 | Cloud radio controller; router and switch configuration and version pages; SITE-1 and home office walk-through | 2026-07-14 to 2026-07-15 |
| Devices, email and accounting | EV-013 to EV-016 | Laptop and phone settings screens; email and file account; accounting SaaS | 2026-07-15 |
| Vendors, contractors and contracts | EV-017 to EV-021 | Signed agreements folder; bank and card statements; tax files and invoices; vendor terms; vendor trust portal | 2026-04-30 to 2026-07-17 |
| Business volume | EV-022 to EV-024 | Billing platform reporting; 2025 Schedule C | 2025-12-31 to 2026-06-30 |
| Customer commitments, documents and insurance | EV-025 to EV-027 | Website and portal captures; search of the owner's files; insurance agent portal | 2026-01-01 to 2026-07-17 |
| AI tools | EV-004, EV-005, EV-028 | Billing platform add-on settings and terms; AI chat service account | 2026-05-04 to 2026-07-16 |

## 3. Observations by area
**Billing platform, customer channels and AI assistant.** The billing platform has one administrator account, the owner's, with MFA on the owner's phone (EV-001). Customer portal passwords are set through a link to the email of record with no account or biographical prompts. Automatic notices go out for portal password changes and not for new online accounts, email of record changes or service address changes. The account screen has no CPNI approval field, and payments are taken on the processor's hosted pages (EV-002). Ticket notes show call detail requests answered by calling back the number of record or by email to the address of record, with no written procedure; no posted outage lasted longer than one day (EV-003). The AI support assistant add-on was turned on on 2026-05-04 with account lookup, home phone call history and ticket skills. On the text line it identifies the sender by account number and service ZIP code, and no review record is attached to the activation (EV-004). Its terms state no training on customer data and 30-day transcript retention by the model provider (EV-005).

**Home phone (VoIP) service.** The VoIP reseller portal holds call detail, line features, 911 registered addresses and porting for 58 lines on 52 accounts. It signs in with a password; MFA is offered and turned off. 911 addresses are typed in at activation with no later confirmation date, and CDRs export as a monthly file (EV-006). The 52 ATAs send signaling and audio unencrypted; the platform offers encryption, which is off (EV-007). The reseller agreement covers 911 routing and lawful intercept support for the VoIP lines and has no security, CPNI confidentiality or breach notice terms (EV-008).

**Network and sites.** The cloud radio controller has the owner's account (MFA on) and a shared installer account used by the tower contractor, unchanged since 2021. It lists 32 access points across 4 sites, the backhaul links and about 310 customer radios, and access points share one local admin password set by template (EV-009). Router web and SSH management are enabled on every interface, including the internet-facing one. Access point management has its own VLAN, the router and switch each have one admin account, and logs are kept in memory only (EV-010). The router runs a release two behind the vendor's current one, a critical vendor advisory applies to it, and the core switch firmware is about 3 years old (EV-011). The SITE-1 shed is locked and alarmed, the tower base is fenced, batteries show about 2 hours of runtime, the generator starts by hand, and a spare router is on the shelf (EV-012).

**Devices, email and accounting.** The laptop has full-disk encryption, automatic updates and antivirus. Its browser stores the VoIP portal and router passwords, the downloads folder holds monthly CDR exports from 2023 onward, and the latest router and switch configuration copy is dated 2026-03-19 (EV-013). The phone is locked and encrypted and holds the second factor for every SaaS account with MFA (EV-014). The business email account uses MFA and holds the same CDR exports as attachments (EV-015). The accounting SaaS has named accounts for the owner and the bookkeeper (EV-016).

**Vendors, contractors and contracts.** The agreements folder holds the reseller agreement, the network consultant's confidentiality and security terms (signed 2026-07-17), the bookkeeper's engagement letter, the site leases, the upstream fiber agreement for one circuit at SITE-1, and the merchant agreement. There is no written agreement with the tower contractor (EV-017). Statements show the recurring vendors and contractors, an AI chat service plan, and no payment for cyber insurance or for a CALEA intercept product or trusted third party (EV-018). A former installer received a 1099 for 2024, and the consultant's invoices list remote sessions on the core router (EV-019). The billing vendor's terms promise incident notice within 72 hours (EV-020). Its SOC 2 Type 2 report covers Security and Availability for the 12 months ending 2026-04-30, states RTO 8 hours and RPO 1 hour, and does not cover the AI add-on. The trust portal shows no earlier download by the company (EV-021).

**Business volume.** About 310 accounts (285 residential, 25 farm and small business), 52 with the home phone add-on, all service addresses in Florida, about 10% of residential accounts with a mailing address in another state; the add-on has been sold since 2023-03-01 (EV-022). About $180,000 billed in 12 months, about $15,000 a month (EV-023). The 2025 Schedule C shows gross receipts of about $180,000 and no wages (EV-024).

**Customer commitments, documents and insurance.** The website and portal carry the terms of service, privacy policy, home phone terms with CPNI and 911 notices, and the broadband consumer labels (EV-025). No written security policy, CPNI or breach procedure, CPNI certification, CALEA policy or designation, incident plan, county 911 center contact, emergency access arrangement, or training record was found, and the general incident log has no entries (EV-026). The general liability declarations list no cyber coverage (EV-027).

**AI tools.** Two were found: the billing platform's AI support assistant (EV-004, EV-005) and a general-purpose AI chat service on an individual plan, whose history holds drafts of customer notices and configuration snippets with no customer data (EV-028).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Written confirmation that customer data is not used for training and of the 30-day transcript retention for the AI add-on | Billing platform vendor | 2026-07-14 | Not answered at intake; carried into P10 as condition 4 (due 2026-10-31) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Account and revenue figures (EV-022 to EV-024), the billing vendor's recovery objectives (EV-021), SITE-1 power (EV-012), the configuration copy date (EV-013), single-person access (EV-014), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-017 |
| P04 Cloud mapping | SaaS components and terms (EV-001 to EV-006, EV-009, EV-015, EV-016) and provider assurance (EV-021) |
| P01 Risk register | Likelihood inputs from the portal, controller and router exports (EV-006, EV-009 to EV-011), the laptop review (EV-013), the agreements and document search (EV-017, EV-026) and the AI assistant settings (EV-004) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document search (EV-026): no prior policy existed to start from |
| P07 Control assessment | Populations to test: the SaaS admin accounts (EV-001, EV-006, EV-009, EV-015, EV-016), the 32 access points and about 310 customer radios (EV-009), the router (EV-010) and the vendors and contractors (EV-017) |
| P08 IR runbook | Notification duties from the obligations register; contacts from the vendor register; insurance status (EV-027) |
| P09 SOC 2 | Vendor assurance on file (EV-021) and the billing vendor's terms (EV-020) |
| P10 AI governance | AI tools found (EV-004, EV-005, EV-028) |
