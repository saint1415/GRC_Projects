# Scenario facts: Cris Santos Company | Defense Industrial Base | Mid-Market

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (privately held; private equity-backed since 2023; board with an audit committee) |
| Business | Aircraft parts manufacturer (NAICS 336413, Other Aircraft Parts and Auxiliary Equipment Manufacturing): machined structural fittings, hydraulic manifolds and valve bodies, sheet-metal subassemblies, and metal additively manufactured brackets for military and commercial aircraft. Quality system certified to AS9100. A small additive and engineering services line (launched 2026) prints and engineers parts for commercial customers |
| Location | Florida only. **Plant 1** (headquarters): machining (64 CNC machines, 8 coordinate measuring machines), the engineering center, and a hydraulic test lab with 6 test stands. **Plant 2** (acquired 2024-10-01 from a smaller supplier, about 90 miles away): sheet-metal and assembly lines, 26 CNC machines, 4 coordinate measuring machines, 6 metal additive printers, and a machine-vision inspection cell |
| Workforce | 850 employees: 500 production, 90 engineering (38 design, 32 manufacturing engineering and NC programming, 8 additive engineering, 12 test engineering), 75 quality, 60 supply chain and logistics, 75 administration (finance, HR, contracts and trade compliance, sales, program management, legal), 28 management, 22 IT and security. About 590 work at Plant 1 and headquarters, 260 at Plant 2 |
| Revenue | About $240 million a year (fictional). About 62% defense (three prime contractors) and 38% commercial. The SBA size standard for NAICS 336413 is 1,250 employees (13 CFR 121.201), so the company is still SBA-small. It is sized as Mid-Market by the tier rule (500-999 employees, Census SUSB class) and flagged as such |
| Defense customers | **Prime A** (about 28% of revenue, military transport aircraft structures), **Prime B** (about 20%, fighter aircraft hydraulic components), **Prime C** (about 14%, unmanned aircraft brackets and fittings). The company is a subcontractor. It holds no prime DoD contract |
| Commercial customers | **Customer D**, a commercial airframe manufacturer (about 18%); **Customer E**, a commercial tier-1 supplier (about 9%); aftermarket and spares (about 7%); the additive and engineering services line (about 4%, three commercial customers) |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): controlled drawings, 3D models, specifications, NC programs, additive build files, and test procedures derived from them. It is covered defense information (CDI) and CUI. Parts for Prime A and Prime B are ITAR defense articles, so their technical data is ITAR-controlled |
| Contract clauses in current subcontracts | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021). All current subcontracts were awarded before 2025-11-10 and do not include DFARS 252.204-7021 |
| CMMC requirement | All three primes notified suppliers that solicitations issued from 2026-11-10 (CMMC Phase 2, 32 CFR 170.3(e)(2)) will flow down DFARS 252.204-7021 (NOV 2025) at **CMMC Level 2 (C3PAO)**. Under 32 CFR 170.23(a)(3), that is the minimum for a subcontractor handling CUI when the prime contract requires Level 2 (C3PAO). Prime A's next production lot solicitation is expected in 2027 Q1, with award in 2027-06 |
| Export controls | Registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1). A technology control plan limits ITAR technical data to U.S. persons. Customer D and Customer E parts carry EAR-controlled technology. Two foreign-national engineers in the commercial engineering group work only on data the Director of Trade Compliance and Contracts classified as not needing a license (classification records on file); they have no enclave accounts |
| Not in scope | Classified information: no facility clearance, so NISPOM (32 CFR Part 117) does not apply. CIRCIA reporting: the final rule is not published (proposed only). SEC cyber disclosure: the company is privately held. Health, payment card, and consumer data: none beyond employee records |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board audit committee | Quarterly cyber risk and CMMC readiness reporting |
| Chief Executive Officer | Accepts High risk; approves the security budget and risk appetite; **CMMC Affirming Official** (32 CFR 170.22) |
| Chief Operating Officer | Executive sponsor of the security program; **system owner** of the CUI Engineering Enclave; accepts Moderate risk; approves policies |
| Chief Financial Officer | ERP owner; cyber insurance policy holder |
| General Counsel | Legal privilege during incidents; contract and export counsel liaison; breach decisions for employee personal information |
| Virtual CISO (vCISO, part-time contractor) | Program strategy; risk appetite; board reporting |
| IT Director | Infrastructure, cloud landing zone, networks, and recovery lead |
| Security Manager, 2 security analysts, and 1 GRC analyst | Security operations; SSP and POA&M owner (Security Manager); incident commander; MSSP liaison; risk register, evidence, and SPRS score calculation (GRC analyst) |
| Director of Engineering | CUI data owner for engineering data; owns CAD/PLM; business owner of AI-001 |
| Vice President of Operations, Plant 1 Manager, Plant 2 Manager | Shop-floor practices, production recovery, visitor escort on the floor; business owner of AI-003 |
| Director of Quality | Document control, travelers, printed CUI on the shop floor; business owner of AI-002 |
| Director of Trade Compliance and Contracts | DFARS flowdowns, SPRS submissions, prime notifications, DIBNet reporting lead; **ITAR Empowered Official**; technology control plan |
| Manufacturing Systems Manager and 3 manufacturing systems engineers | MES, DNC, CNC, CMM, additive printer, and test lab connectivity (operational technology) |
| Director of Supply Chain | Supplier onboarding, purchase order terms, outside processors |
| HR Director | Screening, onboarding, terminations, training records; business owner of AI-005 |
| Facilities and Security Manager | Badges, visitor management, cameras at both plants |
| Director of Additive and Engineering Services | Owner of the commercial services line in the SOC 2 scope (P09) |
| Internal audit (co-sourced firm) | Annual IT audit; performed the P07 control assessment. Reports to the audit committee and does not operate any control |
| Managed security service provider (MSSP) | 24x7 managed detection and response and SIEM. An External Service Provider that handles Security Protection Data (32 CFR 170.19(c)(2)) |
| C3PAO | To be engaged separately for the Level 2 certification assessment. Independent of the internal audit firm |

