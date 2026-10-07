# Risk Register Report: Cris Santos Company | Other Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional electronics and device repair chain: 34 stores, a Depot, national mail-in, protection plan claims) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Other Services (except Public Administration) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also supports | Fla. Stat. 501.171(2) "reasonable measures"; FTC Act Section 5 reasonable security; NIST CSF 2.0 ID.RA and GV.RM outcomes; PCI DSS v4.0.1 targeted risk analyses (input) |
| Prepared | 2026-07-31 by the GRC Analyst and the Security Manager with the vCISO; R-048 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and the risk appetite); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (34 stores, the Depot, the digital channel, partner programs, the contact center, business accounts, and corporate functions), the Service Ticketing and Point-of-Sale Platform (STPP; P02), the systems outside it that hold customer data (SYS-08, SYS-12 to SYS-16), and the customer devices and data in the company's custody while they are repaired, recovered, or recycled. Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**What makes this business different.** Most companies protect data they collect. A repair chain also holds **customers' entire phones and laptops**, often unlocked, with photos, messages, health and location data, and saved passwords, plus full images of failing drives in its lab. At this size it also processes claims as the agent of two protection plan partners and takes card payments on a web page it builds itself. The biggest risks are therefore **people with legitimate physical access** (technicians and lab staff), **data kept too long**, and **the payment and partner channels the company runs in its own cloud**.

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
| Customer device data in custody | **Very low** | No risk of workforce access to customer device content beyond the repair need is accepted above Low once controls are in place. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: risks on device content above Low (3 today: R-001, R-005, R-008; target 0 by 2027-06-30) |
| Payment card data | **Very low** | The company will not hold card data anywhere outside the P2PE terminals and the gateway's frame, and will not sign an SAQ it cannot support with evidence. Measure: R-004, R-009, and R-044 at Low before the 2026-12-15 attestations |
| Confidentiality of customer records | **Low** | No risk of a breach affecting more than 10,000 customers is accepted above Moderate. Measure: R-002, R-023, and R-046 at Moderate or lower by 2027-06-30 |
| Availability of store and partner operations | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test or vendor commitment in the last 12 months |
| Contractual commitments | **Low** | No breach of a manufacturer or partner security term may stay open beyond its next audit or renewal. Measure: R-015 closed before the 2026-10 Manufacturer A audit; R-016 on track for the 2027 SOC 2 Type 2 report |
| Regulatory compliance | **Low** | No known gap against FTC Act Section 5 or Fla. Stat. 501.171 may stay open beyond 2027-06-30. Unsubstantiated claims are removed immediately |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives customer data without security, data-use, and breach notice terms, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants AI in diagnostics, customer service, and operations, but only through the AI governance process in P10. No AI tool that ranks people for jobs runs without human review and adverse impact monitoring |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $150,000 insurance retention are tolerable. Scenarios above $1 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA, interviews with every process owner (Director of Retail Operations, 4 Regional Managers, Depot Director, Data Recovery Manager, Director of Partner Programs, Director of Customer Experience, Digital Engineering Manager, HR Director, Chief Financial Officer), the March 2026 Store 17 case file, the 2026-05 penetration test, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory and contractual, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values and notice cost assumptions, used for the enterprise roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 0 |
| High | 8 |
| Moderate | 31 |
| Low | 11 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 4 Accept (R-030, R-042, R-043, R-045). Status: 28 In progress, 18 Open, 4 Accepted.

Cyber insurance ($5 million limit, $150,000 retention) transfers part of the financial exposure for R-002, R-003, R-004, and R-046. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to customers.

### Top risks (High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Technician views or copies personal data from customer devices | High | Standard bench image (session recording, USB block, EDR) at the remaining 14 stores; block phone pairing; monthly flag review | Director of Retail Operations | 2027-03-31 |
| R-002 | Legacy passcodes and account passwords in ticket notes exposed | High | Bulk redaction of about 12,400 legacy tickets; verify by repeat search | Privacy and Compliance Manager | 2026-11-30 |
| R-003 | Ransomware halts stores, Depot, lab, and cloud workloads | High | EDR everywhere; segment 12 older stores; quarterly restore tests; tabletop | IT Director (Information Security Officer) | 2027-06-30 |
| R-004 | Skimming script on the mail-in checkout page | High | Script inventory, content security policy, change and tamper detection | Digital Engineering Manager | 2026-11-30 |
| R-005 | Recovered data past retention stolen or exposed | High | Fix the purge job; purge 27 TB; encrypt the older shelf; expiring links | Data Recovery Manager | 2026-12-31 |
| R-015 | Manufacturer A restricts authorized status after its October audit | High | Remove leaver accounts; 24-hour notice procedure; evidence pack | Director of Partner Programs | 2026-10-15 |
| R-016 | Partner P1 moves claims for lack of a SOC 2 Type 2 report | High | Remediate, then 6-month observation from 2027-04-01 | Chief Operating Officer | 2027-12-31 |
| R-046 | SYS-01 vendor breach exposes 1.9 million customer records | High | Keep less (R-002, R-023); 24-hour notice term; annual SOC 2 review | Chief Financial Officer | 2027-03-31 |

