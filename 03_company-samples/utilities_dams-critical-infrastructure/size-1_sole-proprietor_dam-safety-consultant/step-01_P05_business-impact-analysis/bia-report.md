# Business Impact Analysis: Cris Santos Company | Dams | Sole Proprietorship

**Organization:** Cris Santos Company (independent dam safety engineering consultant) | **Tier:** Sole Proprietorship (owner-engineer only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-engineer, 2026-07-21, with the on-call IT technician (under NDA) | **Adopted:** Owner-engineer, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the consultancy depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the client duties that depend on being reachable, above all the 24-hour incident notices in Client A's and Client B's agreements (P03).

## 2. Business description
One licensed professional engineer inspects dams and writes sealed safety reports for three clients from a home office in Florida. The business has no employees. Work runs on a business email and file suite, an engineering laptop, a phone, and a field tablet, plus named accounts on client-operated systems: Client A's document portal and vendor remote access gateway, and Client B's instrumentation data platform. The owner is Client A's approved independent consultant for its next Part 12D periodic inspection. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week and a half of revenue) | $1,000 to $5,000 | Less than $1,000 |
| Operations | Client work stops; a fixed field date is lost | Work slowed; deliverables slip by days | Administrative delay only |
| Regulatory | A client misses a FERC duty because of the consultant, or a CEII or contract security term is breached | A client deadline is put at risk | Internal policy deviation |
| Safety | A condition that may affect dam safety is not passed to the dam owner in time | Safety findings delayed but delivered before they matter | None |
| Reputation | Loss of a client or of standing as an approved independent consultant | Client complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Client communications, secure document exchange, and incident notices | High | 24 h | 4 h | 24 h |
| BP-02 Dam safety field inspections | High | 72 h | 24 h | 24 h |
| BP-03 Engineering analysis and sealed reports | High | 120 h | 48 h | 24 h |
| BP-04 Billing and accounting | Low | 240 h | 72 h | 24 h |
| BP-05 Records and compliance administration | Low | 168 h | 72 h | 168 h |

**What drives the values:** BP-01 has the shortest MTD because the business promised two clients a 24-hour incident notice and because a dam owner must hear at once about a condition seen in the field, so it can report under 18 CFR 12.10. BP-02 is set by fixed field windows with client staff and specialty crews. BP-03 is set by Client A's Part 12D filing schedule and by the fact that only the owner can sign and seal the report (18 CFR 12.36(h)). The 24-hour RPO for BP-03 is **not supported today** for engineering model files and the CEII archive: they stay on the laptop and reach only the monthly, unencrypted USB backup (P01 R-006).

**Single-person dependency (the key finding).** The owner is the only engineer, the only signer, and the only person who holds the email, portal, gateway, and device credentials. Two things make this harder to fix than in other one-person businesses:
- **The FERC approval is personal.** The Director of the Division of Dam Safety and Inspections approved the owner by name as Client A's independent consultant (18 CFR 12.34(a)). A replacement engineer needs a new approval before doing the inspection.
- **CEII access is personal.** The upstream project CEII was released to the owner under the owner's own non-disclosure agreement, and the Client A CEII under Client A's written authorization for the owner. Neither can be handed to a stand-in. It must be returned or destroyed.

Actions (P01 R-012, due 2026-12-31):
1. Identify a peer engineer who meets 18 CFR 12.31(a), and agree in writing to step in for client communications and, with the client's approval, for non-FERC work such as Client C.
2. Store the suite and password-manager recovery codes and a one-page emergency sheet in a sealed envelope held by the owner's attorney.
3. The emergency sheet tells the attorney to call Client A and Client B within 24 hours, so Client A can seek a replacement consultant and both clients can direct the return or destruction of their material (CSCA-A (8)).
4. List in the sheet where CEII is kept and that FERC's CEII Coordinator must be told if it cannot be returned or destroyed.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Mobile phone | Authenticator app; client MFA prompts; calls; field photos | BP-01, BP-02 |
| SYS-01 Email and file suite | Correspondence, project folders, version history | BP-01, BP-03, BP-05 |
| SYS-02 Engineering laptop | Analysis software, drafts, CEII archive, signing certificate | BP-03, BP-05 |
| SYS-04 Field tablet | Inspection checklists and photos; spare device for email | BP-02, BP-01 |
| SYS-06 Client-operated access | Client A portal and gateway; Client B platform | BP-01, BP-03 |
| SYS-07 Home network | Internet for the home office; phone hotspot is the fallback | BP-01, BP-03 |
| SYS-05 Accounting SaaS | Invoices and bank feed | BP-04 |
| USB backup drive | Monthly copy of the laptop (unencrypted; never restored) | BP-03 |
| People and services | Owner-engineer; field assistant (field days only); on-call IT technician; tax accountant | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and authenticator app | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the home office | 1 h | Phone hotspot |
| 3 | SYS-01 email and file suite from a clean device | 4 h | Tablet as the spare device |
| 4 | Client contact for any open incident notice | 4 h | Printed client contact sheet; phone calls |
| 5 | A clean engineering laptop with analysis software | 48 h | Reinstall from vendor portals; restore project folders from the suite |
| 6 | Client A portal and gateway access | Set by Client A | Client A re-enables the account after its own checks |
| 7 | SYS-05 accounting SaaS | 72 h | Bank portal; manual invoices |
