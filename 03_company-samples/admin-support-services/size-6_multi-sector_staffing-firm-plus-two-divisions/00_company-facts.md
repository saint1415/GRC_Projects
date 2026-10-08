# Scenario facts: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or standard, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; holding company of a workforce group) |
| Structure | A holding company with three divisions and corporate shared services ("the group"). The divisions are separate subsidiaries under common ownership |
| Division 1: Staffing (NAICS 561320), **focus of this scenario** | Temporary staffing in four lines: **Commercial** (light industrial, warehouse, office; about 58% of division revenue), **Professional** (IT, finance and accounting; about 21%), **Healthcare Staffing** (travel and per diem nurses and allied health clinicians at hospitals and post-acute providers; about 15%), and **Managed Workforce Solutions** (managed service provider programs that run clients' contingent workforce on a vendor management system; about 6%). About 14,000 internal employees. The W-2 employer of record for its temporary associates |
| Division 2: Professional Services and Consulting (NAICS 541512, sector 54) | **Health IT Advisory** (EHR implementation, revenue cycle and interim management for hospitals and health systems), **Workforce and HR Technology Consulting** (HR and payroll system implementations for corporate clients), and **Federal Solutions** (IT service desk and HR systems support for federal civilian agencies). About 9,000 employees. A HIPAA **business associate** of its hospital clients (45 CFR 160.103, "business associate" (1)(ii): consulting and management services that involve disclosure of PHI) |
| Division 3: Home Health (NAICS 621610, sector 62) | Medicare-certified home health agencies providing skilled nursing, therapy, and aide visits in patients' homes. About 18,000 employees. A HIPAA **covered entity** (a health care provider that bills Medicare and other payers electronically). Medicare home health conditions of participation apply (42 CFR Part 484). Acquired in 2023 |
| Corporate shared services | Identity, network, security operations, cloud, the Group Workforce Platform (payroll, HR, and talent acquisition for every division), finance, legal. About 4,000 employees |
| Location | Headquartered in Florida. Staffing operates in 44 states and the District of Columbia; Consulting serves clients in 38 states and federal agencies; Home Health operates in 5 southeastern states. **State law handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 core employees (Staffing 14,000; Consulting 9,000; Home Health 18,000; corporate 4,000). In addition, Staffing employs about **230,000 temporary associates** on assignment in an average week (about 860,000 different associates paid in 2025). About $18.0 billion revenue (fictional) |
| Intra-group relationships | Healthcare Staffing places about 1,100 per diem clinicians a week with Home Health under an intercompany staffing agreement; they work under Home Health's direct control and are part of its workforce (45 CFR 160.103, "workforce"). Consulting's Health IT Advisory team implemented the Home Health EHR in 2024. Corporate pays every W-2 worker in the group through the Group Workforce Platform |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23 and 52.204-25) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. Sources: SRC-FAR-RFO-PART40 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC disclosure controls |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer | Group standards, common controls, and the group risk register |
| Group General Counsel | Contracts, intercompany agreements, the notification matrix; chairs the disclosure committee |
| Division security and compliance leads (3) | Division registers, division supplements, division-specific regulators |
| Home Health HIPAA Privacy Officer and HIPAA Security Officer | Designated by the covered entity (45 CFR 164.308(a)(2); 164.530(a)) |
| Consulting HIPAA compliance officer | Business associate program: BAAs, client notices, consultant access to client systems |
| Staffing Vice President, Employment Compliance | Form I-9, E-Verify, FCRA background screening, and records retention for the group's hiring |
| Group internal audit | Assesses common controls once; samples division controls; reports to the board audit committee |
| Disclosure committee | SEC materiality decisions |
| Group AI council | Approves High-tier AI use cases (P10) |

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform (SSO, MFA, PAM, identity governance) | Corporate |
| SYS-G2 | Group SOC, SIEM, and EDR (24x7, in-house with managed security service provider overflow) | Corporate |
| SYS-G3 | Group cloud platform (two providers, vendor-agnostic), SD-WAN to about 650 sites, and endpoint management | Corporate |
| SYS-G4 | Group Workforce Platform (GWP): the shared payroll and applicant tracking platform: talent acquisition (ATS, career sites, AI ranking add-on), onboarding and electronic Form I-9, clinician credentialing, the payroll and pay delivery engine, and the time and visit-pay intake | Corporate |
| SYS-D1 | Staffing front office: client CRM and portals, client vendor management system (VMS) integrations, branch lobby kiosks, on-site time clocks, recruiting contact center, and the Managed Workforce Solutions VMS tenant | Staffing |
| SYS-D2 | Consulting delivery systems: engagement and document management, consultant laptops (used to reach client EHRs), and the Federal Solutions enclave for federal contract information | Consulting |
| SYS-D3 | Home Health clinical system: home health EHR (vendor-hosted), point-of-care tablets, scheduling and electronic visit verification, OASIS submission, and billing | Home Health |

