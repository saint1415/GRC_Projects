# Scenario facts: Cris Santos Company | Information Technology | Multi-Sector

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; large accelerated filer) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership |
| Division 1: Cloud Hosting (NAICS 518210, sector 51 Information), **focus of this scenario** | Cloud hosting and managed infrastructure provider. About 21,000 employees. Three service lines: **SL-1 Commercial Cloud** (multi-tenant IaaS and PaaS: compute, block and object storage, managed databases, managed Kubernetes, networking, DNS, and content delivery) in five commercial regions (R1 to R5), each with three company-operated data centers; **SL-2 Government Cloud**, a dedicated region (G1) with two company-operated data centers (G1-A and G1-B) in two eastern states; **SL-3 Managed Hosting**, SL-1 tenants whose servers are operated for them by the Managed IT division (section 7). About 38,000 business customers and about 290,000 customer console identities |
| Division 2: Managed IT and Consulting (NAICS 541513 and 541512, sector 54 Professional, Scientific, and Technical Services) | Managed IT services (monitoring, patching, backup, and administration of client servers and endpoints through a remote monitoring and management (RMM) platform), IT consulting, and federal IT services. About 12,000 employees. About 2,900 client organizations, including banks and credit unions, health care organizations, defense industrial base (DIB) companies, and federal agencies (section 7) |
| Division 3: Payment Processing (NAICS 522320, sector 52 Finance and Insurance) | Merchant payment processing (card authorization, clearing, and settlement), ACH origination, and consumer bill payment for billers. About 7,000 employees. About 210,000 merchants and about 2,300 billers; funds move through two sponsor banks. A PCI DSS Level 1 service provider. Group legal treats it as a financial institution under the FTC Safeguards Rule (P03) |
| Corporate shared services | Identity, security operations, the group landing zone, HR, finance, legal, risk, privacy, and internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Commercial region R1 is in Florida; R2 to R5 and G1 are in other states. Employees in 46 states; customers and data subjects in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional) |
| Not in scope by fact | No bank charter in the group; no New York financial services license (NYDFS Part 500 does not apply); no broker-dealer or investment adviser (SEC Reg S-P does not apply); no 42 CFR Part 2 program; no child-directed services. No employees, contractors, or data centers in a country of concern under 28 CFR Part 202 |

## 2. People (role titles only)
| Role | Duties |
|---|---|
| Board risk committee | Group cyber and AI risk oversight; accepts Very High risks |
| Board audit committee | Oversees group internal audit and SEC reporting |
| Group CISO; Group Chief Risk Officer; Group Chief Privacy Officer; Group General Counsel | Group standards, the group risk register, common controls, and the notification matrix |
| Division presidents (3) | Accept Moderate risks for their divisions |
| Cloud Hosting division CISO | Division security and compliance lead; system owner representative for the HCP security program; the FedRAMP senior security official who receives Emergency messages from the FedRAMP Security Inbox |
| Government Cloud compliance director | FedRAMP certification package, Ongoing Certification, and the 2026 rules transition for G1 |
| Managed IT division security and compliance lead | Division register and supplement; HIPAA Security Official for the division's business associate work; CMMC program owner |
| Managed IT federal contracts compliance officer | FAR and DFARS clauses, DIBNet reporting, SPRS scores, and subcontract flowdown |
| Payment Processing division CISO | Division security lead and the **Qualified Individual** under 16 CFR 314.4(a); PCI DSS program owner |
| Payment Processing chief compliance officer | Sponsor bank oversight, money transmitter licensing, card network relationships, FTC Safeguards notices |
| Group SOC director | 24x7 security operations; incident commander for Severity 1 and 2 incidents; business owner of the AI alert triage service |
| Group identity director; Group cloud platform director | Operate the common control providers SYS-G1 and SYS-G3 |
| Group AI council | Approves High-tier AI use cases under the Group AI Standard (P10) |
| Group internal audit | Independent of the teams it assesses (reports to the board audit committee). Assesses common controls once and samples division controls (P07) |
| Disclosure committee | SEC materiality determinations (Form 8-K Item 1.05) |
| External assurance | FedRAMP Recognized independent assessment service (annual G1 assessment); SOC 2 service auditor (independent CPA firm); PCI Qualified Security Assessor (QSA); ISO/IEC 27001 certification body. A CMMC Third-Party Assessment Organization (C3PAO) is not yet engaged |

**Where roles overlap and how it is compensated:** each division CISO both runs the division's controls and reports on them, and the Group SOC director both operates the AI triage service and owns its risk. The group compensates with group internal audit (independent of operations), the external assessors above, and the Group AI council, which approves High-tier AI use cases that the SOC proposes.

