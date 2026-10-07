# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry use case, generative AI for tax and document preparation, is AI-001 and AI-002 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-002, AI-003, and AI-006 |
| Assessors / date | AI review group: General Counsel (chair), Director of Information Security, Privacy Officer, National Tax Practice Leader, Chief People Officer, and Attest Firm Quality and Independence Partner, 2026-08-24 to 2026-09-12 |
| Decision | Chief Operating Officer, 2026-09-22; High-tier decisions noted by the Chief Executive Officer |

## 1. Summary
Every one of the six tools reached the Company without a security, privacy, or IRC 7216 review (gap 12). None is out of control, but three need conditions before they grow or continue:
- **AI-001, tax software AI:** extraction works well on typed forms. The drafting-suggestions feature was turned on by the tax practice without review and sent tax return information for what the regulation calls substantive determinations. It was turned off on 2026-08-28.
- **AI-005, resume screening:** it ranks applicants, and recruiters advanced only the top-ranked third in 2026. The selection rate for two groups fell below four-fifths of the highest group's rate. From 2027-01-01, Colorado law adds duties for Colorado-resident applicants.
- **AI-006, public chatbots:** 9 staff pasted client names and notice text into public tools.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Tax software AI document extraction (and drafting suggestions) | Medium | Extraction: approve with conditions. Drafting: stays off pending counsel |
| AI-002 | Enterprise AI assistant | Medium | Approve with conditions |
| AI-003 | AI tax research assistant | Medium | Approve with conditions |
| AI-004 | Audit journal entry analytics | Medium | Approve with conditions |
| AI-005 | AI resume screening | High | Auto-ranking suspended; approve only with conditions before the 2027 campus cycle |
| AI-006 | Public generative AI chatbots | High (if client data is entered) | Prohibited; blocked by 2026-10-31 |

Tiers: 2 High, 4 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the General Counsel, who chairs the AI review group. The Director of Information Security owns the approved-tools list and the technical controls. Each use case has a business owner (inventory).
- **Policies and standards:**
  - POL-01 4.9: no new AI tool or AI feature goes live without security, privacy, and IRC 7216 review (the new technology gate).
  - POL-04 4.10: client data enters an AI tool only if the tool is approved for that data class with a documented IRC 7216 basis.
  - POL-05 4.9: approved tools only; no client data in public chatbots; the signing professional checks every AI output.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** on the intranet. Today it lists AI-001 extraction, AI-002, AI-003, and AI-004 with their data rules. AI-005 auto-ranking is suspended. AI-006 is prohibited.

### 2.1 Lightweight AI governance process
A 600-person firm does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm that reuses existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Anyone who wants an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the P10 rubric; check of the purchasing gate and of the SaaS change control (POAM-009) | Director of Information Security | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy and IRC 7216 (Privacy Officer), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias testing plan and legal review | Director of Information Security; Privacy Officer; business reviewer; General Counsel for High | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Director of Information Security. Medium: the AI review group (monthly, 30 minutes). High: the AI review group recommends, the Chief Operating Officer decides, and the Chief Executive Officer is informed | As listed | Monthly |
| 5. Monitor | The business owner reports the agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: a new feature, a model change, a new data type, a new population, or an incident | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 6.

### 2.2 Model risk controls
These apply to every approved use case, scaled by tier. They are the "model risk management" layer for a firm that buys rather than builds its models.

| Control | Medium tier | High tier | Main SP 800-53 controls |
|---|---|---|---|
| Inventory and ownership | Entry in the inventory with an owner, vendor, model or feature version, and data classes | Same, plus the decision the model influences and the affected population | CM-8; PM-9 |
| Validation before use | Accuracy test on a sample of the Company's own data against a stated threshold | Same, plus pre-deployment bias testing and legal review | RA-3; SA-9 |
| Vendor terms | U.S. processing, no training on Company data, deletion terms, sub-processor notice, IRC 7216 basis | Same, plus the developer documentation needed for notices and explanations | SA-9; SA-9(5) |
| Change control for model updates | Vendor release notes reviewed monthly; material model changes trigger re-validation | Same, and no new model version in use before re-validation | CM-3 |
| Performance monitoring | Monthly metrics against thresholds | Monthly metrics plus a quarterly deep dive | CA-7 |
| Human oversight | The signing professional reviews every output | Human makes every decision; documented override and reconsideration process | AC-5; PL-4 |
| Independent review | Included in the annual internal audit sample | Annual internal audit review of the model risk controls | CA-2 |
| Decommissioning | Stop criteria and data deletion confirmation | Same | SA-9 |

