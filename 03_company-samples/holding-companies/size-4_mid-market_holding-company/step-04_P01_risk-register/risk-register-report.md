# Risk Register Report: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| Size tier | Mid-Market (600 employees across the group) |
| Vertical | Management of Companies and Enterprises |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | Finance's written risk assessment under the FTC Safeguards Rule (16 CFR 314.4(b)(1)-(2)); the group health plan's HIPAA risk analysis and risk management (45 CFR 164.308(a)(1)(ii)(A)-(B)) |
| Prepared | 2026-08-07 by the Security Manager (Qualified Individual for Finance) and the vCISO; R-047 and R-050 added 2026-08-26 from P07 testing |
| Approved | 2026-09-22: CFO (Moderate and below), CEO (High and Very High), board (risk appetite); presented to the audit committee the same day |

## 1. Scope and risk framing
**Scope.** The Shared Corporate Services Platform (SCSP, SYS-01 to SYS-11 and SYS-16) and every business process in the BIA (P05), for the holding company and all four subsidiaries, including Home Services North. The register also covers the subsidiary systems that connect to the shared platform (SYS-12 to SYS-15) and the third parties that support it (SYS-17). Processes and impact values come from the BIA; vulnerabilities come from the gap analysis (P03) and the control assessment (P07).

**Why one register for the group.** The subsidiaries share one identity service, one email and file tenant, one ERP, one cloud landing zone, and one IT and security team. A risk to the shared platform is a risk to every subsidiary at once, so risks are assessed at group level, and each risk names the subsidiary data or process it affects where that differs.

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | CFO | Treatment plan or documented reason; reviewed every 6 months |
| High | CEO | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The board may approve a temporary exception of up to 90 days, on the audit committee's recommendation, while treatment is under way |

Two extra rules apply because of the group's regulated data:
- Subsidiary Presidents may not accept risks to the shared platform, to Finance customer information, or to plan PHI.
- Any risk to Finance customer information rated Moderate or above is reported to Finance's Board of Managers in the Qualified Individual's annual report (16 CFR 314.4(i)(2)), and any risk to plan PHI rated Moderate or above is reported to the Benefits Committee.

### Risk appetite statements
Approved by the board on 2026-09-22 on the CEO's recommendation, replacing the one-paragraph 2025 statement (gap 1).

| Area | Appetite | Statement and measure |
|---|---|---|
| Safety of customers and workers | **Very low** | No technology risk that could plausibly harm a customer or worker is accepted above Low. Measure: safety-linked risks above Low (1 today: R-026, High; R-049 is Low already; target 0 above Low by 2027-06-30) |
| Customer and plan data (Finance customer information, plan PHI, employee SSNs) | **Low** | No risk of a breach affecting 500 or more people is accepted above Moderate after 2027-06-30. Measure: R-002 and R-011 at Moderate or lower by that date |
| Payment integrity | **Low** | No single fraudulent payment over the crime policy's $250,000 social engineering sublimit is tolerable. Measure: R-005, R-006, and R-050 at Moderate or lower by 2026-12-31 |
| Availability of subsidiary operations | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: each High process has a passed recovery test in the last 12 months (2 of 7 today) |
| Regulatory compliance | **Low** | No Safeguards Rule element and no HIPAA Required implementation specification may stay Not met after 2027-03-31 |
| Acquisitions | **Moderate**, with conditions | The group will keep buying companies, but no acquired company connects to group systems before a compromise assessment and the day-1 control set (POL-01 4.13). Measure: Home Services North integrated by 2027-03-31 |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but every critical vendor is reviewed each year (P09). Measure: 22 of 22 critical vendors reviewed by 2027-03-31 (8 today) |
| Innovation and AI | **Moderate** | The group wants the benefits of AI, but any AI use that affects credit, employment, or customer safety is High tier and needs CEO approval (P10) |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $200,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the vertical overlay, the BIA, interviews with every process owner and subsidiary President at 6 of 9 sites, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact.** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, safety, reputation). Harm to more than one subsidiary, or to Finance customer information or plan PHI, raised the rating by one level where it was not already High.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each level its SP 800-30 Appendix I value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 9 |
| Moderate | 30 |
| Low | 12 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 48 Mitigate, 4 Accept (R-037, R-040, R-044, R-048). Status: 38 Open, 10 In progress, 4 Accepted.

