# AI Risk Assessment: AI-Assisted Security Alert Triage (SIEM)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Small / Information Technology |
| AI use case | AI-001: AI-assisted alert triage in the SaaS SIEM, enabled April 2026. AI-002 (coding assistant) is covered briefly in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1), because the feature writes generative summaries |
| Assessor / date | IT Manager (Information Security Officer) with the NOC and Support Manager and the HR Manager, 2026-08-24 to 2026-09-04 |
| Decision | Approved with conditions by the COO, 2026-09-25 (section 6) |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the IT Manager, who owns the SIEM and every AI setting in it. A platform engineer enabled the feature in April 2026 during a trial, with no review or approval. From now on, AI settings may change only through the change process (POAM-015).
- **Decision authority:** the COO approves High-tier AI use cases, with the Information Security Officer's recommendation. Moderate-risk items in P01 (R-016) sit at the same level.
- **Policies that apply:**
  - POL-04 4.9: no Restricted or Confidential data in AI tools unless approved and covered by contract terms
  - POL-05 4.8: approved tools only
  - POL-05 4.10: monitoring notice, including AI-assisted analysis of security logs
  - POL-01 4.8: vendor review
- **Scale for a 60-person company:** there is no AI committee. The IT Manager, the NOC and Support Manager, and the COO review the AI inventory quarterly. The HR Manager joins when an AI output concerns an employee.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Reduce alert fatigue for a two-person IT team and the NOC. The feature scores each alert from 0 to 100, writes a plain-language summary, groups related alerts, and **auto-closes alerts scoring under 30**. A user-behavior module flags unusual sign-in times, locations, and access patterns for employees |
| Users / operators | IT Manager, IT specialist, and NOC analysts (16 staff on 24x7 shifts) |
| Affected people | **Customers:** a missed attack on the company's tools can harm about 430 customers, including 14 banks. **Employees:** user-behavior alerts can lead to questions or investigations of named staff |
| Data | Inputs: identity provider, cloud tenant, and EDR logs, which include workforce and customer user IDs, IP addresses, and tenant names. Outputs: scores, summaries, and auto-close decisions stored in the SIEM. The vendor's terms allow use of "de-identified telemetry" to improve the service; **the scope of that use has not been reviewed** |
| Build or buy | Configure: a vendor feature in the SaaS SIEM. The company cannot see or retrain the model, but it sets the thresholds, auto-close rules, and categories |
| Volume | July 2026: about 9,800 alerts, **71% auto-closed** with no human review (P07 AU-6 finding) |
| Not in scope today | Hypervisor, BMC, network, and RMM logs are not in the SIEM yet (POAM-010). Once they are, the model will score those alert types, which it has never seen from this environment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (IT sector) | None identified | The vertical profile lists no AI-specific rules for IT service providers |
| MSA confidentiality clause | **Yes** | Logs include customer user IDs and tenant names. The SIEM vendor must be covered as a subprocessor, and its data-use terms must not allow use of customer information beyond providing the service |
| FTC Act Section 5 (15 U.S.C. 45) | Indirectly | Governs the vendor's claims about accuracy and data use. Keep the vendor's documentation and claims in the procurement file |
| State AI employment laws | **Not today** | The company does not use AI output in employment decisions. If user-behavior alerts ever became a factor in discipline or termination, laws where the employee works could apply, such as Illinois HB 3773 or Colorado SB26-189 (effective 2027-01-01). Section 5 forbids that use |
| FedRAMP (C-IT-R01) | Readiness target | Class C controls SI-4 and AU-6 need monitoring that works. An AI tool that silently closes alerts undermines both (P03 G-207, G-071) |

