# Regulatory Gap Analysis: Cris Santos Company | Educational Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Tier / Vertical | Mid-Market / Educational Services |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as applied to Title IV institutions and enforced by Federal Student Aid (FSA). Text checked on eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023) |
| Other regulations for the primary business line | FERPA (34 CFR Part 99); Title IV program requirements tied to information security and fraud (SAIG Enrollment Agreement; 34 CFR 668.16(c) and (g), 668.24(e), 668.25(c), 668.164(h)(2); HEA section 483); Clery Act emergency procedures (34 CFR 668.46(g), cyber-relevant parts) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Information Security Manager and the Chief Compliance Officer, with the vCISO (Qualified Individual); reviewed by the co-sourced internal audit firm |
| Approved | Chief Information Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** postsecondary education (campus and online) funded largely through the federal student aid programs.

| Regulation | Applies? | Basis |
|---|---|---|
| FTC Safeguards Rule, 16 CFR Part 314 | **Yes, in full** | Each Title IV institution agreed in its PPA to comply with 16 CFR Part 314. FSA reviews it in the annual compliance audit and treats safeguards findings as part of administrative capability (FSA Electronic Announcement GENERAL-23-09, Feb. 9, 2023). The college holds customer information on about **41,000 consumers**, so the 16 CFR 314.6 exception (fewer than 5,000) does not apply |
| 314.4(a)(1)-(3) (Qualified Individual from a service provider) | **Yes** | Unlike a college whose Qualified Individual is an employee, this college's Qualified Individual is the vCISO, employed by a consulting firm. So it must retain responsibility, designate a senior overseer, and require the firm to maintain its own program (verified text, 314.4(a)) |
| FERPA, 34 CFR Part 99 | **Yes** | The college receives funds under Department of Education programs. Its security-relevant duties are "reasonable methods" for school-official access (99.31(a)(1)(ii)), reasonable identity authentication of anyone receiving PII (99.31(c)), and disclosure records (99.32) |
| Title IV requirements tied to security and fraud | **Yes** | SAIG Enrollment Agreement breach notice; internal controls and separation of duties (668.16(c)); referral of applicant and agent fraud to the Office of Inspector General (668.16(g)); record retention (668.24(e)); third-party servicer contracts (668.25(c)); credit balance timing (668.164(h)(2)); HEA limits on FAFSA data |
| Clery Act, 34 CFR 668.46(g) | **Yes, cyber-relevant paragraphs** | The college publishes an annual security report. Paragraphs (g)(1), (g)(2), and (g)(6) depend on the emergency notification service and the identity provider |

**Not applicable, with reasons:**
- **COPPA (N61-R03):** no online services directed to children under 13; minimum age at admission 17.
- **CIPA (N61-R04):** not an E-Rate recipient.
- **HIPAA Security Rule (N61-R05):** the college is not a covered entity; counseling treatment records and student health records are excluded from PHI (45 CFR 160.103).
- **CIRCIA (N61-R06):** proposed only (section 6).
- **FAR 52.204-21, -23, -25:** no federal contracts or subcontracts.
- **Clery missing student notification (668.46(h)):** no on-campus student housing.

**Excluded rows:** 314.6 is listed for completeness and marked Not applicable because the college is above the threshold.

