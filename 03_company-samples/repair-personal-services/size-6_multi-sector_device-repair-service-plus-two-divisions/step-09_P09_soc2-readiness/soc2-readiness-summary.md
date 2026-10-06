# SOC 2 Readiness Summary: Cris Santos Company Holdings | Other Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Other Services (except Public Administration) (focus division: Device Repair) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: IT Support managed services (`soc2-readiness.csv`) and Device Repair enterprise depot and protection plan claims service (`soc2-readiness-device-repair.csv`). Electronics Retail is out of scope |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the IT Support and Device Repair security and compliance leads; criteria topic labels are short summaries written for this sample, not AICPA text |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each service line is whether other organizations rely on the group's controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| IT Support Services | Managed IT services for about 4,200 businesses (RMM, patching, monitoring, managed backup) | **Yes, a true service organization.** Customers rely on the division's controls over their endpoints, credentials, and backups; 610 practices also rely on it as their business associate | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending June 30; 2026 report issued 2026-08-28 with 2 exceptions |
| IT Support Services | Consumer tech support subscriptions | No. Consumers are not user entities | Out of scope | n/a | n/a |
| Device Repair | Enterprise depot repair (about 2,300 business accounts) and protection plan claim fulfillment for the TPA | **Yes, for this service line.** The TPA and enterprise accounts hand over devices and plan holders' data and rely on the division's custody, access, and sanitization controls. The TPA asked for a Type 2 report by the end of 2027 (P03 G-142) | **In scope.** First readiness assessment | Security, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30, issued by 2027-12-15 |
| Device Repair | Consumer repair at stores and counters | No. Consumers are not user entities | Out of scope (covered by the same controls, which helps) | n/a | n/a |
| Electronics Retail | Retail sale of electronics, plans, and subscriptions | **No.** Customers buy products; no organization relies on retail systems as part of its own control environment | **Out of scope** (reasons below) | n/a | n/a |

**Why Electronics Retail is out of scope:**
1. **No user entities.** Shoppers and loyalty members are consumers. The TPA and the partner bank receive data from Retail but do not rely on Retail's controls to run their own services.
2. **Assurance comes from somewhere else.** Retail validates PCI DSS every year with a QSA Report on Compliance as a Level 1 merchant (P03). The vertical profile names PCI DSS validation as the retail assurance alternative.
3. **Partner questionnaires** (the TPA, the partner bank) are answered with the group security program description, the retail AOC, and P07 results.
4. **Revisit trigger:** if Retail starts a business service that other companies rely on (for example, device management for business customers), assess whether it needs its own SOC 2 report.

**Other assurance considered.** Some managed services customers ask for ISO/IEC 27001 certification. The group decided SOC 2 remains the primary report for IT Support because customer contracts already require it. For Device Repair the TPA specified SOC 2.

## 2. System descriptions (scope)
### 2.1 IT Support managed services
- **Services:** remote monitoring and management, patching, endpoint protection management, help desk, managed backup and restore, and (pilot since 2026-07-06, 40 customers) the AI remediation agent.
- **Infrastructure and software:** SYS-D5 (RMM, PSA, remote support tool, credential vault, managed backup storage in provider B); group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** the RMM, PSA, remote support, and vault SaaS vendors; cloud provider B; **the AI agent's model provider** (not yet in the description).
- **People:** about 2,900 managed services staff plus group SOC and identity teams.
- **Data:** customers' administrator credentials, endpoint telemetry, backups (including ePHI for practices that buy managed backup).
- **Complementary user entity controls:** customers approve technician access, maintain their own user accounts, and review the RMM change reports the division sends monthly.

### 2.2 Device Repair enterprise depot and claims service
- **Services:** depot repair for business accounts, protection plan claim fulfillment for the TPA, certified destruction of replaced storage.
- **Infrastructure and software:** the STPP (SYS-D1) and the depot bench environment (SYS-D2); group common controls carved in.
- **Subservice organizations (carve-out):** cloud providers A and B; the courier; the certified electronics recycler.
- **Data:** business devices and their contents in custody; plan holders' names, contacts, and device details from the TPA.
- **Complementary user entity controls:** business accounts lock or encrypt devices before shipping and remove accounts they do not want the depot to see; the TPA validates plan holder identity before sending claims.

