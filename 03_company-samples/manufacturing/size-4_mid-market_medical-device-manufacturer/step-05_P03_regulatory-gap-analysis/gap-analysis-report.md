# Regulatory Gap Analysis: Cris Santos Company | Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed connected medical device manufacturer) |
| Tier / Vertical | Mid-Market / Manufacturing (NAICS 334510) |
| Primary regulation | FD&C Act section 524B, ensuring cybersecurity of devices (21 U.S.C. 360n-2), with the FDA regulations that carry it into daily operations (21 CFR 803, 806, 820) and FDA's premarket (2026-02-03) and postmarket (December 2016) cybersecurity guidance |
| Secondary regulation | HIPAA Security Rule (45 CFR Part 164, Subpart C) and business associate breach notice (45 CFR 164.402-164.414), for the Connected Care Cloud |
| Benchmark (nonbinding) | NIST SP 800-82 Rev. 3 for plant OT |
| Assessment dates | 2026-07-06 to 2026-07-31; evidence refreshed with P07 results through 2026-08-28 |
| Assessors | VP QA/RA and Product Security Manager (FDA rows); Security Manager and Compliance and Privacy Officer (HIPAA rows); OT Engineering Manager with the vCISO (OT benchmark); reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-17 |

## 1. Applicability
**Primary business line:** design, manufacture, and service of connected patient-care devices, and the Connected Care Cloud (CCC) that supports them.

| Regulation | Applies? | Basis |
|---|---|---|
| FD&C Act section 524B | **Yes** | 524B(a) covers any person who submits a 510(k), PMA, PDP, De Novo, or HDE for a "cyber device" (524B(c)): a device that includes software, can connect to the internet, and has characteristics that could be vulnerable to cybersecurity threats. VM-7 (510(k), 2024), IP-4 (510(k), 2025), and AI-001 (De Novo, 2025) were all submitted after the effective date (90 days after enactment on 2022-12-29, per Pub. L. 117-328 section 3305(d)), so 524B applied to each. The planned AI-002 510(k) will also be subject to it. There is **no size exemption**; the only route is an FDA exemption list under 524B(d), and none applies. Failure to comply with 524B(b)(2) is a prohibited act (21 U.S.C. 331(q)(3)) |
| VM-5 (cleared 2018) | **Not reached by 524B** | Pub. L. 117-328 section 3305(d) says submissions made before the effective date are not subject to 524B(a) or (b). VM-5 remains subject to the QMSR, MDR, and correction and removal rules, and to FDA's postmarket cybersecurity expectations. Any future VM-5 submission would bring 524B in |
| The CCC | **Yes, as a related system** | 524B(b)(2) covers "the device and related systems." FDA considers related systems to include manufacturer-controlled update servers and connections to health care facility networks (premarket guidance section VII.C.2). The CCC update service and hospital interfaces fit that description |
| QMSR (21 CFR Part 820), 803, 806 | **Yes** | The company is a registered manufacturer of class II devices. The QMSR took effect 2026-02-02 and incorporates ISO 13485 by reference. 820.10(b)(3) and (b)(4) tie complaints to part 803 and advisory notices to part 806 |
| FDA guidance (premarket 2026-02-03; postmarket December 2016) | **Nonbinding, but used** | FDA uses these documents to judge whether a submission shows a reasonable assurance of cybersecurity. The postmarket guidance also states when FDA does not intend to enforce 806 reporting for uncontrolled cybersecurity risks. They are recommendations, not requirements |
| HIPAA Security Rule and breach notice | **Yes, for the CCC** | The company is a business associate of about 290 hospitals (45 CFR 160.103). The Security Rule applies to business associates (164.302) and 164.410 governs breach notice to the hospitals. No size exemption; 164.306(b) lets the company weigh size, complexity, and cost in choosing how to meet each standard |
| NIST SP 800-82 Rev. 3 | **Benchmark only** | No federal rule binds the plant's OT security. The overlay's research note recommends SP 800-82 Rev. 3 for manufacturers with no binding rule. Rev. 4 was released as an initial public draft on 2026-09-21 (comments due 2026-11-30) and is not used as the benchmark |

**Excluded HIPAA Security Rule rows (7), with reasons:**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a health care clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no governmental entity arrangements.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans; 5 rows): the employee health plan is fully insured and the company, as plan sponsor, receives only summary health and enrollment information, which 164.314(b)(1) excludes (disclosures under 164.504(f)(1)(ii) or (iii)). Confirmed with the benefits broker on 2026-07-20.

**Not analyzed (with reasons):** DFARS 252.204-7012, CMMC, and ITAR (N31-33-R01 to R03): no defense contracts or defense articles. EAR (N31-33-R04): U.S. sales only. SEC disclosure rules: privately held. The HIPAA Privacy Rule: privacy duties flow through the BAAs and are handled by the Compliance and Privacy Officer. CIRCIA: proposed only; the proposed criteria would reach manufacturers of class II and III devices (proposed 6 CFR 226.2(b)(11)(iii)), so recheck when final. State breach laws: handled in the P08 notification matrix.

