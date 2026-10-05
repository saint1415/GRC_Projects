# SOC 2 Readiness Summary: Cris Santos Company Holdings | Water and Wastewater Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Environmental Services remote monitoring and compliance data service (`soc2-readiness.csv`). The Water Utility and Construction are out of scope, with reasons. Key vendors' SOC 2 reports reviewed in `vendor-soc2-review.csv` |
| Categories in scope | Security, Availability, Processing Integrity, Confidentiality |
| Target report | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Environmental Services security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build into their own controls.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Environmental Services | Remote monitoring and compliance data service (SYS-E1) for about 210 client treatment systems | **Yes, a true service organization.** Clients use its data in their own permit compliance reports and rely on its alarm forwarding | **In scope.** First readiness assessment | Security, Availability, Processing Integrity, Confidentiality | Type 1 as of 2027-06-30; Type 2 for 2027-07-01 to 2027-12-31 |
| Environmental Services | Remediation, waste transport, liquid waste treatment | No. Clients buy a physical service, not a system they rely on for their own control environment | Out of scope | n/a | n/a |
| Water Utility | Drinking water for about 3.37 million people | **No.** Customers buy water, not an outsourced system | **Out of scope** (reasons below) | n/a | n/a |
| Infrastructure Construction | Design, construction, and controls integration | **No.** Clients receive delivered facilities and systems; the division does not operate systems on their behalf after handover | **Out of scope** (reasons below) | n/a | n/a |

**Why the Water Utility is out of scope:**
1. **No user entities.** Its customers are households and businesses buying water. No one relies on Water Utility systems as part of their own internal control.
2. **Assurance comes from regulators instead.** Each covered system certifies its RRA and ERP to EPA (42 U.S.C. 300i-2), primacy agencies oversee drinking water compliance and public notification (40 CFR 141 Subpart Q), and state utility commissions regulate rates and service.
3. **Its own reliance on vendors** is managed by reviewing their SOC 2 reports (`vendor-soc2-review.csv`): the CIS vendor's 2026 Type 2 report had one access exception that is being followed up.
4. **Revisit trigger:** if the Water Utility starts operating billing or SCADA services for municipalities under contract, assess whether a SOC 1 or SOC 2 report is needed.

**Why Construction is out of scope:**
1. **Its assurance is regulatory.** DoD clients rely on the division's CMMC status (32 CFR Part 170) and DFARS 252.204-7012 compliance, not a SOC 2 report. Fixing the CMMC record before the 2026-12-12 affirmation is the division's assurance priority (P03).
2. **No hosted service.** After handover, client plants run on the client's systems. Commissioning access during projects is governed by contract and the client's own controls.
3. **Revisit trigger:** if the division sells remote operations or monitoring of client control systems after handover, scope it as a service line.

**Other assurance options considered.** No other standard assurance mechanism is named in the vertical overlay. ISO/IEC 27001 certification was considered for Environmental Services; clients asked specifically for SOC 2 (38 requests), so SOC 2 is the choice.

## 2. System description (scope) for the Environmental Services monitoring service
- **Services:** collection of readings (flow, pH, level, and other parameters) from client treatment systems; alarm forwarding to client operators; monthly compliance data reports that clients use in their own permit reports; a client portal. An AI-assisted anomaly alert feature (AI-007) is offered to clients (P10).
- **Infrastructure and software:** SYS-E1 on cloud provider A in the group landing zone (multi-tenant application, managed database with zone replicas, client portal), immutable backups in provider B, and about 210 cellular gateways at client sites on a private APN.
- **Subservice organizations (carve-out):** cloud providers A and B; the cellular carrier.
- **Group services carved in as internal shared services:** identity (SYS-G1), SOC (SYS-G2), cloud platform (SYS-G3), and OT remote access for technicians (SYS-G4).
- **People:** the 24x7 monitoring operations center, field technicians, and platform engineers in Environmental Services, plus group SOC and identity teams.
- **Data:** client process and compliance data; for 31 federal remediation sites, FCI under FAR 52.204-21.
- **Complementary user entity controls:** clients provision and remove their own portal users, review monthly reports before using them in permit reports, and keep physical security of gateway enclosures at their sites.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 23 | 9 | 1 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |

**Why so many Ready criteria for a first report:** governance, risk, identity, monitoring, and backup criteria are met by group common controls that were assessed once in P07 (for example CC5.2, CC6.2, CC6.3, CC7.2, A1.2).

**Not ready:**
- **CC2.3:** there is no system description and no written service, security, or notice commitments to clients. A SOC 2 report is an opinion on whether controls meet stated commitments, so nothing can be tested until they exist (POAM-023).
- **A1.3:** recovery has been tested only as a database restore; there is no failover runbook and the regional failover was never tested (P01 ES-003).

**Partially ready:** CC1.3 (no division supplement or named service roles), CC3.4 and CC8.1 (the AI-007 feature and gateway firmware pushes skipped security review), CC4.1 (inheritance of group controls not confirmed, POAM-015), CC5.3 (service procedures not written), CC6.6 and CC7.1 (23 gateways with default credentials and undetected baseline deviations, POAM-022), CC7.4 (no client notice register, POAM-023), CC9.2 (carrier and gateway vendor contracts lack notice terms), C1.2 (manual deletion at contract end), PI1.1 (no processing commitments), and PI1.3 (data corrections without reason codes, P01 ES-004).

**Processing Integrity is in scope on purpose.** Clients' main reliance is on the accuracy and completeness of the compliance data. Leaving PI out would produce a report that does not answer their question.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.6, CC7.1 | Gateway reset and hardening records; monthly compliance check output |
| 2026 Q4 | CC2.3, CC7.4, PI1.1 | System description; service and processing commitments; client notice register; client communication |
| 2026 Q4 | CC1.3, CC4.1, CC3.4, CC8.1 | Environmental Services supplement; inheritance matrix; change risk reviews; AI-007 review under the Group AI Standard |
| 2027 Q1 | CC5.3, A1.3, C1.2, PI1.3 | Written procedures; failover runbook and test report; automated deletion certificates; correction reason codes |
| 2027 Q2 | CC9.2; all in-scope criteria | Vendor contract amendments at renewal; readiness walkthrough with the service auditor; Type 1 as of 2027-06-30 |
| 2027 Q3 to Q4 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the Environmental Services president sends the 38 requesting clients a readiness letter with this timeline and the gateway hardening completion date (2026-11-30).
