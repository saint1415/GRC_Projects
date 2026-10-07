# Regulatory Gap Analysis: Cris Santos Company | Emergency Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Regulations analyzed | HIPAA Security Rule (45 CFR Part 164, Subpart C; in force, last amended 2020-11-24) (C-EMERGENCY-R04); HIPAA Breach Notification Rule (45 CFR 164.400-164.414), including the company's duties as a business associate; Florida EMS records rules (Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.); Medicare ambulance documentation (42 CFR 410.40(e), 410.41(c), 424.516(f)) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Security Manager and the Compliance and Privacy Officer, with the vCISO; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-16 |

## 1. Applicability
**Primary business line:** ground ambulance service (911 response under county agreements and interfacility transport), billed to Medicare, Florida Medicaid, commercial plans, and facilities. The billing services line is a secondary business line, but it shares the same systems and the same HIPAA program, so its duties are analyzed here too.

Applicability was checked first for every requirement in the vertical registry, because the Emergency Services sector research was written mostly for public agencies and 911 centers. A private ambulance company is a different kind of entity.

| Registry ID or rule | Requirement | Applies? | Basis |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | **Yes** | The company is a health care provider that transmits health information electronically in standard transactions (claims through its clearinghouse), so it is a covered entity (45 CFR 160.103). Medicare pays an initial claim only if it is submitted electronically (42 CFR 424.32(d)(2)), and the small-supplier exception covers only suppliers with fewer than 10 full-time equivalent employees (424.32(d)(1)(viii)(B) and (d)(3)(ii)); the company has 600. The Security Rule also applies to the company as a **business associate** of its 4 billing services clients: the 160.103 definition of business associate includes a person that performs billing on behalf of a covered entity, and states that a covered entity may be a business associate of another covered entity. There is no size exemption. 45 CFR 164.306(b) lets the company weigh its size, complexity, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it |
| Related | HIPAA Breach Notification Rule | **Yes, in two roles** | As a covered entity: notices to individuals, HHS, and the media (164.404-164.408). As a business associate: notice to each client of a breach of that client's unsecured PHI (164.410) |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | **No (trigger tracked)** | The policy governs access to criminal justice information (CJI). The company has no access to state or national criminal justice databases or to law enforcement records systems, and both CAD-to-CAD feeds carry EMS incident data only (type, address, callback number, notes). Under 28 CFR 20.33(a)(7), a private contractor receives criminal history record information only under an agreement with a criminal justice agency, for the administration of criminal justice, with an approved security addendum; ambulance transport is not that. **Trigger:** County A's May 2026 proposal to share law enforcement premise hazard and officer-safety flags through CAD-to-CAD (P01 R-037, treated as Avoid) |
| C-EMERGENCY-R02, R03 | 28 CFR 20.21(f); 28 CFR Part 23 | **No** | These apply to state criminal history systems and to federally funded criminal intelligence systems. The company operates neither |
| C-EMERGENCY-R05 | CIRCIA | **Not yet (proposed only)** | No final rule was in the Federal Register as of 2026-09-25. The proposed rule would reach the company on two grounds: it is a critical infrastructure entity that exceeds the SBA size standard for its industry, and proposed 6 CFR 226.2(b)(5) separately covers entities that provide emergency medical services to a population of 50,000 or more. Tracked in P08, not treated as an obligation |
| C-EMERGENCY-R06 | FCC EAS cybersecurity rule (47 CFR Part 11) | **No** | The company is not an EAS participant and does not originate public alerts |
| State | Florida EMS records rules (Fla. Stat. 401.30; Rule 64J-1.014, F.A.C.) | **Yes** | The company is a licensee under Chapter 401. These rules govern the same CAD and ePCR records that the Security Rule protects |
| Federal | Medicare ambulance documentation (42 CFR 410.40(e), 410.41(c), 424.516(f)) | **Yes** | The company is a Medicare ambulance supplier. These rules govern the documentation that flows from the ePCR to billing |

**Excluded HIPAA Security Rule rows (7), with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a health care clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): this path applies when the covered entity and its business associate are both governmental entities. The municipal clients are governmental, but the company is not, so written BAAs are used.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans; 5 rows): **confirmed not applicable.** The employee health plan is fully insured. The company, as plan sponsor, receives only summary health information and enrollment and disenrollment information, which 164.314(b)(1) excludes (disclosures under 164.504(f)(1)(ii) or (iii)). Confirmed with the benefits broker and the plan documents on 2026-07-15.

