# Scenario facts: Cris Santos Company | Utilities | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner, a licensed professional engineer, files Schedule C) |
| Business | Independent utility engineering consultant (NAICS 541330 Engineering Services). Protection and control engineering (relay settings and coordination studies), field support for relay commissioning and event analysis, and distribution planning and interconnection studies for small electric utilities |
| Why not a utility | A sole proprietor cannot operate an electric distribution utility (NAICS 221122, the vertical's primary industry). The business serves utilities instead, so the utility rules reach it only through client contracts (flow-down). P03 confirms this |
| Location | Florida. Home office in the owner's residence; site visits to client substations |
| Workforce | The owner-engineer only (0 employees). Uses one part-time drafting subcontractor and hourly outside help instead of staff |
| Revenue | About $180,000 a year (fictional), about $3,500 a week. SBA-small (standard $25.5 million, NAICS 541330; 13 CFR 121.201) |
| Clients | 4 active utility clients (section 5 lists the security terms each one passes down). Client A about 40% of receipts, Client B 25%, Client C 15%, Client D 15%, other small jobs 5% |
| NERC status | **Not on the NERC Compliance Registry** and performs no registered function. The NERC CIP standards apply to the "Responsible Entities" listed in each standard's Applicability section 4.1 (Balancing Authority, qualifying Distribution Provider, Generator Operator, Generator Owner, Reliability Coordinator, Transmission Operator, Transmission Owner). The clients are the Responsible Entities; the consultant is their vendor |
| CEII | Holds Critical Energy/Electric Infrastructure Information (CEII) obtained from FERC for the Client D study under a signed non-disclosure agreement (18 CFR 388.113(g)(5) and (h)(2)) |
| Personal information | Very little. A W-9 form (name and Social Security number) for the drafting subcontractor, and the owner's own records. Client data sets contain no customer names. This makes the business a Florida "covered entity" in a narrow way (Fla. Stat. 501.171(1)(b)) |
| Not in scope | Payment cards (clients pay by bank transfer and check); federal contracts or subcontracts (none, so no FAR clauses); TSA pipeline directives, NRC 10 CFR 73.54, and SDWA section 1433 (no pipeline, reactor, or water work) |
| State law approach | Florida law is cited only where unavoidable (breach notice, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-engineer | Every role: owner, the only engineer, security and compliance lead, incident commander, and risk acceptor. Signs and seals all engineering work |
| CAD drafting subcontractor | Part-time (about 10 hours a week, paid on a 1099) since 2025-03-01. Updates one-line and wiring drawings from the owner's markups. Works from the subcontractor's own computer. General subcontract with a confidentiality clause; **no access agreement covering client security information** |
| On-call IT technician | Hourly help with the laptop, phone, and home network. No standing access; no access to client folders. Signed a non-disclosure agreement on 2026-07-17, before the self-assessment |
| Tax accountant | Read-only access to the accounting SaaS for year-end work |
| Insurer | Professional liability (errors and omissions) policy with a cyber endorsement (sublimit $100,000) and a breach response hotline |
| Client security contacts | Client A security and NERC compliance contact; Client B system operations desk and compliance contact; Client C and Client D project managers |

## 3. Systems
| ID | System | Hosting | Holds client security information? | Notes |
|---|---|---|---|---|
| SYS-01 | Business email, calendar, and file storage suite (business plan) | SaaS | Yes: correspondence, project folders, some copies of Client A BCSI | MFA by SMS text code. A shared "Projects" folder was shared with the drafting subcontractor. File version history kept 30 days |
| SYS-02 | Engineering laptop | Owner device | Yes: settings files, studies, the encrypted CEII archive | Full-disk encryption on since 2025-01 (Client A requirement). Built-in antivirus and automatic OS updates. Runs relay manufacturers' settings software and power system analysis software. **Used for email, web, and client relay connections alike, under an administrator account** |
| SYS-03 | Mobile phone | Personal device | Yes: photos of client control houses and relay panels | Passcode and device encryption. Receives SMS codes. Camera roll syncs to a personal consumer photo cloud |
| SYS-04 | Accounting and invoicing SaaS | SaaS | No (client billing records, bank feed) | **Password only, no MFA.** Tax accountant has read-only access |
| SYS-05 | Removable media: 3 USB flash drives | Owner devices | Yes: relay settings files carried to sites | Mixed use (also personal files). Scanned only at Client B's kiosk |
| SYS-06 | Client-operated access: Client A secure file portal account; Client B remote access gateway account | Client-hosted | Yes (the clients' systems) | Named accounts. Client A enforces MFA. Client B enables each vendor session on request and uses an MFA push to the phone. The client systems are outside the boundary; the owner's credentials and devices are inside |
| SYS-07 | Home office network | ISP router and Wi-Fi | In transit | Shared with household devices. Router admin password never changed from the default |
| SYS-08 | AI tools: a third-party load-forecasting SaaS (trial) and a consumer general-purpose AI chatbot | SaaS | Yes: Client C feeder load data (forecasting tool); project details pasted into the chatbot | See P10. Neither tool was reviewed before use |

**SSP system (P02):** the *Core Business Systems (CBS)*: SYS-01 to SYS-08 (the owner's SaaS stack, laptop, phone, removable media, home network, and the owner's accounts on the client-operated systems in SYS-06).

## 4. Current security posture: early (few formal controls)
**In place today:**
- Full-disk encryption on the laptop (since 2025-01) and device encryption with a passcode on the phone
- MFA on the email and file suite (SMS codes); client-enforced MFA on the Client A portal and the Client B gateway
- Automatic OS updates and built-in antivirus on the laptop
- Client B's pre-connection laptop checklist completed at each substation visit (2026-03-18 and 2026-06-09) and USB drives scanned at Client B's kiosk
- Client B remote access only through Client B's gateway, enabled per session (5 sessions in 2026)
- Client A's annual security awareness and BCSI handling module completed 2025-10-20; Client A's BCSI access verification answered 2025-11-12
- CEII kept in an encrypted archive on the laptop; used only for the Client D study
- File version history (30 days) in the business file suite
- Cross-cut shredder for paper in the home office
- Professional liability policy with a cyber endorsement and breach hotline

**Missing:**
1. No risk assessment, written policies, or incident plan had ever been prepared.
2. The drafting subcontractor had access since 2025-03-03 to the shared "Projects" folder, which held Client A BCSI (relay settings files and a communications network drawing for two 230 kV substations). Client A never authorized that access. Found 2026-07-21; access removed the same day; Client A notified 2026-07-22.
3. One laptop is used for email, web browsing, and connecting to client relays, and the owner works in an administrator account every day.
4. The accounting SaaS has no MFA; email MFA uses SMS codes; passwords are saved in the browser; there is no password manager.
5. The home Wi-Fi is shared with household devices, and the router admin password is the default.
6. Photos of client control houses and relay panels (BCSI under Client A's program) sit in the phone's camera roll and sync to a personal consumer photo cloud.
7. USB drives that carry relay settings files are mixed-use and are scanned only at Client B's kiosk.
8. Local settings databases and engineering software license files on the laptop have no backup; no restore has ever been tested.
9. No register of what client information the business holds, where, and when it must be returned or destroyed. Two Client A projects that ended in 2025 were never certified as returned or destroyed.
10. No security training beyond Client A's annual module.
11. Client C feeder load data was uploaded to a third-party AI load-forecasting SaaS without Client C's consent, and project details were pasted into a consumer AI chatbot.
12. No vendor list, no review of SaaS terms, and no access agreement with the drafting subcontractor.
13. No written procedure for the 24-hour incident notices that Client A and Client B require.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | NERC CIP is the primary regulation, but it reaches the business **only by contract**. The rows decompose the CIP requirements each client passes down: Client A (medium impact Responsible Entity) through its Supplier Security Addendum, labeled **SSA-A (1) to (8)**; Client B (low impact Responsible Entity) through its Vendor Access Agreement, labeled **VAA-B (1) to (5)**. The binding non-CIP duties are added: the FERC CEII non-disclosure agreement (18 CFR 388.113(h)(2)) and Fla. Stat. 501.171 (narrow) |
| Client A terms | Client A is a generation and transmission cooperative registered as a Transmission Owner and Transmission Operator, among other functions, with medium impact BES Cyber Systems at some 230 kV substations. The consultant prepares relay settings and coordination studies. Client A's technicians load all settings; the consultant attends commissioning escorted and never connects to Client A equipment. SSA-A, signed 2025-01-15: (1) handle BCSI under Client A's information protection program: store it only in the Client A portal or in encrypted storage under the consultant's sole control, transfer it only through the portal, and never in a personal or consumer account; (2) only individuals Client A has authorized by name may access BCSI; (3) answer Client A's access verification at least every 15 calendar months; (4) tell Client A within 24 hours when an authorized individual no longer needs access; (5) notify Client A within 24 hours of discovering a cyber security incident affecting Client A information or services, and cooperate in the response; (6) disclose known vulnerabilities in the consultant's tools or deliverables that could affect Client A; (7) return or destroy BCSI within 30 days after a project ends, with written certification; (8) complete Client A's security awareness and BCSI handling module each year, use MFA on any account and full-disk encryption on any device that holds Client A information |
| Client B terms | Client B is a municipal electric utility registered as a Distribution Provider with low impact BES Cyber Systems (115 kV protection relays at two substations). The consultant supports relay commissioning and retrieves relay event records. VAA-B, signed 2026-03-02: (1) before connecting a laptop to a Client B relay, show its antivirus update level and patch status on Client B's checklist and run any extra scan Client B asks for; (2) scan every USB drive at Client B's kiosk before use; (3) remote access only through Client B's gateway with a named account and MFA, enabled by Client B for each session, from a device used only for business; (4) never store or share the gateway credentials, and report a suspected compromise immediately; (5) notify Client B within 24 hours of any incident that may affect Client B systems or information |
| Client C | Small municipal distribution utility, not subject to NERC CIP. Ten-year distribution planning study. Provided 3 years of hourly feeder load data for 24 feeders and annual customer counts by class (no customer names). Contract: confidentiality clause; no sharing of Client C data with third parties without written consent |
| Client D | Engineering firm (prime contractor) that subcontracts the consultant for an interconnection study of a solar facility. The consultant obtained transmission planning models designated as CEII from FERC: request granted 2026-02-10 with a signed non-disclosure agreement; the requester verification is valid for calendar year 2026 (18 CFR 388.113(g)(5)(v)) |
| P08 incident | Registry default "Intrusion into distribution control systems (OT)", adapted: the business runs no OT, so the incident is a **suspected intrusion into a client's distribution control systems through the consultant's access**. The owner's email credentials are phished, an attacker finds the Client B gateway user name, and the owner's phone receives an MFA push for a Client B session the owner did not start |
| P09 SOC 2 | Security criteria only. The consultant is not a service organization that would obtain a SOC 2 report; Client A sends an annual security questionnaire instead. Part A is the owner's self-check; Part B is a review of the email and file suite provider's SOC 2 Type 2 report |
| P10 AI | Registry default "Electric load-forecasting model", adapted: a **third-party AI load-forecasting SaaS** the owner trialed for the Client C planning study (AI-001). The consumer AI chatbot is AI-002 |
| Cloud | SaaS only. No IaaS. Primary system name kept close to the registry default ("Core business SaaS stack"), with the laptop, phone, and media added because they carry client data |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT technician (under NDA since 2026-07-17). SaaS mapping 2026-07-22; tests 2026-07-23 |
| 2026-07-21 | Drafting subcontractor's folder access found and removed |
| 2026-07-22 | Client A notified (phone and email) under SSA-A (5) |
| 2026-07-29 | Drafting subcontractor's signed statement that no Client A copies were kept, sent to Client A |
| 2026-08-31 | Deliverables adopted by the owner-engineer |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Open share link | During the SaaS mapping (2026-07-22) the owner found an "anyone with the link" share on a Client B settings folder, created 2026-03-18 so a Client B technician could download files. It was turned off on 2026-07-23 during P07 testing | P04, P07, P01 |
| Drafter's file activity | The file suite's activity log showed the drafting subcontractor opened 6 files in the Client A subfolder between 2025-04 and 2026-06 (drawings for project A-2026-02) | P01, P03, P07 |
| AI trial dates | Load-forecasting SaaS trial 2026-06-01 to 2026-07-15 (Client C data uploaded 2026-06-03); paused 2026-07-20. Consumer chatbot used 2026-04 to 2026-07; stopped 2026-07-24 | P01, P10 |
| Email provider assurance | The email and file suite provider publishes a SOC 2 Type 2 report to business customers through its trust portal. The owner reviewed it on 2026-07-23 | P02, P09 |
| Backup engineer | No arrangement with another engineer exists. Any arrangement must respect Client A's named-authorization rule (SSA-A (2)), so a backup engineer can work on Client A files only after Client A authorizes that person | P05, P01 |
| BCSI copies in email | Client A staff emailed some drawings and settings files as attachments in 2025, before transfers moved fully to the Client A portal. Those copies were still in the mailbox when the self-assessment started. All deliverables from the owner went through the portal | P03, P08, P09 |
| Client B link share notice | The owner reported the open "anyone with the link" share on the Client B settings folder to Client B's compliance contact on 2026-07-23, the day it was turned off | P03, P07 |
| W-9 location | The drafter's W-9 is stored in the accounting SaaS; a copy is also in the drafter's 2025-03 email to the owner | P03, P08 |
| USB drives and CEII | The USB drives hold no Client A files (checked 2026-07-23). CEII was never in email, the file suite, or an AI tool (checked 2026-07-22) | P03 |
| Client A access verification | The 2025-11-12 answer listed only the owner while the drafter's share was open; the corrected list went with the 2026-07-22 notice. Next answer due by 2027-02-12 (15 calendar months) | P03, P06 |
| Chatbot notes | The chatbot notes named Client A substations. The owner deleted the chat history on 2026-07-24 and told Client A the same day under SSA-A (5) | P03, P10 |
| AI forecast outputs | No forecast from the AI forecasting SaaS was used in any deliverable; the Client C study draft had not started when the trial was paused | P10 |
| Email suite SOC 2 details | Type 2, unqualified, Security, Availability, and Confidentiality, 12 months ending 2026-03-31; one exception (remediated); SMS code delivery by telecommunications carriers carved out; bridge letter requested 2026-07-23 | P09 |
| P08 scenario detail | In the P08 scenario the attacker reaches the Client B gateway prompt because the gateway password was one of the two reused passwords found in P07 (IA-05c.) | P08 |
