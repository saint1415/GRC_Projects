# AI Governance Risk Assessment: Enterprise AI Portfolio and Video Analytics for Building Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded office and retail REIT; 140 properties in FL, TX, GA, NC, AZ, and CA) |
| Tier / Vertical | Enterprise / Commercial Facilities |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of video analytics for building access in section 7: AI-001 tailgating detection and AI-002 face verification |
| Framework | NIST AI RMF 1.0 (AI 100-1); the AI RMF Playbook for suggested actions; NIST AI 600-1 (Generative AI Profile) for AI-005, AI-008, and AI-011; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the CIO), meeting of 2026-08-19; GRC team prepared the portfolio review; Chief Privacy Officer prepared the CPPA analysis |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 5, Medium 5, Low 2 |
| Status | In production 9, Pilot 2, Disabled 1 |
| Committee review complete | 7 of 12 |
| Not yet reviewed | 5: AI-003, AI-006, AI-007, AI-010, AI-012 (reviews due 2026-11-30; AI-010 only before any use) |
| Use cases with possible CPPA obligations (California) | AI-001 and AI-003 (notice at collection), AI-002 (risk assessment before any California use), AI-006 (possible ADMT for a significant decision, compliance by 2027-01-01), AI-007 (risk assessment before any California use), AI-010 (ADMT and risk assessment before any use) |
| High-tier use cases with local bias testing | 1 of 5 (AI-002); AI-004 has no individuals to test; AI-006, AI-007, and AI-010 are untested |

**Main findings:** five use cases run (or sit ready) without committee review, including two High-tier employment tools (AI-006 in production, AI-007 in pilot). AI-006 may already be ADMT for a significant decision for about 1,100 California employees, with a compliance date of 2027-01-01. The tailgating analytics (AI-001) meet their accuracy targets but stop people on accessible lanes far more often than others. The face verification pilot (AI-002) shows false rejection disparities above threshold for darker self-reported skin tones and for people aged 60 and over.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** CIO (chair); Chief Privacy Officer; CISO; General Counsel's delegate; Chief Human Resources Officer; Vice President, Corporate Security; Senior Vice President, Engineering; Director of OT Security; Vice President, Digital Products; the data science lead. Internal Audit observes and does not vote.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and bias testing on the company's own population; impact assessment, including the CPPA risk assessment where California data is involved; human review design; notice to affected people; monitoring plan; contract terms on data use and model changes |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features a vendor switches on inside an existing product (for example video analytics or recruiting features), must be registered before use (POL-01 4.13; STD-05.3). Procurement and IT change management block AI features without an inventory ID, and the platform vendor must give 30 days' notice of new analytics features. The GRC team owns the inventory.

**Policies:** POL-01 4.13 (no AI or biometric feature without registration and approval); POL-04 4.6 (no new California sensitive-data processing, employee observation, or ADMT without the CPPA review) and 4.9 (no vendor training on company data); POL-05 4.6 (approved AI tools only) and 4.9 (workplace monitoring notice); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case.

