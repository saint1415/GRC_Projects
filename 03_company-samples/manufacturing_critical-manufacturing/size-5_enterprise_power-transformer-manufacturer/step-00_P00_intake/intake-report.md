# Intake Report: Cris Santos Company | Critical Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded power and distribution transformer manufacturer: 7 plants in FL, GA, TN, TX, NC and OH; 9 service centers; 3 spare yards; 2 colocation data centers) |
| Intake window | 2026-05-04 to 2026-05-29 |
| Collected by | GRC team (second line), with system owners in IT, OT, product security, the plants, the service lines, the Integration Management Office and Internal Audit's prior workpapers |
| Approved | CISO and Chief Compliance Officer, 2026-05-29. Obligations register reviewed by the General Counsel's office, with outside counsel (EV-065) |

## 1. Purpose and scope
Intake collected the company's own records before the enterprise risk analysis, the BIA and the gap analysis began on 2026-06-01, and before Internal Audit's control assessment began on 2026-07-13. It covers the organization (7 plants, including the acquired Ohio plant AQ-01), the IT, OT, product and service line systems that support tier-1 processes, the suppliers that touch them, and the laws, contracts and standards that may bind the company and its two service lines (SL-1 and SL-2). Each item has an ID in [`evidence-register.csv`](evidence-register.csv). Later steps add their own fieldwork evidence (BIA interviews, risk workshops, gap analysis samples and walk-throughs, Internal Audit tests) to the same register, so one list backs every deliverable.

At this size the sources are enterprise systems of record across the business: the identity platform and HR system, the CMDB and the OT asset inventory, the cloud consoles and SIEM, the OT remote access gateway, the third-party risk register and accounts payable vendor master, the contract repository and obligations register, board and committee records, prior Internal Audit and SOX workpapers, and federal contract and trade compliance files.

The [asset inventory](asset-inventory.csv) reconciles the CMDB with the OT asset inventory, the cloud account inventory, the endpoint consoles and the AI register; the [vendor register](vendor-register.csv) reconciles the third-party risk register with the accounts payable vendor master and the contract repository.

This report records **observations, not findings**. Whether an observation meets a requirement is decided in the gap analysis (P03) and the control assessment (P07).

## 2. Sources collected
| Area | Evidence IDs | System of record | As of |
|---|---|---|---|
| Identity and access | EV-001 to EV-009 | Identity platform (SSO, PAM, identity governance); HR system; AQ-01 legacy directory; ERP, supplier portal and MES administration | 2026-04-30 to 2026-05-06 |
| Endpoints, OT and network | EV-010 to EV-021 | EDR and endpoint consoles; CMDB; OT monitoring platform; firewall and network management; OT remote access gateway; OT backup records; advisory tracker; scanner | 2026-04-24 to 2026-05-01 |
| Cloud, logging, backup and recovery | EV-022 to EV-032 | Cloud consoles and posture management; key management; backup accounts; SIEM; ERP audit log; SOC case management; DR records; EPSP document library and change records; integration platform; plant continuity plans | 2026-04-30 to 2026-05-16 |
| Governance, assurance and disclosure | EV-033 to EV-044 | GRC platform; ERM register; board portal; Internal Audit and SOX workpapers; General Counsel's office; SEC filing; SOC knowledge base; learning system; HR case management | 2025-12-31 to 2026-05-01 |
| Third parties, contracts and service lines | EV-045 to EV-059 | Third-party risk register; AP vendor master; sourcing files; contract repository; obligations register; notice log; PSIRT and pipeline records; service auditor report; service line contracts and platforms | 2025-12-31 to 2026-05-08 |
| Federal, trade, DOE and other obligations | EV-060 to EV-069 | Federal Programs files; bid files; Trade Compliance files; quality document control and TDMS; counsel memo; benefits, insurance and records files; threat intelligence platform | 2026-01-01 to 2026-05-15 |
| Facilities and disposal | EV-070 to EV-072 | Physical security systems; IT asset disposition; facilities library | 2026-04-30 |
| Business volume and structure | EV-073 to EV-077 | ERP financial and shipping reports; operational reporting; legal entity register; Integration Management Office tracker | 2025-12-31 to 2026-05-01 |
| Data and business applications | EV-078 to EV-081 | Productivity suite; data inventory; PLM, TDMS and data platform; HR and applicant tracking SaaS | 2026-04-30 to 2026-05-01 |
| AI | EV-082, EV-083 | AI governance committee register; vendor release notes and feature settings | 2026-05-22 |

