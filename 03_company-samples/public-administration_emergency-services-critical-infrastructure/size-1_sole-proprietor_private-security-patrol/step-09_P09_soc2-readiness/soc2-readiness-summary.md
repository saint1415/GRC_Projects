# SOC 2 Readiness Self-Check: Cris Santos Company | Emergency Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Tier / Vertical | Sole Proprietorship / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the patrol app vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`, an added file) |
| Prepared | 2026-08-13 (Part B) and 2026-08-14 (Part A) by the owner with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person patrol would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. Clients rely on the owner's patrols, not on a system the owner runs for them, and the cost of a CPA examination cannot be justified at about $180,000 in revenue. The Emergency Services registry lists no sector assurance alternative. When a property manager sends a security questionnaire, a **self-attestation** supported by this checklist is enough.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board, staff, or a development team, so they are marked N/A or are met through the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the patrol app vendor's SOC 2 report.** The vendor runs the system of record and most inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading its report every year (POL-01 6.6).

## 2. Scope
- **Services:** night patrols, alarm response, and reporting for 7 clients.
- **System:** the Patrol Business SaaS Stack (P02), including client keys and codes held in trust.
- **People:** the owner; the IT technician and backup agency under agreements.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 4 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendor's change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One licensed person sets the tone, holds every role, answers for the license, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (patrol app admin without MFA; codes unprotected), CC6.4 (client keys and cards on a labeled ring in an unlocked vehicle), CC6.7 (codes by SMS; public video links), and CC7.2 (no monitoring). All four map to open POA&M items in P07.

## 4. Patrol app vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-04-30. One exception (late removal of 2 departed vendor employees), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **just meet the BIA** (RTO 8 h, RPO 1 h for BP-01 and BP-03). The phone's offline mode covers a shift.
- **Carve-outs:** the hosting provider and the **AI model provider** that processes voice notes. The AI provider is reviewed by the vendor only by questionnaire, so the report gives no assurance about where voice notes go or how long they are kept (P10).
- **Controls the owner must run (CUECs):** MFA for admin and client users, prompt user removal, mobile device protection, audit log review, and reporting suspected compromise. MFA, user removal, and log review are open gaps (POAM-001, POAM-006, POAM-007), so **the vendor's controls protect the owner's data only once the owner runs these.**
- **Follow-ups:** bridge letter by 2026-10-31; written confirmation of incident notice within 10 days (Fla. Stat. 501.171(6)(a)); questions on the AI model provider.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.7, CC2.3, CC7.3, CC7.4 | MFA screenshots; vault in use; spreadsheet deleted; links expired; printed contacts; walkthrough notes |
| By 2026-10-31 | CC5.2, CC6.2, CC6.3, CC6.4, CC7.2, CC7.5, CC2.1, CC3.4 | Lockbox and coded tags; portal account review; monthly review log; restore test |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC6.6, CC9.1, CC9.2 | Course certificate; disposal record; guest network; signed backup agency agreement; vendor list |
| By 2027-08-31 | CC4.1, CC7.1 | Outside reviewer's notes; IT technician's settings review with the August 2027 assessment |

**Self-attestation for clients:** a one-page letter from the owner that summarizes this check and the POA&M, updated each August and sent with any security questionnaire answer.
