# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Mid-Market / Information Technology |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry default use case, AI-driven security operations (alert triage), is AI-001 and gets the deepest review |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-002, and AI-003 |
| Assessors / date | Director of Security and the Security Operations Manager (security), General Counsel (legal), HR Director (AI-005), VP Platform Engineering (AI-004), with the GRC Manager, 2026-08-24 to 2026-09-11 |
| Decision | Chief Technology Officer, 2026-09-22; High-tier decisions noted by the CEO |

## 1. Summary
All five tools went into use without a security, legal, or bias review (gap 11 in `../00_company-facts.md`). Two need firm conditions before they continue:
- **AI-001, SIEM alert triage:** auto-closed 68% of commercial-partition alerts in July 2026 with no human review, including privileged-access alerts. It decides which security events nobody looks at, on a platform that hosts federal agencies and 38 banks.
- **AI-005, resume screening:** ranks applicants with an undisclosed vendor model and no adverse impact testing. Employment is a consequential decision under the repository rubric and under several state laws.

| ID | Use case | Risk tier | Generative AI? | Decision |
|---|---|---|---|---|
| AI-001 | AI-driven security operations (alert triage) | High | Yes (summaries) | Approve with conditions; auto-close limited by 2026-10-15 |
| AI-002 | Coding assistant | Medium | Yes | Approve with conditions |
| AI-003 | Support reply assistant | Medium | Yes | Approve with conditions |
| AI-004 | Hardware failure and capacity forecasting | Medium | No | Approve with conditions |
| AI-005 | Resume screening pilot | High | No (ranking model) | **Paused** 2026-09-22; restart only after a passed bias review |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Director of Security, with the General Counsel for legal review. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 section 4.17: AI tools that process customer data, act on security alerts, write production code, or support employment decisions must be approved before use.
  - POL-03 section 4.12: AI triage must not close privileged-access or tooling alerts without human review.
  - POL-04 section 4.2 and the classification table: no Federal data in AI tools that are not approved for it.
  - POL-05 section 4.6: approved tools only; human review of outputs before they reach customers, code, or hiring decisions.
  - STD-10 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the GRC Manager on the intranet, with each tool's conditions. AI settings in vendor products (SIEM, ITSM, applicant tracking) may change only through the change process.