## 3. Observations by area
**Identity and access.** About 9,400 workforce identities and 1,850 supplier and customer portal identities use SSO with MFA; AQ-01 users sign in to a legacy directory domain with a two-way trust to the corporate domain (EV-001, EV-006). MFA is required for every SSO application and for remote, cloud and administrative access, FIDO2 keys for privileged roles, and lockout follows 10 failed attempts (EV-002). Privileged access for cloud, domain, ERP and database administrators is just in time through PAM with session recording; there are 64 privileged EPSP accounts (EV-003). Joiner, mover and leaver events flow from the HR system, and quarterly certification for the ERP, HR and payroll closed each quarter; the AQ-01 directory is not connected (EV-004). HR holds about 12,000 employees; AQ-01 terminations are entered by hand (EV-005). The ERP has about 5,600 users, a separation-of-duties rule set and a Trade Compliance role for export release (EV-007). About 420 supplier portal accounts sit outside identity governance with no inactivity disable job (EV-008). About 3,800 MES users sign in with badge and PIN (EV-009).

**Endpoints, OT and network.** EDR reports on 98% of about 7,900 IT endpoints and on servers and supported kiosks (EV-010). Laptops are encrypted; 37 MES kiosks at P3 report an unsupported operating system (EV-011). The OT inventory holds about 3,900 assets; 148 of about 620 HMIs and engineering workstations run unsupported operating systems, 61 of them at AQ-01, and the AQ-01 list covers about 55% of its assets (EV-013, EV-014). P1 to P6 have OT DMZs with deny-by-default IT/OT firewalls; AQ-01 has a flat OT network and a dual-homed MES server (EV-015). NAC covers 70% of office sites, and AQ-01 has one carrier (EV-016). OEM sessions at P1 to P6 go through the gateway with approval, MFA and recording; AQ-01 is not connected (EV-017) and has 5 always-on OEM cellular routers with shared logins (EV-077). OT sensors cover P1 to P6, and their alerts route to the OT team in business hours (EV-018). Controller program backups are automated at P1 to P6, and restores are recorded at P1 (2025-11) and P5 (2026-03) only (EV-019). ICS advisories are tracked against a 30-day triage target (EV-020). IT scans run weekly (EV-021).

**Cloud, logging, backup and recovery.** Both clouds use account vending, guardrails as code and daily posture scans (EV-022). Keys are customer-managed (EV-023). Backups sit in separate accounts with write-once retention, 15-minute ERP log copies and a weekly offline copy at DC-2 (EV-024). The SIEM does not list the P3 and P4 MES application logs or the AQ-01 systems as sources (EV-025). The ERP logs master data and APS rule changes (EV-026). The SOC runs 24x7 with MSSP overflow (EV-027). The ERP failover test on 2026-05-16 lost 9 minutes of data against the 15-minute RPO and recovered in 11 hours against the 8-hour RTO; the FMS failover test on 2026-04-11 met its objectives (EV-028). EPSP documentation includes SSP v1.1 and contingency plan v5 (EV-029). Master data and APS scheduling rule changes are made in production by planners with elevated roles (EV-030).

**Governance, assurance and disclosure.** The 2025 policy set sits in the policy portal with standards, procedures and an exception register (EV-033). The 2025 risk analysis is integrated with ERM, and the board approved the risk appetite in 2026-02 (EV-034, EV-035). Internal Audit has no OT specialist on staff; independent OT test reports exist for P1 (2024) and P5 (2025) (EV-037). The disclosure committee has 7 members, 2 of whom joined in 2026, and its playbook has been exercised only on an IT data breach and has no method for lost production, deferred revenue or liquidated damages (EV-038). The FY2025 10-K includes Item 1C (EV-039). The incident response plan uses a single 48-hour clock for utility notices, and the 2026-03-24 tabletop used an IT ransomware and data breach scenario (EV-040). Training and monthly phishing simulations are recorded (EV-043).

**Third parties, contracts and service lines.** The vendor register lists about 2,400 suppliers, 410 with access or data and 46 Tier 1; 38% of Tier 2 reviews are past their due date, the TMU contract manufacturer has no assessment on record, and the EDI provider's SOC report expired 2026-03 (EV-045). Grain-oriented electrical steel comes from 2 suppliers, one supplying 68% (EV-049). 88 utility addenda set incident notice at 24 hours (27) or 48 hours (61), access-revocation notice at 1 business day and vulnerability disclosure at 30 days (EV-051). The obligations register does not yet hold the 12 AQ-01 addenda and has no field separating 24-hour from 48-hour terms (EV-052). SBOMs are on file for 61% of 2026 TMU firmware releases (EV-054). SL-1 received its first SOC 2 Type 2 report for 2025, with one exception (EV-056), and 5 STRS members have asked for a SOC 2 Type 2 report by 2027-12-31 (EV-059).

