# Scenario facts: Cris Santos Company | Accommodation and Food Services | Enterprise

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about acquirers, card brands' contract terms, franchise and management agreements, and vendors are fictional unless a source is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; hotel franchisor, manager, and owner) |
| Business | Hotel company (NAICS 721110) that **franchises, manages, and owns** hotels under four brands: a full-service brand, a select-service brand, an extended-stay brand, and a resort collection (acquired 2025-06). It also runs the brand's central reservation system, loyalty program, and technology services for franchised hotels |
| Portfolio | **750 hotels, about 96,000 rooms**, in 33 states and the District of Columbia: 38 owned or leased, 72 managed for third-party owners, and 640 franchised. The 110 owned, leased, and managed hotels are **company-operated** (about 34,000 rooms); the 640 franchised hotels (about 62,000 rooms) are independently owned and operated by franchisees |
| Location | Headquartered in Florida. Florida is the largest state (118 hotels, 27 of them company-operated). **State law is handled generically:** apply the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 1,450 at headquarters and two regional offices, about 650 in the central reservations contact center (Florida and Texas), and about 9,900 at the 110 company-operated hotels. Staff at franchised hotels are franchisee employees, not company employees |
| Revenue | About **$4.8 billion** a year (fictional): owned and leased hotel revenue $2.05 billion (rooms $1.38 billion, food and beverage $0.52 billion, other $0.15 billion); management and franchise fees $0.62 billion; cost reimbursements (brand system fund for reservations, marketing, and loyalty, plus reimbursed payroll at managed hotels) $1.93 billion; other $0.20 billion (co-brand credit card license fees and technology service fees) |
| Guests | About 24.5 million room nights a year system-wide. The guest profile hub holds about **61 million guest profiles**; about 8.7 million include identity document numbers captured at company-operated hotels. The loyalty program has about **14.2 million members** |
| Card acceptance | Company-operated hotels run about **14.6 million card transactions a year** (rooms about 4.1 million; food and beverage about 10.5 million). Owned and leased hotels use the company's merchant accounts; managed hotels use their owners' merchant accounts, but the company operates every payment system under the management agreements and includes them in its own PCI DSS program (EV-043, EV-038) |
| PCI DSS status | **Both a merchant and a service provider**, determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (N72-R01): PCI DSS v4.0.1 applies by contract (EV-038, EV-030). (a) **Merchant:** the acquirer agreement (fictional term) requires an annual Report on Compliance (ROC) by a Qualified Security Assessor (QSA); the 2025 merchant ROC (dated 2025-11-21) was compliant with 3 compensating controls; the 2026 ROC and attestation of compliance (AOC) are due **2026-11-30**. (b) **Service provider:** the central reservation system stores guarantee card data for franchised hotels and the company administers the brand property management system (PMS) tenant, the payment tokenization service, and the managed property network for franchisees, so the company validates as a service provider with a QSA ROC (dated 2026-03-27) and gives franchisees its service provider AOC. Card-brand merchant and service provider level thresholds were not verified from a card brand primary source, so no level number is stated in these documents |
| Payment design | **Central reservation system (CRS):** guarantee and prepayment cards from the brand website, app, contact center, and channel connections are tokenized by the company's tokenization service and stored in the card vault (Cloud provider A, a dedicated cardholder data environment account). **Contact center:** card numbers are captured by keypad through a tone-masking service (service provider), so agent desktops never see them. **Front desk at company-operated hotels:** PCI-listed validated point-to-point encryption (P2PE) terminals at 82 of 110 hotels; 28 hotels (including the 9 resorts still on the seller's systems) use semi-integrated chip terminals that are not P2PE. **Food and beverage at company-operated hotels:** 264 outlets; 153 on a cloud POS with validated P2PE devices; **111 outlets at 41 hotels still on a legacy integrated POS** with on-property POS servers. **Franchised hotels:** each franchisee is its own merchant and must use a brand-approved payment solution. Sources: EV-011, EV-012, EV-043 |
| Franchise model and duties | Brand standards require franchisees to use the brand cloud PMS and the CRS, to use a brand-approved payment solution, and to validate PCI DSS and submit an AOC every year. 410 of 640 franchised hotels also subscribe to the **managed property network service**, which connects their property networks to the company's network hubs (EV-039, EV-013). In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a hotel franchisor that managed its branded hotels' PMS systems. The alleged failures included card data in clear text, easily guessed and default passwords, no firewalls between hotel PMS systems, the corporate network, and the internet, an out-of-date operating system, no inventory, unrestricted vendor access, and weak incident response. **The company carries these duties for every system it designs, connects, or manages for franchisees** |
| Added at this size | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls over ERP, payroll, and owner and franchise fee accounting; two service lines offered to external clients (SOC 2); growth by acquisition (resort collection, 14 resorts, closed 2025-06) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv), with counsel's review (EV-056). **HIPAA:** not a covered entity. **FTC Safeguards and Red Flags Rules:** the company extends no consumer credit; the co-brand credit card is issued by a bank. **Florida Digital Bill of Rights:** not a "controller" under Fla. Stat. 501.702 (revenue exceeds $1 billion, but the company does not earn 50% or more of revenue from online advertising, operate a consumer smart speaker and voice command service, or operate an app store with at least 250,000 applications). **Federal contracts:** none; government travelers book like any guest. **CIRCIA:** proposed only (N72-R06); the company exceeds the SBA size standard, so it would be covered by the proposed size-based criterion if the rule is finalized as proposed |
| Other applicable law | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): FTC Act Section 5 (15 U.S.C. 45(a), (n)) for guest data security, privacy statements, and pricing claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066 (rule text at 2166), published 2025-01-10, effective 2025-05-12), which covers short-term lodging and requires the total price, including mandatory resort and destination fees, in any price display (464.1, 464.2); FTC Disposal Rule, 16 CFR 682.3 (N72-R03); state breach notification laws (N72-R04), Florida worked example Fla. Stat. 501.171; Florida guest register, **Fla. Stat. 509.101(2)**; state comprehensive privacy laws, including the CCPA (revenue above $26,625,000) and its cybersecurity audit regulations (11 CCR 7120-7124); state price gouging laws during declared emergencies (Florida worked example Fla. Stat. 501.160) |
| State law approach | Florida law is the worked example. Other states are treated generically ("each state where affected individuals reside") |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board (audit committee plus a risk committee) | Cyber oversight (Item 106 governance disclosure) |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risk; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner; reports to the CEO and quarterly to the board risk committee |
| Director of Payments and PCI Compliance | PCI DSS program manager for the merchant and service provider ROCs; reports to the CISO |
| Chief Privacy Officer | Privacy program, breach determinations |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Commercial Officer | Revenue management, distribution, digital channels, and loyalty (AI-001 and AI-002 executive owner) |
| GRC team (9), Security Operations Center (24x7, in-house plus MSSP overflow), Internal Audit (in-house, with a co-source firm for specialist testing) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Notes |
|---|---|---|
| SYS-01 | Central reservation system (CRS) and guest profile hub | Company-built on Cloud provider A; about 38 million reservation transactions a year; 61 million guest profiles |
| SYS-02 | Brand cloud PMS (vendor SaaS, multi-property tenant administered by the company) | 741 of 750 hotels; the 9 resorts still on the seller's legacy PMS migrate by 2027-03-31 (EV-025, EV-026) |
| SYS-03 | Payment tokenization service, card vault, and payment gateway integration | Company-operated cardholder data environment on Cloud provider A; about 6.2 million active card tokens |
| SYS-04 | POS estate at company-operated hotels | 153 outlets on a cloud POS with validated P2PE; 111 outlets at 41 hotels on a legacy integrated POS (EV-011) |
| SYS-05 | Property networks and the managed property network service | SD-WAN and firewalls at the 110 company-operated hotels and the 410 subscribing franchised hotels; hubs in two colocation data centers and the cloud |
| SYS-06 | Brand website, mobile app, booking engine, and guest chatbot | Company-built booking engine with an embedded tokenization payment form |
| SYS-07 | Loyalty and CRM platform (vendor SaaS) | 14.2 million members; member sign-in with optional MFA (EV-047) |
| SYS-08 | Channel connectivity (distribution switch to online travel agencies and global distribution systems) | Third-party switch; virtual cards delivered to the CRS vault |
| SYS-09 | Identity platform (SSO, MFA, privileged access management, identity governance) | About 12,000 workforce identities plus about 26,400 franchisee staff accounts for the PMS and CRS |
| SYS-10 | Endpoints at offices and company-operated hotels | About 21,000 PCs, POS workstations, tablets, and kiosks |
| SYS-11 | Hotel building and guest-room technology | Door lock systems, building management, guest Wi-Fi, and IPTV at company-operated hotels |
| SYS-12 | ERP, payroll and timekeeping, and owner and franchise fee accounting | SOX-relevant |
| SYS-13 | Contact center platform (CCaaS) with tone-masking card capture | About 650 agents |
| SYS-14 | Data platform on Cloud provider B and the revenue-management system (vendor SaaS) | Warehouse, analytics, AI services |
| SYS-15 | About 1,100 third-party vendors (86 with card data or guest personal information at volume) | Tiered third-party risk program (EV-036) |
| SYS-16 | AI portfolio (12 use cases) | Governed by an AI governance committee formed in 2025 (EV-049, EV-050) |

