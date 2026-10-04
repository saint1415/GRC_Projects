# Regulatory Gap Analysis: Cris Santos Company | Information | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Tier / Vertical | Mid-Market / Information |
| Regulations analyzed | FTC Act Section 5 (15 U.S.C. 45(a)): reasonable security measured against FTC business guidance, and deception measured against the company's own statements and commitments; HIPAA Security Rule as a business associate (45 CFR Part 164, Subpart C; in force, last amended 2020-11-24); HIPAA breach notification duties of a business associate (45 CFR 164.402, 164.410, 164.412, 164.414) |
| Applicability checks only | CCPA/CPRA and CPPA regulations (N51-R03); other state comprehensive privacy laws as a processor; DOJ Data Security Program (N51-R04) |
| Assessment dates | 2026-07-13 to 2026-08-07; evidence refreshed with P07 results through 2026-09-04 |
| Assessor | GRC Manager and the Associate General Counsel, Privacy, with the Director of Security; reviewed by the co-sourced internal audit firm |
| Approved | Chief Technology Officer and General Counsel, 2026-09-29 |

## 1. Applicability
**Primary business line:** subscription sales of a multi-tenant customer service platform (NAICS 513210) to about 2,400 U.S. businesses, including 46 healthcare customers and 9 community banks.

| Regulation | Applies? | Basis |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes** | The company is a for-profit software publisher in interstate commerce and is not in any statutory carve-out (banks, savings and loans, federal credit unions, common carriers, air carriers). There is no size threshold. The FTC uses two theories in data security cases, and both apply here (section 1.1) |
| HIPAA Security Rule | **Yes, for the healthcare cell** | The company creates, receives, maintains, and transmits ePHI for 46 covered entities under BAAs, so it is a business associate (45 CFR 160.103). "A covered entity or business associate must comply with the applicable standards, implementation specifications, and requirements of this subpart" (45 CFR 164.302). No size exemption applies; 164.306(b) lets the company weigh its size, complexity, and costs when choosing *how* to meet each standard |
| HIPAA Breach Notification Rule, business associate duties | **Yes** | 45 CFR 164.410 requires a business associate to notify the covered entity after discovering a breach of unsecured PHI, no later than 60 calendar days after discovery; the BAAs shorten this to 10 business days |
| SOC 2 Trust Services Criteria | **By contract** | Customers require a SOC 2 Type 2 report. The criteria are assessed one by one in P09; this analysis tests the commitments the company makes in its SOC 2 system description as deception rows |

### 1.1 FTC Act Section 5
Section 5(a) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful (15 U.S.C. 45(a)(1)).
- **Unfairness:** a practice is unfair if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition" (15 U.S.C. 45(n)). The 92 million end consumers whose messages sit in the platform cannot protect that data themselves; only the company and its customers can.
- **Deception:** a material representation, omission, or practice likely to mislead a consumer acting reasonably. The trust center, DPA, BAA, MSA, SOC 2 system description, product pages, and questionnaire answers are all representations.

Section 5 does not list controls. This analysis uses the FTC's own business guidance as the requirement set (URLs checked 2026-09-26 for the Small sample and reused):

| Source | URL | Rows |
|---|---|---|
| Start with Security: A Guide for Business (10 lessons, 28 practices) | https://www.ftc.gov/business-guidance/resources/start-security-guide-business | G-001 to G-028 |
| Protecting Personal Information: A Guide for Business | https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business | G-029, G-030 |
| Data Breach Response: A Guide for Business | https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business | G-031 |
| Company statements and commitments (deception) | Trust center, DPA, BAA, MSA, bank contracts, SOC 2 system description, product page, questionnaires | G-032 to G-045 |

