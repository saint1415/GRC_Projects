# SOC 2 Readiness Summary: Cris Santos Company Holdings | Arts, Entertainment, and Recreation | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the ticketing platform service line of Ticketing and Streaming (`soc2-readiness.csv`). Live Venues, Hotels and Restaurants, and the streaming service are out of scope, with reasons |
| Categories in scope | Security, Availability, Confidentiality |
| Report | Existing annual Type 2. Last report: 12 months ending 2026-06-30, issued 2026-08-21, unqualified with no exceptions. Next period: 2026-07-01 to 2027-06-30 |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Ticketing and Streaming security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service that other organizations build their own controls on.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Ticketing and Streaming | Ticketing platform (TVOP) for about 1,150 client venues | **Yes, a true service organization.** Clients sell their tickets, take payments, and admit patrons on it, and rely on its controls for their own PCI DSS and privacy duties | **In scope (full)**; existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending June 30 |
| Ticketing and Streaming | Streaming service for about 3.1 million subscribers | No. Subscribers are consumers, not user entities | Out of scope | n/a | n/a |
| Live Venues | Live events at 38 venues | **No.** It sells tickets and services to patrons. It is a merchant whose assurance is its PCI DSS ROC | Out of scope (reasons below) | n/a | n/a |
| Hotels and Restaurants | Hotels, restaurants, and management of 6 hotels for third-party owners | **No for SOC 2.** Guests are consumers; the 6 owners rely on the division's financial reporting, which is a SOC 1 question | Out of scope (reasons below) | n/a | n/a |

**Why Live Venues is out of scope:**
1. **No user entities.** Patrons buy tickets; artists and promoters receive settlements under contract, not by relying on Live Venues' control environment.
2. **Assurance comes from PCI DSS instead.** Live Venues is a Visa Level 1 merchant validated by a QSA ROC (P03). That is the assurance its acquirers require, and the vertical overlay names PCI DSS validation as the alternative assurance mechanism for card payments.
3. **Revisit trigger:** 7 of the 38 venues are operated for public owners under management agreements. If an owner asks for assurance over ticket revenue reporting, assess a SOC 1 report for that service.

**Why Hotels and Restaurants is out of scope:**
1. **Guests are not user entities.** The division's assurance to its acquirer is its SAQ D (P03).
2. **The 6 managed hotels' owners** rely on monthly financial reports and the management company's accounting. If an owner requests assurance, a **SOC 1** report (controls relevant to the owners' financial reporting) is the right instrument, not SOC 2. No owner has asked; revisit at each management agreement renewal.

**The group's divisions as user entities.** Live Venues and Hotels and Restaurants are themselves users of the TVOP. They rely on its SOC 2 report and its PCI DSS AOC under Requirement 12.8, exactly as an outside client does. Their complementary user entity controls (below) are part of their own P07 evidence.

**Other assurance options considered.** ISO/IEC 27001 certification (named for the Information sector) was considered for the ticketing platform. The group keeps SOC 2 as the primary report because the 2024 client agreement requires it, and pairs it with the PCI DSS service provider AOC, which clients' acquirers ask for.

## 2. System description (scope)
- **Services:** event setup, seat maps, on-sales with virtual queue and bot detection, hosted checkout and payment orchestration, card-on-file tokens, mobile tickets, access control, box office app, reporting and client APIs; the optional dynamic pricing module for 310 opt-in clients.
- **Infrastructure and software:** the TVOP in provider A (two regions) with disaster recovery in provider B; the CDE account with HSMs; group identity (SYS-G1), SOC (SYS-G2), and landing zones (SYS-G3) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud providers A and B; the customer identity service vendor; the CDN; acquirers and gateways for authorization. **The tag management vendor and other script vendors whose code runs on client pages are not described today** (gap; see CC2.3 and CC9.2).
- **People:** about 4,500 division employees plus group SOC, identity, and cloud teams.
- **Data:** about 68 million patron accounts, card data in the CDE, order and attendance data for each client.
- **Complementary user entity controls:** clients manage their own tenant users and require MFA for their administrators, approve any tags they add (until tags are removed from checkout), review the tenant audit log, and report suspected incidents to client support.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 21 | 11 | 1 | 0 |
| Availability (A1, 3) | 3 | 0 | 0 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC6.8. Tenant and vendor scripts run on payment pages without authorization, and the P07 test tag was not detected. This is the control path of the P08 scenario.
**Partially ready:** CC2.3, CC3.4, CC6.1, CC6.2, CC6.3, CC6.7, CC7.1, CC7.2, CC7.4, CC8.1, CC9.2, and C1.1. Most trace to two themes: **tenant content on payment pages** (CC2.3, CC3.4, CC7.1, CC7.2, CC8.1, CC9.2) and **client data and client access** (CC6.1, CC6.3, CC6.7, C1.1).

**Why the last report had no exceptions.** The 2026 report's description treated tenant tags as a client responsibility, so the service auditor did not test them. P03 found that position hard to defend under PCI DSS (the platform serves the page and its policy allows the tags), and the QSA has questioned it. **Management should not repeat it in the next description.** The honest description for the period starting 2026-07-01 includes tags, which means the service auditor will likely find exceptions in CC6.8 and CC8.1 for the months before POAM-006 to POAM-008 close. Closing them by 2026-11-30 limits the exception period to about 5 months of 12.

**Processing Integrity** is out of scope because the platform makes no processing integrity commitments today. It is under review for 2027, because opt-in pricing clients now ask whether price changes stay inside their floors, ceilings, and accessible seating rules (P10).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC6.8, CC7.1, CC7.2, CC8.1 | Content security policy without tags in checkout; script inventory; tamper detection with SOC alerts; tag approval workflow records |
| 2026 Q4 | CC9.2, CC2.3 | Script vendor assessments and contracts; revised system description and responsibility matrix; client acknowledgment letters |
| 2026 Q4 | CC6.2, CC7.4 | Seasonal account expiry; client notice register; tabletop report (2026-12-15) |
| 2027 Q1 | CC6.1, CC6.3, CC3.4 | Client administrator MFA enforcement (2027-01-31); just-in-time support access; change gate records for pricing and payment page features |
| 2027 Q1 | CC6.7, C1.1 | Filtered training feed; deletion of non-permitted client data; purpose tags |
| 2027 Q2 | All in-scope criteria | Operating evidence for the period ending 2027-06-30 |

**Communication:** the General Manager Ticketing sends all clients a notice about the checkout tag change and the MFA requirement by 2026-11-30, and briefs the top 100 clients on the remediation before the next report is issued.
