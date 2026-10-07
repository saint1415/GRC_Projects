# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and Cris Santos Title and Closing, LLC (PE-backed residential real estate brokerage with property management and title and closing services) |
| Tier / Vertical | Mid-Market / Real Estate and Rental and Leasing |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), built around the registry default "Automated tenant and buyer screening"; inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-003 and AI-004 |
| Assessors / date | Business owners of each use case with the vCISO and the Security Manager (security), General Counsel (fair housing, FCRA, privacy), and the GRC analyst (testing), 2026-08-24 to 2026-09-18 |
| Decision | Chief Operating Officer, 2026-09-29; High-tier decisions noted by the CEO; AI-005 co-decided by the President of Title and Closing |

## 1. Summary
All five tools were adopted by departments without a security, privacy, or fair housing review (gap 9 in `../00_company-facts.md` section 4). None is out of control, but four need conditions before they can stay in use:
- **AI-001, tenant screening:** its recommendation is the decision in practice, and it shows a disparity flag for applicants estimated to be Black.
- **AI-002, lead scoring:** uses ZIP code and inquiry language, which act as proxies for race and national origin.
- **AI-004, leasing chatbot:** gave answers in testing that could violate the Fair Housing Act's advertising and disability provisions.
- **AI-005, closing identity verification:** rejects many legitimate older signers and holders of foreign passports, and in 2026-06 passed a forged driver license.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Tenant screening recommendations | High | Approve with conditions |
| AI-002 | Buyer lead scoring | Medium | Approve with conditions |
| AI-003 | Generative AI assistant for marketing | Low | Approve the enterprise tool with conditions; public tools prohibited |
| AI-004 | Leasing assistant chatbot | Medium | Approve with conditions; switch off if not met by 2026-12-31 |
| AI-005 | Identity verification for closings | High | Approve with conditions |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Operating Officer, supported by the vCISO as security reviewer and General Counsel as legal reviewer. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.14: AI tools that touch customer or consumer information or support decisions about housing, brokerage services, or closings must be approved before use.
  - POL-04 4.9: no Restricted data in unapproved AI tools; no-training contract terms.
  - POL-05 4.8: approved tools only; fair housing review of AI-drafted advertising; no unapproved scoring or screening features.
  - STD-11 AI use standard: due 2026-12-31.
- **Risk appetite:** "Fair housing and consumer protection: very low" (P01). No AI tool may be used in housing decisions or access to brokerage services without this review, and no unexplained disparity flag may persist beyond 2 quarters.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions.

### 2.1 Proposed lightweight AI governance process
A mid-market company needs a short, reliable gate and a monthly rhythm, not a standing AI committee with a large charter. The process reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature switched on in an existing platform (the way AI-001 and AI-002 arrived), submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the repository rubric and checks the purchasing gate (no purchase order or feature activation without approval, POL-01 4.9 and 4.14) | Security Manager (Qualified Individual) | 2 business days |
| 3. Review | **Low:** security checklist only. **Medium:** security, privacy, and fair housing review, including a scripted test set for anything that talks to consumers. **High:** a full MAP and MEASURE assessment like this one, with a bias testing plan and counsel review | Security Manager; General Counsel; business owner | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (COO, vCISO, General Counsel), meeting monthly for 30 minutes. High: the AI review group recommends, the COO decides and informs the CEO; for Title and Closing tools the President of Title and Closing co-decides | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (Medium and High) with a quarterly deep dive for High; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model or data-source change, new data type, new population, or a complaint | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Tenant screening | AI-002 Lead scoring | AI-003 Marketing assistant | AI-004 Leasing chatbot | AI-005 Closing ID verification |
|---|---|---|---|---|---|
| Purpose | Recommend accept, accept with conditions, or decline for rental applications | Rank buyer inquiries for callback order | Draft listing and marketing copy | Answer prospects' questions; book showings | Confirm that remote signers are who they claim to be |
| Users | 3 regional leasing teams; Director of Property Management | Inside sales and relocation staff | Marketing staff; agents through marketing | Website visitors | Closers; the President of Title and Closing |
| Affected people | About 15,500 applicants a year and their households; owners of about 4,800 homes | About 6,500 buyer leads a month | Readers of advertising | Prospective tenants | About 3,100 remote buyers and sellers a year |
| Data | Consumer reports, eviction and criminal records, income | ZIP code, language, price range, pre-approval, web activity | Property facts; risk of pasted client data | Contact data, household size, pets and assistance animals (free text) | ID images, selfies, face-match templates and scores (treated as biometric data; see section 3.1) |
| Build or buy | Configure (vendor model; company thresholds) | Configure (vendor model) | Buy (enterprise assistant) | Buy (vendor large language model) | Buy (vendor models) |
| Generative AI? | No | No | Yes | Yes | No |
| Tier and why | **High:** substantial factor in a housing decision | **Medium:** humans decide, but it shapes who gets prompt service. Re-tier to High if used to decline representation or to choose which listings a buyer sees | **Low:** internal drafting with human review. Re-tier to High if client data is entered or it targets or excludes audiences | **Medium:** talks directly to consumers; humans decide applications. Re-tier to High if it pre-screens or rejects applicants | **High:** substantial factor in whether a seller can close and receive proceeds; main control against seller impersonation (P01 R-021); face-match data treated as biometric |