## 2. Method
1. **Requirements.** The 524B rows follow the statute's own structure: (a), (b)(1) through (b)(4), (c), and (d). FDA regulation rows cite the CFR section (eCFR, 2026-09-23 version, verified through the eCFR API); QMSR rows name the ISO 13485 clause by number only, because the standard is copyrighted. Guidance rows cite the section of the guidance. HIPAA Security Rule rows come from NIST SP 800-66 Rev. 2 through the Health Care crosswalk (all 69 rows). Breach notification rows were decomposed from 164.402-164.414. OT rows cite SP 800-82 Rev. 3 sections.
2. **Crosswalk.** NIST has published no mapping for section 524B or FDA regulations, so those rows carry an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. HIPAA rows use the Health Care crosswalk (`02_industry-rules/health-care/`), also an author mapping, with NIST's official SP 800-53 references shown alongside in `nist_official_sp800_53r5_1_1`.
3. **Evidence.** Interviews with the VP QA/RA, VP Engineering, Product Security Manager, Director of Cloud Operations, IT Director, Plant Manager, OT Engineering Manager, and Compliance and Privacy Officer; review of the three submissions' cybersecurity sections, SBOMs, threat models, QMS procedures, and BAAs; a plant walkthrough on 2026-08-18.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population, using the co-sourced internal audit firm's attribute sampling table (25 items for a moderate-risk control operating many times a year):
   - matched component vulnerabilities in the SBOM queue: 25;
   - terminations: 25 of 96; transfers: 25 of 58; production access requests: 25;
   - hospital BAAs: 20 of 290; subcontractor BAAs: 16 of 16; PHI subcontractors: 18 of 18;
   - security incidents: 8 of 29; external vulnerability reports: 14 of 14;
   - product change records: 20; test station change records: 20;
   - IP-4 releases: 4; cybersecurity releases for 806.20 records: 6;
   - MDR decisions: 10; supplemental MDRs: 5;
   - service records: 20; depot wipe records: 20;
   - backup job days: 30 of 30 (July 2026).
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FD&C Act section 524B (statute) | 11 | 3 | 6 | 0 | 2 |
| QMSR (21 CFR Part 820) | 8 | 2 | 5 | 1 | 0 |
| 21 CFR Part 803 (medical device reporting) | 3 | 1 | 2 | 0 | 0 |
| 21 CFR Part 806 (corrections and removals) | 2 | 0 | 2 | 0 | 0 |
| FDA premarket cybersecurity guidance (2026-02-03) | 21 | 5 | 16 | 0 | 0 |
| FDA postmarket cybersecurity guidance (December 2016) | 5 | 1 | 4 | 0 | 0 |
| HIPAA Security Rule (business associate scope) | 69 | 35 | 27 | 0 | 7 |
| HIPAA Breach Notification Rule (business associate) | 7 | 3 | 4 | 0 | 0 |
| NIST SP 800-82 Rev. 3 (plant OT benchmark) | 6 | 0 | 4 | 2 | 0 |
| **Total** | **132** | **50** | **70** | **3** | **9** |

**Security Rule detail.** By section: 164.308 has 13 Met, 16 Partially met, 1 N/A (30 rows); 164.310 has 10 Met, 2 Partially met (12); 164.312 has 9 Met, 3 Partially met (12); 164.314 has 4 Partially met, 6 N/A (10); 164.316 has 3 Met, 2 Partially met (5). Of the 27 Partially met Security Rule rows, 11 are standards, 12 are **Required** implementation specifications, and 4 are **Addressable** specifications.

**Gap risk ratings (73 rows Partially met or Not met):** 15 High, 44 Moderate, 14 Low.

**The three Not met rows** are G-014 (AI-005 used in complaint handling without QMS software validation), G-129 (unmanaged vendor remote access into plant OT), and G-130 (no OT monitoring).

