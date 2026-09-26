# Scenario facts: Cris Santos Company | Commercial Facilities | Small

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner) |
| Business | Owner-operator of multi-tenant office and retail property (NAICS 531120, Lessors of Nonresidential Buildings (except Miniwarehouses)). The company owns and self-manages its buildings: leasing, property management, engineering, and building security |
| Location | Florida, one metro area. Three properties 10 to 20 miles apart. Headquarters and the management office are in Property A |
| Property A (Office Tower) | 12-story multi-tenant office building, about 260,000 sq ft, 38 tenants, about 1,300 active badge holders, 6 lobby turnstile lanes, a staffed security console (24x7), and the engineering server room |
| Property B (Retail Center) | Open-air community shopping center, about 185,000 sq ft, 44 retail and restaurant tenants. The 700-space parking garage is run by a contracted parking operator |
| Property C (Office Park) | Three 2-story office buildings, about 140,000 sq ft, 19 tenants, about 450 active badge holders |
| Workforce | 60 employees: 6 executive and administration, 10 property management and tenant services, 3 leasing and marketing, 6 accounting and lease administration, 24 engineering and maintenance, 9 security operations, 2 IT |
| Revenue | $20.4 million a year in rent and expense recoveries (fictional). Under the SBA standard of $34.0 million for NAICS 531120 (13 CFR 121.201), so SBA-small |
| People whose data the company holds | About 1,750 tenant employees with access credentials (name, employer, badge photo, credential number, door schedule, access history); about 150 registered visitors per business day at Property A (the lobby kiosk scans a government ID); 60 employees (HR and payroll data); tenant contacts and tenant bank details for ACH rent payments |
| Card acceptance | The company **is a merchant**. It takes cards at the management offices (Property A and Property B) for conference-center and event-space bookings, after-hours HVAC charges, badge replacement fees, and seasonal kiosk license fees, about 2,100 transactions a year. Payment is only through 3 terminals from a **validated PCI-listed point-to-point encryption (P2PE) solution** supplied by the company's payment processor. Rent is paid by ACH through the tenant portal (no cards). Parking revenue belongs to the parking operator, which is the merchant of record for the garage |
| PCI DSS validation | Annual self-assessment on **SAQ P2PE** (PCI DSS v4.0.1 SAQ P2PE, October 2024), as confirmed by the acquirer in its annual validation letter. The 2025 SAQ P2PE was signed by the Controller on 2025-11-20 |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate and Retail subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule applies to the company; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary |
| Not in scope | CCPA/CPRA: the company does not do business in California and its revenue is below the threshold. SEC cybersecurity disclosure: privately held. CIRCIA: proposed rule only, and the NPRM relies on a size criterion the company does not meet (see P03). HIPAA: not a covered entity (one medical office tenant runs its own systems). Florida Digital Bill of Rights: applies only to controllers with more than $1 billion in global gross annual revenue (Fla. Stat. 501.702). Gaming and lodging rules: no such operations |
| State law approach | Florida law is cited only where a Florida duty is unavoidable (Fla. Stat. 501.171 breach notice, reasonable security, and record disposal; Fla. Stat. 934.03 for audio recording). The samples otherwise stay federal |

## 2. People (role titles only)

| Role | Security and privacy duties |
|---|---|
| Majority owner (Cris Santos, CEO) | Approves the security budget; accepts High and Very High risks |
| Chief Operating Officer (COO) | Executive owner of the security program; accepts Moderate risks; signs policies; system owner of the building systems platform |
| IT Manager | Security and compliance lead (part-time duties alongside IT operations); runs IT with a contracted managed service provider |
| IT Support Specialist | Help desk escalation, endpoint and account administration |
| Director of Engineering | Owns the building automation system (HVAC, lighting, metering); manages the chief engineers and the BAS integrator |
| Chief Engineers (3, one per property) | Day-to-day BAS operation, engineering workstations, manual operation of plant equipment |
| Security Manager | Owns physical access control, video surveillance, visitor management, and the security console; manages the contracted guard service |
| Controller | Owns PCI DSS compliance, the merchant agreement, and the SAQ; accounting and payroll data owner |
| Property Managers (3) | Tenant relationships, tenant notices, lease obligations |
| HR Manager | Onboarding, terminations, training records |
| Managed service provider (MSP) | Help desk, patching of corporate endpoints and servers, EDR monitoring (24x7), firewall administration |
| BAS integrator | Controls contractor that programs and supports the BAS under a service agreement, with remote access |
| Access control and video integrator | Installs and services door controllers, readers, turnstiles, cameras, and recorders |
| Contracted guard service | Patrol guards at Property B and Property C; remote video viewing |
| Parking operator | Runs the Property B garage under a management agreement; merchant of record for parking |

