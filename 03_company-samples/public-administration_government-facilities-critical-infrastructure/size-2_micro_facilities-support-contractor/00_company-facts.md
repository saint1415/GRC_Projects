# Scenario facts: Cris Santos Company | Government Services and Facilities | Micro

All 10 deliverables in this folder use the facts below. The company and its customers are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is the sole member and general manager) |
| Business | Facilities support contractor (NAICS 561210, Facilities Support Services). The company operates and maintains the building automation (HVAC controls), electronic access control, and entrance video systems of government buildings, and provides one on-site building engineer, under two local government contracts and one federal subcontract. **The customers own the buildings and every field device** (controllers, door hardware, readers, cameras). The company holds the cloud services and site gateways it uses to run them (section 3) |
| Location | Florida. One leased office suite with a locked parts room and network closet. All customer buildings are in the same Florida metro area |
| Workforce | 7 employees: the owner (general manager and senior controls engineer), an Office and Compliance Manager, a Service Coordinator, a Lead Controls Technician, a Controls Technician, a Security Systems Technician, and a Building Engineer. IT is supported by a managed service provider (MSP) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day: CT-C about $540,000 (49%), CT-M about $310,000 (28%), CT-F about $250,000 (23%). SBA-small (standard $47.0 million for NAICS 561210, 13 CFR 121.201) |
| Regulatory status | **Private contractor, not a government entity.** Customer security rules reach the company **through contracts**: NIST SP 800-53 Rev. 5 Moderate controls through the county security exhibit, the city's cybersecurity standards through the city contract, and FAR clauses flowed down through the federal subcontract. Florida statutes that apply to the company directly: Fla. Stat. 119.0701 (a contractor acting on behalf of a public agency), 119.071(3) (keep the exempt status of security system plans and building plans it receives), and 501.171 (reasonable security, third-party agent notice, and disposal; how far it reaches county cardholder data is for counsel to confirm, section 7) |
| Not in scope | Federal tax information (C-GOVERNMENT-R02): none; the county tax collector is not a customer. CJIS (R03): the county sheriff's office and the city police headquarters are not in either contract. Election systems (R04): the county supervisor of elections office is in a separate building outside CT-C. FERPA (R05): no education facilities. CIRCIA (R06): proposed rule only. SLCGP (R07): a grant condition for governments. GovRAMP (R08): no customer requires it of the company; the access control vendor's status is reviewed in P09. FedRAMP: no company system operates on behalf of GSA. DFARS 252.204-7012 and CMMC: no Department of Defense work. NIST SP 800-171: the subcontract does not cite it (watch item). HIPAA: no health information |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: public records duties of contractors and the exemptions for security system plans and building plans (Fla. Stat. 119.0701, 119.071(3)); breach duties (Fla. Stat. 501.171); and the customers' own duties that the contracts flow down (Fla. Stat. 282.3185 and 282.3186) |

**Customers and contracts (fictional)**

