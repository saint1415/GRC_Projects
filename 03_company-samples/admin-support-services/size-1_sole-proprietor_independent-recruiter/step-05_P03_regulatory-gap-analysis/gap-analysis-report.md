# Regulatory Gap Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship; NAICS 561320) |
| Tier / Vertical | Sole Proprietorship / Administrative and Support and Waste Management and Remediation Services |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`) |
| Secondary rules (binding) | Florida Information Protection Act, Fla. Stat. 501.171(2)-(6) and (8); FACTA Disposal Rule, 16 CFR 682.3 (N56-R01) |
| Checked and found not applicable | FCRA 1681b(b) (N56-R02), Form I-9 (N56-R03), Fla. Stat. 448.095, and N56-R04 to N56-R09 |
| Text verified | eCFR (8 CFR 274a.2; 16 CFR 682) as of 2026-09-23; 2026 Florida Statutes (501.171); 42 U.S.C. 2000e and 12111 from govinfo.gov; EEOC "Coverage of Employment Agencies" page, read 2026-10-06 |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment; mailbox and device search 2026-07-23) |
| Assessor | Owner-recruiter, with the on-call IT support technician (confidentiality agreement since 2026-07-17). Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (122 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
**Step 1 was to find a cybersecurity rule that binds an independent recruiter. None does.** The vertical profile names NIST CSF 2.0 as the primary benchmark because NAICS 56 has no sector-specific federal cyber mandate. Each vertical requirement was checked against this business:

| Candidate | Applies? | Why (citation) |
|---|---|---|
| Form I-9 (N56-R03) | **No** | The vertical row says recruiters and referrers for a fee have their own I-9 duties. The rule narrows that: "all references to recruiters and referrers for a fee are limited to a person or entity who is either an agricultural association, agricultural employer, or farm labor contractor" (8 CFR 274a.2(a)(1)). The business is none of these and has no employees. The partner (for contractors) and the clients (for direct hires) complete the forms |
| FCRA employment screening (N56-R02) | **No** | The owner does not procure consumer reports. The partner and clients do |
| FACTA Disposal Rule (N56-R01) | **Yes** | It reaches anyone who possesses "consumer information" for a business purpose, including records derived from a consumer report (16 CFR 682.1(b), 682.2(b)). Two client-forwarded reports are in the mailbox |
| Fla. Stat. 448.095 (E-Verify) | **No** | Applies to private employers with 25 or more employees; the business has none |
| HIPAA as business associate (N56-R04) | **No** | No clinical placements and no services for covered entities involving PHI |
| TCPA / TSR (N56-R05) | **No for this analysis** | No telemarketing; one-to-one texts with candidates. Consent details were not analyzed |
| PCI DSS (N56-R06) | **No** | No payment cards |
| FAR 52.204-21 (N56-R07) | **No** | No federal contracts |
| NYC Local Law 144 (N56-R08) | **No** | No NYC jobs or candidates for NYC jobs |
| PHMSA security plans (N56-R09) | **No** | No hazardous materials |
| CIRCIA, proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25 |

**Size makes no difference to the rule that does apply.** Fla. Stat. 501.171 defines a "covered entity" as "a sole proprietorship, partnership, corporation, trust, estate, cooperative, association, or other commercial entity that acquires, maintains, stores, or uses personal information" (501.171(1)(b)). There is no headcount or revenue threshold. Its personal information elements include a name with an SSN or a government ID number, and "a user name or e-mail address, in combination with a password or security question and answer that would permit access to an online account" (501.171(1)(g)1.b.). Encrypted data is excluded (501.171(1)(g)2.).

**Decision: use NIST CSF 2.0 as the benchmark**, and assess the two binding rules at requirement level as secondary rows. Status ratings on CSF rows measure the business against its own Target Profile, not a legal duty.

**Also checked, outside this workbook:** Title VII (42 U.S.C. 2000e-2(b) and (k)) and the ADA (42 U.S.C. 12112(b)(6)) apply to the AI match add-on, because the business is an employment agency. Title VII defines one as "any person regularly undertaking with or without compensation to procure employees for an employer" (42 U.S.C. 2000e(c)) with no headcount test of its own, the clients are employers with 15 or more employees, and the EEOC states that a recruitment company that regularly refers employees "is covered no matter how many employees it has." These are assessed in P10.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the 2026 Florida Statutes and the eCFR text current as of 2026-09-23, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the business (High 22, Medium 46, Low 38), set by the owner from the risk register (P01) and BIA (P05). Subcategories that protect SSNs, ID numbers, account access, and breach notice are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping.
4. **Evidence.** Self-attested by the owner and checked on screen with the IT technician: account security pages, the account list (2026-07-22), the mailbox and device search (2026-07-23), the partner agreement and a call with the partner's payroll desk (2026-07-22), vendor terms, and a home office walkthrough (2026-07-21).
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 1 (Partial).** Security has been informal and reactive. **Target: Tier 2 (Risk Informed) by 2027-07**, meaning practices written down and driven by the risk register.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 3 | 13 | 15 | 0 |
| CSF 2.0 Identify (21) | 7 | 5 | 8 | 1 |
| CSF 2.0 Protect (22) | 8 | 9 | 4 | 1 |
| CSF 2.0 Detect (11) | 2 | 1 | 7 | 1 |
| CSF 2.0 Respond (13) | 0 | 0 | 13 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 7 | 0 |
| **CSF 2.0 subtotal (106)** | **20** | **29** | **54** | **3** |
| Fla. Stat. 501.171 (6) | 0 | 1 | 5 | 0 |
| Disposal Rule, 16 CFR 682.3 (1) | 0 | 0 | 1 | 0 |
| Rules found not applicable (9) | 0 | 0 | 0 | 9 |
| **Total (122)** | **20** | **30** | **60** | **12** |

Of the 90 unmet or partially met rows, 9 are rated High, 35 Moderate, 44 Low, and 2 Very Low.

**The pattern:** the SaaS vendors give the business a sound base (encryption at rest, logging, capacity, updates), so most Protect rows are Met or Partially met. The gaps are in what only the owner can do: deciding which data to keep (ID.AM-07, ID.AM-08, PR.DS-01), protecting the accounts (PR.AA-01, PR.AA-03), watching them (DE.CM-03), setting vendor terms (GV.SC-05), and knowing the notice duties (RS.CO-02). Respond and Recover are almost entirely Not met, because nothing existed before the P08 runbook.

The three not applicable CSF rows are ID.RA-08 (no products or public-facing systems that receive vulnerability disclosures), PR.PS-06 (no software development), and DE.CM-02 (no business facility beyond a home office).

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Authenticator-app MFA on email; MFA on the ATS; password manager with unique passphrases | G-053, G-055, G-107 | High | 2026-09-15 |
| 2 | Delete the two background reports and tell clients in writing not to send reports | G-113 | Moderate | 2026-09-30 |
| 3 | Adopt POL-01 (policy, roles, change rule, vendor rules, retention) | G-003, G-017, G-045 | Moderate | 2026-08-31 (done) |
| 4 | Adopt and print the P08 runbook and Florida notice matrix | G-095, G-108 to G-110 | High | 2026-09-30 |
| 5 | Turn on new-sign-in alerts; monthly review of email and ATS logs | G-077 | High | 2026-10-31 |
| 6 | Delete SSNs, dates of birth, and ID images from email, laptop, and phone after the partner confirms its copies; retention schedule | G-037, G-038, G-061, G-112 | High | 2026-10-31 |
| 7 | Monthly ATS export; exit steps | G-031, G-064 | Moderate | 2026-10-31 |
| 8 | Partner security addendum (10-day breach notice, bank changes only through contractor self-service) | G-023, G-026, G-111 | High | 2026-11-30 |
| 9 | Security course for the owner, with payment-fraud and AI-hiring modules | G-059, G-060 | Moderate | 2026-11-30 |
| 10 | Separate work network at home | G-071 | Low | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25; the business would not be covered as proposed.
- **Fla. Stat. 501.171:** the 2026 text was used. State bills were not tracked.
- **Form I-9:** no proposed change to 8 CFR 274a.2(a)(1) was identified; if the business ever recruited for agricultural employers as a farm labor contractor, the I-9 rows would apply.
- **Federal posture on AI and disparate impact** is changing (P10 section 2), but the statutes cited in P10 are unchanged. Nothing in this workbook depends on that posture.
- The `pending_rule_change` column is None for every applicable row.