### 3.1 Applicable laws and rules
| Rule | Applies to | Status and effect |
|---|---|---|
| Fair Housing Act, 42 U.S.C. 3604 | AI-001 ((a), (b), (f)); AI-002 ((b), (d)); AI-003 ((c)); AI-004 ((c), (f), including reasonable accommodations in (f)(3)(B)) | In force. Disparate impact claims are cognizable under the Act (*Texas Dept. of Housing and Community Affairs v. Inclusive Communities Project*, 576 U.S. 519 (2015)) |
| HUD discriminatory effects rule, 24 CFR 100.500 | AI-001, AI-002 | **In force** as of 2026-09-23 (eCFR). HUD has **proposed** changing its implementation of the disparate impact standard, including removing this regulation (91 FR 1475, 2026-01-14; supplemental proposal 91 FR 51416, 2026-08-10, comments close 2026-10-09). No final rule as of 2026-10-06. Removal would not remove disparate impact liability under the statute, so the testing below stays |
| Florida Fair Housing Act, Fla. Stat. 760.23 | AI-001, AI-002, AI-004 | Parallel state prohibitions |
| FCRA, 15 U.S.C. 1681b and 1681m(a); disposal rule 16 CFR 682.3 | AI-001 | Permissible purpose; adverse action notice for any adverse action based in whole or part on a consumer report, including a higher deposit; secure disposal |
| FTC Act Section 5, 15 U.S.C. 45(a) (N53-R02) | All five | Accuracy of the company's own representations and of vendor claims it repeats; reasonable data security |
| FTC Safeguards Rule, 16 CFR Part 314 (N53-R01) | AI-005 directly (Title and Closing customer information and a key access control under 314.4(c)(1)(i)); others by company choice | The identity verification vendor is a service provider under 314.4(f) |
| Fla. Stat. 501.171 | AI-005 (ID images with driver license or passport numbers are personal information; biometric data with a name is personal information under 501.171(1)(g)1.a.(VI)); AI-001 and AI-004 (applicant data) | Reasonable security and breach notice (P08). Whether face-match templates computed from selfie images are "biometric data" as defined in Fla. Stat. 501.702 is unsettled, because that definition excludes photographs and data generated from video; counsel to confirm. Until then the company treats them as biometric data and as personal information. The Florida Digital Bill of Rights itself does not apply (it reaches only controllers above $1 billion in global gross annual revenue) |
| RESPA, 12 CFR 1024.15(b) | AI-002 referrals to the mortgage joint venture | Affiliated business disclosure at referral; no required use. Referral data limited to consented fields (P01 R-048) |

**Laws considered and not applicable:**
- **State AI laws such as Colorado SB26-189 and the California ADMT regulations:** the company operates only in Florida and is not doing business in California (P03 section 1.2). This assessment did not identify a Florida AI-specific statute that applies to these uses.
- **HUD's tenant screening guidance (No. 24-098, May 2, 2024):** moved to HUD's archive site, and a Sept. 16, 2025 FHEO memo removed tenant screening algorithm materials from its guidance repository. Treated as background on good practice only, not as a requirement.

## 4. MEASURE
### 4.1 AI-001 tenant screening (main assessment)
Results come from a retrospective review of 15,500 applications screened from 2025-09-01 to 2026-08-31.

| Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|
| Valid and reliable | 50 reports checked against applicant documents: records must belong to the applicant and be current | 0 mismatches | 4 reports included another person's records (name-only match); 3 counted dismissed eviction filings as evictions | **No** |
| Safe | No applicant declined or charged a higher deposit without human review against written criteria | 100% reviewed | Recommendation used as the decision; override rate 2.1% (about 330 of 15,500) | **No** |
| Secure and resilient | Screening provider security review; SSO with MFA for staff | Both | Staff use SSO with MFA; provider not yet reviewed (P09 VEN-10) | Partial |
| Accountable and transparent | FCRA adverse action notice for every decline **and** conditional approval | 100% | Declines only; 0 of 20 sampled conditional approvals got a notice | **No** |
| Explainable and interpretable | Reason codes shown and usable in notices; vendor documents how the score is built | Both | Reason codes shown; no model documentation | Partial |
| Privacy-enhanced | Reports kept only as long as needed; secure disposal | Retention schedule | Kept indefinitely in the platform (P03 G-065; POAM-013) | **No** |
| Fair, harmful bias managed | Approval-rate ratio against the group with the highest rate | No group below 0.80 | Applicants estimated Black **0.73**; Hispanic 0.87; Asian and other 0.96 | **No.** Disparity flagged |

**Bias testing plan (AI-001):**
- **Groups compared.** The company does not collect race or ethnicity on applications. Race and ethnicity are estimated with Bayesian Improved Surname Geocoding (BISG) from surname and address, for aggregate testing only, never recorded on an applicant's file. Sex is estimated from first name for aggregate testing. Familial status and disability cannot be estimated reliably, so the **criteria** are reviewed for them instead (how the income multiple treats disability benefits and housing vouchers; occupancy limits).
- **Metrics.** For each group: approval, conditional approval, and decline rates; the approval-rate ratio against the highest group; reason-code frequency by group to find which criterion drives a gap.
- **Threshold.** A ratio below 0.80 is a **screening flag**, not a legal conclusion; it borrows the four-fifths rule of thumb from employment testing. A flag triggers a driver analysis and a counsel review of whether the criterion is necessary to a substantial, legitimate, nondiscriminatory interest and whether a less discriminatory alternative would serve it (the legally sufficient justification in 24 CFR 100.500(b), with the burdens of proof in 100.500(c)).
- **Frequency.** Quarterly on all applications in the quarter; annually on the full year. Results go to the AI review group and the risk register (P01 R-039).
- **Current result and drivers.** Estimated approval rates: White 70% (5,900 applicants), Black 51% (4,300), Hispanic 61% (3,900), Asian and other 67% (1,400). **55% of declines among applicants estimated Black were driven by eviction filings (including dismissed filings) and criminal records more than 7 years old.** Those two criteria change first.

### 4.2 AI-002 to AI-005
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-07 to 2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-002 | Fair, harmful bias managed | Median time to first contact by inquiry language | No group more than 2 times the overall median | Spanish-language 22 hours against 3 hours for English | **No** |
| AI-002 | Fair, harmful bias managed | Share of leads scored C from ZIP codes with mostly Black residents | No more than 1.25 times the overall share | 58% against 31% overall | **No** |
| AI-002 | Privacy-enhanced | Joint venture API sends only consented fields | All referrals | Full lead record sent (P01 R-048) | **No** |
| AI-003 | Fair, harmful bias managed | Fair housing review of 40 AI-drafted listing descriptions | 0 discriminatory statements published | 2 drafts described an ideal buyer by family status; both caught by the listing agent before publication | Yes (review works) |
| AI-003 | Privacy-enhanced | No-training terms; public tools blocked | Both | Enterprise tool has no-training terms; public tools not yet blocked on company devices | Partial |
| AI-004 | Fair, harmful bias managed; safe | 40 scripted fair housing questions (children, assistance animals, national origin, vouchers) | 0 problematic answers; 100% handoff on accommodation questions | 4 problematic answers (described one home as "not ideal for children"; applied the pet deposit to an assistance animal twice; one answer about vouchers); 3 of 10 accommodation questions not handed off | **No** |
| AI-004 | Accountable and transparent | Visitors told they are talking to an AI tool | Disclosure on every chat | No disclosure | **No** |
| AI-005 | Valid and reliable | Failure rate and share of failures that were legitimate signers on manual review | Failure rate under 3%; legitimate share reviewed monthly | 6.2% of checks failed; 81% of failures were legitimate signers | **No** |
| AI-005 | Fair, harmful bias managed | Failure rate by age band and document type | No group more than 2 times the overall rate | Signers 70 and over 11% against 4% under 40; foreign passports 14% | **No** |
| AI-005 | Secure and resilient | Detection of forged documents on high-risk files | No forged ID accepted without a second check | 2026-06: a forged driver license passed on a vacant-lot sale; the impostor was stopped only because the closer called the owner at the tax-roll mailing address (P01 R-021) | **No** |
| AI-005 | Privacy-enhanced | Retention and use of ID images and face-match data | Deleted within 30 days; no training on company data | Vendor keeps images 3 years; contract silent on training | **No** |
| All | Explainable and interpretable | Users can see why an output was produced (reason codes, score factors, source text, failed check) | Available | Available for AI-001, AI-002, AI-005; partial for AI-003 and AI-004 | Partial |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001 (from 2026-10-31):** written screening criteria, reviewed by counsel, published to applicants before they apply. A leasing coordinator reviews **every** decline and conditional approval against the criteria before any notice, and may override with a written reason; the Director of Property Management reviews overrides monthly. Criminal and eviction records get an **individualized review** (nature and age of the record, what has happened since, relevance to the tenancy); dismissed filings and records that do not match a second identifier are disregarded; applicants can explain or correct a record before the decision. Every decline and conditional approval gets an FCRA adverse action notice.
- **AI-002:** the score orders the queue but never decides service; every lead gets a same-day first contact; Spanish-language leads go to Spanish-speaking staff.
- **AI-003:** a person edits and approves every draft; the listing agent or marketing reviewer checks it for discriminatory statements (POL-05 4.8).
- **AI-004:** the chatbot books showings only for a leasing agent to confirm, and hands off every question about eligibility, accommodations, assistance animals, or vouchers.
- **AI-005:** the tool never blocks a closing on its own. A closer reviews every failure and every pass on a high-risk file; remote sellers of vacant land or non-owner-occupied property also sign before a known notary and get a callback to the address of record.

