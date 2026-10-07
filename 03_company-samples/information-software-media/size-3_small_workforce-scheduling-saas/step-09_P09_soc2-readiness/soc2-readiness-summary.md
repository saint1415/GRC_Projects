# SOC 2 Readiness Summary: Cris Santos Company | Information | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Small / Information |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criteria are cited by ID with short topic labels in our own words |
| Categories in scope | Security (CC1 to CC9), Availability (A1), Confidentiality (C1) |
| Target report | Type 2, observation period 2026-11-01 to 2027-04-30, report expected by 2027-06-30 |
| Prior report | Type 1 (Security and Confidentiality) as of 2026-02-28, issued 2026-03-27: unmodified opinion with 3 exceptions |
| Part A | Readiness checklist, criterion by criterion (`soc2-readiness.csv`) |
| Part B | Sub-processor and critical vendor report reviews (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-08 to 2026-09-11 by the IT Manager with the COO and Platform Engineering Lead; approved by the CTO 2026-09-22 |

## 1. Why SOC 2 for this organization
The company is a service organization in the SOC 2 sense: about 310 businesses run their scheduling and timekeeping on its platform, and their auditors and security teams need assurance about controls they cannot see. The MSA promises a current SOC 2 report under NDA, and enterprise prospects ask for a Type 2 before signing. The Type 1 showed that controls were designed; the Type 2 must show they **operated** for six months.

Alternatives named for this vertical were considered:
- **ISO/IEC 27001 certification:** accepted by some buyers, but the company's U.S. customers ask for SOC 2, and a certificate does not report test exceptions. Not pursued now.
- **FedRAMP authorization:** only for cloud services sold to federal agencies. The company has no federal customers (N51-R07 does not apply).

**How this file relates to P03.** P03 tests the FTC's Section 5 expectations and the company's own promises (security page, DPA, SOC 2 system description). This file checks each Trust Services criterion for the Type 2 and does not repeat the P03 analysis. Where the same weakness appears in both, both point to the same POA&M item in P07.

## 2. System description (scope)
- **Services:** the Workforce Scheduling Platform (WSP): scheduling, time capture, timesheet approval, payroll exports, shift notifications and swaps, and the AI assistant (beta).
- **Infrastructure and software:** the production cloud account (SYS-01), the source repository and CI/CD pipeline (SYS-03), the identity provider (SYS-04), the internal admin console (SYS-05), and observability (SYS-06), as defined in the SSP (P02). The staging account (SYS-02) is in scope for Confidentiality until the purge of production data is verified.
- **Subservice organizations (carve-out method):** the cloud provider, logging and monitoring SaaS, email delivery service, SMS provider, support ticketing SaaS, and AI model provider (the 6 DPA sub-processors), plus the identity provider and source hosting and CI service. Their controls are covered by the Part B reviews.
- **People:** 60 employees; the 6 engineers with production access and the 10 support agents are the key control operators.
- **Data:** customer worker data (Restricted under POL-04), customer administrator accounts, and payroll export files.
- **Procedures:** POL-01 to POL-05 (P06), the P08 runbook, and the procedures listed in section 5.

**Commitments to describe:** 99.9% monthly availability, 72-hour (48-hour for 3 customers) incident notice, 30-day sub-processor notice, deletion within 90 days of termination, and use of customer data only to provide the service. The Type 1 system description does not yet cover Availability or the AI assistant (CC3.1, due 2026-10-30).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1 to CC9, 33 criteria) | 8 | 18 | 7 | 0 |
| Availability (A1, 3 criteria) | 0 | 1 | 2 | 0 |
| Confidentiality (C1, 2 criteria) | 0 | 0 | 2 | 0 |
| Processing Integrity (PI1, 5 criteria) | | | | 5 |
| Privacy (P1 to P8, 18 criteria) | | | | 18 |
| **In scope (38 criteria)** | **8** | **19** | **11** | |

**Ready (8):** CC1.1 code of conduct; CC1.3 roles and reporting lines; CC3.2 risk assessment; CC4.2 deficiency tracking; CC5.1 control selection; CC6.4 physical access (inherited); CC6.5 asset disposal; CC6.6 boundary protection.

