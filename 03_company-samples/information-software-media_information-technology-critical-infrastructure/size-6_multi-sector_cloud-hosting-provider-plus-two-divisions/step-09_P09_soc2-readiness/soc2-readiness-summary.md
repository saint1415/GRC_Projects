# SOC 2 Readiness Summary: Cris Santos Company Holdings | Information Technology | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: SL-1 Commercial Cloud (`soc2-readiness.csv`) and Managed IT managed services (`soc2-readiness-managed-it.csv`). Payment Processing and G1 are out of scope for SOC 2, with reasons |
| Prepared | 2026-09-11 by the Group Chief Risk Officer's assurance team with the Cloud Hosting and Managed IT security leads; presented 2026-09-17 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division and service line is whether customers build their own control environment on it, and whether some other assurance already serves them better.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Cloud Hosting | SL-1 Commercial Cloud (about 38,000 customers) | **Yes.** Customers run their own systems on it and rely on its controls (carved into their own audits) | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending June 30 |
| Cloud Hosting | SL-3 Managed Hosting (about 4,100 tenants) | Yes, as part of SL-1, but the operations are performed by the Managed IT division | **In scope through SL-1**, with the partner-operator path described as a component (not yet done: CC2.3) | Same as SL-1 | Same report |
| Cloud Hosting | SL-2 Government Cloud (G1) | Yes | **Out of SOC 2 scope.** Agencies and DIB customers rely on the FedRAMP certification and its annual independent assessment; no customer has asked for a SOC 2 report on G1 | n/a | FedRAMP package (P03) |
| Managed IT | Managed services (RMM-based operations for about 2,900 clients) | **Yes.** Banks, health care organizations, and DIB clients rely on the division's controls over their systems | **In scope.** First readiness assessment, requested by bank and DIB clients | Security, Availability, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Managed IT | Consulting projects | No ongoing service on which clients build controls | Out of scope | n/a | n/a |
| Payment Processing | Card processing, ACH, bill pay | Yes, but its user entities already get the assurance they need | **Out of SOC 2 scope** (reasons below) | n/a | PCI DSS ROC and AOC; SOC 1 Type 2 |

**Why Payment Processing is out of SOC 2 scope:**
1. **Its user entities rely on other reports.** Merchants and sponsor banks rely on the PCI DSS Attestation of Compliance for the security of account data, and on the SOC 1 Type 2 report for settlement controls that affect their financial statements.
2. **Its regulators and counterparties examine it directly.** Sponsor bank oversight, card network rules, state money transmitter licensing, and the FTC Safeguards Rule set its program (P03).
3. **Questionnaires** from billers and merchants are answered with the AOC, the SOC 1 report, and the group security program description.
4. **Revisit trigger:** if a large biller or platform partner contractually requires SOC 2, or the division launches a service outside PCI DSS scope (for example, a data analytics product), assess SOC 2 again.

Payment Processing still benefits from this work: the SL-1 platform controls and the group common controls that both in-scope reports carve in are the ones its PCI DSS responsibility matrix must now cover (scenario gap 6).

**Other assurance considered.** ISO/IEC 27001, the vertical overlay's other assurance mechanism, is already held by the Cloud Hosting division and is kept. FedRAMP covers G1. Neither replaces SOC 2 for SL-1 customers, whose contracts require a SOC 2 report.

## 2. System descriptions (scope)
### 2.1 SL-1 Commercial Cloud
- **Services:** compute, storage, managed databases, managed Kubernetes, networking, DNS, and content delivery in regions R1 to R5; SL-3 managed hosting.
- **Infrastructure and software:** the HCP (commercial partition), the SYS-H2 fleet, SYS-H3 signing and fleet automation, SYS-H4 edge; group common controls carved in (SYS-G1, SYS-G2, SYS-G3).
- **People:** about 21,000 Cloud Hosting employees; the group SOC and identity teams; **about 1,900 Managed IT partner operators (not yet in the description)**.
- **Subservice organizations (carve-out):** the backup vault at external provider X; the identity SaaS vendor and SIEM vendor (through group services); **the AI triage service's third-party model provider (not yet in the description)**.
- **Complementary user entity controls:** customers manage their own users and MFA, choose replication across zones and regions, and approve partner-operator and support access to their tenants.