**Configuration changes:**
- AI-001 (by 2026-11-30): count eviction judgments only, not filings; limit criminal records to a counsel-approved list of offenses and lookback; require a second identifier for record matches.
- AI-002 (by 2026-11-30): remove ZIP code and inquiry language as inputs; limit the joint venture API to consented fields.
- AI-005 (by 2026-12-31): tune thresholds with the vendor's subgroup performance data; route foreign passports to manual review by default.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group; AI-001 and AI-005 also get a quarterly deep dive. Results feed the risk register (P01 R-021, R-039 to R-044) and the POA&M (POAM-018).

**Incident handling:** a security or privacy incident at an AI vendor follows P08 and the vendor's notice duty (Fla. Stat. 501.171(6)(a); 5 business days for Tier 1 contracts under STD-03). A fair housing complaint, an FCRA dispute pattern, or a wrongful-denial pattern is escalated to General Counsel and the COO and logged in the risk register. A forged ID that passes AI-005 is a Severity 1 incident under the BEC runbook.

**Decommissioning criteria:**
- AI-001: switch off automated recommendations and screen manually against the written criteria if the ratio for applicants estimated Black stays below 0.80 for 2 quarters after the changes without a justification counsel can document, or if the vendor will not provide model and data-source documentation by 2026-12-31.
- AI-002: switch off scoring if the response-time parity check fails for 2 consecutive months after the input changes.
- AI-004: switch off on 2026-12-31 if the fair housing test set, handoff fixes, and AI disclosure are not in place.
- AI-005: revert to known-notary signing for all remote sellers if the vendor will not agree to 30-day image deletion and no-training terms by 2026-12-31.
- Any tool: stop if the vendor changes data sources, data-use terms, or the model without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Written criteria, coordinator review, and individualized review live (2026-10-31); adverse action notices for conditional approvals and configuration changes (2026-11-30); vendor documentation and contract addendum (2026-12-31); first post-change bias test (2027-01-31) | COO, 2026-09-29; noted by the CEO |
| AI-002 | **Approve with conditions** | Remove proxy inputs and limit API fields (2026-11-30); monthly parity check by language and ZIP code group | COO, 2026-09-29 |
| AI-003 | **Approve with conditions** | Enterprise tool only; public tools blocked on company devices (2026-12-31); fair housing review of every published draft | COO, 2026-09-29 |
| AI-004 | **Approve with conditions** | Fair housing test set passed, accommodation handoff, and AI disclosure by 2026-12-31, or switch off | COO, 2026-09-29 |
| AI-005 | **Approve with conditions** | Threshold tuning with subgroup data, known-notary rule for high-risk sellers, 30-day image deletion and no-training terms (2026-12-31); monthly accuracy review | COO and President of Title and Closing, 2026-09-29; noted by the CEO |

Residual risk targets after the conditions: AI-001 and AI-005 Moderate; AI-002, AI-003, and AI-004 Low. The conditions are tracked as POAM-018 in P07 and in the risk register (P01 R-021, R-039 to R-044). The AI review group holds its first monthly meeting on 2026-10-13.
