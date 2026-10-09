# Intake Report: Cris Santos Company | Arts, Entertainment, and Recreation | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (live event venue operator with ticketing, one Florida venue building with two rooms) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Lead), with the Controller and the Director of Ticketing |
| Approved | General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the company's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that hold patron data or carry card data, the suppliers that touch them, both merchant accounts (MID-T and MID-F), and the rules that may bind the company. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, observations, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-010 | Ticketing platform admin console; identity provider; HR and payroll system; IT help desk log; HR files and training records | 2026-06-30 to 2026-07-06 |
| Devices and network | EV-011 to EV-017 | Endpoint and anti-malware consoles; ticketing device list; firewall and Wi-Fi controller; integrator remote support console and tickets; log settings | 2026-06-30 to 2026-07-07 |
| Cloud and backups | EV-018 to EV-020 | Cloud provider console; backup service; provider compliance portal | 2026-03-31 to 2026-07-01 |
| Card payments | EV-021 to EV-031 | Controller's merchant files and contracts; acquirer portal; vendor portals; POS back office; purchase path walk-through; receipts; intake questionnaire | 2024-04-30 to 2026-07-08 |
| Ticketing modules and patrons | EV-032 to EV-034 | Ticketing platform settings and reporting; email marketing service | 2026-06-30 to 2026-07-06 |
| Documents and records | EV-035 to EV-038 | Document request; IT Manager email; company website; insurance files | 2026-07-03 to 2026-07-06 |
| Suppliers and contracts | EV-039 to EV-041 | Accounting system; contracts folder | 2026-06-30 to 2026-07-06 |
| Facilities and disposal | EV-042 to EV-044 | CCTV recorder; door access system; integrator records | 2026-06-30 to 2026-07-02 |
| Business volume | EV-045, EV-046 | Accounting system; show settlement app | 2025-12-31 |
| Email | EV-047, EV-048 | Productivity suite admin console | 2026-07-02 to 2026-07-03 |

## 3. Observations by area
**Users and access.** The ticketing platform has 34 venue user accounts with local passwords. Eleven hold admin, seasonal sellers share one 'boxoffice' login, and 2 marketing agency accounts hold the 'marketing settings' permission with no end date (EV-001). MFA is available on the platform and not enforced; the minimum password length is 8 and no lockout threshold is set; the venue audit log keeps 90 days (EV-002). The nightly export function uses a ticketing API key with full administrator scope, created in 2023, with no rotation recorded and stored in the function's settings (EV-003). The identity provider requires MFA for email, the productivity suite, the cloud console, accounting and the email marketing service, and is not connected to the ticketing platform or the POS (EV-004). HR lists 60 employees and 9 departures from July 2025 to June 2026 (EV-005). Ticketing accounts are created and removed by the box office manager on email request, outside the IT help desk log (EV-006). About 220 event-day workers come from two staffing contractors (EV-007). The 2022 acceptable use form is signed by 49 of 60 employees (EV-008). Training records show card reader tamper awareness for bar leads at hire and nothing else (EV-009). The onboarding checklist includes background checks for box office, cash office and finance hires (EV-010).

**Devices and network.** The endpoint console lists 48 Windows PCs and laptops, including the 6 box office PCs, and 10 tablets. All 48 run signature anti-malware and automatic OS updates. The box office PCs have an email client and web browsers installed, use one shared local sign-in per window, and 2 of them run an OS version whose vendor support ends in 2026-10. No endpoint detection and response agent is installed (EV-011). Anti-malware alerts go to a shared mailbox with no one assigned to read it (EV-012). The 24 ticket scanners can scan offline from a manifest downloaded before doors (EV-013). The firewall has five segments; the box office PCs sit on the corporate segment with the office PCs, guest Wi-Fi is internet only, and both internet links end on the one firewall (EV-014). The corporate wireless passphrase was last changed in 2024 and bridges into the corporate segment (EV-015). The integrator's remote support tool is always on with password-only sign-in (EV-016). No logs are forwarded or reviewed, and the firewall clock is set manually (EV-017).

**Cloud and backups.** The cloud tenant holds the patron marketing database (about 260,000 records, no card data fields), the settlement app, the export function, object storage and the backup vault, all in one account and region. Two named administrators sign in through the identity provider. There is no account-level block on public object storage (EV-018). Daily backups completed from April to June 2026; vault immutability is off and no restore jobs ran (EV-019).

