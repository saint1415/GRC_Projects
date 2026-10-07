# Business Impact Analysis: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

**Organization:** Cris Santos Company (engineering subcontractor handling CUI drawings) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-07-14 | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system security plan (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the incident response capability that SP 800-171 3.6.1 requires ("preparation, detection, analysis, containment, recovery") and the 72-hour DoD reporting duty in DFARS 252.204-7012(c).

## 2. Business description
One engineer works from a home office in Florida. About 70% of the work is for Prime A, a defense prime contractor, and all of it involves CUI drawings and models. The rest is commercial design work. Everything runs on one laptop with desktop CAD, a personal phone, the home network, a commercial productivity suite, an accounting SaaS, and Prime A's file-exchange portal. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of revenue) | $700 to $3,500 | Less than $700 |
| Operations | No CUI work can be done | Work slowed or deliverables rescheduled | Administrative delay only |
| Regulatory | Missed 72-hour DoD report, inaccurate SPRS score or affirmation, or loss of CMMC eligibility | Late deliverable under subcontract terms | Internal rule not followed |
| Safety | Not rated: no physical operations. Design errors are a quality risk handled by Prime A's checking, not a downtime impact | | |
| Reputation | Prime A stops issuing task orders | Customer complaint or rescheduled review | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Defense design engineering for Prime A | High | 120 h | 48 h | 8 h |
| BP-02 CUI exchange and design reviews with Prime A | High | 72 h | 24 h | 24 h |
| BP-05 Contract compliance and DoD incident reporting | Moderate | 72 h | 24 h | 24 h |
| BP-03 Commercial engineering work | Moderate | 120 h | 72 h | 24 h |
| BP-04 Invoicing and accounting | Low | 240 h | 120 h | 24 h |

**What drives the values:** Prime A design review dates drive BP-01 and BP-02. The 48-hour RTO for BP-01 is set by the CAD license transfer: the licenses are node-locked to the laptop, and moving them to a replacement takes the vendor 1 to 2 business days. The 8-hour RPO depends on the cloud folder's version history, because the weekly USB backup alone would lose up to a week of work. BP-05 has a 72-hour MTD because DFARS 252.204-7012(c) requires a cyber incident report within 72 hours of discovery. **That RTO is not supported today:** the owner has no DoD-approved medium assurance certificate (P01 R-006).

**Single-person dependency (the key finding).** The owner is the only engineer, the only person authorized to handle the CUI, the only holder of every credential, and the Affirming Official. The MFA app is on the owner's one phone. If the owner is ill, injured, or without the phone, every function above exceeds its MTD at once, and the CUI cannot simply be handed to someone else: only a person and system that meet DFARS 252.204-7012 may receive it. Actions (P01 R-013, due 2026-12-31):
1. Agree in writing with Prime A's subcontract administrator how task orders will be paused or reassigned if the owner is unavailable for more than a week.
2. Store MFA recovery codes and a one-page emergency access sheet (no passwords to CUI systems) in a sealed envelope in a home safe, with instructions for the spouse to call Prime A and the IT consultant.
3. Buy a spare hardware security key for SYS-10 when it goes live, so the phone is not the only second factor.
4. Ask the CAD vendor in writing how fast a license can move to a replacement laptop, and keep the answer with this BIA.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Engineering laptop | Only device allowed to process CUI; desktop CAD; encrypted disk | BP-01, BP-02, BP-03, BP-05 |
| SYS-03 Mobile phone | MFA app; calls; hotspot | BP-01, BP-02, BP-05 |
| SYS-04 Home network | Internet for the home office; phone hotspot is the fallback | BP-01, BP-02, BP-03 |
| SYS-01 Productivity suite (SYS-10 after migration) | Email and synced project files with version history | BP-01, BP-02, BP-03, BP-05 |
| SYS-06 Prime A portal | CUI exchange (Prime A's system) | BP-02 |
| SYS-07 USB backup drive | Weekly laptop backup (unencrypted today) | BP-01, BP-03 |
| SYS-05 Accounting SaaS | Invoices and task order records (FCI) | BP-04 |
| Outside parties | Prime A; CAD software vendor; internet service provider; IT consultant | All |
| People | Owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA app | 2 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the home office | 1 h | Phone hotspot |
| 3 | A clean, encrypted engineering laptop | 48 h | Same-day replacement laptop; IT consultant rebuilds it; CAD license transfer from the vendor |
| 4 | Project files (SYS-01 today, SYS-10 after migration) | 8 h after a clean laptop | Restore from version history; USB backup as last resort |
| 5 | Prime A portal access | 8 h | Prime A portal support resets the account |
| 6 | Email | 24 h | Phone calls to Prime A engineers (no CUI by phone or text) |
| 7 | Accounting SaaS | 120 h | Invoice later; Prime A pays on 30-day terms |
