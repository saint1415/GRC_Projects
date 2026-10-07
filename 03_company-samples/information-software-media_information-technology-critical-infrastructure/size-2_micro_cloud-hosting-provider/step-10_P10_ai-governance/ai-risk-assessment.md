# AI Risk Assessment: AI-Driven Alert Triage in the MDR Service

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Tier / Vertical | Micro / Information Technology |
| AI use case | AI-001: AI-driven alert triage and automated containment inside the MDR provider's platform (SYS-11), in use since the MDR contract started in November 2025. AI-002 and AI-003 are covered briefly in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (AI 600-1) because the platform writes AI-generated alert summaries |
| Assessor / date | Lead Systems Engineer (Information Security Lead) with the Operations Manager, 2026-08-24 to 2026-08-28; MDR provider's service manager interviewed 2026-08-25 |
| Decision | Owner, 2026-09-15 (section 6) |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

**Why the registry use case was adapted.** The registry default is "AI-driven security operations (alert triage)". A 7-person company does not run its own security operations center or its own AI. It buys 24x7 monitoring from an MDR provider, whose platform uses AI to triage alerts and act on its own. So this assessment covers a **third-party AI service the company relies on**: the company cannot see or retrain the model, but it can set what the model may close or act on, demand evidence, and change the contract.

## 1. GOVERN
- **Accountable owner:** the Lead Systems Engineer, who owns the MDR relationship. **Decision authority:** the Owner. At this size there is no AI committee; AI use is reviewed at the monthly security meeting (POL-02 A.10).
- **How it started.** The MDR provider configured its standard settings at onboarding in November 2025: auto-close below its risk threshold, automatic laptop isolation, and automatic identity account suspension. Nobody at the company reviewed or approved those settings, and the company never received auto-close statistics until P07 asked for them (P01 R-013).
- **Policies that apply:**
  - POL-04 4.6: approved AI tools only. AI-001 is the only approved tool, with the conditions in section 6.
  - POL-02 A.5: vendor review and contract terms, including data-use limits.
  - POL-02 B.5: two-person approval for changes to the MDR's automated containment and auto-close settings.
  - POL-02 B.7: break-glass accounts are excluded from automatic suspension.
  - POL-02 C.6: monitoring notice to staff, including AI-assisted analysis and automatic containment.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Give a 7-person company 24x7 detection it cannot staff. The MDR platform scores every alert from the company's EDR agents, identity provider, and firewalls, writes a plain-language summary, groups related alerts, **auto-closes alerts below its threshold**, and escalates the rest to the provider's human analysts. It can also **isolate a laptop or suspend an identity provider account on its own** when it scores an alert as high confidence |
| Users / operators | MDR provider analysts (operate the platform); the Lead Systems Engineer and the on-call engineer (receive escalations and the monthly report) |
| Affected people | **Customers and the two banks:** a missed attack on staff accounts or laptops is the usual first step toward the RMM tool and the hypervisor manager (P08). **Employees:** automated suspensions and user-behavior alerts fall on named staff, and can lock the on-call engineer out during an outage |
| Data | **Inputs:** EDR telemetry from 9 laptops; identity provider sign-ins (staff names, devices, IP addresses); firewall and VPN logs (connection metadata, including customer IP addresses at DC-1). No customer VM contents and no bank customer information. **Training:** the vendor's model, trained on its customer base. **Outputs:** scores, summaries, auto-close decisions, and automated actions, kept 12 months. **The MDR contract allows the provider to use de-identified telemetry to improve its models** |
| Build or buy | Buy: a feature of the MDR service. Thresholds and automation are set by the provider; the company can ask for changes per category |
| Volume | July 2026: about 2,140 alerts on company telemetry; **about 91% auto-closed** with no human review; 52 reviewed by MDR analysts; 7 escalated to the company. June to August 2026: 3 automatic laptop isolations and 2 automatic account suspensions |
| Not in scope today | RMM, hypervisor manager, cloud tenant, and DNS logs are not sent to the MDR (POAM-009). When they are, the model will score alert types it has never seen from this company |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (IT sector) | None identified | The vertical profile lists no AI-specific rules for IT service providers |
| Bank contracts (Interagency Guidelines III.C.1.f and III.D.2) | **Yes, by contract** | The banks expect monitoring that detects attacks on the systems that reach their information. An AI that silently closes alerts on privileged accounts weakens that monitoring. The MDR is the company's own service provider, so its terms must support the measures the banks expect (P03 G-023, G-030) |
| MSA confidentiality clause | **Yes** | Firewall logs include customer IP addresses and connection metadata. The provider's use of telemetry must stay within providing the service |
| FTC Act Section 5 (15 U.S.C. 45(a)) | Indirectly | Governs the provider's claims about accuracy and data use. Keep its marketing and service documentation in the contract file |
| State AI employment laws | **No** | All staff work in Florida, and AI output is not used in employment decisions. Section 5 forbids that use. If staff ever worked in a state with such a law, recheck |
| FedRAMP (C-IT-R01) | No | No federal customer (P03 G-001) |

