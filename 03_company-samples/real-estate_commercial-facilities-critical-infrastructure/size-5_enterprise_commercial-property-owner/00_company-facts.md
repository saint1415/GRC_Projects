# Scenario facts: Cris Santos Company | Commercial Facilities | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded real estate investment trust, or REIT; SEC registrant listed on a national securities exchange; board with audit and risk committees) |
| Business | Owner-operator of office and retail property (NAICS 531120, Lessors of Nonresidential Buildings (except Miniwarehouses)). The REIT owns its properties through an operating partnership and property-level subsidiaries and self-manages them: leasing, property management, engineering, and in-house building security. A taxable REIT subsidiary, Cris Santos Building Services (the TRS), sells property management and technology services to joint venture (JV) partners and third-party owners |
| Location | Headquartered in Florida. Operates 140 properties in 6 states: Florida 46, Texas 32, Georgia 18, North Carolina 14, Arizona 14, California 16. **State law is handled generically:** the law of each state where affected individuals reside applies, with Florida as the worked example. California is analyzed by name only for the CCPA and the 2026 CPPA regulations, because they are a requirement of this vertical (C-COMMERCIAL-FACILITIES-R03) |
| Portfolio | **112 owned properties** (about 48 million sq ft): 40 Class A office towers, 20 suburban office parks, 38 open-air retail and lifestyle centers, and 14 mixed-use properties. 22 of the 112 are held in JVs with institutional investors, with the company as managing member and property manager. **28 managed properties** (about 9 million sq ft: 16 office towers, 6 office parks, 6 retail centers) are owned by third parties and managed by the TRS. In total the company operates 140 properties (about 57 million sq ft) |
| Acquired portfolio | In November 2025 the company acquired a 19-property portfolio in Texas (12) and Arizona (7): 6 office towers, 5 office parks, and 8 retail centers (AP-01 to AP-19). Its building systems still run on the seller's platforms (gap 1) |
| Tenants and occupants | About 5,600 tenants (about 2,300 office and 3,300 retail and restaurant). About 212,000 tenant employees hold access credentials (cards or mobile credentials). About 18,000 registered visitors per business day at 70 lobbies, where kiosks scan a government ID |
| Workforce | 12,000 employees: 4,900 security operations (in-house security officers and Regional Security Operations Center operators); 3,700 engineering and maintenance; 1,150 property management and tenant services; 420 leasing and marketing; 640 finance, accounting, and lease administration; 380 technology (IT, cybersecurity, OT security, data, and digital products); 160 human resources; 90 legal, risk, and compliance; 210 development and construction; 350 executive, corporate, and TRS administration |
| Revenue | About $4.8 billion a year (fictional): rental revenue and recoveries about $4.45 billion; TRS management and technology fees about $120 million; parking revenue share about $110 million; other (events, after-hours HVAC, amenity and license fees) about $120 million. Not SBA-small: the SBA standard for NAICS 531120 is $34.0 million in average annual receipts (13 CFR 121.201) |
| Card acceptance | The company **is a merchant**. It takes about 210,000 card transactions a year at 64 management offices and conference and event centers (bookings, after-hours HVAC charges, badge replacement fees, kiosk license fees) only through 182 terminals from a **validated PCI-listed point-to-point encryption (P2PE) solution** supplied by its payment processor. Rent is paid by ACH. Contracted parking operators are the merchants of record at the 84 garages. Amenity bookings in the tenant app are billed to tenant accounts, not paid by card |
| PCI DSS validation | Annual self-assessment on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), as required by the acquirer. The 2025 SAQ P2PE was signed by the Chief Accounting Officer on 2025-11-14 |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate and Retail subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule is specific to the sector; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary and the company adopted them as its baseline |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106); CCPA and the 2026 CPPA regulations (the company does business in California and its revenue is far above the threshold); SOX IT general controls; growth by acquisition; the TRS service lines that external clients rely on |
| Not in scope | HIPAA: not a covered entity or business associate (medical office tenants run their own systems). Florida Digital Bill of Rights: revenue is above $1 billion, but the company meets none of the other "controller" conditions in Fla. Stat. 501.702 (online advertising revenue, a smart speaker service, or an app store). Gaming and lodging rules: no such operations. Federal contracts: none, and no leases to federal agencies (confirmed by the General Counsel; recheck if that changes). CIRCIA: proposed rule only (see P03) |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board risk committee | Oversees cybersecurity risk (Item 106 governance); quarterly cyber and enterprise risk reporting |
| Board audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Jointly accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CEO; chairs the policy governance committee |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register; chairs the executive risk committee |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee and administratively to the CFO |
| Chief Privacy Officer | Privacy program, including CCPA and state privacy laws; breach determinations with the General Counsel; reports to the General Counsel |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| GRC team (9), Cyber Defense Center (24x7 in-house security operations center with managed security service provider (MSSP) overflow), OT security team (7), Internal Audit (24, including 6 IT auditors) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Formed in 2025; reviews and tiers every AI use case (P10) |

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Building automation system (BAS). **Platform A** (64 towers and mixed-use properties): 4 supervisory server clusters in the two colocation data centers, 110 engineering workstations, about 61,000 BACnet field controllers. **Platform B** (21 office parks and 36 retail centers): 57 site supervisory servers (virtual machines on site hosts), 64 engineering workstations, about 17,500 field controllers. **Platform C** (the 19 acquired properties): 19 site servers (physical PCs), 23 workstations, about 6,800 field controllers | On-premises and colocation (OT) | Operational data; building drawings | Field controllers keep running their last programs and schedules if a supervisory server is lost |
| SYS-02 | Physical access control system (PACS). **Enterprise platform** (121 properties): cloud-hosted access control platform with about 6,200 door controllers, 31,000 card readers, and 540 turnstile lanes. **Legacy PACS** (19 acquired properties): 2 on-premises servers and about 640 door controllers | Vendor SaaS plus on-premises (OT) | Yes: tenant employee names, employers, badge photos, credential numbers, access history | Door controllers cache credentials for up to 72 hours without the cloud service. The platform vendor has a SOC 2 Type 2 report |
| SYS-03 | Video surveillance and analytics: about 41,000 cameras and 610 network video recorders (NVRs) on the same vendor platform as SYS-02, plus 2,900 cameras and 48 NVRs on a legacy video system at the acquired properties. Monitored from 3 **Regional Security Operations Centers (RSOCs)**: East (Florida), Central (Texas), and West (California) | On-premises plus vendor SaaS | Yes: video of people (no audio); face templates for the AI-002 pilot | Hosts the video analytics features AI-001 and AI-002 (P10) |
| SYS-04 | Enterprise and property networks: SD-WAN to 140 properties, property firewalls, switches, Wi-Fi, and OT zones and conduits for SYS-01 to SYS-03 | On-premises; SD-WAN managed service | In transit | OT segmentation is complete at 121 properties; the 19 acquired properties are flat (gap 1) |
| SYS-05 | Identity platform: single sign-on, MFA, privileged access management (PAM), identity governance | SaaS plus PAM vault in Cloud provider A | Identities | Protects all workforce, administrator, cloud, and OT remote access |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | |
| SYS-07 | Property management, lease accounting, and ERP with tenant portal (ACH rent payments), work orders, CAM reconciliation, and JV and owner reporting | Vendor SaaS | Yes: tenant bank details, contacts, lease terms | System of record for leases and receivables; SOX-relevant |
| SYS-08 | Multi-cloud estate: **Cloud provider A** landing zone (38 accounts: smart building data platform with BAS historian, energy analytics, and data lake; OT remote access gateway; OT log pipeline; file storage; data warehouse; PAM vault; backup accounts with write-once retention). **Cloud provider B** (tenant experience platform SYS-14 in two regions; cloud AI services). **Colocation DC-1 (Florida) and DC-2 (Texas)** (Platform A supervisory clusters, network core, offline backup copies) | Two public cloud providers (vendor-agnostic) and two colocation data centers | Yes | |
| SYS-09 | Endpoints: about 9,800 corporate laptops and desktops, 1,150 security console PCs (RSOCs and lobby desks), and 7,400 tablets and phones under mobile device management | Company-managed | Yes (cached) | EDR on all Windows and macOS endpoints and console PCs |
| SYS-10 | Card payment terminals (182) | Payment processor's validated P2PE solution | Encrypted card data only | Stand-alone; no clear-text card data in any company system |
| SYS-11 | Visitor management: lobby kiosks at 64 Platform A properties (enterprise SaaS) and a legacy kiosk product at the 6 acquired towers | Vendor SaaS | Yes: visitor names, photos, scanned driver license or ID numbers | About 18,000 visitors per business day |
| SYS-12 | HR and payroll | Vendor SaaS | Yes: employee Social Security numbers and bank details | SOX-relevant |
| SYS-13 | Life-safety systems: fire alarm panels, elevator controls, emergency voice communication | Vendor-maintained, separate networks | No | Outside the IT and OT scope. The BAS reads fire alarm status through hardwired, read-only relay points |
| SYS-14 | Tenant experience platform: company-built mobile app and web portal for mobile credentials (issued through the SYS-02 integration), amenity bookings, service requests, building notices, and a virtual assistant (AI-008) | Cloud provider B (company-built) | Yes: tenant employee names, phone numbers, mobile credential data | About 168,000 active users at company properties plus about 41,000 at 36 buildings of third-party owners who license it (service line SL-2) |
| SYS-15 | Third parties: about 3,100 vendors; 420 have system access or hold company, tenant, or employee data; 48 are tier-1 (critical) | Various | Varies | Includes 6 BAS integrators (A for Platform A, B1 to B4 regionally for Platform B, C for Platform C), 3 regional access control and video integrators, the access control and video platform vendor, 2 guard contractors, 3 parking operators, and the MSSP |
| SYS-16 | AI portfolio: 12 use cases (P10) | Vendors and company-built | Varies | Governed by the AI governance committee formed in 2025 |

