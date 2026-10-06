# Scenario facts: Cris Santos Company | Accommodation and Food Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a law, regulation, standard, or court decision, the citation is given. Facts about acquirers, card brands' contract terms, franchise and management agreements, and vendors are fictional unless a source is cited.

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
| Card acceptance | Company-operated hotels run about **14.6 million card transactions a year** (rooms about 4.1 million; food and beverage about 10.5 million). Owned and leased hotels use the company's merchant accounts; managed hotels use their owners' merchant accounts, but the company operates every payment system under the management agreements and includes them in its own PCI DSS program |
| PCI DSS status | **Both a merchant and a service provider.** PCI DSS v4.0.1 applies by contract (N72-R01). (a) **Merchant:** the acquirer agreement (fictional term) requires an annual Report on Compliance (ROC) by a Qualified Security Assessor (QSA); the 2025 merchant ROC (dated 2025-11-21) was compliant with 3 compensating controls; the 2026 ROC and attestation of compliance (AOC) are due **2026-11-30**. (b) **Service provider:** the central reservation system stores guarantee card data for franchised hotels and the company administers the brand property management system (PMS) tenant, the payment tokenization service, and the managed property network for franchisees, so the company validates as a service provider with a QSA ROC (dated 2026-03-27) and gives franchisees its service provider AOC. Card-brand merchant and service provider level thresholds were not verified from a card brand primary source, so no level number is stated in these documents |
| Payment design | **Central reservation system (CRS):** guarantee and prepayment cards from the brand website, app, contact center, and channel connections are tokenized by the company's tokenization service and stored in the card vault (Cloud provider A, a dedicated cardholder data environment account). **Contact center:** card numbers are captured by keypad through a tone-masking service (service provider), so agent desktops never see them. **Front desk at company-operated hotels:** PCI-listed validated point-to-point encryption (P2PE) terminals at 82 of 110 hotels; 28 hotels (including the 9 resorts still on the seller's systems) use semi-integrated chip terminals that are not P2PE. **Food and beverage at company-operated hotels:** 264 outlets; 153 on a cloud POS with validated P2PE devices; **111 outlets at 41 hotels still on a legacy integrated POS** with on-property POS servers. **Franchised hotels:** each franchisee is its own merchant and must use a brand-approved payment solution |
| Franchise model and duties | Brand standards require franchisees to use the brand cloud PMS and the CRS, to use a brand-approved payment solution, and to validate PCI DSS and submit an AOC every year. 410 of 640 franchised hotels also subscribe to the **managed property network service**, which connects their property networks to the company's network hubs. In *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015) (No. 14-3514, opinion filed 2015-08-24), the court affirmed that the FTC may challenge unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a), in a case about a hotel franchisor that managed its branded hotels' PMS systems. The alleged failures included card data in clear text, easily guessed and default passwords, no firewalls between hotel PMS systems, the corporate network, and the internet, an out-of-date operating system, no inventory, unrestricted vendor access, and weak incident response. **The company carries these duties for every system it designs, connects, or manages for franchisees** |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls over ERP, payroll, and owner and franchise fee accounting; two service lines offered to external clients (SOC 2); growth by acquisition (resort collection, 14 resorts, closed 2025-06) |
| Not in scope | **HIPAA:** not a covered entity. **FTC Safeguards and Red Flags Rules:** the company extends no consumer credit; the co-brand credit card is issued by a bank. **Florida Digital Bill of Rights:** not a "controller" under Fla. Stat. 501.702 (revenue exceeds $1 billion, but the company does not earn 50% or more of revenue from online advertising, operate a consumer smart speaker and voice command service, or operate an app store with at least 250,000 applications). **Federal contracts:** none; government travelers book like any guest. **CIRCIA:** proposed only (N72-R06); the company exceeds the SBA size standard, so it would be covered by the proposed size-based criterion if the rule is finalized as proposed |
| Other applicable law | FTC Act Section 5 (15 U.S.C. 45(a), (n)) for guest data security, privacy statements, and pricing claims (N72-R02); FTC Rule on Unfair or Deceptive Fees, **16 CFR Part 464** (90 FR 2066 (rule text at 2166), published 2025-01-10, effective 2025-05-12), which covers short-term lodging and requires the total price, including mandatory resort and destination fees, in any price display (464.1, 464.2); FTC Disposal Rule, 16 CFR 682.3 (N72-R03); state breach notification laws (N72-R04), Florida worked example Fla. Stat. 501.171; Florida guest register, **Fla. Stat. 509.101(2)**; state comprehensive privacy laws, including the CCPA (revenue above $26,625,000) and its cybersecurity audit regulations (11 CCR 7120-7124); state price gouging laws during declared emergencies (Florida worked example Fla. Stat. 501.160) |
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
| ID | System | Notes |
|---|---|---|
| SYS-01 | Central reservation system (CRS) and guest profile hub | Company-built on Cloud provider A; about 38 million reservation transactions a year; 61 million guest profiles |
| SYS-02 | Brand cloud PMS (vendor SaaS, multi-property tenant administered by the company) | 741 of 750 hotels; the 9 resorts still on the seller's legacy PMS migrate by 2027-03-31 |
| SYS-03 | Payment tokenization service, card vault, and payment gateway integration | Company-operated cardholder data environment on Cloud provider A; about 6.2 million active card tokens |
| SYS-04 | POS estate at company-operated hotels | 153 outlets on a cloud POS with validated P2PE; 111 outlets at 41 hotels on a legacy integrated POS |
| SYS-05 | Property networks and the managed property network service | SD-WAN and firewalls at the 110 company-operated hotels and the 410 subscribing franchised hotels; hubs in two colocation data centers and the cloud |
| SYS-06 | Brand website, mobile app, booking engine, and guest chatbot | Company-built booking engine with an embedded tokenization payment form |
| SYS-07 | Loyalty and CRM platform (vendor SaaS) | 14.2 million members; member sign-in with optional MFA |
| SYS-08 | Channel connectivity (distribution switch to online travel agencies and global distribution systems) | Third-party switch; virtual cards delivered to the CRS vault |
| SYS-09 | Identity platform (SSO, MFA, privileged access management, identity governance) | About 12,000 workforce identities plus about 26,400 franchisee staff accounts for the PMS and CRS |
| SYS-10 | Endpoints at offices and company-operated hotels | About 21,000 PCs, POS workstations, tablets, and kiosks |
| SYS-11 | Hotel building and guest-room technology | Door lock systems, building management, guest Wi-Fi, and IPTV at company-operated hotels |
| SYS-12 | ERP, payroll and timekeeping, and owner and franchise fee accounting | SOX-relevant |
| SYS-13 | Contact center platform (CCaaS) with tone-masking card capture | About 650 agents |
| SYS-14 | Data platform on Cloud provider B and the revenue-management system (vendor SaaS) | Warehouse, analytics, AI services |
| SYS-15 | About 1,100 third-party vendors (86 with card data or guest personal information at volume) | Tiered third-party risk program |
| SYS-16 | AI portfolio (12 use cases) | Governed by an AI governance committee formed in 2025 |

