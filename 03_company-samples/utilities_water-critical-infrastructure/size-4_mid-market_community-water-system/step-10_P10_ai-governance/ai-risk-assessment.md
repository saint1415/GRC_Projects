# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed investor-owned water utility) |
| Tier / Vertical | Mid-Market / Water and Wastewater Systems |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. AI-001, water quality anomaly detection, is the registry default use case and gets the deepest review |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-004 and AI-006 |
| Assessors / date | Water Quality and Compliance Manager (AI program lead), Director of Water Operations, vCISO and Security Manager, General Counsel, Director of Customer Service, Engineering and Capital Projects Director; 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
All six tools went into use or pilot without a security, safety, or privacy review (gap 13 in `../00_company-facts.md`). None is out of control, because two design facts hold: **no AI tool can write to SCADA**, and the hardwired chemical feed limits and alarms work without SCADA (P07 SC-24). Three tools need conditions before they grow:
- **AI-001 (anomaly detection)** has not met its validation thresholds and detects less well in one older part of the Regional System.
- **AI-002 (dose recommender)** is a pilot at one plant and must stay advisory, with no write path.
- **AI-004 (virtual agent)** gave callers wrong information during a precautionary boil water notice in July 2026, because its knowledge base was not updated.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Water quality anomaly detection (Regional) | High | Approve continued advisory use with conditions; no reliance for compliance or notice decisions |
| AI-002 | Chemical dose recommender (pilot, WTP-R2) | High | Continue the pilot with conditions; no expansion |
| AI-003 | AMI leak analytics | Medium | Approve with conditions |
| AI-004 | Contact center virtual agent and call summaries | Medium | Approve with conditions |
| AI-005 | Main-break likelihood model | Medium | Approve with conditions |
| AI-006 | Enterprise generative AI assistant | Medium | Approve with conditions; expansion paused |

Tiers: 2 High, 4 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Water Quality and Compliance Manager, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 statement 4.11: no path from the cloud or an AI tool may write to SCADA without a risk assessment and the COO's written approval.
  - POL-01 statement 4.15: AI tools must be approved before use.
  - POL-04 statement 4.7 and POL-05 statement 4.4: approved tools only; no Restricted or Confidential data in unapproved tools; no-training contract terms.
  - STD-10 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. It lists AI-001 to AI-006 with their conditions. Public generative AI chatbots are not approved and are being blocked on managed devices (P01 R-046).

### 2.1 Lightweight AI governance process
A mid-market utility does not need a standing AI committee with a large charter. It needs a short gate and a monthly rhythm that reuse existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature switched on in an existing system, submits a one-page intake: purpose, users, data, vendor, decisions affected, any connection to OT | Requesting business owner | 15 minutes |
| 2. Triage | Security Manager assigns a provisional tier with the P10 rubric and checks the purchasing gate (POL-01 statement 4.10) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (contract terms, retention), and a business reviewer. **High:** a full MAP and MEASURE review like this one, including a validation and fairness plan, and the Director of Water Operations' sign-off for anything touching treatment | Security Manager; General Counsel; business or operations reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Water Quality and Compliance Manager, vCISO, Director of Water Operations, General Counsel) in a 30-minute monthly meeting. High: the AI review group recommends, and the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report agreed metrics monthly; High-tier items get a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data, new plant or system, any proposed write path to OT, or a safety event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. AI that "can affect physical safety or critical infrastructure operations" is High, which is why AI-001 and AI-002 are High even though neither controls equipment.

