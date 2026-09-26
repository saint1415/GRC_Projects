# AI Risk Assessment: Generative AI for tax and document preparation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Small / Professional, Scientific, and Technical Services |
| AI use cases | **AI-001:** the tax software's generative AI document extraction and return-drafting feature, pilot with 8 preparers since June 2026. **AI-002:** the enterprise generative AI assistant in the productivity suite, used to draft client letters and IRS notice responses, pilot with 15 users since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Risk and Quality Partner (chair of AI use reviews) with the Tax Partner and the IT Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owners:** Tax Partner for AI-001 (business owner of the tax practice and the IRC 7216 consent process). Risk and Quality Partner for AI-002.
- **Decision authority:** Firm Administrator for Medium-tier use cases, on the recommendation of the AI use review. Managing Partner if a use case is re-tiered High.
- **Policies that apply:**
  - POL-04 4.9: no Restricted data in an AI tool unless it is on the approved list and the Tax Partner has confirmed the IRC 7216 basis
  - POL-05 4.9: approved tools only; never paste client data into public tools; human review of all AI output
  - POL-04 4.4: the data inventory must name AI sub-processors
  - POL-01 4.9 and 4.10: service provider due diligence and the written IRC 6713 and 7216 notice to contractors
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 (pilot preparers only, extraction only) and AI-002 (pilot users only, with the data rules in section 5). Public chatbots (AI-003) are prohibited.
- **Scale for a 60-person firm:** there is no AI committee. The Risk and Quality Partner, Tax Partner, and IT Manager hold a quarterly AI use review, and any new AI feature in an existing product goes through the pre-adoption review (P03 G-014; P09 CC3.4). That review did not happen for AI-001, which the vendor turned on as a feature update.

## 2. MAP
### 2.1 AI-001: tax software document extraction and return drafting
| Item | Description |
|---|---|
| Purpose and intended use | Read scanned source documents (Forms W-2, 1099, 1098, K-1) and fill the matching input fields in the return, with a confidence score and a link to the source image for each field. The goal is to cut data entry time in the filing season |
| Second feature (return drafting) | The vendor also offers AI "drafting suggestions": proposed treatments, carryovers, and explanations. **Disabled** by the firm on 2026-08-25 pending the IRC 7216 analysis below |
| Users / operators | 8 pilot preparers; reviewers (CPAs and enrolled agents) check the returns |
| Affected people | Individual clients whose documents are processed. About 410 extension-season returns went through the pilot from June to August 2026 |
| Data | Inputs: scanned source documents containing names, SSNs, wages, withholding, and bank details (tax return information and customer information). Outputs: extracted field values. The vendor sends the images to an AI sub-processor that the firm has not reviewed. The vendor's terms allow it to use "de-identified data to improve services" |
| Build or buy | Buy: a feature of the vendor-hosted tax software (SYS-01). The underlying model is supplied by the sub-processor |
| Not intended | Tax positions or advice, e-file without preparer and reviewer sign-off, client-facing chat, or processing outside the United States |

### 2.2 AI-002: enterprise AI assistant for client letters and notice responses
| Item | Description |
|---|---|
| Purpose and intended use | Draft client letters, engagement correspondence, and first drafts of responses to IRS and state notices. A CPA or enrolled agent edits and signs every item sent |
| Users / operators | 15 pilot users (partners, tax managers, client advisory staff) |
| Affected people | Clients who receive letters or whose notices are answered |
| Data | Prompts may contain client names, notice text, and amounts (tax return information). The enterprise terms say prompts and files stay in the firm's tenant, are processed in the United States, and are not used to train models |
| Build or buy | Buy: a licensed feature of the productivity suite (SYS-06) |
| Not intended | Tax research conclusions without a human check of every cited authority; SSNs or bank numbers in prompts |