## 3. Readiness results
### 3.1 IT Support managed services (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 26 | 6 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC6.3. 14 standing RMM global administrators reach every customer, and the 2026 report already carried an exception on RMM access review. A repeat exception in 2027 is likely unless POAM-005 closes early in the period.
**Partially ready:** CC2.3 and CC3.4 (the AI agent is not in the description and started without a risk assessment), CC6.1 (local RMM accounts without MFA, disabled 2026-08-20), CC7.2 (PSA logs not monitored), CC8.1 (the 2026 change approval exception; multi-customer scripts without a second approver), CC9.2 (no subcontractor agreement with the AI model provider), A1.3 (no scheduled restore sampling), C1.1 (passwords in PSA attachments), and C1.2 (no destruction certificate for backup copies after offboarding).

**The immediate issue is the current period** (2026-07-01 to 2027-06-30). The AI agent has run since 2026-07-06, so it falls inside the period. Management must describe it, carve out or include the model provider as a subservice organization, and be ready for the service auditor to evaluate CC2.3, CC3.4, CC8.1, and CC9.2 against it.

### 3.2 Device Repair enterprise depot and claims service (`soc2-readiness-device-repair.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 15 | 16 | 2 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why 15 criteria are already Ready for a first-time report:** control environment, risk assessment, monitoring, user registration, physical access to depots, event evaluation, and recovery are met by group controls already evidenced in IT Support's SOC 2 report and the P07 common control assessment.
**Not ready:** CC2.3 (no system description or written service commitments) and CC6.8 (no allow-listing and no integrity checks on bench tool updates; P08 shows why this matters).
**Partially ready:** CC1.4, CC2.1, CC2.2, CC3.4, CC5.2, CC5.3, CC6.1, CC6.3, CC6.5, CC6.6, CC6.7, CC7.1, CC7.2, CC7.4, CC8.1, CC9.2, C1.1, and C1.2. Almost all are the division's own bench and depot gaps (P03 scenario gaps 1, 2, 4, 5, and 10).

**Availability** is out of scope for the first report because the TPA asked for Security and Confidentiality; it will be reconsidered for 2028.

## 4. Remediation plan and evidence calendar
| Quarter | Division | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | IT Support | CC6.1, CC6.3, CC8.1 | Local accounts removed; break-glass design; two-person approval records; phishing-resistant key issuance |
| 2026 Q4 | IT Support | CC2.3, CC3.4, CC9.2 | AI change gate; agent risk assessment; subcontractor agreement; draft description language |
| 2026 Q4 | IT Support | CC7.2, C1.1 | PSA logs in the SIEM; attachment purge report |
| 2026 Q4 | Device Repair | CC1.4, CC2.2, CC5.3, CC6.1, CC6.5, CC6.6, CC7.4 | Training completion; re-issued supplement; named bench accounts; SP 800-88 Rev. 2 standard and certificates; counter network retest; exercise report |
| 2027 Q1 | Device Repair | CC2.1, CC2.3, CC3.4, CC5.2, CC6.3, CC6.7, CC6.8, CC7.1, CC7.2, CC8.1, CC9.2, C1.1, C1.2 | System description and commitments; inventory; bench image redesign; vault rollout and purge; allow-listing; tool review gate; telemetry; retention reports. Type 1 as of 2027-03-31 |
| 2027 Q1 to Q2 | IT Support | A1.3, C1.2 | Quarterly restore samples; destruction certificates |
| 2027 Q2 to Q3 | Both | All in-scope criteria | Operating evidence for IT Support's 2027 period (ends 2027-06-30) and Device Repair's first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the IT Support president tells managed services customers about the AI agent pilot and the remediation before the 2027 report is issued. Device Repair sends the TPA and the top 100 business accounts a readiness letter with the 2027 timeline.
