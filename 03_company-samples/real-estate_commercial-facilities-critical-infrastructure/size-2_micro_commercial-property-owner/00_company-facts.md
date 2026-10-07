# Scenario facts: Cris Santos Company | Commercial Facilities | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (Florida limited liability company; privately held by Cris Santos, the managing member) |
| Business | Owner-operator of two small multi-tenant commercial properties (NAICS 531120, Lessors of Nonresidential Buildings (except Miniwarehouses)). The company owns and self-manages both: leasing, rent collection, building engineering and maintenance, and building access |
| Location | Florida, one metro area. Two properties about 6 miles apart. The management office and the engineering room are in Property A |
| Property A (Office Building) | 3-story multi-tenant office building, about 44,000 rentable sq ft, 21 tenants (professional offices, the largest an insurance company's regional claims office of about 9,000 sq ft), 2 elevators, a shared tenant conference room, and a 140-space surface lot |
| Property B (Retail Center) | Single-story neighborhood strip center, about 26,000 sq ft, 12 retail and restaurant tenants. Tenants run their own storefronts, HVAC units, and systems. The company controls the rear service corridor doors, the electrical and utility room, and site cameras |
| Workforce | 7 employees: Managing Member (owner), Property Manager, Tenant Services and Leasing Coordinator, Bookkeeper, Building Engineer, 2 Maintenance Technicians |
| Revenue | About $1.1 million a year in rent and expense recoveries (fictional), about $92,000 a month. SBA-small (standard $34.0 million for NAICS 531120, 13 CFR 121.201) |
| People whose data the company holds | About 300 tenant employees, contractors, and staff with building credentials (name, employer, phone or email, credential number, door schedule, door access history; badge photos for about 190 Property A holders); video of people at both properties; about 60 individuals who applied or signed personal guaranties since 2019 (Social Security numbers, driver license copies, personal financial statements, and consumer credit reports); tenant business contacts and tenant bank details for ACH rent; 7 employees (HR files; payroll data at the payroll service) |
| Card acceptance | **The company is a merchant.** One terminal from a **validated PCI-listed point-to-point encryption (P2PE) solution**, supplied by the company's payment processor, at the Property A management office. Used for key fob replacement fees, after-hours HVAC charges, conference room bookings, and Property B seasonal kiosk and sidewalk-sale fees: about 600 transactions a year, in person or keyed on the terminal for phone orders. Rent is paid only by ACH through the tenant portal or by check |
| PCI DSS validation | Annual self-assessment on **SAQ P2PE** (PCI DSS v4.0.1), as stated in the acquirer's annual validation letter. The Bookkeeper prepared the 2025 SAQ P2PE and the Managing Member signed it on 2025-11-14 |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate and Retail subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule applies; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary |
| Not in scope | CCPA/CPRA (no California business; revenue far below the threshold). SEC cybersecurity disclosure (privately held). CIRCIA (proposed rule only; see P03). HIPAA (not a covered entity; medical and dental tenants run their own systems). Florida Digital Bill of Rights (applies only to controllers with more than $1 billion in global gross annual revenue, Fla. Stat. 501.702). Gaming and lodging rules (no such operations) |
| State law approach | Florida law is cited only where unavoidable (Fla. Stat. 501.171 reasonable security, breach notice, and disposal of customer records; Fla. Stat. 934.03 for audio recording). The samples otherwise stay federal |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Managing Member (owner) | Approves policies and the security budget; accepts Moderate and higher risks; signs the SAQ P2PE; decides on ransom, closures, and AI features |
| Property Manager | **Security and privacy lead** (designated in writing on 2026-07-15); day-to-day owner of access control, video, and tenant notices; directs the MSP; incident lead |
| Tenant Services and Leasing Coordinator | Issues and disables building credentials on tenant requests; front counter and card terminal; runs tenant screening and keeps lease application files |
| Bookkeeper | Rent, ACH, payables, the payroll service; prepares the SAQ P2PE |
| Building Engineer | Day-to-day owner of the building automation system (BAS) and its front-end workstation; coordinates the controls contractor; manual operation of HVAC plant |
| Maintenance Technicians (2) | Work orders on tablets; rounds at both properties; manual HVAC and door operation under the Building Engineer |
| Managed service provider (MSP) | Help desk, patching and antivirus on office computers, the Property A firewall and Wi-Fi, productivity suite administration, and the cloud backup service. 4-business-hour response; no recovery time commitment |
| Controls contractor | Programs and services the BAS under an annual service agreement; connects remotely through a remote-desktop tool on the BAS front-end workstation; keeps the only copies of field controller programs |
| Security integrator | Installed the access control and camera platform in 2023; services door hardware and cameras; keeps a standing administrator account in the platform |
| Janitorial contractor | Nightly cleaning at Property A; 6 staff with building credentials |
| Cyber insurer | Cyber liability policy with a 24x7 breach hotline and panel vendors (breach counsel, forensics); requires prompt notice and use of panel vendors |

## 3. Systems
| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Building automation system (BAS), Property A only: one BAS front-end workstation (desktop PC in the engineering room running the controls vendor's front-end software, graphics, trends, and alarms), one supervisory network controller, and about 60 BACnet field controllers (4 rooftop units, 48 VAV boxes, 2 exhaust fans, a lighting relay panel, 3 utility meters) | On-premises (OT) | Operational data; floor plans in the graphics | Field controllers keep running their last programs and schedules if the workstation or supervisory controller is lost. Rooftop units can be run by hand at the unit. The controls contractor connects through a remote-desktop tool installed on the workstation |
| SYS-02 | Access control: cloud-hosted access control platform with 9 door controllers and readers (Property A: front and rear entrances, service door, engineering room, management office, roof hatch; Property B: 2 rear service corridor doors and the electrical and utility room), fobs and phone credentials | Vendor SaaS plus on-premises door controllers (OT) | Yes: holder names, employers, contact details, badge photos, door access history | 342 active credentials at fieldwork. Property A entrances unlock weekdays 7:00 to 19:00 and need a credential at other times. Door controllers cache credentials and schedules and keep working for up to 72 hours without the cloud service. Entrance locks fail secure on power loss; egress is always free. The vendor provides a SOC 2 Type 2 report |
| SYS-03 | Video surveillance: 28 cloud-managed cameras (18 at Property A, 10 at Property B) on the same vendor platform as SYS-02 | Vendor SaaS plus on-premises cameras | Yes: video of identifiable people (no audio) | 30-day cloud retention. AI features: person detection alerts, and a face match trial at the Property A front entrance (P10) |
| SYS-04 | Property networks: Property A business firewall (MSP-managed), switches, staff Wi-Fi, and a separate guest Wi-Fi for the conference room; Property B ISP-supplied router | On-premises | In transit | One business internet line at each property, no failover. At Property A the BAS workstation, supervisory controller, door controllers, cameras, and office computers share one internal network |
| SYS-05 | Productivity suite (email, calendar, shared drive with sync client) | SaaS | Yes: lease application and guarantor files, contracts, HR files | Business plan; MFA by authenticator app for all 7 users; administered by the MSP |
| SYS-06 | Property management and accounting system with tenant portal, ACH rent collection, work orders, and lease documents | Vendor SaaS | Yes: tenant bank details, contacts, lease terms | System of record for leases and receivables. Vendor-enforced MFA |
| SYS-07 | Endpoints: 4 laptops (Managing Member, Property Manager, Tenant Services and Leasing Coordinator, Building Engineer), 2 desktops (Bookkeeper, front counter), 3 tablets (Building Engineer and both Maintenance Technicians) | MSP-managed (laptops and desktops); tablets self-managed | Yes (synced files, downloads) | Laptops encrypted; desktops not. Tablets run the work order app and the BAS graphics viewer |
| SYS-08 | Cloud backup service: nightly image of the BAS front-end workstation and nightly copy of the shared drive | SaaS backup (MSP-operated; subscription resold by the MSP) | Yes (copies of SYS-01 and SYS-05 data) | 30 days of versions; one MSP administrator login; never restore-tested |
| SYS-09 | Card payment terminal (1) | Payment processor's validated P2PE solution | Encrypted card data only | Stand-alone over cellular; the company never has clear-text card data in any system |
| SYS-10 | Online tenant screening service | Vendor SaaS | Yes: consumer credit reports on individual guarantors and applicants | Reports are downloaded as PDFs into the shared drive |
| SYS-11 | Payroll service | Vendor SaaS | Yes: employee Social Security numbers and bank details | Run by the Bookkeeper; biweekly payroll |

Outside the boundary: the fire alarm panels and their monitoring communicators, the elevators and their emergency phones (vendor-maintained, cellular), and every tenant's own network and systems. The BAS reads no life-safety points.

**SSP system (P02):** the *Building Automation and Access Control System (BAACS)*: the BAS (SYS-01), access control and video (SYS-02, SYS-03), the property networks (SYS-04), the BAS workstation image in the cloud backup (SYS-08), the laptops and tablets used to administer them (part of SYS-07), and the controls contractor's, security integrator's, and MSP's remote access paths.

## 4. Current security posture: early to partial
**In place today:**
- MFA by authenticator app on the productivity suite and the property management system (vendor-enforced)
- MSP patching and antivirus on the 6 office computers; the Property A business firewall blocks unsolicited inbound traffic; guest Wi-Fi separated
- Laptop encryption
- A cloud access control and video platform whose vendor provides a SOC 2 Type 2 report; door controllers that cache credentials; fail-secure entrance locks with free egress
- Card acceptance only through a validated P2PE terminal; SAQ P2PE filed for 2025
- Nightly cloud backup of the BAS workstation and the shared drive (MSP-operated)
- A cyber liability policy with a breach hotline
- Life-safety systems on separate vendor-maintained communicators
- A new-hire security video

**Missing:**
1. No risk assessment, no written policies, and no security and privacy lead until the Property Manager was designated on 2026-07-15.
2. One flat network at Property A: the BAS workstation, supervisory controller, door controllers, cameras, and office computers share it. Property B building devices sit on an ISP router.
3. The controls contractor reaches the BAS workstation through an always-on remote-desktop tool with one shared contractor account, password only, no session approval, and no session log.
4. The BAS workstation uses one shared "engineer" login with automatic sign-in. At the controls contractor's request, the MSP has excluded it from patching and antivirus since March 2025. The BAS software is one major version behind.
5. No MFA on the access control and video platform administrator accounts, although the platform supports it. The security integrator keeps a standing full administrator account.
6. Credentials are disabled only when a tenant remembers to ask. No periodic review.
7. Backups are not immutable, keep 30 days, use one MSP administrator login, and have never been restore-tested. Field controller programs exist only at the controls contractor.
8. No incident response plan and no written manual procedures for running HVAC and doors without the BAS or the cloud platform.
9. No review of logs: platform administrator audit logs, firewall logs, or remote access.
10. Guarantor and applicant files (Social Security numbers, driver license copies, credit reports) are kept in the shared drive and in email indefinitely. No retention or disposal rule.
11. MSP, controls contractor, security integrator, and janitorial contracts have no security terms or incident notice clauses.
12. Card handling: staff write card numbers from phone orders on a notepad before keying them into the terminal. Terminal inspections and tampering training from the P2PE Instruction Manual (PIM) are not done.
13. No inventory of building devices and no network diagram.
14. Training is the new-hire video only: no phishing exercises and no OT training for the engineering staff.
15. The video platform's face match feature was turned on as a trial at the Property A front entrance in June 2026 without any assessment or notice. There is no list of approved AI features.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | CISA CPG 2.0 (all 34 goals, voluntary benchmark, OT lines tailored with NIST SP 800-82 Rev. 3); PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) as the binding-by-contract standard; legal baseline: FTC Act Section 5, Fla. Stat. 501.171(2) and (8), and the FTC Disposal Rule (16 CFR 682.3(a)) for consumer credit reports |
| P08 incident | Ransomware on the BAS: the attacker signs in through the controls contractor's remote-desktop tool with a reused password, encrypts the BAS front-end workstation, and spreads over the flat Property A network to the office desktops and the synced shared drive, taking the leasing folder. The MSP, the controls contractor, and the insurer are in the notification chain |
| P09 SOC 2 | Not a service organization. Security plus Confidentiality self-assessment, used to answer the security questionnaire the largest Property A tenant sent with its lease renewal; plus a review of the access control and video platform vendor's SOC 2 Type 2 report |
| P10 AI | Video analytics for building access: AI-001 face match alerts at the Property A front entrance after hours (vendor trial, paused) |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-08). Vendor-agnostic |
| Registry adaptation | The registry defaults are kept. At this size the "building automation system" is one front-end workstation, one supervisory controller, and about 60 field controllers at Property A, not a server; the access control and video systems are a cloud platform |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis with the MSP (walkthroughs of both properties 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant; on site 2026-08-11) |
| 2026-08-31 | Deliverables approved by the Managing Member |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Benchmark adoption | The Managing Member adopted CISA CPG 2.0 as the security benchmark on 2026-07-15, the same day the Property Manager was designated security and privacy lead | P02, P03 |
| Leases | All leases require notice of building service interruptions. Leases signed since 2024 also require notice within 72 hours of learning of unauthorized access to the tenant's employees' data in the access control system. Leases allow rent abatement after 5 consecutive business days of untenantable premises | P05, P08 |
| Finances | A cash reserve covers about 45 days of expenses. An on-call guard from a local guard company costs about $40 an hour | P05 |
| Vendor terms | Property management system: RPO 1 hour and 99.5% availability in its service terms. Controls contractor: next-business-day on-site response. Platform vendor: 72-hour customer incident notice in its subscription terms | P05, P09 |
| Logs | Platform administrator and door logs kept 1 year by the vendor; Property A firewall logs 7 days; the remote-desktop service keeps 30 days of connection history; nothing is reviewed | P02, P07, P08 |
| Network details | The MSP runs a quarterly external port scan of the Property A address (last 2026-07-14: no open ports). The engineering room and network closet need a credential. The Property B router also provides Wi-Fi for seasonal kiosk vendors | P02, P03, P07 |
| Email | The MSP set up SPF and DKIM; the DMARC record is set to monitor only | P03 |
| BAS workstation use | The workstation is also used to read email, and contractor technicians load programs from their own USB drives | P02, P03 |
| Past events | A Maintenance Technician left in April 2026 (since replaced); the fob and platform account were disabled 9 days after the last day. An engineering tablet was lost in 2025 and never reported to the Property Manager. A desktop replaced in 2025 went to the MSP with no wipe record | P02, P03, P07, P09 |
| Credential review | 51 of 342 active credentials had not been used in 90 days or more. They were sent to tenant contacts on 2026-07-28; 38 were disabled by 2026-08-07. A sample of 25 credentials found 6 (imported at the 2023 installation) with no request form | P01, P02, P07 |
| Leasing files | The guarantor and applicant folder is open to all 7 staff and synced to the desktops; applicant files go back to 2019, including applicants who never signed a lease. Applications arrive by plain email | P01, P03, P06 |
| Assessor | The P07 assessor is an independent security consultant with building systems experience, not involved in the risk assessment or the gap analysis | P07 |
| P07 test findings | The supervisory controller accepted the manufacturer default administrator password. The Property B router accepted its factory default password and had UPnP on; the password was changed and UPnP turned off on 2026-08-12. One of the 4 contractor technicians who know the shared remote-desktop password left the contractor in 2025 | P01, P07 |
| Backup jobs | July 2026: 31 of 31 nightly shared drive copies and 29 of 31 nightly workstation images succeeded | P07 |
| Platform vendor report | SOC 2 Type 2, Security and Availability, 12 months ending 2026-03-31, unqualified, one remediated exception; 99.9% monthly availability target. Analytics features are not in the report. Reviewed 2026-08-20 | P02, P09 |
| Tenant questionnaire | The largest Property A tenant sent a security questionnaire in July 2026 with its lease renewal; response due 2026-09-30; renewal decision due 2027-01-31 | P09 |
| Face match trial | Turned on 2026-06-08 by the vendor at the security integrator's request after a tenant complained in May about unfamiliar people at night. Templates were created from about 190 badge photos. 1,240 after-hours entries, 87 alerts, 3 real. Paused 2026-07-24; template deletion and training opt-out requested 2026-08-26. Fob plus PIN after hours at the Property A front entrance from 2026-10-15 | P01, P04, P10 |
| Person detection | After-hours person detection alerts on the Property B rear corridor and parking cameras have been in use since 2024; 41 of the last 60 alerts showed a real person | P10 |
| Monthly security meeting | The Managing Member and the Property Manager meet monthly from September 2026 to review the POA&M and the platform administrator change report | P02, P03, P09 |
