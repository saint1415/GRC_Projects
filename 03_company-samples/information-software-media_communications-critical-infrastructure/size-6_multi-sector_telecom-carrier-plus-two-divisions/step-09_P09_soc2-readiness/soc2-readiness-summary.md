# SOC 2 Readiness Summary: Cris Santos Company Holdings | Communications | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Communications |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs only, with short topic labels written for this repository |
| Scoping | Per division (section 1). One readiness report: Network Engineering Services' Managed Network Operations (MNO) service (`soc2-readiness.csv`). The Telecom Carrier and the Tower and Fiber Infrastructure division are out of scope, with reasons |
| Prepared | 2026-09-17 by the Group Chief Risk Officer's assurance team with the Engineering security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service as part of their own control environment. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Network Engineering Services | Managed Network Operations for 64 network operators (SYS-E1) | **Yes, a true service organization.** Customers outsource monitoring, ticketing, and remote remediation of their networks, and rely on Engineering's access controls and notices to meet their own security, 911, and NORS duties. 37 contracts require a SOC 2 Type 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31; Type 2 for 2027-04-01 to 2027-09-30; report issued by 2027-11-30 |
| Network Engineering Services | Design, construction, and federal engineering projects | No. Deliverables are designs and builds, not an ongoing service the customer's controls depend on | Out of scope | n/a | n/a |
| Telecom Carrier | Broadband, voice, enterprise transport | **No.** The Carrier provides transmission. Customers do not rely on Carrier systems as part of their own control environment | **Out of scope** (reasons below) | n/a | n/a |
| Tower and Fiber Infrastructure | Tower space, rooftop, and dark fiber leases | **No.** Tenants lease real property and fiber; they run their own equipment and controls | **Out of scope** (reasons below) | n/a | n/a |

**Why the Carrier is out of scope:**
1. **Transmission, not processing.** Enterprise and government customers send traffic over the Carrier's network, but their own data security controls do not depend on Carrier systems the way they would on an outsourced processor.
2. **Assurance comes from regulators and contracts instead.** CPNI rules with an annual officer certification, CALEA SSI filings, Part 4 outage reporting, and enterprise contracts with SLAs and CPNI terms (P03 regulation-by-division matrix).
3. **Customer questionnaires** are answered with the group security program description and results from P03 and P07.
4. **Revisit trigger:** if the Carrier launches managed security, managed SD-WAN with customer policy administration, or hosting services, assess a SOC 2 for that service line.

**Why the Tower division is out of scope:**
1. **No user entities in the SOC 2 sense.** Wireless carrier tenants operate their own radios and backhaul; the Tower division controls access to compounds and maintains lighting, which are lease and regulatory obligations, not controls over the tenants' information systems.
2. **Assurance for tenants** comes from lease terms (site access, access logs on request) and FCC antenna structure records.
3. **Revisit trigger:** if the division opens edge data centers at tower sites, assess a SOC 2 (and possibly SOC 1) for colocation.

The Carrier and the Tower division still benefit from this work: the group common controls that the MNO report carves in are the ones they inherit, and the service assurance platform remediation (tenant partitioning, failover test) closes their own P01 risks.

**Other assurance options considered.** Some carrier customers asked whether ISO/IEC 27001 certification would do. The group decided SOC 2 remains the primary report because 37 contracts name it. The vertical overlay names no other standard assurance mechanism for this sector.

## 2. System description (scope)
- **Services:** 24x7 monitoring, alarm correlation, ticketing, and remote remediation of about 210,000 network elements for 64 customers (31 rural carriers, 19 municipal broadband utilities, 14 electric cooperatives); 30-minute outage notices and 24- or 72-hour incident notices under contract.
- **Infrastructure and software:** the SYS-E1 aggregation tier and remote access gateways (provider B); collectors at customer sites; the **MNO tenant on the Carrier's service assurance platform** (SYS-C1, provider A), which is an internal shared service owned by another division.
- **Carved in (internal shared services):** group identity (SYS-G1), SOC (SYS-G2), cloud landing zones (SYS-G3), and the Carrier's service assurance platform. Carving in the platform means its controls (tenant partitioning, failover) are tested as part of the MNO system; the tenant agreement (POAM-026) must define responsibilities first.
- **Subservice organizations (carve-out):** cloud providers A and B; the gateway software vendor's support access.
- **People:** about 410 MNO operators and shift leads in a 24x7 center, plus group SOC and identity teams.
- **Data:** customer network configurations, alarms, and tickets, including subscriber names and addresses in some carrier customers' tickets.
- **Complementary user entity controls:** customers approve change windows, maintain their own on-call contacts and NORS and PSAP duties, review Engineering's access reports, and notify Engineering of staff changes in their approval chain.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first-time report:** control environment, risk assessment, monitoring, identity, endpoint, and SOC criteria are met by group common controls already assessed once in P07.

**Not ready:**
- **CC2.3:** no system description, and service commitments and complementary user entity controls are spread across 64 contracts.
- **CC6.6:** internet-facing gateways patched outside the 14-day target, and tunnels reach the Carrier management plane. This is the P08 entry path.
- **A1.3:** the service assurance platform has never been failed over with the MNO tenant.

**Partially ready:** CC1.4 (customer data and CPNI training for operators), CC5.3 (remote access standard conflicts with POL-02 4.9), CC6.1 (shared gateway accounts), CC6.3 (cross-tenant role), CC7.1 (gateways not in authenticated scanning), CC7.2 (gateway logs not in the SIEM), CC7.4 (no customer notice register), CC8.1 (change approval varies by customer), CC9.2 (no intercompany agreement for the platform), C1.1 (customer data in tickets not identified), and C1.2 (no deletion certificates for 2 departed customers).

**Processing Integrity** is out of scope because the MNO service makes no processing integrity commitments. It should be reconsidered if customers rely on the AI alarm triage model (P10 AI-006) to decide which outages are reportable.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.3, C1.1 | Legacy role removal record; per-customer role catalog |
| 2026 Q4 | CC1.4, CC5.3, CC7.1, CC7.2, CC7.4, CC9.2 | Training records; updated remote access standard; scan and SIEM coverage; notice register; tenant and interconnection agreement |
| 2027 Q1 | CC2.3, CC6.1, CC6.6, CC8.1, A1.3, C1.2 | System description; PAM session records; patch reports for gateways; brokered session logs; change procedure; three-tenant failover test report; offboarding certificates. **Type 1 as of 2027-03-31** |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the Type 2 period 2027-04-01 to 2027-09-30 |
| 2027 Q4 | n/a | Service auditor fieldwork; report issued by 2027-11-30 |

**Communication:** the Engineering MNO general manager sends the 37 customers that require a report a readiness letter with this timeline by 2026-10-31, and briefs all 64 customers on the remote access changes (brokered sessions) before they take effect.