**Other applicable rules and where they are handled:**
| Rule | Where covered |
|---|---|
| HIPAA Privacy Rule | Privacy program (outside this security analysis); BAAs appear here through 164.308(b) and 164.314(a) |
| Section 1557, 45 CFR 92.210 | P10 AI governance (AI-001 call triage) |
| Fla. Stat. 501.171 (breach notification; third-party agent duties) | P08 notification matrix |
| Fla. Stat. 934.03(2)(g) (call recording by a licensed ambulance service) | P10 (AI-001) |
| 42 CFR 401.305 (report and return Medicare overpayments) | P10 (AI-003 coding assistance) |
| County agreements and client BAAs (contracts) | P05 section 7; P08 notification matrix; P09 |
| HIPAA Security Rule NPRM | Proposed only; section 6 below |

## 2. Method
1. **Requirements.** HIPAA Security Rule requirements and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool), all 69 rows of the Health Care crosswalk. One citation was corrected against the current eCFR text: the business associate duty to report security incidents is at 164.314(a)(2)(i)(C), which the NIST dataset lists as 164.314(a)(3)(i) (row G-059). Breach Notification, Florida, and Medicare rows were decomposed from the regulation text.
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. The Security Rule rows use the Health Care crosswalk in `02_industry-rules/health-care/`, which is an **author mapping** (NIST has not published a HIPAA to CSF 2.0 mapping); NIST's official SP 800-53 mapping (OLIR) is shown next to it in the `nist_official_sp800_53r5_1_1` column. The other rows are this analysis's own author mapping.
3. **Evidence.** Interviews with the process owners, document review, configuration exports, and walkthroughs at 5 of 14 sites (headquarters with the primary communications center, Station 10 with the backup center, and Stations 3, 7, and 12), plus 2 ambulances.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, with sizes from the co-sourced internal audit firm's attribute sampling table:
   - departures: 25 of 128 (12 months to 2026-06-30);
   - transfers: 20 of 41;
   - new ePCR accounts: 25;
   - new hires: 25;
   - backup job days: 30 of 30 (July 2026);
   - BAAs: 15 of 52;
   - incidents: 10 of 29;
   - privacy incident files: 5 of 5;
   - media disposals: 10;
   - non-emergency claims for PCS: 25.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

**Addressable is not optional.** For each addressable specification, the company must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented. One equivalent alternative is documented: communications center consoles do not lock automatically (164.312(a)(2)(iii)), because telecommunicators must see live calls, so the badge-controlled center rooms serve as the equivalent measure.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 164.308 Administrative safeguards | 10 | 19 | 0 | 1 | 30 |
| 164.310 Physical safeguards | 6 | 6 | 0 | 0 | 12 |
| 164.312 Technical safeguards | 5 | 7 | 0 | 0 | 12 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 | 10 |
| 164.316 Policies, procedures, documentation | 1 | 4 | 0 | 0 | 5 |
| **HIPAA Security Rule subtotal** | **22** | **40** | **0** | **7** | **69** |
| HIPAA Breach Notification Rule (164.402-164.414) | 3 | 9 | 0 | 0 | 12 |
| Florida EMS records rules | 3 | 2 | 0 | 0 | 5 |
| Medicare ambulance documentation | 1 | 2 | 0 | 0 | 3 |
| **Total** | **29** | **53** | **0** | **7** | **89** |

**Security Rule detail.** Of the 40 partially met Security Rule rows, 16 are standards, 15 are **Required** implementation specifications, and 9 are **Addressable** specifications.

**Gap risk ratings (53 rows Partially met):** 12 High, 25 Moderate, 16 Low.