## 3. Risk tier
**Tier: High**, under the repository rubric (`00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the rubric rates as High any AI that "can affect ... critical infrastructure operations." Here the AI decides, without a human, which security alerts nobody will ever look at. The monitored systems are the tools that reach every customer, including banks' covered services. A wrong auto-close could let the P08 incident (RMM compromise) run undetected.

**Why not a consequential decision about people:** the tool does not make employment decisions, and section 5 keeps it that way.

**Path to Medium:** after the section 6 conditions are in place, a human reviews every privileged-access and tooling alert before it is closed. The AI then influences, but no longer makes, the decision. Re-tier to Medium after 8 consecutive weeks of sampling with fewer than 1% true positives among auto-closed alerts and no missed true positive in the protected categories.

## 4. MEASURE
The tests ran on alerts from July and August 2026. The vendor feature was already in production.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Analyst review of a random sample of 200 auto-closed alerts. Target: fewer than 1% true positives, and none in privileged-access, cloud-admin, or tooling categories | 3 of 200 (1.5%) should have been investigated. One was a credential-stuffing burst against the customer portal, closed as "known scanner" (relates to R-007) | **No** |
| Valid and reliable (generative summaries) | 50 summaries checked against the raw events. Target: no wrong host, user, or action | 4 of 50 named the wrong host or user; 1 described a blocked sign-in as successful | **No.** This is confabulation, a risk the Generative AI Profile names |
| Safe | No auto-close for alerts about administrative tools | Auto-close applies to all categories | **No** |
| Secure and resilient | Vendor SOC 2 reviewed; AI settings changeable only by named administrators with MFA | Vendor report not yet reviewed (POAM-020); settings limited to 2 IT staff with hardware keys | Partial |
| Accountable and transparent | Named owner; approved change; staff told that AI analyzes security logs | Feature enabled with no approval; the POL-05 monitoring notice was approved 2026-09-25 and acknowledgments are due by 2026-11-30 | **No** (improving) |
| Explainable and interpretable | Each score shows the top contributing factors, and analysts can open the raw events | Available for scores; not available for auto-close decisions in bulk | Partial |
| Privacy-enhanced | Vendor's telemetry use limited to service delivery; U.S. data residency; logs kept 90 days | Terms allow "de-identified telemetry" for product improvement; residency is U.S. per the vendor order form | Partial |
| Fair, with harmful bias managed | See the bias testing plan below | Night-shift disparity found | **No** |

**Bias and fairness testing plan (user-behavior module).** The module affects named employees, so its errors must not fall on one group.
- **Groups compared:**
  - (a) NOC night-shift staff (22:00 to 06:00) versus day-shift staff;
  - (b) remote staff versus staff at the Florida headquarters;
  - (c) the 2 contractors versus employees.
- **Metrics:** user-behavior alerts per person per month, and the false-positive rate of alerts that led to any follow-up with the employee.
- **Threshold:** flag if any group's false-positive rate exceeds the comparison group's by more than 5 percentage points, or its alerts per person exceed 2 times the comparison group's.
- **Result (July and August):** night-shift staff drew **4.1 times** as many user-behavior alerts per person as day staff. All of them were false positives driven by "unusual hour" features. Three night-shift employees were questioned by a manager about normal work. **Flagged.**
- **Fix:** give each shift its own baseline, and require an analyst to confirm another indicator before any employee is contacted. Re-test in November 2026.

**Alert-source coverage check.** The model was tuned on the vendor's other customers. Management-plane logs (hypervisor, BMC, RMM) will be new to it. When those sources are onboarded (POAM-010), their alerts go to human review for the first 60 days, with no auto-close, while baseline miss rates are measured.

## 5. MANAGE
**Human-in-the-loop design:**
- **No auto-close** for alerts in these categories:
  - privileged access and identity provider administration
  - cloud administration
  - RMM tool activity
  - hypervisor and BMC activity
  - bulk snapshot or delete actions
  - any alert naming a bank customer's tenant
- **Other alerts** may still auto-close below the score threshold, but an analyst reviews a weekly random sample of 100 auto-closed alerts. Misses are logged and reported to the vendor.
- **Generative summaries are aids, not evidence.** Analysts must check host, user, and action against the raw events before escalating or notifying anyone. Summaries are labeled "AI-generated" in tickets.
- **User-behavior alerts about an employee** need an analyst to confirm another indicator before any contact with the employee. AI output may never be the only basis for discipline. HR is involved before any employment action, and the decision rests on independent evidence.
- **Analysts can always override** a score or reopen a closed alert. Overrides are logged and reviewed monthly for tuning.

**Monitoring:**
- The weekly sample tracks the miss rate by category.
- Summary accuracy is checked monthly on 20 summaries.
- The fairness metrics above are reviewed quarterly.
- Results go into risk R-016 in P01 and the quarterly AI inventory review.

**Incident handling:**
- A missed true positive found in sampling is reopened and handled under POL-03.
- If a missed alert involved an administrative tool, the P08 runbook is used.
- A vendor model change that changes scoring is treated as a change (POAM-015).
- A vendor security incident follows POL-03 4.8.

**Decommissioning criteria:** turn off auto-close entirely, keeping scoring and summaries, if:
- the weekly sample shows more than 2% true positives among auto-closed alerts for 2 weeks in a row;
- any true positive in a protected category was auto-closed;
- the vendor changes its data-use terms to allow training on the company's logs without opt-in.

## 6. Decision
**Approve with conditions.** COO, 2026-09-25. AI-001 may stay in production **only if** these conditions are met:
1. Auto-close is disabled for the protected categories in section 5, by 2026-10-15 (POAM-012 milestone).
2. The weekly 100-alert sample starts by 2026-10-15 and is reported monthly to the COO (POAM-011).
3. Summaries are labeled as AI-generated, and analysts verify facts before escalation, from 2026-10-15.
4. The user-behavior module uses shift-specific baselines and the confirm-before-contact rule by 2026-10-31. The three questioned night-shift employees receive a written note that no concern remains.
5. The SIEM vendor's SOC 2 report and data-use terms are reviewed by 2026-11-30, including opt-out of product-improvement use of customer identifiers (POAM-020).
6. AI settings are owned by the IT Manager and changed only through the change process (POAM-015).

Re-assess before onboarding management-plane logs (POAM-010), and at least annually.

## 7. AI-002: coding assistant (brief assessment)
- **Tier: Medium.** It influences code that runs the control plane and builds the VM templates customers deploy, but a human writes the final change and a reviewer approves it.
- **Main risks:**
  - insecure or incorrect code suggestions (supply chain, R-011);
  - leakage of source code. The enterprise agreement excludes training on company code.
- **Conditions:**
  - pull-request review without bypass (POAM-017);
  - static analysis added to CI before the pilot expands beyond 4 engineers (P03 SA-11 gap);
  - no secrets, customer data, or tenant metadata in prompts (POL-05 4.8).
- **Bias testing** is not relevant to this use case: it makes no decisions about people.
