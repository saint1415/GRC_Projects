# Scenario facts: Cris Santos Company | Information Technology | Multi-Sector

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, a standard, or a government program page, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company Holdings, Inc. (publicly traded SEC registrant; large accelerated filer) |
| Structure | A holding company with three divisions and corporate shared services. Each division is a separate legal subsidiary under common ownership |
| Division 1: Cloud Hosting (NAICS 518210, sector 51 Information), **focus of this scenario** | Cloud hosting and managed infrastructure provider. About 21,000 employees. Three service lines: **SL-1 Commercial Cloud** (multi-tenant IaaS and PaaS: compute, block and object storage, managed databases, managed Kubernetes, networking, DNS, and content delivery) in five commercial regions (R1 to R5), each with three company-operated data centers; **SL-2 Government Cloud**, a dedicated region (G1) with two company-operated data centers (G1-A and G1-B) in two eastern states; **SL-3 Managed Hosting**, SL-1 tenants whose servers are operated for them by the Managed IT division (section 7). About 38,000 business customers and about 290,000 customer console identities (EV-036). Its duties as a FedRAMP certified provider, a cloud provider to DIB customers, a bank service provider, a HIPAA business associate and an affiliate service provider to Payment Processing are decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (C-IT-R01-CH, C-IT-R03-CH, C-IT-R05-CH, N54-R06-CH, N52-R03-AFF) |
| Division 2: Managed IT and Consulting (NAICS 541513 and 541512, sector 54 Professional, Scientific, and Technical Services) | Managed IT services (monitoring, patching, backup, and administration of client servers and endpoints through a remote monitoring and management (RMM) platform), IT consulting, and federal IT services. About 12,000 employees. About 2,900 client organizations, including banks and credit unions, health care organizations, defense industrial base (DIB) companies, and federal agencies (section 7; EV-058). Its duties are decided in the obligations register (C-IT-R02-MI, C-IT-R03-MI, N54-R04-MI, N54-R06-MI, C-IT-R05-MI) |
| Division 3: Payment Processing (NAICS 522320, sector 52 Finance and Insurance) | Merchant payment processing (card authorization, clearing, and settlement), ACH origination, and consumer bill payment for billers. About 7,000 employees. About 210,000 merchants and about 2,300 billers; funds move through two sponsor banks. A PCI DSS Level 1 service provider. Group legal treats it as a financial institution under the FTC Safeguards Rule (EV-034). Both decided in the obligations register (PCI-DSS, N52-R03-PP) |
| Corporate shared services | Identity, security operations, the group landing zone, HR, finance, legal, risk, privacy, and internal audit. About 5,000 employees |
| Location | Headquartered in Florida. Commercial region R1 is in Florida; R2 to R5 and G1 are in other states. Employees in 46 states; customers and data subjects in all 50 states. **State law is handled generically** ("each state where affected individuals reside"), with Florida as the worked example |
| Workforce / revenue | 45,000 employees; about $18.0 billion annual revenue (fictional) |
| Not in scope by fact | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv). No bank charter in the group; no New York financial services license (NYDFS Part 500 does not apply); no broker-dealer or investment adviser (SEC Reg S-P does not apply); no 42 CFR Part 2 program; no child-directed services. No employees, contractors, or data centers in a country of concern under 28 CFR Part 202 |
| FAR overhaul clause numbers | Background fact, not scored in P03. Contracts awarded before the contracting agency adopted its FAR Part 40 class deviation keep the clauses this sample cites (FAR 52.204-21, 52.204-23, 52.204-25 and DFARS 252.204-7019 and -7020) until they are modified. New awards under the deviation carry FAR 52.240-93, which has the same 15 safeguarding requirements as FAR 52.204-21, and FAR 52.240-91, which replaces the separate Kaspersky, Section 889 and FASCSA reports with one report within 72 hours. New DoD awards under DFARS Part 240 (DoD Class Deviation 2026-O0025, Revision 3) carry 252.240-7997 for DoD-led Medium and High NIST SP 800-171 assessments instead of 252.204-7019 and -7020. Sources: SRC-FAR-RFO-PART40 and SRC-DFARS-DEV-2026-O0025 |

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
| External assurance | FedRAMP Recognized independent assessment service (annual G1 assessment); SOC 2 service auditor (independent CPA firm); PCI Qualified Security Assessor (QSA); ISO/IEC 27001 certification body. A CMMC Third-Party Assessment Organization (C3PAO) is not yet engaged (voluntary while CMMC Phase 2 is suspended; EV-063) |

