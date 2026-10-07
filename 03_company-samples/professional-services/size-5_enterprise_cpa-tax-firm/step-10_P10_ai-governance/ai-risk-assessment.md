# AI Governance Risk Assessment: Enterprise AI Portfolio and Generative AI for Tax and Document Preparation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP (national CPA and tax firm; 64 offices in 14 states; privately owned by its partners) |
| Tier / Vertical | Enterprise / Professional, Scientific, and Technical Services |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, generative AI for tax and document preparation, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Risk Officer), meeting of 2026-08-26; the GRC team prepared the portfolio review and Internal Audit observed |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 1, Medium 10, Low 1 |
| Status | In production 10, Suspended 1, Proposed 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-004, AI-007, AI-010, AI-012 (all due 2026-11-30, POAM-020) |
| Use cases that touch tax return information | 9 |
| IRC 7216 basis documented in a counsel memo | 5 of 9 (AI-001, AI-002, AI-003, AI-005, AI-008). Missing: AI-004, AI-006, AI-011, AI-012 (memos due 2026-12-15, POAM-020) |
| Group-level bias testing | Tested 2 (AI-003, AI-005); partial 2 (AI-001, AI-006); not started 3 (AI-004, AI-010, AI-012); not applicable 5 |

**Main findings:**
- Four use cases run without committee review. Three arrived as features in vendor products the firm already licensed (AI-004, AI-007, AI-012) and one was switched on by the HR team (AI-010). This is the gap P03 recorded under 314.4(c)(4) (G-014).
- Four of the nine use cases that touch tax return information have no written IRC 7216 basis (P01 R-014; P03 G-045).
- AI-001, the largest use case, misses its accuracy threshold on photographed and handwritten documents, and two client groups are flagged for higher error rates (P01 R-013).
- AI-007 may send PHI from health care audit files to the audit platform vendor's model service without a business associate agreement covering it. The committee had it switched off for health care engagements on 2026-09-02.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08, Responsible use of AI (P01), which the Audit and Risk Committee of the Partnership Board sees each quarter. Tolerance for ER-08 is Moderate, and ER-08 is within tolerance today only if the POAM-020 dates hold.

**Members:** Chief Risk Officer (chair); National Tax Leader; Vice Chair, Assurance; CISO; Chief Privacy Officer; a delegate of the General Counsel; CIO; Chief Human Resources Officer; Managing Principal, Client Accounting Services; the Director of Professional Standards; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; pre-deployment bias testing on the firm's own data; notice to affected people; human review before action; legal review of state and local AI laws; monitoring plan |
| Medium | Committee vote | IRC 7216 memo where tax return information is involved; human oversight design; output quality monitoring; AI disclosure where people interact with it; security and privacy review; vendor assessment |
| Low | Committee chair (fast track) | Listing on the approved tools list (STD-05.3); data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including an AI feature switched on inside a product the firm already licenses, must be registered and reviewed before use (POL-05 4.5; STD-05.3). Since 2026-06-01, procurement and change management (PRC-01.3) block AI features that have no inventory ID. The GRC team owns the inventory, and the AI pipeline components are being added to the asset inventory (POAM-017).

