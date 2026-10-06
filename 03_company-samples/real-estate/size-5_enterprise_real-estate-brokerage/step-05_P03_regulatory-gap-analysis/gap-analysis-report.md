# Regulatory Gap Analysis: Cris Santos Company | Real Estate and Rental and Leasing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded residential real estate brokerage) with Cris Santos Title and Escrow, LLC and Cris Santos Relocation, LLC; 9 states |
| Tier / Vertical | Enterprise / Real Estate and Rental and Leasing |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314 (N53-R01), applied to Title and Escrow. Text read from eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023; 314.4(j) effective May 13, 2024 under 314.5) |
| Other regulations analyzed | SEC Form 8-K Item 1.05 and Reg S-K Item 106 (N53-R05); CCPA/CPRA and the CPPA regulations on cybersecurity audits, risk assessments, and ADMT (N53-R03); Colorado SB26-189; FTC Act Section 5 (N53-R02); Florida escrow and trust fund rules as the worked example of state escrow law; RESPA affiliated business disclosures (12 CFR 1024.15); FCRA adverse action and disposal (15 U.S.C. 1681m(a); 16 CFR 682.3); state breach and data security laws (Florida worked example); FinCEN residential real estate rule (vacated); PCI DSS (N53-R04, contractual) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14); FinCEN, HUD, and SEC status rechecked 2026-10-06 |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Chief Privacy Officer; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO (Qualified Individual), 2026-09-04, after evidence was refreshed with P07 results through 2026-08-28; roadmap reviewed by the executive risk committee 2026-09-08 and the risk committee of the board 2026-09-10; Safeguards Rule results reported to the Title and Escrow board of managers 2026-09-15 |

## 1. Applicability
### 1.1 Which entity is the "financial institution" under the Safeguards Rule?
The rule applies to financial institutions under FTC jurisdiction: entities whose business is engaging in an activity that is financial in nature under section 4(k) of the Bank Holding Company Act, including the activities listed in 12 CFR 225.28 and 225.86 (314.1(b), 314.2(h)(1)). An entity must be **significantly engaged** in the activity (314.2(h)(1)). The rule attaches to each legal entity, so each was tested separately:

| Entity and line | Financial activity? | Basis |
|---|---|---|
| Cris Santos Title and Escrow, LLC: settlement (closing) services | **Yes** | "An entity that provides real estate settlement services is a financial institution" (314.2(h)(2)(x), citing 12 CFR 225.28(b)(2)(viii)). Title and Escrow acts as settlement agent in about 88,000 closings a year and disburses about $34 billion from 31 trust accounts. Footnote 5 to 225.28(b)(2)(viii) excludes title insurance as principal, agent, or broker from settlement services, so the conclusion rests on the settlement and disbursement work, not on the title agency license |
| Parent: residential sales brokerage | **No** | Brokerage is not listed in 12 CFR 225.28. The nearest listed activity, acting as a **finder** (314.2(h)(2)(xiii); 12 CFR 225.86(d)(1)), excludes any activity that requires a real estate agent or broker license (12 CFR 225.86(d)(1)(iii)(D)) |
| Parent: property management and leasing | **No** | Leasing real property is financial only on a nonoperating basis (12 CFR 225.28(b)(3)(i)); the company manages and maintains the homes it leases |
| Cris Santos Relocation, LLC | **No** | Administers home-sale and move programs that corporate clients fund; it does not lend, extend credit, or buy homes for its own account. This conclusion is reviewed if Relocation ever offers equity advances or guaranteed buyouts |
| Mortgage brokerage joint venture (49%) | **Yes, but not this program** | A mortgage broker is a financial institution (314.2(h)(2)(xi)). The unaffiliated operating partner controls the joint venture and runs its program on its own systems; the company sends it referred leads only |

**The parent's role.** The parent provides IT, security, HR, and finance services to Title and Escrow under the 2021 intercompany services agreement, so it is Title and Escrow's **affiliate** and its **service provider** (314.2(r)). The Qualified Individual (the CISO) is a parent employee, so 314.4(a)(1)-(3) applies: Title and Escrow retains responsibility, the President of Title and Escrow directs and oversees the Qualified Individual, and the parent must maintain a program that protects Title and Escrow (G-004). The parent's systems that hold Title and Escrow's customer information, or that connect to systems that do (314.2(j)), are in scope. **Decision:** the company runs **one enterprise program** for all entities, so every control tested here is a common control.

**Which information is covered.** Customer information is nonpublic personal information about a customer of a financial institution (314.2(d)). A consumer who obtains real estate settlement services has a customer relationship (314.2(e)(2)(i)(K)). Brokerage-only client data, tenant data, and relocation data are not customer information in the rule's sense; they are protected by the same program under FTC Act Section 5 (N53-R02), state law, and the CCPA.

