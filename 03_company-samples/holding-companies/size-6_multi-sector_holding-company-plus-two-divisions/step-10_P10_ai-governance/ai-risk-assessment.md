# AI Governance Risk Assessment: Group AI Program and the Enterprise Generative AI Assistant | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (holding company, Insurance, Health Care Services) |
| Tier / Vertical | Multi-Sector / Management of Companies and Enterprises |
| Scope | The group AI governance program (group standard, inventory, regulator-specific rules) and a full assessment of the priority use case: **AI-001, the enterprise generative AI assistant across subsidiaries**. Division use cases AI-002 (claims fraud scoring) and AI-006 (triage and sepsis alert) are measured against their regulator-specific rules |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / dates | Group AI council (chaired by the Group Chief Risk Officer). Tests 2026-08-17 to 2026-08-21; council review 2026-08-27; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 4 High, 4 Medium, 2 Low) |
| Related | P01 GR-10, GR-15, GR-22, INS-008, INS-014, INS-018, HCS-007, HCS-008, HCS-016; POL-01 4.14, POL-04 4.6, POL-05 4.6; P07 POAM-023; scenario gap 9 |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list each quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group CIO, Group Chief Human Resources Officer, Insurance chief compliance officer, Health Care Services chief medical officer. Approves High-tier use cases, the approved-tools list, and AI-001 expansion |
| Division AI owners | The business owner named for each use case in the inventory; run monitoring |
| Group CISO | AI security standard (prompt injection, data leakage, model supply chain) |
| Group Chief Privacy Officer | Labels, entity boundaries, BAAs, and data use for AI |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06-15, under POL-01 4.14)
1. **Register before use.** Every AI use case that touches Restricted data or supports decisions about people is registered before deployment or material change, including AI features that vendors switch on in existing SaaS.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier needs council approval, an impact assessment, bias testing before deployment, and quarterly monitoring reports.
3. **Entity boundaries apply to AI.** An AI tool may only reach a regulated entity's Restricted data for that entity's approved purpose (POL-04 4.2, 4.6). The assistant does not know which company a user works for; labels and permissions must do that work.
4. **Contracts first.** AI vendors that handle PHI sign BAAs (or confirm the AI feature is inside the existing BAA) with no-training terms; AI vendors that handle the insurers' nonpublic information are overseen as Third-Party Service Providers (Model #668 sec. 4F as enacted).
5. **Regulator overlays.** Division supplements add the NAIC AI Model Bulletin elements for Insurance (adopted in North Carolina, applied group-wide by choice) and Section 1557 (45 CFR 92.210) for Health Care Services.
6. **Approved tools only** for workforce generative AI (POL-05 4.6).

**Where the program fell short in 2026.** The assistant pilot began on 2026-05-04, six weeks before the standard existed, with 6,000 users in three regulated divisions and no labels, training, or confirmation that the AI add-on was inside the productivity vendor's BAA (scenario gap 9). The HCM vendor also switched on resume screening (AI-008) in 2026-03 without review; it was turned off in 2026-06.

## 2. MAP
### 2.1 Division use cases
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Enterprise generative AI assistant | Group | Medium | Pilot (6,000 users); continue with conditions |
| AI-002 | Claims triage and fraud scoring | Insurance | High | In production |
| AI-003 | Photo-based auto damage estimating | Insurance | Medium | In production |
| AI-004 | Homeowners pricing with aerial imagery | Insurance | High | Proposed; not approved |
| AI-005 | Workers' compensation bill review | Insurance | Medium | In production |
| AI-006 | Urgent care triage and sepsis alert | Health Care Services | High | In production |
| AI-007 | AI scribe pilot | Health Care Services | Medium | Proposed; not approved |
| AI-008 | Resume screening in HCM recruiting | Group | High | Retired (turned off) |
| AI-009 | Accounts payable invoice capture | Group | Low | In production |
| AI-010 | Developer coding assistant | Group | Low | Approved |