### 2.2 Managed IT managed services
- **Services:** monitoring, patching, backup oversight, and administration of client servers and endpoints; managed hosting operations on SL-1.
- **Infrastructure and software:** the RMM (vendor SaaS), the PSA and ticketing system and the client access broker (on SL-1); group common controls.
- **People:** about 6,800 managed services engineers.
- **Subservice organizations (carve-out):** the RMM vendor; the Cloud Hosting division (SL-1 hosting of the PSA and access broker), which is an affiliate but must be treated as a subservice organization in the description.
- **Complementary user entity controls:** clients approve changes on their systems, keep their own privileged accounts, and tell the division who may authorize work.

## 3. Readiness results
### 3.1 SL-1 Commercial Cloud (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3. The system description issued for the period ending 2026-06-30 omits the partner-operator path through which another division acts in about 4,100 tenants, and omits the AI triage service's model provider.
**Partially ready:** CC6.1, CC6.2, CC6.3 (the partner-operator path), CC7.2 and CC7.3 (run-command volume detection and AI triage auto-close), CC9.2 (model provider not reviewed), and A1.3 (no shared failure mode test).

**The immediate issue is the current period** (2026-07-01 to 2027-06-30). The partner-operator path operated throughout it. Management should expect the service auditor to evaluate CC2.3, CC6.1 to CC6.3, and CC7.2 for exceptions, and should describe the remediation (POAM-001, POAM-002, POAM-003) in the description for this period. Customers on managed hosting should hear about the path and its fix from the division before they read it in the report.

### 3.2 Managed IT managed services (`soc2-readiness-managed-it.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 19 | 11 | 3 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why many criteria are Ready for a first report:** governance, risk assessment, HR, physical, and general IT controls come from group common controls already evidenced for the SL-1 report.
**Not ready:** CC2.3 (no system description; inconsistent commitments), CC6.3 (one RMM tenant for all clients, access kept after transfers, agents on other divisions' systems), and CC7.2 (RMM logs kept 90 days and not monitored).
**Partially ready:** CC2.1, CC3.4, CC4.1, CC5.3, CC6.1, CC6.2, CC6.7, CC7.3, CC7.4, CC8.1, CC9.2, A1.3, and C1.1. Most trace to the RMM (scenario gap 2), the legacy identity tenant (gap 8), and undocumented inheritance (gap 9).

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | SL-1 | CC6.1, CC6.2, CC6.3, CC7.2, CC7.3, CC9.2 | PAM design for partner operators; certification results; run-command alert; AI triage seeded tests; model provider review |
| 2026 Q4 | Managed IT | CC5.3, CC6.2, CC7.2, CC7.3, CC7.4, CC8.1 | Re-issued supplement; RMM certifications; SIEM forwarding; case system; matrix; two-person approval records |
| 2027 Q1 | SL-1 | CC2.3, A1.3 | Updated system description and customer communication; shared failure mode exercise |
| 2027 Q1 | Managed IT | CC2.1, CC3.4, CC4.1, CC6.1, CC6.3, CC6.7, CC9.2, A1.3, C1.1 | Agent inventory; AI agent assessment (P10); inheritance matrix; SYS-G1 migration; agents removed from regulated environments; secret scanning; vendor term; RMM outage test |
| 2027 Q2 | Managed IT | CC2.3 | System description and standardized commitments. Type 1 as of 2027-06-30 |
| 2027 Q3 to Q4 | Both | All in-scope criteria | Operating evidence for the SL-1 2027-2028 period and the Managed IT Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the Cloud Hosting division president writes to managed-hosting customers about the partner-operator path and its remediation before the current-period report is issued. Managed IT sends bank and DIB clients a readiness letter with the 2027 timeline and, for DIB clients, the ESP responsibility matrix (POAM-022).