**Themes.**
- **Keep less, and let fewer people reach it (R-001, R-002, R-005, R-018, R-023, R-024, R-046).** The company has the right designs (restricted passcode field, data access standard, retention rules), but legacy data and legacy stores fall outside them. Purging old data reduces the impact of almost every confidentiality risk at once, including a breach at the SYS-01 vendor.
- **The channels the company builds itself (R-004, R-011, R-012, R-013, R-047).** The mail-in portal and partner API carry card entry and partner claims. Their design is sound, but secure development and recovery are informal.
- **Contracts as the sharpest consequences (R-015, R-016, R-017).** Losing Manufacturer A authorization or Partner P1 would cost more than most breaches.
- **AI adopted without governance (R-025 to R-031).** Five tools went live without review. P10 addresses them; R-029 (applicant ranking) carries employment law exposure.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-17, $646,000 one-time and $205,000 a year):**
- Standard bench image rollout with EDR at 14 stores and replacement of 31 legacy bench PCs ($160,000 one-time; $18,000 a year for EDR)
- Bench and customer-device VLAN at the 12 older stores ($140,000)
- SIEM onboarding of SYS-01, lab, and portal logs with bulk export use cases ($60,000 a year through the MSSP)
- Checkout page script monitoring service ($24,000 a year) and pipeline security scanning ($30,000 a year)
- Recovery testing program and alternate receiving at two large stores ($90,000)
- SOC 2 readiness support and the Type 2 examination ($180,000 across 2027)
- Encryption upgrade for the older lab storage shelf ($70,000)
- Enterprise generative AI assistant with data-use terms ($48,000 a year) and vendor risk tooling ($25,000 a year)
- Phishing-resistant security keys for administrators ($6,000)

No-cost or operating-budget actions due first: remove the "97% accurate" claim (R-026, due 2026-10-15); remove leaver accounts from the manufacturer portals before the audit (R-015); change CCTV recorder passwords (R-048); pause automatic applicant ranking (R-029); purge the 5 contact center tickets with card numbers (R-044). Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-030 (Low, Supply Chain Director), R-042 (Low, COO), R-043 (Low, COO), R-045 (Low, Director of Retail Operations).

**Contract actions:** security, data-use, and breach notice terms for the 7 vendors without them (R-025, R-032, R-033), due 2026-12-31; a technical interconnection schedule with both partners (R-011); recovery and 24-hour notice terms at the SYS-01 renewal (R-010, R-046).

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity, customer data, and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Service Ticketing and Point-of-Sale Platform (STPP; SSP in P02) | IT Director (Information Security Officer) | 26 risks whose affected assets include SYS-01, SYS-03 to SYS-07, or SYS-09 to SYS-11 (filter the `affected_asset_or_process` column) |
| Payment channels (PCI DSS; feeds the 2026 SAQ attestations) | Chief Financial Officer | R-004, R-009, R-044 |
| Partner claims fulfillment service (SOC 2 scope; P09) | Director of Partner Programs | R-011, R-012, R-016, R-046, R-047, R-050 |
| Customer devices and recovered data | Depot Director | R-001, R-005, R-006, R-008, R-033, R-036, R-037 |
| AI portfolio (P10) | Chief Operating Officer | R-025, R-026, R-027, R-028, R-029, R-030, R-031 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-042 and R-043, 2026-09-17. The Supply Chain Director (R-030) and the Director of Retail Operations (R-045) accepted their Low risks the same day.
- Chief Executive Officer: approved the 8 High-risk treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. Next report: 2026-12 quarterly meeting.
- Next full risk assessment: July 2027, or sooner after a major change (for example a new region, an acquisition, or a new partner integration) or a significant incident.
