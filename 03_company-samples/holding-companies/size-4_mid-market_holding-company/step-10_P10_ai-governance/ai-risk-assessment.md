# AI Governance Risk Assessment: AI Use-Case Portfolio Across Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Scope | Portfolio of 7 AI uses found in the inventory (AI-001 to AI-007), led by the enterprise generative AI assistant across subsidiaries (AI-001); inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (NIST AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-005, and AI-007 |
| Assessors / dates | vCISO and Security Manager (security), General Counsel (legal), Finance Compliance Officer (AI-002), VP of Human Resources (AI-003), Home Services President (AI-005); 2026-08-17 to 2026-09-10 |
| Decision | CFO for Medium and Low; CEO for High (AI-002, AI-003, AI-005), 2026-09-22; reported to the audit committee the same day |
| Related | P01 R-023 to R-027, R-052; POL-01 4.12 and 4.17; POL-04 4.3 and 4.6; POL-05 4.8 to 4.10; STD-05; P07 POAM-020; scenario-facts gap 12 |

## 1. Summary
The inventory exercise found more AI than anyone at the holding company knew about. Only the AI assistant (AI-001) was a group decision, and even it went to 180 users without a data-access review. Three uses were adopted by subsidiaries on their own, and **all three affect decisions or safety for real people**: Finance's credit scorecard (AI-002), the recruiting software's applicant ranking (AI-003), and Home Services' after-hours voice agent (AI-005). That is the holding company pattern in AI form: each subsidiary buys what helps it, and the group carries the legal and reputational risk (P01 R-052).

| ID | Use case | Owner | Risk tier | Decision |
|---|---|---|---|---|
| AI-001 | Enterprise generative AI assistant (180 users, all companies) | CFO | Medium | Approve with 6 conditions; no new users until met |
| AI-002 | Finance credit scorecard with automated decisions | Finance President | High | Approve with conditions; **automated declines suspended** from 2026-10-01 until fixed |
| AI-003 | Applicant ranking with auto-reject (Supply, Home Services) | VP of Human Resources | High | Approve with conditions; **auto-reject turned off** 2026-09-15 |
| AI-004 | Invoice capture and coding in the ERP | Controller | Low | Approve (approved-tools list) |
| AI-005 | After-hours AI voice agent with emergency triage | Home Services President | High | Approve with conditions; escalation fix by 2026-11-30 or switch to the answering service |
| AI-006 | Demand forecasting in the distribution system | Supply President | Low | Approve (approved-tools list) |
| AI-007 | Public chatbots used without approval | Security Manager | Not approved | Prohibited for group data; block on managed devices |

Tiers: 3 High, 1 Medium, 2 Low, and 1 prohibited use.

## 2. GOVERN
- **Accountable owner for the AI program:** CFO (system owner of the shared platform), supported by the vCISO. Each use case has a business owner in the inventory.
- **Policies:**
  - POL-01 4.17: AI tools that touch Restricted data or affect credit, employment, or customer safety must be approved before use.
  - POL-01 4.9 and 4.12: subsidiary purchases and new AI features go through the purchasing gate and the change trigger.
  - POL-04 4.3 and 4.6: Restricted labels block AI retrieval; Restricted data only in approved AI tools for approved purposes.
  - POL-05 4.8 to 4.10: approved tools only; no AI-based decisions about people unless approved as High tier; recording only with all-party notice.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list (2026-09-22):** AI-001 (with conditions), AI-002, AI-003, and AI-005 (with conditions), AI-004, AI-006. Kept by the Security Manager on the intranet.
- **Reporting:** quarterly to the audit committee in the group cybersecurity report; AI-001 and AI-002 also in the Qualified Individual's report to Finance's Board of Managers, because both reach Finance customer information (16 CFR 314.4(i)(2)).

