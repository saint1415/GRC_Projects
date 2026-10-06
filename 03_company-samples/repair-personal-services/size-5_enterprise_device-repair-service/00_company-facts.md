# Scenario facts: Cris Santos Company | Other Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, or standard, the citation is given. Facts about the acquirer, the QSA, the manufacturers' program agreements, clients, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; national electronics and device repair chain) |
| Business | Electronics and device repair (NAICS 811210) for phones, tablets, laptops, desktops, game consoles, and wearables. Six lines of business: walk-in repair at company-operated stores; mail-in repair through three regional repair depots; manufacturer-authorized warranty repair for **Manufacturers A, B, and C**; **claims repair fulfillment (SL-1)** for device protection plan administrators and wireless carriers; **enterprise device lifecycle services (SL-2)** for business, school district, and health care clients (depot repair, imaging and provisioning, data sanitization, and IT asset disposition); and **data recovery and data transfer** at a national data recovery lab. Free device recycling drop-off at every store |
| Location | Headquartered in Florida. **1,120 company-operated stores in 44 states and DC**: 960 core stores and 160 stores of the **acquired chain (AC)**. Three regional repair depots: **Depot East** (Florida, also home of the national data recovery lab), **Depot Central** (Texas), and **Depot West** (Nevada). A customer contact center in Florida. Two colocation sites (COLO-1 Florida, COLO-2 Texas). **State law is handled generically:** apply the law of each state where affected individuals reside, with Florida as the worked example |
| Acquired chain (AC) | A regional repair chain of 160 stores in Arizona, Nevada, New Mexico, Utah, Colorado, and Texas, acquired on **2025-11-03**. Not yet converted to the company's ticketing and POS platform, network, payment solution, or identity platform (see section 4) |
| Workforce | **12,000 employees**: about 7,900 in stores (technicians, customer service advisors, store managers), about 1,900 at the depots and the data recovery lab, about 650 in the contact center, and about 1,550 at headquarters and in field management (including about 420 in technology and digital, of whom 52 are in the security organization) |
| Revenue | About **$4.8 billion** a year (fictional), about $13.2 million per calendar day. Mix: consumer walk-in and mail-in repair 44%; manufacturer warranty reimbursements 21%; SL-1 claims repair fulfillment 18%; SL-2 enterprise device lifecycle services 10%; accessories, parts, and refurbished device wholesale 4%; data recovery 3%. Above the SBA standard of $34.0 million for NAICS 811210 (13 CFR 121.201), so not small |
| Volume | About **13.5 million repair tickets a year** (about 37,000 a day), including about 2.1 million mail-in repairs through the depots and about 2.4 million SL-1 claim repairs. About 46,000 data recovery cases, about 820,000 SL-2 devices sanitized, and about 1.3 million recycling drop-off devices a year |
| Customers | About **31 million customer records** in the core ticketing platform (every customer since 2018) and about 4.1 million in the AC legacy ticketing service: names, phone numbers, email addresses, mailing addresses, device make, model, serial number or IMEI, and repair history. About 6.4 million customer accounts on the website and mobile app (age 18 or older). About 3.6 million records belong to California residents |
| Card acceptance | About 21.4 million card-present transactions a year (about 2.9 million at AC stores) and about 2.6 million card-not-present payments (about 1.9 million through the website and app, about 0.7 million by phone through the contact center and the depots) |
| PCI DSS status | **Level 1 merchant as designated by the acquirer** (letter dated 2026-02-17, fictional). PCI DSS v4.0.1 applies through the merchant agreement; it is a contractual standard, not law (N81-R03). Validation is an annual **Report on Compliance (ROC) by a Qualified Security Assessor (QSA)** with an Attestation of Compliance (AOC). Merchant level thresholds are set by the card brands and are not restated here. The 2025 ROC (core stores, e-commerce, contact center) was compliant with 2 compensating controls. The 2026 ROC is the first to include the AC stores |
| Payment architecture | **Core stores (960):** about 3,100 PIN pads from a **PCI-listed validated P2PE solution** of the primary processor; the acquirer accepts P2PE scope reduction for store lanes. **Web and app:** booking deposits and mail-in payments use the processor's hosted payment fields (inline frames) and mobile SDK; saved cards are processor tokens; the company stores no full card numbers after authorization. **Contact center and depots:** phone payments go through a DTMF masking service (62% of calls) or are keyed by agents into the processor's virtual terminal on managed PCs (38%). **AC stores (160):** legacy Windows POS software with about 410 legacy PIN pads that **do not encrypt at the point of interaction**; card data is in clear text in POS memory and on the store network before it reaches a legacy processor over a site VPN |
| Authorized service provider | Authorized service provider for **Manufacturer A** (phones, tablets, computers) at 610 core stores and all depots, warranty depot for **Manufacturer B** (laptops), and authorized repair for **Manufacturer C** (game consoles and wearables). The program agreements (fictional terms) require background checks for technicians, access to customer data only as the repair requires and with consent, named MFA-protected accounts on the manufacturers' portals and diagnostic tools, parts traceability by serial number, notice to the manufacturer within **24 hours** of a suspected incident involving customer data or devices, and an annual program audit. They are contracts, not law |
| Service lines for external clients | **SL-1 claims repair fulfillment:** repairs for 4 device protection plan administrators and 2 wireless carriers. Clients send claim and customer data through the SL-1 claims API; the company repairs, returns, and reports status and outcome. Annual SOC 2 Type 2 report (Security, Availability, Confidentiality) since 2024. **SL-2 enterprise device lifecycle services:** about 1,400 business, school district, and health care clients; asset tracking portal; depot repair, imaging and provisioning, sanitization, and IT asset disposition (ITAD) with resale of sanitized devices to wholesale refurbishers. No SOC 2 report yet |
| HIPAA role | **Not a covered entity.** For SL-2 only, **38 health care clients** have signed business associate agreements (BAAs) with the company because their devices may hold ePHI. Under those BAAs the company acts as a **business associate**, and the HIPAA Security Rule applies to that ePHI (45 CFR 164.302) along with business associate breach notice (45 CFR 164.410) |
| Not in scope | **FTC Safeguards Rule (16 CFR Part 314):** the company does not extend credit to consumers or offer financing; business accounts are invoiced, so it is not a "financial institution" (16 CFR 314.1(b)). **COPPA:** the website, app, and chatbot are not directed to children and accounts require age 18. **Florida Digital Bill of Rights:** revenue exceeds $1 billion, but the company meets none of the other controller criteria in Fla. Stat. 501.702 (online advertising revenue, smart speaker service, or app store). **Trade-ins:** the company does not buy used devices from consumers. **Federal contracts:** none. **CIRCIA:** final rule not published as of 2026-09-25 |
| Other applicable law | **FTC Act Section 5** (15 U.S.C. 45(a), 45(n)) (N81-R01); **state breach notification and data security laws** (N81-R02), Florida worked example Fla. Stat. 501.171, including (8) disposal; **FTC Disposal Rule** (16 CFR 682.3) for background check reports only (N81-R04); **FACTA receipt truncation** (15 U.S.C. 1681c(g)); **SEC** Form 8-K Item 1.05 and Regulation S-K Item 106; **SOX** internal control over financial reporting; **California CCPA** and the CPPA regulations on cybersecurity audits, risk assessments, and automated decisionmaking technology (11 CCR 7120-7124, 7150-7157, 7200 and following); state AI and employment laws for AI hiring tools (see P10) |
| Benchmark | NIST CSF 2.0 (voluntary; no sector cybersecurity rule applies) (N81-BM). **NIST SP 800-88 Rev. 2**, *Guidelines for Media Sanitization* (final, September 2025), for sanitization of customer, SL-2, and recycled devices |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board: audit committee; risk and technology committee | Risk and technology committee oversees cybersecurity (Item 106 disclosure); audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk jointly; the CFO signs the PCI DSS AOC; both take part in materiality determinations |
| Chief Information Security Officer (CISO) | Security program owner; reports to the CIO with a direct line to the risk and technology committee |
| Director of Security Operations | 24x7 SOC (in-house, with MSSP overflow); incident commander (P08); designated HIPAA security official for SL-2 (45 CFR 164.308(a)(2)) |
| Chief Privacy Officer | Privacy program, state privacy laws including the CCPA, breach determinations with counsel |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Internal Audit (third line, in-house IT audit team of 5); reports to the audit committee; leads P07 |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| GRC team (9, including the PCI Program Manager), SOC, Internal Audit | Three lines model: the first line operates controls, GRC (second line) runs the methods, Internal Audit (third line) tests independently |
| QSA firm (external) | Independent PCI DSS assessor; 2026 ROC fieldwork 2026-10-19 to 2026-11-20 |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Formed 2025; chaired by the Chief Data and Analytics Officer |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | **Service ticketing and point-of-sale platform**: intake, tickets, customer records, parts, POS, website and app booking and status, notifications, and the SL-1 claims API | Company-built on Cloud provider A (managed containers, managed relational database). 31 million customer records. A restricted, encrypted passcode field purged at device release since 2025-04; **free-text notes still hold passcodes** (see section 4) |
| SYS-02 | Payment environment | P2PE PIN pads at the 960 core stores; hosted payment fields and mobile SDK; DTMF masking and virtual terminal for phone payments; AC legacy POS (see SYS-13) |
| SYS-03 | Identity platform (SSO, MFA, privileged access management, identity governance) | AC staff still use the AC legacy directory |
| SYS-04 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus COLO-1 and COLO-2 | Cloud A: SYS-01 and the SL-1 claims API. Cloud B: data platform, AI services, SL-2 asset tracking portal. Colocation: network core, backup copies |
| SYS-05 | Store, depot, and enterprise network (SD-WAN, segmentation, wireless) | Core stores have separate POS, office, bench, and customer device quarantine VLANs. NAC at 640 of 960 core stores. AC stores run flat networks |
| SYS-06 | Endpoints | About 14,500 PCs, laptops, and counter tablets, including about 6,900 technician bench workstations at core stores and depots. EDR on 97% of corporate endpoints and servers and 91% of core bench workstations |
| SYS-07 | Depot and lab systems | Depot management and parts traceability; data recovery lab storage (about 1.1 PB); sanitization stations with sanitization software that writes a per-device record |
| SYS-08 | ERP, payroll, and HR | SOX-relevant; HR system holds background check reports (consumer reports) |
| SYS-09 | Manufacturer portals and diagnostic tools (Manufacturers A, B, C) | Named technician accounts required by the program agreements |
| SYS-10 | Third parties | About 1,300 vendors; 58 third-party service providers (TPSPs) with PCI DSS responsibilities; 26 downstream recyclers and refurbishers for SL-2 and recycling |
| SYS-11 | Customer engagement: CRM, contact center telephony and call recording, chatbot, notifications | Cloud B and SaaS |
| SYS-12 | AI portfolio | 11 use cases (P10), governed by the AI governance committee |
| SYS-13 | AC legacy stack | Legacy ticketing SaaS (free-text passcode field), legacy POS and PIN pads, legacy directory, flat store networks, a legacy managed service provider's remote support tool, no SIEM feed, no EDR on about 720 AC bench PCs |

