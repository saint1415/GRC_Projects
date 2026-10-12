# Intake Report: Cris Santos Company | Accommodation and Food Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel with restaurant and bars, Florida Gulf Coast) |
| Intake window | 2026-06-29 to 2026-07-10 |
| Collected by | IT Manager (Information Security Lead), with the Controller |
| Approved | General Manager, 2026-08-31 |

## 1. Purpose and scope
Intake collected the hotel's own records before any assessment work began on 2026-07-13. It covers the organization, the systems that store, process or transmit card data and guest personal information, the suppliers that touch them, and the rules that may bind the hotel. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (interviews, walkthroughs, scans, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Users and access | EV-001 to EV-008 | Identity provider; timekeeping and payroll system; HR files; PMS admin console; MSP and lock vendor remote tools | 2026-06-30 to 2026-07-06 |
| Devices and network | EV-009 to EV-018 | MSP console; anti-malware console; MSP network documentation; Wi-Fi vendor; logging settings; productivity suite admin console; lock vendor portal; gateway and P2PE portals; receipts; CCTV and time clock settings | 2026-07-01 to 2026-07-08 |
| Cloud and backups | EV-019 to EV-021 | Cloud provider console; backup service; provider compliance portal | 2026-06-30 to 2026-07-06 |
| Documents and records | EV-022 to EV-031 | Document request list; Chief Engineer's and HR files; MSP contract and tickets; General Manager's files; intake interviews; key list; shredding certificates; insurance file | 2026-06-01 to 2026-07-08 |
| Payments and merchant accounts | EV-032 to EV-036 | Controller's PCI folder and contracts; acquirer merchant portal; service provider attestation file | 2026-05-20 to 2026-07-06 |
| Suppliers and contracts | EV-037 to EV-040 | Accounting system; contracts folder; PMS vendor portal; web agency documents | 2026-03-31 to 2026-07-06 |
| AI tools and pricing | EV-041 to EV-044 | Revenue-management, chatbot and booking engine consoles; identity provider app list and license report | 2026-07-07 to 2026-07-08 |
| Business volume | EV-045, EV-046 | Accounting system; PMS reporting | 2025-12-31 to 2026-06-30 |

## 3. Observations by area
**Users and access.** The identity provider lists 60 active named staff accounts and 2 cloud administrators with standing access (EV-001). Conditional access requires MFA for email, the cloud console and PMS administrator sign-in. Non-administrator PMS users are not federated and sign in with a PMS password only (EV-002). HR lists 60 employees and the terminations from January to June 2026; about 45 room attendants and valet staff come from the staffing company (EV-003). At termination HR emails the Front Office Manager and IT, and the checklist has no PMS removal step. Background checks cover managers and front office hires, and the reports are filed in HR with no disposal procedure (EV-004). The handbook has no section on information security (EV-005). The PMS has 22 front office and reservations users; 14 hold the "view full card number" permission, and the night audit uses one shared account (EV-006). The PMS user activity report has never been run, and the PMS-to-lock and POS-to-PMS interface credentials show no change since installation (EV-007). The MSP and lock vendor remote tools are always on, with no MFA and no source address restriction (EV-008).

**Devices and network.** The MSP console lists 34 Windows PCs and laptops, 5 POS stations and 12 staff tablets. PCs are patched monthly and run anti-malware; the lock server is outside the patch policy, and no endpoint detection and response agent is installed. Two front desk PCs share one Windows login and are excluded from the screen lock policy. The MSP asset list does not hold the front desk terminals, P2PE devices or lock system (EV-009). Anti-malware alerts go to an MSP mailbox with no recorded follow-up, and the lock server has no agent (EV-010). One staff network holds the front desk PCs and terminals, back office PCs, the lock server and the CCTV recorder. The firewall blocks unsolicited inbound traffic and allows all outbound traffic. Staff Wi-Fi joins the same network with a passphrase last changed in 2021, and there is one internet provider (EV-011). Guest Wi-Fi and TV run on separate vendor networks with client isolation (EV-012). PCs, the firewall and the lock server send no logs anywhere, and the firewall's local log overwrites (EV-013). Email uses the provider's default filtering (EV-014). The lock server operating system has been past its vendor support end date since 2023 (EV-015). The 4 front desk terminals are semi-integrated and not in a P2PE solution; the 14 restaurant and bar devices are in a PCI-listed validated P2PE solution, and no inspection log exists (EV-016). Receipts show only the last 4 card digits (EV-017). The CCTV recorder keeps video 30 days, and 2 finger-scan time clocks store finger templates with the timekeeping vendor (EV-018).

