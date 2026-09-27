# Regulatory Gap Analysis: Cris Santos Company | Healthcare and Public Health | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital, 12 beds, 24-hour ED) |
| Tier / Vertical | Small / Healthcare and Public Health |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24; eCFR text checked as of 2026-09-23) |
| Secondary regulation | CMS emergency preparedness condition of participation for CAHs, 42 CFR 485.625 (cyber-relevant parts) |
| Voluntary benchmark | HHS Healthcare and Public Health Cybersecurity Performance Goals (CPGs), in `cpg-benchmark.csv` |
| Assessment dates | 2026-07-13 to 2026-07-24; status updated to reflect documents approved 2026-08-31 |
| Assessor | IT Manager (Security Officer) with the Quality and Compliance Manager (Privacy Officer) and the Facilities Manager (Emergency Preparedness Coordinator) |

## 1. Applicability
**HIPAA Security Rule: applies.** The hospital is a health care provider that transmits health information electronically in standard transactions (claims and eligibility through its clearinghouse), so it is a covered entity under 45 CFR 160.103. There is no size exemption. 45 CFR 164.306(b) lets the hospital weigh its size, complexity, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it.

HIPAA rows excluded, with reasons:
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the hospital is not a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): none exist. The state health department receives public health reports as a permitted disclosure, not as a business associate.
- **164.314(b)** and its four implementation specifications (group health plans): the employee plan is fully insured, and the hospital as plan sponsor receives only summary health information and enrollment information, which 164.314(b)(1) excludes.

**CMS emergency preparedness: applies, and it is the most relevant secondary regulation.** The hospital is a Medicare-participating critical access hospital, so its emergency preparedness condition is **42 CFR 485.625**, the CAH counterpart of the hospital rule at 482.15 that the vertical registry lists (C-HPH-R07). The rule has no size threshold. It is chosen as the secondary regulation because it is binding, it is surveyed, and a ransomware attack that takes away the EHR is exactly the kind of all-hazards emergency the plan must handle. The analysis covers the program and each standard, and it decomposes the elements with a cyber or information dimension: the risk assessment and strategies (a)(1)-(a)(4), medical documentation (b)(5), patient transfer arrangements (b)(7), communications (c)(3), (c)(4), (c)(7), and training, testing, and after-action review (d). Elements with no cyber dimension (subsistence, evacuation, sheltering, volunteers, 1135 waivers) are outside this analysis and remain with the Emergency Preparedness Coordinator. Paragraph (e) (emergency power) is included at the standard level only because the generator monitoring panel sits on the hospital network. Paragraph (f) (integrated health systems) does not apply: the hospital is independent.

**Other obligations screened (not analyzed row by row):**

| Obligation | Decision | Basis |
|---|---|---|
| HIPAA Breach Notification Rule (C-HPH-R02), 45 CFR 164.400-414 | Applies | Drives the P08 notification matrix |
| Fla. Stat. 501.171 | Applies | Florida breach notice; in the P08 matrix |
| EMTALA, 42 CFR 489.24 | Applies | 489.24(b) defines "hospital" to include a CAH. Governs how the ED may use diversion during an IT outage (P08) |
| Medicare Promoting Interoperability Program, 42 CFR 495.24 | Applies (payment program) | CAHs attest to a security risk analysis under 45 CFR 164.308(a)(1). For 2023 and later, a CAH must meet the objectives and measures CMS selects for each EHR reporting period (495.24(f)(1)(i)(A)); confirm the current list in the latest IPPS final rule. P01 supports the attestation |
| Section 1557, 45 CFR 92.210 (parent vertical ID N62-R07) | Applies | Medicare Part A and Medicaid are federal financial assistance. Drives the sepsis model review in P10 |
| HHS HPH CPGs (C-HPH-R08) and 405(d) HICP (C-HPH-R09) | Voluntary | HHS describes the CPGs as a voluntary subset of practices. HICP (2023 edition) classes hospitals of 1-50 beds as small organizations, so Technical Volume 1 applies. Neither is incorporated into 485.625 |
| HITECH recognized security practices (C-HPH-R10), 42 U.S.C. 17941 | Applies as a mitigating factor | OCR must consider recognized security practices in place for the prior 12 months. Operating the CPGs and HICP practices now builds that record |
| FDA sec. 524B (C-HPH-R04) | Does not apply directly | Duties fall on device manufacturers. The hospital uses it as a procurement lever (SBOM, MDS2, patch support) |
| FTC Health Breach Notification Rule (C-HPH-R05) | Does not apply | 16 CFR 318.1 excludes HIPAA covered entities |
| 42 CFR Part 2 (C-HPH-R06) | Excluded | Scoping decision; also screened: the hospital is not a Part 2 program (see `../00_company-facts.md`) |
| CIRCIA (C-HPH-R11) | Not in effect | Proposed 6 CFR 226.2 would cover critical access hospitals regardless of size. No final rule as of 2026-09-26. Tracked for P08 |

## 2. Method
1. **Requirements.** HIPAA requirements and their Required and Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool). NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis uses the current rule's 164.308(b)(3). The 485.625 rows follow the regulation's own paragraph structure (eCFR, 2026-09-23); summaries are paraphrased.
2. **Crosswalk.** HIPAA rows use the Health Care crosswalk in `02_industry-rules/health-care/`: the CSF 2.0 and SP 800-53 columns are an author mapping, and NIST's official OLIR 110 mapping (SP 800-53 Rev. 5.1.1) is shown next to it in `nist_official_sp800_53r5_1_1`. No official NIST mapping exists for 485.625, so those rows are an author mapping.
3. **Evidence.** Interviews (CEO, IT Manager, Director of Nursing, Facilities Manager, Laboratory and Imaging Managers, HIM Manager, Business Office Manager, HR Manager), document review, configuration exports, and a walkthrough of the hospital on 2026-07-16.
4. **Status.** Each row is Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Addressable is not optional.** For each addressable specification, the hospital must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented; none is being documented as unreasonable.

