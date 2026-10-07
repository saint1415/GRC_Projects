# SOC 2 Readiness Self-Check: Cris Santos Company | Energy | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Energy |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-12 (Part B) and 2026-08-14 (Part A) by the engineer-owner with the IT support contractor; adopted 2026-09-11 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person consultancy would not obtain a SOC 2 report.** SOC 2 reports on a service organization's system for customers who rely on it. Clients rely on the consultant's engineering judgment, not on a system it runs for them, and a CPA examination would cost more than a year's profit. Client A instead sends an annual supplier security questionnaire (addendum s.11), due 2026-10-30. The vertical's usual assurance alternative, a TSA compliance review, applies to designated pipeline operators, not to their consultants.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist. The results feed the 2026 questionnaire answers, so each answer is backed by evidence (POL-01 6.5).
- **B. Reading the suite provider's SOC 2 report.** The suite holds client files and Client A's SSI. The owner uses the CC criteria as a checklist when reading the provider's report every year (POL-01 6.3).

## 2. Scope
- **Services:** pipeline integrity engineering for three pipeline operators.
- **System:** the Core Business SaaS Stack (P02).
- **People:** the engineer-owner; subcontractors under their terms.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 15 | 6 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software or infrastructure delivered to clients; provider change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC2.3 (contacts untested; an unsupported 2025 questionnaire answer), CC6.1 (accounting SaaS without MFA; daily administrator use), CC6.4 (no secure container for SSI), CC6.5 (no destruction method; data kept past contract periods), CC6.7 (anonymous links, personal email, the AI tool), and CC9.2 (unapproved service and subcontractor). All six map to open POA&M items in P07 or P03 actions.

## 4. Suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. No exceptions.
- **Availability:** daily replicated storage and a 24-hour recovery objective **meet the BIA** for files stored in the suite (RTO and RPO 24 h for BP-02 and BP-03). Local files on the laptop are outside the provider's report.
- **Controls the owner must run (CUECs):** manage users and sharing, enable MFA, review audit logs, protect endpoints, and report suspected compromise. Sharing and log review are open gaps, so **the provider's controls protect client data only as well as the owner's sharing settings allow.**
- **AI writing assistant:** in scope of the report; the provider states it does not train on customer content. Recorded as AI-002 in P10.
- **Follow-ups:** bridge letter by 2026-10-30; anonymous links off tenant-wide by 2026-09-30.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.2, CC6.3, CC6.4, CC6.6, CC6.7, CC7.3, CC7.4 | MFA and encryption screenshots; sharing settings; cabinet photo; printed contacts; walkthrough notes |
| By 2026-10-30 | CC1.4, CC2.1, CC2.3, CC3.4, CC6.1, CC6.5, CC7.2, CC7.5, CC9.2 | Course certificate; review log; corrected questionnaire; destruction certificates; subcontractor terms; restore test |
| By 2026-12-31 | CC9.1 | Peer engineer arrangement; sealed recovery codes |
| By 2027-08-31 | CC3.3, CC4.1, CC7.1 | Updated risk register; outside review; settings review |

**Answer to Client A:** the 2026 questionnaire is answered from this checklist and the POA&M, with each "No" or "In progress" stated plainly and a target date.