**Policies that apply:**
- POL-04 4.8: Restricted information may be used in an AI tool only if the tool is on the approved list, the IRC 7216 basis is documented, processing stays in the United States, and the vendor may not train on firm data
- POL-05 4.5: approved tools only; no client data in public AI tools (blocked at the web gateway since 2026-08-10, P01 R-041); qualified review of AI output before it reaches a client or a return
- POL-05 4.8: recording or transcription only with the prior consent of all parties (AI-006)
- POL-01 4.8 and 4.9: service provider assessment and contract terms; written IRC 6713 and 7216 notice to contractor individuals who receive tax return information
- STD-04.4 IRC 7216 Disclosure and Consent Standard; STD-05.3 Approved AI Tools List

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier and client-facing use case; annual re-review of every use case; re-review before any model or vendor change.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| **IRC 7216 and 26 CFR 301.7216-1 to -3** (N54-R02) | **Yes, 9 use cases** | Everything furnished for or derived from return preparation is tax return information (301.7216-1(b)(3)). Each disclosure to an AI provider needs a permission in 301.7216-2 or the taxpayer's prior written consent (301.7216-3(a)(1)). The IRS has issued no AI-specific guidance (P03 section 6), so each memo applies the regulation text (section 5) |
| **FTC Safeguards Rule, 16 CFR 314** (N54-R01) | **Yes** | AI providers are service providers to be selected, bound by contract, and assessed (314.4(f)); externally developed features must be evaluated before use (314.4(c)(4)); a provider breach affecting 500 or more consumers is a notification event for the firm (314.4(j)) |
| IRS e-file rules (N54-R03) | Yes, AI-001 and AI-012 | The ERO transmits only after the taxpayer signs Form 8879 (Pub. 1345), so AI output always passes a preparer, a reviewer, and the taxpayer's signature before filing |
| Circular 230, 31 CFR 10.22 | Yes, for practitioners who use AI-001, AI-004, and AI-012 output | Practitioners must exercise due diligence in preparing returns and in representations to the IRS and to clients. The firm applies the 10.22(b) reliance standard to AI output: reasonable care in selecting, supervising, and evaluating the tool, and the practitioner stays responsible |
| HIPAA as business associate (N54-R06) | Yes, AI-007 | If the feature sends PHI to the vendor's model service, that vendor is a subcontractor, and the firm may allow it only with satisfactory assurances in a business associate agreement (45 CFR 164.308(b)(2); 164.314(a); P03 G-065 and G-070) |
| FAR 52.204-21 (N54-R04) | Yes, AI-002 | The government services practice holds Federal Contract Information in the productivity tenant; the assistant runs inside that tenant under the same safeguards |
| Title VII disparate impact (42 U.S.C. 2000e-2(k)) | Yes, AI-010 | Disparate impact liability remains in the statute, even though federal enforcement priorities changed (EO 14281) |
| NYC Local Law 144 (automated employment decision tools) | Yes, AI-010 for New York City roles | The firm has a New York City office. Before any use for hiring or promotion: a bias audit within 1 year before use, a public summary of results, and candidate notice 10 business days before use |
| Colorado SB26-189 (C.R.S. 6-1-1701 to -1709) | Yes, AI-010, for consequential decisions made on or after 2027-01-01 | The firm does business in Colorado (an office there). Employment is a consequential decision. Deployers must give notice at the point of interaction, explain adverse outcomes, offer correction and meaningful human review, and keep records for 3 years. The law's scope may change (federal preemption push under EO 14365; litigation over its predecessor SB24-205), so the firm plans to the signed text |
| Illinois HB 3773 (Public Act 103-0804) | Likely, AI-010 for Illinois roles | Notice to employees and applicants when AI is used, and no zip codes as a proxy for protected classes. Only partly verified from the source; counsel to confirm |
| State call recording laws | Yes, AI-006 | Laws differ by state, so the firm applies all-party prior consent on every call (POL-05 4.8). Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| FTC Act Section 5 | Indirectly, AI-003 and AI-011 | Accuracy of what the firm tells assignees and clients about AI, and of marketing based on AI insights |
| California CPPA ADMT rules (11 CCR 7200 and following) | Tracked by the Office of General Counsel | Part of the firm's state privacy program, which is outside these deliverables (scenario facts section 1). Relevant to AI-010 if California applicants are screened when it is re-enabled |
| Colorado SB26-189 for the other 11 use cases | No | None makes or materially influences a decision on employment, education, financial or lending services, housing, insurance, health care, or essential government services |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High means the AI makes, or is a substantial factor in, a consequential decision about a person, or can affect physical safety.

