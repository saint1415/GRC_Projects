# Scenario facts: Cris Santos Company | Critical Manufacturing | Enterprise

All 10 deliverables in this folder use the facts below. The company, its plants, its customers, and its suppliers are fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, standard, or contract clause, the citation is given. Regulatory text was checked on 2026-10-05 against eCFR (version date 2026-09-23), the Federal Register API, the NERC standards pages on nerc.com, and the NIST CSRC publication pages.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | Designs, builds, tests, and services liquid-filled and dry-type transformers for the electric grid (NAICS 335311, Power, Distribution, and Specialty Transformer Manufacturing). **Distribution transformers:** single-phase pole-mounted and pad-mounted units and three-phase pad-mounted units up to 5 MVA (about 310,000 units a year). **Power transformers:** substation, generator step-up, and large power transformers from 10 MVA to 500 MVA and up to 500 kV class (about 1,350 units a year). **Specialty:** dry-type transformers for data centers and industry (acquired plant). **Services:** field commissioning, repair, and storm response; the Fleet Monitoring Service (SL-1) and the Spare Transformer Reserve Service (SL-2) |
| Location | Headquartered in Florida. **7 plants in 6 states:** P1 Florida (HQ campus; three-phase pad-mounted distribution), P2 Florida (large power transformers and the extra-high-voltage test laboratory), P3 Georgia (single-phase distribution), P4 Tennessee (medium power transformers), P5 Texas (substation and generator step-up units for renewable, storage, and data center projects), P6 North Carolina (core steel slitting, cut cores, windings, and tanks for the other plants), and P7 Ohio (dry-type and specialty transformers; **acquired 2025-07 as AQ-01**). Also 9 service and repair centers, 3 spare transformer yards (Florida, Tennessee, Texas), and 2 colocation data centers (DC-1 Florida, DC-2 Texas). **State law is handled generically:** "the law of each state where affected individuals reside," with Florida as the worked example. The company has no operations or employees in California, Colorado, Illinois, or New York City |
| Workforce | **12,000 employees:** about 8,850 at the 7 plants (production, maintenance, controls, quality, and plant management), 900 in field service and repair, 700 in engineering (including a 90-person Grid Products software and firmware group), 180 in Digital Services (SL-1 and SL-2), 380 in sales and customer service, 240 in supply chain and logistics, 410 in corporate functions, and 340 in IT and security (including a 24x7 security operations center and an 8-person OT security team) |
| Revenue | About **$4.8 billion** a year (fictional): distribution and specialty transformers 46%, power transformers 41%, field service and repair 8%, Spare Transformer Reserve Service 3%, Fleet Monitoring Service 2%. About $13.2 million per calendar day. The SBA size standard for NAICS 335311 is 800 employees (13 CFR 121.201), so the company is not small |
| Customers | About 650 electric utilities (investor-owned utilities, municipal utilities, cooperatives, and federal power customers) plus renewable, battery storage, data center, and industrial customers in the United States, Canada, Mexico, and the Caribbean. Large power transformer backlog is about 30 months; distribution backlog about 26 weeks. Utilities place emergency storm-restoration orders each hurricane season, and the company reserves production slots for them. Power transformer contracts carry liquidated damages for late delivery (typically 0.5% of contract value per week, capped at 10%; contract terms, fictional) |
| Utility contract security terms | **88 utilities** that operate medium or high impact BES Cyber Systems have added a **Supplier Cyber Security Addendum** to their purchase agreements. The addenda cover the transformer monitoring units (TMUs) and their firmware, the TMU configuration software, field service access to utility sites and systems, and, for subscribers, the FMS and STRS. Their terms follow the six topics in NERC CIP-013-2 Requirement R1 Part 1.2. **61 addenda require incident notice within 48 hours and 27 within 24 hours** of confirming a cyber incident related to the products or services supplied; all require notice within 1 business day when a company representative's access should no longer be granted, disclosure of known vulnerabilities in supplied firmware and software within 30 days, hashes or signatures for all firmware, software, and patches, and only utility-controlled, MFA-protected, per-session remote access. **These deadlines are contract terms, not NERC requirements** |
| NERC status | **Not a NERC-registered entity.** CIP-013-2 ("Mandatory Subject to Enforcement" on nerc.com; effective 2022-10-01) applies to the Responsible Entities in its section 4.1, not to their suppliers. CIP-013-3 is listed as "Subject to Future Enforcement" (FERC order 2026-03-19; effective date 2028-07-01) |
| Federal contracts | **11 civilian federal contracts** (no DoD), about $160 million of backlog: power and distribution transformers for federal power marketing and water agencies and for federal facilities, built to agency specifications (not COTS). All 11 include FAR 52.204-21, 52.204-23, and 52.204-25; the 8 awarded since 2024 also include 52.204-30. Federal contract information (FCI): agency specifications and drawings, delivery schedules, test reports, and correspondence. No DFARS clauses and no CUI |
| DoD work | None. DoD installation projects are bid through construction primes. A **bid review gate** stops any bid whose terms would flow down DFARS 252.204-7012 or a CMMC level until the executive risk committee approves a compliance plan. One prime asked for DFARS 252.204-7012 flow-down in 2026-04; the bid was declined. Whether to build a CUI enclave is a strategic decision scheduled for the board in 2027 |
| Exports | About 9% of revenue: transformers to utilities in Canada, Mexico, the Caribbean, and Central America. Products and technology were classified **EAR99** by the Director of Trade Compliance (2025 review). Export orders are screened against U.S. government restricted-party lists in the ERP before release. Export records must be kept 5 years (15 CFR 762.6(a)) |
| DOE energy conservation | Distribution transformers are covered equipment under the DOE energy conservation program. The company certifies efficiency by testing (10 CFR 429.47) and must keep certification reports and the underlying test data, organized for DOE review, for 2 years after a model is discontinued (10 CFR 429.71). Test data comes from the test laboratories through the Test Data Management System (SYS-07) |
| Transformer monitoring unit (TMU) | The company's own TMU product line (dissolved gas, temperature, bushing, and load monitoring) ships with every power transformer. Electronics are built by a contract manufacturer; the Grid Products group writes the firmware and the TMU configuration software. Firmware is signed with a key held in a cloud hardware security module. At customer sites the TMU is under utility control |
| Sensitive data | Transformer designs, electromagnetic design calculations, and winding specifications (trade secrets); customer specifications and substation drawings under NDA; utility asset health data (FMS) and spare reservation data (STRS); certified test reports and DOE certification test data; TMU firmware source, the code signing key, and SBOMs; FCI; export classification and screening records; supplier pricing and bills of materials; material nonpublic information; employee and applicant personal information (HR, payroll, applicant tracking) |
| Cyber insurance | $100 million tower with a $10 million retention. The carrier panel supplies breach counsel, forensics, and an OT-capable response firm. The policy requires notice through the carrier hotline before incident vendors are engaged |
| Added at this size | SEC cybersecurity disclosure (Form 8-K Item 1.05; Reg S-K Item 106, 17 CFR 229.106); SOX IT general controls over the ERP, HR, and payroll; growth by acquisition (AQ-01 Ohio plant, 2025-07); two service lines offered to utilities (SL-1 and SL-2) |
| Not in scope | NERC CIP as a direct obligation (not registered). DFARS 252.204-7012 and CMMC (no DoD contracts or subcontracts; C-CRITICAL-MFG-R04). ICTS connected vehicles rule, 15 CFR Part 791 Subpart D (no vehicles or vehicle systems; C-CRITICAL-MFG-R02). Payment cards (customers pay by bank transfer). HIPAA (no such data; the employee health plan is a separate entity handled by the benefits program). CIRCIA reporting (C-CRITICAL-MFG-R01): proposed only; see P03 for how the proposed scope would treat the company. Form DOE-417 (applies to electric utilities and other entities named in its instructions, not to equipment manufacturers) |
| Regulatory driver IDs | C-CRITICAL-MFG-R01 (CIRCIA, proposed; readiness only), C-CRITICAL-MFG-R03 (EAR recordkeeping and screening), and C-CRITICAL-MFG-R04 (DFARS; not applicable, recorded once) are the vertical IDs. The primary benchmark, NIST CSF 2.0 with SP 800-82 Rev. 3, is voluntary, so rows driven only by it read "None binding; CSF 2.0 benchmark (P03 G-###)". Binding rules outside the vertical registry are cited directly: SEC Form 8-K Item 1.05 and 17 CFR 229.106; FAR 52.204-21, -23, -25, and -30; 10 CFR 429.47 and 429.71; the utility addenda ("Utility addendum sec. N (CIP-013-2 R1.2.N flow-down)"); the SL-1 and SL-2 service agreements; and state breach laws ("State breach laws (Fla. Stat. 501.171 worked example)") |
| State law approach | Breach notice for employee, applicant, and other personal information follows the law of each state where affected individuals reside. Florida (Fla. Stat. 501.171) is the worked example because the company is headquartered there and most employees live there |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors: audit committee and risk committee | The risk committee oversees cybersecurity risk (Item 106(c)(1)) and receives quarterly reporting; the audit committee oversees Internal Audit, SOX, and disclosure controls |
| Chief Executive Officer (CEO); Chief Financial Officer (CFO) | Accept Very High risk jointly; materiality determinations with the disclosure committee; ransom decisions |
| Chief Operating Officer (COO) | Owns manufacturing, supply chain, and field service; chairs the crisis management team; business owner and authorizing official equivalent for the EPSP (P02) |
| Chief Information Officer (CIO) | IT operations and the enterprise platform (common control provider); recovery lead |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee; reports to the CEO with a quarterly session with the board risk committee |
| Chief Risk Officer (CRO) | Enterprise risk management (ERM); owns the enterprise risk register and chairs the executive risk committee |
| General Counsel | Chairs the disclosure committee; contracts, utility addenda, federal clauses, and breach notice decisions with outside counsel |
| Chief Audit Executive | Heads Internal Audit (third line), reports functionally to the audit committee; leads the P07 assessment |
| Chief Compliance Officer | Regulatory compliance program (second line with the GRC team); owns the obligations register |
| Chief Technology Officer | Grid Products (TMU hardware, firmware, configuration software) and product security; business owner of the code signing service |
| GRC team (10), Security Operations Center (24x7, in-house with managed security service provider overflow), OT security team (8), Internal Audit (in-house IT audit team of 6, with a co-sourced OT specialist) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions. General Counsel (chair), CFO, Chief Accounting Officer, COO, CISO, CRO, and Vice President, Investor Relations, advised by outside securities counsel |
| Crisis management team | COO (chair), CIO, CISO, General Counsel, Chief Human Resources Officer, Vice President, Corporate Communications, Vice President, Manufacturing Engineering, and the affected plant managers |

