# Risk Register Report: Cris Santos Company | Educational Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Size tier | Mid-Market (600 employees) |
| Vertical | Educational Services |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2, I-3 values); enterprise roll-up per NIST IR 8286 Rev. 1 |
| Also satisfies | The written risk assessment required by the FTC Safeguards Rule, 16 CFR 314.4(b) and (b)(1)(i)-(iii), and its periodic reassessment, 314.4(b)(2) |
| Prepared | 2026-07-31 by the Information Security Manager and the vCISO (Qualified Individual); R-038 added 2026-08-14 from P07 testing |
| Approved | 2026-09-17: Chief Information Officer (Moderate and below), President and Chief Executive Officer (High and Very High); presented to the board audit committee the same day |

## 1. Scope and risk framing
**Scope.** All business units (3 campuses, the online division, student financial services, enrollment management, academic and student affairs, corporate partnerships, and enterprise support), the Student Information and Learning Platform (SILP, the SSP system in P02), the campus safety systems, the about 90 vendors with student data (SYS-15), and the AI tools (SYS-16). Processes and impact values come from the BIA (P05); vulnerabilities come from the gap analysis (P03) and control assessment (P07).

**How this meets 314.4(b)(1).** The rule requires a written risk assessment with (i) criteria for evaluating and categorizing risks, (ii) criteria for assessing confidentiality, integrity, and availability, including the adequacy of existing controls, and (iii) requirements for how risks will be mitigated or accepted. Section 2 gives (i) and (ii); the tolerance table below and section 4 give (iii).

**Who can accept risk (tolerance).**
| Risk level | Who may accept | Conditions |
|---|---|---|
| Very Low and Low | The risk owner (director level or above) | Recorded in the register; reviewed annually |
| Moderate | Chief Information Officer | Treatment plan or documented reason; reviewed every 6 months |
| High | President and Chief Executive Officer | Temporary only (up to 12 months) with a dated treatment plan; reported to the audit committee each quarter |
| Very High | Not acceptable | The CEO may approve a temporary exception of up to 90 days only after notifying the audit committee chair, while treatment is under way |

### Risk appetite statements
Approved by the President and CEO and noted by the audit committee on 2026-09-17; the board approves them with the Qualified Individual's annual report on 2026-10-22.

| Area | Appetite | Statement and measure |
|---|---|---|
| Student and staff safety | **Very low** | No cyber risk that could delay a Clery emergency notification or disable physical security is accepted above Low. Measure: safety-linked risks above Low (4 today: R-003, R-004, R-022, R-038; target 0 by 2027-06-30) |
| Student financial harm | **Low** | Students must not lose living funds to fraud the college could reasonably prevent. Measure: diverted refunds (23 cases in 2025-26; target 0 a term after step-up authentication goes live); R-005 at Low by 2027-03-31 |
| Confidentiality of customer information and education records | **Low** | The college will not accept a risk of a breach affecting 500 or more consumers above Moderate. Measure: R-002, R-008, R-009, and R-037 at Moderate or lower by 2027-06-30 |
| Title IV compliance | **Very low** | No Safeguards Rule element may stay Not met beyond 2027-06-30, and no annual compliance audit may report a repeat GLBA finding. HEA limits on FAFSA data are never knowingly exceeded (R-011) |
| Availability of teaching and student services | **Low** | Recovery must meet the BIA RTOs for all High-criticality processes (P05). Measure: every High process has a passed recovery test in the last 12 months |
| Third parties | **Moderate**, with conditions | Vendors are used widely, but no vendor receives student data without FERPA school-official and security terms, and every Tier 1 vendor is reassessed each year (P09) |
| Innovation and AI | **Moderate** | The college wants AI's benefits in admissions, advising, and teaching, but only through the P10 governance process. No AI tool influences admission, discipline, or academic standing without human review and bias testing |
| Financial loss from cyber events | **Moderate** | Single-event losses up to the $150,000 insurance retention are tolerable. Scenarios above $2 million need a treatment that lowers likelihood, not only insurance |

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the Educational Services overlay (ransomware with student record exposure, account takeover, fraudulent applicants, third-party compromise), the BIA, interviews with every process owner, the gap analysis (P03), and the control assessment (P07).
2. **Rate likelihood (criteria for evaluating risks, 314.4(b)(1)(i)).** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were each rated, then combined with **Table G-5**.
3. **Rate impact (confidentiality, integrity, and availability criteria, 314.4(b)(1)(ii)).** Impact used **Table H-3**, anchored to the BIA impact categories (cost, operations, regulatory, student safety and welfare, reputation). Existing controls are listed for each risk and were weighed in the likelihood of adverse impact.
4. **Determine risk.** Risk level came from **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the two tables, not assigned by hand.
5. **Semi-quantitative view.** `semi_quant_score` gives each risk level its SP 800-30 Appendix I semi-quantitative value (Very High 10, High 8, Moderate 5, Low 2, Very Low 0). `exposure_estimate_usd` gives an order-of-magnitude single-event loss range from the BIA values, used for the enterprise risk roll-up (NIST IR 8286 Rev. 1). The ranges are estimates for prioritizing, not actuarial figures.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 8 |
| Moderate | 34 |
| Low | 9 |
| Very Low | 0 |
| **Total** | **52** |

