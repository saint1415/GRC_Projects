# SOC 2 Readiness Self-Check: Cris Santos Company | Financial Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Tier / Vertical | Sole Proprietorship / Financial Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the AMS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`, an added file) |
| Prepared | 2026-08-06 (Part B) and 2026-08-07 (Part A) by the owner-agent with the IT consultant; adopted 2026-09-14 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person agency would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. The agency sells and services insurance; the insurers rely on their own systems and ask the agency for **security questionnaires** instead, under their data security addenda. A CPA examination would cost more than a month of commissions and answer a question no one is asking.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions, and the answers feed the lead insurer's questionnaire due 2026-09-30. Criteria that assume a board, staff, or a development team are marked N/A or satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the AMS vendor's SOC 2 report.** The AMS vendor operates most of the agency's inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading the report every year (POL-01 6.4).

## 2. Scope
- **Services:** property and casualty insurance sales and service for about 640 client accounts; no services to other businesses' systems.
- **System:** the Agency Systems Profile (P02).
- **People:** the owner-agent; the bookkeeper and IT consultant as contractors.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 14 | 6 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; the vendors' change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Ready on evidence:** CC3.1, CC3.2, CC3.3 (fraud scenarios are the core of P01), CC5.1, CC5.3, and CC6.8.
**Not ready:** CC6.1 (text-code MFA and a shared banking identity), CC6.2 (banking access given by sharing credentials), CC6.5 (devices with client data awaiting disposal), CC6.7 (documents by plain email and text), CC7.2 (no monitoring), and CC9.2 (vendors without terms). All six map to open POA&M items in P07.

## 4. AMS vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One access-removal exception, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** (RTO 8 h, RPO 4 h for BP-01).
- **Controls the agency must run (CUECs):** manage users, protect MFA devices, review activity reports, use the client upload portal for sensitive documents, and report suspected compromise. Two are open gaps (POAM-003 review, POAM-004 upload portal), so **the vendor's protections stop at the agency's own habits.**
- **Follow-ups:** bridge letter by 2026-10-31; ask whether the next report covers the AI assistant added in 2026-06 (P10 AI-002); run the first data export to test the contract's return terms (POAM-007).

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.1, CC6.2, CC6.3, CC2.3 | MFA screenshots; bank sub-user page; client letter; printed contacts |
| By 2026-10-31 | CC2.1, CC3.4, CC6.5, CC6.6, CC6.7, CC7.1, CC7.2, CC7.3, CC7.4, CC9.2 | Disposal log; router settings; monthly review log; walkthrough notes; signed bookkeeper terms |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC7.5, CC9.1 | Course certificate; first AMS export; emergency servicing arrangement |
| Later | CC4.1 (outside review by 2027-08-31), CC6.4 (garage files by 2027-01-31) | Reviewer's notes; shredding certificate |

**Answer to the insurers:** the lead insurer's questionnaire goes back by 2026-09-30 with this checklist's status, POL-01, and the P07 POA&M, and is updated each August.
