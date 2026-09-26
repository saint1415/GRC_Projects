# Regulatory Gap Analysis: Cris Santos Company | Health Care and Social Assistance | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Regulations analyzed | HIPAA Security Rule (45 CFR Part 164, Subpart C; in force, last amended 2020-11-24); HIPAA Breach Notification Rule (45 CFR 164.400-164.414); CMS ASC emergency preparedness condition for coverage, cyber-relevant parts (42 CFR 416.54) |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Security Manager and the Compliance and Privacy Officer, with the vCISO; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
**Primary business line:** physician services, ambulatory surgery, and diagnostic imaging, all billed to Medicare, Florida Medicaid, and commercial payers.

| Regulation | Applies? | Basis |
|---|---|---|
| HIPAA Security Rule | **Yes** | The company is a health care provider that transmits health information electronically in standard transactions (claims and eligibility through its clearinghouse), so it is a covered entity (45 CFR 160.103). No size exemption applies. 45 CFR 164.306(b) lets the company weigh its size, complexity, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it |
| HIPAA Breach Notification Rule | **Yes** | Same covered entity status. Duties run to individuals, HHS, and the media (164.404-164.408), with law enforcement delay and burden-of-proof rules (164.412, 164.414) |
| 42 CFR 416.54 (ASC emergency preparedness) | **Yes, for the ASC only** | The ASC is Medicare-certified, and 416.54 is an ASC condition for coverage. Only the cyber-relevant paragraphs are analyzed here: risk assessment, strategies, continuity, medical documentation, communication, training, and testing. The clinics and imaging center are not provider types covered by the CMS emergency preparedness rule |

**Excluded HIPAA Security Rule rows (7), with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a health care clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no governmental entity business associates.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans; 5 rows): **confirmed not applicable.** The employee health plan is fully insured. The company, as plan sponsor, receives only summary health information and enrollment and disenrollment information. 164.314(b)(1) excludes that case (disclosures under 164.504(f)(1)(ii) or (iii)). A fully insured plan that receives only that information is also relieved of most Privacy Rule administrative requirements (164.530(k)). The health insurance issuer holds the plan's PHI as its own covered entity. Confirmed with the benefits broker and the plan documents on 2026-07-22.

**Other applicable regulations and where they are handled:**
| Regulation | Where covered |
|---|---|
| HIPAA Privacy Rule (N62-R02) | Privacy program (outside this security analysis); BAAs appear here through 164.308(b) and 164.314(a) |
| Section 1557, 45 CFR 92.210 (N62-R07) | P10 AI governance (AI-002 and AI-003) |
| Fla. Stat. 501.171 (breach notification) | P08 notification matrix |
| Fla. Stat. 934.03 (recording consent) | P10 (AI-001 scribe) |
| 42 CFR Part 2 (N62-R05) | Not applicable: no federally assisted SUD program |
| HIPAA Security Rule NPRM (N62-R04) | Proposed only; section 6 below |

## 2. Method
1. **Requirements.** HIPAA Security Rule requirements and their Required or Addressable designations come from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool), all 69 rows of the Health Care crosswalk. Breach Notification Rule and 42 CFR 416.54 requirements were decomposed from the eCFR text (2026-09-23 version, verified through the eCFR API).
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. The HIPAA Security Rule rows use the Health Care crosswalk in `02_verticals/n62_health-care/`, which is an **author mapping** (NIST's official CSF 2.0 mapping is not yet published). The Breach Notification and 416.54 rows are this analysis's own author mapping.
3. **Evidence.** Interviews with the process owners, document review, configuration exports, and walkthroughs at 4 of 10 sites (Clinic 1 with the CBO, Clinic 5, the ASC, and the imaging center).
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were chosen at random from system-generated populations, with sizes based on the co-sourced internal audit firm's attribute sampling table for a moderate-risk control operating many times a year:
   - terminations: 25 of 118;
   - transfers: 25 of 64;
   - new EHR accounts: 25;
   - new hires: 25;
   - backup job days: 30 of 30 (July 2026);
   - BAAs: 20 of 110;
   - vendors from accounts payable: 20;
   - incidents: 10 of 37;
   - privacy incident files: 6 of 6;
   - media disposals: 10.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

**Addressable is not optional.** For each addressable specification, the company must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). Every addressable gap below is being implemented; none is being documented as unreasonable.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 164.308 Administrative safeguards | 10 | 19 | 0 | 1 | 30 |
| 164.310 Physical safeguards | 3 | 9 | 0 | 0 | 12 |
| 164.312 Technical safeguards | 6 | 6 | 0 | 0 | 12 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 | 10 |
| 164.316 Policies, procedures, documentation | 1 | 4 | 0 | 0 | 5 |
| **HIPAA Security Rule subtotal** | **20** | **42** | **0** | **7** | **69** |
| HIPAA Breach Notification Rule (164.402-164.414) | 3 | 9 | 0 | 0 | 12 |
| 42 CFR 416.54 (ASC, cyber-relevant) | 1 | 6 | 2 | 0 | 9 |
| **Total** | **24** | **57** | **2** | **7** | **90** |

