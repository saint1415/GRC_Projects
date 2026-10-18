# Intake Report: Cris Santos Company Holdings | Professional Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company; Tax and Advisory and the affiliated CPA Partners attest firm, Wealth, and Practice Cloud; corporate shared services) |
| Intake window | 2026-04-13 to 2026-05-01 (one late answer received 2026-06-03) |
| Collected by | Group GRC team (Group CISO's office), with the division security and compliance leads, the CPA Partners risk and quality partner, and the Group Chief Privacy Officer |
| Approved | Board risk committee, 2026-09-10, with the other deliverables |

## 1. Purpose and scope
Intake collected the group's own records after the filing season and before any assessment work began on 2026-05-04. It covers the legal entities, the systems that hold tax return information, customer information, client funds instructions, customer firms' data and PHI in each division and in corporate shared services, the suppliers that touch them, and the rules that may bind each entity. Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Rows are grouped by unit: the title of each row starts with Group, Tax and Advisory, CPA Partners, Wealth or Practice Cloud. Later steps add their own fieldwork evidence (interviews, document reviews, tests) to the same register, so one list backs every deliverable.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analyses (P03) and the control assessment (P07).

## 2. Sources collected
| Unit | Area | Evidence IDs | System of record | As of |
|---|---|---|---|---|
| Group | Entities, workforce, revenue and contracts | EV-001 to EV-004 | Entity management system; HR system; ERP and Form 10-K; contract management system | 2025-12-31 to 2026-03-31 |
| Group | Identity and access (SYS-G1) | EV-005 to EV-008; EV-075 | Identity platform, identity governance and PAM consoles; HR, background check and learning systems | 2026-03-31 to 2026-05-31 |
| Group | Security operations (SYS-G2) | EV-009 to EV-014 | Endpoint and EDR consoles; SIEM; email gateway; case management; scanners; penetration test reports | 2026-03-31 |
| Group | Policies and common controls | EV-015 to EV-017 | Policy repository; GRC tool | 2026-03-31 |
| Group | Cloud, network, backups and email (SYS-G3, SYS-G4) | EV-018 to EV-023 | Cloud consoles; guardrail service; network management; key management; backup vault; email admin console | 2026-03-31 |
| Group | Incident, disclosure, risk and audit | EV-024 to EV-028 | SOC library; SEC filings; board minutes; GRC tool; internal audit | 2026-01-31 to 2026-03-31 |
| Group | Workforce, vendors, AI, records and change | EV-029 to EV-038 | Learning and HR systems; vendor master and third-party risk tool; vendor portals; procurement and SaaS discovery; records management; privacy office; facilities; change system | 2025-12-31 to 2026-04-24 |
| Tax and Advisory | Billing, clients, Qualified Individual, TPCP, consent, AI, e-file, client accounting | EV-039 to EV-056 | ERP billing; SYS-T1 reporting and documentation; board of managers minutes; client portal; compliance reviews; AI service console; change system; continuity library; SYS-T2 consoles | 2025-05-30 to 2026-04-30 |
| CPA Partners | Firm, engagements, supplement and SYS-T3 | EV-057 to EV-058 | CPA Partners practice management system; quality management library | 2026-03-31 |
| Wealth | Registration, Regulation S-P and S-ID programs, archive, platform, money movement, analytics | EV-059 to EV-065 | Compliance records and library; archiving console; SYS-W1 consoles; operations procedures; analytics platform | 2026-03-31 |
| Practice Cloud | SOC 2, contracts, AI feature, architecture, recovery, tenants, data use, deletion | EV-066 to EV-074 | Trust and assurance library; contract management; release system; vendor records; architecture repository; admin reporting | 2025-12-12 to 2026-03-31 |

## 3. Observations by area
**Entities and scale.** The holding company is an SEC registrant and wholly owns Tax and Advisory, Wealth and Practice Cloud; CPA Partners is owned by its CPA partners and buys staff, offices and technology from the holding company (EV-001, EV-057). The workforce is 45,000: CPA and Tax Services about 28,500, Wealth about 6,500, Practice Cloud about 5,500, corporate about 4,500, plus about 11,000 seasonal tax professionals from January to April (EV-002). FY2025 revenue was about $18.0 billion: CPA and Tax Services about $9.4 billion, Wealth about $5.2 billion, Practice Cloud about $3.4 billion (EV-003); about 62% of Tax and Advisory revenue is billed from February through April (EV-039). The register holds four intercompany agreements: the 2022 integrated planning agreement has no Regulation S-P 72-hour term, the Wealth services agreement was amended in 2025-11 with it, the 2021 administrative services agreement has no security, incident notice or subcontractor terms, and the 2024 Practice Cloud master agreement has a 72-hour term. No division holds a federal contract (EV-004).

**Group identity and access.** Number-matching MFA for the workforce and hardware keys for administrators; conditional access blocks sign-in from outside the United States for Tax and Advisory users (EV-005). Identity governance runs from HR events; office managers can extend seasonal accounts by up to 30 days; the Q1 2026 certification covered permanent staff (EV-006). For the 2026 season, 14% of seasonal accounts show activation before the background check or training completion date (EV-007), and a late answer to an intake request shows seasonal accounts were disabled an average of 9 days after the season ended (EV-075). Privileged access is just in time through PAM with session recording (EV-008).

**Group security operations.** EDR covers every office workstation, laptop and cloud workload (EV-009). The SOC runs 24x7; inbox-rule and forwarding alerts cover corporate and Wealth mailboxes; tax office mailbox events and Practice Cloud bulk-download alerts are not SIEM data sources; SYS-T1 bank-field and portal download records have no review use case (EV-010). The playbooks contain no IRS reporting step (EV-012). Scanning is continuous for TPCP and Practice Cloud workloads and monthly for office endpoints (EV-013); SYS-T1 and SYS-S1 were penetration tested in 2026-03 (EV-014).

**Policies and common controls.** The group policies in force are aligned to CSF 2.0 and approved by the board risk committee, and the Tax and Advisory program index lists the parts of its written program (EV-015). The CPA Partners supplement is v2023, last aligned 2023-04 (EV-016). The common control catalog covers SYS-G1 to SYS-G4; inheritance is recorded for Tax and Advisory, Wealth and Practice Cloud, and there is no record for CPA Partners (EV-017).

**Cloud, network, backups and email.** Provider A hosts the corporate hub, SYS-T1, SYS-T3 and the Wealth integration hub; provider B hosts Practice Cloud and the immutable backup vault (EV-018). Guardrails are preventive, with a daily compliance scan and an exception register (EV-019). One SD-WAN connects about 1,210 offices, with cellular failover at every tax office (EV-020). Keys are customer-managed per division account (EV-021). Restore tests run each quarter for High-criticality systems (EV-022). One email tenant serves every division: legacy authentication is allowed for the 1,150 office intake mailboxes and external forwarding for 212 mailboxes, both under 2019 exceptions (EV-023).

**Incident notification, disclosure, risk and audit.** Each division keeps its own notification matrix; there is no combined matrix, and exercises to date are technical (EV-024). The Form 10-K Item 106 disclosure and the disclosure committee charter cover cybersecurity incidents (EV-025). The board risk committee receives quarterly cyber reports (EV-026). Risk assessments ran in 2024 and 2025, and the Qualified Individual reviews the POA&M each quarter (EV-027). The 2026 internal audit plan schedules the common control assessment for July and August (EV-028).

**Workforce, vendors, AI and records.** Training covers business email compromise, refund changes and IRC 7216 (EV-029); screening and sanctions records are on file (EV-030). The vendor program is tiered; files hold onboarding assessments for every tier 1 vendor and SOC report reviews each year for the cloud, identity, SIEM and EDR, productivity, payroll and bookkeeping vendors (EV-031, EV-032). AI in use or contracted: AI-001, the AI-002 and AI-003 pilots, audit analytics with an embedded model at CPA Partners, the AI-005 meeting assistant pilot, Practice Cloud's AI document intake, a coding assistant and an enterprise assistant pilot (EV-033). Client files are kept 7 years (EV-034).

**Tax and Advisory.** About 5.6 million individual returns and 380,000 other returns a year; customer information on about 24 million consumers; about 21% of individual clients in Florida (EV-040). The Group CISO was designated Qualified Individual on 2025-02-03, and written reports went to the board of managers for 2024 and 2025 (EV-041). Office managers hold regional read access to returns (EV-043). The referral interface sends a record when a coordinator sets the CRM consent flag and has no step that reads a consent record (EV-044); the 2022 integrated planning consent describes "financial planning and investment services" (EV-045). A compliance review recorded no call-back for 11 of 60 sampled refund bank-account changes (EV-046). AI-001 processed documents for about 1.9 million returns under a contract with U.S.-only processing, no training and 30-day deletion, and its monitoring has no accuracy measure by document type (EV-047, EV-048); the AI-002 and AI-003 change records have no IRC 7216 or Circular 230 review attached (EV-049). EFIN and PTIN volumes were checked weekly in season (EV-050). The 2025-12 contingency test records no e-file gateway failover at season volume (EV-051). Client MFA has been mandatory in the portal since 2025-12 (EV-052). Purge jobs are not running in the archive tier (EV-053). Client accounting services runs on one payroll SaaS and a 2024 contingency plan (EV-055); 3 of 30 sampled direct deposit changes had no recorded call-back, and 60 clients have asked for a SOC 2 report (EV-056).

**CPA Partners.** About 6,200 engagements a year, including about 85 audits of HIPAA covered entities under business associate agreements; no SEC issuer or group entity is a client (EV-057). SYS-T3 grants access per engagement team and is run by Tax division IT (EV-058).

**Wealth.** SEC-registered adviser with about $540 billion under management for about 980,000 households, a larger entity for Regulation S-P, and within Regulation S-ID by counsel's 2024 determination (EV-059). The Regulation S-P program was adopted 2025-11-17; its oversight program lists outside vendors, not Tax and Advisory or corporate (EV-060). The Identity Theft Prevention Program's red flags are written for external requests and account changes (EV-061). The AI-005 pilot is not an archive source (EV-062). Custodial statements and planning data for about 210,000 integrated planning households go to Tax and Advisory (EV-063). Wealth analytics builds household compilations from referral fields (EV-065).

**Practice Cloud.** The SOC 2 Type 2 report for the period ending 2025-09-30 was issued 2025-12-12 and predates the AI feature (EV-066). About 26,000 customer firms; standard notice is 72 hours, 24 hours for 140 enterprise customers; the published sub-processor list does not name the AI intake model provider (EV-067). AI document intake launched 2026-02-02 with no privacy, IRC 7216 or contract review attached, and the product page claims "99% accurate extraction" (EV-068); U.S. processing for the model provider is a configuration setting, not a contract term (EV-069). The service uses a shared database with row-level security and per-tenant keys (EV-070); failover was tested in 2026-01 (EV-071); 31% of customer firms do not enforce MFA (EV-072). Deletion of terminated customers' data is manual (EV-074).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Seasonal account disablement dates for the 2026 season end | Group identity director | 2026-04-20 | Received 2026-06-03 after the extension period ended (EV-075) |
| Inheritance matrix for group common controls used by CPA Partners | CPA Partners risk and quality partner | 2026-04-24 | None exists; carried into P02 and P07 (POAM-016) |
| Legal position on Practice Cloud under the Safeguards Rule and IRC 7216 | Group General Counsel | 2026-04-27 | Answered in P03 fieldwork by the 2026-06-10 memo (EV-084) |
| AI-004 audit analytics tool details and its handling of PHI | CPA Partners risk and quality partner | 2026-04-27 | Not provided at intake; registered in the AI inventory in 2026-06 (P10) |
| Workforce use of public generative AI tools outside the approved tools | Group CISO | 2026-04-27 | Not established at intake; P10 treats it as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Revenue by division (EV-003) and by month (EV-039), client and household volumes (EV-040, EV-055, EV-059, EV-070), backup and recovery records (EV-022, EV-051, EV-071), vendor recovery terms (EV-055), and dependencies from the asset and vendor registers |
| P02 SSP | The TPCP boundary from the asset inventory (SYS-T1, SYS-T1-REF, SYS-T1-TEN, END-TAX); as-found configuration from EV-005 to EV-023 and EV-042 to EV-053; common controls from EV-017 |
| P04 Cloud mapping | Cloud and platform components (EV-018 to EV-023, EV-042, EV-058, EV-063, EV-070) and provider assurance (EV-032, EV-066) |
| P01 Risk registers | Likelihood inputs from configuration exports, inventories, contracts, plans and reviews in every unit (the `likelihood_basis` column) |
| P03 Gap analyses | The obligations register (which rules apply to which entity) and every observation above, compared with the requirements |
| P06 Policies | The group policies in force (EV-015) and the division supplements (EV-016, EV-058) |
| P07 Control assessment | Populations to sample from (EV-002, EV-006, EV-007, EV-023, EV-044, EV-045) |
| P08 IR runbook | Notification duties per entity from the obligations register; the division matrices (EV-024); contract notice terms (EV-004, EV-067) |
| P09 SOC 2 | The Practice Cloud SOC 2 report (EV-066), vendor reports (EV-032) and client accounting services records (EV-055, EV-056) |
| P10 AI governance | AI tools found (EV-033, EV-047, EV-049, EV-068, EV-069, EV-062) |