### 2.3 Applicable laws and rules
| Rule | Applies? | Why |
|---|---|---|
| **IRC 7216 and 26 CFR 301.7216-1 to -3** (N54-R02) | **Yes, both use cases** | Everything in a client's documents is tax return information (301.7216-1(b)(3)). Sending it to an AI service is a disclosure that must fit a permission in 301.7216-2 or have the taxpayer's prior written consent (301.7216-3(a)(1)). The IRS has issued no AI-specific guidance (P03 section 1.2), so this analysis applies the regulation text, and counsel will confirm it in writing by 2026-10-31. See section 2.4 |
| FTC Safeguards Rule, 16 CFR 314 (N54-R01) | **Yes** | The vendor and its AI sub-processor are service providers that must be overseen and bound by contract (314.4(f)); a new externally developed feature must be evaluated before use (314.4(c)(4)); the change should pass change management (314.4(c)(7)); a sub-processor breach can be an FTC notification event for the firm (314.4(j)) |
| Circular 230, 31 CFR 10.22 | **Yes** for the CPAs and enrolled agents who practice before the IRS | Practitioners must exercise due diligence in preparing returns and in representations to the IRS and to clients. Under 10.22(b), relying on another's work product is presumed diligent only with reasonable care in engaging, supervising, training, and evaluating that work. The firm applies the same standard to AI output: the preparer and reviewer remain responsible for every figure and statement |
| Fla. Stat. 501.171 | **Yes, indirectly** | The duty to take reasonable measures to protect personal information (501.171(2)) covers data sent to AI vendors. A vendor that maintains or processes the data is a third-party agent that must report a breach to the firm within 10 days (501.171(6)(a)) |
| FTC Act Section 5 | Indirectly | Applies to the vendors' accuracy and data-use claims and to anything the firm tells clients about its use of AI. Keep the vendor claims the firm relied on in the procurement file |
| Colorado SB26-189 and the California CCPA ADMT rules | **No** | Tax preparation is not one of the consequential or significant decision categories, and the firm makes no decision about a person with these tools. The firm is also not a CCPA "business" (receipts below the $26,625,000 threshold and no sale of personal information) |
| AICPA Code of Professional Conduct, confidentiality | Noted, not assessed | Professional standard; its text was not verified from the source for this sample (scenario facts section 1) |

### 2.4 IRC 7216 analysis
1. **Extraction by the vendor may fit the preparer-to-preparer permission.** 301.7216-2(d)(1) lets a preparer disclose tax return information without consent to another tax return preparer **located in the United States** for auxiliary services, including having that preparer "transfer that information to, and compute the tax liability on, a tax return" by electronic processing, **so long as** the services are not substantive determinations. The vendor is itself a tax return preparer (a software developer and Authorized IRS e-file Provider, 301.7216-1(b)(2)(i)(B)). **Open point:** the sub-processor's location and role are unknown, so the firm cannot yet show the condition is met (P03 G-045).
2. **SSNs must stay in the United States.** For Form 1040 series filers, a U.S. preparer may not even obtain consent to send the SSN to a preparer outside the United States, except under the IRS's adequate-safeguards conditions (301.7216-3(b)(4)). Scanned W-2s always contain SSNs, so U.S.-only processing is a hard requirement (P03 G-050).
3. **Drafting suggestions are likely "substantive determinations."** The regulation defines a substantive determination as "an analysis, interpretation, or application of the law" (301.7216-2(d)(1)), and disclosure to another preparer for that purpose needs the taxpayer's consent. AI-proposed treatments fit that description. The firm's decision is to keep the feature **off** rather than seek consent, because consent must be knowing and voluntary and may not be a condition of service (301.7216-3(a)(1)).
4. **No training or secondary use.** Any use of client data by the vendor or sub-processor beyond preparing the firm's returns (for example, model training, even "de-identified") is not covered by the (d)(1) permission. The firm will not rely on consent for this; it will require a contract prohibition.
5. **Human access at the sub-processor.** If sub-processor staff can view content (for example, for abuse monitoring), each person must receive the written notice described in 301.7216-2(d)(2), or the access must be turned off by contract. The firm will require it to be turned off.
6. **AI-002.** The productivity suite vendor already holds client email that contains tax return information. The firm treats the enterprise assistant as part of that same software service and relies on the vendor's U.S.-processing and no-training terms. **This reading is the firm's own and counsel must confirm it.** Until then, prompts must not contain client names, SSNs, or account numbers (section 5).
7. **AI-003 (public chatbots) is an unauthorized disclosure.** The 3 staff who pasted client notice text into public chatbots (P03 G-043) made disclosures that no permission covers. The Risk and Quality Partner reviewed them as incidents under POL-03: the text contained names and notice amounts but no SSNs, and the count is far below the 500-consumer FTC threshold. Each case was documented, and the staff members were retrained under POL-01 4.11.

