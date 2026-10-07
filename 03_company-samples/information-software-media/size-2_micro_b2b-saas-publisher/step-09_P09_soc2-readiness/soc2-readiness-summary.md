# SOC 2 Readiness Summary: Cris Santos Company | Information | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Micro / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are cited by ID with short topic labels in our own words |
| Categories in scope | Security (CC1 to CC9) and Confidentiality (C1) |
| Target report | SOC 2 **Type 1** as of 2027-03-31, report expected by 2027-05-31; a Type 2 to follow |
| Part A | Readiness self-assessment, criterion by criterion (`soc2-readiness.csv`) |
| Part B | Key vendor assurance reviews (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-31 to 2026-09-04 by the CTO with the Operations and Finance Manager; reviewed by the independent security consultant; approved by the Chief Executive Officer 2026-09-15 |

## 1. Why SOC 2 for this organization
The company is a service organization in the SOC 2 sense: 45 businesses keep their vendors' tax forms and insurance certificates on its platform, and those customers' auditors and security teams need assurance about controls they cannot see. Two mid-market prospects will not sign without a SOC 2 report, and one anchor customer has made a report a condition of its renewal on 2027-06-30. About 30% of revenue rides on the anchor customers (P01 R-023).

**Why a Type 1 first.** A Type 2 tests whether controls operated over a period, usually 6 to 12 months. Most of the company's controls were defined in September 2026 and many are not yet built, so a Type 2 period could not start before 2027. A Type 1 reports on design and implementation at a point in time, which the company can reach by 2027-03-31 and deliver before the renewal date. The Type 2 observation period would then start on 2027-04-01.

**Why Confidentiality and not another category.** Customers' questionnaires focus on how vendors' tax IDs and certificates are protected, used, and deleted. That is the Confidentiality category (C1.1 and C1.2) on top of Security. Availability is not requested: the uptime target has been met (P03 G-041), and the untested recovery is a Security criterion (CC7.5) anyway. Processing Integrity and Privacy were not requested.

**Alternatives named for this vertical were considered.** ISO/IEC 27001 certification is accepted by few of the company's U.S. customers and costs more to reach for a 7-person company. FedRAMP applies only to cloud services sold to federal agencies; the company has none (N51-R07 does not apply).

**How this file relates to P03.** P03 tests the FTC's Section 5 expectations and the company's own statements. This file checks each Trust Services criterion and does not repeat the P03 analysis. Where the same weakness appears in both, both point to the same POA&M item in P07.

**A correction comes first.** Questionnaire answers have said the company is "SOC 2 compliant." It has no SOC 2 report. Corrected answers go to every recipient by 2026-10-15 (P03 G-040). Until the Type 1 report is issued, the company says only that a Type 1 audit is planned for 2027.

## 2. System description (scope)
- **Services:** the Vendor Compliance Platform (VCP): document intake, AI extraction, expiry tracking, compliance status, and reports.
- **Infrastructure and software:** the production cloud account (SYS-01), the repository and CI/CD pipeline (SYS-02), the suite identity service (SYS-03), and error tracking (SYS-05), as defined in the SSP (P02).
- **Subservice organizations (carve-out method):** the cloud provider, the AI model provider, the error tracking service, the email delivery service, and the support desk SaaS. Their controls are covered by the Part B reviews.
- **People:** 7 employees, the contract developer, and the MSP.
- **Data:** customer vendor records and documents (Restricted under POL-04), including about 9,800 Social Security numbers on W-9s.
- **Procedures:** POL-02, POL-03, POL-04 (P06) and the P08 runbook.

**Commitments to describe:** 72-hour incident notice, published sub-processor list with 30 days' notice, deletion within 60 days of termination, use of customer data only to provide the service, and the security exhibit. Two exhibit promises (annual penetration test, 30-day backups) are not true today; they must be made true or the exhibit amended before the report date (P03 G-039).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1 to CC9, 33 criteria) | 6 | 15 | 12 | 0 |
| Confidentiality (C1, 2 criteria) | 0 | 0 | 2 | 0 |
| Availability (A1, 3 criteria) | | | | 3 |
| Processing Integrity (PI1, 5 criteria) | | | | 5 |
| Privacy (P1 to P8, 18 criteria) | | | | 18 |
| **In scope (35 criteria)** | **6** | **15** | **14** | |

**Ready (6):** CC1.3 roles and designations; CC3.2 risk assessment; CC4.1 independent assessment; CC4.2 deficiency tracking; CC5.1 control selection; CC6.4 physical access (inherited from the cloud provider).

**Not ready (14):** CC1.4 training; CC2.1 data inventory and logs; CC2.3 external statements; CC3.3 fraud risk; CC6.1, CC6.2, CC6.3 logical access (the static key, five administrators, no joiner and leaver process); CC6.7 data leaving production; CC7.2 and CC7.3 monitoring and triage; CC7.5 recovery; CC9.2 vendor management; C1.1 and C1.2 confidential data handling and disposal.

**What the numbers say.** The governance criteria are ready because this engagement produced them: a risk assessment, an independent assessment, a POA&M, and named roles. The technical access, monitoring, and data handling criteria are not ready, and they are the ones an auditor tests first for a SaaS company.

### 3.1 Readiness gates (must be in place before the Type 1 date)
| Gate | Criteria | Owner | Due |
|---|---|---|---|
| G1. Statements corrected; approved answer library; exhibit aligned | CC2.3 | Chief Executive Officer | 2026-10-15 (exhibit 2027-01-31) |
| G2. Static CI key retired; federated CI credentials; secrets in the secrets manager | CC6.1 | CTO | 2026-10-15 |
| G3. No production data on laptops; Social Security numbers masked before AI and logs; contractor on a company laptop | CC6.7, C1.1 | CTO | 2026-10-31 |
| G4. Model provider DPA and listing; customer notice; MSP and contractor terms | CC9.2 | Operations and Finance Manager | 2026-10-31 |
| G5. Former customers' data deleted; deletion runbook | C1.2, CC6.5 | Operations and Finance Manager | 2026-10-31 |
| G6. Cloud roles; admin console behind single sign-on; joiner and leaver checklists; first monthly reconciliation | CC6.1, CC6.2, CC6.3 | CTO | 2026-11-30 |
| G7. Data-level logging, threat detection, alerts, and a recorded weekly review | CC7.2, CC7.3 | Senior Software Engineer | 2026-11-30 |
| G8. Backup account, first restore test, contingency plan | CC7.5, CC9.1 | Senior Software Engineer | 2026-12-31 |
| G9. Training delivered; acknowledgments; fraud scenarios; procedures written | CC1.1, CC1.4, CC3.3, CC5.3 | Operations and Finance Manager and CTO | 2026-12-31 |
| G10. Penetration test with findings fixed or tracked; system description drafted | CC4.1, CC3.1 | CTO | 2027-01-31 |

The CTO reports gate status to the Chief Executive Officer at the monthly review. A readiness check with the chosen CPA firm is planned for 2027-02-28. If any of G2, G3, G6, or G7 slips past 2027-01-31, the Chief Executive Officer and the CPA firm decide whether to move the report date, and the anchor customer is told early (R-023).

## 4. Evidence inventory
What the company can show now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register (P01) and assessment results with POA&M (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly review notes (from 2026-09) |
| Cloud provider and model provider report reviews | CC9.2 | Yes (Part B) | Remaining sub-processors (2026-12) |
| Corrected website, product page, and questionnaire answers; approved answer library | CC2.3 | No | 2026-10 |
| Access key report showing no long-lived keys; cloud role export | CC6.1, CC6.3 | No | 2026-10 to 2026-11 |
| Onboarding and offboarding checklists; monthly reconciliation records | CC6.2, CC6.3 | No | Per event and monthly from 2026-11 |
| Weekly log and alert review records | CC7.2 | No | Weekly from 2026-11 |
| Restore test record against the BIA RTO | CC7.5 | No | 2026-10, then twice a year |
| MSP monthly report (encryption, antivirus, patching) | CC6.8, CC7.1 | Yes (July and August 2026) | Monthly |
| Training records | CC1.4 | No | From 2026-10 |
| Deletion certificates for former customers | C1.2 | No | 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11-12 |
| Penetration test report | CC4.1, CC7.1 | No | 2027-01 |

A compliance automation tool (P01 treatment summary) will hold policies and collect much of this evidence from the cloud account and SaaS tools from 2026-11.

## 5. Vendor reviews (Part B)
Four reviews were completed from 2026-09-02 to 2026-09-04; two more are scheduled.

| Result | Vendors |
|---|---|
| SOC 2 Type 2 reviewed, current | V-01 cloud provider, V-02 AI model provider, V-03 error tracking and log management |
| Questionnaire and contract review (no audit report) | V-04 MSP |
| Scheduled by 2026-12-31 | V-05 email delivery, V-06 support desk |

**Key findings:**
- **All three reports have unmodified opinions.** V-02 and V-03 each had one remediated exception that does not affect the company.
- **The company's own gaps defeat the vendors' controls.** Each report lists complementary user entity controls the company must run: protecting keys, managing access, configuring logging and backups, and not sending data that is not needed. Open company gaps affect all three: POAM-002, POAM-004, POAM-005, and POAM-007 on V-01; POAM-004, POAM-010, and POAM-012 on V-02; POAM-012 on V-03.
- **The model provider's report does not cover the zero-retention option** the company plans to rely on. A signed DPA with no-training and zero-retention terms is a P10 condition (due 2026-10-31).
- **The MSP has no audit report.** Its answers confirm MFA on technician accounts but show 2 global administrator accounts, no incident notice term, and no notice when technicians change (POAM-014, R-012).

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4 (by 2026-10-31) | CC2.3, CC6.7, C1.2, CC6.5, CC1.1, CC2.2, CC7.3, CC6.2 | Gates G1 to G5; POAM-004, POAM-011; onboarding checklist; acknowledgments; incident log |
| 2026 Q4 (by 2026-12-31) | CC6.1, CC6.3, CC6.6, CC7.1, CC7.2, CC7.4, CC7.5, CC9.1, CC9.2, C1.1, CC1.4, CC1.2, CC1.5, CC3.3, CC3.4, CC5.3, CC6.8, CC8.1, CC2.1 | Gates G6 to G9; POAM-001 to POAM-003, POAM-005 to POAM-010, POAM-012, POAM-014; tabletop; training; upload scanning |
| 2027 Q1 | CC3.1, CC4.1, CC5.2 | Gate G10; penetration test (POAM-013); system description; remaining infrastructure in code; CPA readiness check 2027-02-28 |
| 2027 Q2 | All in scope | Type 1 as of 2027-03-31; report by 2027-05-31; Type 2 period from 2027-04-01 |

**Owner of the program:** the CTO. **Decision:** the Chief Executive Officer approved this plan, the gates, and the CPA firm budget on 2026-09-15; the CPA firm is to be engaged by 2026-12-15.