## 2. Method
1. **Requirements.** Each row is a paragraph of 16 CFR 314.3 or 314.4 at the most granular level the rule uses, or a security-relevant paragraph of 34 CFR Part 99, Part 668, or the SAIG agreement. Summaries paraphrase public-domain regulatory text verified on eCFR (2026-09-23 version) through the eCFR API.
2. **Requirement type.** The Safeguards Rule has no required/addressable split. Its elements are mandatory ("shall"), with two built-in alternatives: compensating controls for encryption approved by the Qualified Individual (314.4(c)(3)), and reasonably equivalent controls in place of MFA approved by the Qualified Individual in writing (314.4(c)(5)). Neither alternative has been approved today. 314.4(a)(1)-(3) are typed Conditional, because they apply only when the Qualified Individual works for a service provider or affiliate.
3. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**; no official NIST mapping exists for 16 CFR Part 314, FERPA, or 34 CFR Part 668.
4. **Evidence.** Interviews (CIO, vCISO, Chief Compliance Officer, Registrar, Director of Financial Aid, Bursar, Vice President of Enrollment Management, Dean of Online Learning, Director of Campus Safety, Director of Corporate Partnerships), document review, configuration exports, and walkthroughs at Campus 1 and Campus 3.
5. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population, using the co-sourced internal audit firm's attribute sampling table (25 items for a moderate-risk control operating many times a year; fewer for small populations):
   - terminations: 25 of 142; transfers: 25 of 58;
   - refund bank changes: 30 of about 2,400 (2025-26 award year);
   - vendor contracts: 20 of about 90; servicer accounts: 8 of 8;
   - emails from financial aid to the servicer: 20;
   - SIS configuration and integration changes: 20;
   - critical vulnerability findings: 40;
   - incidents: 10 of 44;
   - FERPA access requests: 15 of 15; sponsored students' consents: 20 of about 640;
   - service desk student password resets: 10;
   - Title IV record retrieval: 10 files from 2021-22.
   Each `evidence` cell names the sample and its result.
6. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork. Remediation completed since then (for example POL-03 and the P08 runbooks, approved 2026-09-17) is shown in the remediation columns, not as a changed status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 314.3(a) Written program | 0 | 1 | 0 | 0 | 1 |
| 314.4(a) Qualified Individual | 2 | 2 | 0 | 0 | 4 |
| 314.4(b) Risk assessment | 4 | 1 | 0 | 0 | 5 |
| 314.4(c) Safeguards | 0 | 8 | 3 | 0 | 11 |
| 314.4(d) Testing and monitoring | 0 | 4 | 0 | 0 | 4 |
| 314.4(e) Personnel | 2 | 2 | 0 | 0 | 4 |
| 314.4(f) Service providers | 0 | 3 | 0 | 0 | 3 |
| 314.4(g) Evaluate and adjust | 0 | 1 | 0 | 0 | 1 |
| 314.4(h) Incident response plan | 1 | 5 | 2 | 0 | 8 |
| 314.4(i) Report to the board | 1 | 2 | 0 | 0 | 3 |
| 314.4(j) FTC notification | 0 | 0 | 2 | 0 | 2 |
| 314.6 Exception | 0 | 0 | 0 | 1 | 1 |
| **Safeguards Rule subtotal** | **10** | **29** | **7** | **1** | **47** |
| FERPA, 34 CFR Part 99 | 3 | 9 | 0 | 0 | 12 |
| Title IV and HEA requirements | 2 | 4 | 3 | 0 | 9 |
| Clery Act, 34 CFR 668.46(g) | 1 | 2 | 0 | 0 | 3 |
| **Total** | **16** | **44** | **10** | **1** | **71** |

**Gap risk ratings (54 rows Partially met or Not met):** 9 High, 30 Moderate, 15 Low.

**Reading the results.** The college has a defined program: the Qualified Individual, the written risk assessment, board reporting, qualified staff, separation of duties, and FERPA rights handling are Met. The gaps concentrate in five places:
- authentication of students, the servicer, and partners (314.4(c)(5) Not met; 99.31(c));
- monitoring of SaaS user activity (314.4(c)(8));
- vendor contracts and oversight (314.4(f); 99.31(a)(1)(i)(B));
- notification and fraud referral duties (314.4(j); SAIG agreement; 668.16(g)(1));
- use of FAFSA data beyond aid administration (HEA section 483).