## 3. Risk tier
**AI-001: Medium. AI-002: Medium. AI-003: High (if client data is entered), and prohibited.** Rubric: `00_universal/projects/P10_ai-governance/README.md`.

**Why not High:** neither tool makes, or is a substantial factor in, a consequential decision about a person in the rubric's categories. A preparer and a reviewer check every AI-populated field, and a credentialed professional signs every letter.

**Why not Low:** both process regulated data (tax return information and customer information), both depend on outside AI providers, and their errors reach clients: a wrong withholding amount changes a refund, and a wrong citation in a notice response can harm a client's position.

**Escalation triggers (re-tier to High and re-assess):**
- e-filing or delivering AI output without human review
- enabling drafting suggestions or any feature that proposes tax positions
- any processing outside the United States
- a client-facing AI chat or intake assistant
- vendor terms that allow training on firm data

## 4. MEASURE
### 4.1 AI-001 (pilot results, June to August 2026)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly sample of 20 returns per preparer (P01 R-014): every AI-populated field compared with the source document. Thresholds: field accuracy at least 99% on typed forms and 97% on photographed or handwritten forms; zero critical-field errors (SSN, EIN, wages, withholding, bank routing and account) reaching a signed return | 320 returns (July and August). Typed forms 99.4%. Photographed or handwritten 95.8%. 2 critical-field errors (withholding transposed on a phone photo of a W-2; state wages on a multi-state W-2), both caught at review | **No.** Photographed and handwritten forms miss the threshold |
| Safe | No return transmitted until a reviewer signs off on AI-populated fields; reviewer checklist item for those fields | All 410 pilot returns reviewed before transmission. The checklist item is not yet in the review template (due 2026-11-30) | Partial |
| Secure and resilient | Vendor SOC 2 covers the feature; sub-processor assessed; access through SSO with MFA | Tax software access is through SSO with MFA. The SOC 2 report does not cover the feature and the sub-processor is unreviewed (P09 Part B) | **No** |
| Accountable and transparent | Clients told that AI assists with data entry; AI-populated fields labeled in the software; owner named | Fields are labeled and the owner is named. The engagement letter says nothing about AI | Partial |
| Explainable and interpretable | Each extracted value links to the source image region and shows a confidence score | Available for every field | Yes |
| Privacy-enhanced | U.S.-only processing; no training or secondary use; no human review of content at the sub-processor; deletion of images within 30 days; IRC 7216 basis confirmed | None of these is yet in contract. The vendor's terms permit use of de-identified data | **No** |
| Fair, with harmful bias managed | Plan in 4.2 | Two groups flagged | **No** |

### 4.2 Bias and fairness testing plan (AI-001)
Extraction errors are not spread evenly. They follow document quality and name formats, which track client age, language, and income, so some client groups could get more wrong returns, more e-file rejects, and more IRS letters.