## 3. Systems

| ID | System | Hosting | CUI? | CMMC asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | Enclave identity provider (single sign-on, MFA, device compliance) | Government-community cloud (SaaS) | No (identities) | Security Protection Asset | 318 enclave accounts: 290 named users, 12 administrators, 4 break-glass, 12 service accounts. Hardware security keys for administrators |
| SYS-02 | Enclave collaboration suite (CUI email, file storage, chat) | Government-community cloud (SaaS) | Yes | CUI Asset | FedRAMP authorized at Moderate or higher; customer responsibility matrix (CRM) on file |
| SYS-03 | Enclave cloud landing zone: 4 accounts (security and identity, shared services, workloads, backup) | Government-community cloud (IaaS/PaaS, same provider) | Yes | CUI Asset (workloads, backup); Security Protection Asset (security account, log pipeline) | Shared services: network hub, VPN gateways, virtual desktop pool (120 sessions), managed file transfer (MFT) gateway. Workloads: PLM application and database, CAD license servers, additive build preparation server, test data repository |
| SYS-04 | CAD/PLM | CAD on SYS-05 workstations; PLM in SYS-03 | Yes | CUI Asset | System of record for about 165,000 controlled documents (drawings, models, NC programs, build files, test procedures) |
| SYS-05 | Enclave endpoints | On-premises and mobile | Yes | CUI Asset | 120 CAD workstations and 110 enclave laptops. Full-disk encryption and EDR |
| SYS-06 | MES and DNC servers with 60 shop-floor terminals | On-premises, both plants | Yes | CUI Asset | **Plant 1:** current MES with single sign-on and badge plus PIN, 40 terminals. **Plant 2:** legacy MES and DNC on a server operating system past end of vendor support, 20 terminals with **shared logins** |
| SYS-07 | Operational technology: 90 CNC machines, 12 CMMs, 6 metal additive printers, 6 hydraulic test stands with data acquisition PCs, machine-vision inspection cell | On-premises, both plants | Yes (NC programs, build files, test data) | Specialized Assets | 82 CNC machines receive programs from DNC; **8 legacy machines at Plant 2 are loaded by USB drive**. Additive printer vendor connects through its own remote support tool |
| SYS-08 | Plant enclave networks and SD-WAN | On-premises | Yes (in transit) | Security Protection Asset | Enclave firewalls, engineering and shop-floor VLANs, SD-WAN between plants, site-to-cloud VPN. **Plant 2 shop floor is not separated from the Plant 2 corporate network** |
| SYS-09 | Corporate network, commercial productivity suite, and about 410 corporate endpoints | On-premises and commercial SaaS | No (policy) | Out-of-Scope Asset (must stay separated) | Commercial business, office staff, time clocks. MFA on all corporate accounts |
| SYS-10 | ERP (orders, purchasing, inventory, routings, costing) | Commercial SaaS | No CUI; holds DoD purchase order data (FCI) | Out-of-Scope Asset (attachments disabled since 2025; routings cite drawing numbers only) | FAR 52.204-21 applies |
| SYS-11 | Payroll, HR, and applicant tracking SaaS | Commercial SaaS | No | Out-of-Scope Asset | Employee personal information (Florida breach law applies). Includes the applicant ranking feature (AI-005) |
| SYS-12 | CUI exchange paths | Mixed | Yes | CUI Asset (company side) | (a) Prime A supplier portal, reached from enclave virtual desktops; (b) MFT gateway in SYS-03 used with Prime B, Prime C, the three services customers, and 22 suppliers and outside processors (FIPS mode on); (c) site-to-cloud VPN from both plants and the SD-WAN tunnel between plants. **FIPS-validated mode not confirmed on the Plant 2 SD-WAN appliance** |
| SYS-13 | SIEM and 24x7 managed detection and response | MSSP-operated, hosted in a government-community cloud region | Security Protection Data | Security Protection Asset (ESP services) | Covers SYS-01, SYS-02, SYS-03, enclave and corporate endpoint EDR, and Plant 1 firewalls. **Not covered:** MES and DNC at both plants, Plant 2 network, OT |
| SYS-14 | AI tools | Various | Varies | See P10 | AI-001 enclave generative AI assistant (pilot), AI-002 machine-vision inspection, AI-003 CNC predictive maintenance, AI-004 corporate generative AI assistant, AI-005 applicant ranking, AI-006 public chatbots (prohibited) |

