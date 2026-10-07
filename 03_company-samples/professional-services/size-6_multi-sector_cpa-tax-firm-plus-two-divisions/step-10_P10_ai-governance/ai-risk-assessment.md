# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Tax and Advisory, CPA Partners, Wealth, Practice Cloud, corporate) |
| Tier / Vertical | Multi-Sector / Professional, Scientific, and Technical Services (focus division: CPA and Tax Services) |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for the priority use cases: generative AI for tax and document preparation (AI-001, AI-002, AI-003), Practice Cloud's AI document intake feature (AI-007), and Wealth's adviser meeting assistant (AI-005) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 0 High, 8 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the priority use-case report every quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Chief Tax Officer, Wealth Chief Compliance Officer, Practice Cloud chief technology officer, and the CPA Partners risk and quality partner. Approves priority use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report results |
| Group CISO | AI security standard: prompt injection, model supply chain, data leakage, logging |
| Group Chief Privacy Officer | Data use rules, including the IRC 7216 analysis with the Chief Tax Officer and counsel |
| Chief Audit Executive | Includes priority AI controls in the annual internal audit plan from 2027 |

### 1.2 Group AI Standard (adopted 2026 under POL-01 4.13)
1. **Register before use.** Every AI use case that touches tax return information, customer information, customer firms' data, or PHI, or that supports decisions about clients, is registered in the inventory before deployment or material change (POL-01 4.13).
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias testing, and quarterly monitoring reports.
3. **Priority use cases regardless of tier.** Any use case that (a) sends tax return information outside the preparer that holds it, (b) drafts tax treatments or positions, (c) is sold to customers, or (d) creates records a regulator requires is a **priority use case**. It needs council approval, an IRC 7216 and contract analysis, accuracy testing, and quarterly monitoring, even if it is Medium tier.
4. **Data rules.** Restricted information goes only to approved tools whose contracts prohibit training and secondary use and require U.S.-only processing (POL-04 4.8). Model providers are service providers under POL-01 4.9.
5. **Regulator overlays.** Each division supplement adds its regulator's rules: IRC 7216 and Circular 230 for Tax and Advisory; Regulation S-P and Advisers Act records for Wealth; customer agreements and SOC 2 commitments for Practice Cloud; HIPAA business associate terms and professional standards for CPA Partners.
6. **Change gate.** A new model, a new model provider, a new data type, or a new decision role triggers re-assessment before release.
7. **Practitioners stay responsible.** A CPA or enrolled agent is responsible for every figure and statement in a return or client communication drafted with AI assistance (POL-05 4.8; 31 CFR 10.22).