Cyber insurance ($10 million limit, $200,000 retention) and the crime policy ($250,000 social engineering sublimit) transfer part of the financial exposure for R-001, R-002, R-005, and R-011. Insurance is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to customers, employees, or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware across all subsidiaries after directory takeover | Very High | Directory tiering and privileged access management; off-site backups for HQ and plant; forest recovery test; plant segmentation; integrate Home Services North | VP of Information Technology | 2027-03-31 |
| R-002 | Exfiltration of Finance, plan, and employee data (double extortion) | High | Forward warehouse, file server, and SaaS logs; egress alerting; restrict the HR site; data map | Security Manager | 2027-03-31 |
| R-003 | Adversary-in-the-middle phishing of high-risk users | High | FIDO2 keys for about 70 users; compliant-device access for all | Security Manager | 2027-03-31 |
| R-004 | Directory compromise carried to the cloud by synchronization | High | Tier 0 model; service accounts out of Domain Admins; MFA for directory administration | Security Manager | 2027-03-31 |
| R-005 | Business email compromise redirects a supplier payment | High | Callback evidence in the ERP; 5-day hold; North payments into the ERP | Controller | 2026-12-31 |
| R-007 | Entry through unintegrated Home Services North | High | Day-1 controls now; full integration | VP of Information Technology | 2027-03-31 |
| R-011 | Bulk export of Finance customer information | High | Servicing logs to the SIEM; export alerts; fewer export rights | Finance President | 2027-03-31 |
| R-024 | Credit scorecard declines on a prohibited basis or with non-specific reasons | High | Specific reasons; validation and outcome testing; manual review of auto-declines | Finance President | 2026-12-31 |
| R-026 | AI voice agent mishandles an emergency call | High | Hard-coded escalation; live transfer; monthly test calls | Home Services President | 2026-11-30 |
| R-050 | ACH signing account password exposed in an IT runbook (found in P07) | High | Rotate and vault; restrict; file integrity check | Security Manager | 2026-10-31 |

**Themes.**
- **Identity is the group's front door and its weakest seam (R-001, R-003, R-004, R-036).** One directory and one identity provider serve every company, so one takeover reaches all of them.
- **Growth outpaced governance (R-007, R-030, R-052).** An acquisition joined without cyber due diligence, and subsidiaries bought AI tools on their own.
- **Payments are the most likely target (R-005, R-006, R-050).** The holding company moves about $3.5 million a business day for five companies.
- **AI now touches credit, hiring, and customer safety (R-023 to R-027).** Three uses are High tier under P10.
- **Visibility ends at the core (R-002, R-011, R-018).** The data attackers want most sits in systems that do not log to the SIEM.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the CEO 2026-09-22 and noted by the board; $905,000 one-time and $420,000 a year):**
- Privileged access management, directory tiering, and FIDO2 keys ($210,000 one-time; $85,000 a year)
- Home Services North integration ($160,000 one-time)
- Off-site immutable backups for HQ and plant servers and directory recovery tooling ($95,000 one-time; $30,000 a year)
- SIEM source expansion through the MSSP ($110,000 a year)
- Plant network segmentation and brokered vendor access ($140,000 one-time)
- Vulnerability scanning at all 9 sites ($45,000 a year)
- Vendor risk program tooling and a second GRC analyst ($150,000 a year)
- Independent validation of the credit scorecard ($60,000 one-time)
- SOC 2 readiness and the Type 1 and Type 2 examinations for the bank partner ($240,000 across 2027)

Smaller items (callback evidence in the ERP, the out-of-band messaging group, the plant cellular kit, training modules) are funded from the operating budget. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-037 (Low, VP of Information Technology; encrypted devices), R-040 (Moderate, CFO; within appetite because cloud backups are isolated and write-once), R-044 (Low, Supply President; card data never enters group systems), R-048 (Low, Supply President; dual circuits meet the BIA).

**Contract actions:** recovery terms with the distribution system vendor (R-019) at the 2027-03 renewal; shorter breach notice terms with the TPA and PBM (R-051); security terms with machine vendors and an exit from the seller's IT provider (R-007, R-015).

**No High or Very High risk was accepted without treatment.**

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the company's enterprise risk register as one line, "Cybersecurity and technology resilience", owned by the CFO and reported to the audit committee each quarter with the counts above, the top risks, and the appetite measures in section 1.

System-level and entity-level registers are filtered views of this file, kept by their owners, rather than separate spreadsheets. That keeps one set of ratings.

| Register | Owner | Risks in scope |
|---|---|---|
| Shared Corporate Services Platform (SSP in P02) | CFO (system owner), maintained by the Security Manager | 35 risks whose affected assets include SYS-01 to SYS-11 or SYS-16 (filter the `affected_asset_or_process` column) |
| Finance customer information (Safeguards Rule risk assessment, 16 CFR 314.4(b)) | Finance President with the Qualified Individual | 18 risks citing 16 CFR 314 in `regulatory_driver`: 1 Very High, 5 High, 10 Moderate, 2 Low |
| Group health plan ePHI (HIPAA risk analysis, 164.308(a)(1)(ii)(A)) | VP of Human Resources (Privacy Official) with the Security Manager (Security Official) | 13 risks citing N55-R06: 1 Very High, 3 High, 8 Moderate, 1 Low |
| Fabrication plant | Fabrication President | R-015, R-016, R-017, R-033, R-049 |
| AI portfolio (P10) | CFO | R-023, R-024, R-025, R-026, R-027 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- CFO: approved Moderate and Low treatments and the acceptance of R-040, 2026-09-22.
- CEO: approved the High and Very High treatment plans and the FY2027 security budget, 2026-09-22.
- Board: approved the risk appetite statements, 2026-09-22; the audit committee received the results the same day. Next report: the 2026-12 quarterly meeting.
- Finance's Board of Managers: received the Finance view of this register with the Qualified Individual's 2026 written report, 2026-09-22.
- Benefits Committee: accepted the plan view as the plan's 2026 risk analysis, 2026-09-22.
- Next full assessment: July 2027, or sooner after an acquisition, a major change, or a significant incident.
