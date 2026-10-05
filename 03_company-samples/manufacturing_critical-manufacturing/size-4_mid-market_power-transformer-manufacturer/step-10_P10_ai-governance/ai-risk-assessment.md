# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Mid-Market / Critical Manufacturing |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. AI-001 demand forecasting and AI-002 predictive maintenance are the registry use cases for this vertical; AI-003 to AI-005 were found in this assessment |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-004 |
| Assessors / date | vCISO (chair), Security Manager, Director of Digital Services, General Counsel, HR Director, and the Maintenance Manager, 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
Three of the five AI uses started without any security, legal, or risk review (gap 11): the AI-002 pilot, the AI-005 match score that HR turned on in an existing system, and staff use of personal generative AI accounts, which AI-004 is meant to replace. None of the tools controls plant equipment. Two need firm conditions:
- **AI-003, FMS condition analytics,** is the company's own model, and utilities act on its advisories. It misses more faults on transformers made by other manufacturers and on units older than 25 years, and the advisories do not say so.
- **AI-005, the applicant match score,** shows an adverse impact indicator for Hispanic applicants (selection-rate ratio 0.74, below the four-fifths ratio in 29 CFR 1607.4(D)). It was switched off on 2026-09-15.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Demand forecasting | Medium | Approve with conditions |
| AI-002 | Predictive maintenance (Plant 1 pilot) | Medium | Continue pilot with conditions; no Plant 2 rollout yet |
| AI-003 | FMS transformer condition analytics | High | Approve with conditions; disclosure and change control required |
| AI-004 | Enterprise generative AI assistant | Medium | Approve expansion with conditions |
| AI-005 | Applicant match score | High | **Do not use**; stays off pending an adverse impact study |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the vCISO chairs the AI review group; each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.15: AI tools and AI features in existing software must be approved before use.
  - POL-04 4.3 and 4.5: no Restricted data or FCI in unapproved AI tools.
  - POL-05 4.8: approved tools only; human review of AI output used in designs, quotes, customer documents, or decisions about people.
  - STD-05 AI use standard: due 2026-12-31 (POAM-021).
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-004 with their conditions. AI-005 is listed as **not approved**.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team wanting an AI tool, or an AI feature turned on in existing software, submits a one-page intake: purpose, users, data, vendor, decisions affected, plant or customer impact | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing and feature-change gate (no purchase order or feature activation without approval) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, legal (data terms, no-training clause), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, with a bias and performance plan; OT review by the Director of Manufacturing Engineering if plant data or equipment is involved | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, Director of Digital Services, General Counsel, Security Manager; HR Director when people are affected; Director of Manufacturing Engineering when OT is involved), monthly. High: the group recommends, the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report the agreed metrics monthly; High-tier use cases also get a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data source, new population or plant, or a safety or customer event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. **Re-tier triggers** are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Forecasting | AI-002 Predictive maintenance | AI-003 FMS analytics | AI-004 Generative assistant | AI-005 Match score |
|---|---|---|---|---|---|
| Purpose | Monthly demand by product family 3-12 months ahead; storm slot proposals | Early warning of oven and winder faults | Fault type and urgency for utility transformers | Drafting, summarizing, searching company documents | Rank applicants for production roles |
| Users | 4 planners; Supply Chain | Maintenance Manager and 14 Plant 1 technicians | 4 reliability engineers; 260 utility portal users | 120 pilot users | 5 recruiters |
| Affected parties | About 120 utility customers (slots and lead times) | Maintenance staff and oven operators | 14 utilities and the grid assets they operate | Customers whose documents are drafted | About 2,000 applicants a year |
| Data | ERP order history (includes FCI); weather outlooks | About 220 historian tags from the Plant 1 DMZ replica | Utility TMU data; company test and teardown records | Company documents in the tenant | Resumes and application answers |
| Build or buy | Build | Buy (SaaS) | Build | Buy (enterprise license) | Configure (vendor feature) |
| Generative AI? | No | No | No | Yes | No (vendor ranking model) |
| Re-tier trigger | Automatic slot allocation without approval | Used to extend or skip preventive maintenance (to High) | Auto-publishing Urgent alerts without review | Use in decisions about people (to High) | Any re-enablement (stays High) |

