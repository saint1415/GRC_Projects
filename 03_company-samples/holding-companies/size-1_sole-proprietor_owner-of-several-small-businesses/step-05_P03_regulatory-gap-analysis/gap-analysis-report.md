# Regulatory Gap Analysis: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (the owner's management business for three wholly owned Florida LLCs: Storage, Rentals, Laundry) |
| Tier / Vertical | Sole Proprietorship / Management of Companies and Enterprises |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, as a **voluntary portfolio profile** for the Shared Back-Office Platform, with a note on each row where an LLC differs |
| Binding rules checked | Fla. Stat. 501.171 (2026 statute, read 2026-10-06); for Rentals: FCRA user duties (15 U.S.C. 1681b, 1681m), the FTC Disposal Rule (16 CFR 682.3, eCFR as of 2026-09-23), and the Fair Housing Act (42 U.S.C. 3603-3604) |
| Also recorded | Card processor merchant terms (contract); N55-R01 to N55-R07, all not applicable |
| Assessment dates | 2026-07-27 to 2026-07-31 (self-assessment) |
| Assessor | Owner-manager, with the on-call IT technician (under a confidentiality and security agreement since 2026-07-24). Evidence is self-attested, checked on screen where possible |
| Workbook | `gap-analysis.csv` (124 rows) |
| Adopted | 2026-08-31 |

## 1. Applicability
**Step 1 was to find the rule that binds the holding business. None of the vertical's parent-level rules does.** A holding company's cyber duties come from what it is (public or private, bank holding company or not) and from what its companies do.

| Candidate | Applies? | Why (citation) |
|---|---|---|
| **N55-R01** SEC Regulation S-K Item 106 (17 CFR 229.106) | **No** | Regulation S-K governs registration statements and Exchange Act reports (17 CFR 229.10(a)). No entity has registered securities or files reports |
| **N55-R02** Form 8-K Item 1.05 | **No** | Applies to SEC registrants; same reason |
| **N55-R03** SOX section 404 (15 U.S.C. 7262) | **No** | Applies to issuers filing Exchange Act reports |
| **N55-R04** Federal Reserve incident notification (12 CFR 225.300-225.303) | **No** | Applies to bank holding companies and others listed in 225.300; no entity controls a bank (225.2(c)) |
| **N55-R05** 12 CFR Part 225, Appendix F | **No** | Same reason |
| **N55-R06** HIPAA, group health plans | **No** | No entity sponsors a group health plan, and no LLC is a health care provider |
| **N55-R07** CIRCIA (proposed 6 CFR Part 226) | **No (proposed)** | No final rule as of 2026-09-25 |
| FTC Safeguards Rule (16 CFR Part 314) | **No** | No LLC is a financial institution under 314.2(h): none extends consumer credit, brokers loans, or gives financial advice. Rentals maintains and repairs its units, so its leases are not the nonoperating leases that 12 CFR 225.28(b)(3) lists as a financial activity. Accepting cards it did not issue does not by itself make a business a financial institution (see the retailer example in 314.2(h)(4)(ii)) |
| Florida Digital Bill of Rights (Fla. Stat. 501.702) | **No** | A controller must exceed $1 billion in global gross annual revenue and meet one of three further tests (online advertising revenue, a smart speaker service, or a large app store). Combined revenue is about $750,000 |

**Decision: NIST CSF 2.0 is the benchmark, as a portfolio profile.** This follows the vertical profile: a private holding business that owns no bank has no binding group-level cyber rule, and CSF 2.0's Govern function is built for the question that matters here: one person, one identity, and four legal entities. The profile rates the shared back office once, because every LLC inherits it, and notes on each row where an LLC is different (`llc_differences`). CSF 2.0 is not binding; status ratings measure the business against a voluntary target. Three subcategories are not applicable at this size (ID.RA-08 and PR.PS-06, no software is developed; PR.AA-04, no federated sign-on).