Treatments: 47 Mitigate, 4 Accept (R-043, R-044, R-047, R-048), and 1 Share/Transfer (R-051). Status: 38 Open, 10 In progress, 4 Accepted.

Cyber insurance ($5 million limit, $150,000 retention) transfers part of the financial exposure for R-001, R-002, and R-037. It is not recorded as the treatment for any risk, because it does not lower the likelihood of harm to students or operations.

### Top risks (Very High and High)
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware halts aid processing, refunds, and campus operations | Very High | IT DR plan; restore tests; Campus 3 segmentation; privileged access management for SaaS administrators | Chief Information Officer | 2027-03-31 |
| R-002 | Student and aid records exfiltrated for extortion | High | SIS, FAMS, and LMS logs to the SIEM; egress alerting; warehouse role-based views | Information Security Manager | 2027-01-31 |
| R-004 | Emergency notification delayed by an identity outage | High | Break-glass and secondary sign-in for the notification console | Director of Campus Safety | 2026-11-30 |
| R-005 | Student portal takeover and refund diversion | High | Step-up MFA and confirmation for bank changes; refund hold; student MFA by default | Chief Information Officer | 2027-03-31 |
| R-006 | Fraudulent online applicants receive Title IV funds | High | Document and liveness verification; fraud indicators; OIG referral procedure | Vice President of Enrollment Management | 2027-01-31 |
| R-008 | Third-party servicer account compromise (no MFA) | High | Contract amendment; federation with MFA; incident notice terms | Director of Financial Aid | 2026-10-31 |
| R-009 | SaaS administrator account takeover | High | Separate admin accounts; FIDO2 keys; privileged access management | Information Security Manager | 2027-03-31 |
| R-011 | FAFSA-derived data used beyond HEA purposes | High | Remove ISIR fields from the warehouse; data use review | Director of Financial Aid | 2026-11-30 |
| R-037 | MSSP or SIS vendor compromise as a supply-chain entry point | High | Annual SOC 2 and CUEC review; brokered vendor actions | vCISO (Qualified Individual) | 2027-03-31 |

**Themes.**
- **Identity is the attack surface (R-005, R-006, R-007, R-008, R-009, R-042).** The college's most frequent real losses come from weak student and partner authentication and from identity fraud at admission, not from malware.
- **Recovery is unproven (R-001, R-013 to R-018).** Backups are isolated, but nothing the college runs itself has been restored, and there is no IT DR plan.
- **Data use, not only data security (R-011, R-032).** FAFSA-derived data has drifted into analytics and an AI model.
- **AI adopted without governance (R-031 to R-035, R-052).** Five tools went live without review. P10 addresses them.
- **Campus safety depends on IT (R-003, R-004, R-022, R-038).** A Clery emergency procedure is at stake, not only IT risk.