## 4. Priority gaps (High)
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No MFA for students, the servicer, or partner users; no written QI approval of alternatives | 314.4(c)(5) | High | Step-up for refund changes; servicer federation; partner MFA; student MFA by default; interim written QI decision | vCISO (Qualified Individual) | 2027-03-31 |
| Impostors obtain records and refunds through weak student sign-in and account recovery | 34 CFR 99.31(c) | High | Student MFA; identity-proofed resets; step-up for sensitive changes | Chief Information Officer | 2027-03-31 |
| Fraudulent applicants not referred to the OIG | 34 CFR 668.16(g)(1) | High | Written referral procedure; identity verification | Chief Compliance Officer | 2026-11-30 |
| FAFSA-derived data used in the warehouse, AI-002, and marketing analytics | HEA sec. 483 | High | Remove fields, purge history, data use gate | Director of Financial Aid | 2026-11-30 |
| SIS, FAMS, and LMS activity not monitored | 314.4(c)(8) | High | SIEM onboarding; detections; monthly review | Information Security Manager | 2027-01-31 |
| Broad access to student and customer information (advisors, admissions, warehouse, AI-003) | 314.4(c)(1)(ii) | High | Role redesign; warehouse views; AI-003 scope | Registrar | 2026-12-31 |
| Vendor contracts lack safeguards; servicer lacks MFA and notice terms | 314.4(f)(2) | High | Amend contracts, servicer first | Chief Compliance Officer | 2026-12-31 |
| 22 vendors (including 2 AI vendors) not under direct control | 34 CFR 99.31(a)(1)(i)(B) | High | Amend contracts; purchasing gate | Chief Compliance Officer | 2026-12-31 |
| Emergency notification depends on SSO with no break-glass | 34 CFR 668.46(g)(1) | High | Break-glass account and secondary sign-in | Director of Campus Safety | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`. The Qualified Individual's written report to the board on 2026-10-22 will present the section 3 table as the compliance status required by 314.4(i)(1).

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Servicer amendment and federation; step-up for refund bank changes; ISIR fields removed from the warehouse; OIG referral and FSA, FTC, and state notice procedures in use; emergency notification break-glass; second QI board report; first integration platform restore test; risk-based penetration test | 314.4(c)(5) (servicer, refunds); 314.4(h)(4), (j); SAIG agreement; 668.16(g)(1); HEA sec. 483; 668.46(g)(1)-(2); 314.4(i)(1)-(2) |
| **2. Build** | 2027 Q1 | SIS, FAMS, and LMS logs in the SIEM; role redesign; vendor contract amendments; partner MFA; student MFA by default; IT DR plan exercised; standards issued; applicant identity verification | 314.4(c)(1), (c)(8), (f)(2)-(3); 99.31(a)(1), (c); 314.3(a) |
| **3. Prove** | 2027 Q2 | Retention schedule and first disposal; Campus 3 segmentation; quarterly restore tests passing; SOC 2 Type 2 observation period starts 2027-04-01 (P09) | 314.4(c)(6); 314.4(d)(2); 314.4(h) |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (July 2027); third annual QI report; tiered vendor reassessments; campus safety device replacement | 314.4(b)(2); 314.4(i); 314.4(f)(3) |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
- **16 CFR Part 314:** no pending FTC amendment was identified. The most recent change added the 314.4(j) FTC notice, effective May 13, 2024 (314.5).
- **CIRCIA (N61-R06)** is **still proposed**. The proposed rule (89 FR 23644, Apr. 4, 2024) would cover every institution of higher education that participates in Title IV, with no size floor, and would require reports to CISA within 72 hours of a covered cyber incident and within 24 hours of a ransom payment. As of 2026-09-25 no final rule has been published. It is flagged in the `pending_rule_change` column of the three notification rows and is **not** treated as a current obligation.
- **FSA and NIST SP 800-171:** FSA has encouraged institutions to adopt NIST SP 800-171 (Electronic Announcements of Dec. 18, 2020 and GENERAL-23-09) and said it would issue guidance in a future announcement. It is tracked as guidance, not a requirement.
- **State AI law:** Colorado SB26-189 takes effect 2027-01-01 and covers automated decision-making technology that materially influences consequential decisions, including education. Because the online division enrolls students from other states, counsel is reviewing whether AI-001 is in scope (P01 R-052; P10).
