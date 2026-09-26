# Risk Register Report: Cris Santos Company | Health Care and Social Assistance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Health Care and Social Assistance |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | HIPAA risk analysis and risk management, 45 CFR 164.308(a)(1)(ii)(A)-(B); input to the ASC all-hazards risk assessment, 42 CFR 416.54(a)(1) |
| Prepared | 2026-07-31 by the Security Manager and the vCISO; R-050 added 2026-08-14 from P07 testing |
| Approved | 2026-09-15: Chief Operating Officer (Moderate and below), Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (8 clinics, the ASC, the imaging center, the central business office, and enterprise functions), the Enterprise Clinical Platform (ECP, SYS-01 to SYS-08), the 140 vendors with PHI access (SYS-09), and the AI tools (SYS-10). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and control assessment (P07).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Operating Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the Chief Executive Officer and noted by the audit committee on 2026-09-15.

| Area | Appetite | Statement and measure |
|---|---|---|
| Patient safety | **Very low** | No cyber or technology risk that could plausibly cause patient harm is accepted above Low. Any such risk rated Moderate or higher must have a funded treatment plan within 90 days. Measure: number of safety-linked risks above Low (7 today: R-001, R-003, R-004, R-006, R-013, R-017, R-047; target 0 by 2027-12-31) |
| Confidentiality of PHI | **Low** | The company will not accept a risk of a breach affecting 500 or more patients above Moderate. Measure: R-002 and R-037 at Moderate or lower by 2027-06-30 |
| Availability of clinical operations | **Low** | Recovery capabilities must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months |
| Regulatory compliance | **Low** | No HIPAA Security Rule Required implementation specification may stay Not met or Partially met beyond 2027-06-30. The ASC must meet 42 CFR 416.54 at every survey |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives PHI without a BAA, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The company wants the benefits of AI in documentation, triage, and revenue cycle, but only through the AI governance process in P10. No AI tool touches PHI without review and a BAA |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $250,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that reduces likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Health Care overlay and HHS 405(d) threat themes (ransomware, email phishing, medical device attacks, third-party compromise), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, patient safety, reputation).
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 35 |
| Low | 6 |
| Very Low | 0 |
| **Total** | **50** |

Treatments: 46 Mitigate, 4 Accept (R-022, R-030, R-032, R-043). Status: 28 Open, 18 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $250,000 retention) transfers part of the financial exposure for R-001, R-002, and R-037. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to patients or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware halts clinics, the ASC, and the imaging center | Very High | Segment Clinics 4-8; extend privileged access management; restore tests for interface engine, PACS, data warehouse | IT Director (Security Officer) | 2027-03-31 |
| R-002 | PHI exfiltration for extortion | High | PACS, interface engine, and warehouse logs to SIEM; egress alerting | Security Manager | 2027-01-31 |
| R-009 | Privileged account takeover outside the cloud | High | Privileged access management for directory, IdP, EHR, and PACS admins; phishing-resistant MFA | Security Manager | 2027-03-31 |
| R-012 | Multi-week clearinghouse outage | High | Secondary clearinghouse; vendor outage runbook; cash-flow playbook | Director of Revenue Cycle | 2027-03-31 |
| R-013 | Extended EHR vendor outage beyond clinical MTDs | High | Recovery terms in contract; 15-minute ASC extract; downtime drills | Chief Operating Officer | 2027-03-31 |
| R-017 | Cyber event at the ASC without cyber-specific emergency procedures | High | Cyber hazards in the ASC plan; ASC cyber tabletop; training | ASC Administrator | 2026-12-15 |
| R-019 | AI scribe recording without documented all-party consent | High | Consent notice, script, EHR field, monthly audit | Chief Medical Officer | 2026-11-30 |
| R-037 | MSSP or EHR vendor remote access used as a supply-chain entry point | High | Annual SOC 2 and CUEC review; vendor access through the access broker | vCISO | 2027-03-31 |
| R-050 | PACS vendor service accounts with domain administrator rights (found in P07) | High | Remove rights; managed service accounts; vault secrets | Security Manager | 2026-10-31 |

**Themes.**
- **Recovery and segmentation (R-001, R-003, R-009, R-014 to R-016, R-050).** The company can detect attacks (EDR, MSSP, SIEM) and its backups are isolated, but it has not proven it can recover its own workloads, and flat networks at 5 sites would let an attack reach medical devices.
- **Third parties (R-010 to R-013, R-020, R-037, R-038).** Three single points of failure (EHR, clearinghouse, identity provider) and 30 vendors without BAAs.
- **AI adopted without governance (R-019 to R-025).** Four tools went live without review. P10 addresses them.
- **ASC resilience (R-006, R-013, R-017).** A CMS condition for coverage is at stake, not only IT risk.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-15, $1.15 million one-time and $420,000 a year):**
- Network segmentation at Clinics 4-8 and passive device discovery ($310,000)
- Privileged access management extension and phishing-resistant MFA for administrators ($180,000 one-time, $90,000 a year)
- EHR inappropriate-access analytics ($70,000 a year)
- SIEM onboarding of PACS, interface engine, data warehouse, and device monitoring ($120,000 a year through the MSSP)
- Recovery testing program and a secondary clearinghouse connection ($140,000)
- Vendor risk program tooling and one GRC analyst position ($140,000 a year)
- SOC 2 readiness and Type 2 examination ($220,000 across 2027)
- Replacement of the 2 legacy modality consoles (2027 capital plan, $300,000)

**Accepted (4):** R-022 (Low, CMO), R-030 (Moderate, COO; within appetite because backups are isolated and write-once), R-032 (Low, encrypted devices), R-043 (Low, vendor DDoS protection).

**Contract actions:** BAAs for 30 vendors and amended AI vendor BAAs (R-010, R-020, R-023), due 2026-12-31. EHR vendor recovery terms (R-013) at the 2027 renewal.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and technology resilience", owned by the COO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Enterprise Clinical Platform (ECP; SSP in P02) | IT Director (Security Officer) | 35 risks whose affected assets include SYS-01 to SYS-08 (filter the `affected_asset_or_process` column) |
| ASC (feeds the 42 CFR 416.54 all-hazards risk assessment) | ASC Administrator | R-001, R-004, R-006, R-013, R-017, R-033 |
| AI portfolio (P10) | Chief Medical Officer | R-019, R-020, R-021, R-022, R-023, R-024 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Operating Officer: approved Moderate and Low treatments and the acceptance of R-030, 2026-09-15.
- Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-15.
- Board audit committee: received the results on 2026-09-15. Next report: 2026-12 quarterly meeting.
- Next full risk analysis: July 2027, or sooner after a major change (for example an acquisition, R-048) or a significant incident.
