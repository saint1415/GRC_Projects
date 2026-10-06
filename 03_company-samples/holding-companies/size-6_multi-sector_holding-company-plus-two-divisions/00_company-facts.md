# Scenario facts: Cris Santos Company | Management of Companies and Enterprises | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation or statute, the citation is given; each was read from the primary source for this sample (eCFR current through 2026-09-23, govinfo.gov for the U.S. Code, flsenate.gov for the 2026 Florida Statutes, and the NAIC model law and state pages).

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant and large accelerated filer; parent of an insurance holding company system) |
| Structure | A Florida-headquartered holding company (NAICS 551112) that owns two operating groups through subsidiaries and runs corporate shared services for all of them. 64 legal entities in total |
| Division 1: Holding company and corporate shared services (NAICS 551112), **focus of this scenario** | The parent company: board, executive office, finance, treasury, tax, legal, HR and benefits, IT and security, internal audit, and corporate development. About 5,500 employees. Owns and runs the Shared Corporate Services Platform used by every subsidiary. Sponsors the group's self-insured employee health plan |
| Division 2: Insurance (NAICS 524126, sector 52 Finance and Insurance) | CSC Insurance Group: two Florida-domiciled stock insurers. CSC Property and Casualty Insurance Company writes personal auto and homeowners insurance; CSC Workers' Compensation Insurance Company writes workers' compensation for employers. About 20,500 employees. Licensed in 6 states: Florida, Georgia, Alabama, South Carolina, North Carolina, and Tennessee. Sells through about 2,400 independent agencies and a direct channel |
| Division 3: Health Care Services (NAICS 621111, sector 62 Health Care and Social Assistance) | CSC Health Services: 340 urgent care and occupational medicine clinics in Florida, Georgia, Alabama, and Tennessee. About 19,000 employees. A HIPAA covered entity (health care provider that bills electronically). Accepts Medicare and Medicaid |
| Location | Headquartered in Florida. Operations in 6 southeastern states; employees live in more states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion revenue (fictional) |
| Ownership and securities status | Publicly traded. A large accelerated filer (17 CFR 240.12b-2), so the auditor attests to internal control over financial reporting (15 U.S.C. 7262(b)). Files Form 10-K with Reg S-K Item 106 disclosure (17 CFR 229.106) and is subject to Form 8-K Item 1.05 |
| Banking status | Not a bank holding company or savings and loan holding company: no subsidiary is a bank or savings association (12 CFR 225.2(b), (c)(1)). Federal Reserve Regulation Y Subpart N and 12 CFR Part 225 Appendix F do not apply |
| Insurance holding company status | The holding company is the **ultimate controlling person** of the two insurers. Each insurer registers annually with the Florida Office of Insurance Regulation, and the holding company files the annual enterprise risk report, both by April 1 (Fla. Stat. 628.801(1)-(2)); the Office may examine the insurers and their affiliates (628.801(3)) |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board of directors: risk committee and audit committee | Risk committee oversees cyber and enterprise risk and approves group security policies. Audit committee oversees internal control over financial reporting, group internal audit, and SEC disclosure controls |
| Group Chief Executive Officer | Chairs the executive risk committee |
| Group Chief Financial Officer | Chairs the disclosure committee; accountable for internal control over financial reporting |
| Group Chief Risk Officer | Owns enterprise risk management, the group risk register and roll-up (NIST IR 8286 Rev. 1), and the annual enterprise risk report to the Florida Office of Insurance Regulation; chairs the Group AI council |
| Group Chief Information Officer | Runs shared IT; system owner of the Shared Corporate Services Platform |
| Group CISO | Owns the group information security program and group policies; operates common controls (SYS-G1 to SYS-G3); reports to the Group CIO with direct access to the board risk committee |
| Group Chief Privacy Officer; Group General Counsel | Privacy rules across divisions and the group health plan; contracts, intercompany agreements, and the notification matrix |
| Chief Audit Executive (group internal audit) | Reports to the audit committee. Assesses common controls once and samples division controls; tests SOX IT general controls |
| Group Controller; Group Treasurer; Group Chief Human Resources Officer | Own the ERP and financial close (SYS-G4), treasury and payments (SYS-G6), and the HCM and payroll system (SYS-G5) |
| Group benefits director | Runs plan administration for the self-insured group health plan; designated the plan's **privacy official** (45 CFR 164.530(a)) |
| Group security governance director | Designated the group health plan's **security official** (45 CFR 164.308(a)(2)) |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents (Form 8-K Item 1.05) |
| Insurance division roles | Division president; insurance information security officer (division security and compliance lead, responsible for the insurers' information security program); insurance chief compliance officer (state filings and commissioner notices); claims vice president; special investigations unit director. Each insurer has its own board of directors |
| Health Care Services division roles | Division president; chief medical officer; HIPAA Privacy Officer; HIPAA Security Officer (division security and compliance lead); occupational health vice president |

## 3. Systems
| ID | System | Owner | Hosting |
|---|---|---|---|
| SYS-G1 | Group identity platform: single sign-on, MFA, privileged access management (PAM), identity governance, and the corporate directory | Corporate | Identity SaaS vendor; directory servers in the colocation data center and provider A |
| SYS-G2 | Group SOC, SIEM, EDR, and email security | Corporate | SIEM and EDR SaaS vendors; 24x7 group SOC |
| SYS-G3 | Group infrastructure: cloud landing zones in two providers (vendor-agnostic: provider A primary, provider B for backups and disaster recovery), wide-area network, and one colocation data center | Corporate | Providers A and B; colocation provider |
| SYS-G4 | Group ERP and consolidation: multi-entity general ledger for 64 legal entities, payables, fixed assets, intercompany, consolidation, and close | Corporate | ERP SaaS vendor |
| SYS-G5 | HCM and payroll: HR records, payroll, and benefits enrollment for 45,000 employees; eligibility feed to the group health plan's third-party administrator | Corporate | HCM SaaS vendor |
| SYS-G6 | Treasury management and payments hub: bank connectivity, wires, ACH, positive pay, claims disbursement files, and payroll funding | Corporate | Treasury SaaS vendor; managed file transfer service in provider A |
| SYS-G7 | Productivity and collaboration suite (email, files, chat, device management), including the enterprise generative AI assistant add-on | Corporate | Productivity SaaS vendor |
| SYS-G8 | Board portal, disclosure management, and M&A virtual data rooms | Corporate | SaaS vendors |
| SYS-I1 | Personal lines policy administration and billing (auto and homeowners) | Insurance | Licensed platform in provider A |
| SYS-I2 | Personal lines claims management, including the AI claims triage and fraud scoring model and a vendor photo-estimating service | Insurance | Provider A; estimating SaaS vendor |
| SYS-I3 | Agent portal and policyholder portal and mobile app | Insurance | Provider A; customer identity SaaS vendor |
| SYS-I4 | Workers' compensation policy, claims, and medical bill review | Insurance | Legacy platform in the colocation data center |
| SYS-H1 | Clinic EHR and practice management for 290 clinics; 50 clinics acquired in 2025 still run a legacy EHR | Health Care Services | EHR vendor-hosted; legacy EHR in a hosting provider |
| SYS-H2 | Occupational health employer portal (exam scheduling, work status reports, injury visit summaries) | Health Care Services | Provider A (built by the division) |
| SYS-H3 | Patient online check-in and telehealth app | Health Care Services | Provider A; telehealth SaaS vendor |

**SSP system (P02):** the *Shared Corporate Services Platform (SCSP)*: the group identity platform (SYS-G1), the ERP and consolidation system (SYS-G4), the HCM and payroll system (SYS-G5), and the treasury and payments hub (SYS-G6), with their integration services in provider A; it inherits common controls from SYS-G2 (SOC) and SYS-G3 (cloud, network, and backup).

## 4. Current security posture: defined group program, uneven divisions
**In place today:**
- One group information security program aligned to CSF 2.0, approved by the board risk committee (2025)
- Reg S-K Item 106 disclosure in the 2025 Form 10-K; a disclosure committee charter that covers cybersecurity incidents
- SOX IT general controls over the ERP, HCM, and treasury systems, tested each year by group internal audit and the external auditor; no material weakness reported for 2025
- 24x7 group SOC, SIEM, EDR on endpoints and servers, and email security
- Single sign-on with number-matching MFA for all workforce; PAM for directory and cloud administrators
- Immutable backups of cloud workloads in provider B; colocation backups copied to the same vault
- Written information security programs for both insurers (adopted 2019, updated 2025), with an annual written report to each insurer's board
- A HIPAA program in Health Care Services: designated Privacy and Security Officers, a 2025 risk analysis, and annual training
- Group health plan documents amended in 2014 to restrict the plan sponsor's use of PHI (45 CFR 164.504(f))
- A group cyber insurance program with a breach response panel

**Gaps:**
1. **Flat privilege in the shared identity platform.** 212 accounts hold group-wide identity administration, password reset, or MFA reset rights, including 61 division help desk agents. The help desk resets MFA after checking only an employee ID and the manager's name. A directory trust from the 50 acquired clinics' legacy directory into the corporate forest is still open.
2. **Shared services agreements.** The 2017 intercompany services agreement between the holding company and the insurers has no security requirements, and the insurers have never performed due diligence on the holding company as a service provider holding their consumers' nonpublic information. The Health Care Services business associate agreement with the holding company (2021) predates the AI assistant.
3. **Group health plan safeguards.** The plan documents were never amended with the security terms in 45 CFR 164.314(b)(2). Plan administration files (appeals and stop-loss claims with PHI) sit on a general HR collaboration site that about 140 HR staff outside the plan administration unit can open.
4. **ERP privileged access.** The 2025 SOX testing found 17 standing ERP superuser accounts (including 3 for the ERP vendor's support) and emergency access that was not reviewed. Reported to the audit committee in February 2026 as a control deficiency, not a material weakness.
5. **Payment change verification.** Claimant and vendor bank-detail changes for claims disbursements can be made through the insurance call center with knowledge-based questions only. Two attempted payment redirections were stopped in 2026 by positive pay review, not by the change process.
6. **Cross-division data access.** About 310 workers' compensation adjusters have read access to the clinic EHR for injured workers treated in the group's occupational medicine network. The access role opens the full patient chart, including visits that are not work-related.
7. **Shared incident notification.** The group notification matrix covers SEC, HIPAA for Health Care Services, and state breach laws. It does not cover insurance commissioners in states that enacted the NAIC Insurance Data Security Model Law, notices to producers of record, or the group health plan as a separate covered entity, and it has never been exercised across divisions.
8. **Acquired clinics.** The 50 clinics acquired in 2025 run a legacy EHR and local directory that are not sending logs to the SIEM and are not fully covered by the division's risk analysis or by the common control inheritance matrix.
9. **Enterprise generative AI assistant.** A pilot with 6,000 users across all three divisions started 2026-05-04 without sensitivity labels for PHI, consumer nonpublic information, or MNPI. The assistant can retrieve deal-room exports and benefits files that users can open. Whether the AI add-on is inside the productivity vendor's business associate agreement was not confirmed before Health Care Services staff were enrolled.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 | NIST CSF 2.0 group profile (voluntary benchmark) for the holding company and the shared platform, with division profiles; group-level binding obligations (SEC, SOX 404, HIPAA for the group health plan, Fla. Stat. 628.801); division gap tables for Insurance (state insurance data security laws based on NAIC Model #668, and GLBA through the state insurance authority) and Health Care Services (HIPAA); regulation-by-division matrix |
| P08 | Compromise of the shared identity platform through help desk social engineering, affecting all subsidiaries: payment redirection attempt in treasury, HCM data theft, and access to insurance claims data and clinic PHI. Multi-regulator notification matrix and SEC materiality |
| P09 | SOC 2 scoped per division: the occupational health employer portal is a true service organization (in scope); the Shared Corporate Services Platform is assessed for an affiliate assurance report to the insurers and Health Care Services; Insurance is out of scope, with reasons |
| P10 | Group AI governance program centered on the enterprise generative AI assistant across subsidiaries, with division use cases and regulator-specific rules |
| Cloud | Shared landing zone in two providers plus one colocation data center, vendor-agnostic; division workloads in their own accounts |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division BIAs, risk analyses, and gap analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-27 | Group AI council review of priority AI use cases |
| 2026-09-15 | Results to the board risk committee; SOX-related items to the audit committee |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | Insurance about $14.2 billion (premiums and investment income); Health Care Services about $3.8 billion. Management fees paid to the holding company eliminate on consolidation. Total about $18.0 billion, as in section 1. Insurance earns about $39 million per day; Health Care Services about $10.4 million per day |
| Treasury volume | About $65 million in outgoing payments per business day: claims disbursements, payroll funding, and payables. About 1,900 wires and 140,000 ACH entries per business day |
| Insurance scale | About 3.1 million policies in force: 1.9 million personal auto, 1.0 million homeowners, and 160,000 workers' compensation policies for employers. Nonpublic information on about 6.8 million consumers (policyholders, insureds, claimants, and applicants). About 1.2 million claims a year. Up to 1,500 independent adjusters are added for hurricane catastrophe claims |
| State insurance data security laws | The NAIC state page for Model #668 (Summer 2026) lists Alabama and South Carolina in the Model Adoption column and Tennessee for portions of the model. Florida, Georgia, and North Carolina are listed only under related activity (general breach and privacy statutes). The insurers are domiciled in Florida, so no state's annual certification to the domiciliary commissioner (Model sec. 4I) applies today. Text varies by state; insurance counsel confirms each state's version |
| NAIC AI Model Bulletin | Of the 6 licensed states, only North Carolina has adopted the NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (Bulletin No. 24-B-19, adopted 2024-12-18), per the NAIC implementation map as of 2026-04-01 |
| GLBA for the insurers | Safeguards standards for persons providing insurance are enforced by the State insurance authority of the State of domicile (15 U.S.C. 6805(a)(6)), here Florida. Florida's administrative rules could not be read from this environment, so counsel confirms any Florida Office of Insurance Regulation safeguards rule |
| Insurers and HIPAA | The insurers are not HIPAA covered entities. Workers' compensation, liability (including automobile liability), and automobile medical payment insurance are excepted benefits (42 U.S.C. 300gg-91(c)(1)), and the HIPAA definition of health plan excludes them (45 CFR 160.103). Claimant medical information is still Nonpublic Information under Model #668 sec. 3K(3) |
| Health Care Services scale | 340 clinics; about 6.1 million visits and about 2.4 million unique patients a year. About 6,200 employer clients use occupational health services. About 18% of the workers' compensation insurer's injured-worker claims in the 4 clinic states are treated in the group's occupational medicine network. Disclosures to the insurer rely on 45 CFR 164.512(l) (as authorized by and to the extent necessary to comply with workers' compensation laws); work-injury findings to employers rely on 164.512(b)(1)(v) where its conditions are met |
| Health Care Services acquisitions | 50 clinics acquired 2025-03; migration to SYS-H1 due 2027-03-31 |
| Group health plan | Self-insured medical plan for employees of all three divisions: about 38,000 participants and 92,000 covered lives. Claims are processed by a third-party administrator (a business associate of the plan). The plan administration unit in Group HR (14 staff) handles appeals, stop-loss claims, and plan audits and receives PHI. About 9,000 covered lives are patients of the group's clinics each year |
| SCSP scale | SYS-G1: about 52,000 workforce identities (employees and contractors), 1,240 service accounts, about 900 federated applications. SYS-G4: 3,100 users. SYS-G5: 45,000 employee records plus about 60,000 former employee records. SYS-G6: 260 users at 14 banks |
| Cloud and hosting | Provider A hosts the landing zone hub, the SCSP integration services and managed file transfer, SYS-I1, SYS-I2, SYS-I3, SYS-H2, and SYS-H3. Provider B hosts the immutable backup vault and warm standby for the SCSP integration services and SYS-I2. The colocation data center hosts SYS-I4 and corporate directory servers |
| Enterprise AI assistant pilot | 6,000 users: holding company 1,800; Insurance 2,900; Health Care Services 1,300 (administrative and clinic management staff; clinicians not enrolled). Connectors to email, files, chat, and meetings only; no connectors to SYS-G4, SYS-G5, SYS-I1, SYS-I2, or SYS-H1 |
| AI use cases (P10 inventory) | AI-001 enterprise generative AI assistant (group); AI-002 claims triage and fraud scoring model (Insurance, in-house); AI-003 photo-based auto damage estimating (Insurance, vendor); AI-004 homeowners pricing model with aerial imagery attributes (Insurance, proposed); AI-005 workers' compensation medical bill review rules engine with machine learning (Insurance, vendor); AI-006 urgent care triage and sepsis alert in the EHR (Health Care Services, EHR vendor); AI-007 AI scribe pilot (Health Care Services, proposed); AI-008 resume screening in the HCM recruiting module (holding company, turned off pending review); AI-009 accounts payable invoice capture (holding company); AI-010 developer coding assistant (holding company IT). A Group AI Standard and a Group AI council were set up in 2026 |
| Risk acceptance | Low: division security and compliance lead (for group risks, the Group CISO's security governance director). Moderate: division president (for group risks, the Group CIO). High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only |
| Intercompany agreements | The holding company provides shared services to the insurers under a 2017 intercompany services agreement and to Health Care Services under a 2019 services agreement with a 2021 business associate agreement. The holding company is a Third-Party Service Provider of the insurers as Model #668 sec. 3P defines the term |
