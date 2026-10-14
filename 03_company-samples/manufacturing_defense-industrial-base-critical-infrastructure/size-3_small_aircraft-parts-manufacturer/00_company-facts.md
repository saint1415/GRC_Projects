# Scenario facts: Cris Santos Company | Defense Industrial Base | Small

All 11 deliverables in this folder use the facts below. The company is fictitious. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register on 2026-09-26.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLC (privately held; Cris Santos is majority owner) |
| Business | Aircraft parts manufacturer (NAICS 336413, Other Aircraft Parts and Auxiliary Equipment Manufacturing): machined structural fittings, brackets, and hydraulic manifolds for military and commercial aircraft. Quality system certified to AS9100 |
| Location | Florida. One plant: a manufacturing floor (38 CNC machines, 4 coordinate measuring machines), an engineering and office wing, and a shipping and receiving dock |
| Workforce | 250 employees: 158 production, 24 engineering (10 design, 14 manufacturing engineering and NC programming), 22 quality, 18 supply chain and shipping, 16 administration (finance, HR, contracts, sales), 8 management, 4 IT (IT Manager, 2 systems administrators, 1 manufacturing systems engineer) |
| Revenue | $68 million a year (fictional). About 58% defense (two prime contractors), 42% commercial aerospace. SBA size standard for NAICS 336413 is 1,250 employees (13 CFR 121.201), so the company is SBA-small |
| Defense customers | **Prime A** (about 40% of revenue) and **Prime B** (about 18%). The company is a subcontractor; it holds no prime DoD contract |
| Commercial customers | **Customer C**, a commercial aerospace tier-1 supplier (about 25% of revenue), plus aftermarket and repair customers |
| CUI handled | Controlled technical information (CTI) as defined in DFARS 252.204-7012(a): controlled engineering drawings, 3D models, specifications, and NC programs derived from them. It is covered defense information (CDI) and CUI. Some parts are ITAR defense articles, so their technical data is ITAR-controlled |
| Contract clauses in current subcontracts | DFARS 252.204-7012 (MAY 2024), 252.204-7019 and 252.204-7020 (NOV 2023), FAR 52.204-21 (NOV 2021). Current subcontracts were awarded before 2025-11-10 and do not include DFARS 252.204-7021 (EV-038) |
| CMMC requirement | Prime A notified suppliers (EV-039) that solicitations issued from 2026-11-10 (CMMC Phase 2, 32 CFR 170.3(e)(2)) would flow down DFARS 252.204-7021 (NOV 2025) at **CMMC Level 2 (C3PAO)**. Under 32 CFR 170.23(a)(3), that is the minimum for a subcontractor handling CUI when the prime contract requires Level 2 (C3PAO). The DoD (Department of War) CIO memorandum of 2026-07-13 suspended CMMC Phase 2, so that Level 2 (C3PAO) requirement is suspended. Until 2028-11-09 DoD includes 252.204-7021 only when a program office requires a specific CMMC level, and during the suspension requiring activities may require Level 1 (Self) or Level 2 (Self) (DoD Class Deviation 2026-O0025, Revision 3, DFARS 240.371-5). The company keeps preparing because it still owes NIST SP 800-171 Rev. 2 under DFARS 252.204-7012, and it keeps the C3PAO assessment as a voluntary choice |
| Export controls | Registered with the State Department's Directorate of Defense Trade Controls (22 CFR 122.1: one occasion of manufacturing a defense article requires registration). Some commercial parts carry EAR-controlled technology (EV-008) |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): NISPOM (32 CFR Part 117) does not apply because the company holds no facility clearance; CIRCIA reporting is proposed only; health, payment card, and consumer data rules do not apply because the company holds none beyond employee records |
| State law approach | Florida law is cited only where unavoidable (breach notice for employee personal information, Fla. Stat. 501.171). Otherwise the samples stay federal |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| President (majority owner) | Accepts High and Very High risks; approves the budget; **CMMC Affirming Official** (32 CFR 170.22) |
| Vice President of Operations | Executive owner of the security program; accepts Moderate risks; signs policies |
| Director of Engineering | CUI data owner for engineering data; owns CAD/PLM; business owner for the AI pilot (P10) |
| Quality Manager | Owns document control, travelers, and shop-floor drawing distribution |
| Contracts Manager | DFARS flowdowns, SPRS submissions, prime notifications; **ITAR Empowered Official** and export compliance lead |
| IT Manager | Security program lead; SSP and POA&M owner; incident commander |
| Systems Administrators (2) | Operate the enclave cloud tenant, identity provider, and endpoints |
| Manufacturing Systems Engineer | Operates MES, DNC, and the shop-floor network; CNC and CMM connectivity |
| Plant Manager | Shop-floor practices, visitor escort on the floor, production recovery |
| Facilities and Security Coordinator | Badges, visitor log, physical access devices |
| HR Manager | Screening, onboarding, termination notices, training records |
| Controller | ERP owner; finance; cyber insurance policy holder |
| Managed service provider (MSP) | After-hours help desk and patching for the **corporate network only**. No enclave accounts (confirmed in P03 scoping, EV-057) |
| Independent assessor | Contracted for the P07 readiness assessment; not involved in operating controls. A C3PAO will be engaged separately for a voluntary certification assessment |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | CUI? | CMMC asset category (32 CFR 170.19(c)) | Notes |
|---|---|---|---|---|---|
| SYS-01 | Enclave identity provider (single sign-on, MFA, device compliance) | Government-community cloud (SaaS) | No (identities) | Security Protection Asset | MFA for all 64 enclave accounts; hardware security keys for 4 administrators (EV-001) |
| SYS-02 | Enclave collaboration suite (CUI email, file storage, chat) | Government-community cloud (SaaS) | Yes | CUI Asset | Offering is FedRAMP authorized at Moderate or higher; customer responsibility matrix (CRM) on file (EV-043, EV-054) |
| SYS-03 | Enclave cloud subscription (IaaS/PaaS) | Government-community cloud (same provider) | Yes | CUI Asset | Hosts the PLM application and database VMs, a virtual desktop pool, the SFTP gateway VM, the log workspace, the key vault, and the backup vault |
| SYS-04 | CAD/PLM | CAD on SYS-05 workstations; PLM on SYS-03 | Yes | CUI Asset | System of record for drawings, models, and NC programs; about 41,000 controlled documents (EV-050) |
| SYS-05 | Enclave endpoints | On-premises and mobile | Yes | CUI Asset | 24 CAD workstations (engineering wing) and 16 enclave laptops (quality, program management, contracts, IT). Full-disk encryption and EDR (EV-010, EV-012) |
| SYS-06 | MES and DNC servers with 14 shop-floor terminals | On-premises (shop-floor VLAN inside the enclave boundary) | Yes | CUI Asset | Electronic travelers and work instructions with drawing views; DNC sends NC programs to machines. **Local accounts, no MFA, shared terminal logins** (EV-020) |
| SYS-07 | CNC machines (38) and coordinate measuring machines (4) | On-premises | Yes (NC programs) | Specialized Asset (operational technology) | 32 machines receive programs from DNC; **6 legacy machines are loaded by USB drive**. Controllers run vendor-embedded operating systems that cannot be patched by the company (EV-021) |
| SYS-08 | Plant enclave network | On-premises | Yes (in transit) | Security Protection Asset | Enclave firewall, engineering and shop-floor VLANs, site-to-site VPN to SYS-03, shop-floor printers |
| SYS-09 | Corporate network, commercial productivity suite, and 170 corporate endpoints | On-premises and commercial SaaS | No (policy) | Out-of-Scope Asset (must stay separated) | Commercial business, office staff, time clocks. MFA on commercial email (EV-044) |
| SYS-10 | ERP (orders, purchasing, inventory, routings, costing) | Commercial SaaS | No CUI; holds DoD purchase order data (FCI) | Out of the enclave today; **scoping position open** (EV-051, EV-061; P03 G-125) | Drawings are not stored in ERP by policy; routings reference drawing numbers only |
| SYS-11 | Payroll and HR SaaS | Commercial SaaS | No | Out-of-Scope Asset | Employee personal information (Florida breach law applies) |
| SYS-12 | CUI exchange paths | Mixed | Yes | CUI Asset (company side) | (a) Prime A supplier portal, reached from enclave virtual desktops; (b) SFTP gateway on SYS-03 used with Prime B and 3 outside processors (plating, heat treat, nondestructive testing); (c) site-to-site VPN between the plant and SYS-03. **FIPS-validated cryptography not confirmed for (b) and (c)** (EV-023, EV-013) |
| SYS-13 | Generative AI assistant | Government-community cloud add-on (proposed); public chatbots (observed) | Yes if used with engineering data | CUI Asset if enabled in SYS-02 | See P10. The add-on is not yet enabled. Three engineers used a public chatbot with CUI text (found in interviews, 2026-07-16, EV-057) |