**Why 5 use cases lack review.** AI-006 and AI-012 arrived as features inside existing vendor products before the intake block existed (2025); AI-003 sits in the parking operators' systems; AI-007 started as a regional pilot by security operations; and AI-010 is a recruiting feature that is switched off. The committee set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies to | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02) | All use cases with individuals | Unfair or deceptive practices, including undisclosed collection and unsupported accuracy claims. The FTC *Policy Statement on Biometric Information and Section 5 of the FTC Act* (May 18, 2023) lists practices it may treat as unfair, including failing to assess foreseeable harms before collecting biometric information, surreptitious or unexpected collection, failing to evaluate vendors, and failing to monitor whether the technology works as expected. The statement remained posted on ftc.gov at the September 2026 check; whether current FTC leadership still applies it was not confirmed |
| CCPA and CPPA regulations (C-COMMERCIAL-FACILITIES-R03) | California data in AI-001, AI-002, AI-003, AI-006, AI-007, AI-010 | Notice at collection (Cal. Civ. Code 1798.100(a)); risk assessments before processing sensitive personal information (11 CCR 7150(b)(2)), before systematic observation of employees to infer performance or behavior (7150(b)(4)), and before permitting a vendor to use personal information to train facial recognition or identity verification technology (7150(b)(6)); ADMT for significant decisions, including hiring and allocation of work (11 CCR 7200 et seq.; compliance by 2027-01-01 for existing uses). Biometric information processed to identify a consumer is sensitive personal information (1798.140(ae)(2)(A)) |
| California Civil Rights Council automated-decision system regulations (2 CCR 11008 et seq., effective 2025-10-01) | AI-006, AI-007, AI-010 for California employees and applicants | Using an automated-decision system that discriminates is unlawful; anti-bias testing is relevant to defenses; records kept 4 years |
| Federal equal employment opportunity laws (Title VII) | AI-006, AI-007, AI-010 | Disparate-impact liability remains by statute, although the EEOC's 2023 technical assistance on AI selection tools is no longer posted on eeoc.gov (cross-sector file) |
| State biometric, ALPR, and workplace monitoring laws | AI-002, AI-003, AI-007 | Differ by state. Counsel keeps a state-by-state analysis; AI-002 may not expand beyond Florida until counsel reviews each target state |
| Florida worked example: Fla. Stat. 501.171 and 501.702 | AI-001, AI-002 | Personal information includes "biometric data as defined in s. 501.702". Section 501.702 excludes "physical or digital photographs; video or audio recordings or data generated from video or audio recordings", so lobby video for AI-001 is not biometric data. Whether face templates computed from camera video (AI-002) are biometric data is **unsettled** (counsel to confirm); the company treats them as biometric data for breach notice (P08) and protection |
| Florida Digital Bill of Rights | None | The company meets none of the "controller" conditions beyond revenue (Fla. Stat. 501.702) |
| Fla. Stat. 934.03 (worked example for recording laws) | AI-001, AI-002 | Cameras record no audio; enabling audio would raise interception issues, so audio stays disabled (POL-05 4.7) |
| Texas Responsible AI Governance Act (cross-sector file) | All Texas uses | Intent-based prohibitions (for example AI developed with intent to unlawfully discriminate); none of the use cases is designed for a prohibited purpose |
| CISA CPG 2.0 (voluntary) | AI-001, AI-002, AI-004 | Goals 1.D and 1.E (vendor risk) and 3.P (approval of new hardware and software, including vendor features) |
| Colorado SB26-189 | None | The company does not operate in Colorado |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, employment) or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Tailgating detection at 54 lobbies | Medium | In production | Reviewed 2025-11-12; re-reviewed 2026-08-19 |
| AI-002 | Face verification express lane (opt-in) | High | Pilot (2 Florida towers) | Pilot approved with conditions 2026-03-18; re-reviewed 2026-08-19 |
| AI-003 | License plate recognition at 84 garages (operators) | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-004 | BAS energy optimization writing setpoints | High | In production (40 towers) | Reviewed 2025-10-08; re-reviewed 2026-08-19 |
| AI-005 | Generative AI lease abstraction | Medium | In production | Reviewed 2025-12-10 |
| AI-006 | Security officer scheduling and post assignment | High | In production | Not reviewed (due 2026-11-30; ADMT decision by 2026-10-31) |
| AI-007 | Patrol performance analytics | High | Pilot (Florida and Texas) | Not reviewed (due 2026-11-30) |
| AI-008 | Tenant experience platform virtual assistant | Medium | In production | Reviewed 2026-02-11 |
| AI-009 | Predictive maintenance for chillers and air handlers | Low | In production | Reviewed 2026-04-15 |
| AI-010 | Applicant resume screening and ranking | High | Disabled | Not reviewed (required before any use) |
| AI-011 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-012 | Cyber Defense Center alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-004 is High because it writes setpoints into building systems at 40 towers; controller-enforced limits and the kill switch keep it in production. AI-001 stays Medium because an officer reviews every alert and the model controls no door; any automatic turnstile action would re-tier it to High. AI-011 is Medium rather than Low because Confidential data is allowed in its approved tenant.

## 5. CPPA obligations for the AI portfolio (California)
| Obligation | Use cases | What the company does | Status |
|---|---|---|---|
| Notice at collection (1798.100(a)) | AI-001, AI-003 | Update California lobby kiosk screens, signage, and garage notices to state that analytics run on video and plate reads | Partially met: due 2026-12-31 (POAM-021) |
| Risk assessment before processing sensitive personal information (7150(b)(2)) | AI-002 | No California use; a risk assessment is a precondition in the decision (section 9) | Met by restriction |
| Risk assessment before systematic observation of employees (7150(b)(4)) | AI-007 | No California use before an assessment | Met by restriction; review due 2026-11-30 |
| Risk assessment before permitting a vendor to train identity technology (7150(b)(6)) | AI-001, AI-002 (vendor terms) | Written training opt-out confirmed for the East and Central platform tenants; not yet for the West tenant, which holds California video | Partially met: due 2026-11-30 (POAM-024) |
| ADMT for significant decisions (7200 et seq.) | AI-006 (allocation of work); AI-010 (hiring) | AI-006: design meaningful human review that meets the regulation's definition, or provide the pre-use notice, opt-out or appeal, and access process for California officers by 2027-01-01. AI-010 stays disabled | Not met for AI-006 (POAM-023) |

