# Scenario facts: Cris Santos Company | Dams | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company, its clients, and their dams are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or a FERC program document, the citation is given. Regulatory text was checked against eCFR (version date 2026-09-23) and the FERC Security Program for Hydropower Projects, Revision 3A, as published on ferc.gov.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner, a licensed professional engineer, files Schedule C) |
| Business | Independent dam safety engineering consultant (NAICS 541330 Engineering Services). Dam safety inspections and assessments for owners of hydropower dams, review of dam safety instrumentation data, spillway gate reliability reviews, and participation in potential failure mode analyses |
| Why not a dam operator | A sole proprietor cannot operate a hydroelectric dam (NAICS 221111, the vertical's primary industry). The business serves dam owners instead, so the dam security rules reach it only through client contracts and through the FERC rules on Critical Energy/Electric Infrastructure Information (CEII). P03 confirms this |
| Owner's qualifications | Licensed professional engineer with 24 years of experience in dam design, construction, and safety investigations. Never an employee or agent of any current client. Meets the "independent consultant" definition in 18 CFR 12.31(a) |
| Location | Florida. Home office in the owner's residence; field work at client dams in the Southeast |
| Workforce | The owner-engineer only (0 employees). Uses one field assistant on a per-inspection basis and hourly outside IT help instead of staff |
| Revenue | About $180,000 a year (fictional), about $3,500 a week. SBA-small (standard $25.5 million, NAICS 541330; 13 CFR 121.201) |
| Clients | 3 active clients (section 5 gives the security terms each one passes down). Client A about 45% of receipts, Client B 30%, Client C 10%, other small jobs 15% |
| Client A | A FERC licensee whose hydroelectric project has a **high hazard potential** dam in **Security Group 2** under the FERC Security Program. Two units of about 14 MVA each, connected at 69 kV, so the project is not part of the Bulk Electric System (NERC inclusion I2 needs 100 kV or above and more than 20 MVA per unit or more than 75 MVA per plant). Gate and unit control is remote-capable, so Section 9 of the Security Program applies to Client A. The owner is Client A's approved independent consultant (a one-person team) for its next Part 12D periodic inspection (18 CFR 12.32 to 12.36) |
| Client B | A FERC licensee with a small project whose dam is in **Security Group 3**. The owner is doing a spillway gate reliability and instrumentation review study. Client B gives the owner a read-only account on its instrumentation data platform (vendor SaaS) |
| Client C | A private homeowners' association that owns a small lake dam not under FERC jurisdiction. Annual visual inspection and short report. Contract only |
| NERC status | Not on the NERC Compliance Registry and performs no registered function. Neither Client A's nor Client B's project is a BES generating resource, so NERC CIP is not part of any client contract |
| CEII | Holds two kinds of CEII: (1) Client A's own CEII obtained from FERC as Client A's non-employee agent with Client A's written authorization (18 CFR 388.113(g)(1)); (2) CEII about an upstream project owned by a different licensee, obtained from FERC for the Client B study under a signed non-disclosure agreement (18 CFR 388.113(g)(5) and (h)(2)) |
| Security-sensitive material | Client A documents marked "Privileged - Security Sensitive Material" (Security Program Rev. 3A, 3.4.3.4 and 8.0): parts of its Security Plan, its Form 3 answers, and its Security Checklist results. Rev. 3A 7.3 says no outside agency or non-owner may request or keep hard copies of a site Security Plan |
| Personal information | Very little: the field assistant's W-9 (name and Social Security number) and the owner's own records. Client data holds no customer names. This makes the business a Florida "covered entity" in a narrow way (Fla. Stat. 501.171(1)(b)) |
| Not in scope | Federal contracts or subcontracts (none, so no FAR clauses); NERC CIP (no registered client function in scope); payment cards (clients pay by bank transfer and check); HIPAA (no health data) |
| State law approach | Florida law is cited only where unavoidable (breach notice for the W-9, Fla. Stat. 501.171). The samples otherwise stay federal |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-engineer | Every role: owner, the only engineer, independent consultant of record, security and compliance lead, incident commander, and risk acceptor. Signs and seals every report |
| Field assistant | A retired dam safety technician paid on a 1099 for about 8 field days a year. Accompanies the owner into galleries, adits, and gate structures as a safety partner, carries equipment, and holds the survey rod. Not a member of the independent consultant team and makes no evaluations. **No written agreement**; used a personal phone to take photos at the 2026-04-21 Client B inspection |
| On-call IT technician | Hourly help with the laptop, phone, and home network. No standing access and no access to client folders. Signed a non-disclosure agreement on 2026-07-14, before the self-assessment |
| Tax accountant | Read-only access to the accounting SaaS for year-end work |
| Insurer | Professional liability (errors and omissions) policy. **It excludes data breach and cyber costs; there is no cyber policy** |
| Client security contacts | Client A Compliance and Security Coordinator (its FERC primary security contact) and OT on-call line; Client B Chief Dam Safety Engineer; Client C board president |

## 3. Systems
| ID | System | Hosting | Holds client security information? | Notes |
|---|---|---|---|---|
| SYS-01 | Business email, calendar, and file storage suite (business plan) | SaaS | Yes: correspondence, project folders, working copies of Client B data | MFA with an authenticator app. File version history 30 days. Includes a built-in AI writing assistant (AI-002, P10) |
| SYS-02 | Engineering laptop | Owner device | Yes: analyses, drafts, the encrypted CEII archive, field photos copied from the phone | Full-disk encryption on since 2025-02. Built-in antivirus and automatic OS updates. Runs seepage, slope stability, hydraulic, and CAD software. Holds the owner's digital signing certificate used to seal reports. **Used for email, web, client portals, and the Client A gateway alike, under an administrator account; the browser saves passwords** |
| SYS-03 | Mobile phone | Personal device | Yes: field photos of spillways, gate hoist controls, galleries, and security features | Passcode and device encryption. Authenticator app and client MFA prompts. **Camera roll syncs to a personal consumer photo cloud** |
| SYS-04 | Field tablet | Owner device | Yes: inspection checklists and photos | Passcode and device encryption. Offline inspection-form app that syncs to SYS-01 |
| SYS-05 | Accounting and invoicing SaaS | SaaS | No (client billing records, bank feed, the W-9 copy) | **Password only, no MFA.** Tax accountant has read-only access |
| SYS-06 | Client-operated access: Client A secure document portal; Client A vendor remote access gateway; Client B instrumentation data platform account | Client-hosted or client's vendor SaaS | Yes (the clients' systems) | Named accounts. Client A enforces MFA on its portal and gateway; the gateway gives **view-only** access to HMI screens and historian trends for the spillway gates and units, enabled by Client A for set review windows. Client B's platform offers MFA, but **it is not turned on** for the owner's account. The client systems are outside the boundary; the owner's credentials and devices are inside |
| SYS-07 | Home office network | ISP router and Wi-Fi | In transit | Shared with household devices and a smart TV. Router updates automatically |
| SYS-08 | AI tools: a third-party AI anomaly detection SaaS for dam instrumentation data (trial) and the suite's built-in AI writing assistant | SaaS | Yes: Client B instrument readings (anomaly detection trial) | See P10. Neither tool was reviewed before use |
| Media | One external USB drive for a monthly laptop backup | Owner device | Yes: copies of all project files, including CEII | **Not encrypted; never restore-tested** |
| Paper | Field notebooks, printed drawings for field use, a locked file cabinet, a cross-cut shredder | Home office | Yes | Printed drawings from a former client's 2025 project are still in the cabinet |

