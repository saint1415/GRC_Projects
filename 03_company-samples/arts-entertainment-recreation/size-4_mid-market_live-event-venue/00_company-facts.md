# Scenario facts: Cris Santos Company | Arts, Entertainment, and Recreation | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or card brand rule, the citation is given. Facts about the acquirer, the merchant agreement, the county contract, and vendors are fictional.

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
| Card acceptance | About 2.9 million card transactions a year across all brands, through **two merchant accounts** with one acquiring bank. **Ticketing account (MID-T):** about 600,000 orders a year: about 520,000 online (the ticketing vendor's checkout form embedded in the company's own website event pages), about 50,000 box office window and will-call sales on standalone validated P2PE devices, and about 30,000 phone, group, and premium seating payments keyed by staff into the payment partner's **virtual terminal** in a web browser. **Food, beverage, and merchandise account (MID-F):** about 2.3 million card-present sales a year on validated P2PE devices; the venues have been cashless since 2023. Visa is about 55% of transactions (about 1.6 million a year) |
| Merchant of record | The company is the merchant of record for ticket sales. Ticket revenue settles daily to the company's bank through the ticketing vendor's payment partner |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 (PCI SSC) applies through the merchant agreement. It is a contractual standard, not law. In a letter dated 2026-03-16 (fictional), the **acquirer classified the company as a Visa Level 2 merchant**. That matches Visa's table in *What To Do If Compromised* v10.0 (effective 2026-06-25): Level 2 merchants have 1,000,001 to 6,000,000 Visa transactions a year. The company moved from Level 3 to Level 2 after it took over the Amphitheater in 2025. Other brands' levels were not verified. The acquirer set the 2026 validation (the acquirer's own requirement, fictional): a **Report on Compliance (ROC) by a Qualified Security Assessor (QSA)** with an attestation of compliance (AOC) for MID-T, an **SAQ P2PE** with AOC for MID-F, and passing quarterly external vulnerability scans by an Approved Scanning Vendor (ASV) for MID-T. All are due **2026-12-15** |
| Prior validation | 2025: SAQ A for MID-T (online only) and SAQ P2PE for MID-F. The acquirer's 2026 letter notes that the 2025 MID-T validation did not cover the virtual terminal channel or the company's website pages that embed the payment form |
| Venue management contract | On 2026-06-30 (fictional) a Florida county awarded the company a 10-year agreement to operate the county's 2,400-seat **County Performing Arts Center (County PAC)** from 2027-07-01. The company will sell County PAC tickets on its own ticketing tenant as merchant of record, hold County PAC patron data, and settle net proceeds to the county monthly. The agreement requires a **SOC 2 Type 1 report as of 2027-06-30** and a **SOC 2 Type 2 report** covering Security, Availability, Confidentiality, and Processing Integrity within 12 months after operations begin |
| Not in scope | **Gaming** (Nevada Reg. 5.260, NIGC MICS, BSA/AML for casinos): no casino, gaming, or wagering. **COPPA:** the website, the ticketing pages, and the vendor's mobile ticket app are general audience, not directed to children, and patron accounts require age 18 or older. **HIPAA:** no health care services; first aid is provided by a contracted ambulance service. **SEC disclosure:** privately held. **Federal contracts:** none. **Facial recognition:** the CCTV video management system offers a face-matching feature; it is switched off |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for patron data security, privacy statements, and pricing claims; the FTC Rule on Unfair or Deceptive Fees (16 CFR Part 464, effective 2025-05-12), which covers live-event tickets; the BOTS Act (15 U.S.C. 45c), which protects the company as a ticket issuer; the Florida Information Protection Act (Fla. Stat. 501.171) for reasonable security, disposal, and breach notification; Florida ticket law (Fla. Stat. 817.36) as noted in P10; ADA Title III ticketing rules (28 CFR 36.302(f)) for accessible seating sales and prices. The Texas Data Privacy and Security Act may apply because the company is not SBA-small and sells to Texas residents; counsel is reviewing (P03) |
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

| ID | System | Hosting | Personal or card data? | Notes |
|---|---|---|---|---|
| SYS-01 | Ticketing platform: event and seat-map setup, the **embeddable checkout form** used on the company website, box office and call center apps, the vendor's white-label mobile ticket app, access control scanning, reporting and exports, API, **dynamic pricing module**, **bot mitigation and virtual queue** | Vendor SaaS | About 1.1 million patron accounts (name, email, phone, billing address, order history). Card data only inside the vendor's and payment partner's PCI environments | 186 venue user accounts: 175 sign in through the identity provider (SSO and MFA); **11 local accounts** with passwords and no MFA (4 marketing agency, 3 vendor support, 2 break-glass, 2 legacy integration). Vendor service provider AOC dated 2026-02-20; SOC 2 Type 2 (Security, Availability, Confidentiality; 12 months to 2026-03-31) |
| SYS-02 | Payment partner services for MID-T: gateway, tokenization, card vault for premium installments, chargeback portal, **virtual terminal**, and 18 standalone validated P2PE devices at the three box offices | Service provider, plus devices on premises | Card data | Box office devices are PCI-listed validated P2PE (since 2024). The virtual terminal is used by 26 staff on general-purpose laptops (gap) |
| SYS-03 | Food, beverage, and merchandise POS: 284 validated P2PE devices (176 fixed, 108 handheld) and the vendor's cloud back office | Vendor SaaS; devices on a vendor-managed network segment | Encrypted card data only (P2PE) | Manual card entry disabled |
| SYS-04 | Company website and content management system (CMS), with a SaaS **tag manager** | Company cloud workloads account; tag manager is SaaS | Patron sign-in passes to SYS-01; card data entered only inside the vendor's embedded form | Event pages embed the SYS-01 checkout form. **31 third-party scripts** load on those pages through the tag manager (gap) |
| SYS-05 | Cloud landing zone (4 accounts): identity and security; shared services (network hub, site-to-cloud VPN, log pipeline); workloads (website CMS, **patron data platform** with a nightly copy of about 1.1 million patron records through the SYS-01 API, **show settlement application**); backup (separate account) | Public cloud IaaS/PaaS (vendor-agnostic) | Patron data; settlement data | Immutable backups with 35-day write-once retention in the backup account |
| SYS-06 | Identity provider: single sign-on, MFA (push with number matching), conditional access | SaaS | No (identities only) | Federates email, productivity suite, cloud, SYS-01 (employees), CRM, finance, and HR |
| SYS-07 | Productivity suite (email, files, chat) | SaaS | Yes (patron emails; premium contracts) | |
| SYS-08 | Corporate and venue networks: SD-WAN across 4 sites, firewalls, switches, Wi-Fi | On premises; SD-WAN managed service | Card data typed into the virtual terminal crosses the corporate segment | Segments: corporate, production, POS (vendor managed), physical security (CCTV and door access), box office P2PE, public guest Wi-Fi |
| SYS-09 | Endpoints: 520 Windows and Mac laptops and PCs, 180 handheld ticket scanners managed through SYS-01, 64 tablets | Company-managed | Yes (cached exports) | EDR on all 520 laptops and PCs |
| SYS-10 | Physical security systems: 640 CCTV cameras with a video management system (VMS) at each venue, a **crowd analytics module** (AI-004) at the Amphitheater and the Music Hall since 2026-04, and door access control | On premises; integrator supported | Video; badge records | 30-day video retention |
| SYS-11 | Premium seating CRM | SaaS | Contacts and contracts of 410 premium accounts | P03 data discovery found full card numbers in notes fields (gap) |
| SYS-12 | Marketing platform: email and SMS, audience segments, **propensity scoring and generative copy features** (AI-005) | SaaS | Subscriber contact data and preferences | Receives segments from the patron data platform |
| SYS-13 | Finance, payroll, and HR | SaaS | Employee and vendor data | |
| SYS-14 | Production systems: lighting and audio consoles, video wall controllers | On premises | No | Standalone; touring crews connect to the production segment |
| SYS-15 | Guest service chatbot on the website (AI-003) | SaaS | Names, emails, order numbers, accessibility requests typed by patrons | Generative AI; launched 2026-02 |
| SYS-16 | SIEM and EDR console (MSSP-operated) | SaaS | Security logs | Ingests identity provider, cloud, firewall, and EDR logs. **Does not ingest** ticketing audit logs, CMS and tag manager changes, or payment partner portal activity (gap) |

**SSP system (P02):** the *Ticketing and Venue Operations Platform (TVOP)*: the company's tenant configuration, users, and API keys in SYS-01, the MID-T card channels in SYS-02 (virtual terminal users and box office P2PE devices), the website and tag manager (SYS-04), the cloud landing zone (SYS-05), the identity provider (SYS-06), the corporate and venue networks (SYS-08), endpoints and scanners (SYS-09), and the SIEM (SYS-16), with interfaces to SYS-03, SYS-07, SYS-10, SYS-11, SYS-12, SYS-13, and SYS-15.

## 4. Current security posture: a defined program with gaps in scale

**In place today:**
- A security program since 2024, led by the vCISO, with the Security Manager, 2 security analysts, and a GRC analyst; 5 policies adopted in 2024
- MFA through the identity provider for every employee on email, cloud, the ticketing platform (SSO), the CRM, and finance
- EDR on all laptops and PCs, monitored 24x7 by the MSSP; a SIEM for identity, cloud, firewall, and EDR logs
- Box office and food, beverage, and merchandise card acceptance on PCI-listed validated P2PE solutions, with manual entry disabled
- Premium installments charged from tokens in the payment partner's card vault
- A 4-account cloud landing zone with immutable backups in a separate backup account
- Quarterly external ASV scans of the website addresses (passing since 2024) and monthly internal vulnerability scans of cloud servers
- Annual security awareness training and quarterly phishing simulations
- An external penetration test of the website in 2025
- The ticketing vendor's service provider AOC (2026) and SOC 2 Type 2 report on file
- Bot mitigation, a virtual queue, and posted ticket limits for high-demand on-sales
- Background checks for finance, box office, call center, and premium sales staff
- A 2024 incident response plan (general, not PCI-specific)
- Cyber insurance with a breach hotline (fictional terms in section 7)

**Gaps found in the 2026 assessments:**
1. The PCI DSS scope has never been documented for a ROC (Requirement 12.5.2). The 2025 SAQ A for MID-T did not cover the virtual terminal channel or the website pages that embed the payment form.
2. Website event pages embed the ticketing checkout form and load 31 third-party scripts through the tag manager. There is no script inventory, authorization, or integrity check (6.4.3) and no change or tamper detection (11.6.1). The marketing agency has publish rights in the tag manager through local accounts with no MFA.
3. 26 premium, group sales, and call center staff key card numbers into the virtual terminal on general-purpose laptops on the corporate segment, which puts that segment and those laptops in the cardholder data environment.
4. Card numbers are stored where they should not be: 312 in premium seating CRM notes (9 with security codes) and 47 in mailbox attachments (P03 data discovery).
5. 11 local ticketing platform accounts bypass SSO and MFA; 2 belong to departed agency staff. The patron data platform's nightly sync uses a ticketing API key with full administrator scope, never rotated since 2024.
6. The SIEM does not receive ticketing audit logs, CMS or tag manager change history, or payment partner portal activity. The ticketing audit log keeps 90 days.
7. Access reviews are annual, not quarterly, and privileged access management covers only the cloud accounts.
8. No list of third-party service providers with PCI DSS responsibilities; the payment partner's AOC on file is from 2024; tag vendors and the agencies have never been assessed; agency contracts have no security terms.
9. Restores of the patron data platform and the settlement application have never been tested; written manual entry procedures exist only at the Amphitheater.
10. Production segments and the physical security segment at the venues are reachable from the corporate segment.
11. The 2024 policies have no supporting standards for configuration, logging, scripts, and service providers, and no targeted risk analyses.
12. Five AI uses were adopted by departments without a security, privacy, or legal review (P10). Dynamic pricing changed accessible seating prices on its own.
13. Website calendar listings and marketing emails show base ticket prices without mandatory fees (16 CFR 464.2).
14. The incident response plan has no card data compromise procedures; staff do not know the merchant agreement's 24-hour notice term; no exercise since 2024.
15. The County PAC agreement requires SOC 2 reports, and the company has never been audited against the Trust Services Criteria.

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
| 2026-03-16 | Acquirer letter: Visa Level 2; ROC for MID-T and SAQ P2PE for MID-F; due 2026-12-15 |
| 2026-06-30 | County PAC management agreement awarded |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (on-sale observed 2026-07-15; Amphitheater show night observed 2026-07-18) |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness, vendor report reviews, and AI assessment |
| 2026-09-15 | Deliverables approved (Chief Operating Officer; High risks and the risk appetite by the Chief Executive Officer); results to the audit committee |
| 2026-11-02 to 2026-11-13 | QSA ROC fieldwork |
| 2026-12-15 | ROC, AOCs, SAQ P2PE, and ASV scan reports due to the acquirer |
| 2027-06-30 | SOC 2 Type 1 report date (County PAC) |
| 2027-07-01 | County PAC operations begin; SOC 2 Type 2 observation period starts |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Sites and IT staff | HQ, the Music Hall, and the Club share one metro area; the Amphitheater is about a 2-hour drive away. The 14 IT and security staff are the IT Director, the Security Manager, 2 security analysts, the GRC Analyst, 4 infrastructure and cloud engineers, 3 service desk staff, and 2 venue technology technicians |
| Merchant agreement | The acquirer must be told within 24 hours of a suspected compromise of card data (fictional term) |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensics. Notice through the carrier hotline is required before incident vendors are engaged. Card brand assessments are covered only up to a $1 million sublimit |
| Ticketing vendor recovery | The vendor's SOC 2 system description states RTO 4 hours and RPO 15 minutes. Scanners can work offline from a manifest downloaded before doors |
| Event-day revenue | Average food and beverage sales per show: Amphitheater about $305,000, Music Hall about $67,000, Club about $18,000. About 70% of a show's food and beverage sales happen in the 2 hours around doors and the set break |
| Online sales | About 1,400 online ticket orders on an average day; the largest 2026 on-sale (an Amphitheater headliner on 2026-07-15) sold about 12,500 tickets in the first hour through the virtual queue |
| Website scripts | On 2026-07-20, 31 third-party scripts loaded on event pages that embed the checkout form: 19 analytics and advertising tags, 6 social and video embeds, 4 personalization and A/B testing tags, and 2 with no known owner. Tag manager publish rights: 9 users, including 4 marketing agency staff on local accounts without MFA |
| Virtual terminal | 26 users: 9 premium seating, 8 group sales, and 9 call center leads. The payment partner can supply validated P2PE devices that accept keyed phone orders (about $14,000 for 26 devices, fictional) |
| Card data discovery | Scan of the premium seating CRM, file shares, and mailboxes on 2026-07-22: 312 full card numbers in 141 CRM notes (9 with security codes), 47 in mailbox attachments of 6 users, none on file shares |
| Workforce activity | 96 employee terminations and 51 transfers in the 12 months to 2026-06-30; seasonal Amphitheater staff are added each March. The June 2026 phishing simulation click rate was 6.2% |
| MSSP | Contract requires a call to the Security Manager within 30 minutes of a high-severity alert |
| Ticket limits | Posted limit of 8 tickets per customer for high-demand on-sales, enforced per account. 22 high-demand on-sales in the 12 months to 2026-06-30 |
| County PAC | 2,400 seats; about 180 performances a year; the county receives monthly settlement statements and patron reports. The agreement requires notice to the county within 48 hours of a security incident affecting County PAC data or services |
| Terminology | "Ticketing and Venue Operations Platform (TVOP)" is the SSP system in P02, identifier CSC-TVOP-01 |