**Federal, trade, DOE and other obligations.** The company holds 11 civilian federal contracts with FAR 52.204-21, -23 and -25, and 52.204-30 in the 8 awarded since 2024; FCI is kept in the ERP and 11 labeled project sites (EV-060). SAM.gov FASCSA searches are recorded on 2025-11-04 and 2026-02-10 and none after (EV-061). The bid review gate declined a DFARS flow-down request in 2026-04 (EV-062). Products are EAR99, and AQ-01 screens export orders by hand (EV-063). The TDMS indexes certification data for P1 and P3 models; AQ-01 test data sits on a file server with no index or backup (EV-064). Counsel's view on each candidate rule is in EV-065; the results are in [`obligations-register.csv`](obligations-register.csv).

**Facilities and disposal.** Server rooms are badge-controlled with quarterly access list reviews; CCTV covers 2 of the 3 spare yards, and the Tennessee yard has no intrusion detection (EV-070). Certificates of destruction are on file (EV-071).

**Business volume and structure.** Revenue was about $4.8 billion in FY2025, about $13.2 million per calendar day (EV-073). Shipments are about $16.7 million per production day across the plants (EV-074). AQ-01 (about 650 employees) runs a legacy ERP and MES with nightly backups and no restore test record; its integration milestones run to 2027-06-30 (EV-077).

**AI.** The AI governance committee register lists 9 use cases with completed review (EV-082). The feature review found 5 AI features switched on inside existing products with no committee review record, including applicant ranking in the applicant tracking system (AI-006), for 14 use cases in total (EV-083).

## 4. Open requests
| Request | Asked of | Asked on | Status |
|---|---|---|---|
| Security questionnaire or assessment of the TMU electronics contract manufacturer | Director of Third-Party Risk Management | 2026-05-12 | Not received at intake; carried to the P01 register (R-010, R-023) and POAM-018 |
| Current SOC report from the EDI network provider | Director of Third-Party Risk Management | 2026-05-08 | Not received at intake; carried to P07 SA-9 and POAM-014 |
| Inventory of the remaining OT assets at AQ-01 | Director of OT Security and Vice President, Integration Management Office | 2026-05-07 | About 45% not established at intake; carried to POAM-010 |
| Restore test record for the AQ-01 legacy ERP and MES | Vice President, Integration Management Office | 2026-05-08 | None exists; carried to the BIA (DEP-20) and POAM-007 |
| AI features embedded in vendor products beyond the reviewed tier-1 SaaS | CIO | 2026-05-22 | Not established at intake; P10 treats further embedded features as unknown |

## 5. What each later step takes from intake
| Step | Takes |
|---|---|
| P05 BIA | Processes and owners (EV-005, EV-076), revenue and shipments (EV-073, EV-074), volumes (EV-075), recovery records (EV-019, EV-024, EV-028), contract commitments (EV-051, EV-057, EV-059), supplier concentration (EV-049), and dependencies from the asset and vendor registers |
| P02 SSP | The EPSP boundary from the asset inventory; prior SSP v1.1 and contingency plan v5 (EV-029); as-found configuration from EV-001 to EV-031 |
| P04 Cloud mapping | Cloud components and guardrails (EV-022 to EV-025) and provider assurance (EV-047) |
| P01 Risk register | Likelihood inputs from threat intelligence (EV-069), SOC case history (EV-027), coverage and configuration exports, the AQ-01 status (EV-077), the prior risk analysis and risk appetite (EV-034) |
| P03 Gap analysis | The obligations register (which rules apply) and every observation above, compared with the requirements |
| P06 Policies | The 2025 policy set and exception register (EV-033) |
| P07 Control assessment | Populations to sample from (EV-004, EV-005, EV-007, EV-012, EV-020, EV-021, EV-027, EV-030, EV-045) and prior Internal Audit workpapers (EV-037) |
| P08 IR runbook | Notification duties from the obligations register; the addenda and service line agreements (EV-051, EV-057, EV-059); disclosure committee records (EV-038); insurance terms (EV-067); contacts from the vendor register |
| P09 SOC 2 | The SL-1 2025 report (EV-056), service line agreements and records (EV-057 to EV-059) and vendor assurance on file (EV-047) |
| P10 AI governance | AI tools found (EV-082, EV-083) and AI subscriptions (EV-048) |
