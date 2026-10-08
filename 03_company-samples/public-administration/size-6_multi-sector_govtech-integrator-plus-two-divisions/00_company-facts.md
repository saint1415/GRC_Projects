# Scenario facts: Cris Santos Company | Public Administration | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious, and so are its agency, federal, and local government customers. This scenario is independent of the other sizes. Where a fact comes from a regulation, policy, standard, or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23), govinfo.gov, and the primary sources named in `02_industry-rules/` between 2026-09-25 and 2026-10-06.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; a private contractor to government, not a government entity) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a wholly owned operating subsidiary under common ownership |
| Division 1: GovTech Integration (NAICS 541512; serves Public Administration, sector 92), **focus of this scenario** | Builds, hosts, and operates case management, integrated eligibility, and motor vehicle systems for state and local agencies, and sells implementation, data migration, and integration services. About 19,000 employees. About 1,150 active agency contracts in 34 states |
| Division 2: IT Consulting (NAICS 541611, sector 54 Professional, Scientific, and Technical Services) | Management and IT advisory, program management, and systems modernization consulting for state and local agencies (about 60% of division revenue), federal civilian agencies (about 25%), the Department of Defense (about 10%), and public hospitals and county health departments (about 5%). About 14,000 employees, including about 2,800 who joined with a consulting firm acquired on 2025-07-01 |
| Division 3: Government Software Products (NAICS 513210, sector 51 Information) | Publishes three software-as-a-service products for government: the *Civic Suite* (permitting, licensing, code enforcement, 311, and utility billing for local governments), a *Public Safety Records Management System* (RMS) for law enforcement agencies, and a *Grants Management* service whose federal edition holds a FedRAMP Moderate authorization. About 7,000 employees |
| Corporate shared services | Identity, network, cloud platform, security operations, HR, finance, legal, procurement, and internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Employees in 41 states; customers in 46 states and the District of Columbia. All work on agency, federal, and customer data, including support and administration, is performed in the United States by U.S.-based staff. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional) |
| Ownership | Public shareholders. As an SEC registrant the group files Form 8-K Item 1.05 for material cybersecurity incidents and makes the annual Regulation S-K Item 106 disclosure |
| SBA size status | Not small (SBA standard for NAICS 541512 is $34.0 million in average annual receipts, 13 CFR 121.201) |
| How agency rules reach the group | The group is a **private contractor**. The federal data-owner rules bind the agencies and reach the group **through its contracts**: IRS Publication 1075 through Exhibit 7 contract language (26 CFR 301.6103(n)-1), the FBI CJIS Security Policy through the CJIS Security Addendum (28 CFR 20.33(a)(7)), Medicaid and SNAP confidentiality through contract terms (42 CFR 431.300-431.307; 7 CFR 272.1(c)), and state security standards through each state's IT contract terms (Florida worked example: Rule 60GG-2, F.A.C. through Fla. Stat. 282.318(4)(h)). The Driver's Privacy Protection Act binds the group directly as a contractor of state motor vehicle departments (18 U.S.C. 2721(a)). Almost every agency contract requires the NIST SP 800-53 Rev. 5 Moderate baseline for hosted systems |
| Florida data security duty (worked example) | For Florida customers the group is a "third-party agent" under Fla. Stat. 501.171(1)(h): it must take reasonable measures to protect personal information (501.171(2)) and notify the agency of a breach no later than 10 days after determining it (501.171(6)(a)). Other states' laws are applied the same way for customers in those states |
| Federal contract status | IT Consulting holds about 140 federal civilian contracts with FAR 52.204-21 and 58 DoD contracts and subcontracts with DFARS 252.204-7012 (controlled unclassified information, CUI). Government Software Products holds a FedRAMP Moderate authorization (agency authorization, 2024) for the federal edition of Grants Management. GovTech Integration holds no federal contracts |

**GovTech Integration customer groups (fictional)**

