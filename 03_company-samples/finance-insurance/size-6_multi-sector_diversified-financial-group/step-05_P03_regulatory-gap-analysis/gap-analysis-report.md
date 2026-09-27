# Regulatory Gap Analysis: Cris Santos Company Holdings | Finance and Insurance | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (bank holding company; three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Finance and Insurance (focus division: Banking) |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards as issued by the OCC, 12 CFR Part 30, Appendix B, with Supplement A (N52-R02). Text read from eCFR, current through 2026-09-23 |
| Bank secondary rules | OCC heightened standards (12 CFR 30 App. D; the bank is a covered bank); Computer-Security Incident Notification (12 CFR Part 53; holding company: 12 CFR 225 Subpart N) |
| Division regulations | Financial Software: Bank Service Company Act (12 U.S.C. 1867(c)), bank service provider notice rules (12 CFR 53.4, 225.303, 304.24), the Federal Reserve's Guidelines through the holding company program (12 CFR 225 App. F), SOC 2 commitments, FTC Act Section 5. Commercial Real Estate: 12 CFR 225 App. F through the holding company program, state breach laws, SAR duties of nonbank subsidiaries (12 CFR 225.4(f)) |
| Gap tables | `gap-analysis.csv` (Banking, 56 rows); `gap-analysis-financial-software.csv` (31 rows); `gap-analysis-commercial-real-estate.csv` (23 rows) |
| Assessment dates | 2026-05-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-31) |
| Assessors | Division security and compliance leads with the Group Chief Compliance Officer's team, coordinated by the Head of Technology and Cyber Risk (second line); reviewed by group internal audit |

## 1. Applicability
### 1.1 Which GLBA safeguards rule applies to which entity
GLBA section 505(a) (15 U.S.C. 6805(a)) decides which agency enforces the safeguards standard for each kind of institution. The answer drives everything below.

| Entity | Enforcing agency under 6805(a) | Safeguards standard | Basis (read from primary text) |
|---|---|---|---|
| Cris Santos Bank, N.A. | OCC (6805(a)(1)(A): national banks and their subsidiaries) | 12 CFR 30 App. B | App. B I.A applies to customer information maintained by or on behalf of national banks |
| Cris Santos Company Holdings, Inc. (parent) | Federal Reserve (6805(a)(1)(B): bank holding companies and their nonbank subsidiaries or affiliates) | 12 CFR 225 App. F | App. F I.A; II.A requires the holding company to make sure each subsidiary is subject to a comprehensive program |
| Financial Software and Data Services (nonbank subsidiary) | Federal Reserve (6805(a)(1)(B)) | 12 CFR 225 App. F, through the group program | Its customers are institutions; client institutions' customers are not its consumers (12 CFR 1016.3(e)(2)(v)) |
| Commercial Real Estate: CRE Lending and Group Property Management (nonbank subsidiaries) | Federal Reserve (6805(a)(1)(B)) | 12 CFR 225 App. F, through the group program | Borrowers and guarantors obtain credit for business purposes, so few records are GLBA customer information (1016.3(e)(1)) |

**Decision on the FTC Safeguards Rule (the question the brief asked).** The FTC Safeguards Rule (16 CFR Part 314) does **not** apply to the Commercial Real Estate division, or to any group entity. Section 314.1(b) limits the rule to financial institutions "not otherwise subject to the enforcement authority of another regulator under section 505", and 6805(a)(1)(B) places bank holding companies and their nonbank subsidiaries under the Federal Reserve. CRE Lending is a "financial institution" in the ordinary sense (lending is listed in 12 CFR 225.28(b)(1)), but its safeguards duty runs through the holding company's program under 12 CFR 225 App. F. Group legal recorded this decision on 2026-06-12 (`gap-analysis-commercial-real-estate.csv`, RE-G01). The Safeguards Rule's elements are still useful as a benchmark, and group policy already meets most of them.

**Why Group Property Management can exist inside a bank holding company.** It holds and operates only premises used by the bank and manages foreclosed property for the bank (Bank Holding Company Act section 4(c)(1)(A) and (C), 12 U.S.C. 1843(c)(1)). It does not manage property for outside owners, because the permissible servicing activity in 12 CFR 225.28(b)(2)(vi) excludes real property management. This scope decision also keeps the division out of residential tenant screening and fair housing questions.