| ID | Use case | Tier | Status | Committee review | Tax return information |
|---|---|---|---|---|---|
| AI-001 | Generative AI for tax and document preparation | Medium | In production | Reviewed 2025-11-12; re-reviewed 2026-08-26 | Yes |
| AI-002 | Enterprise generative AI assistant | Medium | In production | Reviewed 2025-10-15 | Yes |
| AI-003 | Global mobility assignee assistant (SL-2) | Medium | In production | Reviewed 2026-01-21 | Yes |
| AI-004 | Tax notice triage and response drafting | Medium | In production | Not reviewed (due 2026-11-30) | Yes |
| AI-005 | Refund and payroll diversion anomaly detection | Medium | In production | Reviewed 2025-12-10 | Yes |
| AI-006 | Contact center call transcription and summary | Medium | In production | Reviewed 2026-02-18 | Yes |
| AI-007 | Audit platform document summarization | Medium | In production (off for health care engagements) | Not reviewed (due 2026-11-30) | No |
| AI-008 | SL-1 invoice coding and bank reconciliation matching | Medium | In production | Reviewed 2026-04-15 | Yes |
| AI-009 | SOC alert triage assistant | Low | In production | Reviewed 2025-09-17 | No |
| AI-010 | Recruiting resume screening and ranking | High | Suspended (ranking off) | Not reviewed (due 2026-11-30) | No |
| AI-011 | Advisory opportunity insights from return data | Medium | Proposed (on hold) | Reviewed 2026-07-22 | Yes |
| AI-012 | Tax return review insights (vendor feature) | Medium | In production | Not reviewed (due 2026-11-30) | Yes |

**Tiering notes:**
- **AI-010 is the only High-tier use case** because ranking applicants is a substantial factor in an employment decision.
- **AI-005 stays Medium.** It delays refunds and payrolls while staff call the client, but a person decides every hold and the screening is not a credit, housing, or other consequential decision. Its hold-rate gap for ITIN filers is still treated as a fairness issue (section 6).
- **AI-009 is Low** because it handles security telemetry and makes no decisions about individuals.
- **The other Medium use cases** all handle regulated data or interact with clients, and in every one a professional makes the final decision.

## 5. IRC 7216 basis by use case
| ID | Basis in the memo or the gap | Conditions |
|---|---|---|
| AI-001 | Use within the firm in the United States (301.7216-2(c)(2)); disclosure to the cloud AI service as a contractor for software used in return preparation (301.7216-2(d)(2)), which makes the provider an auxiliary-services preparer (301.7216-1(b)(2)(iii)). Counsel memo 2025-12-05 | Section 7.2 |
| AI-002 | Same basis and contract terms the firm relies on for the productivity suite itself, which already holds email and files with tax return information. Counsel memo 2026-01-20 | No SSNs or account numbers in prompts; U.S. processing; no training |
| AI-003 | Disclosure to the taxpayer (the assignee) is not a disclosure to a third party; the AI service processes in the United States under the AI-001 contract terms. Counsel memo 2026-01-14 | Status and process answers only; no advice |
| AI-005 | Use by firm members in the United States to assist in preparing and filing the return (301.7216-2(c)(2)); the model runs in the firm's own cloud account. Counsel memo 2025-12-01 | No data leaves the firm's account |
| AI-008 | Use for books and records of the same client (301.7216-2(h)(1)). Counsel memo 2026-04-08 | SL-1 client agreements permit the provider's processing |
| AI-004, AI-012 | **Gap.** Likely preparer-to-preparer processing in the United States (301.7216-2(d)(1)) if the vendors and their sub-processors are in the United States and the features make no substantive determinations; not yet confirmed | Memos due 2026-12-15 |
| AI-006 | **Gap.** Contractor basis expected (as for AI-001), subject to the vendor's data location and staff access terms | Memo due 2026-12-15 (condition of the 2026-02-18 approval) |
| AI-011 | **Gap and design issue.** Counsel's preliminary view: selecting clients from their return data to market non-tax advisory services falls outside the permission for an accountant's other legal or accounting services to the same client (301.7216-2(h)(1)), and the solicitation-list rule covers only tax return preparation services (301.7216-2(n)). The use therefore needs each client's knowing and voluntary written consent (301.7216-3(a)(1)), which may not be a condition of service | On hold until a consent design is approved |

**Substantive determinations.** Disclosure to another preparer for "an analysis, interpretation, or application of the law" needs the taxpayer's consent (301.7216-2(d)(1)). The tax software's AI drafting-suggestion feature would do that, so it was switched off on 2026-08-25 and stays off unless the committee approves a consent design (P01 R-043; P03 G-046).

