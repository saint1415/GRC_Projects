# AI Risk Assessment: AI Batch-Optimization Feature (AI-001)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| Tier / Vertical | Micro / Chemical |
| AI use case | AI-001: the integrator's AI batch-optimization feature in its cloud portal (SYS-12). It recommends heat-up and mixing settings for T-1. Pilot since 2026-05-11; advisory only; write-back to the PLC exists in the portal and is switched off |
| Why not the registry default | The registry default is a "process-optimization model" built by the company. A 7-person blender builds no models. Its real AI exposure is a vendor feature switched on inside the integrator's portal, which is the same use case bought instead of built (`../00_company-facts.md` section 3) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook, with OT context from NIST SP 800-82 Rev. 3. AI 600-1 (Generative AI Profile) applies only to AI-002 and AI-003 |
| Assessor / date | Office Manager (Security Coordinator) with the Operations Manager, the Owner, and the independent consultant, 2026-08-21. The integrator answered written questions on 2026-08-18 |
| Decision | Owner and President, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Operations Manager, who owns the batch control system. **Decision authority:** the Owner, because AI-001 is High tier and only the Owner may decide on Moderate or higher risks (POL-02 A.3).
- **How the pilot started.** The integrator switched the feature on in May 2026 as part of a portal upgrade, without telling the Owner or assessing it (gap 12). The Operations Manager saw the dashboard through the shared portal login and began trying some of its recommendations. Nobody decided to adopt AI. That is the governance failure this assessment fixes (P01 R-010).
- **Policies that apply:**
  - POL-04 4.6: approved AI tools only. AI-001 may receive T-1 process data only under the conditions in section 6. Write-back stays off.
  - POL-02 A.11: no recipe, setpoint, or alarm limit change without the Owner's written approval. **This also covers any change suggested by AI-001.**
  - POL-02 A.5: vendor security terms, including notice before a vendor changes what its service does (POAM-013).
  - POL-02 A.2: switching on write-back is a major change that triggers a new risk review (P01 section 5).
  - POL-02 C.2: no Restricted information in public AI chatbots (AI-003).
- **Scale for a Micro company:** there is no AI committee. The Owner, the Operations Manager, and the Office Manager review AI use at the monthly security meeting. The Office Manager keeps the approved-tools list in POL-04 4.6 and this inventory.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Suggest a shorter heat-up and mixing profile for T-1 batches (hot-water setpoint, ramp rate, mixer speed, and mix time) to cut batch time and energy. The integrator says the goal is 10% shorter T-1 batches |
| Users | The Operations Manager reads recommendations on the portal dashboard. Blend Operators do not see them |
| Affected people | Blend Operators and anyone in the blend room if a recommendation led to an unsafe batch; customers if product quality drifted. No decisions are made about any person |
| Data | **Inputs:** the T-1 process data stream sent through the cellular gateway: temperatures, load cell weights, dosing pump run times, mixer speed, step times, and the recipe number. **Outputs:** recommended settings with a predicted batch time. **No personal data.** The data is **Restricted** (POL-04) because dose weights and step times reveal formulations |
| Build or buy | Buy: a feature of the integrator's portal, supplied by the portal platform vendor. The integrator could not say what data the model was trained on, or whether the vendor uses the company's data to train models for other customers. **Neither the integrator agreement nor the portal terms address this** |
| How output reaches the process | Today: the Operations Manager reads a recommendation and, if it is adopted, edits the recipe on the HMI by hand. **A write-back option in the portal could send settings straight to the PLC.** It is off, but anyone with the shared portal login could switch it on (P04 finding 2) |
| Not intended | Dosing amounts of any raw material; alarm limits; the hardwired high-temperature cutout; T-2; closed-loop control; evaluating operators. These uses are **excluded**, and enabling any of them requires a new assessment |

