# SOC 2 Readiness Self-Check: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent event promoter with one leased room) |
| Tier / Vertical | Sole Proprietorship / Arts, Entertainment, and Recreation |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the ticketing vendor's SOC 2 Type 2 report, with its PCI DSS AOC as a companion check (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-11 (Part B) and 2026-08-12 (Part A) by the owner with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A sole proprietor promoter would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. This business sells tickets to the public, has no business customers relying on its systems, and could not justify the cost of a CPA examination. The assurance that matters here is **PCI DSS validation through SAQ A**, which the processor asks for (P03). Artists, agents, and the landlord do not ask for SOC 2.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Many criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the ticketing vendor's SOC 2 report.** The ticketing vendor runs the checkout, the scanner app, payouts, and the backups behind the BIA's RPO of 0 (P02, P04, P05). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.1).

## 2. Scope
- **Services:** ticket sales and show operations for about 60 public shows a year; no services to other businesses.
- **System:** the Ticketing and Venue Operations Platform (P02).
- **People:** the owner; contractors under written terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 4 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendors' change management is inherited, and the owner's own setting and script changes go in the change log).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (no MFA and a shared password on the ticketing and website accounts), CC6.2 (contractors use the owner's login), CC6.7 (card data by email and text; public share links for exports), and CC7.2 (no activity review). All four map to open POA&M items in P07.

## 4. Ticketing vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One access-removal timing exception, remediated. The payment processor and hosting provider are carved out; the processor's own PCI DSS AOC (2026-01-30) covers the payment fields.
- **Availability:** the vendor's stated RTO of 4 hours and near-zero RPO **meet the BIA** (BP-02 RTO 4 h, RPO 0), and the scanner app's offline mode covers BP-01's 1-hour RTO on show nights.
- **Controls the owner must run (CUECs):** enable MFA, assign roles and remove users promptly, protect credentials, review account activity, control content and scripts added to the owner's own pages, and report suspected compromise. Four of these are open gaps (POAM-001, POAM-002, POAM-005, POAM-008), so **the vendor's controls protect the owner only once the owner runs these.** The vendor offers MFA but does not force it.
- **Follow-ups:** bridge letter by 2026-10-31; ask the vendor for a customer incident notice time in writing; download the AOC again each July.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.2, CC6.3, CC6.7, CC6.8, CC2.3, CC3.3, CC3.4, CC5.2, CC7.1, CC7.3, CC7.4 | MFA screenshots; user lists with roles; payment-link use; approved script list and first page check; printed contacts; walkthrough notes |
| By 2026-10-31 | CC2.1, CC7.2, CC9.2, CC6.6 | Monthly review log; provider list; contractor terms; guest network |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC9.1 | Course certificate; disposal record; show-night card and backup promoter arrangement |
| By 2027-07-31 | CC4.1 | Outside review of the annual assessment |

**For the processor:** the evidence above doubles as the SAQ A evidence folder (POL-01 4.7). The owner signs the 2026 SAQ A only after the 2026-09-30 items are done.
