# SOC 2 Readiness Summary: Cris Santos Company Holdings | Chemical | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Distribution managed inventory service (`soc2-readiness.csv`). Specialty Chemicals and Hazmat Transport are out of scope |
| Prepared | 2026-08-31 to 2026-09-04 (self-assessment) by the Group Chief Risk Officer's assurance team with the Distribution managed inventory service director; approved 2026-09-17 |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service as part of their own control environment. The question for each division is whether it provides such a service.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Distribution | **Managed inventory service** (SYS-D3): tank telemetry, demand forecasting, and automatic replenishment for about 2,600 customer sites, including about 640 water and wastewater utilities, plus the customer portal | **Yes.** Customers outsource tank monitoring and reordering to it and rely on its controls to keep treatment chemicals in stock. The 12 largest customers asked for a SOC 2 Type 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Processing Integrity | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Distribution | Branch and terminal sales and storage | No. Customers buy products; they do not rely on Distribution systems as part of their controls | Out of scope | n/a | n/a |
| Specialty Chemicals | Manufacturing, toll blending, private-label packaging | **No.** Customers buy products made to specification. Toll customers rely on quality and confidentiality terms, certificates of analysis, and audits of the plant, not on a system service | **Out of scope** (reasons below) | n/a | n/a |
| Hazmat Transport | Contract hazmat trucking for about 1,400 shippers | **No.** Shippers buy transportation. Their assurance comes from DOT and FMCSA oversight, safety ratings, and contract terms | **Out of scope** (reasons below) | n/a | n/a |

**Why Specialty Chemicals is out of scope:**
1. **No user entities in the SOC 2 sense.** Toll and private-label customers depend on product quality and formula confidentiality, which they verify through quality audits, certificates of analysis, and contract terms.
2. **Other assurance fits better.** Process safety is overseen under EPA RMP and OSHA PSM, with compliance audits (P03). Customers' security questionnaires are answered with the group program description and the RBPS 8 benchmark results.
3. **Revisit trigger:** if Specialty Chemicals starts hosting formulation or batch data for customers (for example, a customer-facing recipe portal), assess whether a SOC 2 report is needed.

**Why Hazmat Transport is out of scope:**
1. Shippers buy a regulated transportation service. Their due diligence relies on the carrier's DOT registration, safety performance, hazmat security plan, and insurance.
2. **Revisit trigger:** if shippers come to rely on the TMS shipper portal for their own records (for example, as their system of record for shipments), assess a SOC 2 Security report for the portal.

**Other assurance options considered.** The vertical overlay names no chemical-sector assurance alternative to SOC 2, and the customers asked specifically for SOC 2 Type 2. Many utility customers also ask whether the service could affect their own water treatment operations; the Processing Integrity category answers that question directly.

## 2. System description (scope)
- **Services:** cellular tank telemetry from about 2,600 customer tanks; demand forecasting (AI-005, P10); automatic replenishment orders to ERP; the customer portal for orders, SDS, certificates of analysis, and inventory.
- **Infrastructure and software:** SYS-D3 on cloud provider A (containers, managed database, telemetry ingestion, warm standby region), the ERP order interface (SYS-G4), and group identity (SYS-G1) and SOC (SYS-G2) as internal shared services carved in.
- **Subservice organizations (carve-out):** cloud provider A; the cellular carrier; **the telemetry gateway vendor**, whose portal configures and updates every gateway.
- **People:** about 160 Distribution staff (platform, customer service, route planning) plus group SOC and identity teams.
- **Data:** tank readings, usage, orders, and customer business contacts.
- **Complementary user entity controls:** customers provision and remove their portal users, protect gateway enclosures at their sites, and tell Distribution when tanks are taken out of service.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 22 | 9 | 2 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 3 | 2 | 0 | 0 |
| Confidentiality (C1, 2) | | | | 2 |
| Privacy (P1-P8, 18) | | | | 18 |

**Why so many Ready criteria for a first report:** the control environment, risk, monitoring, identity, network, and SOC criteria are met by group common controls (P02 common control catalog) that group internal audit already tests (P07).

**Not ready:**
- **CC2.3:** no system description, no written security commitments, and no defined complementary user entity controls.
- **CC9.2:** the telemetry gateway vendor portal has no MFA and the vendor has not been reviewed since 2023 (P07 SA-9 and IA-2(1); scenario gap 6). A service auditor would treat this vendor as a key subservice organization.

**Partially ready:** CC2.1 (component inventory), CC3.4 and CC8.1 (gateway firmware changes outside change review), CC4.1 (no separate evaluation of the service), CC5.3 (service procedures), CC6.2 (vendor portal users outside identity governance), CC6.8 (firmware integrity), CC7.1 (gateway configuration drift), CC7.4 (customer notice path not exercised), A1.3 (manual fallback untested), PI1.2 (no reconciliation of utility readings), and PI1.4 (no order-to-release match).

**The common thread** is the gateway vendor. Five of the 14 gaps (CC3.4, CC6.2, CC6.8, CC8.1, CC9.2) trace to the vendor portal and its firmware pushes. Fixing POAM-019 closes most of them.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC9.2, CC6.2, CC3.4, CC8.1, CC6.8 | Portal MFA or federation; security addendum; two-approver firmware process with hash checks (POAM-019) |
| 2026 Q4 | CC7.4 | Customer notice path tested in the 2026-12-08 tabletop (POAM-009) |
| 2027 Q1 | CC2.1, CC2.3, CC5.3, CC7.1, CC4.1, A1.3, PI1.2, PI1.4 | Component inventory; system description and commitments; procedures; drift report; internal audit plan; manual fallback test; reconciliation and order-match reports |
| 2027 Q2 | All in-scope criteria | Readiness re-check; Type 1 as of 2027-06-30 |
| 2027 Q3 to Q4 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-07-01 to 2027-12-31); report to the 12 largest customers in early 2028 |

**Timing note.** The customers asked for a Type 2 report by the end of 2027. A Type 2 period ending 2027-12-31 produces a report in early 2028. The service director will offer the Type 1 report (2027 Q3) and a bridge letter, and has asked the 12 customers to accept that timing (P01 DS-014).

**Communication:** the Distribution managed inventory service director sends the 12 largest customers a readiness letter with this timeline by 2026-10-31.