**SSP system (P02):** the *Property and Payment Platform (PPP)*: the company-administered brand cloud PMS tenant and its interfaces (SYS-02), the payment tokenization service and card vault (SYS-03), the POS estate at company-operated hotels (SYS-04), and the property payment network segments (part of SYS-05), with interfaces to SYS-01, SYS-06, SYS-08, and SYS-13. It is the company's highest-value system for card data and hotel operations, and it inherits common controls from the enterprise platform.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. At this size the sources are enterprise systems of record across the business: the identity platform and HR system, the CMDB, the EDR and network consoles, the cloud consoles and SIEM, the PCI DSS program library and ROCs, the third-party risk register and accounts payable vendor master, the contract repository and franchise AOC tracker, board and committee records, prior Internal Audit and QSA work, and the AI governance committee register.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv), reviewed by the General Counsel's office (EV-056).
- **Gaps against PCI DSS and the other applicable rules** are judged in the gap analysis (P03), and **whether controls work** is tested by Internal Audit in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | PCI DSS v4.0.1 as merchant and service provider (primary), plus every other applicable regulation across the enterprise, with evidence sampling |
| P08 | POS and reservation system compromise through a vendor remote access tool, including an **SEC materiality assessment and 8-K Item 1.05** step, card brand reporting, franchisee and owner notices, and a multi-state breach-notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to external clients: SL-1 franchise technology services and SL-2 independent hotel distribution services |
| P10 | Enterprise AI portfolio (12 use cases) with the AI governance committee operating model; full assessments of AI-001 revenue-management pricing and AI-002 guest chatbot (the registry default, kept because both are in production at scale) |
| Cloud | Multi-cloud (vendor-agnostic, Cloud provider A and Cloud provider B) plus two colocation data centers, with common controls |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-05-29 | Intake: evidence requests, exports from systems of record, inventories, obligations register (reviewed by counsel) |
| 2026-05-11 to 2026-05-22 | Annual penetration test and segmentation test (independent testing firm); its report was collected at intake |
| 2026-06-01 to 2026-07-31 | Enterprise BIA update, risk analysis, and gap analysis |
| 2026-06-22 to 2026-07-10 | 2026 annual revision of POL-01 to POL-05 and the policy hierarchy drafted from the intake evidence and early risk and gap results |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line; GRC team supported scoping): operating tests of controls in force under the 2025 policy set; design review of the draft 2026 revisions |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness and AI portfolio review (AI governance committee met 2026-08-19) |
| 2026-09-10 | Results to the audit committee and the risk committee; 2026 policy revisions approved (effective 2026-10-01) |
| 2026-10-19 to 2026-11-13 | QSA fieldwork for the 2026 merchant ROC (planned) |
| 2026-11-30 | 2026 merchant ROC and AOC due to the acquirer |
| 2027-03 (planned) | Internal Audit follow-up: operating effectiveness of the controls the 2026 revisions and POA&M items introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added while building P01 to P10. They do not change sections 1-6. All are fictional unless a source is cited.

