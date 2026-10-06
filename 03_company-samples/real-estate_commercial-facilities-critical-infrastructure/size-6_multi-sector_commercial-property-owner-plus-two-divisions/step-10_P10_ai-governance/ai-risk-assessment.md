# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Commercial Property, Construction, Hotels, corporate) |
| Tier / Vertical | Multi-Sector / Commercial Facilities |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the rules that apply to the priority use cases: **video analytics for building access** (AI-001 tailgating detection and AI-002 face verification), the BAS optimization service (AI-003), and the hourly hiring screening tool (AI-008) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the AI RMF Playbook, and the Generative AI Profile (AI 600-1) for AI-005, AI-007, and AI-009 |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-26; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group OT security lead, Group HR director, and one leader from each division. Approves High-tier use cases, vendor feature changes, and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO and Group OT security lead | AI security standard (prompt injection, model supply chain, data leakage) and, for AI that touches building systems, the OT change process |
| Group Chief Privacy Officer | Biometric and video rules (POL-04 4.7), state privacy law, CPPA regulations |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03-16, under POL-01 4.13)
1. **Register before use.** Every AI use case that processes Restricted or Confidential information, supports decisions about people, or can change building operations is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias or safety testing, notice to affected people, and quarterly monitoring reports.
3. **Vendor features count.** A vendor enabling an analytics, biometric, or automated control feature in a group platform is a new use case (POL-01 4.9). Platform contracts must require the vendor to ask first.
4. **Biometric data rules** (POL-04 4.7): approved use only, written notice and opt-in consent, a non-biometric alternative, no vendor model training, deletion within 30 days after enrollment ends.
5. **Building systems.** AI that writes to building systems goes through the OT change process, works only inside RBOC-defined limits, and never touches life-safety systems.
6. **Federal data.** FCI and CUI never go into an AI tool outside the matching CMMC scope (POL-04 4.9).
7. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted in March, but rule 3 was never written into platform contracts. The access control and video vendor turned on tailgating detection at 23 office properties in May and set up the face verification pilot with the Commercial Property security team in June. The BAS optimization service was bought by engineering in 2025 as an energy project, not as AI. None reached the council until this assessment (scenario gap 6; P01 GR-05).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Tailgating detection | Commercial Property | Medium | In production at 23 properties; conditions |
| AI-002 | Face verification at turnstiles | Commercial Property | High | Pilot at 2 towers; automatic denial off; expansion prohibited |
| AI-003 | BAS optimization (writes setpoints) | Group (BAACS) | High | In production at 41 buildings; no new buildings until conditions met |
| AI-004 | Jobsite safety analytics | Construction | Medium | In production at 60 jobsites; coaching only |
| AI-005 | AI estimating and bid assistant | Construction | Medium | Commercial bids only; federal uploads to be blocked |
| AI-006 | Revenue management (room rates) | Hotels | Medium | In production at 88 hotels |
| AI-007 | Guest messaging assistant (generative) | Hotels | Medium | In production at 52 hotels |
| AI-008 | Hourly hiring screening | Hotels (Group HR) | High | In production; conditions |
| AI-009 | Enterprise generative AI assistant | Group | Low | Pilot (3,000 users) |

### 2.1 Video analytics for building access (AI-001 and AI-002)
| Item | AI-001 tailgating detection | AI-002 face verification |
|---|---|---|
| Purpose | Detect more than one person passing a turnstile lane on one badge read, and alert the security console with a short clip | Compare a live face capture with the enrolled template and confirm the badge holder |
| Affected people | About 64,000 tenant badge holders at 23 office properties, visitors, and staff | About 1,900 tenant employees who opted in at 2 Florida towers |
| Data | Lane video and badge events; alert clips. No identity inferred. **Vendor terms allow use of customer video for model improvement; the group has not opted out** | Face templates (numeric representations of facial geometry) from enrollment photos and live captures, held by the vendor |
| Build or buy | Vendor platform feature, outside the vendor's last SOC 2 period (P09) | Vendor feature in pilot, outside the vendor's last SOC 2 period |
| Not intended | Identifying people, automatic lane or door actions, discipline | Use as the only factor, use on visitors, use for any purpose other than entry |

