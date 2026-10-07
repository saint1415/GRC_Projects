# SOC 2 Readiness Self-Check: Cris Santos Company | Government Services and Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (facilities support contractor operating government buildings) |
| Tier / Vertical | Sole Proprietorship / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1 to CC9) only |
| Target report | None. Self-check only; no SOC 2 examination is planned |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-13 (Part B) and 2026-08-14 (Part A) by the owner with the IT technician; updated with P07 results and adopted 2026-09-04 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**The owner is a service provider to the city** in the SOC 2 sense: the owner operates the city's building systems and holds city data. But **no customer asks a one-person contractor for a SOC 2 report**, and a CPA examination would cost more than a month of receipts. The city uses its own security exhibit and questionnaire, and the prime uses the FAR flow-downs. Neither contract names SOC 2.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions that matches what the city's questionnaire asks. Criteria that assume a board or staff are marked N/A or satisfied by the owner's direct oversight, with the reason in the checklist. The result supports the owner's answers to the city questionnaire.
- **B. Reading the productivity suite provider's report.** The suite holds city drawings, cardholder exports, CUI, and the alarm emails. It is the one provider whose controls the owner relies on most. The owner uses the CC criteria as a checklist when reading its report every year (POL-01 6.3).

## 2. Scope
- **Services:** BAS operation, controls maintenance, and access control administration for three city buildings; BAS support at one federal building as a subcontractor.
- **System:** the Building Systems Support Environment (P02).
- **People:** the owner; the on-call IT technician under NDA.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1 to CC9, 33 criteria) | 11 | 14 | 6 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1 to P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (remote-desktop path and shared BAS password), CC6.3 (administrator account for daily work), CC6.7 (CUI and city data movement), CC7.2 (no monitoring of the riskiest path), CC7.5 (controller programs not recoverable), and CC9.1 (single-person dependency). Each maps to a POA&M item in P07 or a High risk in P01.

**Change management (CC8.1) is in scope, not N/A.** Unlike a business that only uses SaaS, this owner changes customer systems every week (programs, schedules, setpoints, cardholders). The city's written approval before each change is the control; the gap is the owner's own device and tenant changes, which are not recorded.

## 4. Productivity suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, 12 months ending 2026-03-31. Two exceptions (late removal of one departed provider employee; one change without a documented test), both remediated.
- **Availability:** the provider's stated recovery objectives are shorter than the BIA needs for BP-05 (RTO 8 h, RPO 24 h). **Meets the BIA.**
- **Controls the owner must run (CUECs):** manage users and MFA, configure sharing, review sign-in and audit logs, protect devices and recovery codes, and report suspected compromise. Two are open gaps: log review (POAM-006) and recovery codes (POAM-002). **The provider's logging protects the owner only once the owner reviews it.**
- **Government data:** the plan stores data in U.S. regions but is not a government cloud offering. That is acceptable for CUI held incidentally on a non-federal system (32 CFR 2002.14(h)(2)), and is a watch item if a future CT-F modification adds a CUI clause requiring NIST SP 800-171.
- **Follow-ups:** bridge letter by 2026-10-31; record the provider's incident notice terms on the provider list.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.2, CC6.3, CC6.8, CC2.3 | Account list sent to the city; standard account screenshot; printed contacts |
| By 2026-10-31 | CC6.1 (agent removed 2026-09-30; named BAS account 2026-10-31), CC6.7, CC7.2, CC7.5, CC9.2, CC2.1 | City IT manager's confirmation; restricted CUI folder; monthly review log; backup and comparison record; provider list |
| By 2026-12-31 | CC1.4 (courses by 2026-11-30), CC6.5, CC6.6, CC7.1, CC7.4, CC8.1, CC9.1, CC5.2 | Course certificates; disposal record; router settings; tabletop notes; change log; backup firm approval letter from the city |
| By 2027-08-31 | CC3.3, CC4.1 | Updated risk register; outside review report |

**Answer to the city questionnaire:** a one-page letter from the owner that summarizes this check and the POA&M, updated each August and sent with the account list.