### 2.2 AI-001: the enterprise assistant
| Item | Description |
|---|---|
| Purpose | Draft and summarize email and documents, recap internal meetings, and find information in files the user can already open |
| Users | 6,000 pilot users: holding company 1,800; Insurance 2,900 (claims, underwriting, service); Health Care Services 1,300 (administrative and clinic management staff; clinicians not enrolled) |
| Affected people | Employees and former employees, plan members, policyholders and claimants, patients, and deal counterparties, because the assistant can surface their information and draft messages to them |
| Data inputs | Prompts, plus anything the user can open: email, chat, collaboration sites, and meetings. That includes Restricted data of four regulated populations and MNPI |
| Training | None by the group. The vendor's enterprise terms say prompts and outputs are not used to train its models |
| Features off | Connectors to SYS-G4, SYS-G5, SYS-I1, SYS-I2, SYS-H1; agent actions; transcription of calls with outside parties |
| Not intended | Any decision about hiring, discipline, pay, insurance coverage, claims, or patient care; clinical or legal advice; translating regulated notices |

**Why AI-001 is a holding company risk.** One assistant in one tenant serves four regulated populations held by different legal entities with different laws. Every over-shared site in any division becomes searchable by staff in the other divisions, and the assistant does it at scale.

### 2.3 Applicable laws and rules
| Rule | Use cases | What it means here |
|---|---|---|
| HIPAA Security and Privacy Rules (N62-R01, N62-R02) | AI-001 (Health Care Services and plan data), AI-006, AI-007 | A vendor that handles PHI for Health Care Services or the plan needs a BAA covering the AI feature (164.308(b)(1); 164.502(e)). Scope for the AI add-on was not confirmed before Health Care Services staff were enrolled. Plan PHI must stay with the plan administration unit (164.504(f)(2)(iii)) |
| State insurance data security laws based on Model #668 (N52-R07) | AI-001 (Insurance users), AI-002, AI-003, AI-005 | Access only for authorized individuals (sec. 4D(2)(a)); program adjusted for material changes such as new AI tools (sec. 4G); AI vendors overseen as Third-Party Service Providers (sec. 4F) |
| NAIC AI Model Bulletin (North Carolina Bulletin No. 24-B-19) | AI-002, AI-003, AI-004, AI-005; AI-001 if used in claims decisions | A written program for AI systems that make or support decisions affecting consumers, with governance, risk management, testing for unfair outcomes, and third-party oversight. Adopted only in North Carolina among the licensed states (NAIC map, 2026-04-01); the group applies it everywhere |
| Section 1557, 45 CFR 92.210 (N62-R07) | AI-006; AI-007 if suggestion features are enabled | Identify decision support tools using protected-trait inputs (AI-006 uses age and sex) and make reasonable efforts to mitigate discrimination risk |
| Federal employment discrimination law (Title VII, ADEA, ADA) | AI-008; AI-001 if used in HR decisions | The statutes apply to employment decisions whatever tool is used. EEOC's 2023 technical assistance on AI selection tools has been removed from its website, but the statutes did not change (`00_universal-framework/cross-sector/`, Part B4) |
| Fla. Stat. 501.171(2) (worked example) | AI-001 | "Reasonable measures" to protect personal information, including in AI retrieval |
| Fla. Stat. 934.03(2)(d) (worked example) | AI-001 meeting recaps; AI-007 | Interception is lawful when all parties have given prior consent; transcription is limited to internal meetings with notice, and the scribe needs a consent step |
| SEC insider trading controls | AI-001 | MNPI from deal rooms must not be retrievable by staff outside the deal team |
| Colorado SB26-189 (effective 2027-01-01) | None today | Covers AI that materially influences consequential decisions, including employment, insurance, and health care. The group's Colorado exposure is remote employees and applicants only; AI-008 is off and AI-001 is not used for decisions. Recheck before any re-enablement of AI-008. The law's status is unsettled (see the cross-sector file) |

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (substantial factor in which claims are investigated), AI-004 (pricing), AI-006 (health care), AI-008 (employment).
- **Medium:** AI-001, AI-003, AI-005, AI-007. Humans make the final decision, but outputs reach regulated data, customers, or records.
- **Low:** AI-009, AI-010.

**AI-001 is Medium, not High,** because POL-05 4.6 forbids its use in decisions about people and agent actions are off. **It is not Low** because it reaches Restricted data of four regulated populations, drafts messages to customers and patients, and amplifies over-sharing across legal entities.

