# SOC 2 Readiness Summary: Cris Santos Company Holdings | Commercial Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: Commercial Property's third-party property management and remote building operations service line (`soc2-readiness.csv`). Construction and Hotels are out of scope, with reasons. A review of subservice organizations' reports is in `vendor-soc2-review.csv` |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Commercial Property security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations rely on as part of their own control environment.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Commercial Property | Third-party property management and remote building operations for 34 buildings owned by 9 institutional investors | **Yes.** The owners rely on the group's systems (BAACS, SYS-D1) and people to run their buildings, protect their tenants' data, and report to them. Several owners asked for a SOC 2 report by the end of 2027 | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Commercial Property | Leasing owned space to tenants | No. Tenants lease space; they do not outsource a function to the landlord's systems. Tenant questions are answered with the security program description and lease commitments | Out of scope | n/a | n/a |
| Construction | Construction services; BTI installation and warranty work for clients | **No.** Clients buy construction and installation, not an ongoing outsourced service. BTI's ongoing remote service is provided only to the group's own buildings. Federal clients rely on **CMMC** (32 CFR Part 170), the assurance mechanism their contracts require | **Out of scope.** Revisit if BTI sells an ongoing remote monitoring service to external clients | n/a | n/a |
| Hotels | Lodging and food service to guests | **No.** Guests and corporate accounts buy stays, not a service built into their control environments. Card security assurance comes from the annual **PCI DSS Report on Compliance** the acquirer requires | **Out of scope.** Revisit if the group starts managing hotels owned by others | n/a | n/a |

**Why SOC 2 for third-party management, and why not SOC 1 instead.** The owners rely on two different things. For **financial reporting** (rent collection, operating statements, owner distributions) the right report is a **SOC 1**, and the property management platform vendor already provides one for its part (`vendor-soc2-review.csv`). For **security and availability of building operations and confidentiality of owner and tenant data**, the right report is SOC 2. The owners asked for both; this readiness work covers SOC 2. A SOC 1 readiness review is planned separately by the Commercial Property controller.

**Other assurance options considered.** The vertical overlay names no standard assurance alternative for commercial facilities. Owners could accept the group's P07 results under an audit-rights clause, but 9 owners auditing separately would cost more than one report.

## 2. System description (scope)
- **Services:** building operations (HVAC, lighting, access control, video) for 34 managed buildings from the RBOC and site engineering teams; lease administration, tenant billing, and owner reporting through SYS-D1.
- **Infrastructure and software:** the BAACS (P02) and SYS-D1; group common controls (SYS-G1 identity, SYS-G2 SOC, SYS-G3 cloud and WAN) carved in as internal shared services.
- **Subservice organizations (carve-out):** the access control and video platform vendor, the property management platform vendor, the identity platform vendor, and cloud providers A and B. The BAS optimization service, which writes setpoints at 4 managed buildings, has no assurance report (section 3).
- **People:** the third-party management team, RBOC operators, engineers at managed buildings, security operations, and the BTI unit (an internal supplier, described in the system description).
- **Data:** owners' financial and lease data; tenant contacts; badge holder records and video for the managed buildings; building drawings and controller programs.
- **Complementary user entity controls:** owners approve capital and access changes for their buildings, review monthly reports, and tell the group about tenant changes that affect access.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 17 | 14 | 2 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

Of the 38 in-scope criteria, 19 are Ready, 16 Partially ready, and 3 Not ready.

**Why so many Ready criteria for a first-time report:** control environment, risk assessment, monitoring, change management, physical access, and SOC criteria are met by group common controls already assessed in P07.

**Not ready (3):**
- **CC2.3** (communication with external parties): there is no system description, and security commitments are scattered across 9 agreements with different terms.
- **CC9.2** (vendor and business partner risk): the BTI unit is not managed as a supplier, the BAS optimization service has never been reviewed, and the guard contractor uses a shared login.
- **A1.3** (recovery plan testing): no multi-site restore test, and none at a managed building.

**Partially ready (16):** CC1.4, CC2.1, CC3.4, CC4.1, CC6.1, CC6.2, CC6.3, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC9.1, A1.2, and C1.2. Most are the same OT gaps found in P03 and P07 (legacy remote tools, segmentation, site logging, site program backups), seen through the owners' eyes. Segmentation is the hardest: only 9 of the 34 managed buildings are segmented, because each owner decides whether to fund it.

**What a service auditor would see today.** The common controls would test well. The service-line controls would produce exceptions in remote access, recovery, and vendor management, the same areas the board already funded through the P01 group programs. The Type 1 date of 2027-06-30 is set so that POAM-006, POAM-009, POAM-018, and POAM-023 close first.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC3.4, CC6.1, CC6.2, CC6.3, CC9.2 | Feature change gate records; legacy tool removal at the 5 managed buildings; BTI end dates; administrator reduction; intercompany agreement; vendor reviews; guard named accounts |
| 2027 Q1 | CC1.4, CC2.1, CC2.3, CC7.1, CC7.5, CC9.1, A1.2, A1.3, C1.2 | Training records; inventory for managed buildings; system description and standard security exhibit; OT vulnerability standard; site program backups; manual procedures; regional restore test including a managed building; offboarding procedure |
| 2027 Q2 | CC4.1, CC6.6, CC6.8, CC7.2, CC7.4 | Internal audit sample of 2 managed buildings; owner-funded segmentation plans; allow-listing; site log forwarding; tabletop record with an owner notice. **Type 1 as of 2027-06-30** |
| 2027 Q3 to Q4 | All in-scope criteria | Operating evidence for the first Type 2 period (2027-07-01 to 2027-12-31) |

**Communication:** the Commercial Property vice president of third-party management sends the 9 owners a readiness letter with this timeline and a standard security exhibit to replace the differing clauses at the next renewal.