## 3. Systems

| ID | System | Notes |
|---|---|---|
| SYS-01 | Enterprise ERP with advanced planning and scheduling (APS) | Single global instance on Cloud provider A for P1 to P6: orders, configuration and quoting, bills of materials, purchasing, inventory, shipping, export screening, finance, and the finite-capacity production schedule. **P7 (AQ-01) still runs its own legacy ERP on premises; migration due 2027-06-30** |
| SYS-02 | Identity platform (SSO, MFA, privileged access management, identity governance) | Covers about 9,400 workforce identities and 1,850 supplier and customer portal identities. **AQ-01 runs a legacy directory domain with a two-way trust to the corporate domain** |
| SYS-03 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud provider A: ERP, integration platform, PLM, central Test Data Management System, STRS portal. Cloud provider B: FMS, enterprise data platform and AI services, product build pipeline. DC-1 and DC-2: network core, engineering compute cluster, offline backup copies |
| SYS-04 | Enterprise network | SD-WAN to all sites; next-generation firewalls; network access control at 70% of office sites; an IT/OT boundary firewall and OT DMZ at P1 to P6 |
| SYS-05 | Manufacturing execution systems (MES) | One standard MES product at P1 to P6, with its application servers in each plant's OT DMZ and about 1,100 shop-floor kiosks. **AQ-01 runs a legacy MES on a server dual-homed on its office and plant networks** |
| SYS-06 | Plant control systems (OT) | About 3,900 OT assets: PLCs, CNC core cutting lines, winding machines, vapor-phase drying ovens, vacuum oil processing, robotic welding, paint lines, crane controls, and about 620 HMIs and engineering workstations. P1 to P6 are zoned behind OT DMZs with passive OT monitoring and a central secure remote access gateway for OEMs. **AQ-01 has a flat OT network and 5 always-on OEM cellular routers** |
| SYS-07 | Test systems and Test Data Management System (TDMS) | Routine test stations at every plant and high-voltage test laboratories at P2, P4, and P5. Test data replicates to the central TDMS (Cloud provider A), which produces certified test reports and holds DOE certification test data |
| SYS-08 | Plant historians | One per plant, with a read-only replica in each OT DMZ that feeds the enterprise data platform (AI-002) |
| SYS-09 | Endpoints | About 7,900 laptops and desktops, 1,100 shop-floor kiosks, and 3,200 managed mobile devices, with EDR and full-disk encryption on laptops |
| SYS-10 | Product software and firmware pipeline | SaaS code repositories, build pipeline on Cloud provider B, code signing with a cloud hardware security module, customer download portal, SBOM generation |
| SYS-11 | Fleet Monitoring Service (FMS, service line SL-1) | Cloud provider B. About 60 utility subscribers and 14,500 monitored transformers (about 2,100 made by other manufacturers). Utilities push TMU data from their own data platforms (utility-initiated, one-way, mutually authenticated TLS); **the FMS has no connection into utility networks or to TMUs** |
| SYS-12 | Spare Transformer Reserve Service platform (STRS, service line SL-2) | Member portal on Cloud provider A plus the spare asset registry in the ERP. 27 utility members; 64 spare large power and generator step-up transformers held in the 3 spare yards |
| SYS-13 | Productivity suite, HR and payroll, and applicant tracking (SaaS) | HR, payroll, and applicant tracking are SOX-relevant and hold employee and applicant personal information |
| SYS-14 | Security operations tooling | SIEM, SOAR, EDR, vulnerability scanning, OT monitoring sensors, cloud posture management |
| SYS-15 | Physical security systems | Badge access, visitor management, and about 1,600 CCTV cameras. The AQ-01 due diligence found 14 covered cameras (FAR 52.204-25); they were reported to the contracting officers within 1 business day and replaced by 2026-01-30 |
| SYS-16 | Third parties | About 2,400 active suppliers; 410 have system access or company data; 46 are Tier 1 |
| SYS-17 | AI portfolio | 14 use cases, governed by the AI governance committee formed in 2025 (P10) |

