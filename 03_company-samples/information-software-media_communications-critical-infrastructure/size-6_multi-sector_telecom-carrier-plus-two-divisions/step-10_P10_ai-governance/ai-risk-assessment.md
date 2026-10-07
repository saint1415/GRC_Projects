# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Telecom Carrier, Network Engineering Services, Tower and Fiber Infrastructure, corporate) |
| Tier / Vertical | Multi-Sector / Communications |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for three priority use cases: the Carrier's customer-service chatbot with account access (AI-001, the focus use case), the Carrier's deposit decision model (AI-003), and Engineering's MNO alarm triage (AI-006) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 1 High, 6 Medium, 3 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Carrier CPNI compliance officer, Carrier customer operations vice president, Engineering MNO general manager, Tower site operations director. Approves High-tier use cases, any use case that touches CPNI or account actions, and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer and Carrier CPNI compliance officer | CPNI and personal information use, customer authentication rules in AI channels |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-04, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches CPNI or personal information, takes account actions, or supports decisions about customers, landowners, or network and structure safety is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves, a pre-deployment impact assessment and bias testing are required, and monitoring is reported quarterly.
3. **CPNI rules apply in every channel.** An AI channel that discloses CPNI must authenticate exactly as a human channel must (POL-02 4.10; 47 CFR 64.2010). Any change to authentication, recovery, or account actions is a material change.
4. **No agreement, no data** (POL-01 4.8; POL-04 4.10). AI vendors that handle Restricted data sign terms that prohibit training on group data, limit retention, and require incident notice within 24 hours.
5. **Regulator overlays.** Each division supplement adds its rules: CPNI and FCRA for the Carrier, customer contracts and SOC 2 commitments for Engineering, antenna structure duties for the Tower division.
6. **Approved tools only** for workforce generative AI (POL-05 4.7). Lawful-intercept information, FCI, and CPNI may never be entered into general assistants.

**Where the program fell short in 2026.** The standard was adopted in April, after the chatbot (2025-11) and the deposit model were live. The chatbot's account recovery feature launched on 2026-06-02 without council review, though it changed authentication (scenario gap 4). The Tower inspection imagery pilot started without registration. Both are under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Customer-service chatbot with account access | Carrier | Medium | In production; recovery feature disabled |
| AI-002 | AI voice agent in the IVR | Carrier | Medium | Pilot; expansion paused |
| AI-003 | Residential deposit decision model | Carrier | High | In production with conditions |
| AI-004 | Network anomaly detection and predictive maintenance | Carrier | Medium | In production |
| AI-005 | Generative design assistant | Engineering | Low | Pilot |
| AI-006 | MNO alarm correlation and ticket triage | Engineering | Medium | In production with conditions |
| AI-007 | Tower inspection imagery analysis | Tower | Medium | Pilot; registration completed 2026-08 |
| AI-008 | Lease abstraction | Tower | Low | Approved |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-010 | Coding assistant | Group | Low | Approved |

### 2.1 Customer-service chatbot with account access (AI-001): CPNI rules
| Rule | What it requires | What it means for the chatbot |
|---|---|---|
| 47 CFR 64.2010(c) | Authenticate without readily available biographical or account information before online access to CPNI; then access only by a compliant password | Account data only after portal or app sign-in. The recovery pilot (account number plus SSN4) did not meet this; about 23,000 sessions used it before it was disabled on 2026-08-07 |
| 47 CFR 64.2010(e) | Backup authentication may not prompt for biographical or account information; a customer who fails must set a new password under this paragraph | The new recovery design sends a one-time code to the telephone number or email of record and then requires a new password |
| 47 CFR 64.2010(f) | Immediate notice of changes to a password, backup authentication, online account, or address of record, by voicemail or text to the telephone number of record or mail to the address of record | Any account change the chatbot ever makes in these categories must trigger the BSS notice. None is enabled today |
| 47 CFR 64.2007(b); 64.2009(a) | Approval before using CPNI to market communications-related services; approval status checked before use | Plan suggestions check the BSS approval flag (in place since 2026-03) |
| 47 CFR 64.2011 | Law enforcement notice and hold before customer notice for a breach | The Carrier CPNI compliance officer reviewed the 23,000 recovery sessions with counsel: 61 sessions came from devices and locations never seen on the account, and 9 of those accounts later reported unrecognized changes. Counsel's determination is recorded in the incident register; this assessment does not restate it |
| FTC Act Section 5 | Truthful claims | Section 5 excludes common carriers subject to the Communications Act (15 U.S.C. 45(a)(2)); counsel reads the exclusion as limited to common carrier services, so chatbot statements about broadband must be accurate |
| State AI laws (Colorado, Texas, Utah) | Various | Not identified as applicable: no customers in those states (`../00_company-facts.md` section 7). The chatbot still discloses that it is AI at the start of every chat |

