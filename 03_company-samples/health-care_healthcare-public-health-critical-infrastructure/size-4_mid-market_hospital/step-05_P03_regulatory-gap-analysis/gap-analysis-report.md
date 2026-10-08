# Regulatory Gap Analysis: Cris Santos Company | Healthcare and Public Health | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital with an off-campus outpatient center) |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Regulations analyzed (113 rows) | HIPAA Security Rule (45 CFR Part 164, Subpart C; in force, last amended 2020-11-24; eCFR text checked as of 2026-09-23); HIPAA Breach Notification Rule (45 CFR 164.400-164.414); hospital emergency preparedness condition of participation, cyber-relevant parts (42 CFR 482.15); Section 1557 decision support duties (45 CFR 92.210); medical record services (42 CFR 482.24(b)); EMTALA diversion (42 CFR 489.24(b)); Promoting Interoperability security risk analysis measure (42 CFR 495.24); device user facility reporting (21 CFR 803.30) |
| Voluntary benchmark | HHS Healthcare and Public Health Cybersecurity Performance Goals (CPGs), 20 goals, in `cpg-benchmark.csv` |
| Assessment dates | 2026-06-22 to 2026-07-17; evidence refreshed with P07 results through 2026-08-14 and the P10 review through 2026-08-28 |
| Assessor | Information Security Manager and the Compliance and Privacy Officer, with the vCISO and the Director of Emergency Management; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here.

**Primary business line:** acute inpatient, emergency, surgical, obstetric, and diagnostic services billed to Medicare, Florida Medicaid, and commercial payers, plus EHR services to 18 affiliated practices.

At Mid-Market size the gap analysis covers every rule that binds the primary business line, not just the primary regulation. Each rule in the vertical registry (C-HPH-R01 to C-HPH-R11) and each other rule found in the screening was checked for applicability at this size first.

| Regulation | Applies? | Basis | Where analyzed |
|---|---|---|---|
| HIPAA Security Rule (C-HPH-R01) | **Yes** | The hospital is a health care provider that transmits health information electronically in standard transactions (claims and eligibility through its clearinghouse), so it is a covered entity (45 CFR 160.103). For the affiliated practice program it is also a business associate of 18 practices. No size exemption applies. 45 CFR 164.306(b) lets the hospital weigh its size, complexity, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it | 69 rows |
| HIPAA Breach Notification Rule (C-HPH-R02) | **Yes** | Same covered entity status; as a business associate, 164.410 also runs from the hospital to the practices | 12 rows; P08 matrix |
| 42 CFR 482.15 emergency preparedness (C-HPH-R07) | **Yes** | Medicare-participating hospital. No size threshold. Only the elements with a cyber or information dimension are decomposed: the program, (a) plan and risk assessment, (b) policies including patient tracking, medical documentation, and receiving arrangements, (c) communications, (d) training and testing, and (e) power at the standard level because the data center depends on it. Subsistence, evacuation, sheltering, volunteers, 1135 waivers, and transplant provisions stay with the Director of Emergency Management | 22 rows |
| Section 1557, 45 CFR 92.210 | **Yes** | Medicare and Medicaid are federal financial assistance. Applies to AI-001, AI-002, and AI-004 (P10) | 3 rows |
| 42 CFR 482.24(b) medical record services | **Yes** | Hospital condition of participation; its record security and confidentiality standards overlap the Security Rule | 3 rows |
| EMTALA, 42 CFR 489.24 | **Yes** | The hospital has a dedicated emergency department. Governs diversion during an IT outage | 1 row; P05, P08 |
| Promoting Interoperability, 42 CFR 495.24 | **Yes (payment program)** | For 2023 and later, an eligible hospital must meet the objectives and measures CMS selects for each EHR reporting period (495.24(f)(1)(i)(A)) and, from 2026, earn at least 80 points (495.24(f)(1)(i)(D)). The security risk analysis measure has been among them; confirm the current list in the latest IPPS final rule | 1 row |
| FDA medical device reporting, 21 CFR 803.30 | **Yes** | A hospital is a device user facility (21 CFR 803.3). Device-related deaths and serious injuries must be reported within 10 work days, including when a cyber event or software fault is the cause | 2 rows; P08 |
| Fla. Stat. 501.171 | **Yes** | Breach notice for Florida residents | P08 matrix |
| Fla. Stat. 934.03 | **Yes (AI scribe)** | All-party consent to record (AI-003) | P10 |
| Florida Digital Bill of Rights (controller definition, Fla. Stat. 501.702) | **No** | A "controller" under 501.702 must have global gross annual revenue above $1 billion and meet one of three further tests (50% or more of revenue from online advertising; a consumer smart speaker and voice command service; or an app store with at least 250,000 applications). The hospital's $100 million in revenue fails the first test | Not analyzed |
| HHS HPH CPGs (C-HPH-R08) and 405(d) HICP (C-HPH-R09) | **Voluntary** | HHS describes the CPGs as voluntary. HICP (2023 edition) treats a hospital of 51-299 beds as a medium-sized organization, so the medium-sized sub-practices in Technical Volume 2 apply | `cpg-benchmark.csv` |
| HITECH recognized security practices (C-HPH-R10), 42 U.S.C. 17941 | **Applies as a mitigating factor** | OCR must consider recognized security practices in place for the previous 12 months. Operating the CPGs and HICP practices now builds that record | Roadmap |
| FDA sec. 524B (C-HPH-R04) | **Not directly** | Duties fall on device manufacturers. The hospital uses it in purchasing (SBOM, vulnerability plan, update support) | P06 STD-04 |
| FTC Health Breach Notification Rule (C-HPH-R05) | **No** | 16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such | Not analyzed |
| 42 CFR Part 2 (C-HPH-R06) | **No** | The hospital is not a Part 2 program (obligations register C-HPH-R06; EV-047, EV-056) | Not analyzed |
| HIPAA Security Rule NPRM (C-HPH-R03) | **Proposed only** | Not a current obligation | Section 6 |
| CIRCIA (C-HPH-R11) | **Not in effect** | Proposed 6 CFR 226.2(b)(11) would cover hospitals with 100 or more beds; this hospital has 112. No final rule as of 2026-10-06 | Section 6; P08 |