**Reading the results.** The company is partially compliant with good tooling. MFA, encryption, training, evaluation, sanctions, and media disposal are Met. No row is fully Not met. The gaps concentrate in four places:
- contingency planning and recovery testing for CAD (the 164.308(a)(7) standard and 4 of its 5 implementation specifications are rated High);
- business associate arrangements in both directions (164.308(b)(1), 164.314(a), 164.410);
- activity review and access reviews (164.308(a)(1)(ii)(D), 164.308(a)(4)(ii)(C));
- malware protection on the communications center consoles (164.308(a)(5)(ii)(B)).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Contingency plan does not cover loss of CAD at both centers or ransomware | 164.308(a)(7) | High | Update the plan from P05 and P08 | Director of IT (Security Officer) | 2026-12-15 |
| Integration engine and call recordings not in write-once backups | 164.308(a)(7)(ii)(A) | High | Copy to the backup account with write-once retention | Director of IT (Security Officer) | 2026-11-30 |
| CAD rebuild never tested; 1-hour RTO unproven | 164.308(a)(7)(ii)(B), (D) | High | Rebuild runbook and full rebuild test; quarterly restore tests | Director of IT (Security Officer) | 2026-12-31 (tests through 2027-03-31) |
| Manual mode not drilled for a multi-day outage at both centers | 164.308(a)(7)(ii)(C) | High | Ransomware manual dispatch drill at both centers | Director of Communications | 2026-11-30 |
| Consoles run EDR in detect-only mode and are patched quarterly | 164.308(a)(5)(ii)(B) | High | EDR block mode; monthly console patching | Security Manager | 2026-12-31 |
| No regular review of ePCR, CAD, or billing platform activity | 164.308(a)(1)(ii)(D) | High | Monthly ePCR access analytics; CAD and billing workspace reviews | Compliance and Privacy Officer | 2027-03-31 |
| Annual access reviews; transfers keep roles; excess CAD administrator rights | 164.308(a)(4)(ii)(C) | High | Quarterly reviews; transfer workflow; CAD configuration role | Director of IT (Security Officer) | 2027-03-31 |
| 6 vendors without BAAs; AI triage audio not covered | 164.308(b)(1); 164.314(a) | High | Execute BAAs and the AI amendment or stop PHI flows | Compliance and Privacy Officer | 2026-12-31 |
| Cannot split affected individuals by client for business associate notices | 164.410 | High | Client notice procedure and templates; client tagging in exports | Compliance and Privacy Officer | 2026-11-30 |
| Funded treatments not yet in place | 164.308(a)(1)(ii)(B) | High | Execute the roadmap below | Director of IT (Security Officer) | 2027-06-30 |
| Subcontractor BAAs (mail vendor, cloud fax) do not cover client PHI | 164.314(a)(2)(iii) | Moderate | Extend both BAAs | Compliance and Privacy Officer | 2026-12-31 |
| Pre-2025 PCS documents subject to 2-year deletion | 42 CFR 424.516(f) | Moderate | Suspend deletion; move to the billing platform | Director of Revenue Cycle | 2026-10-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Write-once backups for the integration engine and recordings; ransomware manual dispatch drill at both centers; BAAs for 6 vendors and the AI amendment; client notice procedure; decision log; PCS deletion suspended; break-glass for CAD and cloud; console EDR in block mode | 164.308(a)(7)(ii)(A), (C); 164.308(b)(1); 164.410; 164.402-164.414 items; 424.516(f) |
| **2. Build** | 2027 Q1 | CAD rebuild test; contingency plan approved and reviewed by the County A EMS office; quarterly access reviews; ePCR access analytics; SIEM onboarding of CAD, integration engine, and ePCR logs; named MDC sign-in; standards issued; joint tabletop with both counties | 164.308(a)(1)(ii)(D); (a)(4)(ii)(C); (a)(7)(ii)(B), (D); 164.312(a)(2)(i); 164.312(b); 164.316(a) |
| **3. Segment and prove** | 2027 Q2 | Station network segmentation at 9 stations; warm CAD standby in the backup region; BIA RTOs demonstrated; SOC 2 Type 2 observation period starts 2027-04-01 (P09) | 164.308(a)(7); 164.310(d); 164.312(a) |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk analysis (July 2027); tiered vendor reassessments; second annual evaluation; SOC 2 Type 2 report | 164.308(a)(1)(ii)(A); (a)(8); 164.314(a)(2)(i) |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met to Met.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of these items is treated as a current obligation. If finalized as proposed, these verified proposals would affect this company:
- The distinction between Required and Addressable would be removed. The 9 addressable gaps become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions. Today's encryption rows are Met.
- MFA would be required. The 92 per-vehicle MDC accounts would not meet it.
- A written technology asset inventory and network map would be required (vehicle and station devices are missing today).
- Penetration testing at least every 12 months, and vulnerability scanning, would be required.
- Certain systems and data would have to be restorable within 72 hours (CAD rebuild is untested).
- A compliance audit would be required at least every 12 months (the annual internal audit is a good base).
- Business associates would have to give notice within 24 hours of activating their contingency plan. That would bind the company's vendors and would also bind the company toward its 4 billing services clients.

**CIRCIA** (C-EMERGENCY-R05) is also still proposed. As drafted it would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. See section 1 for why the proposal would reach this company.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected Security Rule row. The roadmap already moves toward these proposals, so a final rule would change deadlines more than direction.
