# Regulatory Gap Analysis: Cris Santos Company | Finance and Insurance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank; OCC-supervised national bank) |
| Tier / Vertical | Small / Finance and Insurance |
| Regulation analyzed | Interagency Guidelines Establishing Information Security Standards, as issued by the OCC: 12 CFR Part 30, Appendix B, with Supplement A (N52-R02). Text read from eCFR, current through 2026-09-23 |
| Secondary regulation | Computer-Security Incident Notification Rule, 12 CFR Part 53, and the parallel Federal Reserve rule for the holding company, 12 CFR 225 Subpart N |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | IT Manager (Information Security Officer) with the Compliance Officer and the outsourced internal audit firm |

## 1. Applicability
The Guidelines **apply**. Section I.A of Appendix B says they apply to customer information maintained by or on behalf of national banks and their subsidiaries, and the bank is a national bank. They implement section 501(b) of the Gramm-Leach-Bliley Act (N52-R01) and section 39 of the Federal Deposit Insurance Act.

There is no size exemption. Section II.A requires a program "appropriate to the size and complexity" of the bank. That lets a $510 million bank choose simpler ways to meet each standard, but not skip one. Section III.C.1 works like an "addressable" list: the bank "must consider" each of eight security measures (III.C.1.a to h) and adopt those it concludes are appropriate. For a bank that sends wires and offers online banking, every one of the eight is appropriate, so each is assessed below as if required.

**Excluded, with reasons:**
- **III.G** (implementation dates of 2001, 2003, 2005, and 2006): historical and already passed.

**Other agencies' versions.** The Federal Reserve and FDIC publish the same Guidelines for their banks (12 CFR 208 App. D-2 and 225 App. F; 12 CFR 364 App. B). Only the OCC version applies to the bank. The holding company has no operations or customer information of its own, so its Federal Reserve version is satisfied through the bank's program.

**Secondary regulation (Small tier: primary plus the most relevant secondary):**
- **12 CFR Part 53** applies to all national banks (53.1(c)). It requires notice to the OCC no later than 36 hours after the bank determines that a "notification incident" has occurred (53.3), and it requires bank service providers to notify the bank of certain incidents (53.4).
- **12 CFR 225.302** puts the same 36-hour duty on U.S. bank holding companies, so the holding company must notify the Federal Reserve if a notification incident affects it. It is included as one row.

**How the bank is examined.** OCC examiners assess the Guidelines using the **FFIEC Information Technology Examination Handbook**, a set of booklets. What was verified from primary sources:
- The OCC's Supplement A names the handbook's **Information Security** booklet.
- Federal Reserve SR letters announced the **Business Continuity Management** booklet (SR 19-13, 2019), the **Architecture, Infrastructure, and Operations** booklet (SR 21-11, 2021; it described the handbook as 11 booklets), and the **Development, Acquisition, and Maintenance** booklet (SR 24-6, 2024).
- The September 11, 2026 interagency statement on core providers cites the booklet **Supervision of Technology Service Providers** (October 2012).
- The FFIEC Cybersecurity Assessment Tool was removed from the FFIEC website on 2025-08-31. The FFIEC pointed institutions to NIST CSF 2.0, the CISA Cybersecurity Performance Goals, the Cyber Risk Institute's profile, and the CIS Critical Security Controls (SR 24-7).

The ffiec.gov site could not be reached from this environment (it returned a CAPTCHA page), so this analysis does not quote the booklets' examination procedures. That is why the gap analysis maps each requirement to CSF 2.0 and SP 800-53.

## 2. Method
1. **Requirements.** Each paragraph of Appendix B sections II and III was made one row. III.C.1.a has two parts (authentication and access; fraudulent-means controls) and gets two rows. Supplement A's response-program and customer-notice paragraphs were added because III.C.1.g requires a response program and Supplement A is the OCC's interpretation of what that program contains. Supplement A uses "should", so those rows are typed **Guidance**. Part 53 and 225.302 rows are typed **Rule**.
2. **Crosswalk.** Each row was mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of these Guidelines was found.
3. **Evidence.** Current state came from interviews (CEO, COO, ISO, Deposit Operations Manager, Treasury Management Officer, BSA/AML Officer, Compliance Officer, and all six Branch Managers), board minutes and reports, contracts and vendor files, system exports, a sample of 25 branch-originated wires, and a walkthrough of the main office and two branches on 2026-08-05.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| II Standards (program and objectives) | 0 | 5 | 0 | 0 |
| III.A Involve the board | 1 | 1 | 0 | 0 |
| III.B Assess risk | 0 | 3 | 0 | 0 |
| III.C Manage and control risk | 1 | 12 | 0 | 0 |
| III.D Oversee service providers | 1 | 1 | 1 | 0 |
| III.E to III.G Adjust, report, implement | 0 | 2 | 0 | 1 |
| Supplement A (response programs, customer notice) | 1 | 5 | 3 | 0 |
| Part 53 and 225.302 (incident notification) | 0 | 1 | 3 | 0 |
| **Total (42)** | **4** | **30** | **7** | **1** |

