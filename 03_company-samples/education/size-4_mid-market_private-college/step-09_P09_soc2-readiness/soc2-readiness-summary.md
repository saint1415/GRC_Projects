# SOC 2 Readiness Summary: Cris Santos Company | Educational Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Tier / Vertical | Mid-Market / Educational Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | College readiness assessment for the employer education services (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the vCISO (Qualified Individual) and the Information Security Manager, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A college is usually **not** a SOC 2 service organization, because it educates students rather than providing services to other businesses' systems. One service line changes that:
- The college runs **employer education services** for 9 employer partners, who sponsor about 640 employees as students.
- The partners rely on the college's **employer partner portal** and file feeds for enrollment and progress reports (with each student's written consent under 34 CFR 99.30) and monthly invoices of about $560,000.
- Two hospital-system partners must show their own auditors that the college protects their employees' data and keeps the service available. They asked for a SOC 2 Type 2 report covering Security, Availability, and Confidentiality before their contracts renew on 2027-12-31.

For that service line, the college is a service organization, and a SOC 2 Type 2 report is the right assurance tool. The vertical overlay lists no sector-specific alternative to SOC 2 for education.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in recovery, monitoring, access, and vendor oversight. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1, issue a Type 1 (design) report on 2027-03-31 as an interim deliverable, then run a 6-month observation period from 2027-04-01. Both hospital partners accepted this plan with quarterly status updates.

**Alternatives considered:**
- **Security questionnaire only:** acceptable to 7 partners, not to the 2 hospital systems' auditors.
- **ISO/IEC 27001 certification:** broader than needed and slower; the partners asked for SOC 2.
- **Type 1 only:** an interim step, not the end state.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm (P07) and not the vCISO's firm, so neither the assessment work nor the Qualified Individual role creates an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Employer education services: enrollment and progress reporting, invoicing, and the employer partner portal |
| Infrastructure | The cloud landing zone (P04), with emphasis on the workloads account (partner portal, data warehouse, integration platform) and the backup account; the identity provider |
| Software | Employer partner portal (contractor-built), SIS, LMS, data warehouse, integration platform |
| People | Corporate partnerships team (6), Registrar's office, IT and security team, MSSP, vCISO |
| Data | Sponsored students' enrollment, progress, and consent records; invoices |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, and the IT DR plan (due 2026-12-31) |
| Subservice organizations (carve-out) | SIS vendor, LMS vendor, cloud provider, identity vendor, and MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the college's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 18 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **21** | **6** | **23** |

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- malware protection: CC6.8;
- capacity: A1.1.

**Not ready (6):**
- CC6.1: partner portal users sign in with passwords only, and SaaS administrators have standing access;
- CC6.3: broad role-based access and annual reviews;
- CC7.2: no monitoring of SIS, LMS, or portal user activity;
- CC7.5 and A1.3: no IT DR plan, and the only restore attempted (P07) failed;
- CC9.2: vendor contract terms and reviews.

Each maps to a P07 POA&M item. Processing Integrity and Privacy are out of scope because the partners did not request them; FERPA consent and disclosure duties stay with the FERPA program (P03).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments: BP-12 RTO 24 hours), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC3.4, CC8.1, CC9.1, A1.2, C1.1 | Material-change trigger records; change tickets with second reviewer; IT DR plan; license server backup; automated consent check |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.3, CC3.3, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.7, CC7.1, CC7.2, CC7.3, CC7.4, CC7.5, CC9.2, A1.3, C1.2 | Quarterly audit committee minutes; role-based training records; SIEM source list and alerts; partner system description; partner MFA settings; semiannual access reviews; encryption rule and interconnection terms; fraud incident records; tabletop reports; restore test records; vendor amendments and reviews; retention schedule |
| 2027 Q1 (by 2027-03-31) | CC6.4 (badge readers at Campus 3) | Badge system reports |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the partners | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (access reviews, monthly scans, quarterly restore tests, vendor reviews, change tickets) |

**Status reporting.** The vCISO reports readiness monthly to the CIO and quarterly to the audit committee and the two hospital-system partners.

## 5. Vendor SOC 2 review program (Part B)
The college relies on vendor controls for many inherited controls (P02: 8 Common/Inherited and 30 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03) and of 16 CFR 314.4(f)(3).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Customer information or education records at scale (more than 1,000 students), privileged access to college systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to college controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited student data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available; FERPA and no-training contract terms | Every 2 years, and before any expansion |
| **Tier 3** | No student data and no system access | Contract terms only | At contract renewal |

Of about 90 student-data vendors, 14 are Tier 1 and about 35 are Tier 2 under this approach. The CSV holds the first 8 Tier 1 reviews and 1 Tier 2 example (the AI tutor vendor). The remaining 6 Tier 1 reviews (admissions CRM vendor, third-party servicer, emergency notification vendor, payment plan vendor, ERP vendor, and the vCISO consulting firm) are due by 2027-03-31 (POAM-020). The servicer has no SOC 2 report; its annual Title IV servicer compliance audit and a security attestation will be used instead.

**Key findings:**
1. **SIS vendor:** unqualified Type 2, but its stated RTO of 24 hours and RPO of 4 hours **do not meet the BIA** (RTO 8 hours, RPO 1 hour for registration and records). Three of the complementary user entity controls the college must operate are open gaps: access reviews, student MFA and step-up, and log review. **The vendor's controls only protect the college once those gaps close.**
2. **FAMS vendor:** Security-only report with no recovery objectives, so availability for aid processing cannot be compared with the BIA; its 5-business-day incident notice term is below the college's 72-hour standard.
3. **Proctoring vendor (AI-005):** qualified opinion for vendor support staff access reviews (since remediated); recording retention must be set by the college (P10).
4. **MSSP:** escalation exceptions in 2 of 40 samples, and the SIEM platform is carved out; the platform's own report must be obtained.
5. **AI tutor vendor (AI-004):** no SOC 2, no contract beyond card terms, and prompts used to improve its models. The pilot cannot continue without FERPA, no-training, and deletion terms (P10).