## 3. Risk tier
**Tier: High**, under the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High.** The rubric rates as High any AI that "can affect ... critical infrastructure operations." This AI decides, with no human at the company involved, which security alerts nobody ever looks at. It also takes containment actions on its own. The accounts and laptops it watches are the way into tools that reach about 310 customer servers and two banks' covered services. A wrong auto-close could let the P08 incident run undetected. A wrong suspension locked the on-call engineer out of the VPN for about 50 minutes during a host failure on 2026-06-27.

**Why not a consequential decision about people.** The tool does not decide employment, credit, or other consequential matters, and section 5 keeps it that way.

**Path to Medium.** Once the section 6 conditions are in place, every alert in the protected categories gets a human review before closing, and suspensions of on-call staff need a call first. The AI then influences, but does not make, the decisions that matter. Re-tier to Medium after 3 consecutive monthly samples with no missed true positive in a protected category and an overall miss rate under 1%.

## 4. MEASURE
The tests used the MDR's July 2026 alert export and automated-action log (received 2026-08-14 for P07), plus 3 months of escalation summaries.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Review of a random sample of 100 auto-closed alerts. Target: fewer than 1% that should have been investigated, and none on privileged accounts or the VPN | 2 of 100 (2%). (1) A sign-in to the Owner's administrator account from a foreign VPN exit node at 02:10, closed as "known consumer VPN". The Owner confirmed it was his own travel, but it needed a human check. (2) Repeated VPN sign-in attempts against the former Support Engineer's username, closed as "low-volume scanning" | **No** |
| Valid and reliable (generative summaries) | 20 escalation summaries checked against the raw events. Target: no wrong host, user, or action | 2 of 20 named the wrong laptop; 1 described a blocked sign-in as successful | **No.** This is confabulation, a risk the Generative AI Profile names |
| Safe | Automated actions must not stop the company from responding to an incident | One automatic suspension (2026-06-27) locked the on-call Systems Engineer out of the VPN for about 50 minutes while he was responding to a night-time host failure (the cluster restarted the affected VMs, but he could not check them). No break-glass account existed | **No** |
| Secure and resilient | Provider's SOC 2 report reviewed; MDR console access limited to named users with MFA | SOC 2 report requested, not received (POAM-012); console access is 2 named company users with identity provider MFA | Partial |
| Accountable and transparent | Named owner; company-approved settings; staff told about AI monitoring | Settings never approved by the company; no monitoring notice before POL-02 C.6 (effective 2026-10-01) | **No** (improving) |
| Explainable and interpretable | Each escalation shows the top contributing factors, and the company can open the raw events | Available for escalations; auto-close decisions available only as a monthly export | Partial |
| Privacy-enhanced | Telemetry use limited to providing the service; U.S. processing; 12-month retention | Contract allows de-identified telemetry for model improvement; the provider states U.S. processing but the contract does not say so; retention 12 months | Partial |
| Fair, with harmful bias managed | See the bias testing plan below | After-hours disparity found | **No (flagged)** |

**Bias and fairness testing plan (user-behavior alerts and automated suspensions).** These outputs fall on named employees, so their errors must not fall mostly on one group.
- **Groups compared:** the 5 technical staff during on-call and after-hours work, versus all staff during office hours (the Owner and the Operations Manager work office hours only).
- **Metrics:**
  - user-behavior alerts per person per month;
  - the false-positive rate of alerts that led to any follow-up with the employee;
  - automated suspensions per person.
- **Threshold:** flag if one group's alerts per person exceed 2 times the other's, or its false-positive rate is more than 5 percentage points higher.
- **Result (June to August 2026):**
  - 81% of user-behavior alerts and both automated suspensions fell on technical staff working after hours or from DC-1.
  - All were false positives, driven by "unusual hour" and "new location" features.
  - **Flagged.** With 7 people the numbers are small, so the result is treated as a pattern to fix, not a statistic.
- **Fix:**
  - The provider adds the DC-1 network and the on-call schedule to its baseline.
  - Before suspending an on-call engineer's account, the provider calls the on-call phone unless the account is actively doing harm (for example deleting data).
  - Re-test with the November 2026 export.

