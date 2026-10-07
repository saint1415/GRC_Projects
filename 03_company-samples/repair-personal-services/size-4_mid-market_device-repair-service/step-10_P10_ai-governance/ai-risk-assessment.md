# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain) |
| Tier / Vertical | Mid-Market / Other Services (except Public Administration) |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry use case "AI-assisted diagnostics and customer chatbot" is AI-002 and AI-001 here; at this size the company runs three more AI tools that need the same governance |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001 and AI-003 |
| Assessors / date | vCISO and Security Manager (security), Privacy and Compliance Manager and General Counsel (privacy and legal), and each business owner, 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-17; the High-tier decision (AI-005) by the Chief Executive Officer the same day |

## 1. Summary
All five tools were adopted by departments without a security, privacy, or legal review (gap 12). None is out of control, but four need conditions before they grow:
- **AI-005, applicant ranking:** recommended women and Black applicants at rates below four-fifths of the highest group's rate. It is the only use case that makes a consequential decision about people (employment). Auto-ranking was paused on 2026-09-18.
- **AI-003, call summaries:** records and summarizes calls with an announcement that does not mention AI, recorded outbound callbacks with no announcement, and captures card numbers read out during payments. That is a Florida recording consent issue (Fla. Stat. 934.03) and a PCI DSS issue.
- **AI-002, diagnostics:** the website claims "97% accurate"; the measured agreement with technicians is 76%.
- **AI-001, chatbot:** customers type passcodes and card numbers into it, and the vendor may keep and train on transcripts.

| ID | Use case | Risk tier | Consequential decision? | Decision |
|---|---|---|---|---|
| AI-001 | Customer chatbot | Medium | No | Approve with conditions |
| AI-002 | AI-assisted diagnostics | Medium | No (influences quotes) | Approve with conditions; no expansion until met |
| AI-003 | Contact center call transcription and summaries | Medium | No | Conditional: conditions by 2026-11-30, or switch off |
| AI-004 | Parts demand forecasting | Low | No | Approve |
| AI-005 | Applicant ranking | High | **Yes (employment)** | Paused; may resume only on conditions |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable executive:** Chief Operating Officer, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.14: AI tools that process customer, claimant, applicant, or employee data, or influence prices, repairs, or decisions about people, must be approved before use.
  - POL-04 4.10: no Restricted or Confidential data in unapproved AI tools; data-use terms with a no-training clause.
  - POL-05 4.9 and 4.10: approved tools only; human check of AI outputs; recording announcements that mention AI summaries.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-004 with their conditions, and AI-005 as paused.
- **Shadow AI:** staff use public generative AI tools for emails and repair write-ups. POL-05 4.9 prohibits customer data in them, and the company will block public tools on company endpoints once an approved enterprise assistant with data-use terms is available (P01 R-031).
- **Claims about AI:** any public statement about AI performance must be approved by the Director of Customer Experience and backed by the measurements in section 4.

### 2.1 Lightweight AI governance process
A 600-person company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm, reusing existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the P10 rubric and checks the purchasing gate (no purchase order without approval, POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (data-use terms, retention, no training), legal (disclosure, consent), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias testing plan and counsel review of employment or other consequential-decision law | Security Manager; Privacy and Compliance Manager; General Counsel | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, Privacy and Compliance Manager, General Counsel, and the business owner), monthly for 30 minutes, with the COO deciding. High: the AI review group recommends; the CEO decides | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (Medium and High); quarterly bias review for High | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new population, or a complaint pattern | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Chatbot | AI-002 Diagnostics | AI-003 Call summaries | AI-004 Forecasting | AI-005 Applicant ranking |
|---|---|---|---|---|---|
| Purpose | Answer questions, give status, book, quote from the price list | Suggest the likely fault and repair | Transcribe calls and draft a ticket note | Forecast part demand and suggest orders | Score and rank applicants |
| Users | Customers on the web and by text; staff take over | About 160 technicians at the Depot and 20 stores | 45 contact center agents | 6 buyers | 5 recruiters and hiring Store Managers |
| Affected people | About 9,000 chats a month | About 700 devices a day and their owners | About 2,400 calls a day | None directly | About 810 applicants a month |
| Data | Questions, first name, ticket status; customers type passcodes and card numbers | Diagnostic logs (may include account identifiers), photos | Call audio, transcripts, summaries; card numbers read out during payments | Parts and sales data only | Resumes, application answers, work history, home ZIP code |
| Build or buy | Configure vendor model | Buy | Configure vendor add-on | Configure ERP module | Configure ATS feature |
| Generative AI? | Yes | No | Yes | No | No |
| Not intended | Approving refunds or claims; collecting payment details or passcodes | Final diagnosis; automatic quotes; repair-or-replace decisions for partner claims | Recording without consent; capturing card data | Automatic purchase orders | Rejecting applicants without human review |
| Re-tier triggers | Approves anything; collects payments | Quotes without a technician; decides repair or replace | Used for quality scoring of agents (employment) | Orders placed automatically | Any automatic rejection; use for promotions |

