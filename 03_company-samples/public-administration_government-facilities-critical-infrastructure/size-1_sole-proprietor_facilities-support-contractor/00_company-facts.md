# Scenario facts: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company and its customers are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Facilities support contractor (NAICS 561210, Facilities Support Services). The owner is a building controls technician who operates and maintains the building automation (HVAC controls) and electronic access control systems of government buildings, under one city contract and one federal subcontract. **The company owns no building system.** The government customers own every controller, reader, door, and server |
| Location | Florida. Home office in a spare room of the owner's residence (lockable door) and a work van with a locked parts and drawings cabinet. On site at customer buildings about 4 days a week. All customer buildings are in the same Florida metro area |
| Workforce | The owner only (0 employees, no subcontractors). Uses an on-call IT technician from a local IT services shop by the hour |
| Revenue | About $180,000 a year (fictional), about $720 per working day. CT-C about $115,000 (fixed monthly fee of $7,500 plus about $25,000 of repairs and after-hours call-outs); CT-F about $65,000 (hourly, billed monthly to the prime contractor). SBA-small (standard $47.0 million for NAICS 561210, 13 CFR 121.201) |
| Regulatory status | **Private contractor, not a government entity.** Customer security rules reach the owner **through contracts**: NIST SP 800-53 Rev. 5 Moderate safeguards through the city contract's security exhibit, and FAR clauses flowed down through the federal subcontract. Florida statutes that apply to the owner directly: Fla. Stat. 119.0701 (a contractor acting on behalf of a public agency) and 119.071(3)(b)4. (keep the exempt status of government building plans received). Fla. Stat. 501.171 (third-party agent) is treated as applying to the city cardholder exports; counsel to confirm (section 7) |
| Not in scope | Federal tax information (C-GOVERNMENT-R02): none. CJIS (R03): the city police station is a separate building outside CT-C. Election systems (R04): no election equipment is kept in the three city buildings. FERPA (R05): no education facilities. CIRCIA (R06): proposed rule only. SLCGP (R07): a grant condition for governments. GovRAMP (R08): the owner offers no cloud service. FedRAMP: no company system is operated on behalf of GSA. DFARS 252.204-7012 and CMMC: no Department of Defense work. NIST SP 800-171: the subcontract does not cite it (watch item) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: public records duties of contractors and the exemptions for security plans and building plans (Fla. Stat. 119.0701, 119.071(3)); breach duties of a third-party agent (Fla. Stat. 501.171); and the city's own duties that its contract flows down (Fla. Stat. 282.3185 and 282.3186) |

**Customers and contracts (fictional)**

| ID | Customer | Work | Data and access the owner holds | How security requirements reach the owner | Share of receipts |
|---|---|---|---|---|---|
| CT-C | A Florida city (population about 22,000) | Facilities support for 3 city buildings: city hall (about 38,000 sq ft), the public library (about 24,000 sq ft), and the community center (about 15,000 sq ft). BAS operation (schedules, setpoints, trends, alarm response), preventive maintenance of controls, and access control administration (cardholders, door schedules, lockdown and unlock requests). Three-year contract, 2024-10-01 to 2027-09-30 | Administrator access to the city's BAS (one supervisory controller and 31 field controllers) and to the city's cloud access control tenant (9 door controllers, 38 card readers, 312 cardholders). Monthly cardholder exports (name, department, badge photo, credential number, door groups, 30 days of access history). Building drawings, BAS riser diagrams, and door hardware schedules | City contract security exhibit: contractor devices and accounts used to administer city building systems or store city data must meet the NIST SP 800-53 Rev. 5 **Moderate** baseline as applicable to the contractor's environment (the city chose this for contractors with privileged access when it adopted its cybersecurity standards under Fla. Stat. 282.3185(4)(a)); MFA for remote access; notice to the city IT manager within 24 hours of discovering a suspected security incident; fingerprint-based background check; the city's annual basic cybersecurity training; the Fla. Stat. 119.0701(2) public records clause; return or destruction of city data at contract end; no subcontracting of system administration without written approval. Service levels: critical alarms acknowledged within 1 hour and worked within 4 hours, 24x7; badge removals completed within 4 business hours of the request | About 64% |
| CT-F | A prime facilities contractor that holds a GSA Public Buildings Service operations and maintenance contract for one federal office building (about 260,000 sq ft) | BAS controls technician support: programming changes, troubleshooting, and sequence checks, about 8 days a month on site, on call within 1 business day. Subcontract since 2025-03-01 | Federal contract information (FCI): work orders and BAS point lists emailed by the prime. 3 sets of mechanical and controls drawings marked **CUI** (Physical Security category). GSA's BAS is reached **only on site**, through a GSA-furnished engineering workstation on the GSA Building Systems Network (BSN), with the owner's GSA-issued PIV card. No remote access to any GSA system | Subcontract flow-downs: FAR 52.204-21 (NOV 2021) per paragraph (c); FAR 52.204-23 (DEC 2023); FAR 52.204-25 (NOV 2021) without paragraph (b)(2), as 52.204-25(e) directs; FAR 52.204-30 (DEC 2023) without paragraph (c)(1), as 52.204-30(e)(1) directs; FAR 52.204-9 (JAN 2011). CUI handling under 32 CFR Part 2002 and GSA Order PBS 3490.3 CHGE 1. GSA IT security policies through the GSA Building Technologies Technical Reference Guide (BTTRG) v3.0. Notice to the prime **immediately** on discovery of any incident involving GSA systems, GSA data, or the owner's PIV card or GSA credentials, so the prime can report to GSA IT immediately (BTTRG section 1.6.1). GSA annual IT security awareness training | About 36% |

