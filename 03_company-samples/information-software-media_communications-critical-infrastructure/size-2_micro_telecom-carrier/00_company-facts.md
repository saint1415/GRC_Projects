# Scenario facts: Cris Santos Company | Communications | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Legal status was checked against eCFR (point in time 2026-09-23) and the Federal Register (searched through 2026-10-05).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; the owner is the General Manager) |
| Business | Rural fiber broadband and voice carrier (NAICS 517111). Built a fiber-to-the-home (FTTH) network in one rural north Florida town and the farmland around it between 2017 and 2021. Services: fiber broadband internet access; **interconnected VoIP** voice under the company's own brand, delivered over the fiber through a **wholesale hosted voice platform**; 6 dedicated internet access circuits for local business and public customers. **No** legacy copper or TDM switching, **no** video, **no** wireless (CMRS), **no** submarine cable |
| Location | Florida. One office building in town (customer counter, 4 workstations, small warehouse bay, network closet) and one **network hut** on a fenced company lot about 1 mile away (optical line terminals, edge router, 2 small servers, batteries, propane standby generator). About 140 route miles of fiber with passive splitters (no electronics in the field). All internet traffic leaves over **one leased 10 Gbps middle-mile circuit** to an upstream transit provider |
| Workforce | 7 employees: Owner and General Manager, Office Manager, Network Operations Lead, 2 Field Technicians, 2 Customer Service Representatives |
| Customers | About 1,420 accounts (1,330 residential, 90 business). About 1,385 broadband subscribers. About 440 telephone numbers on about 390 voice accounts. 6 dedicated internet access circuits (including the town hall and a community bank branch) with a 99.9% monthly availability commitment. A driver license number is recorded at sign-up for identity checks on about 1,050 accounts (practice since 2019) |
| Revenue | About $1.1 million a year (fictional), about $3,000 per day. The SBA size standard for NAICS 517111 is 1,500 employees (13 CFR 121.201), so the company is SBA-small |
| Regulatory status | **Interconnected VoIP provider**, which the CPNI rules treat as a telecommunications carrier (47 CFR 64.2003(o)). **Broadband internet access provider**: broadband is an information service after *Ohio Telecom Ass'n v. FCC* (6th Cir. Jan. 2, 2025), and the FCC conformed its rules (90 FR 38406, 2025-08-08). **Wireline communications provider and interconnected VoIP provider** for outage reporting (47 CFR 4.3(g), (h)). **Covered by CALEA** as a facilities-based broadband internet access provider and an interconnected VoIP provider (FCC First Report and Order, 70 FR 59664, effective 2005-11-14; 47 CFR 1.20002(e)(3)) |
| Customer commitments | Website privacy policy and terms of service; broadband consumer labels (47 CFR 8.1); business contracts for the 6 dedicated circuits with service credits for missed availability |
| Not in scope | SEC disclosure rules (privately held; C-COMMUNICATIONS-R06). Submarine cable rules (C-COMMUNICATIONS-R04). CMRS-only CPNI rules (64.2010(h)). Emergency Alert System rules (no video or broadcast service). FAR clauses (no federal contracts). Payment card data: cards and bank accounts are taken on the payment processor's hosted page and stored as tokens; PCI DSS duties are contractual and outside this sample |
| State law approach | Florida law is cited only where unavoidable: breach notification (Fla. Stat. 501.171). The company serves only Florida addresses |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Owner and General Manager | Accepts Moderate and higher risks; approves policies and spending; **officer who signs the annual CPNI certification** (47 CFR 64.2009(e)); **CALEA senior officer** named in the 2017 SSI filing (47 CFR 1.20003(a)) |
| Office Manager | **Security and compliance lead** (designated in writing 2026-07-15); CPNI compliance coordinator; billing system (BSS) administrator; HR, vendor contracts, and records; accepts Low risks |
| Network Operations Lead | Owner of the network systems (optical line terminals, edge router, hut servers) and the technical administrator of the hosted voice platform; on-call lead; outage reporting (NORS, DIRS) and 911 outage contacts; CALEA technical contact |
| Field Technicians (2) | Installations, repairs, ONT activation in the element management system; after-hours on-call rotation |
| Customer Service Representatives (2) | Phone and counter support, orders, billing questions, collections |
| Managed service provider (MSP) | Office IT only: endpoints, productivity suite administration, office firewall and Wi-Fi, cloud backup. Does **not** manage the network |
| Network engineering consultant (retainer) | Edge router and BGP configuration, optical line terminal upgrades; remote access through the hut VPN |
| Telecom regulatory consultant | Prepares FCC filings, including the annual CPNI certification package and CALEA filings |
| Independent assessor (contracted) | Performed the P07 control assessment; operates no control |