**Applicable laws and rules (summary; details in the inventory):**
| Rule | Applies to | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a)(1) and 45(n) | AI-001, AI-002, AI-003 | The "97% accurate" claim must be substantiated; customers must not be misled about talking to a person; recommending unneeded repairs or keeping transcripts with credentials can injure customers they cannot avoid |
| Fla. Stat. 501.171(2) and (6) | AI-001, AI-002, AI-003 | Chat transcripts, logs, and call transcripts hold personal information; the vendors are third-party agents with a 10-day notice duty |
| Fla. Stat. 934.03(2)(d) | AI-003 | Interception is lawful when all parties have given prior consent; the inbound announcement does not mention AI summaries, and outbound callbacks had no announcement |
| PCI DSS v4.0.1 (SAQ P2PE and SAQ A eligibility; 3.2.1) | AI-001, AI-003 | Card numbers typed into chat or kept in recordings and transcripts are electronic storage the company's SAQs say does not exist |
| Title VII, 42 U.S.C. 2000e-2(k); 29 CFR 1607.4(D); Fla. Stat. 760.10 | AI-005 | A selection procedure with disparate impact on the basis of race, color, religion, sex, or national origin is unlawful unless job related and consistent with business necessity; the Uniform Guidelines treat a selection rate below four-fifths of the highest group's rate as evidence of adverse impact; Florida law also covers age |
| Utah AI Policy Act as amended (Utah Code 13-72 and 13-75) | AI-001 | Disclose generative AI when a Utah customer clearly asks; the chatbot discloses at the start of every chat anyway |
| Colorado SB26-189 (effective 2027-01-01) | AI-005 | Covers consequential decisions such as employment by deployers doing business in Colorado. The company hires only in Florida, so it is not expected to apply; counsel rechecks if hiring expands |

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | 200 scripted questions; price answers must match the price list | 95% correct; 0 off-list prices | 93% correct; 3 off-list prices | **No** |
| AI-001 | Privacy-enhanced | Passcodes and card numbers in 500 real chats; vendor terms | 0 stored; no training; 30-day retention | 11 passcodes and 3 card numbers stored; terms allow training; indefinite retention | **No** |
| AI-001 | Accountable and transparent | AI disclosure at the start of every chat; handover on request | 100% | Website yes; text messages no | **No** |
| AI-001 | Secure and resilient | 10 prompt-injection tests; connector returns status only | 0 leaks | Connector held; 2 of 10 prompts revealed internal instructions | Partial |
| AI-001 | Fair, harmful bias managed | Correct-answer rate, English vs Spanish | Gap no more than 5 points | 94% vs 86% (8 points) | **No** |
| AI-002 | Valid and reliable | Agreement between the AI's suggestion and the technician's confirmed fault (random sample of 2,400 devices, June to August) | Supports any public claim | 76% overall versus the "97%" website claim | **No** for the claim; acceptable as a triage aid |
| AI-002 | Safe | Missed battery swelling or liquid damage | 0 reach the customer | 6 missed by the AI, all caught by technicians | Partial |
| AI-002 | Fair, harmful bias managed | Agreement and upsell rate by device age and brand | Gap no more than 5 points | Devices 4+ years 66% vs 80%; Manufacturer B laptops 68%; upsell rate 7% | **No** |
| AI-002 | Privacy-enhanced | Account identifiers stripped from uploaded logs | Stripped | Not stripped | **No** |
| AI-003 | Accountable and transparent | Consent: inbound announcement wording; 40 sampled outbound callbacks | All parties told about recording and AI summaries before recording | Inbound says "recorded for quality and training" only; 0 of 40 outbound calls had any announcement | **No** |
| AI-003 | Valid and reliable | 50 summaries compared with the recordings | Material errors under 2% | 4 material errors (wrong device, wrong promised date) = 8% | **No** |
| AI-003 | Privacy-enhanced | Card numbers in transcripts of 50 payment calls; vendor terms | 0; no training | 6 of 50 transcripts held card numbers (manual pause missed); add-on terms allow model improvement use | **No** |
| AI-004 | Valid and reliable | Forecast error versus the buyers' previous method | Better than baseline | 18% versus 24% mean absolute percentage error | Yes |
| AI-005 | Fair, harmful bias managed | Selection rate ("recommended") by sex and by race or ethnicity (4,860 applicants, February to July 2026; self-identification response rate 65%) | Each group's rate at least four-fifths of the highest (29 CFR 1607.4(D)) | Women 21% vs men 31% (ratio 0.68); Black applicants 22% vs White applicants 30% (0.73); Hispanic applicants 24% (0.80) | **No** |
| AI-005 | Explainable and interpretable | Features that drive the score | Job related | Employment gaps and distance from the store (home ZIP code) weigh heavily; neither was validated as job related | **No** |
| AI-005 | Valid and reliable | Vendor validation evidence for technician and advisor roles | Validation study | None provided | **No** |
| All | Secure and resilient | Vendor accounts use company SSO; data-use terms signed | Both | SSO for AI-004 and AI-005 only; data-use terms for none of AI-001 to AI-003 | **No** |