## 2. People and outside parties (role titles only)
| Role | Duties |
|---|---|
| Owner (building controls technician) | Every role: owner, security officer, privacy and records contact named in the contracts, CUI handler, incident handler, contract compliance, and risk acceptor |
| On-call IT technician (local IT services shop) | Hourly help with the laptop, phone, and home network. No standing access; remote sessions are started and watched by the owner. Signed a nondisclosure agreement on 2026-08-03 |
| City IT manager (customer role) | Owns the city identity provider, VPN, and network; second administrator of the access control tenant; receives the 24-hour incident notice |
| City facilities manager (customer role) | Directs the owner's work; approves door schedule and setpoint changes; asked for the face verification trial (P10) |
| Prime contractor project manager and security officer (customer roles) | Issue CT-F work orders; sponsor the owner's PIV card with GSA; receive the owner's incident notices and report to GSA |
| Controls distributor and parts suppliers | Sell replacement controllers, sensors, readers, and network parts |
| Insurance agent | General liability and professional liability policies. **No cyber coverage** |

## 3. Systems
| ID | System | Hosting | Holds customer data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business laptop | Owner device | Yes (city drawings, cardholder exports, controller program backups; CUI drawings in the downloads folder) | The only work computer. Built-in full-disk encryption on; built-in antivirus; automatic updates. Holds the BAS engineering software, the city VPN client, and the remote-desktop client. **The owner signs in daily with an administrator account** |
| SYS-02 | Productivity suite, business plan (email, calendar, cloud file storage with a sync folder) | SaaS | Yes (drawings, cardholder exports, CT-F work orders, CUI drawings) | MFA on (authenticator app). Receives BAS alarm emails. **New sharing links default to "anyone with the link"** |
| SYS-03 | Mobile phone | Owner's personal phone | Incidental (email, alarm texts, photos of panels and door hardware) | Passcode, encrypted. Holds the authenticator app for every MFA prompt and the access control vendor's mobile administrator app. **No recovery codes stored anywhere** |
| SYS-04 | Remote-desktop service (SaaS subscription) with an agent on the city hall BAS engineering workstation | SaaS plus an agent on city equipment | A path into the city BAS network | Installed 2024-11 with the city facilities manager's verbal approval for after-hours alarm response. **Unattended access on; account protected by a password only (MFA available but off); city IT manager never told; bypasses the city VPN** |
| SYS-05 | Accounting and invoicing SaaS | SaaS | No (invoices to the city and the prime) | MFA on |
| SYS-06 | Home office network | ISP-supplied router | In transit | **Default router administrator password; firmware never updated; one Wi-Fi network shared with family devices** |
| SYS-07 | Consumer generative AI chatbot (free plan) | SaaS | Yes, from June 2026 (see P10) | Used to troubleshoot BAS logic and draft monthly reports. **Model-improvement setting on** |
| SYS-08 | City building systems (customer-owned; outside the boundary) | City | Yes | BAS supervisory controller in the city hall mechanical office and 31 field controllers (city hall 14, library 11, community center 6), reached through the city VPN (city MFA) or SYS-04. Cloud access control tenant reached through the city identity provider (city MFA). **The owner uses the BAS supervisory controller's shared built-in administrator account; its password has not changed since 2023** |
| SYS-09 | GSA building systems at the federal building (outside the boundary) | GSA | CUI and GSA data | GSA BAS on the BSN, reached only on site through a GSA-furnished workstation with the owner's PIV card. GSA's system under GSA's authorization |

