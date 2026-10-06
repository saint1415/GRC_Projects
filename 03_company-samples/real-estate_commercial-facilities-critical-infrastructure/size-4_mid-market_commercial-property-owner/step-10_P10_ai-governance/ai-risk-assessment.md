# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Tier / Vertical | Mid-Market / Commercial Facilities |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry use case, **video analytics for building access**, is AI-001 and AI-002 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-005; NIST SP 800-82 Rev. 3 for AI-004, which writes to building systems |
| Assessors / date | vCISO (chair), Security Manager, OT security analyst, General Counsel, Director of Security Operations, VP of Engineering, 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
All five AI uses arrived without review (gap 9): two were switched on by the access control and video platform vendor, one came with the parking operator's system, one was bought by engineering for energy savings, and one by Legal for lease work. None is out of control, but two are High tier and need firm limits:
- **AI-002, face verification,** decides who may enter a workplace and creates face templates for about 240 people with no assessment, notice design, retention limit, or accuracy evidence. **Decision: suspend and delete.**
- **AI-004, energy optimization,** writes setpoints into the BAS at two towers from a vendor's cloud. Its limits are enforced by the vendor, not by the company, and testing found writes outside the engineering-approved range. **Decision: approve with company-enforced write limits.**

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Tailgating detection (Towers 1-4) | Medium | Approve with conditions; turn off if thresholds are not met by 2026-11-30 |
| AI-002 | Face verification pilot (Tower 2) | High | **Suspend** (2026-09-30); templates deleted by 2026-10-31 |
| AI-003 | License plate recognition data from the parking operator | Medium | Approve sharing with conditions |
| AI-004 | BAS energy optimization (Towers 1-2) | High | Approve with conditions; expansion paused |
| AI-005 | Generative AI lease abstraction | Medium | Approve with conditions |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** vCISO, who chairs the AI review group. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.10: no AI use case or new analytics, biometric, or automation feature is enabled before approval; features that decide entry, use biometric data, or write to building systems need COO approval after a full assessment.
  - POL-04 4.7 and 4.8: no biometric data without COO approval, notice, opt-in, and a deletion schedule; no Restricted or Confidential data in unapproved tools; no-training clause.
  - POL-05 4.8: approved tools only; human review of outputs that affect people or building systems.
  - STD-06 AI use standard: due 2026-12-31.
- **How the gap happened.** Vendors turned on features inside platforms the company already used (AI-001, AI-002), and departments bought tools with their own budgets (AI-004, AI-005). Purchasing reviewed new vendors but not new features, and nobody kept an AI inventory (P03 G-026, CPG 3.P).
- **Approved-tools list:** kept by the GRC Analyst on the intranet. After this decision it lists AI-001, AI-003 (data sharing), AI-004, and AI-005, each with its conditions. AI-002 is listed as **not approved**.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm that reuses existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing platform, submits a one-page intake: purpose, users, people affected, data, vendor, and whether it decides anything or writes to building systems | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the repository rubric and checks the purchasing and feature gate (POL-01 4.10) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy and legal (notice, retention, no-training clause), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan, and for anything that writes to building systems an OT safety review by the VP of Engineering | Security Manager; General Counsel; business reviewer; VP of Engineering | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, General Counsel, Director of Security Operations, VP of Engineering), 30 minutes monthly. High: the group recommends and the COO decides, informing the CEO | As listed | Monthly |
| 5. Monitor | The owner reports the agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, expansion to a new property or population, or a safety event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 4.

