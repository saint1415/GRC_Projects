# AI Risk Assessment: Video Analytics for Building Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Small / Commercial Facilities |
| AI use cases | **AI-001:** tailgating detection at the Property A lobby turnstiles (vendor-enabled pilot since May 2026). **AI-002:** face verification against badge photos at the turnstiles (vendor proposal, not in use) |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI 600-1 (Generative AI Profile) is not used: neither feature is generative |
| Assessor / date | Security Manager with the IT Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Security Manager (owner of access control and video). **Decision authority:** COO for Medium-tier use cases; the majority owner for High-tier use cases.
- **Policies that apply:**
  - POL-01 4.10: vendor-enabled analytics or biometric features need approval, and biometric features need COO approval after this assessment
  - POL-04 4.1 and 4.8: face templates would be Restricted data; video is Confidential; no new analytics use without approval
  - POL-05 4.8: approved AI tools and features only
- **How the gap happened.** The platform vendor turned tailgating detection on as a free pilot in May 2026 without asking. There was no AI approved-tools list and no approval step for new platform features (scenario-facts gap 15; P01 R-024, R-025). This assessment and POL-01 4.10 close that gap.
- **Approved AI list:** kept by the IT Manager. After this decision it lists only AI-001, at Property A, with the conditions in section 6.
- **Scale for a Small company:** there is no AI committee. The COO, IT Manager, and Security Manager review AI use cases each quarter, together with the alert-quality report.

## 2. MAP
### 2.1 AI-001 tailgating detection (pilot)
| Item | Description |
|---|---|
| Purpose and intended use | Detect when more than one person passes a lobby turnstile lane on a single badge read, and alert the security console with a short clip so an officer can check the person's badge |
| Users / operators | 9 security operations staff at the Property A console |
| Affected people | About 1,300 tenant employees with Property A badges, about 150 visitors a day, company staff, and anyone else in the lobby |
| Data | Inputs: video from the 6 existing cameras over the turnstile lanes, and turnstile badge events. Outputs: an alert with a 10-second clip, lane, and time. No identity is inferred; the model counts people. **The vendor's terms allow it to use customer video to improve its models unless the customer opts out. The company has not opted out.** Alert clips are kept for 1 year by default, longer than the 30-day video retention in POL-04 4.6 |
| Build or buy | Buy: a feature of the access control and video platform (vendor computer-vision model). Not covered by the vendor's SOC 2 report, which ended before the feature was released (P09) |
| Not intended | Identifying people, locking turnstiles or doors automatically, refusing entry, or disciplining anyone. Enabling any of these requires re-assessment |

### 2.2 AI-002 face verification (proposal)
| Item | Description |
|---|---|
| Purpose proposed by the vendor | At the turnstile, compare a live face image with the badge holder's enrolled photo, and deny entry on a mismatch ("two-factor" entry) |
| Affected people | About 1,750 tenant employees across the portfolio and 60 employees; visitors if extended to visitor passes |
| Data | A face template (a numeric representation of facial geometry) created from each badge photo and from each live capture. Stored by the vendor |
| Effect | The system, not a person, would decide whether someone can enter their workplace |

### 2.3 Applicable laws and rules
| Rule | AI-001 | AI-002 | Why |
|---|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02) | **Yes** | **Yes** | Covers unfair or deceptive practices, including undisclosed collection and unsupported accuracy claims. The FTC's *Policy Statement on Biometric Information and Section 5 of the FTC Act* (May 18, 2023) lists practices it may treat as unfair, including failing to assess foreseeable harms before collection, surreptitious or unexpected collection, failing to evaluate vendors, failing to train staff, and failing to monitor whether the technology works as expected. It defines biometric information broadly enough to include video of identifiable people. The statement is still posted on ftc.gov (checked 2026-09-26); whether current FTC leadership still applies it was not confirmed |
| Fla. Stat. 501.171 | Limited | **Yes** | Personal information includes "biometric data as defined in s. 501.702" (501.171(1)(g)1.a.(VI)). Section 501.702 defines biometric data as automatic measurements of biological characteristics used to identify a person, and **excludes photographs and video recordings and data generated from them**. So tailgating video is not biometric data. Whether **face templates** count is unsettled: they are measurements of facial characteristics used to identify a person, but templates computed from camera video could fall within the "data generated from video or audio recordings" exclusion (text verified 2026-10-06; counsel to confirm). The company treats them as biometric data: a breach of the template store would trigger the 30-day notice duties (P08), and it would apply "reasonable measures" to protect it (501.171(2)) |
| Florida Digital Bill of Rights (Fla. Stat. 501.701 et seq.) | No | No | Applies only to controllers with more than $1 billion in global gross annual revenue (501.702) |
| Fla. Stat. 934.03 (interception of oral communications) | Keep it that way | Keep it that way | The cameras record no audio. Enabling audio would raise interception issues; audio stays disabled |
| State AI or biometric statutes of other states | No | No | The company operates only in Florida. No Florida statute specific to private-sector collection of biometric data was identified in this review (not exhaustively researched) |
| CISA CPG 2.0 (voluntary) | Yes | Yes | Goals 1.D and 1.E (vendor risk) and 3.P (approval process for new hardware and software, which here includes vendor features) |

