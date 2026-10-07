# AI Risk Assessment: Generative AI for tax and document preparation

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (CPA and tax preparation firm) |
| Tier / Vertical | Micro / Professional, Scientific, and Technical Services |
| AI use case | **AI-001:** a business-plan generative AI assistant (3 seats, SYS-09), used since 2026-03-02 to draft client letters and IRS notice responses and to summarize uploaded documents |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (Qualified Individual) with the Senior Tax Accountant, 2026-08-25 |
| Decision | Owner CPA, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

**Why this use case.** The registry default for this industry is generative AI for tax and document preparation. At this size the firm does not use the tax software's AI document extraction; it is turned off (AI-002 in the inventory). What the firm actually uses is a general-purpose AI assistant, bought on the Owner CPA's card, so that is the use case assessed here.

## 1. GOVERN
- **Accountable owner:** the Senior Tax Accountant (business owner of AI-001). **Decision authority:** the Owner CPA.
- **Policies that apply:**
  - POL-04 4.7: only approved AI tools; no client names, SSNs, account numbers, addresses, or client documents until counsel confirms an IRC 7216 basis
  - POL-04 4.5: pre-adoption checklist for any new tool or AI feature (the assistant skipped it in March 2026)
  - POL-04 4.6: tax return information is disclosed only under an IRC 7216 permission or the client's prior written consent
  - POL-02 C.2: no client information in unapproved AI tools (AI-003)
- **Approved-tools list:** kept by the Office Manager in POL-04 4.7. It has one entry: AI-001, for the 3 enrolled users only, under the rules in section 5.
- **Scale for a Micro firm:** there is no AI committee. The Owner CPA, the Senior Tax Accountant, and the Office Manager review AI use at the monthly program review (POL-02 A.10).

**How the use started.** The Owner CPA subscribed on 2026-03-02 to save time in the filing season. Three staff used it to draft letters and notice responses and, to get better drafts, uploaded IRS notices for about 40 clients and Forms W-2 for 3 clients. No one checked the vendor's terms or the IRC 7216 basis first (P01 R-013; P03 G-043, G-048, G-051).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Draft client letters (engagement reminders, document request lists, explanations of IRS notices) and first drafts of responses to IRS and state notices. A CPA or enrolled agent edits and signs every item that leaves the firm |
| Users | Owner CPA, Senior Tax Accountant, Tax Accountant (enrolled agent) |
| Affected people | Clients who receive letters or whose notices are answered; people named in uploaded documents |
| Data | Prompts and uploads. From March to July 2026 they included client names, notice text (tax return information under 26 CFR 301.7216-1(b)(3), which covers information received from the IRS in connection with processing a return), and 3 Forms W-2 with full SSNs. Outputs: draft text |
| Vendor terms (business plan) | Inputs are not used to train models by default; inputs are kept up to 30 days for abuse monitoring and may be reviewed by vendor staff if flagged; no commitment to U.S.-only processing; MFA available but not enforced (2 of 3 users had it on) |
| Build or buy | Buy: general-purpose vendor SaaS, not integrated with any firm system |
| Not intended | Tax positions or research conclusions without a human check of every cited authority; return preparation; anything sent without a signature; client-facing chat |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| **IRC 7216 and 26 CFR 301.7216-1 to -3** (N54-R02) | **Yes** | Uploading client notices or documents is a disclosure of tax return information. The preparer-to-preparer permission (301.7216-2(d)(1)) covers disclosures to another **tax return preparer** in the United States. The AI vendor sells a general-purpose tool and does not hold itself out as providing auxiliary services to tax preparers (301.7216-1(b)(2)(i)(B), (iii)), so the firm does not rely on that permission. The contractor permission (301.7216-2(d)(2)) covers programming, maintenance, repair, testing, or procurement of tax software or equipment, not drafting. That leaves the client's prior written consent (301.7216-3(a)(1)), in the form 301.7216-3(a)(3) requires. For Form 1040 filers, no consent may be sought to send an SSN to a preparer outside the United States (301.7216-3(b)(4)); the vendor does not commit to U.S. processing. **This reading is the firm's own; counsel will confirm it in writing by 2026-10-31.** The IRS has issued no AI-specific guidance (P03 section 1.2) |
| FTC Safeguards Rule, 16 CFR 314 (N54-R01) | **Yes** | The vendor is a service provider that must be chosen with care, bound by contract, and reviewed (314.4(f)); a new external application must be evaluated before use (314.4(c)(4)). An unauthorized acquisition of 500 or more consumers' unencrypted information at the vendor would be an FTC notification event (314.4(j)) |
| Circular 230, 31 CFR 10.22 | **Yes** for the CPAs and the enrolled agent | Practitioners must exercise due diligence in preparing papers relating to IRS matters and in representations to clients (10.22(a)). Reliance on another's work product is presumed diligent only with reasonable care in engaging, supervising, training, and evaluating it (10.22(b)). The firm applies that standard to AI drafts: the signer is responsible for every figure and citation |
| Fla. Stat. 501.171 | **Yes, indirectly** | The duty to take reasonable measures to protect personal information covers data sent to an AI vendor; a vendor that stores the data is a third-party agent that must report a breach to the firm within 10 days (501.171(6)(a)) |
| Colorado SB26-189 (ADMT) | **No** | The firm operates in Florida, tax preparation is not a consequential decision category, and the assistant makes no decision about a person |
| ABA Formal Opinion 512 | **No** | Ethics guidance for lawyers, not law, and the firm is not a law firm. Its confidentiality reasoning parallels the IRC 7216 analysis above |
| AICPA Code of Professional Conduct, confidentiality | Noted, not assessed | Professional standard; its text was not verified from the source for this sample |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the assistant does not make, and is not a substantial factor in, a consequential decision about a person. A credentialed professional reviews and signs everything it drafts.
- **Why not Low:** it has processed regulated data (tax return information, SSNs), and its errors can reach clients and the IRS: a wrong response deadline or a nonexistent Code section in a notice response can harm a client.

