# Scenario facts: Cris Santos Company | Financial Services | Micro

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a card brand rule, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (a merchant services provider operating as an independent sales organization, or ISO) |
| Business | Merchant services provider (NAICS 522320). It signs up, boards, equips, and supports small merchants for one card processor (the "processor partner") and that processor's sponsor bank. It does not authorize, clear, or settle transactions itself: the processor partner does. The company earns residuals (a share of the processing fees) and terminal rental fees |
| What it does for merchants | Sales and underwriting packets; terminal deployment and swaps; merchant help desk; administration of its merchants' accounts on the processor partner's white-label payment gateway (users, hosted payment page settings, fraud filter settings); a **backup keyed-entry service**: when a merchant's terminal fails, a support specialist takes the card details by phone and keys the sale into the merchant's virtual terminal |
| Location | Florida. One office suite. Staff can work from home on company laptops. About 92% of merchants are in Florida; the rest are in Georgia, Alabama, and six other states. State law is handled generically ("each state where affected individuals reside") with Florida as the worked example |
| Workforce | 7 employees (see section 2). Also 6 independent outside sales agents (contractors, not employees) who solicit merchants in the company's name |
| Size | About $1.1 million in annual receipts (fictional), about $4,400 per business day. SBA-small (standard $47.0 million for NAICS 522320) |
| Merchant portfolio | About 850 active merchants (restaurants, retail, salons, auto repair, professional services). About 120 sell online through the gateway's hosted payment page and about 300 use the gateway's virtual terminal. The processor partner processes about 3.4 million card transactions (about $310 million) a year for these merchants |
| Keyed-entry volume | About 1,900 keyed transactions in the 12 months to June 2026, all keyed by company staff into merchants' virtual terminals |
| ISO agreement | Three-party agreement with the processor partner and its sponsor bank (an OCC-supervised national bank), renewed 2025-01-01. It requires: PCI DSS validation every year (SAQ D for Service Providers and an Attestation of Compliance, by October 30) and passing quarterly ASV scans; notice to the processor partner and sponsor bank of any suspected compromise of card data or merchant accounts **immediately and no later than 24 hours**; and indemnity for card brand assessments caused by the company. The sponsor bank registers the company with the card brands |
| Card brand registration | Registered by the sponsor bank in Visa's Third Party Agent program as an ISO (merchant solicitation, sales, and service). Visa states that agents that "perform solicitation activities (ISO) ... or store, process, transmit, or have access to Visa cardholder data must be registered in the TPA Registration Program" (Visa Account Information Security page, checked 2026-10-06). Other brands' registrations are handled by the sponsor bank and were not verified here |
| PCI DSS status | **Service provider** under PCI DSS v4.0.1: it transmits card data (keyed entry) and controls settings that can affect the security of its merchants' card data (gateway administration). **Level 2** under Visa's service provider levels (fewer than 300,000 Visa transactions a year): annual Self-Assessment Questionnaire, quarterly ASV scan, and Attestation of Compliance. Validates with **SAQ D for Service Providers**. Last SAQ and AOC: "Compliant", signed by the Owner on 2025-10-15. That SAQ described the scope as "the gateway reseller console only" and left out the laptops, office network, and phone system used for keyed entry (EV-033). Status decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (PCI-DSS) |
| GLBA status | Treated as a **financial institution** under the FTC Safeguards Rule, 16 CFR Part 314, because it provides data processing and transmission of financial data for merchants (12 CFR 225.28(b)(14), incorporated by 314.1(b)). It maintains customer information concerning **fewer than 5,000 consumers**, so the 314.6 exception applies: 314.4(b)(1), (d)(2), (h), and (i) do not apply. 314.4(j) (FTC notice) still applies. Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (FTC-314, FTC-314.4(j)) |
| Bank service provider status | **Not** a bank service provider under 12 CFR 53.2(b)(2) on the company's analysis: it performs no services for the sponsor bank that are subject to the Bank Service Company Act; its services go to merchants and the processor partner. Written confirmation requested from the sponsor bank (see P03). Recorded in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-FINANCIAL-R01) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): NYDFS 23 NYCRR Part 500 (no New York license); SEC Regulation SCI and Form 8-K (not an SCI entity or SEC registrant); NCUA 12 CFR 748.1(c) (not a credit union); Interagency Guidelines 12 CFR 30 App. B (bind the sponsor bank, reach the company only through the ISO agreement); PIN key management (terminals arrive already injected by the processor partner's key injection facility) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (breach notification, Fla. Stat. 501.171; call recording consent, Fla. Stat. 934.03). For merchant owner data the company is the covered entity; for card data it handles for merchants it is usually a third-party agent |

