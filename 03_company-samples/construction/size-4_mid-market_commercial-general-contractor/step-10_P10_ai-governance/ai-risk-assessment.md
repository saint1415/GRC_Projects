# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial and institutional building general contractor) |
| Tier / Vertical | Mid-Market / Construction |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry use case, AI-001 (AI estimating and bid assistant), gets the deepest review in section 3.1 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001 and AI-003 |
| Assessors / date | vCISO and Security Manager (security), General Counsel (legal), each business owner, and the GRC analyst (risk method), 2026-08-24 to 2026-09-12 |
| Decision | Chief Operating Officer, 2026-09-17; High-tier decisions (AI-005, AI-006) noted by the CEO the same day |

## 1. Summary
All six AI uses were adopted by departments without a security, privacy, or bias review (gap 11). None is out of control, but each needs conditions:
- **AI-001, estimating:** works well for new construction, poorly for renovations, and its subcontractor ranking pushes first-time bidders down. It must never receive CUI.
- **AI-002, jobsite video analytics:** went live with no written notice to workers and no retention limit.
- **AI-003, the productivity suite assistant:** was switched on for every user in 2026-04 and surfaces files that were overshared long before AI arrived.
- **AI-004, invoice capture:** could write extracted remittance details into payment data. That path is the business email compromise risk in a new form.
- **AI-005, MBSS alarm triage:** could suppress a real alarm at a hospital or school.
- **AI-006, applicant screening:** ranked applicants with a vendor default and no adverse impact analysis.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | AI estimating and bid assistant | Medium | Approve with conditions |
| AI-002 | Jobsite safety video analytics | Medium | Approve with conditions |
| AI-003 | Productivity suite generative AI assistant | Medium | Restrict to reviewed groups until conditions are met |
| AI-004 | Accounts payable invoice capture and coding | Medium | Approve with conditions |
| AI-005 | MBSS alarm triage | High | Approve with conditions |
| AI-006 | Applicant screening | High | Suspend ranking until conditions are met |

Tiers: 2 High, 4 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the vCISO, chairing the AI review group. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.17: AI tools must be approved through the AI review process; no AI tool may receive CUI or change payment data.
  - POL-04 4.10: no CUI in any AI tool; FCI, Restricted, and Confidential data only in approved tools with terms that bar training on company data.
  - POL-05 4.10: approved tools only; never paste federal drawings, bid documents, pricing, client security details, or personal information into an unapproved tool.
  - STD-05 AI use standard: due 2026-12-31 (POAM-021).
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions. AI-006 ranking is listed as suspended. Public chatbots are blocked for FCI, Restricted, and Confidential data.
- **Purchasing gate:** no purchase order or vendor feature activation for an AI capability without an intake ticket (from 2026-10-01). Several of these tools arrived as features switched on inside existing products, so the IT Director also reviews vendor release notes monthly for new AI features.

### 2.1 AI review process (scaled for a mid-market company)
The company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page intake: purpose, users, data, vendor, decisions affected, whether it touches FCI, CUI, payment data, client systems, or people decisions | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; CUI and payment-data checks; purchasing gate | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, contract terms (no training on company data, retention, incident notice), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan and counsel review | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, Security Manager, General Counsel, HR Director, and the requesting director), meeting monthly for 30 minutes. High: the group recommends, the COO decides, and the CEO is informed | As listed | Monthly |
| 5. Monitor | Owners report the section 4 metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type (especially FCI or CUI), new population, or a safety, payment, or discrimination complaint | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case below.

## 3. MAP
| Item | AI-001 Estimating | AI-002 Video analytics | AI-003 Suite assistant | AI-004 Invoice capture | AI-005 Alarm triage | AI-006 Applicant screening |
|---|---|---|---|---|---|---|
| Purpose | Takeoff, pricing, bid leveling, proposal drafting | PPE and exclusion zone alerts | Draft and summarize from the user's own files | Extract invoice fields and propose job-cost coding | Classify, group, and suppress client alarms | Rank applicants for interviews |
| Users | 18 preconstruction and estimating staff | 18 safety staff and 22 superintendents | Was all 610 users; now 120 reviewed users | 6 accounts payable staff | MBSS monitoring staff | 10 HR and recruiting staff |
| Affected people | Owners (price), subcontractors (selection), the company (fixed-price exposure) | Workers and visitors at 14 jobsites | Anyone whose data sits in shared files | Subcontractors and suppliers (payment) | Occupants of 38 client buildings | About 2,400 applicants a year |
| Data | Drawings (FCI on federal work), costs, bids | Video (no audio) | Email, files, chat (FCI, bid data, HR data) | Invoices, remittance details | Alarm and event streams | Applications and resumes |
| Build or buy | Buy (SaaS) | Configure (vendor feature) | Configure (suite feature) | Buy (SaaS) | Configure (RMM feature) | Configure (HR SaaS feature) |
| Generative AI? | Yes | No | Yes | Partly (field extraction) | No | No |
| Tier | Medium | Medium | Medium | Medium | High | High |