**Re-tier to High and reassess if:** drafts are sent without a signature; the tool is used to decide tax positions or penalty abatement arguments without a human check of authorities; it is connected to the suite, the tax software, or the portal; client-facing chat is added; or the vendor's terms change to allow training on firm data.

## 4. MEASURE
The Senior Tax Accountant and the Office Manager reviewed 24 drafts from June and July 2026 (16 English, 8 Spanish) and 30 prompts from the conversation history on 2026-08-20.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Every cited Code section, regulation, form, and notice number checked against the primary source; every amount and date checked against the file. Threshold: zero errors reaching a sent item | 5 of 24 drafts had an error: 3 cited a wrong or nonexistent authority (the AI 600-1 "confabulation" risk), 1 carried a wrong amount from the notice, and 1 a wrong response deadline. All were caught before sending except the last: a May 2026 letter told a client the response period was 60 days when the notice said 30. The Tax Accountant found it the next day and called the client | **No** |
| Safe | Every client-facing item reviewed and signed by a CPA or enrolled agent | 24 of 24 signed, but the May letter shows that signing without a checklist misses errors | Partial |
| Secure and resilient | MFA on every seat; vendor security evidence reviewed | MFA on 2 of 3 seats; no vendor security evidence requested before purchase | **No** |
| Accountable and transparent | Owner named; clients told that AI helps draft correspondence | Owner named in this assessment; engagement letters say nothing about AI | Partial |
| Explainable and interpretable | Reviewer can trace each statement in a draft to a source | Drafts give no sources unless asked; the reviewer must check each authority independently | Partial |
| Privacy-enhanced | No client identifiers or documents in prompts; no SSNs ever; U.S. processing; no training; short retention | 22 of 30 prompts contained client names; 9 contained notice text with partial SSNs; 3 uploads contained full SSNs. No training by default; up to 30 days of retention; no U.S. commitment | **No** |
| Fair, with harmful bias managed | Plan below | One group flagged | **No (flagged)** |

