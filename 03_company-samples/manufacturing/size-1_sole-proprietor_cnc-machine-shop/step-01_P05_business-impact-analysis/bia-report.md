# Business Impact Analysis: Cris Santos Company | Manufacturing | Sole Proprietorship

**Organization:** Cris Santos Company (owner-operated CNC machine shop) | **Tier:** Sole Proprietorship (owner-machinist only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-machinist, 2026-08-11, with the on-call IT technician (under NDA since 2026-08-07) | **Adopted:** Owner-machinist, 2026-09-04

## 1. Overview and purpose
This one-page BIA lists the five business functions the shop depends on, how long each can be down, and how much data it can lose. No regulation requires a BIA from this shop. It is done because the medical OEM supplier quality agreements (SQAs) expect the shop to protect quality records and deliver on time, and because the NIST CSF 2.0 benchmark (RC.RP, ID.RA-04) asks for it. It feeds:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the ransomware runbook (P08);
- the contingency section of the consolidated policy (P06, POL-01 section 11).

## 2. Business description
One owner-machinist quotes, programs, machines, inspects, and ships small lots of precision parts in a leased bay in Florida. About 65% of receipts come from three medical device OEMs, 20% from an aerospace supplier on a DoD program, and 15% from local industrial customers. The work runs on the Shop Business Systems (P02): a business email and file plan (SYS-01), an accounting SaaS (SYS-02), one laptop with CAD/CAM software (SYS-03), a phone (SYS-04), two CNC machine controllers (SYS-05), and one flat shop network (SYS-06). See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $3,500 a week.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $7,000 (about two weeks of receipts) | $1,500 to $7,000 | Less than $1,500 |
| Operations | No parts can be made or shipped | New jobs delayed; repeat jobs continue | Administrative delay only |
| Regulatory and contract | Breach of an SQA or PO security term; loss of eligibility for the aerospace award (CMMC Level 1) | Missed customer record or notice requirement | Internal policy deviation |
| Safety | A nonconforming part could reach a medical device, or a bad program could crash a machine near the operator | Rework or scrap, caught before shipping | None |
| Reputation | An OEM or the aerospace customer drops the shop from its approved supplier list | Late-delivery marks on a customer scorecard | None outside the shop |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 CNC programming and machining | High | 72 h | 24 h | 8 h |
| BP-02 Inspection, quality records, and shipping | High | 72 h | 24 h | 24 h |
| BP-03 Quoting and order intake | Moderate | 120 h | 48 h | 24 h |
| BP-04 Invoicing, payments, and purchasing | Moderate | 168 h | 72 h | 24 h |
| BP-05 Shop administration and compliance | Low | 240 h | 120 h | 24 h |

**What drives the values:** receipts and OEM scorecards drive BP-01 and BP-02. The VMC and turning center keep running programs already in controller memory, which is why the MTD is three days and not one. Customers accept a short slip when told early, but three lost production days usually means a missed ship date. The 8-hour RPO for BP-01 (one shift of CAM work) and the 24-hour RPO for BP-02 depend on the productivity suite's sync and its 30-day version history, which has **never been test-restored**, and ransomware on the laptop would sync encrypted files to the cloud (P01 R-001). Until a separate backup exists (POAM-002), these RPOs are **not proven**.

**Integrity matters as much as uptime.** For OEM parts, a program restored from the wrong version is worse than a late part. Any program restored after an incident must be compared with the released copy before it runs (P08; P01 R-006).

**Single-person dependency (the key finding).** The owner-machinist is the only estimator, programmer, machinist, inspector, and administrator, and the only person who holds the email, accounting, laptop, and customer portal credentials. Email MFA codes go to the owner's one phone. If the owner is ill or injured, every function passes its MTD at once and no one can reach customers, systems, or records. Actions (P01 R-009, due 2026-12-31):
1. Write a one-page emergency access sheet (email and accounting recovery codes, where the records are, customer contacts) and keep it sealed with the owner's designated emergency contact.
2. Agree in writing with a nearby machine shop to finish urgent repeat jobs. The agreement must require customer approval first: the OEMs must approve any change of manufacturing site, and aerospace drawings (FCI) may go only to a shop that meets FAR 52.204-21.
3. Give each main customer a named backup contact (the emergency contact) who can tell them the shop is down.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Shop laptop | CAD/CAM software, synced Jobs folder, VMC program share | BP-01, BP-02, BP-03, BP-05 |
| SYS-05 CNC controllers | VMC (network) and turning center (USB); programs in controller memory | BP-01 |
| SYS-06 Shop network and internet | Program transfer to the VMC; SaaS access; phone hotspot is the fallback | BP-01, BP-03 |
| SYS-01 Productivity suite | Email, drawings, CAM files, programs, inspection reports; 30-day versions | BP-01, BP-02, BP-03, BP-05 |
| SYS-02 Accounting SaaS | Invoices, payments, bank feed | BP-04 |
| SYS-04 Phone | Email MFA codes; customer calls; hotspot | BP-03, BP-04 |
| SYS-07 Customer portals | POs, drawing packages, first article uploads | BP-02, BP-03 |
| Paper travelers and records cabinet | Source inspection records | BP-02 |
| Contracted services | IT technician, bookkeeper, outside processors, calibration lab, machine service technician | BP-01, BP-02, BP-04 |
| People | Owner-machinist only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and email MFA | 1 h | Recovery codes on the emergency access sheet; replacement phone from the carrier |
| 2 | Machines running from controller memory | Immediate | Keep running released repeat jobs; do not load new programs until the source is known clean |
| 3 | A clean laptop with CAD/CAM | 24 h | IT technician reinstalls from clean media; CAM license re-activated with the vendor |
| 4 | Jobs folder restored and released programs verified | 24 h | Restore from the separate backup (planned) or file versions; compare each program with the released copy |
| 5 | Inspection records and certificates | 24 h | Paper travelers are the source; retype certificates |
| 6 | Quoting and customer portals | 48 h | Download from portals on the phone; quote by phone |
| 7 | Accounting SaaS | 72 h | Paper invoices; phone verification of any bank change |