**SSP system (P02):** the *CUI Engineering Enclave (CEE)*: SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07 (as Specialized Assets), SYS-08, and the company side of SYS-12, plus the people, printed CUI, and plant areas that handle them.

## 4. Where the evidence is

This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against NIST SP 800-171 Rev. 2 and the DFARS clauses** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07), including the plant walkthrough on 2026-08-05. Both cite evidence IDs.

## 5. Scenario choices

| Deliverable | Scenario choice |
|---|---|
| P08 incident | Exfiltration of CUI: an adversary-in-the-middle phishing page steals an engineer's enclave session token, and the attacker syncs CAD models from enclave file storage |
| P09 SOC 2 | Security-only readiness self-assessment requested by Customer C (commercial aerospace), mapped to CMMC evidence. CMMC is the primary assurance mechanism |
| P10 AI | Generative AI assistant used with CUI engineering documents: the enclave suite's integrated assistant (proposed) and public chatbots (prohibited) |
| Cloud | Vendor-agnostic. Services are described by category. The environment is a government-community cloud offering; AWS, Azure, and Google Cloud equivalents are noted only where needed |

## 6. Assessment calendar (fictional unless a regulation is cited)

| Date | Event |
|---|---|
| 2024-08-30 | SSP v1.0 and POA&M written (not updated since) |
| 2024-09-12 | SPRS Basic Assessment score of 96 posted (self-assessment) |
| 2026-06-29 to 2026-07-10 | Intake: evidence requests, exports, plant walk-through (2026-07-08), inventories, obligations register |
| 2026-07-13 to 2026-07-24 | BIA interviews, risk assessment and gap analysis fieldwork |
| 2026-07-13 | The DoD (Department of War) CIO memorandum suspends CMMC Phase 2 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2026-07-27 to 2026-07-31 | Policies, SSP v2.0 and the P08 runbook drafted from the gaps |
| 2026-08-03 to 2026-08-07 | Control assessment fieldwork (independent assessor; plant walkthrough 2026-08-05): operating tests of controls already in place; design review of the draft policies, SSP and runbook |
| 2026-08-31 | Deliverables and policies approved by the Vice President of Operations; High risks and budget approved by the President |
| 2026-09-30 | Corrected SPRS Basic Assessment score due (Contracts Manager) |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2): one calendar year after Phase 1, which began with the DFARS rule effective 2025-11-10, 90 FR 43560); suspended by the 2026-07-13 CIO memorandum |
| 2027-01 (planned) | Readiness re-check: operating effectiveness of the controls the new policies introduced, after a quarter of operation |
| 2027-02-15 to 2027-02-26 | Target window for a voluntary Level 2 certification assessment by a C3PAO |