**Registry defaults.** The registry's primary system ("property management and point-of-sale system") is kept and widened into the *Property and Payment Platform* (section 3), because at this size the PMS tenant, the card vault, the POS estate, and the payment network segments share one boundary and one owner. The registry's P08 incident ("point-of-sale and reservation system compromise") is kept, with the entry path set to a vendor remote access tool because that is the company's largest open exposure: 5 vendors on their own remote tools at 37 hotels (EV-017). The registry's P10 use case is kept (section 5).

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer | Authorizing official equivalent for the PPP (P02); chairs the crisis management team (P08); co-approves the BIA (P05) |
| Chief Information Officer (CIO) | IT operations and the enterprise platform; executive risk committee member |
| Chief Audit Executive | Heads Internal Audit; reports functionally to the audit committee; leads P07 |
| General Counsel; Deputy General Counsel | Disclosure committee chair and backup; outside counsel engagement |
| Controller | Disclosure committee member; SOX program |
| Chief Human Resources Officer | Workforce screening, terminations, training; owner of AI-006 |
| Executive Vice President, Hotel Operations | Company-operated hotels; owner relations for managed hotels |
| Executive Vice President, Franchise Operations and Development | Brand technology standards enforcement with franchisees |
| Vice President, Hotel Technology | PPP system owner; property systems and vendor support |
| Vice President, Distribution and Reservations | CRS, channels, contact center; SL-2 service line owner |
| Vice President, Digital and Loyalty | Website, app, chatbot operation, loyalty platform, AI-005 |
| Vice President, Revenue Strategy | Operates AI-001 and the franchise pricing service |
| Vice President, Franchise Technology Services | SL-1 service line owner |
| Vice President, Integration Management Office | Integration of the acquired resorts |
| Vice President, Corporate Security and Facilities | Physical security, colocation oversight, media destruction |
| Vice President, Food and Beverage | Outlet operations and fallback during POS incidents |
| Vice President, Corporate Communications; Vice President, Investor Relations | Incident communications; investor relations is a disclosure committee member |
| Directors of Security Operations, Identity and Access Management, Network Engineering, Cloud Platform Engineering, Endpoint Engineering, Third-Party Risk Management, and Franchise Technology Compliance | Common control providers and program owners (P02 section 10.3) |
| PMS Tenant Administration Manager; Payments Platform Engineering Manager; POS Operations Manager | PPP system administrators |
| Data science lead | AI governance committee member |

