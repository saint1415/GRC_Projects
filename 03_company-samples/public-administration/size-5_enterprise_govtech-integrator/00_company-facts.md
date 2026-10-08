# Scenario facts: Cris Santos Company | Public Administration | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency customers. This scenario is independent of the other sizes. Where a fact comes from a regulation, policy, or standard, the citation is given.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; a GovTech systems integrator, not a government entity) |
| Business | GovTech systems integrator (NAICS 541512, Computer Systems Design Services) serving state and local agencies, in four segments: **State and Local Platforms** hosts the Agency Case Management Cloud (ACMC), a multi-tenant case management service (about 38% of revenue); **Eligibility and Enrollment Operations** builds and operates integrated eligibility systems (IES) for state human services agencies, with document processing and contact center staff (about 27%); **Systems Integration** delivers implementations, data migration, legacy managed hosting, and staff augmentation (about 29%); **Federal Programs** delivers IT modernization services to federal civilian agencies and one Department of Defense (DoD) subcontract (about 6%) |
| Location | Headquartered in Florida. Delivery centers in Florida, Georgia, North Carolina, Ohio, and Virginia, plus remote staff. Agency customers in 16 states. All work on agency data, including support and administration, is performed in the United States. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 4,100 engineers and developers, 2,300 cloud, IT, and security operations staff, 2,600 implementation consultants and business analysts, 1,500 eligibility operations staff (document processing and contact centers), and 1,500 corporate staff. About 3,400 staff can reach criminal justice information (CJI), about 1,900 can reach federal tax information (FTI), and about 2,200 work on site at agency facilities |
| Revenue | About $4.8 billion a year (fictional): about $13.2 million per calendar day, or about $18.5 million per business day. Not small under the SBA standard for NAICS 541512 ($34.0 million; 13 CFR 121.201) |
| Customers | About 145 state and local agency customers in 16 states (see the customer table below). About 41 million individuals have records across the company's platforms |
| Regulatory status | The company is a **private contractor**. Data-owner rules reach it **through its contracts**: the FBI CJIS Security Policy through the CJIS Security Addendum (28 CFR 20.33(a)(7)), IRS Publication 1075 through Exhibit 7 contract language (26 CFR 301.6103(n)-1), the HIPAA Security Rule through a business associate agreement with one Medicaid agency (45 CFR 164.302; 164.314(a)), Medicaid and SNAP confidentiality through contract terms (42 CFR 431.300-431.307; 7 CFR 272.1(c)), and Florida Rule 60GG-2, F.A.C. through state agency contracts (Fla. Stat. 282.318(4)(h)). Every agency contract requires the NIST SP 800-53 Rev. 5 Moderate baseline for hosted systems. Some rules bind the company **directly**: the Driver's Privacy Protection Act reaches contractors of a state motor vehicle department (18 U.S.C. 2721(a)); SEC disclosure rules apply as a registrant; and Fla. Stat. 501.171 applies as a third-party agent |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls; GovRAMP (formerly StateRAMP) verification for ACMC; federal contract clauses (FAR 52.204-21; DFARS 252.204-7012 on the DoD subcontract; CMMC under 32 CFR Part 170); growth by acquisition (a court e-filing software company, AQ-1, acquired in December 2025) |
| Not in scope | FedRAMP: no federal agency uses ACMC or IES today, so FedRAMP authorization is not required (the company uses FedRAMP Moderate authorized cloud services, which Pub. 1075 requires for FTI). Election systems: none. SLCGP: a grant condition on recipient governments, not on the company. CIRCIA: proposed rule only. The company's employee health plan is a separate covered entity outside these deliverables |
| State law approach | Florida law is cited where a Florida duty is unavoidable (Rule 60GG-2 and Fla. Stat. 282.318 for Florida state agency customers, Fla. Stat. 282.3185 and 282.3186 for Florida local government customers, and Fla. Stat. 501.171). Other states are handled generically: "each state where affected individuals reside," with counsel's state matrix |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

