# SOC 2 Readiness Self-Check: Cris Santos Company | Information | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Tier / Vertical | Sole Proprietorship / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are cited by ID with short topic labels in our own words |
| Categories in scope | Security (CC1 to CC9) only |
| Part A | Owner's readiness self-check (`soc2-readiness.csv`) |
| Part B | Review of the hosting provider's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-08 to 2026-09-10 by the owner-developer (Part B reviewed 2026-09-09); adopted 2026-09-25 |

## 1. Why SOC 2 here, and why not a SOC 2 report yet
The company **is** a service organization in the SOC 2 sense: about 240 businesses run their bookings on its platform. Two larger subscribers have asked for a SOC 2 report, and the owner has called one "planned". But a CPA examination is a large cost for a business with about $180,000 in revenue, and the self-check below shows that a Type 1 today would report several exceptions. The plan is:
1. **Now:** use this self-check to fix the gaps, and give subscribers an accurate one-page security summary instead of a SOC 2 report. Correct the questionnaire answer document (P03 G-040).
2. **When most Security criteria are Ready** (target: mid-2027, after the POA&M closes) **and revenue supports the fee:** decide on a SOC 2 Type 1 for Security, with Availability added because the website makes an uptime claim.

**Why fewer criteria are N/A than for a medical practice.** The Health Care sole proprietor sample marks change management N/A because the practice writes no software. This company writes and deploys software every week, so CC8.1 is in scope, and only CC1.2 (board oversight) is N/A.

Alternatives named for this vertical (ISO/IEC 27001 certification; FedRAMP authorization) were considered and set aside: the subscribers are small U.S. businesses that do not ask for ISO certification, and there are no federal customers.

## 2. Scope
- **Services:** online booking, calendars, client records, confirmations and reminders, and the Smart Replies beta.
- **System:** the Multi-tenant Booking Platform (P02).
- **Subservice organization:** the hosting provider (carve-out; Part B). The other five sub-processors are listed for review by 2026-12-31.
- **People:** the owner-developer and the support contractor.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1 to CC9, 33 criteria) | 8 | 18 | 6 | 1 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1 to P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board; oversight is the owner's yearly review plus the outside consultant's challenge).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, and CC4.2. One person sets the tone, holds every role, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with outside testing every year. Also Ready: CC3.1, CC3.2, CC5.1, CC5.3, and CC6.4 (inherited from the hosting provider).
**Not ready (6):** CC2.3 (inaccurate public statements and a missed sub-processor notice), CC6.1 (plaintext secrets; two administrator logins without MFA), CC6.3 (shared super-admin), CC6.7 (exports by email, laptop data copy, AI prompts), CC7.2 (no monitoring), and CC9.2 (no sub-processor oversight). All six map to open POA&M items in P07.

**A one-person business and CC8.1.** Change management normally relies on a second person approving each change. That is impossible here. The compensating design is that every change goes through the repository and CI with automated tests, plus isolation and authorization tests that fail the build (due 2027-03-31), plus an outside review of high-risk changes once a standby developer is engaged. A future auditor would test exactly this.

## 4. Hosting provider report (Part B)
- **Opinion:** Type 2, unmodified, Security and Availability, period ending 2026-03-31. One exception (late removal of provider staff access in 2 of 40 samples), remediated.
- **Complementary user entity controls:** the report makes the customer responsible for its own users, tokens, MFA, database network access, backup configuration and restore testing, and audit log review. **Several of these are the company's open gaps** (POAM-001, POAM-002, POAM-004, POAM-005, POAM-007). The provider's controls protect the company only once the owner runs these.
- **Availability:** backups and point-in-time recovery are features the customer configures, not a provider promise. The BIA's 4-hour RTO depends on the owner's restore steps and an outside copy.
- **Follow-ups:** bridge letter; record the provider's incident notice contact in the P08 contact sheet; review the other five sub-processors by 2026-12-31.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-10-31 | CC2.3, CC1.5, CC2.2, CC6.8, CC7.3, CC7.4 | Corrected website and questionnaire; contractor agreement; package-check rule; walkthrough notes |
| By 2026-11-30 | CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC7.2, CC2.1 | MFA screenshots; support role; deletion log; allow list; export links; review log |
| By 2026-12-31 | CC1.4, CC3.4, CC5.2, CC7.1, CC7.5, CC9.1, CC9.2 | Course certificates; outside backup copies; restore steps; sub-processor reviews; emergency kit receipt |
| By 2027-08-31 | CC8.1 (2027-03-31), CC3.3, CC4.1 | Isolation tests; fraud scenarios in P01; second yearly assessment |

**Security summary for subscribers:** a one-page statement from the owner that describes the controls as they actually operate and points to the sub-processor list, updated after each yearly assessment.
