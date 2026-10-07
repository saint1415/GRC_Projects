# Regulatory Gap Analysis: Cris Santos Company | Information Technology | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Tier / Vertical | Sole Proprietorship / Information Technology |
| Vertical primary regulation | FedRAMP (C-IT-R01). **Does not apply**: the company has no federal customer (section 1.1) |
| Requirement set analyzed | FTC Act Section 5 (15 U.S.C. 45(a), 45(n)) measured against the FTC's own business guidance; Fla. Stat. 501.171 duties of a third-party agent and covered entity; the company's own public statements, Terms of Service, and questionnaire answers |
| Applicability checks only | C-IT-R01 to C-IT-R06 (FedRAMP, CMMC, DFARS, DOJ Data Security Program, bank service provider rule, CIRCIA); CCPA |
| Assessment dates | 2026-08-17 to 2026-08-21 (self-assessment; tests on 2026-08-19 with the contract security consultant) |
| Assessor | Owner. Evidence is self-attested, checked on screen with the consultant where possible |
| Sources checked | FTC "Start with Security" headings re-read on ftc.gov on 2026-10-05; Fla. Stat. 501.171 (2026) read on leg.state.fl.us; vertical requirements file (verified 2026-09-25) |
| Adopted | 2026-09-28 |

## 1. Applicability
### 1.1 The vertical's primary regulation does not apply at this size
| ID | Requirement | Applies? | Why |
|---|---|---|---|
| C-IT-R01 | FedRAMP (44 U.S.C. 3607-3616) | **No** | FedRAMP governs cloud services that federal agencies use. It has no size threshold; it applies because of the customer. The company has no federal customer and resells another provider's platform. If an agency ever asked, the upstream provider's own FedRAMP status would decide what is possible, not the reseller's |
| C-IT-R02 | CMMC (32 CFR Part 170) | **No** | No DoD contracts or subcontracts. If a customer discloses that it handles federal contract information or CUI in its hosted mailboxes, recheck before renewing that customer |
| C-IT-R03 | DFARS 252.204-7012 | **No** | No covered defense information; no clause flowed down |
| C-IT-R04 | DOJ Data Security Program (28 CFR Part 202) | **No, on current facts** | The rule restricts covered data transactions that give countries of concern or covered persons access to bulk U.S. sensitive personal data. The company has none: the freelancer is U.S.-based and the upstream servers are in U.S. data centers. The shopper data (about 38,000 accounts) is mostly contact data and is below the 100,000-person bulk threshold for covered personal identifiers in `requirements.csv`. Recheck when adding any vendor with access to customer data (G-039 asks two vendors where data is stored) |
| C-IT-R05 | Bank service provider notification (12 CFR 53.4; 225.303; 304.24) | **No** | No bank customers. If a bank becomes a customer and its contract treats the hosting as a covered service, the "as soon as possible" notice for incidents disrupting covered services for four or more hours would apply |
| C-IT-R06 | CIRCIA | **Not in force** | No final rule as of 2026-09-25. Tracked in section 5 |
| n/a | CCPA (Cal. Civ. Code 1798.140(d)) | **No** | The company's revenue (about $180,000) is far below the $26,625,000 threshold, it does not buy, sell, or share personal information of 100,000 or more consumers, and it earns nothing from selling personal information |

### 1.2 What does apply
**FTC Act Section 5.** Section 5(a) declares unfair or deceptive acts or practices in or affecting commerce unlawful (15 U.S.C. 45(a)(1)). The company is a for-profit business selling to customers in six states, outside the statutory carve-outs, and **there is no size threshold**. Two theories matter:
- **Unfairness** (15 U.S.C. 45(n)): a practice that causes or is likely to cause substantial injury to consumers that they cannot reasonably avoid and that is not outweighed by benefits. Shoppers of the 12 online stores, and the tenants whose rental applications sit in a customer's mailbox, cannot protect data held on the company's platform.
- **Deception:** the website security claims and questionnaire answers are representations to customers.

Section 5 lists no controls, so the requirement set is the FTC's own business guidance:

| Source | URL | Rows |
|---|---|---|
| Start with Security: A Guide for Business (10 lessons, 28 practices) | https://www.ftc.gov/business-guidance/resources/start-security-guide-business | G-001 to G-028 |
| Protecting Personal Information: A Guide for Business | https://www.ftc.gov/business-guidance/resources/protecting-personal-information-guide-business | G-029, G-030 |
| Data Breach Response: A Guide for Business | https://www.ftc.gov/business-guidance/resources/data-breach-response-guide-business | G-031 |

