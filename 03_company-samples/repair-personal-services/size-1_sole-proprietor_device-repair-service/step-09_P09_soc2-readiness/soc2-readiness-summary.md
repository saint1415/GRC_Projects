# SOC 2 Readiness Self-Check: Cris Santos Company | Other Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| Tier / Vertical | Sole Proprietorship / Other Services (except Public Administration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. The shop will not obtain a SOC 2 report (section 1) |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the ticketing and POS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-03 by the owner-technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person repair shop is not a service organization in the SOC 2 sense and will never obtain a SOC 2 report.** SOC 2 reports on controls over systems a company operates for its business customers. The shop repairs consumers' devices; no business relies on its systems, and a CPA examination would cost more than a month of revenue. The vertical research names no assurance alternative for this industry. When a customer asks about security, a one-page **self-attestation** backed by this checklist and the P07 POA&M is the right answer.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Criteria that assume a board or software development are marked N/A with the reason; criteria about tone, roles, and fixing deficiencies are met by the owner's direct oversight.
- **B. Reading the ticketing vendor's SOC 2 report.** SYS-01 holds all 5,600 customer records and operates most inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading the vendor's report each year (POL-01 6.3).

## 2. Scope
- **Services:** walk-in device repair, data transfer and recovery, and recycling drop-off for about 1,400 tickets a year; no services to other businesses.
- **System:** the Service Ticketing and Point-of-Sale System (P02).
- **People:** the owner-technician; the fill-in technician about 12 days a year.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 16 | 9 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC8.1 (no software development or infrastructure; the vendor's change management is inherited). Unlike a business with no one else in it, CC2.2 is not N/A here, because the fill-in technician works in the shop.
**Ready through the owner's direct oversight or the July work:** CC1.3 (roles), CC3.1 to CC3.3 (P05 and P01, including fraud risks such as fake payment texts and terminal skimming), CC4.2 (deficiencies go straight to the POA&M), and CC6.4 (locked, alarmed shop and cabinet).
**Not ready (9):** CC6.1, CC6.2, and CC6.3 (shared SYS-01 login, no MFA, stale session, unencrypted bench), CC6.5 (no sanitization or deletion), CC7.2 to CC7.4 (no monitoring, criteria, or incident plan at the time of the check), CC3.4 (new tools adopted without review), and CC9.2 (vendors and the fill-in technician without terms). Each maps to an open POA&M item in P07 or a P03 action.

**The repair-shop criterion is CC6.5.** For most small businesses, disposal is about old laptops. Here it is a daily service: drop-off devices, reused transfer drives, and copies of customers' phones. It is Not ready today and is the criterion a customer would care about most.

## 4. Ticketing vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One change-approval exception, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** (BP-01: RTO 8 h, RPO 1 h).
- **Controls the shop must run (CUECs):** user provisioning and removal, least-privilege roles, MFA, log review, and **no card data or credentials in free-text fields**. All four are open gaps today (POAM-001 to POAM-003, P03 G-077). The vendor's restricted credential field with automatic purge exists but is off by default, so **the vendor's controls protect the shop only once the owner does its part.**
- **Follow-ups:** bridge letter by 2026-10-31; ask how the vendor monitors the carved-out messaging gateway (fake texts are the P08 scenario); record the 72-hour incident notice term in the vendor list.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC1.1, CC1.5, CC2.2, CC2.3, CC6.1 (MFA), CC6.2, CC6.3, CC7.3, CC7.4, CC7.5 | MFA screenshots; named account list; signed fill-in agreement; new intake form; printed P08 contacts and walkthrough notes |
| By 2026-10-31 | CC2.1, CC3.4, CC4.1, CC5.2, CC5.3, CC6.1 (encryption), CC6.5 to CC6.8, CC7.2 | Encryption status; deletion and sanitization logs; router settings; monthly review log; approved tool list |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC5.1, CC7.1, CC9.1, CC9.2 | Course certificate; vendor list and recycler addendum; sealed envelope receipt |

**Self-attestation:** a one-page letter from the owner that summarizes this check and the POA&M, updated each July and given to anyone who asks how the shop protects customer data.