| Rule | AI-001 | AI-002 | Why |
|---|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02) | **Yes** | **Yes** | Covers undisclosed collection and unsupported accuracy claims. The FTC's *Policy Statement on Biometric Information and Section 5 of the FTC Act* (2023-05-18) lists practices it may treat as unfair, including failing to assess foreseeable harms before collection, surreptitious collection, failing to evaluate vendors, and failing to monitor whether the technology works as expected. Whether current FTC leadership still applies the statement was not confirmed |
| State breach and reasonable-security law (Florida worked example) | Limited | **Yes** | Fla. Stat. 501.171 includes "biometric data as defined in s. 501.702" in personal information. Section 501.702 excludes photographs, video or audio recordings, and data generated from them. So tailgating video is not biometric data. Whether **face templates computed from camera video** fall within that exclusion is **unsettled** (counsel to confirm). The group treats them as biometric data: they are covered by reasonable-security duties and by the P08 breach notices |
| Other states' biometric laws | No | **Check** | Enrollees work in Florida but may live elsewhere. Counsel is mapping residence. The group has no operations in Illinois |
| CPPA regulations | No | No | No California sites in these use cases |
| CISA CPG 2.0 (voluntary, adopted) | Yes | Yes | Goals 1.D and 1.E (vendor risk) and 3.P (approval of new software features) |

### 2.2 BAS optimization service (AI-003)
| Rule or commitment | Implication |
|---|---|
| Repository rubric: "can affect physical safety or critical infrastructure operations" | High tier: the service changes heating and cooling in occupied buildings, including tenant server rooms and medical office suites |
| CISA CPG 2.0 goals 1.E and 3.P; NIST SP 800-82 Rev. 3 | A remote SaaS service with write access to OT is a managed service provider path into the BAS; it must be reviewed, limited, and monitored |
| Leases and property management agreements | HVAC service levels and owner approval for changes at managed buildings (4 managed buildings use the service) |
| No AI-specific law identified | The governing rules are safety, contract, and security, not AI statutes |