**SSP system (P02):** the *CUI Engineering Enclave (CEE)*: SYS-01 to SYS-08, the company side of SYS-12, and the MSSP services in SYS-13 (as Security Protection Assets), plus the people, printed CUI, and plant areas at both plants that handle CUI. Moderate baseline with tailoring.

## 4. Current security posture: defined program with gaps in scale

**In place today:**
- A CUI enclave in a government-community cloud whose offering is FedRAMP authorized at Moderate or higher, built in 2025 as a 4-account landing zone, with the provider's CRM on file (DFARS 252.204-7012(b)(2)(ii)(D))
- MFA for all enclave and corporate accounts; hardware security keys for administrators
- U.S.-person verification before enclave access (technology control plan)
- EDR on all managed endpoints, with 24x7 MSSP monitoring and SIEM for the cloud enclave, identities, endpoints, and Plant 1 firewalls
- Immutable backups of cloud workloads in a separate backup account (35-day write-once retention); Plant 1 MES and DNC back up nightly to the same account
- SSP v3.0 and POA&M dated 2025-05-30 (Plant 1 scope only)
- SPRS Basic Assessment score of **74** (self-assessment), posted 2025-06-12, covering Plant 1 only
- Policies adopted in 2024, with standards for cloud configuration, encryption, and endpoints
- Quarterly authenticated vulnerability scanning of cloud workloads and endpoints
- Annual security awareness training plus CUI handling training (since 2025)
- Annual co-sourced internal IT audit
- Two DoD-approved medium assurance certificates for DIBNet reporting (Director of Trade Compliance and Contracts, Security Manager)
- DDTC registration, technology control plan, and badge access at both plants