### 3.1 AI-001: AI estimating and bid assistant (registry use case)
**Purpose and intended use:** speed up estimating through (1) quantity takeoff from drawings, (2) unit pricing from the company's historical cost database and the vendor's market data, (3) subcontractor bid leveling (normalizing scope, flagging exclusions, ranking bids), and (4) drafting proposal narratives. Not intended for automatic bid submission, automatic subcontract award, structural or life-safety quantities, or any hiring or crew assignment.

**Is the data FCI or CUI?** It depends on the stage.
- Public solicitation documents posted for all bidders are not FCI. FAR 52.204-21(a) excludes "information provided by the Government to the public".
- Drawings and change-order packages on an **awarded** federal contract are FCI. The tool is listed in the SSP as an external service for FCI (P02 section 8), under enterprise terms signed 2026-02.
- **CUI is prohibited.** A 2026-08 search of the tool's project library by the GRC analyst found no CUI-marked files. Since 2026-09-01, uploads of files carrying CUI markings are blocked. Any CUI found in the tool would be handled under the CUI runbook (P08).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** for FCI | The company must verify and control connections to and use of external information systems. The enterprise terms, single sign-on, and listing in the SSP meet this |
| DFARS 252.204-7012 and POL-04 4.10 | **Yes**, as a prohibition | The vendor is not FedRAMP authorized; CUI in the tool would fail 252.204-7012(b)(2)(ii)(D) |
| DFARS 252.204-7021(d)(2) | **Yes** once a contract requires CMMC | FCI or CUI may be processed only on systems with the required CMMC status. Before the follow-on MATOC, counsel confirms whether that contract's FCI may enter the tool, or uploads are blocked for it |
| FAR 52.203-2, Certificate of Independent Price Determination | **Yes** on federal bids | The offeror certifies prices were arrived at independently, without consultation with competitors about prices or "the methods or factors used to calculate the prices". A vendor feature that pools competitors' pricing into shared "market" suggestions puts that certification at risk |
| FAR 15.403-4 (certified cost or pricing data) | **When required** | For negotiated actions above the threshold, the company certifies data are accurate, complete, and current. AI-derived figures need traceable sources |
| FAR 52.219-8 and 52.219-9 | **Yes** on federal jobs | The company is not small, so its larger federal contracts carry subcontracting plans. A ranking model that disfavors small businesses works against the plan goals and the 52.219-8 policy of "maximum practicable opportunity" |
| Sherman Act Section 1 (15 U.S.C. 1) | Indirectly | Counsel reviews any vendor feature that shares or aggregates pricing across contractors |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims; the claims relied on are kept in the procurement file |
| State AI laws (for example Colorado SB26-189) | No | The company operates in Florida, and AI-001 makes no consequential decision about individuals |

### 3.2 AI-002: worker notice and federal sites
- The cameras are rented with the analytics feature switched on. Workers were never told in writing that video is analyzed, and the vendor kept alert snapshots for 1 year by default.
- Audio is disabled. If audio were ever enabled, Fla. Stat. 934.03(2)(d) makes interception of oral communications lawful only with the prior consent of all parties, which a jobsite cannot practically get. Audio therefore stays off by contract.
- Using alerts for discipline would turn this into an employment use and a High tier. It is prohibited. Counsel also reviews the program under the National Labor Relations Act, because monitoring can chill protected activity.
- **Federal jobs.** Camera hardware on FC-1 to FC-4 must pass the Section 889 check. The FC-2 finding in P07 involved rented jobsite cameras, so the analytics vendor confirmed in writing on 2026-09-02 that its cameras are not covered equipment. No analytics cameras are placed at FC-3 or FC-4 installation sites without the Contracting Officer's written approval, and no camera may view the FC-4 CUI room.

### 3.3 AI-003: oversharing, not the model, is the risk
The assistant can only read what the user can already open. The problem is what users can already open: the review found 41 project sites and 6 finance folders shared with "everyone in the company", including bid summaries and 2 folders with certified payroll exports. The assistant made those findable in seconds. Access was restricted to 120 reviewed users on 2026-09-10 while permissions are cleaned up (P01 R-029).