### 1.2 Size and designation tests
- **No size exemption** applies to the Guidelines. Section II.A of App. B and App. F requires a program "appropriate to the size and complexity" of the institution. At $212 billion in bank assets, every III.C.1 measure the bank "must consider" is appropriate, so each is assessed as if required.
- **Heightened standards apply.** App. D applies to any bank with average total consolidated assets of $50 billion or more (App. D I.A). The bank is a covered bank. Because its assets are about 94% of the parent's, below the 95% test in App. D I.4, it keeps its own risk governance framework and relies on group components in consultation with the OCC (I.5, I.6). Selected App. D paragraphs that bear on cyber and third-party risk are rows G-043 to G-056. App. D is written as guidelines ("should"); rows are typed accordingly.
- **Incident notification applies to all three levels:** the bank (53.1(c)), the holding company (225.300(c)), and the Financial Software division as a bank service provider (53.1(c), 225.300(c), and the FDIC's 304.24).
- **Bank Service Company Act.** Services the Financial Software division performs for its 212 client banks are subject to examination by each client's federal banking agency (1867(c)(1)). The 98 credit union clients are supervised by the NCUA, which is not an "appropriate Federal banking agency", so the Act does not reach those relationships; they rest on contract.

### 1.3 Excluded requirements, with reasons
- **App. B III.G** (implementation dates of 2001 to 2006): historical and already passed.
- **FTC Safeguards Rule:** see 1.1.
- **NYDFS Part 500:** no group entity holds a New York banking, insurance, or financial services license.
- **SEC Regulation S-P and S-ID:** no broker-dealer, investment adviser, investment company, or transfer agent in the group.
- **NAIC Model #668:** no insurance licensee in the group.
- **FedRAMP, COPPA, FCC CPNI:** no federal customers, no child-directed services, no carrier operations.
- **PCI DSS for Commercial Real Estate:** rent is collected by ACH; no card acceptance. The bank's card data sits with the card processor (bank service provider) and is outside this analysis.

## 2. Regulation-by-division matrix
| Requirement | Banking | Financial Software | Commercial Real Estate | Group (holding company) |
|---|---|---|---|---|
| N52-R01 GLBA (15 U.S.C. 6801-6809) | Applies | Applies (Federal Reserve jurisdiction) | Applies, limited customer information | Applies |
| N52-R02 Guidelines, OCC version (12 CFR 30 App. B and Supp. A) | **Primary** | Flow-down through client banks' contracts (III.D) and as the bank's own service provider | Group Property Management and CRE Lending are service providers to the bank (III.C.1.b; III.D) | n/a |
| N52-R02 Guidelines, Federal Reserve version (12 CFR 225 App. F and Supp. A) | n/a (the bank is excluded from "subsidiary", App. F I.C.2.f) | Applies through the group program | **Primary for the division** | **Applies**: program must cover every nonbank subsidiary (II.A) |
| OCC heightened standards (12 CFR 30 App. D) | Applies (covered bank) | Its services to the bank are technology services the bank must govern | n/a | Parent framework components relied on by the bank |
| Incident notification (12 CFR 53.3; 225.302) | Applies (OCC notice within 36 hours of determination) | n/a as a banking organization | n/a as a banking organization | Applies (Federal Reserve notice within 36 hours of determination) |
| Bank service provider notice (12 CFR 53.4; 225.303; 304.24) | Receives notices (inbound) | **Applies** to client banks' designated contacts | n/a | n/a |
| Bank Service Company Act (12 U.S.C. 1867(c)) | Its outside providers are examinable | **Applies** (examinable service provider) | n/a | n/a |
| SAR rules | 12 CFR 21.11 | 12 CFR 225.4(f) | 12 CFR 225.4(f) | 12 CFR 225.4(f) |
| Identity theft red flags | 12 CFR 41.90 (OCC) | n/a (no covered accounts) | n/a (commercial accounts; not reviewed further) | n/a |
| ECOA and Regulation B (12 CFR Part 1002) | Applies (AI credit model; P10) | Client banks' duty; developer documentation needed (P10) | Applies to business credit; AI-008 (P10) | Group AI Standard |
| N52-R03 FTC Safeguards Rule | Not applicable (OCC) | Not applicable (Federal Reserve) | **Not applicable** (Federal Reserve; section 1.1) | Not applicable |
| N51-R01 FTC Act Section 5 | Not applicable (banks carved out, 15 U.S.C. 45(a)(2)) | Applies | Applies | Applies to nonbank entities |
| N51-R04 DOJ Data Security Program (28 CFR Part 202) | Applies (bulk financial data) | Applies | Applies | Group vendor screening |
| N51-R03 / N53-R03 CCPA | GLBA data exempt at the data level | Non-GLBA data only | Non-GLBA data only (under counsel review) | Group privacy program |
| Colorado SB26-189 | Deployer duties for Colorado applicants, under counsel review (P10) | Developer duties for the cash-flow score, under counsel review | Not reviewed (commercial lending) | Group AI Standard |
| State breach notification laws | Each state where affected individuals reside (Fla. Stat. 501.171 worked example) | Third-party agent duties to clients where state law sets them | Guarantor and tenant personal information | Coordinates |
| N52-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| SOC reporting (contractual) | Uses providers' SOC reports (P09 review) | Issues SOC 1 and SOC 2 Type 2 (P09) | Out of scope for SOC 2 (P09) | Group services carved in |

## 3. Method
1. **Requirements.** Each paragraph of App. B sections II and III is one row; III.C.1.a has two parts and gets two rows. Supplement A's response-program and customer-notice paragraphs were added because III.C.1.g requires a response program. App. D, Part 53, 225 Subpart N, App. F, and the Bank Service Company Act rows were read from the eCFR and the U.S. Code. SOC 2 rows list Trust Services Criteria IDs with short topic labels in our own words (the AICPA text is not reproduced).
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of these Guidelines or rules was found.
3. **Evidence.** Interviews with each division's leadership; board and committee minutes; contracts and intercompany agreements; configuration exports; the P07 test results; a sample of 60 bank wires and 30 CRE loan fundings.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**The FFIEC IT Examination Handbook** is how examiners assess the Guidelines. The ffiec.gov site could not be reached from this environment, so its examination procedures are not quoted; the FFIEC Cybersecurity Assessment Tool was retired on 2025-08-31. This is why the analysis maps to CSF 2.0 and SP 800-53.

## 4. Results
### 4.1 Banking (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| App. B II Standards (program and objectives) | 4 | 1 | 0 | 0 |
| App. B III.A Involve the board | 2 | 0 | 0 | 0 |
| App. B III.B Assess risk | 2 | 1 | 0 | 0 |
| App. B III.C Manage and control risk | 8 | 5 | 0 | 0 |
| App. B III.D Oversee service providers | 0 | 3 | 0 | 0 |
| App. B III.E to III.G Adjust, report, implement | 2 | 0 | 0 | 1 |
| Supplement A (response programs, customer notice) | 8 | 1 | 0 | 0 |
| Part 53 and 225.302 (incident notification) | 1 | 3 | 0 | 0 |
| App. D heightened standards (selected) | 11 | 3 | 0 | 0 |
| **Total (56)** | **38** | **17** | **0** | **1** |

Of the 17 partially met rows: 6 are **Required** ("shall") provisions, 4 are **III.C.1 measures** the bank must consider and has judged appropriate, 3 are **Rule** provisions of Part 53 or 225.302, 3 are **App. D** guidelines, and 1 is **Supplement A** guidance. Gap risk: 1 High, 12 Moderate, 4 Low.

The bank is mature: its own controls meet the Guidelines. Every gap sits where the bank depends on the rest of the group:
- **Affiliates are not overseen like vendors** (G-010, G-024 to G-026, G-035, G-047). The bank reviews every outside critical vendor's SOC reports but has never reviewed those of the affiliate that runs its digital channels, and the 2021 intercompany agreement has no incident notice term. App. D makes this sharper: the platform provides technology services the bank depends on, yet it is neither a front line unit inside the bank nor a monitored third party.
- **Shared identity** (G-012, High). Affiliate support staff can read the bank tenant's configuration and user lists, and a stolen 12-hour session reaches it.
- **Cross-division notification** (G-019, G-039, G-042). The determination criteria do not cover incidents that start in an affiliate or a deliberate platform suspension (P08 is built on exactly that case).

### 4.2 Financial Software (`gap-analysis-financial-software.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Bank Service Company Act | 2 | 0 | 0 | 0 |
| Bank service provider notification (53.4, 225.303, 304.24) | 1 | 5 | 0 | 0 |
| Credit union clients (contract) | 0 | 1 | 0 | 0 |
| Client banks' Guidelines duties that flow to the division | 2 | 2 | 0 | 0 |
| Holding company program (App. F) | 2 | 0 | 0 | 0 |
| SOC 2 commitments | 0 | 4 | 1 | 1 |
| Client contracts | 0 | 2 | 0 | 0 |
| FTC Act, DOJ rule, CCPA, Colorado, FedRAMP, COPPA, CPNI, SEC | 3 | 1 | 1 | 3 |
| **Total (31)** | **10** | **15** | **2** | **4** |

**Not met:** the cash-flow data service is missing from the SOC 2 system description (FS-G16, High); and there is no developer documentation for the data service, which Colorado SB26-189 would require for Colorado client banks from 2027-01-01 and which all 64 client banks need anyway for their own model risk and Regulation B reviews (FS-G27).

**The notice gap in numbers.** The division holds a bank-designated point of contact (53.4(a)(1)) for 151 of 212 client banks. For the other 61, notice must go to the CEO and CIO (53.4(a)(2)), and those contacts are current for only 80% of them. In the P08 scenario, a 5.5-hour suspension of business wires would have required notices to every client bank as soon as possible.

### 4.3 Commercial Real Estate (`gap-analysis-commercial-real-estate.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| FTC Safeguards Rule | 0 | 0 | 0 | 1 |
| Holding company program (12 CFR 225 App. F) | 6 | 8 | 2 | 0 |
| State breach notification laws | 0 | 1 | 0 | 0 |
| SAR duties (225.4(f)) | 0 | 1 | 0 | 0 |
| Service provider duties to the bank | 0 | 1 | 0 | 0 |
| CCPA, PCI DSS, SEC | 1 | 1 | 0 | 1 |
| **Total (23)** | **7** | **12** | **2** | **2** |

**Not met:** funding instructions accepted by email with callbacks to numbers in the closing package (RE-G06, High: 9 of 30 sampled fundings); and no payment-fraud training for closers and funding staff (RE-G13, High). App. F III.E expressly names mergers and acquisitions as a trigger for adjusting the program; the 2024 integration covered identity and email but not policies, funding controls, or retention (RE-G16).

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | CRE funding on emailed instructions; no closer training (1) | CRE, Bank | App. F III.C.1.a, III.C.2 | High | Group callback standard; bank verified-instruction service; training | Director of loan closing and funding | 2026-11-30 |
| 2 | Shared sessions and support console reach (6, and P07) | All | App. B III.C.1.a; SOC 2 CC6.1, CC6.3 | High | Device-bound sessions; tenant-scoped support access | Group CISO; Head of Digital Banking Platform | 2026-12-31 |
| 3 | AI data service documentation and SOC 2 description (4) | FS, Bank | SOC 2 CC2.3; Colorado SB26-189; 12 CFR 1002.9 | High | Developer documentation; description update; reason code remap (P10) | Financial Software data services lead | 2026-12-31 |
| 4 | Bank service provider notice contacts (3) | FS | 53.4(a)(1)-(2); 225.303; 304.24 | Moderate | Contacts for all 212 client banks; 4-hour timer | Client risk and assurance director | 2026-10-31 |
| 5 | Affiliate oversight by the bank (3) | Bank, FS, CRE | App. B III.D.1-3; Supp. A II.A.2; App. D II.C.1 | Moderate | Due diligence, amended agreements, SOC review, CUEC mapping | Head of Technology and Cyber Risk | 2026-12-31 |
| 6 | Cross-division notification (5) | All | App. B III.C.1.g; 53.3; 225.302 | Moderate | P08 matrix; affiliate and suspension triggers; tabletop | Group General Counsel | 2026-12-15 |
| 7 | CRE supplement and inheritance (2) | CRE | App. F II.A, III.C.3, III.E | Moderate | Re-issue supplement; inheritance matrix | Commercial Real Estate security and compliance lead | 2027-01-31 |
| 8 | Business payment MFA in client tenants (6) | FS | Client contracts; SOC CUECs | Moderate | Mandatory MFA default | Head of Digital Banking Platform | 2027-03-31 |
| 9 | Payment gateway resilience | Bank | App. B III.C.1.h | Moderate | Hot standby; failover test | Head of Commercial Payments Operations | 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-012, POAM-015, POAM-019, and POAM-022 to POAM-024 trace directly to this analysis).

