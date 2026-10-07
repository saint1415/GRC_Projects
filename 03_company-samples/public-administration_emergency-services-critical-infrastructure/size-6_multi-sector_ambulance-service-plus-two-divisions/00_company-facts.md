# Scenario facts: Cris Santos Company | Emergency Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant) |
| Structure | A holding company with three operating divisions, each a separate subsidiary, plus corporate shared services in the parent |
| Division 1: Ambulance Services (NAICS 621910), **focus of this scenario** | Ground ambulance service: basic life support (BLS), advanced life support (ALS), and critical care transport. 911 emergency response under 38 county and municipal ambulance agreements, plus interfacility transport for about 260 hospitals and facilities. About 2,400 ambulances and 3.1 million responses a year. About 24,000 employees (about 19,000 EMTs and paramedics). A HIPAA covered entity and a Medicare ambulance supplier |
| Division 2: Urgent Care (NAICS 621493, sector 62 Health Care and Social Assistance) | 520 freestanding urgent care clinics plus a telehealth service; about 11 million visits a year. About 13,000 employees. A HIPAA covered entity. Accepts Medicare and Medicaid |
| Division 3: Billing and Dispatch Services, "BDS" (NAICS 561110, sector 56 Administrative and Support Services) | (a) Revenue cycle services for both internal divisions and about 170 external clients (fire-based and municipal EMS agencies, hospital-based ambulance services, other ambulance companies, physician groups) in 22 states; (b) emergency medical communications services: 4 regional communications centers that dispatch the Ambulance division's units and provide dispatch under contract to 14 external EMS agencies; (c) a patient billing contact center that takes card payments. About 5,000 employees. A **business associate** of both internal divisions and of its external clients; issues a SOC 2 Type 2 report for revenue cycle services |
| Corporate shared services | Identity, network, cloud platform, security operations, finance, HR, legal, internal audit. About 3,000 employees |
| Location | Headquartered in Florida. Ambulance Services and Urgent Care operate in 7 southeastern states; BDS billing clients are in 22 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Licenses | State EMS licenses in each of the 7 states (Florida worked example: Fla. Stat. 401.25 and Chapter 64J-1, F.A.C.) and county certificates of public convenience and necessity where counties require them. Each state operation has a physician medical director (Florida: Fla. Stat. 401.265(1)) |
| County 911 relationship | County public safety answering points (PSAPs), run by sheriffs or county 911 authorities, answer 911 calls. 21 PSAPs send EMS incidents to the BDS CAD over CAD-to-CAD interfaces and transfer callers to BDS telecommunicators. The group has **no access** to state or national criminal justice databases. One county feed is under review (gap 5) |
| Not in scope | 42 CFR Part 2 (no federally assisted substance use disorder program); FTC Health Breach Notification Rule (all health data is held by or for HIPAA covered entities); FCC EAS rules (not an EAS participant); federal procurement clauses (no federal contracts; Medicare and Medicaid billing is not a procurement contract) |

## 2. People (role titles only)
| Role | Security and privacy duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks; approves group policy POL-01 and POL-03 |
| Board audit committee | Oversees group internal audit |
| Disclosure committee | SEC materiality decisions (Form 8-K Item 1.05) |
| Group CISO | Group security program; operates common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up; chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Data classification, minimum-necessary protocols, BAAs with the Group General Counsel |
| Group General Counsel | Intercompany and client agreements; owns the notification matrix |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Division security and compliance leads (3) | Division supplements, division risk registers, division regulators; accept Low risks |
| Division HIPAA Security and Privacy Officers | Ambulance Services and Urgent Care (separate covered entities) each designate their own (45 CFR 164.308(a)(2)); BDS designates security and privacy officials as a business associate |
| Ambulance Services chief medical officer | Clinical oversight across state medical directors; clinical owner of AI call triage |
| BDS vice president of communications operations | Runs the 4 communications centers and manual dispatch procedures |
| Group dispatch and clinical platforms director | System owner of the Dispatch and Patient Care Platform (the P02 system) |
| Group internal audit | Independent assessor; reports to the board audit committee; assesses common controls once and samples division controls |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (single sign-on, MFA, privileged access management, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and endpoint detection and response (EDR) | Corporate |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic: provider A primary, provider B for disaster recovery and the backup vault) and the group wide-area network to about 1,100 sites | Corporate |
| SYS-G4 | Group ERP, HR, and payroll platforms (SaaS) | Corporate |
| SYS-D1 | Ambulance fleet and patient care systems: electronic patient care reporting (ePCR, vendor SaaS), fleet mobile systems (vehicle routers, mobile data computers, ePCR tablets, cardiac monitors with a vendor 12-lead relay), crew scheduling | Ambulance Services |
| SYS-D2 | Urgent Care EHR and practice management (vendor-hosted), online check-in and scheduling, telehealth service | Urgent Care |
| SYS-D3 | BDS revenue cycle platform (multi-client) with clearinghouse connections, and the patient billing contact center (contact-center SaaS with call recording and card payments) | BDS |
| SYS-D4 | BDS communications centers: computer-aided dispatch (CAD, vendor-licensed software run on SYS-G3), call handling and recording, radio console gateways to county P25 systems, AI call triage module (CAD vendor cloud service) | BDS |

