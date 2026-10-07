# Scenario facts: Cris Santos Company | Defense Industrial Base | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant) |
| Business | Tier-1 aerostructures and aircraft components manufacturer (NAICS 336413, Other Aircraft Parts and Auxiliary Equipment Manufacturing): machined titanium and aluminum structural assemblies, composite wing and fuselage panels, flight-control and landing-gear actuation components, additively manufactured metal parts, and component repair and overhaul (MRO). Military fixed-wing and rotorcraft programs and commercial aircraft. Quality system certified to AS9100 at every plant |
| Location | Headquartered in Florida. 8 operating sites in 6 states plus 2 data centers: **FL-1** headquarters and engineering center (holds the facility clearance), **FL-2** machining plant, **FL-3** MRO depot, **GA-1** composites plant, **AL-1** final assembly plant, **TX-1** machining and actuation plant, **KS-1** fabrication plant (acquired 2025-06), **AZ-1** additive manufacturing center (opened 2026-05); **DC-1** company data center on the FL-1 campus and **DC-2** colocation data center in Texas. **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 6,900 production and MRO technicians, 2,100 engineers, 950 quality staff, 780 supply chain staff, and 1,270 corporate and administrative staff (including 420 in IT and security). About 90 employees are foreign persons on nonimmigrant visas who work on commercial programs under EAR deemed-export licenses or with technology that needs no license. None may access ITAR technical data |
| Revenue | About $4.8 billion a year (fictional): 56% defense, 44% commercial. Defense revenue is about 14% from DoD prime contracts (spares, sustainment, and repair for military services and the Defense Logistics Agency) and about 42% from subcontracts with four aircraft prime contractors (**Prime A, Prime B, Prime C, Prime D**). SBA size standard for NAICS 336413 is 1,250 employees (13 CFR 121.201), so the company is not small |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): drawings, 3D models, specifications, NC programs, additive build files, process specifications, and test data. It is covered defense information (CDI) and CUI. Most military part data is also ITAR technical data. Commercial programs carry EAR-controlled technology. Federal contract information (FCI) is in ERP and contracts systems |
| Classified information | FL-1 holds a facility clearance for one classified subcontract (Program K). Classified work happens in one closed area on a stand-alone classified information system authorized by DCSA. NISPOM (32 CFR Part 117) applies. The classified system is outside the CUI scope of these deliverables except for reporting duties (P08) |
| Contract clauses | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021), and FAR 52.204-25 in current DoD contracts and subcontracts. Contracts and subcontracts awarded from 2025-11-10 also include DFARS 252.204-7021 (NOV 2025), most at **CMMC Level 2 (C3PAO)** |
| CMMC status | **Final Level 2 (C3PAO)** for the CMMC Assessment Scope "CEE and MOZ" as assessed at FL-1, FL-2, FL-3, GA-1, AL-1, and TX-1 (sections 3 and 6), CMMC Status Date 2026-03-20, valid for 3 years (32 CFR 170.17). The C3PAO's results, with a score of 110, were transmitted to SPRS. Annual affirmation of continuing compliance is due by 2027-03-20 (32 CFR 170.22). **Affirming Official:** the Chief Operating Officer |
| CMMC Level 3 | A DoD requiring activity told the company in 2026-06 that the planned solicitation for the Program H actuation subsystem, on which the company intends to bid as prime, will require **CMMC Level 3 (DIBCAC)**. Release is expected after Phase 3 begins on 2027-11-10 (32 CFR 170.3(e)(3)). Final Level 2 (C3PAO) on the Level 3 scope is a prerequisite (32 CFR 170.18(a)) |
| Export controls | Registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1). Technology control plans at every site. The Vice President, Trade Compliance is the Senior Empowered Official |
| Public company duties | SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106); SOX internal control over financial reporting, including IT general controls for ERP |
| Not in scope | CIRCIA reporting (final rule not published; proposed only). Health and consumer payment data: none beyond employee benefits data handled by the benefits program. FedRAMP as a seller: the company sells no cloud services to the Government |
| State law approach | State breach laws are handled generically (each state where affected individuals reside), with Florida (Fla. Stat. 501.171) as the worked example. Employee personal information is the main personal data in scope |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (audit committee; risk and technology committee) | Cyber risk oversight (Item 106 governance). The risk and technology committee receives quarterly cyber reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | **CMMC Affirming Official** (32 CFR 170.22); authorizing official equivalent for the CEE; business owner for plant operations |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee; recommends system authorization |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Audit Executive | Heads Internal Audit (third line); reports to the audit committee; leads the P07 assessment |
| Vice President, Trade Compliance | **Senior Empowered Official** (ITAR); export classification, licenses, technology control plans, voluntary disclosures |
| Vice President, Engineering | **CUI data owner** for engineering data; PLM business owner; business owner for the generative AI assistant (P10 AI-001) |
| Director, CMMC Program Office | Runs the CMMC program in the GRC team: SSPs, scope changes, SPRS entries, C3PAO and DIBCAC liaison, supplier CMMC verification |
| Corporate Facility Security Officer (FSO, FL-1) | NISPOM FSO and Insider Threat Program Senior Official (ITPSO) (32 CFR 117.7(b)) |
| Information System Security Manager (ISSM) | Classified information system at FL-1 (32 CFR 117.18(c)(2)) |
| GRC team (10), Security Operations Center (24x7, in-house), Internal Audit (in-house) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

