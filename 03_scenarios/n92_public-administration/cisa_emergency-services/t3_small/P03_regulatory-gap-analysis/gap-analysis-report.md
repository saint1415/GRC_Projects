# Regulatory Gap Analysis: Cris Santos Company | Emergency Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| Tier / Vertical | Small / Emergency Services |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) (C-EMERGENCY-R04) |
| Secondary regulation | EMS and ambulance records rules: Fla. Stat. 401.30 and Rule 64J-1.014, F.A.C.; Medicare ambulance documentation, 42 CFR 410.40(e), 410.41(c), 424.516(f) |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | IT Manager (Security Officer) with the Billing and Compliance Manager (Privacy Officer) |

## 1. Applicability
Applicability was checked first for every requirement in the vertical registry, because the Emergency Services sector research was written mostly for public agencies and 911 centers. A private ambulance company is a different kind of entity.

| Registry ID | Requirement | Applies? | Reason |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | **Yes** | See below |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | **No** | The policy governs access to criminal justice information (CJI). The company has no access to state or national criminal justice databases or to law enforcement records systems. The county CAD-to-CAD feed carries EMS incident data only (type, address, callback number, notes). Under 28 CFR 20.33(a)(7), a private contractor receives criminal history record information only under an agreement with a criminal justice agency, for the administration of criminal justice, with an approved security addendum. Ambulance transport is not that. **Trigger to recheck:** any proposal to show law enforcement premise, warrant, or officer-safety data in the company's CAD (P01 R-033) |
| C-EMERGENCY-R02, R03 | 28 CFR 20.21(f); 28 CFR Part 23 | **No** | These apply to state criminal history systems and to federally funded criminal intelligence systems. The company operates neither |
| C-EMERGENCY-R05 | CIRCIA | **Not yet (proposed only)** | No final rule was in the Federal Register as of 2026-09-25. The proposed rule would reach the company: proposed 6 CFR 226.2(b)(5) covers any entity that provides emergency medical services to a population of 50,000 or more, regardless of size, and the preamble says this criterion is meant to capture privately owned Emergency Services entities that fall under the SBA size standard. The company serves a county of about 400,000. Tracked in P08, not treated as an obligation |
| C-EMERGENCY-R06 | FCC EAS cybersecurity rule (47 CFR Part 11) | **No** | The company is not an EAS participant and does not originate public alerts |

**Why HIPAA applies.** A "covered entity" includes "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter" (45 CFR 160.103). The company furnishes and bills for health care, so it is a health care provider under the same section. It submits claims electronically to Medicare, Medicaid, and commercial plans. It must: Medicare pays an initial claim only if it is submitted electronically (42 CFR 424.32(d)(2)), and the small-supplier exception covers only suppliers with fewer than 10 full-time equivalent employees (424.32(d)(1)). The company has 60.

There is no size exemption. 45 CFR 164.306(b) lets the company consider its size, complexity, capabilities, and costs when choosing *how* to meet each standard, but not *whether* to meet it.

**Excluded HIPAA rows, with reasons (7):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): no governmental entity is the company's business associate. The county exchanges data with the company for dispatch and treatment.
- **164.314(b)** and its four implementation specifications (group health plans): the company does not administer a group health plan.

**Secondary regulation** (Small tier: primary plus the most relevant secondary). The most relevant secondary requirements are the **records rules that govern the same CAD and ePCR data**:
- Fla. Stat. 401.30 requires accurate records of emergency calls, a patient care record to the receiving hospital, and confidentiality of records with examination or treatment information.
- Rule 64J-1.014, F.A.C. requires that records be kept at least 5 years and that a patient care record be available to the receiving hospital on request within 48 hours of dispatch. Providers report to the state either electronically in the EMSTARS format or with quarterly aggregate reports on DH Form 1304. The rule's wording makes electronic EMSTARS submission one of two options, not the only one.
- Medicare requires certification statements on file for non-emergency transports (42 CFR 410.40(e)), ambulance billing and reporting rules (410.41(c)), and documentation kept for 7 years from the date of service (424.516(f)).

These rows are an **author mapping** to CSF 2.0 and SP 800-53. No official NIST mapping exists for them.

The HIPAA Breach Notification Rule (45 CFR 164.400-414) and Fla. Stat. 501.171 drive the notification matrix in P08.

