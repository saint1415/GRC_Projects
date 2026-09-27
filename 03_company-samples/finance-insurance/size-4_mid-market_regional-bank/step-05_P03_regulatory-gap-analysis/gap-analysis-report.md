# Regulatory Gap Analysis: Cris Santos Company | Finance and Insurance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank; OCC-supervised national bank) and its parent Cris Santos Company, Inc. (bank holding company) |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Primary regulation | Interagency Guidelines Establishing Information Security Standards, as issued by the OCC: 12 CFR Part 30, Appendix B, with Supplement A (N52-R02). Text read from eCFR (2026-09-23 version) |
| Other rules for the primary business line | Computer-Security Incident Notification (12 CFR Part 53; 12 CFR 225 Subpart N for the holding company); Identity Theft Red Flags (12 CFR 41.90); SAR reporting (12 CFR 21.11); Regulation B as it applies to the AI credit model (12 CFR 1002.4, 1002.6, 1002.9); Florida breach notification as the worked example of state law; FFIEC authentication guidance as a supervisory expectation |
| Assessment dates | 2026-06-29 to 2026-07-24; evidence refreshed with P07 results through 2026-08-21 and P10 results through 2026-09-04 |
| Assessor | IT Risk and Compliance Manager and the ISO, with the Chief Compliance Officer and General Counsel; reviewed by the Chief Audit Executive |
| Approved | Chief Risk Officer, 2026-09-18 (reviewed by the Board Risk Committee on 2026-09-15) |

## 1. Applicability
**Primary business line:** commercial banking (deposits, lending, payments, and treasury management), including correspondent payment services for 18 respondent institutions.

| Rule | Applies? | Basis (verified on eCFR, 2026-09-23 version, unless noted) |
|---|---|---|
| Interagency Guidelines, 12 CFR 30 App. B (N52-R02) | **Yes** | Section I.A applies them to customer information maintained by or on behalf of national banks. There is no size exemption: II.A requires a program "appropriate to the size and complexity" of the bank. III.C.1 lists eight measures the bank "must consider" and adopt if appropriate; for a bank that sends wires and offers online banking, every one is appropriate, so each is assessed as if required |
| Supplement A to App. B | **Yes (guidance)** | The OCC's interpretation of the response program under III.C.1.g, including when to notify the OCC and customers about unauthorized access to sensitive customer information. It uses "should", so its rows are typed Guidance |
| 12 CFR Part 53 | **Yes** | Applies to all national banks (53.1(c)). A notification incident must reach the OCC as soon as possible and no later than 36 hours after the bank determines one has occurred (53.3). Bank service providers must notify the bank of incidents that disrupt covered services for 4 or more hours (53.4) |
| 12 CFR Part 53 and parallel rules, bank as provider | **Yes, per counsel** | The bank processes payments for bank respondents. General Counsel's working view is that these are covered services under the Bank Service Company Act, so the bank owes 53.4-type notices to bank respondents (12 CFR 53.4, 225.303, or 304.24, depending on the respondent's regulator). This is a legal judgment, recorded as such |
| 12 CFR 225 Subpart N | **Yes** | The holding company is a U.S. bank holding company (225.300(c)); it must notify the Federal Reserve within 36 hours of determining a notification incident (225.302) |
| 12 CFR 41.90 (Red Flags) | **Yes** | Applies to national banks (41.90(a)); the bank offers covered accounts |
| 12 CFR 21.11 (SARs) | **Yes** | National bank. Included because security incidents and payment fraud trigger SAR duties |
| Regulation B (12 CFR Part 1002) | **Yes, for AI-001** | The bank is a creditor and AI-001 supports small business credit decisions. 1002.6(a) now states that the Act does not provide for the "effects test", so outcome disparities are not by themselves a Regulation B violation; the bank still measures them as a signal of proxy discrimination (P10) |
| FFIEC authentication guidance (2021) | **Supervisory expectation** | "Authentication and Access to Financial Institution Services and Systems", announced by the Federal Reserve in SR 21-14 (2021-08-11) on behalf of the FFIEC agencies. It is guidance that examiners take into account, not a regulation. Verified on federalreserve.gov |
| State breach laws | **Yes** | The bank holds personal information of Florida and Georgia residents. Florida is the worked example (Fla. Stat. 501.171); each affected person's state law applies |
| OCC heightened standards (12 CFR 30 App. D) | **No** | Apply to banks with average total consolidated assets of $50 billion or more, banks whose parent controls such a bank, or banks the OCC designates as highly complex (App. D I.A, I.C, I.E.5). The bank has $2.5 billion in assets, its parent controls no other bank, and there is no OCC designation. One row records this |
| FTC Safeguards Rule (N52-R03) | No | The bank is supervised by the OCC, not the FTC |
| NYDFS Part 500 (N52-R04) | No | Not New York-chartered or licensed |
| SEC Regulation S-P and S-ID (N52-R05, N52-R06) | No | No broker-dealer, investment adviser, or trust department |
| NAIC Model #668 (N52-R07) | No | No insurance agency |
| SEC Form 8-K Item 1.05 and Regulation S-K Item 106 (N52-R08) | **No** | Both companies are privately held and are not Exchange Act reporting companies. If the holding company ever registered securities, both would apply and the P08 runbooks would add a materiality step |
| CFPB small business lending data collection (Regulation B subpart B) | No | A covered financial institution originated at least 1,000 covered credit transactions for small businesses in each of the two preceding calendar years (12 CFR 1002.105(b)); the bank originates about 420 a year. Rechecked each January against 1002.114 |