## 3. MAP
| Item | AI-001 Anomaly detection | AI-002 Dose recommender | AI-003 Leak analytics | AI-004 Virtual agent | AI-005 Main-break model | AI-006 Gen AI assistant |
|---|---|---|---|---|---|---|
| Purpose | Earlier warning of water quality changes than fixed alarm limits | Suggest caustic and hypochlorite doses at WTP-R2 | Tell customers about likely leaks | Answer calls and chats; summarize calls | Rank mains for replacement | Draft and summarize documents |
| Users | ROC operators; Water Quality and Compliance Manager | WTP-R2 Chief Operators | Customers; customer service | Callers; contact center agents | Engineers | 120 staff |
| Affected people | 171,400 Regional customers (indirectly) | Regional customers (indirectly) | 81,000 AMI customers | Callers for 123,400 accounts | Neighborhoods (indirectly) | Customers whose correspondence is processed |
| Data | Process data; no personal information | Process data | Interval usage; contacts | Voice, transcripts, account data | Asset and break data | Any file the user can open |
| Build or buy | Buy (vendor model in company cloud) | Buy (pilot) | Configure (AMI SaaS) | Buy (CIS feature) | Configure (GIS feature) | Buy (enterprise SaaS) |
| Generative AI? | No | No | No | Yes | No | Yes |
| Connection to OT | Read-only replica; no write path | Read-only replica; no write path | None | None | None | None |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| SDWA section 1433 | AI-001, AI-002, AI-005 | The RRA must assess monitoring practices, chemical handling, and automated systems, and may evaluate capital needs (42 U.S.C. 300i-2(a)(1)(A)(ii), (iii), (v); (a)(1)(B)); the ERP must include detection strategies (300i-2(b)(4)). Each RRA addendum must describe these tools and their limits accurately (P03 G-005) |
| 40 CFR Part 141 monitoring and public notice | AI-001, AI-002, AI-004 | Unchanged by AI. Required monitoring and Tier 1 decisions (141.202) stay with people, based on confirmed data. AI-004 must not contradict an active notice |
| Fla. Stat. 934.03(2)(d) | AI-004 | Interception of a call is lawful when all parties have given prior consent. Calls are recorded and transcribed only after a recording announcement; callers who object are routed to a person without recording |
| Fla. Stat. 501.171 | AI-003, AI-004, AI-006 | Customer personal information processed by vendors must be protected (501.171(2)); vendors are third-party agents with a 10-day notice duty (501.171(6)(a)) |
| FTC Act Section 5 | AI-001 to AI-004 | Vendor accuracy claims; customer-facing claims about leak detection and the virtual agent |
| Utility Services agreements | AI-004 | The agent answers calls for client customers under each client's name; clients must be told AI is in use |

**Laws considered and not applicable:**
- **State AI laws such as Colorado SB26-189** (effective 2027-01-01): the company operates only in Florida, and none of these tools makes a consequential decision about a person in the categories those laws cover. Florida-specific AI law was not researched beyond the recording statute.
- **Federal AI rules for critical infrastructure:** none binds a water utility's use of AI as of 2026-10-05. CISA and EPA guidance is voluntary and was used as background only.

## 4. Risk tier and escalation triggers
| Use case | Tier | Why | Re-tier or re-assess before |
|---|---|---|---|
| AI-001 | High | Operators act on its alerts in a critical infrastructure process | Any write path; any use to reduce grab sampling or support a compliance determination; suppressing or reprioritizing SCADA alarms; extending to Lakes or Ridge; a vendor model change |
| AI-002 | High | Recommendations directly concern chemical doses | Any write path or closed-loop control; any second plant; any new chemical |
| AI-003 | Medium | Customer-facing alerts; no decisions about service or charges | Linking alerts to automatic shutoff, fees, or adjustments (would be High) |
| AI-004 | Medium | Interacts directly with customers; staff decide anything that changes an account | Deciding payment arrangements, disconnections, or adjustments (would be High) |
| AI-005 | Medium | Influences capital decisions that affect neighborhoods; engineers decide | Using the model as the sole basis of the capital plan |
| AI-006 | Medium | Internal productivity, but with access to Restricted and customer data | Connecting it to OT data or giving it actions (sending email, changing files) |