**Not ready (11):** CC2.3 external communication; CC6.1 and CC6.3 privileged and least-privilege access; CC6.7 data movement to staging; CC7.2 security monitoring; CC7.5 recovery; CC9.2 vendor management; A1.2 backup and recovery infrastructure; A1.3 recovery testing; C1.1 and C1.2 confidential data handling and disposal.

### 3.1 Type 1 exceptions: status
| Type 1 exception | Criteria | Status at readiness | Fix and date |
|---|---|---|---|
| 1. Shared break-glass database role, no session recording | CC6.1, CC6.3 | Still occurring (38 uses in 90 days, P07) | Named just-in-time access with session recording, 2026-10-23 (POAM-001, POAM-003) |
| 2. Unmasked production data in staging | C1.1, CC6.7 | Still occurring (monthly refresh) | Refreshes stopped 2026-09-30; purge verified 2026-10-30 (POAM-010) |
| 3. No sub-processor security or SOC 2 review | CC9.2 | 7 of 8 reviews done in Part B; program not yet adopted | Program adopted and model provider DPA signed, 2026-10-31 (POAM-011) |

A repeat of any Type 1 exception during the observation period would be reported again, so all three are readiness gates.

### 3.2 Readiness gates (must be operating by 2026-10-31)
| Gate | Criteria | Owner | Due |
|---|---|---|---|
| G1. Retire the shared break-glass role; named just-in-time access with session recording | CC6.1, CC6.3 | CTO | 2026-10-23 |
| G2. Stop staging refreshes and verify the purge | C1.1, CC6.7 | Engineering Manager | 2026-10-30 |
| G3. Sub-processor review program adopted; model provider DPA signed; customers re-noticed with a 30-day objection window | CC9.2, CC2.3 | COO | 2026-10-31 |
| G4. Federated CI credentials; static keys deleted | CC6.1 | Platform Engineering Lead | 2026-10-16 |
| G5. Provider threat detection on | CC7.2 | Platform Engineering Lead | 2026-10-16 |
| G6. Security page and AI claim corrected; quarterly statement review scheduled | CC2.3 | COO | 2026-10-15 |
| G7. Baseline access review of cloud roles, database users, repository, staging, and admin console | CC6.2, CC6.3 | IT Manager | 2026-10-30 |
| G8. System description updated for Availability and the AI assistant | CC3.1 | IT Manager | 2026-10-30 |
| G9. Policy acknowledgments from all staff; 3 new procedures approved | CC1.5, CC2.2, CC5.3 | People Operations Manager and IT Manager | 2026-10-31 |

The IT Manager reports gate status to the CTO weekly in October. If G1, G2, or G3 is not met by 2026-10-31, the CTO and the service auditor will decide whether to move the period start (P01 R-026).

### 3.3 Changes during the period
Some controls cannot start before 2026-11-01: weekly privileged log review (from 2026-11-02), the tabletop exercise (2026-11-18), object logging and the 1-year log archive, the vulnerability deploy gate, and tenant deletion (2026-11-30), the separate backup account and secure coding training (2026-12-15), and the DR plan, first failover test, and database row security (2027-01-31). They will be described as changes during the period. Controls that start late may still produce exceptions for the months before they start, most likely on A1.2, A1.3, and CC7.5. The CTO accepted that risk on 2026-09-22 and kept Availability in scope because customers rely on the 99.9% SLA.

## 4. Sub-processor and critical vendor reviews (Part B)
Eight reports were reviewed from 2026-09-08 to 2026-09-11: the 6 DPA sub-processors plus the identity provider and the source hosting and CI service.

| Result | Vendors |
|---|---|
| SOC 2 Type 2 reviewed, current | V-01 cloud provider, V-02 logging SaaS, V-03 email delivery, V-05 support SaaS, V-06 AI model provider, V-07 identity provider |
| Alternative assurance accepted | V-04 SMS provider (ISO/IEC 27001 certificate and questionnaire) |
| Pending a newer report | V-08 source hosting and CI service (latest report period ended 2025-06-30) |

