# SOC 2 Readiness Self-Check: Cris Santos Company | Real Estate | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| Tier / Vertical | Sole Proprietorship / Real Estate and Rental and Leasing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the transaction platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-19 (Part B) and 2026-08-21 (Part A) by the broker-owner with the IT technician; adopted 2026-09-15 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-broker brokerage would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This brokerage serves home buyers, sellers, and a few landlords; no business runs on its systems, and a CPA examination would cost more than a year's profit. Landlord clients and the professional liability insurer's renewal questionnaire accept a **self-attestation**, which this checklist supports.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are met through the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the transaction platform vendor's SOC 2 report.** The platform holds every contract and deadline and most identity documents. The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.3).

## 2. Scope
- **Services:** residential sales brokerage (about 20 sides a year) and tenant placement (about 10 a year).
- **System:** the TMCC (P02).
- **People:** the broker-owner; the coordinator and bookkeeper under engagement terms (pending).
- **Procedures:** POL-01, the callback rule (POL-01 8.4), and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 15 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; vendors' change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an independent settings check at least every second year.
**Ready because of this year's work:** CC3.3. Fraud is the center of the risk register: payment redirection and deposit diversion are R-001 to R-003, and the callback rule (POL-01 8.4) took effect on 2026-09-15.
**Not ready:** CC2.3 (clients are not told how wire instructions will arrive, and the website overstates security), CC6.1 (shared mailbox identity and weak MFA), CC6.7 (identity documents and wire instructions sent as ordinary attachments), CC7.2 (no monitoring), and CC9.2 (contractors with client data have no written terms). All five map to open POA&M items or dated actions in P07 and P01.

## 4. Transaction platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-05-31. One exception (late removal of access for departed vendor staff), remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the BIA** (BP-02: RTO 8 h, RPO 4 h).
- **Controls the brokerage must run (CUECs):** turn on MFA, assign roles and remove users promptly, review access logs, never share credentials, and report suspected compromise. Today the brokerage fails three of these (MFA off, a shared credential on email, no log review), so **the vendor's controls protect the brokerage only once POAM-001 to POAM-004 close.**
- **Follow-ups:** bridge letter by 2026-10-31; review the e-signature vendor separately; confirm that the vendor's incident notice period is no longer than 10 days after determination, to match Fla. Stat. 501.171(6)(a).

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.3, CC5.2, CC3.4 | Separate coordinator login; MFA screenshots; coordinator role settings |
| By 2026-10-31 | CC2.3, CC6.7, CC7.2, CC6.2, CC1.5, CC6.6, CC7.1, CC7.3, CC7.4, CC2.1 | Signed wire safety notices; website statement; alert settings and weekly review log; signed engagement terms; router settings; walkthrough notes |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC7.5, CC9.1, CC9.2 | Course certificates; disposal record; backup restore test; backup broker arrangement; screening vendor review |
| By 2027-08-31 | CC4.1 | IT technician settings check |

**Self-attestation for landlord clients and the insurer:** a one-page letter from the owner that summarizes this check and the POA&M, updated each August.
