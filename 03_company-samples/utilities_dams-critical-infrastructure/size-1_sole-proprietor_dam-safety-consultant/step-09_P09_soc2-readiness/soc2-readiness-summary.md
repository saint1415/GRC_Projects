# SOC 2 Readiness Self-Check: Cris Santos Company | Dams | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Dams |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. A self-check, not a SOC 2 examination |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the email and file suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the owner-engineer with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person engineering consultancy would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for customers that rely on its systems. The business does not host or run anything for its clients; it inspects their dams and writes reports. Its clients check its security in other ways: Client A through CSCA-A and its own gateway controls, Client B through GRS-B, and both through security questionnaires. The Dams vertical names no sector-specific alternative to SOC 2.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. It doubles as the answer sheet for client questionnaires. Criteria that assume a board, staff, or a development team are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the suite provider's SOC 2 report.** The suite holds client files and agreements and runs most inherited controls (P02, P04). The owner uses the CC criteria as a checklist when reading the provider's report every year (POL-01 6.2).

## 2. Scope
- **Services:** dam safety inspections, instrumentation reviews, gate reliability studies, and sealed reports for three clients.
- **System:** the Core Business SaaS Stack (P02), including the owner's credentials for client-operated systems.
- **People:** the owner-engineer; the field assistant on field days; the IT technician on request.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 16 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; providers' change management is covered by their reports).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role, and fixes deficiencies, and the Part 12D statement of independence makes the integrity commitment explicit. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC2.1 and CC7.2 (no review of sign-ins or gateway sessions), CC6.1 (gateway credentials on a mixed-use administrator laptop; two accounts without MFA), CC6.7 (client data with an AI vendor and a personal photo cloud; CEII on an unencrypted drive), and CC9.2 (vendors and the field assistant unreviewed). All five map to open POA&M items in P07.

**Confidentiality is out of scope on paper, not in practice.** The C1 criteria are marked N/A because this is a Security-only self-check. The business's real obligations on confidential information (CSCA-A, the CEII non-disclosure agreement, GRS-B) are analyzed row by row in P03 and enforced by POL-01 section 8.

## 4. Suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. One access-removal exception, remediated.
- **Availability:** the provider's commitments and annual recovery test **meet the BIA** for BP-01 (RTO 4 h, RPO 24 h).
- **Controls the business must run (CUECs):** turn on MFA, manage sharing, review sign-in activity, and protect devices. Sign-in review is an open gap (POAM-009), so **the provider's logging protects the business only once the owner reads it.**
- **Gap in coverage:** the built-in AI writing assistant (P10 AI-002) was released after the report period. The owner relies on the business plan terms for it until the next report.
- **Follow-ups:** bridge letter by 2026-10-31; ask whether the next report covers the AI assistant.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.1, CC6.4, CC6.7, CC2.3, CC7.3, CC7.4 | Standard account and password manager screenshots; encrypted drive; printed contacts; walkthrough notes |
| By 2026-10-31 | CC1.5, CC2.1, CC6.2, CC6.5, CC6.6, CC7.2, CC9.2, CC3.4 | Field assistant agreement; session log; account list; register and certificate; network change record; vendor list |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC7.5, CC9.1 | Course certificate; restore test record; peer engineer letter |
| By 2027-07-31 | CC3.3, CC4.1, CC7.1 | Updated risk register; outside review notes |

**Answer for client questionnaires:** a one-page letter from the owner summarizing this check and the open POA&M items, updated each July and sent to Client A with the CSCA-A items marked.
