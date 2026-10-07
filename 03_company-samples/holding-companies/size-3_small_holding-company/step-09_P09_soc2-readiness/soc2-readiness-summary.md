# SOC 2 Readiness Summary: Cris Santos Company | Management of Companies and Enterprises | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries) |
| Tier / Vertical | Small / Management of Companies and Enterprises |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Internal self-benchmark; no CPA examination planned |
| Part A | Security-only self-benchmark of the Shared Corporate Services Platform (`soc2-readiness.csv`) |
| Part B | ERP vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-18 by the IT Manager |

## 1. Why SOC 2 for this organization
SOC 2 reports on controls at a *service organization*: a company whose services to other businesses affect those businesses' information. **The holding company is not a service organization in that sense.** It provides shared IT, HR, payroll, and accounting only to its own subsidiaries, under an intercompany services agreement, and it sells nothing to outside customers. No lender, customer, or regulator has asked the group for a SOC 2 report, and a CPA examination would cost far more than it would return.

The Trust Services Criteria are still useful here for two reasons.

**A. Security self-benchmark of the shared platform.** Each subsidiary relies on the holding company the way a customer relies on a service provider. For Finance this is a legal relationship: the holding company is Finance's service provider under the Safeguards Rule (16 CFR 314.2(r)), and Finance must periodically assess it (314.4(f)(3)). Scoring the shared platform against the Security criteria gives Finance's Board of Managers a familiar, structured view of the provider it depends on, and it reuses the evidence already gathered in P02, P06, and P07. Only Security is in scope. The subsidiaries' availability and confidentiality expectations are already set by the BIA (P05) and POL-04, so scoring A1 and C1 would repeat that work.

**B. Third-party risk management.** The shared platform depends on SaaS vendors for most inherited controls (P02, P04). Their SOC 2 reports are the evidence for those controls. The ERP vendor's report is reviewed first because the ERP is the system of record for all four companies. The loan servicing vendor's report, which matters most for Finance customer information, is due for review by 2026-11-30.

**Alternatives considered:** a CPA-issued SOC 2 Type 2 (no one is asking, and controls have not operated long enough), an ISO/IEC 27001 certification (disproportionate for 60 people), and the vertical overlay names no sector-specific alternative. The CSF 2.0 group profile (P03) is the group's main benchmark; this checklist complements it.

## 2. System description (scope)
- **Services:** shared accounting and consolidation, treasury and payments, payroll and HR, email and files, identity, and data integration for the holding company and its three subsidiaries.
- **Infrastructure and software:** the Shared Corporate Services Platform (SSP, P02).
- **People:** the holding company's 14 employees (3 in IT) and the MSP.
- **Data:** financial records, employee personal information, Finance customer information passing through shared email, files, backups, and bank files, and acquisition information.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 22 | 6 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC3.1 and CC3.2: objectives, tolerance, and the 2026 risk assessment
- CC4.2: deficiencies tracked in the POA&M
- CC6.2: manager-approved onboarding
- CC6.4: physical access to network equipment

**Not ready:**
- CC6.3: late terminations, no access reviews, over-broad sharing
- CC7.1 and CC7.2: no vulnerability scanning, log review, or after-hours monitoring
- CC7.5: recovery not demonstrated (the same gap as risk R-004)
- CC8.1: no change management
- CC9.2: vendor risk management

## 4. Findings from the ERP vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-06-30. One exception (late approval of 3 of 40 emergency changes), with a management response.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the group BIA** for payables and the close (P05).
- **Controls the group must run.** The report lists complementary user entity controls: user provisioning and removal, periodic access review, MFA through the customer's identity provider, segregation of duties in role assignment, and review of change reports. **Three are open gaps at the group:** timely removal (POAM-002), access reviews (POAM-001), and change report review (POAM-011). The vendor's controls only protect the group once those are closed.
- **Finance relevance:** the ERP holds no borrower-level data, so this review does not by itself meet Finance's service provider assessment. The loan servicing vendor review does.
- **Follow-ups:**
  - Obtain a bridge letter through 2026-09-30.
  - Confirm the vendor monitors its carved-out cloud hosting provider.
  - Record data location and deletion terms in the supplier inventory.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.2, CC6.1, CC6.3, CC6.7, CC7.3-7.4, CC9.2 | Policy acknowledgments, admin role reports, termination tickets, access review sign-offs, tabletop report, supplier reviews |
| 2027 Q1 | CC6.8, CC7.1-7.2, CC7.5, CC8.1, CC9.1 | Managed detection tickets, scan reports, restore test records, change log, contingency plan |
| 2027 Q2-Q3 | CC1.2, CC1.4, CC3.3, CC4.1 | Board reports, IT training records, updated risk assessment, KPI dashboard |

**Use of this summary:** the Qualified Individual presented it to Finance's Board of Managers on 2026-09-25 as part of Finance's periodic assessment of the holding company as service provider (16 CFR 314.4(f)(3)). It will be refreshed each September.