**What the review found.** On 2026-08-21 the Operations Manager confirmed that the 2 batch tickets that did not match the HMI recipe in P07 testing (CM-3) were trials of AI-001 recommendations on a non-peroxide degreaser in June 2026. They were made without the Owner's approval and left no record. QC passed both batches. The recipes are being reconciled (POAM-009).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| EPA RMP (40 CFR Part 68) and OSHA PSM (29 CFR 1910.119) | No | No chemical is held above a threshold quantity or at a listed concentration (P03 G-032, G-033). There is no legal management-of-change duty. The company's own change control (POL-02 A.11) does that job for AI-001 |
| CFATS RBPS 8 (C-CHEMICAL-R01) | Voluntary benchmark | AI-001 rides on the remote access path that RBPS 8 aims to protect, and its write-back option is a path for changing critical process controls (P03 G-004) |
| Sector-specific federal AI rules | None identified | The vertical registry lists no chemical-sector AI rule |
| State AI laws (for example Colorado SB26-189) | No | These target automated decisions about people (employment, credit, housing, and similar). AI-001 makes no decisions about people, and the company operates only in Florida |
| FTC Act Section 5 | No (today) | The company makes no public claims about AI. Recheck if AI-assisted production is ever marketed |
| Federal AI executive actions (EO 14179, EO 14365) | No direct obligations | They direct federal agencies, not private businesses |
| Trade secret protection | Yes (business) | Formulations are the company's main asset. Sending process data to a vendor whose data-use terms are unknown risks that protection |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. AI-001 suggests heating and mixing settings for a tank that doses 35% hydrogen peroxide, at a chemical-sector facility. A wrong heat-up setting on a peroxide product could speed decomposition, which gives off heat and oxygen. If write-back were switched on, the model, or anyone with the shared login, could change the process directly.

**What keeps the residual risk acceptable, once the section 6 conditions are met:**
- advisory only, with write-back locked off by a named company administrator
- every adopted recommendation goes through the Owner's written change approval
- recommendations are off for any recipe that contains hydrogen peroxide
- the hardwired emergency stop and T-1 high-temperature cutout work without the PLC
- the gateway is powered on only for approved sessions (POL-02 B.8), so data flows only then

**Escalation triggers (new assessment before any of these):** write-back switched on; recommendations for peroxide recipes or for T-2; any input or output beyond heat-up and mixing; a new model version that the integrator flags as significant; or the portal vendor changing its data-use terms.

## 4. MEASURE
The consultant and the Operations Manager reviewed the portal's history of 160 T-1 batches from 2026-05-11 to 2026-08-14 against the **safe-limit envelope** that the Owner and the Operations Manager wrote down on 2026-08-20: the maximum product temperature and hot-water setpoint stated on each recipe's written safe limits.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Predicted against actual T-1 batch time: mean absolute error under 10% | 9% overall; 16% on the 38 batches of peroxide water-treatment products | **Partial.** Fails for one product family |
| Safe | 100% of recommendations inside the safe-limit envelope; write-back cannot be switched on by a regular user | 7 of 160 recommendations (4%) proposed a heat-up setpoint above the recipe's written maximum, all for peroxide products. None was adopted. Write-back can be switched on by anyone with the shared login | **No** |
| Secure and resilient | Named portal accounts with MFA; write-back setting locked; vendor security evidence (SOC 2 or equivalent) | Shared login without MFA (POAM-001, POAM-002); setting not locked; integrator could not supply the portal vendor's security report | **No** |
| Accountable and transparent | The company is told before features change; each viewed and adopted recommendation is logged with the approval | Feature switched on without notice; adoptions in June left no record | **No** |
| Explainable and interpretable | The dashboard shows why a setting is recommended | Shows the predicted batch time and input trends, with no reason codes. The Operations Manager can compare the suggestion with the recipe | Partial |
| Privacy-enhanced | No personal data in inputs or outputs; vendor does not reuse company data | No personal data (confirmed). Vendor data reuse unknown; the data is Restricted because it reveals formulations | Partial |
| Fair, with harmful bias managed | (a) **Representativeness:** out-of-envelope rate and error by product family (degreasers, cleaners, peroxide water-treatment products) and by season; flag a family more than 5 points worse than overall. (b) **Workforce fairness:** recommendation use is never used to rate individual operators | (a) Peroxide family flagged: 7 of 38 out of envelope (18%) against 0 of 122 for the others; error 16% against 9% overall. Summer and spring within 2 points. (b) Not used for operators; there are no operator-level data (shared HMI login) | **Partial.** One family flagged |