**Where roles overlap and how it is compensated:** each division CISO both runs the division's controls and reports on them, and the Group SOC director both operates the AI triage service and owns its risk. The group compensates with group internal audit (independent of operations), the external assessors above, and the Group AI council, which approves High-tier AI use cases that the SOC proposes.

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv). Suppliers and affiliates are in the [vendor register](step-00_P00_intake/vendor-register.csv).

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
| SYS-M1 | Managed operations platform: the RMM (a SaaS product from an RMM vendor; one tenant for all clients and internal uses), plus professional services automation and ticketing and the client privileged access broker (company-run on SL-1) | Managed IT |
| SYS-M2 | Consulting delivery workspace (on SL-1) and the DoD CUI enclave (a separate tenant in G1, the FedRAMP-certified Government Cloud, for the division's own DoD subcontracts) | Managed IT |
| SYS-P1 | Payment processing platform: authorization switch, tokenization vault, payment HSMs, clearing and settlement. This is the cardholder data environment (CDE), in dedicated SL-1 accounts in R1 and R3 | Payment Processing |
| SYS-P2 | Merchant and biller portals, consumer bill-pay service, ACH origination, merchant onboarding and risk scoring | Payment Processing |

**SSP system (P02):** the *Hosting Control Plane and Customer Portal (HCP)*: SYS-H1 in both partitions (commercial and G1), with the management interfaces of SYS-H2 and the fleet automation of SYS-H3 that act through it, inheriting common controls from SYS-G1, SYS-G2, and SYS-G3; its G1 partition is the control plane of the FedRAMP Rev5 Class C Government Cloud offering.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Rows are grouped by division (Group, Cloud Hosting, Managed IT, Payment Processing). Every item has a source system, an owner, and as-of and collected dates.
- **Which rules apply** to each division and to the group is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps** against the FedRAMP Consolidated Rules for 2026 and the Cloud Hosting customer duties, DFARS 252.204-7012, CMMC and the Managed IT client duties, the FTC Safeguards Rule and PCI DSS, and the group-wide rules are judged in the gap analyses (P03), which also number the ten group gaps cited across this sample, and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

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
| 2026-03-30 to 2026-04-24 | Intake: evidence requests, exports, interviews, inventories, obligations register, grouped by division |
| 2026-05-04 to 2026-07-31 | Group and division BIAs (BIA interviews in May) and risk analyses (risk interviews in June) |
| 2026-06-01 to 2026-06-26 | Group policies v2026 drafted from the intake observations and the risks found so far (P06); the Cloud Hosting supplement was aligned to the drafts on 2026-06-30 |
| 2026-07-06 to 2026-08-28 | Common control assessment (group internal audit) plus division samples: operating tests of controls in place under the 2025 group policies; the draft v2026 policies were reviewed for design only |
| 2026-08-03 to 2026-08-28 | Regulatory gap analyses (three divisions and group) |
| 2026-08-31 to 2026-09-11 | SOC 2 readiness (two in-scope service lines) and AI risk assessment |
| 2026-09-17 | Results to the board risk committee; deliverables and group policies v2026 approved (policies effective 2026-10-01) |
| 2026-10-01 | Group policies v2026 effective |
| 2026-11-10 | Planned start of CMMC Phase 2 (32 CFR 170.3(e)(2)); suspended by the DoD (Department of War) CIO memorandum of 2026-07-13 (DoD Class Deviation 2026-O0025, Revision 3) |
| 2026-12-07 | FedRAMP Rev5 VDR and VER rules must be followed to maintain certification (grace ends 2027-03-07) |
| 2026-12-09 | First cross-division incident tabletop (P08 scenario) |
| 2027-01-01 | FedRAMP Consolidated Rules for 2026 take mandatory effect |
| 2027-02-08 | G1 annual FedRAMP independent assessment starts (the first after 2027-01-01, which ends the grace period for the FRC, IVV, and MAS rulesets) |
| 2027-04 (planned) | Follow-up assessment: operating effectiveness of the controls the v2026 policies introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables could be completed. They do not change sections 1 to 6.

| Topic | Added fact |
|---|---|
| Revenue split (fictional) | Cloud Hosting about $10.2 billion (about $27.9 million per day); Managed IT about $4.8 billion (about $13.2 million per day); Payment Processing about $3.0 billion in net revenue (about $8.2 million per day), while moving about $1.9 billion of merchant and biller funds per business day. Total about $18.0 billion, as in section 1 (FY2025, EV-003) |
| Risk acceptance | Very Low and Low: division security lead. Moderate: division president. High: Group Chief Risk Officer with the Group CISO, reported to the board risk committee. Very High: board risk committee only. A High risk to federal customer data, CUI, cardholder data, or a bank's covered services must be treated, not accepted (POL-01 4.4; risk acceptance standard, EV-005) |
| Workforce detail | About 1,400 contractors in addition to the 45,000 employees. The group SOC has about 260 analysts in three sites. Managed IT has about 6,800 managed services engineers; about 1,900 hold the HCP partner-operator role. G1 operations staff are U.S. persons (EV-002, EV-047) |
| Cloud Hosting footprint | 17 company-operated data centers (15 commercial in R1 to R5; G1-A and G1-B) and 41 edge points of presence. The public status page is hosted outside SL-1 and G1 (EV-053, EV-054) |
| Cloud Hosting customers | About 260 banking organizations on SL-1 (designated contacts on file for 182); about 900 health care customers under BAAs (standard BAA breach notice: 10 calendar days); customer agreement incident notice within 72 hours of confirmation; SLA 99.99% multi-zone and 99.9% console and API; maintenance notices to bank customers 10 days ahead. MFA is required for tenant root owners (since 2025) and enabled by about 61% of other customer administrator users (EV-036, EV-037, EV-038, EV-056) |
| Managed hosting (SL-3) | About 4,100 SL-1 tenants are operated by Managed IT engineers through the HCP partner-operator role, with each tenant's contractual consent (EV-036, EV-047) |
| G1 details | Legacy FedRAMP Moderate agency authorization on 2023-03-15 with a civilian agency as sponsor; now a Rev5 Class C certification. Annual independent assessment last completed 2026-03-20; the next starts 2027-02-08. FedRAMP Security Inbox since 2026-01 (a 2026-05 Emergency test was acknowledged in 20 minutes). Secure Configuration Guide published 2026-02. The FedRAMP IEC rules were adopted early in 2026-08. Agencies order G1 under federal contracts that include FAR 52.204-21, 52.204-23, 52.204-25, and 52.204-30. Agency incident procedures are on file for 21 of 27 agencies. Two Cloud Hosting staff hold DoD medium assurance certificates for DIBNet. Two G1 services (managed database proxy, object storage gateway) lack cryptographic module documentation (EV-039 to EV-045, EV-093, EV-094) |
| Managed IT clients | About 380,000 client servers and endpoints under the RMM. About 190 banks (designated contacts on file for 121) and about 120 credit unions; about 210 health care clients under BAAs (breach notice terms from 10 to 60 days); about 150 DIB clients (CUI enclaves managed for 18); 11 federal civilian agency contracts with FAR 52.204-21 (6 subcontracts with flowdown); 9 DoD subcontracts with DFARS 252.204-7012. Client agreement incident notice within 48 hours of confirmation (EV-058, EV-059) |
| Managed IT identity and tooling | The legacy identity tenant dates from before the 2022 group consolidation; migration to SYS-G1 is due 2027-03-31. The RMM vendor keeps audit logs 90 days by default; the RMM contract has no incident notice clock. One DIBNet medium assurance certificate holder. The enclave's SP 800-171 basic self-assessment (2024-02-12) shows 96 of 110 requirements fully met (EV-060, EV-061, EV-028, EV-064, EV-063) |
| Payment Processing | About 3.1 billion card transactions a year; about 14 million enrolled consumer bill payers. Sponsor bank A sponsors card acquiring; sponsor bank B handles ACH origination and bill-pay settlement. Both sponsor bank agreements require notice within 24 hours of determining a security incident that affects program data or disrupts program services, and treat the division's processing as covered services. PCI DSS Report on Compliance 2026-04-30 (no open items); segmentation tests 2025-09 and 2026-03. Group legal decided in 2023 to treat the division as a financial institution under 16 CFR 314.2(h); the division CISO was designated Qualified Individual the same year. Division security team of about 140. State money transmitter licenses are held where the bill-pay service requires them; none in New York. 140 settlement-support servers in the CDE connected-to segment carry RMM agents (EV-069, EV-072, EV-080, EV-034, EV-070, EV-061) |
| Vendors | Two follow-the-sun support vendors (in countries that are not countries of concern under 28 CFR Part 202) can see support tickets and logs (EV-027) |
| AI | Group AI Standard adopted 2026-04-20; Group AI council chaired by the Group Chief Risk Officer. AI triage enabled 2025-11 (about 64% of alerts auto-closed). The Managed IT runbook automation agent ran unattended from 2026-03 until 2026-10-01. Inventory of 10 use cases in P10 (EV-029, EV-030, EV-013, EV-068) |
| SOC 2 periods | SL-1 Type 2 periods run July 1 to June 30 (EV-055, EV-082). Managed IT targets a Type 1 as of 2027-06-30 and a Type 2 for 2027-07-01 to 2027-12-31 |
| Registry defaults | Kept: the primary system (HCP), the incident type (compromise of provider tooling, adapted to cross divisions), and the AI use case (AI-driven security operations, AI-001) |
