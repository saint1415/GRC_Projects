# SOC 2 Readiness Summary: Cris Santos Company Holdings | Energy | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Energy |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; criteria text is not reproduced |
| Scoping | Per division (section 1). One readiness report: the Integrity Services **Integrity Data Platform** (`soc2-readiness.csv`). Gas Transmission and Gathering and Production are out of scope |
| Prepared | Self-assessment 2026-08-31 to 2026-09-04 by the Group Chief Risk Officer's assurance team with the Integrity Services Client Security Officer and Chief Technology Officer; reviewed 2026-09-22 |

## 1. Scoping decisions per division
A SOC 2 report describes controls at a **service organization** for the **user entities** that rely on its service as part of their own control environment. The question for each division is whether other organizations rely on its systems that way.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Integrity Services | Integrity Data Platform (SYS-E1): a multi-tenant service that about 160 pipeline operators use as their integrity management records system | **Yes.** Clients keep integrity records required for their own regulatory programs on it and rely on its controls | **In scope.** Type 1 report as of 2025-12-31 issued; first Type 2 period 2026-01-01 to 2026-12-31 under way | Security, Availability, Confidentiality | Type 2, calendar year; 28 clients require it by 2027-03-31 |
| Integrity Services | ILI analysis, integrity engineering, and the OT Assessment Practice | No. These are professional services delivered as reports; clients rely on the work product, not on a system | **Out of scope.** Client assurance comes from engagement terms, the SSI program (P06), and the authorized representative addendum (POAM-024) | n/a | n/a |
| Gas Transmission | Interstate transportation; nominations platform (SYS-T5) for about 340 shippers | **No, for SOC 2.** Shippers use the platform to nominate, but the service is FERC-regulated transportation under a tariff, not an outsourced system shippers build their controls on | **Out of scope** (reasons below) | n/a | n/a |
| Gathering and Production | Production, gathering, and royalty payments | **No.** Purchasers buy gas and royalty owners are paid; neither relies on division systems as part of their own control environment | **Out of scope** | n/a | n/a |

**Why Gas Transmission is out of scope:**
1. **Assurance comes from regulators.** TSA inspects against the approved implementation plan and receives the annual assessment report (SD 02G III.G); PHMSA inspects control room management; FERC sets the tariff and the NAESB WGQ standards for electronic communications (18 CFR 284.12), including the WGQ Cybersecurity Related Standards.
2. **Shippers are not user entities in the SOC 2 sense.** They depend on deliveries and on accurate measurement and invoices under the tariff, not on platform controls inside their own control environment.
3. **Revisit trigger:** if large shippers ask for assurance over measurement and imbalance settlement for their financial reporting, the right report would be a SOC 1 on SYS-T4 and SYS-T5, not SOC 2.

**Why Gathering and Production is out of scope:** it is the user entity, not the service organization. It relies on the hydrocarbon accounting SaaS (SYS-P3) and reviews that vendor's SOC reports under POL-01 4.10. Royalty owners and purchasers are protected through state law and contracts.

**Other assurance options considered.** The vertical overlay names no other standard assurance mechanism for pipeline integrity services. Clients that ask about OT assessment work receive the methodology, the SSI program description once live, and the authorized representative addendum.

## 2. System description (scope)
- **Services:** integrity records for about 96,000 miles of client pipelines plus the Gas Transmission system (intercompany): ILI results, alignment sheets and GIS, risk models, MAOP and material records, dig and repair records. About 3,900 client users.
- **Infrastructure and software:** SYS-E1 on cloud provider A (containers, managed databases, object storage) with a warm standby in provider B; group identity (SYS-G1), SOC (SYS-G2), and cloud platform (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the identity SaaS vendor; the ticketing SaaS vendor.
- **People:** about 300 IDP platform staff in Integrity Services, plus group SOC, identity, and cloud teams.
- **Data:** client integrity data (Confidential), including some SSI and CEII that clients upload with their records (gap 2).
- **Complementary user entity controls:** clients provision and remove their users, enable MFA for their users until it becomes mandatory, classify what they upload, and review the platform's reports.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 6 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many criteria are Ready:** the control environment, risk, monitoring, change management, identity, network, and SOC criteria are met by group common controls that P07 found strong, and the Type 1 report already tested their design.

**Not ready:** C1.1. SSI and CEII inside client tenants are not identified, marked, or handled as Restricted, and there is no SSI register (POAM-019).
**Partially ready:**
- CC2.3: no register of negotiated client notice terms, and marketing claims Part 1520 handling that does not yet exist;
- CC6.1 and CC6.3: SSI datasets are not separated or limited to need-to-know groups within tenants;
- CC6.6: MFA optional for most client users;
- CC7.4: client notice register and SSI disclosure step missing;
- CC9.2: subservice providers reviewed only once a year (POAM-022);
- A1.3: the 2026-02 failover took 5.5 hours against a 4-hour objective.

**The immediate issue is the 2026 Type 2 period, which ends 2026-12-31.** Fixes made in Q4 will not cover the whole period. Management should expect the service auditor to report deviations for C1.1, CC6.1, and CC6.3 for most of the year, and should describe the SSI program and its start date in the system description. The SSI marketing claim must be corrected by 2026-10-15 (POAM-023 milestone) so the description and client communications match what was in place (CC2.3).

**Processing Integrity** is out of scope because the platform makes no processing accuracy commitment. Clients increasingly ask about the ILI anomaly classification model; any commitment about analysis accuracy belongs in engagement terms and the P10 conditions, not in a platform report, until the model is validated.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC2.3, CC7.4 | Corrected marketing material; client notice register; updated reporting procedure (POAM-005) |
| 2026 Q4 | C1.1, CC6.1, CC6.3 | SSI register; dataset labels; need-to-know group membership and access tests (POAM-019) |
| 2027 Q1 | CC9.2 | Continuous monitoring reports; first quarterly complementary control review (POAM-022) |
| 2027 Q1 | CC6.6, A1.3 | MFA enforcement report for all client users; second failover test within the 4-hour objective |
| 2027 Q1 | All in-scope criteria | 2026 Type 2 report issued by 2027-03-31, as 28 clients require |
| 2027 Q2 to Q4 | All in-scope criteria | Operating evidence for the 2027 period with the SSI program in place for the full year |

**Communication:** the Integrity Services Client Security Officer briefs the 28 clients that require the report on the expected deviations and the remediation before the report is issued, and sends the 9 TSA-designated clients the SSI program description and the authorized representative addendum.