| ID | System | Hosting | CUI? | CMMC asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | Identity platform: two directories (commercial tenant for corporate users; government-community tenant for CEE users), SSO, phishing-resistant MFA, privileged access management (PAM), identity governance | Government-community cloud and commercial SaaS | No (identities) | Security Protection Asset | About 3,600 CEE accounts; hardware security keys for all CEE users |
| SYS-02 | CUI collaboration suite (email, file storage, chat) | Government-community cloud (SaaS) | Yes | CUI Asset | Offering FedRAMP authorized at Moderate or higher; customer responsibility matrix (CRM) on file |
| SYS-03 | CEE cloud subscriptions (IaaS/PaaS) | Government-community cloud (same provider) | Yes | CUI Asset | PLM application tier, CAD virtual desktop pool (1,400 concurrent sessions), CUI exchange gateway (managed file transfer), log analytics, key management, backup vault, and the AI-001 assistant (pilot) |
| SYS-04 | CAD/PLM | CAD on SYS-05 workstations and virtual desktops; PLM on SYS-03 | Yes | CUI Asset | System of record for about 2.4 million controlled documents; about 3,100 named PLM users |
| SYS-05 | Engineering endpoints | 7 in-scope sites and mobile | Yes | CUI Asset | About 2,650 CAD workstations and enclave laptops; full-disk encryption, EDR, secure boot |
| SYS-06 | Manufacturing Operations Zone (MOZ): MES (central instance in DC-1 with standby in DC-2), DNC servers at each plant, about 1,150 CNC machines, 240 coordinate measuring machines (CMMs), 36 metal additive printers at AZ-1, test cells | On-premises | Yes | CUI Assets (MES, DNC, build-prep workstations) and Specialized Assets (machines, printers, test equipment) | Documented in its own SSP (MOZ SSP) inside the same CMMC Assessment Scope |
| SYS-07 | Enterprise and plant networks: SD-WAN, plant enclave segments, network access control (802.1X with device certificates at FL-1, FL-2, GA-1, AL-1, TX-1; not yet at FL-3 and AZ-1) | On-premises and carrier services | Yes (in transit) | Security Protection Asset | IPsec tunnels with FIPS-validated modules from plants to SYS-03 |
| SYS-08 | Security operations platform: 24x7 SOC, SIEM, EDR, user behavior analytics, vulnerability management, threat intelligence | Government-community cloud (SIEM) and DC-1 | Security data | Security Protection Asset | Common control provider for monitoring and response |
| SYS-09 | ERP (orders, purchasing, inventory, government contract accounting) | DC-1 and DC-2 | No CUI; FCI | Out of the CUI scope; FAR 52.204-21 applies | SOX IT general controls tested annually; drawings referenced by number only |
| SYS-10 | Corporate network, commercial productivity suite, about 9,000 corporate endpoints | On-premises and commercial SaaS | No (policy) | Out-of-Scope Asset (separated) | Commercial business and administration |
| SYS-11 | Commercial cloud (Cloud provider A): SL-1 MRO customer portal, SL-2 aircraft health monitoring analytics, corporate data platform | Commercial IaaS/PaaS | No (EAR99 or not subject to the EAR) | Out-of-Scope Asset | Service lines in P09 |
| SYS-12 | KS-1 legacy environment (acquired 2025-06): own directory, file server holding CUI drawings, legacy MES and DNC, flat plant network | On-premises at KS-1 | Yes | **Outside the certified CMMC scope** | Acquired company's SPRS Basic Assessment score of 72 (self-assessment, 2025-01-28) under the KS-1 CAGE code. Integration into the CEE and MOZ due 2027-03-31 |
| SYS-13 | Classified information system (Program K) | Stand-alone in the FL-1 closed area | Classified | Not in the CMMC scope (NISPOM) | Authorized by DCSA; ISSM manages |
| SYS-14 | Third parties: about 1,400 active suppliers, 380 of which receive CUI; 6 machine and printer manufacturers with remote support; PLM and CAD software vendors; government-community cloud provider | Mixed | Yes for 380 suppliers | External service providers where they handle Security Protection Data | Supplier CMMC status tracked by the CMMC Program Office |
| SYS-15 | AI portfolio (12 use cases) | Mixed | Some (AI-001) | AI-001 is a CUI Asset inside SYS-03 | Governed by the AI governance committee formed in 2025 (P10) |

