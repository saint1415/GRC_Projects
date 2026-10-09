# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreement, the county contract, and vendors are fictional.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (live event venue operator with ticketing; privately held; private equity-backed; board with an audit committee) |
| Business | Promoter of live events with its own facilities (NAICS 711310). Operates **three Florida venues**: **the Amphitheater** (outdoor, 19,500 capacity: 7,500 reserved seats and a 12,000-person lawn; season March to November; operating lease acquired in January 2025), **the Music Hall** (indoor, 5,800 capacity: 3,900 fixed seats and a convertible floor), and **the Club** (1,600 standing). Promotes and co-promotes concerts, comedy, and family shows, sells premium seating (suites and club seats) and group tickets, and rents the venues for private and corporate events |
| Location | Florida only. A headquarters office (executive, finance, IT, central box office and call center, premium and group sales) in the same metro area as the Music Hall and the Club; the Amphitheater is in a second Florida metro area. Four network sites: HQ and the three venues |
| Activity | About 410 shows a year (2025: 46 at the Amphitheater, 150 at the Music Hall, 214 at the Club). About 1.55 million attendees and about 1.38 million tickets sold a year in about 600,000 ticket orders |
| Workforce | 600 employees: 40 executive and administration; 28 finance and settlement; 14 IT and security; 62 ticketing, box office, and call center; 24 premium seating and group sales; 22 marketing and digital; 12 booking and programming; 190 operations, production, and facilities; 170 food and beverage; 38 guest services and security supervisors. About 1,400 event-day workers (ushers, bartenders, stand cashiers, security guards, parking attendants) are supplied by three staffing contractors and are not employees |
| Revenue | $100.0 million a year (fictional): ticket sales and ticket fees about $54.0 million; food and beverage about $28.0 million; premium seating and hospitality about $9.0 million; sponsorship, naming rights, parking and merchandise commissions, and rentals about $9.0 million. Above the SBA standard of $40.0 million for NAICS 711310 (13 CFR 121.201), so **not SBA-small** |
| Patrons | About 1.1 million patron accounts on the ticketing platform (anyone who bought a ticket in the last 5 years), about 640,000 email marketing subscribers, and 410 premium seating accounts (mostly businesses). About 71% of ticket buyers have a Florida billing address; the rest live in every other state (touring fans and visitors; Georgia, New York, and Texas are the largest) |
| Card acceptance | About 2.9 million card transactions a year across all brands, through **two merchant accounts** with one acquiring bank. **Ticketing account (MID-T):** about 600,000 orders a year: about 520,000 online (the ticketing vendor's checkout form embedded in the company's own website event pages), about 50,000 box office window and will-call sales on standalone validated P2PE devices, and about 30,000 phone, group, and premium seating payments keyed by staff into the payment partner's **virtual terminal** in a web browser. **Food, beverage, and merchandise account (MID-F):** about 2.3 million card-present sales a year on validated P2PE devices; the venues have been cashless since 2023. Visa is about 55% of transactions (about 1.6 million a year) (EV-041) |
| Merchant of record | The company is the merchant of record for ticket sales. Ticket revenue settles daily to the company's bank through the ticketing vendor's payment partner |
| PCI DSS status | **Merchant**, determined in the intake obligations register (N71-R04). PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement (EV-040). It is a contractual standard, not law. In a letter dated 2026-03-16 (fictional), the **acquirer classified the company as a Visa Level 2 merchant**. That matches Visa's table in *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 2 merchants have 1,000,001 to 6,000,000 Visa transactions a year. The company moved from Level 3 to Level 2 after it took over the Amphitheater in 2025. Other brands' levels were not verified. The acquirer set the 2026 validation (the acquirer's own requirement, fictional): a **Report on Compliance (ROC) by a Qualified Security Assessor (QSA)** with an attestation of compliance (AOC) for MID-T, an **SAQ P2PE** with AOC for MID-F, and passing quarterly external vulnerability scans by an Approved Scanning Vendor (ASV) for MID-T. All are due **2026-12-15** (EV-039) |
| Prior validation | 2025: SAQ A for MID-T (online only) and SAQ P2PE for MID-F. The acquirer's 2026 letter notes that the 2025 MID-T validation did not cover the virtual terminal channel or the company's website pages that embed the payment form (EV-038, EV-039) |
| Venue management contract | On 2026-06-30 (fictional) a Florida county awarded the company a 10-year agreement to operate the county's 2,400-seat **County Performing Arts Center (County PAC)** from 2027-07-01. The company will sell County PAC tickets on its own ticketing tenant as merchant of record, hold County PAC patron data, and settle net proceeds to the county monthly. The agreement requires a **SOC 2 Type 1 report as of 2027-06-30** and a **SOC 2 Type 2 report** covering Security, Availability, Confidentiality, and Processing Integrity within 12 months after operations begin (EV-050) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). **Gaming** (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos): no casino, gaming, or wagering. **COPPA:** the website, the ticketing pages, and the vendor's mobile ticket app are general audience, not directed to children, and patron accounts require age 18 or older. **HIPAA:** no health care services; first aid is provided by a contracted ambulance service. **SEC disclosure:** privately held. **Federal contracts:** none. **Facial recognition:** the CCTV video management system offers a face-matching feature; it is switched off (EV-017) |
| Other applicable law | Listed with its basis in the intake [obligations register](step-00_P00_intake/obligations-register.csv): FTC Act Section 5 (15 U.S.C. 45(a), (n)) for patron data security, privacy statements, and pricing claims; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464, effective 2025-05-12), which covers live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the company as a ticket issuer; the Florida Information Protection Act (Fla. Stat. 501.171) for reasonable security, disposal, and breach notification; Florida ticket law (Fla. Stat. 817.36) as noted in P10; ADA Title III ticketing rules (28 CFR 36.302(f)) for accessible seating sales and prices. The Texas Data Privacy and Security Act may apply because the company is not SBA-small and sells to Texas residents; counsel is reviewing (P03) |
| State law approach | Florida law is the worked example. Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk and PCI DSS status reporting |
| Chief Executive Officer | Accepts High risks; approves the risk appetite and the security budget; executive officer who signs the PCI DSS AOCs |
| Chief Operating Officer | Executive sponsor of the security program and **system owner** of the TVOP; accepts Moderate risks; chairs the crisis management team |
| Chief Financial Officer | Owns the merchant agreement, the acquirer relationship, the QSA engagement, and the cyber insurance policy |
| General Counsel | In-house counsel and **Privacy Officer**; breach determinations and notices; owns the County PAC agreement |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; SOC 2 program lead |
| IT Director | Runs IT (infrastructure, service desk, venue technology) and recovery; owns the identity provider |
| Security Manager | **Information Security Officer** and PCI DSS program lead; incident commander; leads 2 security analysts |
| GRC Analyst | Risk register, policy set, evidence files for the ROC and SOC 2 |
| Vice President of Ticketing | Owns the ticketing tenant configuration, box offices, call center, pricing rules, ticket limits, and bot mitigation settings. Business owner for AI-001 and AI-002 |
| Vice President of Marketing and Digital | Owns the website and its content management system, the tag manager, email and SMS marketing, the patron data platform, and the marketing agency relationship. Business owner for AI-003 and AI-005 |
| Director of Premium Seating and Group Sales | Owns the premium seating CRM and the virtual terminal users in premium and group sales |
| Vice President of Venue Operations | Facilities, event-day operations, and production at all three venues; owns CCTV and door access |
| Director of Safety and Security | Crowd management, venue security, emergency plans. Business owner for AI-004 |
| Venue General Managers (3) | Event-day command at each venue; decide on doors, holds, and evacuations with the Director of Safety and Security |
| Director of Food and Beverage | Concessions at all three venues; owns the POS and its P2PE devices |
| Controller | Show settlements, artist payments, and county remittances (from 2027) |
| HR Director | Onboarding, terminations, training records, staffing contractor rosters |
| Co-sourced internal audit firm (external) | Annual IT audit; performed the P07 assessment. Not the QSA |
| QSA firm (external) | Performs the 2026 ROC for MID-T (fieldwork 2026-11-02 to 2026-11-13). Independent of the internal audit firm and of the MSSP |
| Managed security service provider (MSSP, external) | 24x7 EDR and SIEM monitoring |
| Ticketing platform vendor (external) | White-label ticketing SaaS. PCI DSS validated service provider with a SOC 2 Type 2 report |
| Payment partner (external) | The ticketing vendor's payment gateway and tokenization partner for MID-T; provides the virtual terminal, the card vault for premium installments, and the box office validated P2PE devices. PCI DSS validated service provider |
| POS vendor (external) | Cloud POS with a PCI-listed validated P2PE solution for MID-F |
| Web agency (external) | Builds website templates and plug-ins for the content management system; has deploy access to the website |
| Marketing agency (external) | Runs paid media; holds publish rights in the tag manager and 4 local accounts on the ticketing platform |
| Network and security integrator (external) | SD-WAN, firewalls, Wi-Fi, CCTV, and door access installation and support; has remote access |
| Staffing contractors (external, 3) | Supply event-day workers |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers are in [`step-00_P00_intake/vendor-register.csv`](step-00_P00_intake/vendor-register.csv).

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: event and seat-map setup, the **embeddable checkout form** used on the company website, box office and call center apps, the vendor's white-label mobile ticket app, access control scanning, reporting and exports, API, **dynamic pricing module**, **bot mitigation and virtual queue** | Vendor SaaS | About 1.1 million patron accounts (name, email, phone, billing address, order history). Card data only inside the vendor's and payment partner's PCI environments | 186 venue user accounts: 175 sign in through the identity provider (SSO and MFA); **11 local accounts** with passwords and no MFA (4 marketing agency, 3 vendor support, 2 break-glass, 2 legacy integration) (EV-006). Vendor service provider AOC dated 2026-02-20; SOC 2 Type 2 (Security, Availability, Confidentiality; 12 months to 2026-03-31) (EV-044) |
| SYS-02 | Payment partner services for MID-T: gateway, tokenization, card vault for premium installments, chargeback portal, **virtual terminal**, and 18 standalone validated P2PE devices at the three box offices | Service provider, plus devices on premises | Card data | Box office devices are PCI-listed validated P2PE (since 2024) (EV-019). The virtual terminal is used by 26 staff on general-purpose laptops (EV-010) |
| SYS-03 | Food, beverage, and merchandise POS: 284 validated P2PE devices (176 fixed, 108 handheld) and the vendor's cloud back office | Vendor SaaS; devices on a vendor-managed network segment | Encrypted card data only (P2PE) | Manual card entry disabled (EV-019) |
| SYS-04 | Company website and content management system (CMS), with a SaaS **tag manager** | Company cloud workloads account; tag manager is SaaS | Patron sign-in passes to SYS-01; card data entered only inside the vendor's embedded form | Event pages embed the SYS-01 checkout form. **31 third-party scripts** load on those pages through the tag manager (EV-068) |
| SYS-05 | Cloud landing zone (4 accounts): identity and security; shared services (network hub, site-to-cloud VPN, log pipeline); workloads (website CMS, **patron data platform** with a nightly copy of about 1.1 million patron records through the SYS-01 API, **show settlement application**); backup (separate account) | Public cloud IaaS/PaaS (vendor-agnostic) | Patron data; settlement data | Immutable backups with 35-day write-once retention in the backup account (EV-026) |
| SYS-06 | Identity provider: single sign-on, MFA (push with number matching), conditional access | SaaS | No (identities only) | Federates email, productivity suite, cloud, SYS-01 (employees), CRM, finance, and HR |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (patron emails; premium contracts) | |
| SYS-08 | Corporate and venue networks: SD-WAN across 4 sites, firewalls, switches, Wi-Fi | On premises; SD-WAN managed service | Card data typed into the virtual terminal crosses the corporate segment | Segments: corporate, production, POS (vendor managed), physical security (CCTV and door access), box office P2PE, public guest Wi-Fi |
| SYS-09 | Endpoints: 520 Windows and Mac laptops and PCs, 180 handheld ticket scanners managed through SYS-01, 64 tablets | Company-managed | Yes (cached exports) | EDR on all 520 laptops and PCs (EV-013) |
| SYS-10 | Physical security systems: 640 CCTV cameras with a video management system (VMS) at each venue, a **crowd analytics module** (AI-004) at the Amphitheater and the Music Hall since 2026-04, and door access control | On premises; integrator supported | Video; badge records | 30-day video retention (EV-017) |
| SYS-11 | Premium seating CRM | SaaS | Contacts and contracts of 410 premium accounts | P03 data discovery found full card numbers in notes fields (EV-069) |
| SYS-12 | Marketing platform: email and SMS, audience segments, **propensity scoring and generative copy features** (AI-005) | SaaS | Subscriber contact data and preferences | Receives segments from the patron data platform |
| SYS-13 | Finance, payroll, and HR | SaaS | Employee and vendor data | |
| SYS-14 | Production systems: lighting and audio consoles, video wall controllers | On premises | No | Standalone; touring crews connect to the production segment |
| SYS-15 | Guest service chatbot on the website (AI-003) | SaaS | Names, emails, order numbers, accessibility requests typed by patrons | Generative AI; launched 2026-02 |
| SYS-16 | SIEM and EDR console (MSSP-operated) | SaaS | Security logs | Ingests identity provider, cloud, firewall, and EDR logs. **Does not ingest** ticketing audit logs, CMS and tag manager changes, or payment partner portal activity (EV-027) |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the company's tenant configuration, users, and API keys in SYS-01, the MID-T card channels in SYS-02 (virtual terminal users and box office P2PE devices), the website and tag manager (SYS-04), the cloud landing zone (SYS-05), the identity provider (SYS-06), the corporate and venue networks (SYS-08), endpoints and scanners (SYS-09), and the SIEM (SYS-16), with interfaces to SYS-03, SYS-07, SYS-10, SYS-11, SYS-12, SYS-13, and SYS-15.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against PCI DSS v4.0.1, the FTC Act and the fee rule, the ADA ticketing rules, and the Florida Information Protection Act** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 primary standard | PCI DSS v4.0.1 (contractual), assessed as readiness for the 2026 ROC, with the FTC Act Section 5 and the Rule on Unfair or Deceptive Fees, the ADA Title III ticketing rules (28 CFR 36.302(f)), and the Florida Information Protection Act (data security and disposal). One-row applicability check of the BOTS Act; Texas privacy law applicability noted for counsel |
| P08 incidents | **Two incident types:** (1) ticketing platform breach: a skimming script published through a marketing agency tag manager account on the website pages that embed the checkout form, plus a patron export through a local agency account on the ticketing platform (the registry default, kept); (2) event-day outage: loss of ticketing and scanning during doors at the Amphitheater (vendor outage or a cyberattack on the venue network), integrated with venue emergency operations |
| P09 SOC 2 | Readiness for the SOC 2 Type 1 and Type 2 reports the County PAC agreement requires (Security, Availability, Confidentiality, Processing Integrity), plus a vendor SOC 2 review program |
| P10 AI | Portfolio of 5: AI-001 dynamic ticket pricing and AI-002 bot detection and virtual queue (the registry default, kept as the core), AI-003 guest service chatbot, AI-004 CCTV crowd analytics, AI-005 marketing propensity scoring and generative copy |
| Cloud | Multi-account landing zone, vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents only for shared responsibility |
| Registry defaults | Primary system kept (Ticketing and Venue Operations Platform). The P08 incident was kept and a second incident type added because the Mid-Market tier calls for two. The P10 use case was kept and widened to a portfolio because the Mid-Market tier calls for one |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-03-16 | Acquirer letter (EV-039): Visa Level 2; ROC for MID-T and SAQ P2PE for MID-F; due 2026-12-15 |
| 2026-06-15 to 2026-07-02 | Intake: evidence requests, exports, walk-throughs at the 4 sites, inventories, obligations register |
| 2026-06-30 | County PAC management agreement awarded (EV-050) |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (on-sale observed 2026-07-15; Amphitheater show night observed 2026-07-18) |
| 2026-07-27 to 2026-07-31 | 2026 policy set (POL-01 to POL-05), the standards index, and the P08 runbooks drafted from the gaps |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm: operating tests of controls already in place; design review of the draft policies, standards, and runbooks |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness, vendor report reviews, and AI assessment |
| 2026-09-15 | Deliverables, policies, and runbooks approved (Chief Operating Officer; High risks and the risk appetite by the Chief Executive Officer); results to the audit committee |
| 2026-10-01 | 2026 policies take effect |
| 2026-11-02 to 2026-11-13 | QSA ROC fieldwork |
| 2026-12-15 | ROC, AOCs, SAQ P2PE, and ASV scan reports due to the acquirer |
| 2027-03 (planned) | Follow-up assessment: operating effectiveness of the controls the new policies and standards introduced, after at least one quarter of operation |
| 2027-06-30 | SOC 2 Type 1 report date (County PAC) |
| 2027-07-01 | County PAC operations begin; SOC 2 Type 2 observation period starts |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Sites and IT staff | HQ, the Music Hall, and the Club share one metro area; the Amphitheater is about a 2-hour drive away. The 14 IT and security staff are the IT Director, the Security Manager, 2 security analysts, the GRC Analyst, 4 infrastructure and cloud engineers, 3 service desk staff, and 2 venue technology technicians |
| Merchant agreement | The acquirer must be told within 24 hours of a suspected compromise of card data (fictional term; EV-040) |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensics. Notice through the carrier hotline is required before incident vendors are engaged. Card brand assessments are covered only up to a $1 million sublimit (EV-049) |
| Ticketing vendor recovery | The vendor's SOC 2 system description states RTO 4 hours and RPO 15 minutes. Scanners can work offline from a manifest downloaded before doors (EV-044, EV-014) |
| Event-day revenue | Average food and beverage sales per show: Amphitheater about $305,000, Music Hall about $67,000, Club about $18,000. About 70% of a show's food and beverage sales happen in the 2 hours around doors and the set break (EV-055, EV-057) |
| Online sales | About 1,400 online ticket orders on an average day; the largest 2026 on-sale (an Amphitheater headliner on 2026-07-15) sold about 12,500 tickets in the first hour through the virtual queue (EV-056, EV-065) |
| Website scripts | On 2026-07-20, 31 third-party scripts loaded on event pages that embed the checkout form: 19 analytics and advertising tags, 6 social and video embeds, 4 personalization and A/B testing tags, and 2 with no known owner. Tag manager publish rights: 9 users, including 4 marketing agency staff on local accounts without MFA (P03 capture EV-068; tag manager users EV-011) |
| Virtual terminal | 26 users: 9 premium seating, 8 group sales, and 9 call center leads. The payment partner can supply validated P2PE devices that accept keyed phone orders (about $14,000 for 26 devices, fictional). Users from EV-010 |
| Card data discovery | Scan of the premium seating CRM, file shares, and mailboxes on 2026-07-22: 312 full card numbers in 141 CRM notes (9 with security codes), 47 in mailbox attachments of 6 users, none on file shares (EV-069) |
| Workforce activity | 96 employee terminations and 51 transfers in the 12 months to 2026-06-30; seasonal Amphitheater staff are added each March. The June 2026 phishing simulation click rate was 6.2% (EV-003, EV-036) |
| MSSP | Contract requires a call to the Security Manager within 30 minutes of a high-severity alert (EV-028) |
| Ticket limits | Posted limit of 8 tickets per customer for high-demand on-sales, enforced per account. 22 high-demand on-sales in the 12 months to 2026-06-30 (EV-007, EV-056) |
| County PAC | 2,400 seats; about 180 performances a year; the county receives monthly settlement statements and patron reports. The agreement requires notice to the county within 48 hours of a security incident affecting County PAC data or services (EV-050) |
| Terminology | "Ticketing and Venue Operations Platform (TVOP)" is the SSP system in P02, identifier CSC-TVOP-01 |
| Additional role titles | Head of Booking (owner of BP-12); box office managers at each venue; a ticketing operations supervisor; venue security managers; the production manager at each venue |
| Ticketing tenant details | 14 venue users hold the admin role (target 6). 3 API keys: the patron data platform sync (full admin scope), the settlement application (report read), and the marketing platform connector (segment read). A 2023 setting caps orders that include a wheelchair space at 4 seats although the posted limit is 8. The ticketing FAQ describes the order fee as "charged by the ticketing company"; the company sets it and receives a share. 3 ticketing supervisors can change pricing rules (EV-006, EV-007, EV-008, EV-060) |
| Website details | 12 named CMS editors on SSO; 3 web agency deploy roles through the cloud pipeline; 23 CMS plug-ins (5 custom), 4 out of date in July 2026, 1 with a critical issue open 46 days. The P07 capture of 2026-08-11 showed 33 scripts on pages that embed the checkout form (2 added since 2026-07-20; both removed 2026-08-14). The privacy notice dates from 2023 (EV-012, EV-072, EV-CM-7, EV-060) |
| Endpoints and facilities | 22 laptops keep local admin rights by exception. 9 venue network closets, 2 of them on keys with no key log. 4 VMS servers run an operating system past vendor support. 12 integrator-installed servers and controllers (CCTV, door access, crowd analytics) (EV-013, EV-052, EV-017) |
| Assessment populations | 143 new identity provider accounts and 38 federated privileged accounts (2025-07 to 2026-06); 41 incidents in the queue (2025-2026); 18 critical vulnerability findings (Jan-Jun 2026); 214 ticketing setting changes and 61 infrastructure changes (Jan-Jun 2026); 312 website calendar listings and 58 email campaigns since 2026-01; 9,840 CRM notes and 38 CRM users; 64 mailboxes of payment-handling staff scanned. The 5 group sales staff with virtual terminal access had no background check (EV-001, EV-009, EV-033, EV-020, EV-007, EV-023, EV-060, EV-061, EV-069, EV-071) |
| Service provider assurance | Payment partner AOC on file dated 2024-06-12; the 2026 AOC was requested 2026-08-20 and promised by 2026-10-15. Ticketing vendor bridge letter to 2026-09-30 received 2026-09-08. POS vendor AOC dated 2026-04-15. The tag manager vendor, identity provider, cloud provider, MSSP, and chatbot vendor provided SOC 2 Type 2 reports (details in P09). AOCs on file at intake: EV-044, EV-045, EV-046 |
| Budget | FY2027 security plan approved by the CEO on 2026-09-15: $584,000 one-time and $255,000 a year (fictional) |
| Exercises and drills | Amphitheater manual entry drill each March (last 2026-03, passed). Music Hall drill due 2026-10-31; Club drill due 2026-11-30. Card compromise tabletop 2026-11-04; event-day outage tabletop 2027-02-17 (EV-035, EV-032) |
| AI use cases | AI-001 in use since 2025-11 on 61 reserved-seat shows; AI-002 protected 22 on-sales in the 12 months to 2026-06-30 (4 since 2026-06-01, about 140,000 queue entrants); AI-003 in use since 2026-02 (about 9,000 chat sessions a month; transcripts kept 1 year by default); AI-004 in use since 2026-04; AI-005 in use since 2026-05 by 6 marketing staff. The AI review group (vCISO, General Counsel, Vice President of Ticketing, Vice President of Marketing and Digital, Director of Safety and Security) first meets 2026-10-06. Uses found at intake: EV-058 |
| Assessment results used across deliverables | P03 samples (EV-074, EV-070, EV-021, EV-069): 40 of 40 calendar listings, 12 of 12 email campaigns, and 9 of 20 social posts showed base prices only; 281 of 284 POS devices and 18 of 18 box office devices located; inspection records for 4 of 10 sampled event days; ASV scans passed 4 of 4 quarters; 2 of 6 printed premium files held card numbers. P07 tests (EV-SI-3, EV-SI-4, EV-CP-9, EV-AU-6): EICAR files quarantined within 4 minutes; MSSP escalated a simulated sign-in in 22 minutes; a test restore of a CMS folder succeeded on 2026-08-13; 3 bulk exports in July 2026 had not been reviewed (later confirmed legitimate). P10 tests: AI-001 had 388 price changes on 14 shows, 3 shows above artist caps (up to 15%) and 2 parity breaches ($9 and $14, for 2 and 4 days); AI-002 found 41 linked-account clusters buying 1,610 tickets above the limit, and challenge failure of 4.1% on mobile networks against 1.2% on home broadband; AI-003 answered 33 of 40 scripted questions correctly and disclosed order details in 2 of 10 crafted attempts; AI-004 undercounted the Amphitheater lawn by 18% to 25% after dark; AI-005 generated copy used base prices in 5 of 12 campaigns |
| P08 scenario assumptions | The card compromise runbook assumes an export of about 410,000 patron records and a 9-day window covering about 21,000 checkouts. These are planning assumptions, not events that occurred |
| SOC 2 plan | Type 1 as of 2027-06-30; Type 2 period 2027-07-01 to 2027-12-31 with the report by 2028-03-31; the service auditor will be a CPA firm independent of the internal audit firm and the QSA |
