# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Ambulance Services, Urgent Care, Billing and Dispatch Services, corporate) |
| Tier / Vertical | Multi-Sector / Emergency Services |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator- and contract-specific rules for the priority use case, AI-assisted emergency call triage (AI-001), plus the other two High-tier use cases (AI-003 unit posting, AI-005 symptom checker) and the claim coding assistant (AI-006) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-26; presented to the board risk committee 2026-09-16 |
| Inventory | `ai-use-case-inventory.csv` (8 use cases: 3 High, 4 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Ambulance Services chief medical officer, Urgent Care chief medical officer, BDS vice president of communications operations, BDS revenue cycle president. Approves High-tier use cases, mode changes, and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (data leakage, vendor model changes, prompt injection for generative tools) |
| Group Chief Privacy Officer | PHI use, BAAs, client terms, recording consent |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches PHI or caller audio, or that supports decisions about patients, callers, response priority, unit deployment, or claims, is registered in the inventory before deployment, a **mode change** (shadow to advisory, advisory to wider use), or a material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves, a pre-deployment impact assessment and bias testing are required, and monitoring is reported quarterly.
3. **No BAA, no PHI** (POL-01 4.8; POL-04 4.9). AI vendors that handle PHI sign BAAs or subcontractor agreements with no-training and retention terms. **Client data needs client permission:** BDS must not send an external client's data to an AI feature until that client's agreement allows it.
4. **Regulator and contract overlays.** Each division supplement adds its rules: dispatch protocol and county response standards for Ambulance Services, recording consent and Section 1557 for Urgent Care, client BAAs, SOC 2 commitments, and Medicare coding rules for BDS.
5. **Change gate.** A vendor model update triggers a 30-day return to shadow mode for AI-001 and re-testing for others.
6. **Approved tools only** for workforce generative AI (POL-05 4.8).

**Where the program fell short in 2026.** The standard was adopted on 2026-03 while AI-001 was already in shadow mode, and BDS moved it to advisory mode at the Florida center on 2026-06-01 without council review (scenario gap 6). In shadow mode the module also processed audio from client agencies' callers, which their BAAs do not cover. AI-003 has run since 2024 and had never been assessed. Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI-assisted emergency call triage | BDS (for Ambulance Services) | High | Advisory at the Florida center (internal English calls); shadow elsewhere; conditions |
| AI-002 | ePCR narrative drafting | Ambulance Services | Medium | Pilot (300 tablets) |
| AI-003 | Unit posting (system status management) model | Ambulance Services | High | In production since 2024; conditions |
| AI-004 | Urgent care AI scribe | Urgent Care | Medium | In production (140 providers); expansion paused |
| AI-005 | Online symptom checker | Urgent Care | High | Proposed; not approved |
| AI-006 | Ambulance claim coding assistant | BDS | Medium | In production since 2026-07-15; conditions |
| AI-007 | Claim denial prediction model | BDS | Low | Approved |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (1,500 users) |

### 2.1 AI-001 AI-assisted emergency call triage
| Item | Description |
|---|---|
| Purpose and intended use | Transcribe calls in real time and suggest a call type, a response priority, and alerts for critical keywords (for example, "not breathing"), so time-critical calls such as cardiac arrest and stroke are recognized sooner |
| Users / operators | About 1,100 telecommunicators at 4 centers; only Florida center telecommunicators see prompts today |
| Affected people | Callers and patients on about 8,500 responses a day, including callers transferred from 21 county PSAPs and, until 2026-10-07, callers to 14 client agencies; crews sent at the chosen priority |
| Data | Live call audio and transcripts (ePHI). The amended BAA (2026-04-30) bars training on group data and sets 7-day audio deletion |
| Build or buy | Buy: the CAD vendor's cloud AI service |
| Not intended | Automatic dispatch; lowering a priority; pre-arrival instructions; calls through relay services |

| Rule | Applies? | What it means for AI-001 |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | The vendor is a business associate (for Ambulance Services) and a subcontractor (for BDS). The amendment covers the two internal divisions only. For client agencies, BDS may use and disclose PHI only as each BAA permits (164.502(a)(3)) and needs subcontractor assurances (164.308(b)(2)); neither was in place, so client calls were excluded on 2026-10-07 (POAM-017) |
| Section 1557, 45 CFR 92.210 | **Yes (treated as in scope)** | Ambulance Services receives federal financial assistance through Medicaid. A patient care decision support tool is "any automated or non-automated tool" used to support clinical decision-making (45 CFR 92.4), and assigning response priority by symptom acuity supports a clinical decision. The tool takes no race or age input, but its accuracy varies by caller language (a national origin factor) and by patient age, so the 92.210(b) identification and 92.210(c) mitigation duties are applied |
| State recording laws (Florida worked example: Fla. Stat. 934.03(2)(g)) | **Yes, with a question for counsel** | The paragraph lets employees of a licensed ambulance service and other entities with published emergency numbers record incoming calls, and limits recording on 911 and published nonemergency numbers to those staffed at PSAPs. BDS is not itself the licensed ambulance service. Counsel must confirm which BDS lines and centers the paragraph covers in each state; a recorded announcement on request lines is the safeguard meanwhile |
| Fla. Stat. 501.171 and other state breach laws | Yes | Audio and transcripts contain personal information, including medical information |
| County ambulance agreements and client contracts | Yes (contract) | Response standards; clients' rights over their callers' data |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims; keep them in the procurement file |
| FDA device rules | Not determined | The vendor, as manufacturer, must state its regulatory position in writing |
| State AI laws (Colorado SB26-189; Texas TRAIGA) | No | The 7 states of operation and BDS's 22 client states include neither Colorado nor Texas. Recheck before any expansion; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md` |

### 2.2 Other use cases: key rules
| Use case | Rule | Implication |
|---|---|---|
| AI-003 unit posting | County ambulance agreements (response standards); the repository rubric (safety and critical infrastructure operations) | A model that minimizes average response time can lengthen response times in low-demand neighborhoods. Equity by zone must be measured |
| AI-005 symptom checker | 45 CFR 92.210; HIPAA; FTC Act Section 5 | The tool would tell patients where to seek care, including whether to call 911. It must not be deployed until validated and bias-tested |
| AI-006 coding assistant | Medicare ambulance rules (42 CFR 410.40, level of service and medical necessity); client BAAs; SOC 2 Processing Integrity | Suggestions that overstate the level of service create false claims risk for BDS's clients. The feature must be described in the next revenue cycle SOC 2 report (P09) |
| AI-004 scribe | State recording consent laws (Fla. Stat. 934.03(2)(d) worked example); HIPAA | Recording may start only after every party consents in all-party consent states |
| AI-002 narrative drafting | State EMS records accuracy (Fla. Stat. 401.30(1) worked example) | Accurate records are a licensure duty; crews own the narrative |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (a factor in response priority, which affects physical safety), AI-003 (affects where ambulances wait and therefore response times, a safety and critical infrastructure operations effect), AI-005 (would steer patients' choice of care, including emergencies).
- **Medium:** AI-002, AI-004, AI-006, AI-008. Humans make the final decision, but outputs enter records, claims, or decisions.
- **Low:** AI-007.

**Re-tier triggers:** letting AI-001 lower a priority or dispatch automatically (prohibited); enabling scribe or narrative suggestions about treatment (AI-002, AI-004 to High); letting AI-006 release claims without coder review (to High).

## 4. MEASURE
### 4.1 AI-001 AI-assisted emergency call triage
**Reference standard:** the Ambulance Services quality team's review of each sampled call against the acuity found at patient contact (from the ePCR), overseen by the chief medical officer. Shadow-mode sample: 6,000 calls from all 4 centers (2026-02-02 to 2026-07-31), 1,240 of them time-critical. Advisory-mode data: all English-language calls at the Florida center, 2026-06-01 to 2026-07-31.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Under-triage: share of time-critical calls where the AI suggested a lower priority. Threshold: 2% or less, and no worse than telecommunicators using the protocol | AI 3.1% (38 of 1,240); telecommunicators 1.2% (15 of 1,240) | **No** |
| Valid and reliable | Over-triage: share of non-critical calls suggested as highest priority. Threshold: 25% or less (tolerable in an upgrade-only design) | 17% | Yes |
| Safe | Critical keyword sensitivity. Threshold: 98% or more | English 97.1%; Spanish 84% | **No** |
| Safe (advisory effect) | Median time from call answer to dispatch for time-critical calls, Florida center, advisory period vs the same months of 2025 | 9 seconds faster; no case found where a prompt delayed dispatch | Yes |
| Safe (automation bias) | Share of upgrade prompts accepted on calls later judged non-critical. Flag above 50% | 44% | Yes (watch) |
| Secure and resilient | BAA coverage; named CAD accounts; vendor assurance covering the AI service; alert if the transcript stream fails | Internal BAA in place; client callers were not covered; vendor SOC 2 does not cover the AI service (POAM-020); failure alert works | **No** |
| Accountable and transparent | Suggestions and telecommunicator decisions logged with model version; recorded announcement on request lines | Logging complete; announcement in place at 2 of 4 centers | Partial |
| Explainable and interpretable | Telecommunicator can see which transcript words drove each prompt | Available and used at the Florida center | Yes |
| Privacy-enhanced | No training on group data; audio deleted within 7 days; client data only with client permission | Internal terms met; client callers processed in shadow mode without permission until 2026-10-07 | **No** |
| Fair, with harmful bias managed | Under-triage by caller language (English, Spanish, Haitian Creole) and by patient age (75 and over vs under 75). Flag if a group exceeds the English or under-75 rate by more than 2 points; fewer than 50 time-critical calls is reported as insufficient data | English 2.2% (22 of 1,002); Spanish 7.4% (14 of 190); Haitian Creole 2 of 48 (insufficient data); 75 and over 4.6% (24 of 520) vs under 75 1.9% (14 of 720) | **No.** Spanish-language and age disparities flagged |

**Bias finding.** As in smaller deployments, most of the gap traces to transcription errors in Spanish and to indirect symptom descriptions by elderly callers or their family members. At this scale the Spanish sample is large enough to be meaningful (190 time-critical calls). Under 45 CFR 92.210(c), the mitigation is: (1) the upgrade-only design, so the AI can never lower a telecommunicator's priority; (2) advisory mode only for English-language calls; (3) the dispatch protocol remains the decision of record; and (4) the vendor must supply accuracy data by language and age before any wider use.

### 4.2 AI-003 unit posting model
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 90th-percentile response time vs county standards, all zones | Meets standards in 36 of 38 agreements | Yes |
| Fair, harmful bias managed | 90th-percentile response time by zone, flag a zone more than 2 minutes above its county median | 11 rural and low-income zones in 4 counties flagged | **Flagged** |
| Accountable | Supervisor overrides logged | Logged | Yes |

### 4.3 AI-006 coding assistant
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly audit of 50 claims; suggested level of service matches the record | 46 of 50 (92%); all 4 errors suggested a higher level of service | **No** (target 98%) |
| Safe (automation bias) | Coder acceptance rate of suggestions; flag above 90% | 96% | **Flagged** |
| Accountable | Feature permitted by each client's agreement | Confirmed for internal divisions and 112 of 170 clients; disabled for the rest | Partial |

### 4.4 Other use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 narrative drafting | Narratives with a statement not supported by the structured fields (target under 1%) | 2.3% (7 of 300 sampled) | **No** |
| AI-004 scribe | Consent documented before recording (target 100%) | 93% (186 of 200, P03) | **No** |
| AI-005 symptom checker | Not deployed; vendor validation data requested | n/a | n/a |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the telecommunicator runs the protocol and sets the priority on every call. The AI may show an upgrade prompt and keyword alerts; it never shows a lower priority and never dispatches. Dismissals take one click and are logged; supervisors sample 20 dismissals per center each week. If the transcript stream fails, the screen says so and the protocol continues.
- **AI-003:** deployment analysts approve each hourly plan; shift supervisors can override at any time; zones flagged for equity get a minimum-coverage rule.
- **AI-006:** certified coders accept or change every suggestion; claims cannot be released by the feature.
- **AI-002 and AI-004:** crews and providers review, edit, and sign every narrative and note.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, AMB-011, AMB-012, UC-004, UC-005, BDS-004, BDS-010.

**Incident handling:** any call where AI output contributed to a delay is a clinical incident reviewed by the chief medical officer, with P08 escalation if data or security is involved. A vendor security incident follows P08 and the BAA terms.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05 BP-BD06 and BP-AM08): the dispatch protocol without prompts, static posting plans, manual coding, and standard documentation.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 call triage | **Continue with conditions** (council, 2026-08-26; board risk committee informed 2026-09-16). Advisory mode stays at the Florida center for internal English-language calls only; shadow mode elsewhere | Client agency calls excluded by 2026-10-07 and until each client's agreement is amended (POAM-017); recorded announcement at all centers by 2026-10-31; counsel's written view on state recording law coverage of BDS centers by 2026-11-30; vendor accuracy data by language and age and a statement of its FDA position by 2026-12-31; **no expansion** to other centers or languages until under-triage is 2% or less overall and no group is flagged over 60 more days |
| AI-003 unit posting | **Continue with conditions** | Minimum-coverage rule for the 11 flagged zones by 2026-11-30; response-time equity metric in each monthly county report by 2027-01-31 |
| AI-006 coding assistant | **Continue with conditions** | Monthly 50-claim audit by level of service; acceptance-rate alert to coding supervisors; feature described in the next revenue cycle SOC 2 system description; disabled for any client whose agreement does not allow it |
| AI-002 narrative drafting | **Continue pilot; no expansion** | Below 1% unsupported statements for 3 consecutive months |
| AI-004 AI scribe | **Continue; expansion paused** | Consent field mandatory by 2026-11-30 |
| AI-005 symptom checker | **Not approved** | Pre-deployment impact assessment, clinical validation against emergency department outcomes, bias testing by age, sex, and language, and a design that always shows 911 for red-flag symptoms |
| AI-007, AI-008 | **Approved** | Standard monitoring; AI-008 prohibited for dispatch, clinical, or coding decisions |
