# SOC 2 Readiness Self-Check: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system) |
| Tier / Vertical | Sole Proprietorship / Water and Wastewater Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs and short topic labels only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the remote access portal vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-22 (Part B) and 2026-07-24 (Part A) by the owner-operator with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A small water system would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. This business sells drinking water to households, has no business customers relying on its systems, and could not justify a CPA examination. Its regulator is the primacy agency, not a customer's auditor.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Criteria that assume a board are marked N/A; criteria that assume staff are met by the owner's direct oversight or applied to the relief operator, with the reason written in the checklist.
- **B. Reading the portal vendor's SOC 2 report.** The remote access portal is the path to the treatment process (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.5).

## 2. Scope
- **Services:** drinking water for 138 homes; no services to other businesses.
- **System:** the Water System Operations Profile (P02).
- **People:** the owner-operator; the relief operator, integrator, and IT technician under agreements.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 16 | 6 | 1 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not N/A, unlike a pure office business:** CC8.1 (change management). The integrator changes the PLC program, so change approval and a new program copy after each change matter here (POL-01 6.2 and 6.3).
**Not ready:** CC6.1 (portal password only; default passwords), CC6.3 (integrator's standing privilege), CC7.1 (firmware never updated), CC7.2 (no review of portal events), CC7.5 (no PLC program copy), and CC9.2 (no security terms with the integrator). All six map to open POA&M items in P07 or dated actions in P01.

## 4. Portal vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security only, period ending 2026-03-31. One access-removal exception, remediated.
- **The lesson of the report:** the vendor's controls tested cleanly, but the report lists five **complementary user entity controls** (MFA, user management, log review, router credentials, reporting compromise), and **none of the five was operating** when the owner read it. A clean SOC 2 report on the portal does not protect the panel until the owner runs those five controls (POAM-001, POAM-002, POAM-004, POAM-006, POAM-007).
- **Follow-ups:** bridge letter by 2026-10-31; ask how router firmware updates are signed; ask for a written incident notice time.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.2, CC6.6, CC2.2, CC2.3, CC7.3, CC7.4 | Portal account list with MFA; router settings record; walkthrough notes |
| By 2026-10-31 | CC6.3, CC6.7, CC7.2, CC7.5, CC8.1, CC9.2, CC2.1 | Maintenance log; integrator agreement terms; monthly review entries; program copies |
| By 2026-12-31 | CC1.4 and CC7.1 (by 2026-11-30), CC3.4, CC5.2, CC6.1, CC6.5, CC9.1 | Course certificate; firmware and password change record; disposal record; manual-operation sheet |
| By 2027-07-31 | CC3.3, CC4.1 | Fraud scenarios in P01; outside reviewer's notes |

If a lender, insurer, or the primacy agency asks about cybersecurity, the owner can share a one-page summary of this check and the POA&M, updated each July.
