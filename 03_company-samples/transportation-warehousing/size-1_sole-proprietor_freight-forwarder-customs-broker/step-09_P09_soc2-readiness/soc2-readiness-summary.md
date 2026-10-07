# SOC 2 Readiness Self-Check: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| Tier / Vertical | Sole Proprietorship / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the customs software vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-25 (Part B) and 2026-08-28 (Part A) by the owner with the IT consultant; adopted 2026-09-14 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person brokerage would not obtain a SOC 2 report.** It is a service organization in the plain sense (importers rely on it to file their entries), but its clients are small businesses that do not ask for a CPA examination, and an audit would cost a large share of a year's revenue. The vertical has no sector-specific assurance alternative to SOC 2. What clients do ask for is a **completed security questionnaire**: three CTPAT importer clients send a business partner security questionnaire every year (N48-49-R05). This checklist supplies the answers and the evidence behind them.

The Security criteria are useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Many criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the customs software vendor's SOC 2 report.** The vendor operates most of the inherited controls for the system of record (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.3).

## 2. Scope
- **Services:** customs brokerage and ocean freight forwarding for about 40 clients.
- **System:** the Core Brokerage SaaS Stack (P02).
- **People:** the owner; the contract bookkeeper and IT consultant under written terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 14 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendors' change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (email readable without MFA; shared bookkeeper login), CC6.7 (client records in a consumer AI assistant and messaging app), CC7.2 (no sign-in monitoring), CC7.5 (no independent archive backup), and CC9.2 (no vendor list and no verification of partner payment changes). All five map to open POA&M items in P07.

**What to tell CTPAT clients now.** Answer the questionnaire truthfully from this checklist: MFA and encryption are in place for the system of record; the email, backup, and payment verification fixes are scheduled with dates; a written policy and incident runbook were adopted on 2026-09-14.

## 4. Customs software vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-06-30. One exception (late removal of a departed vendor employee's access), remediated.
- **Location:** production and backups in U.S. data centers, which supports 19 CFR 111.23(a).
- **Availability:** the vendor's RTO of 4 hours and RPO of 1 hour **meet the BIA** (BP-01: RTO 8 h, RPO 1 h).
- **Controls the business must run (CUECs):** manage users and MFA, protect credentials, review sign-in activity, report suspected compromise, and **check the accuracy of data submitted to CBP**. Sign-in review is an open gap (POL-01 7.7), and the last CUEC is the same duty the broker already carries under 111.28(a) and 111.39(b); it is why AI-assisted classifications need the review rule in P10.
- **Follow-ups:** bridge letter by 2026-10-31; ask for incident notice within 24 hours so the 72-hour CBP clock can be met.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC5.2, CC6.2, CC6.5 | MFA and account screenshots; wipe record |
| By 2026-10-31 | CC2.1, CC2.3, CC6.7, CC7.2, CC7.3, CC7.4, CC7.5, CC9.2 | Monthly review log; vendor list; backup restore record; walkthrough notes |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC3.4, CC6.3, CC6.6, CC9.1 | Course certificate; user review; business Wi-Fi setup; backup broker agreement |
| By 2027-08-31 | CC4.1, CC7.1 | Outside review notes; settings review |