## 3. MAP
| Item | AI-001 Tax software AI | AI-002 AI assistant | AI-003 Research assistant | AI-004 Journal entry analytics | AI-005 Resume screening | AI-006 Public chatbots |
|---|---|---|---|---|---|---|
| Purpose | Extract source document data into returns; drafting suggestions (off) | Draft letters and notice responses | Answer research questions with links to authorities | Score ledger entries for unusual patterns | Score and rank applicants | None approved |
| Users | All preparers (about 300 with seasonal staff) | 250 licensed users | 120 tax professionals | Assurance teams on 140 engagements | 9 recruiters | Unknown; 9 staff found |
| Affected people | Individual clients (about 21,400 returns in 2026) | Clients who receive letters | Clients who receive advice | Client companies | About 6,800 applicants in 2026 | Clients whose data was pasted |
| Data | Scanned source documents with SSNs and bank details | Notice text, amounts; restricted identifiers | Anonymized facts | General ledgers; occasional PHI | Resumes and application answers | Client names, notice text |
| Build or buy | Buy (SaaS feature with an AI sub-processor) | Buy (licensed feature of SYS-06) | Buy (feature of a research subscription) | Buy (software in the Company enclave) | Buy (module of the applicant tracking system) | Consumer services |
| Generative AI? | Yes | Yes | Yes | No (anomaly model) | No (scoring model) | Yes |
| Key rules | IRC 7216; 16 CFR 314; 31 CFR 10.22 | IRC 7216; 31 CFR 10.22 | 31 CFR 10.22 | Professional standards; HIPAA for PHI | Title VII; 29 CFR 1607.4; Colorado SB26-189; CCPA ADMT (if applicable) | IRC 7216 |

### 3.1 IRC 7216 analysis (AI-001, AI-002, AI-006)
The IRS has issued no AI-specific guidance under section 7216 (P03 section 6), so this analysis applies the regulation text, and counsel will confirm it in writing by 2026-10-31.
1. **Extraction may fit the preparer-to-preparer permission.** 26 CFR 301.7216-2(d)(1) lets a preparer disclose tax return information without consent to another tax return preparer **located in the United States** for auxiliary services, as long as no substantive determinations are made. The tax software vendor is itself a preparer (a software developer and Authorized IRS e-file Provider). Its 2025 contract amendment states that the AI sub-processor processes and stores data only in the United States and does not train on it. That statement has not been independently assured (P09 VEN-01).
2. **Drafting suggestions are likely "substantive determinations."** The regulation describes these as an analysis, interpretation, or application of the law. Proposed treatments and explanations fit that description, so disclosure to another preparer for that purpose needs the taxpayer's consent (301.7216-3(a)(1)). The feature was used on about 2,100 returns before it was turned off. Counsel is reviewing whether those uses require client notice or other remediation; the Privacy Officer has logged them as a potential unauthorized use.
3. **SSNs must stay in the United States.** For Form 1040 filers, a U.S. preparer may not obtain consent to disclose the SSN to a preparer outside the United States except through an IRS-defined adequate data protection safeguard (301.7216-3(b)(4)). Scanned W-2s always contain SSNs, so U.S.-only processing is a hard requirement for AI-001, as it is for the offshore program.
4. **AI-002.** The productivity suite vendor already holds client email containing tax return information. The Company treats the assistant as part of the same service, relying on the vendor's U.S.-processing and no-training terms. **This reading is the Company's own; counsel must confirm it.** Until then, prompts may not contain client names, SSNs, or account numbers, and a data loss prevention rule blocks SSNs.
5. **AI-006 is an unauthorized disclosure.** No permission covers pasting client data into a public chatbot. The Privacy Officer reviewed the 9 cases as incidents: names and notice amounts, no SSNs, far below the 500-consumer FTC threshold. All 9 were retrained, and 3 who had been warned before were sanctioned under POL-01 4.14.