**SSP system (P02):** the *Property and Payment Platform (PPP)*: the company-administered brand cloud PMS tenant and its interfaces (SYS-02), the payment tokenization service and card vault (SYS-03), the POS estate at company-operated hotels (SYS-04), and the property payment network segments (part of SYS-05), with interfaces to SYS-01, SYS-06, SYS-08, and SYS-13. It is the company's highest-value system for card data and hotel operations, and it inherits common controls from the enterprise platform.

## 4. Current security posture: mature, with residual gaps in legacy systems, third parties, and independence
**In place today:**
- A mature program aligned to CSF 2.0 and PCI DSS v4.0.1, with annual merchant and service provider ROCs by a QSA
- Tokenization of all stored card data in the CRS and PMS; tone-masking card capture in the contact center
- Validated P2PE at 82 front desks and 153 food and beverage outlets
- Annual risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with an MSSP for overflow; EDR on corporate and company-operated hotel endpoints
- PAM and MFA for all workforce and franchisee staff accounts on the PMS and CRS
- Quarterly access certification
- Immutable backups; annual DR tests for the CRS, PMS integrations, and the card vault
- Quarterly ASV scans; annual penetration tests; a public bug bounty for the website and app
- Tiered vendor reviews, including AOC and SOC report reviews
- Annual SOC 2 Type 2 report for franchise technology services since 2023
- Total price display, including resort and destination fees, on the brand website and app since 2025-05 (16 CFR Part 464)
- SEC Item 106 disclosure in its 10-K