## 6. MEASURE: bias and performance testing plan for the High-tier use cases
| Use case | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-002 face verification | False rejection rate (a genuine enrolled person not matched) | Self-reported skin tone (three bands), sex, and age band in a consented volunteer study | Any group's rate more than 1.5 times the overall rate | Tested: fails (section 7.4) |
| AI-006 officer scheduling | Share of overtime, night posts, and undesirable posts assigned | Sex, age band, and race and ethnicity where recorded | Ratio below 0.8 or above 1.25 for any group compared with the overall share | Not tested (due with the 2026-11-30 review) |
| AI-007 patrol analytics | Share of officers flagged as underperforming | Sex, age band, disability accommodation status (aggregate only) | Flag-rate ratio above 1.25 for any group | Not tested (pilot; no California use) |
| AI-010 resume screening | Selection rate by stage | Sex, race and ethnicity where self-reported | Ratio below 0.8 (four-fifths rule of thumb) | Not tested (feature disabled; vendor adverse impact data requested) |
| AI-004 energy optimization | Comfort complaints by floor and tenant type | Not about individuals | Complaint rate above twice the non-optimized floors | Monitored quarterly; within threshold |

**Data limits:** the company does not hold demographic data about tenant employees, so AI-001 and AI-002 testing uses lane-level analysis and consented volunteer studies. Employee demographic data used for AI-006, AI-007, and AI-010 testing comes from voluntary self-identification, is held by HR, and is used only for testing in aggregate.

## 7. Full assessment: video analytics for building access (AI-001 and AI-002)
### 7.1 MAP
| Item | AI-001 tailgating detection | AI-002 face verification express lane |
|---|---|---|
| Purpose and intended use | Detect when more than one person passes a turnstile lane on a single badge read, and alert the RSOC and lobby desk with a short clip so an officer can check the person's badge | Let tenant employees who opt in pass the express lane without presenting a badge, by matching a live face capture with their enrolled photo |
| Users | RSOC operators and lobby officers at 54 lobbies (8 in California) | Lobby officers at 2 Florida towers; about 1,450 enrolled tenant employees |
| Affected people | About 150,000 tenant employees with credentials at those properties, visitors, and anyone in the lobbies | Enrolled tenant employees; others in the express lane field of view (captures of non-enrolled people are discarded at the edge, vendor-stated and not yet verified) |
| Data | Video of turnstile lanes; badge events; alert clips kept 30 days. No identity inferred | Face templates (treated as biometric data) stored by the vendor; deleted within 24 hours of opt-out or when the credential ends (verified weekly) |
| Build or buy | Buy: feature of the access control and video platform. Covered by the vendor's 2026 SOC 2 report | Buy: feature of the same platform. **Not covered** by the vendor's SOC 2 report; vendor bridge letter only |
| Not intended | Identifying people, locking turnstiles or doors automatically, refusing entry, reporting to tenants, or disciplining anyone | Denying entry, watchlists, identifying non-enrolled people, attendance tracking, or any use outside the 2 pilot towers |

### 7.2 Risk tier
AI-001: Medium (section 4). AI-002: High: the system decides whether a person may pass a workplace entrance at a critical infrastructure facility without a badge, it creates biometric data, and face recognition accuracy can differ across demographic groups (NIST IR 8280, *Face Recognition Vendor Test Part 3: Demographic Effects*, 2019). The opt-in design and the open badge lanes limit the harm, which is why a pilot is allowed at all.

### 7.3 Notice and choice
- Lobby signs at all 54 lobbies state that video analytics detect tailgating and that no face recognition is used in the general lanes. California kiosk screens and the notice at collection do not yet say this (POAM-021).
- AI-002 enrollment is opt-in through the tenant experience app, with a plain-language notice, written consent, a stated retention rule, and a one-tap opt-out. The tenant administrator must agree before its employees are offered enrollment.

