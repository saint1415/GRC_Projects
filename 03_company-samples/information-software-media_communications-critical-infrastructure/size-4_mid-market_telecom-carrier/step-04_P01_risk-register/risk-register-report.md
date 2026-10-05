# Risk Register Report: Cris Santos Company | Communications | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Size tier | Mid-Market (850 employees) |
| Vertical | Communications (CISA critical infrastructure sector) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Regulatory link | Supports the CPNI duty to take "reasonable measures to discover and protect against attempts to gain unauthorized access to CPNI" (47 CFR 64.2010(a)); the covered 911 service provider duty to take reasonable measures to provide reliable 911 service (47 CFR 9.19(b)); outage duties (47 CFR Part 4); CALEA SSI (47 CFR 1.20003) |
| Prepared | 2026-07-31 by the Security Manager and the GRC analyst with the vCISO; R-032 and R-051 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High, and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units, the OSS/BSS platform defined in the SSP (P02), the voice and broadband network it manages (SYS-07, SYS-08), the lawful-intercept system (SYS-10), the Business Services platform (SYS-15), the customer channels (SYS-11, SYS-12), the 34 vendors with CPNI, PII, or network access (SYS-17), and the AI tools in P10. Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-17.

| Area | Appetite | Statement and measure |
|---|---|---|
| 911 and public safety | **Very low** | No cyber, technology, or facility risk that could plausibly stop 911 calls or PSAP notice is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: 911-linked risks above Low (7 today: R-001, R-004, R-013, R-014, R-015, R-016, R-038; target 2 or fewer by 2027-12-31, because storms (R-013) cannot be engineered away) |
| Confidentiality of CPNI and lawful-intercept data | **Low** | The company will not accept a risk of a CPNI breach affecting more than 1,000 customers, or any lawful-intercept compromise, above Moderate. Measure: R-002, R-005, R-006, and R-009 at Moderate or lower by 2027-06-30 |
| Network integrity and availability | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test or failover in the last 12 months |
| Regulatory compliance | **Low** | No FCC duty (CPNI, CALEA, outage, 911 reliability, robocall mitigation) may stay Not met beyond 2027-03-31. Filings are made on time, and the annual CPNI certification statement is evidence-based |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives CPNI without CPNI, no-training, and 24-hour incident notice terms, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI in customer care, network operations, and marketing, but only through the P10 process. No AI tool touches CPNI or makes network changes without review |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $500,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, public reporting on intrusions into U.S. carriers (the FCC's 2025 order on reconsideration describes the "Salt Typhoon" campaign that "exploited publicly known common vulnerabilities and exposures"; 90 FR 58006), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, public safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 31 |
| Low | 10 |
| Very Low | 0 |
| **Total** | **51** |

Treatments: 45 Mitigate, 5 Accept (R-029, R-033, R-034, R-035, R-046), 1 Share/Transfer (R-028). Status: 28 In progress, 18 Open, 5 Accepted.

Cyber insurance ($15 million limit, $500,000 retention) transfers part of the financial exposure for R-001 to R-003. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to 911 or to customers. R-028 (DDoS) is recorded as Share/Transfer because the upstream providers' scrubbing contracts carry the mitigation.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Nation-state exploitation of edge routers or SBCs with long-term access | Very High | Scan and patch network elements; SBC upgrades; element logs to the SIEM; threat hunt | Director of Network Engineering | 2027-01-31 |
| R-002 | Intruder crosses the management plane and steals CDRs (P08 runbook 1) | High | Named TACACS+ accounts with MFA; POP segmentation; read-only mediation account; CDR read logging | Security Manager | 2027-03-31 |
| R-003 | Ransomware halts IT and cloud operations (P08 runbook 2) | High | IT contingency plan; restore tests; ransomware tabletop | IT Director | 2027-03-31 |
| R-004 | Destructive attack on access elements causes an outage including 911 | High | Named accounts; bulk configuration restore exercise; access element baselines | Director of Network Engineering | 2027-03-31 |
| R-005 | Lawful-intercept system compromise | High | Isolated management path; compromise reporting; SSI refiling | Vice President of Network Operations | 2026-12-31 |
| R-006 | Chatbot fallback with SSN4 lets a fraudster see call detail and take over the account | High | Fallback stays off; sign-in only; session review | Director of Customer Operations | 2026-11-30 |
| R-009 | Network element activity unmonitored | High | Element syslog and TACACS+ accounting to the SIEM; MDR use cases | Security Manager | 2027-01-31 |
| R-013 | Hurricane causes a multi-day outage | High | Portable generators for 911-critical cabinets; fuel contracts; storm exercise | Vice President of Network Operations | 2027-05-31 |
| R-014 | Shared fiber segment under 2 "diverse" 911 circuit pairs | High | Re-route and re-audit | Chief Technology Officer | 2026-12-31 |
| R-051 | Vendors' shared VPN account with standing management access (found in P07) | High | Disable; named vendor accounts through the access broker | Security Manager | 2026-10-31 |

**Themes.**
- **The management plane is the main attack path (R-001, R-002, R-004, R-009, R-023, R-032, R-049, R-051).** Core and edge routers are well protected, but access elements, SBCs, POPs, and vendor access are not, and nobody watches network element logs. This is the path used against larger carriers. Fixing it lowers 8 risks at once.
- **911 reliability (R-004, R-013 to R-016, R-038).** Two engineering gaps (shared fiber segment, CO-6 generator) and one process gap (stale PSAP contacts) sit under the company's covered 911 duties.
- **CPNI in new channels (R-006, R-007, R-036, R-037, R-039).** The chatbot, agent assist, the overflow vendor, and the churn model all reached CPNI before review. P10 addresses the AI tools.
- **Recovery beyond the network (R-003, R-026, R-027).** The network is engineered for failover; IT recovery is unproven.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $1.41 million one-time, including the SOC 2 work, and $250,000 a year):**
- Management plane hardening: named TACACS+ accounts with MFA on all element types, POP segmentation, access broker for vendors ($260,000 one-time)
- Network element vulnerability scanning and SIEM onboarding of element logs, CDR reads, SYS-15, and SYS-18 ($90,000 one-time; $150,000 a year through the MDR and scanner licenses)
- Privileged access management extension to jump hosts and SYS-18 ($70,000 one-time; $40,000 a year)
- SBC upgrades ($180,000) and acceleration of copper-line migration off the TDM switches (2027 capital plan)
- 911 reliability fixes: re-route of 2 circuit pairs and the CO-6 transfer switch ($210,000)
- Recovery testing program and IT contingency plan ($80,000 one-time)
- Vendor risk program and contract amendments ($60,000 a year)
- SOC 2 readiness, Type 1, and Type 2 examination for Business Services ($240,000 across 2027)
- AI governance conditions in P10 (chatbot redesign, approval-flag filter, agent assist contract) ($110,000)
- Portable generators for 911-critical cabinet sites ($170,000)
- Legacy CLEC billing migration (in the billing project budget, not the security plan)