Of the 37 unmet or partially met rows: 17 are **Required** ("shall") provisions, 8 are **III.C.1 measures** the bank must consider and has judged appropriate, 8 are **Supplement A guidance** items, and 4 are **Rule** provisions of Part 53 or 225.302. Gap risk: 4 High, 25 Moderate, 8 Low.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Wire callbacks skipped at 2 of 6 branches (7 of 25 sampled wires) | III.C.1.a (fraudulent means) | High | Callback enforced as a required field in the wire platform; branch training; monthly sampling | Deposit Operations Manager | 2026-10-31 |
| Customer MFA optional; no quarterly core access reviews; 4 stale core accounts | III.C.1.a (authentication and access); II.B.3 | High | Required customer MFA; quarterly core reviews | Treasury Management Officer; IT Manager | 2026-12-31 |
| No 36-hour OCC notice step or determination criteria | 53.3; III.C.1.g | High | Determination step and clock in P08; plan update | Information Security Officer | 2026-10-31 |
| SOC reports collected but never reviewed; CUECs unmapped | III.D.3 | Moderate | Documented annual review (core processor done, P09) | Chief Operating Officer | 2026-11-30 |
| No incident notice terms or 53.4 contacts with service providers | III.D.2; 53.4; Supp. A II.A.2 | Moderate | Designated contacts now; side letters; renewal terms | COO; ISO | 2026-09-30 (contacts) |
| No board-approved risk appetite | III.A.2; III.B.2 | Moderate | Risk appetite statement to the board | President and CEO | 2026-10-15 |
| Holding company notice to the Federal Reserve missing | 225.302 | Moderate | Add to the determination step | Information Security Officer | 2026-10-31 |
| No regulator or customer notice procedure for sensitive customer information | Supp. A II.A.1.b, III.A, III.B | Moderate | Criteria, contacts, and templates in P08 | Compliance Officer | 2026-10-31 |
| Admin console, wire platform, and core activity not reviewed | III.C.1.f | Moderate | Daily change report; monthly core review | Deposit Operations Manager | 2026-11-30 |
| Alternate wire procedure untested; backups not isolated | III.C.1.h | Moderate | Semiannual test; immutable backups | Chief Operating Officer | 2027-05-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes to watch
- **Third-party guidance.** The June 2023 **Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920, final as of 2023-06-06) is current. It describes a life cycle of planning, due diligence and third-party selection, contract negotiation, ongoing monitoring, and termination. It says a bank may consider reviewing SOC reports during due diligence, and that contracts can set the audit reports the bank is entitled to receive. On 2026-09-15 the OCC, Federal Reserve, FDIC, and NCUA **proposed** replacement guidance (91 FR 58536; comments due 2026-11-16) that would put more weight on tailoring oversight to each relationship's risk. The three banking agencies also issued a **Joint Statement on Community Banks' Engagement with Core Service Providers** (2026-09-11). It calls core providers community banks' "most material, complex, and highest-risk" third parties and says the agencies will consider a core provider's transparency with its client banks when deciding how closely to supervise it. None of this changes the Guidelines' own service provider duties (III.D), which are regulation text. The rows that could be affected carry a watch note in the `pending_rule_change` column.
- **Supplement A edit.** eCFR shows Appendix B was last amended at 91 FR 18293 (2026-04-10), in the agencies' rule prohibiting the use of reputation risk. The amendment removed one sentence from the introduction to Supplement A section III and changed "Effective" to "Timely and effective". It does not change the customer notice standard analyzed here.
- **No proposed amendment to 12 CFR Part 53** was found in a Federal Register search covering 2023-01-01 to 2026-09-25. The only Part 53 notices in that period were information-collection renewals.
