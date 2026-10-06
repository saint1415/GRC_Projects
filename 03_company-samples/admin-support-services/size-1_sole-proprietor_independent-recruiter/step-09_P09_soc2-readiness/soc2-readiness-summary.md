# SOC 2 Readiness Self-Check: Cris Santos Company | Administrative and Support | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Administrative and Support and Waste Management and Remediation Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the back-office partner's SOC 2 Type 2 report (`vendor-soc2-review.csv`, added for this tier) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the owner-recruiter with the IT support technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**An independent recruiter would not obtain a SOC 2 report.** SOC 2 reports on a service organization's system for the business customers that rely on it. This business refers people. Clients receive resumes by email; they do not rely on a system the owner runs on their behalf, and the contractors' pay runs on the partner's system, not the owner's. The cost of a CPA examination would also be out of proportion to $180,000 in receipts. Clients that ask about security accept a short written answer, which this checklist supports.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the partner's SOC 2 report.** The back-office partner holds the most sensitive data in the business model (contractor SSNs, bank accounts, I-9s, background checks). The owner uses the CC criteria as a checklist when reading its report every year (POL-01 6.3).

## 2. Scope
- **Services:** recruiting and placement for about 15 Florida clients; contract staffing through the partner.
- **System:** the Recruiting and Placement Systems Profile (P02).
- **People:** the owner-recruiter; the bookkeeper and IT technician under contract.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 15 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; SaaS setting changes, including AI settings, are handled by the change rule under CC3.4).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (weak MFA and a reused password over Restricted data), CC6.5 (consumer reports and devices with no disposal step), CC6.7 (SSNs by email; resumes in a consumer chatbot), CC7.2 (no account monitoring), and CC9.2 (no vendor security terms). All five map to open POA&M items in P07.

## 4. Partner report (Part B)
- **Opinion:** Type 2, unqualified, Security and Confidentiality, period ending 2026-03-31. One access-removal exception (2 of 25 terminated partner employees kept portal access for more than 5 business days), remediated.
- **What the report does not cover:** bank-change requests received by the partner's payroll desk. The desk accepts forms forwarded from the owner's email without a call-back. **The partner's strong self-service controls protect contractors only if forwarded changes are refused**, which is why the owner asked for that in writing (POAM-004) and adopted POL-01 6.6.
- **Controls the owner must run (CUECs):** protect portal credentials and MFA, keep access to authorized users, submit changes only through the portal, review margin statements, and report suspected compromise. MFA and reporting are open gaps (POAM-001, POAM-006).
- **Follow-ups:** bridge letter by 2026-10-31; authenticator-app codes for the owner's portal account; a 10-day breach notice clause; the portal's recovery time objective (the BIA needs start requests back within 8 hours, and the phone fallback covers that today).

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.2, CC6.5, CC6.7, CC2.3, CC7.3, CC7.4 | MFA screenshots; disposal record; client letters; printed contacts; walkthrough notes |
| By 2026-10-31 | CC6.1, CC2.1, CC6.3, CC7.1, CC7.2, CC7.5 | Purge re-search result; monthly review log; account review; first ATS export |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC9.2 (addendum by 2026-11-30), CC3.4, CC6.6, CC9.1 | Course certificate; signed addendum; change log; network settings; continuity sheet |
| By 2027-07-31 | CC3.3, CC4.1 | Updated P01; outside review notes |

**Answer for client questionnaires:** a one-page letter from the owner that summarizes this check, the POA&M, and the partner's SOC 2 opinion, updated each July.