**Where the program fell short in 2026.** The standard was adopted after three priority use cases were already running. The tax drafting assistant pilot (AI-002) started without the IRC 7216 and Circular 230 review (scenario gap 4), Practice Cloud launched AI document intake (AI-007) without the change gate (gap 5), and the audit analytics tool (AI-004) was registered late. All three are now under conditions or have been registered (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Priority | Status |
|---|---|---|---|---|---|
| AI-001 | AI document extraction assistant | Tax and Advisory | Medium | Yes (a) | In production; conditions |
| AI-002 | Tax drafting assistant | Tax and Advisory | Medium | Yes (a), (b) | Pilot; restricted |
| AI-003 | Notice response drafting | Tax and Advisory | Medium | Yes (a), (b) | Pilot; restricted |
| AI-004 | Audit analytics and document testing | CPA Partners | Medium | No | In production |
| AI-005 | Adviser meeting notes and summaries | Wealth | Medium | Yes (d) | Pilot; no expansion |
| AI-006 | Client service email drafting | Wealth | Medium | No | Approved |
| AI-007 | AI document intake feature | Practice Cloud | Medium | Yes (a), (c) | In production; enrollments paused |
| AI-008 | Engineering coding assistant | Practice Cloud | Low | No | Approved |
| AI-009 | Enterprise generative AI assistant | Group | Medium | No | Pilot (6,000 users) |

### 2.1 Generative AI for tax and document preparation (AI-001, AI-002, AI-003): IRC 7216 and Circular 230
| Rule | What it requires | What it means for the use cases |
|---|---|---|
| 26 U.S.C. 7216; 26 CFR 301.7216-1(a) | A tax return preparer may not knowingly or recklessly disclose or use tax return information except as the regulations permit | Every model call that carries client documents or return data is a disclosure to the model provider and must fit a permission or a consent |
| 26 CFR 301.7216-2(d)(1) | Disclosure without consent to another tax return preparer in the United States for preparing a return or for auxiliary services, "so long as the services provided are not substantive determinations or advice affecting the tax liability reported by taxpayers." "A substantive determination involves an analysis, interpretation, or application of the law" | **AI-001** extracts data; counsel's 2025 memo treats the model provider as an auxiliary-services provider under a contract limited to extraction. Counsel must reconfirm (P03 G-048). **AI-002 and AI-003** ask the model to analyze and apply the law, which is a substantive determination, so (d)(1) does not cover them. They need a 301.7216-3 consent, or prompts without client tax return information |
| 26 CFR 301.7216-3(b)(4) | Limits on consent to disclose a Form 1040 filer's SSN to a preparer outside the United States | U.S.-only processing must be a contract term, not only a setting. It is a contract term for AI-001; it is not yet for AI-007 (P03 PC-G06) |
| 26 CFR 301.7216-1(b)(3)(i)(B); 301.7216-2(o) | Statistical compilations of tax return information are tax return information; limited permitted uses | Model evaluation sets and usage analytics built from client data are compilations. Keep them inside Tax and Advisory and use them only for its tax preparation business |
| 31 CFR 10.22(a), (b) | Due diligence in preparing returns and in representations to clients; a practitioner relying on another person's work product is presumed diligent only if it used reasonable care in engaging, supervising, training, and evaluating that person | The group applies the same test to AI tools by policy: evaluate them before use, supervise their outputs, train users, and document the review. Counsel confirms how 10.22(b) applies to software |
| 16 CFR 314.4(c)(4), (c)(7), (f) | Secure development and evaluation of applications; change management; service provider selection, contracts, and periodic assessment | The model provider is a Safeguards Rule service provider (P07 SA-9; POAM-013), and AI changes go through the change gate (POAM-011) |

The IRS Section 7216 Information Center has no guidance on artificial intelligence (checked 2026-09-25 for the Small sample of this industry). These rows apply the regulation text; counsel confirms them.

### 2.2 Practice Cloud AI document intake (AI-007): customer commitments
| Rule or commitment | Implication |
|---|---|
| 26 CFR 301.7216-2(d)(1) (Practice Cloud as an auxiliary-services preparer, group legal position) | Practice Cloud may use customer firms' client data only for the services it provides them. Sending it to a model provider must stay within extraction for return preparation. Each customer firm must also decide its own IRC 7216 basis, so Practice Cloud owes customers the information to decide (P03 PC-G05) |
| Customer agreements and the sub-processor list | Customers were promised notice of new sub-processors. The model provider was added without notice (P03 PC-G14) |
| SOC 2 system description and criteria CC2.3, CC3.4, CC8.1, CC9.2 | The feature and the model provider must be described for the period ending 2026-09-30, and the change must be evaluated. See P09 |
| 16 CFR 314.4(f) (customers' duty) | Customer firms must oversee Practice Cloud as their service provider. They need the model provider's terms and Practice Cloud's monitoring results to do so |
| FTC Act Section 5 (N51-R01) | The "99% accurate extraction" claim must be substantiated or withdrawn (P03 PC-G18) |

### 2.3 Wealth meeting assistant and email drafting (AI-005, AI-006)
| Rule | Implication |
|---|---|
| 17 CFR 275.204-2(a)(7) | Written communications relating to recommendations or advice, receipt or disbursement of funds, and orders must be kept. AI meeting summaries saved to the CRM are such communications and must be in the archive (POAM-019) |
| 17 CFR 248.30(a)(5) | The meeting assistant vendor holds Wealth customer information and is a service provider: due diligence, monitoring, and a 72-hour breach notice term (in place for this vendor) |
| 17 CFR 275.206(4)-7(b) | The annual compliance review must cover the AI pilot (P03 WM-G19) |
| State recording consent laws | In all-party consent states, recording may start only after every party consents. Florida is the worked example (Fla. Stat. 934.03(2)(d)); advisers meet clients in 40 states, so the tool applies the all-party rule everywhere |
| SEC predictive data analytics proposal (S7-12-23) | **Withdrawn** on 2025-06-17 (90 FR 25531). Not an obligation |

### 2.4 Other rules checked
- **CPA Partners (AI-004):** PHI in audit documents may go to the analytics vendor only where the client's BAA and the vendor agreement permit it (N54-R06). The engagement partner remains responsible for audit conclusions.
- **Colorado SB26-189** (effective 2027-01-01) covers automated decision-making technology that materially influences consequential decisions, including financial or lending services. No group use case makes or materially influences such a decision today. Counsel re-checks if Wealth or Practice Cloud adds AI to account approval, suitability, or lending-related features. The law's status is unsettled (litigation and federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`).
- **FTC proposed AI-accuracy policy statement** (July 2026): proposed only, not final as of 2026-09-25. Tracked.

## 3. Risk tiers (repository rubric)
- **High:** none today. No use case makes, or is a substantial factor in, a consequential decision about a person in the rubric's categories, and none affects physical safety.
- **Medium:** AI-001 to AI-007 and AI-009. Humans make the final decision, but outputs enter returns, client records, or customer workflows, or interact with clients.
- **Low:** AI-008.

**Tier is not the whole story here.** The group's main AI risks are **disclosure** (IRC 7216, customer commitments) and **accuracy of tax and advice records**, not consequential decisions. That is why the Group AI Standard adds the priority test (rule 3), which brings AI-001, AI-002, AI-003, AI-005, and AI-007 under council approval and quarterly monitoring.

**Re-tier triggers:** any AI output sent to a client or filed without practitioner review (AI-001 to AI-003 to High); AI used to approve accounts, transfers, or suitability (Wealth, High); AI-007 marketed as producing filing-ready data without customer review (High).

## 4. MEASURE
Results are from a baseline test and pilot reviews run for this assessment between 2026-06 and 2026-08. Ongoing monitoring does not exist yet (scenario gap 4); POAM-011 builds it before the 2027 season.

### 4.1 AI document extraction assistant (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Key-field accuracy on 2,400 documents from the 2026 season, by document type (target 99.5%) | Overall 99.1%. W-2 99.8%; 1099-INT and 1099-DIV 99.6%; 1099-R 99.2%; brokerage composite statements 98.4%; K-1 96.9% | **No** (composite statements and K-1s) |
| Safe (errors reaching clients) | Uncorrected extraction errors in 500 filed returns prepared with AI-001 (target: none that change tax liability) | 6 returns had an uncorrected error; 2 changed tax liability and were amended at no charge | **No** |
| Fair, harmful bias managed | Field error rate by document capture method and language of supporting documents; flag a group above 1.5 times the overall rate. The group collects no demographic data, so these are proxies | Mobile photos 2.3% vs 0.9% overall (flagged); non-English supporting documents 1.4% (flagged); scanned and digital imports within range | **Flagged.** Mandatory second check for photographed and non-English documents |
| Privacy-enhanced | Contract terms: no training, no human review, U.S.-only processing, 30-day deletion | All four in the 2025 contract | Yes |
| Accountable and transparent | Annual assurance review of the model provider | Reviewed at onboarding only (P07 SA-09c.) | **No** (POAM-013) |
| Secure and resilient | Prompt-injection test with crafted source documents | Not done | **No** (added to the POAM-011 test plan) |
| Explainable and interpretable | Each extracted field links to its location in the source document | In place | Yes |

### 4.2 Tax drafting assistant and notice response drafting (AI-002, AI-003)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable (confabulation, AI 600-1) | 150 AI-002 outputs reviewed by senior tax reviewers: incorrect or unsupported statements, such as outdated thresholds or citations to guidance that does not exist (target under 2%) | 8% | **No** |
| Accountable (automation bias) | Share of proposed treatments accepted unchanged; share of accepted treatments with a documented basis | 64% accepted unchanged; basis documented in 41 of 100 sampled | **No** (31 CFR 10.22 diligence) |
| Privacy-enhanced (IRC 7216) | Share of sampled sessions whose prompts contained client tax return information | 92%; no consent covers substantive analysis by the model provider | **No** (restricted from 2026-10-15) |
| Governance | Impact analysis and council approval before the pilot | Not done (P07 CM-04[01], CM-04[02]) | **No** (POAM-011) |

### 4.3 Practice Cloud AI document intake (AI-007), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Field-level accuracy on documents from 25 customer tenants that agreed to testing; compared with the "99% accurate" claim | 98.0% | **No.** Claim withdrawn by 2026-10-31 |
| Information integrity | Document classification accuracy | 97% | Partial |
| Data privacy | No-training terms; U.S. processing as a contract term; per-client request logging | No-training in contract; U.S. region in configuration only; requests not linked to end clients (P03 PC-G03) | **No** |
| Information security | Red-team test with crafted documents | Not done | **No** (POAM-021) |
| Value chain and component integration | Model provider on the sub-processor list, in the system description, and assessed | None of the three | **No** (POAM-020) |
| Human-AI configuration | AI-extracted fields labeled; customer review step in the workflow; feature off unless the customer opts in | In place | Yes |
| Harmful bias or homogenization | Error rate by capture method across tenants | Not measured | **No.** Added to the 2026 Q4 test plan |

### 4.4 Wealth adviser meeting assistant (AI-005)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Accountable and transparent (records) | Share of saved summaries captured in the communications archive (target 100%) | 0% | **No** (POAM-019) |
| Valid and reliable | 100 summaries checked against recordings for misstated client instructions or risk tolerance (target: none saved with an error) | 6 had a misstatement; advisers corrected 4 before saving; 2 were saved with the error | **No** |
| Privacy-enhanced | Recording consent captured from every party before recording (target 100%) | 97% | **No** |
| Secure | Vendor due diligence and 72-hour breach notice term (248.30(a)(5)) | In place | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** preparers verify every extracted field against the source before review. From the 2027 season, fields from photographed, non-English, K-1, and composite documents need a second check. Reviewers see which fields were AI-extracted.
- **AI-002 and AI-003:** from 2026-10-15, prompts may not contain client tax return information until a consent route exists. A proposed treatment can be adopted only with a cited authority recorded by the CPA or enrolled agent. Outputs never go to clients unedited.
- **AI-005:** the adviser approves every summary. Recording starts only after the consent prompt is completed. Summaries are archived before the pilot expands.
- **AI-007:** customer staff review extracted data in the workflow; customers can turn the feature off per tenant; Practice Cloud gives customers the information they need for their own IRC 7216 decision.
- **All:** users can disregard AI output at any time without justification. AI-009 is prohibited for tax treatments, investment recommendations, and attest conclusions.

**Monitoring:** monthly metrics to division owners; quarterly priority use-case report to the council and the board risk committee; P01 risks GR-04, GR-14, TX-008, TX-009, TX-010, WM-006, WM-007, SW-002, SW-003, and SW-009.

**Incident handling:** an AI failure that discloses tax return information or customer data, breaches customer commitments, or produces a wrong filed return follows P08 and POL-03. A model provider breach follows the service provider and customer notice rows in `notification-matrix.csv` (Practice Cloud customer notices; Tax and Advisory's FTC and IRS duties).

**Decommissioning:** each use case has an off switch and a manual fallback that the BIA already covers (P05 BP-T10 and BP-S03 are Low for availability: preparers key data by hand, and customers turn the feature off). A use case is retired if a monitoring target is missed for two quarters in a row, or if counsel finds no lawful IRC 7216 basis for it.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 extraction assistant | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-10) | Counsel reconfirms the 301.7216-2(d)(1) basis by 2026-11-30; second check for flagged document types and monthly accuracy and fairness monitoring live by 2027-01-04; annual model provider assurance review by 2026-11-30 (POAM-011, POAM-013) |
| AI-002 drafting assistant | **Continue the pilot, restricted** | No client tax return information in prompts from 2026-10-15; impact analysis and counsel review of a consent route by 2026-11-30; documented-basis rule enforced in the review tool; no expansion beyond 300 preparers until the confabulation rate is under 2% (POAM-011) |
| AI-003 notice response drafting | **Continue the pilot, restricted** | Same conditions as AI-002 |
| AI-007 AI document intake | **Continue for the 2,300 opt-in customer firms; pause new enrollments** | Accuracy claim withdrawn by 2026-10-31; release gate live by 2026-10-31; system description updated and sub-processor notice with customer information pack sent by 2026-11-30; contract term for U.S. processing, model provider assurance review, and red-team test by 2026-12-31 (POAM-020, POAM-021) |
| AI-005 meeting assistant | **Continue the pilot; no expansion** | Archive capture verified by 2026-12-31; consent prompt made mandatory by 2026-11-30; monthly accuracy sampling (POAM-019) |
| AI-004 audit analytics | **Continue** | BAA and vendor agreement check for PHI by 2026-11-30 |
| AI-006, AI-008, AI-009 | **Approved** | Standard monitoring; AI-009 prohibitions above |