## 3. Systems
| ID | System | Hosting | Holds CPNI or subscriber PII? | Notes |
|---|---|---|---|---|
| SYS-01 | Billing and customer care system (BSS) with the customer portal: accounts, service orders, invoices with itemized toll call detail, payment tokens, trouble tickets | Vendor SaaS | Yes (CPNI and PII, including driver license numbers) | MFA enforced for staff. Vendor SOC 2 Type 2 report on file, not yet reviewed. Portal password reset uses the account number and last name (gap) |
| SYS-02 | Hosted voice platform (wholesale provider): softswitch, 440 numbers, voicemail, 911 routing and registered locations, call detail records (CDRs) kept 18 months; voice lawful-intercept capability under contract | Wholesale provider SaaS | Yes (CDRs and voice features) | Company admin portal: MFA available but **not enabled**; 4 named logins plus 1 shared "support" login; CDR search and export open to every login |
| SYS-03 | Fiber access network: 2 optical line terminals (OLTs), about 1,420 optical network terminals (ONTs) at customer premises, aggregation switch | On-premises (hut and customer premises) | Indirect (port-to-subscriber mapping) | One shared local administrator account on the OLTs |
| SYS-04 | Network core and management: edge router (BGP to the transit provider, VPN for remote administration) and 2 hut servers running the OLT element management system (EMS), DHCP, DNS, RADIUS, and configuration backups; provisioning link to SYS-01 through an API key | On-premises (hut) | Yes (IP assignments; the API key can read every SYS-01 account) | EMS web page reachable from the internet (gap); edge router firmware 2 years behind (gap) |
| SYS-05 | Network monitoring and alerting service | SaaS | No | Watches device and circuit availability; pages the on-call technician. No security event monitoring |
| SYS-06 | Productivity suite (email, shared drive) | SaaS | Incidental (customer emails, exported reports) | MFA enforced; administered by the MSP |
| SYS-07 | Endpoints: 4 desktops (2 customer service, front counter, Office Manager), 3 laptops (General Manager, Network Operations Lead, Field Technician shared), 3 technician tablets | MSP-managed | Cached | Laptops encrypted; desktops not |
| SYS-08 | Office network: small-business firewall, staff Wi-Fi, guest Wi-Fi in the lobby; office internet rides on the company's own fiber | On-premises, MSP-managed | In transit | |
| SYS-09 | Cloud backup service (MSP-operated) for the productivity suite | SaaS | Incidental | Network device configurations are **not** included; they stay on the hut server (gap) |
| SYS-10 | AI chat assistant in the customer portal (BSS vendor add-on built on a large language model platform) | Vendor SaaS | Yes | Enabled 2026-05-04 for after-hours help; "guest verification" with account number and service address (gap). Assessed in P10 |

Outside the systems list: the CALEA trusted third party (TTP) that handles broadband intercepts (one order served in 2022), the after-hours answering service (takes caller name and callback number; no system access), the payment processor, and the middle-mile and transit providers.