**SSP system (P02):** the *Building Automation and Access Control System (BAACS)*: SYS-01 (Platforms A, B, and C), SYS-02, SYS-03, the OT zones and zone firewalls of SYS-04, the OT workloads in SYS-08 (smart building data platform, OT remote access gateway, OT log pipeline, and their backups), the security console PCs and engineering devices in SYS-09, and their interfaces to SYS-05, SYS-11, SYS-14 (mobile credentials), and the energy optimization service (AI-004). A high-value system at the Moderate baseline that inherits common controls from the enterprise platform.

## 4. Current security posture: mature program with targeted gaps

**In place today:**
- A security program aligned to NIST CSF 2.0, with CISA CPG 2.0 adopted as the IT and OT baseline (2026-02); an OT security team under the CISO since 2024
- Annual enterprise risk analysis integrated with ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and an exceptions register
- A 24x7 Cyber Defense Center with MSSP overflow; SIEM with identity, cloud, EDR, firewall, email, Platform A, and enterprise PACS administrator logs
- PAM for IT and Platform A administration; phishing-resistant security keys for privileged users; quarterly access certification for IT systems
- OT zones and conduits (NIST SP 800-82 Rev. 3) at 121 properties; an OT remote access gateway (named accounts, MFA, per-session approval, recording) used by every integrator except Integrator C
- Immutable backups in separate cloud accounts; annual disaster recovery tests for tier-1 IT systems; Platform A supervisory clusters fail over between the two data centers
- Tiered third-party risk management with annual reassessment of tier-1 vendors
- An annual SOC 2 Type 2 report for the tenant experience platform (SL-2) since 2025
- SEC Item 106 disclosure in the Form 10-K; a disclosure committee and materiality playbook
- Card acceptance only through validated P2PE terminals; SAQ P2PE filed for 2025
- Life-safety systems on separate vendor-maintained networks with read-only relay points into the BAS