## 3. MAP
| Item | AI-001 Tailgating | AI-002 Face verification | AI-003 LPR data | AI-004 Energy optimization | AI-005 Lease abstraction |
|---|---|---|---|---|---|
| Purpose | Alert the SCC when more than one person passes a turnstile lane on one badge read | Deny entry when a live face does not match the badge photo ("two-factor" entry) | Enforce garage permits; support investigations | Lower energy cost by adjusting setpoints | Draft lease abstracts faster |
| Users | 40 SCC and lobby operators | Lobby officers at Tower 2 | Parking operator; 4 company investigators | Chief engineers at Towers 1-2; energy manager | 6 lease administrators |
| Affected people | About 9,800 tenant employees at Towers 1-4, about 1,000 visitors a day, staff | About 240 enrolled tenant employees of one anchor tenant | About 3,100 monthly permit holders and all garage visitors | Occupants of Towers 1-2 (comfort); equipment | Tenants (contract terms) |
| Data | Video and badge events; alert clips | Face templates from badge photos and live captures | Plate reads, images, times; names for permit holders | BAS trends; setpoint writes | Leases (Confidential) |
| Build or buy | Buy (platform feature) | Buy (vendor pilot) | Third-party system | Buy (SaaS with a write connector) | Buy (SaaS) |
| Generative AI? | No | No | No | No (optimization model) | Yes |
| Decides or acts? | Advises an operator | **Decides entry** (officer can override) | Advises investigators | **Writes to building systems** | Drafts for human review |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02) | All five | Covers unfair or deceptive practices, including undisclosed collection, unsupported accuracy or savings claims, and unreasonable data security. The FTC's *Policy Statement on Biometric Information and Section 5 of the FTC Act* (2023-05-18) lists practices it may treat as unfair, including failing to assess foreseeable harms before collecting biometric information, surreptitious or unexpected collection, failing to evaluate vendors, failing to train staff, and failing to monitor the technology. It defines biometric information broadly enough to include video of identifiable people. The statement was still posted on ftc.gov in September 2026; whether current FTC leadership still applies it was not confirmed |
| Fla. Stat. 501.171 | AI-002, AI-003 (and AI-001 clips) | Personal information includes "biometric data as defined in s. 501.702" and "any information regarding an individual's geolocation" (501.171(1)(g)1.a.(VI) and (VII)). Section 501.702 defines biometric data as automatic measurements of biological characteristics used to identify a person, and excludes photographs and video recordings and data generated from them. Tailgating video is therefore not biometric data. Whether **face templates computed from camera video** fall within that exclusion is unsettled (counsel to confirm); the company treats them as biometric data. Whether plate reads linked to names are geolocation information is also for counsel; the company treats them as personal information |
| Florida Digital Bill of Rights (Fla. Stat. 501.701 et seq.) | None | Applies only to controllers with more than $1 billion in global gross annual revenue (501.702); the company has about $100 million |
| Fla. Stat. 934.03 | AI-001, AI-002 | Cameras record no audio. Enabling audio would raise interception issues, so audio stays disabled (POL-05 4.10) |
| State AI and automated decision laws of other states (for example Colorado SB26-189, effective 2027-01-01) | None | The company operates only in Florida. They are noted because AI-002 affects access to a workplace. No Florida statute specific to private-sector AI or biometric collection was identified in this review (not exhaustively researched) |
| CISA CPG 2.0 (voluntary) | All five; AI-004 especially | Goals 1.D and 1.E (vendor risk), 3.I (segmentation of what can reach OT), and 3.P (approval process for new hardware and software, which here includes vendor features) |
| NIST SP 800-82 Rev. 3 (guidance) | AI-004 | Changes to OT setpoints are OT changes; they need change control, bounds, and monitoring |

## 4. Risk tiers
**AI-001: Medium.** It makes no decision about a person and controls no door or turnstile; an operator reviews every alert. It is not Low because it processes video of identifiable people, and a noisy or biased alert stream can lead officers to stop some people more than others (P01 R-013). **Re-tier to High** if alerts trigger any automatic turnstile or door action, are linked to identities in reports to tenants, add face matching, or extend to Mixed-Use 1-2.

**AI-002: High.** The system itself decides whether a person may enter their workplace in a critical infrastructure facility, and it creates face templates treated as biometric data. Face recognition accuracy can differ across demographic groups (NIST IR 8280, *Face Recognition Vendor Test Part 3: Demographic Effects*, 2019), so errors could fall unevenly on tenant employees.

**AI-003: Medium.** The company does not run the model, but it uses the output in investigations that affect individuals, and plate reads linked to names reveal people's movements. **Re-tier to High** if exports are used for real-time alerts on named people.

**AI-004: High.** It writes to building systems, which can affect occupant comfort and equipment and is "critical infrastructure operations" under the rubric. Field controller safety limits and chief engineer overrides reduce the risk but do not remove it, and a compromise of the vendor would give an attacker the same write path (P01 R-011).

**AI-005: Medium.** It makes no decision about people, but its outputs feed business decisions (renewal options, notice dates) and it processes Confidential leases. Generative AI can produce confident, wrong text (NIST AI 600-1 "confabulation").

