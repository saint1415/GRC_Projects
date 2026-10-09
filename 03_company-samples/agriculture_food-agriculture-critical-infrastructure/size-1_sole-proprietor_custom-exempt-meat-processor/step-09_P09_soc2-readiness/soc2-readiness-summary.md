# SOC 2 Readiness Self-Check: Cris Santos Company | Food and Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| Tier / Vertical | Sole Proprietorship / Food and Agriculture |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the cold-chain monitoring vendor's SOC 2 Type 2 report, received at intake (EV-005; `vendor-soc2-review.csv`, added file) |
| Prepared | 2026-07-30 (Part B) and 2026-07-31 (Part A) by the owner-operator with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A custom-exempt shop would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This shop processes meat for households; no customer relies on its computers, and none has asked about security. The cost of a CPA examination would be out of proportion to $180,000 in fees.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the cold-chain vendor's SOC 2 report.** The cold-chain service is the one vendor whose failure can spoil customers' meat. The owner uses the same CC criteria as a checklist when reading its report every year (POL-01 6.3).

## 2. Scope
- **Services:** custom processing of about 480 animals a year for their owners; no services to other businesses.
- **System:** the Shop Production and Cold-Chain Monitoring System (P02).
- **People:** the owner-operator; contractors on call.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 15 | 4 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; vendor change management is the vendors').
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.4 addresses with the IT technician's review at least every second year.
**Not ready:** CC6.1 (shared password and no MFA on the cold-chain account and booking admin), CC6.5 (no disposal rule), CC7.2 (no activity review; alerts fail silently), and CC7.5 (the shop's own data has no backup). Each maps to an open item in P07 or P01.

## 4. Cold-chain vendor report (Part B)
- **Opinion:** Type 2, unmodified, Security and Availability, period ending 2026-03-31. One access-removal exception, remediated.
- **What the report does not cover:** text-message delivery is a carved-out subservice organization, and the gateway **cannot alert while it is offline**. The vendor's platform can be fully reliable and the shop can still get no alert.
- **Controls the shop must run (CUECs):** enable MFA, maintain alert contacts and set points, keep gateways powered and connected, review activity reports, and report suspected compromise. Today the shop runs none of the first four fully (POAM-001, POAM-004, P01 R-003). **The vendor's controls protect the product only once the shop runs its side.**
- **Follow-ups:** bridge letter by 2026-10-15; ask how gateway firmware updates are signed; register a shop security contact for incident notices.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC5.2, CC6.3, CC6.7, CC2.3, CC7.3, CC7.4 | MFA and password manager screenshots; standard account; printed contacts; walkthrough notes |
| By 2026-10-15 | CC2.1, CC6.4, CC6.6, CC7.1, CC7.2, CC7.5, CC3.4 | Review log; locked box; network settings; firmware versions; offline notice and battery backup; first export and restore |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC9.2 | Course certificate; shredding log; vendor list with terms reviewed |
| By 2027-07-31 | CC4.1, CC9.1 (generator by 2027-05-31) | IT technician's evidence review; reciprocal agreement; storm procedure; transfer switch invoice |

**If a customer ever asks:** a one-page letter from the owner summarizing this check and the POA&M, updated each July, is the right size of answer.
