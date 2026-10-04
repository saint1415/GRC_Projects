# SOC 2 Readiness Self-Check: Cris Santos Company | Educational Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| Tier / Vertical | Sole Proprietorship / Educational Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. A self-check and a self-attestation, not a SOC 2 examination |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the client-management SaaS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-07-15 (Part B) and 2026-07-17 (Part A) by the owner-tutor with the IT technician; adopted 2026-07-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person tutoring business would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This business teaches children for their families. No business customer relies on its systems, and a CPA examination would cost more than a month of revenue. Families, and the occasional school or library that refers students, ask about safety and privacy; they accept a **self-attestation**, which this checklist supports. The Educational Services profile names no other assurance alternative for a business of this size.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Two criteria assume a board or staff and are marked N/A; four are satisfied by the owner's direct oversight; the reason is written in the checklist.
- **B. Reading the client-management SaaS vendor's SOC 2 report.** That vendor holds the schedule, parent contacts, session notes, and billing, and runs most of the inherited controls (P02, P04). The owner uses the same CC criteria as a checklist when reading its report every year (POL-01 6.3), and checks the written assurances 16 CFR 312.8(c) requires.

## 2. System description (scope)
- **Services:** one-to-one tutoring, SAT and ACT preparation, and study-skills coaching for about 55 active students; no services to other businesses.
- **Infrastructure and software:** the Core Business SaaS Stack (P02): five SaaS services, one laptop, one phone, the home network, and a consumer AI assistant (use narrowed in P10).
- **People:** the owner-tutor; the on-call IT technician under a signed agreement.
- **Data:** children's personal information collected through the portal and sessions; student records parents provide; parent contacts; billing records.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 18 | 5 | 2 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board) and CC2.2 (no internal workforce). CC8.1 is **not** N/A here, unlike a business with no online service: the owner changes portal features, and one change (reading audio) went live without a risk check or parent notice.
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses with an outside review at least every second year.
**Not ready:** CC2.3 (no privacy notice to parents), CC6.1 (no MFA on three services; laptop unencrypted), CC6.7 (open links, SMS, photo sync, AI assistant), CC7.2 (no monitoring), and CC9.2 (three vendors with children's information and no written assurances). All five map to open POA&M items or dated actions in P07 and P01.
**Privacy criteria are out of scope** because children's privacy is measured against the COPPA Rule in P03, which is the legal standard that applies.

## 4. Client-management SaaS vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One exception (late removal of departing vendor staff), remediated.
- **Availability:** the vendor's stated RPO of 1 hour meets the BIA. Its RTO of 12 hours is longer than BP-02's 8-hour RTO but inside the 24-hour MTD; the printed weekly schedule covers the gap (P01 R-014, accepted).
- **Children's data commitments:** the vendor's data processing addendum gives the written assurances 16 CFR 312.8(c) requires. It is the only vendor that does today.
- **Controls the business must run (CUECs):** protect MFA devices, remove users and parent logins no longer needed, set permissions, review activity, and report suspected compromise. Activity review is an open gap (POL-01 7.7), so **the vendor's logging protects the business only once the owner reviews it.**
- **Follow-ups:** bridge letter by 2026-10-31; ask for a fixed incident notice period at renewal.

## 5. Remediation plan and evidence calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-08-17 (before the fall term) | CC2.3, CC5.2, CC6.1, CC6.2, CC6.3, CC6.4, CC6.6, CC6.8, CC8.1 | Notice screenshots and consent records; MFA and encryption screenshots; closed-account list; family account setup |
| By 2026-09-30 | CC2.1, CC6.5, CC6.7, CC7.2, CC7.3, CC7.4, CC7.5, CC9.2 | Disposal log; monthly review log; walkthrough notes; backup restore test; vendor assurances |
| By 2026-12-31 | CC1.4 (course by 2026-10-31), CC3.4, CC9.1 | Course certificate; change log; emergency sheet and backup-tutor agreement |
| By 2027-07-31 | CC3.3, CC4.1, CC7.1 | Updated register; outside review |

**Self-attestation for families and referral partners:** a one-page letter from the owner that summarizes this check, the children's privacy notice, and the POA&M, updated each July.