**Missing or weak, found in the 2026 assessments:**
1. Plant 2 is not integrated. Its shop floor shares a network with its corporate segment, its MES uses shared logins, its visitor log is on paper and incomplete, and it was excluded from the 2025 SSP and SPRS score (3.13.1, 3.5.1, 3.10.4).
2. The Plant 2 MES and DNC servers run an operating system past end of vendor support, and 8 legacy CNC machines are loaded by USB drive (3.14.1, 3.8.7).
3. MES, DNC, OT, and Plant 2 network logs do not reach the SIEM. MSSP coverage stops at the cloud, identities, endpoints, and Plant 1 firewalls (3.3.1, 3.14.6).
4. Vulnerability scanning is quarterly and excludes the MES and DNC servers at both plants and all Plant 2 systems (3.11.2).
5. Supplier flowdown: 22 suppliers and outside processors receive CUI. 9 hold legacy purchase orders without current DFARS 252.204-7012 and 252.204-7020 terms, and the SPRS or CMMC status of 14 has not been verified (252.204-7012(m); 252.204-7020(g)).
6. The 2025 SPRS score (74) excluded Plant 2 and was not updated after the acquisition. The 2026 recalculation is lower (P03).
7. Recovery: Plant 2 MES and DNC back up weekly to a local storage device in the same room; no MES restore has been tested at either plant; the PLM restore was last tested in 2025-04.
8. Configuration baselines and change control cover the cloud and endpoints only. OT servers and shop-floor terminals have neither (3.4.1 to 3.4.3).
9. FIPS-validated cryptography is not confirmed on the Plant 2 SD-WAN appliance, which carries CUI between the plants (3.13.11).
10. The MSSP is not documented in the SSP as an External Service Provider, and its customer responsibility matrix is incomplete (32 CFR 170.19(c)(2)(ii)).
11. AI tools were adopted without review: the enclave generative AI assistant pilot (20 users since 2026-05), a predictive maintenance gateway that streams CNC telemetry from the Plant 1 shop-floor VLAN to a vendor's commercial cloud, and an applicant ranking feature turned on by the HR vendor's default settings (P10).
12. Incident response was exercised only for ransomware (2025 tabletop). There has been no CUI exfiltration exercise and no DIBNet drill since 2024, and the image preservation procedure covers cloud systems only (3.6.3; 252.204-7012(e)).
13. Printed CUI at Plant 2 is not marked, stored, or destroyed as CUI (3.8.1 to 3.8.4).
14. Enclave access reviews are semiannual, not quarterly. Additive printer vendor remote access uses the vendor's own tool, outside company control (3.1.1, 3.7.5).

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 | **Two incident types:** (1) exfiltration of CUI, in which an adversary-in-the-middle phishing page steals an engineer's enclave session and the attacker stages PLM exports and drawings through the virtual desktop pool, with a variant for a CUI breach at a supplier; and (2) ransomware on the Plant 2 shop floor (MES, DNC, OT). Integrated with crisis management and legal |
| P09 | Readiness for a SOC 2 Type 2 examination (Security, Availability, Confidentiality) of the additive and engineering services line, required by its three commercial customers by 2027-12-31. CMMC stays the primary assurance mechanism for defense work. Includes a vendor assurance review program |
| P10 | AI use-case portfolio: AI-001 enclave generative AI assistant used with CUI engineering documents (the registry use case), AI-002 machine-vision inspection, AI-003 CNC predictive maintenance, AI-004 corporate generative AI assistant (no CUI), AI-005 applicant ranking, AI-006 public chatbots (prohibited) |
| Cloud | Multi-account landing zone in a government-community cloud, vendor-agnostic. Services are described by category; AWS, Azure, and Google Cloud equivalents are noted only in an equivalents table |

The registry defaults (primary system, CUI exfiltration incident, generative AI with CUI) fit this business at this size and are kept. The mid-market depth adds a second plant, a second incident type, and an AI portfolio.

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2024-10-01 | Plant 2 acquired |
| 2025-05-30 | SSP v3.0 and POA&M written (Plant 1 scope) |
| 2025-06-12 | SPRS Basic Assessment score of 74 posted (self-assessment, Plant 1 scope) |
| 2026-07-06 to 2026-07-31 | Risk assessment and gap analysis fieldwork |
| 2026-08-03 to 2026-08-21 | Control assessment by the co-sourced internal audit firm (plant walkthroughs 2026-08-11 to 2026-08-13) |
| 2026-09-17 | Results to the audit committee. Deliverables approved by the Chief Operating Officer; High risks, risk appetite, and budget approved by the Chief Executive Officer |
| 2026-09-30 | Corrected SPRS Basic Assessment score due (Director of Trade Compliance and Contracts) |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2027-03-08 to 2027-03-19 | Target window for the Level 2 certification assessment by a C3PAO |

## 7. Facts added while completing the deliverables (fictional)

| Topic | Added fact | Used in |
|---|---|---|
| Revenue split | Plant 1 machined parts about $132 million, Plant 2 assemblies and additive parts about $98 million, services line about $10 million, over about 250 production days: about $528,000, $392,000, and $40,000 of shipments per production day | P05, P01 |
| Cyber insurance | $15 million aggregate limit, $500,000 retention. The carrier's panel supplies breach counsel and forensics; notice goes through the carrier hotline before vendors are engaged | P01, P08 |
| MSSP terms | Call to the Security Manager within 30 minutes of a high-severity alert; the SIEM keeps 1 year of searchable logs | P02, P08 |
| Workforce activity | 96 terminations and 41 internal transfers in the 12 months to 2026-06-30; the last enclave access review was completed 2026-02-27; the June 2026 phishing simulation click rate was 6.1% | P07 |
| Budget | FY2027 security plan approved by the Chief Executive Officer on 2026-09-17: $1.62 million one-time and $540,000 a year | P01 |
| Services line | About 30 build and engineering jobs a month for three commercial customers; their files arrive and leave through the MFT gateway and are processed in the enclave | P05, P09 |
| Vendors | About 60 IT, OT, and service vendors have access to company systems or data; 12 are Tier 1 under the P09 tiering approach | P09 |
