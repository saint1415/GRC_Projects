# Scenario facts: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

All 10 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation, the citation is given. This scenario is independent of the other sizes.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held by its owner, who is also the Principal Health Physicist) |
| Business | Radiation safety consulting practice (NAICS 541690). Five service lines: (1) consulting Radiation Safety Officer (RSO) support and annual radiation protection program audits for materials licensees and x-ray registrants; (2) **Part 37 security program services** for clients that hold category 2 quantities of radioactive material: drafting security plans and implementing procedures, and performing the annual security program review (10 CFR 37.55) and access authorization program review (37.33); (3) shielding design and radiation surveys; (4) a small **calibration laboratory** that calibrates portable radiation survey instruments and analyzes sealed source leak test samples; (5) supplemental health physics support at 2 nuclear power plants during refueling outages |
| Size substitution | The vertical's primary industry is nuclear power generation (NAICS 221113). A 7-person business cannot operate a reactor, so this sample uses a consulting practice that serves reactor and materials licensees. Sector rules reach it mainly through client contracts (see P03) |
| Location | Florida. One office suite in a light-industrial park, with an attached calibration laboratory (a shielded calibration room and a locked source storage cabinet). Consultants travel to client sites |
| Workforce | 7 employees: Principal Health Physicist (owner), 2 Senior Health Physicists, 1 Health Physicist, 1 Calibration Laboratory Technician, 1 Project Coordinator, 1 Office Manager |
| Clients | About 140 consulting client accounts: about 70 medical (nuclear medicine, radiation oncology, imaging), about 30 industrial (portable gauges, industrial radiography, well logging), about 25 universities and research laboratories, and others. **6 consulting clients hold category 2 quantities under 10 CFR Part 37** (2 hospital blood irradiators, 1 radiosurgery center, 2 industrial radiography companies, 1 university research irradiator); all 6 are Florida licensees. Plus **2 power reactor operators** (outage support) and about 300 calibration and leak test customers (about 1,600 calibrations and 900 leak test analyses a year) |
| Revenue | About $1.1 million a year (fictional), about $4,400 per business day. SBA-small: the standard for NAICS 541690 is $19.0 million in average annual receipts (13 CFR 121.201) |
| Revenue mix | Consulting RSO and audits 45%; Part 37 security program services 15%; shielding and surveys 15%; calibration laboratory and leak tests 15%; reactor outage support 10% |
| Radioactive materials license | **Limited Florida specific license** (Florida Department of Health, Bureau of Radiation Control, under Chapter 64E-5, F.A.C.; Florida is an NRC Agreement State, agreement effective 1964). It authorizes one sealed Cs-137 source of about 0.4 Ci (about 15 GBq) in a shielded beam calibrator, small check and reference sources, and receipt and analysis of customers' leak test samples. The Principal Health Physicist is the RSO named on the license |
| Part 37 status of its own license | **Does not apply.** Part 37 Subparts B and C apply to a person who "possesses or uses at any site, an aggregated category 1 or category 2 quantity" (37.3(a)). The category 2 threshold for Cs-137 is 1 TBq (27.0 Ci) (Part 37, Appendix A). The practice holds about 1.5% of it |
| Part 37 information it handles for clients | Copies of the 6 clients' security plans, implementing procedures, and lists of individuals approved for unescorted access, plus the annual review reports the practice writes. The clients must protect this information under 37.43(d), and their consulting contracts flow that duty down to the practice. Each client's reviewing official decides which practice staff are trustworthy and reliable and may see its information (37.43(d)(3)) |
| Reactor client terms | Practice staff working outages receive unescorted access under each plant's own access authorization program (the plant certifies access; 10 CFR 73.56(a)(4)). The contracts require staff to follow the plant's cyber security program rules for portable media and mobile devices (from each licensee's 10 CFR 73.54 program), forbid connecting practice devices to plant networks, state that the plant will not share Safeguards Information with the practice, and require notice to the plant **within 4 hours** of discovering a cyber incident that involves any device or media used at the site |
| Part 37 client contract terms | The 6 Part 37 clients' contracts (all renewed 2024-2025) require the practice to handle their security information under the client's 37.43(d) procedures, give access only to staff the client has approved, tell the client within **2 working days** when an approved person leaves or no longer needs access, return or destroy copies at the end of each engagement, and notify the client **within 24 hours** of discovering any actual or suspected unauthorized access to the client's information |
| Not in scope | **10 CFR 73.54, 73.77, 73.110** (not a power reactor licensee); **NERC CIP** (not a registered entity); **Safeguards Information** (10 CFR 73.21 reaches any person who "produces, receives, or acquires" SGI; the practice does none of these, and the reactor contracts exclude SGI); **10 CFR 73.56 contractor or vendor program** (the practice runs no access authorization program; the plants process its staff); **10 CFR Part 810 and Part 110** (no foreign work, imports, or exports); **CIRCIA** (proposed only; as proposed, the practice is below the SBA size standard and meets no sector criterion); **HIPAA** (not a covered entity; medical clients give only de-identified patient data for dose and medical event work); **federal contracts** (none, so the FAR clauses do not apply) |
| State law approach | Florida is cited as the licensing authority (Chapter 64E-5, F.A.C., and the clients' Part 37 license condition) and for breach notification (Fla. Stat. 501.171). Otherwise the samples stay federal |

### Regulatory driver IDs used in this sample
The vertical's `requirements.csv` lists power reactor and grid rules (C-NUCLEAR-R01 to R05). None applies directly to this practice (P03 section 1). As in the Small sample, this sample adds **scenario-level driver IDs (C-NUCLEAR-S01 to S06)** for the rules and contract terms that do apply. They are defined here and nowhere else; the numbering is specific to this sample.

| ID | Requirement | Citation | Status for this practice |
|---|---|---|---|
| C-NUCLEAR-R01 | NRC cyber rule for power reactors | 10 CFR 73.54 | Not applicable (cited only in P03 applicability rows and as the source of reactor contract terms) |
| C-NUCLEAR-R02 | Part 53 cyber rule | 10 CFR 73.110 | Not applicable |
| C-NUCLEAR-R03 | NRC cyber security event notifications | 10 CFR 73.77 | Not applicable (the reactor clients' own duty) |
| C-NUCLEAR-R04 | NERC CIP | 16 U.S.C. 824o; 18 CFR Part 40 | Not applicable |
| C-NUCLEAR-R05 | CIRCIA (proposed) | Proposed 6 CFR Part 226 | Not in effect; not covered as proposed |
| **C-NUCLEAR-S01** | Protection of Part 37 security information and background investigation information, flowed down by client contracts | 10 CFR 37.43(d) and 37.31, imposed on the 6 clients by their Florida license condition | **Applies by contract (primary regulation in P03)** |
| C-NUCLEAR-S02 | Florida radiation control rules for the practice's own license | Chapter 64E-5, F.A.C. | Applies to the calibration laboratory; radiation safety rules, considered but not decomposed in P03 |
| C-NUCLEAR-S03 | Reactor client contract terms derived from the plants' 10 CFR 73.54 and 73.56 programs | Client contracts | Applies by contract |
| C-NUCLEAR-S04 | NIST CSF 2.0 (with the CSF 2.0 Small Business Quick-Start Guide, NIST SP 1300) | Voluntary benchmark | Adopted by the owner as the practice's cybersecurity benchmark |
| C-NUCLEAR-S05 | Florida data security and breach notification | Fla. Stat. 501.171 | Applies to personal information (employee records, staff dose records, and client background investigation pages the practice holds) |
| C-NUCLEAR-S06 | FTC Act Section 5 | 15 U.S.C. 45(a) | Applies (unfair or deceptive practices, including security claims made to clients) |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Principal Health Physicist (owner) | Accepts risk; approves policies and spending; RSO named on the practice's license; final technical reviewer of every Part 37 deliverable |
| Office Manager | **Designated Security Officer** (in writing, 2026-08-03); billing, HR, and payroll; MSP contact; requests and removes accounts. Not approved by any client for Part 37 information |
| Senior Health Physicist (Part 37 services lead) | Leads Part 37 engagements; **custodian of client security information**: tracks which staff each client has approved |
| Senior Health Physicist (field services lead) | Leads reactor outage support and field surveys; responsible for devices and media taken to client sites |
| Health Physicist | Consulting RSO visits, audits, and surveys. Joined 2026-04-06 |
| Calibration Laboratory Technician | Runs the calibration laboratory; administrator of the calibration and leak test system (SYS-02); business owner of the AI pilot (P10) |
| Project Coordinator | Scheduling, report formatting and production, client file transfers. Not approved by any client for Part 37 information |
| Managed service provider (MSP) | Help desk, patching, antivirus, firewall and Wi-Fi, laptop encryption, and backup administration under a monthly contract |

**Approved by client reviewing officials for Part 37 information (37.43(d)(3)):** 4 staff. The owner and the Part 37 services lead are approved by all 6 clients, the field services lead by 3, and the Health Physicist by 2 (approval pending at the other 4).

**Where roles overlap.** The owner is the RSO, the risk acceptor, and the final reviewer of client deliverables. The Office Manager runs day-to-day security while also doing billing and HR. Compensating checks: the MSP's monthly report, client reviewing officials' own access decisions, and an independent consultant for the control assessment (P07).

## 3. Systems

| ID | System | Hosting | Sensitive data | Notes |
|---|---|---|---|---|
| SYS-01 | Productivity suite (email, calendar, file storage and sharing, chat) | SaaS | Yes: client security information, client reports, personnel records | MFA enforced (push approval); one "Clients" shared library readable by all 7 staff; "anyone with the link" sharing allowed |
| SYS-02 | Calibration and leak test management system | Vendor SaaS | Yes: client instrument inventories, calibration and leak test results, certificates; the practice's own source inventory | MFA only for the 2 administrators; vendor has a SOC 2 Type 2 report (P09); vendor's calibration drift prediction module piloted since 2026-05-04 (P10) |
| SYS-03 | Accounting, invoicing, and payroll service | SaaS | Yes: employee personal information, client billing | MFA enforced |
| SYS-04 | Endpoints: 7 laptops and 2 calibration laboratory workstations | MSP-managed | Yes (synced and cached files) | Laptops encrypted; lab workstations not encrypted; lab workstation 2 runs an operating system version past end of support, because the gamma spectroscopy software is certified only on it. Staff also carry USB drives to client sites; 4 of them are personal |
| SYS-05 | Office network: small-business firewall, staff Wi-Fi, guest Wi-Fi | On-premises, MSP-managed | In transit | Guest Wi-Fi separated; firewall managed with one shared MSP login without MFA |
| SYS-06 | SaaS-to-SaaS backup of the productivity suite (mail and files) | SaaS, operated by the MSP | Yes | 30 days of versions; never restore-tested |
| SYS-07 | Calibration laboratory instruments: beam calibrator controller, reference electrometer, gamma spectroscopy system | On-premises | No personal data; measurement results | Connected to the lab workstations by USB and serial cables; results entered into SYS-02 the same day |
| SYS-08 | Dosimetry processor web portal | Vendor SaaS | Yes: staff occupational dose records | NVLAP-accredited processor (10 CFR 20.1501(d)); password only |

**SSP system (P02):** the *Practice Business Platform (PBP)*: SYS-01 to SYS-07 (the dosimetry portal, SYS-08, is an external service outside the boundary).

## 4. Current security posture: early to partial

**In place today:**
- MFA on the productivity suite and the accounting and payroll service
- MSP patching, antivirus, and firewall for laptops and the office network
- Full-disk encryption on all 7 laptops
- Nightly SaaS-to-SaaS backup of the productivity suite
- Client reviewing officials' trustworthiness and reliability approvals for 4 staff, with approval letters on file for 4 of the 6 clients
- Reactor plant access training and fitness-for-duty processing for outage staff (run by the plants)
- Guest Wi-Fi separated from staff Wi-Fi
- A cyber liability insurance policy with a breach hotline and panel vendors
- A two-page "IT rules" memo from 2021

**Missing or weak, found in the 2026 assessments:**
1. The 6 Part 37 clients' security plans, implementing procedures, and approved-individual lists sit in the general "Clients" library, readable by all 7 staff. The Office Manager and Project Coordinator have never been approved by any client. Copies also sit in mailboxes and in files synced to laptops.
2. There is no written procedure for handling client security information and no list of which staff each client has approved.
3. 14 "anyone with the link" sharing links were open, 2 of them to folders holding a client's Part 37 documents (removed 2026-08-05).
4. A Health Physicist who resigned on 2026-02-13 kept an active SYS-02 account until 2026-08-04, and the 2 clients that had approved him were not told he had left until 2026-08-05.
5. In June 2026 a consultant pasted part of a client's implementing procedure into a public AI chatbot to reformat it. There is no approved-tools list for AI.
6. During a 2025 access authorization program review, a consultant photographed 3 pages of a client's background investigation file (including a copy of a driver license) as sample evidence. The photos sit in the "Clients" library.
7. Staff carry USB drives to client sites, 4 of them personal. On 2026-04-14 a reactor client's portable media kiosk quarantined malware on a staff member's personal USB drive. The practice kept no record beyond an email and did not examine the laptop.
8. MFA is not enforced on SYS-02 for 5 of 7 users, on the dosimetry portal, or on the MSP's firewall login.
9. The lab workstations are unencrypted and excluded from patching; lab workstation 2 runs an unsupported operating system.
10. The productivity suite backup has never been restore-tested, and nobody has exported the SYS-02 records.
11. No risk assessment, no adopted policies (only the 2021 memo), no incident response plan, and no tracking of client notification clocks (24 hours for Part 37 clients, 4 hours for reactor clients).
12. No security awareness training beyond what the reactor plants give outage staff.
13. No inventory of devices, SaaS services, or where client security information lives.
14. No vendor review; the MSP contract has no security or incident notice terms.
15. Older staff dose reports from the dosimetry processor (before 2023) list full Social Security numbers and sit in the "Admin" library.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P03 regulation | 10 CFR 73.54 recorded as not applicable, with the other reactor rules. Primary analysis: the 10 CFR Part 37 information protection duties (37.43(d), 37.31, plus the review and event-reporting provisions the practice supports) as flowed down by the 6 client contracts. Also analyzed: reactor client contract terms, Fla. Stat. 501.171(2) and (8), and a NIST CSF 2.0 benchmark for the practice's own program |
| P08 incident | **Adapted.** Registry default: cyber attack on a plant business network with an attempted pivot to digital assets. The practice has no plant. The adapted incident: a phished consultant account on the practice's business systems, with attempted pivots to client digital assets (malware on media headed for a reactor outage, and malicious documents sent from the trusted mailbox to Part 37 clients), plus access to client security information. MSP and cyber insurer in the notification chain |
| P09 SOC 2 | The practice is not a SOC 2 service organization. (a) Security plus **Confidentiality** readiness self-assessment, used to answer a Part 37 client's vendor security questionnaire (due 2026-10-30); (b) review of the SYS-02 vendor's SOC 2 Type 2 report |
| P10 AI | **Adapted.** Registry default: predictive maintenance for non-safety plant equipment. The practice owns no plant equipment. The closest real use is the SYS-02 vendor's machine-learning **calibration drift prediction** module, which predicts which client survey instruments are likely to fail their next calibration (pilot since 2026-05-04) |
| Cloud | SaaS plus one cloud workload: the SaaS-to-SaaS backup (SYS-06). Vendor-agnostic |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-08-03 to 2026-08-14 | Business impact analysis, risk assessment, and gap analysis (Office Manager and Part 37 services lead, with the MSP lead technician) |
| 2026-08-24 to 2026-08-26 | Control assessment by an independent cybersecurity consultant (on site 2026-08-25) |
| 2026-09-15 | Deliverables approved by the Principal Health Physicist (owner) |