**SSP system (P02):** the *CUI Engineering Enclave (CEE)*: SYS-02, SYS-03, SYS-04, SYS-05, and the CEE segments of SYS-07 at the 7 in-scope sites (FL-1, FL-2, FL-3, GA-1, AL-1, TX-1, AZ-1), inheriting common controls from SYS-01, SYS-07, SYS-08, and the enterprise programs; it shares one CMMC Assessment Scope with the MOZ (SYS-06), which has its own SSP.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- Final Level 2 (C3PAO) status since 2026-03-20 for the CEE and MOZ, with a score of 110 in SPRS
- A CUI enclave in a government-community cloud offering that is FedRAMP authorized at Moderate or higher, with the provider's CRM on file (DFARS 252.204-7012(b)(2)(ii)(D))
- Phishing-resistant MFA (hardware security keys) for every CEE user; PAM for administrators
- A 24x7 in-house SOC with user behavior analytics and threat intelligence feeds
- Immutable backups; annual disaster recovery tests for tier-1 systems
- Four DoD-approved medium assurance certificates and a DIBNet reporting drill (2026-04-15)
- A policy hierarchy of policies, standards, procedures, and exceptions
- A NISPOM security program at FL-1 with an FSO, ITPSO, and ISSM
- An export compliance program with technology control plans
- A SOC 2 Type 2 report for the SL-1 MRO customer portal since 2025
- Item 106 disclosure in the Form 10-K; Internal Audit reports to the audit committee

