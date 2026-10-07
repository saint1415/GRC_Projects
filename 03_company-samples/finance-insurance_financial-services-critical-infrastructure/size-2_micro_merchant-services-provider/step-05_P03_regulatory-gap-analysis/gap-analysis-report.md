# Regulatory Gap Analysis: Cris Santos Company | Financial Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| Tier / Vertical | Micro / Financial Services |
| Primary standard | PCI DSS v4.0.1 (PCI SSC, June 2024), as a **service provider** validating at Visa Level 2 with SAQ D for Service Providers |
| Secondary regulation | FTC Safeguards Rule, 16 CFR Part 314, with the 314.6 small-institution exception |
| Considered and not applicable | Bank service provider notice, 12 CFR 53.4 (C-FINANCIAL-R01), and the other vertical requirements |
| Assessment dates | 2026-07-13 to 2026-07-24 (6.4.3 evidence added 2026-08-05) |
| Assessor | Operations Manager (Qualified Individual) with the MSP lead technician |
| Approved | Owner, 2026-08-31 |

## 1. Applicability
Applicability was decided first, one rule at a time, before any gap was rated. Federal text was checked on the eCFR (point-in-time text for 2026-09-23). Card brand facts come from Visa's public pages, checked 2026-10-06.

### 1.1 PCI DSS v4.0.1: applies, as a service provider (primary)
- **Why it applies.** PCI DSS is not a law. It binds the company through the ISO agreement and the card brands' rules. The PCI DSS glossary treats as a service provider any business that processes, stores, or transmits cardholder data for another entity, or that provides services that control or could affect the security of that data. The company does both:
  - it **transmits** card data when support staff key a sale into a merchant's virtual terminal (about 1,900 a year);
  - it **controls settings that affect card data security** for about 420 merchants: console users, "log in as merchant", and the content of about 120 hosted payment pages.
- **Card brand registration.** Visa requires agents that "perform solicitation activities (ISO) ... or store, process, transmit, or have access to Visa cardholder data" to be registered in its Third Party Agent program before acquirers, issuers, and merchants use their services. The sponsor bank registered the company as an ISO. Visa's Third Party Agent registration page lists a current AOC or an SAQ D for Service Providers as the PCI DSS documents for registration.
- **Validation level: set by the card brands, not by PCI SSC.** Visa's published service provider levels:
  - **Level 1:** over 300,000 Visa transactions a year: annual assessment by a QSA, quarterly ASV scan, and AOC.
  - **Level 2:** fewer than 300,000: annual Self-Assessment Questionnaire, quarterly ASV scan, and AOC.

  The company stores, processes, or transmits about 1,900 transactions a year itself, so it is **Level 2**. The volume its merchants process through the processor partner (about 3.4 million a year) is the processor partner's, not the company's. The ISO agreement requires the SAQ D for Service Providers and AOC by October 30 each year.