**Other agencies' versions.** The Federal Reserve and FDIC publish the same Guidelines for their banks (12 CFR 208 App. D-2 and 225 App. F; 12 CFR 364 App. B). Only the OCC version applies to the bank. The holding company has no operations or customer information of its own, so its Federal Reserve version (225 App. F) is satisfied through the bank's program.

**How the bank is examined.** OCC examiners assess the Guidelines using the FFIEC Information Technology Examination Handbook. The FFIEC Cybersecurity Assessment Tool was sunset on 2025-08-31, and the FFIEC pointed institutions to NIST CSF 2.0 and other frameworks, which is why each row is mapped to CSF 2.0 and SP 800-53. FFIEC material is treated as supervisory expectation, not regulation. The ffiec.gov site could not be read from this environment, so the handbook's examination procedures are not quoted.

## 2. Method
1. **Requirements.** Each paragraph of Appendix B sections II and III is one row; III.C.1.a has two parts (authentication and access; fraudulent means). Supplement A's response-program and customer-notice paragraphs were added. Part 53, 225.302, 41.90, 21.11, and the Regulation B provisions were decomposed from the eCFR text. Row types: Required (shall), Consider (III.C.1), Guidance (Supplement A), Rule (must), Supervisory guidance, and State statute.
2. **Crosswalk.** Each row is mapped to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. This is an **author mapping**: no official NIST mapping of these rules was found.
3. **Evidence.** Interviews with the process owners and 8 Branch Managers, board and committee minutes, contracts and vendor files, system exports, and walkthroughs of the headquarters campus, the Georgia regional office, and 4 branches (FL-01, FL-07, FL-15, GA-03).
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested. Samples were drawn at random from system-generated populations, using the co-sourced IT audit firm's attribute sampling table (25 items for a control that operates many times a year; more where the population is small and risk is high):
   - business contact-information changes (April to June 2026): 40 of about 1,100;
   - non-face-to-face wire requests (June 2026): 25 of about 1,900;
   - terminations: 25 of 142;
   - teller and universal banker core entitlements: 30 of about 180;
   - new hires: 25;
   - infrastructure and application changes: 20; payments hub limit changes: 10;
   - SARs: 15 of 212;
   - incidents: 10 of 31;
   - AI-001 declines with adverse action notices: 40 of about 160;
   - media disposals: 10.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. The `related_risks` column links each gap to P01.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| App. B II Standards (program and objectives) | 3 | 2 | 0 | 0 | 5 |
| App. B III.A Involve the board | 1 | 1 | 0 | 0 | 2 |
| App. B III.B Assess risk | 1 | 2 | 0 | 0 | 3 |
| App. B III.C Manage and control risk | 3 | 10 | 0 | 0 | 13 |
| App. B III.D Oversee service providers | 1 | 2 | 0 | 0 | 3 |
| App. B III.E to III.G Adjust, report, implement | 1 | 1 | 0 | 1 | 3 |
| **Interagency Guidelines subtotal** | **10** | **18** | **0** | **1** | **29** |
| Supplement A (response programs, customer notice) | 2 | 7 | 0 | 0 | 9 |
| 12 CFR Part 53 (including the bank as provider) | 1 | 2 | 1 | 0 | 4 |
| 12 CFR 225 Subpart N (holding company) | 0 | 0 | 1 | 0 | 1 |
| 12 CFR 41.90 Red Flags | 3 | 5 | 1 | 0 | 9 |
| 12 CFR 21.11 SARs | 2 | 1 | 0 | 0 | 3 |
| Regulation B (AI-001) | 1 | 1 | 1 | 0 | 3 |
| FFIEC authentication guidance | 1 | 1 | 0 | 0 | 2 |
| State breach notification (Florida example) | 0 | 1 | 1 | 0 | 2 |
| OCC heightened standards (App. D) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **20** | **36** | **5** | **2** | **63** |

Of the 41 unmet or partially met rows: 10 are **Required** ("shall") provisions of the Guidelines, 8 are **III.C.1 measures** the bank must consider and has judged appropriate, 7 are **Supplement A guidance** items, 13 are **Rule** provisions (Part 53, 225.302, 41.90, 21.11, Regulation B), 2 are **state statute** items, and 1 is **supervisory guidance**. Gap risk: 8 High, 27 Moderate, 6 Low.