Smaller items (PSAP contact confirmation, RMD update, SNMP string replacement, CALEA refiling) are funded from operating budgets. Each funded item maps to a P07 POA&M entry.

**Accepted (5, all Low):** R-029 (CTO), R-033 (Director of Network Engineering), R-034 and R-035 (IT Director), R-046 (Billing Director, until migration).

**Contract actions:** CPNI, no-training, and 24-hour incident notice terms for the chatbot, CCaaS (agent assist), overflow call center, and bill print vendors (R-024, R-039), due 2026-12-31. BSS vendor recovery terms (R-025) at the 2027 renewal.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as two lines: "Cybersecurity and network resilience" (owned by the COO) and "911 reliability and public safety" (owned by the CTO), each reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| OSS/BSS (SSP in P02) | Chief Operating Officer, maintained by the Security Manager | 21 risks whose affected assets include SYS-01 to SYS-05, SYS-09, SYS-13, SYS-16, or SYS-18 (filter the `affected_asset_or_process` column) |
| Network (voice core and access network) | Chief Technology Officer | 19 risks whose affected assets include SYS-07 or SYS-08 |
| Business Services (P09 SOC 2 system) | Director of Business Services | R-010, R-019, R-028, R-044, R-045, R-050 |
| AI portfolio (P10) | Vice President of Regulatory Affairs (AI review group chair) | R-006, R-036, R-037, R-038, R-039, R-040 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments, 2026-09-17.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (SYS-18 retirement, TDM retirement, SBC replacement, a new AI use case) or a significant incident.