## 3. Risk tier
Tiers use the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`.

**AI-001: Medium.**
- **Why not High:** the model makes no decision about a person and does not control any door or turnstile. A console officer reviews every alert and decides whether to act. Turnstiles, emergency egress, and fire alarm release work exactly as before.
- **Why not Low:** it processes video of identifiable people, and a biased or noisy alert stream can lead officers to stop some people more than others, or to ignore real tailgating (P01 R-024).
- **Escalation triggers (re-tier to High and re-assess):** any automatic turnstile or door action; linking alerts to badge identities for reports to tenants or discipline; adding face matching; extending to Properties B and C.

**AI-002: High.**
- The system itself would decide whether a person may enter their workplace, which directly affects the physical security operations of a critical infrastructure facility and people's access to their jobs.
- It would create biometric data for about 1,810 people, which is personal information under Fla. Stat. 501.171.
- Face recognition accuracy can differ across demographic groups (NIST IR 8280, *Face Recognition Vendor Test Part 3: Demographic Effects*, 2019), so errors would fall unevenly on tenant employees.

## 4. MEASURE (AI-001 pilot)
Results cover 2026-06-01 to 2026-08-21 (12 weeks). The staged tests were run on 2026-08-12 with 12 volunteer staff.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision: at least 70% of alerts are real tailgating, from a monthly review of 100 random alerts. Recall: at least 90% of 40 staged tailgating passes detected | 1,140 alerts (about 14 per day). 58 of 200 sampled alerts were real tailgating (29% precision). 35 of 40 staged passes detected (87.5% recall) | **No.** Both thresholds missed |
| Safe | Alerts cannot lock turnstiles or doors; emergency egress unaffected | Confirmed in platform settings and a walk test with the fire alarm vendor present (turnstiles release on the hardwired relay) | Yes |
| Secure and resilient | Feature access limited to console roles; portal behind SSO with MFA; vendor security evidence for the feature | Portal MFA in place; the feature is outside the vendor's SOC 2 report; 9 full administrators can change analytics settings (POAM-012) | Partial |
| Accountable and transparent | Tenants and visitors told that analytics run on lobby video; owner named; alerts logged | Lobby signs say only "video surveillance in use"; no tenant notice (P03 G-057) | **No** |
| Explainable and interpretable | The officer can see why an alert fired (clip, lane, badge count) before acting | Clip and badge count shown with every alert | Yes |
| Privacy-enhanced | Customer video not used for vendor model training; alert clips kept no longer than video (30 days) | Training opt-out not exercised; clips kept 1 year | **No** |
| Fair, with harmful bias managed | False-alert rate for passes involving wheelchairs, mobility aids, strollers, carts, or escorted groups compared with all other passes. Flag if the rate is more than twice the baseline | Such passes are about 3% of traffic (lane counts) but 21% of sampled false alerts; false-alert rate about 7 times the baseline, mostly on the wide accessible lane | **No.** Disparity flagged |

**Bias finding.** The model treats a wheelchair user with a companion, or a person with a cart, as two people on one badge. Officers then stop people using the accessible lane far more often than others. That is a real harm to people with disabilities even though no one intended it. Until the vendor fixes it, alerts from the accessible lane go to the console as low-priority "review only" events, and officers must never stop a person on the accessible lane based on an alert alone.

**What was not tested.** Detection performance across skin tones and clothing under the lobby's lighting was not tested, because the staged volunteer group was too small to compare groups fairly. The vendor must provide its own test data by group before the review on 2026-11-30.

## 5. MANAGE
**Human-in-the-loop design (AI-001):**
- The alert is advice to the officer, not a decision.
- The officer watches the clip and checks the badge record before acting. The only permitted action is a courteous badge check by an officer. Nobody is refused entry, reported to a tenant, or disciplined based on an alert.
- Officers can dismiss an alert as a false positive with one click; dismissals feed the monthly quality review.

**Monitoring:**
- Monthly review of 100 random alerts for precision, tracked with P01 R-024.
- Quarterly staged tailgating test (40 passes) for recall.
- Monthly false-alert rate for the accessible lane versus other lanes.
- Tenant and visitor complaints about analytics go to the Security Manager.

**Incident handling:** a security incident at the vendor affecting video or analytics data follows P08 and the vendor's notice terms (72 hours today; 24 hours requested). A pattern of wrongful stops is handled as a service complaint and reported to the COO.

**Change control:** the vendor may not change the model, thresholds, or features without notice, and the company re-runs the staged test after any model update (POL-01 4.10).

**Decommissioning:**
- Turn AI-001 off if precision is still below 50% after 90 days of tuning (by 2026-11-30).
- Turn it off if the vendor will not confirm the training opt-out in writing by 2026-10-31.
- Turn it off if the accessible-lane disparity is not below twice the baseline by 2027-02-28.

## 6. Decision
**AI-001: Approve with conditions.** COO, 2026-08-31. The pilot may continue at Property A only if these conditions are met by 2026-10-31:
1. The vendor confirms in writing that company video is excluded from model training.
2. Alert clip retention is set to 30 days.
3. A plain-language notice goes to Property A tenants, and lobby signs state that video analytics detect tailgating (no face recognition).
4. Accessible-lane alerts are routed as "review only," and officers are briefed on the no-action-on-alert-alone rule.
5. Acceptance thresholds (70% precision, 90% recall) are met by 2026-11-30, or the feature is turned off (section 5).

**AI-002: Reject.** COO, 2026-08-31. Face verification is not approved, and the vendor has been told in writing not to enable it (P01 R-025, treatment Avoid). Reasons:
- It is High tier, and the company has no business need that badges plus tailgating detection do not already meet.
- It would create biometric data for about 1,810 people, adding breach exposure under Fla. Stat. 501.171 and the FTC's biometric concerns.
- The vendor supplied no accuracy or demographic performance evidence, and the feature is outside its SOC 2 report.

A new proposal would need, at minimum: vendor demographic accuracy evidence from an independent evaluation; badge-only entry for anyone who does not opt in; a template storage, encryption, and deletion design; tenant agreement; and a new P10 assessment approved by the majority owner.