**Reading the results.** The company is a defined program with gaps in scale. It met section 524B at submission for all three current products and runs the required machinery: SBOMs in every build, a published CVD policy, ISAO membership, HSM-backed signing. The HIPAA Security Rule basics for the CCC are Met. The gaps concentrate in four places:
- **postmarket throughput:** vulnerability triage backlog, a slow IP-4 patch cycle, and slow field adoption (524B(b)(1), (b)(2)(A));
- **the factory as a related system:** test station software and the provisioning key sit outside the SPDF and the threat models (524B(b)(2); ISO 13485 clause 7.5.6), which is how R-049 happened;
- **third parties and contracts:** 2 PHI subcontractors without BAAs, and BAA notice terms not tracked (164.308(b), 164.314(a), 164.410(b));
- **plant OT:** flat segments, unmanaged vendor access, no monitoring (SP 800-82 benchmark).

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared factory credential reachable on 1,140 shipped IP-4 pumps (G-035) | Premarket guidance App. 1; 524B(b)(2)(B) | High | Out-of-cycle firmware; advisory sent 2026-09-11 (P08) | VP Engineering | 2026-10-16 |
| Production software changes bypass revalidation (G-013) | 21 CFR 820.10(a); ISO 13485 clause 7.5.6 | High | Station software under change control with revalidation; CAPA | VP QA/RA | 2026-12-31 |
| SPDF and threat models stop at the factory door (G-005, G-006) | 524B(b)(2) | High | Extend the SPDF; provisioning key into the HSM | VP Engineering; Product Security Manager | 2026-12-31 |
| Triage backlog of 41 vulnerabilities; manual KEV matching (G-003, G-031) | 524B(b)(1); guidance V.A.4(b) | High | Daily automated KEV matching; service levels; one more engineer | Product Security Manager | 2026-12-31 |
| IP-4 patch cycle not justified; slow adoption (G-007) | 524B(b)(2)(A) | High | Quarterly releases with justification; adoption reports | VP Engineering | 2027-03-31 |
| 2 PHI subcontractors without BAAs (G-079, G-080, G-105, G-108) | 164.308(b)(1), (b)(4); 164.314(a) | High | Execute BAAs or stop PHI flows; purchasing gate | Compliance and Privacy Officer | 2026-10-31 |
| No privileged activity review in the CCC (G-055) | 164.308(a)(1)(ii)(D) | High | Weekly review; export alerts | Security Manager | 2026-12-31 |
| Plant OT flat segment and vendor VPN (G-128, G-129) | SP 800-82 Rev. 3 sections 5.2.3, 6.2.10 (benchmark) | High | Segment; brokered vendor access | OT Engineering Manager | 2027-03-31 |
| AI-005 not validated (G-014) | 21 CFR 820.10(a); ISO 13485 clause 4.1.6 | Moderate | Validate or switch off | VP QA/RA | 2026-11-30 |
| BAA and state notice clocks not tracked (G-123, G-109) | 164.410(b); 164.314(a)(2)(i)(C) | Moderate | BAA terms register with the shortest clock per hospital | Compliance and Privacy Officer | 2026-11-30 |
| No fallback if the 60-day fix date slips (G-023, G-048) | 21 CFR 806.10; postmarket guidance VII.B | Moderate | Day-50 checkpoint; 806.10 report path | VP QA/RA | 2026-10-31 |
| VM-5 legacy fleet: no SBOM, shared key, end of support 2027-06 (G-050) | Postmarket guidance; premarket guidance VI.A | Moderate | SBOM; end-of-support notice; compensating controls guide | VP QA/RA | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Contain** | 2026 Q4 | IP-4 out-of-cycle release and field follow-up; subcontractor BAAs; BAA terms register; AI-005 validated or off; CVD intake in the eQMS; day-50 checkpoint and 806 fallback; complaint handler training | G-035, G-036, G-079, G-080, G-105, G-108, G-014, G-004, G-023, G-048, G-015 |
| **2. Extend the SPDF to the factory** | 2026 Q4 to 2027 Q1 | Station software under design change control with revalidation; provisioning and VM-5 keys in the HSM; threat models and architecture views cover the provisioning path; automated KEV matching and backlog cleared | G-005, G-006, G-013, G-026, G-034, G-037, G-003, G-031 |
| **3. Scale postmarket and OT** | 2027 Q1 | Quarterly IP-4 cycle; TPLC metrics for all products; OT segmentation, brokered vendor access, OT monitoring; privileged activity review; quarterly access reviews; standards issued | G-007, G-033, G-044, G-128 to G-132, G-055, G-064, G-115 |
| **4. Sustain and prepare the next submission** | 2027 Q2 to Q3 | AI-002 submission with the 524B package; VM-5 end-of-support program; SOC 2 scope expansion (P09); annual risk assessment (July 2027) | G-002 (next submission), G-050, G-043, 164.308(a)(1) cycle |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met. The appetite statement in P01 requires every 524B statutory row to be Met by 2027-06-30.

## 6. Pending regulatory changes
- **Section 524B(b)(4) regulations.** FDA may add cybersecurity requirements by regulation. eCFR searches on 2026-09-27 found none. Watch for a proposed rule.
- **FDA guidance updates.** The premarket guidance was issued in September 2023 and revised in June 2025 and on 2026-02-03. Recheck the current version before the AI-002 submission. The postmarket guidance (December 2016) is still posted, now with an FDA note pointing readers to the QMSR.
- **NIST SP 800-82 Rev. 4** (initial public draft, 2026-09-21) restructures the guide around CSF 2.0. Review the final version when published; the OT standard (STD-04) is written against Rev. 3.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of these items is treated as a current obligation. If finalized as proposed, it would affect the CCC:
  - The required and addressable distinction would be removed (20 rows flagged).
  - Encryption at rest and in transit and MFA would be required, with limited exceptions. The CCC already meets both, and VM-5's shared key would need review.
  - A written technology asset inventory and network map would be required.
  - Certain systems would have to be restorable within 72 hours.
  - A compliance audit would be required at least every 12 months; penetration testing is also proposed.
  - Business associates would have to notify covered entities within 24 hours of activating a contingency plan, which would change the P08 notice steps.
- **CIRCIA** final rule not published as of 2026-09-25; the proposed rule would reach manufacturers of class II and III devices (proposed 6 CFR 226.2(b)(11)(iii)). Tracked in the P08 notification matrix.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