### 2.3 Hourly hiring screening (AI-008)
| Rule | Implication |
|---|---|
| Cal. Code Regs. tit. 11, 7200 et seq. (CPPA ADMT rules) | Employment decisions are "significant decisions". For applicants to the 2 California hotels, the group needs a pre-use notice, an opt-out path (with the regulation's exceptions), access responses, and a risk assessment. Businesses already using ADMT must comply by 2027-01-01 (P03 GRP-07, Not met) |
| Title VII of the Civil Rights Act of 1964 | Disparate-impact liability still exists by statute even though EEOC guidance on AI selection tools was removed in 2025 and enforcement is deprioritized (EO 14281). The Uniform Guidelines' four-fifths rule (29 CFR 1607.4(D)) is used here as a screening test, not a safe harbor |
| Colorado SB26-189 | Not applicable: no Colorado operations |
| FTC Act Section 5 | Vendor accuracy and fairness claims must be checked, not assumed |

### 2.4 Other use cases (summary)
- **AI-004 jobsite safety analytics:** worker video; becomes an employment use if alerts feed discipline, so the coaching-only rule is the control.
- **AI-005 estimating assistant:** the risk is federal data reaching a tool outside the CMMC scopes (P03 CN-G-003; POAM-017).
- **AI-006 revenue management and AI-007 guest messaging:** 16 CFR 464.2 requires the total price, including mandatory fees, in every price display; July samples found base rates without the resort fee in the assistant's answers and two channel feeds (P03 HO-G-070).
- **AI-009 enterprise assistant:** internal productivity with data loss rules; Low.

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (decides, or would decide, whether a person can enter their workplace and creates biometric data), AI-003 (can affect safety and critical infrastructure operations), AI-008 (substantial factor in employment decisions).
- **Medium:** AI-001, AI-004, AI-005, AI-006, AI-007. Humans make the final decision, but outputs reach people or regulated data.
- **Low:** AI-009.

**Re-tier triggers:** any automatic lane or door action from AI-001 (to High); extending AI-002 beyond the 2 towers or to visitors (re-assess); AI-003 writing outside RBOC limits or to any life-safety interface (prohibited); AI-004 alerts used for discipline (to High); AI-007 answering accessibility or safety questions without handoff (re-assess).

## 4. MEASURE
Results are from monitoring and tests between 2026-06-01 and 2026-08-21. The staged tests were run on 2026-08-12 with 40 volunteer staff at one tower.

### 4.1 AI-001 tailgating detection
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision at least 70% (monthly review of 100 random alerts per region); recall at least 90% of 40 staged tailgating passes | 31% precision (186 of 600 sampled alerts were real tailgating); 36 of 40 staged passes detected (90% recall) | **No** (precision) |
| Safe | Alerts cannot lock lanes or doors; emergency egress unaffected | Confirmed in platform settings and a walk test with the fire alarm vendor present | Yes |
| Secure and resilient | Feature settings limited to 6 administrators; vendor evidence for the feature | 40 enterprise administrators can change settings; feature outside the vendor's SOC 2 period | **No** |
| Accountable and transparent | Tenants and visitors told that analytics run on lobby video | Lobby signs say only "video surveillance in use" (P03 G-057) | **No** |
| Privacy-enhanced | Vendor training opt-out exercised; alert clips kept no longer than video (30 days) | Opt-out not exercised; clips kept 1 year (POAM-014) | **No** |
| Fair, harmful bias managed | False-alert rate for passes with wheelchairs, mobility aids, strollers, carts, or escorted groups compared with all other passes; flag above 2 times the baseline | About 3% of traffic but 19% of sampled false alerts; false-alert rate about 6 times the baseline, mostly on wide accessible lanes | **No. Disparity flagged** |

**Bias finding.** The model counts a wheelchair user with a companion, or a person with a cart, as two people on one badge. Officers then stop people using the accessible lane far more often than others. Until the vendor fixes it, accessible-lane alerts are review-only and officers must never stop a person on that lane based on an alert alone.

### 4.2 AI-002 face verification (pilot)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False rejection rate (genuine user rejected) under 1% per attempt; false acceptance in staged impostor tests 0 of 200 | 2.4% false rejections over 61,000 attempts; 1 of 200 impostor attempts accepted | **No** |
| Fair, harmful bias managed | False rejection rate by self-reported age band, sex, and skin tone group (volunteer subset of 40, plus vendor test data); flag a group more than 2 times the lowest group | Rejections for enrollees 65 and older were 3.1 times the lowest group; vendor provided no demographic test data. Face recognition accuracy can differ across demographic groups (NIST IR 8280, *Face Recognition Vendor Test Part 3: Demographic Effects*, 2019) | **No. Disparity flagged** |
| Safe | Rejection never blocks emergency egress; a rejected person can enter with badge plus guard check | Since 2026-08-31, yes; before that, the vendor default denied entry and 23 people were sent to the desk in one week | Yes (after change) |
| Accountable and transparent | Written notice and opt-in consent for every enrollee; badge-only alternative | Consent records for 1,710 of about 1,900 enrollees (90%); the alternative exists but is not described in the notice | **No** |
| Privacy-enhanced | Templates used only for entry; deleted within 30 days after enrollment ends; no vendor training | No deletion rule configured; vendor terms silent on template training | **No** |
| Secure and resilient | Template store protected; export alerts | Templates were included in the platform's bulk export function (relevant to the P08 scenario) | **No** |

### 4.3 AI-003 BAS optimization
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Safe | Setpoints stay inside RBOC ranges; critical rooms (server rooms, medical suites, kitchens) excluded | Ranges enforced; 11 critical rooms at 6 buildings were not excluded; 4 comfort complaints traced to the service | **No** |
| Valid and reliable | Energy savings against baseline; no excursions outside comfort bands longer than 30 minutes | 9% energy savings; 37 excursions over 30 minutes in 12 weeks | Partial |
| Secure and resilient | Vendor security assurance; API least privilege; RBOC override tested | No SOC report; API scoped to setpoints; override tested at 3 buildings | **No** |
| Accountable and transparent | Owners of managed buildings approved use | 2 of 4 owners approved in writing | **No** |

### 4.4 AI-008 hourly hiring screening
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Fair, harmful bias managed | Selection-to-interview rate by sex and by race and ethnicity, compared under the four-fifths rule (29 CFR 1607.4(D)), from the group's own 2026 applicant data where self-identification exists | Sex and race and ethnicity ratios above 0.8 (self-identification coverage 64%). Age is outside the Uniform Guidelines but was compared the same way: applicants aged 55 and older were interviewed at 0.71 of the rate of the highest group | **Flagged** (age; low coverage) |
| Accountable and transparent | Applicants told that an automated tool is used; California ADMT notice | No notice anywhere | **No** |
| Valid and reliable | Ranked applicants hired and retained at 90 days, compared with recruiter-sourced applicants | Similar retention (78% versus 76%) | Yes |
| Human oversight | No rejection without recruiter review | In place from 2026-10-01; before that, low-ranked applicants received automatic decline emails | Yes (after change) |

### 4.5 Generative use cases (AI 600-1)
| Use case | AI 600-1 risk | Test | Result | Pass? |
|---|---|---|---|---|
| AI-007 guest messaging | Confabulation; information integrity | 300 sampled answers checked against hotel policies and prices | 4% wrong; 9 answers quoted rates without the resort fee | **No** |
| AI-007 guest messaging | Data privacy; information security (prompt injection) | Red-team test of 50 crafted messages | 1 message retrieved another guest's arrival date | **No** |
| AI-005 estimating | Data privacy (value chain) | CUI discovery scan of the workspace | FCI found; no CUI | Partial |
| AI-009 enterprise assistant | Data privacy | Data loss rule test for Restricted data, FCI, and CUI markings | Blocked in 50 of 50 tests | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** officers review every clip before acting; only a courteous badge check is allowed; accessible-lane alerts are review-only.
- **AI-002:** a mismatch alerts a guard, who checks the badge; no automatic denial; badge-only entry always available.
- **AI-003:** the RBOC sets ranges and can override at any time; critical rooms excluded; the service never writes to life-safety interfaces.
- **AI-008:** no applicant is declined without a recruiter review; applicants can ask for a human review.
- **AI-007:** safety, accessibility, and billing topics hand off to staff; the assistant tells guests it is an AI.

**Monitoring:** monthly metrics to use-case owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-05, CF-010, CF-011, CF-012, HO-010, HO-012, HO-013, CN-010, CN-011.

**Incident handling:** AI failures that affect safety, expose personal or federal data, or breach contract commitments follow P08 and POL-03. A breach of the face template store is handled as biometric data under state law (Florida worked example).

**Decommissioning:** each use case has an off switch and a fallback the BIA covers (P05): guards and badges for AI-001 and AI-002, RBOC schedules for AI-003, recruiter screening for AI-008, staff for AI-007. On retirement of AI-002, templates are deleted within 30 days with a vendor certificate.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-002 face verification | **Pilot continues without automatic denial; no expansion** (council, 2026-08-26; board risk committee informed 2026-09-15) | Consent records for every enrollee and a revised notice describing the badge-only alternative by 2026-10-31; 30-day deletion rule and no-training terms by 2026-11-30; vendor demographic test data and a fix for the age-band disparity before any decision to continue past 2026-12-31; templates removed from bulk export (POAM-023) |
| AI-001 tailgating detection | **Continue with conditions** | Vendor training opt-out and 30-day clip retention by 2026-11-30 (POAM-014); tenant and visitor notice by 2026-11-30; precision of at least 70% and an accessible-lane fix by 2026-12-31, or switch the feature off |
| AI-003 BAS optimization | **Continue at current buildings only** | Exclude critical rooms by 2026-10-31; vendor security review or SOC report by 2026-12-31; written approval from the 2 remaining managed-building owners or removal from their buildings by 2026-11-30 |
| AI-008 hiring screening | **Continue with conditions** | Applicant notice by 2026-11-30; age-band analysis with the vendor by 2026-12-15; California: comply with the ADMT rules or stop use there by 2026-12-31 (POAM-028) |
| AI-007 guest messaging | **Continue; no new hotels** | Fix total-price answers and the cross-guest retrieval issue; retest by 2026-12-31 |
| AI-005 estimating | **Continue for commercial bids** | Block federal uploads by 2026-11-30 (POAM-017) |
| AI-004 jobsite analytics | **Approved** | Coaching only; re-assess if any discipline use is proposed |
| AI-006 revenue management | **Approved** | Total price in channel feeds by 2026-12-31 |
| AI-009 enterprise assistant | **Approved for the pilot** | Data loss rules stay on; no use for decisions about people |