### 2.2 Deposit decision model (AI-003): FCRA
| Rule | What it requires | Implication |
|---|---|---|
| 15 U.S.C. 1681a(k)(1)(B)(iv) | "Adverse action" includes an action or determination made in connection with an application by a consumer that is adverse to the consumer's interests | Requiring a deposit from a new applicant, based in whole or in part on a consumer report, is treated by counsel as adverse action |
| 15 U.S.C. 1681m(a) | A person taking adverse action based in whole or in part on a consumer report must give notice of the action, the credit score used and related disclosures, the consumer reporting agency's contact details, a statement that the agency did not make the decision, and notice of the right to a free report and to dispute | Agents' orders send the notice. **Gap:** online and chat orders do not (about 31% of deposit decisions since 2025-11) |
| Colorado SB26-189 (effective 2027-01-01) | Duties for automated decisions in financial and lending decisions | Not applicable: no Colorado customers. Revisit before any expansion |
| State utility deposit rules | Vary by state commission | Generic; the Carrier's regulatory team tracks state rules on deposits for ILEC service |

### 2.3 MNO alarm triage (AI-006): customer commitments
| Commitment | Implication |
|---|---|
| 30-minute outage notice to carrier customers | If triage auto-closes or merges a 911-affecting alarm, the customer may miss its own 30-minute PSAP and 120-minute NORS clocks (47 CFR 4.9). The model must never auto-close an alarm tagged 911 or special facility |
| SOC 2 in preparation (P09) | The model is part of the service; its change management and monitoring fall under CC8.1 and CC7.2. If customers rely on it to decide reportability, Processing Integrity may come into scope |
| Customer data confidentiality | Tickets may contain carrier customers' subscriber data; the model runs inside the MNO tenant and sends no data to the vendor for training |

### 2.4 Other division use cases
| Use case | Key rule | Implication |
|---|---|---|
| AI-002 voice agent | 47 CFR 64.2010(b); state recording consent laws (Fla. Stat. 934.03(2)(d) worked example) | Never reads call detail aloud; the IVR consent announcement plays before recording |
| AI-004 anomaly detection | 47 CFR Part 4 | The NOC, not the model, decides whether an outage is reportable; automated changes stay disabled |
| AI-007 inspection imagery | 47 CFR 17.47-17.48 | The model does not replace lighting monitoring or FAA reporting; engineers review flagged and sampled unflagged images |
| AI-005, AI-008, AI-009, AI-010 | POL-04 4.6, 4.10; customer contracts | No FCI, lawful-intercept information, or CPNI in general assistants; human review of every output used |

## 3. Risk tiers (repository rubric)
- **High:** AI-003 (a substantial factor in a credit-type decision about consumers).
- **Medium:** AI-001, AI-002, AI-004, AI-006, AI-007, AI-009. Humans decide, but the use case touches CPNI, safety-relevant alarms, or structure safety.
- **Low:** AI-005, AI-008, AI-010.

**Re-tier triggers:**
- AI-001 or AI-002: any authentication, recovery, password, or address-of-record function; credits, deposits, or disconnections; any use of CPNI for marketing at scale. These make the use case High. **The 2026 recovery pilot met this trigger and was not escalated**, which is the governance failure behind P01 GR-05.
- AI-004 or AI-006: enabling automated configuration changes or automated closure of customer-reportable alarms.
- AI-007: using the model to reduce physical inspections required by Part 17 or tenant leases.

## 4. MEASURE
Results are from monitoring and tests between 2026-05 and 2026-08.

### 4.1 Customer-service chatbot (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly sample of 400 transcripts graded against the knowledge base and BSS data; incorrect billing or policy answers under 3% | 2.4% incorrect | Yes |
| Secure and resilient | Red-team set of 100 prompt injection and data extraction prompts: no access to another customer's data, no action outside the allow-list | 0 cross-account disclosures; 0 actions outside the allow-list (enforced at the API gateway) | Yes |
| Privacy-enhanced | CPNI shown only after compliant authentication (64.2010(c), (e)) | Failed during the recovery pilot; compliant since 2026-08-07 | **No** (for the period; fixed) |
| Accountable and transparent | AI disclosure at chat start; hand-off to a person on request; transcripts exportable within 1 business day | In place | Yes |
| Governance | Material changes reviewed by the council before release | Recovery feature released without review | **No** |
| Fair, with harmful bias managed | Incorrect-answer rate and task completion by chat language (English, Spanish) and by customer type; flag a group whose incorrect-answer rate exceeds the baseline by more than 3 points or whose completion is more than 10 points lower | Spanish incorrect answers 4.8% vs 2.1% English (within 3 points); task completion 39% vs 52% (13 points lower) | **Flagged** (completion) |

