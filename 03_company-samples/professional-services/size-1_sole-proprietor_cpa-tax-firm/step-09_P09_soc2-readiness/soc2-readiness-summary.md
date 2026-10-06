# SOC 2 Readiness Self-Check: Cris Santos Company | Professional Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Tier / Vertical | Sole Proprietorship / Professional, Scientific, and Technical Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the tax software vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-28 (Part B) and 2026-07-31 (Part A) by the CPA-owner with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person tax practice would not obtain a SOC 2 report.** SOC 2 reports on a service organization's system for business customers that rely on it. This firm prepares returns and keeps books; its bookkeeping clients work in their own accounting and payroll systems and do not rely on a system the firm runs. The firm also performs no SOC examinations, so there is no independence question. When a bookkeeping client or a client's lender asks about security, a **self-attestation** letter backed by this checklist is the right answer.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Criteria that assume a board or staff are marked N/A or are met through the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the tax software vendor's SOC 2 report.** The vendor runs the practice's most important inherited controls (P02, P04). The owner reads its report against the same CC criteria every July (POL-01 6.4; 16 CFR 314.4(f)(3)).

## 2. Scope
- **Services:** individual and business return preparation, bookkeeping and payroll support, and IRS notice representation.
- **System:** the Tax Practice Systems Profile (P02).
- **People:** the CPA-owner; the IT consultant under a services agreement and the IRC 7216 notice.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 16 | 4 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board; the 314.4(i) report is also exempt under 314.6) and CC2.2 (no internal workforce). CC8.1 is *not* marked N/A even though the firm writes no software: the 2024 decision to turn off mailbox MFA was an unreviewed configuration change, which is exactly what change management is for.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Ready because of the tax preparer threat model:** CC3.3. The risk register treats refund diversion and misuse of the EFIN as fraud risks (R-002, R-005), not only as data security risks.
**Not ready:** CC6.1 (no MFA on the mailbox, which is the suite administrator), CC6.7 (plain attachments, text photos, and AI uploads), CC7.2 (no monitoring of sign-ins, rules, or EFIN counts), and CC9.2 (no oversight of most providers). All four map to open POA&M items in P07.

## 4. Tax software vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-03-31. One exception (late removal of departing vendor staff access), remediated.
- **Scope:** tax preparation, e-file transmission, and the client portal are in scope. **The AI document extraction feature is not**, which is one more reason it stays off (P10 AI-002).
- **Availability:** the vendor's RTO of 4 hours and RPO of 1 hour **meet the BIA** (BP-01: RTO 24 h, RPO 1 h).
- **Controls the firm must run (CUECs):** manage and promptly remove users, protect MFA devices, review activity reports, report suspected compromise, and secure endpoints and networks. The first one **failed**: the 2025 contract preparer's account stayed active for 15 months (P07). Activity review is also an open gap (POAM-007), so **the vendor's controls protect the firm only once the owner runs these.**
- **Follow-ups:** bridge letter by 2026-10-31; written confirmation that the vendor will report a breach to the firm within 10 days (Fla. Stat. 501.171(6)(a)); ask whether the vendor alerts customers to unusual filing activity under their EFIN.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-15 | CC6.1, CC5.2, CC3.4, CC8.1 | MFA and sign-in screenshots; change log entry for the scan-to-folder and MFA change |
| By 2026-10-31 | CC2.1, CC6.2, CC6.3, CC6.6, CC7.1, CC7.2, CC9.2 | Monthly review log; quarterly user review; vendor list; router settings |
| By 2026-12-31 | CC1.4, CC2.3, CC6.5, CC7.3, CC7.4, CC7.5, CC9.1 | Course certificate; client letter; walkthrough notes; backup restore test; retention schedule; continuation agreement |
| By 2027-01-15 | CC6.7 | Portal-only setting; required client MFA; photo cleanup record |
| By 2027-07-31 | CC4.1 | Plan for the outside review in the second year |

**Self-attestation for clients and lenders:** a one-page letter from the owner that summarizes this check and the POA&M, updated each July.
