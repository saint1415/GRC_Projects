# SOC 2 Readiness Self-Check: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| Tier / Vertical | Sole Proprietorship / Critical Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the productivity suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-26 (Part B) and 2026-08-28 (Part A) by the owner-technician with the IT consultant; adopted 2026-09-11 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person repair business would not obtain a SOC 2 report.** The cost of a CPA examination would be a large share of a year's receipts, and no customer has asked for one. What customers do send is a **supplier security questionnaire**: Customer A's comes each year with its exhibit, and Customers B and C have asked similar questions. The questionnaires follow the same themes as the Security criteria, so this checklist is how the owner answers them honestly and consistently.

The Security criteria are used in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board or staff, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the productivity suite provider's SOC 2 report.** The provider holds the synced Customer Machine Library, email, and drawings. The owner uses the CC criteria as a checklist when reading the provider's report every August (POL-01 6.3).

## 2. Scope
- **Services:** repair and maintenance of production machinery controls for about 10 business customers, and substation cabinet work for Customer A.
- **System:** the Field Service Business Systems (P02).
- **People:** the owner-technician; the IT consultant and bookkeeper as contracted services.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 15 | 7 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce). CC8.1 is **not** N/A here, unlike in most one-person businesses: the owner changes customers' machine programs, and those changes need a version and hash record.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (MFA gaps, administrator account, password spreadsheet), CC6.3 (no least privilege), CC6.5 (old laptop not wiped), CC6.6 (router at Customer B, home network, virtual machine), CC7.2 (no log review), CC7.5 (no backup that ransomware cannot reach), and CC9.2 (no supplier oversight; AI trial without consent). All seven map to open POA&M items in P07.

**Not in scope:** Availability, Confidentiality, Processing Integrity, and Privacy were not assessed. Confidentiality is the next category to add if a customer asks, because customer trade secrets are the main data the business holds.

## 4. Suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-06-30. One access-removal exception at the provider, remediated.
- **Availability:** the provider's platform recovery is tested, but the report does not promise to recover a customer's files after the customer's own device encrypts them. Version history (30 days) restores one file at a time (P07). **The report does not meet the BIA on its own** (BP-02 RTO 4 hours); offline backups are needed (POAM-003).
- **Controls the owner must run (CUECs):** enable MFA (done for the suite), manage sharing permissions (fixed 2026-08-25), protect devices, and keep own backups. The backup CUEC is the open gap.
- **Follow-ups:** bridge letter by 2026-12-31; note the provider's incident notice route in the P08 contacts.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| 2026-09-11 (done) | CC3.4 | POL-01 4.3 change triggers |
| By 2026-09-30 | CC3.3 | Accounting SaaS MFA screenshot; customer bank-details letter |
| By 2026-10-31 | CC2.3, CC5.2, CC6.1, CC6.5, CC6.7, CC6.8, CC7.1, CC7.2, CC7.3, CC7.4, CC9.2 | MFA screenshots; laptop baseline check; disposal record; scan log; review log; walkthrough notes; Customer A consent reply; supplier list |
| By 2026-12-31 | CC1.4, CC2.1, CC6.2, CC6.3, CC6.6, CC7.5, CC8.1 | Course certificates; library index; account review; router decision; restore test record |
| By 2027-06-30 | CC9.1 | Referral arrangement; cyber liability policy |
| By 2027-08-31 | CC4.1 | Second assessment with an outside reviewer |

**Answer to customer questionnaires:** the owner answers from this checklist and attaches the P07 POA&M summary, updated each August. Gaps are stated as gaps with their dates, not as "in place."