- **Service-provider-only requirements.** Assessed as their own rows: 8.2.3 (Met: unique one-time codes for remote support), 11.5.1.1, 12.4.1, 12.4.2, 12.4.2.1, 12.5.2.1, 12.5.3, 12.9.1, 12.9.2. Not applicable, with reasons in the CSV: 3.6.1.1 and 3.7.9 (no keys), 8.3.10.1 (merchant users belong to the processor partner's gateway), 11.4.6 (no segmentation used), 11.4.7 and Appendix A1 (not multi-tenant). 8.3.10 and 10.7.1 are superseded.
- **What is in scope.** The PCI DSS scope is the keyed-entry path plus the console administration (P02 section 7). The 2025 SAQ named only the console. **That understatement is itself a finding** (G-070). The Owner disclosed it to the processor partner on 2026-08-20.
- **Size.** PCI DSS has no small-business exemption. Size changes only the validation method (self-assessment instead of a QSA).

### 1.2 FTC Safeguards Rule, 16 CFR Part 314: applies, with the small-institution exception
- **Financial institution.** The rule covers businesses engaged in an activity that is financial in nature under 12 U.S.C. 1843(k), which incorporates the activities in 12 CFR 225.28 (314.1(b); 314.2(h)(1)). 12 CFR 225.28(b)(14) lists "providing data processing, data storage and data transmission services ... if ... the data to be processed, stored or furnished are financial, banking or economic." Keying card sales for merchants and administering their payment gateway settings are data processing and transmission of financial data. The company therefore treats itself as a financial institution. No other federal functional regulator covers it, so the FTC does.
- **Whose information counts.** "Customer information" is nonpublic personal information about a customer of a financial institution. The rule also covers information about "the customers of other financial institutions that have provided such information to you" (314.1(b)). Merchant owners obtain merchant services for business purposes, so they are not "consumers" (314.2(b)(1)). Their Social Security numbers and bank details are protected by state law and company policy (POL-04), not by Part 314. The company takes the conservative reading for cardholders: card data it handled in keyed entry is counted.
- **The 314.6 exception applies.** 314.6 says that 314.4(b)(1), (d)(2), (h), and (i) "do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers." The company's count:
  - about 1,700 distinct cardholders in the deleted call recordings (2025-05 to 2026-07);
  - about 1,900 keyed sales a year, recorded by the gateway, not by the company;
  - masked card numbers in console reports (not enough to identify a person).

  The total is well under 5,000. The exempt paragraphs are rows G-084, G-095, G-099, and G-100, marked Not applicable. **PCI DSS still requires most of the same things** (a risk analysis under 12.3.1, testing under 11.3 and 11.4, an incident response plan under 12.10), so the exception saves little work. The count is redone each July; if keyed entry grew past 5,000 consumers the exception would lapse.
- **FTC notice, 314.4(j): applies.** The exception does not cover paragraph (j). A "notification event" involving the information of at least 500 consumers must be reported to the FTC as soon as possible and no later than 30 days after discovery (G-101).

### 1.3 Bank service provider notice, 12 CFR 53.4 (C-FINANCIAL-R01): does not apply
- **The test.** Part 53 reaches "bank service providers": a bank service company or other person "that performs covered services," meaning services "subject to the Bank Service Company Act (12 U.S.C. 1861-1867)" (53.2(b)(2), (b)(5)).
- **The company's analysis.** The company performs no service for the sponsor bank of the kind the Bank Service Company Act covers. Its services go to merchants (sales, support, keyed entry) and to the processor partner (boarding packets). The processor partner, not the company, performs the processing and settlement services for the bank. The ISO agreement names no company service as subject to the Act.
- **What the company does instead.** The ISO agreement's own clause requires notice of a suspected compromise to the processor partner and sponsor bank immediately and within 24 hours. That is the operative bank notice (P08). The Owner asked the sponsor bank in writing on 2026-08-24 to confirm this; if the bank designates any company service as a covered service, rows G-102 to G-104 are reopened.

### 1.4 Considered and not applicable
| Requirement | Decision |
|---|---|
| Interagency Guidelines (C-FINANCIAL-R02), 12 CFR 30 App. B | Apply to the sponsor bank. They reach the company only through the ISO agreement's oversight terms |
| NCUA 12 CFR 748.1(c) (C-FINANCIAL-R03) | Not a credit union and serves none |
| SEC Regulation SCI (C-FINANCIAL-R04) | Not an SCI entity |
| NYDFS 23 NYCRR Part 500 (C-FINANCIAL-R05) | Applies only to entities licensed, registered, or chartered under New York banking, insurance, or financial services law. The company holds no New York license. (Even if it did, with fewer than 20 employees it would fall under the limited exemption in 500.19(a).) |
| CIRCIA (C-FINANCIAL-R06) | Proposed rule only (89 FR 23644); no final rule as of 2026-09-25. Tracked in section 5 |
| State breach laws | Apply after a breach in each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example in P08 |
| Florida call recording, Fla. Stat. 934.03(2)(d) | Applies to recorded calls: interception is lawful when all parties have given prior consent. Not a security standard, so not analyzed row by row; tracked as P01 R-015 |

## 2. Method
1. **Requirements.**
   - PCI DSS was decomposed at the requirement level (1.1 to 12.10), with each service-provider-only sub-requirement as its own row, plus the appendices. PCI DSS is copyrighted, so rows give the requirement number and a short topic label in the company's own words. Read the full text in the PCI SSC document library.
   - The Safeguards Rule was decomposed to the paragraph level of 16 CFR 314.4, and 12 CFR 53.4 to its paragraphs.
2. **Crosswalk.** Each row is mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. These are **author mappings**: no official NIST mapping from PCI DSS v4.0.1 or 16 CFR 314 to CSF 2.0 or SP 800-53 was used.
3. **Documentary evidence.** Each status rests on a named record:
   - console user, role, and MFA exports; the console audit log; CRM and suite settings;
   - the phone system administrator settings and a masked sample of recordings (2026-07-21);
   - the firewall and Wi-Fi exports, the MSP's device, patch, and antivirus reports;
   - the 2025 SAQ D and AOC, the ASV reports, the ISO agreement, the processor partner's AOC, and vendor contracts;
   - a walkthrough of the office on 2026-07-16 and interviews with all 7 employees and the MSP lead technician.
4. **Status.** Each row is rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since (for example, the recordings deleted on 2026-08-14) are noted in the remediation column but do not change the status.
5. **Gap risk.** Each gap is rated with the P01 scale. A gap is High when it would leave a PCI DSS requirement "not in place" on the 2026 SAQ in a way that exposes card data, or when it leaves a High risk in P01 untreated.

This is a gap analysis, not a PCI DSS assessment. The SAQ and AOC, signed by the Owner, are the company's formal validation.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| PCI DSS Req. 1 Network security controls | 1 | 3 | 1 | 0 | 5 |
| PCI DSS Req. 2 Secure configurations | 0 | 3 | 0 | 0 | 3 |
| PCI DSS Req. 3 Protect stored account data | 1 | 2 | 2 | 4 | 9 |
| PCI DSS Req. 4 Protect data in transmission | 0 | 2 | 0 | 0 | 2 |
| PCI DSS Req. 5 Anti-malware | 2 | 2 | 0 | 0 | 4 |
| PCI DSS Req. 6 Secure systems and software | 0 | 3 | 1 | 2 | 6 |
| PCI DSS Req. 7 Restrict access by need to know | 1 | 1 | 1 | 0 | 3 |
| PCI DSS Req. 8 Identify and authenticate | 1 | 4 | 1 | 3 | 9 |
| PCI DSS Req. 9 Physical access | 1 | 4 | 0 | 0 | 5 |
| PCI DSS Req. 10 Logging and monitoring | 2 | 3 | 2 | 1 | 8 |
| PCI DSS Req. 11 Security testing | 0 | 4 | 3 | 2 | 9 |
| PCI DSS Req. 12 Policies and programs | 0 | 7 | 8 | 0 | 15 |
| PCI DSS Appendices A1 to A3 | 0 | 0 | 0 | 3 | 3 |
| FTC Safeguards Rule 16 CFR 314.4 | 1 | 10 | 5 | 4 | 20 |
| 12 CFR 53.4 and parallels | 0 | 0 | 0 | 3 | 3 |
| **Total** | **10** | **48** | **24** | **22** | **104** |

Of the 72 gaps (Partially met or Not met), 12 are rated High, 37 Moderate, and 23 Low. PCI DSS accounts for 57 of them: 38 Partially met and 19 Not met.

**What the pattern says:**
- **The base the company inherits is sound.** The processor partner protects its platform, the MSP keeps laptops encrypted, patched, and protected, and the ASV scans pass. Most Met rows are inherited.
- **The gaps are on the company's own side of the line.** Who can sign in to the console (8.4, 7.2, 8.2), what the company puts on payment pages (6.4.3), what it keeps (3.2, 3.3), and what it writes down (12.x).
- **Requirement 12 carries the most Not met rows.** Eight of the 19 PCI DSS Not met rows are program items the company never set up: acceptable use, quarterly reviews, scope confirmation, the merchant responsibility summary, and the incident response plan.
- **One decision removes several gaps.** Stopping the keyed-entry service (P01 R-003) makes 1.3, 2.3, 4.2 (calls), 9.4, and 11.2 moot and takes the office network out of the cardholder data environment.

## 4. Priority gaps
Ten of the 12 High gaps have a target date on or before the 2026 SAQ due date (2026-10-30). The two exceptions: the penetration test (G-058), which the 2026 SAQ will report as not in place with a remediation date, and the incident response plan (G-078), which was approved on 2026-08-31 but will not be tested until the tabletop on 2026-11-30.

| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| G-039 | PCI 8.4 (MFA into the CDE) | High | Require MFA on every console account; MFA on phone administrators | Operations Manager | 2026-09-15 |
| G-090 | 16 CFR 314.4(c)(5) | High | Same, plus the hosting account | Operations Manager | 2026-09-30 |
| G-010, G-011 | PCI 3.2, 3.3 (card data and security codes in recordings) | High | Recordings deleted 2026-08-14; recording off; stop keyed entry | Merchant Support Lead | 2026-10-15 |
| G-028 | PCI 6.4.3 (payment page scripts) | High | Script inventory and approval; unapproved scripts removed 2026-08-12 | Terminal and Integration Technician | 2026-09-30 |
| G-031, G-034 | PCI 7.2, 8.2 (privilege, shared and stale accounts) | High | Limit impersonation; named phone admins; offboarding checklist; reviews | Operations Manager | 2026-09-30 |
| G-050 | PCI 10.4 (log review) | High | Daily console alert digest plus weekly review | Operations Manager | 2026-10-15 |
| G-070 | PCI 12.5 (scope) | High | P02 boundary as the 2026 scope; inventory | Operations Manager | 2026-09-30 |
| G-075 | PCI 12.8 (service providers) | High | Provider list, AOCs, responsibility matrix | Operations Manager | 2026-10-15 |
| G-078 | PCI 12.10 (incident response) | High | POL-03 and P08 runbook; tabletop | Operations Manager | 2026-11-30 |
| G-058 | PCI 11.4 (penetration test) | High | First test of the remaining scope | Operations Manager | 2027-01-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are console settings, one-page procedures, or MSP work, not new systems. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Lock the console | 2026-09-30 | MFA for all console accounts and phone administrators; impersonation limited to support staff; named phone admin accounts; offboarding checklist; Wi-Fi password changed; script inventory; change log; call-back rule for deposit changes; policies approved and acknowledged; scope redrawn | G-005, G-008, G-009, G-010, G-028, G-029, G-030, G-031, G-033, G-034, G-039, G-040, G-045, G-047, G-064, G-065, G-070, G-072, G-082, G-086, G-090, G-092, G-101 |
| 2. Shrink and validate scope | 2026-10-31 | Stop keyed entry 2026-10-15; daily console alerts; targeted risk analyses; service provider list and matrix; merchant responsibility summary; first quarterly review; internal scans; secure upload link; accurate 2026 SAQ and AOC with an action plan (due 2026-10-30) | G-001, G-002, G-003, G-007, G-011, G-013, G-018, G-019, G-024, G-036, G-044, G-046, G-050, G-055, G-056, G-057, G-063, G-066, G-068, G-069, G-071, G-073, G-075, G-077, G-087, G-088, G-089, G-093, G-098 |
| 3. Detection and contracts | 2026-12-31 | EDR; DNS filtering alerts; MSP contract amendment; agent addendum and screening; retention purge; suite log retention; tabletop | G-006, G-020, G-022, G-026, G-042, G-048, G-051, G-053, G-061, G-062, G-067, G-074, G-076, G-078, G-091, G-096, G-097 |
| 4. Testing | 2027-01-31 | First penetration test | G-058 |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk assessment update (July); independent assessment (August) | G-085, G-094 |

**Progress check.** The Operations Manager reports to the Owner at the quarterly PCI review (12.4.2), using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
- **PCI DSS.** v4.0.1 is the current version in the PCI SSC document library. Every future-dated v4.0 requirement took effect on 2025-03-31 and is assessed here as current. No newer version is assumed.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644, 2024-04-04). No final rule had been published as of 2026-09-25. The proposed rule used size criteria tied to SBA small-business standards plus sector criteria; whether a 7-person ISO would be covered depends on the final criteria. **Not a current obligation.**
- **FTC Safeguards Rule.** No pending amendment affects these rows. The 314.6 count is a fact that can change, not a rule change.

The `pending_rule_change` column in `gap-analysis.csv` is "None" for every row, because no proposed rule changes a requirement assessed here.