## 4. Treatment summary
**Funded in the FY2027 security plan (approved by the President and CEO 2026-09-17, $980,000 one-time and $390,000 a year):**
- Student identity: step-up authentication, MFA by default, and applicant document and liveness verification ($160,000 one-time, $85,000 a year)
- Privileged access management for SaaS administrators and FIDO2 keys ($120,000 one-time, $45,000 a year)
- SIEM onboarding of SIS, FAMS, and LMS logs and new detection use cases ($140,000 a year through the MSSP)
- IT DR plan, restore testing program, and tabletop facilitation ($110,000)
- Campus 3 segmentation and lab isolation ($180,000)
- Vendor risk program and contract amendments, plus one GRC analyst position already budgeted ($40,000 one-time, $120,000 a year)
- SOC 2 readiness and the Type 2 examination for the employer education services ($190,000 across 2027)
- Campus safety controller and recorder replacement (2027 capital plan, $180,000)

Smaller items (copier sanitization terms, the emergency notification break-glass account, the retention schedule) are funded from operating budgets. Each funded item maps to a P07 POA&M entry.

**Accepted (4):** R-043 (Low, CIO), R-044 (Low, CIO), R-047 (Low, CIO; full-disk encryption), R-048 (Low, Chief Compliance Officer). **Shared (1):** R-051 (Low; card handling sits with PCI DSS-validated vendors by contract).

**Contract actions:** servicer amendment (R-008) by 2026-10-31; FERPA and security terms for 22 vendors and the AI-003 and AI-004 vendors (R-010, R-033, R-034) by 2026-12-31; SIS recovery terms (R-013) at the 2027 renewal.

## 5. Enterprise and system-level registers
This file is the **enterprise register**. Following NIST IR 8286 Rev. 1, it rolls up to the college's enterprise risk register as one line, "Cybersecurity, student data, and technology resilience", owned by the CIO and reported to the audit committee each quarter with the counts above and the top risks.

System-level registers are filtered views of this file, kept by each system owner, rather than separate spreadsheets. That keeps one set of ratings.

| System-level register | Owner | Risks in scope |
|---|---|---|
| Student Information and Learning Platform (SILP; SSP in P02) | Chief Information Officer | 38 risks whose `affected_asset_or_process` cites a SILP component (SYS-01, SYS-02, SYS-03, SYS-04, SYS-06, SYS-08, SYS-10, SYS-11, SYS-14) |
| Student financial services (Title IV) | Chief Financial Officer | R-005, R-006, R-008, R-011, R-012, R-018, R-024, R-027 |
| Campus safety (feeds the Clery emergency procedures) | Director of Campus Safety | R-003, R-004, R-022, R-038 |
| AI portfolio (P10) | Provost and Chief Academic Officer | R-031, R-032, R-033, R-034, R-035, R-052 |

When a system-level review changes a rating, the owner updates this file, and the change flows to the enterprise roll-up.

## 6. Approval
- Chief Information Officer: approved Moderate and Low treatments and the acceptance of R-043, R-044, and R-047, 2026-09-17.
- Chief Compliance Officer: accepted R-048, 2026-09-17.
- President and Chief Executive Officer: approved the High and Very High treatment plans, the risk appetite statements, and the FY2027 security budget, 2026-09-17.
- Board audit committee: received the results on 2026-09-17. The Qualified Individual's written report to the full board (314.4(i)) on 2026-10-22 will summarize them.
- Next full risk assessment: July 2027, or sooner after a material change (for example a new campus or a new AI use) or a significant incident, as 314.4(b)(2) requires.
