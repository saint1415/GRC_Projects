# Regulatory Gap Analysis: Cris Santos Company | Information | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher, Vendor Compliance Platform) |
| Tier / Vertical | Micro / Information |
| Primary analysis | FTC Act Section 5 data security expectations (15 U.S.C. 45(a)), measured against the FTC's own business guidance, plus the security, data-use, and AI statements the company makes on its website, in its MSA, DPA, and security exhibit, and in questionnaire answers |
| SOC 2 | Related Trust Services criteria are mapped in each row; criterion-by-criterion readiness is in P09 |
| Applicability checks only | CCPA/CPRA (N51-R03); DOJ Data Security Program (N51-R04) |
| Assessment dates | 2026-07-27 to 2026-08-07 |
| Assessor | CTO (security and compliance lead) with the Operations and Finance Manager; outside counsel reviewed sections 1 and 5 |
| Approved | 2026-09-15 by the Chief Executive Officer |

## 1. Applicability

### 1.1 FTC Act Section 5 applies, with no size threshold
Section 5(a) declares "unfair or deceptive acts or practices in or affecting commerce" unlawful (15 U.S.C. 45(a)(1)). The company is a for-profit software publisher selling to customers in six states. It is not in any of the statutory carve-outs (banks, savings and loans, federal credit unions, common carriers, air carriers), and Section 5 has no size threshold (N51-R01). Being a 7-person company changes how much the FTC would expect, not whether Section 5 applies. Both theories the FTC uses in data security cases are relevant:
- **Unfairness:** a practice is unfair if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers themselves and not outweighed by countervailing benefits to consumers or to competition" (15 U.S.C. 45(n)). About 9,800 vendors who are individuals gave their Social Security numbers to customers on W-9s. They cannot protect that data once it is on the platform; only the company can.
- **Deception:** a material representation, omission, or practice likely to mislead a consumer acting reasonably (FTC Policy Statement on Deception, as summarized on the FTC's enforcement authority page). The website security page, the product page's AI accuracy claim, the security exhibit, and questionnaire answers are all representations.

Section 5 does not list specific controls. The FTC explains what it expects through business guidance drawn from its cases. This analysis uses three FTC guidance documents as the requirement set. The 28 practices of the Start with Security guide were checked against the live page on 2026-10-04.

| Source | URL | Used for |
|---|---|---|
| Start with Security: A Guide for Business (10 lessons, 28 practices) | https://www.ftc.gov/business-guidance/resources/start-security-guide-business | G-001 to G-028 |
| Protecting Personal Information: A Guide for Business (5 principles) | https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business | G-029, G-030 |
| Data Breach Response: A Guide for Business | https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business | G-031 |
| FTC enforcement authority page (Section 5 tests) | https://www.ftc.gov/about-ftc/mission/enforcement-authority | Deception and unfairness tests |
| FTC data security guidance hub | https://www.ftc.gov/business-guidance/privacy-security/data-security | Index of guidance and cases |

### 1.2 SOC 2 commitments and the Florida reasonable-measures duty
SOC 2 is not a law. It matters because two prospects and one anchor customer require a report. The overlap with Section 5 is the reason both sit in this analysis: once the company writes something in its security exhibit, a DPA, or a questionnaire, a control that does not work as described is both a SOC 2 problem and a deception risk. Rows G-032 to G-041 test those statements. Criterion-by-criterion readiness for the Type 1 is **not** repeated here; it is in P09, which reuses the `related_tsc_criteria` column.

Florida law adds a general duty. As a "third-party agent" contracted to maintain, store, or process personal information for customers (Fla. Stat. 501.171(1)(h)), the company must "take reasonable measures to protect and secure data in electronic form containing personal information" (501.171(2)). A name with a Social Security number is personal information (501.171(1)(g)1.a.(I)). The FTC rows below are used as the measure of "reasonable"; the Florida notice duties are in P08.

### 1.3 CCPA applicability check (no gap table)
| Test | Threshold (N51-R03) | Company | Result |
|---|---|---|---|
| "Business" (Cal. Civ. Code 1798.140(d)) | Annual gross revenue over $26,625,000 (CPI-adjusted, effective 2025-01-01); or buys, sells, or shares personal information of 100,000 or more consumers or households; or 50% or more of revenue from selling or sharing | About $1.1 million revenue; no selling or sharing; no California customers | **Not a business.** The CCPA's own duties do not apply |
| Service provider terms | Contract terms a CCPA business must put in place with its service providers | No customer is known to be a CCPA business today | **Not applicable now.** The DPA already limits use to providing the service; if a California customer signs, counsel checks the service-provider terms |
| Cybersecurity audits, risk assessments, ADMT rules | Apply only to businesses that meet the thresholds | Not a business | **Not applicable** |

### 1.4 DOJ Data Security Program check
28 CFR Part 202 restricts covered data transactions (data brokerage, vendor, employment, and investment agreements) that give countries of concern or covered persons access to bulk U.S. sensitive personal data. The platform's largest data set is about 52,000 vendor contacts, and about 9,800 records include a Social Security number. Both are below the 100,000-person bulk threshold for covered personal identifiers (28 CFR 202.205). The company also has no covered data transactions: all staff, the contractor, and all providers are U.S.-based, and the platform holds no government-related data. **Not applicable today.** Recheck if the vendor count passes 100,000 or if any offshore provider or staff is added (POL-04).

### 1.5 Not applicable
COPPA (N51-R02), PADFA (N51-R05: the company does not sell data and is not a data broker), FCC CPNI (N51-R06), FedRAMP (N51-R07), and SEC disclosure (N51-R08) do not apply; reasons are in `../00_company-facts.md` section 1. The FTC Health Breach Notification Rule does not apply because the platform holds no health records. State breach laws are handled in P08.

## 2. Method
1. **Requirements.** Each practice in the three FTC guides became one row, cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work, so headings are quoted). Each statement or commitment the company makes publicly or by contract became one deception row.
2. **Crosswalk.** Each row was mapped to CSF 2.0, SP 800-53 Rev. 5, and related SOC 2 criterion IDs. This is an **author mapping**: no official NIST or FTC mapping of this guidance exists. SOC 2 criteria are listed by ID only (the AICPA text is copyrighted).
3. **Documentary evidence.** Each status rests on a named document or record: cloud permission and configuration exports (2026-07-28), the CI secret list and access key report, the tenant list, sample error payloads, the prompt template, the admin console walkthrough (2026-07-29), website and product page captures (2026-07-29), the DPA, MSA, security exhibit, and the questionnaire answer document, vendor contracts, the MSP device report, and the uptime monitor report. Interviews covered all 7 staff, the contract developer, and the MSP lead technician.
4. **Status.** Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-08-07)**. Later evidence, such as the P10 accuracy test, is noted where it confirms a finding but does not change the status. Gap risk uses the P01 scale.

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 28 | 4 | 15 | 9 | 0 |
| FTC Protecting Personal Information | 2 | 0 | 0 | 2 | 0 |
| FTC Data Breach Response | 1 | 0 | 0 | 1 | 0 |
| Deception: security, data-use, and AI representations and commitments | 10 | 1 | 2 | 7 | 0 |
| **Total** | **41** | **5** | **17** | **19** | **0** |