## 5. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08 review) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Back-test on 12 months with 15 labeled events (storm pressure losses, analyzer failures, residual dips, a nitrification episode) plus 30 injected synthetic events; detection within 30 minutes | At least 90% | Labeled 13 of 15 (87%); synthetic 27 of 30 (90%); median 19 minutes | **No** (labeled) |
| AI-001 | Valid and reliable (false alerts) | False alerts per week across all stations | 5 or fewer | 8 a week on average | **No** |
| AI-001 | Fair, harmful bias managed | Detection rate by station group (see plan below) | Gap of 10 points or less | Zone 4 (pre-1975 cast-iron mains): 70%; other zones: 92% | **No** |
| AI-001 | Safe | No write path; SCADA alarms and sampling stay primary | Confirmed | Confirmed in P04 design and firewall rules | Yes |
| AI-001 | Secure and resilient | Pinned version; change notice; replica reconciliation; read-only identity | All in place | Pinned and read-only since 2026-08; reconciliation since 2026-09-01; change notice clause pending | **Partial** |
| AI-002 | Valid and reliable | 60 days of recommendations compared with Chief Operator doses | 95% within plus or minus 5% of the operator dose; 0 outside the safe range | 94% within 5%; 3 recommendations outside the safe range (all would have been capped by stroke limits; none applied) | **No** |
| AI-002 | Safe | Recommendation display, operator entry only, hardwired limits | All true | All true | Yes |
| AI-002 | Accountable and transparent | Each applied recommendation logged with the operator's initials | 100% | 71% logged (paper log) | **No** |
| AI-003 | Valid and reliable | 200 alerts checked against field visits or customer confirmation | At least 80% confirmed | 82% confirmed | Yes |
| AI-003 | Accountable and transparent | Customer wording does not promise detection | Reviewed | Alert text says "we detected a leak" | **No** |
| AI-004 | Valid and reliable | 40 scripted calls covering outages, notices, and billing | No wrong safety information; at least 90% correct | 2 wrong answers on notice status; 92% correct overall | **No** |
| AI-004 | Safe | Agent reflects active boil water and Tier 1 notices | Updated within 1 hour of a notice | July 2026: 11 callers told no notice was active for about 6 hours | **No** |
| AI-004 | Fair, harmful bias managed | Successful completion rate, English versus Spanish callers | Gap of 10 points or less | English 64%, Spanish 41% (Spanish callers are transferred to agents, so no harm found, but longer waits) | **No** |
| AI-004 | Privacy-enhanced | Recording announcement before capture; caller verification before account details | Both | Announcement in place; verification uses account number and service address only | **Partial** |
| AI-005 | Fair, harmful bias managed | Predicted versus actual breaks by system (Regional, Lakes, Ridge) for 2023-2025 | Ratio between 0.8 and 1.25 for each | Regional 1.04; Lakes 0.62; Ridge 0.71 (acquired systems under-predicted because of sparse history) | **No** |
| AI-006 | Privacy-enhanced | Assistant does not surface Restricted content to users without a need to know | 0 findings in a 30-prompt test | 1 finding: an ERP draft surfaced from a folder open to all staff (folder fixed 2026-08-28) | **No** (fixed; retest due) |
| AI-006 | Secure and resilient | Enterprise terms prohibit training on company data; audit logging on | Both | Both confirmed in the contract and admin settings | Yes |
| All | Explainable and interpretable | Users can see why: contributing signals (AI-001), input trends (AI-002), usage pattern (AI-003), source documents (AI-004, AI-006), segment factors (AI-005) | Available | Available for all six | Yes |

