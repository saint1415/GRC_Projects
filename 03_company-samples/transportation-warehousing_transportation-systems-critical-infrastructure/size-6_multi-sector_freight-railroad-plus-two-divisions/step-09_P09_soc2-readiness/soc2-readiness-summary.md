# SOC 2 Readiness Summary: Cris Santos Company Holdings | Transportation Systems | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Freight Railroad division's contract dispatching and car management service (CDS) (`soc2-readiness.csv`). Transload and Wholesale terminal inventory services are routed to a SOC 1 evaluation. Real Estate is out of scope |
| Categories in scope (CDS) | Security, Availability, Confidentiality |
| Target report (CDS) | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Prepared | 2026-09-10 by the Group Chief Risk Officer's assurance team with the Director, Rail Technology Services and the division security and compliance leads |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division and service line is whether other organizations rely on its controls as part of their own.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Freight Railroad | Contract dispatching and car management service (CDS) for 11 unaffiliated short lines, on SYS-R1 and SYS-R4 | **Yes.** The customers rely on group dispatchers and systems for movement authority and car records on their own railroads | **In scope.** First readiness assessment; 2 customers asked for a Type 2 report by the end of 2027 | Security, Availability, Confidentiality | Type 1 as of 2027-03-31; Type 2 for 2027-04-01 to 2027-09-30 |
| Freight Railroad | Freight transportation for shippers | No. Shippers buy transportation; they do not build their controls on the railroads' systems | Out of scope | n/a | n/a |
| Transload and Wholesale | Terminal storage and inventory services for customer-owned product at 14 terminals | **Yes, but for financial reporting.** 3 large customers record the stored inventory in their financial statements from terminal inventory reports | **Out of SOC 2 scope; evaluate SOC 1 Type 2 for 2027.** The customers' need is assurance over inventory records that affect their financial reporting, which is what a SOC 1 report addresses | n/a for SOC 2 | SOC 1 decision by 2027-03-31 |
| Transload and Wholesale | Merchant wholesale sales | No. Customers buy products | Out of scope | n/a | n/a |
| Railside Industrial Real Estate | Leasing and property management | **No.** Tenants lease space; they do not rely on the division's systems as part of their control environment | **Out of scope** (reasons below) | n/a | n/a |

**Why Real Estate is out of scope:**
1. **No user entities.** Tenants rent buildings. Building access control and BAS serve the landlord's duties under the leases, not an outsourced service tenants build their controls on.
2. **Tenant questions are contractual.** Tenants that ask about building security receive the lease security exhibit and a summary of the group program.
3. **Revisit trigger:** if the division sells managed security or monitoring services to tenants, assess whether a SOC 2 report is needed.

**Why freight carriage is out of scope.** Shippers rely on the railroads to move cars, and their questions are answered in transportation contracts and by the TSA and FRA framework. Nothing in the vertical overlay names a standard assurance report for carriers, and no shipper has asked for one.

**Other assurance options considered.** The CDS customers are railroads subject to the same TSA and FRA rules. Two of them are Covered Railroads in their own right and must account for dispatching done for them in their own CIPs; a SOC 2 report gives them independent evidence for that. The group decided SOC 2 is the right report because the customers asked for it by name and because its Security, Availability, and Confidentiality categories match the CDS commitments.

## 2. System description (scope): CDS
- **Services:** dispatching (track warrants, track and time, CTC control for 2 customers with CTC) and car management (car orders, waybills, interchange reporting) for 11 short lines.
- **Infrastructure and software:** SYS-R1 CAD (DC-1, DC-2 standby, 6 CDS dispatch positions at the primary NOC), SYS-R4 TMS on cloud provider A, the industrial DMZ; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider A (TMS hosting); the CAD vendor (remote support only); the hosted telephony provider (dispatcher phone lines).
- **People:** the CDS dispatch desk, the Director, Rail Technology Services, and the group SOC, identity, and OT security teams.
- **Data:** customers' train sheets, authorities, track bulletins, car records, and waybills.
- **Complementary user entity controls:** customers request and remove their users, approve territory changes, keep their own manual dispatch procedures, and review the SOC 2 report.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 25 | 7 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** the control environment, risk, monitoring, identity, network, and recovery criteria are met by group common controls and the TSA-driven rail program already assessed in P07.
**Not ready:** CC2.3 (no system description and no written complementary user entity controls).
**Partially ready:** CC3.4, CC6.1, CC6.6, CC7.2, CC7.4, CC8.1, CC9.2, A1.3, C1.2. Most trace to group gaps that P01 and P07 already track: the SYS-G5 flow and change control (CC3.4, CC6.6, CC8.1; POAM-001), the directory trust (CC6.1; POAM-018), OT logging (CC7.2; POAM-003), and the untested notification steps (CC7.4; POAM-008).

**Processing Integrity** is out of scope today because the CDS makes no commitments about the completeness or accuracy of processing beyond the dispatch rules themselves. Revisit if customers ask for commitments on car record accuracy for billing.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC3.4, CC6.6, CC7.4 | CIP amendment request and DMZ rule change (POAM-001); tabletop report including CDS notices (POAM-008) |
| 2026 Q4 | CC6.1, CC7.2, CC8.1 | Trust review record (POAM-018); CTC log forwarding (POAM-003); change rule in the group change tool |
| 2027 Q1 | CC2.3, CC9.2, A1.3, C1.2 | System description and customer responsibilities guide; telephony review and second-provider test; TMS regional failover test; offboarding procedure. Type 1 as of 2027-03-31 |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the Director, Rail Technology Services sends the 11 CDS customers a readiness letter with the 2027 timeline and the customer responsibilities guide by 2027-01-31. The Transload and Wholesale division tells the 3 inventory customers that a SOC 1 decision will be made by 2027-03-31.
