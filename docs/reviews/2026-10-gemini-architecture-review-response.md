# Response to the external architecture review (Gemini), October 2026

**Date:** 2026-10-07
**Reviewed document:** "Architectural & Methodological Review: GRC Sample Company Explorer" (external reviewer: Gemini). It has 10 findings in four groups: narrative (1.1, 1.2), sequencing (2.1, 2.2), size scaling (3.1, 3.2, 3.3), and industry blind spots (4.1, 4.2, 4.3).
**Method:** each claim was checked against the repository with file reads, grep, and counts. Legal claims were checked against primary sources: eCFR (point-in-time 2026-10-01, through the eCFR versioner API), the U.S. Code on govinfo (2023 edition, because uscode.house.gov was down for maintenance), NIST SP 800-37 Rev. 2 (PDF from nvlpubs.nist.gov), the NIST SP 800-53 Rev. 5 OSCAL catalog (usnistgov/oscal-content), and the NYC DCWP AEDT page. A source that could not be reached is marked **not verified**.
**Scope of this document:** it records verdicts and proposed fixes.
**Status:** fixes A to G are applied in the same change as this document. For the credit union and the cooperative, the existing "Legal form and ownership" row was split into "Legal form" and "Ownership" rows instead of adding new ones. The backlog is not started.

## Summary

| Finding | Verdict | Confidence | Action |
|---|---|---|---|
| 1.1 Single-owner governance | Partly agree (premise rejected; documentation gaps accepted) | 0.85 | Fix in this round: correct three README legal forms; add control-approval and FOCI fact rows to four samples |
| 1.2 One-size-fits-all pipeline | Partly agree | 0.70 | Fix in this round: write the P09 and P10 fit checks into the build guide and the P10 method. No structural branching |
| 2.1 SSP before risk and gaps | Partly agree | 0.70 | Fix in this round: state in the build guide that the step 2 SSP is an as-is baseline that later steps update. No reorder |
| 2.2 Policies after design | Disagree | 0.75 | No change (covered by the 2.1 note) |
| 3.1 Size 1 separation of duties | Partly agree | 0.75 | Fix in this round: add a compensating controls table for sizes 1-2. Backlog: explicit tailoring rows in 36 size-1 SSPs |
| 3.2 Enterprise drift at sizes 2-3 | Disagree | 0.85 | No change |
| 3.3 Size 6 blast radius | Partly agree | 0.60 | Fix in this round: add a tenancy and identity decision to the P04 method. Backlog: add it to 36 size-6 samples |
| 4.1 (a) Custom-exempt processor | Partly agree (narrow) | 0.75 | Fix in this round: label the README "What the business handles" list as industry-typical |
| 4.1 (b) OT/ICS runbooks | Disagree | 0.85 | No change |
| 4.2 NYC Local Law 144 and bias audits | Disagree | 0.85 | No change |
| 4.3 SP 800-171 Rev. 3 trap | Disagree | 0.95 | No change |

---

## 1.1 The single-owner governance paradox

**Claim.** One owner holding 100% of critical infrastructure companies violates statutory governance. Add boards, proxies, or trusts for sizes 5-6 and critical infrastructure.