**The binding rules sit with each LLC.** Holding the LLCs through one owner does not merge their duties. Each LLC answers for its own data:
- **Fla. Stat. 501.171.** The definition of "covered entity" includes a sole proprietorship and any other commercial entity that "acquires, maintains, stores, or uses personal information" (501.171(1)(b)). **Each LLC is a separate covered entity** for its own tenants, applicants, customers, and employees, with its own 30-day notice clock and its own count toward the 500-person Department notice. **The sole proprietorship is each LLC's third-party agent** (501.171(1)(h)): it is contracted under the management agreements to maintain and process that information, so it must "take reasonable measures to protect and secure" the data (501.171(2)), dispose of customer records properly (501.171(8)), and notify the LLC of a breach of a system it maintains within 10 days (501.171(6)(a)).
- **Rentals: FCRA, Disposal Rule, and Fair Housing Act.** Rentals obtains consumer reports on applicants who apply (a legitimate business need in connection with a business transaction initiated by the consumer, 15 U.S.C. 1681b(a)(3)(F)(i)), must give adverse action notices when a decision is based in whole or in part on a report (1681m(a)), and must dispose of consumer information properly (16 CFR 682.3(a)). The Fair Housing Act (42 U.S.C. 3604) governs tenant selection, and neither exemption in 3603(b) fits: the units are in duplexes, not single-family houses, and the owner lives in none of them. That matters for the AI assistant (P10).
- **Storage and Laundry** take card payments only through processors; PCI DSS reaches them through the merchant agreements (contract, one row).

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from `00_universal-framework/frameworks/csf2_core.csv`. Statute and regulation rows cite the 2026 Florida Statutes, the eCFR text current as of 2026-09-23, and the U.S. Code (govinfo, 2023 edition), with short quotes or paraphrases.
2. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`; `sp800_53_controls` is a key-control subset chosen by the author. Statute and regulation rows use an **author mapping**.
3. **Evidence.** Self-attested by the owner, checked on screen with the IT technician where possible: user lists and security settings in all seven SaaS services (2026-07-29), a file listing of the suite (2026-07-29), router and gate settings and a walkthrough of both sites (2026-07-28), and the P07 tests (2026-07-30).
4. **Status.** Met, Partially met, Not met, or Not applicable, as of fieldwork. Gap risk uses the P01 scale.
5. **Traceability.** None of the vertical's requirement IDs (N55-R01 to N55-R07) applies, so `regulatory_driver` columns in all deliverables cite the statute or the CSF subcategory directly (for example "Fla. Stat. 501.171(2)" or "CSF 2.0 portfolio profile PR.AA-03 (voluntary)").

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 2 | 17 | 12 | 0 |
| CSF 2.0 Identify (21) | 4 | 8 | 8 | 1 |
| CSF 2.0 Protect (22) | 3 | 13 | 4 | 2 |
| CSF 2.0 Detect (11) | 0 | 2 | 9 | 0 |
| CSF 2.0 Respond (13) | 0 | 0 | 13 | 0 |
| CSF 2.0 Recover (8) | 0 | 2 | 6 | 0 |
| **CSF 2.0 subtotal (106)** | **9** | **42** | **52** | **3** |
| Fla. Stat. 501.171 (6) | 0 | 2 | 4 | 0 |
| FCRA user duties, Rentals (2) | 1 | 1 | 0 | 0 |
| FTC Disposal Rule, Rentals (1) | 0 | 0 | 1 | 0 |
| Fair Housing Act, Rentals (1) | 0 | 1 | 0 | 0 |
| Card processor terms, contractual (1) | 0 | 1 | 0 | 0 |
| N55-R01 to N55-R07 (7) | 0 | 0 | 0 | 7 |
| **Total (124)** | **10** | **47** | **57** | **10** |

Of the 104 unmet or partially met rows, 8 are rated High, 44 Moderate, and 52 Low. All 8 High rows are CSF subcategories: ID.RA-06, ID.IM-04, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-02, PR.DS-11, and RS.CO-02.

**The pattern.** The business now knows its risks (the 2026 risk assessment and BIA meet ID.RA-03 to ID.RA-05 and ID.AM-05), and vendors protect data in transit and their own platforms. The gaps cluster in three places: **identity** (one phishable email account administers four entities; shared and stale accounts at the LLCs), **response** (all 13 Respond subcategories are Not met, and nobody knew that each LLC is a separate covered entity with its own 30-day clock), and **data life cycle** (Rentals' applications and screening reports, and Storage's license scans, are kept forever in general file storage).

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | App-based MFA on every administrator account; hardware key for email and banking; password manager with unique passphrases | PR.AA-03, PR.AA-01; Fla. Stat. 501.171(2) | High | 2026-09-15 |
| 2 | Callback rule for any new or changed payee; payee changes by the owner only; payment fraud briefing for the owner and bookkeeper | PR.AT-02 | High | 2026-09-30 |
| 3 | Individual Laundry PINs and delegated mailbox; Storage desktop sign-in and encryption; gate password changed; hire and departure checklist | PR.AA-01, PR.AA-05, GV.RR-04, PR.DS-01 | High | 2026-09-30 |
| 4 | Adopt POL-01 and the P08 runbook with the four-entity notice map; print contacts; walkthrough | GV.PO-01, RS.CO-02, ID.IM-04; Fla. Stat. 501.171(3)-(6) | High | 2026-08-31 (adopted); 2026-09-30 (walkthrough) |
| 5 | Written tenant selection criteria; adverse action notice whenever a report contributes; no AI in applicant selection | 15 U.S.C. 1681m(a); 42 U.S.C. 3604; POL-01 9.5 | Moderate | 2026-09-30 |
| 6 | Reduce the bookkeeper's role; separate administrator account; quarterly account review for every LLC system | PR.AA-05 | High | 2026-10-31 |
| 7 | Retention schedule; delete old application downloads and license scans with a deletion record; wipe devices before disposal | ID.AM-08; Fla. Stat. 501.171(8); 16 CFR 682.3 | Moderate | 2026-10-31 |
| 8 | Backup service for suite mail and files; monthly exports; first restore test | PR.DS-11, RC.RP-03 | High | 2026-10-31 |
| 9 | Vendor list with notice contacts; confidentiality and security terms with the bookkeeper; close the former payroll account | GV.SC-04, GV.SC-05, GV.SC-10; Fla. Stat. 501.171(6) | Moderate | 2026-10-31 |
| 10 | Sealed access sheet and recovery codes for the successor manager; Storage manager authority; bank signer question | ID.IM-04, PR.IR-03 | High | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes and triggers (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. Recheck when final.
- **Fla. Stat. 501.171** was read as the 2026 statute; state bills were not tracked.
- **Structural triggers that would change this analysis:** an LLC offering consumer credit or owner financing (the Safeguards Rule could apply, 16 CFR 314.2(h)); any LLC or a new acquisition growing past 1,000 people's personal information (consumer reporting agency notice, 501.171(5)); hiring the first employee of the sole proprietorship itself; sponsoring a health plan (N55-R06); registering securities (N55-R01 to N55-R03). The profile is refreshed each July and before buying or selling a business.