**SSP system (P02):** the *Core Business SaaS Stack (CBSS)*: SYS-01 to SYS-08, the USB backup drive, and paper records in the home office, including the owner's own credentials and devices used to reach the client-operated systems in SYS-06 (those client systems themselves are outside the boundary).

## 4. Current security posture: early (few formal controls)
**In place today:**
- Full-disk encryption on the laptop (since 2025-02); device encryption with a passcode on the phone and tablet
- MFA with an authenticator app on the email and file suite; client-enforced MFA on the Client A portal and gateway
- Automatic OS updates and built-in antivirus on the laptop
- Client A's security awareness module completed 2026-06-05, before portal and gateway access was granted
- Client A gateway sessions enabled by Client A for each review window (3 sessions before the self-assessment: 2026-07-07, 2026-07-09, 2026-07-14), view-only
- The upstream project's CEII (Client B study) kept in an encrypted archive on the laptop and used only for that study
- File version history (30 days) in the business suite
- Locked file cabinet and a cross-cut shredder in the home office
- Professional liability insurance (no cyber cover)

**Missing:**
1. No risk assessment, written policies, or incident plan had ever been prepared.
2. In June 2026 the owner downloaded two Client A security-sensitive documents (the Information Technology/SCADA section of its Security Plan and its Form 3 answers) from the Client A portal to the laptop for offline review. The copies synced to the business file suite. This conflicts with Rev. 3A 7.3 and Client A's agreement. Found 2026-07-21; deleted the same day; Client A told on 2026-07-22.
3. One laptop is used for email, web browsing, client portals, and the Client A gateway, and the owner works in an administrator account every day. The browser saves passwords, including the gateway password.
4. The accounting SaaS and the Client B instrumentation platform account have no MFA; there is no password manager.
5. Field photos of gate controls, galleries, and security cameras sync from the phone to a personal consumer photo cloud. The field assistant took photos at the Client B inspection on a personal phone with no agreement.
6. The monthly backup goes to an unencrypted USB drive that holds CEII and client files; no restore has ever been tested.
7. No register of client information (CEII and security-sensitive material) showing where it is and when it must be returned or destroyed. Printed drawings from a former client's 2025 project were never returned or certified destroyed.
8. The home Wi-Fi is shared with household devices, and Client A gateway sessions run over it.
9. Client B instrument readings were uploaded to a third-party AI anomaly detection SaaS without Client B's consent.
10. No vendor list, no review of SaaS terms, and no agreement with the field assistant.
11. No written procedure for the 24-hour notices Client A and Client B require, or for reporting an unauthorized CEII disclosure to FERC.
12. No security training beyond Client A's module.
13. No cyber insurance.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | The FERC Security Program for Hydropower Projects (Rev. 3A) is the primary regulation, but it binds licensees, not their consultants. It reaches the business **only through Client A's contract**, labeled **CSCA-A (1) to (9)**. Binding non-contract duties are added: the CEII rules (18 CFR 388.113(g)(1) agent authorization and the (h)(2) non-disclosure agreement), the 18 CFR Part 12 Subpart D independent consultant rules that govern the Client A inspection report, Client B's agreement terms (GRS-B), and Fla. Stat. 501.171 (narrow). 18 CFR 12.10 and NERC CIP are recorded as not applicable directly |
| Client A terms | Consultant Security and Confidentiality Agreement (CSCA-A), signed 2026-06-01: (1) handle any Client A security-sensitive material and CEII only in the Client A portal or in encrypted storage under the consultant's sole control, mark derived notes "Privileged - Security Sensitive Material", and never use a personal or consumer account; (2) review the Security Plan and Form 3 answers only on site or in the portal, never download, print, or keep copies; (3) use the Client A vendor remote access gateway only, with the named account and MFA, only during windows Client A enables, view-only, from a device used only for business; (4) keep a log of each gateway session (date, time, purpose) and answer Client A's weekly session review; (5) complete Client A's security awareness module before access and every year; (6) never connect removable media to Client A equipment; (7) report any suspected security incident affecting Client A information, accounts, or systems to Client A's security contact within 24 hours, and any suspicious activity seen at the site at once; (8) return or destroy Client A material within 30 days after the engagement ends, with written certification; (9) no other person may see Client A material or enter restricted areas without Client A's written approval; photos of security features only with escort approval, stored as security-sensitive material |
| Client B terms | Gate Reliability Study Agreement (GRS-B), signed 2026-02-16: (1) confidentiality, no sharing of Client B data with any third party without written consent; (2) use MFA wherever Client B systems offer it; (3) notify Client B within 24 hours of any incident that may affect Client B information or accounts |
| CEII | Client A: written authorization for the owner to request Client A's CEII from FERC as its agent, dated 2026-06-03; FERC released prior Part 12D reports and the Supporting Technical Information Document on 2026-06-24. Upstream project (Client B study): request with a signed non-disclosure agreement granted 2026-03-10; the requester verification is valid for the rest of calendar year 2026 (388.113(g)(5)(v)) |
| P08 incident | Registry default "Unauthorized access to spillway and turbine control systems", adapted: the business runs no control systems, so the incident is **unauthorized access to Client A's spillway and turbine control systems (view-only HMI and historian) through the consultant's gateway account**, using a session token stolen from the laptop browser by information-stealing malware |
| P09 SOC 2 | Security criteria only. The consultant is not a service organization that would obtain a SOC 2 report; clients send security questionnaires instead. Part A is the owner's self-check; Part B reviews the email and file suite provider's SOC 2 Type 2 report |
| P10 AI | Registry default "Dam-safety sensor anomaly detection", kept but adapted to the consultant's view: a **third-party AI anomaly detection SaaS** the owner trialed on Client B instrument readings (AI-001). The suite's built-in AI writing assistant is AI-002 |
| Cloud | SaaS only. No IaaS. The primary system keeps the registry default name ("Core business SaaS stack") and adds the laptop, phone, tablet, and media because they carry client data |

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2026-02-16 | GRS-B signed with Client B |
| 2026-03-10 | FERC grants the upstream project CEII request under a non-disclosure agreement |
| 2026-04-21 | Client B field inspection (owner and field assistant) |
| 2026-04-30 | Client A submits its Part 12D inspection plan naming the owner as its independent consultant (more than 180 days before the field inspection, 18 CFR 12.34(b)) |
| 2026-05-19 | Client B instrument readings uploaded to the AI anomaly detection SaaS trial (AI-001), without Client B's consent |
| 2026-06-01 | CSCA-A signed with Client A |
| 2026-06-15 | Director of the Division of Dam Safety and Inspections approves the owner as Client A's independent consultant (18 CFR 12.34(a)) |
| 2026-07-20 | AI-001 trial use stopped |
| 2026-07-20 to 2026-07-24 | Self-assessment with the on-call IT technician (under NDA since 2026-07-14). SaaS mapping 2026-07-22; tests 2026-07-23 |
| 2026-07-21 | Downloaded Client A security-sensitive documents found and deleted |
| 2026-07-22 | Client A told under CSCA-A (7) |
| 2026-07-24 | Client B told about the AI upload under GRS-B (1) and (3); deletion requested from the AI vendor |
| 2026-08-12 | AI vendor confirms deletion of the Client B readings in writing |
| 2026-08-25 | P10 AI use assessment completed by the owner-engineer |
| 2026-08-31 | Deliverables adopted by the owner-engineer |
| 2026-11-16 to 2026-11-18 | Client A Part 12D field inspection (planned) |
| 2026-12-31 | Upstream project CEII requester verification ends (a new request is needed for 2027 work) |