**SSP system (P02):** the *Network Operations and Customer Billing Platform (OSS/BSS)*: SYS-01 to SYS-09, with the interface to SYS-10 (assessed in P10). Lawful intercept is governed by the CALEA SSI plan, outside the SSP boundary.

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite and on staff accounts in the BSS
- MSP patching, antivirus, firewall, and laptop encryption for office IT
- Annual CPNI certification filed each year by March 1 through the regulatory consultant (latest filed 2026-02-24, for calendar year 2025)
- CALEA SSI policies filed in 2017; CALEA TTP contract; voice intercept capability in the hosted voice platform contract
- Hut on a fenced lot with a keyed, alarmed door; batteries and a propane standby generator
- Nightly OLT and router configuration backups to the hut server
- Cloud network monitoring that pages the on-call technician
- An optional phone account PIN offered at sign-up (set on about 30% of voice accounts)
- Billing vendor SOC 2 Type 2 report on file
- Cyber liability insurance with a 24x7 breach hotline and panel vendors

**Missing:**
1. Customer service releases call detail on inbound calls when the representative recognizes the caller or after the caller gives the name and service address. The PIN is optional and set on only about 30% of voice accounts (47 CFR 64.2010(b)).
2. The portal password reset asks for the account number and last name, and the AI assistant's guest verification uses the account number and service address (64.2010(c), (e)).
3. Customers get no notice when a password, online account, or address of record is created or changed (64.2010(f)).
4. No written CPNI procedures, no CPNI training beyond on-the-job coaching, and no disciplinary rule that mentions CPNI (64.2009(b)).
5. The statement filed with the CPNI certification is the consultant's template. It says customers are authenticated with passwords before call detail is released, which is not accurate (64.2009(e)).
6. No CPNI breach procedure. Nobody knows the 7-business-day law enforcement notice or the customer notice hold (64.2011).
7. The CALEA SSI filing (2017) lists a former technician as the 24x7 contact and has never been amended or refiled (47 CFR 1.20003, 1.20005).
8. Network management is weakly protected: one shared administrator login on the OLTs and the EMS; the EMS web page is reachable from the internet; the consultant's VPN login is shared and has no MFA; edge router firmware is 2 years behind vendor security advisories.
9. The hosted voice platform admin portal has no MFA, a shared login, and unrestricted CDR export.
10. No security monitoring or log review. Router and EMS logs are kept about 14 days on the devices.
11. Network configuration backups sit only on the hut server and have never been restore-tested.
12. No incident response plan. Outage handling is informal, 911 outage contacts for the county 911 center were never collected (47 CFR 4.9(h)(1)), and the company has no DIRS procedure (47 CFR 4.18).
13. No inventory of network devices, SaaS services, or where CPNI is stored, and no vendor security reviews.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011, as in force on 2026-09-23 (the 2023 amendments to 64.2011 are not yet effective). Secondary: CALEA SSI rules (47 CFR 1.20000-1.20008) and FCC outage reporting (47 CFR Part 4). Voluntary benchmark for "reasonable measures": a short set of NIST CSF 2.0 outcomes |
| P08 incident | Network intrusion exposing CPNI: exploitation of the internet-exposed EMS web page in the hut, theft of stored credentials, export of CDRs from the hosted voice platform, and reads of customer records through the BSS API key. The MSP, the network engineering consultant, and the insurer's panel are in the notification chain |
| P09 SOC 2 | Security plus Availability. The readiness check is used to answer a vendor security questionnaire from the community bank branch (dedicated circuit customer); also a review of the BSS vendor's SOC 2 Type 2 report |
| P10 AI | Customer-service chat assistant with account access (the registry default), adapted to Micro size: a feature of the BSS vendor's portal rather than a separately bought chatbot. Kept because the company has no after-hours staff and the assistant reads CPNI, which makes it the company's most important AI risk |
| Primary system | Network operations and customer billing (OSS/BSS), the registry default, scaled to a micro carrier: SaaS billing and a wholesale voice platform plus a small on-premises network management stack |
| Cloud | SaaS plus one cloud workload: the MSP-operated cloud backup (SYS-09). Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-31 | Risk assessment and gap analysis (walkthrough of the office and the network hut on 2026-07-22) |
| 2026-08-10 to 2026-08-12 | Control assessment (independent consultant; on site 2026-08-11) |
| 2026-08-25 | AI risk assessment and SOC 2 readiness self-assessment completed |
| 2026-08-31 | Deliverables approved by the Owner and General Manager |

