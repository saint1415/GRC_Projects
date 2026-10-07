# Regulatory Gap Analysis: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| Tier / Vertical | Sole Proprietorship / Accommodation and Food Services |
| Primary standard | PCI DSS v4.0.1 (PCI Security Standards Council, published 2024-06-11). A contractual standard that reaches the inn through the payment facilitator's sub-merchant agreement, **not law** (N72-R01) |
| Short checks | FTC Act Section 5, 15 U.S.C. 45(a) and (n), with the FTC Rule on Unfair or Deceptive Fees, 16 CFR Part 464 (N72-R02); Fla. Stat. 509.101(2), 501.171(2) and (8) (N72-R04); FTC Disposal Rule 16 CFR 682.3 (N72-R03, not applicable) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-innkeeper, with the on-call IT consultant (under a confidentiality agreement since 2026-07-17). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability

### 1.1 Does PCI DSS reach a one-person inn?
**Yes, by contract.** PCI DSS is not a law, and PCI SSC sets no size exemption. The inn accepts cards as a **sub-merchant of a payment facilitator** built into its innkeeping software. The facilitator's sub-merchant agreement (fictional terms) requires the inn to comply with PCI DSS, to validate every year by self-assessment questionnaire (SAQ) in the facilitator's portal, and to report a suspected compromise within 24 hours. The inn has never validated, and the facilitator has charged a $19.95 monthly non-compliance fee since March 2024. Card-brand merchant levels are set by the brands and were not verified here, so no level number is stated; the facilitator decides how the inn validates.

**Independent, not franchised.** No brand mandates the inn's systems or runs a PCI program for it. *FTC v. Wyndham Worldwide Corp.*, 799 F.3d 236 (3d Cir. 2015), affirmed that the FTC may treat unreasonable cybersecurity as an unfair practice under 15 U.S.C. 45(a); the practices alleged there (card data in clear text, default passwords, no network separation, weak incident response) appear in this inn today at a much smaller scale (row G-068).

### 1.2 Which SAQ? The design decides, not the size
PCI SSC's v4 SAQ family includes SAQ A, A-EP, B, B-IP, C-VT, C, P2PE, SPoC, and D. Eligibility was tested channel by channel against each SAQ's eligibility criteria (summarized in our words; read the official forms):

| Channel | Today's design | SAQ tested | Result |
|---|---|---|---|
| Booking engine | Vendor-hosted page on the innkeeping vendor's own address; the website only links to it; token returned | SAQ A | Fits on its own |
| Card-present | Mobile reader in a PCI-listed validated P2PE solution (listing checked 2026-07-21) | SAQ P2PE | Fits on its own, if the P2PE Instruction Manual is followed |
| Phone bookings | Keyed into the innkeeping payment screen on the family laptop, or written on a paper pad first | SAQ C-VT | **Not eligible:** the laptop is a general-purpose family device, and card data is kept on paper with security codes |
| Card authorization forms | Emailed forms kept in the consumer email account | Any SAQ short of D | **Not eligible:** card data stored electronically |
| OTA virtual cards | Full numbers displayed in the innkeeping software and OTA portals | SAQ A | **Not eligible while numbers are displayed on inn devices** |

**Result for the current design: SAQ D for Merchants.** That is the full merchant questionnaire for a six-room inn, including vulnerability scans and penetration testing (rows G-051, G-052). The rows below assess the inn against that full scope so that every gap is visible.

**Decision: change the design, then validate.** By 2026-10-31 the inn (a) sends phone guests and third-party payers a pay-by-link from the facilitator instead of keying or writing card numbers, (b) shreds the pad pages and purges the email forms, (c) charges OTA virtual cards by token without displaying them, and (d) keeps the booking engine fully outsourced and card-present on the P2PE reader. The inn then validates for 2026 on **SAQ A plus SAQ P2PE**. The facilitator agreed by email on 2026-08-14 (fictional), and the attestations are due 2026-12-31. This removes the laptop, the router, and most of the 62 gap rows from card data scope rather than fixing them one by one. The rows that remain are answered from the official SAQ A and SAQ P2PE forms.

### 1.3 Short checks
- **FTC Act Section 5** applies with no size threshold. Broken privacy or security promises can be deceptive (45(a)(1)); unreasonable security can be unfair when it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits (45(n)).
- **16 CFR Part 464** (90 FR 2066, rule text at 2166; published 2025-01-10; effective 2025-05-12). A "covered good or service" includes short-term lodging "at a hotel, motel, inn, short-term rental, vacation rental, or other place of lodging," and a "business" includes an individual (464.1). Any offer, display, or advertisement of a price must disclose the total price, including mandatory fees, more prominently than other pricing (464.2(a)-(b)). Government charges may be excluded but must be disclosed with the final amount before the guest consents to pay (464.2(c)). Fees must not be misrepresented (464.3). The inn's $15 housekeeping fee is mandatory, so it belongs in the total price.
- **Fla. Stat. 509.101(2):** each operator of a transient establishment must keep a chronological register of guests with dates of occupancy and rates, available to the division, and may keep it electronically; registers more than 2 years old need not be made available. A bed and breakfast inn is a transient public lodging establishment (509.242(1)(f)).
- **Fla. Stat. 501.171(2) and (8):** a "covered entity" includes a sole proprietorship (501.171(1)(b)). It must take reasonable measures to protect electronic personal information and must shred or erase customer records with personal information when they are no longer to be retained. Breach notice under 501.171(3) to (6) is in P08.

