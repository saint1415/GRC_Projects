# SOC 2 Readiness Self-Check: Cris Santos Company | Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm) |
| Tier / Vertical | Sole Proprietorship / Agriculture, Forestry, Fishing and Hunting |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs and short topic labels only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the FMIS vendor's SOC 2 Type 2 report, received at intake (EV-007; `vendor-soc2-review.csv`, an added file) |
| Prepared | 2026-07-15 (Part B) and 2026-07-17 (Part A) by the owner-operator with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person farm would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. The farm sells peanuts to a buying point and berries to the public; no customer relies on its systems, no buyer asks for a report, and the vertical profile lists no assurance alternative. A CPA examination would cost more than the farm's whole security budget for years.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board or staff, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the FMIS vendor's SOC 2 report.** SYS-01 runs the farm's records and its irrigation control (P02, P04). The owner uses the CC criteria as a checklist when reading the vendor's report every year (POL-01 6.4).

## 2. Scope
- **Services:** growing and selling peanuts, strawberries, watermelons, and sweet corn; no services to other businesses.
- **System:** the Farm Management and Irrigation Control Platform (P02).
- **People:** the owner-operator; the irrigation dealer and IT technician as contractors.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 15 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not N/A, unlike in an office business:** CC8.1 (change management). The farm writes no software, but irrigation schedules, setpoints, and fertigation rates are configuration changes to equipment that can damage a crop, and today nobody records them. It is Partially ready until the change log (POL-01 7.8) is in use.
**Not ready:** CC6.1 (no MFA on irrigation control; default passwords), CC6.6 (customer Wi-Fi reaches the pump controller), CC7.2 (no monitoring), CC7.5 (no farm-held backups; unwritten manual procedure), and CC9.2 (dealer and AI vendor terms). All five map to open POA&M items in P07.

## 4. FMIS vendor report (Part B)
- **Opinion:** Type 2, unmodified, Security and Availability, period ending 2026-03-31. One exception (late user-access removals at the vendor), remediated.
- **The carve-out that matters:** the cellular device connectivity service that carries commands to the pivot panel is a carved-out subservice organization. The report does not test the path that actually starts and stops the pivot. Follow-up: ask the vendor how it monitors that provider.
- **Availability:** RPO 1 hour meets the BIA. RTO 8 hours **does not meet** the 1-hour RTO for irrigation (P05 BP-01); manual operation at the pump house covers the gap.
- **Controls the farm must run (CUECs):** turn on MFA, manage users and roles, review activity reports, protect mobile devices, and secure field devices and networks. **Four of the five are open gaps at the farm**, so the vendor's controls protect the farm only once the owner closes POAM-001, POAM-003, and POAM-004 and starts the monthly review.
- **Follow-ups:** bridge letter by 2026-10-31; a stated incident notice time at renewal.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.1, CC6.2, CC6.3, CC6.7, CC2.3 | MFA and password manager screenshots; dealer role change; vendor list; printed contacts |
| By 2026-10-31 | CC2.1, CC7.2 | Monthly review log |
| By 2026-11-30 (before freeze season) | CC6.6, CC7.1, CC7.3, CC7.4, CC7.5, CC8.1, CC9.1, CC3.4, CC1.4 | Network test result; firmware record; walkthrough notes; change log; freeze alarm and procedure; course certificate |
| By 2026-12-31 | CC6.5, CC9.2 | Disposal record; dealer terms; AI vendor decision |
| By 2027-07-31 | CC4.1 | Second self-assessment (outside review in 2028) |

If a buyer or lender ever asks about security, the owner will answer with a one-page letter summarizing this check and the POA&M, updated each July.