## 6. Pending changes to watch
- **Third-party guidance.** The June 2023 Interagency Guidance on Third-Party Relationships (88 FR 37920) is current. On 2026-09-15 the OCC, Federal Reserve, FDIC, and NCUA **proposed** replacement guidance (91 FR 58536; comments due 2026-11-16). The agencies also issued a Joint Statement on Community Banks' Engagement with Core Service Providers (2026-09-11). The Financial Software division is a digital banking provider rather than a core provider, but its community bank clients will apply the same transparency expectations to it. None of this changes the Guidelines' own III.D text; affected rows carry a watch note.
- **Colorado SB26-189** takes effect 2027-01-01. Its enforcement posture is unsettled (litigation and federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`). It is tracked, not treated as settled.
- **Regulation B.** The 2026 amendment (91 FR 21620, effective 2026-07-21) states in 1002.6(a) that the Act does not provide for the "effects test". The small business data collection rule (Regulation B subpart B) now has a compliance date of 2028-01-01 for institutions with at least 1,000 covered originations in each of 2026 and 2027 (12 CFR 1002.114(b)(1)). Both affect P10, not the Guidelines.
- **No proposed amendment to 12 CFR Part 53 or 225 Subpart N** was found in a Federal Register search covering 2023-01-01 to 2026-09-25. CIRCIA reporting is not in effect (final rule not published as of 2026-09-25).
