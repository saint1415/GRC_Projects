# SOC 2 Readiness Self-Check: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Tier / Vertical | Sole Proprietorship / Accommodation and Food Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the innkeeping software vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-22 (Part B) and 2026-07-24 (Part A) by the owner-innkeeper with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A bed-and-breakfast inn would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. The inn serves travelers, has no business customers relying on its systems, and could not justify a CPA examination. Its assurance mechanism is **PCI DSS validation** with the payment facilitator (SAQ A plus SAQ P2PE, due 2026-12-31; P03). Guests, OTAs, and the facilitator do not ask for SOC 2.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board, staff, or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the innkeeping vendor's SOC 2 report.** The innkeeping vendor operates most of the inn's inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.2).

## 2. Scope
- **Services:** lodging and breakfast for about 600 stays a year; no services to other businesses.
- **System:** the Inn Business Systems Profile (P02).
- **People:** the owner-innkeeper and the relief innkeeper; contractors under their agreements.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 18 | 4 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC8.1 (no software development or infrastructure; the vendors' change management is inherited). CC2.2 is **not** N/A, unlike a practice with no helpers: the relief innkeeper uses the systems and needs a written briefing.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (passwords only, saved in a family browser; laptop unencrypted), CC6.5 (card data and ID photos never disposed of), CC6.7 (card numbers by email and chat), and CC7.2 (no monitoring). All four map to open POA&M items in P07.

## 4. Innkeeping vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One access review exception, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** (BP-01 RTO 8 h, BP-02 RTO 4 h, both RPO 1 h).
- **Scope gap:** the AI add-on launched after the report period and is not in the system description; P10 handles it.
- **Controls the inn must run (CUECs):** manage users and roles, turn on MFA, protect credentials, review activity logs, and report suspected compromise. MFA and log review are open gaps (POAM-001, POAM-008), so **the vendor's controls protect the inn only once the owner does these.**
- **Follow-ups:** bridge letter by 2026-10-31; confirm the vendor's breach notice time against the Florida 10-day third-party agent rule (Fla. Stat. 501.171(6)(a)).

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC2.3, CC5.2, CC6.4, CC6.6, CC7.1, CC7.3, CC7.4 | MFA and encryption screenshots; router checklist; printed contacts; walkthrough notes |
| By 2026-10-31 | CC2.1, CC3.4, CC6.1, CC6.2, CC6.3, CC6.5, CC6.7, CC7.2, CC7.5, CC9.2 | Password manager in use; shredding and purge records; named relief account; monthly review log; provider list |
| By 2026-12-31 | CC1.4, CC2.2 (by 2026-11-30), CC9.1 | Course certificate; relief briefing; relocation arrangement |
| By 2027-07-31 | CC3.3, CC4.1 | Updated risk register; outside review |

**Statement for guests, OTAs, and the payment facilitator:** the 2026 SAQs and attestations of compliance, supported by this check and the POA&M, updated each year.
