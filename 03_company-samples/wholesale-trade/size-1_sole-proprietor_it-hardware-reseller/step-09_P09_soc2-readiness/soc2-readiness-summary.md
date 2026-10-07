# SOC 2 Readiness Self-Check: Cris Santos Company | Wholesale Trade | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Tier / Vertical | Sole Proprietorship / Wholesale Trade |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022), criterion IDs only |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Owner's self-check (`soc2-readiness.csv`) |
| Part B | Review of the accounting and inventory SaaS vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-05 (Part B) and 2026-08-07 (Part A) by the owner with the IT consultant; adopted 2026-08-31 |

## 1. Why SOC 2 here, and why not a SOC 2 report
**A one-person reseller would not obtain a SOC 2 report.** SOC 2 reports on a service organization's controls for business customers that rely on its systems. This business sells and stages equipment; no customer relies on its systems to run their own, and a CPA examination would cost more than a year's margin on the DoD channel. The prime's supplier questionnaire accepts a **self-attestation** plus the CMMC Level 1 (Self) status in SPRS, and this checklist supports that letter.

The Security criteria are still useful in two ways:
- **A. Owner's self-check.** The CC series is a structured list of questions. Several criteria assume a board, staff, or a development team, so they are marked N/A or are satisfied by the owner's direct oversight, with the reason written in the checklist.
- **B. Reading the order management vendor's SOC 2 report.** The accounting and inventory SaaS vendor operates most of the inherited controls for SYS-01 (P02, P04). The owner uses the same CC criteria as a checklist when reading that report every year (POL-01 6.6).

## 2. Scope
- **Services:** reselling, staging, and delivering network equipment; no services that run on the business's systems for others.
- **System:** the Reseller Order Desk (P02).
- **People:** the owner; contractors under agreements.
- **Procedures:** POL-01 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 15 | 5 | 3 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**N/A with rationale:** CC1.2 (no board), CC2.2 (no internal workforce), CC8.1 (no software development or infrastructure; vendor change management is inherited).
**Ready through the owner's direct oversight:** CC1.1, CC1.3, CC1.5, and CC4.2. One person sets the tone, holds every role, is accountable for the affirmation, and fixes deficiencies. The limit is independence, which POL-01 4.5 addresses by having the IT consultant check the evidence every year.
**Ready because it was used:** CC7.4. The P08 runbook handled the cloned optics case from detection to customer replacement in 18 days.
**Not ready:** CC6.1 (no MFA on the order management administrator account; reused passwords), CC6.5 (no sanitization), CC6.7 (FCI in open links and an AI assistant), CC7.2 (no activity review), and CC9.2 (no supplier vetting; counterfeit optics found). All five map to open POA&M items or POL-01 rules due by 2026-10-31.

## 4. Order management vendor report (Part B)
- **Opinion:** Type 2, unqualified, Security and Availability, period ending 2026-03-31. One access-removal exception, remediated.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 24 hours **meet the BIA** (RTO 24 h, RPO 24 h for BP-01 and BP-02).
- **Controls the business must run (CUECs):** manage users, enable MFA, protect credentials, review sign-ins and connected apps. MFA is an open gap (POAM-001), so **the vendor's strong platform protects the business only once the owner turns MFA on.**
- **Follow-ups:** bridge letter by 2026-10-31; ask how the vendor monitors the carved-out payment page provider.

## 5. Remediation calendar
| When | Criteria | Evidence to keep |
|---|---|---|
| By 2026-09-30 | CC6.1, CC6.2, CC6.3, CC6.7, CC2.3, CC3.3, CC5.2 | MFA and sharing screenshots; account list; walkthrough notes; call-back log |
| By 2026-10-31 | CC1.4, CC2.1, CC3.4, CC4.1, CC6.4, CC6.5, CC6.6, CC7.1, CC7.2, CC7.3, CC7.5, CC9.2 | Course certificates; wipe records; router and network settings; review log; receiving checklists; backup report |
| By 2026-12-31 | CC9.1 | Emergency sheet; agreement with the prime |

**Self-attestation for the prime:** a one-page letter from the owner that summarizes this check, the CMMC Level 1 (Self) status once entered, and the POA&M, updated each August.