### 2.1 Lightweight AI governance process
A 600-person company does not need a standing AI committee with a large charter. It needs a reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team that wants an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data (including whether Federal data is involved), vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The GRC Manager assigns a provisional tier with the rubric and checks the purchasing gate; feature toggles in SaaS tools are checked in the change process | GRC Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, legal (data use, retention, no training on company data), and the business owner. **High:** full MAP and MEASURE assessment like this one, with a bias plan where people are affected and a FedRAMP boundary check where the government partition is affected | Director of Security; General Counsel; owner | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: GRC Manager. Medium: the **AI review group** (Director of Security, General Counsel, GRC Manager, HR Director when people are affected), meeting monthly. High: the AI review group recommends, the CTO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report the section 4 metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type (for example management-plane logs for AI-001), new population, or an incident | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`.

## 3. MAP
| Item | AI-001 Alert triage | AI-002 Coding assistant | AI-003 Support replies | AI-004 Forecasting | AI-005 Resume screening |
|---|---|---|---|---|---|
| Purpose | Score, summarize, group, and auto-close alerts | Code completion and chat | Draft ticket answers | Predict hardware failures and capacity | Rank applicants and suggest shortlists |
| Users | SOC (6 analysts), MDR partner | About 70 engineers | 118 NOC and support staff | Platform engineers | 4 recruiters |
| Affected people | All 2,300 customers (a missed attack); employees (user-behavior alerts) | Customers who deploy templates and use the portal | Customers who receive answers | Customers (availability) | Applicants (about 1,900 a year) |
| Data | Security logs with user IDs and tenant names | Source code; prompts | Ticket text with customer details | Telemetry only | Resumes and application answers |
| Build or buy | Configure (vendor feature) | Buy | Configure (vendor feature) | Build | Configure (vendor add-on) |
| Volume | About 41,000 alerts in July 2026; 68% of commercial alerts auto-closed | About 60 releases a month touched | About 2,600 tickets a week | Monthly forecasts for 16 clusters | 3 pilot requisitions, 240 applicants |
| Partition | Commercial auto-close only; government alerts always reviewed | Used on all repositories, including government deployment code | Commercial tickets; government tickets excluded | Both | Not applicable |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| FedRAMP Rev5 Class C controls SI-4 and AU-6; IEC rules (C-IT-R01) | AI-001 | Monitoring must work for the government partition and the shared components that can affect it. An AI that silently closes alerts on shared tooling undermines the 1-hour reporting clock |
| FedRAMP Minimum Assessment Scope (MAS-CSO-TPR) | AI-002 | A coding assistant used on government deployment code handles information that can affect federal customer data, so it must be documented as a third-party information resource or kept off those repositories |
| Bank service provider rule (C-IT-R05) | AI-001 | A missed tooling compromise delays the 4-hour determination for bank customers |
| MSA confidentiality clause | AI-001, AI-002, AI-003 | Customer identifiers and code go to AI vendors; contracts must limit their use to providing the service |
| FTC Act Section 5 (15 U.S.C. 45) | AI-001 to AI-003 | Governs vendors' claims and the company's own statements to customers made with AI help |
| Title VII (42 U.S.C. 2000e-2), including disparate impact; ADA (42 U.S.C. 12112); Uniform Guidelines (29 CFR Part 1607) | AI-005 | An applicant ranking tool is a selection procedure. Disparate-impact liability exists by statute even though federal enforcement priorities changed under EO 14281. The Uniform Guidelines treat a selection rate below four-fifths of the highest group's rate as general evidence of adverse impact (29 CFR 1607.4(D)) |
| State AI employment laws, applied where applicants live or work | AI-005 | Examples: Illinois HB 3773 (in effect 2026-01-01); Colorado SB26-189 (effective 2027-01-01, applies to consequential decisions made from that date); NYC Local Law 144 (bias audit and candidate notice for NYC roles). The company hires in Florida, the DC-2 and DC-3 states, and remotely, so General Counsel checks each requisition's locations |

**Laws considered and not applicable:** the IT vertical profile lists no sector-specific AI rule for hosting providers. Federal AI executive orders (for example EO 14179 and EO 14365) direct federal agencies and do not by themselves impose duties on the company. EO 14365 does not preempt any state law.

## 4. MEASURE (by use case)
Tests ran on July and August 2026 data, with the tools already in production.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Analyst review of 200 randomly sampled auto-closed commercial alerts | Under 1% true positives; none in privileged-access, RMM, pipeline, or signing categories | 4 of 200 (2%) needed investigation, including the 2 privileged-access alerts on DC-1 that P07 also found in its own sample of 50 (AU-6) | **No** |
| AI-001 | Valid and reliable (generative summaries) | 50 summaries checked against raw events | No wrong host, user, or action | 3 of 50 named the wrong host or user (confabulation, a risk named in AI 600-1) | **No** |
| AI-001 | Safe | No auto-close for tooling and privileged categories | Configured | Auto-close applied to all commercial categories | **No** |
| AI-001 | Secure and resilient | Vendor FedRAMP package and SOC 2 reviewed; AI settings changeable only by named administrators | Both | Vendor reviewed (P09 VEN-06); settings limited to 3 SOC engineers with hardware keys | Yes |
| AI-001 | Fair, harmful bias managed | User-behavior alert rate per person: NOC night shift versus day shift; remote versus office staff | No group's false-positive rate more than 5 points above, or alerts per person more than 2 times, the comparison group's | Night-shift NOC staff drew 3.6 times as many alerts per person, all false positives from "unusual hour" features | **No** |
| AI-002 | Secure | Secret scanning of prompts and suggestions for 30 days; data-use terms | No secrets sent; no training on company code | 2 API keys pasted into prompts (revoked); enterprise terms exclude training | Partial |
| AI-002 | Valid and reliable | Static analysis findings per 1,000 lines in assistant-heavy versus other pull requests | No more than 1.2 times | 1.4 times (mostly input validation) | **No** |
| AI-003 | Privacy-enhanced | Drafts checked for another customer's details (retrieval scope) | 0 | 1 of 300 drafts quoted another tenant's ticket (caught by the agent) | **No** |
| AI-003 | Valid and reliable | 100 drafts reviewed for wrong recovery steps | Under 2% | 3% | **No** |
| AI-004 | Valid and reliable | Back-test of 2025-2026 forecasts against actual disk and host failures and capacity use | Recall of 70% for failures within 30 days; capacity error under 10% | 74% recall; capacity error 8% for DC-2 and DC-3 but 15% for DC-1 (older hardware) | Partial |
| AI-005 | Fair, harmful bias managed | Selection-rate ratio of the shortlist by sex and by race or ethnicity (self-identified, voluntary data), against the highest group | 0.80 or above (29 CFR 1607.4(D)) and no group below 0.80 without a job-related explanation | Female applicants 0.62 of the male rate in the NOC requisition (small sample: 96 applicants); other groups not enough data | **No** |
| AI-005 | Accountable and transparent | Vendor validation evidence and the features the model uses | Documented | Vendor would not disclose features; no validation study provided | **No** |
| All | Explainable and interpretable | Users can see why the output was produced (score factors, cited sources, feature importance) | Available | AI-001 scores yes, auto-close decisions in bulk no; AI-002 and AI-003 cite sources; AI-004 yes; AI-005 no | Partial |

**Bias and fairness testing plans:**
- **AI-005 (before any restart):** groups compared are sex, race or ethnicity, and age 40 and over versus under 40, from voluntary self-identification; metric is the shortlist selection rate per group divided by the highest group's rate; threshold 0.80. Because pilot samples are small, the review also checks whether the vendor model uses proxies (graduation year, address, employment gaps). General Counsel decides whether a bias audit by an independent auditor is required for any location (for example NYC roles).
- **AI-001 user-behavior module:** groups are shift (night versus day), work location (remote versus office), and contractors versus employees; metrics are alerts per person and false-positive rate; re-test after shift-specific baselines in 2026-11.

**Alert-source coverage check (AI-001).** The model has never seen DC-1 hypervisor, BMC, or RMM alerts from this environment. When those sources are onboarded (POAM-005), their alerts go to human review for the first 60 days with no auto-close.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** no auto-close for alerts on privileged access, identity provider administration, cloud administration, the RMM tool, hypervisors and BMCs, the pipeline and signing keys, bulk snapshot or delete actions, or any bank customer's tenant. Other commercial alerts may auto-close below the threshold, with a weekly random sample of 50 reviewed by an analyst. Summaries are labeled "AI-generated" and verified against raw events before any escalation or notice. User-behavior alerts about an employee need a second indicator before anyone contacts the employee, and AI output is never the sole basis for discipline.
- **AI-002:** a human writes the final change and two approvers review it; no secrets, customer data, or tenant metadata in prompts; not used on government deployment repositories until documented as a third-party information resource or replaced with a FedRAMP-certified option.
- **AI-003:** the agent reviews every draft; retrieval limited to the requesting customer's own tickets and the public knowledge base.
- **AI-004:** forecasts inform engineers' decisions; nothing is ordered or moved automatically.
- **AI-005:** paused. If restarted, recruiters review every applicant, not only the shortlist, and the tool may only reorder, never reject.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group; AI-001 and AI-005 also get a quarterly deep dive with the CTO. Results feed the risk register (P01 R-016, R-040 to R-043).

**Incident handling:**
- A missed true positive found in sampling is reopened and handled under POL-03; if it involves a tooling or privileged alert, the P08 tooling-compromise runbook applies.
- Customer data exposed through AI-003 is a security incident with MSA notice duties (P08 matrix).
- A vendor security incident or a model change that alters behavior is handled through P08 and the change process.

**Decommissioning criteria:**
- AI-001: turn off auto-close entirely (keep scoring and summaries) if the weekly sample shows more than 2% true positives for 2 weeks in a row, or any protected-category true positive was auto-closed.
- AI-003: switch off if another tenant's data appears in a draft after the retrieval fix.
- AI-005: retire if the vendor will not provide validation evidence and feature disclosure by 2026-12-31.
- Any tool: stop if the vendor changes data-use terms to allow training on company or customer data without opt-in.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Auto-close disabled for protected categories by 2026-10-15; weekly 50-alert sample from 2026-10-15; summary labeling and verification; shift-specific baselines and confirm-before-contact by 2026-10-31; 60-day no-auto-close period for new sources | CTO, 2026-09-22; noted by the CEO |
| AI-002 | **Approve with conditions** | Secret scanning on prompts (2026-10-31); removed from government deployment repositories until documented (2026-10-15); assistant-heavy pull requests get an added security reviewer until the static analysis ratio is at or below 1.2 | CTO, 2026-09-22 |
| AI-003 | **Approve with conditions** | Retrieval limited to the requesting customer (2026-10-31); required agent review recorded in the ticket | CTO, 2026-09-22 |
| AI-004 | **Approve with conditions** | Quarterly back-testing; DC-1 forecasts checked by an engineer before purchase decisions; model documentation written | CTO, 2026-09-22 |
| AI-005 | **Paused** | Restart only after a passed bias review, vendor validation evidence, applicant notice where state law requires, and a General Counsel location check | CTO, 2026-09-22; noted by the CEO |

The conditions are tracked as POAM-006 (AI-001) and POAM-025 (AI-002 to AI-005) in P07, and in the risk register (P01 R-016, R-040 to R-043). The AI review group holds its first monthly meeting on 2026-10-13.