**SSP system (P02):** the *Group Workforce Platform (GWP)*: the shared payroll and applicant tracking platform (SYS-G4) operated by corporate shared services for all three divisions, covering talent acquisition, onboarding and electronic Form I-9, clinician credentialing, payroll and pay delivery, and time and visit-pay intake, and inheriting common controls from SYS-G1 to SYS-G3.

## 4. Current security posture: a defined program, mature in Staffing, weaker in the acquired Home Health division
**In place today:**
- Group policies aligned to CSF 2.0 (2025) and a common control catalog
- 24x7 group SOC with SIEM and EDR on managed laptops and servers
- SSO with MFA for all workforce applications; PAM for administrators
- Quarterly access certification for SOX and tier-1 applications
- Immutable backups for cloud workloads in a separate backup account
- SSN and bank account tokenization inside the payroll engine
- Electronic Form I-9 and E-Verify for all new hires in every division
- An annual NYC Local Law 144 bias audit of the AI ranking tool (NYC requisitions only)
- Consulting business associate program with signed BAAs for all hospital clients; a Federal Solutions enclave for federal contract information
- Home Health annual HIPAA risk analysis and an emergency preparedness program
- SEC Reg S-K Item 106 disclosure in the annual report

**Gaps:**
1. **Visit-pay feed carries PHI into the GWP.** Home Health pays field clinicians per visit. Since 2024-04 the scheduling system has sent each visit record to the GWP with the patient's name, address, visit date, and visit type. No minimum-necessary review was done, the intercompany BAA does not cover payroll, and about 640 payroll users can view the records.
2. **Payroll diversion.** Associates change direct deposit accounts in the self-service app after an SMS one-time code. In 2025, 690 fraudulent changes diverted about $1.9 million of pay, which the group repaid.
3. **Home Health integration and policy drift.** Home Health's supplement was last aligned to group policy in 2023. About 11,500 field tablets sit in a legacy device management tool, and group EDR covers 72% of them.
4. **AI in hiring.** The AI ranking add-on scores applicants for all three divisions. Only NYC requisitions have a bias audit; there is no group-wide adverse impact monitoring, and the Colorado and California duties that start 2027-01-01 are not designed.
5. **Shared incident notification.** A GWP incident would trigger state breach laws in most states, the E-Verify MOU notice to DHS, HIPAA notices for Home Health, client contract notices, and an SEC materiality decision. The single notification matrix has not been exercised.
6. **Common control inheritance** is documented for Staffing and Consulting but not for Home Health.
7. **Consulting access to client systems.** About 6,300 client-issued accounts (EHRs and other client systems) are not inventoried centrally; client notices at consultant roll-off are late; client PHI is saved in the engagement document repository without classification.
8. **E-Verify and I-9 access.** About 1,400 E-Verify user accounts sit outside SSO, and the 2026 Q2 review found 52 accounts of departed users. The scanned paper I-9 archive (2009-2016) has no access audit trail.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | Per division. **Staffing:** NIST CSF 2.0 (voluntary benchmark, all 106 subcategories) plus the binding rules for its records (Form I-9, E-Verify MOU, Fla. Stat. 448.095 worked example, FCRA, the Disposal Rule, ADA medical files, NYC Local Law 144). **Consulting:** HIPAA business associate duties and FAR 52.204-21, with an applicability test of the FTC Safeguards Rule. **Home Health:** the HIPAA Security Rule (covered entity) with selected Privacy and Breach Notification rows, Medicare home health conditions (42 CFR 484.102, 484.110), and Section 1557 (45 CFR 92.210). **Group-wide:** SEC rules, state breach and data security laws, CCPA for California workers and applicants, Colorado SB26-189. Regulation-by-division matrix in the report |
| Regulatory driver labels | `N56-BM (...)` is the P03 voluntary benchmark (NIST CSF 2.0) with the subcategory in parentheses; it is a scenario label, not a row in `requirements.csv`. `N56-R01` to `N56-R09` cite this vertical's requirements with the specific section. Consulting rows cite `N54-R0x` and Home Health rows cite `N62-R0x` from those divisions' industry rules. `E-Verify MOU Art. II.A.x` cites the MOU for Employers (revision 06/01/13). `SEC 8-K 1.05` and `SEC S-K 106` cite Form 8-K Item 1.05 and 17 CFR 229.106 |
| P08 | A breach of the Group Workforce Platform exposing worker PII from all three divisions, plus Home Health patient data from the visit-pay feed: a multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: Staffing's Managed Workforce Solutions program is in scope (first Type 2 readiness); Consulting and Home Health are out of scope, with reasons |
| P10 | Group AI governance program: group standard, division use cases, and the regulator-specific rules (employment discrimination law and state AI laws for hiring tools; Section 1557 for Home Health; client BAAs for Consulting) |
| Cloud | Shared corporate platform on two providers plus division workloads, vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-01 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-01 to 2026-08-31 | Common control assessment (group internal audit) plus division samples |
| 2026-09-10 | Results to the board risk committee; deliverables approved |