## 3. Systems
| ID | System | Owner |
|---|---|---|
| SYS-G1 | Group identity platform: workforce single sign-on, MFA (phishing-resistant for administrators), privileged access management (PAM) with just-in-time elevation, identity governance | Corporate |
| SYS-G2 | Group SOC stack: SIEM, security orchestration and automated response (SOAR), endpoint detection and response (EDR), and the AI alert triage service (P10) | Corporate |
| SYS-G3 | Group landing zone: corporate accounts on the Cloud Hosting division's own commercial cloud (SL-1), the central log archive, key management, and an immutable backup vault held with an unaffiliated public cloud provider ("external provider X", vendor-agnostic) | Corporate |
| SYS-G4 | Corporate SaaS: productivity suite, HR information system, ERP and finance, IT service management | Corporate |
| SYS-H1 | **Hosting control plane and customer portal**: console, public API, customer identity and access management, orchestration and provisioning, metering, support tooling, the run-command service, and the partner-operator access path, in two partitions (commercial and G1) | Cloud Hosting |
| SYS-H2 | Data center and virtualization fleet: hypervisor hosts, baseboard management controllers (BMCs), storage clusters, and region networks in R1 to R5 and G1 | Cloud Hosting |
| SYS-H3 | Software supply chain: source hosting, CI/CD, artifact signing with hardware security modules (HSMs), and the fleet automation and guest-agent update service | Cloud Hosting |
| SYS-H4 | Edge services: authoritative DNS, content delivery, and DDoS protection | Cloud Hosting |
| SYS-M1 | Managed operations platform: RMM (one tenant for all clients and internal uses), professional services automation and ticketing, and the client privileged access broker | Managed IT |
| SYS-M2 | Consulting delivery workspace and the DoD CUI enclave (a separate tenant on SL-1 for the division's own DoD subcontracts) | Managed IT |
| SYS-P1 | Payment processing platform: authorization switch, tokenization vault, payment HSMs, clearing and settlement. This is the cardholder data environment (CDE), in dedicated SL-1 accounts in R1 and R3 | Payment Processing |
| SYS-P2 | Merchant and biller portals, consumer bill-pay service, ACH origination, merchant onboarding and risk scoring | Payment Processing |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-H1 in both partitions (commercial and G1), with the management interfaces of SYS-H2 and the fleet automation of SYS-H3 that act through it, inheriting common controls from SYS-G1, SYS-G2, and SYS-G3; its G1 partition is the control plane of the FedRAMP Rev5 Class C Government Cloud offering.

## 4. Current security posture: a defined program, mostly effective, with gaps where the divisions meet
**In place today:**
- Group policies aligned to NIST CSF 2.0, with division supplements, and a common control catalog
- 24x7 group SOC with SIEM, SOAR, and EDR on all managed endpoints and workloads; AI alert triage since 2025-11
- Workforce single sign-on with MFA; phishing-resistant authenticators and just-in-time PAM for group and Cloud Hosting administrators
- A FedRAMP certification for the Government Cloud: a legacy FedRAMP Moderate agency authorization (2023-03-15), now a Rev5 Class C certification under the FedRAMP Consolidated Rules for 2026, with annual independent assessments (last completed 2026-03-20) and monthly continuous monitoring deliverables
- SOC 2 Type 2 for SL-1 Commercial Cloud (Security, Availability, Confidentiality; 12 months ending June 30) and ISO/IEC 27001 certification for the Cloud Hosting division
- PCI DSS v4.0.1 Report on Compliance for the payment processing platform (QSA, 2026-04-30) and a SOC 1 Type 2 report for settlement services
- Immutable backups with external provider X; HSM-backed signing of images and guest-agent packages
- Quarterly access certification for group applications and the HCP
- Board risk committee oversight; SEC Reg S-K Item 106 disclosure in the annual report

**Gaps found in the 2026 assessments:**
1. **Cross-division privileged tooling.** The HCP partner-operator role lets about 1,900 Managed IT engineers run commands on the virtual machines of about 4,100 managed-hosting tenants. The access is standing, not just in time, and it is federated from the Managed IT division's legacy identity tenant, which accepts push MFA and 12-hour sessions instead of SYS-G1 phishing-resistant MFA and PAM. Run-command actions are logged but there is no alert on volume across tenants.
2. **RMM reach into other divisions.** One RMM tenant (SYS-M1) serves all clients and internal uses. It has agents on 140 Payment Processing settlement-support servers in the CDE's connected-to segment and on the management servers of the DoD CUI enclave (SYS-M2). A script can be sent to many clients with one approver.
3. **FedRAMP 2026 rules transition (G1).** Vulnerability Detection and Response (VDR) and Vulnerability Evaluation and Reporting (VER) must be followed by 2026-12-07; Incident Evaluation and Communication (IEC), Significant Change Notification (SCN), Cryptographic Module Use (CMU), and others by 2027-01-01. G1 still uses the legacy POA&M model, has no tested incident procedure based on the Potential Agency Impact N-rating (PAIN), no machine-readable Security Decision Record, and no FedRAMP-compatible trust center. The shared corporate services that handle G1 logs and identities (SYS-G1, SYS-G2 and its AI triage service) are not documented as information resources of the offering.
4. **AI alert triage autonomy.** The SOC's AI triage service auto-closes about 64% of alerts and can run 7 SOAR containment actions without a human, across all divisions, including CDE and G1 logs. Its auto-close accuracy has never been validated by division, and it sends alert context to a third-party hosted model service.
5. **CMMC Level 2 readiness.** CMMC Phase 2 begins 2026-11-10 (32 CFR 170.3(e)(2)). The Managed IT division's own NIST SP 800-171 basic self-assessment in SPRS dates from 2024-02-12, 14 of the 110 requirements are not fully met in the CUI enclave, and its responsibilities as an External Service Provider to about 150 DIB clients are not documented in a responsibility matrix.
6. **Payment Processing affiliate oversight.** The CDE runs on SL-1 and relies on the Cloud Hosting and Managed IT divisions, but no intercompany agreement carries 16 CFR 314.4(f) safeguards terms or a PCI DSS responsibility matrix (Requirements 12.8 and 12.9) for either affiliate, and the RMM-managed connected-to servers are not in the 2026 PCI DSS scope description.
7. **Notification matrix.** No single group matrix covers FedRAMP IEC reports, DFARS 72-hour reports, bank service provider notices (designated contacts on file for 70% of Cloud Hosting's and 64% of Managed IT's bank customers), HIPAA business associate notices, sponsor bank and card network notices, FTC Safeguards notices, and SEC materiality. It has never been exercised across divisions.
8. **Division supplement drift.** The Managed IT supplement was last aligned in 2024. It allows push MFA for technicians, 12-hour sessions, and 90-day RMM log retention, which conflict with 2026 group policy.
9. **Common control inheritance.** Documented for Cloud Hosting (FedRAMP package and SOC 2 system description) and Payment Processing (PCI DSS responsibility matrix for group services), but not for Managed IT.
10. **DOJ Data Security Program screening.** Two follow-the-sun support vendors with access to support tickets and logs are screened against sanctions lists but not for covered-person ownership or control under 28 CFR Part 202.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P02 | The HCP (registry default "Hosting control plane and customer portal", kept). It is the focus division's primary system and also the platform the other two divisions run on, so it carries the group's top risk |
| P03 | Cloud Hosting (focus): FedRAMP Consolidated Rules for 2026, for maintaining the G1 Rev5 Class C certification, plus the bank service provider rule, DFARS 252.204-7012(b)(2)(ii)(D) cloud duties for DIB customers, HIPAA business associate duties, and Fla. Stat. 501.171 third-party agent duties. Managed IT: DFARS 252.204-7012 and CMMC Level 2 (NIST SP 800-171 Rev. 2), External Service Provider scoping, FAR 52.204-21, HIPAA business associate duties, and the bank rule. Payment Processing: FTC Safeguards Rule (16 CFR Part 314) and PCI DSS v4.0.1, sponsor bank terms, and state money transmitter licensing (generic). Group-wide: SEC disclosure, DOJ Data Security Program, state breach laws, CIRCIA status. A regulation-by-division matrix ties them together |
| P08 | Compromise of provider tooling affecting downstream customers (registry default), adapted to cross divisions: a stolen Managed IT engineer session reaches the HCP run-command service and the RMM, touching managed-hosting tenants, Managed IT clients, Payment Processing connected-to servers, and the CUI enclave |
| P09 | SOC 2 scoped per division: SL-1 Commercial Cloud in scope (existing Type 2); Managed IT managed services in scope (first report, requested by bank and DIB clients); Payment Processing out of scope for SOC 2, with reasons (PCI DSS and SOC 1 already serve its user entities) |
| P10 | Group AI governance program, with AI-driven security operations (alert triage) as the priority use case (registry default, kept) and division use cases under their own rules (FedRAMP third-party resources, CMMC Security Protection Data, card network and FTC rules, Colorado SB26-189 watch) |
| Cloud | The group runs on its own commercial cloud (SL-1), so the Cloud Hosting division is both a provider and the group's internal platform. The backup vault is held with an unaffiliated provider. Vendor-agnostic |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-05-04 to 2026-07-31 | Group and division BIAs and risk analyses |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples |
| 2026-08-03 to 2026-08-28 | Regulatory gap analyses (three divisions and group) |
| 2026-08-31 to 2026-09-11 | SOC 2 readiness (two in-scope service lines) and AI risk assessment |
| 2026-09-17 | Results to the board risk committee; deliverables approved |
| 2026-10-01 | Group policies v2026 effective |
| 2026-11-10 | CMMC Phase 2 begins (32 CFR 170.3(e)(2)) |
| 2026-12-07 | FedRAMP Rev5 VDR and VER rules must be followed to maintain certification (grace ends 2027-03-07) |
| 2026-12-09 | First cross-division incident tabletop (P08 scenario) |
| 2027-01-01 | FedRAMP Consolidated Rules for 2026 take mandatory effect |
| 2027-02-08 | G1 annual FedRAMP independent assessment starts (the first after 2027-01-01, which ends the grace period for the FRC, IVV, and MAS rulesets) |
