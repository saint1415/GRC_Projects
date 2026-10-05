# SOC 2 Readiness Self-Check: Cris Santos Company | Chemical | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| Tier / Vertical | Sole Proprietorship / Chemical |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Self-check only; no SOC 2 examination is planned |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the email and file suite provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-11 (Part B) and 2026-09-18 (Part A) by the owner with the IT technician; adopted 2026-10-05 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person brokerage would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This business sells chemicals; no customer relies on its systems to run their own. A CPA examination would cost more than a year's profit. The vertical overlay names no assurance alternative. Two parties do ask about security, and both accept a **self-attestation**:
- The largest customer, a food and beverage processor, sends an annual supplier security questionnaire.
- The hydrogen peroxide producers review distributors under their product stewardship terms. In 2026 the review asks how the distributor prevents fraudulent orders and pickups.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Some criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the email suite provider's SOC 2 report.** The email account is the business's critical system (P02), and the provider runs most of its inherited controls. The owner uses the same CC criteria as a checklist every year (POL-01 6.2).

## 2. Scope
- **Services:** order taking, hazmat shipping papers, pickup authorization, and billing for drop-shipped chemicals; no services to other businesses' systems.
- **System:** the Brokerage Core SaaS Stack (P02).
- **People:** the owner; contracted IT technician; partners under HSP-01.
- **Procedures:** POL-01, HSP-01, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 14 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), and CC8.1 (no software development or infrastructure; the vendors' change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** five criteria.
- CC1.4: HMR training lapsed.
- CC6.1: no MFA on email.
- CC6.3: daily administrator use on a shared laptop.
- CC6.7: release and payment instructions move by unverified email.
- CC7.2: no monitoring of email sign-ins or forwarding rules.

All five map to open POA&M items in P07 or to HSP-01 measures.

## 4. Email suite provider report (Part B)
- **Opinion:** Type 2, unqualified, Security, Availability, and Confidentiality, for the period ending 2026-06-30, with no exceptions. A bridge letter is posted.
- **The report protects the platform, not the account.** The provider's MFA works only if the customer turns it on. Its logs help only if the customer reads them. Its recovery objectives do not cover data the customer deletes or an attacker removes. Three of the five complementary user entity controls were not operated: MFA (POAM-001), log review (POAM-007), and the customer's own backup (POAM-006).
- **Follow-up:** turn on suspicious sign-in alerts to the phone; repeat the review each year.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-10-15 | CC6.1 (email MFA), CC6.2, CC6.3 | MFA and account screenshots |
| By 2026-10-31 | CC2.3, CC6.7 | Supplier acknowledgments of the HSP-01 hold-release and pickup-number rules; printed contacts |
| By 2026-11-30 | CC1.4, CC2.1, CC4.1, CC5.2, CC6.6, CC7.1, CC7.2, CC7.5, CC9.2 | Training records; monthly review log; backup and restore test; router settings; carrier list |
| By 2026-11-15 | CC7.3, CC7.4 | Walkthrough notes |
| By 2026-12-31 | CC6.5, CC9.1 | Disposal record; coverage arrangement; sealed-envelope receipt |

**Self-attestation for the customer questionnaire and the producers' stewardship review:** a one-page letter from the owner that summarizes this check, HSP-01's pickup verification rules, and the POA&M. It is updated each September.