## 7. Facts added while building the deliverables
These facts were added because the deliverables needed them. They do not change sections 1-6.

| Topic | Added fact | Used in |
|---|---|---|
| Shared network password | A Field Technician who left in March 2026 still knew the shared OLT and EMS password. The walkthrough found this on 2026-07-22 and the password was changed on 2026-07-23. Device logs go back only about 14 days, so earlier use cannot be ruled out; no changed configurations were found | P01, P02, P07 |
| EMS exposure | The Network Operations Lead removed internet access to the EMS web page on 2026-08-03. The router firmware upgrade is scheduled for the 2026-09-20 maintenance window | P01, P02, P04, P07 |
| Hut server secrets | The hut server holds a text file of shared network passwords and the BSS API key used by the provisioning link. The key has full administrator rights | P01, P02, P04, P07, P08 |
| Network management protocols | OLT administration uses Telnet and SNMP version 2c. P07 testing found the vendor default read-write SNMP string active on the aggregation switch; removal scheduled 2026-09-15 | P01 (R-024), P02, P07 |
| Hut servers | No malware protection; patched only when the consultant visits; disks not encrypted | P02, P04 |
| Office details | The front counter desktop is excluded from the screen lock so it can show the outage map; tablets use a 4-digit passcode; exported customer reports were found in the general shared-drive folder; the cloud backup console has one MSP administrator account with a password only | P02, P04, P07 |
| Equipment disposal | Returned ONTs and replaced OLT cards are reused or scrapped without a factory reset or disposal record | P02, P06 |
| Voice platform logs | The provider keeps admin portal sign-in and export logs 90 days | P02, P04 |
| Call detail sample | In 10 BSS tickets where customers asked for call detail (reviewed 2026-07-27), 7 releases were made without a PIN | P03, P07 |
| Outage history | The NORS login was set up in 2018 and has never been used. A 2025 middle-mile cut lasted 2 hours 40 minutes and was not assessed against the 667 OC3-minute threshold; counsel is reviewing it | P01, P03 |
| Capacity and power | Middle-mile peak use about 40% of 10 Gbps; OLT ports about 60% used; generator fuel for about 72 hours at full load | P05, P09 |
| Vendor terms | Middle-mile contract: 4-hour repair target. Voice platform contract: 99.99% availability, no CPNI terms. MSP contract: 4-business-hour response, no recovery commitment. Consultant: retainer letter, best effort. TTP: collection within 24 hours of a valid order | P05, P02 |
| Finances and operations | About $92,000 billed a month; cash reserve about 45 days; about 15 installs a month; office phones run on the company's own voice service, with the answering service as fallback | P05 |
| AI assistant | Offered free for six months by the BSS vendor; about 1,150 sessions from 2026-05-04 to 2026-08-14; guest verification used in 210 sessions; guest verification and personalized offers turned off 2026-08-14; chat can change the account email address; transcripts kept 180 days; Spanish chats about 5% of sessions | P01, P03, P10 |
| Driver license numbers | The company stops recording them on 2026-10-01 and purges stored numbers by 2026-11-30 | P01, P06, P08 |
| Bank questionnaire | The community bank branch sent a vendor security questionnaire in July 2026; the response is due 2026-09-30 | P09 |
| Assessor | The P07 assessor is an independent security consultant with telecom experience, not involved in P01 or P03 and operating no control | P07 |