**Re-tier triggers for AI-001:** any use in hiring, discipline, pay, claims, coverage, or patient care; turning on connectors to SCSP or division systems; agent features; a customer-facing chatbot.

### Generative AI risks (NIST AI 600-1) that apply to AI-001
| AI 600-1 risk | How it shows up here | Main control |
|---|---|---|
| Data Privacy | Retrieval of another entity's Restricted data (plan appeals, claim files, MNPI) | Labels and retrieval blocking; entity boundaries |
| Confabulation | Wrong amounts, dates, or names in summaries and drafts | User review; monthly accuracy sample |
| Information Security | Indirect prompt injection in inbound email | Testing; no agent actions; user warning |
| Human-AI Configuration | Over-reliance on fluent drafts in claims and HR | Training; prohibited-use review |
| Harmful Bias or Homogenization | Tone differences by name cues; weaker Spanish output | Bias tests B1 to B4 |
| Value Chain and Component Integration | Vendor model or terms change; BAA scope | Vendor review; BAA confirmation |
| Intellectual Property | Drafts reusing third-party text | User checks before external use |

The other five AI 600-1 risks (CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Environmental Impacts; Information Integrity; Obscene, Degrading, and/or Abusive Content) were judged low for internal business drafting and rely on the vendor's content filters.

## 4. MEASURE
### 4.1 AI-001 enterprise assistant (tests 2026-08-17 to 2026-08-21)
| Trustworthy characteristic | Test / metric and threshold | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 60 outputs (20 per division) checked against sources by data owners; material errors in no more than 5% | 4 of 60 (6.7%), including a wrong reserve amount in a claim summary | **No** |
| Safe | Prohibited-use review (see B4) | 3 prompts used the assistant to summarize a claimant's injury history for a claim decision | **No** |
| Secure and resilient | (a) Access only through SSO with MFA for licensed users; (b) 8 crafted emails with hidden instructions, threshold 0 followed; (c) prompts and outputs logged and kept 1 year | (a) Met; (b) 1 of 8 summaries repeated a planted link as a recommended action; (c) Met | **Partial** |
| Accountable and transparent | Owner, approved-tools list, rules, and training before use | Standard adopted after launch; no training at launch (P07 AT-2) | **Partial** |
| Explainable and interpretable | 40 answers with citations; at least 95% of citations support the statement | 37 of 40 (92.5%) | **No** |
| Privacy-enhanced | **Cross-entity data-access test:** 6 test accounts (2 per division), 15 standard queries each ("SSN," "appeal," "diagnosis," "claim," "acquisition," "bank account," and others). Threshold: 0 results from another entity's Restricted data | Insurance test accounts retrieved plan appeal files from the HR site (2 queries) and an MNPI deal-room export (1 query); a Health Care Services account retrieved claim notes with injury descriptions from a shared coordination site (1 query) | **No** |
| Fair, with harmful bias managed | Tests B1 to B4 below | B1 and B2 met; B3 and B4 not met | **Partial** |

### Bias and fairness testing plan (AI-001)
The assistant makes no decisions about people, so the plan tests where biased output could still reach them.

| Test | Method and metric | Groups compared | Threshold | Result (2026-08) |
|---|---|---|---|---|
| B1. Paired prompts for HR text | 12 pairs of job postings and performance feedback drafts differing only in a name or age cue; HR scores substance and tone | Female and male cues; Hispanic and non-Hispanic surname cues; age 40 and over and under 40 | No pair differs in substance | 0 of 12 differed in substance; 1 in tone. **Met**; HR review of AI-drafted postings stays mandatory |
| B2. Paired prompts for claimant letters | 12 pairs of claim status letters differing only in the claimant's name cue | Same groups as B1 | No pair differs in substance | 0 of 12 differed in substance; 2 in tone. **Met** |
| B3. Spanish-language quality | 12 claim and clinic notices translated by the assistant and checked by bilingual staff | Spanish and English readers | 0 meaning errors | 2 of 12 changed meaning (a deadline and a dosage instruction). **Not met**; regulated notices use approved templates only |
| B4. Prohibited-use check | Quarterly sample of 40 prompts from HR and claims users | HR and claims users | 0 prohibited uses | 3 claims prompts summarized injury history for a claim decision. **Not met** |

