# Regulatory Gap Analysis: Cris Santos Company | Finance and Insurance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Tier / Vertical | Sole Proprietorship / Finance and Insurance |
| Regulation analyzed | **FTC Safeguards Rule, 16 CFR Part 314** (N52-R03), implementing GLBA section 501(b) (N52-R01). Text read from eCFR, current through 2026-09-23 (last amended 88 FR 77508, 2023-11-13) |
| Also checked | Florida duties that add a security or records obligation: Fla. Stat. 501.171(2), (4), (8) and 517.121 |
| Regulation named in the scenario brief | Interagency Guidelines Establishing Information Security Standards (N52-R02). **Does not apply** (section 1) |
| Assessment dates | 2026-07-13 to 2026-07-17 (self-assessment) |
| Assessor | Owner-adviser, with the on-call IT consultant (services agreement since 2026-07-10). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**Step 1: who registers the adviser?** Advisers Act section 203A(a)(1) (15 U.S.C. 80b-3a(a)(1)) says "No investment adviser that is regulated or required to be regulated as an investment adviser in the State in which it maintains its principal office and place of business shall register" with the SEC unless it has at least $25,000,000 under management or advises a registered investment company. Section 203A(a)(2) extends the bar to mid-sized advisers up to $100,000,000 that must register with, and would be examined by, their home state, and Rule 203A-1(a) (17 CFR 275.203A-1) makes SEC registration optional from $100 million to under $110 million, with no need to withdraw until assets fall below $90 million. With about $19 million under management and no fund clients, **the adviser is prohibited from SEC registration and must register with the Florida OFR** (Fla. Stat. 517.12(3)).

**Step 2: which GLBA safeguards rule follows from that?**
- **SEC Regulation S-P does not apply.** 17 CFR 248.30(d)(3) defines a covered institution as an investment adviser "registered with the Commission". The 2024 amendments (incident response program, 30-day customer notice, 72-hour service provider notice) therefore do not reach a state-registered adviser. Regulation S-ID (17 CFR 248.201(a)(3)) likewise covers only advisers "registered or required to be registered" under the Advisers Act.
- **The FTC Safeguards Rule applies.** GLBA section 505(a)(5) gives the SEC enforcement only over "investment advisers registered with the Commission", and section 505(a)(7) gives the FTC every other financial institution (15 U.S.C. 6805). 16 CFR 314.1(b) names "investment advisors that are not required to register with the Securities and Exchange Commission" among the covered financial institutions.
- **The Interagency Guidelines (N52-R02) do not apply.** They cover banks and bank holding companies; this is a sole proprietorship with no charter. No bank passes them down by contract, because the custodian is a broker-dealer and the adviser is not its service provider.

**Step 3: size exceptions.** 16 CFR 314.6 says 314.4(b)(1), (d)(2), (h), and (i) "do not apply to financial institutions that maintain customer information concerning fewer than five thousand consumers." Customer information here covers about 160 consumers (current and former clients), so four paragraphs are exempt: the written risk assessment, penetration testing and vulnerability scans, the written incident response plan, and the annual report to a board. Every other element of 314.4 applies, and 314.3(a) still requires a written program "appropriate to your size and complexity". The owner chose to keep a written risk assessment (P01) and incident plan (P08) anyway, because the FTC notice duty and Florida's 30-day notice clock need them.

**Florida.** Only duties I could verify are included: registration (517.12(3)), books and records that the OFR examines and can demand (517.121), reasonable data security measures (501.171(2)), 30-day notice to individuals (501.171(4)), and disposal (501.171(8)). Rule 69W-600, F.A.C., could not be retrieved from the Florida rules site during this analysis (it returned a browser challenge), so **no record list or retention period from that rule is stated here.** The compliance consultant is asked to confirm it (G-039).

**Excluded, with reasons (7 rows):**
- **314.4(a)(1) to (a)(3):** apply only when the Qualified Individual is at a service provider or affiliate. The owner is the Qualified Individual.
- **314.4(b)(1), (d)(2), (h), (i):** exempt under 314.6.

