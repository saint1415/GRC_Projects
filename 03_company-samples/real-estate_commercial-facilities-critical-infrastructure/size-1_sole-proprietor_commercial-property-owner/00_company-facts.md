# Scenario facts: Cris Santos Company | Commercial Facilities | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; no separate legal entity; the owner is personally liable for the business) |
| Business | Owner-operator of one small mixed-use commercial building (NAICS 531120, Lessors of Nonresidential Buildings (except Miniwarehouses)). The owner leases the space and self-manages it: leasing, rent collection, maintenance coordination, and building access |
| Location | Florida. One two-story building of about 9,500 rentable sq ft on a commercial street, with a 24-space surface parking lot. The owner works from a home office and from a small management closet in the building's utility room |
| Tenants | 8 tenants: 3 ground-floor retail and food-service tenants (a cafe, a dry-cleaning drop-off, a nail salon) and 5 second-floor professional offices (including an insurance agency and a tax preparation office). Each tenant runs its own internet service and its own systems |
| Workforce | The owner only (0 employees). Uses contracted services instead of staff |
| Revenue | About $180,000 a year in rent and expense recoveries (fictional), about $15,000 a month. SBA-small (standard $34.0 million for NAICS 531120, 13 CFR 121.201) |
| Tax note | The owner's outside CPA prepares the return. The tier default in the README says Schedule C. The IRS Instructions for Schedule E say rental real estate activity is generally reported on Schedule E even if it is a trade or business, and on Schedule C only if significant services (such as maid service) are provided to the renter. This does not affect the security work |
| People whose data the business holds | About 40 tenant employees, 2 janitorial contractor staff, and 1 HVAC technician with building credentials (name, employer, phone or email, credential number, door schedule, and door access history); video of anyone at the entrances and in the parking lot; about 15 individuals who signed personal guaranties or applied as guarantors since 2022 (Social Security numbers, driver license copies, personal financial statements, and consumer credit reports); tenant business contacts and the tenants' business bank details used for ACH rent |
| Card acceptance | **None.** The owner is not a merchant. Rent is paid by ACH through the property management SaaS tenant portal (its payment partner moves the funds) or by check. No card terminal, no card-not-present payments |
| Sector context | Commercial Facilities critical infrastructure sector (Real Estate and Retail subsectors). Sector Risk Management Agency: CISA. No mandatory federal cybersecurity rule applies; the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0, December 2025) are voluntary |
| Not in scope | PCI DSS (no card acceptance; reassess if card payments are ever turned on in the tenant portal). CCPA/CPRA (no California business; revenue far below the threshold). SEC cybersecurity disclosure (not a public company). CIRCIA (proposed rule only; see P03). HIPAA (no covered functions; tenants run their own systems). Florida Digital Bill of Rights (applies only to controllers with more than $1 billion in global gross annual revenue, Fla. Stat. 501.702). Life-safety systems (see SYS notes) |
| State law approach | Florida law is cited only where unavoidable (Fla. Stat. 501.171 reasonable security, breach notice, and disposal of customer records; Fla. Stat. 934.03 for audio recording) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner | Every role: owner, security lead, privacy lead, system administrator for every building system and SaaS account, incident commander, and risk acceptor |
| Access control and camera installer (security integrator) | Installed SYS-01 and SYS-02 in 2024. Services door hardware and cameras on call. **Keeps a standing administrator account in both cloud portals**; no written security terms |
| HVAC service contractor | Quarterly maintenance and emergency calls for the 8 rooftop units. **Signs in to the thermostat platform with the owner's own login (shared password)**. Holds one building credential |
| On-call IT consultant | Hourly help. Set up the router in 2023. No standing access |
| Outside CPA | Bookkeeping review and tax return. Has a named accountant-role account in SYS-05 and reads the lease application folder through a shared link |
| Janitorial contractor | Nightly cleaning of common areas; 2 staff with building credentials |
| Real estate attorney | Leases and legal questions; first call for breach questions until the insurer's breach counsel is engaged |
| Fire alarm monitoring company and elevator maintenance contractor | Maintain the life-safety systems on their own cellular communicators (outside the security boundary) |