### 3.2 Employment law analysis (AI-005)
- **Federal.** Title VII prohibits employment practices with an unjustified disparate impact. The Uniform Guidelines on Employee Selection Procedures treat a selection rate for any race, sex, or ethnic group that is less than four-fifths (80%) of the rate for the group with the highest rate as generally regarded as evidence of adverse impact, while noting that smaller differences can matter and that small numbers may not be reliable (29 CFR 1607.4(D)). Users should keep records that show the impact of their selection procedures by race, sex, and ethnic group (29 CFR 1607.4(A)). The EEOC's 2023 technical assistance on AI selection tools is no longer on the EEOC website (checked 2026-09-25); the statute and the Guidelines still apply.
- **Colorado.** SB26-189 repealed and reenacted Colo. Rev. Stat. 6-1-1701 and following, effective 2027-01-01, for consequential decisions made on or after that date. Employment is a covered domain, and "consumer" includes a job applicant who is a Colorado resident. The Company employs 4 people in Colorado and receives applications from Colorado residents for remote roles, so counsel treats it as doing business in Colorado. A deployer whose tool materially influences the decision must give a clear point-of-interaction notice (6-1-1704(1)-(2)), explain any adverse outcome within 30 days (6-1-1704(3)), offer correction of personal data and meaningful human review and reconsideration (6-1-1705), and keep records for 3 years (6-1-1703). Ranking that decides who advances is a material influence (6-1-1701(13)). The signed act has no small-business exemption.
- **California.** The Company exceeds the CCPA revenue threshold. Whether it "does business in California" (it has California-resident clients and California applicants for remote roles, but no California employees) is referred to counsel. If it does, the CPPA ADMT rules apply to AI-005 from 2027-01-01. The AI-005 conditions below are designed to meet those rules as well.
- **Other places.** State and local AI-in-employment laws such as Illinois's and New York City's apply only when the Company hires for roles there. It posts no roles located in Illinois or New York City; the recruiting team must re-check before it does.
- **Federal preemption.** EO 14365 directs federal action against some state AI laws but does not itself preempt any. The Company plans to comply with Colorado law as enacted.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Monthly sample of 20 returns per team; every AI-populated field compared with the source | Typed forms at least 99%; photographed or handwritten at least 97%; zero critical-field errors (SSN, EIN, wages, withholding, bank routing and account) on signed returns | 600 returns (2026-02 to 2026-04): typed 99.5%; photographed or handwritten 96.1%; 3 critical-field errors caught at review, 0 on signed returns | **No** for photographed and handwritten forms |
| AI-001 | Fair, harmful bias managed | Name-field mismatch rate for compound, hyphenated, or accented surnames vs. others; error rate for phone photos vs. scans | Flag if more than 2 points above baseline | Names 2.8% vs 0.5%; phone photos 3.9% vs 0.5% | **No** (both flagged) |
| AI-001 | Privacy-enhanced | U.S.-only processing; no training; deletion within 30 days; IRC 7216 basis | All contractual and assured | Contractual by 2025 amendment; not assured; drafting basis unresolved | **Partial** |
| AI-002 | Valid and reliable | 40 sampled drafts: every cited authority and amount checked | 0 wrong authorities reach clients | 5 of 40 drafts cited a wrong or nonexistent authority (AI 600-1 confabulation); all caught before sending | Pass with mandatory check |
| AI-002 | Privacy-enhanced | 40 sampled prompts checked for client identifiers | 0 SSNs or account numbers | 1 SSN; 14 client names | **No** |
| AI-003 | Valid and reliable | 50 sampled answers: every linked authority opened and checked | 0 wrong authorities in client work | 4 of 50 answers summarized an authority incorrectly; none reached a client memo | Pass with mandatory check |
| AI-004 | Valid and reliable | Seeded test ledger with 40 known unusual entries, run on each model version | At least 90% of seeded entries in the top-scored decile | 37 of 40 (92.5%) on the current version | Yes |
| AI-004 | Accountable and transparent | Each score shows the features that drove it; auditors document their own selection rationale | Available for every score | Available | Yes |
| AI-005 | Fair, harmful bias managed | Selection rate (advanced to interview) by sex and race or ethnicity, as a ratio of the highest group's rate (29 CFR 1607.4(D)); age 40 and over vs. under 40 as a Company check | Flag any ratio below 0.80, or a smaller difference that is statistically significant | 2026 cycle, about 6,800 applicants, 71% self-identified: highest group (Asian) 33%; White 30% (0.91); Black 26% (0.79); Hispanic or Latino 22% (0.67); women 29% vs men 31% (0.94); age 40 and over 18% vs under 40 31% (0.58) | **No** (3 flags) |
| AI-005 | Accountable and transparent | Applicants told that an automated tool is used; a process for human review | Notice and process in place | Neither in place | **No** |
| AI-005 | Explainable and interpretable | Recruiters can see the factors behind a score | Available | Vendor shows a score and 3 "match" factors only | Partial |
| AI-006 | Privacy-enhanced | Public chatbot use with client data | 0 | 9 cases | **No** |