**Evidence from the repository.**
- The samples are not one conglomerate. `01_company-sizes/README.md`: "Six parallel, independent size variants ... Each is a standalone scenario, not a growth story."
- Only sizes 1-3 are owner-controlled. `01_company-sizes/tiers.csv`: t4 "Private equity-backed; board with an audit committee"; t5 "Public shareholders; board with audit and risk committees"; t6 "Public shareholders; divisions report to a corporate holding entity". So the proposed fix for sizes 5-6 already exists.
- Regulated small samples already have boards or are member-owned. `finance-insurance/size-3_small_community-bank/00_company-facts.md`: a 7-director board and an Audit and Risk Committee; the bank is "wholly owned by Cris Santos Company, its bank holding company". `finance-insurance/size-2_micro_community-credit-union` and `utilities/size-2_micro_small-electric-cooperative` are member-owned with elected boards.
- Nuclear reactors start at size 4 (`utilities_nuclear-critical-infrastructure/size-4_mid-market_nuclear-power-plant`, PE-backed with a board). The size 3 nuclear sample is a waste processor licensed by Florida as an NRC Agreement State, not a reactor.
- Only the size 5 and size 6 DIB samples hold facility clearances. Sizes 1-4 say "no facility clearance, so NISPOM (32 CFR Part 117) does not apply" (`manufacturing_defense-industrial-base-critical-infrastructure/size-*/00_company-facts.md`).
- **Real gaps found.**
  1. Three generated READMEs show the wrong legal form and ownership. `finance-insurance/size-3_small_community-bank/README.md` says "Legal form | LLC or privately held corporation" for "Cris Santos Bank, N.A.". The credit union and the electric cooperative READMEs say "Limited liability company (LLC)" and "Privately held by Cris Santos", although their facts files say they are member-owned. Cause: `tools/build_scenarios.py` (`write_scenario`) takes legal form from the tier unless the facts file says "not publicly traded".
  2. No sample records the regulator approvals that control of a bank or a reactor licensee requires (grep for "Change in Bank Control", "1817(j)", "50.80": no hits in facts files).
  3. The two cleared DIB samples (sizes 5 and 6) do not state a FOCI status (grep "FOCI", "SF 328": no hits).

**Primary sources checked.**
- A single U.S. person may control a bank, with notice or approval. 12 U.S.C. 1817(j)(1): no person may acquire control of an insured depository institution "unless the appropriate Federal banking agency has been given sixty days' prior written notice". For a national bank, 12 CFR 5.50(b) requires the 60-day notice to the OCC, but 5.50(c)(2)(iii) exempts a transaction subject to approval under BHC Act section 3. 12 U.S.C. 1842(a) and 12 CFR 225.11(a)-(b) require Federal Reserve approval to become a bank holding company or to make a bank its subsidiary. 12 CFR 225.41(a) and (c)(1) require 60 days' notice to the Board before acquiring control (25% or more of voting securities) of a bank holding company.
- A national bank is a corporation. 12 U.S.C. 24: a national banking association "shall become ... a body corporate". So "LLC" is wrong.
- Nuclear: 10 CFR 50.80(a) bars any direct or indirect transfer of control of a Part 50 license "unless the Commission gives its consent in writing"; 50.80(b)(1)(i) asks for the transferee's technical and financial qualifications. 10 CFR 50.38 (as amended, 91 FR 21723, 2026-04-23) limits licenses for entities owned, controlled, or dominated by foreign interests. Neither bars a U.S. individual owner.
- FOCI: 32 CFR 117.11(a) describes "FOCI procedures for cleared U.S. entities". An uncleared company has no FOCI review. 117.11(c) requires an SF 328 for the entity eligibility determination and when significant changes occur.
- CFIUS: a covered transaction must be "by or with any foreign person" (31 CFR 800.210, 800.213, 800.224). The repository is U.S.-only (`README.md`, "United States only"), and the DIB size-1 facts say "The owner is a U.S. citizen". CFIUS does not arise.

**Verdict.** Partly agree, 0.85. The statutory premise is wrong: single-person control is lawful with approvals, and the samples already add boards and public ownership at sizes 4-6. The reviewer is right that the samples are silent on the approvals, and the review led us to three wrong README legal forms.

**Action.** Fix in this round (see Fixes A and B). No change to the tier ownership model.

## 1.2 The "one-size-fits-all" project pipeline

**Claim.** Every company runs the same 10 projects, so a sole-proprietor farm or custom-exempt processor is forced into a SOC 2 Type 2, and micro farms into AI bureaucracy.