**Security Rule detail.** Of the 42 partially met Security Rule rows, 15 are standards, 15 are **Required** implementation specifications, and 12 are **Addressable** specifications.

**Gap risk ratings (59 rows Partially met or Not met):** 13 High, 26 Moderate, 20 Low.

**Reading the results.** The company is partially compliant with good tooling: MFA, EDR, encryption, isolated backups, training, and evaluation are Met. The gaps concentrate in five places:
- contingency planning and recovery testing (164.308(a)(7));
- business associate contracts (164.308(b), 164.314(a));
- access reviews and privileged access (164.308(a)(4)(ii)(C));
- EHR activity review (164.308(a)(1)(ii)(D));
- the ASC emergency plan's silence on cyber events (416.54).

The only two Not met rows are in 416.54.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| ASC plan has no cyber hazards or strategies | 42 CFR 416.54(a)(1)-(2) | High | Add cyber hazards and downtime strategies from P01 and P05; ASC tabletop 2026-11-18 | ASC Administrator | 2026-12-15 |
| No company DR plan or recovery testing for interface engine, PACS, data warehouse | 164.308(a)(7), (7)(ii)(B)-(D) | High | Contingency plan; quarterly restore tests from 2026-10-20 | IT Director | 2027-03-31 |
| ASC medical documentation availability (vendor RPO 1 h, RTO 12 h) | 42 CFR 416.54(b)(4); 164.308(a)(7)(ii)(C) | High | 15-minute ASC extract; vendor recovery terms | ASC Administrator | 2027-03-31 |
| 30 PHI vendors without BAAs | 164.308(b)(1), (b)(4); 164.314(a) | High | Execute BAAs or stop PHI flows; purchasing gate | Compliance and Privacy Officer | 2026-12-31 |
| Annual access reviews; privileged access management only in the cloud | 164.308(a)(4)(ii)(C) | High | Quarterly reviews; privileged access management for directory, IdP, EHR, PACS | Security Manager | 2027-03-31 |
| EHR access review limited to VIP patients | 164.308(a)(1)(ii)(D) | High | EHR access analytics; monthly review | Compliance and Privacy Officer | 2027-03-31 |
| Risk treatment backlog | 164.308(a)(1)(ii)(B) | High | Execute the roadmap below | IT Director | 2027-06-30 |
| Discovery time and four-factor analysis not documented | 164.402; 164.404(a); 164.414(b) | Moderate | Decision log in P08 | Compliance and Privacy Officer | 2026-11-30 |
| Device inventory about 60% | 164.310(d), (d)(2)(iii); 164.308(a)(1)(ii)(A) | Moderate | Passive discovery at 10 sites | IT Director | 2026-12-31 |
| Missing standards (configuration, logging, vendor, device, AI) | 164.316(a) | Moderate | Issue the P06 standards | Security Manager | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Remove PACS vendor domain administrator accounts; BAAs for the 30 vendors; decision log and discovery-time capture; ASC cyber tabletop and plan update; first interface engine restore test; transfer workflow fix | 164.308(b)(1); 164.402-164.414 items; 416.54(a)(1)-(3), (c)(3), (d)(2) |
| **2. Build** | 2027 Q1 | Quarterly access reviews; privileged access management for all admin planes; EHR access analytics; contingency plan approved; standards issued; SIEM onboarding of PACS and interface engine | 164.308(a)(1)(ii)(D); (a)(4)(ii)(C); (a)(7); 164.312(b); 164.316(a) |
| **3. Segment and prove** | 2027 Q2 | Segmentation at Clinics 4-8; PACS and data warehouse restore tests; BIA RTOs demonstrated; SOC 2 Type 2 observation period starts 2027-04-01 (P09) | 164.308(a)(7)(ii)(D); 164.310(d); 416.54(b)(4) |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk analysis (July 2027); legacy modality console replacement; tiered vendor reassessments; second annual evaluation | 164.308(a)(1)(ii)(A); (a)(8); 164.314(a)(2)(i) |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of these items is treated as a current obligation. If finalized as proposed, these verified proposals would affect this company:
- The distinction between Required and Addressable would be removed. The 12 addressable gaps become mandatory.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions. Today's rows are Met, but the legacy consoles and devices need review.
- MFA would be required. Met today for workforce; modality consoles and vendor service accounts need review.
- A written technology asset inventory and network map would be required (device inventory gap).
- Penetration testing at least every 12 months, and vulnerability scanning, would be required.
- Certain systems and data would have to be restorable within 72 hours (recovery testing gap).
- A compliance audit would be required at least every 12 months (the annual internal audit is a good base).
- Business associates would have to give notice within 24 hours of activating their contingency plan (BAA amendments).

The `pending_rule_change` column in `gap-analysis.csv` flags each affected Security Rule row. The roadmap already moves toward these proposals, so a final rule would change deadlines more than direction.