## 2. Method
1. **Requirements.** HIPAA requirements and their Required/Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool). Secondary rows cite the statute, rule, or CFR paragraph directly.
2. **Crosswalk.** HIPAA rows were mapped to CSF 2.0 and SP 800-53 Rev. 5 using the Health Care crosswalk in `02_verticals/n62_health-care/`. That crosswalk is an author mapping, because NIST has not published a HIPAA to CSF 2.0 mapping. NIST's official SP 800-53 mapping (OLIR 110) is shown next to it in the `nist_official_sp800_53r5_1_1` column.
3. **Evidence.** Current state was established by interviews (COO, IT Manager, Communications Center Supervisor, Operations Manager, Billing and Compliance Manager, Clinical Services Coordinator, HR Manager), document review, configuration exports, a sample of 8 departures, a sample of 20 non-emergency claims, and a walkthrough of headquarters, Station 2, and two ambulances.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable.

**Addressable is not optional.** For each addressable specification, the company must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented. One exception is documented as an equivalent alternative: dispatch consoles do not auto-lock (164.312(a)(2)(iii)) because dispatchers must see live calls, so the badge-controlled dispatch room serves as the equivalent measure.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 5 | 18 | 6 | 1 |
| 164.310 Physical safeguards | 2 | 8 | 2 | 0 |
| 164.312 Technical safeguards | 2 | 9 | 1 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 4 | 1 | 0 |
| **HIPAA Security Rule total (69)** | **9** | **43** | **10** | **7** |
| Florida EMS records rules (5) | 2 | 3 | 0 | 0 |
| Medicare ambulance documentation (3) | 1 | 1 | 1 | 0 |
| **All rows (77)** | **12** | **47** | **11** | **7** |

Of the 53 unmet or partially met HIPAA rows, 20 are standards, 18 are **Required** implementation specifications, and 15 are **Addressable** specifications. Across all 58 unmet or partially met rows, gap risk is High for 8, Moderate for 31, and Low for 19.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No contingency or disaster recovery plan; manual dispatch not drilled; backups exposed and untested | 164.308(a)(7), (7)(ii)(A)-(D) | High | Contingency plan from the BIA; immutable separate-account backups; quarterly restore tests and manual dispatch drills | IT Manager; Communications Center Supervisor | 2026-12-31 (first restore test 2026-10-15) |
| No EDR; dispatch consoles unpatched | 164.308(a)(5)(ii)(B) | High | MSP-managed EDR with 24x7 alerting; monthly console patching | IT Manager | 2026-12-31 |
| CAD without MFA; router default passwords | 164.312(d) | High | CAD federation with MFA; central router management | IT Manager | 2026-12-31 |
| Treatments approved but not yet in place | 164.308(a)(1)(ii)(B) | High | Execute funded treatments | IT Manager | 2027-05-31 |
| Shared CAD logins | 164.312(a)(2)(i) | Moderate | Named CAD accounts through the identity provider | Communications Center Supervisor | 2026-12-31 |
| No audit log, CAD query, or ePCR access review | 164.308(a)(1)(ii)(D) | Moderate | Monthly ePCR and CAD review; weekly identity review | Billing and Compliance Manager | 2026-10-31 |
| Missing BAAs (hosted phone; AI triage service) | 164.308(b)(1), 164.314(a) | Moderate | Execute BAA and amendment or replace vendor | COO | 2026-10-31 |
| No HIPAA sanctions policy | 164.308(a)(1)(ii)(C) | Moderate | Sanctions procedure | COO | 2026-11-30 |
| Late account removal for field staff | 164.308(a)(3)(ii)(C) | Moderate | Same-day disable; federated ePCR | HR Manager | 2026-10-31 |
| No break-glass access | 164.312(a)(2)(ii) | Moderate | Two offline emergency accounts; sealed CAD admin credential | IT Manager | 2026-10-31 |
| PCS documentation not kept 7 years or linked to claims | 42 CFR 424.516(f); 410.40(e) | Moderate | Attach PCS to the billing record; 7-year retention | Billing and Compliance Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. A Federal Register search on 2026-09-26 found no final rule. The regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, these items from the proposal would affect the company:
- The distinction between "required" and "addressable" would be removed. The 15 addressable gaps above would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (dispatch consoles, office desktops, and facility email).
- MFA would be required for technology assets (CAD today has none).
- A written technology asset inventory and network map would be required (MDCs, routers, and cardiac monitors are missing today).
- Penetration testing would be required at least once every 12 months, along with vulnerability scanning.
- Certain systems and data would have to be restorable within 72 hours.
- A compliance audit would be required at least once every 12 months.
- Business associates would have to give notice within 24 hours of activating their contingency plan.

**CIRCIA** (C-EMERGENCY-R05) is also still proposed. As drafted it would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. See section 1 for why the proposal would reach this company.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected HIPAA row. None of these is treated as a current obligation.