**Evidence.**
- Depth already scales. `01_company-sizes/tier-project-scaling.csv`: t1 P09 "Readiness self-check; many criteria marked not applicable with rationale"; t1 P10 "One third-party AI tool the owner uses ... One-page AI use assessment". A Type 2 readiness target starts only at t4.
- All 72 size-1 and size-2 P09 summaries open with a "## 1. Why SOC 2" section (72 of 72). `agriculture/size-1_sole-proprietor_crop-farm/step-09_P09_soc2-readiness/soc2-readiness-summary.md`: "A one-person farm would not obtain a SOC 2 report." The custom-exempt shop says the same: "A custom-exempt shop would not obtain a SOC 2 report." Non-service businesses use the criteria for an insurer or customer questionnaire, for example the credit union ("**not** a SOC 2 service organization") and the micro grocery ("PCI DSS validation is the store's assurance mechanism").
- All 72 size 1-2 samples include `vendor-soc2-review.csv`, a review of a key vendor's report.
- The universal P09 method already starts with a fit check: "Decide whether SOC 2 fits (macro) ... If the scenario is not a service organization ..." (`00_universal-framework/projects/step-09_P09_soc2-readiness/README.md`).
- P10 at size 1 targets a real risk. The custom-exempt shop's one-page P10 covers a public chatbot used to scale cure amounts; one answer was "about 25% above the chart", which bears on 9 CFR 424.21(c) (`agriculture_food-agriculture-critical-infrastructure/size-1_sole-proprietor_custom-exempt-meat-processor/step-10_P10_ai-governance/ai-risk-assessment.md`).
- **Real gap.** The universal P10 method has no fit check like P09 step 1 or P03's applicability check. The build guide lists P09 and P10 as steps every company takes, and its step table does not say they can end early.

**Primary sources.** No legal claim needs checking. The reviewer's description of SOC 2 scope (AICPA) was **not verified**, but the samples already agree that a non-service business does not seek a report.

**Verdict.** Partly agree, 0.70. The content is already conditional. The framing in the guide and the P10 method is not.

**Action.** Fix in this round (Fix C). We keep all 10 folders in every sample so sizes stay comparable side by side. A sample can still conclude "not applicable" inside a folder.

## 2.1 Premature System Security Plan

**Claim.** Writing the SSP (step 2) before the risk register (step 4) and gap analysis (step 5) inverts NIST SP 800-37 and ISO 27001.

**Evidence.**
- `docs/how-to-build-the-10-projects.md`, section 1: "Describe the system before judging it. The SSP (step 2) and cloud mapping (step 3) say what is in place."
- Every sample is an operating business documented "as found". 215 of 216 facts files describe the current policy state, often "No written security policies".
- The SSPs are not frozen at step 2. All 216 SSP folders cite P01, P03, P06, and P07. Example: `health-care/size-3_small_multi-specialty-practice/step-02_P02_system-security-plan/control-implementation.csv`, AC-1: "POL-02 (P06) replaces it and was approved 2026-08-31".
- The reviewer's proposed order puts the BIA after the risk register.

**Primary source (NIST SP 800-37 Rev. 2).**
- The RMF Prepare step includes the system-level risk assessment (Task P-14) and the definition of requirements, with "laws, executive orders, directives, regulations, or policies that apply to the system" as an input (Task P-15). These come before Select. Task S-4 (document controls in security and privacy plans) lists risk assessment results, the BIA, and organizational policies as inputs. **On this point the reviewer is right.**
- But: "the steps following the Prepare step can be carried out in a nonsequential order" (Chapter Two, p. 9-10). Task C-1 is "Document the characteristics of the system". S-4 and I-2 apply to existing systems in Operations/Maintenance, and I-2 updates the plans with "as-implemented" detail.
- Task P-14 lists "business impact analyses" as an input to the system risk assessment. That supports keeping the BIA first, against the proposed reorder.
- ISO/IEC 27001:2022 clause order: **not verified** (the standard is paywalled).

**Verdict.** Partly agree, 0.70. For a new system, RMF puts risk and requirements before the plan. For an existing system, the repo's as-is SSP followed by updates is defensible, but the guide does not say so clearly.

**Action.** No reorder. Rebuilding 2,160 deliverables would not improve the teaching. Fix in this round: rewrite the guide bullet (Fix D).

## 2.2 Policy generation detached from governance

**Claim.** Policies (P06) come after cloud mapping and the gap analysis. Move them to just after the gap analysis and risk register.

**Evidence.** In the build order, step 4 is P01 (risk register), step 5 is P03 (gap analysis), and step 6 is P06 (policies) (`PLAN.md` section 3). The proposed position is the current one. Cloud mapping (step 3) documents what is already deployed. It does not design a new architecture. The SSPs are updated to cite the approved policies (see 2.1).