**Targeted gaps:**
1. **Legacy POS.** 111 of 264 food and beverage outlets at 41 company-operated hotels still run a legacy integrated POS with on-property servers. Card data is in clear text in POS workstation memory before it reaches the gateway. P2PE replacement is 58% complete and due 2027-06-30.
2. **Resort acquisition.** 9 of the 14 resorts acquired in 2025-06 still run the seller's PMS, network, and directory under a transition services agreement that ends 2027-03-31. Their 3 resort booking microsites have no payment page script inventory or tamper detection (PCI DSS 6.4.3 and 11.6.1).
3. **Franchisee PCI oversight.** 141 of 640 franchised hotels (22%) did not submit a 2025 AOC. The company has no technical visibility into the 230 franchised hotels that do not use the managed property network service, and brand standards set no technical minimums for them.
4. **Managed network segmentation.** The 2026-05 penetration test found one hub firewall rule that let franchised hotel network segments reach the CRS integration tier on 2 ports. The service provider segmentation test due in the second half of 2025 was not performed (PCI DSS 11.4.6 requires one every six months).
5. **Vendor remote access.** 5 of 14 property-system vendors (legacy POS, two door lock vendors, building management, IPTV) still use vendor-managed remote tools outside the PAM gateway at 37 company-operated hotels.
6. **Card data outside the vault.** A 2026 data loss prevention scan found about 4,800 emails with full card numbers in group sales and events mailboxes at managed hotels; 29 hotels still accept emailed card authorization forms.
7. **Loyalty account takeover.** Credential stuffing against member accounts; MFA is optional (23% adoption); fraudulent points redemptions cost about $1.9 million in 2026 Q2.
8. **Door lock servers.** 31 lock servers at company-operated hotels run operating systems out of vendor support.
9. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. The revenue-management system offered to franchisees pools non-public rate and occupancy data from competing hotels; the guest chatbot quotes resort collection rates without the mandatory resort fee; an applicant screening tool went live at 22 hotels without review.
10. **Materiality.** The disclosure committee has not exercised the materiality playbook since 3 members changed in 2026, and the playbook does not address incidents that start at a franchised hotel or affect franchisee guests only.
11. **Independence.** Independence safeguards for the QSA (the 2025 QSA firm also designed segmentation fixes) and for the Internal Audit co-source firm (its consulting arm configured the PAM tool in 2025) are handled case by case and are not written into the internal audit charter or the QSA selection procedure.
12. **Retention.** The guest profile hub keeps all 61 million profiles indefinitely, including about 8.7 million with identity document numbers.

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
| 2026-05-11 to 2026-05-22 | Annual penetration test and segmentation test (independent testing firm) |
| 2026-06-01 to 2026-07-31 | Enterprise BIA update, risk analysis, and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line; GRC team supported scoping) |
| 2026-08-17 to 2026-08-28 | SOC 2 readiness and AI portfolio review (AI governance committee met 2026-08-19) |
| 2026-09-10 | Results to the audit committee and the risk committee |
| 2026-10-19 to 2026-11-13 | QSA fieldwork for the 2026 merchant ROC (planned) |
| 2026-11-30 | 2026 merchant ROC and AOC due to the acquirer |
