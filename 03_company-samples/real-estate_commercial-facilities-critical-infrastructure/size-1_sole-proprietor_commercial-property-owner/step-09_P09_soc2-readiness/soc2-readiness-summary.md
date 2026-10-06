# SOC 2 Readiness Self-Check: Cris Santos Company | Commercial Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Tier / Vertical | Sole Proprietorship / Commercial Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the access control vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-23 (Part B) and 2026-07-24 (Part A) by the owner with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-building landlord would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. The owner leases space; tenants rely on the building, not on the owner's IT. A CPA examination would cost more than a year's profit from a suite. In 2026 the insurance agency tenant asked how the building protects its employees' credential data. A **one-page security letter** from the owner, based on this checklist and the POA&M, answers that kind of question.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Criteria that assume a board or staff are marked N/A or are met by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the access control vendor's SOC 2 report.** The vendor operates the platform that decides who can open the building's doors (P02, P04). The owner uses the CC criteria as a checklist when reading its report every year (POL-01 6.4). The camera and thermostat vendors offered no assurance report for their small-business plans; that is noted in the vendor list.

## 2. Scope
- **Services:** leasing and operating one 8-tenant building; no services to other businesses' systems.
- **System:** the Property Systems Profile (P02).
- **People:** the owner; contractors under security terms (from 2026-10-31).
- **Procedures:** POL-01, the P08 runbook, and the P05 manual procedures.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 15 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce). CC8.1 is **not** N/A here, even though the owner develops no software: the owner and two contractors change door schedules, devices, and camera features, and those changes went unrecorded (Partially ready).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC6.1 (no MFA on the building portals; browser-saved passwords; default router password), CC6.3 (installer standing access and stale credentials), CC6.5 (no disposal rule for guarantor files), CC7.2 (no monitoring), and CC9.2 (contractors with building access and no terms). All five map to open POA&M items in P07 or treatments in P01.

## 4. Access control vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12-month period ending 2026-04-30. One exception (late removal of departing vendor employees' access), remediated.
- **Availability:** a 99.9% platform availability target, and door controllers that run on cached credentials during an outage, **meet the BIA** for BP-01 (RTO 8 h).
- **What the report cannot cover:** an attacker signed in with the owner's password. The vendor's controls work as designed when someone with valid credentials unlocks a door. That is why the complementary user entity controls matter.
- **Controls the owner must run (CUECs):** manage administrator users and credentials, enable MFA, review the administrator audit log, protect the controllers physically, keep firmware updates on, and report suspected compromise. Three are open gaps (POAM-001, POAM-005, POAM-009), so **the vendor's security protects the building only once the owner does these.**
- **Follow-ups:** bridge letter by 2026-10-31; ask for a stated incident notice time at renewal.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.7, CC7.1, CC7.3, CC7.4 | MFA screenshots; password manager in use; router firmware page; walkthrough notes |
| By 2026-10-31 | CC2.1, CC2.3, CC6.2, CC6.3, CC6.5, CC7.2, CC8.1, CC9.2 | Signed contractor terms; credential review log; disposal record; monthly review log; change log |
| By 2026-12-31 | CC1.4 (course by 2026-11-30), CC3.4, CC5.2, CC6.6, CC7.5, CC9.1 | Course certificate; router replacement record; backup restore; manual procedures |
| By 2027-07-31 | CC4.1 | Outside reviewer's notes |

**Security letter for tenants:** one page from the owner summarizing this check and the POA&M status, updated each July. It describes what is in place and what is in progress, and makes no claim of SOC 2 compliance.