**SSP system (P02):** the *Service Ticketing and Point-of-Sale Platform (STPP)*: the company-built ticketing, customer, and POS application and its database on Cloud provider A (SYS-01), the store POS clients and P2PE PIN pads at the 960 core stores, the website and app booking with hosted payment fields, and the SL-1 claims API, with interfaces to SYS-02, SYS-07, SYS-09, SYS-11, the primary processor, and SL-1 clients. The 160 AC stores (SYS-13) are outside the boundary until they convert.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with three lines of defense and ERM integration (NIST IR 8286)
- Annual PCI DSS ROC by a QSA since 2016; the 2025 ROC was compliant with 2 compensating controls
- Validated P2PE at all 960 core stores; tokenization; hosted payment fields on the web checkout
- 24x7 SOC with SIEM; EDR on 97% of corporate endpoints and servers
- Privileged access management; quarterly access certification for SYS-01 and the cardholder data environment
- Immutable backups; annual disaster recovery tests for tier-1 systems
- Named bench accounts, USB storage blocked except at data transfer stations, and session recording at data transfer stations at core stores and depots
- A restricted, encrypted passcode field in SYS-01, purged at device release (since 2025-04)
- A sanitization standard based on NIST SP 800-88 (updated to Rev. 2 in 2026-03) with per-device records at Depot East and Depot Central
- Tiered third-party risk program with annual AOC and SOC report collection
- SOC 2 Type 2 for SL-1 since 2024
- SOX IT general controls tested annually; SEC Item 106 disclosure in the 10-K