**Excluded HIPAA Security Rule rows (7), with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the hospital is not a health care clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no governmental entity business associates. State and county health departments receive public health reports as permitted disclosures, not as business associates.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans; 5 rows): **confirmed not applicable.** The employee health plan is fully insured, and the hospital as plan sponsor receives only summary health information and enrollment and disenrollment information, which 164.314(b)(1) excludes (disclosures under 164.504(f)(1)(ii) or (iii)). Confirmed with the benefits broker on 2026-07-08 (EV-069, EV-048).

**One 482.15 row is excluded:** 482.15(f) (unified program for a multi-facility health system), because the hospital is independent.

## 2. Method
1. **Requirements.** HIPAA Security Rule requirements and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool), all 69 rows of the Health Care crosswalk. NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis uses the current rule's 164.308(b)(3). The Breach Notification, 482.15, 482.24, 489.24, 495.24, 92.210, and 803.30 rows were decomposed from the eCFR text (2026-09-23 version); summaries are paraphrased.
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. The HIPAA rows use the Health Care crosswalk in `02_industry-rules/health-care/`, an **author mapping**; NIST's official OLIR mapping (SP 800-53 Rev. 5.1.1) is shown beside it in `nist_official_sp800_53r5_1_1`. No official NIST mapping exists for the other rules, so those rows are this analysis's own author mapping.
3. **Evidence.** Current state was established from the intake evidence (exports and documents collected 2026-06-01 to 2026-06-19: EV-001 to EV-056 and EV-071 to EV-073), gap analysis interviews with the process owners (EV-059), walkthroughs of the ED, ICU, 3 nursing units, pharmacy, laboratory, the data center, and the outpatient center (2026-07-07 to 2026-07-09, EV-063), the configuration and access reviews and the TLS scan (EV-064 to EV-066), the samples below (EV-061, EV-062, EV-067, EV-068), and the benefits broker confirmation (EV-069). Where a row was refreshed with P07 results through 2026-08-14, the `evidence` column cites the P07 ID (for example EV-CP-9). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested, chosen at random from the system-generated populations collected at intake or refreshed to 2026-06-30 (EV-036, EV-037, EV-041, EV-051 and EV-060), using the co-sourced internal audit firm's attribute sampling table:
   - employee terminations: 25 of 142;
   - non-employee departures (contracted, agency, practice users): 25 of about 210;
   - transfers: 25 of 88;
   - new EHR accounts: 25;
   - new hires: 25;
   - backup job days: 31 of 31 (July 2026, from P07, EV-CP-9);
   - BAAs: 20 of 168;
   - vendors from accounts payable: 20;
   - incidents: 10 of 41;
   - privacy incident files: 9 of 9 (2025-2026);
   - device returns to vendors: 6 of 6 (2026).
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