**Fla. Stat. 501.171.** The company is a **third-party agent** for its customers, because it is "contracted to maintain, store, or process personal information on behalf of a covered entity" (501.171(1)(h)). The customers' sites and mailboxes hold personal information as the statute defines it: shopper user names or emails with passwords (501.171(1)(g)1.b.), and Social Security and driver license numbers in rental applications (501.171(1)(g)1.a.). The duties are reasonable measures (501.171(2)), notice to the customer **no later than 10 days** after determining a breach or having reason to believe one occurred, with all the information the customer needs (501.171(6)(a)), and disposal (501.171(8)). For its own portal sign-ins and billing contacts, the company is a covered entity (rows G-032 to G-036). A violation is treated as an unfair or deceptive trade practice in an action by the Department of Legal Affairs (501.171(9)(a)).

**The company's own statements** (rows G-037 to G-042): the website, the Terms of Service, and the 2026 questionnaire answers.

## 2. Method
1. **Requirements.** Each practice in the three FTC guides became one row, cited by guide, lesson, and practice heading (FTC guidance is a U.S. government work). Each Florida duty became one row cited by subsection. Each public statement or contract promise became one deception row.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. This is an **author mapping**; no official NIST or FTC mapping of this guidance exists.
3. **Evidence.** Self-attested by the owner and checked on screen where possible: account lists, the spreadsheet and email review on 2026-08-19, the website captured on 2026-08-17, the security service report of 2026-08-18, vendor terms, and calls to three customers about what their sites and mailboxes hold.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Requirement set | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FTC Start with Security (reasonable security) | 28 | 5 | 15 | 7 | 1 |
| FTC Protecting Personal Information | 2 | 0 | 2 | 0 | 0 |
| FTC Data Breach Response | 1 | 0 | 0 | 1 | 0 |
| Fla. Stat. 501.171 | 5 | 0 | 2 | 3 | 0 |
| Deception: public statements and contract promises | 6 | 0 | 3 | 3 | 0 |
| **Total** | **42** | **5** | **22** | **14** | **1** |

Of the 36 rows that are not met or partially met, 9 are rated High, 22 Moderate, and 5 Low. The one N/A row is G-025 (paper and removable media), because the company keeps none.

**The main finding.** The owner protects the owner's own accounts well (unique passwords, MFA on email and the reseller console, an encrypted laptop). The gaps are in the tools that reach every customer: the portal administrator login (G-005), the contractor's dashboard access (G-004, G-016), the credential spreadsheet (G-007), and the lack of monitoring (G-014). Two legal gaps need no money to fix: the 10-day notice procedure (G-033) and the false backup claim (G-037).

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Correct the website claims and send corrected questionnaire answers | G-037, G-038, G-039, G-042 | High | 2026-10-15 |
| 2 | MFA on the portal administrator login and every dashboard account; freelancer limited to assigned sites; only the owner holds system-wide rights | G-004, G-005, G-016 | High | 2026-10-15 |
| 3 | Stop pasting customer data into the consumer AI tool; delete laptop copies | G-003 | Moderate | 2026-09-30 |
| 4 | 10-day customer notice procedure, templates, and a security contact for every customer | G-033, G-031, G-034 | High | 2026-10-31 |
| 5 | Weekly log review and sign-in alerts; human review of protected AI-dismissed findings | G-014, G-024 | High | 2026-10-31 |
| 6 | Customer credentials into a password manager vault; rotate all 140 | G-007, G-006, G-027 | High | 2026-10-31 |
| 7 | Security addendum for the freelancer; vendor list with security terms | G-021, G-015, G-041 | Moderate | 2026-10-31 |
| 8 | Close and delete closed customers' accounts after export | G-002, G-035 | Moderate | 2026-11-30 |
| 9 | Patching for hosting-only sites: monthly notices, free automatic security updates, Terms of Service clause | G-023, G-008 | High | 2026-12-31 |
| 10 | Independent 30-day backups for every site, then quarterly restore tests | G-019, G-037 | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and, for the assessed controls, the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Pending regulatory changes
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. If finalized as proposed, covered entities would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours. The proposed rule covers entities above the SBA size standard or meeting a sector-based criterion; this company is far below the size standard, and whether any sector-based criterion would reach a hosting reseller depends on the final text. Not a current obligation. Flagged on G-033.
- **No pending change to Fla. Stat. 501.171 or the FTC guidance** was identified during this review. Recheck each August with the risk review.