**Not applicable, with reasons:** FTC Disposal Rule (no consumer reports: no employees, no background checks); Illinois BIPA (no Illinois operations, no biometrics); CIRCIA (proposed only; far below the SBA size standard); CCPA (no California operations; far below its thresholds); Florida Digital Bill of Rights (a controller must exceed $1 billion in global gross annual revenue and meet one of three further tests); HIPAA and SEC disclosure.

## 2. Method
1. **Requirements.** PCI DSS was broken into its 12 principal requirements and their requirement groups, plus the appendices, with 3.3.1, 6.4.3, and 11.6.1 at the defined-requirement level because they decide scope or carry the largest risk. Labels are short topics written for this analysis, not PCI SSC text, because PCI DSS is copyrighted. Read the requirement text in the official standard.
2. **FTC, Part 464, and Florida rows** cite the text verified on uscode.house.gov, eCFR (2026-09-23), the Federal Register, and the Florida Senate's 2026 statutes.
3. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**. No official NIST mapping from PCI DSS v4.0.1 was used.
4. **Evidence.** Self-attested by the owner and checked on screen with the IT consultant: router and device settings, user lists, the facilitator portal and fee statements, AOCs, a desk drawer review and house walkthrough (2026-07-21), and a mailbox search (2026-07-22).
5. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Area | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| PCI Req 1 Network security controls | 0 | 2 | 3 | 0 | 5 |
| PCI Req 2 Secure configurations | 0 | 1 | 2 | 0 | 3 |
| PCI Req 3 Stored account data | 0 | 0 | 5 | 2 | 7 |
| PCI Req 4 Transmission | 0 | 0 | 2 | 0 | 2 |
| PCI Req 5 Malware and phishing | 0 | 3 | 1 | 0 | 4 |
| PCI Req 6 Secure systems and software | 0 | 2 | 2 | 2 | 6 |
| PCI Req 7 Restrict access | 0 | 1 | 2 | 0 | 3 |
| PCI Req 8 Identify and authenticate | 0 | 0 | 5 | 1 | 6 |
| PCI Req 9 Physical access and devices | 0 | 3 | 2 | 0 | 5 |
| PCI Req 10 Logging | 1 | 3 | 3 | 0 | 7 |
| PCI Req 11 Security testing | 0 | 0 | 5 | 1 | 6 |
| PCI Req 12 Policies and programs | 0 | 3 | 5 | 2 | 10 |
| PCI Appendices A1-A3 | 0 | 0 | 0 | 3 | 3 |
| **PCI DSS subtotal** | **1** | **18** | **37** | **11** | **67** |
| FTC Act Section 5 | 0 | 1 | 1 | 0 | 2 |
| 16 CFR Part 464 (fees) | 1 | 1 | 2 | 0 | 4 |
| FTC Disposal Rule | 0 | 0 | 0 | 1 | 1 |
| Florida Statutes (509.101, 501.171) | 1 | 1 | 1 | 0 | 3 |
| **Total (77)** | **3** | **21** | **41** | **12** | **77** |

Of the 62 rows with gaps, 7 are rated High, 26 Moderate, and 29 Low. Many Low rows are "documented processes and roles" items that POL-01 closes on adoption.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Stop writing card numbers; shred all pad pages; purge card forms from email | G-010, G-011, G-040 | High | 2026-09-15 |
| 2 | MFA on the innkeeping software, email, and OTA-2; password manager; delete saved browser passwords | G-033, G-034 | High | 2026-09-15 |
| 3 | Adopt POL-01 (policy, roles, acceptable use, retention) | G-055, G-056, G-077 | Moderate | 2026-08-31 (done) |
| 4 | Guest Wi-Fi on its own network; change the router password; update firmware | G-003, G-007, G-008, G-024 | Moderate | 2026-09-30 |
| 5 | Adopt and print the P08 runbook with the facilitator's 24-hour notice line | G-064 | High | 2026-09-30 |
| 6 | Show the total price including the $15 fee everywhere; correct the privacy statement and the OTA-2 fee name | G-069, G-070, G-071, G-073 | Moderate | 2026-09-30 |
| 7 | Pay-by-link for phone bookings; front desk role without card display; named relief account | G-012, G-029, G-032 | Moderate | 2026-10-31 |
| 8 | Monthly log review; weekly reader tamper check | G-045, G-041 | Moderate | 2026-10-31 |
| 9 | Owner training and relief innkeeper briefing | G-021, G-060 | Moderate | 2026-11-30 |
| 10 | Scope record and SAQ A plus SAQ P2PE with attestations | G-059 | High | 2026-12-31 |

**Before signing the 2026 SAQs:** actions 1, 2, 5, 7, and 10 must be complete, so that the inn attests to a design it actually runs. High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes and watch items
- **PCI DSS.** v4.0.1 is current. PCI SSC ran a request for comments on v4.0.1 from 2026-06-03 to 2026-07-20 toward the next version; this analysis will be updated when one is published.
- **CIRCIA** final rule not published as of 2026-09-25; it would not reach an inn this size under the proposed size test.
- None of these is treated as a current obligation.