**AI-001 bias and fairness testing plan.** For this model, fairness means every neighborhood gets the same early warning. The groups compared are monitoring station groups, not individuals:
- **Groups:** (a) the 3 stations in zone 4, served by pre-1975 cast-iron mains, versus the other 11; (b) stations fed mainly by WTP-R2 (reverse osmosis blend) versus WTP-R1 (lime softening).
- **Metrics:** detection rate on labeled and injected events; false alerts per station per week; median time to detect.
- **Thresholds:** detection rate gap of 10 points or less; false-alert rate within 2 times the best group.
- **Frequency:** before production reliance, then quarterly, and after any model change.
- **Finding:** zone 4 analyzers are noisier because of older mains and frequent flushing, so the model learned a wider "normal" band and missed more events (70% versus 92%). Older infrastructure can coincide with lower-income areas, so an unmanaged gap would give some customers less protection. Until the vendor re-baselines zone 4 or the company sets station-specific thresholds, zone 4 keeps its fixed SCADA alarm limits and sampling schedule with no reliance on the model.

**AI-005 fairness note.** Under-prediction in Lakes and Ridge would push replacement spending toward the Regional System. Engineers will weight Lakes and Ridge segments by pipe age and material until 3 years of company break history exist there.

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** alerts only; an operator confirms with a grab sample or second instrument before any change; public notice decisions stay with the Water Quality and Compliance Manager and the COO; operators may silence model email alerts during an incident, never SCADA alarms.
- **AI-002:** the Chief Operator decides every dose and enters it at the HMI; recommendations are logged with the decision; stroke limits stay in force.
- **AI-003:** alerts are informational; staff decide any adjustment under the tariff.
- **AI-004:** no account changes; a person is always one step away; summaries are reviewed before saving.
- **AI-005:** engineers review every list; the COO approves the capital plan.
- **AI-006:** users review all output; no autonomous actions.

**Monitoring:** owners report section 5 metrics monthly to the AI review group; AI-001 and AI-002 get a quarterly deep dive. Results feed the risk register (P01 R-043 to R-048).

**Incident handling:** a compromise of the cloud workloads account or a model follows P08; the model is switched off first, and plant operations are not affected. A wrong AI-004 answer during a public notice is handled as a public notice issue by the Water Quality and Compliance Manager. Vendor breaches follow the third-party agent rows in the notification matrix.

**Decommissioning criteria:**
- AI-001: stop if thresholds are not met by 2027-03-31, or if the vendor will not accept change-notice terms.
- AI-002: end the pilot if any applied recommendation leads to an out-of-range result, or if thresholds are not met by 2027-03-31.
- AI-004: switch to scripted mode only during any public notice until the notice feed works; stop if wrong safety information recurs.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve continued advisory use** | Change-notice clause (2026-11-30); zone 4 excluded from reliance until re-baselined; alerts labeled "advisory, model output" and logged outside email (done 2026-09-10); thresholds met by 2027-03-31 before any reliance; RRA addenda describe its limits | COO, 2026-09-15; noted by the CEO |
| AI-002 | **Continue pilot at WTP-R2 only** | Electronic log of every recommendation and decision (2026-10-31); out-of-range guard in the model output (2026-11-30); no write path ever without COO approval under POL-01 statement 4.11 | COO, 2026-09-15; noted by the CEO |
| AI-003 | **Approve with conditions** | Revise alert wording (2026-12-31); quarterly accuracy sample; 72-hour breach notice term at the AMI renewal | Director of Customer Service and AI review group, 2026-09-15 |
| AI-004 | **Approve with conditions** | Live notice feed from the public notice SOP to the agent (2026-11-30); scripted mode during notices; stronger caller verification (2027-01-31); Spanish performance improvement plan from the vendor; clients informed in writing | COO, 2026-09-15 |
| AI-005 | **Approve with conditions** | Engineering weighting for Lakes and Ridge; fairness check before the 2027 capital plan (2027-03-31) | Engineering and Capital Projects Director and AI review group, 2026-09-15 |
| AI-006 | **Approve with conditions; expansion paused** | Sensitivity labels on Restricted libraries and exclusion of the RRA library from indexing (2026-12-31); retest of the 30-prompt check; user guidance | COO, 2026-09-15 |

The conditions are tracked as POAM-022 in P07 and in the risk register (P01 R-043 to R-048). The AI review group holds its first monthly meeting on 2026-10-06.
