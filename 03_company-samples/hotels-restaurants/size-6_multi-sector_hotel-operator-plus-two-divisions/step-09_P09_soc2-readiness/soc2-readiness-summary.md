# SOC 2 Readiness Summary: Cris Santos Company Holdings | Accommodation and Food Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Accommodation and Food Services (focus division: Hotels) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). Two readiness reports: Hotels service line SL-1 (`soc2-readiness.csv`) and Vacation Ownership service line SL-2 (`soc2-readiness-vacation-ownership.csv`). Attractions is out of scope |
| Categories in scope | SL-1: Security, Availability, Confidentiality. SL-2: Security, Availability, Confidentiality, Processing Integrity |
| Target reports | SL-1: Type 1 as of 2027-03-31, then Type 2 for 2027-04-01 to 2027-09-30. SL-2: Type 1 as of 2027-06-30, then Type 2 for 2027-07-01 to 2027-12-31 |
| Readiness review | 2026-08-17 to 2026-08-28; prepared 2026-09-10 by the Group Chief Risk Officer's assurance team with the Hotels and Vacation Ownership security and compliance leads |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. The question for each division is whether it provides a service to other organizations that rely on its controls. The vertical's usual assurance mechanism is PCI DSS validation for card payments; the group already has that for every division (P03). SOC 2 is needed only where an organization relies on the group for more than card data.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Hotels | **SL-1: hotel management technology services** to the owners of 58 managed hotels (41 ownership groups): PMS tenant administration, POS, payment integration, property networks, door lock and guest technology interfaces, owner reporting | **Yes.** Owners are separate companies that rely on the division's controls for their hotels' systems and guest data. Owners and their lenders have asked for an independent report beyond the PCI DSS service provider AOC, which covers card data only | **In scope.** First readiness assessment | Security, Availability, Confidentiality | Type 1 as of 2027-03-31; Type 2 for 2027-04-01 to 2027-09-30 |
| Hotels | Rooms, food and beverage, and loyalty for guests | No. Guests are consumers, not user entities | Out of scope | n/a | n/a |
| Vacation Ownership | **SL-2: owners' association management services** for 24 associations: maintenance-fee billing and collection, owner records, reserves accounting, and the reservation platform | **Yes.** Each association is a separate entity with its own board and auditor, and relies on the division's billing and records | **In scope.** First readiness assessment | Security, Availability, Confidentiality, **Processing Integrity** (billing accuracy is the associations' main concern) | Type 1 as of 2027-06-30; Type 2 for 2027-07-01 to 2027-12-31 |
| Vacation Ownership | Timeshare sales and consumer loans | No. Owners and borrowers are consumers; the Safeguards Rule, not SOC 2, sets the bar | Out of scope | n/a | n/a |
| Attractions | Park admission, passes, food, merchandise, park app, kids' club | **No.** It sells to consumers; no organization relies on its controls | **Out of scope** (reasons below) | n/a | n/a |

**Why Attractions is out of scope:**
1. **No user entities.** Visitors, passholders, and parents are consumers. No business builds its own control environment on the park systems.
2. **Assurance comes from elsewhere.** Card data is covered by the annual merchant ROC for Acquirer B (P03), the kids' club by the COPPA Rule program the division is now writing (16 CFR 312.8(b)), and ride safety by engineering programs outside this assessment.
3. **Group partners** (tour operators, travel agents selling park tickets) are answered with the group security program description and the AOC.
4. **Revisit trigger:** if Attractions starts selling its ticketing, gate, or app platform to third-party venues, assess SOC 2 for that service line.

**Why the timing differs.** SL-1 can move first because most of its controls are group common controls already tested by internal audit and the QSA. SL-2 waits until Vacation Ownership moves to SYS-G1 and the SIEM (2027-03-31), because a report issued earlier would describe a system about to change and would carry exceptions for MFA and encryption that are already being fixed.

**Other reports considered.** Owners also receive accounting from the division under the management agreements. Controls over that accounting are a financial reporting matter, so Group finance is evaluating a **SOC 1** report for owners separately; it is not part of this assessment. HITRUST and ISO/IEC 27001 certification were not requested by any user entity.

## 2. System descriptions (scope)
### 2.1 SL-1 Hotel management technology services
- **Services:** operation of the PMS tenant, POS, payment integration, property networks, and guest technology interfaces at 58 managed hotels; incident notice and responsibility matrices for owners.
- **Infrastructure and software:** the PMPS (P02): cloud PMS tenant (vendor SaaS), cloud POS and P2PE devices, legacy POS at the managed hotels that still have it, property payment segments, and interface services in Cloud provider A. Group identity (SYS-G1), SOC (SYS-G2), network (SYS-G3), and payment services (SYS-G4) are carved in as internal shared services.
- **Subservice organizations (carve-out):** Cloud provider A; the PMS vendor; the cloud POS vendor; the payment gateway. The legacy POS vendor is also a subservice organization until the legacy POS is retired (2027-06-30); its support service has no assurance report today (CC9.2).
- **People:** about 25,000 Hotels employees (including managed hotel staff), plus group SOC, identity, and network teams.
- **Data:** guest reservation and identity data, folios, and tokenized card data for the owners' hotels.
- **Complementary user entity controls (owners):** owners manage their own corporate networks and merchant accounts, approve owner-side connections, and notify the division of incidents on owner systems.

### 2.2 SL-2 Owners' association management services
- **Services:** maintenance-fee billing and collection (about $1.1 billion a year), owner records, reserves accounting, and the points and reservation platform for 24 associations.
- **Infrastructure and software:** SYS-V3 owner services (legacy data center until the 2027 migration to Cloud provider B); owner portal (Cloud provider A); group SOC and payment services carved in.
- **Subservice organizations (carve-out):** cloud providers; the ACH bank; lockbox, print and mail, and collections providers.
- **Data:** owner contact, ownership, and billing data; owners' bank data for autopay (tokenized in SYS-V3 after POAM-013).
- **Complementary user entity controls (associations):** boards approve budgets and assessments, review monthly financial reports, and approve write-offs.

## 3. Readiness results
### 3.1 SL-1 Hotels (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 24 | 8 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3. There is no system description for owners, 31 pre-2020 management agreements contain no security commitments, and the responsibility matrix has reached only 23 of 41 ownership groups (POAM-026).
**Partially ready:** CC6.2, CC6.3, CC6.6, CC6.8, CC7.1, CC7.2, CC7.4, CC9.2, A1.3, C1.1, and C1.2. Nearly all trace to the shared legacy POS and its vendor, the CRS integration credential, and owner notices, the same items as P07.

**Why so many criteria are Ready for a first report:** control environment, risk assessment, monitoring, identity, network, backup, and SOC criteria are met by group common controls already tested by internal audit (P07) and, for card data, by the QSA.

### 3.2 SL-2 Vacation Ownership (`soc2-readiness-vacation-ownership.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 20 | 10 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

**Not ready:** CC2.3 (no system description; association agreements lack security commitments), CC6.1 (no MFA for 340 users; unencrypted archive in the same data center), CC7.1 (legacy data center not scanned or tested), and A1.3 (no 2026 restore test).
**Partially ready:** CC3.4, CC4.1, CC5.3, CC6.2, CC6.3, CC6.7, CC7.2, CC7.4, CC7.5, CC9.2, A1.2, C1.1, C1.2, and PI1.3.

Billing processing is in good shape (4 of 5 Processing Integrity criteria Ready). The gaps are the same technical baseline gaps the Safeguards Rule analysis found (P03), so the Safeguards Rule remediation plan and SOC 2 readiness are one program.

## 4. Remediation plan and evidence calendar
| Quarter | Service line | Criteria | Evidence to collect |
|---|---|---|---|
| 2026 Q4 | SL-1 | CC6.3, CC6.6, CC7.1, CC7.2, CC7.4, CC9.2 | Scoped CRS credential; PAM vendor sessions; lock server retest; SIEM onboarding; tabletop report; amended vendor contract |
| 2026 Q4 | SL-2 | CC5.3, CC6.3, CC6.7, CC7.1, CC7.4, A1.3 | Re-issued supplement; bank data removed from the hub; penetration test of the legacy data center; updated IR plan; restore test |
| 2027 Q1 | SL-1 | CC2.3, CC6.2, A1.3, C1.1, C1.2 | System description and service commitments; side letters; legacy POS account certification; witnessed restore; purge reports. **Type 1 as of 2027-03-31** |
| 2027 Q1 | SL-2 | CC6.1, CC6.2, CC7.2, CC9.2, A1.2, PI1.3 | MFA and SYS-G1 migration; archive encryption; SIEM; provider assessments; backups in the immutable vault; independent reconciliation review |
| 2027 Q2 | SL-1 | CC6.8 | Legacy POS retired (P2PE replacement complete 2027-06-30) |
| 2027 Q2 | SL-2 | CC2.3, CC3.4, C1.1, C1.2 | System description; change assessment; purpose tags; retention schedule. **Type 1 as of 2027-06-30** |
| 2027 Q2 to Q4 | Both | All in-scope criteria | Operating evidence for the Type 2 periods |

**Communication:** the Hotels senior vice president of owner relations sends every owner a readiness letter with the 2027 timeline together with the 2026 service provider AOC. The Vacation Ownership vice president of association management briefs the 24 association boards at their 2026 Q4 meetings.