**Bias and fairness testing plan.**
| Group compared | Against | Metric | Threshold | Result |
|---|---|---|---|---|
| Spanish-language client letters (many of the firm's Florida clients prefer Spanish) | English-language letters | Share of drafts with a factual, deadline, or authority error found at review | Flag if more than 10 points above the English rate | 3 of 8 Spanish drafts (38%) vs 2 of 16 English drafts (13%). **Flagged.** Small sample, so treated as a real risk until disproved |
| Letters to clients with IRS notices about refundable credits (often lower-income clients) | Letters about balance-due notices | Error rate at review | Flag if more than 10 points apart | 1 of 6 (17%) vs 4 of 18 (22%). Not flagged (small sample; recheck quarterly) |

**Why it matters.** A wrong deadline or a confusing letter costs a client more when the client reads the letter in a second language or has less room to absorb an IRS adjustment. Until the Spanish rate is at or near the English rate, Spanish-language letters are drafted in English with the assistant and translated and checked by a bilingual employee, or written without the assistant.

## 5. MANAGE
**Data protection (in force from 2026-08-31):**
- Use a client code, never a name. No SSNs, ITINs, account numbers, addresses, or uploaded client documents. Paste only the minimum notice text needed, with identifiers removed.
- MFA on every seat; seats added to the monthly account reconciliation (POL-02 B.7); conversation history set to the shortest retention the plan allows.
- The Office Manager asks the vendor in writing to delete all firm conversation history and uploads from March to August 2026 and to confirm deletion (by 2026-09-30).
- Even with identifiers removed, client-specific facts may still be tax return information. Counsel's opinion (condition 3 below) decides whether the de-identified use may continue, or whether consent forms in the 301.7216-3(a)(3) format, following the IRS format guidance for Form 1040 filers, are needed.

**Past uploads.** The Office Manager logged the March to July uploads and the April personal-chatbot paste (AI-003) as one incident under POL-03. Fewer than 50 clients are involved, far below the 500-consumer FTC threshold. Counsel will advise by 2026-10-31 whether IRC 7216 or Florida law calls for any notice to the clients involved, and the firm will follow that advice. The Tax Preparer was retrained under POL-02 A.5.

**Human in the loop:**
- The assistant drafts only. The signer checks every cited authority against the primary source, every amount and date against the client file and the notice, and the response deadline against the notice itself, using a 5-item checklist kept with the file (31 CFR 10.22).
- Spanish-language letters follow the bias rule in section 4.
- **Automation bias (AI 600-1 "human-AI configuration"):** the monthly sample measures what reviewers missed, not only what the assistant got wrong.

**Monitoring:**
- Monthly: 10 drafts and 10 prompts sampled by the Senior Tax Accountant; results logged against P01 R-013 and R-014.
- Quarterly: error rates by language and notice type.
- Vendor terms checked before each filing season and on any change notice.

**Incident handling:** a sent letter with an error is corrected by phone and a follow-up letter, reviewed by the Owner CPA. Client data in an unapproved tool, or a vendor security incident, is handled under POL-03 and the P08 runbook.

**Decommissioning:** cancel the subscription and obtain written confirmation of deletion if counsel finds no workable IRC 7216 basis, if the vendor will not delete past uploads, if an uncaught error reaches the IRS in a signed response, or if the vendor's terms change to allow training on firm data.

## 6. Decision
**Approve with conditions.** Owner CPA, 2026-08-31, on the recommendation of the Senior Tax Accountant and the Office Manager.

Use may continue for the 3 enrolled users only if:
1. From 2026-08-31: the data rules in section 5 (client codes; no identifiers, SSNs, or documents) and the review checklist are in use.
2. By 2026-09-30: MFA on every seat, retention set to the minimum, and the vendor's written confirmation that March to August 2026 content was deleted (P01 R-013; POAM-012).
3. By 2026-10-31: counsel's written opinion on the IRC 7216 basis for de-identified use, on any notice owed for past uploads, and on whether a consent form is worth adopting.
4. Until the Spanish error rate is within 10 points of the English rate: no assistant drafts sent in Spanish without a bilingual check.
5. From the 2027 engagement letters: a plain statement that the firm may use AI tools to help draft correspondence, never with client identifiers, and that a credentialed professional reviews everything sent.

**Any client-identifying use** (names, documents, or SSNs) needs a new assessment and the Owner CPA's approval after counsel's opinion. **AI-002** (the tax software's AI extraction) stays off until it passes the POL-04 4.5 checklist and this assessment is repeated for it. **AI-003** (public and personal chatbots) is prohibited, and the MSP blocks known public chatbots other than the approved assistant on firm computers by 2026-10-31.