**New-source check.** When RMM, cloud, hypervisor manager, and DNS logs are onboarded (POAM-009), their alerts go to human review with no auto-close for the first 60 days, while baseline miss rates are measured.

## 5. MANAGE
**Human-in-the-loop design:**
- **No auto-close** for alerts in these protected categories:
  - privileged accounts (administrator and break-glass accounts in the identity provider and cloud tenant);
  - VPN sign-ins to the management network;
  - RMM tool activity, once its logs arrive;
  - hypervisor manager and BMC activity, once their logs arrive;
  - any alert naming a bank customer's systems.

  The provider's analysts review these first, then escalate or close with a note.
- **Other alerts** may still auto-close. The Lead Systems Engineer reviews a random sample of 50 auto-closed alerts every month (POAM-010). Misses are logged and sent to the provider.
- **Automated containment:**
  - Laptop isolation stays automatic. A clean laptop is quick to restore, and a compromised one is the most likely first step.
  - Account suspension is automatic for everyone except the on-call engineer, who gets a call first (section 4 fix).
  - Break-glass accounts are never suspended automatically (POL-02 B.7).
- **Summaries are aids, not evidence.** Before acting or notifying anyone, the engineer checks host, user, and action against the raw events. Summaries pasted into PSA tickets are labeled "AI-generated."
- **No employment use.** AI output may never be the only basis for questioning or disciplining a staff member. Any concern goes to the Owner with independent evidence.
- **Override.** The on-call engineer can ask the provider to reverse any automated action at any time. Overrides are logged and reviewed monthly.

**Monitoring:**
- Monthly: the 50-alert sample, the automated-action log, and summary accuracy on 10 summaries. Results go into risk R-013 and the monthly report to the Owner.
- Quarterly: the fairness metrics above.
- Any provider notice of a model or threshold change is treated as a change under POL-02 B.5 and triggers a fresh sample.

**Incident handling:**
- A missed true positive found in sampling is reopened and handled under POL-03.
- If it involved a privileged account or a tool that reaches customers, the P08 runbook is used.
- A security incident at the MDR provider is handled under POL-03 4.11.

**Decommissioning criteria.** Ask the provider to turn off auto-close entirely, keeping scoring, summaries, and analyst review, if any of these occurs:
- the monthly sample shows more than 2% missed true positives in two months in a row;
- any true positive in a protected category is auto-closed;
- the provider changes its terms to train on the company's telemetry without an opt-out.

If the provider cannot meet the conditions in section 6 by 2026-12-31, the Owner reconsiders the MDR contract at renewal.

## 6. Decision
**Approve with conditions.** Owner, 2026-09-15. AI-001 may stay in production **only if** these conditions are met:
1. The provider configures no auto-close for the protected categories in section 5, by 2026-10-15. Requested in writing on 2026-09-16.
2. The monthly 50-alert sample starts with the September 2026 export and is reported to the Owner from 2026-10-31 (POAM-010).
3. Break-glass accounts are excluded from automatic suspension, and the call-first rule for the on-call engineer is in place, by 2026-10-31 (POAM-002).
4. Summaries are labeled as AI-generated, and engineers verify facts before acting, from 2026-10-01.
5. The MDR contract is amended to exclude the company's telemetry from model training, state U.S. processing, and require notice of model or threshold changes, by 2026-12-31 (POAM-012).
6. Changes to auto-close and automated containment settings need two-person approval at the company (POL-02 B.5), from 2026-10-01.

Re-assess before the management-plane logs are onboarded (POAM-009) and at least once a year. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; the next assessment checks whether a profile has been published.

## 7. Other AI use cases (brief)
- **AI-002: public generative AI chatbots.** Staff have used public chatbots to draft emails and scripts.
  - **Tier: High if customer data, credentials, or configurations are entered;** Low for generic drafting.
  - **Rule:** prohibited for any customer data, credentials, tickets, configurations, or RMM scripts (POL-02 C.2; POL-04 4.6). Generic drafting with no company or customer information is allowed.
  - **Revisit** if the Owner wants an enterprise assistant with no-training terms.
- **AI-003: PSA vendor's AI ticket-summary feature.** The vendor added it in 2026, and it is turned off.
  - **Tier: Medium.** Tickets contain customer names, server names, and sometimes credentials pasted by customers, and summaries would go to customers.
  - **Rule:** stays off until the vendor's data-use terms are reviewed under POL-02 A.5 and a short assessment is done.
  - **No bias testing is needed** for AI-002 or AI-003: neither makes decisions about people.