**SSP system (P02):** the *Enterprise ERP and Production Scheduling Platform (EPSP)*: the ERP and APS (SYS-01), the integration platform that links the ERP to the MES, EDI, and the TDMS, the MES application tier in the OT DMZs at P1 to P6 (SYS-05), the supplier collaboration portal, and the EPSP workload accounts in Cloud provider A; it inherits identity, network, landing zone, security operations, endpoint, facilities, HR, and third-party controls from the enterprise common control providers, and the AQ-01 legacy ERP and MES, plant OT, PLM, TDMS, FMS, and STRS are interconnected systems outside the boundary.

## 4. Current security posture: mature, with targeted gaps

**In place today:**
- A program aligned to CSF 2.0 since 2022, with a policy hierarchy of policies, standards, procedures, and exceptions
- Annual enterprise risk analysis integrated with ERM (NIST IR 8286 Rev. 1); quarterly board risk committee reporting
- 24x7 SOC with SIEM, SOAR, and EDR on 98% of IT endpoints
- Privileged access management for cloud, domain, ERP, and database administrators; FIDO2 security keys for privileged users
- Quarterly access certification for the ERP, HR, and payroll (SOX)
- Immutable backups in separate backup accounts with write-once retention; annual disaster recovery tests for tier-1 IT systems
- OT DMZs, deny-by-default IT/OT firewalls, passive OT monitoring, a central OEM remote access gateway (MFA, approval, recording), and automated controller program backups at P1 to P6 (OT program built 2023-2025)
- A product security incident response team (PSIRT), signed firmware, and a coordinated vulnerability disclosure policy
- Tiered third-party risk program
- An obligations register for the 88 utility addenda, the federal clauses, EAR, and DOE certification duties
- SOC 2 Type 2 report for the FMS (SL-1) since 2025 (Security, Availability, Confidentiality)
- SEC Item 106 disclosure in the 10-K; a disclosure committee and materiality playbook
- ISO 9001 quality system at all 7 plants; restricted-party screening of export orders; FCI kept in labeled, access-restricted project sites