**Reading the results.** The bank has a defined program: the board approves it, the risk assessment is sound, testing is independent, and disposal, encryption, SARs, and physical security are Met. The gaps concentrate where the program has not scaled:
- **payment fraud through upstream processes** (contact changes, relayable one-time codes): II.B.3, III.C.1.a, 41.90(d)(2);
- **privileged access to money-moving applications** and core role design: III.C.1.a, III.C.1.e;
- **monitoring of payments events**: III.C.1.f;
- **recovery of bank-run systems**: III.C.1.h;
- **notices**: the notification incident determination, the holding company notice, and the bank's own outbound notices to respondents (Part 53, 225.302);
- **third parties at scale**: III.D.2, III.D.3, 53.4 inbound;
- **AI credit reasons**: 1002.9(b)(2).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Contact-information changes accepted without out-of-band verification (11 of 40 sampled) | III.C.1.a (fraudulent means); 41.90(d)(2)(ii)-(iii); II.B.3 | High | Out-of-band verification; customer alerts; wire hold after a change | Retail Banking Director | 2026-12-31 |
| Relayable customer one-time codes; no out-of-band beneficiary confirmation | II.B.3; FFIEC 2021 guidance | High | Phishing-resistant options; out-of-band beneficiary confirmation | Treasury Management Director | 2027-03-31 |
| Core roles not templated; core and payments hub admins outside PAM; late core removals; generic portal accounts | III.C.1.a (authentication and access) | High | Role templates; PAM extension; automated deprovisioning | Chief Information Officer | 2027-03-31 |
| Payments hub, portal, and core events not monitored | III.C.1.f | High | SIEM onboarding and change-anomaly use cases | Information Security Officer | 2027-01-31 |
| Payments hub recovery unproven; legacy servers | III.C.1.h | High | Failover redesign and retest; replace servers | Chief Information Officer | 2027-03-31 |
| No notification incident determination criteria | 53.2(b)(7); 53.3 | High | Criteria, clock, and record in P08; tabletop | Information Security Officer | 2026-11-30 |
| Adverse action reasons not specific (9 of 40) | 1002.9(b)(2) | High | Reason-code mapping; corrected statements | Chief Credit Officer | 2026-10-31 |
| Holding company notice missing; no outbound notice to respondents | 225.302; 53.4 (outbound) | Moderate | Add both to the determination step in P08 | Information Security Officer; Correspondent Services Director | 2026-11-30 |
| 53.4 contacts missing for 4 of 7 providers; 9 contracts without notice terms | 53.4(a); III.D.2; Supp. A II.A.2 | Moderate | Send contacts; side letters | Third-Party Risk Manager | 2026-10-31 (contacts) |
| CUECs unmapped for most Tier 1 vendors | III.D.3; III.B.3 | Moderate | P09 review method for all Tier 1 vendors | Third-Party Risk Manager | 2027-03-31 |
| No measurable cyber tolerances | III.A.2; III.B.2 | Moderate | Tolerances to the board | Chief Risk Officer | 2026-10-20 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Generic portal accounts removed (done 2026-08-14); corrected adverse action statements; 53.4 contacts to all providers and from all respondents; determination criteria and holding company step in P08; executive tabletop; contact-change verification live; board adopts tolerances | 1002.9(b)(2); 53.3; 53.4; 225.302; III.A.2; 41.90(d)(2)(ii)-(iii) |
| **2. Build** | 2027 Q1 | PAM for core and payments hub administrators; SIEM onboarding; payments hub configuration baseline and dual approval; phishing-resistant customer MFA and beneficiary confirmation; standards STD-01 to STD-08; payments hub failover retest | III.C.1.a; III.C.1.d; III.C.1.e; III.C.1.f; III.C.1.h; II.A |
| **3. Scale third parties and prove** | 2027 Q2 | CUEC mapping for all Tier 1 vendors; side letters and renewal terms; full relocation exercise; legacy servers replaced; core role templates complete; SOC 2 Type 2 observation period for correspondent services starts (P09) | III.D.2; III.D.3; III.C.1.h; 41.90(e)(4) |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (December 2027); Red Flags program annual update; second annual independent assessment; AI fairness monitoring each quarter | III.B; III.C.3; 41.90(d)(2)(iv); 1002.6 |

Progress is reported quarterly to the Board Risk Committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending changes to watch
- **Third-party guidance.** The June 2023 **Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920) is current. On 2026-09-15 the OCC, Federal Reserve, FDIC, and NCUA **proposed** replacement guidance (91 FR 58536; comments due 2026-11-16) that would tailor oversight to each relationship's risk. The banking agencies also issued a **Joint Statement on Community Banks' Engagement with Core Service Providers** (2026-09-11). None of this changes the Guidelines' own service provider duties (III.D). Affected rows carry a watch note in `pending_rule_change`.
- **Supplement A edit.** eCFR shows Appendix B was last amended at 91 FR 18293 (2026-04-10), which removed one sentence from the introduction to Supplement A section III and changed "Effective" to "Timely and effective". It does not change the customer notice standard analyzed here.
- **No proposed amendment to 12 CFR Part 53** was found in a Federal Register search through 2026-09-25.
- **Payments fraud.** The OCC, Federal Reserve, and FDIC published a **Request for Information on Potential Actions To Address Payments Fraud** (90 FR 26293, 2025-06-20). It is a request for information, not a rule.
- **Model risk guidance.** The current status of the agencies' model risk management guidance for banks of this size was not verified for this analysis. The bank applies its own model risk management policy (2023) as a policy choice (P10).
