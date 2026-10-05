# Business Impact Analysis: Cris Santos Company | Energy | Sole Proprietorship

**Organization:** Cris Santos Company (pipeline integrity engineering consultant) | **Tier:** Sole Proprietorship (engineer-owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Engineer-owner, 2026-08-11, with the on-call IT support contractor (under NDA) | **Adopted:** Engineer-owner, 2026-09-11

## 1. Overview and purpose
This one-page BIA lists the five business functions the consultancy depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- Client A's supplier questionnaire, which asks how the consultant would keep delivering work after an outage.

No regulation requires this consultant to have a BIA. Client A's addendum asks for backups of work product, and this table sets the targets those backups must meet.

## 2. Business description
One licensed professional engineer works from a home office in Florida for three pipeline operators: an interstate transmission operator that TSA has designated as critical (Client A), an intrastate transmission operator (Client B), and a municipal gas distribution system (Client C). The work is engineering analysis of client data: ILI results, integrity records, GIS data, and SCADA historian exports. Everything runs on a business productivity suite, one laptop, one phone, an accounting SaaS, and client-provided portals. Two 1099 subcontractors help with maps and field data. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $750 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week of revenue) or loss of a client | $1,000 to $5,000 | Less than $1,000 |
| Operations | No client work can be delivered | Deliverables late by days | Administrative delay only |
| Regulatory and contract | SSI released without authorization (49 CFR 1520.9) or a client contract breached | Late notice or record under a contract | Internal deviation only |
| Safety | A client's safety decision is delayed because a finding did not reach it | Analysis delayed but no pending safety decision | None |
| Reputation | A pipeline operator stops using the consultant or warns peers | Client complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Urgent findings to clients | High | 24 h | 4 h | 24 h |
| BP-02 Engineering analysis and deliverables | High | 72 h | 24 h | 24 h |
| BP-03 Client data intake and secure exchange | Moderate | 72 h | 24 h | 24 h |
| BP-04 Invoicing and payments | Moderate | 240 h | 120 h | 24 h |
| BP-05 Business administration and records | Low | 240 h | 120 h | 168 h |

**What drives the values:** BP-01 is the only function with a safety link. When the owner finds an ILI anomaly that appears to need immediate action, the client must hear about it within 1 business day so the operator can decide on pressure reductions under its own integrity program. That function needs only a phone and read access to client data, so its RTO is short and achievable. BP-02 is driven by revenue and by Client A, which is half the business. BP-03 has low downtime impact but **Severe regulatory impact**, because mishandling Client A's SSI breaks 49 CFR 1520.9, which 1520.17 makes grounds for a civil penalty, and breaks the Client A addendum.

**RPO gap.** Files in cloud storage meet the 24-hour RPO through version history (30 days on this plan). Local analysis files and scripts on the laptop do not: they reach the USB drive about once a month, so up to about 30 days of work could be lost (P01 R-001, R-004).

**Single-person dependency (the key finding).** The engineer-owner is the only engineer, the only person with client portal accounts, the only holder of every password, and the only person whose phone answers every MFA prompt. If the owner is ill, injured, or without the phone, BP-01 exceeds its 24-hour MTD on the first day and nobody can tell a client about an urgent finding. Actions (P01 R-010, due 2026-12-31):
1. Agree in writing with a peer pipeline integrity engineer (another sole proprietor) to take urgent client calls and to review an urgent finding if the owner is unavailable. Each client must approve the peer in writing before any client data is shared.
2. Keep the suite, accounting, and password manager recovery codes and a one-page emergency sheet (client contacts, insurer hotline) in a sealed envelope held by the owner's attorney.
3. Tell each client's integrity engineer the escalation path, so an unanswered urgent call goes to the peer.
4. Keep a second MFA method (a hardware security key) registered for the suite and the password manager.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Mobile phone | Calls to clients; every MFA prompt; field photos | BP-01, BP-02, BP-03 |
| SYS-01 Productivity suite | Email, files with version history, calendar | BP-01 to BP-05 |
| SYS-02 Engineering laptop | Analysis software, scripts, local working files | BP-02, BP-03 |
| SYS-06 Client portals | Source data for every project | BP-01, BP-02, BP-03 |
| SYS-04 USB backup drive | Monthly copy of project files (unencrypted) | BP-02 |
| SYS-05 Accounting SaaS | Invoices, payments, W-9s | BP-04 |
| SYS-08 Home office network | Internet; phone hotspot is the fallback | BP-01 to BP-03 |
| Contracted services | GIS and field subcontractors; on-call IT support | BP-02, BP-03 |
| People | Engineer-owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner phone and MFA | 1 h | Replacement phone from the carrier; recovery codes in the sealed envelope |
| 2 | Internet | 1 h | Phone hotspot |
| 3 | Read access to client data (portals) | 4 h | Client portal from any clean device; call the client's integrity engineer |
| 4 | SYS-01 email and files | 8 h (provider-hosted) | Provider web access from a clean device |
| 5 | A clean laptop with the engineering software | 24 h | Replacement laptop; reinstall from vendor media; license transfer through the vendor portal |
| 6 | Local analysis files and scripts | 24 h | Restore from cloud version history; USB drive only if clean |
| 7 | SYS-05 accounting SaaS | 120 h | Manual invoices from a template |
