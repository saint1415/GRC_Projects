# SOC 2 Readiness Summary: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-07-01 to 2027-12-31 (6 months), report expected by 2028-02-29; interim SOC 2 Type 1 as of 2027-06-30 |
| Part A | Readiness assessment of Finance's loan servicing and the shared platform that supports it (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-18 by the vCISO and the Security Manager, using P02, P05, P06, and P07 evidence; presented 2026-09-22 |

## 1. Why SOC 2 for this organization
A holding company that serves only its own subsidiaries is usually **not** a SOC 2 service organization. That changed on 2026-08-15, when Finance signed a forward-flow participation agreement with a community bank:
- From 2027-01 the bank will buy participations in new Finance loans, and **Finance will service those loans for the bank** (payment collection, posting, borrower contact, reporting).
- Servicing runs on the loan servicing vendor's platform (SYS-14) and on the **Shared Corporate Services Platform**: identity, email and files, the SFTP server that carries ACH collection files, the treasury system, and the reporting warehouse.
- The bank's third-party risk program requires a SOC 2 Type 2 report covering Finance's servicing and the shared platform, and asked for **Security, Availability, Processing Integrity, and Confidentiality**. Processing Integrity matters because the bank relies on accurate posting and participation reports.

For those services, Finance and the holding company together are a service organization, and a SOC 2 Type 2 report is the right assurance tool.

**SOC 1 is separate.** The bank also asked for a SOC 1 Type 2 report on servicing controls relevant to its financial reporting (cash application, investor reporting). That report uses a different standard and is planned separately; this readiness assessment does not cover it, though many of the IT general controls overlap.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access lifecycle, monitoring of the servicing system, change management, and recovery. Starting the observation period before those are fixed would produce exceptions. The plan is to remediate through 2027 Q2, issue a Type 1 report as of 2027-06-30, then run a 6-month observation period from 2027-07-01. The bank accepted this plan with monthly status updates; its agreement requires the Type 2 report by 2028-03-31.

**Alternatives considered:**
- **Bank's own questionnaire and on-site review only:** the bank's policy requires an independent report for servicers above its materiality threshold.
- **ISO/IEC 27001 certification:** not requested, and it does not cover Processing Integrity.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is neither the co-sourced internal audit firm (which performed P07) nor the group's financial statement auditor.

**Privacy was considered and left out.** The bank did not request it, and Finance's consumer privacy notices and practices are managed in its own compliance program. The group will reconsider Privacy for the second report period.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Loan servicing provided by Finance to the bank partner for participated loans: payment collection by ACH and phone, posting, borrower service, payoff quotes, and participation reporting |
| Infrastructure | SCSP components that support servicing: identity (SYS-02), suite (SYS-03), cloud landing zone with the SFTP server and warehouse (SYS-04), treasury system and bank portals (SYS-06), HQ endpoints and network (SYS-08, SYS-09 at HQ), security operations (SYS-11) |
| Software | Loan origination and servicing system (SYS-14, vendor SaaS); ERP for the loan general ledger feed |
| People | Finance servicing staff (12), Finance President and Compliance Officer, treasury team, shared IT and security team, MSSP, vCISO |
| Data | Borrower customer information for participated loans; ACH files; participation reports |
| Procedures | POL-01 to POL-05, the standards index, servicing procedures, and the P08 runbooks |
| Subservice organizations (carve-out) | Loan servicing vendor, cloud provider, identity vendor, suite provider, MSSP, ERP vendor, treasury system vendor, operating banks. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls in the system description |
| Excluded | Supply, Home Services, and Fabrication operations and sites; the plant; Home Services North. They share the directory, so directory weaknesses are still in scope |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 17 | 6 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 0 | 5 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **24** | **8** | **18** |

**Ready (11):**
- governance and risk: CC1.1, CC3.1, CC3.2, CC4.1, CC4.2, CC5.1;
- access and protection: CC6.2, CC6.4, CC6.7, CC6.8;
- capacity: A1.1.

