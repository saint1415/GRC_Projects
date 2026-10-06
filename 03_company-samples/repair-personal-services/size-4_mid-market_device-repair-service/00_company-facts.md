# Scenario facts: Cris Santos Company | Other Services | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the acquirer, the manufacturers' program agreements, the protection plan partners, customers, and vendors are fictional. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (electronics and device repair service; privately held, private equity-backed, board with an audit committee) |
| Business | Regional electronics and device repair chain (NAICS 811210): phones, tablets, laptops, desktops, and game consoles. Walk-in repair at **34 Florida stores**, national **mail-in repair** through a central **Depot**, board-level (microsoldering) repair, **data recovery and data transfer**, warranty repair as a **manufacturer-authorized service provider**, **repair network partner for two device protection plan administrators** (claims fulfillment), repair contracts for about 520 business accounts, and a free **device recycling drop-off** with data wiping |
| Location | Florida headquarters. 34 stores (Store 01 to Store 34) in four regions; the **Depot** (central repair and logistics center: mail-in intake, board-level and warranty repair bench, partner claims repair, data recovery lab, parts warehouse) in central Florida; and a corporate office (finance, HR, IT and security, contact center). Stores open 9:00 to 20:00 Monday to Saturday and 11:00 to 17:00 Sunday. The Depot runs two shifts, 7:00 to 23:00 Monday to Friday and 8:00 to 16:00 Saturday. All workforce members work in Florida; mail-in customers live in all 50 states |
| Workforce | 600 employees: 340 at stores (34 Store Managers, 170 store technicians, 136 customer service advisors), 120 at the Depot (Depot Director and 7 shift supervisors, 60 Depot technicians, 12 data recovery specialists, 40 receiving and logistics staff), 45 in the customer contact center, 15 field technicians for business accounts, and 80 in corporate functions (including 16 in IT and 4 in security and GRC). Store staff turnover was about 48% in the 12 months to 2026-06-30 |
| Revenue | $100.0 million a year (fictional), about $322,600 per store business day over about 310 days. Split: consumer walk-in repair $46.0 million; mail-in repair $9.0 million; manufacturer warranty reimbursements $17.0 million; protection plan partner repairs $16.0 million; business accounts $7.0 million; data recovery $4.0 million; accessories and recycling rebates $1.0 million. Above the SBA standard of $34.0 million for NAICS 811210 (13 CFR 121.201), so **not SBA-small** |
| Volume | About 310,000 repair tickets a year (about 1,000 a business day): 228,000 walk-in, 30,000 mail-in, 38,000 protection plan claims, and 14,000 business account tickets. About 6,200 data recovery cases and about 21,000 recycling drop-off devices a year |
| Customers | About 1.9 million customer records in the ticketing system (every customer since 2016): names, phone numbers, email addresses, mailing addresses, device make, model, serial number or IMEI, and repair history. About 520 business accounts (small and mid-size businesses, private schools, property managers, 3 dental and medical practices) pay by invoice and ACH |
| Card acceptance | About 390,000 card-present transactions a year on **96 payment terminals** that belong to a **validated PCI-listed P2PE solution** from the payment processor (82 at stores, 6 at the Depot counter, 8 spares), and about 52,000 **e-commerce** transactions a year on the mail-in checkout page, which embeds the payment gateway's hosted payment fields (inline frame). Phone payments are keyed directly into a P2PE terminal at the Depot or the contact center's 4 P2PE terminals (counted in the 96). The company never stores card numbers by design |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement with the acquiring bank. It is a contractual standard, not law. In a letter dated 2026-04-15 (fictional), the acquirer confirmed annual self-assessment validation on **SAQ P2PE** for the card-present channel and **SAQ A** (the January 2025 revision of the v4.0.1 SAQ A) for the e-commerce channel, both due 2026-12-15. Merchant levels are set by the card brands and the acquirer and are not stated here |
| Authorized service provider | Authorized service provider for **Manufacturer A** (phones, tablets, computers) at 18 stores and the Depot, and warranty repair depot for **Manufacturer B** (laptops). The program agreements (fictional terms) require background checks for technicians who handle customer devices, access to customer data only as the repair requires and with consent, named MFA-protected accounts on the manufacturer portals, parts traceability by serial number, notice to the manufacturer within **24 hours** of a suspected incident involving customer data or devices, and an annual program audit (Manufacturer A's next audit: 2026-10) |
| Protection plan partners | **Partner P1** and **Partner P2** (fictional device protection plan administrators) send about 38,000 claims a year to the company through the **partner integration API** (claim number, customer name, contact details, device, and fault). The company repairs or replaces the device and posts repair outcomes and costs back, which drive the partners' claim settlement and the company's invoices. The partner agreements (fictional terms) require: use of claim data only to perform the repair; breach notice to the partner within **48 hours** of discovery; annual security questionnaires; and, from the Partner P1 renewal on 2027-06-30, a **SOC 2 Type 2 report** on the claims fulfillment service, delivered by 2027-12-31 |
| Not in scope | **FTC Safeguards Rule (16 CFR Part 314):** the company does not extend credit to consumers or offer in-house financing; business accounts get net-30 invoice terms, which are not consumer financial products (16 CFR 314.1(b)). **HIPAA:** the company is not a covered entity. Policy since 2025 declines data recovery and data transfer work for HIPAA covered entities so that the company does not become a business associate (45 CFR 160.103); P03 tests whether that policy works. The employee group health plan is fully insured, and the company as plan sponsor receives only summary health information and enrollment information. **COPPA:** the website, chatbot, and portal are not directed to children. **Florida Digital Bill of Rights:** not applicable; a controller under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue (and meet one more test). **SEC disclosure:** privately held. **Federal contracts:** none |
| Other applicable law | **FTC Act Section 5** (15 U.S.C. 45(a)(1), 45(n)). **Fla. Stat. 501.171** (2026): reasonable security measures (2), breach notice (3) to (6), disposal of customer records (8). As claims fulfillment provider for the partners, the company also acts as a **third-party agent** under 501.171(1)(h) and (6) (author interpretation, counsel to confirm). **Other states' breach laws** for mail-in customers and partner claimants in every state. **FTC Disposal Rule** (16 CFR Part 682): applies only to consumer report information (background check reports on applicants and employees). **State comprehensive privacy laws without a numeric threshold** that exclude only SBA-small businesses (for example Texas, Tex. Bus. & Com. Code 541.002): the company is no longer SBA-small and serves residents of those states by mail-in, so the Privacy and Compliance Manager owns a privacy program review (outside this security analysis). **Fla. Stat. 934.03** (recording consent) for the contact center |
| Benchmark | NIST CSF 2.0 (voluntary; no sector cybersecurity rule applies). **NIST SP 800-88 Rev. 2**, *Guidelines for Media Sanitization* (final, September 2025; supersedes Rev. 1 of 2014), for wiping customer and recycled devices |
| State law approach | Florida law is cited where a Florida duty is unavoidable (breach notice, disposal, recording consent). Other states' laws are treated generically ("each state where affected individuals reside"), with Florida as the worked example |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Two private equity sponsor directors and one independent director. Receives quarterly cyber risk reports |
| Chief Executive Officer | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer | Executive sponsor of the security program; **system owner of the STPP** (P02); accepts Moderate risks |
| Chief Financial Officer | Owns the merchant agreement, both SAQ attestations, cyber insurance, and the financial terms of partner contracts |
| General Counsel | Contracts, breach notice decisions with outside breach counsel; supervises the Privacy and Compliance Manager |
| Virtual CISO (vCISO, part-time contractor) | Program strategy, risk appetite, board reporting |
| IT Director | Designated **Information Security Officer**; runs the program day to day; owns the SSP and contingency planning |
| Security Manager plus 2 security analysts | Security operations, MSSP oversight, vulnerability management; one analyst is the **GRC Analyst** (risk register, POA&M, vendor reviews) |
| Privacy and Compliance Manager | Privacy notices, consumer requests, breach determinations with counsel, state privacy law program |
| Director of Retail Operations | Owns the 34 stores through 4 Regional Managers and the Store Managers: device custody, intake and release, PIN pad inspections |
| Depot Director | Owns Depot operations, mail-in intake, partner claims repair, and the recycling sanitization line |
| Data Recovery Manager | Custodian of recovered customer data and the data recovery lab |
| Director of Partner Programs | Manufacturer A and B programs and Partners P1 and P2; leads the Manufacturer A audit and the partner security questionnaires |
| Director of Customer Experience | Website, mail-in portal content, chatbot (AI-001), contact center (AI-003), and marketing claims |
| Digital Engineering Manager | Leads 6 developers who build and run the mail-in portal and the partner integration API |
| Director of Business Accounts | 520 business accounts and their security questionnaires |
| HR Director | Hiring, background checks, terminations, training records; business owner of AI-005 |
| Supply Chain Director | Parts and inventory; business owner of AI-004 |
| Co-sourced internal audit firm | Annual IT audit; performs the P07 assessment; reports to the audit committee |
| Managed security service provider (MSSP, external) | 24x7 EDR and SIEM monitoring |
| Ticketing and POS vendor (external) | SaaS repair management and POS platform. SOC 2 Type 2 report (P09) |
| Payment processor and gateway (external) | P2PE solution provider and e-commerce payment gateway. PCI DSS validated service provider |
| Certified electronics recycler (external) | Collects recycling drop-off devices and retired company equipment |

## 3. Systems

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | **Service ticketing and point-of-sale platform**: intake, tickets, customer records, POS, invoicing, inventory, customer status portal, SMS and email updates | Vendor SaaS (enterprise tier) | Yes: about 1.9 million customer records; restricted passcode field purged at release since 2024-09; **legacy passcode and password notes** (gap 2); no card data by design | System of record. Vendor SOC 2 Type 2 (Security, Availability, Confidentiality). Vendor states RTO 8 hours, RPO 1 hour |
| SYS-02 | Payment processor P2PE solution (96 terminals) and payment gateway (hosted payment fields for e-commerce) | Service provider | Card data (provider side only) | The company never holds decryption keys or card numbers |
| SYS-03 | Identity provider (single sign-on, MFA, conditional access) | SaaS | No (identities only) | All named users. Counter tablets use badge tap plus PIN for named sessions |
| SYS-04 | Cloud landing zone: 4 accounts (security and identity, shared services, workloads, backup) | Public cloud provider (vendor-agnostic) | Yes | Workloads: mail-in portal, partner integration API, recovered-data delivery storage, chatbot connector, reporting database. Backup account with 30-day write-once retention |
| SYS-05 | **Company-built applications**: mail-in portal with checkout page, and the partner integration API | Containers in the SYS-04 workloads account | Yes (customer and claim data; the checkout page embeds the gateway's payment fields) | Built by the digital engineering team (6 developers) |
| SYS-06 | Data recovery lab | On-premises (Depot) | Yes (full images of customer devices) | Storage array (about 95 TB used of 160 TB), 14 imaging workstations, write blockers, clean-room bench |
| SYS-07 | Technician bench workstations | On-premises (stores and Depot) | Yes (cached customer data during transfers and diagnostics) | 238 bench PCs and laptops (170 at stores, 68 at the Depot) |
| SYS-08 | Manufacturer service portals and diagnostic tools (Manufacturer A and B) | Manufacturer SaaS | Device serials, repair records, customer names for warranty claims | Named technician accounts required |
| SYS-09 | Site networks: 34 stores, the Depot, and the corporate office on SD-WAN | On-premises | Card data in transit (encrypted by P2PE) | Separate bench and customer-device VLAN at 22 of 34 stores and the Depot |
| SYS-10 | Office endpoints and counter tablets | On-premises | Yes (cached) | 260 office laptops and PCs; 120 counter tablets in device management |
| SYS-11 | Security monitoring: EDR and SIEM | SaaS (MSSP-operated) | Security logs | 24x7 MSSP monitoring |
| SYS-12 | Contact center platform with call recording | Vendor SaaS | Yes (call recordings, transcripts) | 45 agents; hosts AI-003 |
| SYS-13 | AI services | Vendor SaaS | Yes | AI-001 chatbot, AI-002 diagnostics, AI-005 applicant ranking (in SYS-14). See P10 |
| SYS-14 | HR, payroll, and applicant tracking SaaS, with a background check vendor | Vendor SaaS | Employee and applicant data; **consumer reports** | Background check reports are consumer report information under 16 CFR 682.1(b) |
| SYS-15 | CCTV | On-premises recorders | Video | Counters, bench areas, the Depot, and the lab door; 30-day retention |
| SYS-16 | Finance and supply chain ERP | Vendor SaaS | Vendor and business account bank data | Hosts AI-004 parts forecasting |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale Platform (STPP)*: SYS-01, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07, SYS-09, SYS-10, and SYS-11, with their interfaces to SYS-02, SYS-08, SYS-12, and SYS-13.

## 4. Current security posture: a defined program with gaps in scale

**In place today:**
- Validated P2PE terminals for all card-present payments; e-commerce card entry only in the gateway's hosted payment fields; the acquirer confirmed SAQ P2PE and SAQ A for 2026
- Single sign-on with MFA for all named workforce accounts; badge-plus-PIN named sessions on counter tablets (since 2025)
- Restricted passcode field purged at device release (since 2024-09); account passwords are no longer collected
- Customer data access standard for technicians (2025) with repair test checklists; signed confidentiality agreements
- EDR on all office endpoints and 190 of 238 bench workstations; 24x7 MSSP monitoring with a SIEM
- Five security policies adopted in 2024
- Quarterly vulnerability scanning; annual external penetration test of the mail-in portal and partner API (last 2026-05)
- Immutable backups of cloud workloads in a separate backup account (30-day write-once retention)
- Annual security awareness training and quarterly phishing simulations
- Background checks for all technicians and data recovery staff
- Annual co-sourced internal IT audit
- SOC 2 reports or PCI attestations collected for the ticketing vendor, identity provider, cloud provider, payment processor, and MSSP
- Per-device sanitization certificates at the Depot (procedure written to SP 800-88 Rev. 1)
- Cyber insurance: $5 million aggregate limit, $150,000 retention

**Missing or weak, found in the 2026 assessments:**
1. Technician access controls are uneven. Bench session recording and USB storage blocking run on the standard bench image at the Depot and 20 of 34 stores. 48 bench workstations at 14 stores run a legacy image without EDR, 31 of them on an unsupported operating system that legacy diagnostic tools require. In March 2026 a technician at Store 17 copied a customer's photos to a personal phone (substantiated; employee terminated).
2. Legacy credential data. A search on 2026-07-15 found about 11,800 tickets created before 2024-09 with device passcodes in free-text notes and about 640 with account passwords. Chatbot transcripts also hold passcodes typed by customers.
3. Retention is not enforced. Customer records go back to 2016 (policy: 3 years after the last service). The lab purge job has failed silently since a storage firmware upgrade in 2025-11, leaving about 27 TB from about 2,300 cases older than 90 days. Recovered-data download links for business accounts do not expire.
4. Sanitization is uneven. 12 of 34 stores wipe recycling drop-off devices with no per-device certificate; the procedure still follows SP 800-88 Rev. 1 and has no validation step; the recycler's certificates list lots, not serial numbers.
5. PCI controls are incomplete. PIN pad inspection logs are missing or incomplete at 9 of 34 stores; the terminal list differs from the processor's list by 6 devices; the mail-in checkout page has no script inventory or change detection, so the company cannot yet confirm the SAQ A eligibility criterion on script attacks.
6. 12 of 34 stores (the older stores) still run one flat network shared by office PCs, counter tablets, bench PCs, and customer devices.
7. Access lifecycle gaps. SYS-01 access is reviewed quarterly, but manufacturer portal and contact center accounts are not provisioned from HR and have never been reviewed.
8. Logging gaps. SYS-01 audit events (exports and bulk views), the lab storage array, and the mail-in portal application logs are not sent to the SIEM. Nothing alerts on bulk ticket exports.
9. Recovery is unproven. The lab storage backup has never had a full restore test; the mail-in portal and partner API have no tested recovery; the SYS-01 vendor's stated RTO of 8 hours exceeds the BIA need of 4 hours for intake and release.
10. Secure development is informal. The digital team uses peer review but no security testing in the build pipeline, and secrets sit in pipeline variables. The 2026-05 penetration test found one High finding (fixed 2026-06-10).
11. Third-party gaps. 92 vendors, 26 of them with customer data. Seven lack security and data-use terms (courier, recycler, chatbot vendor, diagnostics vendor, contact center AI add-on, overflow answering service, applicant tracking AI feature). Only 5 Tier 1 SOC 2 reviews are done; the recycler and courier were never assessed.
12. No AI governance. Five AI uses were adopted by departments without review. The website says "AI diagnosis, 97% accurate" without substantiation.
13. The 2024 incident response plan covers ransomware only. There is no runbook for device data exposure or checkout skimming, the contract notice clocks (acquirer, Manufacturer A, partners) are missing, and the last tabletop was in March 2025.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary benchmark | NIST CSF 2.0 (voluntary; all 106 subcategories). Secondary: the binding legal baseline (FTC Act Section 5, Fla. Stat. 501.171, other states' breach laws, FTC Disposal Rule), PCI DSS v4.0.1 (SAQ P2PE and the SAQ A eligibility criteria; binding by contract), the manufacturer and partner agreements, and an applicability screen. Requirement-level with evidence sampling |
| Regulatory driver IDs | N81-R01 FTC Act Section 5; N81-R02 state breach laws (Fla. Stat. 501.171 as the worked example); N81-R03 PCI DSS v4.0.1; N81-R04 FTC Disposal Rule (background check reports only); N81-R05 COPPA and N81-R06 HIPAA screened out in P03; `N81-BM` points to the NIST CSF 2.0 benchmark and SP 800-88 Rev. 2. Contract terms are cited as "Manufacturer A agreement (contract)" and "Partner agreements (contract)" |
| P08 incidents | **Two incident types** (the registry default "Customer device data exposure and point-of-sale compromise" split in two, because at this size each needs its own crisis and legal path): (1) `ir-runbook.md`, customer device data exposure (a workforce member copies data from customer devices, or recovered data in the lab or delivery storage is exposed); (2) `ir-runbook-pos-compromise.md`, point-of-sale compromise (skimming script on the mail-in checkout page, payment terminal tampering, or takeover of a SYS-01 administrator account) |
| P09 SOC 2 | Readiness for a **SOC 2 Type 2** examination of the claims fulfillment service requested by Partner P1 (Security, Availability, Confidentiality, Processing Integrity), plus a vendor SOC 2 review program |
| P10 AI | Portfolio of 5: AI-001 customer chatbot, AI-002 AI-assisted diagnostics, AI-003 contact center call transcription and summaries, AI-004 parts demand forecasting, AI-005 applicant ranking in the applicant tracking system |
| Cloud | Multi-account landing zone, vendor-agnostic. AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-04-15 | Acquirer letter confirming SAQ P2PE and SAQ A validation for 2026 |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (site visits 2026-07-14 to 2026-07-23: 8 stores, the Depot, and the corporate office) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness assessment, vendor report reviews, and AI assessment |
| 2026-09-17 | Results presented to the audit committee; deliverables approved by the Chief Operating Officer (High risks and the risk appetite by the Chief Executive Officer) |
| 2026-10 | Manufacturer A annual program audit |
| 2026-12-15 | 2026 SAQ P2PE and SAQ A attestations due to the acquirer |
| 2027-06-30 | Partner P1 agreement renewal (SOC 2 Type 2 report due by 2027-12-31) |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