## 3. Systems
| ID | System | Hosting | Sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Cloud-managed access control: 4 door controllers and readers (front entrance, rear entrance, second-floor corridor door, utility room), key fobs and phone credentials, admin web portal and phone app | Vendor SaaS plus on-premises door controllers | Yes: credential holder names, employers, contact details, door access history | 58 active credentials. Entrances unlock on a schedule (weekdays 7:00 to 19:00, Saturday 8:00 to 14:00) and need a credential at other times. Door controllers cache credentials and schedules and keep working if the internet or the cloud service is down. Egress is always free (mechanical exit hardware). The vendor provides a SOC 2 Type 2 report |
| SYS-02 | Cloud video: 6 cameras (2 entrances, lobby, rear service area, 2 parking lot) with cloud recording | Vendor SaaS plus on-premises cameras | Yes: video of identifiable people | 30-day cloud retention. AI features: person and vehicle detection alerts, and a "familiar faces" face recognition feature (see P10). The 2 entrance cameras recorded audio by default until 2026-07-21 |
| SYS-03 | Smart thermostats: 8 cloud-connected thermostats, one per rooftop HVAC unit and tenant space | Vendor SaaS plus on-premises thermostats (Wi-Fi) | No (operational schedules and setpoints) | This is the building automation at this size. Thermostats keep their last schedule and can be adjusted at the wall if the internet or cloud service is down. One owner login, shared with the HVAC contractor |
| SYS-04 | Building network: one business internet line and one ISP-supplied router with Wi-Fi in the utility room | On-premises | In transit | Serves SYS-01 to SYS-03 and a "free lobby Wi-Fi" network name for retail customers. Guest isolation is off, so customers' devices and building devices share one flat network |
| SYS-05 | Property management and accounting SaaS with tenant portal, ACH rent collection, maintenance requests, and lease document storage | Vendor SaaS | Yes: tenant bank details, contacts, lease terms | System of record for leases and receivables. The vendor enforces MFA (authenticator app) |
| SYS-06 | Business email and file storage suite (custom domain) | SaaS | Yes: lease applications, guarantor documents, credit reports, contracts | MFA on, by text-message codes. The lease application folder has been shared with the CPA by an "anyone with the link" link since 2024 |
| SYS-07 | Laptop | Owner device | Yes (synced files, downloads, browser-saved passwords) | Full-disk encryption on by default, automatic OS updates, built-in antivirus. Passwords for every building portal are saved in the browser |
| SYS-08 | Smartphone (personal, also used for the business) | Owner device | Yes (apps for SYS-01 to SYS-03, MFA text codes, the owner's own door credential) | Passcode and biometric unlock |
| SYS-09 | Online tenant screening service | Vendor SaaS | Yes: consumer credit reports on individual guarantors; business credit reports on tenants | Reports are downloaded as PDFs into SYS-06 |

Outside the boundary: the fire alarm panel (monitored by the fire alarm monitoring company over its own cellular communicator), the elevator and its emergency phone (cellular), and every tenant's own network and systems.

**SSP system (P02):** the *Property Systems Profile (PSP)*: the cloud-managed building access, camera, and climate control services (SYS-01 to SYS-03) plus the building network, the owner's SaaS stack, and the owner's devices (SYS-04 to SYS-09).

## 4. Current security posture: early (few formal controls)
**In place today:**
- MFA on the property management SaaS (vendor-enforced) and on email (text-message codes)
- Full-disk encryption, automatic OS updates, and built-in antivirus on the laptop; passcode on the phone
- Rent by ACH through the property management SaaS; no card acceptance
- Vendor-kept door event logs (SYS-01) and 30-day cloud video (SYS-02)
- Door controllers that cache credentials and schedules; thermostats that keep their schedules offline; mechanical door keys held by the owner
- Paper lease files in a locked cabinet in the owner's home office
- A business owner's insurance policy with a data compromise endorsement (notification costs and a breach response hotline; no cyber extortion or funds-transfer fraud coverage)
- Life-safety systems on their own cellular communicators, not on the building network

**Missing:**
1. No risk assessment and no written policies.
2. No MFA on the access control, camera, or thermostat administrator accounts, although all three platforms offer it. The thermostat password is shared with the HVAC contractor.
3. The installer keeps standing administrator accounts in the access control and camera portals. Nobody has reviewed them or checked whether they use MFA.
4. One flat building network: door controllers, cameras, thermostats, and the free lobby Wi-Fi share it. The router administrator password is the factory default and its firmware has not been updated since 2023.
5. Passwords are saved in the laptop browser and reused across several accounts. No password manager.
6. Building credentials are not removed when tenant employees or contractors leave. Tenants are not asked to confirm their lists.
7. Guarantor files (Social Security numbers, driver license copies, credit reports) sit in email attachments and in a folder shared by "anyone with the link". No retention or disposal rule.
8. No backup of email and files beyond the provider's deleted-items retention, no export of the access control configuration, and no backup of the laptop.
9. No incident plan, no contact list, and no written manual procedures for running doors and HVAC without the cloud services.
10. Contractors (installer, HVAC contractor, IT consultant, janitorial contractor) have no written security terms or incident notice clauses.
11. The camera service's "familiar faces" face recognition was turned on in a trial without any assessment or notice, and the entrance cameras recorded audio by default.
12. No security training for the owner.
13. The owner is the only person who can run doors, HVAC, cameras, and rent. Every second factor is on one phone.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | CISA CPG 2.0 (all 34 goals, voluntary benchmark, OT lines tailored with NIST SP 800-82 Rev. 3 for door controllers, cameras, and thermostats), plus the legal baseline that binds the owner: FTC Act Section 5, Fla. Stat. 501.171(2) and (8), and the FTC Disposal Rule (16 CFR 682.3) for consumer credit reports on guarantors. PCI DSS is recorded as not applicable because the owner is not a merchant |
| P08 incident | Ransomware on the owner's laptop that reaches the cloud building controls: the attacker uses browser-saved passwords to sign in to the access control and thermostat portals and takes guarantor files. Adapted from the registry default "Ransomware on building automation systems" because at this size there is no on-premises BAS server to encrypt; the building automation is cloud-managed and is reached through the owner's credentials |
| P09 SOC 2 | Security criteria only. The owner's self-check supports a one-page security letter for tenants that ask (the insurance agency did in 2026). Plus a review of the access control vendor's SOC 2 Type 2 report |
| P10 AI | Video analytics for building access: the camera service's AI features. AI-001 "familiar faces" face recognition (trial, retired); AI-002 person and vehicle detection alerts (in use) |
| Cloud | SaaS only. No IaaS. Vendor-agnostic service categories |
| Registry adaptation | The registry's primary system "Building automation and access control system" is kept as the cloud-managed access control, camera, and smart thermostat services (SYS-01 to SYS-03). A one-building sole proprietor has no BAS server, field controller network, or security console |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT consultant (building walkthrough 2026-07-21; tests 2026-07-23) |
| 2026-08-31 | Deliverables adopted by the owner |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Benchmark adoption | The owner adopted CISA CPG 2.0 as the security benchmark on 2026-07-17, before the self-assessment | P02, P03 |
| Door hardware | Entrance locks fail secure on power loss; egress is always free through mechanical exit hardware | P01, P08 |
| Building device management | Door controllers, cameras, and thermostats have no local login; they are managed only through their cloud accounts. Automatic firmware updates are on in all three platforms. All three platforms offer app-based MFA, and the thermostat platform supports invited users with limited rights | P03, P04 |
| Installer accounts | The installer has two administrator accounts, one in the access control portal and one in the video portal, both with full rights and no MFA | P01, P07 |
| Credential review | Tenants and contractors were asked to confirm their credential lists on 2026-07-22. By 2026-07-24, 7 of the 58 active credentials were found to belong to people who had left; the owner disabled them on 2026-07-24. Some holders have both a fob and a phone credential, so the credential count is higher than the number of people | P01, P02, P03, P07 |
| Public folder link | The "anyone with the link" share of the lease application folder opened from a signed-out browser in testing on 2026-07-23. The owner removed it on 2026-08-05, after setting up a named share for the CPA | P01, P03, P07, P09 |
| Network tests (2026-07-23) | An external port check found no open ports on the building's public address. A network scan from a phone on the free lobby Wi-Fi listed the cameras, door controllers, and thermostats. The router accepted its factory password | P03, P07 |
| Email domain | The email provider published an SPF record at setup; DKIM signing is off and there is no DMARC record | P03 |
| Laptop | The owner uses the laptop's administrator account for daily work. The office suite blocks macros in files from the internet by default, and autorun is off | P03 |
| Camera AI and audio | The owner turned on the video vendor's "familiar faces" feature during a free trial on 2026-05-04 and named 9 recurring people (2 janitorial staff, the HVAC technician, 6 tenant employees). Face recognition and entrance audio were turned off on 2026-07-21. The owner opted out of vendor model training and asked for deletion of face data on 2026-07-24; the vendor confirmed deletion on 2026-08-12 | P04, P10 |
| Person and vehicle alerts | After-hours (19:00 to 7:00) alerts on the rear service area and parking lot cameras, in use since 2024. 41 alerts from 2026-06-22 to 2026-07-21, 33 showing a real person | P10 |
| Access control vendor report | SOC 2 Type 2, Security and Availability, 12-month period ending 2026-04-30, unqualified, one remediated exception; 99.9% monthly availability target. Reviewed 2026-07-23. The camera and thermostat vendors offered no assurance report for their small-business plans | P02, P09 |
| Contracts | Leases have no data incident clause. The tenant screening service's terms include an end-user certification under the Fair Credit Reporting Act | P02, P08 |