**Cloud and backups.** The cloud tenant holds the guest-marketing hub (about 48,000 profiles), a reporting database fed nightly from the PMS, PMS report exports, the chatbot integration and the backup vault, which sits in the production account. The integration's PMS API key has no rotation recorded (EV-019). Nightly lock server and file share backups completed from April to June 2026, with no restore jobs; the PMS vendor runs its own daily backups (EV-020). The cloud provider's SOC 2 report is on its compliance portal (EV-021).

**Documents and records.** The request for a PCI DSS scope document, a card data-flow diagram, an incident response plan, an IT contingency plan, a retention schedule, a configuration standard and change records returned none. The brand policy set lapsed in 2021 (EV-022). The hurricane plan has no IT section (EV-023). The last security awareness completions are from the brand program in 2021 (EV-024). The MSP contract does not assign firewall reviews or scanning, and the MSP states that no internal scans or penetration tests are run (EV-025). Firewall changes are requested by email with no change record (EV-026). The IT Manager was named part-time Information Security Lead on 2026-06-01 (EV-027). Phone and form payments are keyed into the PMS in a browser on front office PCs, and emailed card authorization forms are printed and filed in a front desk binder, with no retention limit stated (EV-028). Six server room keys are issued with no key log (EV-029). Shredding bins are emptied by a vendor with certificates (EV-030). The cyber policy has a breach hotline (EV-031).

**Payments and merchant accounts.** The acquirer's letter of 2026-05-20 questions the 2025 SAQ A and asks the hotel to confirm its SAQ types by 2026-12-31 (EV-032). The merchant agreements require notice to the acquirer within 24 hours of suspecting a compromise (fictional term) (EV-033). The 2025 SAQ A was submitted for both accounts after a vendor salesperson recommended it, and no scoping worksheet exists (EV-034). About 97,000 card transactions ran in 12 months, and the acquirer portal shows no ASV scan submissions (EV-035). AOCs are on file for the PMS vendor (2026-03) and booking engine (2026-01); the gateway AOC is dated 2025-02, and none is on file for the channel manager, the MSP or the lock vendor (EV-036).

**Suppliers and contracts.** Accounts payable shows the hotel's technology and service suppliers, including an enterprise AI assistant add-on (EV-037). The PMS contract has no recovery terms, the revenue-management contract allows pooled benchmarking, and the chatbot contract has no retention or masking terms (EV-038). The PMS vendor's SOC 2 Type 2 report covers the 12 months ending 2026-03-31 and states an RTO of 4 hours and an RPO of 15 minutes (EV-039). The web agency's contract sets no secure development requirements (EV-040).

**AI tools and pricing.** The revenue-management system publishes daily rates automatically, with no floor, ceiling or emergency rule; the vendor provides a SOC 2 Type 1 report only (EV-041). The chatbot handles about 2,400 conversations a month, keeps transcripts with no limit, has no card masking, and takes the base nightly rate from the PMS (EV-042). The booking engine's total price has included the $35 amenity fee since May 2025 (EV-043). Three AI tools were found, and no approved-tools list (EV-044).

**Business volume.** FY2025 revenue was $24.0 million: rooms $17.4 million, food and beverage $5.3 million, other $1.3 million (EV-045). The PMS recorded about 15,700 stays in 2025 and holds about 112,000 guest profiles and 61,000 ID scans since the 2021 migration, with no purge rule (EV-046).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Use of consumer AI tools with hotel data outside the identity provider | Department heads | 2026-07-08 | Not established at intake; P10 treats it as unknown |
| Current gateway AOC (the file copy is dated 2025-02) | Payment gateway | 2026-07-06 | Not provided; carried into P03 row 12.8 and P04 |
| Channel manager AOC | Channel manager vendor | 2026-07-06 | Not provided; carried into the P01 risk register (R-022) |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-003), revenue and volume (EV-045, EV-046), backups (EV-020), the PMS vendor's recovery objectives (EV-039), and dependencies from the asset and vendor registers |
| P02 SSP | The system boundary from the asset inventory; as-found configuration from EV-001, EV-002, EV-006 to EV-016 and EV-019 |
| P04 Cloud mapping | Cloud and SaaS components (EV-019, EV-037) and provider assurance (EV-021, EV-036, EV-039) |
| P01 Risk register | Likelihood inputs from the configuration exports, the vendor files and contracts (EV-036, EV-038), and the AI tool settings (EV-041, EV-042) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The document request response (EV-022) and the handbook (EV-005) |
| P07 Control assessment | Populations to sample from (EV-001, EV-003, EV-006, EV-009, EV-036) |
| P08 IR runbook | Notification duties from the obligations register and the merchant agreements (EV-033); contacts from the vendor register; the insurer hotline (EV-031) |
| P09 SOC 2 | Vendor assurance on file (EV-036, EV-039) |
| P10 AI governance | AI tools found (EV-041, EV-042, EV-044) |