**Targeted gaps:**
1. **Acquisition integration (AQ-01).** The Ohio plant runs a legacy ERP and a dual-homed MES, a flat OT network, a legacy directory with a two-way trust to the corporate domain, and 5 always-on OEM cellular routers with shared logins. It has no OT monitoring and its systems do not log to the SIEM.
2. **Recovery at scale is unproven.** The 2026-05 ERP failover test met the 15-minute RPO but took 11 hours against an 8-hour RTO. Controller program restores have been tested at only 2 of 7 plants.
3. **Legacy OT.** 148 of about 620 HMIs and engineering workstations run operating systems past vendor support (61 at AQ-01). The OT asset inventory is complete at P1 to P6 but about 55% complete at AQ-01. ICS advisory triage misses its 30-day target for about a third of applicable advisories.
4. **Product security.** SBOMs were delivered for 61% of 2026 TMU firmware releases; 1 of 9 vulnerability disclosures to addendum utilities in 2026 went out on day 38 against a 30-day term.
5. **Utility addenda operations.** 3 of 41 access-revocation notices in 2026 were late, and the incident runbook does not distinguish the 27 utilities with 24-hour notice terms from the 61 with 48-hour terms.
6. **Third parties.** 38% of Tier 2 supplier reviews are overdue; the TMU electronics contract manufacturer has never been assessed; grain-oriented electrical steel comes from 2 suppliers.
7. **Materiality.** The materiality playbook has been exercised only on an IT data breach scenario. It has no method for quantifying lost production, deferred revenue, and liquidated damages, and two of seven disclosure committee members joined in 2026.
8. **Monitoring gaps.** MES application logs at P3 and P4 and all AQ-01 systems are not in the SIEM; OT monitoring alerts at P1 to P6 reach the OT security team only during business hours.
9. **AI.** 14 AI use cases, but only 9 have completed AI governance committee review. The predictive maintenance pilot (AI-002) has a proposal to extend preventive maintenance intervals on the drying ovens, and an applicant screening feature (AI-006) was switched on by the HR software vendor without review.
10. **Assurance independence.** Internal Audit has no OT specialist on staff; the 2026 OT testing used a co-sourced specialist, and 2 of 7 plants have never had independent OT testing.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P02 SSP | Enterprise ERP and Production Scheduling Platform (EPSP), the registry's "ERP and production scheduling system", Moderate baseline with availability supplements and common control provider inheritance |
| P03 regulation | All applicable regulations across the enterprise. Primary benchmark: NIST CSF 2.0 with NIST SP 800-82 Rev. 3, as a **full profile of all 106 CSF 2.0 subcategories** with evidence sampling. Binding: SEC Form 8-K Item 1.05 and Reg S-K Item 106; FAR 52.204-21, -23, -25, and -30; the 88 utility addenda (CIP-013-2 R1.2 flow-down); DOE certification records (10 CFR 429.47, 429.71); EAR recordkeeping; state breach laws (Florida worked example). Applicability rows for CIRCIA (proposed), the ICTS connected vehicles rule, DFARS, and CIP-013-2 |
| P04 cloud | Multi-cloud (two providers, vendor-agnostic) with platform, landing zone, workload, SaaS, and colocation layers and a common control catalog; AWS, Azure, and Google Cloud names appear only in an equivalents table |
| P05 BIA | Enterprise-wide: 18 processes with dollar impact, a dependency map with third parties |
| P07 assessment | 44 controls on the EPSP and the common controls it inherits, with statistical sampling, by Internal Audit with a co-sourced OT specialist |
| P08 incident | Ransomware disrupting production of grid equipment (registry default), with the **SEC materiality assessment and Form 8-K Item 1.05 step**, the crisis management team, utility addendum notices, and multi-state employee breach notification |
| P09 SOC 2 | Type 2 readiness across two service lines offered to utilities: SL-1 Fleet Monitoring Service (fourth category added) and SL-2 Spare Transformer Reserve Service (first report) |
| P10 AI | Enterprise AI portfolio (14 use cases) with the AI governance committee; full assessment of AI-001 demand forecasting and AI-002 predictive maintenance (the registry default, kept and split into two use cases because they have different owners, data, and risks at this size) |
| Cloud | Multi-cloud, vendor-agnostic. Services are described by category |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis (plant walkthroughs 2026-06-08 to 2026-06-26, AQ-01 on 2026-06-23 and 2026-06-24; evidence sampling completed 2026-08-14) |
| 2026-07-13 to 2026-08-28 | Control assessment by Internal Audit (OT tests in Saturday maintenance windows: P2 on 2026-08-08, AQ-01 on 2026-08-15, P4 on 2026-08-22) |
| 2026-08-17 to 2026-09-04 | SOC 2 readiness for SL-1 and SL-2; AI governance committee portfolio review (2026-08-26) |
| 2026-09-08 | Executive risk committee approves the risk register, treatments, and policies |
| 2026-09-10 | Results to the board risk committee and audit committee |
| 2026-09-14 | EPSP SSP approved; authorization decision |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be specific. They do not change sections 1-6.