### 4.2 Deposit decision model (AI-003)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Rank-ordering of 12-month non-payment (AUC) on a holdout; stable within 0.03 of validation | 0.71 vs 0.72 at validation | Yes |
| Accountable and transparent | Adverse action notices with the 1681m(a) content for every deposit based on a consumer report (target 100%) | Agent orders 100%; online and chat orders 0% | **No** |
| Fair, with harmful bias managed | Deposit rate by age band and by state; flag a group more than 5 points above the overall rate without a credit-risk explanation | Ages 18-24: 22% vs 14% overall (thin credit files explain part); states within range | **Flagged.** Analysis due 2026-11-30 |
| Explainable and interpretable | Reason codes available to agents and in notices | Available to agents only | Partial |
| Human oversight | Agent waiver and customer review path used and logged | 1,900 waivers in 2026; review requests logged | Yes |

### 4.3 MNO alarm triage (AI-006)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Safe | Replay of 3 months of alarms: no alarm tagged 911 or special facility auto-closed or merged | 2 of 1,140 tagged alarms merged into a parent ticket in the replay | **No** (rule added 2026-09; retest due 2026-11-30) |
| Valid and reliable | Weekly sample of 100 auto-closed alarms reviewed by shift leads; wrongly closed under 1% | 0.6% | Yes |
| Accountable and transparent | Suppressed-alarm queue visible to operators | In place | Yes |

### 4.4 Other use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 voice agent | 200 test calls: call detail never read aloud; transfers on request | 0 disclosures; transfers worked | Yes |
| AI-002 voice agent | Speech recognition error rate for Spanish-speaking callers vs English; flag above 5 points | 11% vs 4% | **Flagged** |
| AI-007 inspection imagery | Missed defects in a sample of 500 unflagged images (target under 1%) | 1.8% | **No** |
| AI-004 anomaly detection | Share of model alerts confirmed by engineers (target over 60%) | 68% | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** account data only after sign-in; allow-listed actions enforced at the API gateway; customer confirmation for every change; credits, disputes, deposits, disconnections, and authentication changes go to agents.
- **AI-003:** agents may waive deposits; every deposit decision based on a consumer report sends the 1681m(a) notice in every channel; customers can ask for review.
- **AI-006:** alarms tagged 911 or special facility are never auto-closed or merged; operators see every suppressed alarm.
- **AI-007:** engineers review all flagged images and a 10% sample of unflagged images.

**Monitoring:** monthly metrics to division owners; quarterly High-tier and CPNI-touching use cases to the council and the board risk committee; P01 risks GR-05, TC-006, TC-020, NE-012, NE-014, TF-011.

**Incident handling:** any AI disclosure of CPNI to someone other than the customer is a suspected incident under POL-03 and follows the P08 matrix (64.2011). A vendor security incident must be reported to the group within 24 hours (POL-01 4.8). The chatbot can be switched to "outage messages only" mode in minutes.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (agents, manual triage, physical inspection, manual lease review).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 chatbot | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-17) | Recovery feature stays disabled until the one-time-code design passes red-team testing (POAM-012, 2026-12-31); release gate in the Carrier supplement for any authentication or account-action change; Spanish task-completion gap closed by 2027-01-31 (rewritten articles; bilingual hand-off) |
| AI-002 voice agent | **Continue pilot; no expansion** | Spanish recognition gap below 5 points before expansion; recording consent announcement verified in each state |
| AI-003 deposit model | **Continue with conditions** | Adverse action notices in online and chat orders by 2026-11-30; age-band analysis by 2026-11-30; reason codes in notices; quarterly fairness report to the council |
| AI-004 anomaly detection | **Continue** | Automated changes remain disabled |
| AI-005 design assistant | **Continue pilot** | No FCI; professional engineer review of every design |
| AI-006 MNO triage | **Continue with conditions** | Retest the 911 rule by 2026-11-30; include in the P09 system description and change management |
| AI-007 inspection imagery | **Continue pilot with conditions** | 10% sample of unflagged images reviewed; missed-defect rate under 1% before any reduction in manual review |
| AI-008, AI-009, AI-010 | **Approved** | Standard monitoring; AI-009 prohibited for CPNI, lawful-intercept information, FCI, and regulatory filings |