**Bias testing plans.**
- **AI-001:** monthly in season and quarterly otherwise on the R-032 sample; groups are compound or accented surnames, phone photos or handwriting, and ITIN filers; flag at 2 points above baseline; flagged categories go to mandatory manual verification.
- **AI-005:** each hiring cycle and quarterly during campus season; groups by sex and race or ethnicity under 29 CFR 1607.4, plus age 40 and over; flag below 0.80 or on statistical significance. Results go to the AI review group before the tool is used for advance decisions again. The vendor must supply its own validation and adverse impact studies and the factor list behind each score.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the preparer verifies every low-confidence field, every critical field, and every field from a photographed or handwritten document; the reviewer ticks the AI checklist item before sign-off; e-file only after Form 8879 is signed.
- **AI-002 and AI-003:** drafts and research only; the signing professional checks every authority in the primary source and every amount (31 CFR 10.22 due diligence, including reasonable care when relying on another's work product, 10.22(b)).
- **AI-004:** the score helps auditors choose entries to test; it never replaces the auditor's own selection rationale.
- **AI-005:** a recruiter reviews every application; the score may be shown but may not set a cut-off; any applicant can request human review and reconsideration.
- **Automation bias (AI 600-1 "human-AI configuration"):** reviewers are trained to treat AI output as unverified, and the monthly samples measure what reviewers missed, not only what the tool got wrong.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group; the High-tier use case gets a quarterly deep dive. Results feed the risk register (P01 R-032 to R-037).

**Incident handling:** a security incident at an AI vendor follows P08 (vendor notice within 10 days under Fla. Stat. 501.171(6)(a); FTC notice if 500 or more consumers). An AI error found in a filed return is corrected by amended return and client notice. Client data in a public chatbot is an incident under POL-03. An adverse impact finding for AI-005 is handled by the General Counsel with the Chief People Officer.

**Decommissioning criteria:**
- AI-001 drafting: stays off unless counsel confirms a basis and the taxpayer consent design is approved.
- AI-001 extraction: stop if processing moves outside the United States, the vendor changes its training terms, or an uncaught critical-field error reaches a filed return.
- AI-005: stop permanently if the vendor cannot supply validation data and factor explanations by 2026-12-31, or if adverse impact persists after mitigation.
- Any tool: on shutdown, obtain written confirmation that the vendor and its sub-processors deleted Company data.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Re-tier triggers | Decided by |
|---|---|---|---|---|
| AI-001 | **Approve extraction with conditions; drafting stays off** | Sub-processor assurance (2026-12-31); counsel's written 7216 opinion on extraction and on the 2,100 drafting uses (2026-10-31); mandatory manual verification for photographed documents and flagged name formats (2026-11-30); engagement letter statement on automated data entry (2027 letters) | Drafting re-enabled; offshore processing; e-file without review | Chief Operating Officer, 2026-09-22 |
| AI-002 | **Approve with conditions** | SSN-blocking rule (2026-10-31); counsel confirms the 7216 basis before client names are allowed (2026-10-31); mandatory citation check | Client-facing use without review; vendor term changes | Chief Operating Officer, 2026-09-22 |
| AI-003 | **Approve with conditions** | Mandatory citation check (in force 2026-09-15); anonymized prompts only | Client identifiers in prompts; client-facing access | Chief Operating Officer, 2026-09-22 |
| AI-004 | **Approve with conditions** | Change notice clause and validation on the seeded ledger before each new model version (2027-03-31); PHI ledgers processed only in the enclave | Use as a substitute for auditor selection; new data types | Chief Operating Officer, 2026-09-22 |
| AI-005 | **Auto-ranking suspended; approve only with conditions** | Vendor validation and adverse impact studies and factor explanations (2026-12-31); adverse impact testing each cycle; no score cut-offs; Colorado point-of-interaction notice, adverse-outcome explanation, correction, and human review process live before 2027-01-01; 3-year records; counsel confirms the California position | Any use to reject applicants automatically | Chief Operating Officer, 2026-09-22; noted by the Chief Executive Officer |
| AI-006 | **Prohibited** | Blocking on Company devices and networks (2026-10-31); training on IRC 7216 and AI (POAM-005) | n/a | Chief Operating Officer, 2026-09-22; noted by the Chief Executive Officer |

The conditions are tracked as POAM-021 in P07 and in the risk register (P01 R-032 to R-037). The AI review group's first monthly meeting is scheduled for 2026-10-06.