| ID | Customer | Work | Data and access the company holds | How security requirements reach the company | Share of receipts |
|---|---|---|---|---|---|
| CT-C | A Florida county (population about 140,000) | Facilities support for 4 county buildings: the county administration building (about 110,000 sq ft), 2 branch libraries, and the parks operations building. BAS operation and preventive maintenance, one Building Engineer on site at the administration building on weekdays, 24x7 alarm response, and a **managed access control and video service** run on the company's own cloud tenant (SYS-01). Contract 2025-01-01 to 2027-12-31 | Cardholder records for about 1,050 county employees, contractors, and volunteers (name, department, badge photo, credential number, access groups, access history); entrance video; 52 face templates in the face verification pilot (P10); BAS point lists, trends, and graphics; building drawings, door hardware schedules, and security system layouts | County security exhibit: systems the vendor hosts for the county, and vendor accounts with privileged access to county systems, must meet the **NIST SP 800-53 Rev. 5 Moderate** controls as applicable to the vendor's environment (the county chose this when it adopted its cybersecurity standards under Fla. Stat. 282.3185(4)(a)); MFA for all remote and administrator access; notice to the county IT security officer **within 24 hours** of discovering a suspected security incident affecting county systems, data, or buildings; fingerprint-based background checks; the county's annual basic cybersecurity training for vendor staff with county system access; the Fla. Stat. 119.0701(2) public records clause; return or destruction of county data within 30 days after contract end; an annual vendor security questionnaire answered with a SOC 2 report **or an equivalent readiness self-assessment**. Service levels: critical alarms acknowledged within 1 hour and a technician on site within 4 hours, 24x7; badge removals within 4 business hours of a county request; emergency lockdown or unlock within 15 minutes of a request | About 49% |
| CT-M | A Florida city (population about 48,000) | BAS controls service and access control administration for 3 city buildings: city hall, the community center, and the public works administration building. Contract 2024-10-01 to 2027-09-30 | Named administrator accounts on the **city-owned** BAS supervisory server and on-premises access control server (SYS-10), reached through the city VPN with city MFA. Read-only BAS alarm and trend feed through the company's monitoring service (SYS-02). City drawings and door schedules | City contract security terms: follow the city's cybersecurity standards (NIST CSF-based, adopted under Fla. Stat. 282.3185(4)(a)); named accounts and city MFA for all access; incident notice to the city IT manager **within 24 hours** of discovery; fingerprint-based background checks; the 119.0701(2) public records clause. Critical alarms acknowledged within 1 hour, 24x7 | About 28% |
| CT-F | A prime facilities contractor that holds a GSA Public Buildings Service operations and maintenance contract for one federal office building (about 300,000 sq ft) | BAS controls technician support: programming changes, troubleshooting, and sequence checks, about 10 days a month on site. Subcontract since 2025-06-01 | Federal contract information (FCI): work orders and BAS point lists emailed by the prime. 3 sets of mechanical and controls drawings marked **CUI** (Physical Security category). GSA's BAS is reached **only on site**, through a GSA-furnished engineering workstation on the GSA Building Systems Network (BSN), with GSA-issued PIV cards (2 staff). No remote access to any GSA system | Subcontract flow-downs: FAR 52.204-21 (NOV 2021) per its paragraph (c); FAR 52.204-23 (DEC 2023); FAR 52.204-25 (NOV 2021) without paragraph (b)(2), as 52.204-25(e) directs; FAR 52.204-30 (DEC 2023) without paragraph (c)(1), as 52.204-30(e)(1) directs; FAR 52.204-9 (JAN 2011). CUI handling under 32 CFR Part 2002 and GSA Order PBS 3490.3 CHGE 1. GSA IT security policies through the GSA Building Technologies Technical Reference Guide (BTTRG) v3.0. Notice to the prime **immediately** on discovery of any incident involving GSA systems, GSA data, or a PIV card or GSA credential, so the prime can report to GSA IT immediately (BTTRG section 1.6.1). GSA annual IT security awareness training for PIV holders | About 23% |

## 2. People and outside parties (role titles only)
| Role | Security and privacy duties |
|---|---|
| Owner (general manager and senior controls engineer) | System owner of the SSP system; accepts all Moderate and higher risks; approves policies, spending, and AI use; executive contact for all three customers; backup incident lead |
| Office and Compliance Manager | Designated **Information Security Officer** (part-time, alongside office, HR, billing, and contract administration); keeps the risk register, SSP, and POA&M; CUI program lead; FAR flow-down and supplier screening; onboarding and terminations; incident lead and notice coordinator |
| Service Coordinator | Dispatch, CMMS work orders, phones, parts purchasing; backup to the Office and Compliance Manager for notices and records |
| Lead Controls Technician | Administers the BAS monitoring service (SYS-02) and the site gateways (SYS-03); BAS programming standards; on-call rotation lead; PIV holder (CT-F) |
| Controls Technician | BAS field work; on site at the federal building about 10 days a month; on-call rotation; PIV holder (CT-F) |
| Security Systems Technician | Administers the managed access control and video tenant (SYS-01); card enrollment, door schedules, lockdown requests; turned on the face verification pilot; on-call rotation |
| Building Engineer | On site at the county administration building on weekdays; uses a rugged tablet for CMMS work orders; no administrator rights |
| Managed service provider (MSP) | IT support for the office network, laptops, productivity suite, and the suite backup, through a remote monitoring and management (RMM) agent. Does **not** manage the site gateways or any OT. Service contract with a confidentiality clause and a 4-business-hour response time; no other security terms |
| SaaS vendors | Access control and video platform (SYS-01, SOC 2 Type 2 report), BAS monitoring service (SYS-02), productivity suite (SYS-04), CMMS (SYS-05), suite backup (SYS-08, resold by the MSP), payroll and HR service (SYS-09) |
| Mechanical subcontractor | Specialty HVAC repairs at the county buildings; receives work orders and drawings |
| Cyber insurer | Cyber liability policy bought in 2025 at the county's request, with a 24x7 breach hotline and panel vendors (breach counsel, forensics) |
| Customer contacts (customer roles) | County IT security officer and county facilities director; city IT manager and city facilities manager; the prime contractor's project manager and security officer |