### 3.4 AI-004: the payment path
The tool extracted remittance details from invoices and, until 2026-09-15, could write them to the vendor master as a "suggested update" that an accounts payable clerk could accept with one click. That bypassed the call-back rule (POL-01 4.8). Write access to bank fields is now removed. Any invoice whose remittance details differ from the vendor master goes to the Controller's call-back queue (P01 R-033).

### 3.5 AI-005: alarm suppression at client sites
The vendor's model learned to suppress repeated "door held open" events. At 2 hospital sites it also suppressed 3 "door forced" events at a pharmacy door during a 2026-06 controller fault; a technician caught them in a routine health check the next day. Critical alarm classes can no longer be suppressed (since 2026-09-11). This use affects physical security at hospitals and schools, so it is High tier.

### 3.6 AI-006: employment decisions
The applicant tracking vendor switched ranking on by default in 2025. Recruiters used the top 20 ranked applicants as the interview pool for craft roles. This makes the tool a substantial factor in an employment decision.
- **Title VII of the Civil Rights Act of 1964** prohibits employment practices with an unjustified disparate impact (42 U.S.C. 2000e-2).
- **The Uniform Guidelines on Employee Selection Procedures** treat a selection rate for any race, sex, or ethnic group that is less than four-fifths of the rate for the group with the highest rate as generally evidence of adverse impact (29 CFR 1607.4(D)). The rule also says smaller differences can be adverse impact when statistically and practically significant, and larger differences may not be when based on small numbers.
- Age is not covered by the Uniform Guidelines but is protected by the **ADEA** (29 U.S.C. 621 et seq.); disability by the **ADA** (42 U.S.C. 12112).

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Takeoff quantity error by trade against the estimator's final takeoff on 12 completed bids | Within 5% for concrete, steel, drywall; 10% for other trades | Concrete 3%, drywall 4%, steel 4%; MEP fixture counts 13%; renovations average 11% against 4% for new construction | **No** for MEP and renovations |
| AI-001 | Fair, harmful bias managed | Recommendation rate for each subcontractor group divided by the rate for all others, among bids within 5% of the low price (certified small, small disadvantaged, women-owned, HUBZone, service-disabled veteran-owned, and first-time bidders). Flag any ratio below 0.8. This borrows the employment heuristic; it is not a legal threshold for subcontracting | No ratio below 0.8 | Certified small business groups 0.86 to 0.97; **first-time bidders 0.58** | **No** |
| AI-001 | Privacy-enhanced (confidentiality) | Enterprise terms: no training on company data, deletion on request, US data location, cross-customer pricing features off | All true | All true since 2026-02; "market pricing insights" was on until 2026-08-30 | Yes (fixed) |
| AI-001 | Secure and resilient | Single sign-on with MFA; CUI marking block on upload; vendor SOC 2 Type 2 (VEN-10) | All true | All true since 2026-09-01 | Yes |
| AI-001 | Accountable and transparent | Each AI-derived figure in a federal estimate tagged with its source | 100% of federal estimates | 4 of 9 federal estimates tagged | **No** |
| AI-002 | Privacy-enhanced | Written worker notice at every site; retention of alert snapshots 30 days | Both | Neither | **No** |
| AI-002 | Valid and reliable | False alert rate from 200 sampled alerts | Below 20% | 27% (shadows and reflective vests) | **No** (tuning) |
| AI-002 | Accountable and transparent | Alerts used only for coaching; no alert in any disciplinary file | 0 | 2 alerts found in disciplinary files at one jobsite | **No** |
| AI-003 | Privacy-enhanced | Sites and folders shared with everyone that contain Restricted or bid data | 0 | 47 found (41 project sites, 6 finance folders) | **No** |
| AI-003 | Secure and resilient | Assistant cannot reach the CPE; CUI markings blocked by data loss prevention in the suite | Both | CPE unreachable (separate tenant); data loss prevention rule due 2026-12-31 | Partial |
| AI-004 | Valid and reliable | Field extraction accuracy on 100 invoices (amount, job, cost code, remittance) | 98% amount; 95% coding | 99% amount; 93% coding | Partial |
| AI-004 | Safe (payment integrity) | Tool cannot write bank fields; changed remittance routed to call-back | Both | Both since 2026-09-15 | Yes |
| AI-005 | Safe | Critical alarm classes suppressed | 0 | 3 in 2026-06 (before the fix); 0 since 2026-09-11 | Yes (fixed) |
| AI-005 | Valid and reliable | Nuisance alarm reduction without missed true alarms, from a weekly sample of 50 suppressed events | 0 true alarms suppressed | 1 true "door held" at a school in 4 weekly samples | **No** |
| AI-005 | Explainable and interpretable | Technicians can see why an event was suppressed | Available | Rule reason shown; model score not explained | Partial |
| AI-006 | Fair, harmful bias managed | Selection rate (ranked into the interview pool) by sex and by race and ethnicity, 2026-01 to 2026-07, 1,380 applicants; age band (40 and over against under 40) tested separately | No ratio below 0.8 (29 CFR 1607.4(D)), with a significance test | Women 0.71 for craft roles (small numbers, 68 women applicants); applicants 40 and over 0.74; race and ethnicity groups 0.84 to 1.0 | **No** |
| AI-006 | Accountable and transparent | Vendor validation evidence (job-relatedness) and a list of model inputs | Both provided | Vendor provided input list only; no validation study for craft roles | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts only. Estimators verify every major trade takeoff; MEP and renovation takeoffs are done manually until the tool meets the thresholds for two quarters. Bid leveling is advisory, and the estimator records the reason for each selection. The Director of Preconstruction approves every bid and signs any federal price certification only after confirming no pooled pricing was used.
- **AI-002:** the safety manager reviews each alert before talking to a worker; alerts are coaching tools only.
- **AI-003:** users review every draft; the assistant cannot send or share on its own.
- **AI-004:** accounts payable approves every invoice; bank changes only through the Controller's call-back queue.
- **AI-005:** critical classes never suppressed; technicians review the suppressed queue each shift.
- **AI-006:** ranking off. If re-enabled, it is advisory only, every qualified applicant is reviewed by a recruiter, and rejections have recorded reasons.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. High-tier items (AI-005, AI-006) also get a quarterly deep dive with the COO. Results feed the risk register (P01 R-029 to R-034).