## 6. MEASURE: portfolio bias testing gaps and plan
| Use case | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-001 | Field error rate; name mismatch rate | Section 7.5 | Section 7.5 | Partial: 4 of 6 comparisons tested, 2 flagged |
| AI-003 | Answer accuracy against the knowledge base | Conversation language (English, Spanish, Portuguese, Mandarin) | Accuracy more than 3 points below English | Tested before launch and quarterly; no gap over threshold |
| AI-005 | Hold rate and false-positive rate | ITIN filers compared with SSN filers; first-time clients; age band (under 30, 30 to 69, 70 and over) | Hold-rate ratio above 1.5 for any group | Tested 2026-06: ITIN filers 2.1 times the overall rate (flagged); other groups within threshold |
| AI-006 | Transcription word error rate and summary accuracy | Call language and accent | More than 3 points above the English baseline | Partial: English and Spanish tested; other languages not yet tested |
| AI-004, AI-012 | Classification and flag accuracy | Return type; client language for AI-004 | Set at committee review | Not started (after review by 2026-11-30) |
| AI-010 | Selection-rate ratio (adverse impact) by sex and race or ethnicity, using the independent bias audit categories | Applicant groups | Ratio below 0.8 for any group compared with the highest group | Not started; required before any re-enable |

**AI-005 mitigation.** ITIN filers are often first-year filers whose bank accounts differ from the prior year, so the model holds them more often. Holds are calls, not denials, but they delay refunds. Since 2026-07 e-file operations calls every held ITIN filer within 1 business day. The model will be retrained without features that track ITIN status, and the hold rate is reported monthly to the committee.

## 7. Full assessment: AI-001 generative AI for tax and document preparation
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Classify each client source document (Forms W-2, 1099, 1098, K-1, brokerage statements, and others), extract the values into the tax software's input fields with a confidence score and a link to the image region, and draft a short preparer summary of what changed from the prior year. The goal is faster, more consistent data entry in the filing season |
| Users / operators | About 4,100 preparers and reviewers; intake staff at the 12 processing hubs; the offshore provider sees extracted data only for business returns covered by consent (PRC-04.1) |
| Affected people | Individual clients and the owners, partners, and beneficiaries named on business returns. In the 2026 filing season the pipeline processed documents for about 240,000 individual and 31,000 business returns |
| Data | Inputs: images of source documents with names, SSNs, income, withholding, and bank details (tax return information and GLBA customer information). Outputs: extracted fields and a draft summary. The AI provider deletes inputs and outputs within 30 days |
| Build or buy | Build: firm-built orchestration in the Tax Engagement Platform on Cloud provider A (P02), calling a contracted cloud AI service with the model version pinned. U.S.-only processing, no training on firm data, and no human review of content are in the contract (DEP-16, confirmed 2026-06) |
| Not intended | Tax positions or advice; e-file without preparer and reviewer sign-off; client-facing output; processing outside the United States. The tax software vendor's separate drafting-suggestion feature is off (section 5) |
| Fallback | Manual keying. The switch-off drill in 2026-07 confirmed the hubs can return to manual entry within one shift (P05 DEP-16) |

### 7.2 IRC 7216 analysis
1. **Inside the firm.** Firm staff in the United States may use a client's tax return information to prepare the return without consent (301.7216-2(c)(2)). The pipeline runs in the firm's own cloud account in the United States.
2. **The AI provider.** Sending document images to the cloud AI service is a disclosure to a third party. Counsel's memo (2025-12-05) treats the provider as a contractor that processes data through software used to prepare returns, under 301.7216-2(d)(2): disclosure only to the extent needed, and a written IRC 6713 and 7216 notice to every individual who receives the information. A person that receives information this way is itself a tax return preparer providing auxiliary services (301.7216-1(b)(2)(iii)), so the provider is bound by section 7216 too. **This is counsel's reading of the text.** The IRS has issued no AI-specific guidance, so the memo also checks that the conditions of the preparer-to-preparer permission in 301.7216-2(d)(1) are met: the provider is in the United States and makes no substantive determinations.
3. **Conditions that make the basis hold.** U.S.-only processing and storage, including any sub-processor (offshore use would need consent, and consent cannot cover the SSNs of Form 1040 series filers, which must be masked before any disclosure outside the United States, 301.7216-3(b)(4)); no human review of content at the provider, so no individual there receives the information, and any future support access requires the written notice first (POL-01 4.9); no training or other secondary use; deletion within 30 days; advance notice of any model or sub-processor change.
4. **Preparer summaries.** The summary describes what changed in the documents. It does not interpret or apply the law, so it is not a substantive determination. If a future version proposed tax treatments, consent would be required (section 5).
5. **Offshore provider.** AI-001 does not change the offshore consent program: extracted data for business returns goes offshore only under signed consents, through the consent gate being built under POAM-008.

