# AI Use Assessment: Generative AI Assistant and the City Benefits Pre-Screen (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| Tier / Vertical | Sole Proprietorship / Public Administration |
| AI use case | AI-001: the general-purpose generative AI assistant (SYS-08) used from 2026-07-27 to 2026-07-31 to pre-screen 25 real applications to the city's utility bill assistance program for eligibility. Stopped 2026-08-12. AI-002: the same tool for code and drafting with no agency data |
| Why this use case | Adapted from the registry default ("AI eligibility determination for public benefits"). At this size the owner builds no eligibility system; the risk is one third-party tool pointed at a local benefits program |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-consultant, 2026-09-10; decision 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it did (Map)
The city's program manager asked, by phone, whether "AI could sort the backlog." The owner uploaded 25 applications with their income documents to an individual-plan AI assistant and asked it to label each one likely eligible, likely ineligible, or missing documents against the program's income limits. Six pay stubs showed full Social Security numbers. The plan has **no data agreement**, its setting that lets the provider use conversations to improve its models **was on**, and the city contract allows city data to be used only for the project, with no AI service approved. City staff decided all 25 applications the normal way, without seeing the AI labels.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| City contract (CL-02) | **Yes** | City data may be used only for the project and kept confidential. Sending it to an unapproved service broke that term |
| Fla. Stat. 501.171(2) and (6)(a) | **Yes** | Reasonable measures for personal information (names with Social Security numbers). If the city or its counsel determines a breach, the owner's 10-day notice duty is already met: the owner told the city IT director on 2026-08-13 and sent the facts on 2026-08-17 |
| City program rules | **Yes** | City staff decide eligibility. A consultant's tool may not decide or recommend outcomes unless the city chooses, buys, and governs it |
| Colorado SB26-189 | No | The owner has no Colorado clients. Recheck before any work for a Colorado agency |
| CJIS Security Policy (N92-R02) | Not for AI-001; **yes as a limit on AI-002** | No CJI may leave the sheriff's virtual desktop (POL-01 8.2), so it can never reach an AI tool |

## 3. Risk screen (repository rubric)
**AI-001 tier: High.** Labeling applicants as likely eligible or ineligible for a public benefit makes the tool a likely substantial factor in a consequential decision about essential government services, even if staff sign the decision. **AI-002 tier: Low:** internal drafting with no decisions about people and no agency data. Neither tier allows agency data to go to a provider with no agreement (POL-01 6.1).

## 4. Measure: what the trial showed
The sample is far too small for conclusions, but it shows why High-tier controls matter. Comparing the AI labels with the city's own decisions on the same 25 applications: the labels agreed on 19 (76%). Of the 6 disagreements, 4 labeled eligible households as "likely ineligible"; 3 of those 4 had handwritten benefit letters or Spanish-language pay stubs. No accuracy, bias, or security testing was done before use.

## 5. Data-sharing rules (Govern)
1. **No agency data of any level in any AI tool** unless the tool is on POL-01 Appendix A for that agency, the agency has approved it in writing, and this assessment is repeated (POL-01 9.5).
2. For AI-002, only synthetic sample data and generic descriptions go in: no agency data, credentials, network details, or screenshots of agency systems. The model-improvement setting stays off.
3. **No AI tool may decide or recommend who is eligible for a public benefit** in the owner's work. If an agency wants that, the agency procures and governs it, and the owner's role is limited to configuring the agency's own rules engine with the agency's approval.

## 6. Human review of outputs (Measure and Manage)
For AI-002: the owner reads every line of generated code or text, runs it only against synthetic data, and hands nothing to an agency without its normal test and approval (P03 SA-11). Generated policy citations or legal statements are never used without checking the source.

## 7. Decision (approved 2026-09-15)
**AI-001: stopped, not to resume.** Done or due:
1. Conversations deleted and the model-improvement setting turned off (2026-08-12); a written deletion request sent to the provider (reply due by 2026-09-30).
2. City told on 2026-08-13 and facts supplied on 2026-08-17. The owner supports the city attorney's decision on notice to the 6 residents and pays any notice costs the city asks for.
3. Lessons added to the owner's training notes (POAM-007).

**AI-002: approved with conditions** (section 5 rules 2 and 3; POL-01 9.5). Reviewed each August with the risk register (P01 R-005).