**Revenue by plant and day.** About 250 production days a year. Shipments per production day: P1 about $4.6 million, P2 $3.9 million, P3 $3.4 million, P4 $2.0 million, P5 $2.0 million, P7 (AQ-01) $0.8 million. P6 ships components to the other plants (internal transfers); the other plants hold about 5 production days of P6 parts. Field service and repair about $1.5 million, STRS about $0.4 million, and FMS about $0.26 million per calendar day.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Vice President, Enterprise Applications | EPSP system owner (P02); ERP, APS, and integration platform |
| ERP Platform Manager | Day-to-day EPSP administration and change control |
| Vice President, Manufacturing Engineering | Owns plant control systems standards; approves OT changes; OT incident lead with the Director of OT Security |
| Director of OT Security | OT security architecture, OT monitoring, remote access gateway, OT inventory; reports to the CISO with a dotted line to the Vice President, Manufacturing Engineering |
| Plant managers (P1 to P7) | Production, safe shutdown, and manual operations decisions at each plant |
| Director of Security Operations | Runs the SOC; incident commander for cyber incidents |
| Director of Identity and Access Management | Identity platform (SYS-02) |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, firewalls, NAC, IT/OT boundary firewalls (common control provider) |
| Director of Endpoint Engineering | Workstations, kiosks, EDR, and baselines (common control provider) |
| Director of Third-Party Risk Management | Supplier tiering, assessments, SOC report reviews (in the GRC team) |
| Director of Product Security | PSIRT, SBOMs, vulnerability disclosure to utilities, code signing operations |
| Director of Trade Compliance | Export classification, restricted-party screening, export records |
| Director of Federal Programs | Federal contract clauses, FCI handling, SAM.gov checks for FASCSA orders and covered equipment |
| Corporate Director of Quality | ISO 9001, test data integrity, DOE certification records |
| Chief Supply Chain Officer | Procurement, supplier concentration, EDI; business owner of AI-001 |
| Vice President, Digital Services | SL-1 FMS service line owner; business owner of AI-003 |
| Vice President, Spares and Services | SL-2 STRS service line owner and field service |
| Vice President, Integration Management Office | AQ-01 integration |
| Chief Human Resources Officer | Workforce onboarding, terminations, training records; business owner of AI-006 |
| Chief Accounting Officer | SOX program owner for financial reporting controls; member of the disclosure committee |
| Vice President, Investor Relations | Investor communications; member of the disclosure committee |
| Vice President, Corporate Communications | Media, customer, and employee communications during incidents |
| Vice President, Environmental Health and Safety | Process safety at the plants; member of the AI governance committee |
| Maintenance Director (corporate) | Maintenance program across the plants; business owner of AI-002 |