Of the 36 rows that are not met or partially met, 8 are rated High, 25 Moderate, and 3 Low.

**What the numbers say.** The company does the basics that come with good cloud and SaaS defaults: standard encryption, TLS, private networks, password hashing, and lockout. It falls short where a small team has to choose to do something: limiting administrator rights, retiring old keys, logging who reads data, deleting data it no longer needs, and checking its vendors. The deception rows score worst: 7 of 10 statements the company makes to customers are not true today. For a 7-person company that is the cheapest set of gaps to close, and the most urgent.

## 4. Priority gaps
| Gap | Row | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Static CI administrator key, never rotated, copied to a personal laptop | G-007 | High | Federated short-lived CI credentials; delete the key | CTO | 2026-10-15 |
| False claim that tax IDs never leave the platform | G-032 | High | Remove the claim now | Chief Executive Officer | 2026-10-15 |
| Unsupported "99% accuracy" AI claim | G-034 | High | Withdraw; publish only tested figures | Chief Executive Officer | 2026-10-15 |
| False questionnaire answers ("SOC 2 compliant", penetration test) | G-040 | High | Corrected answers to every recipient; CTO approval | Chief Executive Officer | 2026-10-15 |
| Real vendor data on laptops and in model prompts | G-003 | High | Stop extracts; mask Social Security numbers before sending | CTO | 2026-10-31 |
| Five full cloud administrators | G-005 | High | Separate roles; break-glass only for two people | CTO | 2026-11-30 |
| No monitoring of data leaving the platform | G-014 | High | Data-level logging, threat detection, alerts, 1-year archive | Senior Software Engineer | 2026-11-30 |
| Security exhibit promises a penetration test and 30-day backups | G-039 | High | Make both true, or amend the exhibit | Chief Executive Officer | 2027-01-31 |
| Model provider not on the sub-processor list | G-036, G-021 | Moderate | List, notify with 30-day objection window, sign a DPA | Operations and Finance Manager | 2026-10-31 |
| Former customers' data kept past 60 days | G-037, G-002 | Moderate | Delete; deletion runbook | Operations and Finance Manager | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most fixes are configuration changes in the cloud account, one-page procedures, and corrected statements, not new systems. The CTO and Senior Software Engineer do the technical work; the Operations and Finance Manager handles contracts; the Chief Executive Officer owns every public statement. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Rows closed |
|---|---|---|---|
| 1. Stop saying what is not true | 2026-10-15 | Remove or correct the website, product page, and questionnaire claims; send corrected answers; CTO approval for questionnaires; retire the static CI key | G-032, G-033, G-034, G-040, G-007 |
| 2. Contracts and data minimization | 2026-10-31 | Model provider DPA and customer notice; MSP and contractor security terms; stop database extracts; mask Social Security numbers before AI extraction; redact error payloads; delete former customers' data; data inventory; contact list and templates; company laptop for the contractor | G-003, G-010, G-021, G-036, G-037, G-038, G-002, G-028, G-029, G-031, G-015, G-026 |
| 3. Access, logging, and hygiene | 2026-11-30 | Cloud roles; admin console behind single sign-on; contractor and MSP access limits; data-level logging, threat detection, and archive; configuration features on; patch time limits; security contact; AI accuracy tests; tabletop (2026-11-12) | G-005, G-009, G-012, G-014, G-016, G-019, G-023, G-024, G-030, G-035 |
| 4. Product and people | 2026-12-31 | Role-limited TIN view; customer password and MFA rules; ticket-linked view-as-customer; secure coding training; vendor reviews; platform guidance review | G-001, G-004, G-006, G-017, G-018, G-022 |
| 5. Testing | 2027-01-31 | Cross-tenant tests; image scanning; first external penetration test; backups and exhibit aligned | G-013, G-020, G-039 |

**Progress check.** The CTO reports progress to the Chief Executive Officer at the monthly 30-minute review, using the P07 POA&M as the tracker. Phase 1 and 2 completion is also a SOC 2 readiness gate in P09.

## 6. Pending and watch items
- **FTC proposed AI-accuracy policy statement** (Docket FTC-2026-0727; comments closed 2026-07-31): **not final** as of 2026-09-25. Flagged on G-034; not treated as a current obligation. The current Section 5 deception standard already requires the "99% accuracy" claim to be substantiated.
- **FTC staff views on AI and data use** (Office of Technology blog posts, 2024-01-09 and 2024-02-13): staff state that companies that promised not to use customer data for other purposes must keep that promise, and that quietly changing terms to allow new AI uses may be unfair or deceptive. These are staff views, not rules, but they explain why G-036 and G-038 matter.
- **Bulk data thresholds (N51-R04):** recheck the DOJ Data Security Program if vendor contacts pass 100,000 (section 1.4).
- **CCPA:** recheck if the company signs a California customer or its revenue approaches the threshold (section 1.3).