| Group compared | Against | Metric | Threshold | Result |
|---|---|---|---|---|
| Clients whose names have compound surnames, hyphens, or accents (common in the firm's Florida client base) | All other clients | Name-field mismatch rate against the prior-year return | Flag if more than 1% or more than 2 points above baseline | 3.1% vs 0.4%. **Flagged.** A name mismatch can cause an e-file reject on the name and SSN check |
| Documents photographed on a phone or handwritten (more common for older clients and clients without scanners) | Scanned typed documents | Field error rate | Flag if more than 2 points above baseline | 4.2% vs 0.6%. **Flagged** |
| Clients with an ITIN instead of an SSN | Clients with an SSN | Identification-number field error rate | Flag if above 0.5% or more than 2 points above baseline | 0.3% vs 0.2%. Not flagged (small sample: 22 returns) |
| Puerto Rico wage statements (Spanish-language forms) | n/a | Supported or not | Unsupported forms must go to manual entry, never partial extraction | Not supported by the vendor; routed to manual entry. Pass |

Testing runs monthly in the filing season and quarterly otherwise, on the R-014 sample. Results go to the quarterly AI use review.

### 4.3 AI-002 (pilot, May to August 2026)
| Check | Result | Pass? |
|---|---|---|
| Accuracy of citations: a reviewer checks every Code section, regulation, form, and notice number in 30 sampled drafts | 4 of 30 drafts cited a wrong or nonexistent authority (the AI 600-1 "confabulation" risk); all were caught before sending | **No** without mandatory citation check |
| Prompt content: 30 sampled prompts checked for client identifiers | 2 contained a full SSN; 11 contained a client name | **No** |
| Human sign-off: every client-facing item signed by a CPA or enrolled agent | 30 of 30 | Yes |
| Tenant and data terms: U.S. processing, no training, no human review of content | Confirmed in the enterprise terms reviewed 2026-08-20 | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the preparer must verify every field with a confidence score below the vendor's high-confidence level, every critical field, and every field from a photographed or handwritten document, against the source image. The reviewer ticks the AI checklist item before sign-off. The ERO transmits only after the client signs Form 8879. A preparer can reject an extraction and key the return manually at any time.
- **AI-002:** drafts only. The signer checks every cited authority against the primary source and every amount against the file. No SSNs, bank numbers, or client names in prompts until counsel confirms the IRC 7216 basis; use a client code instead.
- **Automation bias (AI 600-1 "human-AI configuration"):** reviewers are trained to treat AI-populated fields as unverified entries, and the monthly sample measures what reviewers missed, not only what the AI got wrong.

**Monitoring:**
- Monthly R-014 sample and the bias metrics in 4.2, reported at the quarterly AI use review.
- Vendor release notes and sub-processor change notices checked by the Tax Partner before each filing season.
- Data loss prevention rule blocking SSNs in AI-002 prompts (IT Manager, by 2026-10-31).
- Client complaints and e-file rejects traced to AI-populated fields.

**Incident handling:**
- A security incident at the vendor or sub-processor follows P08 and the notification matrix (vendor notice to the firm within 10 days under Fla. Stat. 501.171(6)(a); FTC notice if 500 or more consumers).
- An AI error found in a filed return is corrected by amended return and client notice, reviewed by the Tax Partner.
- Client data in a public chatbot is an incident under POL-03 (as in section 2.4 item 7).

**Decommissioning:**
- Turn AI-001 off for the firm (vendor setting) if the contract terms in condition 1 below are not signed by 2026-10-31, if processing moves outside the United States, or if an uncaught critical-field error reaches a filed return.
- Turn AI-002 off if the vendor changes its training or data-location terms.
- On shutdown, obtain written confirmation of deletion of firm data from the vendor and sub-processor.

## 6. Decision
**AI-001: approve with conditions.** Firm Administrator, 2026-08-31, on the recommendation of the Risk and Quality Partner and the Tax Partner. The pilot may continue for the 8 enrolled preparers, extraction only, **only if** these conditions are met:
1. By 2026-10-31: a contract amendment requiring U.S.-only processing and storage (including the sub-processor), no training or secondary use of firm data, no human review of content at the sub-processor, image deletion within 30 days, and advance notice of sub-processor changes (POAM-010; P01 R-013; P03 G-045, G-050).
2. By 2026-10-31: counsel's written confirmation of the 301.7216-2(d)(1) basis for extraction. Drafting suggestions stay off.
3. By 2026-11-30: the AI checklist item is in the review template (P01 R-014), and manual verification of name fields and photographed or handwritten documents is mandatory.
4. From the 2027 engagement letters: a plain statement that the firm uses automated tools, including AI, to enter data from client documents, with preparer review.

Expansion to all preparers for the 2027 filing season requires conditions 1 to 3, two consecutive monthly samples at threshold, and no open bias flag. The Tax Partner decides by 2027-01-05.

**AI-002: approve with conditions.** Firm Administrator, 2026-08-31. Continue for the 15 pilot users with the prompt rules in section 5, the SSN-blocking rule by 2026-10-31, mandatory citation checks, and counsel's confirmation of the IRC 7216 basis by 2026-10-31 before client names may be used.

**AI-003: prohibited.** Public generative AI chatbots are blocked on firm devices by 2026-10-31 (P01 R-012), and the training in POAM-013 covers IRC 7216 and AI use.