**Committees.** Executive risk committee: Chief Risk Officer (chair), CIO, Chief Operating Officer, CISO, General Counsel; meets monthly. Disclosure committee: General Counsel (chair), CFO, Controller, CISO, Chief Privacy Officer, Chief Risk Officer, Vice President, Investor Relations; outside securities counsel advises; 3 members changed in 2026. AI governance committee (formed 2025): Chief Risk Officer (chair), Chief Commercial Officer (recuses on AI-001 and AI-002), Chief Privacy Officer, CISO, General Counsel's delegate with antitrust counsel, Chief Human Resources Officer, Executive Vice President, Hotel Operations, Vice President, Digital and Loyalty, Director of Franchise Technology Compliance, data science lead; Internal Audit observes. Board-approved risk appetite dated 2026-02. Sources: EV-032, EV-049, EV-029.

**Operations and volumes.** Revenue of about $4.8 billion is about $13.2 million per calendar day (EV-053). Colocation DC-1 is in Florida and DC-2 in Texas. The CRS runs active-passive across two regions; franchise agreements commit it to 99.9% monthly availability. About 92% of card volume runs through one payment gateway. Enterprise DR test 2026-04-25: CRS failover 1.6 hours, card vault restore 1.8 hours. The contact center handles about 1.1 million booking calls a year. 212 franchised hotels subscribe to the franchise pricing service (AI-001); separately, 212 franchise agreements signed before 2022 lack incident notice and PCI DSS acknowledgment terms. Sources: EV-013, EV-023, EV-024, EV-043, EV-051, EV-054, EV-038.

