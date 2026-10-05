# Scenario facts: Cris Santos Company | Construction | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or contract clause, the citation is given. Regulatory text was checked on eCFR (version date 2026-09-23) and the Federal Register.

## 1. The organization

| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, Inc. (publicly traded SEC registrant; not a smaller reporting company) |
| Business | Commercial and institutional building general contractor (NAICS 236220). Delivery methods: construction management at risk, design-build, and general contracting. Markets: health care, higher education, K-12 and civic, federal and defense, aviation, data centers, and commercial office. Self-performs concrete, carpentry, drywall and interiors, and general conditions. Four business units: **Building Group** (private, state, and local work), **Federal Group** (federal civilian and Department of Defense work), **Building Technology Services (BTS)** (low-voltage, video surveillance, access control, and building automation installation, plus managed services), and **Program Management Services (PMS)** (owner's representative and capital program management for institutional owners) |
| Location | Headquartered in Florida (**HQ-1**). Nine regional offices in Florida (2), Georgia, Alabama, South Carolina, North Carolina, Tennessee, Texas, and Virginia. About **300 active projects at about 140 jobsites**, each with a field office trailer; **16 jobsites are on military installations**. Two prefabrication and equipment yards: **YD-1** (Florida) and **YD-2** (Texas). Two colocation data centers: **COLO-1** (Florida) and **COLO-2** (Texas). **State breach laws are handled generically:** notify under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: about 6,600 craft workers, 2,900 project management and field supervision staff (project executives, project managers, superintendents, project engineers), 450 preconstruction and estimating staff, 600 BTS technicians and engineers, and 1,450 corporate and administrative staff (about 420 in IT and security). On a typical day about 22,000 subcontractor workers are on company jobsites |
| Revenue | About $4.8 billion a year (fictional): about $13.2 million per calendar day and $19.2 million per business day (250 business days). Gross margin about 7% (about $336 million). By unit: Building Group 70% (about $3.36 billion); Federal Group 22% (about $1.06 billion: $640 million DoD, $420 million federal civilian); BTS 5% (about $240 million); PMS 3% (about $144 million). The SBA size standard for NAICS 236220 is $45.0 million in average annual receipts (13 CFR 121.201), so the company is not small |
| Billing and payments | About **300 monthly progress payment applications (pay apps)** to owners, about **$400 million billed a month**. Private, state, and local owners pay by ACH or wire. Federal agencies pay by electronic funds transfer to the bank account in the company's SAM registration (FAR 52.232-33(b)). The company pays about **7,500 active subcontractors and suppliers** about **$300 million a month** through about 10,500 ACH payments. On federal contracts it must pay subcontractors within 7 days of receiving payment (FAR 52.232-27(c)(1)). Three treasury banks |
| Federal work | About 38 active federal contracts and task orders: 26 DoD (Army Corps of Engineers, Naval Facilities Engineering Systems Command, Air Force civil engineering) and 12 federal civilian (VA, GSA). All include FAR 52.204-21, 52.204-23, and 52.204-25. DoD contracts include DFARS 252.204-7012, -7019, and -7020. The 11 DoD awards made since 2025-11-10 include DFARS 252.204-7021: 4 design-build military construction (MILCON) contracts require **Level 2 (Self)** and 7 require **Level 1 (Self)** |
| Controlled Unclassified Information (CUI) | Federal Group design-build and MILCON projects use CUI-marked facility drawings, specifications, and site security and force protection details. CUI is allowed only in the **Federal Programs CUI Enclave (FPCE)** and in **controlled plan rooms** at the 16 installation jobsites |
| CMMC status | **FPCE: Final Level 2 (Self)**, CMMC Status Date **2026-02-27**, score 110 out of 110, affirmed in SPRS by the Affirming Official. The next annual affirmation is due by 2027-02-27 (32 CFR 170.22(a)(3)(iii)); a new Level 2 self-assessment is due within 3 years (32 CFR 170.16(a)(1)). Because Phase 2 begins **2026-11-10** (32 CFR 170.3(e)(2)) and DoD intends to require Level 2 (C3PAO) from then, a **C3PAO certification assessment is booked for 2027-01-25**. **Enterprise FCI scope** (the PDPP, the productivity suite, endpoints, and jobsite networks): **Final Level 1 (Self)**, status date 2026-01-30, affirmed annually. **AQ-2** holds its own Final Level 1 (Self) status for its legacy systems (status date 2025-12-12) until it joins the enterprise scope. **Affirming Official:** President, Federal Group (32 CFR 170.22(a)(1)) |
| Public company duties | SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (17 CFR 229.106). SOX internal control over financial reporting, including IT general controls over the ERP and payroll |
| Insurance | Cyber insurance tower of $60 million with a **$2.5 million social engineering (funds transfer fraud) sublimit**. Performance and payment bonds through two sureties |
| Acquisitions | **AQ-1:** a Texas mechanical, electrical, and plumbing (MEP) contractor acquired 2025-10 (about 900 employees). Still on its own ERP (migration due 2027-03-31), its own email tenant (migration due 2026-11-30), a legacy directory (federation due 2026-12-15), and its own accounts payable team. **AQ-2:** a Virginia federal builder acquired 2026-03 (about 400 employees) with 3 DoD contracts that carry FCI but no CUI. Joins the enterprise FCI scope by 2027-03-31 |
| Not in scope | HIPAA (BTS contracts with health care clients exclude access to clinical systems and PHI; the company is not a covered entity or business associate). PCI DSS (no card payments accepted). CCPA (no operations in California; rechecked yearly). CIRCIA reporting (final rule not published as of 2026-09-25). Classified work (no facility clearance and no classified contracts) |
| State law approach | State breach laws are handled generically (each state where affected individuals reside), with Florida (Fla. Stat. 501.171) as the worked example. Personal information in scope: employees (including certified payroll records with Social Security numbers), subcontractor worker data in jobsite badging, and owner and subcontractor contact data |

## 2. People (role titles only)

| Role | Security and compliance duties |
|---|---|
| Board of directors (audit committee; risk committee) | Cyber risk oversight (Item 106 governance). The risk committee receives quarterly cyber reporting |
| Chief Executive Officer; Chief Financial Officer | Accept Very High risks jointly; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer (COO) | Business owner for project delivery; authorizing official equivalent for the PDPP (P02) |
| Chief Information Security Officer (CISO) | Program owner; chairs the policy governance committee; recommends system authorization |
| Chief Information Officer (CIO) | IT operations; owns the enterprise platform (common control provider) |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register |
| General Counsel | Chairs the disclosure committee; engages outside counsel |
| Chief Audit Executive | Heads Internal Audit (third line); reports to the audit committee; leads the P07 assessment |
| President, Federal Group | **CMMC Affirming Official** (32 CFR 170.22); business owner of the FPCE |
| Vice President, Treasury | Owns treasury, the payment hub, bank portals, and payment verification (Payment Operations team) |
| GRC team (9, including the CMMC Program Office of 3), Security Operations Center (24x7, in-house with managed security service provider overflow), Internal Audit (in-house, co-sourced for CMMC specialists) | Three lines model |
| Disclosure committee | Form 8-K materiality decisions (General Counsel chairs) |

## 3. Systems

| ID | System | Hosting | FCI / CUI | Notes |
|---|---|---|---|---|
| SYS-01 | Enterprise project management platform: drawings, RFIs, submittals, daily logs, pay app workflow, subcontractor and owner portals | Vendor SaaS (commercial; not FedRAMP authorized) | FCI. **CUI found** on 2 DoD projects (section 4, gap 1) | About 9,200 internal and 41,000 external users (subcontractors, design teams, owners). Vendor SOC 2 Type 2 |
| SYS-02 | Construction ERP: project accounting, owner billing, accounts payable, vendor master with bank details, payment file generation | Commercial ERP, customer-managed on Cloud provider A (IaaS and managed database) | FCI | About 3,600 users; about 9,800 active vendor records. SOX IT general controls. AQ-1 still on its own ERP |
| SYS-03 | Payroll, HR, and certified payroll | Vendor SaaS | FCI (certified payrolls on federal jobs) | Employee PII including Social Security numbers and bank accounts; weekly craft payroll |
| SYS-04 | Identity platform: SSO, MFA, privileged access management (PAM), identity governance | SaaS plus on-premises directory | Identities | Phishing-resistant MFA for privileged users, Treasury, and executives; number-matching push for other users. AQ-1 on a legacy directory |
| SYS-05 | Productivity suite (email, files, chat): commercial tenant | SaaS | FCI | AQ-1 still on its own email tenant |
| SYS-06 | Treasury and payment hub: bank connectivity (secure file transfer gateway), payment approval workflow, positive pay, bank account validation service | Cloud provider A plus bank-hosted portals | No | Dual approval for all wires and for ACH batches above $250,000 |
| SYS-07 | Multi-cloud estate: Cloud provider A (ERP, integration platform, file-transfer portal, BIM/CAD virtual desktops, Capital Program Portal) and Cloud provider B (BTS monitoring platform, data platform, AI services); COLO-1 and COLO-2 | IaaS/PaaS, colocation | FCI in Cloud A workloads | Vendor-agnostic; landing zones in both clouds |
| SYS-08 | Enterprise network: SD-WAN for offices and yards; jobsite trailers on cellular routers | On-premises and carrier services | FCI in transit | About 140 jobsite trailer networks; AQ-1 sites on a legacy VPN |
| SYS-09 | Endpoints | All sites | FCI | About 11,000 laptops and desktops, 9,500 managed phones, 3,200 rugged jobsite tablets (about 18% not yet in device management), 400 jobsite kiosks and time clocks |
| SYS-10 | **Federal Programs CUI Enclave (FPCE)**: government community cloud productivity and collaboration suite, CUI document control repository, virtual desktops for BIM/CAD on CUI models, a CUI exchange gateway for subcontractors and design firms, and plan-room plotters at installation jobsites | Government community cloud offering, FedRAMP authorized at Moderate; plotters on-site | **CUI** | About 1,150 enclave users; its own CMMC SSP. Final Level 2 (Self) |
| SYS-11 | BTS managed services platform: remote monitoring and management of client access control, video surveillance, and building automation systems; client credential vault | Cloud provider B | Client facility security details; FCI for 9 federal buildings | About 420 client buildings under service contracts. Service line SL-1 (P09) |
| SYS-12 | Capital Program Portal: owner-facing program controls (budgets, pay app review, change orders, schedules, document control) | Company-built on Cloud provider A (managed containers) | Owner confidential data | About 35 institutional owner clients. Service line SL-2 (P09) |
| SYS-13 | Jobsite technology: equipment telematics, temporary cameras, drones, sensors, badging and gate access | Vendor services | None | Badging holds subcontractor worker names and photos |
| SYS-14 | Third parties | Mixed | FCI and CUI for some subcontractors | About 7,500 subcontractors and suppliers (about 640 handle FCI; 48 handle CUI) plus about 1,300 IT and service vendors (150 tier-1) |
| SYS-15 | AI portfolio (12 use cases) | Mixed | Some FCI | Governed by the AI governance committee formed in 2025 (P10) |

**SSP system (P02):** the *Project Delivery and Payment Platform (PDPP)*: the enterprise project management platform (SYS-01), the ERP project accounting, billing, accounts payable, and vendor master modules (SYS-02), the treasury and payment hub (SYS-06), and the integration platform that connects them, with interfaces to payroll (SYS-03), the identity platform (SYS-04), the productivity suite (SYS-05), and the banks. It is a Moderate system that inherits common controls from the enterprise platform, and it is the core of the enterprise FCI scope for CMMC Level 1.

## 4. Current security posture: mostly compliant, with targeted gaps

**In place today:**
- A mature program aligned to CSF 2.0, with three lines of defense
- Annual enterprise risk analysis tied to ERM (NIST IR 8286)
- A policy hierarchy of policies, standards, procedures, and exceptions
- 24x7 SOC with SIEM, EDR on about 97% of endpoints, and mailbox rule and risky sign-in alerting (except AQ-1)
- PAM and quarterly access certification
- Treasury payment controls: call-back verification of bank-account changes by the Payment Operations team (except AQ-1), a bank account validation service, dual approval for all wires, positive pay, and DMARC at reject on all company domains
- Immutable backups and annual DR tests for tier-1 systems
- Tiered third-party risk program
- Annual security awareness training with monthly phishing simulations
- Final Level 2 (Self) for the FPCE and Final Level 1 (Self) for the enterprise FCI scope
- SOC 2 Type 2 report for SL-1 (Security and Availability) since 2025
- SEC Item 106 disclosure in the Form 10-K

**Targeted gaps:**
1. **CUI outside the enclave.** CUI-marked drawings were found on the commercial project management platform (SYS-01) on 2 DoD projects, uploaded by design-team and subcontractor users. The platform is not FedRAMP authorized.
2. **CMMC drift before the C3PAO assessment.** The 2026 internal readiness check found 8 of 110 requirements no longer fully met (internal score 96). Most relate to the installation plan rooms, which the FPCE SSP did not describe as part of the boundary. Several of these requirements cannot be placed on a CMMC POA&M (32 CFR 170.21(a)(2)).
3. **Payment fraud.** In 2026-04 the AQ-1 accounts payable team changed a supplier's bank account on an email request and paid $612,000 to a fraudulent account; $455,000 was recovered through a bank recall. In 2026-06 an owner received false remittance instructions from a lookalike domain and caught them by calling back. Project managers are not yet on phishing-resistant MFA.
4. **Acquisition integration.** AQ-1 is still on its own ERP, email tenant, and legacy directory, outside enterprise payment controls and mailbox monitoring. AQ-2 holds FCI on legacy systems under its own Level 1 status.
5. **Subcontractor cyber assurance.** About 640 subcontractors handle FCI and 48 handle CUI. CMMC status and SPRS checks before subcontract award are not yet systematic (DFARS 252.204-7020(g)(2); 252.204-7021(f)(2)).
6. **Client building systems.** BTS holds administrator credentials for about 420 client buildings; vendor remote access paths and credential rotation are uneven.
7. **AI.** 12 AI use cases, but only 8 have completed committee review. The AI estimating and bid assistant has a pricing feature that pools market data across the vendor's customers.
8. **Materiality.** The disclosure committee playbook has no payment-fraud scenario and no guidance on when related occurrences should be assessed together.

## 5. Scenario choices

| Deliverable | Choice |
|---|---|
| P03 | Primary: **NIST SP 800-171 Rev. 2** (110 requirements) for the FPCE under DFARS 252.204-7012 and CMMC Level 2. Also: FAR 52.204-21 (CMMC Level 1) for the enterprise FCI scope; FAR 52.204-23 and 52.204-25; DFARS 252.204-7012, -7019, -7020, and -7021 clause duties with 32 CFR Part 170; FAR 52.232-33 and 52.232-27 payment duties; SEC Item 1.05 and Item 106; state breach and data security laws (Florida worked example) |
| P08 | **Business email compromise redirecting progress payments**, kept from the registry because payment fraud is the company's most frequent loss event. At this size it adds an **SEC materiality assessment** step (including related occurrences), a federal EFT variant, and a multi-state breach notification workflow when a compromised mailbox holds personal information |
| P09 | SOC 2 Type 2 readiness across two service lines offered to clients: **SL-1** BTS managed building technology services and **SL-2** Capital Program Portal |
| P10 | Enterprise AI portfolio (12 use cases) with a full assessment of **AI-001, the AI estimating and bid assistant**, kept from the registry because bid pricing is the company's highest-value AI use and raises federal price certification and competition issues |
| Cloud | Multi-cloud (vendor-agnostic) with common controls; the FPCE uses a FedRAMP Moderate government community cloud offering |

## 6. Assessment calendar (fictional)

| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis and gap analysis, including the FPCE internal readiness check (2026-07-06 to 2026-07-24) and plan room walkthroughs at 6 installation jobsites (2026-07-14 to 2026-07-17) |
| 2026-07-13 to 2026-08-28 | Control assessment of the PDPP (Internal Audit, third line) |
| 2026-08-21 | Gap analysis approved by the Chief Compliance Officer and the CISO |
| 2026-09-10 | Results to the audit committee and the risk committee of the board |
| 2026-09-14 | PDPP SSP approved and authorization decision |
| 2026-11-10 | CMMC Phase 2 begins |
| 2027-01-25 | C3PAO certification assessment of the FPCE |
| 2027-02-27 | Annual Level 2 (Self) affirmation due |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

**Additional roles (titles only).**
| Role | Duties in the deliverables |
|---|---|
| Chief Compliance Officer | Regulatory compliance program; second line with the GRC team; approves P03 |
| Chief Accounting Officer (Controller) | SOX program owner; financial close and SEC reporting |
| Chief Human Resources Officer | Workforce onboarding, terminations, training records; payroll owner |
| Vice President, Project Controls and Systems | **PDPP system owner**; owns SYS-01 configuration and the pay app workflow |
| Director of ERP Applications | Day-to-day ERP administration (reports to the CIO) |
| Director of Payment Operations | Bank-account change verification and payment release (reports to the Vice President, Treasury) |
| Director, CMMC Program Office | FPCE SSP, CMMC self-assessments, SPRS records (in the GRC team) |
| Director of Government Contracts | Federal clause compliance, SAM Entity Administrator, Section 889 representations, flowdowns |
| Director of Identity and Access Management | Identity platform (SYS-04) |
| Director of Security Operations | SOC, SIEM, EDR, incident commander |
| Director of Cloud Platform Engineering | Landing zones in both clouds (common control provider) |
| Director of Network Engineering | SD-WAN, jobsite networks (common control provider) |
| Director of Endpoint Engineering | Laptops, tablets, phones, and baselines (common control provider) |
| Director of Third-Party Risk Management | Vendor and subcontractor cyber assurance (in the GRC team) |
| Vice President, Integration Management Office | Integration of AQ-1 and AQ-2 |
| Vice President, Preconstruction | Estimating and bidding; business owner of AI-001 (P10) |
| Vice President, Procurement and Subcontracts | Subcontractor prequalification, buyout, and flowdowns |
| Vice President, Building Technology Services | SL-1 service line owner |
| Vice President, Program Management Services | SL-2 service line owner |
| Vice President, Safety | Jobsite safety programs and OSHA recordkeeping |
| Vice President, Corporate Communications; Vice President, Investor Relations | Incident communications; investor communications (disclosure committee member) |
| Federal project security managers (16) | One per installation jobsite; run the controlled plan room and visitor control |

**Pay app and payment volumes.** About 300 pay apps a month, average about $1.33 million; the pay app window runs from the 20th to the 25th of each month. Owner receipts average about $13.2 million per calendar day. Subcontractor and supplier payments run twice a week (about $35 million per run). Federal receipts are about $88 million a month.

**Disclosure committee membership (P08).** General Counsel (chair), CFO, Chief Accounting Officer, CISO, Chief Risk Officer, Vice President, Investor Relations, and President, Federal Group, advised by outside securities counsel.

**2026 payment fraud events.** EV-2026-04: AQ-1 supplier bank change by email; $612,000 paid, $455,000 recovered, $157,000 net loss; insurance claim under the social engineering sublimit accepted less the retention. The disclosure committee reviewed it on 2026-05-06 and recorded it as not material. EV-2026-06: an owner received false remittance instructions from a lookalike domain; no payment was made.

**Plan rooms.** Each of the 16 installation jobsites has a controlled plan room in the field office trailer with a plotter connected to the FPCE virtual desktops and locked drawing cabinets. The Federal Group plan room procedure requires escorted visitors and a visitor log. The plan rooms hold printed CUI drawing sets for the trades.

**Policy owners (P06).** POL-01 CISO (approved by the risk committee of the board); POL-02 Director of Identity and Access Management; POL-03 Director of Security Operations; POL-04 Chief Compliance Officer; POL-05 Chief Human Resources Officer (POL-02 to POL-05 approved by the executive risk committee). Policies approved 2026-09-10, effective 2026-10-01. The policy governance committee is chaired by the CISO; the Chief Audit Executive observes.

**Internal Audit assessment (P07).** An IT audit manager and three IT auditors under the Chief Audit Executive assessed 44 PDPP controls (263 determination statements). The vendor default password on the payment file transfer gateway console was found on 2026-08-12 and changed on 2026-08-13.

**SOC 2 service lines (P09).** SL-1 has issued SOC 2 Type 2 reports since 2025 (Security and Availability) and adds Confidentiality for the 2027 period. SL-2 targets its first Type 2 for 2027-04-01 to 2027-09-30. 37 SL-1 client buildings use owner-mandated remote tools (exception EXC-2026-030).

**AI governance committee (P10).** Chaired by the CIO; members include the CISO, Chief Compliance Officer, a General Counsel delegate, Chief Human Resources Officer, Vice President, Preconstruction, Vice President, Safety, Vice President, Building Technology Services, Director, CMMC Program Office, Director of Government Contracts, and the data science lead. AI-001 is used by about 120 estimators; its pooled market pricing feature was disabled on 2026-08-05. The 4 unreviewed use cases are AI-003, AI-009, AI-010, and AI-012.

**Registry adaptations.** The registry defaults were kept: the primary system is the PDPP (the registry's "project management and payment application system", widened to include the ERP and payment hub because payment integrity is the main risk); the P08 incident is business email compromise redirecting progress payments; the P10 use case is the AI estimating and bid assistant.