## 7. Facts added while completing the deliverables (fictional)

| Fact | Used in |
|---|---|
| About $272,000 of shipments per production day ($68 million over about 250 production days); about 3 new part numbers start each week (EV-049, EV-050) | P05 |
| PLM daily backups have never been restore-tested; MES and DNC back up weekly to a local disk (EV-018, EV-019; SSP CP-9) | P05, P07 POAM-019 |
| One internet circuit at the plant; 2 break-glass accounts with hardware keys kept in the IT safe (EV-013, EV-001) | P01 R-024, P05 |
| Remediation budget of $185,000 for 2026 Q4 and 2027 Q1, approved by the President on 2026-08-31 | P01 |
| P07 test details: 6 disabled enclave accounts older than 1 year not removed; 9 of 31 shop-floor visits in July 2026 not logged; a commercial customer's visitor seen unescorted on 2026-08-05; printed drawings in general recycling in 4 of 6 cells; 4 USB drives with no identifiable owner at the legacy CNC machines (EV-AC-2, EV-PE-3, EV-MP-6, EV-MP-7) | P07 |
| Customer C accepts a Trust Services Criteria self-assessment (Security only) in place of a SOC 2 report (EV-052) | P09 |
| The 2026-07 public chatbot pastes (EV-057) were referred to the Contracts Manager and counsel on 2026-07-17 for the DIBNet and export disclosure decisions; the 3 engineers were briefed on CUI handling on 2026-07-24 | P10 |
| SYS-02 permission audit: 11 of 38 project sites open to all enclave users; AI assistant pre-deployment test 2026-08-17 to 2026-08-21 (44 of 50 correct; 2 wrong numeric values; scanned legacy drawings 60%) (EV-065) | P10 |