**Card payments.** The acquirer's letter of 2026-05-18 classifies the company as a Visa Level 3 merchant and sets SAQ D for MID-T and SAQ P2PE for MID-F, both due 2026-12-15 (EV-021). For 2025, MID-T was validated with SAQ A (EV-022). The merchant agreement requires notice within 24 hours of a suspected compromise (EV-023). Statements show about 610,000 card transactions a year, about 335,000 of them Visa (EV-024). The ticketing vendor's service provider AOC is dated 2026-02-20, and its responsibility matrix leaves to the company its user accounts, MFA, API keys, and content added through marketing settings (EV-025). Its SOC 2 Type 2 report covers the 12 months ending 2026-03-31 (EV-026). The latest payment partner AOC on file is from 2024, and the 4 box office readers are not part of a validated P2PE solution (EV-027). The POS vendor lists 38 P2PE readers on a PCI-listed solution with manual entry disabled; no inspection records were provided (EV-028). Online purchases go from the company website to vendor-hosted checkout pages (EV-029). Receipts show only the last 4 card digits (EV-030). Phone-order staff write the card number, expiration date and security code on a paper slip when a callback is needed (EV-031).

**Ticketing modules and patrons.** Dynamic pricing was switched on in March 2026 in auto-apply mode for reserved-seat Hall shows, with no per-show floor or ceiling. Bot mitigation and the virtual queue run on high-demand on-sales, the limit of 6 is enforced per account, and the vendor keeps session records 30 days (EV-032). The platform holds about 260,000 patron accounts, about 78% with a Florida billing address, and requires account holders to be 18 or older (EV-033). The email service has about 140,000 subscribers, and sampled campaigns show 'from $39' base prices (EV-034).

**Documents and records.** The only security document returned is the 2022 acceptable use form. The request for policies, an incident response plan, a PCI DSS scope document, network and card data flow diagrams, change procedures, a retention schedule, a service provider list, reader inspection logs, a manual entry procedure and a dynamic pricing review returned none (EV-035). No internal or ASV scans have been run (EV-036). The 2021 privacy notice says no third-party tracking is used on checkout pages, and the FAQ says the ticketing company sets the order processing fee (EV-037). A cyber insurance policy with a breach hotline is in force (EV-038).

**Suppliers and contracts.** Payments in the last 12 months went to the suppliers in the [vendor register](vendor-register.csv) (EV-039). The ticketing services agreement requires PCI DSS compliance and sets no breach notice time; its fee schedule shows that the company sets the order processing fee (EV-040). The marketing agency contract has no security, privacy or data-use terms, and the integrator contract has confidentiality terms only (EV-041).

**Facilities and disposal.** Ninety-six cameras record to one on-premises recorder with 30-day retention and cover the box office, the cash office and all bars; facial recognition is not enabled (EV-042). Badges control the staff doors, the box office and the cash office, and no badge log review is recorded (EV-043). The 2 PCs retired in 2026 have wipe certificates (EV-044).

**Business volume.** FY2025 revenue was $24.0 million, with no gaming revenue (EV-045). The company ran about 260 shows on about 200 event days, and an average Hall show brought in about $95,000 on the night (EV-046).

**Email.** Patron exports were sent as attachments to the agency's email domain (EV-047). Default spam filtering is on, and link and attachment protection is not enabled (EV-048).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Current payment partner AOC | Controller | 2026-07-06 | Not provided at intake; carried into P07 (POAM-019) and P09 |
| Network diagram and card data flow diagram | IT Manager and integrator | 2026-07-02 | None exists; carried into P03 (G-002) |
| Whether the P2PE solution allows offline card acceptance | Food and Beverage Manager | 2026-07-06 | Not established; carried into P05 |
| Whether staff use public AI tools with company data | General Manager | 2026-07-08 | Not established at intake; P10 records it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-005), revenue and show volume (EV-045, EV-046), card volume (EV-024), backup schedule (EV-019), vendor recovery commitments (EV-026), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001 to EV-004, EV-011 to EV-019 and EV-042 to EV-043 |
| P04 Cloud mapping | Cloud and SaaS components (EV-003, EV-018) and provider assurance (EV-020, EV-025, EV-026) |
| P01 Risk register | Likelihood inputs from the configuration exports, the module settings (EV-032), the document request (EV-035) and the contracts |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with PCI DSS v4.0.1 and the FTC rules |
| P06 Policies | The 2022 acceptable use form (EV-008, EV-035) |
| P07 Control assessment | Populations to sample from (EV-001, EV-005, EV-011, EV-028) |
| P08 IR runbook | Notification duties from the obligations register and the merchant agreement (EV-023); contacts from the vendor register |
| P09 SOC 2 | Vendor assurance on file (EV-025, EV-026, EV-027) |
| P10 AI governance | AI modules found (EV-032) and the vendor's system description (EV-026) |
