# Scenario facts: Cris Santos Company | Accommodation and Food Services | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about the acquirer, the franchisor, the merchant agreements, the management agreement, and vendors are fictional.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (private; private equity-backed; board with an audit committee) |
| Business | Florida hotel owner and operator (NAICS 721110). Owns and operates **6 hotels with 1,160 rooms**: 2 independent full-service beach resorts and 4 franchised select-service hotels. Runs a central reservations office (CRO) and shared services (finance, HR, sales and marketing, revenue management, IT) from a corporate office |
| Hotels | **Resort 1** (Gulf Coast, 320 rooms, 3 restaurants, 3 bars, spa, retail, 40,000 square feet of meeting space). **Resort 2** (Atlantic coast, 280 rooms, 2 restaurants, 2 bars, spa, 25,000 square feet of meeting space). **Hotels 3 to 6** (select-service, 130, 140, 140, and 150 rooms, in central and north Florida; breakfast room and lobby market only) |
| Franchise status | **Mixed.** Resorts 1 and 2 are independent. Hotels 3 to 6 operate under franchise agreements with one national hotel brand (the franchisor). The franchisor mandates and hosts the property management system, central reservation system, and loyalty program for Hotels 3 to 6, mandates their payment gateway and terminals, and installs a brand-managed firewall at each of them. The company, as franchisee, is still the merchant of record and owns everything else at those hotels (PCs, switches, staff, procedures) |
| Location | Florida only: 6 hotels and the corporate office (with the CRO) in the Tampa Bay area. Hurricane season (June to November) is the main natural hazard for both coastal resorts |
| Workforce | 600 employees: Resort 1 about 230, Resort 2 about 190, Hotels 3 to 6 about 100 (about 25 each), corporate office and CRO about 80 (22 CRO agents). About 260 more workers (housekeeping, valet, security) are supplied by 2 staffing companies and are not employees |
| Revenue | About $100 million a year (fictional): rooms $78 million (Resort 1 $30 million, Resort 2 $24 million, Hotels 3 to 6 $24 million), food and beverage $17 million, other $5 million (spa, parking, retail, meeting space). Room revenue at the resorts includes a **mandatory $40 per night resort fee**. Not SBA-small: the standard for NAICS 721110 is $40.0 million in average annual receipts (13 CFR 121.201) |
| Guests | About 147,000 stays a year (about 61,000 at the resorts and 86,000 at Hotels 3 to 6). The resort PMS holds about 410,000 guest profiles created since 2019, including about 152,000 scanned identity documents. The cloud guest-marketing database (CRM) holds about 265,000 profiles with email consent |
| Card acceptance | About **1.05 million card transactions a year** under **10 merchant accounts (MIDs)** with one acquirer, which validates the company as one merchant: 2 per resort (rooms; food, beverage, spa, and retail), 1 per select-service hotel, and 2 e-commerce MIDs for the resort booking engine. About 48,000 card-not-present card numbers a year are keyed by CRO agents, about 30,000 online travel agency virtual cards are charged, and about 35,000 booking engine prepayments are taken |
| PCI DSS status | **Merchant.** PCI DSS v4.0.1 applies through the merchant agreement (contract, not law; N72-R01). The 2025 validation was an **SAQ D for Merchants** prepared internally and signed by the Chief Financial Officer. The acquirer's letter dated 2026-05-18 (fictional) requires, from the 2026 validation, an SAQ D prepared with the support of a Qualified Security Assessor (QSA) firm and signed by an officer, plus passing quarterly external scans by an Approved Scanning Vendor (ASV). The 2026 SAQ D and attestation of compliance are due **2026-12-31**. Card-brand merchant level thresholds were not verified from a card brand primary source, so no level number is stated in these documents |
| Payment design | **Resort front desks:** 14 PCI-listed validated P2PE devices, semi-integrated with the resort PMS through the resort payment gateway. **Resort 1 outlets:** cloud POS with 64 validated P2PE devices. **Resort 2 outlets:** a legacy on-premises POS (POS server, 38 POS workstations, 30 card readers); card data passes through the workstations and server before going to the processor over TLS, so this is **not** P2PE. **Hotels 3 to 6 front desks:** 12 brand-mandated chip terminals integrated with the brand PMS through the brand's gateway; not P2PE; on the hotels' flat staff networks. **CRO:** agents key card numbers from phone calls into the resort PMS payment field on general-purpose PCs. **Group sales and catering:** card authorization forms still arrive by email. **Online travel agency virtual cards:** delivered through the channel manager into the resort PMS card vault. **Booking engine:** a vendor-hosted payment form embedded in an inline frame (iframe) on the resort websites, which the company manages |
| Management agreement | On 2026-06-30 the company signed its first third-party **hotel management agreement** (fictional): from 2027-01-01 it will manage 2 hotels owned by a publicly traded lodging REIT, using its CRO, revenue management, accounting, and IT platform. The REIT requires a SOC 1 Type 2 report for accounting services and a **SOC 2 Type 2 report (Security, Availability, Confidentiality)** on the hotel management platform within 18 months of the start date |
| Not in scope | **SEC disclosure rules:** privately held. **HIPAA:** not a covered entity (the spas provide no medical services). **FTC Safeguards and Red Flags Rules:** no consumer credit is extended (direct billing to group clients is business credit). **Illinois BIPA (N72-R05):** no Illinois operations or employees. **Florida Digital Bill of Rights:** revenue far below the $1 billion controller threshold in Fla. Stat. 501.702. **Federal contracts:** none |
| Other applicable law | FTC Act Section 5, 15 U.S.C. 45(a) and (n) (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10, effective 2025-05-12), which covers short-term lodging and requires the total price, including mandatory fees, in any price display (464.1, 464.2); FTC Disposal Rule, 16 CFR 682.3 (N72-R03); FACTA receipt truncation, 15 U.S.C. 1681c(g); Florida guest register, **Fla. Stat. 509.101(2)**; Florida Information Protection Act, **Fla. Stat. 501.171** (N72-R04); Florida unconscionable pricing during a declared state of emergency, **Fla. Stat. 501.160** (P10); Florida interception law, **Fla. Stat. 934.03(2)(d)** (all-party consent; P10 call recording) |
| State law approach | Florida only for operations. Guests come from every state, so breach notice is treated generically ("each state where affected individuals reside") with Florida as the worked example |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board audit committee | Quarterly cyber risk and PCI status reporting |
| Chief Executive Officer | Accepts High risk; approves risk appetite and security budget |
| Chief Operating Officer | Executive sponsor of the security program; PMPS system owner; accepts Moderate risk |
| Chief Financial Officer | Owns the merchant agreement and acquirer relationship; signs the SAQ D; business owner of PCI DSS compliance; cyber insurance |
| General Counsel | Privacy lead; breach determinations with outside counsel; franchise and management agreements |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting |
| IT Director | Runs IT infrastructure and the corporate IT team (8 staff); PCI DSS technical lead |
| Security Manager plus 1 security analyst | Security operations, vulnerability management, MSSP oversight |
| GRC Analyst | Risk register, policies and standards, vendor reviews, evidence (the "small GRC function" with the Security Manager) |
| Director of Revenue Management | AI-001 business owner |
| Vice President of Sales and Marketing | Websites, guest chatbot (AI-002), CRM, group sales and card authorization forms |
| Director of Central Reservations | CRO, call recording and call analytics (AI-003) |
| HR Director | Hiring, background checks, timekeeping, applicant screening tool (AI-004) |
| Director of Loss Prevention and Safety | CCTV and video analytics (AI-005), physical security, emergency procedures |
| Hotel General Managers (6) | Operational owners at each hotel; downtime procedures |
| Resort Directors of Food and Beverage (2) | Outlet POS, P2PE device inspections at Resort 1, legacy POS at Resort 2 |
| Resort Chief Engineers (2) | Lock servers, building management systems, hurricane preparation |
| Internal audit (co-sourced firm) | Annual IT audit; the P07 assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring |
| Franchisor (brand) | Operates the brand PMS, central reservation system, loyalty program, gateway, and property firewalls for Hotels 3 to 6 |
| QSA firm | Engaged for the 2026 SAQ D support and a scoping review (October and November 2026) |