**AQ-01 (Ohio plant).** Acquired 2025-07-01, about 650 employees. Legacy ERP and MES (on-premises servers in the plant server room), legacy directory with a two-way trust, flat OT network, 5 always-on OEM cellular routers (2 drying ovens, 2 cast-coil molding lines, 1 vacuum pressure impregnation system). Integration plan: identity federation by 2026-12-31, OT DMZ and gateway by 2027-03-31, ERP and MES migration by 2027-06-30.

**Workforce activity (12 months to 2026-06-30).** 1,960 terminations (1,410 production), 2,110 new hires, 640 internal transfers. 41 utility access-revocation notices sent. The June 2026 phishing simulation click rate was 4.1%.

**EPSP numbers.** About 5,600 ERP users, 420 supplier collaboration portal users, about 3,800 MES users (badge and PIN) at P1 to P6, about 46,000 work orders released a month, and about 3,400 EDI documents a day. ERP database: continuous point-in-time recovery for 7 days in the ERP account, plus copies every 15 minutes of transaction logs and daily full copies to the backup account in a second region (35-day write-once retention), with a weekly copy to offline media at DC-2.

**Disaster recovery results (2026).** ERP failover test 2026-05-16: RPO met (9 minutes of data loss), RTO missed (11 hours against 8). FMS failover test 2026-04-11: met. Controller program restores tested at P1 (2025-11) and P5 (2026-03) only.