**Laws and rules considered:**
| Rule | Use case | How it applies |
|---|---|---|
| Title VII (42 U.S.C. 2000e-2) and the Uniform Guidelines on Employee Selection Procedures (29 CFR Part 1607) | AI-005 | A selection procedure with adverse impact on a race, sex, or ethnic group must be job-related. 29 CFR 1607.4(D) says a selection rate for any group below four-fifths of the rate for the highest group "will generally be regarded by the Federal enforcement agencies as evidence of adverse impact." 1607.4(A) asks users to keep records of impact by group. The company uses the ratio as an internal indicator, not a safe harbor |
| FAR 52.204-21 | AI-001, AI-004 | FCI may be processed only on covered contractor information systems; the company's cloud account and productivity tenant are in scope (P03 G-107) |
| FTC Act Section 5 | AI-002, AI-003 | Marketing and vendor claims about accuracy must be substantiated. The FMS brochure claim that AI-003 "detects developing faults months in advance" needs evidence by transformer population |
| FMS subscription agreements and utility addenda | AI-003 | Confidentiality of utility data; where the FMS is a supplied service, incident and vulnerability terms apply to the model and its pipeline (P08 runbook 2) |
| Fla. Stat. 501.171 | AI-005 | Applicant records are personal information for breach notice |
| State consequential-decision AI laws (for example Colorado SB26-189) | AI-005 | The company hires only in Florida. This assessment did not identify a Florida statute specific to AI in hiring; Florida AI law was not researched further. Counsel rechecks before any re-enablement |
| Sector AI rules for critical manufacturing | All | None identified in the vertical profile |

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026 data) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Mean absolute percentage error, 3-month horizon | Under 15% overall | 14% | Yes |
| AI-001 | Fair, harmful bias managed | Error by customer segment (investor-owned, municipal, cooperative, developer) | No segment more than 5 points above the best | Investor-owned 11%, municipal 19%, cooperative 22%, developer 15% | **No** |
| AI-002 | Valid and reliable | Failure events flagged at least 48 hours ahead (pilot 2026-04 to 2026-08) | At least 70% | 7 of 9 (78%) | Yes |
| AI-002 | Safe | False alerts per month | 15 or fewer | 12 on average | Yes |
| AI-002 | Secure and resilient | Connector is outbound-only from the OT DMZ replica; no path to plant zones | All true | All true (P07 SC-7 Plant 1 test) | Yes |
| AI-003 | Valid and reliable | Recall on teardown-confirmed faults, 2024-2026 | At least 85% overall and in every subgroup | 41 of 46 (89%) overall | Yes overall |
| AI-003 | Fair, harmful bias managed (performance by transformer population) | Recall by manufacturer and by age band | At least 85% in every subgroup | Company-built 33 of 35 (94%); other manufacturers 8 of 11 (73%); under 10 years 12 of 12; 10-25 years 21 of 23 (91%); over 25 years 8 of 11 (73%) | **No** |
| AI-003 | Safe | Urgent alerts not confirmed (false urgent rate) | Under 25% | 14 of 78 (18%) | Yes |
| AI-003 | Accountable and transparent | Advisories state model limits and subgroup performance | Stated | General limits stated; subgroup gaps not stated | **No** |
| AI-003 | Secure and resilient | Model versions registered; changes approved; ingestion certificates revocable | All true | Registry since 2026-06; no change approval; no revocation checking | **No** |
| AI-003 | Explainable and interpretable | Each advisory shows the gas ratios, trend chart, and contributing features | Available | Available | Yes |
| AI-004 | Privacy-enhanced | Contract prohibits training on company data; data stays in the tenant | Both | Both | Yes |
| AI-004 | Valid and reliable (AI 600-1 confabulation) | 20 sampled engineering answers checked by a senior engineer | No numerical errors used without review | 3 of 20 contained numerical errors; none reached a design because reviewers caught them | Partial |
| AI-004 | Secure (AI 600-1 information security) | Design files pasted into personal AI accounts (data loss prevention detections, July 2026) | 0 | 14 detections, all on personal mobile devices outside the web filter | **No** |
| AI-005 | Fair, harmful bias managed | Selection-rate ratio at the "advanced to interview" step, 2026-05-01 to 2026-08-31, 2,140 applicants (78% self-identified) | At least 0.80 for every group (29 CFR 1607.4(D) indicator), with a significance test | Sex: women 21.0% vs men 24.1% (0.87). Race and ethnicity: White 25.3%; Black 22.4% (0.89); Asian 23.0% (0.91); **Hispanic 18.7% (0.74)**. Significance not yet tested; the vendor supplied no adverse impact data | **No** |
| AI-005 | Accountable and transparent | Applicants told that AI ranks applications | Notice given | No notice | **No** |