**Targeted gaps:**
1. **Acquired chain.** The 160 AC stores run legacy POS without encryption at the PIN pad, a legacy ticketing service with passcodes in free text, flat store networks, a legacy directory, and a legacy managed service provider's remote support tool with shared credentials. No SIEM feed and no EDR on AC bench PCs. Conversion is due in two waves: 70 stores by 2026-12-15 and 90 stores by 2027-03-31.
2. **Passcodes in notes.** A data loss prevention scan of SYS-01 on 2026-07-21 found about 212,000 tickets with passcode-like strings in free-text notes and 1,140 with full card numbers. The AC legacy ticketing service holds about 1.9 million tickets with device passcodes and about 96,000 with account passwords.
3. **Technician access.** 31% of core bench workstations still run the 2023 image, which does not wipe data transfer caches at the end of a job. Bench session logs are reviewed only when an alert fires. In 2026, 37 customer complaints alleged that a technician accessed personal content; 3 were substantiated.
4. **Sanitization.** Depot West does not yet verify sanitization per device, and store recycling drop-off relies on lot-level recycler certificates. In 2026-05 a wholesale buyer reported SL-2 client data on a refurbished laptop sanitized at Depot West (a secondary drive was missed).
5. **Retention.** Recovered data is deleted 30 days after delivery since 2025-01, but about 180 TB from older data recovery cases is still on the lab storage.
6. **Payment pages and phone payments.** Script controls (PCI DSS 6.4.3 and 11.6.1) cover the main web checkout but not the mobile web deposit page. DTMF masking covers 62% of phone payments; 8 of 60 sampled call recordings held spoken card numbers.
7. **Service providers.** Of 58 TPSPs, 7 had an expired AOC and 11 had no written split of PCI DSS responsibilities. 9 of 26 downstream recyclers and refurbishers have no data protection terms.
8. **AI.** 11 use cases; 6 reviewed by the AI governance committee. The applicant screening tool (High tier) is in use without a bias audit in states with AI hiring laws. The chatbot receives passcodes from customers.
9. **Materiality.** The disclosure committee has never exercised a combined card compromise and customer data exposure. The playbook does not tie card brand and forensic steps to the materiality timeline.
10. **SL-2 assurance.** No SOC 2 report. The BAA inventory for the 38 health care clients is incomplete, and BA duties are not mapped to SL-2 controls.
11. **California cybersecurity audit.** The first audit period starts 2027-01-01 (report due 2028-04-01); the audit scope and auditor are not yet set.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | NIST CSF 2.0 (all 106 subcategories, voluntary benchmark) as the primary analysis, plus every binding requirement: PCI DSS v4.0.1 at ROC depth (contractual), FTC Act Section 5, FACTA receipt truncation, the FTC Disposal Rule, state breach and data security law (Florida worked example), the California CCPA cybersecurity audit, risk assessment, and ADMT rules, SEC Item 1.05 and Item 106, HIPAA Security Rule standards for SL-2 as a business associate, the manufacturer program agreements, and an applicability screen |
| Regulatory driver IDs | N81-R01 FTC Act Section 5; N81-R02 state breach and data security laws (Florida worked example); N81-R03 PCI DSS v4.0.1; N81-R04 FTC Disposal Rule (background check reports only); N81-R06 HIPAA (here as business associate duties for SL-2 only); `N81-BM` points to the NIST CSF 2.0 benchmark and SP 800-88 Rev. 2. SEC, CCPA, FACTA, and contract terms are cited by name |
| P08 | Customer device data exposure and point-of-sale compromise at the AC stores (memory-scraping malware on legacy POS plus theft of legacy ticket data with passcodes and account passwords), with acquirer and card brand steps, an **SEC materiality assessment and 8-K Item 1.05** step, manufacturer and SL-1 client notices, and a multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines: SL-1 claims repair fulfillment (existing report; Processing Integrity added) and SL-2 enterprise device lifecycle services (first report) |
| P10 | Enterprise AI portfolio (11 use cases) with the committee operating model, and a full assessment of AI-001 AI-assisted diagnostics and AI-002 customer chatbot |
| Cloud | Multi-cloud (vendor-agnostic) with common controls, plus two colocation sites |
| Registry defaults | Primary system "Service ticketing and point-of-sale system" kept, named the STPP. Incident "Customer device data exposure and point-of-sale compromise" kept, set at the AC stores because that is where card data is exposed. AI use case "AI-assisted diagnostics and customer chatbot" kept as AI-001 and AI-002 within the portfolio |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-02-17 | Acquirer letter confirming Level 1 and ROC validation, with the AC stores in 2026 scope |
| 2026-06-01 to 2026-07-31 | Enterprise BIA, risk analysis, and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit) |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness and AI portfolio review |
| 2026-09-10 | Results to the risk and technology committee of the board |
| 2026-10-19 to 2026-11-20 | QSA fieldwork for the 2026 ROC |
| 2026-11-12 | Disclosure committee tabletop (card compromise and customer data exposure) |
| 2026-12-15 | 2026 ROC and AOC due to the acquirer |
| 2027-01-01 | First California cybersecurity audit period starts (report due 2028-04-01) |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.