**Targeted gaps found in the 2026 assessments:**
1. **KS-1 integration.** The acquired KS-1 plant still keeps CUI drawings on a legacy file server and legacy MES outside the certified scope. Its SPRS score (72, 2025-01-28) is out of date. One work order for a contract that includes DFARS 252.204-7021 was routed to KS-1 in 2026-08 (P03).
2. **AZ-1 additive center.** AZ-1 joined the CEE and MOZ by a change on 2026-05-18, after the C3PAO assessment, so it is not yet covered by a certification assessment and contracts that include DFARS 252.204-7021 are not routed there. Build-prep workstations have no documented baseline, the 36 printers sit on a plant segment reachable from the corporate network, printers are loaded by USB drive, and one printer manufacturer's remote support tool runs outside PAM.
3. **Supplier CMMC status.** Of 380 suppliers that receive CUI, 176 (46%) have a verified CMMC status in SPRS at the level their subcontract needs. 4 of 60 sampled purchase orders lacked the DFARS clauses.
4. **Level 3 readiness.** 10 of the 24 Level 3 requirements are met. No penetration test of the CEE in the last 12 months (last 2025-06-12), and specialized assets at AZ-1 are not segregated.
5. **Operating exceptions in the certified scope.** Late account disablement, visitor escort lapses at TX-1, an EAR-licensed foreign-person engineer with access to a PLM project folder holding ITAR data, missing sanitization records for machine controller drives, and vulnerability remediation past SLA.
6. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. The generative AI assistant used with CUI engineering documents (AI-001) is in a 300-user pilot.
7. **Materiality.** The SEC materiality playbook was exercised on 2026-04-22, but only with a ransomware scenario. It does not cover theft of program data with no operational outage, review of a draft 8-K for CUI, export-controlled, or classified content, or a request to the U.S. Attorney General for delay.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P08 | Exfiltration of CUI: a state-sponsored actor exploits a zero-day vulnerability in the managed file transfer software used for the CEE's CUI exchange gateway and for a separate corporate instance, and takes CUI and employee personal information. Includes the DoD 72-hour report, an **SEC materiality assessment and Form 8-K Item 1.05** step, and multi-state breach notification for employees |
| P09 | SOC 2 Type 2 readiness across two commercial service lines: SL-1 MRO customer portal (Security, Availability, Confidentiality; Type 2 since 2025) and SL-2 aircraft health monitoring analytics (Security, Availability, Confidentiality, Processing Integrity; first Type 2). CMMC remains the primary assurance for defense work |
| P10 | Enterprise AI portfolio (12 use cases) under the AI governance committee, with a full assessment of AI-001, the generative AI assistant used with CUI engineering documents |
| Cloud | Multi-cloud, vendor-agnostic: a government-community cloud offering for CUI, a commercial cloud provider (Cloud provider A) for non-CUI workloads, two data centers, and SaaS. AWS, Azure, and Google Cloud names appear only in an equivalents table |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2025-06-30 | KS-1 acquisition closes |
| 2026-02-09 to 2026-02-20 | Level 2 certification assessment by a C3PAO (CEE and MOZ at FL-1, FL-2, FL-3, GA-1, AL-1, TX-1) |
| 2026-03-20 | CMMC Status Date: Final Level 2 (C3PAO); affirmation submitted by the COO |
| 2026-04-22 | SEC materiality tabletop (ransomware scenario) |
| 2026-05-18 | AZ-1 opens and joins the CEE and MOZ by change (not yet covered by a certification assessment) |
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit (third line) |
| 2026-09-10 | Results to the risk and technology committee of the board |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-03-20 | Annual CMMC affirmation due (32 CFR 170.22(a)(3)(iii)) |
| 2027-03-31 | KS-1 CUI migration into the CEE and MOZ complete |
| 2027-05-03 to 2027-05-14 | Target window for a new Level 2 certification assessment by a C3PAO of the expanded scope (adds AZ-1 and KS-1); it is also the Level 2 prerequisite for Level 3 |
| 2027-08-02 to 2027-08-13 | Target window for the Level 3 certification assessment by DCMA DIBCAC |
| 2027-11-10 | CMMC Phase 3 begins (32 CFR 170.3(e)(3)) |

## 7. Facts added while completing the deliverables (fictional)

These facts were added while building the deliverables. They do not change sections 1 to 6.

