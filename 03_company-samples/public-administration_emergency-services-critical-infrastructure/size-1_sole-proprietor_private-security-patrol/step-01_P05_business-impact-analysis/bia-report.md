# Business Impact Analysis: Cris Santos Company | Emergency Services | Sole Proprietorship

**Organization:** Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner, 2026-08-11, with the on-call IT technician (under a confidentiality agreement since 2026-08-07) | **Adopted:** Owner, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the patrol depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the contingency section of the information security policy (POL-01, P06);
- the recovery order in the incident runbook (P08).

No regulation requires a contingency plan for this business. The drivers are the client contracts (45-minute alarm response, nightly patrols, reports by 6:30 a.m.) and the licensing duty to produce records to the Department of Agriculture and Consumer Services on request (Fla. Stat. 493.6121(2)).

## 2. Business description
One licensed security officer patrols 7 client properties at night in one marked vehicle and answers alarm calls for 4 of them at any hour. Everything runs on a phone, a laptop at the home office, a body camera, and four SaaS services: the patrol management app (SYS-01, the system of record), a consumer email and file account, and an accounting SaaS. The owner also holds 23 client keys and 6 access cards, and the alarm and gate codes for every client. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual revenue, or about $580 per patrol night.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $5,000 (lost contract or a client's loss charged to the business) | $1,000 to $5,000 (several nights of credits) | Less than $1,000 |
| Operations | No patrols or no alarm response | Patrols run but reports or responses are late | Administrative delay only |
| Regulatory | License discipline under Fla. Stat. 493.6118, or a breach notice under Fla. Stat. 501.171 | Missed contract or record-keeping duty | Internal policy deviation |
| Safety | Plausible harm to people at a client site or to the owner (missed fire, flood, or intrusion) | Delayed but safe response | None |
| Reputation | Loss of a client or of referrals between property managers | Client complaint | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Night patrols and checkpoint reporting | High | 24 h | 8 h | 1 h |
| BP-02 Alarm response and client call-outs | High | 4 h | 1 h | 24 h |
| BP-03 Incident reporting and client communications | Moderate | 24 h | 8 h | 1 h |
| BP-04 Billing and collections | Low | 168 h | 72 h | 24 h |
| BP-05 Licensing, insurance, and records administration | Moderate | 72 h | 24 h | 24 h |

**What drives the values:** safety and the 45-minute contract clause drive BP-02, because an unanswered alarm can mean a fire, a flood, or an intruder on site. The patrol app vendor states an RTO of 8 hours and an RPO of 1 hour in its SOC 2 report (P09), which just meets BP-01 and BP-03; the app's offline mode keeps scans on the phone until it reconnects. The 24-hour RPO for BP-02 applies to the client access code list. **It is not supported today**: the list is a spreadsheet in the consumer cloud drive with no separate backup, so ransomware on the laptop would encrypt it (P01 R-001, R-003). BP-05 is rated Moderate even though it is administrative, because the Department may ask for records at any time and they must be available "immediately" (493.6121(2)).

**Single-person dependency (the key finding).** The owner is the only patrol officer, the only alarm responder, the only person who holds client keys and codes, and the only person with the patrol app, email, and accounting credentials. Patrol work at night carries its own risk of injury. If the owner is hurt, ill, or without the phone, BP-01 and BP-02 exceed their MTD within hours, and nobody else can open a client site or read the codes. Actions (P01 R-007, due 2026-12-31):
1. Turn the verbal arrangement with the backup patrol agency (license confirmed 2026-08-11) into a written coverage agreement with confidentiality terms, and tell each client who the backup is.
2. Keep a sealed paper code book and spare app recovery codes in a locked safe at the home office, with a one-page emergency sheet a trusted family member can hand to the backup agency (POL-01 6.3 and 11.2).
3. Give each alarm monitoring company a second contact (the backup agency) once the agreement is signed.
4. Ask the patrol app vendor how a second admin can be added and limited to a client set, and record the answer.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Mobile phone | Patrol app, alarm calls, client texts, MFA codes, vehicle hotspot | BP-01, BP-02, BP-03 |
| SYS-01 Patrol management app (SaaS) | Checkpoints, GPS, reports, post orders, client portal; vendor backups | BP-01, BP-03, BP-05 |
| Client keys, access cards, and codes | 23 keys, 6 cards or fobs; codes in a spreadsheet and phone note today | BP-02 |
| Patrol vehicle | Marked vehicle; keys carried on one labeled ring | BP-01, BP-02 |
| SYS-02 Email and files | Client email, contracts, the code spreadsheet, video clips (no separate backup) | BP-02, BP-03, BP-05 |
| SYS-04 Laptop | Administration, report review, video copies; shared with a family member | BP-03, BP-04, BP-05 |
| SYS-03 Accounting SaaS | Invoices and payments | BP-04 |
| Outside parties | Patrol app vendor, mobile carrier, alarm monitoring companies, backup patrol agency (verbal), IT technician | BP-01, BP-02, BP-03 |
| People | Owner only | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner reachable by phone with the patrol app working | 1 h | Spare phone kept charged at home with the patrol app installed; replacement SIM from the carrier |
| 2 | Client codes and keys available | 1 h | Sealed paper code book in the home safe (from 2026-09-15); keys on the person or in the vehicle lockbox |
| 3 | SYS-01 patrol app access | 8 h (vendor-hosted) | Paper patrol log and time-stamped phone photos |
| 4 | Email from the phone | 8 h | Calls and texts with no codes or personal information |
| 5 | Records available for the Department | 24 h | Patrol app exports; paper key log |
| 6 | A clean laptop | 72 h | Phone and the vendor web portals; IT technician reinstalls the laptop |
| 7 | SYS-03 accounting SaaS | 72 h | Invoice from the phone; paper invoices |