**SSP system (P02):** the *Dispatch and Patient Care Platform (DPCP)*: the CAD and communications center components of SYS-D4, the ePCR and fleet mobile systems of SYS-D1, and the integration engine that links them, used by the Ambulance and BDS divisions; it inherits common controls from SYS-G1 to SYS-G3.

## 4. Current security posture: a defined program with group-level gaps
**In place today:**
- Group policies aligned to CSF 2.0 and a common control catalog
- 24x7 group SOC with EDR on servers and corporate endpoints
- Privileged access management for cloud and server administrators
- MFA for all workforce applications federated to SYS-G1, and quarterly access certification for them
- Immutable backups for group cloud workloads in provider B
- An annual penetration test of internet-facing systems
- BDS revenue cycle services SOC 2 Type 2 report, issued annually
- SEC Reg S-K Item 106 disclosure in the annual report
- A group incident response plan and cyber insurance

**Gaps:**
1. **CAD resilience.** The CAD runs as one production instance in provider A that serves all 4 communications centers. Failover to provider B has never been tested, and manual dispatch drills at each center are annual and assume an outage of a few hours.
2. **CAD and fleet identity.** Dispatchers sign in to CAD through SYS-G1, but mobile data computers use one shared CAD account per vehicle, and the CAD vendor's 6 remote support accounts are local, persistent, and outside PAM.
3. **Legacy shared account.** The CAD servers and the revenue cycle integration and file transfer servers share a management subnet in a cloud account created in 2019, before the landing zone. It was never migrated.
4. **Fleet devices.** About 2,400 vehicle routers and the cardiac monitors are managed by the Ambulance division's fleet technology team outside group configuration management. Router firmware is not centrally tracked.
5. **Possible criminal justice information.** One county's CAD-to-CAD feed carries premise notes copied from the sheriff's law enforcement records system. Whether these notes are criminal justice information under the FBI CJIS Security Policy has not been determined.
6. **AI call triage.** The CAD vendor's AI triage module went into advisory mode at the Florida communications center on 2026-06-01, before Group AI council review. External dispatch clients were not told that their callers' audio is processed by the module.
7. **Multi-party notification.** A dispatch incident could trigger notices from two covered entities, BDS notices to external clients under different BAA terms, county contract notices, and an SEC materiality decision. The notification matrix has not been exercised.
8. **Urgent Care drift.** 46 clinics acquired in 2025 still run a legacy practice management and EHR system that is not federated to SYS-G1 or sent to the SIEM, and the Urgent Care policy supplement was last aligned to group policy in 2024.
9. **Card payments in the contact center.** Billing contact center agents hear card numbers read aloud, and call recording is paused manually during payment.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 | Ransomware takes down the CAD across all 4 communications centers and steals data from the CAD database and the revenue cycle file transfer server: a cross-division incident with a multi-regulator, multi-client notification matrix and an SEC materiality decision (the registry scenario, computer-aided dispatch outage from ransomware, at group scale) |
| P09 | SOC 2 scoped per division: BDS is a true service organization (revenue cycle services Type 2 continues; dispatch services gets a first readiness assessment). Ambulance Services and Urgent Care are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the regulator-specific rules. Priority use case: AI-assisted emergency call triage (the registry use case) |
| Cloud | Shared corporate platform on two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division risk analyses, BIAs, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-26 | Group AI council assessment of AI use cases |
| 2026-09-02 | SOC 2 readiness assessments completed |
| 2026-09-16 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Legal entities | Ambulance Services and Urgent Care are legally separate subsidiaries under common ownership. They have **not** designated themselves an affiliated covered entity (45 CFR 164.105(b)); each is a separate covered entity. BDS is a separate subsidiary that acts as business associate to both. Corporate shared services is a business associate of both covered entities and a subcontractor business associate of BDS, under intercompany BAAs signed in 2023 |
| Revenue split (fictional) | Ambulance Services about $8.1 billion (about $22.2 million a day); Urgent Care about $6.7 billion (about $18.4 million a day); BDS about $3.2 billion including intercompany fees (about $8.8 million a day). Total about $18.0 billion |
| Communications centers | 4 regional centers (Florida, plus 3 in other states), about 1,100 telecommunicators. About 8,500 ambulance responses a day are dispatched through the CAD. Each center can take another center's calls over the shared CAD; there is no CAD instance outside provider A |
| External dispatch clients | 14 EMS agencies (8 fire-based or municipal EMS agencies and 6 hospital-based ambulance services) contract with BDS for dispatch. All are HIPAA covered entities and have BAAs with BDS. Their contracts require a phone call to the agency duty officer within 15 minutes of a CAD outage and a written report within 24 hours (contract terms, not law) |
| County ambulance agreements | The 38 county and municipal agreements require immediate phone notice to the county PSAP supervisor of any dispatch disruption and a written report within the period each agreement sets (most say 24 hours). They also set response-time standards with penalties (contract terms) |
| Billing clients and BAA terms | About 170 external revenue cycle clients. The standard BDS BAA (2025 version) requires notice of a breach of unsecured PHI within 10 calendar days of discovery and of other security incidents within 5 business days. 31 clients negotiated 72-hour breach notice |
| Data volumes | CAD database: about 21 million incident records over 7 years, including patient names, addresses, callback numbers, and chief complaints, about 9.6 million of them Florida residents. Revenue cycle platform: about 34 million patient accounts across both divisions and external clients. Urgent Care EHR: about 7.5 million patients |
| CAD-to-CAD and CJIS question | 21 county PSAP interfaces. The county feed in gap 5 has delivered premise notes into the BDS CAD since 2024-11 (about 3,400 premises). The note field was suppressed on 2026-08-20 pending a determination by the county and its CJIS Systems Agency |
| AI call triage | Shadow mode at all 4 centers since 2026-02-02; advisory (upgrade-prompt only) mode for English-language calls at the Florida center since 2026-06-01. The CAD vendor BAA was amended on 2026-04-30 to cover AI processing for the two internal divisions; it does not cover external clients' callers |
| Other AI use cases (P10 inventory) | ePCR narrative drafting (Ambulance, piloted on 300 tablets); system status management model that recommends ambulance posting locations (Ambulance); urgent care AI scribe (Urgent Care, 140 providers in 2 states); online symptom checker chatbot (Urgent Care, proposed); ambulance claim coding assistant that suggests level of service from the ePCR (BDS); claim denial prediction model (BDS); enterprise generative AI assistant (Group pilot, 1,500 users). A Group AI Standard and the Group AI council were adopted in 2026-03 |
| Payment cards | The billing contact center takes about 40,000 card payments a month by phone. The online patient payment page is hosted by a payment processor, outside group systems. BDS has filed a self-assessment as a merchant only; it has never assessed the contact center as a service provider for its clients |
| Cloud | Provider A hosts the landing zone, the CAD, the integration engine, the revenue cycle platform, and Urgent Care online check-in. Provider B hosts the disaster recovery region (not yet built for the CAD) and the immutable backup vault. The ePCR, the Urgent Care EHR, the telehealth service, the contact-center service, and the AI triage module are vendor SaaS |
| Florida Digital Bill of Rights | Not applicable. The group exceeds $1 billion in global gross annual revenue, but it earns no revenue from selling online advertisements, operates no consumer smart speaker and voice command service, and operates no app store, so it is not a "controller" under Fla. Stat. 501.702 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. Risks that could delay an emergency response or harm a patient may not be accepted at High; they must be treated |