## 3. Results summary
**HIPAA Security Rule (69 rows)**

| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 3 | 20 | 6 | 1 |
| 164.310 Physical safeguards | 2 | 10 | 0 | 0 |
| 164.312 Technical safeguards | 1 | 11 | 0 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 4 | 1 | 0 |
| **Total (69)** | **6** | **49** | **7** | **7** |

Of the 56 unmet or partially met HIPAA rows, 20 are standards, 19 are **Required** implementation specifications, and 17 are **Addressable** specifications. By gap risk: 8 High, 29 Moderate, 19 Low.

**CMS emergency preparedness, 42 CFR 485.625 (20 rows)**

| Area | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| Program and (a) emergency plan (6 rows) | 1 | 4 | 1 | 0 |
| (b) policies and procedures (3 rows) | 1 | 2 | 0 | 0 |
| (c) communication plan (4 rows) | 1 | 3 | 0 | 0 |
| (d) training and testing (5 rows) | 2 | 3 | 0 | 0 |
| (e) power and (f) integrated systems (2 rows) | 1 | 0 | 0 | 1 |
| **Total (20)** | **6** | **12** | **1** | **1** |

By gap risk: 8 Moderate, 5 Low. The pattern is consistent: the emergency program is mature for hurricanes and mass casualties, and almost silent on cyberattacks. The CMS rule does not use the word "cyber," but its all-hazards risk assessment (485.625(a)(1)) and its medical documentation element ((b)(5)) are where a prolonged EHR outage belongs.

**Voluntary CPG self-benchmark (20 goals, `cpg-benchmark.csv`)**

| CPG tier | Met | Partially met | Not met |
|---|---|---|---|
| Essential (10) | 0 | 8 | 2 |
| Enhanced (10) | 0 | 6 | 4 |

The two Essential goals not met, **Revoke Credentials for Departing Workforce Members** and **Vendor/Supplier Cybersecurity Requirements**, are also HIPAA gaps, so fixing them serves both.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Vendor remote access without MFA or named accounts | 164.312(d) | High | Named vendor accounts through the identity provider with MFA | IT Manager | 2026-10-31 |
| Backups reachable from the directory; not immutable | 164.308(a)(7)(ii)(A) | High | Separate immutable backup account in a second region | IT Manager | 2026-11-30 |
| No IT contingency or disaster recovery plan; no testing | 164.308(a)(7), (7)(ii)(B), (7)(ii)(D) | High | IT contingency plan from the BIA as an annex to the emergency plan; quarterly restore tests | IT Manager | 2026-12-31 (tests from 2026-11) |
| Drug-library integrity not monitored | 164.312(c) | High | Change alerting and restricted access on the pump server | Facilities Manager | 2026-12-31 |
| Malware alerts unwatched nights and weekends | 164.308(a)(5)(ii)(B) | High | 24x7 managed detection and response | IT Manager | 2027-01-31 |
| No cyber hazard or IT outage strategy in the emergency plan | 485.625(a)(1)-(a)(2) | Moderate | Score cyber hazards from P01; IT outage annex with diversion criteria | Facilities Manager | 2026-12-31 |
| Medical documentation during downtime untested | 485.625(b)(5); 164.308(a)(7)(ii)(C) | Moderate | Monthly downtime PC tests; paper record custody and back-entry procedure | HIM Manager and Director of Nursing | 2026-12-31 |
| Stale contracted and agency accounts | 164.308(a)(3)(ii)(C) | Moderate | End dates on all contracted accounts; monthly agency reconciliation | HR Manager | 2026-10-31 |
| No log or access report review | 164.308(a)(1)(ii)(D) | Moderate | Monthly EHR access review; weekly sign-in review | Quality and Compliance Manager | 2026-10-31 |
| Missing BAAs (cloud fax, biomedical contractor) | 164.308(b)(1); 164.314(a) | Moderate | Execute BAAs or replace vendors | CFO | 2026-10-31 |
| Alternate communications depend on the network | 485.625(c)(3) | Moderate | Analog or cellular phones for laboratory and imaging; phones on their own segment | Facilities Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**One exercise, two rules.** The next "additional exercise" under 485.625(d)(2)(ii) should be the facilitated ransomware and EHR downtime tabletop that POL-03 and HIPAA 164.308(a)(7)(ii)(D) also call for. One well-run exercise can produce evidence for both, if the after-action report is filed in the emergency program binder (485.625(d)(2)(iii)).

## 5. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The Federal Register shows no final rule as of 2026-09-26, and the regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, these verified proposals would affect this hospital:
- The distinction between "required" and "addressable" would be removed, so the 17 addressable gaps above would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (desktops, workstations on wheels, and external email are gaps today).
- MFA would be required, with limited exceptions (vendor VPN and on-site EHR sign-in are gaps today).
- A written technology asset inventory and network map would be required (medical devices and OT are missing today).
- Penetration testing would be required at least every 12 months, along with vulnerability scanning.
- Certain systems and data would have to be restorable within 72 hours.
- A compliance audit would be required at least every 12 months.
- Business associates would have to give notice within 24 hours of activating their contingency plan.

The `pending_rule_change` column flags 34 HIPAA rows the proposal would affect. None of these is treated as a current obligation.

**CIRCIA** (proposed 6 CFR Part 226) would, if finalized as proposed, cover this hospital because the proposal names critical access hospitals regardless of size. It would add a 72-hour incident report and a 24-hour ransom payment report to CISA. It is not in effect and is tracked in the P08 matrix only.