## 5. MEASURE
Results cover 2026-05-25 to 2026-08-14 unless stated. Staged tests ran on 2026-08-12 at Towers 1 and 3 with 15 volunteer staff.

### 5.1 AI-001 tailgating detection
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision of at least 70% (monthly review of random alerts); recall of at least 90% on staged tailgating passes | About 4,900 alerts (about 58 a day across 4 towers). 64 of 200 sampled alerts were real tailgating (32% precision). 52 of 60 staged passes detected (86.7% recall) | **No** |
| Safe | Alerts cannot lock turnstiles or doors; egress unaffected | Confirmed in platform settings and in a walk test with the fire alarm vendor (turnstiles release on the hardwired relay) | Yes |
| Secure and resilient | Feature settings changeable only by named administrators; vendor security evidence covers the feature | 23 administrators can change settings (POAM-002); feature outside the vendor's SOC 2 report period (P09 VEN-02) | Partial |
| Accountable and transparent | Tenants and visitors told that analytics run on lobby video | Lobby signs say only "video surveillance in use"; no tenant notice (P03 G-057) | **No** |
| Explainable and interpretable | Operator sees why an alert fired before acting | Clip, lane, and badge count shown with every alert | Yes |
| Privacy-enhanced | Company video excluded from vendor model training; clips kept no longer than video | Vendor terms allow training unless the customer opts out (not exercised); clips kept 1 year | **No** |
| Fair, with harmful bias managed | False-alert rate for passes by people using wheelchairs or mobility aids, with strollers or carts, or in escorted groups, compared with all other passes; flag if more than twice the baseline | Such passes are about 3% of lane traffic but 19% of sampled false alerts; false-alert rate about 6 times the baseline, mostly on the wide accessible lanes | **No.** Disparity flagged |

**Bias finding.** The model treats a wheelchair user with a companion, or a person with a cart, as two people on one badge, so officers stop people on the accessible lanes far more often. That harms people with disabilities even though nobody intended it (counsel to consider federal disability law). Until the vendor fixes it, accessible-lane alerts go to the SCC as "review only" events, and officers must never stop a person on an accessible lane on an alert alone.

**Not tested.** Performance across skin tones and clothing under each lobby's lighting; the volunteer group was too small to compare groups fairly. The vendor must supply its own group-level test data before the 2026-11-30 review.

### 5.2 AI-002 face verification pilot
| Characteristic | Finding |
|---|---|
| Valid and reliable | 534 rejections in about 18,400 attempts (2.9%); officers overrode all but 6 after checking the badge photo. The vendor supplied no accuracy data |
| Fair, with harmful bias managed | No demographic performance evidence from the vendor or an independent evaluation; the company does not and should not collect demographic data to test it itself |
| Privacy-enhanced | Templates kept by the vendor indefinitely; no deletion on unenrollment; the tenant's internal memo was the only notice; no non-biometric alternative at the 2 pilot lanes (enrolled employees could use other lanes, but were not told so) |
| Accountable and transparent | No company notice, no company assessment, no contract terms for biometric data |
| Secure and resilient | Feature and template store outside the vendor's SOC 2 report |

### 5.3 AI-003, AI-004, AI-005
| Use case | Test / metric | Result | Pass? |
|---|---|---|---|
| AI-003 | Request log for every export; retention of shared exports; data use terms | 11 exports in 2026 with no log; exports kept in investigators' mailboxes; no terms with the operator | **No** |
| AI-004 | All setpoint writes within engineering-approved ranges; savings claim verified | 3 writes in July 2026 were up to 2 degrees F above the approved chilled water supply limit during peak hours (no equipment harm); verified savings 6.2% of tower energy cost against the vendor's claim of 10% | **No** (bounds); savings partly confirmed |
| AI-004 | Kill switch works | Chief engineers disabled writes from the BAS workstation in under 1 minute in a test on 2026-08-12 | Yes |
| AI-005 | Accuracy of critical dates, options, and notice terms in a sample of 30 abstracts against the leases | 4 of 30 abstracts (13%) had a wrong critical date; 1 described a renewal option that does not exist in the lease | **No** |
| AI-005 | Vendor data use terms (NIST AI 600-1 data privacy and information security risks) | Business subscription; training opt-out available but not set | **No** |

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the alert is advice to an operator, not a decision. The operator watches the clip and checks the badge record; the only permitted action is a courteous badge check. Nobody is refused entry, reported to a tenant, or disciplined on an alert alone. One-click false-positive dismissals feed the monthly quality review.
- **AI-003:** investigators request exports through a logged form stating the incident number; no bulk exports; no real-time alerts on named people.
- **AI-004:** the chief engineer on duty can disable writes at any time, and the SCC sees a BAS alarm when a write is rejected. A human approves any change to the allowed ranges.
- **AI-005:** a lease administrator verifies every critical date, option, and notice term against the lease before entry in the property management system, and initials the abstract.

