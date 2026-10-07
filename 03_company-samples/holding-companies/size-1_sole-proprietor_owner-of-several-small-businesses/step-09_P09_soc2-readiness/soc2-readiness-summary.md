# SOC 2 Readiness Self-Check: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (the owner's management business for three wholly owned LLCs) |
| Tier / Vertical | Sole Proprietorship / Management of Companies and Enterprises |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the accounting service's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-29 (Part B) and 2026-07-31 (Part A) by the owner-manager with the IT technician; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**This business would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for its customers. The sole proprietorship provides back-office services, but only to the three LLCs the owner already owns; no outside customer relies on its systems, and a CPA examination would cost more than a year of management fees. Tenants, customers, the bank, and the processors have never asked for one.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions about the shared back office. Some criteria assume a board or a development team, so they are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the accounting service's SOC 2 report.** The accounting service holds the books of all four entities and is the closest thing the business has to an ERP. The owner uses the CC criteria as a checklist when reading its report every year (POL-01 6.5).

## 2. Scope
- **Services:** back-office management for Storage, Rentals, and Laundry; no services to outside businesses.
- **System:** the Shared Back-Office Platform (P02).
- **People:** the owner-manager; three LLC staff; the bookkeeper and the IT technician.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 9 | 17 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board; each LLC is single-member and owner-managed) and CC8.1 (no software development or infrastructure; vendor change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role for every entity, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Different from a solo business with no staff:** CC2.2 applies here, because three LLC employees work at the sites and had never been told what to do with a suspicious email or a shared PIN.
**Not ready:** CC6.1 (one phishable account administers everything; no MFA on two LLC systems), CC6.3 (stale, shared, and excess access), CC7.2 (no monitoring), CC7.5 (no independent copy of mail and files), and CC9.2 (no vendor oversight). All five map to open POA&M items in P07.

## 4. Accounting service report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, period ending 2026-03-31. One deprovisioning exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 12 hours and RPO of 1 hour **meet the BIA** for payments and bookkeeping (BP-03: RTO 24 h, RPO 24 h).
- **Controls the owner must run (CUECs):** grant roles and remove users promptly, review access, protect MFA devices, review the audit trail, confirm bank-feed connections, and report suspected compromise. Two are open gaps: the bookkeeper's role is broader than needed (POAM-004) and nobody reviews the audit trail for payee changes (POAM-008). **The vendor's controls protect the four company files only once the owner runs these.**
- **Follow-ups:** bridge letter by 2026-10-31; ask how the vendor monitors the carved-out bank-feed provider; ask for a stated incident notice period.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.2, CC6.4, CC2.2, CC2.3, CC7.3, CC7.4 | MFA and password manager screenshots; hire and departure checklist; staff notice; printed contacts; walkthrough notes |
| By 2026-10-31 | CC2.1, CC3.4, CC5.2, CC6.3, CC6.5, CC6.6, CC6.7, CC7.2, CC7.5, CC9.2 | Bookkeeper role change; deletion record; guest network setting; monthly review log; restore test; signed bookkeeper terms |
| By 2026-12-31 | CC1.4 and CC1.5 (by 2026-11-30), CC9.1 | Course certificate and briefing sheet; staff duties; sealed envelope receipt; insurance quotes |
| By 2027-07-31 | CC4.1, CC7.1 | Outside reviewer's notes; IT technician's router and gate firmware check |

**If an outside party asks:** a one-page letter from the owner that summarizes this check and the POA&M, updated each July, is the right response at this size.