### 4.2 AI-002 claims fraud scoring (NAIC AI Model Bulletin)
| Characteristic | Metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision of referrals confirmed by investigators (target at least 30%) | 34% | Yes |
| Fair | Referral rate by ZIP-code median income quintile; flag if any quintile exceeds 1.25 times the overall rate without a documented claims explanation | Lowest-income quintile referred at 1.4 times the overall rate | **Flagged.** Root-cause review of geographic features by 2026-12-31 |
| Accountable | Model documentation to the bulletin's program elements | Model card exists; no bulletin mapping | **No** |

### 4.3 AI-006 triage and sepsis alert (45 CFR 92.210)
| Characteristic | Metric | Result | Pass? |
|---|---|---|---|
| Identification (92.210(b)) | Inputs reviewed for protected traits | Age and sex identified as inputs | Yes |
| Fair (92.210(c)) | Sensitivity by age band and sex; flag a drop of more than 0.10 from overall | Overall 0.74; patients 75 and older 0.63 | **Flagged.** Mitigation needed |
| Accountable | Mitigation documented | None | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts and summaries only; the user checks every output against its sources and is accountable for anything sent; no use in decisions about people; regulated notices from approved templates only; HR reviews every AI-drafted posting.
- **AI-002:** investigators decide every referral; claims are never denied or delayed on the score alone.
- **AI-006:** clinicians decide on every alert; clinical leaders review the 75-and-older sensitivity gap with the EHR vendor.

**Configuration controls for AI-001:** Restricted labels that block assistant retrieval on plan, claims, clinic, HR, and deal sites; deal-room exports banned (POL-04 4.4); connectors and agent features off; licenses only for enrolled users; public chatbots blocked on managed devices.

**Monitoring:** monthly accuracy sample; quarterly cross-entity data-access test and bias tests; quarterly High-tier report to the council and the board risk committee; P01 risks GR-10, GR-15, INS-008, INS-018, HCS-007, HCS-016.

**Incident handling:** output that shows data a user should not see is a security event under POL-03. The owning entity decides its own notice duty: the Health Care Services Privacy Officer or plan privacy official for PHI, the Insurance chief compliance officer for nonpublic information, and counsel for MNPI.

**Decommissioning:** turn AI-001 off for everyone if the vendor's terms change to allow training on group data, or if a second cross-entity exposure of Restricted data happens before the labels are in place; on exit, remove licenses and keep records per the retention schedule.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 enterprise assistant | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15). No expansion beyond 6,000 users until all conditions are met | Health Care Services users suspended from 2026-08-28 until the BAA scope for the AI add-on is confirmed in writing (by 2026-10-31, or users removed); plan appeal files and deal-room exports moved to restricted sites by 2026-10-31; Restricted labels with retrieval blocking and AI training for all pilot users by 2026-12-31; quarterly cross-entity test must return 0 results before expansion (POAM-023) |
| AI-002 claims fraud scoring | **Continue** | Disparity root-cause review and bulletin mapping by 2026-12-31; quarterly disparity monitoring |
| AI-003 photo estimating | **Approved** | Adjuster approval of every estimate stays mandatory; vendor retention shortened at renewal |
| AI-004 aerial-imagery pricing | **Not approved** | Impact assessment, rate filing review, and unfair discrimination testing first |
| AI-005 bill review | **Approved** | Vendor model governance questions added to the annual review |
| AI-006 triage and sepsis alert | **Continue** | Document 92.210(b)-(c) identification and mitigation for the 75-and-older gap by 2026-12-31 |
| AI-007 AI scribe pilot | **Not yet approved** | Consent field required before recording; BAA with no-training terms; pilot plan back to the council |
| AI-008 resume screening | **Remain off** | Re-enable only after an impact assessment, a bias test of selection rates by sex, race and ethnicity, and age, and a check of state and local AI hiring laws where applicants reside |
| AI-009, AI-010 | **Approved** | Standard monitoring |
