# Business Impact Analysis: Cris Santos Company | Educational Services | Sole Proprietorship

**Organization:** Cris Santos Company (tutoring and educational support service) | **Tier:** Sole Proprietorship (owner-tutor only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-tutor, 2026-07-14, with the on-call IT technician (under a confidentiality and data-handling agreement since 2026-07-08) | **Adopted:** Owner-tutor, 2026-07-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the tutoring business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01), which is also the risk assessment that 16 CFR 312.8(b)(2) requires for children's personal information;
- the recovery order in the ransomware runbook (P08);
- the contingency rules in the consolidated policy (POL-01 section 11).

## 2. Business description
One owner-tutor works with about 55 active students (36 under 13, 19 teens), about 32 session hours a week in the school year. About 60% of sessions are online; the rest are in students' homes or a library study room. There are no employees and no substitute tutor. The business runs on SaaS: an email and files suite (SYS-01), a client-management SaaS for scheduling and billing (SYS-02), a website-builder site with a student practice portal (SYS-03), a video platform (SYS-04), and an accounting SaaS (SYS-08), reached from one laptop (SYS-05), one personal phone (SYS-06), and the home network (SYS-07). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $700 of sessions per weekday.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of sessions) | $700 to $3,500 | Less than $700 |
| Operations | No sessions can be held or families cannot be reached | Sessions held with workarounds or partly rescheduled | Administrative delay only |
| Regulatory | Exposure of children's or student records that triggers Florida notice, or an FTC COPPA issue | Missed notice, consent, or deletion duty that can be fixed quickly | Internal policy deviation |
| Safety | A child is placed at risk (for example, an in-home session time miscommunicated) | Inconvenience to a family | None |
| Reputation | Families withdraw or warn other families; school or library partners stop referrals | Complaints or a poor online review | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Tutoring sessions (online and in person) | High | 48 h | 24 h | 24 h |
| BP-02 Scheduling and parent communication | High | 24 h | 8 h | 24 h |
| BP-05 Student records and learning plans | High | 120 h | 72 h | 24 h |
| BP-03 Student practice portal and progress tracking | Moderate | 168 h | 72 h | 24 h |
| BP-04 Billing and payments | Moderate | 336 h | 72 h | 24 h |

**What drives the values:** families must hear about a cancelled or moved session the same day, so BP-02 has the shortest MTD. Sessions (BP-01) can be moved within a week, but SAT and ACT students have fixed test dates and families leave after repeated cancellations. Billing (BP-04) has the longest MTD because most families prepay 10-session packages. BP-05 is rated High because the student folders hold IEP and 504 plans and evaluations: losing them disrupts sessions, and exposing them triggers Florida notice (Fla. Stat. 501.171). The 24-hour RPO for BP-05 is **not supported today**. The only copy outside the laptop is cloud storage with desktop sync, so ransomware would sync encrypted files to the cloud, and version history lasts only 30 days (P01 R-001).

**Single-person dependency (the key finding).** The owner-tutor is the only tutor, the only administrator of every account, and the only person families know. The second factor for the client-management SaaS and the accounting SaaS is on the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-02 exceed their MTD within two days, and nobody else can tell 55 families what is happening. Actions (P01 R-012, due 2026-12-31):
1. Write a one-page emergency sheet (how to send one message to all families from the client-management SaaS, and which families have SAT or ACT test dates soon) and give it, in a sealed envelope with account recovery codes, to a trusted family member designated as the emergency contact. The envelope is for notifying families only, not for reading student records.
2. Agree in writing with another independent tutor to take urgent SAT and ACT students for up to four weeks if the owner cannot teach.
3. Store recovery codes for every account (SYS-01 to SYS-04, SYS-08) in that envelope and in the password manager, so a lost phone does not lock the owner out.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Client-management SaaS | Schedule, parent contacts, session notes, invoices, card payments; vendor backups; MFA enforced | BP-01, BP-02, BP-04 |
| SYS-06 Mobile phone | Calls and texts with parents; second factor for SYS-02 and SYS-08; hotspot | BP-01, BP-02 |
| SYS-05 Laptop | Teaching device for online sessions; access to every SaaS | BP-01, BP-03, BP-05 |
| SYS-04 Video platform | Online sessions (about 60% of hours) | BP-01 |
| SYS-07 Home network | Internet for online sessions; the phone hotspot is the fallback | BP-01, BP-02 |
| SYS-01 Email and files suite | Student folders, lesson plans, progress reports, email | BP-01, BP-02, BP-05 |
| SYS-03 Website and student practice portal | Assignments, work photos, reading audio, messages | BP-03 |
| SYS-08 Accounting SaaS | Bookkeeping and tax export | BP-04 |
| Contracted help | On-call IT technician (hourly); tax preparer (annual) | BP-04, all recovery |
| People | Owner-tutor only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and account second factors | 2 h | Recovery codes in the password manager and the sealed envelope; replacement phone from the carrier |
| 2 | SYS-02 Client-management SaaS (schedule and parent contacts) | 8 h (vendor-hosted) | Printed weekly schedule and parent contact sheet; call or text from the phone |
| 3 | A clean teaching device | 24 h | The IT technician's loaner laptop (available within a day), used through the browser only; move sessions to in person; the IT technician rebuilds the owner's laptop |
| 4 | SYS-04 Video platform | 24 h | Phone calls with printed worksheets; in-person sessions |
| 5 | SYS-01 Email and files suite (student folders) | 72 h | Restore from 30-day version history; ask parents to resend IEP and 504 plans; rebuild learning plans from SYS-02 session notes |
| 6 | SYS-03 Student practice portal | 72 h | Paper worksheets; parents email photos of work to the business email |
| 7 | SYS-08 Accounting SaaS and billing exports | 72 h | Paper session log; invoice when restored |
