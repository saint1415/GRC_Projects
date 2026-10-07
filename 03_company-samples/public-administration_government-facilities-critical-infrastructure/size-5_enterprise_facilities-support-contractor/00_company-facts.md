# Scenario facts: Cris Santos Company | Government Services and Facilities | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Contract terms described here are fictional scenario choices unless a regulation is cited.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | Facilities support contractor (NAICS 561210, Facilities Support Services). The company operates and maintains government buildings: integrated facility management, operations and maintenance (O&M), building automation (BAS), and electronic security (access control and video) services for federal, state, local, and public education customers |
| Location | Headquartered in Florida. Operations in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia, Maryland, and the District of Columbia. Three 24x7 **Remote Operations Centers** (ROC-1 Florida, ROC-2 Georgia, ROC-3 Virginia). **State law is handled generically:** each state where affected individuals reside or where a customer is located, with Florida as the worked example |
| Segments and revenue | About $4.8 billion a year (fictional): **Federal Facilities (FF)** $1.73 billion; **State and Local Government (SLG)** $1.68 billion; **Education Facilities (EDU)** $0.86 billion; **Security Integration (SI)** $0.53 billion. About $13.2 million per calendar day (about $18.5 million per business day). Not small under the SBA standard of $47.0 million for NAICS 561210 (13 CFR 121.201) |
| Workforce | 12,000 employees: about 8,900 field operations staff (building engineers, technicians, trades), 1,150 controls and electronic security technicians, 210 ROC operators, 420 IT, security, and technology staff, and 1,320 corporate and segment staff. About 3,700 staff on federal contracts hold GSA-issued PIV cards |
| Buildings served | **FF:** 64 GSA-controlled federal buildings (about 23 million rentable square feet) under 11 GSA Public Buildings Service contracts. **SLG:** about 1,050 buildings for 5 state governments and 38 counties and cities, including 41 courthouses and 27 public safety buildings (sheriff and police headquarters and 911 centers). **EDU:** 9 public universities (about 640 buildings) and 12 school districts (about 380 schools) |
| Who owns the building systems | **The customers.** All field equipment (BACnet controllers, door controllers, readers, cameras, recording servers) is customer-owned. At federal buildings the BAS runs on GSA servers on the GSA Building Systems Network (BSN) under GSA's authorization (GSA Building Technologies Technical Reference Guide (BTTRG) v3.0, May 2024); physical access control at federal buildings is a GSA and Federal Protective Service responsibility that the company does not administer. For SLG and EDU customers the company runs the supervisory and administration layer on its own platform, the IBOP (section 3) |
| Data the company holds | About 585,000 cardholder records (about 168,000 state and local employees, about 372,000 university students, faculty, and staff, and about 45,000 contractors and visitors): name, affiliation, badge photo, credential number, door schedule, access history. 1,850 face templates in face verification pilots (P10). Building drawings, security system layouts, and door schedules for all customers. GSA building drawings marked **CUI** (Physical Security category, GSA Order PBS 3490.3 CHGE 1) and federal contract information (FCI) in work orders. Employee data for 12,000 staff (SSNs, background check results, bank details) |
| Federal contract clauses (FF) | FAR 52.204-21 (Basic Safeguarding of Covered Contractor Information Systems, NOV 2021); FAR 52.204-23 (Kaspersky, DEC 2023); FAR 52.204-25 (Section 889, NOV 2021) with representations under 52.204-24 and 52.204-26; FAR 52.204-30 (FASCSA orders, DEC 2023); FAR 52.204-9 and GSAR 552.204-9 (PIV of contractor personnel). Statements of work incorporate the BTTRG, GSA IT Security Policy (CIO 2100.1), and CUI handling under 32 CFR Part 2002 and GSA Order PBS 3490.3. **No DoD contracts**, so DFARS 252.204-7012 and CMMC do not apply. **No FedRAMP:** the company provides no cloud service to federal agencies; it operates GSA's systems only through GSA-furnished access |
| State contract terms (SLG) | Each of the 5 state customers has a cybersecurity exhibit requiring **NIST SP 800-53 Rev. 5 Moderate** controls for contractor-managed systems that store or process agency data, background screening, incident notice to the agency within 24 hours, and an annual independent assessment. Florida worked example: Fla. Stat. 282.318(4)(h) requires state agency IT service contracts to meet NIST CSF and to assign security duties. Two state customers' procurement policies require **GovRAMP** verification for contractor SaaS used by agency staff |
| Local contract terms (SLG) | County and city security addenda: compliance with the customer's cybersecurity standards (Florida worked example: adopted under Fla. Stat. 282.3185(4)(a), NIST CSF-based), incident notice within 24 hours of discovery, fingerprint-based background checks, and public records clauses (Florida worked example: Fla. Stat. 119.0701). **Public safety buildings (27):** the agencies treat parts of these buildings as physically secure locations under the FBI CJIS Security Policy v6.1 and require company personnel with unescorted access to complete CJIS role-based training (CJISSECPOL AT-3) and the fingerprint-based checks the agency requires (PS-3). The company performs no criminal justice functions and the IBOP holds no CJI. Detention door control systems at jails are customer-operated and out of scope |
| Education contract terms (EDU) | The 9 universities designate the company a "school official" under 34 CFR 99.31(a)(1)(i)(B) for the student cardholder records it maintains, subject to the redisclosure limits in 99.33(a). School district contracts cover staff credentials only; the company holds no K-12 student records |
| SEC registrant duties | Form 8-K Item 1.05 (material cybersecurity incidents, within 4 business days after the materiality determination); Regulation S-K Item 106 (17 CFR 229.106) annual disclosure in the 10-K; SOX IT general controls over ERP, payroll, and project accounting |
| Sector context | Government Services and Facilities sector (co-Sector Risk Management Agencies: DHS and GSA, NSM-22). The company is a contractor to government facility owners, not a government entity |
| Not in scope | IRS Pub. 1075 (C-GOVERNMENT-R02): the state contracts for revenue and benefits agency buildings exclude restricted FTI areas, where company staff enter only under escort. VVSG 2.0 (R04): no election systems. SLCGP (R07): a grant condition for governments. CIRCIA (R06): proposed only. FedRAMP, DFARS 252.204-7012, and CMMC: no federal cloud service and no DoD contracts. Colorado SB26-189 and Texas HB 149: the company does no business in Colorado or Texas |
| Acquisitions | **AQ-1:** a regional electronic security integrator acquired 2025-10 (620 employees, now in the SI segment; installed base at about 240 customer sites, 142 of them still serviced through AQ-1's legacy tools). **AQ-2:** a campus facilities services firm acquired 2026-03 (1,100 employees, now in the EDU segment; 3 university contracts). Both are included in the 12,000 employees |
| State law approach | Florida is cited where a Florida duty is the worked example: breach notice and reasonable security (Fla. Stat. 501.171), the definition of biometric data (501.702), contractor public records duties and the security plan exemption (119.0701; 119.071(3)(a)), customers' incident reporting duties that contracts flow down (282.318; 282.3185), and the ransom payment ban for state agencies and local governments (282.3186). Other states are handled through outside counsel's state matrix |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee and risk committee | Risk committee oversees cybersecurity and physical safety risk (Item 106 governance); audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Information Security Officer (CISO) | Program owner for IT and OT security; reports to the CEO and to the risk committee quarterly |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register; chairs the executive risk committee |
| Chief Audit Executive | Heads Internal Audit (third line); reports functionally to the audit committee; leads the P07 assessment |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Compliance Officer | Regulatory and government contract compliance program (second line) |
| Chief Privacy Officer | Privacy program; breach determinations; biometric and student data rules |
| Chief Information Officer (CIO) | Corporate IT, ERP, collaboration, endpoints; owns several common control providers |
| Chief Technology Officer (CTO) | Building technology platforms: IBOP and the Facility Services Portal; chairs the AI governance committee |
| Segment presidents (Federal Facilities; State and Local Government; Education Facilities; Security Integration) | Business owners of customer contracts and customer notices |
| GRC team (12), Security Operations Center (24x7, in-house plus MSSP overflow), OT security team (9), Internal Audit (in-house, 22 staff with an IT audit group of 7) | Three lines model |
| Disclosure committee | 8-K materiality decisions (General Counsel chairs) |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | **Integrated Building Operations Platform (IBOP)**: multi-tenant BAS supervisory servers, physical access control (PACS) and video management software (commercial, company-hosted), the IBOP customer console, and the OT remote access gateways | Cloud provider A (two regions) plus site edge gateways. BAS supervision at 1,420 buildings (about 61,000 BACnet field controllers); PACS administration at 910 buildings (about 10,800 door controllers, 27,500 readers); video management at 560 buildings (about 34,000 cameras, 1,750 recording servers). Field controllers keep running local programs, and door controllers cache credentials for up to 72 hours, if the platform is lost |
| SYS-02 | Identity platform (SSO, MFA, privileged access management (PAM), identity governance) | AQ-1 staff still use a legacy directory that is not federated |
| SYS-03 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers (DC-1 Florida, DC-2 Virginia) | Cloud A: IBOP. Cloud B: Facility Services Portal, data platform, AI services. Colocation: network core, video evidence archive, offline backup copies |
| SYS-04 | OT remote access and site edge: about 1,480 company-managed edge gateways at customer sites; PAM-brokered OT remote access gateway with session recording | 142 AQ-1 sites still reached through AQ-1's legacy always-on remote-support tool |
| SYS-05 | Enterprise network (SD-WAN), 3 ROCs, and about 15,500 endpoints (9,200 rugged tablets, 5,800 laptops, 500 ROC and engineering workstations) | |
| SYS-06 | ERP, payroll, and project accounting (SOX-relevant) | SOX IT general controls tested annually |
| SYS-07 | **Facility Services Portal (FSP)**: company-built multi-tenant work order, asset, and service request SaaS | Used by all segments and by about 180 customer organizations. Holds FCI (federal work orders). SOC 2 Type 2 since 2025 |
| SYS-08 | GSA-furnished access (FF) | GSA BAS applications on the BSN reached only through GSA's virtual desktop with PIV cards. **GSA's systems under GSA's authorization; outside the company's boundary** |
| SYS-09 | Collaboration suite (SaaS) with a CUI enclave (restricted document library for GSA CUI drawings) | |
| SYS-10 | About 2,600 subcontractors and suppliers (about 340 with remote or data access) | Tiered third-party risk program |
| SYS-11 | AI portfolio (12 use cases) | Governed by the AI governance committee formed 2025-11 |
| SYS-12 | Face verification module of the PACS software (pilots at 3 customer sites) | Part of SYS-01 configuration (P10) |

**SSP system (P02):** the *Integrated Building Operations Platform (IBOP)*: the multi-tenant BAS supervisory and PACS and video management platform the company operates for state, local, and education customers from three ROCs, including its Cloud provider A workloads, the OT remote access gateways, the company-managed site edge gateways, the ROC and engineering workstations, and the face verification module configuration, and inheriting common controls from the enterprise platform.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A mature program aligned to CSF 2.0, with three lines of defense
- Annual enterprise risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with an OT security team; PAM-brokered OT remote access gateway for company technicians
- Quarterly access certification; identity governance for corporate and IBOP accounts
- Immutable backups for cloud workloads; annual regional failover tests for tier-1 systems
- Tiered third-party risk program; FAR clause compliance program with Section 889 screening of IT purchases
- CUI enclave for GSA drawings; HSPD-12 and PIV processes for federal staff
- Annual SOC 2 Type 2 for the Facility Services Portal (Security, Availability, Confidentiality) since 2025
- SEC Item 106 disclosure in the 10-K; disclosure committee with a materiality playbook

**Targeted gaps:**
1. **AQ-1 integration.** 142 customer sites from AQ-1's installed base are still reached through AQ-1's legacy always-on remote-support tool instead of the PAM gateway, and AQ-1's 620 staff sign in through a legacy directory with MFA only for email.
2. **OT visibility.** Passive OT network monitoring covers 870 of 1,420 IBOP buildings (61%). Edge gateway logs from AQ-1 sites are not in the SIEM.
3. **Field device credentials.** Factory default credentials remain on some field controllers and recording servers, and shared technician accounts remain on legacy BAS supervisory instances at the 3 AQ-2 campuses.
4. **Supply chain screening.** Section 889 and FASCSA screening covers corporate IT purchases but not field-installed equipment bought by subcontractors or AQ-1's own office equipment and spare-parts stock. The quarterly SAM check for FASCSA orders runs only for corporate procurement.
5. **Subcontractor flow-downs.** Of the 340 subcontractors and suppliers with remote or data access, some lack the FAR 52.204-21(c) and 52.204-25 flow-downs and the 24-hour incident notice term, and some have no security review.
6. **IBOP recovery.** The 2026-05-09 regional failover test restored PACS administration in 7.5 hours against a 4-hour RTO; the controller program repository has never been restored at full scale.
7. **AI and biometrics.** 12 AI use cases, of which 7 have completed committee review. Face verification pilots at 3 customer sites (1,850 enrolled) started on customer orders before committee review, and bias testing rests on vendor data.
8. **Disclosure readiness.** The materiality playbook was built for IT and ransomware scenarios. It has never been exercised for an OT incident with physical safety effects at customer buildings, and government-customer contract factors are not in the worksheet.
9. **CUI outside the enclave.** GSA CUI drawings were found in general project sites of the collaboration suite.
10. **Customer data retention.** Cardholder records of departed people are kept beyond customer retention schedules in some IBOP tenants.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The IBOP (the registry's "physical access control and building automation system", at enterprise scale), Moderate baseline with High-baseline supplements for door and setpoint integrity, inheriting from enterprise common control providers |
| P03 | NIST SP 800-53 Rev. 5 (Release 5.2.0) **Moderate** baseline (177 base controls): **binding by contract** for the IBOP under the state cybersecurity exhibits and the **enterprise control standard** elsewhere, tailored for OT with NIST SP 800-82 Rev. 3. Plus every other applicable requirement across the enterprise: FAR clauses, CUI, the BTTRG, SEC rules, CJIS (agency-imposed), FERPA (school official), GovRAMP (FSP), and state laws (Florida worked example), with evidence sampling |
| P08 | Intrusion into building access control and automation systems through AQ-1's legacy remote-support tool, with an **SEC materiality assessment** step, crisis management, legal, and customer notice workflows |
| P09 | SOC 2 Type 2 readiness across two service lines: SL-1 Managed Building Operations and Security (on the IBOP; all five categories, first report) and SL-2 Facility Services Portal (existing Type 2; adding Processing Integrity) |
| P10 | Enterprise AI portfolio (12 use cases) under the AI governance committee, with a full assessment of facial recognition for facility access (AI-001 face verification pilots; AI-002 1:N identification request declined) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |
| Registry defaults | All three registry defaults were kept: the primary system is the IBOP, the incident is an intrusion into building access control and automation systems, and the AI use case is facial recognition for facility access, placed inside the enterprise AI portfolio that this size requires |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (site sampling visits 2026-06-15 to 2026-07-17) |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-10 | Results to the risk committee of the board |

## 7. Facts added while building the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.