**Addressable is not optional.** For each addressable specification, the hospital must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented; none is being documented as unreasonable.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 164.308 Administrative safeguards | 6 | 21 | 2 | 1 | 30 |
| 164.310 Physical safeguards | 4 | 8 | 0 | 0 | 12 |
| 164.312 Technical safeguards | 2 | 10 | 0 | 0 | 12 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 | 10 |
| 164.316 Policies, procedures, documentation | 3 | 2 | 0 | 0 | 5 |
| **HIPAA Security Rule subtotal** | **15** | **45** | **2** | **7** | **69** |
| HIPAA Breach Notification Rule (164.402-164.414) | 3 | 9 | 0 | 0 | 12 |
| 42 CFR 482.15 (cyber-relevant) | 6 | 14 | 1 | 1 | 22 |
| 45 CFR 92.210 (Section 1557) | 0 | 3 | 0 | 0 | 3 |
| 42 CFR 482.24(b) | 1 | 2 | 0 | 0 | 3 |
| 42 CFR 489.24(b) (EMTALA) | 0 | 1 | 0 | 0 | 1 |
| 42 CFR 495.24 (security risk analysis measure) | 0 | 1 | 0 | 0 | 1 |
| 21 CFR 803.30 | 0 | 2 | 0 | 0 | 2 |
| **Total** | **25** | **77** | **3** | **8** | **113** |

**Security Rule detail.** Of the 47 Security Rule rows that are Partially met or Not met, 17 are standards, 16 are **Required** implementation specifications, and 14 are **Addressable** specifications. By gap risk: 11 High, 26 Moderate, 10 Low.

**Gap risk ratings (all 80 rows Partially met or Not met):** 13 High, 48 Moderate, 19 Low.

**Voluntary CPG self-benchmark (20 goals):**
| CPG tier | Met | Partially met | Not met |
|---|---|---|---|
| Essential (10) | 0 | 10 | 0 |
| Enhanced (10) | 0 | 9 | 1 |

Every Essential goal is started and none is complete, which is typical of a mid-market hospital with good tools that do not yet reach devices, vendors, and non-employees. The one Enhanced goal not met is Third Party Vulnerability Disclosure.

**Reading the results.** The hospital is partially compliant with a defined program: sanctions, security responsibility, training reminders, log-in monitoring, evaluation, and the criticality analysis are Met. The gaps concentrate in six places:
- recovery and emergency mode operation (164.308(a)(7)) and its CMS counterpart (482.15(a)(2), (b)(5)), where all 3 Not met rows sit;
- activity review and audit controls (164.308(a)(1)(ii)(D), 164.312(b)), because the systems that matter most for patient safety send no logs;
- access lifecycle for non-employees and privileged users (164.308(a)(3)(ii)(C), (a)(4)(ii)(C));
- vendor access and business associate contracts (164.308(b)(1), 164.312(d));
- medical devices across inventory, passwords, encryption, and disposal (164.310(d), 164.308(a)(5)(ii)(D));
- governance of AI decision support (92.210).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| No IT outage strategy or diversion criteria in the emergency plan | 42 CFR 482.15(a)(2) | High | IT outage annex: diversion criteria, 72-hour downtime, recovery order from P05; tabletop 2026-11-10 | Director of Emergency Management | 2026-12-15 |
| No disaster recovery plan or restore testing for on-premises clinical servers | 164.308(a)(7), (7)(ii)(B), (7)(ii)(D) | High | IT DR plan; quarterly restore tests from 2026-10-20 | IT Director (Security Officer) | 2027-03-31 |
| Medical documentation availability (vendor RTO 12 h; paper never tested past 4 h) | 42 CFR 482.15(b)(5); 164.308(a)(7)(ii)(C) | High | Recovery terms at renewal; 72-hour paper procedures | IT Director (Security Officer); Director of Emergency Management | 2027-03-31 |
| Vendor VPN accounts and on-campus admin sign-in without MFA | 164.312(d) | High | Vendor access platform with MFA for all 46 vendors; MFA for all admin sign-in | Information Security Manager | 2026-12-31 |
| Shared vendor passwords and default device credentials | 164.308(a)(5)(ii)(D) | High | Change and vault; onboarding check | Director of Biomedical Engineering | 2026-10-31 |
| 42 PHI vendors without BAAs | 164.308(b)(1); 164.314(a) | High | Execute BAAs or stop PHI flows; purchasing gate | Compliance and Privacy Officer | 2026-12-31 |
| Annual access reviews; standing privileged access | 164.308(a)(4)(ii)(C) | High | Quarterly reviews; privileged access management for all admin planes | IT Director (Security Officer) | 2027-03-31 |
| EHR access review limited to VIP records; clinical servers, devices, and OT not logged | 164.308(a)(1)(ii)(D); 164.312(b) | High | EHR access analytics; SIEM onboarding | Compliance and Privacy Officer; Information Security Manager | 2027-03-31 |
| Risk treatment backlog | 164.308(a)(1)(ii)(B) | High | Execute the roadmap below; first penetration test | IT Director (Security Officer) | 2027-06-30 |
| Non-employee accounts not removed on time | 164.308(a)(3)(ii)(C); 482.24(b)(3) | Moderate | End dates and monthly reconciliation | HR Director | 2026-12-31 |
| Decision support tools adopted without 92.210 review | 45 CFR 92.210(a)-(c) | Moderate | AI intake gate; P10 conditions | Compliance and Privacy Officer; Chief Medical Officer | 2026-12-31 |
| Discovery time and four-factor analysis not documented | 164.402; 164.404(a); 164.414(b) | Moderate | Decision log in P08 | Compliance and Privacy Officer | 2026-11-30 |
| Device security inventory at 70% | 164.310(d); 164.308(a)(1)(ii)(A) | Moderate | Passive discovery; reconcile inventories | Director of Biomedical Engineering | 2027-03-31 |
| Missing standards | 164.316(a) | Moderate | Issue the P06 standards | Information Security Manager | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

