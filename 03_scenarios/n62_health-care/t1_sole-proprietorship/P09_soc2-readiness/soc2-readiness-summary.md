# SOC 2 Readiness Self-Check: Cris Santos Company | Health Care | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Tier / Vertical | Sole Proprietorship / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the EHR vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the physician-owner with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A solo practice would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its business customers. This practice delivers care to patients, has no business customers relying on its systems, and could not justify the cost of a CPA examination. Payers and referral partners that ask about security accept a **self-attestation**, which this checklist supports.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Many criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the EHR vendor's SOC 2 report.** The EHR vendor operates most of the practice's inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report every year (POL-01 6.3; 45 CFR 164.308(b)).

## 2. Scope
- **Services:** primary care for about 900 patients; no services to other businesses.
- **System:** the Practice Systems Profile (P02).
- **People:** the physician-owner; contracted services under BAAs.
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
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (no MFA on email; laptop unencrypted), CC6.7 (texting and a consumer email account with PHI), CC7.2 (no log review), and CC9.2 (three vendors with PHI and no BAA). All four map to open POA&M items in P07.

## 4. EHR vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One change-approval exception, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** (RTO 8 h, RPO 1 h for BP-01 and BP-02).
- **Controls the practice must run (CUECs):** remove users promptly, protect MFA devices, review audit reports, and report suspected compromise. Audit review is an open gap (POAM-005), so **the vendor's logging protects the practice only once the owner reviews it.**
- **Follow-ups:** bridge letter by 2026-10-31; ask how the vendor monitors the carved-out e-prescribing network; ask for a shorter incident notice period at BAA renewal.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC2.3, CC7.3, CC7.4 | MFA and encryption screenshots; printed contacts; walkthrough notes |
| By 2026-10-31 | CC6.7, CC7.2, CC7.5, CC9.2, CC6.2, CC6.3 | Signed BAAs; monthly review log; EHR user review |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC6.6, CC9.1 | Course certificate; disposal record; coverage arrangement |

**Self-attestation for payers and referral partners:** a one-page letter from the owner that summarizes this check and the POA&M, updated each July.
