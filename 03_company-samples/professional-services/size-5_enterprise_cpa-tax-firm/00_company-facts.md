# Scenario facts: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, statute, or IRS publication, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company, LLP (a registered limited liability partnership and licensed CPA firm; privately owned by its partners and not publicly traded) |
| Why not publicly traded | The Enterprise tier default is a publicly traded corporation, but a CPA firm cannot be owned by public shareholders. Florida, the worked example, lets a partnership practice public accounting only if partners owning at least 51 percent of the financial interest and voting rights are CPAs (Fla. Stat. 473.309(1)(b)). The firm is sized as a large private firm: it has no SEC reporting duties of its own, so SEC Form 8-K Item 1.05 and Regulation S-K Item 106 do not apply to it. They matter to the firm only through its SEC-registrant clients (P08 section 6) |
| Business | National CPA and tax firm (NAICS 541211). Three service areas: **Tax** (about 46% of receipts: individual and private client, business, state and local, international and global mobility, and tax compliance outsourcing); **Assurance** (about 30%: financial statement audits of private and public companies, employee benefit plan, nonprofit, and governmental audits, and SOC 1 and SOC 2 examinations for service organization clients); **Advisory** (about 24%: client accounting and payroll services, risk and cybersecurity advisory, transaction advisory, health care consulting, and government services) |
| Location | Headquartered in Florida. 64 offices in 14 states (12 in Florida), plus clients in all 50 states. **State law is handled generically:** notify and protect under the law of each state where affected individuals reside, with Florida as the worked example |
| Workforce | 12,000 employees: 760 partners and principals, about 8,600 client service professionals, and about 2,640 operations and technology staff (about 610 in IT and security). About 1,500 seasonal tax staff join from January to April as temporary employees and are not counted in the 12,000 |
| Revenue | About $4.8 billion a year (fictional), about $19.0 million per business day on average. Above the SBA standard of $26.5 million for NAICS 541211, so not small |
| Tax volumes | About 420,000 individual income tax returns (Form 1040 series) a year, covering about 700,000 individual consumers; about 96,000 business, trust, and exempt-organization returns; tax compliance outsourcing for about 380 corporate clients, including global mobility returns for about 38,000 assignees |
| Customer information held | Records on about 2.9 million consumers: current individual clients plus former clients whose files go back to 2004 in the document management system and a legacy archive (see gap 3) |
| GLBA status | **Financial institution under the FTC Safeguards Rule.** 16 CFR 314.2(h)(2)(viii) names "an accountant or other tax preparation service that is in the business of completing income tax returns." Individual tax clients have a customer relationship (314.2(e)(2)(i)(H)). The 314.6 exception (fewer than 5,000 consumers) does not apply |
| IRS status | Tax return preparer under IRC 7216 (26 CFR 301.7216-1(b)(2)). About 5,200 PTIN holders (including seasonal staff). Authorized IRS e-file Provider acting as an ERO, with 30 EFINs (28 for the firm's originating office groups and 2 still held by acquired firms AF-05 and AF-06). Returns are transmitted through the tax software vendor, an Authorized IRS e-file Provider (transmitter and software developer) |
| HIPAA status | **Business associate** for about 240 health care clients (audits and consulting engagements that require PHI). Not a covered entity. The firm's employee health plan is a separate covered entity outside these deliverables |
| Federal contracts | The government services practice holds about 30 federal civilian agency contracts that include FAR 52.204-21 (Federal Contract Information). No DoD contracts and no CUI clauses; engagement acceptance declines work that would require DFARS 252.204-7012 or CMMC |
| Professional status | Registered with the PCAOB, as a firm that audits SEC issuers (about 140 issuer audits). AICPA, SEC, and PCAOB independence rules apply to attest work. The firm's own SOC examination practice may not examine the firm itself; an unaffiliated CPA firm is the service auditor for the firm's own SOC reports (P09) |
| Not in scope | SEC Form 8-K Item 1.05 and Item 106 for the firm itself (not a registrant); DFARS 252.204-7012 and CMMC (no DoD work); ABA Model Rules (the firm does not practice law); CIRCIA (proposed rule only); comprehensive state consumer privacy laws (tracked by the Office of General Counsel, not analyzed here); payment cards (client payments run on a payment processor's hosted page) |

## 2. People (role titles only)
| Role | Security and compliance duties |
|---|---|
| Partnership Board (elected partners) with an Audit and Risk Committee | The firm's governing body for 16 CFR 314.4(i). Approves the risk appetite and POL-01; receives the Qualified Individual's annual written report and quarterly cyber risk reporting |
| Chief Executive Officer and Managing Partner | Accepts Very High risks with the Chief Financial Officer; chairs the executive committee |
| Chief Financial Officer | Accepts Very High risks with the CEO; member of the Incident Disclosure Committee |
| Chief Information Security Officer (CISO) | **Qualified Individual** under 16 CFR 314.4(a), designated in writing on 2024-01-15. Program owner |
| Director of Security Operations | Runs the 24x7 SOC; **HIPAA Security Official** for the firm's business associate role (45 CFR 164.308(a)(2)) |
| Chief Privacy Officer | Privacy program; HIPAA privacy lead for the business associate role; breach determinations with the General Counsel |
| Chief Risk Officer | Enterprise risk management (ERM); owns the enterprise risk register; chairs the AI governance committee |
| General Counsel | Chairs the Incident Disclosure Committee; IRC 7216 and contract interpretations |
| National Tax Leader (Vice Chair, Tax) | Business owner of the Tax Engagement Platform (P02); owns the IRC 7216 consent program |
| GRC team (12), Security Operations Center (24x7, in-house with managed security service provider overflow), Internal Audit (in-house, reports to the Audit and Risk Committee) | Three lines model |
| Incident Disclosure Committee | Decides notices to regulators, individuals, and clients, and runs the client-impact assessment for SEC-registrant clients (P08). General Counsel chairs |

## 3. Systems
| ID | System | Notes |
|---|---|---|
| SYS-01 | Professional tax preparation and e-file software (commercial, licensed) | Customer-managed in the firm's hosted application environment on Cloud provider A; the vendor transmits all of the firm's e-files to the IRS and states |
| SYS-02 | Client document portal | Firm-built web application on Cloud provider A; about 760,000 client user accounts; uploads, e-signature of Forms 8879 and consents, return delivery |
| SYS-03 | Document management system (DMS) and tax workflow | DMS is vendor SaaS; the tax workflow and e-file queue are firm-built on Cloud provider A; records back to 2004 |
| SYS-04 | Identity platform (SSO, MFA, privileged access management, identity governance) | All workforce and contractor identities; acquired firms AF-05 and AF-06 are not yet federated |
| SYS-05 | Productivity suite (email, files, chat) | About 13,800 mailboxes in season; the main target of business email compromise |
| SYS-06 | Multi-cloud estate (two public cloud providers, vendor-agnostic) plus 2 colocation data centers | Cloud A: tax platform, client portal, data lake. Cloud B: client accounting and payroll platform, advisory analytics, AI services. Colocation: legacy audit applications and offline backup copies |
| SYS-07 | Audit platform (assurance workpapers) | Vendor software customer-managed on Cloud provider B; holds PHI for health care audit clients |
| SYS-08 | Client accounting and payroll platform (service line SL-1) | Accounting SaaS instances per client plus a firm-built payroll engine on Cloud provider B |
| SYS-09 | Enterprise network (SD-WAN to 64 offices; zero-trust network access for remote work) | |
| SYS-10 | Endpoints | About 14,800 managed laptops and about 900 office printer-scanners |
| SYS-11 | Practice management, ERP, time and billing, engagement acceptance and independence system | Firm finance and engagement records |
| SYS-12 | About 1,400 third-party vendors (about 260 with access to customer or tax return information) | Tiered third-party risk program; one tax software vendor transmits 100% of e-files |
| SYS-13 | AI portfolio (12 use cases) | Governed by the AI governance committee formed in 2025 |

**SSP system (P02):** the *Tax Engagement Platform (TEP)*: SYS-01, SYS-02, and SYS-03, the document ingestion and AI extraction pipeline, and their interfaces to the IRS and state e-file systems through the tax software vendor, inheriting common controls from SYS-04, SYS-05, SYS-06, SYS-09, and SYS-10.

## 4. Current security posture: mostly compliant, with targeted gaps
**In place today:**
- A program aligned to CSF 2.0, documented as a policy hierarchy of policies, standards, procedures, and exceptions
- A Qualified Individual (the CISO) designated in writing, who has reported in writing to the Partnership Board each year since 2024
- Annual enterprise risk assessment tied to ERM (NIST IR 8286)
- A written incident response plan, exercised for ransomware in 2026-02
- 24x7 SOC with SIEM and user behavior analytics
- MFA for all workforce access; phishing-resistant authenticators for privileged users and partners
- Privileged access management and quarterly access certification
- Encryption of customer information at rest and in transit on firm systems
- Immutable backups and annual disaster recovery tests for tier-1 systems
- Annual external and internal penetration tests and monthly vulnerability scanning
- A tiered third-party risk program with SOC report reviews
- A SOC 2 Type 2 report for the client accounting and payroll service line (SL-1) since 2024, issued by an unaffiliated CPA firm
- An IRC 7216 consent program for the main disclosures (lenders, offshore processing, related services)

**Targeted gaps:**
1. **Business email compromise.** Staff other than privileged users and partners use push MFA with number matching, which adversary-in-the-middle phishing can bypass. Browser access to email from unmanaged devices is allowed, session token replay is not detected, and 9 service mailboxes still have legacy authentication exceptions.
2. **Client portal and email intake.** Client MFA is optional for individual clients (64% enrolled). About 15% of individual clients' source documents still arrive by email.
3. **Retention and disposal.** Tax files go back to 2004. About 2.1 million former-client consumer records are past the firm's 7-year schedule, and no disposal has been run (16 CFR 314.4(c)(6)).
4. **Acquired firms.** Six regional CPA firms were acquired in 2024-2026 (AF-01 to AF-06). AF-05 and AF-06 still run their own email tenants, tax software, and EFINs, and their managed service providers have not received the written IRC 7216 notice.
5. **Offshore processing.** A contracted tax outsourcing provider's delivery center outside the United States prepares draft business returns with taxpayer consent. Sampling found missing consents and unmasked SSNs on partner Schedules K-1.
6. **Seasonal workforce.** About 1,500 seasonal staff. Some start before completing training, and access removal after the season is slow.
7. **E-file concentration.** One tax software vendor transmits 100% of e-files. Its contract RTO (12 hours) misses the peak-season BIA RTO (8 hours), and no alternative has been tested.
8. **AI.** 12 AI use cases, 8 reviewed by the AI governance committee. The IRC 7216 basis is documented for only 5 of the 9 use cases that touch tax return information. Bias testing is incomplete.
9. **Need-to-know and bulk export.** 31% of DMS tax repositories are open to whole office tax teams, and bulk export alerts are not tuned by role.
10. **Incident readiness.** The business email compromise and data theft playbook, with its client-notice and Incident Disclosure Committee steps, has never been exercised. The state notification matrix was last updated in 2024-11, and contractual client notice deadlines are not tracked centrally.
11. **HIPAA business associate role.** No separate risk analysis covers PHI in audit workpapers and consulting data rooms, 22 of about 240 business associate agreements are on legacy templates, and PHI is not tagged in the DMS.
12. **Federal contract information.** Federal Contract Information sits in the general environment without tagging, and 4 of 19 subcontracts lack the FAR 52.204-21 flow-down.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P03 regulations | Primary: FTC Safeguards Rule, 16 CFR Part 314 (full rule; 314.6 does not apply). Also: IRC 7216 and 26 CFR 301.7216; IRS e-file and PTIN program requirements; HIPAA as business associate; FAR 52.204-21; state breach and data security laws (Florida worked example) |
| P08 | Business email compromise and taxpayer data theft at enterprise scale, with an **Incident Disclosure Committee step** that replaces the SEC 8-K step: client-impact assessment and prompt notice to SEC-registrant clients, who must judge materiality for incidents on third-party systems they use. Multi-state notification workflow |
| P09 | SOC 2 Type 2 readiness across two service lines offered to clients: SL-1 client accounting and payroll services, and SL-2 tax compliance outsourcing with the corporate client tax portal |
| P10 | Enterprise AI portfolio (12 use cases) under the AI governance committee, with a full assessment of generative AI for tax and document preparation (AI-001) |
| Cloud | Multi-cloud (vendor-agnostic) with common controls |
| Registry defaults | The primary system, incident, and AI use case fit this business at this size and are kept; the system is scoped as the enterprise Tax Engagement Platform, and the SEC step is adapted because the firm is not a registrant |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-01 to 2026-07-31 | Enterprise risk analysis, BIA, and gap analysis |
| 2026-07-13 to 2026-08-28 | Control assessment (Internal Audit, third line) |
| 2026-09-15 | Results to the Audit and Risk Committee of the Partnership Board |
| 2026-09-17 | Qualified Individual's annual written report to the Partnership Board (16 CFR 314.4(i)) |

## 7. Facts added for the deliverables
These facts were added while building the deliverables. They do not change sections 1-6.

| Fact | Used in |
|---|---|
| Office footprint: the 14 office states include Colorado, Illinois, and New York, with an office in New York City. Other states are not named | P10 (state and local AI employment laws for AI-010) |
| SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) for each calendar year since 2024 and a SOC 1 Type 2 report for payroll. The 2025 SOC 2 report had one exception (late access removal). Processing Integrity is added for the 2027 period | P09 |
| SL-2's first SOC 2 Type 2 period is 2027-04-01 to 2027-09-30 (Security, Availability, Confidentiality), with the report expected in 2027-11. Privacy is deferred to SL-2's second period (decision 2026-08-21); Processing Integrity is out of scope for SL-2 | P09 |
| Subservice organizations (carve-out): SL-1, the accounting SaaS provider, Cloud provider B, the ACH originating bank, and the payroll tax filing service; SL-2, Cloud provider A, the tax software vendor and transmitter, the DMS vendor, and the offshore tax outsourcing provider | P09 |
| SL-2 has about 1,700 staff plus seasonal staff. About 9,000 of the 38,000 assignee portal accounts use a password only. SL-1 business client users must use MFA. SL-1 contracts require deletion of a former client's data within 90 days; 37 former SL-1 clients' data is past that date | P09 |
| AI governance committee: chaired by the Chief Risk Officer; members are the National Tax Leader; Vice Chair, Assurance; CISO; Chief Privacy Officer; a General Counsel delegate; CIO; Chief Human Resources Officer; Managing Principal, Client Accounting Services; Director of Professional Standards; and the data science lead. Internal Audit observes. Meets monthly; met 2026-08-26 for the portfolio review. Since 2026-06-01, procurement and change management block AI features without an inventory ID | P10 |
| AI portfolio (12): AI-001 generative AI for tax and document preparation; AI-002 enterprise assistant; AI-003 global mobility assignee assistant (SL-2); AI-004 tax notice triage and response drafting; AI-005 refund and payroll diversion anomaly detection; AI-006 contact center call transcription and summary; AI-007 audit platform document summarization; AI-008 SL-1 invoice coding and bank reconciliation matching; AI-009 SOC alert triage; AI-010 recruiting resume screening and ranking (ranking disabled 2026-08-14); AI-011 advisory opportunity insights (proposed, on hold); AI-012 tax return review insights. Review and IRC 7216 memo dates are in the P10 inventory | P10; consistent with P01 R-012 to R-014 and POAM-020 |
| AI-001 volumes and results: documents for about 240,000 individual and 31,000 business returns in the 2026 filing season; 1,800-return sample: typed fields 99.6% accurate, photographed or handwritten 96.1%, 3 critical-field errors on filed returns; 2 of 4 tested client groups flagged. AI-005 holds ITIN filers 2.1 times as often as the overall rate | P10 |
| Additional role titles: Director of Client Service Operations (contact center), Chief Growth Officer, Director of Professional Standards, data science lead | P10 |
| Operating scale used across P01 to P08: 12 processing hubs (about 140 printer-scanners); about 4,100 preparers and reviewers; about 6,300 workforce TEP accounts in season; about 516,000 tax engagement repositories in the DMS; SL-1 serves about 3,100 client businesses (about 410,000 client employees) with about 1,300 client accounting staff; about 610 SOC examination clients a year; the offshore provider drafts about 22% of business returns in season through about 410 virtual desktop accounts | P01, P02, P05, P07 |
| Governance and testing events used across P01 to P08: risk appetite approved by the Partnership Board 2026-02; ransomware exercise 2026-02-24; tier-1 DR test 2026-05-09 (tax workflow and e-file queue recovered in 9.5 hours); TEP SSP version 3.0 (identifier CSC-SYS-TEP-001) approved by the Chief Operating Officer 2026-09-14; executive risk committee approvals 2026-09-08; Internal Audit report issued 2026-09-04; business email compromise tabletop scheduled 2026-11-19 | P01, P02, P05, P07, P08 |
| Committees: the executive risk committee (Chief Risk Officer chair; Chief Operating Officer, CIO, CISO, General Counsel, National Tax Leader) approves High risk acceptances; the Incident Disclosure Committee members are the General Counsel (chair), CFO, Chief Risk Officer, CISO, Chief Privacy Officer, National Tax Leader, Vice Chair, Assurance, and Chief Communications Officer; Internal Audit is led by the Chief Audit Executive | P01, P07, P08 |
