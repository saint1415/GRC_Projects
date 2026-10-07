# Regulatory Gap Analysis: Cris Santos Company | Transportation Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments, NAICS 488510) |
| Tier / Vertical | Sole Proprietorship / Transportation Systems |
| Primary regulation named for this vertical | TSA Security Directive 1580/82-2022-01E, Rail Cybersecurity Mitigation Actions and Testing (C-TRANSPORTATION-R01): **not applicable**, directly or through contracts |
| Rules analyzed | FMCSA broker registration and financial security: 49 U.S.C. 13901, 13904; 49 CFR 387.307; 49 CFR part 366 (C-TRANSPORTATION-S09). FMCSA brokers of property: 49 CFR part 371 Subpart A (S10). Fla. Stat. 501.171 (S07). Two contract sources (CT). Federal text read from eCFR (point in time 2026-09-23) and govinfo.gov; Florida text from the Florida Statutes, 2026-10-05 |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment) |
| Assessor | Owner, with the on-call IT consultant. Evidence is self-attested and checked on screen where possible |
| Adopted | 2026-09-08 |

## 1. Applicability
### 1.1 The TSA rail directives do not apply, directly or through contracts
Both rail cyber directives reach "each freight railroad carrier identified in 49 CFR 1580.101 and other TSA-designated" railroads (the Small sample in this vertical read the directive texts; rows G-001 and G-002). A broker is not a railroad carrier, and TSA has never contacted the business. The directives also do not arrive through contracts: the largest shipper's agreement and the railroads' portal terms were read on 2026-08-12 and neither passes down directive requirements. The portal terms do impose their own credential rules, which are analyzed as contract rows (G-034).

### 1.2 Neither do the other TSA rail rules, SSI, or the hazmat security plan rule
- **49 CFR part 1580** (and through it 1570.201 and 1570.203) covers five kinds of person in 1580.1(a): freight railroad carriers, rail hazardous materials shippers, rail hazardous materials receivers in an HTUA, host railroads, and owners or operators of private rail cars. A broker who places car orders as a shipper's agent is none of them (G-003). The shippers and railroads keep their own duties.
- **SSI (49 CFR part 1520):** the business is not a covered person today. It would become one under 1520.7(j) if it were given access to SSI, so POL-01 tells the owner to decline SSI (G-004).
- **Hazmat security plans (49 CFR 172.800):** apply to persons who offer or transport the listed materials. The business declines hazmat loads (G-005).

### 1.3 What does bind the business
- **FMCSA broker registration.** A person may provide service as a broker for motor carrier transportation "only if the person is registered" (49 U.S.C. 13901(a)). Registration stays in effect only while the $75,000 surety bond or trust fund does (13904(b); 49 CFR 387.307(a)). The 2023 financial responsibility rule, effective 2026-01-16, added the immediate suspension process in 387.307(e): if the broker does not respond within 7 business days to a claim the surety finds valid, the surety may pay, and a payment that takes the bond below $75,000 leads FMCSA to suspend the broker's authority within 7 business days of notice unless the bond is restored. **For a one-person business, a security incident that stops carrier payments, or an absence that leaves a claim unanswered, can now cost the broker its authority within weeks.** There is no size threshold.
- **Part 371 Subpart A** applies to all brokers of transportation by motor vehicle (371.1). The record duty in 371.3 is the business's core information duty: six data elements per transaction, kept three years, open to review by each party. Conduct rules with no information-handling element (371.9 rebating and gifts; 371.10, which binds a broker to the bill and payment rules of the person it acts for) are outside a security gap analysis; the owner self-attests compliance.
- **The rail side has no FMCSA rule.** Part 371 defines a broker by "transportation of property by an authorized motor carrier" (371.2). The rail coordination work is governed by the shipper's own rail arrangements and the railroads' portal terms.
- **Fla. Stat. 501.171.** A "covered entity" includes a sole proprietorship that acquires, maintains, stores, or uses personal information (501.171(1)(b)). The business holds owner-operator Social Security numbers, some driver license numbers, and driver location data, all elements of "personal information" in 501.171(1)(g)1.a. when combined with a name. So the reasonable-measures duty (501.171(2)) and the notice duties apply. The disposal duty in 501.171(8) is written for "customer records" (information an individual gives to obtain a service); carriers sell services rather than buy them, so the owner applies that standard to carrier records as a policy choice (G-031).
- **Contracts.** The largest shipper's master agreement (safeguards and 72-hour incident notice) and the railroads' portal terms (individual IDs, no sharing) bind by contract (G-032 to G-034).