**SSP system (P02):** the *Building Systems Support Environment*: SYS-01 to SYS-07, plus the owner's administrator accounts and remote access paths into the city building systems (SYS-08). The city and GSA systems themselves (SYS-08, SYS-09) are outside the boundary.

## 4. Current security posture: informal, basic hygiene with big gaps
**In place today:**
- MFA on the productivity suite, the accounting service, the city VPN, and the city access control tenant (through the city identity provider)
- Built-in full-disk encryption on the laptop (turned on by the IT technician in 2025); the phone is encrypted by its passcode
- Automatic operating system updates and built-in antivirus with real-time protection
- City fingerprint-based background check (September 2024); GSA PIV card issued in March 2025 after GSA's background investigation
- GSA annual IT security awareness training (completed 2026-03-12) and the city's basic cybersecurity training (completed 2026-02-20)
- At the federal building the owner uses only the GSA-furnished workstation and never connects the laptop to the BSN
- Signed contracts with security terms for both customers
- Paper drawings kept in the locked van cabinet or the home office; cross-cut shredder at home

**Missing:**
1. No risk assessment, no written security policy, and no record of where city and GSA data are kept.
2. The remote-desktop agent on the city hall BAS engineering workstation allows unattended access with a password-only account, bypasses the city VPN, and was never disclosed to the city IT manager.
3. The BAS supervisory controller uses one shared built-in administrator account; its password was set by the city's previous integrator in 2023, has not changed, and is kept in the phone's notes app.
4. Controller programs and door schedule exports exist only on the laptop (the engineering folder is excluded from cloud sync). No restore has ever been tested.
5. CUI drawings are kept in the general cloud folder and email, with no marking or handling routine and no CUI training.
6. No incident response plan. The contract clocks (city 24 hours; prime immediately; Fla. Stat. 501.171(6)(a) 10 days) are not written down.
7. No screening of parts against FAR 52.204-23, 52.204-25, or 52.204-30, and no check of SAM.gov for FASCSA orders.
8. The owner uses an administrator account for daily work on the laptop.
9. Home router: default administrator password, old firmware, and one flat network shared with family devices.
10. No review of the access control audit trail, the remote-desktop session log, or the BAS audit log.
11. Single-person dependency: only the owner can answer city alarms after hours; the city has no backup technician; every MFA prompt goes to one phone.
12. The consumer AI chatbot was used with city BAS point lists and a door schedule excerpt, with the model-improvement setting on.
13. The city asked the owner to configure the access control vendor's face verification add-on at the city hall staff entrance; a vendor trial is on in the city's tenant with no AI assessment.
14. No cyber insurance.
15. No security training beyond the two customer awareness courses.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | The registry default ("Physical access control and building automation system") is owned by the customers, not by a one-person contractor. The SSP covers the owner's **Building Systems Support Environment**, the devices, SaaS accounts, and access paths used to run the customers' systems. The city and GSA systems stay outside the boundary, but the owner's access into them is in scope everywhere |
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline, reached through the city security exhibit and scoped to what the owner controls, with an overlay of the FAR clauses flowed down by the federal subcontract (FAR 52.204-21, -23, -25, -30, -9) and three Florida rows (Fla. Stat. 119.0701(2)(b), 119.071(3), 501.171(2)) |
| P08 incident | Intrusion into the city's building access control and automation systems through the owner's remote-desktop account or stolen credentials (the registry default, adapted to the owner's access path: the owner does not host the systems) |
| P09 SOC 2 | Security criteria only, as a self-check. The owner is a service provider to the city but no customer asks a one-person contractor for a SOC 2 report; the city uses its security exhibit and questionnaire. Includes a review of the productivity suite provider's SOC 2 report, because that service holds city files and CUI |
| P10 AI | AI-001: the face verification add-on in the city's access control tenant (facial recognition for facility access, the registry default), which the city asked the owner to configure; AI-002: the consumer generative AI chatbot the owner uses. At this size the owner builds nothing; the question is whether the owner will configure and operate a third-party AI feature |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-08-10 to 2026-08-14 | Self-assessment (BIA, system profile, SaaS mapping, risk register, gap analysis), with the on-call IT technician under NDA |
| 2026-08-18 to 2026-08-20 | Control tests (P07), with the on-call IT technician; library controller tests on the evening of 2026-08-19 with the city facilities manager present |
| 2026-09-04 | Deliverables adopted by the owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
