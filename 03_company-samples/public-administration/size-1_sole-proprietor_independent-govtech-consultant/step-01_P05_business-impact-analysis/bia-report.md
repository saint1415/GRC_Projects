# Business Impact Analysis: Cris Santos Company | Public Administration | Sole Proprietorship

**Organization:** Cris Santos Company (independent GovTech consultant) | **Tier:** Sole Proprietorship (owner-consultant only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-consultant, 2026-08-11, with the on-call IT technician (under NDA) | **Adopted:** Owner-consultant, 2026-09-15

## 1. Overview and purpose
This one-page BIA lists the four business functions the consultancy depends on, how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the contingency planning rows (CP family) of the gap analysis (P03), which the county contract requires for contractor devices that store county data;
- the recovery order in the incident runbook (P08).

## 2. Business description
One person configures, builds reports for, and migrates data into case management systems that three Florida agencies run or license: a county (CL-01), a city (CL-02), and a sheriff's office (CL-03). The owner hosts no agency system. The work runs on one laptop, one phone, a business productivity suite, a password manager, and the agencies' own accounts. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $720 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $3,500 (about a week of billings) | $700 to $3,500 | Less than $700 |
| Operations | No agency work can be done | Work slowed or milestones rescheduled | Administrative delay only |
| Regulatory and contract | Agency breach notice, CJIS violation, or missed contract notice clock | Missed contract deadline (deletion, deliverable) | Internal rule broken, no external effect |
| Safety | Not applicable: no function affects anyone's physical safety | | |
| Reputation | Loss of an agency contract or of CJI access | An agency complaint or a poor reference | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Agency incident notices and client communications | High | 24 h | 4 h | 24 h |
| BP-02 Agency project delivery | High | 48 h | 24 h | 8 h |
| BP-03 Agency data handling and return | Moderate | 120 h | 72 h | 24 h |
| BP-04 Invoicing, collections, and business administration | Low | 240 h | 72 h | 24 h |

**What drives the values:** contract clocks drive BP-01, not revenue. If the owner cannot reach the sheriff's LASO within 1 hour or the county within 24 hours of finding an incident, the owner breaks the contract even when no data was lost. BP-02 is driven by booked county migration windows. Its 8-hour RPO **is not supported today** for project scripts, which sit in a local repository with no other copy (P01 R-010). BP-03 looks low on time but high on consequence: losing control of an extract is what triggers agency breach notices.

**Single-person dependency (the key finding).** The owner is the only person who does the work, the only person cleared for CJI, the only person who can tell the agencies about an incident, and the only holder of every credential. Every MFA prompt except the sheriff's token goes to one phone, and no recovery codes are stored. If the owner is ill, injured, or without the phone, BP-01 exceeds its 24-hour MTD and nobody tells the agencies anything. Actions (P01 R-009, due 2026-12-31):
1. Print an **agency contact sheet** (each agency's security contact, its reporting clock, and the contract notice clause) and keep it in the locked file box and with the owner's attorney.
2. Store recovery codes for the productivity suite, password manager, and accounting service in a sealed envelope held by the owner's attorney, with a one-page instruction: call each agency contact on the sheet and say the owner is unavailable. The attorney gets **no** access to agency systems or data.
3. Sign a short backup agreement with a peer independent consultant who can be introduced to agencies for non-CJI work. Any substitute needs each agency's approval, and the sheriff would require its own screening first.
4. Add a second MFA method (a hardware security key) to the productivity suite and the password manager.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Mobile phone | MFA prompts; calls to agencies; email | BP-01, BP-02 |
| SYS-02 Productivity suite | Email, calendar, cloud files and sync folder | BP-01, BP-02, BP-04 |
| SYS-01 Business laptop | Scripts, working files, agency access | BP-02, BP-03 |
| SYS-05 Agency accounts | County single sign-on, city 311 accounts, sheriff virtual desktop and token | BP-02 |
| SYS-04 Password manager | Credentials for every service | BP-01, BP-02, BP-04 |
| SYS-06 Home network | Internet for the home office; phone hotspot is the fallback | BP-01, BP-02 |
| SYS-09 USB backup drive | Monthly copy of the documents folder (unencrypted) | BP-02, BP-03 |
| SYS-07 Accounting SaaS | Invoices and books | BP-04 |
| People | Owner-consultant only; on-call IT technician by the hour | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner reachability: phone, MFA, and the printed agency contact sheet | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier; any phone for calls |
| 2 | Email and calendar (SYS-02) | 2 h | Web access from the phone or any clean device |
| 3 | Internet in the home office | 2 h | Phone hotspot; work from a client office |
| 4 | A clean laptop | 8 h | Buy a replacement the same day; the IT technician sets it up from the build checklist (P08) |
| 5 | Agency access re-established (county single sign-on, city accounts, sheriff virtual desktop client) | 24 h | The sheriff's IT unit registers the new device (about 1 business day); county and city access needs only the browser and MFA |
| 6 | Project files and scripts | 24 h | Sync folder restores automatically; scripts rebuilt from notes until the repository has an off-device copy |
| 7 | Accounting SaaS | 72 h | Invoice later; paper contract copies in the locked file box |