**Company-enforced limits for AI-004 (condition).** The connector in the workloads account (P04) must allow writes only to an allowlist of points at Towers 1-2, within ranges set by the VP of Engineering, at most one change per point per 15 minutes; it must reject and alert on anything else. Field controller safety limits stay in place as the last line.

**Monitoring:**
- AI-001: monthly precision on 100 random alerts, quarterly staged recall test, monthly accessible-lane false-alert ratio.
- AI-003: quarterly review of the export log by the General Counsel.
- AI-004: daily report of rejected writes; monthly savings verification by the energy manager.
- AI-005: monthly sample of 10 abstracts checked by a second administrator.

**Incident handling:** a security incident at an AI vendor follows P08 and the vendor's notice terms. A harmful pattern (wrongful stops, an unsafe write, a missed lease date) is handled as a P08 event when it involves security, and is otherwise reported to the AI review group within 5 business days.

**Decommissioning criteria:**
- AI-001: turn off if precision is below 50% after 90 days of tuning (by 2026-11-30), if the training opt-out is not confirmed in writing by 2026-10-31, or if the accessible-lane ratio is not below 2 by 2027-02-28.
- AI-004: disable writes if any write is accepted outside the allowlist after the connector limits go live, or if the vendor will not sign the interconnection addendum by 2026-12-31.
- AI-005: stop use if the error rate on critical dates is above 5% in two consecutive monthly samples after verification starts.

## 7. Decisions
**AI-001: Approve with conditions.** COO, 2026-09-15. Conditions due 2026-10-31 unless stated:
1. The vendor confirms in writing that company video is excluded from model training.
2. Alert clip retention set to 30 days (POL-04 4.4).
3. Plain-language tenant notice and lobby signs saying that video analytics detect tailgating and that no face recognition is used for tailgating detection.
4. Accessible-lane alerts routed as "review only"; officers briefed on the no-action-on-alert-alone rule.
5. Acceptance thresholds (70% precision, 90% recall) met by 2026-11-30, or the feature is turned off.

**AI-002: Suspend and delete.** COO, 2026-09-15, noted by the CEO (P01 R-012, treatment Avoid). The pilot ends on 2026-09-30, the 2 lanes return to badge-only entry, and the vendor must delete all templates and certify deletion by 2026-10-31. The anchor tenant was told on 2026-09-16. Reasons:
- It is High tier, and the company has no security need that badges plus tailgating detection do not meet.
- It created biometric data for about 240 people with no company notice, retention limit, or deletion design.
- The vendor supplied no accuracy or demographic performance evidence, and the feature is outside its SOC 2 report.

A new proposal would need, at minimum: independent demographic accuracy evidence; badge-only entry for anyone who does not opt in, at every lane; a template storage, encryption, and deletion design; written notice; vendor terms limiting use of the templates; tenant agreement; and a new P10 assessment approved by the COO and noted by the CEO.

**AI-003: Approve data sharing with conditions.** COO, 2026-09-15. A data use and retention addendum with the parking operator (exports only on a logged request, kept 30 days by the company, no onward sharing) by 2027-01-31 (P01 R-014).

**AI-004: Approve with conditions.** COO, 2026-09-15, noted by the CEO. Company-enforced write limits on the connector by 2026-11-30; an interconnection and security addendum with the vendor, including 24-hour incident notice and a ban on remote changes to the allowlist, by 2026-12-31; the vendor added to the Tier 1 review list (P09). Expansion to Towers 3-4 is paused until both are done.

**AI-005: Approve with conditions.** General Counsel, as business owner, with the AI review group, 2026-09-15. Second-person verification of all critical terms (in place 2026-09-15); training opt-out set and confirmed in writing, and the enterprise terms reviewed, by 2026-10-31; no tenant employee personal information in prompts. Abstracts made before 2026-09-15 (about 180) are re-verified by 2026-11-30.

These decisions are tracked as POAM-020 in P07.