**Volumes.** About $19.2 million of shipments per production day ($4.8 billion over about 250 production days), or about $13.2 million per calendar day. About 1,100 DoD spare and repair orders open at any time. About 9,800 CUI file transfers a week through the CUI exchange gateway.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Vice President, Manufacturing Operations | Business owner for the MOZ and plant recovery |
| Vice President, Supply Chain | Supplier flowdowns and supplier CMMC verification with the CMMC Program Office |
| Vice President, Integration Management Office | KS-1 integration |
| Vice President, Aftermarket Services | Owner of SL-1 (MRO customer portal) and FL-3 |
| Vice President, Digital Services | Owner of SL-2 (aircraft health monitoring analytics) |
| Vice President, Contracts | DFARS clauses, DIBNet reports, prime notifications, CMMC UIDs to contracting officers |
| Chief Human Resources Officer | Screening, terminations, training records |
| Director of Security Operations | Runs the SOC; incident commander |
| Director of Identity and Access Management | Identity platform (SYS-01) |
| Director of Cloud Platform Engineering | Government-community and commercial cloud landing zones |
| Director of Network Engineering | SD-WAN, plant segments, NAC |
| Director of Endpoint Engineering | Workstation baselines, EDR, patching |
| Director of OT Engineering | MES, DNC, machines, printers, OT segmentation |
| Director of Third-Party Risk Management | Vendor tiering, contract security terms, SOC report reviews |
| PLM Platform Manager | Day-to-day PLM administration (reports to the Vice President, Engineering) |
| AZ-1 Site Director | AZ-1 operations and its build-prep workstations |
| Vice President, Corporate Communications; Vice President, Investor Relations | Incident communications; investor messages |
| Chief Data and AI Officer | Chairs the AI governance committee |
| Vice President, Quality | Inspection and product acceptance; quality owner for AI-004 |
| Director of Corporate Security | Badges, visitors, escorts, and site security at all sites (common control provider) |
| Controller | Financial reporting; Item 106 XBRL tagging; member of the disclosure committee |

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Controller, CISO, Chief Risk Officer, Vice President, Contracts, and Vice President, Investor Relations, advised by outside securities counsel.

**Why the registry defaults were kept.** The primary system (CUI engineering enclave with CAD/PLM), the incident (exfiltration of CUI), and the AI use case (generative AI assistant with CUI engineering documents) fit an enterprise aerostructures supplier. At this size the enclave spans 7 sites and a government-community cloud, the incident adds an SEC materiality step, and the AI use case sits inside a 12-item portfolio.

**Facts found or set while building the deliverables.**
| Fact | Used in |
|---|---|
| About 310 cleared employees at FL-1; about 412 privileged CEE users; about 1,400 design engineers | P03, P07, P05 |
| PLM export attribute event: 14 folders migrated in 2026-04 lacked the ITAR attribute; an EAR-licensed foreign-person engineer opened 3 ITAR files (found 2026-08-11; access removed the same day); the Senior Empowered Official filed an initial voluntary disclosure notification with DDTC on 2026-08-19 | P01 R-004; P03 G-003, G-158; P07 POAM-002 |
| One work order for a contract that includes DFARS 252.204-7021 was routed to KS-1 for a secondary operation in 2026-08 (found in sampling) | P01 R-015; P03 G-148; POAM-020 |
| Score under 32 CFR 170.24 today: 80 for the six certified sites, 50 including AZ-1, -14 for the KS-1 legacy environment; Level 3: 10 of 24 met | P02, P03 |
| Remediation funding of about $7.4 million for 2026 Q4 to 2027 Q3, approved by the CEO and CFO on 2026-09-08 | P01 |
| SL-1 serves about 140 airline, lessor, and repair station customers; SL-2 serves 19 airline operators | P09 |
| The government-community cloud provider confirmed in writing on 2026-07-30 that the AI-001 assistant is inside its FedRAMP authorization boundary and listed in the CRM; the 300-user pilot started 2026-06-15 | P10 |
| Penetration test of the CEE contracted for 2026-11 (last CEE test 2025-06-12) | P07 POAM-013 |

