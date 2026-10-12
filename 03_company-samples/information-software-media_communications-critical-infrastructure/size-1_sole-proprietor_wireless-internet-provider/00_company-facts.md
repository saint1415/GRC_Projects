# Scenario facts: Cris Santos Company | Communications | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, court decision, or Federal Register document, the citation is given. Legal status was checked against eCFR (point in time 2026-09-23) and the Federal Register on 2026-10-05.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-operator files Schedule C) |
| Business | Owner-operated fixed wireless internet service provider (WISP), NAICS 517112. Sells fixed wireless broadband internet access to rural homes, farms, and small businesses. Since 2023-03-01 it also sells a **home phone add-on**: interconnected VoIP service sold and billed under the company's own name and delivered from a wholesale hosted VoIP platform. **No** mobile (CMRS) service, **no** wireline or fiber service, **no** video, **no** submarine cable. In business since 2019 |
| Location | Florida. Home office at the owner's residence. The network core (edge router, core switch, battery backup) sits in a locked equipment shed on the owner's property at the base of a 40-foot tower (**SITE-1**). Three more tower sites: a leased spot on a municipal water tank (**SITE-2**) and two leased farm towers (**SITE-3**, **SITE-4**). Service area: parts of one rural county |
| Workforce | The owner-operator only (0 employees). Contracted help instead of staff (section 2) |
| Customers | About 310 subscriber accounts (285 residential, 25 farm and small business). 52 accounts also buy the home phone add-on (58 VoIP lines). All service addresses are in Florida; about 10% of residential accounts belong to seasonal residents who also have an address in another state |
| Revenue | About $180,000 a year (fictional), about $490 a day: broadband about $164,000, home phone add-on about $15,000, installation fees about $1,000. SBA-small (standard for NAICS 517112: 1,500 employees, 13 CFR 121.201) |
| Regulatory status | Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-COMMUNICATIONS-R01 to R03) from the subscriber and product report, the reseller agreement, and the controller and router records (EV-022, EV-008, EV-009, EV-010). **Broadband internet access service provider** (47 CFR 8.1(b)). After *Ohio Telecom Ass'n v. FCC* (6th Cir. 2025-01-02) set aside the 2024 reclassification order, broadband is an information service, and the FCC conformed its rules effective 2025-08-08 (90 FR 38406). **Provider of interconnected VoIP service** (47 CFR 9.3) for the home phone add-on, which it sells, bills, and supports under its own name. The CPNI rules treat an interconnected VoIP provider as a carrier (47 CFR 64.2003(o)). **CALEA telecommunications carrier** as a facilities-based broadband internet access provider and an interconnected VoIP provider (FCC First Report and Order, 70 FR 59664, 2005-10-13; 47 CFR 1.20002(e)(3)). **Interconnected VoIP provider for outage reporting** (47 CFR 4.3(h)); not a wireline or wireless provider under Part 4 |
| Customer commitments | Online terms of service and privacy policy; home phone add-on terms with a CPNI notice and 911 limitations notice; broadband consumer labels on the website and in the customer portal (47 CFR 8.1(a)) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): SEC disclosure rules (no securities; C-COMMUNICATIONS-R06). Submarine cable rules (C-COMMUNICATIONS-R04). CMRS-only rules, including SIM change authentication (47 CFR 64.2010(h)). Part 4 wireline and wireless outage sections. Emergency Alert System rules (no broadcast or video service). FAR 52.204-25 reporting (no federal contracts). Radio equipment authorization and spectrum rules (not security rules). Payment cards: the payment processor's hosted pages take card and bank details; PCI DSS duties are contractual and outside this sample |
| State law approach | Florida law is cited only where unavoidable (breach notification, Fla. Stat. 501.171). Seasonal residents are handled generically: the law of each state where affected individuals reside |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-operator | Every role: owner, security lead, privacy lead, risk acceptor, incident commander, network engineer, installer, and customer support. Also the **officer who signs the annual CPNI certification** (47 CFR 64.2009(e)) and the **CALEA senior officer** (47 CFR 1.20003(a)); neither role was designated in writing before this project (EV-026) |
| Tower and installation contractor (1099, about 2 days a month) | Tower climbs, radio installs and alignment. Signs in to the cloud radio controller with a **shared "installer" account** (EV-009). No written confidentiality or security terms (EV-017) |
| On-call network consultant (another WISP's engineer, hourly) | Router and outage help on request, through a VPN into the core router. Uses the owner's router admin account (EV-010, EV-019). Signed confidentiality and security terms on 2026-07-17 (EV-017) |
| Bookkeeper (contract) | Accounting SaaS with its own login (EV-016); receives monthly billing summary reports |
| Telecommunications regulatory counsel (hourly, as needed) | CPNI certification, CALEA filing, and breach advice. No retainer |
| Wholesale VoIP platform provider | Runs call switching, 911 call routing, number porting, call detail records (CDRs), and voicemail for the home phone lines; supports lawful intercept of the VoIP lines under its contract (EV-008) |
| Upstream fiber provider | One internet transit circuit at SITE-1 (no second upstream; EV-017) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds CPNI or subscriber PII? | Notes |
|---|---|---|---|---|
| SYS-01 | Subscriber billing and management platform: accounts, plans, invoices, autopay through the payment processor, customer portal, support tickets, text-message support line | Vendor SaaS | Yes (subscriber PII; home phone invoices list toll calls, which is CPNI) | System of record. The vendor has a SOC 2 Type 2 report (EV-021; reviewed in P09). Owner admin account uses MFA (EV-001) |
| SYS-02 | VoIP reseller portal of the wholesale VoIP platform: line provisioning, CDRs, call forwarding and voicemail settings, 911 registered addresses, porting | Vendor SaaS | Yes (call detail and service features for all 58 lines) | **MFA offered but not turned on** (EV-006). Password saved in the laptop browser (EV-013). The owner downloads a monthly CDR export to bill toll calls |
| SYS-03 | Business email and file storage (business plan) | SaaS | Incidental (customer emails, sign-up forms, CDR exports) | MFA on (EV-015) |
| SYS-04 | Cloud radio controller (the radio vendor's cloud management service) for access points, backhaul links, and customer radios | Vendor SaaS | Indirect (customer radio, service location, signal data) | Owner account uses MFA; contractor uses the shared installer account (EV-009) |
| SYS-05 | Owner-operated network: edge router and core switch at SITE-1, carrier-grade NAT, DHCP and DNS, access points and backhaul radios at 4 sites, about 310 customer radios, and analog telephone adapters (ATAs) at 52 home phone accounts | Owner-operated equipment | Yes in transit (subscriber traffic; VoIP signaling, which carries call detail); NAT logs map IP addresses to subscribers | **Router management (web and SSH) enabled on every interface, including the internet-facing one** (EV-010; confirmed by the P07 port check, EV-SC-7); firmware two releases behind (EV-011); router logs kept in memory only (EV-010) |
| SYS-06 | Owner laptop and phone | Owner devices | Yes (CDR exports, customer lists, saved passwords, MFA app) | Laptop full-disk encryption on (EV-013); phone holds the MFA app (EV-014) |
| SYS-07 | Accounting SaaS | SaaS | No CPNI (customer names on receivables reports) | Bookkeeper has a named login (EV-016) |
| SYS-08 | AI support assistant: the billing platform's add-on on the customer portal chat and the text-message support line, with read access to the customer's account | Vendor SaaS (large language model service) | Yes (account data; for home phone customers, recent call history) | Turned on 2026-05-04 (EV-004); see P10 |

**SSP system (P02):** the *ISP Operations Systems Profile*: SYS-01 to SYS-08, the owner's SaaS stack plus the owner's devices and the management plane of the owner-operated network.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person ISP the sources are the vendors' admin portals (billing platform, VoIP reseller portal, cloud radio controller, email, accounting), the router and switch configuration, the laptop and phone, bank and card statements, tax files, the signed agreements folder, the vendor trust portal, the company website, the insurance agent's portal, and a walk-through of SITE-1 and the home office.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against the FCC CPNI rules, the CALEA system security and integrity rules and the outage rules for interconnected VoIP** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system (P02) | The registry default, "core business SaaS stack (email, files, client and billing records)", is kept and **extended to the management plane of the owner's network**, because for a WISP the network is the service and the most likely path to CPNI |
| P03 regulation | FCC CPNI rules, 47 CFR 64.2001-64.2011, as in force on 2026-09-23. They reach this business **only through the home phone add-on**. Secondary: CALEA system security and integrity rules (47 CFR 1.20000-1.20008) and outage rules for interconnected VoIP (47 CFR 4.9(g), (h); 4.18). Voluntary network security benchmark: 8 NIST CSF 2.0 outcomes |
| P08 incident | Network intrusion exposing CPNI (registry default): an attacker takes over the internet-exposed edge router, captures home phone signaling, and uses a password taken from the owner's laptop to export call detail from the VoIP reseller portal |
| P09 SOC 2 | The business is not a service organization for other businesses. Security criteria (CC1-CC9) self-check plus a review of the billing platform vendor's SOC 2 Type 2 report |
| P10 AI | Registry default adapted: the "customer-service chatbot with account access" is the billing platform's AI support assistant add-on, the one third-party AI tool the owner uses with customer data. A stand-alone chatbot would not fit a business of this size |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Intake: the owner collects vendor portal exports and settings, the router and switch configuration, device settings, statements, tax files, agreements, website captures, the vendor's SOC 2 report and the SITE-1 and home office walk-through; inventories; obligations register |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call network consultant (after the consultant signed confidentiality and security terms on 2026-07-17): BIA, risk register, gap analysis, cloud mapping and control assessment. Site walkthrough of SITE-1 and SITE-3 on 2026-07-21; AI support assistant tested 2026-07-22; control tests 2026-07-23; counsel's review 2026-07-24 |
| 2026-07-27 to 2026-08-28 | POL-01 drafted from the gaps and the test results |
| 2026-08-12 | Wholesale VoIP provider answers the security questionnaire (P09) |
| 2026-08-14 to 2026-08-20 | AI support assistant transcript and prompt tests (2026-08-14) and AI use assessment (P10) |
| 2026-08-31 | Deliverables and POL-01 adopted by the owner-operator (POL-01 effective 2026-09-01) |
| 2027-02 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| AI assistant test | On 2026-07-22 the owner texted the support line from a phone that was not the number of record, gave a test account's number and service ZIP code, and received that account's last 5 home phone calls. The owner turned off the call history skill on the text line the same day. A review of text-line sessions from 2026-05-04 to 2026-07-22 found 14 sessions that showed call history; the owner called each account holder back at the number of record, all 14 confirmed they made the request, and no breach was determined (logged in the incident log) (EV-032, EV-033) | P01, P03, P10 |
| Default credentials | During P07 testing on 2026-07-23 the consultant found that one access point at SITE-3 (installed by the contractor in 2026-06) still had the vendor-default local password and SNMP community string. Changed the same day (EV-IA-5) | P01, P07 |
| Router exposure | An external port check on 2026-07-23 confirmed the edge router's web and SSH management answered from the internet. The owner blocked management from the internet the same day. Management still answers from the subscriber-facing interfaces (about 310 customer networks), and the firmware update and filter rework wait for a maintenance window on 2026-09-15 (EV-SC-7) | P01, P07, P08 |
| VoIP signaling | The ATAs send call signaling and audio unencrypted to the wholesale platform. The platform supports encrypted signaling and media, which the owner has not turned on (EV-007) | P02, P08 |
| Vendor assurance | The billing platform vendor provided its SOC 2 Type 2 report (Security and Availability). The owner reviewed it on 2026-07-23. The wholesale VoIP provider has no SOC 2 report; it answered a security questionnaire on 2026-08-12 (EV-021, EV-035) | P09 |
| Cyber insurance | No cyber insurance. The owner's general liability policy has no cyber coverage (EV-018, EV-027) | P01, P08 |
| Power | SITE-1 batteries carry the core for about 2 hours; the generator is started by hand. Access points at SITE-2 to SITE-4 have about 4 hours of battery (EV-012, EV-029) | P05, P01 |
| Network inventory | 32 access points across the 4 sites. A spare edge router is kept in the SITE-1 shed. The core switch runs firmware about 3 years old (EV-009, EV-011, EV-012) | P05, P07 |
| Credentials history | The shared access point password and the radio controller installer login have not changed since 2021, although a former installer stopped working for the company in 2024 (EV-009, EV-019, EV-IA-5) | P01, P07 |
| Restore test | On 2026-07-23 loading the last saved configuration onto the spare router failed on the first attempt because the switch configuration had not been saved with it (EV-CP-9) | P05, P07 |
| Counsel review | Counsel agreed on 2026-07-24 that the company provides interconnected VoIP service for CPNI purposes, and searched the FCC's CPNI certification docket (EB Docket No. 06-36) and CEFS: no filings by the company were found (EV-034) | P03 |
| AI assistant use | About 620 sessions from 2026-05-04 to 2026-08-14 (380 portal chat, 240 text line). The add-on terms say customer data is not used for model training and the model provider keeps transcripts 30 days; written confirmation requested. The add-on was launched after the period of the billing vendor's SOC 2 report, which ends 2026-04-30 (EV-036, EV-005, EV-021) | P09, P10 |
| Billing vendor terms | Customer incident notice within 72 hours under the service terms (EV-020) | P08, P09 |
| Second AI tool | The owner uses a paid individual plan of a general-purpose AI chat service to draft customer notices and configuration snippets (AI-002), with no customer data (EV-028) | P10 |
