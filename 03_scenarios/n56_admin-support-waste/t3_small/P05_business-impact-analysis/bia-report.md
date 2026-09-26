# Business Impact Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

**Organization:** Cris Santos Company, LLC (temporary staffing firm) | **Tier:** Small (60 internal staff; about 450 associates on assignment weekly) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Information Security Lead) with the Payroll Manager, HR and Compliance Manager, and Director of Recruiting | **Approved:** COO, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the firm depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan due 2026-12-31 (CP-2; CSF 2.0 RC.RP), including the manual payroll procedure;
- the backup and recovery part of the electronic Form I-9 records security program (8 CFR 274a.2(g)(1)(ii));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The firm places temporary associates with about 180 Florida clients from headquarters and 3 other branches. Every week it onboards about 40 new associates, dispatches about 450 to client shifts, collects approved time, and pays them on Friday. Work runs on the Associate Payroll and Applicant Tracking Platform (APATP): a SaaS ATS with the I-9 module and client portal, a SaaS payroll platform, a timekeeping app, an identity provider, and a cloud tenant (integration service, reporting database, document archive, backups). See `../scenario-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $20.4 million in receipts a year: about $80,000 in billings and about $19,000 in gross margin per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $60,000 (about 3 days of gross margin) or any loss of payroll funds | $20,000 to $60,000 | Less than $20,000 |
| Operations | Associates not paid on payday, or shifts cannot be filled at 2 or more branches | One branch or one division stops | Staff slowed but working |
| Regulatory | Missed I-9 or E-Verify deadlines across many hires; missed breach notice; inability to produce I-9s on inspection | A single late form or notice | Internal policy deviation |
| Safety | Associates sent to a closed or unsafe site | Delayed site safety information | None |
| Reputation | Loss of a top-10 client or public wage complaints | Associate complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Weekly associate payroll | High | 48 h | 24 h | 24 h |
| BP-02 Time capture and client approval | High | 72 h | 24 h | 4 h |
| BP-03 Associate onboarding (I-9, E-Verify, background checks) | High | 72 h | 24 h | 4 h |
| BP-04 Client order intake and dispatch | High | 24 h | 8 h | 4 h |
| BP-05 Associate communications | Moderate | 24 h | 8 h | 24 h |
| BP-06 Recruiting and candidate screening | Moderate | 72 h | 48 h | 24 h |
| BP-07 Compliance records and inspection response | Moderate | 72 h | 48 h | 24 h |
| BP-08 Client billing and collections | Moderate | 120 h | 72 h | 24 h |
| BP-09 Internal staff payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Payday drives BP-01.** Payroll is processed Thursday for Friday pay. A payroll that is not funded within 48 hours of the Thursday cutoff means associates go unpaid, and temporary workers move to competitors fast.
- **Legal clocks drive BP-03 and BP-07.** Section 2 of Form I-9 and the E-Verify case are due within 3 business days of hire, and an inspection notice gives 3 business days to produce forms. These are fixed by rule, so the MTD cannot be longer than 72 hours; paper I-9 packets make that achievable.
- **Tomorrow's shifts drive BP-04.** Account Managers can dispatch by phone from the last export for about a day.
- **Punch data drives the 4-hour RPOs.** Clock-in records and onboarding forms entered in the last few hours are hard to recreate.

**Key findings:**
- The payroll vendor's stated recovery objectives (RTO 8 hours, RPO 1 hour; P09 Part B) **meet** BP-01. The ATS vendor has not yet stated its objectives, so the 24-hour RTO and 4-hour RPO for BP-02 and BP-03 are **unconfirmed** until its SOC 2 report arrives.
- The firm-managed backups of the reporting database and I-9 archive have **never been restore-tested**, so BP-07 recovery is unproven (P01 R-004, R-009).
- There is **no manual payroll procedure**. It is the most important workaround in this BIA and does not yet exist (POAM-011).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Payroll and billing platform (SaaS) | Pay calculation, funding, tax, invoices | BP-01, BP-08, BP-09 |
| SYS-01 ATS and onboarding (SaaS) | Candidates, onboarding, I-9 module, client portal, texting | BP-02 to BP-07 |
| SYS-03 Identity provider | Single sign-on and MFA for SYS-01, SYS-04, SYS-06 admin | All except SYS-02 access |
| SYS-06 Timekeeping app (SaaS) | Clock-in with GPS | BP-02 |
| SYS-04 Integration service | New hires, rates, and time into payroll | BP-01, BP-02 |
| SYS-04 Document archive and backup vault | Scanned I-9s 2014-2022; backups | BP-07 |
| SYS-08 E-Verify; SYS-07 screening provider | Eligibility cases; consumer reports | BP-03 |
| SYS-10 Office networks and internet | Firewalls, Wi-Fi, single ISP at each office | All |
| SYS-11 Endpoints | 62 laptops, 34 smartphones | All |
| People | Payroll team (4), Onboarding and Compliance Specialists (6), recruiters, Account Managers, IT Manager, managed IT provider | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 Identity provider and payroll platform access for the payroll team | 1 h | Two break-glass accounts stored offline (to be created); payroll vendor support line for emergency funding |
| 2 | SYS-10 Internet at HQ (payroll team) | 2 h | Cellular hotspots; payroll team can work from home |
| 3 | SYS-11 Clean laptops for the payroll team and Account Managers | 4 h | 4 pre-imaged spare laptops at HQ |
| 4 | SYS-02 Payroll platform | 8 h (vendor) | Manual off-cycle payroll from the prior register (to be written) |
| 5 | SYS-01 ATS, client portal, and texting | 8 h | Phone dispatch from the last export; paper timesheets; paper I-9 packets |
| 6 | SYS-06 Timekeeping app | 24 h | Paper timesheets signed by client supervisors |
| 7 | SYS-04 Integration service | 24 h | Manual entry of new hires and time batches into payroll |
| 8 | SYS-08 E-Verify and SYS-07 screening provider access | 24 h | Direct website access from any laptop; record outage screenshots |
| 9 | SYS-04 Document archive | 48 h | Restore from the immutable backup (once built) |
| 10 | SYS-04 Reporting database | 72 h | Reports run directly in the ATS and payroll platform |