## 3. Systems
| ID | System | Hosting | Holds customer or sensitive data? | Notes |
|---|---|---|---|---|
| SYS-01 | Managed access control and video service: the company's tenant in a vendor's cloud access control and video platform, serving the 4 CT-C buildings: 16 county-owned door controllers, 52 readers, 38 cloud-connected entrance cameras | Vendor SaaS (company subscription) plus county-owned field devices | Yes: about 1,050 cardholder records, access history (365 days, the vendor default), video (30 days), 52 face templates (pilot) | Door controllers keep enforcing the last downloaded cardholder list and schedules if the cloud service is unreachable. Vendor has a SOC 2 Type 2 report. 3 company administrator accounts with MFA (vendor authenticator app); 2 county security staff hold operator accounts (view, lockdown) |
| SYS-02 | BAS monitoring and alarm service: vendor SaaS (company subscription) that collects BACnet alarms and trends from 7 customer buildings (4 county, 3 city) through SYS-03 and sends alarm notifications to the on-call phone. Remote write (schedules and setpoints) is enabled for the county buildings; the city buildings are read-only | Vendor SaaS | Operational data: point lists, trends, alarm history, floor-plan graphics | Named accounts with MFA for the owner and the Lead Controls Technician. **A shared "oncall" account with a password only is used by the 3 technicians on the on-call rotation** |
| SYS-03 | Site edge gateways: 7 company-owned industrial gateways, one per monitored building, with outbound encrypted tunnels to SYS-02 and a technician remote-access VPN into each building's BAS network | On customer premises (BAS networks) | In transit | Managed by the Lead Controls Technician, not the MSP. No inbound services from the internet |
| SYS-04 | Productivity suite (email, calendar, files, chat), business plan | SaaS | Yes: drawings, cardholder exports, CUI drawings, FCI | MFA on (authenticator app). External sharing allowed, including "anyone with the link" |
| SYS-05 | Computerized maintenance management system (CMMS) | Vendor SaaS | FCI for CT-F; asset lists and work orders for all three contracts | MFA on |
| SYS-06 | Endpoints: 6 laptops (owner, Office and Compliance Manager, Service Coordinator, 3 technicians), 3 rugged tablets, 7 company phones | Company-owned; laptops MSP-managed; tablets and phones in the suite's basic mobile device management | Yes (cached): technician laptops hold the BAS and access control engineering software and the only copies of controller programs and door schedule exports | Laptops encrypted (built-in full-disk encryption). Technicians are local administrators because the BAS engineering tools require it |
| SYS-07 | Office network: small-business firewall, staff Wi-Fi, separate guest Wi-Fi, one business internet line | On-premises, MSP-managed | In transit | |
| SYS-08 | SaaS-to-SaaS backup of the productivity suite (mail and files), 1-year retention | SaaS, operated by the MSP | Yes | Never restore-tested. Does not cover laptops, SYS-01, or SYS-02 configuration |
| SYS-09 | Payroll and HR service | Vendor SaaS | Yes: employee SSNs, bank details, background check results | Outside the SSP boundary |
| SYS-10 | City building systems (customer-owned): BAS supervisory server and on-premises access control server on the city network | City | Yes | Outside the boundary. Reached through the city VPN with city MFA and named accounts |
| SYS-11 | GSA building systems at the federal building | GSA | CUI and GSA building data | Outside the boundary. GSA BAS on the BSN, reached only on site through a GSA-furnished workstation with a PIV card; GSA's system under GSA's authorization |
| SYS-12 | Face verification add-on (pilot): a feature of the SYS-01 platform with 2 face-capable readers at the county administration building employee entrance | Part of SYS-01 | Yes: face templates (treated as biometric data) | Turned on 2026-06-15 at the county facilities director's request; 52 county employees enrolled (P10) |