**Agency customers (fictional)**

| ID | Customer | Platform and use | Regulated data | How requirements reach the company |
|---|---|---|---|---|
| AG-01 | A Florida state revenue agency | ACMC: tax compliance casework (audit follow-up, collections, taxpayer correspondence) | **FTI** received under IRC 6103(d), plus state tax data. About 2.4 million taxpayer case records | Contract with Pub. 1075 Exhibit 7 language; the agency's 45-day notification to the IRS names the company and its cloud provider (Pub. 1075 Exhibit 6); SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AG-02 | A Florida county sheriff's office | ACMC: pretrial services and probation supervision | **CJI** including criminal history record information (CHRI). About 84,000 supervision records | Contract with the CJIS Security Addendum; CJISSECPOL v6.1 (06/25/2026); SP 800-53 Moderate |
| AG-03 | A Florida state human services agency | IES operated by the company (SYS-03) for SNAP, TANF, and Medicaid eligibility; AI eligibility assistant pilot (AI-001) | Applicant and household data, Social Security numbers, income documents. About 4.9 million individuals. **FTI is prohibited** in the environment (see below) | Contract terms reflecting 7 CFR 272.1(c) and 42 CFR 431.300-431.307; SP 800-53 Moderate; Rule 60GG-2 contract terms |
| AG-04 | An out-of-state human services and Medicaid agency | IES plus Medicaid enrollment and premium processing support | Applicant data and Medicaid enrollee data (**ePHI**: the agency's Medicaid program is a health plan). About 3.8 million individuals | Business associate agreement (45 CFR 164.314(a)(2)(i)); contract terms for 42 CFR 431.300-431.307 and 7 CFR 272.1(c); SP 800-53 Moderate |
| AG-05 | An out-of-state motor vehicle agency | ACMC: driver license hearings, suspensions, and reinstatement casework | Motor vehicle record personal information, including **highly restricted personal information** (photographs, Social Security numbers, medical or disability information; 18 U.S.C. 2725(4)). About 1.6 million driver records | DPPA applies directly to the agency's contractors (18 U.S.C. 2721(a)); contract; SP 800-53 Moderate |
| AG-06 | An out-of-state state court system | Legacy managed hosting (SYS-09, DC-1) of the court case management system; e-filing through the AQ-1 platform (SYS-15) | Criminal case records (CJI), sealed and juvenile records. About 6.2 million case records | CJIS Security Addendum; contract; SP 800-53 Moderate |
| Portfolio | 5 other state revenue agencies (ACMC, FTI); 22 other criminal justice agencies (14 on ACMC, 8 on legacy hosting; CJI); 2 other state human services agencies (IES); about 108 counties and cities (ACMC constituent services, permits, code enforcement) | | | |

Customer counts: 6 state revenue agencies, 24 criminal justice agencies, 4 state human services agencies, 1 motor vehicle agency, and about 110 local governments: about 145 in total. About 40 customers are in Florida (AG-01, AG-02, AG-03, and about 37 counties and cities).

**Why FTI is prohibited in the IES environments.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (Pub. 1075 section 2.C.11.2; Exhibit 6). Each IES contract forbids FTI in the environment. The agencies keep IRS income match results in their own systems.

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (audit committee; risk committee) | Cyber risk oversight; the risk committee receives the CISO's quarterly report (Item 106 governance); the audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Information Security Officer (CISO) | Security program owner; reports to the CEO and quarterly to the board risk committee |
| Chief Privacy Officer | Privacy program; breach determinations; privacy contact under the AG-04 business associate agreement |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee |
| Chief Compliance Officer | Regulatory and contract compliance program (second line, with the GRC team) |
| Director of Regulated Data Compliance | Runs the CJIS and Pub. 1075 program for all agency contracts; company liaison to agency security officers; **HIPAA security official** for the AG-04 business associate scope (45 CFR 164.308(a)(2)) |
| GRC team (14), Security Operations Center (24x7, in-house, two sites), Internal Audit (6 IT auditors, co-sourced for specialist testing) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |
| AI governance committee | Formed in 2025; chaired by the Chief Data and AI Officer; reviews every AI use case before production |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Agency Case Management Cloud (ACMC), production | Multi-tenant case management service on Cloud provider A (two U.S. regions, active and standby), using FedRAMP Moderate authorized services. About 132 agency tenants (all customers except the 4 IES agencies and the 9 legacy hosting customers), about 31,000 agency user accounts, and about 22 million individuals' records. The 6 FTI tenants run on dedicated database instances with customer-managed keys; CJI tenants share a cluster with row-level tenant separation |
| SYS-02 | Integration hub | About 640 interfaces: state message switches (CJI), revenue agency file transfers (FTI), motor vehicle systems, court systems. Cloud services plus an on-premises edge in colocation DC-1 that terminates 31 site-to-site VPN tunnels to agency sites |
| SYS-03 | Integrated eligibility system (IES) environments | Four single-tenant environments (AG-03, AG-04, and two other states) on Cloud provider B, using FedRAMP Moderate authorized services in U.S. regions. About 14 million individuals. No FTI |
| SYS-04 | Enterprise identity platform | Single sign-on, MFA (phishing-resistant security keys for privileged users), privileged access management (PAM), identity governance. AQ-1 is not yet federated |
| SYS-05 | Corporate applications | Productivity suite, ERP and financials (SOX-relevant), HR and payroll, CRM |
| SYS-06 | Software delivery platform | Source repositories, CI/CD pipelines, artifact registry, code and dependency scanning, image signing |
| SYS-07 | Security operations platform | SIEM, EDR, SOAR, vulnerability and cloud posture management; 24x7 in-house SOC |
| SYS-08 | Endpoints | About 14,800 company laptops with full-disk encryption and EDR. About 2,200 staff also use agency-furnished devices at agency sites |
| SYS-09 | Colocation data centers DC-1 (Florida) and DC-2 (out of state) | Legacy managed hosting for 9 customers (AG-06, 4 other courts, and 4 sheriffs' records systems): about 410 servers; the integration hub edge; offline backup vault copies |
| SYS-10 | CUI enclave (Federal Programs) | A separate cloud environment for the DoD subcontract, using FedRAMP Moderate authorized services (DFARS 252.204-7012(b)(2)(ii)(D)); about 140 users |
| SYS-11 | Data and AI platform | Analytics for IES reporting, machine learning services, and a managed large language model service; 12 AI use cases (P10) |
| SYS-12 | Customer support and contact center | Ticketing (SaaS) and telephony; a subcontracted tier-1 help desk for municipal customers |
| SYS-13 | Non-production environments | Development, test, and staging accounts for ACMC, IES, and AQ-1 |
| SYS-14 | Third parties | About 1,450 vendors; 214 with access to agency data or systems; 41 subcontractors whose staff can reach FTI or CJI |
| SYS-15 | AQ-1 court e-filing platform | Acquired 2025-12 (about 420 employees). Runs in its own Cloud provider A account with its own identity directory; e-filing for 9 courts including AG-06; connected to the integration hub by network peering. Integration due 2027-06-30 |

The cloud providers are described by service category only (vendor-agnostic). The services used for ACMC, IES, and the CUI enclave are FedRAMP Moderate authorized and run in U.S. regions (checked on the FedRAMP Marketplace in June 2026), as Pub. 1075 section 3.3.1 requires for FTI.

**SSP system (P02):** the *Agency Case Management Cloud (ACMC)*: SYS-01 and SYS-02, with the ACMC non-production accounts in SYS-13, inheriting common controls from the enterprise identity platform (SYS-04), software delivery platform (SYS-06), security operations (SYS-07), and the Cloud provider A landing zone.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with an annual risk assessment tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 in-house SOC with SIEM, EDR, and SOAR
- PAM with just-in-time elevation for ACMC and IES administrators; quarterly access certification
- Phishing-resistant MFA for privileged users; MFA for all workforce users
- Immutable backups in separate accounts for ACMC and IES; annual DR tests for tier-1 systems
- A dedicated CJIS and Pub. 1075 compliance function; agency-led CJIS audits and IRS safeguard reviews passed in 2025 with minor findings
- An annual SOC 2 Type 2 report for ACMC since 2024 (Security, Availability, Confidentiality); GovRAMP Authorized status for ACMC since 2025
- Tiered third-party risk management
- SEC Item 106 disclosure in the 10-K; SOX IT general controls tested annually

**Targeted gaps:**
1. **Acquisition (AQ-1).** AQ-1 runs its own identity directory and cloud account, keeps logs 90 days outside the SIEM, and gives 31 engineers standing administrator rights. Its network peering reaches the integration hub. 39 of the 118 AQ-1 staff who can reach court CJI have no fingerprint-based check or signed CJIS Security Addendum certification.
2. **Legacy hosting (SYS-09).** 64 of about 410 servers run unsupported operating systems on a flat management network; backups are not immutable. 7 site-to-site VPN appliances at the integration hub edge still use FIPS 140-2 modules on CJI paths; CJISSECPOL v6.1 SC-13 does not accept FIPS 140-2 certificates after 2026-09-21.
3. **Third parties and subcontractors.** The help desk vendor's overnight tier, located outside the United States, could view tickets from FTI tenants. 2 subcontractors that support FTI tenants are not covered by the agencies' IRS notifications. 31 tier-1 vendor reviews are overdue.
4. **Independence.** The 2025 ACMC control assessment was performed by the GRC team, which also designs the controls. Internal Audit has 6 IT auditors for an enterprise of this size.
5. **Disclosure readiness.** The SEC materiality playbook does not weigh harm that falls mainly on agency customers (contract termination, public trust), and the disclosure committee has not exercised since 2025-04. Two of its seven members joined in 2026.
6. **Recovery of eligibility systems.** The AG-04 IES recovered in 14 hours against an 8-hour contract RTO in the 2026 DR test.
7. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. The AI eligibility assistant pilot (AI-001) has bias testing only on English-language test data, and caseworkers accept most of its suggestions.
8. **Federal readiness.** The CUI enclave has 6 open NIST SP 800-171 requirements on its plan of action, and no CMMC Level 2 (C3PAO) assessment is scheduled. The prime's expected Level 2 (C3PAO) requirement for the 2027-04-01 option is suspended with CMMC Phase 2 (the DoD (Department of War) CIO memorandum of 2026-07-13; DoD Class Deviation 2026-O0025, Revision 3), but SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 regulation | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline required by every agency contract, with the CJIS Security Policy v6.1 and IRS Pub. 1075 (Rev. 11-2021) overlays, plus every other rule that applies across the enterprise (HIPAA as a business associate, Medicaid confidentiality, DPPA, SEC, Florida law as the worked example, federal contract clauses) |
| P08 incident | Ransomware affecting agency systems holding CJI and FTI: entry through AQ-1, spread over the network peering into the integration hub and legacy hosting, encryption of court and sheriff systems, and theft of staged revenue agency files. Includes the **SEC materiality assessment and Form 8-K Item 1.05** step and a multi-agency, multi-state notification workflow |
| P09 SOC 2 | SOC 2 Type 2 readiness across two service lines offered to agencies: SL-1 ACMC and SL-2 IES operations |
| P10 AI | Enterprise AI portfolio (12 use cases) with the AI governance committee; full assessment of AI-001, the AI eligibility assistant. The registry default "AI eligibility determination for public benefits" is adapted to **decision support**, because SNAP certification must be done by state merit staff (7 CFR 272.4(a)(2)) and the Medicaid agency determines eligibility (42 CFR 431.10) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls, plus two colocation data centers |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk assessment and regulatory gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment of ACMC (Internal Audit with a co-sourced firm) |
| 2026-09-10 | Results to the board risk committee and audit committee |

## 7. Facts added for the Phase 5 deliverables

These facts were added while building the deliverables. They do not change sections 1-6.

**People and committees (P08, P09, P10)**
- **Crisis management team:** chaired by the President, State and Local Platforms (backup: President, Systems Integration), with the four segment presidents, CIO, CISO, General Counsel, Chief Privacy Officer, Chief Human Resources Officer, Director of Regulated Data Compliance, Vice President, Corporate Communications, and Vice President, Investor Relations.
- **Disclosure committee (seven members):** General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Chief Privacy Officer, and Vice President, Investor Relations; outside securities counsel advises. The General Counsel records materiality determinations.
- **AI governance committee members:** Chief Data and AI Officer (chair), CISO, Chief Privacy Officer, Chief Compliance Officer, the General Counsel's delegate, Chief Human Resources Officer, the presidents of Eligibility and Enrollment Operations and of State and Local Platforms (or delegates), Director of Regulated Data Compliance, and a civil rights and accessibility lead; Internal Audit observes. High-tier AI use cases also need executive risk committee approval (POL-01 4.4).
- **Other role titles used:** Deputy CISO; Deputy General Counsel; Federal Programs security lead; regulated data compliance managers (one per program); Director of Eligibility Operations (contact centers and document processing).

**Incident readiness (P08)**
- Last ransomware exercise: a technical exercise on 2026-05-21 with the SOC, cloud platform, and data center teams; no disclosure committee or agency contacts took part.
- Printed incident binders are kept at headquarters, both SOC sites, and each delivery center.
- Legacy hosting has a weekly offline vault copy in DC-2 (the "offline backup vault copies" in SYS-09); until POAM-008 closes it is the only legacy backup an attacker cannot reach.

**SOC 2 (P09)**
- ACMC SOC 2 Type 2 reports cover calendar years; the 2026 report is due in 2027-02. P09 prepares the 2027 period (2027-01-01 to 2027-12-31). Readiness summary prepared 2026-09-25.
- IES contracts require an independent assurance report for the operation; the 2027 renewals of the two out-of-state IES agencies name a SOC 2 Type 2 report with Processing Integrity. SL-2's first Type 2 period is 2027-04-01 to 2027-09-30, with the report expected in 2027-11.
- IES document processing: second-person verification of 5% of indexed pages each day; intake error queues reviewed each shift. A daily reconciliation of notices generated against notices mailed runs for AG-03 only.

**AI portfolio (P10)**
- The 12 use cases are AI-001 to AI-012 in P10 `ai-use-case-inventory.csv`; 8 reviewed by the committee; AI-005, AI-009, AI-010, and AI-012 unreviewed (due 2026-12-31). Tiers: 4 High, 5 Medium, 3 Low.
- AI-001 pilot: committee intake approval 2026-02-18 without a risk assessment; live since 2026-03-02 for 120 AG-03 caseworkers in one region; about 31,000 applications March to July 2026. Validation: AG-03 quality control re-worked 600 cases blind (54 wrong suggestions; caseworkers caught 22). P10 fieldwork 2026-07-06 to 2026-08-14; committee review 2026-08-19; executive risk committee decision 2026-09-10.
- AI-005 (call analytics) was switched on in a 2026-05 vendor release; AI-010 (redaction suggestions) came with AQ-1; AI-012 ranking was disabled on 2026-08-24. New intake gates for vendor AI features and acquisitions take effect 2026-10-01.
- AI-003 serves 41 local government tenants; AI-004 runs in 2 states; AI-007 is used by about 3,900 engineers.

**Corrections made while finishing the deliverables:** the SSP (P02 section 10.2) now states 46 assessed controls, matching P07; STD-05.3 Approved AI Tools List is owned by the Chief Data and AI Officer (P06 `policy-hierarchy.md`).