**Targeted gaps:**
1. **Acquisition integration.** The 19 acquired properties still run BAS Platform C (site servers and workstations on an unsupported operating system, no backups), a legacy on-premises PACS, flat property networks, and BAS Integrator C's always-on remote-support tool with a shared account and no MFA. None of it sends logs to the SIEM. The integration plan runs to 2027-06-30.
2. **OT visibility at scale.** The OT asset inventory is about 82% complete; passive OT network monitoring covers 54 of 140 properties; Platform B and Platform C BAS logs and legacy PACS logs do not reach the SIEM; door controller and NVR firmware versions are tracked only at Platform A properties.
3. **Third-party concentration.** One access control and video platform vendor runs PACS and video at 121 properties (its stated recovery time is 8 hours against a BIA need of 2 hours for administration). 9 integrators hold privileged OT access. 11 of 48 tier-1 vendor reassessments are overdue, and the acquired portfolio's inherited contracts have not been reviewed.
4. **Credential lifecycle at scale.** Tenant badges depend on tenant administrators; about 14,200 active badges have not been used in more than 90 days, and only 61% of tenants completed the 2026 credential attestation. Local BAS and console accounts at Platform B and Platform C are not tied to identity governance.
5. **AI.** 12 AI use cases; 7 have completed AI governance committee review. A face verification pilot (AI-002) runs at 2 Florida towers. No CPPA risk assessment has been completed for California processing, and one workforce scheduling tool (AI-006) may be ADMT for a significant decision under the CPPA rules.
6. **Materiality.** The materiality playbook has been exercised only with a data breach scenario (2025). It has not been exercised for a portfolio-wide building outage, its worksheet does not quantify rent abatement and tenant claims, and three disclosure committee members joined after the last exercise.
7. **California cybersecurity audit.** The first CPPA cybersecurity audit covers 2027 and its report is due 2028-04-01. Internal Audit advised on the 2025 OT security standard, which limits its independence for that area (Cal. Code Regs. tit. 11, 7122(a)(2)).
8. **Legacy data retention.** Visitor ID images are kept beyond the 30-day standard at the 6 acquired towers (legacy kiosks) and in one regional visitor management tenant: about 2.4 million records older than the standard.
9. **Recovery at scale.** Platform C has no backups. A sampled Platform B restore took 14 hours against a 12-hour RTO. RSOC regional failover has been tested for 4 hours only, not a full shift.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | All applicable rules across the enterprise: CISA CPG 2.0 (voluntary, adopted baseline; all 34 goals, OT tailoring from NIST SP 800-82 Rev. 3); PCI DSS v4.0.1 (SAQ P2PE requirements, binding by contract); SEC Form 8-K Item 1.05 and Reg S-K Item 106; CCPA and the 2026 CPPA regulations (reasonable security, cybersecurity audit, risk assessments, ADMT, notice and retention); FTC Act Section 5; state breach and data security laws (Florida worked example); CIRCIA tracked as a pending rule that would cover the company |
| P08 incident | Ransomware on building automation systems spreading across regions, entering through Integrator C's remote-support tool at the acquired properties, with an SEC materiality assessment and Form 8-K Item 1.05 step, crisis management, and a multi-state notification workflow |
| P09 SOC 2 | Type 2 readiness across two TRS service lines: SL-1 property management and building operations services for JV partners and third-party owners (first report; Security, Availability, Confidentiality, Processing Integrity); SL-2 tenant experience platform licensed to third-party owners (annual report since 2025; Privacy added) |
| P10 AI | Enterprise AI portfolio (12 use cases) with the AI governance committee operating model, and a full assessment of video analytics for building access (AI-001 tailgating detection and AI-002 face verification) |
| Cloud | Multi-cloud (vendor-agnostic) with two colocation data centers and common controls |
| Registry defaults | Kept. The primary system (building automation and access control), the P08 incident (ransomware on building automation systems), and the P10 use case (video analytics for building access) fit an office and retail REIT. At this size the system is the enterprise BAACS with common control inheritance, the incident adds the SEC materiality step and spreads across regions, and the AI use case sits inside a governed portfolio |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (property walkthroughs at 24 sampled properties, 2026-06-15 to 2026-07-17) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, with a co-sourced OT assessment firm for the OT standard areas) |
| 2026-09-10 | Results to the risk committee and the audit committee of the board; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