**Bias and representativeness finding.** The model is least reliable on the products where a wrong setting matters most. The likely reason is that it learned mainly from degreaser and cleaner batches, which make up most of T-1's volume. It is not a fairness problem about people, but it is the same kind of failure: a model that works well on average and badly on the group it saw least. Recommendations are **switched off for every recipe that contains hydrogen peroxide** until the integrator shows results inside the envelope on that family.

## 5. MANAGE
**Human in the loop:**
- AI-001 is advisory. Recommendations reach the process only when the Operations Manager proposes a recipe change and **the Owner approves it in writing** on the batch ticket (POL-02 A.11). The approval notes "AI-001 recommendation."
- The first batch after any adopted change is watched from start to finish by the Operations Manager and checked by QC before release.
- Anyone may ignore any recommendation without giving a reason. The recipe's written safe limits, the field thermometer, and the hardwired cutout always take priority.
- Write-back stays off. Only a named company administrator account (the Owner) may change the setting, once named portal accounts exist (POAM-001).

**Data protection:**
- Data flows only while the gateway is on for an approved session (POL-02 B.8).
- At renewal, the integrator agreement must state that company process data is used only to provide the service to the company, is not used to train models for others, and is deleted at the end of the contract (POL-02 A.5; POAM-013).

**Monitoring:**
- Monthly, at the security meeting: number of recommendations, any outside the envelope, any adopted, and the related batch tickets.
- **Pause trigger:** any adopted recommendation that leads to an off-spec batch, or more than 2 recommendations outside the envelope in a month for non-peroxide recipes. Either one pauses AI-001 until reviewed.
- The integrator must tell the company before any model or feature change (POAM-013).

**Incident handling:**
- A recommendation that contributes to a process upset or an off-spec lot is handled as a process incident and logged under POL-03 4.3.
- Suspected misuse of the portal or a write-back event follows the P08 runbook. AI-001 stays off until the Operations Manager confirms the recipes match the paper binder (P08 section 7).

**Decommissioning (switch AI-001 off and ask the integrator to delete company data) if:**
- named portal accounts with MFA and the locked write-back setting are not in place by 2026-10-31;
- the integrator cannot obtain data-use terms from the portal vendor by 2026-12-31;
- recommendations fall outside the envelope again after the integrator's changes.

## 6. Decision
**Approve with conditions.** Owner and President, 2026-08-31.

AI-001 may continue in advisory mode for **non-peroxide T-1 recipes only**, and only if:
1. Recommendations for recipes containing hydrogen peroxide are switched off by the integrator (target 2026-09-15).
2. Write-back stays off and is locked to a named company administrator once named portal accounts with MFA are live (2026-10-31; POAM-001, POAM-002).
3. Every adopted recommendation goes through the Owner's written change approval (in effect from 2026-09-01; POL-02 A.11).
4. The safe-limit envelope is kept with the recipes and reviewed with every recipe change (done 2026-08-20).
5. Data-use and change-notice terms are added to the integrator agreement by 2026-12-31 (POAM-013).
6. The Operations Manager briefs the Blend Operators that AI-001 exists, that it never writes to the PLC, and that a setting that differs from the batch ticket must be reported (POL-03 4.2), by 2026-09-30.

**Extending AI-001 to peroxide recipes** requires three months with no recommendation outside the envelope on that family and a new assessment.

**AI-002 (the SDS service's drafting assistant)** is not approved until it is assessed with AI 600-1. Any SDS it drafts would still need QC Technician review and Owner approval, because a wrong SDS reaches customers, responders, and the ERI provider. **AI-003 (public chatbots)** stays prohibited for Restricted and Internal information (POL-04 4.6; POL-02 C.2).