**Not ready (8):**
- CC3.4: the acquisition and the AI rollout were not assessed as significant changes;
- CC6.3: late terminations, transfers keeping access, 19 Finance export users, no quarterly reviews;
- CC7.2: the servicing system and warehouse, the core of the scope, send no logs to the SIEM;
- CC7.5 and A1.3: recovery of identity and on-premises systems is untested;
- CC8.1: 7 of 25 changes without approval;
- CC9.2: 14 of 22 critical vendors unreviewed;
- C1.2: Finance customer information is never disposed of.

Each maps to a P07 POA&M item. All 5 Processing Integrity criteria are Partially ready: daily posting reconciliations exist, but the ACH file integrity check (P01 R-050) and the participation reports are not built yet.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | PI1.2 (ACH integrity check), CC3.3, CC1.3, CC2.1, CC2.2, CC3.4, CC6.5, CC7.2 (servicing logs), CC8.1, CC7.3, PI1.4 (participation reports built and tested), C1.1 | Hash and control-total records; forum minutes; change tickets with approval; SIEM use cases for servicing exports; data map; disposal tracking records |
| 2027 Q1 | CC6.1, CC6.3, CC6.6, CC7.1, CC7.4, CC7.5, A1.2, A1.3, CC9.1, CC9.2, CC5.2, CC5.3, CC2.3, PI1.1, PI1.3, PI1.5, C1.2, CC1.4, CC1.5 | Quarterly access review sign-offs; FIDO2 rollout records; scan and patch reports; tabletop reports; forest recovery and restore test records; vendor reviews; standards; purge records |
| 2027-06-30 | Type 1 report as an interim deliverable to the bank | Management's system description and assertion |
| 2027-07-01 to 2027-12-31 | Type 2 observation period | All recurring control evidence (quarterly access reviews, monthly scans, daily reconciliations, restore tests, vendor reviews) |
| 2027 Q2 | CC1.2 (sustained quarterly audit committee reporting) | Minutes for 4 consecutive quarters |

**Status reporting.** The vCISO reports readiness monthly to the CFO and the Finance President, monthly to the bank partner, and quarterly to the audit committee (P01 R-042).

## 5. Vendor SOC 2 review program (Part B)
The shared platform relies on vendor controls for many inherited controls (P02: 10 Common/Inherited and 35 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03). It also serves Finance's duty to periodically assess its service providers (16 CFR 314.4(f)(3)) and the plan's oversight of its business associates.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1 (critical)** | Restricted data at scale (Finance customer information, plan PHI, employee SSNs), privileged access to group systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent report) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to group controls, availability against the BIA, and incident notice terms | Annually |
| **Tier 2** | Limited Restricted data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No Restricted data and no system access | Contract terms only | At renewal |

Of about 160 vendors with access to group systems or data, 22 are Tier 1. The CSV holds the 8 Tier 1 reviews completed by 2026-09. The other 14 are due by 2027-03-31 (POAM-013), starting with the plan TPA and PBM (P01 R-051), the distribution system vendor (no SOC 2; contract RTO 24 hours does not meet the BIA, P05 finding 3), the field-service vendors, the AI voice agent vendor, and the recruiting software vendor (P10).

**Key findings:**
1. **Treasury system vendor: qualified opinion.** Privileged database access was not reviewed for 2 quarters (CC6.1). The bridge letter confirms reviews resumed in 2026-05, and bank-enforced dual approval and positive pay are the group's compensating controls. The Treasurer reviews the next report early (2027-03-31).
2. **Loan servicing vendor:** unqualified Type 2 covering all four requested categories, and its recovery commitments (RTO 8 hours, RPO 1 hour) meet the BIA for collections. But two of its CUECs are open group gaps (export rights and activity review), so **the vendor's controls only protect borrower data once those close.** Model governance for the credit scorecard is outside the report (P10 AI-002).
3. **ERP vendor:** unqualified, and its RTO of 12 hours and RPO of 1 hour meet the BIA. Two CUECs (access review, change report review) are open group gaps.
4. **MSSP:** unqualified Type 2 (Security only) with 2 escalation exceptions. The SIEM platform is carved out; its own SOC 2 must be obtained (P01 R-021). Log source coverage is the group's CUEC and is incomplete.
5. **Identity provider and suite provider:** unqualified. The CUECs the group must run (administrator roles, MFA policy, sharing settings, labels) are exactly where P07 found the largest gaps.