| ID | Customer group | Systems used | Regulated data | How requirements reach the group |
|---|---|---|---|---|
| CG-REV | 7 state revenue agencies (one is Florida's) | ACMP tax compliance module, each in a dedicated tenant | **Federal tax information (FTI)** received by the agencies from the IRS under IRC 6103(d), plus state tax data. About 14.0 million taxpayer case records | Contracts with Pub. 1075 Exhibit 7 language; each agency's IRS 45-day notification names the group and its cloud providers (Pub. 1075 Exhibit 6; 26 CFR 301.6103(n)-1); SP 800-53 Moderate |
| CG-CJ | 212 criminal justice agencies (sheriffs, police, pretrial, probation, and courts) in 11 states, under 11 state CJIS Systems Agencies (CSAs). 46 are in Florida | ACMP supervision and court case modules in the CJI cluster | **Criminal justice information (CJI)**, including criminal history record information (CHRI). About 4.6 million case records | Contracts incorporating the CJIS Security Addendum (28 CFR 20.33(a)(7)); CJISSECPOL v6.1 (06/25/2026); SP 800-53 Moderate |
| CG-LOC | 211 counties and cities in 19 states (58 in Florida) | ACMP constituent services and code enforcement modules | Names, addresses, phone numbers, some driver license numbers. About 9.1 million constituent records | Contract security terms (SP 800-53 Moderate by reference) |
| CG-HS | 4 state human services agencies (Florida's and three others) | Integrated Eligibility Platform (IEP) for SNAP, TANF, and Medicaid, including the AI eligibility assistant in 2 states | Applicant and household data, Social Security numbers, income documents. About 11.5 million individuals. **FTI is prohibited** on the IEP | Contract confidentiality terms reflecting 7 CFR 272.1(c) and 42 CFR 431.300-431.307; **business associate agreements** with 2 state Medicaid agencies whose health care components include the eligibility functions (45 CFR 164.105; 160.103); SP 800-53 Moderate |
| CG-MV | 3 state motor vehicle departments (not Florida's) | Motor Vehicle Services Platform (MVSP) | Driver and vehicle records, including highly restricted personal information (photographs, Social Security numbers). About 22 million records | **Driver's Privacy Protection Act** applies directly to the group as a contractor (18 U.S.C. 2721(a)); contract terms |

**Why FTI is prohibited on the IEP.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (Pub. 1075 section 2.C.11.2; Exhibit 6). The IEP contracts forbid FTI; each agency keeps IRS income match results in its own systems.

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and AI risk oversight; approves group policies; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC reporting |
| Disclosure committee | SEC materiality determinations (Form 8-K Item 1.05) |
| Group CISO | Group security program, group policies, common controls (SYS-G1 to SYS-G3); co-accepts High risks |
| Group Chief Risk Officer | Group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Data classification, privacy, and state breach laws across divisions |
| Group General Counsel | Contracts, the group notification matrix, SEC and customer notices |
| Group public sector compliance director | Tracks CJIS Security Addendum, Pub. 1075 Exhibit 7, DPPA, and state contract security terms across all divisions; owns the agency contract obligations register; reports to the Group General Counsel |
| Division presidents (3) | Accept Moderate risks for their division. The IT Consulting president is the **CMMC Affirming Official** for the division's CAGE codes (32 CFR 170.22) |
| GovTech division CISO | GovTech security and compliance lead; division register, supplement, CJIS and IRS review liaison; accepts Low risks |
| IT Consulting security and compliance lead | Division register and supplement; HIPAA Security Official for the division's business associate engagements; CUI enclave security |
| IT Consulting federal contracts compliance officer | FAR 52.204-21 and DFARS 252.204-7012 compliance, SPRS submissions, subcontract flowdown |
| Government Software Products security and compliance lead | Division register and supplement; SOC 2, GovRAMP, and FedRAMP programs |
| GovTech HIPAA Security Official | Designated for the group's business associate work on the IEP (Medicaid) |
| GovTech personnel security manager | CJIS fingerprint-based checks, Security Addendum certification pages, and Pub. 1075 background investigations for GovTech staff |
| Group SOC director | 24x7 SOC; incident commander for incidents in shared services |
| Group cloud platform director | System owner of SYS-G3; common control provider |
| Group identity director | System owner of SYS-G1; common control provider |
| ACMP platform director (GovTech) | **System owner of the SSP system** (ACMP) |
| Group AI council | Approves High-tier AI use cases under the Group AI Standard (P10) |
| Group internal audit | Independent assessor: reports to the board audit committee, neither designs nor operates the controls; assesses common controls once and samples division controls (P07) |
| Agency counterparts (customer roles) | Revenue agency disclosure officers; criminal justice agency local agency security officers (LASOs) and state CJIS Systems Officers (CSOs); human services information security managers; Medicaid agency privacy officers; motor vehicle department records custodians |

## 3. Systems
| ID | System | Owner | Regulated data |
|---|---|---|---|
| SYS-G1 | Group identity platform: workforce single sign-on, MFA, privileged access management (PAM), identity governance | Corporate | Identities only |
| SYS-G2 | Group SOC (24x7, in-house), SIEM in provider A's government-community region, and endpoint detection and response (EDR) | Corporate | Log content can include fragments of CJI and FTI |
| SYS-G3 | Group cloud platform: a government-community landing zone in provider A (FedRAMP High authorized services) for regulated workloads, a commercial landing zone in provider B (FedRAMP Moderate authorized services) for other workloads, the immutable backup vault in provider B, CI/CD, and secrets management | Corporate | Yes (hosting) |
| SYS-G4 | Corporate SaaS: productivity suite, HR information system, ERP and finance, and the IT service management (ticketing) system | Corporate | Incidental |
| SYS-D1 | **Agency Case Management Platform (ACMP)**: multi-tenant case management with tax compliance, supervision and court, and constituent services modules; integration gateway; agency sign-in | GovTech Integration | FTI (7 dedicated tenants); CJI (CJI cluster); constituent data |
| SYS-D2 | Integrated Eligibility Platform (IEP) for SNAP, TANF, and Medicaid, including the AI eligibility assistant | GovTech Integration | Benefits applicant data; Medicaid PHI for 2 states |
| SYS-D3 | Motor Vehicle Services Platform (MVSP) | GovTech Integration | Motor vehicle records (DPPA) |
| SYS-D4 | Consulting delivery environment: project workspaces, data migration toolkit, client access gateway; plus the acquired firm's separate identity provider, VPN, and endpoint management until migration | IT Consulting | Client data incidentally; FCI |
| SYS-D5 | CUI enclave for DoD engagements, in provider A's government-community landing zone | IT Consulting | CUI |
| SYS-D6 | Civic Suite SaaS (multi-tenant) | Government Software Products | Constituent and permit data |
| SYS-D7 | Public Safety RMS SaaS (multi-tenant), including on-premises connectors at agencies | Government Software Products | CJI |
| SYS-D8 | Grants Management federal edition (FedRAMP Moderate authorized) | Government Software Products | Federal data |

**SSP system (P02):** the *Agency Case Management Platform (ACMP)*: the GovTech Integration division's multi-tenant case management service (SYS-D1) hosted for about 430 state and local agency tenants, including its FTI tenants, CJI cluster, integration gateway, agency sign-in, non-production environments, backups, and logging, which inherits common controls from SYS-G1, SYS-G2, and SYS-G3.

The cloud providers are described by service category only (vendor-agnostic). Every service the ACMP uses is FedRAMP authorized and runs in U.S. regions, as Pub. 1075 section 3.3.1 requires for FTI.

## 4. Current security posture: a defined program that varies by division
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements, and a common control catalog
- 24x7 group SOC, SIEM, and EDR on all group-managed endpoints and cloud workloads (not yet on the acquired consulting firm's estate)
- Single sign-on with MFA for all workforce users on SYS-G1; phishing-resistant hardware keys and just-in-time PAM elevation for administrators
- Quarterly access certification for group and division applications
- Immutable backups of regulated workloads in provider B
- GovTech: state CSA CJIS audits passed in 9 of 11 states since 2024 (2 with findings closed); IRS Office of Safeguards on-site reviews of 3 revenue agencies that included the group's facilities, with no open findings against the group; SOC 2 Type 2 for the ACMP (Security, Availability, Confidentiality; 12 months ending June 30)
- Government Software Products: SOC 2 Type 2 for the Civic Suite and the RMS; GovRAMP verification of the Civic Suite at the Authorized status; FedRAMP Moderate authorization of the Grants Management federal edition
- IT Consulting: a CUI enclave with an SP 800-171 Basic self-assessment posted in SPRS
- Board risk committee oversight; SEC Reg S-K Item 106 disclosure; annual group internal audit of common controls

**Gaps found in the 2026 assessments:**
1. **Shared-service staff screening.** About 860 corporate shared-service staff (SOC analysts, cloud platform engineers, identity administrators, backup operators) hold technical access to environments holding CJI or FTI. Screening is tracked by each division for its own staff, not for corporate. 212 of the 860 lack a fingerprint-based check or Security Addendum certification for one or more of the 11 states, and 96 of those with FTI-environment access lack a Pub. 1075 background investigation.
2. **Log retention for FTI systems.** ACMP application audit logs for FTI tenants are archived for 7 years, but the common control logs (cloud control plane, identity, and EDR) are kept 2 years. Pub. 1075 requires 7 years for systems that handle FTI (sec. 4 AU-11).
3. **Common control inheritance.** Documented for the ACMP (this SSP), the IEP, and the Software division's FedRAMP and GovRAMP packages; **not documented** for the IT Consulting CUI enclave, which is the scope of the coming CMMC assessment.
4. **CMMC Level 2 readiness.** The CUI enclave's Basic self-assessment score was 92 in SPRS (2025-06). About 340 acquired-firm consultants work on DoD programs from the acquired firm's laptops and identity provider, and some CUI is held on the acquired firm's file shares outside the enclave. Phase 2 was planned for 2026-11-10 (32 CFR 170.3(e)(2)) but is suspended by the DoD (Department of War) CIO memorandum of 2026-07-13. During the suspension requiring activities may require Level 1 (Self) or Level 2 (Self), and NIST SP 800-171 Rev. 2 under DFARS 252.204-7012 still applies (DoD Class Deviation 2026-O0025, Revision 3 (DFARS 240.371-5)). No Level 2 certification assessment by a C3PAO is scheduled; it is now a voluntary choice.
5. **Cross-division incident notification.** About 1,150 GovTech contracts, 620 RMS agency agreements, and the federal contracts carry incident clocks of 1 hour (CJI), 24 hours (FTI, through the agencies), 12 hours (Florida agency ransomware reports), and 72 hours (DoD). Each division keeps its own runbook. The group notification matrix is incomplete and has never been exercised.
6. **AI ahead of governance.** The IEP AI eligibility assistant went live for caseworkers in 2 states in 2026-03, before the Group AI Standard was adopted (2026-06); bias testing is incomplete and one state has no applicant notice. The RMS AI report-writing assist is in a beta with 37 agencies without Group AI council review or a CJIS review of the model service.
7. **Acquired consulting firm.** The firm acquired on 2025-07-01 still runs its own identity provider (password plus SMS codes for VPN), VPN, endpoint tools, and policies. A directory trust to the group directory, built for migration, is live. The IT Consulting supplement predates the acquisition. Migration is due 2027-03-31.
8. **Recovery at scale.** ACMP contracts set an 8-hour recovery time for CJI and FTI tenants. Restores are tested per tenant; the 2026 test restored 12 tenants in 6 hours. A full restore of about 430 tenants from the immutable vault has never been tested, and the platform team estimates more than 30 hours.
9. **FIPS 140-3 for CJI in transit.** GovTech finished moving ACMP CJI paths to FIPS 140-3 certified modules in 2026-08. The RMS on-premises connectors at 41 agencies still use modules with FIPS 140-2 certificates, which CJISSECPOL v6.1 SC-13 says "will not be acceptable after September 21, 2026."
10. **Subcontractor flowdown.** GovTech uses about 180 subcontractor staff with access to agency data. For 23 of them, Security Addendum certifications or IRS-approved subcontract terms (Pub. 1075 Exhibit 7 I(8)) could not be shown.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | The focus division's primary requirement set is the NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline required by the agency contracts, with the CJISSECPOL v6.1 and Pub. 1075 (Rev. 11-2021) overlays and the DPPA, HIPAA business associate, and Medicaid rows. IT Consulting: FAR 52.204-21, DFARS 252.204-7012, CMMC (32 CFR Part 170), and selected SP 800-171 Rev. 2 requirements. Government Software Products: CJIS for the RMS, FedRAMP, GovRAMP, SOC 2 commitments, and FTC Act Section 5. A regulation-by-division matrix and a group roadmap |
| P08 | Ransomware affecting agency systems holding CJI and FTI (registry default, kept), spanning divisions: entry through the acquired consulting firm's VPN, a stolen group cloud platform engineer credential, data theft and encryption in the ACMP CJI cluster and two FTI tenants, and CUI on the acquired firm's file shares. A multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: the ACMP (GovTech) and the Civic Suite and RMS (Government Software Products) are in scope as true service organizations; IT Consulting is out of scope, with reasons; the Grants Management federal edition relies on its FedRAMP authorization |
| P10 | Group AI governance program. Priority use case: AI eligibility recommendations for public benefits on the IEP. The registry default ("AI eligibility determination") was adapted: federal program rules keep the determination with state merit staff (7 CFR 272.4(a)(2); 42 CFR 431.10), so the AI recommends and the caseworker determines. Plus division use cases with their regulator-specific rules |
| Cloud | Shared corporate platform plus division workloads, vendor-agnostic: provider A (government-community regions, FedRAMP High authorized services) for CJI, FTI, CUI, Medicaid, and federal workloads; provider B (commercial regions, FedRAMP Moderate authorized services) for other workloads and the immutable backup vault |

**Registry defaults kept:** the primary system (case management system hosted for state and local agencies) is the SSP system; the P08 incident is kept and made to span divisions; the P10 use case is kept with the adaptation above.

## 6. Assessment calendar (fictional unless a regulation is cited)
| Date | Event |
|---|---|
| 2025-07-01 | Consulting firm acquired by IT Consulting |
| 2025-11-10 | CMMC Phase 1 begins (DFARS rule effective date, 90 FR 43560) |
| 2026-05-04 to 2026-07-31 | Group and division risk analyses, BIAs, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-09-15 | Results to the board risk committee; deliverables approved |
| 2026-09-21 | CJISSECPOL v6.1 SC-13: FIPS 140-2 certificates no longer acceptable |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2027-03-31 | Acquired consulting firm migration due |
| 2027-09-30 | CJISSECPOL v6.1 zero-cycle ends for [Priority 2] to [Priority 4] requirements (section 1.4) |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Revenue split (fictional) | GovTech Integration about $8.1 billion (about $22 million per calendar day); IT Consulting about $6.3 billion; Government Software Products about $3.6 billion (about $9.9 million per calendar day). Total about $18.0 billion, as in section 1 | P05 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary, with a dated plan. Very High: board risk committee only. A risk that would breach a CJIS Security Addendum, Pub. 1075 Exhibit 7, or DFARS 252.204-7012 term may not be accepted; it must be treated or the regulated data removed | P01, P06 |
| P08 exercise scenario (illustrative counts) | Entry through an acquired-firm consultant's VPN sign-in (password and SMS code relayed by a phishing page); a migration server in the acquired estate used by group cloud platform engineers for the directory migration; just-in-time elevations are scoped per cloud account, and the stolen elevation covered only the ACMP production accounts. Data read from the CJI cluster for 64 criminal justice agencies in 4 states (31 in Florida): about 1.3 million case records, about 1.1 million individuals (about 520,000 Florida residents), about 410,000 records with CHRI. FTI tenants affected: the Florida revenue agency (about 2.1 million taxpayer case records) and one other state's revenue agency (about 0.9 million), which is one of the 2 agencies whose IRS notifications predate the provider B vault. About 2,300 CUI files from 4 DoD programs (the division is prime on 2 and subcontractor on 2). Extortion email to the group and 3 agencies. Restore estimate with today's tooling: 15 to 18 hours for about 214 tenants. Most of the 46 Florida CG-CJ agencies are county or municipal agencies | P08 |
| SOC 2 report periods and scope | ACMP: 12 months ending June 30 (current period 2026-07-01 to 2027-06-30). RMS and Civic Suite: separate Type 2 reports for each calendar year, covering Security, Availability, and Confidentiality. The RMS AI assist beta has run since 2026-04-06. Civic Suite utility billing hands card data to a payment processor (a carved-out subservice organization). The IEP and MVSP are not in SOC 2 scope because their state contracts name other assurance. A GovRAMP verification of the ACMP is planned for 2027 | P09 |
| IEP AI eligibility assistant | Runs for Florida's human services agency and one other state's agency; neither is one of the 2 business associate states. About 1,450 caseworkers; about 182,000 applications processed with it from 2026-03 to 2026-08. Florida's portal gives applicants notice; the other state does not. Validation (800 cases, 400 per state): income field accuracy 96.4%; outcome agreement 92.0% (64 wrong); caseworkers caught 18 of 64 and 17 accepted errors led to incorrect denials, which the states reopened; 9 reason summaries cited nonexistent policy; 2 of 25 prompt-injection documents changed the recommendation; non-English income extraction errors 8.7% vs 3.1%; households with a member 60 or older 11.4% vs 7.0% outcome errors | P10 |
| RMS AI report-writing assist measurements | 300 drafts reviewed by report supervisors in 6 beta agencies: 2.3% added a fact not in the dictation, 5.0% omitted a material fact, 41% signed with no edits | P10 |
| Group AI program details | Group AI council members: Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, group public sector compliance director, GovTech Data and AI director, Software division RMS general manager, IT Consulting security and compliance lead. P10 fieldwork 2026-07-13 to 2026-08-21; council decisions 2026-08-28. Other inventoried uses: the Civic Suite 311 chatbot and permit plan review assistant (in production), an approved enterprise generative AI assistant, and public AI tools (not approved) | P10 |
| Additional role titles used in the deliverables | Group HR director; Group chief financial officer; Group communications lead; Government Software Products president; GovTech chief technology officer; GovTech Data and AI director; GovTech customer support director; GovTech delivery director; IEP program director; MVSP program director; IT Consulting chief operating officer; IT Consulting defense programs director; IT Consulting managed services director; Software division RMS, Civic Suite, and Grants general managers; Software division customer success director. All are role titles under the structure in section 2 | P01 to P10 |
| Service scale used in the deliverables | ACMP: about 430 agency tenants in 29 states, about 61,000 agency users, records of about 27.7 million individuals. RMS: about 620 agencies; RMS support staff cover 17 states. Civic Suite: about 1,900 local governments | P02, P05, P09 |