**Primary source.** SP 800-37 Rev. 2 Task S-4 lists "organizational security, privacy, and SCRM policies" as an input to the plans. The repo meets this because the final SSP cites the P06 policies.

**Verdict.** Disagree, 0.75. The proposal matches the current order.

**Action.** No change. Fix D also states that the final SSP reflects the approved policies.

## 3.1 Size 1: separation of duties

**Claim.** AC-5, CM-3, and CA-2 cannot exist with one person. Add a compensating controls matrix for sizes 1-2.

**Evidence.**
- In the 36 size-1 `control-implementation.csv` files: AC-5 in 0, CA-2 in 0, CA-2(1) in 0, CM-3 in 1 (Planned), AU-9 in 1. Enterprise controls are not forced on size 1.
- Tailoring is explained in prose in 35 of 36 size-1 SSPs. Example: "tailored out because they assume staff, servers, software development, or a federal program" (`agriculture/size-1_sole-proprietor_crop-farm/step-02_P02_system-security-plan/system-security-plan.md`).
- All 36 size-1 P07 assessment plans state limited independence. Example: "Independence is limited ... POL-01 4.5 requires an outside reviewer at least every second year."
- At size 2: AC-5 appears in 8 of 36 SSPs, CM-3 in 17, CA-2 in 36.
- **Real gap.** There is no shared list that names the compensating control for each "needs a second person" control. Size-1 SSPs drop AC-5 and CA-2(1) silently at control level. Only a handful of size-1 files use the words "compensating control" for a specific control (example: an SA-11 and CM-3 row in the SaaS developer's P09 checklist).

**Primary source (NIST SP 800-53 Rev. 5, OSCAL catalog; baselines from `00_universal-framework/frameworks/sp800-53r5_controls.csv`).** AC-5, CM-3, CA-2(1), and CA-7(1) are in the Moderate baseline, not Low. The reviewer's labels are loose: base CA-2 needs an assessor and plan, not independence. Independence is CA-2(1), "Employ independent assessors". CM-3(g) lets the organization name its own change control element. It does not require a board.

**Verdict.** Partly agree, 0.75.

**Action.** Fix in this round: Fix E (one table in the build guide). Backlog: add explicit tailoring rows for AC-5, AU-9, CM-3, and CA-2(1) to the 36 size-1 `control-implementation.csv` files, with status "Not applicable (tailored)" and the compensating control.

## 3.2 Sizes 2-3: enterprise architecture drift

**Claim.** P04 imposes multi-account landing zones and dedicated SIEMs on SaaS-only businesses.

**Evidence.**
- The universal P04 method sets the tier first: "Sole Proprietorship and Micro are mostly SaaS. Small adds one IaaS/PaaS tenant. Mid-Market and above run multiple accounts" (`00_universal-framework/projects/step-03_P04_cloud-control-mapping/README.md`, step 1). `tier-project-scaling.csv` matches: t1 "SaaS tenants only (no IaaS)"; t4 is the first "Multi-account/subscription cloud environment".
- Grep of the P04 `.md` files: "landing zone" 0 at size 1, 0 at size 2, 1 at size 3. The size-3 hit is a data "Historian landing zone" (a storage area) in `utilities_energy-critical-infrastructure/size-3_small_gas-transmission-pipeline`, not an account structure. "SIEM" is 0 at sizes 1-2 and 2 at size 3: a payment processor (PCI logging) and a cloud hosting provider, which plausibly run one. Example from a micro sample: "The farm runs no servers and no IaaS tenant" (`agriculture/size-2_micro_crop-farm/.../cloud-architecture.md`).
- Size 3 is defined as hybrid with one cloud tenant (`tiers.csv`), so an IaaS tenant at size 3 is by design.

**Verdict.** Disagree, 0.85.

**Action.** No change.

## 3.3 Size 6: blast radius

**Claim.** A centralized identity provider lets an OT breach in one division reach PHI or PII in another. Use separate tenants per division.

**Evidence.**
- Typical size-6 design: "Corporate runs one landing zone per provider: identity federation from SYS-G1 ... Divisions get their own accounts" (`agriculture/size-6_multi-sector_crop-farm-plus-two-divisions/step-03_P04_cloud-control-mapping/cloud-architecture.md`; same pattern in `health-care/size-6_.../cloud-architecture.md`). So identity is shared and workloads are separated by account.
- The risk is named, not ignored. All 36 size-6 risk registers contain risks of lateral movement or of an incident spreading across divisions. Agriculture size 6, GR-01: ransomware "spreads from farm OT to the corporate cloud network and ERP". Its P04 says "the bridge from the cloud into farm OT is" the weak point and plans an OT DMZ (POAM-002).
- Separate tenants are used where a rule demands them. Example: a "Construction CUI enclave ... in a separate tenant of a government-community cloud offering with its own identity". 8 of 36 size-6 P04 files mention a separate tenant, identity, or account for some part of the group.
- **Real gap.** No sample states the shared versus separate identity decision as an explicit, reasoned choice, with what limits blast radius (division-scoped admin roles, PAM, conditional access, OT identities kept off the corporate directory).

**Primary source.** DFARS 252.204-7012(b)(2)(ii)(D) requires an external cloud holding covered defense information to meet FedRAMP Moderate-equivalent requirements. That is one real driver of a separate tenant. The reviewer's "corporate veil protection" rationale is **not verified**: we found no primary source tying IT tenancy to veil doctrine, and we do not adopt it.

**Verdict.** Partly agree, 0.60. Shared identity with per-division accounts is a common, defensible pattern, and the samples treat lateral movement as a top risk. A blanket "separate tenants" rule is not justified. A written decision is.

**Action.** Fix in this round: Fix F (method only). Backlog: add a short "Tenancy and identity decision" paragraph to the 36 size-6 `cloud-architecture.md` files.

## 4.1 (a) Custom-exempt meat processor

**Claim.** 9 CFR 303.1(a)(2) custom operations cannot sell meat. Applying CISA critical manufacturing frameworks confuses them with inspected plants.

**Evidence.**
- `agriculture_food-agriculture-critical-infrastructure/size-1_sole-proprietor_custom-exempt-meat-processor/00_company-facts.md`: "Custom exempt operation, not an official establishment ... Every package goes back to the animal's owner marked 'Not for Sale'". It sets "No binding federal cybersecurity rule applies" and uses NIST CSF 2.0 as a voluntary benchmark.
- Its P03 `gap-analysis.csv` has 106 rows labeled "NIST CSF 2.0 (voluntary benchmark)" and 17 FMIA custom exemption rows. 21 CFR Part 121, CIRCIA, and the USCG MTS rule are each one row marked not applicable. No CISA framework (for example the CPGs) is applied. The sample sits in the Food and Agriculture sector folder, not Critical Manufacturing.
- **Real gap.** The generated `README.md` lists industry defaults that this shop does not have: "Food defense plans", "Cold-chain and refrigeration controls (ammonia systems)", "Batch/recipe control systems (DCS/PLC)", "MES and ERP". The facts file says "No anhydrous ammonia on site". Source: `tools/build_scenarios.py`, lines 348-350, which print the vertical profile for every sample.

**Primary source.** 9 CFR 303.1(a)(2) (eCFR): the exemption covers custom preparation of an owner's livestock "exclusively for use in the household of such owner, by him and members of his household and his nonpaying guests and employees". The reviewer's reading is correct, and the sample already applies it.

**Verdict.** Partly agree, 0.75, on the README only. The analysis itself is correct.

**Action.** Fix in this round: Fix G.

## 4.1 (b) OT/ICS integrity in agriculture runbooks

**Claim.** Agriculture runbooks focus on IT credential theft and lack OT isolation playbooks.

**Evidence (12 P08 folders across the two agriculture verticals).**
- Size 4 in both verticals has a second, OT-only runbook: `agriculture/size-4_mid-market_crop-farm/step-08_P08_incident-response-runbook/ir-runbook-ot-integrity.md` ("Unauthorized or unexplained change to fertigation, irrigation, ethylene ripening, or cold-chain controls"; framework "NIST SP 800-82 Rev. 3 sections 6.3 to 6.5") and `agriculture_food-agriculture-critical-infrastructure/size-4_mid-market_meat-processor/.../ir-runbook-process-tampering.md`.
- OT steps at size 3 (`agriculture/size-3_small_diversified-crop-farm/.../ir-runbook.md`): "Switch each well pump and pivot to local or Hand control at its panel"; "Compare the PLC program with the farm-held approved backup (hash comparison)"; "Reload the PLC from the farm-held approved program". The size-4 OT runbook: "isolate the affected OT segment at the firewall".
- Even the one-person shop has physical safe-state steps: "Walk the cooler and freezer. Read both dial thermometers"; "If it differs, stop the cook, hold the product".
- Purdue/DMZ language appears at sizes 3-6. Sizes 1-2 have no SCADA, so there is none.

**Verdict.** Disagree, 0.85.

**Action.** No change.

## 4.2 Staffing: algorithmic bias compliance

**Claim.** Staffing P10 files use automated resume screening but do not operationalize NYC Local Law 144 bias audits or disparate impact testing.

**Evidence (`03_company-samples/admin-support-services/`).**
- Applicability is decided per size. Sizes 1-4 P10: "NYC Local Law 144 (N56-R08) | **No** | No NYC candidates or jobs" (size 1 adds a re-check trigger before work outside Florida). Each size 1-4 P03 has one not-applicable LL144 row.
- Sizes 5-6 apply it. Size 5 P10: "**Yes, for NYC jobs** | AI-001 ... bias audit within one year before use, public summary, and candidate notices", with an audit dated 2026-02-09. Size 5 P03 has separate rows G-164 (bias audit), G-165 (published summary), and G-166 (notices). Size 6 P03 G-138 records missed notices on NYC jobs (High).
- Disparate impact testing runs at sizes 2-6, whether or not LL144 applies. Each uses the four-fifths ratio "as an internal screening indicator only" plus a two-proportion z test (p < 0.05). Size 2 reports actual rates by sex (men 73.2%, women 56.3%).

**Primary sources.** NYC DCWP AEDT page (nyc.gov, fetched 2026-10-07): the law "prohibits employers and employment agencies from using an automated employment decision tool unless the tool has been subject to a bias audit within one year of the use of the tool, information about the bias audit is publicly available, and certain notices have been provided". 29 CFR 1607.4(D) (eCFR): a selection rate below "four-fifths (4/5) (or eighty percent)" of the highest group's rate "will generally be regarded ... as evidence of adverse impact". The DCWP rule text on geographic scope (rules.cityofnewyork.us returned 403) and the EEOC and OLC items the samples cite were **not verified** in this review.

**Verdict.** Disagree, 0.85.

**Action.** No change.

## 4.3 DIB: the NIST SP 800-171 Rev. 3 trap

**Claim.** The crosswalk assesses DIB companies against Rev. 3, which breaks SPRS scoring and CMMC alignment.

**Evidence.**
- Gap rows whose `regulation` column names SP 800-171, across all samples: 675 rows in the six DIB samples, all "NIST SP 800-171 Rev. 2". The other industries (construction, wholesale, IT, public administration, water, dams) also use Rev. 2 only. **Zero rows anywhere use Rev. 3 as the regulation.**
- Rev. 3 appears only in `crosswalk_source` (to borrow NIST's official mappings) and `pending_rule_change` ("Rev. 3 is not required for CMMC Level 2 (32 CFR 170.14(c)(3) fixes Rev. 2)").
- The rows carry `cmmc_id` and the DoD Assessment Methodology `point_value` used for SPRS.
- `manufacturing_defense-industrial-base-critical-infrastructure/size-3_small_aircraft-parts-manufacturer/step-05_P03_regulatory-gap-analysis/gap-analysis-report.md`: "Rev. 3 is not treated as a current obligation." 48 files cite 32 CFR 170.14(c)(3).

**Primary sources.** 32 CFR 170.14(c)(3): "The security requirements in CMMC Level 2 are identical to the requirements in NIST SP 800-171 R2." 32 CFR 170.2 incorporates by reference "Revision 2, February 2020 (includes updates as of January 28, 2021)". DFARS 252.204-7012(b)(2)(i) refers to SP 800-171 "in effect at the time the solicitation is issued or as authorized by the Contracting Officer". The DoD class deviation that keeps 7012 at Rev. 2 (2024-O0013) is **not verified**: acq.osd.mil failed TLS through the proxy. Note: CMMC Level 2 is fixed to Rev. 2 in regulation by incorporation by reference, so moving it to Rev. 3 needs rulemaking, not only a class deviation.

**Verdict.** Disagree, 0.95. The repository already does what the reviewer proposes.

**Action.** No change.

---

## Fixes for this round

Every fix is documentation or a one-row fact. No verdict, risk score, or count changes. After the edits, run `python3 tools/build_scenarios.py`, `python3 tools/build_explorer.py`, and `python3 tools/validate.py`.

- **A (1.1). README legal form.** In `tools/build_scenarios.py` `write_scenario()`: if the facts file has a `| Legal form | ... |` row, use it for the README "Legal form", and use the `| Ownership | ... |` row for "Ownership" if one exists. Add rows to three facts files:
  - `finance-insurance/size-3_small_community-bank/00_company-facts.md`: `| Legal form | National banking association, a body corporate (12 U.S.C. 24), wholly owned by a privately held bank holding company |` (its existing `| Ownership |` row then feeds the README).
  - `finance-insurance/size-2_micro_community-credit-union/00_company-facts.md`: `| Legal form | Federal credit union (member-owned, not-for-profit cooperative) |` and `| Ownership | Owned by its members, one member, one vote; no shareholders |`.
  - `utilities/size-2_micro_small-electric-cooperative/00_company-facts.md`: `| Legal form | Electric cooperative; nonprofit membership corporation (Fla. Stat. chapter 425) |` and the same Ownership row.
- **B (1.1). Control-approval and FOCI fact rows** (background facts; not scored in P03):
  - Bank size 3, new row "Change of control approvals": the holding company and the bank's place in it needed prior Federal Reserve approval (12 U.S.C. 1842(a)(1)-(2); 12 CFR 225.11(a)-(b)). Any person acquiring control of the holding company, including Cris Santos, gives the Federal Reserve 60 days' prior notice (12 U.S.C. 1817(j)(1); 12 CFR 225.41(a), (c)(1)). The OCC notice in 12 CFR 5.50(b) does not apply to a transaction needing BHC Act section 3 approval (5.50(c)(2)(iii)).
  - `utilities_nuclear-critical-infrastructure/size-4_mid-market_nuclear-power-plant/00_company-facts.md`, new row "License transfer and ownership": the PE acquisition was an indirect transfer of control that needed the NRC's prior written consent (10 CFR 50.80(a)), with the transferee's technical and financial qualifications (50.80(b)(1)(i)). Foreign ownership, control, or domination would bring in 10 CFR 50.38.
  - `manufacturing_defense-industrial-base-critical-infrastructure/size-5_enterprise_aircraft-parts-manufacturer/00_company-facts.md` and the size-6 sample, new row "FOCI status": not determined to be under FOCI (32 CFR 117.11(a)(1)); SF 328 completed for the entity eligibility determination and updated on significant changes (117.11(c)); at size 6, a consolidated corporate-family response as 117.11(c) allows.
- **C (1.2). Fit checks for P09 and P10.**
  - `docs/how-to-build-the-10-projects.md`, section 1: add a bullet to "Why this order works": "**Check fit before SOC 2 and AI work.** Step 9 opens by asking whether the company is a service organization. If it is not, the step is a questionnaire self-check plus a review of a key vendor's SOC 2 report, and it says no report will be sought. Every Sole Proprietor and Micro sample states this. Step 10 opens by listing the AI tools actually in use. If there are none, record an empty inventory with the date and stop."
  - `00_universal-framework/projects/step-10_P10_ai-governance/README.md`: add step 0, "Decide whether AI governance fits", with the same rule, and keep sizes 1-2 to the one-page screen from `tier-project-scaling.csv`.
- **D (2.1, 2.2). As-is SSP note.** Replace the "Describe the system before judging it" bullet in `docs/how-to-build-the-10-projects.md` with: "**Describe the system before judging it.** Every sample is an operating business. The SSP (step 2) and cloud mapping (step 3) record the system as found. This is the RMF Categorize task C-1 for an existing system. In the RMF Prepare step, a new system would get its risk assessment (P-14) and requirements (P-15) before controls are selected. Here, steps 4 to 7 add risks, gaps, policies, and test results, and the SSP is updated to the as-implemented state (NIST SP 800-37 Rev. 2, Tasks S-4 and I-2). That is why every sample's SSP cites P01, P03, P06, and P07. The BIA stays first because SP 800-37 lists it as an input to the system risk assessment (P-14)."
- **E (3.1). Compensating controls at sizes 1-2.** Add a short table after the "Teaching point" in `docs/how-to-build-the-10-projects.md` section 2.1:
  - AC-5 (Moderate): the platform enforces a second approval where it can (bank dual approval, payment holds), and an outside bookkeeper or CPA reviews statements each month.
  - AU-9: logs live where the owner cannot delete them (the SaaS provider's retained audit log or write-once storage).
  - CM-3 (Moderate): CM-3(g) lets the organization name its own change control element. Use a change log, a backup before each change, and an MSP or vendor check for high-risk changes.
  - CA-2(1) and CA-7(1) (Moderate): state limited independence in P07, use an outside reviewer at a set interval, and rely on vendor SOC 2 reports for inherited controls. Base CA-2 still applies as a self-assessment.
- **F (3.3). Tenancy decision in the P04 method.** In `00_universal-framework/projects/step-03_P04_cloud-control-mapping/README.md`, add to step 1: "Multi-Sector: record the tenancy and identity decision. Say whether divisions share the group identity provider with separate accounts, or get a separate tenant with their own identity. Use a separate tenant where a rule or contract requires its own boundary (for example, covered defense information in an external cloud must meet FedRAMP Moderate equivalency, DFARS 252.204-7012(b)(2)(ii)(D)). Name what limits blast radius: division-scoped administrator roles, privileged access management, conditional access, OT identities kept off the corporate directory, and one-way OT data paths."
- **G (4.1a). README industry defaults.** In `tools/build_scenarios.py` lines 348-350, change the heading to `## What the business handles (typical for this industry)` and add the line: "This sample's own systems and data are in `00_company-facts.md`. Items above that the company does not have are out of scope." Keep the heading prefix "## What the business handles", because `tools/build_explorer.py` (`glance()`, line 251) uses it to stop parsing the at-a-glance table.

## Backlog

1. **3.1:** add explicit tailoring rows (AC-5, AU-9, CM-3, CA-2(1)) with named compensating controls to the 36 size-1 `step-02_P02_system-security-plan/control-implementation.csv` files.
2. **3.3:** add a "Tenancy and identity decision" paragraph to the 36 size-6 `step-03_P04_cloud-control-mapping/cloud-architecture.md` files, following Fix F.
3. **1.1:** add "License transfer and ownership" rows to the nuclear size-5 and size-6 facts files (10 CFR 50.80 consent on any future change of control).
4. **4.3:** re-verify DFARS class deviation 2024-O0013 on acq.osd.mil when reachable, and add it to `00_universal-framework/sources/source-register.csv` if confirmed.
5. **2.1:** check the ISO/IEC 27001:2022 clause order against a licensed copy before citing ISO in the build guide.

## Not adopted

- Reordering the 10 steps (2.1, 2.2). The current order matches RMF for existing systems once Fix D is in. The proposed order would put the BIA after the risk register, against SP 800-37 Task P-14.
- Separate tenants for every size-6 division (3.3), and the corporate-veil rationale.
- Turning P09 and P10 into optional folders (1.2). Every sample keeps all 10 so sizes compare side by side. A folder can conclude "not applicable".
- Trusts or voting proxies for owner-run samples (1.1). U.S. law allows a single U.S. owner with the approvals now recorded.