## 3. Systems
| ID | System | Hosting | Card or personal data? | Notes |
|---|---|---|---|---|
| SYS-01 | Resort property management system (PMS) with card vault, used by Resorts 1 and 2 and the CRO | Vendor SaaS | Guest profiles, ID scans, stay history, tokens; full virtual card numbers in the vendor's vault | Vendor holds a PCI DSS service provider AOC (2026-02) and a SOC 2 Type 2 report (Security and Availability, 12 months to 2026-03-31). 162 users through SSO with MFA; 46 have the "view full card number" permission |
| SYS-02 | Brand PMS, central reservation system, and loyalty platform for Hotels 3 to 6 | Franchisor-hosted | Guest and loyalty data; card data through the brand gateway | Operated by the franchisor under the franchise agreements. 64 company user accounts on brand-issued credentials with the brand's MFA |
| SYS-03 | Payment gateways and front desk payment devices | Service providers plus on-premises devices | Card data | 14 validated P2PE devices at the resort front desks; 12 brand-mandated chip terminals (not P2PE) at Hotels 3 to 6 |
| SYS-04 | Outlet point-of-sale (POS) systems at the resorts | Resort 1: vendor cloud POS; Resort 2: on-premises POS server | Card data (Resort 2 in clear on workstations and server) | Resort 1: 64 validated P2PE devices. Resort 2: legacy POS, server operating system out of vendor support, POS vendor has always-on remote support access. Replacement with a P2PE cloud POS planned for 2027 Q2 |
| SYS-05 | Booking engine and channel manager | Vendor SaaS | Card data on the booking engine side; virtual cards in transit through the channel manager | Booking engine payment form is embedded by iframe on the resort websites. Booking engine AOC 2026-01; channel manager AOC 2025-04 (expired for annual purposes) |
| SYS-06 | Property and corporate networks: SD-WAN at 7 sites | On-premises; SD-WAN managed service | Card data in transit | Resorts segmented into payment, POS, PMS workstation, door lock, building systems, CCTV, and office VLANs. Hotels 3 to 6: brand-managed firewall with **one flat staff network** behind it. Guest Wi-Fi at all hotels is a separate vendor-managed network (internet only) |
| SYS-07 | Endpoints | Company-managed | Yes: keyed card numbers pass through CRO browsers | 520 Windows PCs and laptops (430 at the corporate office, CRO, and resorts; 90 at Hotels 3 to 6) and 180 tablets and phones. EDR on 470 of 520 PCs |
| SYS-08 | Door lock systems | Resorts: on-premises lock servers; Hotels 3 to 6: lock vendor cloud service | Guest names and room assignments | 1,160 locks. Resort 2 lock server runs an operating system out of vendor support since 2024 |
| SYS-09 | Identity provider (single sign-on and MFA) | SaaS | No (identities only) | All corporate apps, email, cloud consoles, VPN, and SYS-01 users |
| SYS-10 | Cloud landing zone: 4 accounts (identity and security, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Guest CRM, data warehouse, call recordings | Workloads: data warehouse fed nightly by SYS-01 and SYS-02 extracts, guest CRM, integration services (chatbot, RMS, call analytics), resort websites |
| SYS-11 | Productivity suite (email, files, chat) | SaaS | **Yes: card authorization forms in group sales, catering, and accounting mailboxes** | 2,860 emails with card numbers found in P03 fieldwork |
| SYS-12 | SIEM (MSSP-operated) | SaaS | Security logs | Identity, email, cloud, EDR, and corporate and resort firewall logs. Not connected: Resort 2 POS server, lock servers, Hotels 3 to 6 |
| SYS-13 | Revenue-management system (AI-001) | Vendor SaaS | Aggregated stay data | Publishes rates automatically to SYS-01, the booking engine, and the channel manager for the resorts, and recommendations to the brand system for Hotels 3 to 6 |
| SYS-14 | Guest chatbot (AI-002) on the resort websites and text messaging | Vendor SaaS | Guest questions and contact details | Live since 2025-11; about 9,000 conversations a month |
| SYS-15 | CRO contact center with call recording and AI transcription and quality scoring (AI-003) | Vendor SaaS; recordings in SYS-10 | **Yes: spoken card numbers and security codes in recordings** | About 900 calls a day; recordings kept 13 months |
| SYS-16 | HR, payroll, timekeeping (14 finger-scan time clocks), and applicant tracking with AI screening (AI-004) | Vendor SaaS plus devices | Employee data; finger templates | Biometric data is personal information under Fla. Stat. 501.171(1)(g)1.a.(VI) |
| SYS-17 | CCTV video management at the resorts with video analytics (AI-005); building management systems | On-premises | Video | 30-day retention. Facial recognition feature available but disabled |
| SYS-18 | Third parties | Various | Varies | About 120 vendors; 31 store, process, or transmit card or guest data |

**SSP system (P02):** the *Property Management and Point-of-Sale Platform (PMPS)*: SYS-01, SYS-03, SYS-04, SYS-06, SYS-07, SYS-08, SYS-09, SYS-10, and SYS-12, including the company-managed property side of Hotels 3 to 6. Moderate baseline with tailoring. SYS-02 (the franchisor's platform) and the other systems are interconnected external services.

## 4. Current security posture: defined program with gaps in scale
**In place today:**
- Security program led by the vCISO; policies adopted in 2024; annual risk assessment (last June 2025); annual co-sourced internal IT audit
- MFA through the identity provider for all corporate apps, email, cloud consoles, VPN, and every SYS-01 user (since 2025)
- EDR with 24x7 MSSP monitoring on 470 of 520 PCs; SIEM for identity, email, cloud, EDR, and corporate and resort firewalls
- Validated P2PE devices at the resort front desks and at Resort 1's outlets
- Passing quarterly external ASV scans since Q1 2025
- Network segmentation at both resorts; guest Wi-Fi separated from staff networks at all hotels
- Immutable backups in a separate cloud backup account (35-day write-once retention)
- Annual security awareness training and quarterly phishing simulations
- Background checks for finance, IT, front office managers, and CRO agents
- Payment links replaced card authorization forms at the resort front offices in 2025
- Booking engine shows the total price including the $40 resort fee (changed in May 2025 for 16 CFR Part 464)
- Annual SAQ D (2025) signed by the CFO; cyber insurance

**Gaps:**
1. **PCI scope is larger than it needs to be.** Resort 2's legacy POS is not P2PE; the Hotels 3 to 6 terminals sit on flat staff networks; CRO agents key card numbers on general-purpose PCs. There is no current scope document or data-flow diagram for Hotels 3 to 6 and the CRO (PCI DSS 12.5.2).
2. **Stored card data outside the vault.** 2,860 emails with card numbers (418 with security codes) in group sales, catering, and accounting mailboxes back to 2022. CRO call recordings are kept 13 months and an estimated 31,000 of about 148,000 recordings contain spoken card numbers and security codes (3.3.1).
3. **Franchise shared responsibility is not defined.** There is no written PCI DSS responsibility matrix with the franchisor (12.8.5). The company cannot see the rules on the brand-managed firewalls, and the brand's network vendor has always-on remote access.
4. **Excess card visibility and slow access reviews.** 46 of 162 SYS-01 users can display full card numbers (8 need to). Access reviews are annual, not every 6 months (7.2.4). Night auditors at 3 franchised hotels share one brand PMS login.
5. **Vendor remote access.** The Resort 2 POS vendor and lock vendor use always-on remote tools without MFA. The privileged access broker covers only the cloud and SYS-01 administration.
6. **Logging gaps.** The Resort 2 POS server, both resort lock servers, and Hotels 3 to 6 do not send logs to the SIEM. CDE logs are not reviewed daily (10.4.1).
7. **Unsupported systems.** The Resort 2 POS server and Resort 2 lock server run operating systems out of vendor support.
8. **Testing gaps.** Internal vulnerability scans do not cover Hotels 3 to 6. The last segmentation test was in 2024 (11.4.5). Scripts on the resort website pages that embed the booking engine's payment form are not inventoried or monitored (6.4.3, 11.6.1).
9. **Third-party oversight.** Of 31 vendors that handle card or guest data, 9 have no current AOC or SOC 2 report, and compliance status is not checked each year (12.8.4).
10. **Recovery.** The SYS-01 contract has no recovery commitments; lock server, data warehouse, and CRM restores have never been tested; the IT parts of the hurricane plans cover only the resorts.
11. **AI adopted without governance.** Five AI uses went live without a security or privacy review. The RMS publishes rates with no emergency cap, and the chatbot quotes rates without the $40 resort fee (16 CFR 464.2).
12. **No retention schedule.** About 152,000 ID scans and all guest registers are kept indefinitely, although Fla. Stat. 509.101(2) only requires registers to be available for 2 years.
13. **Thin standards.** Policies exist (2024), but there are no configuration, logging, vendor, or payment device standards. Payment device inspections at Resort 2 and Hotels 3 to 6 are informal (9.5.1.2).

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | PCI DSS v4.0.1 at requirement-group level, with 21 defined requirements that decide scope or carry the largest risk, plus FTC Act Section 5, 16 CFR Part 464, the FTC Disposal Rule, FACTA truncation, and Florida rows (509.101(2), 501.171(2), (6)(a), and (8)). Evidence sampling |
| P08 | **Two incident types:** (1) POS and reservation system compromise: attackers enter through the Resort 2 POS vendor's remote tool, install memory-scraping malware on the legacy POS, and move to CRO PCs to capture keyed card numbers; discovered through an acquirer common-point-of-purchase alert. (2) Ransomware with guest data theft that disables resort PMS interfaces and lock servers. Both integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination (Security, Availability, Confidentiality) required by the REIT management agreement, plus a vendor SOC 2 and AOC review program |
| P10 | AI use-case portfolio: AI-001 revenue-management pricing, AI-002 guest chatbot, AI-003 CRO call recording with AI transcription and quality scoring, AI-004 applicant screening, AI-005 CCTV video analytics, AI-006 enterprise generative AI assistant. The registry default (pricing and chatbot) is kept and widened, because a mid-market operator runs several AI tools |
| Registry defaults | Primary system and incident type kept. The incident list adds ransomware as a second type because the tier calls for two |
| Cloud | Multi-account landing zone, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-18 | Acquirer letter on 2026 validation requirements |
| 2026-07-06 to 2026-07-31 | BIA, risk assessment, and gap analysis fieldwork (walkthroughs at all 6 hotels, 2026-07-13 to 2026-07-24) |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit) |
| 2026-08-24 to 2026-09-04 | SOC 2 readiness, vendor report reviews, and AI assessment |
| 2026-09-15 | Results to the audit committee; deliverables approved |
| 2026-10-05 to 2026-11-20 | QSA-supported PCI DSS assessment and scoping review |
| 2026-12-31 | 2026 SAQ D and attestation of compliance due to the acquirer |
| 2027-01-01 | REIT management agreement starts |
| 2027-04-01 to 2027-09-30 | Planned SOC 2 Type 2 observation period |

## 7. Facts added during the Phase 5 build (fictional; used across P01-P10)
These details were added so the deliverables could be specific. They do not change sections 1-6.

| Topic | Added fact |
|---|---|
| Revenue per day | About $274,000 a day in total: Resort 1 about $82,000 rooms and $32,000 food, beverage, and other; Resort 2 about $66,000 rooms and $25,000 food, beverage, and other; Hotels 3 to 6 about $66,000 rooms in total (about $16,500 each) and $3,000 other. The CRO books about 22% of resort room revenue (about $33,000 a day) |
| Arrivals | About 400 arrivals a day: Resort 1 about 89, Resort 2 about 78, Hotels 3 to 6 about 59 each. Most arrive between 15:00 and 22:00 |
| SYS-01 recovery commitments | The SYS-01 vendor's SOC 2 system description states RTO 4 hours and RPO 15 minutes. The contract states none. Each resort front desk prints an arrivals and in-house list at night audit and every 4 hours during the day |
| Franchise agreement terms | The franchise agreements (fictional terms) require the franchisee to follow the brand's IT and PCI standards, to report any suspected compromise of brand systems or guest data to the franchisor within 24 hours, and to allow the brand's network vendor remote access to the property firewall. They do not allocate PCI DSS requirements between the parties |
| Workforce activity | 212 terminations and 70 internal transfers in the 12 months to 2026-06-30. The last access review of SYS-01 was completed in February 2026. The June 2026 phishing simulation click rate was 6.1% |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensic firms. Notice through the carrier hotline is required before incident vendors are engaged |
| MSSP | 24x7 monitoring; must call the Security Manager within 30 minutes of a high-severity alert |
| Backups | Daily backups of the workloads account to the backup account, 35-day write-once retention, separate administrator credentials. Resort lock servers are backed up weekly to a local disk only |
| Management agreement | The REIT management agreement (fictional terms) requires notice to the owner within 48 hours of a suspected security incident affecting the managed hotels' data or systems, and makes the company a third-party agent for the owner's guest data |
| Additional role titles | Director of Finance (controller function); Director of Group Sales; Resort Front Office Managers (2); Hotel night auditors; Director of Marketing; Corporate Communications Manager |
| Other operating details | The CRO handles about 900 calls a day and books about 210 reservations a day. SYS-01 has 31 roles. The data warehouse receives a nightly extract of about 1.2 million folio lines a month. 12 of the 31 card and guest-data vendors are Tier 1 under the P09 tiering approach. Card authorization forms found: 2,860 emails across 6 shared mailboxes (sales, catering, and accounting). Counsel's view on CCPA (2026-07-28): revenue exceeds the CCPA threshold, but the company has no California presence; whether online marketing to California residents is "doing business in California" is unsettled, so CCPA is a watch item |