## 2. Method
1. **Requirements.** Each paragraph of 16 CFR 314.3 and 314.4 was made one row, using the rule's own numbering; 314.4(c)(1) and (c)(6) were split into their numbered parts. Four Florida statute rows were added. 39 rows in total.
2. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**; no official NIST mapping of Part 314 was found.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant (account security pages, sign-in tests on 2026-07-15, the USB drive, the vendor contracts folder, the file shares on 2026-07-14).
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3 Program and objectives | 0 | 4 | 0 | 0 |
| 314.4(a)-(b) Qualified Individual and risk assessment | 1 | 1 | 1 | 4 |
| 314.4(c) Safeguards | 1 | 4 | 5 | 0 |
| 314.4(d)-(j) Testing, people, providers, adjustment, response, reporting, FTC notice | 0 | 8 | 3 | 3 |
| Florida (501.171, 517.121) | 0 | 3 | 1 | 0 |
| **Total (39)** | **2** | **20** | **10** | **7** |

Of the 30 unmet or partially met rows, 27 are **Required** ("shall") provisions and 3 are **objectives** in 314.3(b) that the program must be designed to achieve. Gap risk: 3 High, 12 Moderate, 15 Low.

## 4. Action list (half page)
In order. The first four cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Turn on MFA for email, CRM, portfolio platform, e-signature, and accounting; password manager | 314.4(c)(5); 314.4(c)(1)(i) | High | 2026-09-15 |
| 2 | Callback to the number on file before any money movement request; letter to clients | 314.3(b)(3) | High | 2026-09-30 |
| 3 | Adopt POL-01 as the written program; designate the Qualified Individual | 314.3(a); 314.4(a) | Moderate | 2026-08-31 (done) |
| 4 | Adopt the P08 runbook with the Florida 30-day clock and the FTC count step | Fla. Stat. 501.171(4); 314.4(j) | Moderate | 2026-09-30 |
| 5 | Encrypted USB drive; secure links instead of attachments; data locations list | 314.4(c)(3); 314.4(c)(2) | Moderate | 2026-09-30 |
| 6 | Monthly review of sign-ins, forwarding rules, and connected apps | 314.4(c)(8) | Moderate | 2026-10-31 |
| 7 | Vendor list, pre-adoption checklist, compliance consultant security terms; no client data in the consumer AI assistant | 314.4(c)(4); 314.4(f) | Moderate | 2026-10-31 |
| 8 | Encrypted cloud backup with 1-year retention | 314.3(b)(2); Fla. Stat. 517.121 | Moderate | 2026-10-31 |
| 9 | Annual security course with a business email compromise module | 314.4(e)(1) | Moderate | 2026-11-30 |
| 10 | Retention and disposal schedule; wipe old devices; confirm the Rule 69W-600 record list | 314.4(c)(6); Fla. Stat. 501.171(8) | Low | 2027-01-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes and triggers to watch
- **No proposed amendment to 16 CFR Part 314** was found in a Federal Register search covering 2024-01-01 to 2026-09-27. The last change was the FTC notification requirement (314.4(j), effective 2024-05-13 under 314.5).
- **Registration trigger.** If assets under management pass $100 million (SEC registration optional) or $110 million (required), the adviser moves to the SEC, and Regulation S-P and S-ID replace the Safeguards Rule. S-P would add a written incident response program, customer notice within 30 days, and service provider notice within 72 hours (17 CFR 248.30(a)(3)-(5)). Rows G-034 and G-035 carry this note.
- **Consumer count trigger.** The 314.6 exemptions end if customer information reaches 5,000 consumers. Rows G-010, G-023, G-032, and G-033 carry this note.
- **FinCEN investment adviser AML rule.** It covers SEC-registered and exempt reporting advisers, and its effective date was delayed to 2028-01-01 (FR Doc. 2025-24184). It does not reach this adviser while it is state-registered.