## 3. Systems

| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Building automation system (BAS): supervisory server (a virtual machine on the on-premises host at Property A), 2 engineering workstations, about 420 BACnet field controllers (chillers, air handlers, VAV boxes, lighting, meters) across all three properties | On-premises (OT) | Operational data; building drawings | Field controllers keep running their last programs and schedules if the supervisory server is lost. The BAS integrator connects through a vendor remote-support tool installed on the server |
| SYS-02 | Physical access control system (PACS): cloud-hosted access control platform with 46 on-premises door controllers, about 180 card readers, and 6 turnstile lanes | Vendor SaaS plus on-premises (OT) | Yes: tenant employee names, employers, badge photos, credential numbers, access history | Door controllers cache credentials and keep working for up to 72 hours without the cloud service. The vendor has a SOC 2 Type 2 report |
| SYS-03 | Video surveillance: about 260 cameras and 4 network video recorders (NVRs), managed from the same vendor platform as SYS-02 | On-premises plus vendor SaaS | Yes: video of people (no audio) | 30-day retention on NVRs. Hosts the video analytics pilot (P10) |
| SYS-04 | Property networks: firewalls, switches, and Wi-Fi at each property, including the OT segments for SYS-01 to SYS-03; site-to-site VPN from Properties B and C to Property A and to SYS-08 | On-premises | In transit | OT segmentation exists only at Property A, and it is weak (see gaps) |
| SYS-05 | Identity provider (single sign-on and MFA) | SaaS | Identities only | Protects SYS-06, SYS-07, SYS-08, and the SYS-02 administrator portal |
| SYS-06 | Productivity suite (email, files, chat) | SaaS | Yes (incidental) | Includes the events mailbox used for conference bookings |
| SYS-07 | Property management and accounting system with tenant portal, ACH rent payments, and engineering work orders | Vendor SaaS | Yes: tenant bank details, contacts, lease terms | System of record for leases and receivables |
| SYS-08 | Cloud tenant (IaaS/PaaS) | Public cloud provider (vendor-agnostic) | Yes (building drawings, corporate files) | Hosts three company-managed workloads: the BAS historian and energy dashboard, file storage for drawings and corporate files, and the backup vault |
| SYS-09 | Endpoints | On-premises | Yes (cached) | 72 laptops and desktops (including 6 security console PCs) and 24 tablets used by engineers for work orders and BAS graphics |
| SYS-10 | Card payment terminals (3) | Payment processor's validated P2PE solution | Encrypted card data only | Stand-alone; the company never has clear-text card data in any system |
| SYS-11 | Visitor management (lobby kiosks at Property A) | Vendor SaaS | Yes: visitor names, photos, and scanned driver license or ID numbers | ID scans are kept indefinitely (see gaps) |
| SYS-12 | HR and payroll | Vendor SaaS | Yes: employee Social Security numbers and bank details | |
| SYS-13 | Life-safety systems: fire alarm panels, elevator controls, emergency voice communication | Vendor-maintained, separate networks | No | Outside the IT and OT scope. The BAS reads fire alarm status through hardwired relay points only (read-only) |

**SSP system (P02):** the *Building Automation and Access Control System (BAACS)*: SYS-01, SYS-02, SYS-03, the OT segments and shared firewalls of SYS-04, the BAS historian and backup vault in SYS-08, the engineering workstations and security console PCs in SYS-09, and their interfaces to SYS-05, SYS-11, and the integrators' remote access.

## 4. Current security posture: partially compliant