| Topic | Detail |
|---|---|
| Revenue per day | About $13.2 million of revenue per calendar day. Rent accrues at about $12.2 million per day: office about $7.1 million, retail about $3.6 million, mixed-use about $1.5 million |
| Lease terms | The office lease template (2023 and later) allows rent abatement after 3 consecutive business days of untenantable premises caused by landlord-controlled building systems; about 70% of office rent is on that template. Retail leases allow abatement after 5 business days. About 1,100 leases carry negotiated 72-hour notice clauses for unauthorized access to tenant employee data in the access control system |
| Platform vendor recovery commitments | The access control and video platform vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour for the cloud service. Door controllers cache credentials for up to 72 hours |
| Cyber insurance | $150 million tower with a $5 million retention. The primary carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before incident vendors are engaged |
| California footprint | 16 properties in California (12 owned, 4 managed). About 24,000 California tenant employees hold credentials; about 2,100 visitors per business day at California lobbies have ID scans (more than 500,000 visits a year); about 1,100 employees in California |
| Other state privacy laws | The Chief Privacy Officer's state privacy program tracks other state comprehensive privacy laws where the company does business (the cross-sector file lists the Texas law as applying to businesses that are not SBA-small). They are outside the row-by-row analysis in P03 |
| Operating volumes (P05) | About 1,900 credential changes per business day; officers can staff about 900 main entrances for one shift; about 92,000 tenant employees use only mobile credentials; about 4,200 new work orders and service requests per business day; about $370 million billed per month (up to about $310 million of cash delayed if an outage falls in the first week of a month); about 21,000 vendor payments and about $95 million of debt service per month; payroll about $31 million per biweekly period for about 8,600 hourly and 3,400 salaried employees; about 575 card transactions per day; the company share of parking revenue is about $300,000 per day; energy optimization saves about 5% of tower energy cost (about $40,000 per day); about 10,000 workforce members use email and files daily |
| BIA scenario and thresholds (P05) | Cost thresholds per day: Severe above $250,000 (or $1 million of rent at risk, or $100 million of cash delayed); Moderate $50,000 to $250,000. Rent at risk after the abatement thresholds: about $4.5 million per day for Platform A properties, $2.6 million for Platform B (about $0.8 million office parks, $1.8 million retail), $0.9 million for the acquired properties. A 5-business-day outage of Platforms A and B is estimated at about $14.4 million before incident costs |
| Networks and recovery (P05, P02) | Dual carriers at 98 properties (42 single carrier); the seller site VPN serves the 19 acquired properties until the SD-WAN migration; Platform A configuration and databases backed up every 4 hours, Platform B site servers nightly; the company holds controller program copies for Platform A and 48 of 57 Platform B properties (Integrator B3 holds the only copies for 9); the legacy PACS backs up nightly to a storage device on the same flat network; Platform A cluster failover tested 2026-05-16; the tenant experience platform failed over in 2.5 hours on 2026-06-20; the OT remote access gateway recovered in 3 hours; Platform B restore observed 2026-08-11 took 14 hours; BAACS contingency plan version 3 |
| Integration plan | Acquired towers move to Platform A and acquired office parks and retail centers to Platform B by 2027-06-30; the legacy PACS migrates to the enterprise platform by 2027-03-31; the 4 acquired garages use the seller's parking operator under a transition agreement; acquired-property staff moved to SYS-06 in 2026-01; acquired properties are billed from SYS-07 since 2026-02 and use the seller's work order system until 2027-03. The 19 acquired properties are wholly owned (not JV or SL-1 properties). 29 inherited vendor contracts came with them |
| Program details (P02, P03, P06) | Monthly IT and OT security council; policy attestation 98.4%; June 2026 phishing click rate 4.2%; DMARC at reject; public vulnerability disclosure policy and security.txt since 2025; OT network penetration test at 4 properties (2026-04); logs kept 1 year online and 7 years in the archive; retention schedule: visitor ID images 30 days, visit logs 1 year, access history 2 years, video 30 days unless held; 41 OT log source types defined (16 not onboarded); 14 of 48 tier-1 contracts lack incident notice of 72 hours or less; 3 of 9 integrators never security-assessed; the access control platform has 61 full administrators; about 6,900 workforce members in OT roles; an NVR at a retail center was found exposed on 2026-07-08 and closed in 2 days; the 2025 policy set was reviewed 2025-09-11; SSP versions 1.0 (2024-09-20) and 2.0 (2025-12-15); the Chief Privacy Officer confirmed CPPA audit applicability on 2026-06-19; risk appetite approved by the board in 2026-02; about $11.8 million of treatment funded for 2026 Q4 to 2027 Q2; two retail portfolios under evaluation for 2027 |
| Card acceptance details (P03) | 2 conference centers wrote phone bookings with security codes on paper forms (found 2026-07); weekly POI inspection logs kept at 55 of 64 offices; tampering training 91% complete; email data loss prevention found no card numbers in 2026; P2PE listing checked 2026-07-09 |
| Assessment populations (P07) | 1,212 terminations of workforce members with BAACS access in 2026 H1 (214 at Platform B and C properties); about 3,600 workforce BAACS accounts; about 1,840 OT gateway maintenance sessions and 312 unapproved Integrator C sessions in 2026 H1; 214 OT-flagged security cases and 61 OT events logged by acquired-property staff; about 92 BAACS servers; about 300 OT Windows hosts; about 900 OT conduit rules; about 420 OT closets and engineering rooms; about 7,500 NVRs and door controllers; 212 Platform B program changes in 2026 H1. Interim access lists were applied at the tested acquired property on 2026-08-15 |
| Devices | About 2,600 of the 7,400 tablets and phones are engineering and security tablets used with the BAACS |
| California lobbies and AI (P03, P10) | 8 California lobbies have visitor kiosks. Tailgating detection (AI-001) runs at 54 lobbies, including all 8 in California, covering about 150,000 credential holders. The face verification pilot (AI-002) runs at 2 Florida towers with about 1,450 enrolled tenant employees; a consented volunteer accuracy study used 320 employees. The video platform has 3 regional tenants (East, Central, West); written training opt-outs exist for East and Central. The vendor must give 30 days' notice of new analytics features. The enterprise generative AI assistant (AI-011) has about 4,200 users |
| Contract terms (P08, P09) | SL-1 management agreements require notice of material incidents within 2 business days; SL-2 service agreements require security incident notice within 72 hours of confirmation, a status page update within 1 hour of an outage, and 99.9% monthly availability; new vendor contracts require incident notice within 24 hours. The SL-2 2025 SOC 2 report had no exceptions. SL-1 detail: passive OT monitoring covers 19 of the 50 SL-1 properties, 9 SL-1 properties have unsupported Platform B workstations, 4 SL-1 retail centers lack degraded-mode procedures, and 14 submeter bills were corrected after release in 2026 H1 |

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Operating Officer (COO) | Business owner for property operations; authorizing official for the BAACS (P02); chairs the crisis management team |
| Chief Information Officer (CIO) | IT operations and the enterprise platform; chairs the AI governance committee |
| Chief Accounting Officer | Signs the SAQ P2PE; disclosure committee member |
| Controller | SOX program owner for financial reporting controls |
| Chief Human Resources Officer (CHRO) | Workforce onboarding, terminations, training records; owner of AI-006, AI-007, and AI-010 |
| Executive Vice President, Property Operations | System owner of the BAACS; owns property management, engineering, and security operations |
| Senior Vice President, Engineering | Owns the BAS platforms and the BAS integrators; manages regional engineering directors and chief engineers |
| Vice President, Corporate Security | Owns physical access control, video, visitor management, the RSOCs, the security officer force, and the guard contractors |
| Vice President, Integration Management Office | Integration of the acquired portfolio (AP-01 to AP-19) |
| President, Cris Santos Building Services (TRS) | Owner of service line SL-1 |
| Vice President, Digital Products | Owner of the tenant experience platform (SYS-14) and service line SL-2 |
| Director of OT Security | Leads the OT security team (common control provider for OT monitoring, OT vulnerability management, and the OT remote access gateway) |
| Director of Security Operations | Runs the Cyber Defense Center; incident commander for security incidents |
| Director of Identity and Access Management | Identity platform (SYS-05) |
| Director of Cloud Platform Engineering | Cloud landing zones and colocation services |
| Director of Network Engineering | SD-WAN, property firewalls, and OT zone firewalls |
| Director of Endpoint Engineering | Workstations, console PCs, EDR, and endpoint baselines |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews (in the GRC team) |
| Building Technology Directors (3, one per region) | Platform A and B administration, integrator access approvals, OT change requests |
| Chief Engineers (one per property) | Day-to-day BAS operation; manual operation of plant equipment |
| Vice President, Leasing | Lease templates and tenant notice clauses |
| Vice President, Investor Relations | Investor communications; disclosure committee member |
| Vice President, Corporate Communications | Media, tenant, and employee communications during incidents |
| Treasurer | Debt service and bank relationships |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Privacy Officer, Chief Risk Officer, and Vice President, Investor Relations, advised by outside securities counsel. Three members joined after the 2025 exercise.

**Service lines offered to external clients (P09).** SL-1: property management and building operations services delivered by the TRS for 50 properties (the 22 JV properties for 6 JV partners, and 28 properties of 9 third-party owners), using the company's own platforms. Owners' management agreements (amended 2026) require a SOC 2 Type 2 report by 2027-12-31 and a SOC 1 report on rent billing (handled by the Controller outside P09). SL-2: the tenant experience platform licensed to third-party owners for 36 buildings they operate themselves; annual SOC 2 Type 2 (Security, Availability, Confidentiality) since 2025.
