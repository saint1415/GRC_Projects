# SOC 2 Readiness Summary: Cris Santos Company Holdings | Transportation and Warehousing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs with short topic labels in our own words; the criteria text is not reproduced |
| Scoping | Per division (section 1). One readiness report: Marine Terminals' terminal customer data services (`soc2-readiness.csv`). Freight Trading and Port Real Estate are out of scope |
| Prepared | 2026-08-31 to 2026-09-04 by the Group Chief Risk Officer's assurance team with the Marine Terminals director of customer services and the director of terminal systems; approved 2026-09-15 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build into their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Marine Terminals | **Terminal customer data services:** the customer portal and truck appointment system (SYS-T6) and partner EDI for terminal customers through the integration hub (SYS-G4) | **Yes, for this service line.** Carriers and large cargo owners rely on the terminals' container status, release and appointment data in their own operations, and their security questionnaires ask about these controls (about 140 questionnaires in 2025) | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30 |
| Marine Terminals | Physical cargo handling (stevedoring, vessel and yard operations) | No. Carriers buy a physical service; its assurance comes from the Coast Guard (Subpart F and the FSPs), CTPAT and terminal services agreements | Out of scope | n/a | n/a |
| Freight Trading | Merchant trading of steel, lumber and construction commodities | **No.** It buys and sells goods; customers do not rely on its systems as part of their controls | **Out of scope** (reasons below) | n/a | n/a |
| Port Real Estate | Warehouse and yard leasing | **No.** Tenants rent space; building access control is a lease service, not an outsourced information system | **Out of scope** (reasons below) | n/a | n/a |

**Why Freight Trading is out of scope:**
1. **No user entities.** Customers buy commodities. Suppliers and customers exchange EDI with it as trading partners, not as users of an outsourced service.
2. **Assurance comes from contract clauses instead.** DoD customers rely on FAR 52.204-21, the CMMC Level 1 self-assessment and affirmation in SPRS (32 CFR 170.15, 170.22), and DFARS 252.204-7012 when covered defense information is involved (P03). A SOC 2 report would not satisfy any of them.
3. **Revisit trigger:** if Freight Trading starts offering logistics or inventory management services to customers (for example vendor-managed inventory on its systems), assess whether a SOC 1 or SOC 2 report is needed.

**Why Port Real Estate is out of scope:**
1. **No user entities.** About 180 tenants lease space. A few large tenants ask about building access control and CCTV in lease negotiations; they are answered with the building security description in the lease and, after POAM-018 closes, a summary of the integrator access controls.
2. **Revisit trigger:** if the division sells managed security or monitoring services to tenants, or runs a shared tenant network, reassess.

Both divisions still benefit: the group common controls carved into this report are the same ones they inherit, and their vendors' SOC reports are reviewed under POL-01 4.9.

**Other assurance options considered.** Carriers also accept CTPAT partner status and, for some, ISO/IEC 27001 certification. The group chose SOC 2 because the largest carriers' questionnaires ask for it by name and because the controls are already documented to SP 800-53 (P02). The vertical overlay names no sector-specific assurance mechanism.

## 2. System description (scope)
- **Services:** container availability, holds and release status, truck appointments, vessel schedules and billing views for carriers, cargo owners and about 4,200 trucking companies (SYS-T6); EDI with carriers (bay plans, load lists, container status) and the customs status feed through SYS-G4, for all 9 terminals.
- **Infrastructure and software:** SYS-T6 on cloud provider A; the SYS-G4 integration hub; the TOS (SYS-T1) as the source of data. Group identity (SYS-G1) and SOC (SYS-G2) are carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the customer identity service; the managed file transfer software vendor (support only).
- **People:** customer services, terminal systems and integration teams, plus the group SOC and identity teams.
- **Data:** customers' cargo, booking and appointment data (Restricted: commercial, POL-04); driver identifiers used for appointments.
- **Complementary user entity controls:** customer administrators provision and remove their own portal users, protect their EDI certificates, and verify release instructions they send.
- **Boundary note:** the Gulf terminals' data reaches customers through the same hub today. Their move to SYS-T1 in 2027 is a significant change to assess before the Type 1 date (CC3.4).

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 7 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **26** | **9** | **3** | **23** |

**Why so many Ready criteria for a first-time report:** the control environment, risk assessment, monitoring, change management, identity, SOC and backup criteria are met by group common controls that group internal audit has already tested (P07: 121 of 138 common statements satisfied).

**Not ready (3):**
- **CC6.1 and C1.1:** the group logistics role gives 212 Freight Trading users every customer's cargo, vessel and appointment data. A service auditor would find that confidential customer information is not restricted to authorized users, which goes to the heart of the Confidentiality commitment (P07 AC-3; scenario gap 1). It must be fixed and the fix must operate before the Type 1 date (POAM-008).
- **CC2.3:** no system description and no written security, availability and confidentiality commitments to customers.

**Partially ready (9):** CC3.4 (Gulf migration not assessed against the description), CC6.2 and CC6.3 (cross-division roles approved and certified by the requester's own manager), CC6.6 (MFA optional for trucker users), CC6.7 (2 carriers on FTP; hub routes shared across divisions), CC7.4 (no customer incident notice commitment; matrix not exercised), CC9.2 (two vendors without a current SOC report on file), A1.3 (hub rebuild and portal failover never tested) and C1.2 (no retention rule for hub message stores).

**Processing Integrity** is out of scope for the first report because the division makes no processing integrity commitments. It is under evaluation for 2027, because carriers increasingly ask whether container status and release data are complete and accurate.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.1, C1.1, CC6.2, CC6.3 | Role removal record; cargo-owner view for Freight Trading; data-owner certification campaign; access log review results |
| 2026 Q4 | CC6.7, CC7.4 | FTP retirement; hub route separation; customer notice commitment; tabletop report |
| 2027 Q1 | CC2.3, CC3.4, CC6.6, CC9.2, A1.3, C1.2 | System description and commitments; Gulf migration assessment; portal MFA settings; vendor SOC report reviews; hub rebuild and portal failover tests; retention rule. **Type 1 as of 2027-03-31** |
| 2027 Q2 to Q3 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-04-01 to 2027-09-30) |

**Communication:** the director of customer services sends the top 40 carrier and cargo owner customers a readiness letter with this timeline by 2026-11-30, and tells them that the affiliate access issue has been found and is being removed. The Group General Counsel approves the wording, because the same facts are under Shipping Act review (P03 G-070).