**PPP (P02).** Identifier CSC-SYS-PPP-001; SSP version 3.0 approved by the Chief Operating Officer on 2026-09-14; the board risk committee approved the Moderate baseline with 10 High-baseline supplements on 2026-09-10. About 36,500 PMS tenant accounts (about 8,900 company-operated hotel staff, 26,400 franchisee staff, 1,200 corporate and support), 46 vault and tokenization administrators and engineers, 64 privileged accounts, about 5,600 POS users. Components: about 1,900 P2PE devices, 41 legacy POS servers and about 470 workstations, about 1,150 front desk PCs, about 640 front desk terminals, 110 hotel firewall pairs. Brand technology standards BS-TECH-01 to BS-TECH-06; exception register entries EXC-2026-011, -017, -022, and -026 (P06; EV-027). Sources: EV-005, EV-003, EV-010.

**Contract terms used in P08 (fictional).** Acquirer agreement: notice within 24 hours of suspicion. Management agreements: owner notice within 24 hours. Franchise agreements since 2022 and SL-2 client agreements: notice within 72 hours. BS-TECH-06: franchisees report to the brand within 24 hours. Vendor contracts: 72-hour breach notice (PMS vendor: 24 hours). Last enterprise IR tabletop: 2026-03-24 (no disclosure committee). Sources: EV-038, EV-034.

**Internal Audit assessment (P07).** An IT audit manager and four IT auditors; the co-source firm performed only the reachability test and packet captures; PAM tests were done in house. Report issued 2026-09-04. Testing found vendor default credentials on legacy POS servers at 3 hotels (reported 2026-08-12, changed 2026-08-14; EV-IA-5); vendor remote tools enabled outside approved windows at 11 of the 37 hotels (EV-AC-17, EV-MA-4); 14 terminals missing from device lists at 5 hotels (EV-CM-8); 4 of 25 sampled patches installed after 30 days (EV-SI-2). Populations: 2,210 account events, 1,318 terminations (96 at the resorts), 1,640 PAM vault sessions, 1,420 PAM vendor sessions, 212 PPP changes, 286 security incidents, 238 patches, 181 backup jobs (2026-01-01 to 2026-06-30). Segmentation retest scheduled 2026-10-23.

**Service lines (P09).** SL-1 franchise technology services (PMS tenant administration, CRS access, managed property network, help desk for 640 franchised hotels): SOC 2 Type 2 (Security, Availability, Confidentiality) every year since 2023; the 2025 report had 2 exceptions (late removal of franchisee accounts, one missed quarterly hub rule review); Processing Integrity added for the 2027 period. SL-2 independent hotel distribution services (CRS and booking engine for about 180 unbranded independent hotels): first Type 2 planned for 2027-04-01 to 2027-09-30 (Security, Availability, Confidentiality, Processing Integrity, Privacy), report expected 2027-11; two hotel management companies among its clients require it; 41 client booking pages lack a link to the client's own privacy notice. Sources: EV-041, EV-042.

**AI portfolio (P10).** 12 use cases AI-001 to AI-012 as listed in the P10 inventory; 8 reviewed, 4 not reviewed (AI-006, AI-008, AI-010, AI-011; due 2026-11-30) (EV-049, EV-050). AI-002 is company-built on Cloud provider B's managed generative AI service and handles about 1.9 million conversations a year. AI-006 was switched on by a hotel group in 2026-04 at 22 hotels (including 2 in Illinois and 3 in California; none in Colorado or New York City); ranking disabled 2026-08-20 (EV-083). AI-005 is disabled at Illinois hotels (EV-052). Procurement block on AI features without an inventory ID from 2026-10-31.