## 2. Method
1. **Requirements.** Rows follow each rule's own structure (statute subsection or CFR paragraph) at the most granular citation that can be checked separately. Brief quotes are used; this is public-domain federal and state text. Contract rows summarize the clause.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has published no mapping for these rules.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant where possible: the FMCSA public record and account settings (2026-08-11), a sample of 60 TMS loads and the shipper and carrier templates (2026-08-12), the bond and BOC-3 copies, and the sharing report from P04.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| A. Applicability (TSA directives, part 1580, SSI, hazmat, household goods) | 0 | 0 | 0 | 6 |
| B. FMCSA registration and financial security (S09) | 5 | 3 | 1 | 0 |
| C. FMCSA part 371 Subpart A records and conduct (S10) | 6 | 5 | 0 | 0 |
| D. Fla. Stat. 501.171 (S07) | 0 | 2 | 3 | 0 |
| E. Contract flow-down (CT) | 0 | 1 | 2 | 0 |
| **Total (34)** | **11** | **11** | **6** | **6** |

Of the 17 unmet or partially met rows, 1 is rated High, 8 Moderate, and 8 Low.

**The pattern.** The business is in good standing with FMCSA on paper: registration, bond, process agent, and the six record elements are all in place. The gaps sit where those duties depend on security. The transaction records live in one vendor's system (G-022); the FMCSA account recovers to a personal email and the contact details are stale (G-010); and the new 7-business-day surety and suspension windows have no one but the owner to answer them (G-012, G-013). Florida's reasonable-measures duty is the one High gap (G-027), for the same reasons that drive the High risks in P01.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | MFA on the TMS, accounting, and load board; authenticator app on email; carrier packets only in the TMS | Fla. Stat. 501.171(2) | High | 2026-09-30 |
| 2 | Update the FMCSA phone number; move account recovery to the business email | 49 U.S.C. 13904(g) | Moderate | 2026-09-30 |
| 3 | Registered name and MC number on the signature, load board profile, and quote template | 49 CFR 371.7(a); 49 U.S.C. 13901(c) | Low | 2026-10-31 |
| 4 | Owner confirms the BOL number on every POD review (automatic capture is not trusted alone) | 49 CFR 371.3(a)(3) | Low | 2026-09-30 |
| 5 | Stop using the shared railroad login; request an individual user ID | Railroad portal terms | Moderate | 2026-10-31 |
| 6 | Adopt the P08 runbook with the 72-hour shipper notice and the Florida 30-day notice | Fla. Stat. 501.171(3)-(4); shipper agreement | Moderate | 2026-10-31 |
| 7 | Quarterly export of transaction records; POL-01 retention and disposal schedule | 49 CFR 371.3(b); Fla. Stat. 501.171(8) | Moderate | 2026-12-31 |
| 8 | Surety notices to the business email; attorney authorized to answer surety and FMCSA notices; backup broker agreement | 49 CFR 387.307(e) | Moderate | 2026-12-31 |
| 9 | Remove the record review waiver from the carrier agreement | 49 CFR 371.3(c) | Low | 2026-12-31 |
| 10 | Answer the shipper's 2026 security questionnaire from P09 | Shipper agreement | Moderate | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01). Gaps tied to the controls assessed in P07 also appear in the P07 POA&M.

## 5. Pending regulatory changes
- **FMCSA Transparency in Property Broker Transactions NPRM** (89 FR 91648, 2024-11-20; comment period reopened at 90 FR 9702, 2025-02-18; RIN 2126-AC63). **Still proposed:** no final rule was found in the Federal Register as of 2026-10-05. FMCSA's summary says it "would revise the regulatory text to make clear that brokers have a regulatory obligation to provide transaction records to the transacting parties on request" and "make changes to the format and content of the records." Flagged on G-018, G-020, G-022, and G-023. Removing the waiver clause now (action 9) costs nothing either way.
- **FMCSA registration system.** FMCSA announced Motus, its new registration system, at 91 FR 23144 (2026-04-29), to be introduced in phases. This is a system change, not a new duty; the owner rechecks account recovery and MFA settings after moving (G-010).
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR part 226, 89 FR 23644; C-TRANSPORTATION-R07). No final rule has been published. As proposed, it would not cover this business: proposed 226.2(a) reaches entities that exceed the SBA size standard (this business is SBA-small), and the transportation criteria in proposed 226.2(b)(14) list railroads, transit, over-the-road buses, pipelines, aircraft and airport operators, indirect air carriers, and cargo screening facilities, not freight brokers.
- **TSA Enhancing Surface Cyber Risk Management NPRM** (89 FR 88488; C-TRANSPORTATION-R06). Still proposed; it would apply to certain pipeline, freight and passenger rail, and over-the-road bus owner/operators, not to brokers.

None of these proposals is treated as a current obligation. The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