**Size exception.** 314.6 exempts institutions with customer information on fewer than 5,000 consumers. Title and Escrow holds customer information on about 1.2 million consumers, so **the full rule applies**. FTC notice under 314.4(j) applies to notification events involving at least 500 consumers.

GLBA privacy notice duties are handled by the Chief Privacy Officer and are outside this security gap analysis.

### 1.2 SEC disclosure (N53-R05)
The company is an SEC registrant and not a smaller reporting company. Form 8-K Item 1.05 and Reg S-K Item 106 apply in full. The definition of a cybersecurity incident in 17 CFR 229.106(a) includes "a series of related unauthorized occurrences", which matters for a BEC campaign that produces many small losses (G-065; P08 section 5).

### 1.3 California and Colorado (N53-R03; SB26-189)
- **CCPA business.** The company does business in California and its annual gross revenue is far above the threshold, so it is a business under Civ. Code 1798.140(d). Data subject to GLBA (Title and Escrow's customer information) is exempt at the data level (1798.145(e)), but the exemption does not apply to the breach right of action in 1798.150.
- **Cybersecurity audit.** The revenue threshold is met and the company processed personal information of about 410,000 California consumers in 2025 (consumer website, CRM, and brokerage records), so a cybersecurity audit is required (Cal. Code Regs. tit. 11, 7120). With 2026 revenue above $100 million, the first audit covers 2027-01-01 to 2028-01-01 and the report is due 2028-04-01 (7121(a)(1)).
- **ADMT and risk assessments.** Tenant screening (AI-001) is used for California homes. The screening score is ADMT because leasing staff follow it without the review the regulation calls human involvement. The FCRA exemption (1798.145(d)) covers the use of the consumer report itself to the extent the FCRA regulates it, but not the model's use of application data (income, rental history, applicant statements). The company therefore treats the decision as in scope. It must comply by 2027-01-01 (7200(b)), either with a Pre-use Notice, opt-out or human appeal, and access rights (7220-7222), or by redesigning the process so a trained reviewer with authority decides each adverse case. A risk assessment is required for ADMT used for a significant decision (7150(b)(3)) and, for processing that predates the regulations, by 2027-12-31 (7155(b)).
- **Colorado SB26-189.** Tenant screening for Colorado homes is a consequential decision in a covered domain, the lease of residential real estate in Colorado (C.R.S. 6-1-1701(6)(c) as enacted). The act takes effect 2027-01-01 and applies to decisions made on or after that date. As a deployer, the company must give notice (6-1-1704(1)-(2)), give post-adverse outcome disclosures within 30 days (6-1-1704(3)), offer correction and human review on request (6-1-1705(1)), and keep records for at least three years (6-1-1703). The Attorney General enforces the act; it creates no private right of action. Advertising, marketing, and differentiated product recommendations are excluded from consequential decisions, so buyer lead scoring (AI-002) is outside it.

### 1.4 Other rules considered
| Rule | Applies? | Where handled |
|---|---|---|
| FTC Act Section 5 (N53-R02) | Yes, no size threshold | G-089; P01; P10 |
| State escrow and license law (Florida worked example: Fla. Stat. 475.25; ch. 61J2-14; 626.8473) | Yes, in each state; Florida rows are the worked example | G-048 to G-058 |
| RESPA affiliated business arrangements (12 CFR 1024.15) | Yes, for referrals to Title and Escrow and the mortgage joint venture | G-059, G-060 (disclosure records live in SYS-01) |
| FCRA adverse action and disposal | Yes, for tenant screening | G-061, G-063; P10 |
| State breach notification and data security laws | Yes, in each state where affected individuals reside (Florida worked example: Fla. Stat. 501.171) | G-085 to G-088; P08 |
| Fair Housing Act (42 U.S.C. 3604) | Yes | P10 |
| FinCEN residential real estate rule (31 CFR 1031.320) | **Not in effect.** Vacated by the U.S. District Court for the Eastern District of Texas on 2026-03-19; FinCEN, with the Department of Justice, has appealed. FinCEN states that reporting persons are not required to file and are not liable while the order remains in force (FinCEN website checked 2026-10-06). It would reach Title and Escrow as settlement agent, not the brokerage | G-062 (watch) |
| PCI DSS (N53-R04) | Contractual only; no company system stores, processes, or transmits cardholder data | G-090; P04 |
| Florida Digital Bill of Rights (Fla. Stat. 501.701 et seq.) | No: revenue exceeds $1 billion, but the company meets none of the other criteria in the controller definition in Fla. Stat. 501.702 (50% or more of revenue from online advertising, a consumer smart speaker service, or an app store) | None |
| SOX Section 404 | Separate program; IT general controls over SYS-12 are tested by the SOX program | P01 R-052 |
| CIRCIA | Not in force: final rule not published as of 2026-09-25; reporting to CISA is voluntary | P08 |

## 2. Method
1. **Decompose.** Each paragraph of 16 CFR 314.3, 314.4, and 314.6 became a row, split where one paragraph holds two separable duties (for example, encryption in transit and at rest in 314.4(c)(3)). Other regulations were broken into citation-level duties from primary text: eCFR (17 CFR 229.106, 12 CFR 1024.15, 16 CFR 682.3, 31 CFR 1031.320), the U.S. Code (15 U.S.C. 1681m), the CPPA's published regulation text and the CCPA statute as posted by the CPPA, the enrolled Colorado SB26-189, and the Florida statutes and rules. Only provisions that bear on security, funds integrity, AI decisions, notification, or disclosure were included.
2. **Requirement type.** The Safeguards Rule has no required/addressable split. Its elements are mandatory, with three built-in alternatives: Qualified Individual-approved compensating controls for encryption (314.4(c)(3)), written approval of equivalent controls instead of MFA (314.4(c)(5)), and continuous monitoring instead of annual penetration testing and semiannual vulnerability assessments (314.4(d)(2)). One alternative is in use: compensating controls for the legacy file servers (G-014).
3. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **These are author mappings.** No official NIST mapping of these regulations was found.
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random or stratified as noted. **34 rows were tested by sampling or full-population analytics; 21 found exceptions.**
5. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FTC Safeguards Rule (N53-R01) | 26 | 20 | 0 | 1 | 47 |
| Florida broker escrow (Florida worked example) | 6 | 2 | 0 | 0 | 8 |
| Florida title agency trust funds (Florida worked example) | 2 | 1 | 0 | 0 | 3 |
| RESPA affiliated business arrangements | 2 | 0 | 0 | 0 | 2 |
| FCRA (tenant screening) | 1 | 1 | 0 | 0 | 2 |
| FinCEN residential real estate rule | 0 | 0 | 0 | 1 | 1 |
| SEC Form 8-K Item 1.05 (N53-R05) | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 (N53-R05) | 5 | 0 | 0 | 0 | 5 |
| CCPA/CPRA and CPPA regulations (N53-R03) | 1 | 5 | 3 | 0 | 9 |
| Colorado SB26-189 (ADMT) | 0 | 1 | 3 | 0 | 4 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| FTC Act Section 5 (N53-R02) | 1 | 0 | 0 | 0 | 1 |
| PCI DSS v4.0.1 (N53-R04) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **48** | **33** | **6** | **3** | **90** |

**Safeguards Rule:** 26 Met, 20 Partially met, 0 Not met, 1 Not applicable (47 rows). No element is wholly unmet; the gaps concentrate in agent identity, acquired firms, legacy data, third parties, and incident records.

**Gap risk levels across all regulations (39 rows with gaps):** High 11, Moderate 16, Low 12. All 6 Not met rows are new state AI obligations (California ADMT and Colorado SB26-189) that take effect 2027-01-01.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-002 | 314.3(b) | Design does not yet close the main diversion paths | Complete POAM-001, POAM-005, and POAM-006 | CISO | 2027-03-31 |
| G-010 | 314.4(c)(1)(i) | 9 of 60 sampled agent departures kept access more than 7 days; 1,940 of 28,600 external Hub accounts inactive more than 90 days still enabled | Automated agent departure feed (POAM-002); external account inactivity job (POAM-017) | Executive Vice President, Brokerage Operations | 2027-01-31 |
| G-011 | 314.4(c)(1)(ii) | Least privilege broken for bank channel secrets | Rotate and vault secrets; pipeline guardrail (POAM-010) | Director of Closing Platform Engineering | 2026-10-31 |
| G-021 | 314.4(c)(8) | Authorized user activity not monitored in the legacy tenants | SIEM connectors and alerts (POAM-003) | Director of Security Operations | 2026-12-15 |
| G-057 | Fla. Stat. 626.8473(4) | Trust funds can move on an unverified or singly approved instruction | Bank-enforced dual approval at AQ-09 and migration (POAM-005); independent callback numbers and verification coverage (POAM-006) | President, Title and Escrow | 2027-03-31 |
| G-064 | Form 8-K Item 1.05; SEC Release 33-11216 | No fraud-loss (BEC) scenario; the committee has never assessed a funds-diversion case | Add fraud-loss criteria and run a BEC tabletop with the disclosure committee on 2026-11-17 (POAM-008) | General Counsel | 2026-11-30 |
| G-065 | Form 8-K Item 1.05 (materiality determination); 17 CFR 229.106(a) (definition includes a series of related unauthorized occurrences) | No method to assess a series of related occurrences; 3 diverted wires in 2026 H1 were never assessed together | Related-incident aggregation method and quarterly look-back (POAM-008) | General Counsel | 2026-11-30 |
| G-078 | Cal. Code Regs. tit. 11, 7200(b); 7220 | Notice missing; compliance date 2027-01-01 | Pre-use Notice in the application, or human review that removes the use from the ADMT definition (POAM-021) | President, Property Management | 2026-12-15 |
| G-079 | Cal. Code Regs. tit. 11, 7221 | No opt-out or qualifying appeal | Human appeal path with trained reviewers (POAM-021) | President, Property Management | 2026-12-15 |
| G-081 | C.R.S. 6-1-1704(1)-(2) (as enacted by SB26-189) | Notice missing | Point-of-interaction notice for Colorado applications (POAM-021) | President, Property Management | 2026-12-15 |
| G-082 | C.R.S. 6-1-1704(3) (as enacted by SB26-189) | No post-adverse outcome disclosure | Colorado adverse outcome disclosure in SYS-10 (POAM-021) | President, Property Management | 2026-12-15 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Bank API secrets vaulted (POAM-010); AQ-09 bank-enforced dual approval (POAM-005 interim); BEC disclosure tabletop and playbook update (POAM-008); legacy tenant SIEM connectors (POAM-003); external Hub account cleanup (POAM-017); emergency change enforcement (POAM-009); ADMT notices, appeal path, and Colorado disclosures (POAM-021); overdue vendor reviews and contract amendments (POAM-012); AI committee reviews of the remaining 5 use cases (POAM-019); CPPA audit scope and auditor decision (POAM-020); intercompany agreement amendment (G-004) | 314.4(a)(3), (c)(1), (c)(7), (c)(8), (f); 626.8473(4); Item 1.05; 7120-7122; 7220-7222; C.R.S. 6-1-1703 to 6-1-1705 | Vault inventory; bank settings; tabletop report; SIEM source list; notices and appeal records; vendor reviews |
| 2027 Q1 | Agent passkeys and session binding (POAM-001); agent departure feed (POAM-002); payee verification to 98% (POAM-006); legacy tenant migration (POAM-004); consumer second factor (POAM-014); Disbursement Hub DR retest (POAM-011); AQ-09 migration (POAM-005); local bias testing for tenant screening (POAM-019); Internal Audit test of Item 106 statements | 314.4(c)(1), (c)(5), (c)(8), (h); 626.8473(4); Item 106; Fair Housing Act | Authentication reports; verification coverage report; DR test report; bias test results |
| 2027 Q2 | Transaction platform contract amendment and fallback test (POAM-007); legacy file disposal and encrypted archive (POAM-013); CPPA-format risk assessments (POAM-020) | 314.4(c)(2), (c)(3), (c)(6); 7150-7155 | Contract; fallback test; disposal certificates; risk assessments |
| 2027 Q3 and later | Annual risk assessment and gap reassessment; first CPPA audit period runs through 2027; audit report and risk assessment submission due 2028-04-01 | All | Updated P01 and P03; CPPA audit report |

## 6. Pending regulatory changes
- **Safeguards Rule.** No proposed amendment to 16 CFR Part 314 was found in a Federal Register search through 2026-10-06. The last change was the notification amendment (88 FR 77499, Nov. 13, 2023).
- **FinCEN residential real estate rule.** Vacated, with the government's appeal pending (section 1.4). If the vacatur is reversed, Title and Escrow would need a reporting procedure for non-financed transfers to entities and trusts. G-062 carries a watch note.
- **HUD disparate impact rule.** HUD proposed on 2026-01-14 (91 FR 1475) and in a supplemental proposal on 2026-08-10 (91 FR 51416) to change its implementation of the Fair Housing Act's disparate impact standard. Both are proposals; no final rule was found as of 2026-10-06. This affects P10, not the Safeguards Rule.
- **SEC.** No SEC proposal to amend or rescind Item 1.05 or Item 106 was found in the Federal Register as of 2026-10-06, so both remain in force.
- **Colorado.** The Attorney General must adopt rules to implement 6-1-1705 on or before 2027-01-01, and may add detail to the post-adverse outcome disclosures. G-081 to G-083 carry watch notes.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an FTC inquiry, a state real estate commission or insurance department audit, a CPPA request, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk assessment, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the Qualified Individual's annual reports to the Title and Escrow board of managers (2025 and 2026);
- trust account reconciliations, positive pay exception logs, and payee verification reports;
- FTC notification event log and state notification files;
- AI governance committee records and ADMT notices (from P10).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-09-04. The roadmap was reviewed by the executive risk committee on 2026-09-08 and the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, with a targeted refresh of the California and Colorado rows in 2027-01.
