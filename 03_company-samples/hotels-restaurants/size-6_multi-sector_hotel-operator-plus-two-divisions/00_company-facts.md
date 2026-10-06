# Scenario facts: Cris Santos Company | Accommodation and Food Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about acquirers, card brand contract terms, management agreements, owners' associations, and vendors are fictional unless a source is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; hospitality, leisure, and vacation ownership group) |
| Structure | A holding company with three divisions, each a separate subsidiary, plus corporate shared services in the parent |
| Division 1: Hotels (NAICS 721110), **focus of this scenario** | Cris Santos Hotels, LLC. Owns, leases, and manages **88 full-service and resort hotels (about 36,400 rooms)** under two group brands in 11 states: **30 owned or leased** (about 12,600 rooms, including the 3 resort hotels at the group's Florida destination resort) and **58 managed for third-party owners** (about 23,800 rooms, 41 ownership groups). **No franchising.** About 25,000 employees, including the staff of managed hotels, who are company employees under the management agreements. About 9.8 million room nights a year |
| Division 2: Attractions and Entertainment (NAICS 713110, sector 71 Arts, Entertainment, and Recreation) | Cris Santos Parks and Attractions, LLC. A Florida destination resort with **2 theme parks and 1 water park**, plus **4 regional parks** in Texas, Georgia, Tennessee, and Ohio. About 24 million visits a year and about 820,000 annual passholders. About 11,500 employees at peak, including seasonal staff. **No casino or gaming** |
| Division 3: Resort Real Estate and Vacation Ownership (NAICS 531210 and 531311, sector 53 Real Estate and Rental and Leasing) | Cris Santos Vacation Ownership, Inc. and its consumer finance subsidiary, Cris Santos Vacation Finance, LLC (the **finance subsidiary**). Develops and sells vacation ownership (timeshare) interests at **24 resorts (about 5,600 units)** in 6 states, manages the 24 owners' associations, runs a points and reservation program for about **410,000 owner families**, and finances purchases (about **126,000 active consumer loans**, about $2.8 billion). **Joined the group by acquisition on 2024-07-01.** About 6,500 employees |
| Corporate shared services | Identity, network, security operations, cloud platform, group payment services, the unified guest identity and loyalty platform, finance, HR, and legal. About 2,000 employees |
| Location | Headquartered in central Florida. Operations in 12 states (Florida, Georgia, South Carolina, North Carolina, Tennessee, Texas, Ohio, Arizona, Colorado, Nevada, California, and Hawaii); guests, visitors, and owners live in every state. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about **$18.0 billion** revenue (fictional): Hotels about $7.45 billion; Attractions about $5.60 billion; Vacation Ownership about $4.95 billion |
| Card acceptance | About 57 million card transactions a year: Hotels about 13.9 million (rooms 3.6 million, food and beverage 10.3 million); Attractions about 41 million (tickets, food, merchandise); Vacation Ownership about 2.6 million (down payments, maintenance fees, rentals). Loan and maintenance-fee autopay runs by ACH |
| PCI DSS status | PCI DSS v4.0.1 applies by contract to every division (N72-R01, N71-R04, N53-R04). **Hotels:** merchant with Acquirer A (annual QSA Report on Compliance (ROC) required by contract; 2025 ROC dated 2025-11-14, compliant with 4 compensating controls; 2026 ROC due **2026-11-30**) and **service provider** to the owners of the 58 managed hotels, who are the merchants of record but whose payment systems the division operates (service provider ROC dated 2026-03-20). **Attractions:** merchant with Acquirer B (QSA ROC; 2025 ROC dated 2025-12-05; 2026 ROC due **2026-12-15**). **Vacation Ownership:** merchant with Acquirer C (annual SAQ D for Merchants; 2026 SAQ due **2026-12-31**). Card-brand level thresholds were not verified from a card brand primary source, so no level number is stated |
| Franchise model and FTC v. Wyndham | The group does not franchise. It **manages** 58 hotels for owners and designs, connects, and operates their PMS, POS, payment, and property networks. In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a hotel franchisor that managed its branded hotels' PMS systems. The alleged failures included card data in clear text, easily guessed and default passwords, no firewalls between hotel PMS systems, the corporate network, and the internet, an out-of-date operating system, no inventory, unrestricted vendor access, and weak incident response. **The group carries these duties for every hotel system it manages for an owner** |
| Not in scope | **Gaming rules** (Nevada Gaming Commission Regulation 5.260, NIGC 25 CFR 543.20, BSA casino program rules): no casino or gaming at any park or resort. **Illinois BIPA (N72-R05):** no Illinois operations and no biometric collection in Illinois; its text was not verified. **HIPAA:** park first-aid stations do not bill health plans electronically, so the group is not a covered entity. **Florida Digital Bill of Rights:** not a "controller" under Fla. Stat. 501.702 (revenue exceeds $1 billion, but the group does not earn 50% or more of revenue from online advertising, operate a consumer smart speaker and voice command service, or operate an app store with at least 250,000 applications). **Federal contracts:** none. **Bank regulation:** the finance subsidiary is not a bank and is subject to the FTC's GLBA rules |
| State law approach | Florida law is the worked example. Other states are treated generically |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board of directors: audit committee and risk committee | Cyber oversight (Reg S-K Item 106 governance disclosure); the risk committee accepts Very High risks |
| Chief Executive Officer; Chief Financial Officer | Take part in materiality determinations with the disclosure committee |
| Disclosure committee (Group General Counsel chairs) | SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Group CISO | Owns the group security program and group policies; runs common controls through SYS-G1 to SYS-G4 |
| Group Chief Risk Officer | Group risk register and enterprise risk management (NIST IR 8286 Rev. 1); chairs the Group AI council |
| Group Chief Privacy Officer | Privacy program, guest data purpose rules, breach determinations with counsel |
| Group General Counsel | Notification matrix, management agreements, owners' association agreements, disclosure committee chair |
| Group Director of Payments and PCI Compliance | One group PCI DSS program across three merchant validations and the Hotels service provider validation; reports to the Group CISO |
| Division security and compliance leads (3) | Division registers, division supplements, division regulators. The **Vacation Ownership lead is the finance subsidiary's Qualified Individual** under 16 CFR 314.4(a) |
| Finance subsidiary president and board | Senior officer who directs and oversees the Qualified Individual (314.4(a)(2)); the board receives the Qualified Individual's annual report (314.4(i)) and approves the Identity Theft Prevention Program (16 CFR 681.1(e)(1)) |
| Attractions digital products director | Coordinates the children's information security program for the kids' club (16 CFR 312.8(b)(1)) |
| Group internal audit (third line; reports to the audit committee), with a co-source firm | Assesses common controls once; samples division controls |
| Group AI council (formed 2026-03) | Approves High-tier AI use cases and the approved-tools list |

## 3. Systems
| ID | System | Owner | Notes |
|---|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate | About 38,500 workforce identities plus about 6,200 contractor and vendor identities. Vacation Ownership's 6,500 users stay on the division's legacy directory until 2027-03-31 |
| SYS-G2 | Group SOC, SIEM, and EDR | Corporate | 24x7 in-house SOC with a managed security service provider (MSSP) for overflow |
| SYS-G3 | Group cloud platform (Cloud provider A primary, Cloud provider B for disaster recovery and backup; vendor-agnostic) and group network (SD-WAN to every property, hubs in two colocation data centers) | Corporate | Landing zones, guardrails, log archive, key management, immutable backup vault |
| SYS-G4 | Group payment services: payment tokenization service, card vault, payment gateway integration, and the hosted payment form | Corporate | A shared cardholder data environment (CDE) account in Cloud provider A, used by all three divisions; about 11.8 million active tokens |
| SYS-G5 | Unified guest identity and loyalty platform: guest profile hub ("one account" for hotel guests, park visitors, and owners) and the loyalty program | Corporate | About 52 million guest profiles; about 11.4 million loyalty members; member sign-in with optional MFA |
| SYS-G6 | ERP, HR and payroll | Corporate | SOX-relevant |
| SYS-H1 | Hotel cloud PMS (vendor SaaS, multi-property tenant administered by the Hotels division) | Hotels | All 88 hotels; about 14,800 PMS users |
| SYS-H2 | Central reservation system (CRS), brand website and app booking engine, channel connectivity, and the reservations contact center (tone-masking card capture) | Hotels | Company-built on Cloud provider A; about 900 contact center agents |
| SYS-H3 | Hotel POS estate | Hotels | 214 food and beverage outlets: 142 on a cloud POS with validated P2PE devices; **72 outlets at 23 hotels on a legacy integrated POS** with on-property POS servers |
| SYS-H4 | Property networks and hotel building technology (door locks, guest Wi-Fi, IPTV) | Hotels | SD-WAN edge and firewalls at 88 hotels |
| SYS-H5 | Revenue-management system (vendor SaaS, AI) and the guest chatbot (vendor generative AI) | Hotels | See P10 |
| SYS-A1 | Ticketing, annual pass, and park access platform (vendor platform configured by Attractions), including finger-scan gate validation at the 3 Florida parks | Attractions | Online ticket store uses the SYS-G4 hosted payment form |
| SYS-A2 | Park POS | Attractions | 430 points of sale at 7 parks: 334 on the cloud POS with validated P2PE; **96 merchandise kiosks and food carts at the 2 Florida theme parks on the same legacy integrated POS as the hotels** |
| SYS-A3 | Park mobile app: tickets, virtual queue, mobile food ordering, maps with opt-in precise location, and the "Junior Explorers" kids' club | Attractions | Kids' club launched 2025-11 |
| SYS-A4 | Ride and show control systems (operational technology) | Attractions | Isolated networks at 7 parks; safety-critical |
| SYS-V1 | Vacation ownership sales platform (CRM, tour booking, contracting, and closing) at 38 sales galleries | Vacation Ownership | 6 galleries are inside group hotels and 2 at the Florida destination resort |
| SYS-V2 | Loan origination (in-house, with an AI credit model) and loan servicing (vendor SaaS) | Vacation Ownership (finance subsidiary) | Consumer reports, Social Security numbers, bank accounts; **legacy loan document archive** on a file server in the division's legacy data center |
| SYS-V3 | Owner services: points and reservation platform, owner portal, owners' association management and maintenance-fee billing | Vacation Ownership | About $1.1 billion in maintenance fees billed each year for 24 associations |
| SYS-V4 | Inventory forecasting and rental model | Vacation Ownership | Reserves unused owner inventory for rental through SYS-H2 |

**SSP system (P02):** the *Hotel Property Management and Point-of-Sale Platform (PMPS)*: the Hotels division's cloud PMS tenant (SYS-H1), the hotel POS estate (SYS-H3), and the property payment network segments at the 88 hotels (part of SYS-H4), with interfaces to SYS-H2, SYS-G4, and SYS-G5. It inherits common controls from SYS-G1 to SYS-G4.

## 4. Current security posture: varies by division
**In place today:**
- Group policies aligned to CSF 2.0 and PCI DSS v4.0.1; a group common control catalog
- 24x7 group SOC with EDR on corporate, hotel, and park endpoints
- PAM and MFA for workforce access through SYS-G1 (except Vacation Ownership's legacy directory)
- Tokenization of stored card data in SYS-G4; tone-masking card capture in the contact center
- Validated P2PE at 71 of 88 hotel front desks, 142 of 214 hotel outlets, and 334 of 430 park points of sale
- Annual QSA ROCs for Hotels (merchant and service provider) and Attractions
- Quarterly ASV scans; annual penetration tests; immutable backups in Cloud provider B
- Quarterly access certification for SYS-G1-connected systems
- Total price display, including resort fees, on brand websites and apps since 2025-05 (16 CFR Part 464)
- SEC Item 106 disclosure in the annual report

**Gaps (found in the 2026 assessments):**
1. **Legacy POS and its vendor.** 72 hotel outlets at 23 hotels and 96 park kiosks and carts at the 2 Florida theme parks run the same legacy integrated POS. Card data is in clear text in POS memory before it reaches the gateway. The POS vendor's always-on remote support tool reaches every legacy POS server outside group PAM, and the vendor's support terms do not allow EDR on those servers. P2PE replacement is 61% complete and due 2027-06-30.
2. **Guest profile hub mixes division data.** SYS-G5 holds hotel guests, park visitors, and owners in one store. A "payment preferences" table synced from SYS-V3 in 2025 holds full bank account and routing numbers for about 212,000 owners enrolled in autopay. The CRS integration service account used by PMS and POS loyalty lookups can read the whole hub. Hotel and park guest data feed vacation ownership tour marketing although the hotel and park privacy notices do not say so clearly.
3. **Vacation Ownership Safeguards Rule program.** The division still runs its own directory and email; 340 sales gallery and loan processing users reach the loan origination platform without MFA and without the Qualified Individual's written approval of an equivalent control (16 CFR 314.4(c)(5)); the legacy loan document archive (about 3.1 million scanned contracts and credit applications) is not encrypted at rest (314.4(c)(3)); 12 of 31 service providers with customer information have not been assessed (314.4(f)); the incident response plan has no FTC notification step (314.4(j)); the 2026 penetration test excluded the legacy data center.
4. **Kids' club (COPPA).** The Junior Explorers kids' club (about 96,000 child profiles) has no written children's information security program as required since 2026-04-22 (16 CFR 312.8(b)) and no written retention policy (312.10). Parents consent once by email, and the same consent covers sharing game activity with a marketing analytics vendor.
5. **Biometric gate data.** About 640,000 passholders and multi-day ticket holders at the 3 Florida parks have finger-scan templates held in the gate vendor's cloud with no deletion after the pass expires. Biometric data is personal information under Fla. Stat. 501.171(1)(g)1.a.(VI).
6. **Managed hotel agreements.** 31 of 58 management agreements were signed before 2020 and do not assign security responsibilities or incident notice duties to owners. Owners have not all received the PCI DSS responsibility matrix (Requirement 12.9).
7. **Division supplements and inheritance.** Vacation Ownership still follows its pre-acquisition (2023) standards, and its inheritance of group common controls is not documented. Attractions' supplement does not cover ride control networks.
8. **Shared incident notification.** A cross-division incident may trigger three acquirers and the card brands, managed hotel owners, FTC Safeguards Rule notice, state breach laws, and an SEC materiality decision. The multi-regulator matrix has not been exercised.
9. **Ride control networks.** The 2026-05 penetration test found that ride and show control networks at 2 of 7 parks are reachable from the park business network through a vendor maintenance jump host.
10. **AI governance.** 11 AI use cases; 6 reviewed by the Group AI council since it formed in 2026-03. The hotel guest chatbot quotes nightly rates without the mandatory resort fee at 6 resort hotels; the Vacation Ownership credit model's adverse action reasons are not always specific (12 CFR 1002.9(b)(2)); the inventory forecasting model keeps no decision records (Fla. Stat. 721.13(12)(c)).
11. **Third parties.** About 1,400 vendors; 140 are high risk. Vacation Ownership's vendor reviews lapsed after the acquisition.
12. **Retention.** The guest profile hub keeps all 52 million profiles indefinitely, including about 7.9 million with identity document numbers.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Each division's primary regulation: PCI DSS v4.0.1 for Hotels (focus, merchant and service provider) and Attractions (with COPPA); the FTC Safeguards Rule (16 CFR Part 314) for Vacation Ownership (with the Red Flags Rule and Fla. Stat. 721.13). Group-wide obligations: SEC disclosure, state breach and privacy laws, FTC Act Section 5, and 16 CFR Part 464. Regulation-by-division matrix |
| P08 | Point-of-sale and reservation system compromise spanning divisions: an attack through the shared legacy POS vendor reaches hotel and park POS, and a stolen CRS integration credential exposes the guest profile hub, including owners' bank account data. Card brands through three acquirers, owners, FTC Safeguards Rule notice, state laws, and SEC materiality |
| P09 | SOC 2 scoped per division: Hotels SL-1 hotel management technology services to owners (in scope); Vacation Ownership SL-2 owners' association management services (in scope); Attractions out of scope, with reasons |
| P10 | Group AI governance program. The registry default (revenue-management pricing and guest chatbot) is kept as the Hotels division's priority use cases, because both run at scale; division use cases add regulator-specific rules (credit decisions, timeshare inventory reservations, ticket pricing) |
| Cloud | Shared corporate platform (Cloud provider A and Cloud provider B, vendor-agnostic) plus division workloads, two colocation data centers, and SaaS |
| Registry defaults | Primary system and incident kept; the incident was widened to span divisions because the legacy POS vendor and the guest profile hub are shared (gaps 1 and 2) |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-04-27 to 2026-05-08 | Annual penetration and segmentation tests by an independent testing firm (the Vacation Ownership legacy data center was excluded) |
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment and division samples (group internal audit) |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness and AI program review (Group AI council met 2026-08-26) |
| 2026-09-10 | Results to the board risk committee and audit committee; deliverables approved |
| 2026-10-19 to 2026-11-13 | QSA fieldwork for the Hotels 2026 merchant ROC (planned) |
| 2026-11-30 | Hotels 2026 ROC and AOC due to Acquirer A |
| 2026-12-15 | Attractions 2026 ROC and AOC due to Acquirer B |
| 2026-12-31 | Vacation Ownership 2026 SAQ D and AOC due to Acquirer C |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Placeholder | Filled in at the end of the build |