### 1.2 CCPA applicability check (no gap table)
| Test | Threshold (N51-R03) | Company | Result |
|---|---|---|---|
| "Business" (Cal. Civ. Code 1798.140(d)) | Annual gross revenue over $26,625,000 (CPI-adjusted, effective 2025-01-01), or other tests | $100.0 million in 2025; does business in California | **Is a business** for personal information it collects for its own purposes (about 70,000 California consumers) |
| Service provider | Processes personal information on behalf of a business under a written contract | Processes about 11 million California end consumers' records for customers under DPAs with service-provider terms | **Acts as a service provider** for customer data; use limits are tested in G-039 |
| Cybersecurity audit (Cal. Code Regs. tit. 11, 7120) | Revenue threshold met and, in the preceding year, personal information of 250,000 or more consumers or households, or sensitive personal information of 50,000 or more consumers | Own-purpose data: about 70,000 California consumers, so not met on that count. Service-provider processing: about 11 million | **Open question.** Counsel notes it is unsettled whether personal information processed as a service provider counts toward the threshold. Decision due 2026-12-31 (P01 R-043). If triggered, 2026 revenue (forecast about $112 million) puts the first audit report at 2028-04-01 under the CPPA schedule |
| Risk assessments and ADMT rules | Listed processing; ADMT used for significant decisions | Customers decide how they use AI Assist, Answer Bot, and triage | Handled in P10 as customer-side duties the company supports |

By decision (vertical profile, 2026-09-26), the CCPA stays an applicability check and is not decomposed into a gap table.

### 1.3 Other state privacy laws as a processor
Several state comprehensive consumer privacy laws place duties on processors that act for a controller, generally carried out through the contract with the controller. The company meets them through its DPA, which counsel keeps aligned with state-specific terms. They are not decomposed here; the DPA commitments are tested in G-036 to G-039.

### 1.4 DOJ Data Security Program check
28 CFR Part 202 restricts covered data transactions that give countries of concern or covered persons access to bulk U.S. sensitive personal data. The platform holds far more than the bulk thresholds for covered personal identifiers (100,000 U.S. persons) and personal health data (10,000, in the healthcare cell). The company has **no** covered data transactions identified today: hosting is in the United States, all 14 sub-processors are U.S.-based or process in the United States, and the engineering contractor in Poland (not a country of concern) has no access to customer data. The gap is screening: there is no Data Security Program attestation or check for contractor personnel or sub-processors (P01 R-033).

### 1.5 Not applicable
COPPA (N51-R02), FCC CPNI (N51-R06), FedRAMP (N51-R07), SEC disclosure (N51-R08), and PADFA (N51-R05) do not apply; reasons are in `../00_company-facts.md` section 1. The FTC Health Breach Notification Rule does not apply because PHI is handled as a HIPAA business associate. The bank service provider notification rule (12 CFR 53.4) and state breach laws are handled in P08.

**Excluded HIPAA Security Rule rows (7), with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a health care clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): applies to governmental entities; all 46 covered entities use BAAs.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans; 5 rows): group health plan requirements, not part of the company's business associate role. The company's own employee benefit plan is outside this analysis.