**Incident handling:**
- A security incident at an AI vendor, or CUI found in an AI tool, follows P08 (`ir-runbook-cui-incident.md` for CUI).
- A diverted payment involving AI-004 follows the business email compromise runbook (P08 `ir-runbook.md`).
- A missed alarm involving AI-005 is reviewed with the client under the MBSS agreement and logged for the SOC 2 examination (P09).
- A discrimination complaint involving AI-006 goes to General Counsel and the HR Director.

**Decommissioning criteria:**
- AI-001: stop federal uploads if the vendor changes data-use terms or turns on cross-customer pricing that cannot be disabled; stop use if accuracy thresholds are missed after two quarters.
- AI-002: switch off at any site where written notice is not posted by 2026-10-31.
- AI-003: switch off for any group whose oversharing is not cleaned up by 2026-11-30.
- AI-005: revert to rule-based filtering if a true critical alarm is suppressed again.
- AI-006: keep ranking off permanently if the vendor cannot provide validation evidence, or if the adverse impact analysis shows ratios below 0.8 that cannot be explained by job-related factors.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | CUI upload block (done 2026-09-01); market pricing feature off with counsel's written confirmation for federal bids (done 2026-08-30); manual MEP and renovation takeoffs now; missing performance history scored as neutral and bias check rerun (2026-10-31); source tagging for federal estimates (2026-11-30); counsel decision on FCI from any contract with DFARS 252.204-7021 before the follow-on MATOC bid | COO, 2026-09-17 |
| AI-002 | **Approve with conditions** | Written notice at every site and in onboarding; 30-day snapshot retention; remove the 2 alerts from disciplinary files; no cameras viewing the FC-4 CUI room or at installation sites without approval (2026-10-31) | COO, 2026-09-17 |
| AI-003 | **Restrict** to 120 reviewed users | Oversharing clean-up and sensitivity labels (2026-11-30); data loss prevention rule for CUI markings (2026-12-31); user guidance in awareness training (POAM-007) | COO, 2026-09-17 |
| AI-004 | **Approve with conditions** | Bank-field write access removed (done 2026-09-15); coding accuracy to 95% or second review of coding (2026-12-31) | CFO and COO, 2026-09-17 |
| AI-005 | **Approve with conditions** | Critical classes never suppressed (done 2026-09-11); weekly review of suppressed events and rules; explanation of model scores from the vendor (2026-12-31); disclosure to MBSS clients in the SOC 2 system description | COO, 2026-09-17; noted by the CEO |
| AI-006 | **Suspend ranking** | Adverse impact analysis with counsel, including significance testing (2026-10-31); vendor validation evidence for each job family; ranking may return only on the AI review group's recommendation and the COO's approval | COO, 2026-09-17; noted by the CEO |

The conditions are tracked as POAM-021 in P07 and in the risk register (P01 R-029 to R-034). The AI review group holds its first monthly meeting on 2026-10-06.