**Service lines (P09).** SL-1 FMS: SOC 2 Type 2 (Security, Availability, Confidentiality) issued for 2025 (one exception: a late access removal, remediated); subscription agreements commit to 99.5% monthly portal availability, confidentiality of utility data, and condition advisories within 24 hours of a high-severity alert. SL-2 STRS: member agreements commit to a dispatch decision within 24 hours of a qualifying emergency request, accurate spare reservation and allocation records, and confidentiality of member asset data. Five STRS members asked for a SOC 2 Type 2 report by 2027-12-31.

**Federal contracts.** The Director of Federal Programs last searched SAM.gov for FASCSA orders on 2026-02-10. FAR 52.204-30(c)(1) asks for a review at least once every three months, so the 2026-05 review was missed; the next search was done on 2026-07-21 during the gap analysis.

**Facts added for P06 to P10.**
- **Role added:** Vice President, Sales (sales and customer service; business owner of AI-007 and AI-010).
- **Exercises and testing history:** enterprise tabletop on 2026-03-24 (IT ransomware with an employee data breach; the OT-capable response firm took part). Independent OT testing: P1 (2024) and P5 (2025) by an external industrial control systems assessment firm; P2, P4, and AQ-01 by Internal Audit with the co-sourced OT specialist in 2026; P3 and P6 never (scheduled for 2027).
- **Contract notice terms (fictional):** FMS subscription agreements and STRS member agreements require notice within 72 hours of confirming unauthorized access to customer data, and STRS outage notices immediately. Tier 1 supplier security addenda require the supplier to notify the company within 72 hours of confirming an incident affecting company systems, data, or supplied components; the TMU contract manufacturer has no such term until its addendum is signed (POAM-018).
- **Service lines (P09):** SL-1 is in its second Type 2 period (calendar 2026); Processing Integrity is added for the 2027 period. SL-2's first Type 2 period is planned for 2027-04-01 to 2027-09-30.
- **AI governance committee (P10):** chaired by the Chief Technology Officer; members listed in P10 section 2. Portfolio: High 2 (AI-003, AI-006), Medium 10, Low 2; AI-006 disabled on 2026-07-14.
- **Policy set (P06):** 5 policies, 24 standards, 15 procedures, 56 policy statements; exception register IDs EXC-2026-011, -017, -018, -021, and -024 are cited as examples.