**Bias testing plan (quarterly):**
| Use case | Groups compared | Metric | Threshold | Why |
|---|---|---|---|---|
| AI-005 | Sex; race or ethnicity (voluntary self-identification); age 40 and over vs under 40 | Selection rate at each stage | Four-fifths of the highest group's rate; also test statistical significance | Employment decisions; federal and Florida law |
| AI-002 | Device age; brand; store (median household income of the store's ZIP code as a proxy) | Agreement rate; upsell rate | Gap no more than 5 points (3 points for upsell) | Older devices and some neighborhoods may get worse suggestions and higher quotes |
| AI-001 | Customer language (English, Spanish) | Correct-answer and handover rates | Gap no more than 5 points | A large share of Florida customers prefer Spanish |
| AI-003 | Caller language | Summary error rate | Gap no more than 5 points | Transcription quality often varies by language and accent |

The company does not collect customers' race, ethnicity, or income and will not start collecting them for these tests. The customer-side proxies are imperfect and are used only to find patterns worth investigating. Applicant self-identification data stays in the HR system and is used only for this analysis and EEO reporting.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** cannot change tickets, approve anything, or take payment; customers can type "person" at any time.
- **AI-002:** suggestion only. The technician inspects the device and records their own diagnosis before any quote; the quote screen shows the technician's diagnosis, not the AI's. Repair-or-replace decisions for partner claims are made by the Depot supervisor under the partner's rules.
- **AI-003:** agents review and edit every summary before it is saved; recording pauses automatically during payments (vendor setting, due 2026-10-31).
- **AI-004:** buyers approve every purchase order.
- **AI-005:** paused. If resumed, recruiters must review every applicant who meets the minimum qualifications, and the ranking may only order the review queue; it may not reject anyone.

**Data protection:**
- Mask passcodes and card numbers in chat before they reach the vendor, with a warning when a customer starts typing one (POL-04 4.3 and 4.5).
- Data-use addenda for the chatbot, diagnostics, and contact center AI vendors: no training on company data, 30-day retention, deletion on request, breach notice within 72 hours (POL-01 4.9; POAM-009).
- Strip account identifiers from diagnostic logs before upload.

**Claims:** remove "97% accurate" by 2026-10-15. Any future claim must state what was measured, for example "the tool's first suggestion matched our technicians' diagnosis for 76% of devices in our June to August 2026 data", and be refreshed quarterly.

**Monitoring:** owners report section 4 metrics monthly to the AI review group; AI-005 also gets the quarterly bias review. Results feed the risk register (P01 R-025 to R-031).

**Incident handling:** a vendor security incident, or AI output that exposes another customer's data, follows P08 and the vendor's notice terms. A complaint pattern (for example several customers disputing AI-influenced quotes) triggers a re-review.

**Decommissioning criteria:**
- AI-001 and AI-003: switch off if the data-use addendum is not signed by 2026-11-30.
- AI-002: stop if a bias flag stays open two quarters in a row, or if the vendor changes its data-use terms.
- AI-005: retire if the vendor cannot provide validation evidence and remove the gap and distance features by 2027-03-31.
- Any tool: stop if the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | AI disclosure on text messages; passcode and card-number masking (also protects the SAQ eligibility); off-list prices blocked; Spanish answers reviewed and retested; data-use addendum, all by 2026-11-30 | COO, 2026-09-17 |
| AI-002 | **Approve with conditions**; no expansion to the remaining 14 stores until met | Claim removed (2026-10-15); technician diagnosis enforced before quoting (2026-10-31); identifiers stripped (2026-11-30); vendor response on older devices and Manufacturer B laptops (2026-12-31) | COO, 2026-09-17 |
| AI-003 | **Conditional** | Outbound recording off (done 2026-09-18); inbound announcement updated to mention AI summaries (2026-10-31); automatic payment pause (2026-10-31); purge card numbers from existing transcripts; data-use addendum (2026-11-30), or switch off | COO, 2026-09-17 |
| AI-004 | **Approve** | Annual re-review | Security Manager (Low tier), noted by the COO, 2026-09-17 |
| AI-005 | **Paused**; may resume only on conditions | Vendor validation evidence for the roles; removal of the employment-gap and distance features; human review of every minimally qualified applicant; two consecutive quarters with no four-fifths flag in a shadow test; counsel review of the applicants affected February to September 2026 | CEO, 2026-09-17, on the AI review group's recommendation |

The conditions are tracked as POAM-022 in P07 and in the risk register (P01 R-025 to R-031). The AI review group holds its first monthly meeting on 2026-10-07.