## 7. Facts added while building the deliverables (Phase 5)
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Registry defaults | Kept. The primary system (payroll and applicant tracking system) is the GWP, a shared corporate system, because at this size one platform pays and hires for every division. The incident (payroll and HR system breach exposing worker PII) is kept and widened to all divisions. The AI use case (AI resume screening and candidate ranking) is kept as AI-001 inside a group portfolio |
| Revenue split (fictional) | Staffing about $13.5 billion (about $37 million per calendar day); Consulting about $2.7 billion (about $10.4 million per business day); Home Health about $1.8 billion (about $4.9 million per calendar day). Total about $18 billion, as in section 1 |
| Risk acceptance | Low: division security and compliance lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. High patient-safety risks and High risks that would leave workers unpaid must be treated, not accepted |
| Staffing scale | About 520 sites in 44 states and DC: 390 branches (kiosks segmented at 329; on the staff network at 61 legacy branches) and 130 on-site offices at client facilities. About 14,000 active clients, including about 620 hospital and post-acute clients. About 28,000 Healthcare Staffing clinicians on assignment a week. Requisitions in New York City, Illinois, Colorado, and California |
| Hospital client contracts | 214 hospital staffing agreements contain BAA or confidentiality terms; counsel treats them as contract duties because placed clinicians are the hospital's workforce. Shortest incident notice term: 48 hours |
| Hiring volumes | About 3.1 million applications a year group-wide; about 640,000 hires a year (about 610,000 of them Staffing associates), about 2,500 per business day; about 430,000 employment background checks a year through two screening providers |
| E-Verify | Each employing entity (the Staffing, Consulting, and Home Health subsidiaries and corporate) has its own E-Verify MOU for Employers; the Consulting entity is also enrolled as a Federal contractor (MOU Art. II.B; FAR 52.222-54). About 1,400 named users work from 9 onboarding centers |
| GWP scale | About 9,600 staff users (recruiters about 6,100; onboarding and compliance about 1,400; payroll about 640; credentialing about 380; HR and associate service about 900; administrators about 180); about 1.1 million self-service accounts; about 7.2 million candidate profiles; about 3.4 million current and former worker records with SSNs and bank accounts (since 2014); about 1.9 million electronic Forms I-9 (since 2017) and about 0.9 million scanned paper forms (2009-2016) in the I-9 archive; credential files for about 96,000 clinicians; 41 integration service accounts |
| Visit-pay feed | Live since 2024-04. Each Home Health visit record sent to the GWP carries patient name, address, visit date, and visit type, for about 214,000 patients so far; copies sit in the payroll engine and the workforce data hub |
| Payroll calendar | Clients approve associate time by Monday 18:00; payroll runs Wednesday; associates are paid Friday (about $190 million a week) by direct deposit or paycard through two ACH originating banks and a paycard program manager. Core employees are paid every two weeks |
| GWP hosting | Provider A hosts the corporate hub, the payroll engine and tokenization service, the integration platform, the workforce data hub, the I-9 archive, and the Home Health visit-pay interface. Provider B hosts the GWP DR replica (warm standby; last DR test 2026-02), the backup vault, and the Federal Solutions enclave. The ATS, onboarding and I-9 service, and credentialing service are vendor SaaS. Last GWP penetration test 2026-03 |
| Intercompany BAA | Corporate and Home Health signed a BAA in 2023-10 covering IT hosting, identity, SOC, and EHR integration services. It does not cover payroll |
| Managed Workforce Solutions | MSP programs for 48 clients and about 1,900 suppliers on a vendor VMS tenant that the division configures and operates (about 160 program staff). Some program workers are payrolled through the GWP. All MSP contracts require incident notice within 48 hours; 31 require a SOC 2 Type 2 report by 2027-12-31 |
| Consulting scale | Health IT Advisory about 4,200 consultants serving about 160 hospital and health-system clients under BAAs (23 negotiated 72-hour breach notice; standard term 10 business days); Workforce and HR Technology Consulting about 3,100; Federal Solutions about 1,700 on 11 federal civilian prime contracts and 4 subcontracts (no DoD; no CUI designated). About 6,300 client-issued accounts; about 240 independent subcontractors. Counsel memo (2026-07): Consulting is not a financial institution under 16 CFR 314.2(h)(1) |
| Home Health scale | 64 Medicare-certified agency locations in 5 southeastern states (29 in Florida); average daily census about 30,000; about 140,000 admissions and 3.6 million visits a year; about 11,000 field clinicians with about 11,500 tablets (EDR on 72%); vendor-hosted EHR; state Medicaid EVV interfaces. Bills Medicare and Medicaid. No operations in California or New York City |
| Division supplements | Staffing v2026 (aligned 2026-06-20); Consulting v2026 (aligned 2026-07-15); Home Health v2023 (written at acquisition) |
| Employment compliance evidence | Standalone FCRA disclosure since 2024; quarterly I-9 self-audit of 300 forms; mock I-9 inspection 2026-06 (50 forms retrieved in 1 business day) |
| AI portfolio (P10) | AI-001 resume screening and ranking (ATS add-on, all divisions, since 2025-05; auto-advance at 75 and above on Commercial requisitions since 2025-09; NYC bias audit 2026-04); AI-002 recruiting assistant with knockout questions; AI-003 clinician shift matching and pay-rate recommendation; AI-004 bank-change fraud scoring (pilot since 2026-07); AI-005 Home Health hospitalization risk model (EHR vendor, since 2025); AI-006 ambient documentation pilot in 6 agencies; AI-007 consultant drafting assistant; AI-008 claim denial-prediction model for 9 hospital clients; AI-009 enterprise generative AI pilot (3,000 users); AI-010 job ad drafting. Group AI Standard and Group AI council established 2026 |