**SSP system (P02):** the *Building Systems Operations Platform*: SYS-01 (the company's tenant and its configuration, including SYS-12), SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07, and SYS-08, plus the company's administrator accounts and access paths into the city building systems (SYS-10). The customer field devices, the city and GSA systems themselves (SYS-10, SYS-11), and the payroll service (SYS-09) are outside the boundary.

## 4. Current security posture: early to partial
**In place today:**
- MFA on the productivity suite, the CMMS, the SYS-01 administrator accounts, the named SYS-02 accounts, and the city VPN (city MFA)
- MSP patching, antivirus, and firewall management for the office and laptops; full-disk encryption on all 6 laptops
- Site gateways use outbound-only encrypted tunnels; no inbound services from the internet
- Fingerprint-based background checks for all 7 employees (county and city requirement); 2 GSA PIV cards issued after GSA's background investigations
- GSA annual IT security awareness training for the 2 PIV holders; the county's basic cybersecurity training for the 4 staff with county system access
- At the federal building, staff use only the GSA-furnished workstation and never connect company devices to the BSN
- An access control vendor with a SOC 2 Type 2 report
- Cyber insurance with a breach hotline
- Locked office suite, parts room, and network closet with an alarm

**Missing:**
1. No risk assessment before 2026 and no written security policies. The county security exhibit, signed in 2025, was never mapped to what the company does.
2. A shared "oncall" account with a password only is used on SYS-02 to change schedules and setpoints at the county buildings.
3. Account removal is ad hoc. A former Security Systems Technician (left 2026-04-17) still had an active SYS-01 administrator account when it was found on 2026-07-15.
4. Gateway hygiene: firmware is 2 releases behind on 5 of the 7 gateways; no change records; nobody patches them on a schedule.
5. No reconciled inventory of gateways and customer field devices; the CMMS asset list is the only list.
6. Controller programs, door schedules, and SYS-01 and SYS-02 configuration exports exist only on technician laptops; the suite backup (SYS-08) has never been restore-tested.
7. CUI drawings sit in the general shared folder with no marking routine or CUI training.
8. No incident response plan. The contract clocks (county and city 24 hours, prime immediately) and the Fla. Stat. 501.171 clocks are not written down.
9. No supplier screening against FAR 52.204-23, 52.204-25, or 52.204-30 for parts supplied under CT-F, and no search of SAM.gov for FASCSA orders.
10. No review of the SYS-01 audit trail, SYS-02 audit log, gateway logs, or suite sign-in logs.
11. The MSP holds standing administrator access through its RMM tool with no evidence of MFA, and its contract has no security or incident notice terms.
12. No security training beyond the customer courses; no phishing exercises; no role-based OT or CUI training.
13. The face verification add-on was turned on in SYS-01 at the county's request with no AI assessment, no consent form, and the vendor's default (indefinite) template retention.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| Primary system | The registry default ("Physical access control and building automation system") is adapted to what a 7-person contractor holds. The SSP covers the **Building Systems Operations Platform**: the company's own access control tenant (SYS-01), BAS monitoring service (SYS-02), site gateways (SYS-03), and the office SaaS and endpoints used to run them. The customers' field devices and the city and GSA systems stay outside the boundary, but the company's access into them is in scope everywhere |
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline (177 base controls), binding by the county security exhibit for SYS-01, SYS-02, SYS-03, and the accounts that administer them, and used as the benchmark for the rest of the platform. OT tailoring from NIST SP 800-82 Rev. 3. Overlays: the FAR clauses flowed down by the federal subcontract (52.204-21, -23, -25, -30, -9) and the Florida statutes that bind the company directly (501.171, 119.0701, 119.071(3)) |
| P08 incident | Intrusion into building access control and automation systems through the shared SYS-02 account or a stolen SYS-01 administrator credential (the registry default, adapted to the company's access paths); the MSP and the cyber insurer are in the notification chain |
| P09 SOC 2 | Security plus Confidentiality, as a readiness self-assessment that answers the county's annual vendor security questionnaire; plus a review of the SYS-01 vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: face verification (1:1) pilot in SYS-01 at the county administration building employee entrance (facial recognition for facility access, the registry default); AI-002: the SYS-02 vendor's machine-learning alarm prioritization feature; AI-003: public generative AI chatbots |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup of the productivity suite (SYS-08), operated by the MSP. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-24 | Risk assessment and gap analysis fieldwork with the MSP lead technician (site walkthroughs 2026-07-15 to 2026-07-16) |
| 2026-08-03 to 2026-08-06 | Control assessment by an independent consultant (gateway tests on the evening of 2026-08-05 with the county facilities director's approval) |
| 2026-08-31 | Deliverables approved by the owner |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
