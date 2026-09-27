# SOC 2 Readiness Self-Check: Cris Santos Company | Finance and Insurance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Tier / Vertical | Sole Proprietorship / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. No SOC 2 examination is planned (section 1) |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the portfolio and billing platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-16 (Part B) and 2026-07-17 (Part A) by the owner-adviser with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person adviser would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This adviser serves individuals and families, no business relies on its systems, and a CPA examination would cost more than a month's revenue. The assurance that matters here runs the other way: the vertical profile (`02_industry-rules/finance-insurance/profile.csv`) names regulatory examinations and SOC 1 reports from service providers as the assurance alternatives. For this adviser that means the **Florida OFR examination** of books and records (Fla. Stat. 517.121(2)) and the **vendors' own reports**. Clients and referral sources who ask about security get a one-page letter from the owner that summarizes this check and the POA&M.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason in the checklist.
- **B. Reading vendor reports.** The portfolio platform operates the inherited controls for billing and reporting (P02, P04). The owner uses the CC criteria as a checklist when reading its report each year (POL-01 6.3; 16 CFR 314.4(f)(3)).

## 2. Scope
- **Services:** discretionary portfolio management and financial planning for about 70 client households; no services to other businesses.
- **System:** the Advisory Practice Systems Profile (P02).
- **People:** the owner-adviser; contracted services.
- **Procedures:** POL-01 (including the callback rule) and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 15 | 4 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board; the 314.4(i) board report is also exempt at this size), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; vendors' change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, CC4.2, and CC6.2. One person sets the tone, holds every role, is the only user, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Ready on its merits:** CC3.3. Fraud is the top risk in the register (R-001), which is unusual for a firm this small and a direct result of the 2026-06-18 near miss.
**Not ready:** CC6.1 (MFA off on five administrator accounts; USB backup unencrypted), CC6.7 (attachments, a consumer AI assistant, and money movement requests by email), CC7.2 (no monitoring), and CC9.2 (vendor oversight). All four map to open POA&M items in P07.

## 4. Portfolio platform report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One access-removal exception, remediated.
- **Availability:** the vendor's stated RTO of 24 hours and RPO of 4 hours meet BP-04 (fee billing, RTO 72 h). They do **not** meet BP-01's 8-hour RTO on their own; BP-01 relies on trading directly in the custodian portal while the platform is down.
- **Controls the adviser must run (CUECs):** turn on MFA, remove users promptly, review fee calculations before sending fee files, and report suspected compromise. **The vendor's access controls assumed MFA was on; it was off** (POAM-001). The fee-file review is already done each quarter.
- **Follow-ups:** bridge letter by 2026-10-31; ask for a fixed incident notice time; request the custodian's SOC 1 Type 2 at the July 2027 review.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC5.2, CC6.1, CC6.4, CC2.3, CC7.3, CC7.4 | MFA screenshots; encrypted drive; client letter; printed contacts; walkthrough notes |
| By 2026-10-31 | CC2.1, CC6.3, CC6.7, CC7.2, CC7.5, CC9.2, CC3.4 | Monthly review log; vendor list and signed terms; backup service records |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC6.5, CC6.6, CC7.1, CC9.1 | Course certificate; disposal record; router settings; successor adviser arrangement |
| By 2027-07-31 | CC4.1 | Outside reviewer's notes |