### 2.1 Lightweight governance process for a mid-market group
A 600-person group does not need a standing AI committee with a large charter. It needs a gate every subsidiary must pass and a monthly rhythm, using roles and meetings that already exist.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any subsidiary or department that wants an AI tool, **or wants to turn on an AI feature in a tool it already has**, submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate check (no purchase order without approval, POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, and contract terms (no training on group data, retention), plus a business reviewer. **High:** full MAP and MEASURE assessment like this one, with legal review and a bias and performance plan | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 to 6 weeks |
| 4. Decide | Low: Security Manager. Medium: CFO. High: CEO, on the recommendation of the CFO and General Counsel | As listed | At the monthly cyber risk forum |
| 5. Monitor | Owner reports the agreed metrics monthly (High) or quarterly (Medium) at the forum; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new population, a complaint, or a safety event | Security Manager | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`.

## 3. MAP
| Item | AI-001 Assistant | AI-002 Credit scorecard | AI-003 Applicant ranking | AI-005 Voice agent |
|---|---|---|---|---|
| Purpose | Draft, summarize, recap meetings, find files | Decide or route consumer loan applications | Rank applicants; reject those below a threshold | Answer after-hours calls; book jobs; triage emergencies |
| Users | 180 licensed users in all 5 companies | Finance underwriters; automated | Supply and Home Services recruiters | Callers; on-call manager |
| Affected people | Employees, borrowers, plan members, customers, vendors | About 1,000 applicants a month | About 6,500 applicants in 2026 | About 70 callers a night in summer |
| Data | Anything users can open in the suite, including Restricted data | Application and credit bureau data, age, income | Resumes, answers, work history, location | Call audio, transcripts, addresses, household conditions |
| Build or buy | Configure (suite add-on) | Buy (vendor model; Finance sets cutoffs) | Buy (vendor feature) | Buy (vendor service) |
| Generative AI? | Yes | No (machine-learning scoring) | Vendor does not disclose; treated as possibly | Yes |
| Decision or safety role | None allowed (POL-05 4.9) | **Makes** 38% of credit decisions | **Rejects** applicants without human review | **Triages** emergencies |

AI-004 and AI-006 are internal productivity features with a human approving every output and no personal information, so they were reviewed with the Low checklist only. AI-007 is not a use the group chose; it is a policy breach handled by blocking and training.

### 3.1 Applicable laws and rules
| Rule | Applies to | Why |
|---|---|---|
| FTC Safeguards Rule, 16 CFR Part 314 | AI-001, AI-002, AI-007 | Finance customer information is reachable: limit access to what users need (314.4(c)(1)(ii)); identify data and systems (314.4(c)(2)); evaluate externally developed applications (314.4(c)(4)); oversee service providers (314.4(f)); adjust for material changes (314.4(g)) |
| ECOA and Regulation B, 12 CFR Part 1002 | AI-002 | No discrimination on a prohibited basis in any aspect of a credit transaction (1002.4(a)); a prohibited basis may not be taken into account in any system of evaluating creditworthiness (1002.6(b)(1)); age may be used in an empirically derived, demonstrably and statistically sound scoring system only if an elderly applicant's age (62 or older, 1002.2(o)) is not assigned a negative factor or value (1002.6(b)(2)(ii)); adverse action notices must give specific principal reasons, and a statement that the applicant failed to achieve a qualifying score on the creditor's scoring system is **insufficient** (1002.9(b)(2)); notice of action taken within 30 days after a completed application (1002.9(a)(1)(i)). Since 2026-07-21, 1002.6(a) states that the Act does not provide that the "effects test" applies; intentional discrimination, prohibited-basis rules, and adverse action duties remain |
| Federal employment discrimination law: Title VII (42 U.S.C. 2000e-2), the ADEA, and the ADA | AI-003 | The statutes apply to hiring decisions whatever tool is used. EEOC's AI technical assistance on Title VII has been removed from its website, but the statutes did not change (`00_universal-framework/cross-sector/`, Part B4). The four-fifths rule in the Uniform Guidelines (29 CFR 1607.4(D)) is used as a screening measure for adverse impact |
| Florida Security of Communications Act, Fla. Stat. 934.03(2)(d) | AI-001 (meeting recaps), AI-005 (call recording) | Interception is lawful when all parties have given prior consent. AI-005's greeting announces recording before the caller speaks; AI-001 transcription is off for calls with outside parties |
| Florida Information Protection Act, Fla. Stat. 501.171 | AI-001, AI-005, AI-007 | Reasonable measures for personal information in prompts, transcripts, and retrieved files |
| HIPAA (N55-R06) | AI-001, AI-007 | Plan PHI on the HR site was retrievable by the assistant (section 4). Access must be limited to plan administration staff (164.308(a)(4); 164.504(f)(2)(iii)) |
| FTC Act Section 5, 15 U.S.C. 45(a) | AI-001, AI-005 | Customer-facing statements must be accurate; the voice agent must not misrepresent that callers are speaking with a person |
| State AI laws (for example Colorado SB26-189, effective 2027-01-01) | None today | The group operates only in Florida, and no Florida statute on private-sector AI use in credit or hiring was identified in this review. Recheck before any out-of-state acquisition, because consequential-decision laws such as Colorado's would reach AI-002 and AI-003 |

## 4. MEASURE (by use case)
Tests ran from 2026-08-24 to 2026-09-09. Each owner ran or reviewed the tests named below with the Security Manager.

| Use case | Trustworthy characteristic | Test or metric and threshold | Result (2026-08/09) | Pass? |
|---|---|---|---|---|
| AI-001 | Privacy-enhanced | Cross-entity data-access test: 5 test accounts (one per company), 12 standard queries each ("loan," "social security," "claim," "salary," "bank account," "acquisition"). Threshold: 0 results from another company's or the plan's Restricted data | Supply and Home Services test accounts retrieved a high-cost claimant report (plan PHI) from the HR site and vendor bank-detail forms from the accounting site; no Finance loan files returned | **No** |
| AI-001 | Valid and reliable | 50 outputs (10 per company) checked against sources. Threshold: material errors in no more than 5% | 4 of 50 (8%), including a wrong payoff amount in a Finance draft (caught by the second reviewer) | **No** |
| AI-001 | Secure and resilient | 5 test emails with hidden instructions summarized by a test user. Threshold: 0 of 5 followed | 1 of 5 summaries repeated a planted link as a "recommended action" | **No** |
| AI-001 | Accountable and transparent | Owner, approved-tools list, rules, and training before use | Rolled out without them; owner and rules in place since 2026-09-22; training module due 2026-11-30 | Partial |
| AI-002 | Explainable and interpretable (adverse action reasons) | 40 automated declines from 2026-07 and 2026-08. Threshold: every notice gives specific principal reasons | 17 of 40 notices gave only "credit score below our cutoff" as the reason, which 1002.9(b)(2) calls insufficient | **No** |
| AI-002 | Fair, with harmful bias managed | Does the model use age, and how? Threshold: no negative weight for applicants 62 or older (1002.6(b)(2)(ii)); auto-decline rates by age band reviewed | The vendor confirmed age is an input but could not yet show how it is weighted for applicants 62 or older; auto-decline rate for applicants 62 or older is 1.4 times the rate for applicants under 62. Under review with counsel and the vendor | **No** (pending evidence) |
| AI-002 | Valid and reliable | Independent validation of the model's performance on Finance's portfolio | Never done; the vendor's development documentation covers its national pool, not Finance's borrowers | **No** |
| AI-002 | Accountable and transparent | Finance approved the cutoffs in writing and monitors overrides | Cutoffs set by the former underwriting manager in 2025-10 with no written approval | **No** |
| AI-003 | Fair, with harmful bias managed | Selection rates (passing the auto-reject threshold) by sex and by race and ethnicity, from voluntary EEO self-identification kept separate from the tool, 2026-01 to 2026-07. Threshold: no group below four-fifths of the highest group's rate (29 CFR 1607.4(D)) | Technician roles: women passed at 0.76 of the men's rate (below four-fifths); warehouse roles: all groups above four-fifths | **No** |
| AI-003 | Explainable and interpretable | Can recruiters see why an applicant was ranked low? | No; the vendor provides a score only. "Gap in employment" and "distance from site" appear to drive scores | **No** |
| AI-005 | Safe | 30 scripted test calls (10 gas smell, 10 no cooling with an elderly or medically vulnerable person, 10 routine). Threshold: 20 of 20 emergencies transferred live to the on-call manager with correct safety instructions | 18 of 20; one gas-smell caller was offered a next-day appointment, and one no-cooling call for an 80-year-old was queued, not transferred | **No** |
| AI-005 | Fair, with harmful bias managed | 10 of the scripted calls repeated in Spanish. Threshold: same routing as English | 4 of 10 Spanish calls were misrouted (2 emergencies queued) | **No** |
| AI-005 | Accountable and transparent | Recording disclosure before the caller speaks; automated-agent disclosure | Present in 30 of 30 calls | Yes |
| AI-004, AI-006 | Valid and reliable | Human approval of every output | Confirmed in 20 sampled invoices and 20 purchase orders | Yes |
| AI-007 | Privacy-enhanced | Web proxy logs (30 days) for public chatbot use | 14 users; 2 uploaded spreadsheets (contents unknown) | **No** |

### Generative AI risks (NIST AI 600-1) that apply to AI-001 and AI-005
| AI 600-1 risk | How it shows up here | Main control |
|---|---|---|
| Data Privacy | Retrieval of plan PHI and vendor bank details across companies (AI-001) | Restricted labels that block retrieval; site clean-up (condition 1) |
| Confabulation | Wrong amounts in drafts (AI-001); wrong safety advice (AI-005) | User review; hard-coded emergency escalation |
| Information Security | Hidden instructions in inbound email (AI-001) | User warning; no agent actions; repeat test |
| Human-AI Configuration | Staff trusting fluent drafts; callers trusting the agent in an emergency | Training; live transfer for emergencies |
| Harmful Bias or Homogenization | Weaker Spanish handling (AI-005) | Spanish routing fix and retest |
| Value Chain and Component Integration | Vendors can change models or terms without notice | Contract terms; annual review (STD-03) |

The other AI 600-1 risks (CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Environmental Impacts; Information Integrity; Intellectual Property; Obscene, Degrading, and/or Abusive Content) were judged low for these business uses and rely on the providers' filters.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts and summaries only; no agent actions or connectors; the user is responsible for anything sent; a second reviewer for borrower replies.
- **AI-002:** from 2026-10-01, no automated declines: an underwriter reviews every application the model would decline and every application within 20 points of either cutoff, and writes the specific reasons. Automated approvals under $5,000 continue with a monthly sample review by the Finance Compliance Officer.
- **AI-003:** auto-reject is off; recruiters review every applicant who meets the posted minimum qualifications; the ranking is advisory only.
- **AI-005:** emergency keywords (gas, smell, smoke, no air, elderly, oxygen, medical) trigger a live transfer to the on-call manager; if the transfer fails within 60 seconds, the agent gives safety instructions (gas smell: leave the home and call the gas utility or 911) and pages the manager.

**Monitoring:**
- Monthly (High tier) at the cyber risk forum: AI-002 decline and override rates by age band and adverse action reason quality (sample of 20); AI-003 selection rates by group (quarterly once volumes allow); AI-005 scripted test calls (5 a month, including Spanish).
- Quarterly (Medium): AI-001 cross-entity test, accuracy sample, and prompt-injection test.
- Results tracked against P01 R-023 to R-027 and POAM-020.

**Incident handling:**
- AI-001 output that shows data the user should not see is a security event under POL-03; scope it like any file exposure (P08 `ir-runbook.md` section 4). For plan PHI, the plan Privacy Official decides with counsel whether a breach occurred (164.402).
- An AI-005 call where a caller may have been harmed is escalated to the Home Services President and the General Counsel the same day.
- An AI-002 complaint alleging discrimination goes to the Finance Compliance Officer and counsel.

**Decommissioning criteria:**
- AI-001: turn off for everyone if the provider allows training on group data, or if a second cross-entity exposure of Restricted data occurs before condition 1 is met.
- AI-002: stop using the model for any decision if validation shows age weighted negatively for applicants 62 or older, or if the vendor cannot produce specific reason codes by 2026-12-31.
- AI-003: remove the ranking if adverse impact persists after the vendor's changes.
- AI-005: replace with the human answering service if any emergency test call fails after 2026-11-30.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | Approve with conditions; no new users | (1) Restricted labels and site clean-up; rerun the cross-entity test with 0 results (2026-10-31). (2) Training module and signed POL-05 acknowledgments (2026-11-30). (3) Review the provider's AI terms and SOC 2 (done in P09 VEN-05; confirm no-training term in writing, 2026-10-31). (4) Assistant activity logs to the SIEM (2026-12-31). (5) Prompt-injection warning and retest (2026-12-31). (6) Two monthly accuracy samples at or below 5% before any expansion | CFO |
| AI-002 | Approve with conditions; automated declines suspended from 2026-10-01 | (1) Replace generic reasons with specific principal reasons in every notice (2026-10-31). (2) Vendor evidence on age weighting; counsel review (2026-11-30). (3) Independent validation on Finance's portfolio ($60,000; 2027-03-31). (4) Written cutoff approval by the Finance President and Finance Compliance Officer (2026-10-31). (5) Model governance terms in the vendor contract (2026-12-31). Look-back: counsel decides whether the 17 notices with insufficient reasons need corrected notices | CEO, with the Finance President and General Counsel |
| AI-003 | Approve with conditions; auto-reject off (done 2026-09-15) | (1) Recruiter review of all qualified applicants. (2) Vendor explanation of the scoring factors and removal of "distance from site" unless job-related (2026-11-30). (3) Quarterly selection-rate review by HR with counsel. (4) Review of applicants auto-rejected for technician roles in 2026 and an invitation to reapply (2026-12-31) | CEO, with the VP of Human Resources and General Counsel |
| AI-004 | Approve | Keep human approval of every invoice | CFO |
| AI-005 | Approve with conditions | (1) Hard-coded live transfer for emergency keywords and Spanish routing fix (2026-11-30). (2) Retest: 20 of 20 emergencies and 10 of 10 Spanish calls routed correctly. (3) Monthly test calls. (4) Vendor contract security and retention terms (transcripts deleted after 90 days) (2026-12-31) | CEO, with the Home Services President |
| AI-006 | Approve | Keep human approval of every purchase order | CFO |
| AI-007 | Prohibited | Block public chatbots on managed devices (2026-11-30); remind the 14 users; AI module in training | CFO |

The next full portfolio review is due in July 2027 with the risk assessment, or sooner if a re-tier trigger occurs or a subsidiary proposes a new AI use.