**Key findings:**
- **All opinions are unmodified.** Two vendors had one remediated exception each (V-02, V-05). None affects the company's controls.
- **The company's own gaps defeat the vendors' controls.** Every report lists complementary user entity controls the company must run: protecting API and cloud keys, managing access, configuring logging and backups. Open company gaps affect 7 of the 8 (all but V-05): for example POAM-005 (keys) on V-01, V-03, V-04, V-06, and V-08; POAM-006 and POAM-014 on V-01; POAM-018 on V-02; R-024 on V-07. The vendors' controls only protect customer data once those POA&M items close.
- **The AI model provider's report does not cover the zero-retention option** the company relies on. A signed DPA with no-training and zero-retention terms is a condition in P10 (due 2026-10-31).
- **Bridge letters** are requested for V-01, V-05, and V-07 to cover the gap to 2026-09-30.
- **DOJ Data Security Program:** all 8 vendors state U.S.-based processing in their reports or contracts. A specific question on access from countries of concern will be added to the review template for the next cycle (P01 R-034, due 2026-12-31).

## 5. Remediation plan and evidence calendar
The service auditor will sample evidence across the six months. The IT Manager checks each month that the evidence below exists (CA-7), starting 2026-11.

| Frequency | Evidence | Criteria | Owner | First due |
|---|---|---|---|---|
| Per event | Joiner, mover, and leaver tickets with access changes; change tickets and pull requests; incident tickets with severity; customer approvals for view-as-tenant | CC6.2, CC6.3, CC8.1, CC7.3 | People Operations Manager; Engineering Manager; Customer Support Manager | 2026-11-01 |
| Weekly | Privileged activity review record | CC7.2, CC6.1 | IT Manager | 2026-11-02 |
| Monthly | View-as-tenant session review; vulnerability report with overdue items; POA&M review minutes; backup job and uptime report; incident review | CC7.2, CC7.1, CC4.2, A1.2, CC7.3 | IT Manager; Platform Engineering Lead | 2026-11-30 |
| Quarterly | Access reviews of all in-scope systems; public statement review; customer security contact list check; emergency account test; capacity review; security review with the Chief Executive Officer | CC6.2, CC6.3, CC2.3, CC7.4, A1.1, CC1.2 | IT Manager; COO; Customer Support Manager; Platform Engineering Lead | 2026-12-15 |
| Semiannual | Restore test against the BIA RTO and RPO; phishing simulation | A1.3, CC1.4 | Platform Engineering Lead; IT Manager | 2026-12-15 |
| Annual | Risk assessment update; policy review; awareness and secure coding training; tabletop exercise; penetration test; sub-processor report reviews | CC3.2, CC5.3, CC1.4, CC7.4, CC4.1, CC9.2 | IT Manager; COO; Engineering Manager | 2026-11-18 (tabletop); 2027-01-31 (penetration test) |

**Remediation by quarter:**
| Quarter | Criteria addressed | Main actions |
|---|---|---|
| 2026 Q4 (before 2026-11-01) | CC6.1, CC6.3, CC6.7, C1.1, CC9.2, CC2.3, CC3.1, CC1.5, CC2.2, CC5.3 | Gates G1 to G9 |
| 2026 Q4 (in period) | CC7.2, CC7.1, CC7.4, C1.2, CC1.4, A1.2 | Log review and archive, alerts, tabletop, deploy gate, tenant deletion, backup account, secure coding training |
| 2027 Q1 | CC7.5, CC9.1, A1.3, CC6.8, CC3.3 | DR plan, failover test, image signing and pinning, fraud risk scenarios, database row security |
| 2027 Q2 | All | Readiness check with the service auditor in 2027-04; period ends 2027-04-30; report by 2027-06-30 |

**Owner of the program:** the IT Manager. **Decision:** the CTO approved the readiness plan and gates on 2026-09-22. The observation period stays 2026-11-01 to 2027-04-30 unless G1, G2, or G3 slips.