## 2. Method
1. **Requirements.** FTC guidance practices are cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work). Each company commitment became one deception row. HIPAA Security Rule requirements and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (the 69 rows of the repository's Health Care crosswalk). One crosswalk citation, 164.314(a)(3)(i), is shown with its current eCFR location, 164.314(a)(2)(i)(C). Breach notification rows were decomposed from the eCFR text (2026-09-23 version, checked through the eCFR API).
2. **Crosswalk.** Each row is mapped to CSF 2.0, SP 800-53 Rev. 5, and SOC 2 criterion IDs. All mappings are **author mappings**: no official NIST or FTC mapping of the FTC guidance exists, and NIST's official CSF 2.0 mapping of the HIPAA Security Rule is not yet published. SOC 2 criteria are listed by ID only (the AICPA text is copyrighted).
3. **Evidence.** Interviews with the CTO, VP Platform Engineering, VP Engineering, Director of Security, VP Customer Support, VP Product, Director of IT, and the Associate General Counsel, Privacy; configuration exports; the SOC 2 Type 2 report; contracts; and the trust center as captured on 2026-07-20.
4. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population, sized with the co-sourced internal audit firm's attribute sampling table:
   - terminations: 25 of 96; transfers: 25 of 58; new hires: 25;
   - healthcare cell just-in-time sessions: 25 of 312 (Q2 2026); healthcare role grants: 15;
   - support view sessions: 30 of about 4,100 (90 days);
   - terminated tenants: 20 of 61;
   - security questionnaires: 10 of 212;
   - incidents: 10 of 44;
   - bug bounty reports: 10 of 47;
   - critical image findings: all 38 (2026-02 to 2026-07);
   - backup job days: 31 of 31 (August 2026);
   - error-log events: 200;
   - warehouse saved queries: 10 of 120;
   - sub-processor contracts: 14 of 14; BAAs: 46 of 46;
   - laptop wipe certificates: 10 of 31;
   - Answer Bot replies: 400 (P10 evaluation).
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

**Addressable is not optional.** For each addressable HIPAA specification, the company must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented.

## 3. Results summary
| Requirement set | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 11 | 17 | 0 | 0 | 28 |
| FTC Protecting Personal Information | 0 | 2 | 0 | 0 | 2 |
| FTC Data Breach Response | 0 | 1 | 0 | 0 | 1 |
| FTC deception: statements and commitments | 2 | 8 | 4 | 0 | 14 |
| **FTC Act Section 5 subtotal** | **13** | **28** | **4** | **0** | **45** |
| HIPAA 164.308 Administrative safeguards | 11 | 17 | 1 | 1 | 30 |
| HIPAA 164.310 Physical safeguards | 12 | 0 | 0 | 0 | 12 |
| HIPAA 164.312 Technical safeguards | 9 | 3 | 0 | 0 | 12 |
| HIPAA 164.314 Organizational requirements | 0 | 4 | 0 | 6 | 10 |
| HIPAA 164.316 Policies, procedures, documentation | 3 | 2 | 0 | 0 | 5 |
| **HIPAA Security Rule subtotal** | **35** | **26** | **1** | **7** | **69** |
| HIPAA breach notification (business associate) | 0 | 6 | 0 | 0 | 6 |
| **Total** | **48** | **60** | **5** | **7** | **120** |

**Security Rule detail.** Of the 27 Security Rule rows that are Partially met or Not met, 10 are standards, 13 are **Required** implementation specifications (including the one Not met, 164.308(a)(7)(ii)(C) emergency mode operation), and 4 are **Addressable**.

**Gap risk ratings (65 rows Partially met or Not met):** 18 High, 40 Moderate, 7 Low.

**Reading the results.** The company has a defined program, and its gaps are of scale, not of absence:
- **Physical and transmission safeguards are Met,** largely inherited from the cloud provider and evidenced by its SOC 2 report.
- **Authentication for the workforce is strong** (G-006, G-008, 164.312(d)), and encryption is everywhere it is claimed (G-032).
- **The gaps concentrate in five places:** machine credentials (G-007); data-level visibility (G-014, 164.308(a)(1)(ii)(D), 164.312(b), 164.410(c)); tenant isolation (G-013, 164.312(a)); the healthcare cell boundary (G-003, 164.308(b), 164.314(a)); and recovery (164.308(a)(7)).
- **4 of the 5 Not met rows are deception rows.** The trust center says AI providers do not retain data and that all staff access needs permission and is logged; the DPA promises deletion in 30 days; a product page says Answer Bot answers only from the help center. None of those is true today. Under Section 5, the cheapest fix comes first: correct the statements, then fix the practice.

## 4. Priority gaps
| Gap | Row(s) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Inaccurate trust center statements (AI retention; staff access and logging) | G-033, G-034 | High | Correct the statements now; restore only when practice matches | General Counsel | 2026-10-15 |
| 9 long-lived cloud keys, including one that reads all attachments | G-007 | High | Federated short-lived credentials; delete the keys | VP Platform Engineering | 2026-10-31 |
| Healthcare subject lines exported to the warehouse; ePHI to 2 subcontractors without BAAs | G-003, G-052, G-074, G-075, G-100, G-103 | High | Stop the export; purge; sign BAAs or stop the flows; counsel four-factor assessment (G-115) | Associate General Counsel, Privacy | 2026-11-30 |
| No object-level or database audit logs; cannot identify affected records | G-014, G-050, G-066, G-093, G-118 | High | Object and database audit logs (healthcare cell first); MDR on cloud workloads | Director of Security | 2026-12-31 |
| Tenant isolation is one layer | G-013, G-088 | High | Database row-level security; per-tenant search credentials; cross-tenant tests | VP Engineering | 2027-03-31 |
| Backups deletable; no regional DR plan; no emergency mode procedures | G-068, G-069, G-070 | High | Write-once backup vault; warm standby; DR plan with emergency mode procedures | VP Platform Engineering | 2027-06-30 |
| Answer Bot claim not substantiated | G-045 | Moderate | Withdraw the claim; grounded-only mode (P10) | VP Product | 2026-10-15 |
| Terminated tenants' attachments kept past 30 days | G-002, G-038 | Moderate | Extend deletion; purge 61 tenants | VP Engineering | 2026-11-30 |
| Notice readiness (24-hour, BAA, bank 4-hour; 71% contacts) | G-030, G-031, G-036, G-043, G-044 | Moderate | P08 runbooks, clock sheet, contact collection; tabletop 2026-11-10 | VP Customer Support | 2026-11-30 |
| Questionnaire answers inaccurate in 5 of 10 samples | G-042 | Moderate | Locked answer library; correct affected customers' records | GRC Manager | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Tell the truth and close the doors** | 2026 Q4 | Correct the trust center and product claims; retire the 9 keys; stop the healthcare export; subcontractor BAAs; fix the webhook SSRF; P08 runbooks and tabletop; contact collection | G-033, G-034, G-045, G-007, G-003, G-074, G-075, G-020, G-030, G-031 |
| **2. See and prove** | 2026 Q4 to 2027 Q1 | Object and database audit logs; MDR on cloud workloads; write-once backups; deletion job; standing roles removed; STD-02, STD-03, STD-07 issued; SOC 2 readiness gates (P09) | G-014, G-050, G-093, G-118, G-068, G-002, G-038, G-005, G-110, G-112 |
| **3. Isolate** | 2027 Q1 | Database row-level security; per-tenant search credentials; cross-tenant test suite; customer approval for support view on all plans | G-013, G-088, G-004, G-009 |
| **4. Recover** | 2027 Q2 | Warm standby; DR plan with emergency mode; failover within 4 hours; restore the trust center claims that are then true | G-069, G-070, G-071, G-040 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes and watch items
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of these items is treated as a current obligation. If finalized as proposed, the verified proposals that would affect the healthcare cell are: removal of the Required and Addressable distinction; encryption of all ePHI at rest and in transit (Met today); MFA (Met for the workforce); a written technology asset inventory and network map; penetration testing at least every 12 months, plus vulnerability scanning; restoring certain systems and data within 72 hours; a compliance audit at least every 12 months; and **business associate notice within 24 hours of activating a contingency plan**, which would add a new clock to P08. The `pending_rule_change` column flags each affected row.
- **FTC proposed policy statement on suppression of accuracy in AI systems** (91 FR 41638, published 2026-07-07; File No. P264200; comments closed 2026-07-31): a **proposed** statement on how Section 5's deception prohibition applies to companies that market AI systems. Not final as of 2026-09-25; flagged on G-019, G-033, and G-045 as a watch item only.
- **CCPA cybersecurity audits:** applicability open (section 1.2). If triggered, the first report would be due 2028-04-01.
- **CPPA ADMT rules:** compliance for existing ADMT uses by 2027-01-01. These fall on customers that are CCPA businesses and use AI features for significant decisions; the company's supporting duties are in P10.
- **Colorado SB26-189** (signed 2026-05-14, effective 2027-01-01): developer documentation duties for AI used in consequential decisions. P10 assesses whether any of the company's AI features fall in scope.
