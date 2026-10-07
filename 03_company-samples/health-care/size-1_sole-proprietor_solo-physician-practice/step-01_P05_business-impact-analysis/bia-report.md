# Business Impact Analysis: Cris Santos Company | Health Care and Social Assistance | Sole Proprietorship

**Organization:** Cris Santos Company (solo primary care physician practice) | **Tier:** Sole Proprietorship (physician-owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Physician-owner, 2026-07-22, with the on-call IT consultant (under BAA) | **Adopted:** Physician-owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the practice depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan standard of the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the applications and data criticality analysis (164.308(a)(7)(ii)(E));
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08).

## 2. Business description
One physician sees about 12 patients a day, 4 days a week, in a leased exam suite in a shared medical office building in Florida. The practice has no employees. The EHR/PM (SYS-01) is vendor SaaS and holds the medical record. Everything else runs on a laptop, a tablet, and a personal phone, plus a consumer email account, a cloud fax service, a billing company, and an answering service. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $900 per clinic day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (about a week of revenue) | $1,000 to $5,000 | Less than $1,000 |
| Operations | No patients can be seen | Visits slowed or partly rescheduled | Administrative delay only |
| Regulatory | Reportable breach or federal program issue | Missed documentation or timeliness requirement | Internal policy deviation |
| Safety | Plausible patient harm (missed allergy, medication, or result) | Delayed but safe care | None |
| Reputation | Loss of payer or referral relationships | Patient complaints or online reviews | None outside the practice |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Patient visits and clinical documentation | High | 24 h | 8 h | 1 h |
| BP-02 E-prescribing and refills | High | 24 h | 8 h | 1 h |
| BP-03 Patient communications | Moderate | 24 h | 8 h | 24 h |
| BP-04 Billing and claims | Moderate | 120 h | 72 h | 24 h |
| BP-05 Practice administration | Low | 120 h | 72 h | 24 h |

**What drives the values:** patient safety drives BP-01 and BP-02, because the physician cannot safely prescribe without the allergy and medication lists. Revenue drives BP-04 less than time suggests, because payers accept late claims within their filing limits. The 1-hour RPO for BP-01 and BP-02 depends on the EHR vendor's backups (confirmed in the vendor's SOC 2 report, P09). The 24-hour RPO for BP-05 is **not supported today**: downloaded files and clinical photos have no backup (P01 R-012).

**Single-person dependency (the key finding).** The physician-owner is the only clinician, the only prescriber, the only administrator, and the only person who holds the EHR, email, and device credentials. The EHR's second factor is on the owner's one phone. If the owner is ill, injured, or without the phone, every function above exceeds its MTD at once, and nobody else can reach patients, the EHR, or the vendors. Actions (P01 R-010, due 2026-12-31):
1. Sign a written coverage arrangement with a nearby physician for urgent patient needs and refills.
2. Store the EHR and email recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney (164.312(a)(2)(ii) emergency access procedure).
3. Give the answering service a script that routes urgent calls to the covering physician.
4. Ask the EHR vendor how a designated person can obtain records access if the owner is incapacitated, and record the answer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 EHR/PM (vendor SaaS) | Medical record, scheduling, portal, e-prescribing; vendor backups | BP-01, BP-02, BP-03, BP-04 |
| SYS-04 Mobile phone | EHR second factor; calls and texts; clinical photos | BP-01, BP-02, BP-03 |
| SYS-03 Laptop and tablet | Access devices; tablet is the spare | BP-01, BP-02, BP-05 |
| SYS-06 Building Wi-Fi | Internet for the suite; phone hotspot is the fallback | BP-01, BP-02, BP-03 |
| SYS-05 Cloud fax | Referrals and records requests | BP-03 |
| SYS-02 Email and files | Correspondence and documents (no backup, no BAA) | BP-03, BP-05 |
| Contracted services | Billing company (BA), answering service (no BAA), IT consultant (BA since 2026-07-17) | BP-03, BP-04 |
| People | Physician-owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and EHR second factor | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | Internet in the suite | 1 h | Phone hotspot |
| 3 | A clean access device | 2 h | Tablet as the spare; laptop reinstalled by the IT consultant |
| 4 | SYS-01 EHR/PM access | 8 h (vendor-hosted) | Paper visit notes and printed next-day schedule |
| 5 | SYS-05 Cloud fax | 8 h | Fax through the EHR if available; phone the referring office |
| 6 | Billing company claims feed | 72 h | Queue charges |
| 7 | SYS-02 Email and files | 72 h | Vendor portals; paper copies |
