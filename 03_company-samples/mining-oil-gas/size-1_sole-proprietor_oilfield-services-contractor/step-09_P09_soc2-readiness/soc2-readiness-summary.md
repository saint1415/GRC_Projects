# SOC 2 Readiness Self-Check: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor) |
| Tier / Vertical | Sole Proprietorship / Mining, Quarrying, and Oil and Gas Extraction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-22 (Part B) and 2026-07-24 (Part A) by the owner-operator with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person contractor would not obtain a SOC 2 report.** SOC 2 reports on a service organization's systems that its customers rely on. The producers rely on the owner's labor and skill, not on a system the owner hosts for them, and a CPA examination would cost more than a month of receipts. What customers do ask for is a **security questionnaire**: Customer A's annual one is organized by NIST CSF 2.0 and is due 2026-09-30. The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions that maps cleanly onto the questionnaire. Some criteria assume a board or staff, so they are marked N/A or are met through the owner's direct oversight, with the reason written down.
- **B. Reading the productivity suite provider's SOC 2 report.** That service holds the customer reports and program copies, so the owner reads its report each year and runs the customer-side controls it lists (POL-01 6.4).

## 2. Scope
- **Services:** contract pumping for 34 wells and automation service for about 60 field devices of 2 producers.
- **System:** the Field Service Business Systems (P02).
- **People:** the owner-operator; the IT technician on request.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 13 | 7 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Different from an office business: CC8.1 applies.** Change management is usually N/A for a small business that develops nothing. Here the owner changes customer control logic and setpoints as a paid service, so CC8.1 is in scope and **Not ready** (phone approvals, no change log; POAM-006).
**Not ready:** CC2.3 (customer incident notice), CC6.1 (MFA, administrator account, password spreadsheet), CC6.7 (USB drives and AI uploads), CC7.2 (no monitoring), CC7.5 (no offline program copies), CC8.1 (change control), and CC9.2 (provider and customer-path terms). All seven map to open POA&M items in P07.

## 4. Provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. One Availability exception (an unmonitored backup job), remediated.
- **Availability:** the provider's commitments **meet the BIA** for email and files (BP-03 RTO 8 h, RPO 24 h).
- **Controls the business must run (CUECs):** manage users and MFA, configure sharing and retention, review sign-in activity, and protect endpoints and credentials. **The password spreadsheet in the synced folder breaks the credential CUEC**, so the provider's controls do not protect those passwords until POAM-003 is closed.
- **Limit:** 30-day file versions are a convenience, not a backup for customer programs (POAM-005).

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC2.3, CC5.2, CC6.1, CC6.7, CC7.3, CC7.4, CC8.1 | MFA and account screenshots; password manager in use; printed contact sheet; first change log entries; walkthrough notes |
| By 2026-10-31 | CC2.1, CC3.4, CC6.2, CC6.3, CC7.2, CC7.5, CC9.2 | Monthly review log; Customer B decision; offline backup and restore test record; AI consent or tier change |
| By 2026-12-31 | CC1.4 (courses by 2026-11-30), CC6.5, CC6.6, CC7.1, CC9.1 | Course certificates; new router; disposal checklist; coverage agreement |
| By 2027-07-31 | CC4.1 | Outside review record |

**Answer to Customer A:** the questionnaire answers are drawn from P03 and this check, state each gap plainly, and attach the POA&M summary. They are updated each July.