**One exercise, several rules.** The 2026-11-10 ransomware and 72-hour EHR downtime tabletop counts as the 482.15(d)(2)(ii) additional exercise, tests 164.308(a)(7)(ii)(D) and POL-03, and exercises the EMTALA diversion decision. Filing one after-action report in the emergency program binder (482.15(d)(2)(iii)) produces evidence for all of them.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Vendor passwords changed and vaulted; all vendors on the access platform with MFA; BAAs for the 42 vendors; decision log; IT outage annex and diversion criteria; tabletop; first interface engine restore test; DMARC enforcement; AI intake gate and 92.210 records | 164.308(a)(5)(ii)(D); 164.312(d); 164.308(b)(1); 164.402-164.414 items; 482.15(a)(1)-(3), (b)(2), (c)(4); 489.24(b); 92.210 |
| **2. Build** | 2027 Q1 | Quarterly access reviews; privileged access management for all admin planes; EHR access analytics; IT DR plan approved; restore tests of the LIS and cabinet server; SIEM onboarding of clinical servers and the interface engine; standards issued; non-employee lifecycle | 164.308(a)(1)(ii)(D); (a)(3)(ii)(C); (a)(4)(ii)(C); (a)(7)(ii)(B); 164.312(b); 164.316(a); 482.24(b)(3) |
| **3. Segment and prove** | 2027 Q2 | Device VLANs for monitors, analyzers, cabinets, fetal monitoring, and the cath lab; OT segment; 72-hour functional downtime exercise; analog or cellular lines on every unit; first penetration test; SOC 2 observation period starts 2027-04-01 (P09) | 164.308(a)(7)(ii)(C)-(D); 164.310(d); 482.15(b)(5), (c)(3); CPG Enhanced Network Segmentation |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk analysis (June 2027) and Promoting Interoperability attestation; Tier 1 vendor reassessments; unsupported device replacement (capital plan); second annual evaluation | 164.308(a)(1)(ii)(A); (a)(8); 164.314(a)(2)(i); 495.24 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met, and the count of CPG goals Met.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The Federal Register shows no final rule as of 2026-10-06, and the regulatory agenda projects a final rule in July 2027. None of these items is treated as a current obligation. If finalized as proposed, these verified proposals would affect this hospital:
- The distinction between Required and Addressable would be removed, so the 14 addressable gaps above would become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (device storage and internal analyzer feeds are gaps today).
- MFA would be required (vendor VPN accounts and on-campus administrator sign-in are gaps today).
- A written technology asset inventory and network map would be required (the device inventory is 70% complete and OT is not inventoried).
- Penetration testing would be required at least every 12 months, along with vulnerability scanning (no penetration test to date).
- Certain systems and data would have to be restorable within 72 hours (recovery testing gap).
- A compliance audit would be required at least every 12 months (the annual internal audit is a good base).
- Business associates would have to give notice within 24 hours of activating their contingency plan (BAA amendments; this would also bind the hospital toward its 18 practices).

The `pending_rule_change` column flags 34 Security Rule rows the proposal would affect.

**CIRCIA** (proposed 6 CFR Part 226) would, if finalized as proposed, cover this hospital because the proposal names hospitals with 100 or more beds. It would add a 72-hour covered incident report and a 24-hour ransom payment report to CISA. No final rule has been published (the latest Federal Register item is the May 2026 town hall notice), so it is tracked in the P08 matrix only.

**ONC HTI-5 proposed rule** (FR Doc 2025-23896, 2025-12-29; RIN 0955-AA09) is still proposed. It would remove the source attribute and intervention risk management requirements for predictive decision support in 45 CFR 170.315(b)(11). Those duties fall on the EHR developer, but they are the hospital's main source of documentation for the sepsis model, so P10 writes the documentation duties into the EHR contract.
