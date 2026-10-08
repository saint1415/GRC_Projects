# Regulatory Gap Analysis: Cris Santos Company | Health Care and Social Assistance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| Tier / Vertical | Small / Health Care and Social Assistance |
| Regulation analyzed | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | IT Manager (Security Officer) with the Privacy Officer |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rule analyzed here. The HIPAA Security Rule **applies**. The practice is a health care provider that transmits health information electronically in standard transactions (claims and eligibility through its clearinghouse). That makes it a covered entity under 45 CFR 160.103.

There is no size exemption. 45 CFR 164.306(b) lets the practice consider its size, complexity, capabilities, and costs when choosing *how* to meet each standard, but not *whether* to meet it.

**Excluded, with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the practice is not a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): none exist.
- **164.314(b)** (group health plans): the practice does not administer a group health plan.

**Secondary regulations considered** (Small tier: primary plus the most relevant secondary):
- The HIPAA Breach Notification Rule (45 CFR 164.400-414) drives the notification matrix in P08.
- 42 CFR Part 2 does not apply, because the practice runs no federally assisted SUD program.

## 2. Method
1. **Requirements.** Requirements and their Required/Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool).
2. **Crosswalk.** Each requirement was mapped to CSF 2.0 and SP 800-53 Rev. 5 using the Health Care crosswalk in `02_industry-rules/health-care/`. That crosswalk is an author mapping; NIST's official mapping is not yet published for CSF 2.0.
3. **Evidence.** Current state was established from the intake evidence (exports, documents and the walk-through of both clinics on 2026-07-09), the TLS scan (EV-034), and gap analysis interviews with the Practice Administrator, IT Manager, Clinic Managers, Billing Manager and HR (EV-035). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable.

**Addressable is not optional.** For each addressable specification, the practice must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented; none is being documented as unreasonable.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 5 | 17 | 7 | 1 |
| 164.310 Physical safeguards | 1 | 9 | 2 | 0 |
| 164.312 Technical safeguards | 4 | 7 | 1 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 4 | 1 | 0 |
| **Total (69)** | **10** | **41** | **11** | **7** |

Of the 52 unmet or partially met rows, 18 are standards, 18 are **Required** implementation specifications, and 16 are **Addressable** specifications.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No contingency plan, DR plan, or backup testing; backups exposed | 164.308(a)(7), (7)(ii)(A)-(D) | High | Contingency plan from the BIA; immutable separate-account backups; quarterly restore tests | IT Manager | 2026-12-31 (first restore test 2026-10-15) |
| No EDR; signature antivirus only | 164.308(a)(5)(ii)(B) | High | MSP-managed EDR with 24x7 alerting | IT Manager | 2027-01-31 |
| No audit log or access review | 164.308(a)(1)(ii)(D) | Moderate | Monthly EHR access review; weekly identity sign-in review | Privacy Officer | 2026-10-31 |
| Missing BAAs (fax, telehealth, AI scribe) | 164.308(b)(1), 164.314(a) | Moderate | Execute BAAs or replace vendors | Practice Administrator | 2026-10-31 |
| No HIPAA sanctions policy | 164.308(a)(1)(ii)(C) | Moderate | Sanctions procedure | Practice Administrator | 2026-11-30 |
| Late account terminations | 164.308(a)(3)(ii)(C) | Moderate | Same-day disable | HR and Payroll Specialist | 2026-10-31 |
| Unencrypted desktops | 164.312(a)(2)(iv) | Moderate | Full-disk encryption | IT Manager | 2026-11-30 |
| No break-glass access | 164.312(a)(2)(ii) | Moderate | Two offline emergency accounts | IT Manager | 2026-10-31 |
| No downtime procedures | 164.308(a)(7)(ii)(C) | Moderate | Paper downtime kits | Clinic Managers | 2026-12-31 |
| Shared login on the X-ray modality | 164.312(a)(2)(i) | Moderate | Named accounts or replacement | Clinic A Manager | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, these items verified in the proposal text would affect this practice:
- The distinction between "required" and "addressable" would be removed. The 16 addressable gaps above would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (desktop encryption and external email).
- MFA would be required for technology assets.
- A written technology asset inventory and network map would be required (medical devices and network gear are missing today).
- Penetration testing would be required at least once every 12 months, along with vulnerability scanning.
- Certain systems and data would have to be restorable within 72 hours.
- A compliance audit would be required at least once every 12 months.
- Business associates would have to give notice within 24 hours of activating their contingency plan.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these is treated as a current obligation.
