# Scenario facts: Cris Santos Company | Commercial Facilities | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held corporation; private equity-backed; board with an audit committee) |
| Business | Owner-operator of office and retail property (NAICS 531120, Lessors of Nonresidential Buildings (except Miniwarehouses)). The company owns 14 properties and self-manages them: leasing, property management, engineering, and in-house building security. Four of the 14 are owned by a joint venture (JV) with an institutional investor; the company is the JV's managing member and its property manager under a management agreement |
| Location | Florida only, in three metro areas (Metro 1, Metro 2, Metro 3). Headquarters, the corporate data room, and the 24x7 Security Command Center (SCC) are in Tower 1 (Metro 1) |
| Portfolio | 14 properties, about 4.2 million sq ft: 4 Class A office towers (Towers 1-4), 2 suburban office parks (Parks 1-2), 6 open-air retail centers (Retail 1-6), and 2 mixed-use properties (Mixed-Use 1-2, office over street retail with structured parking). JV properties: Tower 3, Tower 4, Retail 5, and Mixed-Use 2 |
| Tenants and occupants | About 420 tenants (about 250 office, about 170 retail and restaurant). About 14,500 tenant employees hold access credentials (cards or mobile credentials). About 1,100 registered visitors per business day at the tower and mixed-use lobbies, where kiosks scan a government ID |
| Workforce | 600 employees: 28 executive and corporate administration; 54 finance, accounting, and lease administration; 6 legal and risk; 30 leasing and marketing; 72 property management and tenant services; 212 engineering and maintenance; 162 security operations (in-house security officers and SCC operators); 20 IT and security; 10 human resources; 6 development and construction |
| Revenue | About $100 million a year (fictional): rent and expense recoveries, plus a parking revenue share, conference and event fees, after-hours HVAC charges, and JV management fees. Not SBA-small: the SBA standard for NAICS 531120 is $34.0 million in average annual receipts (13 CFR 121.201) |
| Card acceptance | The company **is a merchant**. It takes about 16,000 card transactions a year at 6 management offices (the conference centers at Towers 1-4, the Mixed-Use 1 event space, and the Retail 3 management office for kiosk license fees and event plaza bookings): bookings, after-hours HVAC charges, and badge replacement fees. Payment is only through 14 terminals from a **validated PCI-listed point-to-point encryption (P2PE) solution** supplied by the company's payment processor. Rent is paid by ACH through the tenant portal. A contracted parking operator runs the 6 structured garages and is the merchant of record for parking. Amenity bookings in the tenant app are billed to tenant accounts, not paid by card |
| PCI DSS validation | Annual self-assessment on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), as required by the acquirer in its annual validation letter. The 2025 SAQ P2PE was signed by the Controller on 2025-11-18 |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate and Retail subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule applies to the company; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary |
| Not in scope | CCPA/CPRA: revenue is above the CPI-adjusted threshold, but the company does not do business in California (recheck before any acquisition or marketing there). SEC cybersecurity disclosure: privately held. HIPAA: not a covered entity (medical office tenants run their own systems). Florida Digital Bill of Rights: applies only to controllers with more than $1 billion in global gross annual revenue (Fla. Stat. 501.702). Gaming and lodging rules: no such operations. CIRCIA: proposed rule only, but the company would be covered under the NPRM's size criterion (see P03) |
| State law approach | Florida only. Florida law is cited where a Florida duty applies (Fla. Stat. 501.171 for reasonable security, breach notice, and record disposal; Fla. Stat. 934.03 for audio recording). The deliverables otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Board audit committee | Quarterly cyber risk reporting |
| Chief Executive Officer (CEO) | Accepts High risks; approves the risk appetite and the security budget |
| Chief Operating Officer (COO) | Executive sponsor of the security program; accepts Moderate risks; system owner of the Building Automation and Access Control System (P02); chairs the crisis management team |
| Chief Financial Officer (CFO) | Cyber insurance, lender and JV partner reporting; executive owner of PCI DSS compliance and of the SOC 1 and SOC 2 commitments to the JV |
| General Counsel | Breach determinations with outside breach counsel; contract and lease notice terms; legal hold |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; board reporting; chairs the AI review group (P10) |
| IT Director | Information security officer: runs the security program day to day; IT operations; owns the cloud landing zone |
| Security Manager plus 2 security analysts | Security operations, vulnerability management, MSSP oversight. One analyst focuses on OT (hired 2026-03) |
| GRC Analyst | Risk register, policies and standards, evidence collection, vendor reviews |
| Vice President of Engineering | Owns the building automation systems across the portfolio; manages the chief engineers and both BAS integrators |
| Building Technology Manager | Reports to the VP of Engineering: BAS servers, OT network change requests, integrator access approvals |
| Chief Engineers (14, one per property) | Day-to-day BAS operation; manual operation of plant equipment |
| Director of Security Operations | Owns physical access control, video surveillance, visitor management, the SCC, the security officer force, and the guard contractor |
| Controller | Signs the SAQ P2PE; owner of accounting data |
| Vice President of Property Management and 10 Property Managers | Tenant relationships, lease notices, tenant communications |
| Internal audit (co-sourced firm) | Annual IT audit; performs the P07 control assessment |
| Managed security service provider (MSSP) | 24x7 EDR and SIEM monitoring of IT systems. OT systems are not monitored |
| BAS Integrator A | Programs and supports BAS Platform A (Towers 1-4, Mixed-Use 1-2); remote access through the company's remote access gateway |
| BAS Integrator B | Programs and supports BAS Platform B (Parks 1-2, Retail 1-6); remote access through its own always-on remote-support tool (gap 2) |
| Access control and video integrator | Installs and services door controllers, readers, turnstiles, cameras, and recorders |
| Contracted guard service | Night patrols at Parks 1-2 and Retail 1-6; remote video viewing |
| Parking operator | Runs the 6 garages under management agreements; merchant of record for parking; operates license plate recognition (AI-003) |

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Building automation system (BAS). **Platform A** (Towers 1-4, Mixed-Use 1-2): one enterprise supervisory server (a virtual machine in the Tower 1 data room), 6 engineering workstations, about 5,200 BACnet field controllers. **Platform B** (Parks 1-2, Retail 1-6): 8 site supervisory servers (physical PCs in each property's engineering room), 8 engineering workstations, about 1,600 field controllers | On-premises (OT) | Operational data; building drawings | Field controllers keep running their last programs and schedules if a supervisory server is lost |
| SYS-02 | Physical access control system (PACS): cloud-hosted access control platform with about 410 on-premises door controllers, about 2,300 card readers, and 36 turnstile lanes (Towers 1-4, Mixed-Use 1-2) | Vendor SaaS plus on-premises (OT) | Yes: tenant employee names, employers, badge photos, credential numbers, access history | Door controllers cache credentials and keep working for up to 72 hours without the cloud service. The vendor has a SOC 2 Type 2 report |
| SYS-03 | Video surveillance: about 3,400 cameras and 46 network video recorders (NVRs), managed from the same vendor platform as SYS-02 | On-premises plus vendor SaaS | Yes: video of people (no audio) | Hosts the video analytics features AI-001 and AI-002 (P10) |
| SYS-04 | Property networks at 14 sites: SD-WAN, firewalls, switches, Wi-Fi, and the OT segments for SYS-01 to SYS-03 | On-premises; SD-WAN managed service | In transit | OT segmentation is complete at Towers 1-4 only (gap 1) |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | Identities only | Protects SYS-06, SYS-07, SYS-08, SYS-12, SYS-14 administration, and the SYS-02/SYS-03 administrator portal |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Includes the conference and event booking mailboxes |
| SYS-07 | Property management and accounting system with tenant portal (ACH rent payments), work orders, CAM reconciliation, and JV reporting | Vendor SaaS | Yes: tenant bank details, contacts, lease terms | System of record for leases and receivables |
| SYS-08 | Cloud landing zone: 4 accounts (identity and security, shared services, workloads, backup) | Public cloud (vendor-agnostic) | Yes (building drawings, corporate files, investor data) | Workloads: BAS historian and energy analytics, file storage, data warehouse for JV and lender reporting. Shared services: network hub, site VPN, remote access gateway, log pipeline. Backup: vault with 35-day write-once retention |
| SYS-09 | Endpoints: 430 corporate laptops and desktops, 40 security console PCs (SCC and lobby desks), 190 tablets (engineering and security officers) | Company-managed | Yes (cached) | EDR on all Windows and macOS endpoints; tablets under mobile device management |
| SYS-10 | Card payment terminals (14) | Payment processor's validated P2PE solution | Encrypted card data only | Stand-alone; no clear-text card data in any company system |
| SYS-11 | Visitor management: lobby kiosks at Towers 1-4 and Mixed-Use 1-2 | Vendor SaaS | Yes: visitor names, photos, scanned driver license or ID numbers | About 610,000 visitor records kept since 2021 (gap 10) |
| SYS-12 | HR and payroll | Vendor SaaS | Yes: employee Social Security numbers and bank details | |
| SYS-13 | Life-safety systems: fire alarm panels, elevator controls, emergency voice communication | Vendor-maintained, separate networks | No | Outside the IT and OT scope. The BAS reads fire alarm status through hardwired, read-only relay points |
| SYS-14 | Tenant experience app: mobile credentials (issued through the SYS-02 integration), amenity bookings, service requests, building notices by push and SMS | Vendor SaaS | Yes: tenant employee names, phone numbers, mobile credential data | About 9,800 active users. Used for tenant emergency and service notices |
| SYS-15 | Third parties: about 210 vendors, of which 41 have system access or hold company, tenant, or employee data | Various | Varies | Includes both BAS integrators, the MSSP, the access control and video vendor, the guard contractor, and the parking operator |
| SYS-16 | AI tools: 5 use cases (P10) | Vendors | Varies | Adopted without review (gap 9) |

**SSP system (P02):** the *Building Automation and Access Control System (BAACS)*: SYS-01, SYS-02, SYS-03, the OT segments and shared firewalls of SYS-04, the BAS historian and energy analytics workload, remote access gateway, and backup vault in SYS-08, the security console PCs and engineering tablets in SYS-09, and their interfaces to SYS-05, SYS-11, SYS-14 (mobile credentials), and the energy optimization service (AI-004). Moderate baseline with tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- MFA through the identity provider for all corporate users; phishing-resistant security keys for identity provider, cloud, and access control platform administrators
- EDR on all corporate endpoints, security console PCs, and Windows servers, with 24x7 MSSP monitoring; MSSP-operated SIEM with identity provider, cloud, firewall, EDR, and email logs
- OT segmentation at Towers 1-4 (2025 project): OT zones behind deny-by-default firewall rules
- A remote access gateway (2025) with named accounts, MFA, per-session approval, and session recording, used by BAS Integrator A and the access control and video integrator
- A 4-account cloud landing zone with a separate backup account and 35-day write-once retention; nightly backups of the Platform A BAS server and the historian
- Annual risk assessment since 2024; security policies adopted in 2024; annual training and quarterly phishing simulations
- Annual external penetration test of the IT perimeter (last 2026-03); OT is excluded
- Annual co-sourced internal IT audit
- Card acceptance only through validated P2PE terminals; SAQ P2PE filed for 2025
- SOC 2 reports reviewed when SaaS vendors are onboarded
- Cyber insurance with a breach hotline
- Life-safety systems on separate vendor-maintained networks, with read-only relay points into the BAS
- A lease template (2024 and later) that requires prompt notice to tenants of unauthorized access to tenant employee data in the access control system; 31 tenants negotiated a 72-hour notice clause

**Missing or weak, found in the 2026 assessments:**
1. OT segmentation exists only at Towers 1-4. At Mixed-Use 1-2 the BAS is segmented, but door controllers and NVRs share corporate VLANs. At Parks 1-2 and Retail 1-6, BAS controllers, door controllers, and NVRs share flat property networks.
2. BAS Integrator B reaches the 8 Platform B servers through an always-on vendor remote-support tool, with one shared account, no MFA, no session approval, and no session logging.
3. OT visibility is poor. The OT asset inventory is about 55% complete (Platform B devices are mostly missing). There is no OT network monitoring, and BAS servers, network controllers, and access control administrator actions do not send logs to the SIEM.
4. BAS recovery is unproven. The Platform A server is backed up nightly but has never been restore-tested. The 8 Platform B servers have no backups. Field controller programs and graphics are held only by the integrators. Written degraded-mode (manual) operating procedures exist only at Towers 1-4.
5. The 8 Platform B servers and 5 Platform B engineering workstations run an operating system past vendor support, have no EDR, and are patched only when the integrator visits. Platform B software is two major versions behind.
6. Credential lifecycle is incomplete. Identity provider accounts are disabled automatically at termination, but local BAS accounts, console accounts, and badges are not tied to that process. Tenant badges are revoked only when a tenant asks; about 1,900 active badges have not been used in more than 90 days, and there is no tenant badge recertification. IT access reviews are annual, not quarterly. The access control platform has 23 full administrators.
7. Third-party risk management covers SaaS vendors at onboarding only. Of the 41 vendors with system access or data, 25 contracts have no incident notice clause, the integrators, guard service, and parking operator contracts have no security requirements, and no vendor is reassessed annually.
8. The incident response plan (2024) covers IT only. There is no playbook for OT or access control incidents, no documented crisis management structure, and the plan has never been exercised with engineering or security operations.
9. AI tools were adopted without governance: tailgating detection (AI-001), a face verification pilot (AI-002), license plate recognition data from the parking operator (AI-003), BAS energy optimization that writes setpoints (AI-004), and generative AI lease abstraction (AI-005). There is no AI inventory or review step.
10. The visitor management system keeps driver license scans and photos indefinitely (about 610,000 records since 2021). Video retention varies from 14 to 90 days by property, with no written rule.
11. Card handling: phone bookings at 2 conference centers (Towers 2 and 4) are written on paper forms with card numbers and security codes, and 5 emails containing card numbers were found in the event mailboxes. POI device inspections are done at the towers but not at the Retail 3 and Mixed-Use 1 offices.
12. Policies (2024) exist, but supporting standards are missing or thin (OT security, configuration, logging, vendor risk, AI).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | CISA CPG 2.0 (voluntary; all 34 goals, tailored for OT with NIST SP 800-82 Rev. 3) as the primary benchmark; PCI DSS v4.0.1 (SAQ P2PE requirements) as the binding-by-contract secondary standard; FTC Act Section 5 and Fla. Stat. 501.171 (reasonable security, breach notice readiness, disposal) as the legal baseline; CIRCIA tracked as a pending rule that would cover the company |
| P08 incidents | **Two incident types:** (1) ransomware on building automation systems, entering through BAS Integrator B's remote-support tool; (2) compromise or extended outage of the cloud access control and video platform. Both integrated with crisis management and legal |
| P09 SOC 2 | The JV management agreement requires a SOC 2 Type 2 report on the company's property management and building operations services (Security, Availability, Confidentiality), first report due 2027-12-31. Plus a vendor SOC 2 review program |
| P10 AI | AI use-case portfolio: AI-001 tailgating detection, AI-002 face verification pilot (both video analytics for building access), AI-003 license plate recognition, AI-004 BAS energy optimization, AI-005 generative AI lease abstraction |
| Cloud | Multi-account landing zone, vendor-agnostic |
| Registry defaults | Kept: the primary system (building automation and access control), the P08 incident (ransomware on building automation systems), and the P10 use case (video analytics for building access) fit this business. At this size the AI use case is widened to a portfolio and P08 adds a second incident type, as the tier requires |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork (property walkthroughs 2026-07-14 to 2026-07-23 at 6 of 14 properties) |
| 2026-08-03 to 2026-08-21 | Control assessment (co-sourced internal audit) |
| 2026-09-15 | Results to the audit committee; deliverables approved |

## 7. Operating details used across the deliverables (fictional)
These details make the deliverables specific. They do not change sections 1-6.

| Topic | Detail |
|---|---|
| Revenue split | Office about $58 million (Towers $46 million, Parks $12 million), retail about $30 million, mixed-use about $9 million, other about $3 million. Rent accrues daily: about $159,000 per day for office, $82,000 for retail, and $25,000 for mixed-use (about $274,000 per day in total) |
| Lease terms | The 2024 office lease template allows rent abatement after 3 consecutive business days of untenantable premises caused by landlord-controlled building systems; retail leases allow it after 5. About 60% of office leases by rent are on the 2024 template |
| Security Command Center | 24x7 at Tower 1: 6 console positions monitor video, door alarms, and BAS critical alarms for all 14 properties. Backup console positions at Tower 3 have never been used for a full shift |
| Cyber insurance | $10 million aggregate limit, $250,000 retention. The carrier's panel supplies breach counsel and forensics. The policy requires notice through the carrier hotline before incident vendors are engaged |
| MSSP | 24x7 monitoring; contract requires a call to the Security Manager within 30 minutes of a high-severity alert. OT systems send no logs |
| Workforce activity | 96 terminations and 41 internal transfers in the 12 months to 2026-06-30. The last IT access review was completed in February 2026. The June 2026 phishing simulation click rate was 6.1% |
| Tenant credentials | About 2,600 badge revocations were requested by tenants in the 12 months to 2026-06-30 |
| External exposure | The MSSP's external scan on 2026-07-21 found 2 NVRs (Retail 2, Retail 6) and the Platform B BAS web interface at Park 2 reachable from the internet through port forwarding |
| JV | The JV with an institutional investor owns Tower 3, Tower 4, Retail 5, and Mixed-Use 2. The management agreement (amended 2026-05) requires a SOC 2 Type 2 report on the company's property management and building operations services by 2027-12-31, and a SOC 1 report on rent billing and accounting (handled by the CFO outside P09) |
| Platform vendor recovery commitments | The access control and video platform vendor's SOC 2 system description states RTO 8 hours and RPO 1 hour for the cloud service. Door controllers cache credentials for up to 72 hours |
| Acquisitions | Two retail centers are under contract for purchase in 2027 (P01 R-045) |
| Additional role titles | Vice President of Leasing; HR Director; Director of Marketing and Communications |
