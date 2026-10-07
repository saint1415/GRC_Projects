# Business Impact Analysis: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

**Organization:** Cris Santos Company (owner-operated industrial equipment repair service) | **Tier:** Sole Proprietorship (owner-technician only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-technician, 2026-08-24, with the on-call IT consultant (under NDA since 2026-08-20) | **Adopted:** Owner-technician, 2026-09-11

## 1. Overview and purpose
This one-page BIA lists the five business functions the business depends on, how long each can be down, and how much data it can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the CSF 2.0 benchmark outcomes on critical services and recovery (GV.OC-04, RC.RP; P03).

No regulation requires this business to have a BIA. Customer A's exhibit (S4) requires the owner to coordinate incident response with Customer A, which is not possible without knowing what can be restored and how fast.

## 2. Business description
One technician repairs and maintains the electrical controls of production machinery for about 10 business customers in Florida. Three of them build grid equipment: Customer A (distribution transformers), Customer B (power transformers), and Customer C (switchgear). The owner also works at utility substations as Customer A's subcontractor. Everything runs on one service laptop, one phone, a field kit, a business email and file plan, and an accounting SaaS. The most valuable thing the business holds is the **Customer Machine Library**: the control programs for about 70 customer machines. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to about $180,000 in annual receipts, or about $800 per working day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $4,000 (about a week of receipts) or a liability claim | $800 to $4,000 | Less than $800 |
| Operations | A customer production line stays stopped because of the owner | Customer work delayed by a day or more | Administrative delay only |
| Contract (regulatory column) | Breach of Customer A's exhibit or an NDA, or a missed contract notice | Late delivery of a contract record | Internal policy deviation |
| Safety | Plausible equipment damage or operator injury at a customer plant | Machine runs degraded but safe | None |
| Reputation | Loss of Customer A, B, or C | Complaint from a customer | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Breakdown repair calls | High | 24 h | 4 h | 24 h |
| BP-02 Customer machine program custody | High | 24 h | 4 h | 24 h |
| BP-03 Utility substation field work | Moderate | 72 h | 24 h | 24 h |
| BP-04 Quoting, invoicing, and administration | Moderate | 120 h | 72 h | 24 h |
| BP-05 Scheduled preventive maintenance and vibration monitoring | Low | 168 h | 120 h | 168 h |

**What drives the values:** customers' production lines drive BP-01 and BP-02. When a Customer A winding machine loses its program, the line that builds distribution transformers for utilities is down until the owner reloads the right version, so the owner must have a working laptop with the engineering software and a clean library copy within 4 hours. Safety also drives BP-02: loading a wrong or altered program into a drying oven or winding machine can damage the equipment or a transformer coil and endanger operators. BP-03 is scheduled around utility outage windows, so a day of delay is recoverable, but its contract duties are strict (exhibit S4 to S6). **The 4-hour RTO for BP-02 is not supported today:** the library exists only on the laptop and its synced cloud copy, a restore has never been tried, and ransomware would sync encrypted files to the cloud (P01 R-001).

**Single-person dependency (the key finding).** The owner is the only technician, the only person who knows the customers' machines, and the only person who can open the Customer Machine Library, the email account, and the accounting SaaS. The MFA codes are on the owner's one phone. If the owner is ill, injured, or without the phone, every function above exceeds its MTD at once, and customers cannot get their own programs back. Actions (P01 R-008, due 2026-12-31):
1. After each visit, give the customer an encrypted copy of its own current programs. The customers own those programs, and a customer-held copy is the fastest recovery path for everyone.
2. Sign a written referral arrangement with another independent controls technician for breakdown calls when the owner is unavailable.
3. Keep the email and accounting recovery codes and a one-page emergency access sheet in a sealed envelope held by the owner's attorney.
4. Keep a list of the engineering software licenses, installers, and the virtual machine image location, so a replacement laptop can be rebuilt in one day.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Service laptop | Engineering software, the local library, quotes; the only machine that can program customer equipment | BP-01, BP-02, BP-03 |
| SYS-01 Productivity suite | Synced library copy, email, drawings, manuals | BP-01 to BP-04 |
| SYS-04 Phone | MFA codes, customer calls and texts, hotspot | BP-01, BP-03, BP-04 |
| SYS-05 Field connection kit | Cables, adapters, USB sticks for machines without network ports | BP-01, BP-02 |
| SYS-02 Accounting SaaS | Invoices and payments | BP-04 |
| SYS-08 Vibration analytics SaaS | Trend data and fault predictions (trial) | BP-05 |
| Third parties | Automation makers' license servers, productivity suite provider, accounting SaaS provider, bookkeeper, Customer A (gateway and field work) | As listed in `bia.csv` |
| People and facilities | Owner-technician only; service van; home office | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner access: phone and MFA codes | 1 h | Recovery codes in the sealed envelope; replacement phone from the carrier |
| 2 | A clean laptop with the engineering software | 4 h (not supported today) | IT consultant reinstalls from clean media; software license list and virtual machine image (action 4 above) |
| 3 | Customer Machine Library | 4 h (not supported today) | Customer-held copies (action 1); an offline backup that ransomware cannot reach (P01 R-001) |
| 4 | Field connection kit | 4 h | Spare cables in the van; new USB sticks, never reused from an infected laptop |
| 5 | Email and files (SYS-01) | 24 h | Phone email app; 30-day version history |
| 6 | Accounting SaaS (SYS-02) | 72 h | Hand-written tickets; invoice later |
| 7 | Vibration analytics (SYS-08) | 120 h | Handheld readings on paper |