**AI-005 interpretation.** The ratio is measured at the step where recruiters chose whom to interview, so recruiter decisions also affect it. That is why the result is treated as an indicator that requires a study, not a finding of discrimination. The feature ranked resumes lower when work history was outside the United States or listed Spanish-language certifications, which is a plausible mechanism and is part of the study scope.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** planners approve every monthly plan; the minimum storm-slot rule by customer segment overrides the forecast.
- **AI-002:** the Maintenance Manager decides every action; preventive maintenance intervals do not change on the model's advice.
- **AI-003:** a reliability engineer reviews every Urgent alert within 4 hours before release; from 2026-11-30 engineers also review every Watch advisory on transformers made by other manufacturers or older than 25 years; utilities make all operating decisions.
- **AI-004:** a qualified person reviews any output used in a design, quote, customer document, or decision about a person.
- **AI-005:** off. Recruiters review all applicants in date order.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. AI-003 also gets a quarterly validation against new teardown findings. Results feed the risk register (P01 R-014, R-028 to R-031).

**Incident handling:**
- A security incident in the FMS model or pipeline follows P08 runbook 2 (product or service compromise), including subscriber and addendum notices.
- A missed fault that a subscriber reports goes to the Director of Digital Services and the General Counsel within 1 business day and is reviewed as a quality event.
- AI vendor incidents follow P08 and the vendor's contract terms.

**Decommissioning criteria:**
- AI-001: revert to planner-only forecasts if segment error gaps persist for 2 quarters after correction.
- AI-002: end the pilot if recall falls below 70% for 2 quarters.
- AI-003: suspend automated Watch advisories for any subgroup whose recall stays below 85% for 2 quarters after retraining; Urgent review continues.
- AI-004: suspend for any user group with repeated data loss prevention detections.
- AI-005: stays off unless a study shows no adverse impact or establishes job-relatedness, and a High-tier review approves it.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Segment correction and monthly segment error report (2026-12-31); storm-slot minimums reviewed each May | COO, 2026-09-15 |
| AI-002 | **Continue pilot with conditions** | No change to preventive maintenance intervals; no Plant 2 rollout until its OT DMZ exists (2027-06-30); vendor security terms at renewal | COO, 2026-09-15 |
| AI-003 | **Approve with conditions** | Advisories state subgroup performance (2026-11-30); added engineer review for other-manufacturer and older units (2026-11-30); marketing claim revised (2026-10-31); change control for model updates (2027-02-28, POAM-019); certificate revocation checking (2027-03-31); quarterly validation | COO, 2026-09-15; noted by the CEO |
| AI-004 | **Approve expansion to 300 users with conditions** | Training before access; data loss prevention on managed mobile devices (2026-12-31); quarterly confabulation sample | COO, 2026-09-15 |
| AI-005 | **Do not use** | Feature stays off with a feature-change alert in the HR system; any proposal to re-enable needs a High-tier review, an adverse impact study by the vendor and an outside expert under 29 CFR 1607.4, applicant notice, and human review of every application; decision point 2027-03-31 | COO, 2026-09-15; noted by the CEO |

The conditions are tracked as POAM-021 (AI governance) and POAM-019 (AI-003 change control) in P07, and in the risk register (P01 R-014, R-028 to R-031). The AI review group holds its first monthly meeting on 2026-10-06.
