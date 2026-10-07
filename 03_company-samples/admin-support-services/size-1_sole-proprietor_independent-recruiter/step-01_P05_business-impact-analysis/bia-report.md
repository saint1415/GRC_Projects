# Business Impact Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Sole Proprietorship

**Organization:** Cris Santos Company (independent recruiter: contract staffing and direct-hire placement) | **Tier:** Sole Proprietorship (owner-recruiter only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-recruiter, 2026-07-22, with the on-call IT support technician (under a confidentiality agreement) | **Adopted:** Owner-recruiter, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the Recover outcomes of the CSF 2.0 benchmark in the gap analysis (P03, RC.RP).

No law requires this business to have a contingency plan. The BIA exists because one person runs everything, and the business has no slack if that person or the accounts are unavailable.

## 2. Business description
The owner recruits IT support, accounting, and data analyst professionals for about 15 Florida client companies from a home office. About 65% of receipts are the owner's share of contract gross margin on 11 contractors, who are employed and paid by a contract staffing back-office partner. About 35% are direct-hire fees. The work runs on SaaS: the recruiting ATS (SYS-01), business email and files (SYS-02), the partner portal (SYS-03), accounting (SYS-04), and e-signature (SYS-05), reached from one laptop, a personal phone, and a home network. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of receipts, or a lost direct-hire fee) | $700 to $3,500 | Less than $700 |
| Operations | A contractor cannot start, or a client search is lost | Searches slowed; submittals a day late | Administrative delay only |
| Regulatory | Reportable breach of personal information (Fla. Stat. 501.171) or a discrimination charge | Missed contract or records duty | Internal policy deviation |
| Safety | Not applicable: no physical operations | | |
| Reputation | A client or the back-office partner ends the relationship | Candidate complaints or online reviews | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Contractor start requests and assignment support | High | 24 h | 8 h | 24 h |
| BP-02 Client submittals and interview coordination | High | 48 h | 24 h | 24 h |
| BP-03 Candidate sourcing and screening | Moderate | 72 h | 24 h | 24 h |
| BP-04 Billing and collections | Low | 168 h | 72 h | 24 h |
| BP-05 Business administration | Low | 168 h | 72 h | 24 h |

**What drives the values:** client relationships drive BP-01 and BP-02. A contractor who cannot start on the agreed Monday, or a candidate lost to a competing recruiter, can cost a month of margin or a whole fee. The 24-hour RPO for the ATS depends on the ATS vendor's daily backups, which the owner has not confirmed (the vendor's SOC 2 report was not requested). If the ATS account itself is lost (subscription lapse, account takeover, or vendor deletion 30 days after the subscription ends), **no RPO is supported today**, because there is no independent export (P01 R-010).

**What does not depend on the owner:** contractor pay. Clients approve timesheets directly in the partner portal and the partner runs payroll, so contractors are paid on time even if the owner is out for weeks. That is the most important resilience fact in this business, and it is why payroll recovery is not one of the owner's processes.

**Single-person dependency (the key finding).** The owner-recruiter is the only person who knows the open searches, holds the client and candidate relationships, and holds every credential. The email second factor is on the owner's one phone. If the owner is ill, injured, or without the phone, BP-01 and BP-02 exceed their MTD within one to two days, and no one can tell clients or contractors what is happening. Actions (P01 R-009, due 2026-12-31):
1. A one-page continuity sheet listing open searches, contractors on assignment, and client contacts, updated every Friday and kept in the file storage and on paper.
2. A sealed envelope with recovery codes for email, the ATS, and the partner portal, and the continuity sheet location, held by the owner's attorney.
3. An agreement with the partner's account manager to contact clients and contractors if the owner is unavailable for more than 2 business days.
4. A reciprocal arrangement with another independent recruiter to hold open searches for clients during a long absence, with a confidentiality agreement.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Recruiting ATS/CRM | Candidates, job orders, submittal history, AI match add-on | BP-02, BP-03 |
| SYS-02 Email, calendar, and files | Submittals, client and candidate correspondence, documents | BP-01 to BP-05 |
| SYS-03 Partner portal | Start requests, assignment changes, margin statements | BP-01, BP-04 |
| SYS-07 Phone | Calls and texts with candidates and clients; email second factor | BP-01, BP-02, BP-03 |
| SYS-06 Laptop | Main work device | All |
| SYS-08 Home network | Internet for the home office; phone hotspot is the fallback | All |
| SYS-04 Accounting SaaS | Invoices and bank feed | BP-04 |
| SYS-05 E-signature | Fee agreements and consent forms | BP-05 |
| Contracted services | Back-office partner (employer of record), outside bookkeeper, on-call IT support technician | BP-01, BP-04 |
| People | Owner-recruiter only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and email second factor | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the home office | 1 h | Phone hotspot; library or client office |
| 3 | SYS-02 Email | 4 h | Phone contact with clients and candidates from the printed continuity sheet |
| 4 | SYS-03 Partner portal access | 8 h (partner-hosted) | Start requests by phone to the partner's account manager |
| 5 | A clean work device | 8 h | Use the phone; IT technician reinstalls the laptop |
| 6 | SYS-01 ATS access | 24 h (vendor-hosted) | Job board inboxes; dated spreadsheet of notes |
| 7 | SYS-04 Accounting and SYS-05 e-signature | 72 h | Invoice template by email; paper signatures |