**Driver labels used in this folder.** The vertical requirement IDs (C-FINANCIAL-R01 to R06) are used where they apply or where a row records why they do not. PCI DSS and the FTC Safeguards Rule are not in the vertical requirements list, so rows cite them directly: "PCI DSS 8.4.2" (requirement number in PCI DSS v4.0.1) and "16 CFR 314.4(c)(5)".

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Owner (managing member) | Accepts Moderate risk; approves policies, spending, and High-risk treatment plans; signs the SAQ D and AOC; holds executive responsibility for PCI DSS (12.4.1) |
| Operations Manager | **Qualified Individual** under 16 CFR 314.4(a) and day-to-day security and PCI DSS lead, combined with office management, HR, and vendor management. Not designated in writing before 2026-08-31 (EV-035; EV-059) |
| Merchant Support Lead | Help desk lead; keyed-entry service; merchant user administration in the gateway console |
| Merchant Support Specialist | Help desk; keyed-entry service |
| Onboarding and Risk Specialist | Merchant applications and underwriting packets; merchant risk monitoring; gateway fraud filter settings (business owner of AI-001 in P10) |
| Terminal and Integration Technician | Terminal deployment and swaps; spare terminal inventory; e-commerce integrations and hosted payment page settings |
| Sales and Agent Manager | Direct sales; manages the 6 outside sales agents and their access |
| Managed service provider (MSP) | IT support, laptops, patching, antivirus, firewall, Wi-Fi, productivity suite administration, suite backup. Contract has no security incident terms (EV-027) |
| Outside sales agents (6 contractors) | Solicit merchants and collect applications in the company's name. CRM accounts; "sales" role in the gateway console (view merchant status only) |
| Freelance web developer | Built the website and application intake form in 2023; holds the only administrator login to the web hosting account (EV-023) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Card data or NPI? | Notes |
|---|---|---|---|---|
| SYS-01 | Gateway reseller console (the processor partner's white-label payment gateway, company-branded) | Vendor SaaS (processor partner) | **Card data (keyed entry); masked PAN in reports** | 6 company user accounts. Console can create merchant users, reset merchant passwords, "log in as merchant" to the merchant's virtual terminal (sales and refunds), edit hosted payment page settings including a custom header field that accepts HTML and script, set fraud filter thresholds, and export reports (first six and last four digits). MFA is available but optional: 2 of 6 accounts enrolled (EV-003; EV-004; EV-005) |
| SYS-02 | Processor partner portal | Vendor SaaS (processor partner) | Merchant owner NPI | Boarding submissions, residual reports, chargeback cases, merchant change requests (including deposit bank account changes). MFA enforced by the processor partner (EV-007; EV-008) |
| SYS-03 | CRM and merchant document store | Vendor SaaS | **Merchant owner NPI** | About 1,250 merchant files (850 active, about 400 declined or closed): applications, owner Social Security numbers, dates of birth, driver's license images, voided checks. MFA enforced since 2025. Vendor SOC 2 Type 2 report available (EV-010; EV-029) |
| SYS-04 | Productivity suite (email, files, chat) | SaaS | NPI (in attachments and exports) | Outside agents email merchant applications as unencrypted attachments; a monthly CRM export sits in the shared drive. MFA by push approval (EV-011; EV-012) |
| SYS-05 | Cloud phone system with call recording | Vendor SaaS | **Spoken card data in recordings (EV-056)** | 5 user seats plus one shared "support" administrator login. All support calls recorded since go-live on 2025-05-12. Inbound calls play a recording announcement; outbound calls do not (EV-013) |
| SYS-06 | Laptops | MSP-managed | Card data in transit (keyed entry) | 9 laptops (7 in use, 2 spares). Full-disk encryption, antivirus, MSP patching. No EDR. Keyed entry is done on the two support laptops, at the office or at home (EV-015 to EV-019; EV-043) |
| SYS-07 | Office network | On-premises, MSP-managed | Card data in transit | Small-business firewall, staff Wi-Fi (shared password unchanged since 2023), separate guest Wi-Fi, one business internet line. No separate segment for keyed entry (EV-020; EV-051) |
| SYS-08 | Website and merchant application intake | Cloud workload: managed cloud web hosting (one virtual server) plus a cloud object storage bucket for uploads | **Merchant owner NPI** | Online "apply now" form; uploads (applications, IDs, voided checks) go to the bucket. About 610 files since 2023, never deleted. The form plugin is two major versions out of date. The bucket access key sits in the website configuration file with full rights (EV-023; EV-055) |
| SYS-09 | Spare payment terminals (POI devices) | Office, locked cabinet | Keys injected by the processor partner | About 40 spare terminals for swaps. Inventory is a spreadsheet, last reconciled in 2025. Returned terminals are not inspected for tampering before redeployment (EV-024; EV-043) |
| SYS-10 | Suite backup | SaaS, operated by the MSP | Copies of SYS-04 data | Daily backup of email and files with 1 year of retention. CRM data relies on the CRM vendor's own backups plus the monthly export (EV-021; EV-029) |
| External | Processor partner (gateway, portal, authorization, settlement); sponsor bank; CRM vendor; phone vendor; suite vendor; web hosting and storage provider; MSP; ASV; e-signature service; payroll service; cyber insurer | | | |

**SSP system (P02):** the *Merchant Payments Platform (MPP)*: SYS-01 to SYS-10, the systems the company uses or administers to board, equip, and support merchants, including the keyed-entry path (SYS-01, SYS-05, SYS-06, SYS-07) that PCI DSS brings into scope.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). For a 7-person ISO the systems of record are the processor partner's console and portal, the SaaS admin consoles, the payroll service, the MSP's exports and monthly report, the contracts folders, the card statements, the ASV portal, and a walk-through. Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS and the FTC Safeguards Rule** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P08 incident | Compromise of the payment processing environment, at the scale the company touches it: a phishing email captures a support specialist's gateway console password (no MFA). The attacker uses "log in as merchant" to push refunds to prepaid cards and inserts a skimming script into the hosted payment page custom header of e-commerce merchants. The MSP, the cyber insurer, the processor partner, and the sponsor bank are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality. The readiness self-assessment answers the processor partner's annual ISO risk review questionnaire and a merchant association's vendor questionnaire; PCI DSS stays the main assurance for card data. Part B is a review of the CRM vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: the gateway's machine-learning fraud-scoring filter, which the company configures (thresholds and actions) for its 120 e-commerce merchants. The registry default "transaction fraud-detection model" is kept but adapted: at this size the company does not build or host a model; it configures a vendor's model for its merchants. AI-002: staff use of public generative AI chatbots |
| Primary system | The registry default "payment processing platform (cardholder data environment)" is adapted to the Merchant Payments Platform: the company does not run a processing platform, but its gateway administration and keyed-entry path are the part of the payment environment it controls |
| Cloud | SaaS plus one cloud workload: the website and application intake (SYS-08). Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2025-05-12 | Cloud phone system with call recording goes live |
| 2025-10-15 | 2025 SAQ D for Service Providers and AOC signed by the Owner |
| 2026-02-13 | Contract with one outside sales agent ends |
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports from the processor partner's console and portal, the SaaS consoles, the payroll service and the MSP, the contracts folders, a walk-through, inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis (Operations Manager with the MSP lead technician) |
| 2026-07-27 to 2026-07-31 | Policies drafted from the gaps |
| 2026-08-03 to 2026-08-05 | Control assessment (independent consultant): operating tests of controls already in place; design review of the draft policies |
| 2026-08-31 | Deliverables and policies approved by the Owner |
| 2026-10-30 | 2026 SAQ D for Service Providers and AOC due to the processor partner |
| 2027-02 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables

These facts were added because the deliverables needed them. They do not change sections 1 to 6. Facts drawn from the company's records cite the evidence register ID they rest on.

| Topic | Added fact | Used in |
|---|---|---|
| Former agent accounts | Found active on 2026-07-15 during the risk assessment, 5 months after the contract ended on 2026-02-13, and disabled that day. The console and CRM sign-in logs showed no use after 2026-02-13 (EV-049) | P01, P03, P07 |
| Card data in recordings | Found on 2026-07-21 during the gap analysis. Recording of the support queue was paused on 2026-07-22. After counsel's review, the recordings with card data were deleted on 2026-08-14 and the phone vendor confirmed deletion in writing on 2026-08-17 (EV-056; EV-058). The notice analysis is in P08 section 6.5 | P01, P03, P07, P08 |
| Disclosure to the processor partner | On 2026-08-20 the Owner told the processor partner's partner risk team that the 2025 SAQ left out the keyed-entry path. The processor partner asked for an accurate 2026 SAQ and a remediation plan by 2026-10-30 | P01, P03 |
| Unapproved scripts | P07 testing on 2026-08-04 found that the custom header field of 2 e-commerce merchants' hosted payment pages carries third-party analytics scripts that the Terminal and Integration Technician added at the merchants' request in 2025, with no approval, inventory, or integrity check (EV-CM-8) | P01, P03, P07 |
| Deposit account change requests | Support staff submit merchant deposit bank account changes in the processor partner portal on the strength of a phone call or email, with no call-back to a number on file. In March 2026 a caller posing as a salon owner asked for a change; the request was stopped only because the processor partner asked for a signed form (EV-008; EV-043) | P01, P03, P06 |
| MSP contract | Covers help desk, patching, antivirus, firewall, Wi-Fi, suite administration, and backup, with a 4-business-hour response time. No security incident notice, no named technicians, no evidence of MFA on the MSP's remote management tool (EV-027; EV-048) | P01, P05, P07 |
| Cyber insurance | Policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics). Requires prompt notice and use of panel vendors (EV-032) | P08 |
| Office security | Keyed suite entry with an after-hours alarm; keys held by the Owner and Operations Manager. No visitor log (EV-044; EV-052) | P03 |
| Internet and remote work | One business internet line with no failover. All staff can work from home on company laptops; the phone system runs in a browser or mobile app (EV-020; EV-043) | P05 |
| Finances | A cash reserve covers about 45 days of expenses. Residuals arrive monthly from the processor partner. Payroll runs biweekly through an outside payroll service (EV-042; EV-009; EV-001) | P05 |
| Assessor | The P07 assessor is an independent security consultant with PCI DSS experience, not involved in the risk assessment or the gap analysis and operating no control | P07 |
| Merchant association questionnaire | A regional restaurant association that refers members to the company sent a vendor security questionnaire in July 2026, due 2026-09-30 (EV-041) | P09 |
| Business volumes | The help desk takes about 15 merchant calls a day; about 160 keyed sales a month; about 25 new merchants and 40 disputes a month. Each merchant is worth about $1,300 a year in residuals (EV-014; EV-005; EV-009) | P05 |
| Processor partner assurance | The processor partner provides a PCI DSS AOC as a Level 1 service provider (dated 2026-03) and no SOC 2 report. Console audit logs are kept 13 months (EV-026; EV-004) | P02, P05, P09 |
| Remote support | The Terminal and Integration Technician helps merchants set up gateway plugins through a remote support tool that uses a one-time code the merchant generates for each session (EV-054) | P03 |
| Cardholder count | The deleted recordings held card data for about 1,700 distinct cardholders; this count supports the 314.6 exception (EV-056) | P03 |
| Sponsor bank question | On 2026-08-24 the Owner asked the sponsor bank in writing to confirm that no company service is a covered service under 12 CFR 53 | P03, P08 |
| Recordings notice analysis | Completed by the Operations Manager with the insurer's panel counsel on 2026-08-12: not a notification event (P08 section 6.5) | P08 |
| Assessment findings | P07 found a spare terminal count of 41 against 44 on the spreadsheet (3 units shipped in 2025 swaps without an update), 2 spare laptops unpatched since March 2026, 212 emails with merchant owner Social Security numbers in attachments, and a backup console administered with one MSP account without MFA. The 2 unapproved payment page scripts were removed on 2026-08-12 with the merchants' agreement (EV-CM-8; EV-SI-2; EV-SC-28; EV-CP-9) | P01, P07 |
| Fraud filter | Defaults set by the company in 2024: automatic decline at score 80 and above, merchant review 60 to 79. 104 of 120 merchants use the defaults. A sales brochure claimed the filter "stops 99% of fraud"; withdrawn 2026-08-25 (EV-006; EV-046) | P10 |
| CRM AI assistant | The CRM vendor switched on a generative AI writing assistant by default in June 2026; the company switched it off on 2026-08-25 pending the vendor's data use terms (EV-010) | P10 |
| CRM vendor report | SOC 2 Type 2 (Security, Availability, Confidentiality), period ending 2026-03-31, reviewed 2026-08-21; states RTO 8 h and RPO 1 h (EV-029) | P05, P09 |
| 2026 budget | About $3,900 one-time and $5,700 a year approved by the Owner on 2026-08-31 (P01 section 4) | P01 |