### 7.3 Risk tier
**Medium** (section 4). Escalation triggers that require re-tiering and a new assessment: any automatic population of a return that skips preparer verification; enabling tax treatment suggestions; client-facing output; processing outside the United States; a model or provider change without revalidation; vendor terms that allow training on firm data.

### 7.4 MEASURE (2026 filing season, sample of 1,800 returns from February to August 2026, stratified by region and document type)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Field accuracy at least 99.0% on typed and digital forms and at least 97.0% on photographed or handwritten forms; zero critical-field errors (SSN, EIN, wages, withholding, bank routing and account) on filed returns | Typed and digital 99.6%; photographed or handwritten 96.1%; 3 critical-field errors on filed returns (withholding and state wages read from phone photos), corrected by amended returns | **No** |
| Valid and reliable (generative summary) | Unsupported statements in preparer summaries (AI 600-1 confabulation) below 2% of 400 reviewed summaries | 1.5% (6 summaries), all labeled "AI summary, verify against documents" | Yes |
| Safe | Reviewer AI checklist item completed before sign-off on 100% of returns | 96% of sampled returns | Partial |
| Secure and resilient | Red-team test (2026-06) of 40 crafted documents with hidden instructions (AI 600-1 information security, prompt injection); SSO with MFA; isolation of the pipeline | 0 extracted fields changed; 3 summaries altered by hidden text. Isolation in its own account is planned (SC-7(21), 2027-03-31); pipeline components missing from the asset inventory (POAM-017) | Partial |
| Accountable and transparent | Owner named; AI-populated fields labeled; clients told | National Tax Leader owns it; fields labeled; the 2026 engagement letters tell clients the firm uses automated tools, including AI, to enter data from their documents, with professional review | Yes |
| Explainable and interpretable | Each extracted value links to the source image region and shows a confidence score | Available for every field | Yes |
| Privacy-enhanced | U.S.-only processing; no training; no human review of content; deletion within 30 days; IRC 7216 basis documented | Contract terms in place; quarterly deletion attestation received; counsel memo 2025-12-05 | Yes |
| Fair, with harmful bias managed | Plan in 7.5 | 2 groups flagged; 2 comparisons not yet tested | **No** |

### 7.5 Bias and fairness testing plan (AI-001)
Extraction errors follow document quality and name formats, which track client age, language, and how clients send documents. A group with more errors gets more wrong returns, more e-file rejects, and more IRS letters.

| Group compared | Against | Metric | Threshold | Result |
|---|---|---|---|---|
| Clients whose names have compound surnames, hyphens, or accents | All other clients | Name-field mismatch rate against the prior-year return | Flag if more than 1% or more than 2 points above baseline | 2.7% vs 0.5%. **Flagged.** A name mismatch can cause an e-file reject on the name and SSN check |
| Documents photographed on a phone or handwritten (more common for older clients and clients who mail paper) | Scanned typed and digital documents | Field error rate | Flag if more than 2 points above baseline | 3.9% vs 0.4%. **Flagged** |
| Clients with an ITIN | Clients with an SSN | Identification-number field error rate | Flag if above 0.5% or more than 2 points above baseline | 0.3% vs 0.2%. Not flagged |
| Puerto Rico wage statements (Spanish-language forms) | n/a | Supported or not | Unsupported forms go to manual entry, never partial extraction | Routed to manual entry. Pass |
| Clients aged 70 and over | Clients under 70 | Return-level error rate after review | Flag if more than 2 points above baseline | Not yet tested (due 2027-01-08, POAM-020) |
| Global mobility assignees with foreign-language source documents | Domestic clients | Field error rate | Flag if more than 2 points above baseline | Not yet tested (due 2027-01-08, POAM-020) |