**In place today:**
- MFA through the identity provider for email, the property management system, the cloud console, and the access control platform's administrator portal
- EDR with 24x7 alerting by the MSP on corporate laptops, desktops, and security console PCs
- Automatic OS patching on corporate endpoints
- Next-generation firewalls at all three properties; site-to-site VPN; no inbound services on corporate networks
- A cloud-hosted access control platform whose vendor provides a SOC 2 Type 2 report
- Card acceptance only through validated PCI-listed P2PE terminals; SAQ P2PE filed for 2025
- Daily backups of the cloud tenant's file storage and historian, and a weekly image of the BAS server, all stored in the same cloud account and region
- A cyber insurance policy with a breach hotline
- Badge access and cameras on the Property A server room and all engineering rooms
- An annual security awareness video for all staff
- Fire alarm and life-safety systems on separate vendor-maintained networks, with only read-only relay points into the BAS
- A lease template (2023 and later) that requires the landlord to notify tenants promptly of any unauthorized access to tenant employee data held in the access control system; 12 tenants negotiated a 72-hour notice clause

**Missing or weak, found in the 2026 assessments:**
1. OT networks are not segmented. At Property A the BAS network is a separate network segment but routes to the corporate network with permissive rules. At Properties B and C, BAS controllers, door controllers, and NVRs share the flat corporate network.
2. The BAS integrator's remote access uses an always-on vendor remote-support tool on the BAS server, with a shared vendor account, no MFA, no session approval, and no session logging.
3. The BAS server and engineering workstations use one shared "engineer" login that is not in the identity provider. P07 testing also found manufacturer default passwords on 12 BACnet field controllers at Property B and on 2 NVRs.
4. The BAS server runs an operating system past vendor support, is excluded from EDR, and is patched only when the integrator visits. The BAS software is two major versions behind.
5. There is no OT asset inventory and no network diagram for BAS, access control, or video devices. P07 testing found 31 of 144 field controllers at Property B missing from the integrator's device list.
6. BAS backups are a weekly server image in the same cloud account as production, not immutable. Field controller programs and graphics are held only by the integrator. No restore has ever been tested.
7. There is no written incident response plan, and no manual (degraded-mode) operating procedures for HVAC or doors.
8. There is no central log collection or review for the BAS, access control administrator actions, firewalls, or remote access sessions. Default retention only.
9. Credential revocation is slow. Employee accounts are disabled within about 3 business days. Tenant employee badges are revoked only when a tenant asks; 212 active badges have not been used in more than 90 days. No periodic review.
10. Integrator, MSP, guard, and parking operator contracts have no security requirements or incident notice clauses, and no vendor security review is done.
11. An NVR at Property B is exposed to the internet through port forwarding for the guard contractor's remote viewing (found by the MSP's external scan on 2026-07-16).
12. The visitor management system keeps driver license scans and photos indefinitely. There is no retention or disposal rule.
13. Training is an annual video only. There are no phishing exercises and no OT-specific training for engineers or security console operators.
14. Card handling: event staff write card numbers and security codes on paper booking forms kept in a binder, and 3 emails containing card numbers were found in the events mailbox. POI device inspections and tampering training (from the P2PE Instruction Manual) are not done.
15. The video analytics vendor enabled a tailgating-detection feature in May 2026 as a pilot without any assessment, and has proposed face verification at the turnstiles. There is no AI approved-tools list.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | CISA CPG 2.0 (voluntary; all 34 goals, tailored for OT with NIST SP 800-82 Rev. 3) as the primary benchmark; PCI DSS v4.0.1 (SAQ P2PE requirements) as the binding-by-contract secondary standard; Fla. Stat. 501.171(2) and (8) and FTC Act Section 5 as the legal baseline |
| P08 incident | Ransomware on building automation systems, entering through the BAS integrator's remote-support tool |
| P09 SOC 2 | Not a service organization. (a) Security-only (CC1-CC9) self-benchmark; (b) review of the access control and video platform vendor's SOC 2 Type 2 report |
| P10 AI | Video analytics for building access: AI-001 tailgating detection (pilot at Property A turnstiles); AI-002 face verification against badge photos (vendor proposal, not approved) |
| Cloud | Vendor-agnostic. Services are described by category, with AWS, Azure, and Google Cloud equivalents noted only where needed for shared responsibility |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork (property walkthroughs 2026-07-15 to 2026-07-17) |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork |
| 2026-08-31 | Deliverables approved by the Chief Operating Officer |
