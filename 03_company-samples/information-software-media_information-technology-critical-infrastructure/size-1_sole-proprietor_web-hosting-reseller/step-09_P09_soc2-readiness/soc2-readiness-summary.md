# SOC 2 Readiness Self-Check: Cris Santos Company | Information Technology | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Tier / Vertical | Sole Proprietorship / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. No SOC 2 examination is planned at this size (section 1) |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the upstream hosting provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-09 (Part B) and 2026-09-10 (Part A) by the owner; adopted 2026-09-28 |

## 1. Why SOC 2 here, and why not a SOC 2 report
A hosting reseller **is** a service organization: about 150 businesses rely on its systems for their websites, mail, and domains. In 2026 the two law firms and the property management company sent security questionnaires. That is the demand a SOC 2 report answers. A SOC 2 examination by a CPA firm would still cost more than the company earns in several months, so it is not planned at about $180,000 a year in revenue. The vertical's other assurance paths (FedRAMP authorization, ISO/IEC 27001 certification) fit even less: there is no federal customer, and certification needs a formal management system.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of the questions customers ask. It also produces a **maintained answer document** for questionnaires (POL-01 12.2), so the owner stops answering from memory. Two 2026 answers were wrong (P03 G-042).
- **B. Reading the upstream provider's SOC 2 report.** The upstream provider operates most of the inherited controls (P02, P04). The report shows which controls the company itself must run, called complementary user entity controls (CUECs). The owner uses the same CC criteria as a checklist each year (POL-01 6.2).

## 2. System description (scope)
- **Services:** shared web hosting, business email, and domain names resold under the company's brand; website care plans for 120 sites.
- **Infrastructure:** none owned. The upstream provider's shared servers in U.S. data centers, plus SaaS tools (P02 section 9).
- **Software:** the customer portal, reseller console, registrar account, site management dashboard, and website security service (SYS-01 to SYS-05).
- **People:** the owner; the freelance web developer with dashboard access; the contract security consultant on call.
- **Data:** customer websites and databases (including about 38,000 shopper accounts), mailboxes, domain contacts, and the credentials that control them.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 19 | 5 | 1 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2, because there is no board. Unlike the solo health care sample, **CC8.1 (change management) is in scope**. The company writes no software, but it changes 120 customer sites every week through bulk updates. Those updates broke 2 sites in July 2026.

**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with outside testing at least every second year. CC1.5 is only partially ready, because the freelance developer holds privileged access with no security duties in writing.

**Not ready:**
- CC2.3: inaccurate public claims and no incident notice commitment;
- CC6.1: no MFA on the portal administrator login or the freelancer's dashboard account;
- CC6.3: the freelancer's administrator role over all 120 sites;
- CC6.7: credentials sent by email, and customer data pasted into a consumer AI tool;
- CC7.2: no log review, and AI-dismissed findings never reviewed.

All five map to open POA&M items in P07 or to P03 actions.

**Availability** is out of scope at this tier, but it is the category customers would ask about next, because of the 99.9% uptime guarantee. Uptime has been measured only since 2026-08 (POL-01 12.4).

## 4. Upstream provider report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, 12 months ending 2026-06-30. One exception: 2 of 40 sampled backup failures were not rerun within 24 hours. The provider fixed this with automatic reruns.
- **What it confirms:**
  - account isolation, encryption of backups and stored data (closes the open question in P02 SC-28 and P07 CP-09d.[01]);
  - U.S. data centers, which substantiates "Your data never leaves the USA" for SYS-02 only;
  - physical controls at the cages, with facility controls carved out to colocation operators.
- **Availability:** a 24-hour RPO and an 8-hour target to restore a failed shared server **meet the BIA** for BP-01. They do not cover an account deleted by an attacker or a provider-wide failure (P01 R-005, R-010).
- **CUECs the company must run:**
  - MFA on the reseller console (met);
  - managing its own sub-users;
  - **patching customer applications** (gap: hosting-only sites, POAM-008);
  - **keeping its own backups** beyond 7 days and outside the account (gap: POAM-005);
  - reporting suspected compromise.

  The provider's report says in writing that the gaps in R-004 and R-005 are the reseller's to close.
- **Follow-ups:** bridge letter by 2026-10-31; ask for a time-bound incident notice to resellers.

## 5. Remediation plan and evidence calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-10-15 | CC5.2, CC6.1, CC6.8 | MFA screenshots for the portal and every dashboard account; AI triage settings |
| By 2026-10-31 | CC1.5, CC2.1, CC2.2, CC6.2, CC6.3, CC7.2, CC8.1 | Signed freelancer addendum; weekly review log; account review record; test-site update log |
| By 2026-11-30 | CC6.5, CC6.7, CC7.3, CC7.4 | Termination records for closed accounts; vault report and spreadsheet deletion; walkthrough notes |
| By 2026-12-31 | CC1.4, CC2.3, CC3.4, CC6.6, CC7.1, CC7.5, CC9.1, CC9.2 | Course certificates; updated Terms of Service; independent backup report; emergency envelope receipt; vendor list |
| By 2027-08-31 | CC3.3, CC4.1 | Fraud scenarios in the risk register; outside test report |

**Answer document for customers:** a short security summary built from this check, the P07 results, and the POA&M, with dates. It replaces answers from memory. The owner sends it, with the corrected 2026 answers, to the three customers who asked, by 2026-10-15, and updates it each September.