### 7.4 MEASURE (2026-05-01 to 2026-07-31)
| Trustworthy characteristic | Test / metric | AI-001 result | AI-002 result | Pass? |
|---|---|---|---|---|
| Valid and reliable | AI-001: precision of at least 70% (300-alert monthly sample) and recall of at least 90% (120 staged passes at 6 lobbies). AI-002: false rejection rate of 2% or less; false matches 0 in testing | About 46,000 alerts; precision 71% (213 of 300); recall 90.8% (109 of 120) | False rejection 1.1% in production (212,000 express-lane passes) and 0.8% in the volunteer study; false match rate vendor-reported only (not tested locally) | AI-001 Yes; AI-002 Partial |
| Safe | Analytics cannot lock turnstiles, doors, or egress paths | Confirmed in platform settings; fire alarm release test with the fire alarm vendor present | Non-match keeps the lane closed; badge lanes always open; egress unaffected (tested) | Yes |
| Secure and resilient | Console behind single sign-on with MFA; administrator roles limited; vendor security evidence | MFA in place; 61 full administrators can change analytics settings (POAM-014) | Templates encrypted per vendor; feature outside the vendor SOC 2 report; template terms not yet in the contract (POAM-024) | Partial |
| Accountable and transparent | Notice to affected people; owner named; decisions logged | Signs updated outside California; California notice incomplete | Opt-in notice and consent records complete for all 1,450 enrollees | AI-001 No; AI-002 Yes |
| Explainable and interpretable | The officer can see why an alert or non-match happened | Clip, lane, and badge count shown with every alert | Non-match shown to the officer with the enrolled photo | Yes |
| Privacy-enhanced | No vendor training on company video; retention limits enforced | Clips kept 30 days; training opt-out confirmed for 2 of 3 platform tenants | Deletion within 24 hours of opt-out verified weekly (0 orphan templates in 13 checks); training opt-out confirmed for the Florida tenant | Partial |
| Fair, with harmful bias managed | AI-001: false alert rate on accessible lanes against other lanes; flag above 2 times. AI-002: false rejection rate by group; flag above 1.5 times the overall rate | Accessible lanes 3.4 times the baseline (wheelchairs, carts, and companions counted as extra people) | Darker self-reported skin tone band 3.2 times the overall rate; age 60 and over 2.9 times; sex within threshold | **No** for both |

**What was not tested.** AI-001 detection performance across skin tones and clothing was not tested, because lane-level samples carry no demographic data; the vendor must provide its own group-level test data. AI-002 false matches (wrongly opening the lane for a non-enrolled person) were not tested locally; the vendor's figure is used until a staged test with consented participants is run in 2026 Q4.

### 7.5 MANAGE
**Human-in-the-loop design:**
- AI-001 alerts are advice, not decisions. The officer watches the clip and checks the badge record before acting, and the only permitted action is a courteous badge check. Nobody is refused entry, reported to a tenant, or disciplined because of an alert. Accessible-lane alerts are routed as review-only, and officers must never stop a person on the accessible lane based on an alert alone.
- AI-002 never denies entry by itself. A non-match keeps the express lane closed; the person uses a badge lane or an officer checks the badge. Officers log non-matches so false rejections can be measured.

**Monitoring:** monthly AI-001 precision and accessible-lane ratio; quarterly AI-001 staged recall test; monthly AI-002 false rejection rate by lane; quarterly AI-002 volunteer study by group; weekly template reconciliation. Results go to the committee and roll up to ER-08 in P01.

**Incident handling:** a vendor security incident affecting video or templates follows P08 and the vendor notice terms (24 hours requested in the contract amendment); a template breach is treated as a breach of biometric data under state law until counsel decides otherwise. A pattern of wrongful stops or rejections is handled as a service complaint and reported to the committee.

**Change control:** the vendor may not change models, thresholds, or features without 30 days' notice, and the company reruns the staged tests after any model update (POL-01 4.13).

**Decommissioning:**
- Turn off AI-001 accessible-lane alerts entirely if the ratio is not below 2 times the baseline by 2027-03-31.
- End the AI-002 pilot and delete all templates if the group disparities are not below the 1.5 threshold by 2027-03-31, if the vendor will not put template terms in the contract by 2026-12-31, or if counsel concludes the pilot needs consents or notices the company cannot obtain.

## 8. MANAGE: portfolio controls
- **Monitoring:** every High-tier use case has quarterly performance and fairness metrics in the inventory's `monitoring` column, reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged in the case system and follow P08 where security or personal information is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts must prohibit training on company data (POL-04 4.9) and require notice of material model changes.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, change data-use terms, or lose their legal basis; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: California notice at collection and kiosk screens updated by 2026-12-31 (POAM-021); written training opt-out for the West tenant by 2026-11-30 (POAM-024); accessible-lane alerts stay review-only and the vendor must fix the model by 2027-03-31.
2. **AI-002:** pilot continues at the 2 Florida towers only, with no expansion. Before any expansion: group disparities below threshold, a local false match test, template terms in the contract, counsel's state review, and, for California, a CPPA risk assessment (7150(b)(2)). Decommissioning triggers in section 7.5 apply.
3. **AI-004:** approved to continue; quarterly limit review and kill-switch test.
4. **AI-006:** the CHRO and counsel must decide by 2026-10-31 whether supervisors can perform meaningful human review that meets the CPPA definition; if not, ADMT notices, opt-out or appeal, and access for California officers by 2027-01-01 (POAM-023). Committee review and bias testing by 2026-11-30.
5. **AI-007:** pilot may continue in Florida and Texas until review on 2026-11-30; results may not be used for discipline or pay; no California use before a CPPA risk assessment.
6. **AI-003 and AI-012:** may continue in current scope until review by 2026-11-30.
7. **AI-010:** stays disabled until committee review, vendor adverse impact data, and an ADMT and risk assessment decision.
