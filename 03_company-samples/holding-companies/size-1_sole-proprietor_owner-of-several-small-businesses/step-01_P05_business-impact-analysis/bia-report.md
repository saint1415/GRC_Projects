# Business Impact Analysis: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

**Organization:** Cris Santos Company (the owner's management business for three wholly owned LLCs) | **Tier:** Sole Proprietorship (owner only, 0 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, short form
**Prepared by:** Owner-manager, 2026-07-28, with the on-call IT technician | **Adopted:** Owner-manager, 2026-08-31

## 1. Overview and purpose
This one-page BIA lists the five business functions the owner runs for the four entities (the sole proprietorship and its three LLCs), how long each can be down, and how much data each can lose. It supports:
- the availability rating in the system profile (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident runbook (P08);
- the CSF 2.0 outcomes on business continuity in the gap analysis (P03: ID.AM-05, ID.IM-04, RC.RP-01).

## 2. Business description
The owner runs the back office for three small Florida LLCs from a home office: **Storage** (a 180-unit self-storage facility with one part-time manager), **Rentals** (12 residential units in six duplexes), and **Laundry** (a laundromat with wash-and-fold service and two part-time attendants). Everything is SaaS: one productivity suite tenant for email and files, a multi-company accounting service, online banking for four accounts, a payroll service, and one line-of-business system per LLC. The owner holds every administrator account. See `../00_company-facts.md` sections 1 to 3.

## 3. Impact categories and values
Dollar values are scaled to the LLCs' combined revenue of about $750,000 a year (about $2,050 a day), because an outage hurts the LLCs before it hurts the management fees.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $10,000 (about a week of combined revenue, or one redirected payment) | $2,000 to $10,000 | Less than $2,000 |
| Operations | An LLC cannot serve customers or tenants at all | Service slowed or done by hand | Administrative delay only |
| Regulatory | Missed Florida breach notice, FCRA notice, or payroll obligation | Late filing or notice that can be cured | Internal policy deviation |
| Safety | Plausible harm to a tenant or worker | Delayed repair or access, but safe | None |
| Reputation | Loss of tenants or customers to competitors | Complaints or online reviews | None outside the business |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Owner email, files, and records (all four entities) | High | 24 h | 8 h | 24 h |
| BP-02 Storage rentals, gate access, and rent collection | High | 48 h | 24 h | 24 h |
| BP-03 Payments, payroll, and bookkeeping (all four entities) | High | 72 h | 24 h | 24 h |
| BP-04 Laundry operations and wash-and-fold orders | Moderate | 48 h | 24 h | 24 h |
| BP-05 Rentals leasing and rent collection | Moderate | 120 h | 72 h | 24 h |

**What drives the values.** BP-01 comes first even though it earns nothing by itself: the owner's mailbox is the administrator and recovery address for every other system, so no other function can be restored without it. BP-02 is set by the gate: existing codes keep working while the cloud system is down, but new tenants cannot get in and autopay stops. BP-03 is set by payroll (every second Friday) and by payment fraud, where hours matter for a recall. BP-04 has a coin fallback. BP-05 can wait days, because rent is monthly and tenants can pay by check.

**RPO gaps.** The 24-hour RPO for BP-01 is **not supported today**: email and files have no backup beyond the vendor's 30-day deleted-item retention, and the 47 rental application files exist only there (P01 R-008). The RPOs for BP-02 to BP-05 rely on each vendor's own backups, which the owner has confirmed only for the accounting service (its SOC 2 report, P09).

**Single-person dependency (the key finding).** The owner is the only person who can sign in as administrator anywhere, release a payment, issue a gate code remotely, approve an applicant, or answer a vendor's security notice, for four legal entities at once. The second factor for the email account arrives by text message on the owner's one phone. The successor manager named in each LLC operating agreement has the legal authority to step in but no way to reach any system. If the owner is ill, injured, or loses the phone, all five functions pass their MTD within three days. Actions (P01 R-010, due 2026-12-31):
1. Write a one-page access sheet per entity (systems, account names, vendor support numbers, bank contact) and store it with recovery codes in a sealed envelope held by the business attorney, released to the successor manager under the operating agreements.
2. Give the Storage manager written authority and a separate, limited account to run Storage day to day for up to two weeks.
3. Ask the bank how the successor manager can be added as an authorized signer on each LLC account if the owner is incapacitated, and record the answer.
4. Register a second MFA method (a hardware security key kept in the envelope) on the email and banking accounts.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 Productivity suite | Email, files, and identity for all four entities; recovery address for every system | BP-01 to BP-05 |
| SYS-08 Owner laptop and phone | Administrator device; MFA codes; payment approvals | BP-01, BP-03 |
| SYS-02 Accounting service | Four company files; bank feeds | BP-03 |
| SYS-03 Online banking | Four accounts; one-time codes for wires and new payees | BP-03 |
| SYS-04 Payroll service | Storage and Laundry payroll | BP-03 |
| SYS-05 Storage management system | Tenants, gate codes, autopay | BP-02 |
| SYS-07 Laundry POS and payment platform | Machine payments; wash-and-fold orders | BP-04 |
| SYS-06 Property management platform | Applications, screening, leases, rent | BP-05 |
| SYS-09 Site devices and networks | Storage desktop and gate controller; laundromat POS tablet and router | BP-02, BP-04 |
| Contracted services | Bookkeeper (all four entities), IT technician, maintenance contractor | BP-03, BP-05 |
| People | Owner-manager; Storage manager; two Laundry attendants | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Owner identity: phone, email account, MFA | 2 h | Recovery codes in the sealed envelope; replacement phone and SIM from the carrier in person |
| 2 | A clean administrator device | 4 h | Phone app for urgent tasks; laptop reinstalled by the IT technician |
| 3 | SYS-01 email and files (BP-01) | 8 h | Vendor account recovery; paper copies of key contracts |
| 4 | SYS-03 banking and payment hold (BP-03) | 8 h | Call the bank's fraud line; freeze new payees |
| 5 | SYS-05 storage system and gate (BP-02) | 24 h | Gate works on stored codes; manager escorts new tenants |
| 6 | SYS-02 and SYS-04 bookkeeping and payroll (BP-03) | 24 h | Pay staff from the last pay register by bank transfer |
| 7 | SYS-07 laundry payments and POS (BP-04) | 24 h | Coin only; paper order tickets |
| 8 | SYS-06 property management (BP-05) | 72 h | Checks or bank transfers; phone maintenance requests |