Testing runs monthly in the filing season and quarterly otherwise, on the R-013 sample. Results go to the committee each quarter and to the National Tax Leader each month in season.

### 7.6 MANAGE
**Human in the loop:**
- The preparer must verify against the source image every field below the high-confidence level, every critical field, every name field, and every field from a photographed or handwritten document. The tax software enforces this from the 2027 filing season (condition 1 below).
- The reviewer completes the AI checklist item before sign-off; the review template will not close without it.
- The ERO transmits only after the client signs Form 8879. A preparer can reject an extraction and key the return manually at any time.
- **Automation bias (AI 600-1 human-AI configuration).** Reviewers are trained to treat AI-populated fields as unverified entries, and the monthly sample measures what reviewers missed, not only what the AI got wrong.

**Monitoring:**
- Monthly stratified accuracy sample and the bias metrics in 7.5.
- E-file rejects and IRS notices traced to AI-populated fields.
- Provider release notes and sub-processor notices checked by the Director of Tax Technology; no model version change without revalidation on a held-out set of 500 documents.
- Summary injection tests repeated before each filing season.

**Incident handling:**
- A security incident at the AI provider follows P08 and the notification matrix (provider notice to the firm within 10 days under Fla. Stat. 501.171(6)(a) as the worked example; FTC notice if 500 or more consumers are affected).
- An AI error found on a filed return is corrected by an amended return and client notice, reviewed by the engagement partner, and logged for the monthly report.
- A suspected disclosure outside the IRC 7216 basis is an incident under POL-03, assessed by the Chief Privacy Officer and the General Counsel.

**Decommissioning:** switch to manual keying for the firm (tested 2026-07) if the provider changes its data location, training, or human-review terms; if critical-field errors reach filed returns in two consecutive months after the 2027 controls are in place; or if a flagged group gap is not closed by 2027-06-30. On shutdown, obtain written confirmation of deletion from the provider.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier and client-facing use case has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; a breached threshold triggers re-review.
- **Incidents:** AI incidents (harmful output, bias finding, data misuse, unauthorized disclosure) are logged as SOC events and follow P08 where client data is involved.
- **Third parties:** AI providers are tier-1 vendors (STD-01.3). Contracts require U.S. processing, no training, notice of material model changes, and incident notice.
- **Retirement:** a use case is retired if it fails monitoring thresholds twice, if its vendor changes data-use terms, or if its legal basis lapses; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001: approve with conditions** for the 2027 filing season.
   1. By 2026-12-15: mandatory preparer verification of low-confidence, critical, name, and photographed-document fields enforced in the tax software; the review template will not close without the AI checklist item.
   2. By 2027-01-08: the two untested group comparisons completed and a plan for each flagged group (POAM-020).
   3. By 2027-03-31: the pipeline isolated in its own account (SC-7(21)) and its components in the asset inventory (POAM-017).
   4. Summaries stripped of document-embedded instructions and kept labeled as unverified.

   If a flagged group gap is still open at 2027-06-30, the committee re-decides.
2. **AI-004, AI-007, AI-010, AI-012:** committee review by 2026-11-30 and IRC 7216 memos (AI-004, AI-012) by 2026-12-15 (POAM-020). Until then: AI-004 drafts only, with no automatic sending; AI-007 stays off for engagements holding PHI until the vendor signs a business associate agreement or confirms that no PHI leaves the platform; AI-012 shows flags only; AI-010 ranking stays off.
3. **AI-010:** before any re-enable, an adverse impact analysis, an independent bias audit for New York City roles, a Colorado SB26-189 compliance design for decisions from 2027-01-01, and counsel's confirmation of the Illinois requirements. The executive risk committee must approve.
4. **AI-006:** continues; the IRC 7216 memo is due 2026-12-15 or the feature is switched off for the 2027 season.
5. **AI-011:** stays on hold. It may proceed only with a written use consent that meets 301.7216-3 and is never a condition of service, and only for clients who sign it.
6. **AI-002:** continues; the data loss prevention rule for prompts goes live by 2027-01-08 (P01 R-012).
7. **AI-005:** continues with the 1-business-day call-back for held ITIN filers and retraining before the 2027 season.
