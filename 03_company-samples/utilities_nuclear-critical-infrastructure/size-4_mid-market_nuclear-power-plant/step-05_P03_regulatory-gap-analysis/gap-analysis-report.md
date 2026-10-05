# Regulatory Gap Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station, NAICS 221113) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Primary regulation | **10 CFR 73.54**, decomposed by paragraph, with the CSP's controls benchmarked against **NRC Regulatory Guide 5.71 Rev. 1** (February 2023) Appendices A.4.1, B, and C. Text checked on eCFR (version date 2026-09-23) |
| Also analyzed | 10 CFR 73.77; 10 CFR 73.21-73.22; 10 CFR 73.56; 10 CFR 73.58 and 73.55(m); NERC CIP-002-5.1a and CIP-003-9 (low impact); Fla. Stat. 501.171. Applicability decided for 10 CFR 73.110, CIRCIA, Form DOE-417, and SEC rules |
| Assessment dates | 2026-07-06 to 2026-07-31 (Station walkthrough 2026-07-21 to 2026-07-23); evidence refreshed with P07 results through 2026-08-21 |
| Assessor | Compliance and GRC Lead and the IT Security Manager, with the Cyber Security Program Manager and the Regulatory Affairs Manager; reviewed by Nuclear Oversight |
| Approved | Site Vice President, 2026-09-17 |
| Workbook | `gap-analysis.csv` (85 rows, G-001 to G-085) |

## 1. Applicability
**Primary business line:** generation of electricity from one Part 50 licensed pressurized water reactor, sold at wholesale.

| Regulation | Applies? | Basis |
|---|---|---|
| 10 CFR 73.54 | **Yes** | The section applies to "each licensee currently licensed to operate a nuclear power plant under part 50." The company holds a Part 50 operating license, and its NRC-approved CSP is a license condition. No size exemption exists |
| RG 5.71 Rev. 1 | **Benchmark** | NRC guidance describing an acceptable approach to 73.54. The company's licensing basis is its approved CSP (NEI 08-09 Rev. 6 template). RG 5.71 Rev. 1 is used here because it is public, current, and organized control by control. A difference from RG 5.71 is not a violation unless it is also a departure from the approved CSP; each such row says which it is |
| 10 CFR 73.77 | **Yes** | Applies to "each licensee subject to the provisions of § 73.54 or § 73.110" |
| 10 CFR 73.21-73.22 | **Yes** | Power reactor licensees must maintain an information protection system with the 73.22 measures (73.21(a)(1)(i)) |
| 10 CFR 73.56 | **Yes** | Includes "any individual whose duties and responsibilities permit the individual to take actions by electronic means, either on site or remotely, that could adversely impact" safety, security, or EP (73.56(b)(1)(ii)) |
| 10 CFR 73.58; 73.55(m) | **Yes** | 73.58 applies to operating power reactor licensees. 73.55(m)(2) requires the security program review to include "cyber security programs" |
| NERC CIP-002-5.1a, CIP-003-9 | **Yes, low impact only** | The company is a registered Generator Owner and Generator Operator. The unit (about 1,020 MW) is below the 1,500 MW medium-impact criterion 2.1, and the Planning Coordinator and Transmission Planner have not designated it under criterion 2.3 or 2.6, so its BES Cyber Systems are low impact under criterion 3.3. Systems, structures, and components "regulated by the Nuclear Regulatory Commission under a cyber security plan pursuant to 10 C.F.R. Section 73.54" are exempt (CIP-002-5.1a Applicability 4.2.3.3). That leaves the dispatch telemetry RTU, the dispatch workstation, and interconnection revenue metering (SYS-15) |
| Fla. Stat. 501.171 | **Yes** | The company holds personal information of Florida residents (employees, contractors, access authorization files) |
| 10 CFR 73.110 | No | Part 53 plants that elect it; the company is a Part 50 licensee (G-082) |
| CIRCIA | **Not in effect** | No final rule was published as of 2026-09-25. As proposed (89 FR 23644), the nuclear sector criterion (owns or operates a commercial nuclear power reactor) would cover the company regardless of size. The P08 runbooks note it as proposed only (G-083) |
| Form DOE-417 | No, as a filer | The form instructions define "Generating Entities" as entities with 300 MW or more dedicated to end-use customers "except for commercial power reactors regulated by the Nuclear Regulatory Commission and subject to the physical and cybersecurity event notification requirements of 10 CFR Part 73." The Balancing Authority files; the company gives it information (G-084) |
| SEC Form 8-K Item 1.05 and Reg. S-K Item 106 | No | The company is privately held (G-085) |

**What is not decomposed here.** 10 CFR 50.72 and 50.73 (safety event reporting) and 73.1200 (physical security event notifications) are referenced in P08 where a cyber event could also trigger them, but they are not rated. The emergency plan rules and export controls (Part 810 and Part 110) are outside this cyber analysis.

## 2. Method
1. **Requirements.** 10 CFR rows follow the regulation's own paragraph structure at the most granular citation that can be verified separately. Brief quotes come from the public-domain eCFR text. RG 5.71 Rev. 1 rows follow the guide's appendix sections (public NRC guidance), one row per control family. NERC CIP rows list the requirement number with a short summary in the author's own words; the standards' text is not reproduced.
2. **Requirement type.** "Mandatory (regulation; CSP license condition)" for 10 CFR; "NRC guidance" for RG 5.71; "Mandatory (NERC Reliability Standard)"; "Mandatory (state law)".
3. **Crosswalk.** No official NIST mapping exists for 10 CFR 73.54, RG 5.71, or NERC CIP, so every CSF 2.0 and SP 800-53 mapping is the **author's mapping**. RG 5.71 draws on SP 800-53 and SP 800-82, but the guide does not publish a control-by-control crosswalk that was used here.
4. **Evidence.** Interviews (Cyber Security Program Manager and the CST, Director of Security, Shift Managers, Regulatory Affairs Manager, Emergency Preparedness Manager, IT Director, IT Security Manager, MSSP service lead), document review (CSP and implementing procedures in the SRI room, the 2025 Nuclear Oversight review, NERC low-impact plan), configuration exports, and the Station walkthrough. SGI was reviewed only in the SGI room by authorized individuals; no SGI left it.
5. **Evidence sampling.** Samples were chosen at random from system-generated populations, using the co-sourced internal audit firm's attribute sampling table:
   - IT change tickets 2024-2026: 25 of 212 (3 touched Level 3 data or EP functions without a CST evaluation);
   - CDA design change packages 2025-2026: 15 of 41 (all evaluated);
   - CDA assessment packages: 10;
   - cyber condition reports in the CAP: 12 (all recorded within 24 hours);
   - SGI-authorized individuals: 10 of 64;
   - SGI documents for marking: 10;
   - outage contractor training records: 25 of 96 sampled from the 2025 outage roster;
   - PMMD kiosk log entries: 20; Level 2 field tablets: 20;
   - third-party transient cyber asset connections to the dispatch network: 12;
   - CDA-privileged staff in the access authorization program: 18 of 18;
   - general file shares searched for SRI markings: 4 (3 SRI documents found).
   Each `evidence` cell names the sample and its result.
6. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 10 CFR 73.54 (by paragraph) | 16 | 10 | 0 | 0 | 26 |
| RG 5.71 Rev. 1 benchmark (A.4.1, B.1-B.5, C.1-C.13) | 14 | 5 | 0 | 0 | 19 |
| 10 CFR 73.77 | 4 | 6 | 0 | 0 | 10 |
| 10 CFR 73.21-73.22 (SGI) | 7 | 1 | 0 | 0 | 8 |
| 10 CFR 73.56 | 1 | 2 | 0 | 0 | 3 |
| 10 CFR 73.58 and 73.55(m) | 1 | 1 | 0 | 0 | 2 |
| NERC CIP-002-5.1a and CIP-003-9 (low impact) | 8 | 2 | 0 | 0 | 10 |
| Fla. Stat. 501.171 | 0 | 3 | 0 | 0 | 3 |
| Applicability decisions (73.110, CIRCIA, DOE-417, SEC) | 0 | 0 | 0 | 4 | 4 |
| **Total** | **51** | **30** | **0** | **4** | **85** |

**Gap risk ratings (30 rows Partially met):** 9 High, 15 Moderate, 6 Low.

**Reading the results.** The CSP itself is mature: every CDA-facing control family in RG 5.71 is Met except where the program meets the business network. The SGI program and the access authorization program are sound. The gaps concentrate in one place, **the seam between IT and the CSP**:
- changes made by IT that consumed Level 3 data or supported EP functions without a CST evaluation (G-005, G-006, G-008, G-017, G-042, G-067);
- business network detections that may never reach the Shift Manager's 73.77 decision (G-018, G-047 to G-050);
- the Level 2 side of the one-way device (G-012, G-038);
- recovery and recording when business systems fail (G-023, G-051, G-052).

No row is Not met. Each Partially met row has a working control for most of its scope and a specific, bounded gap.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| ERO callout service never evaluated by the CST | 73.54(a)(1)(iii) (G-005) | High | CST evaluation; second callout path | Emergency Preparedness Manager | 2026-11-30 |
| CDA analysis not current for IT-initiated changes | 73.54(b)(1) (G-008) | High | Analyze the 3 changes; IT change gate | Cyber Security Program Manager | 2026-11-30 |
| Modifications not evaluated before implementation | 73.54(d)(3) (G-017); RG 5.71 C.11 (G-042); 73.58 (G-067) | High | CSP scope and 73.58 questions on every IT change and purchase, with CST sign-off; CAP entries | Cyber Security Program Manager | 2026-11-30 |
| Level 2 side of the boundary not hardened or monitored | 73.54(c)(2) (G-012); RG 5.71 C.7 (G-038) | High | Re-home the receive server management interface; boundary-attempt alerting | Cyber Security Program Manager | 2026-10-31 |
| Business network events may not reach the 73.77 decision | 73.54(d)(4) (G-018); 73.77(a)(2)(i) (G-047); 73.77(a)(2)(iii) (G-049) | High | Integrated P08 runbooks; IT calls the Shift Manager and the CST; external reports only through the decision point; joint tabletop 2026-11-05 | IT Security Manager | 2026-11-30 |
| CIP-003-9 Section 6.3 not implemented | CIP-003-9 Att. 1 Sec. 6 (G-077) | High | Detection on the RTU vendor path; self-report decision | Compliance and GRC Lead | 2026-10-31 |
| No manual CAP fallback for 24-hour recording | 73.77(b)(1)-(2) (G-051, G-052) | Moderate | Paper CAP intake procedure; drill | Regulatory Affairs Manager | 2026-11-30 |
| EP-support administrators outside the access authorization program | 73.56(b)(1)(ii) (G-064) | Moderate | Enroll or reassign after the CST evaluation | Director of Security | 2026-12-31 |
| Access authorization files reachable by domain administrators | 73.56(m) (G-065); 501.171(2) (G-079) | Moderate | Dedicated enclave administrators | Director of Security | 2027-01-31 |
| Transient cyber asset evidence | CIP-003-9 Att. 1 Sec. 5 (G-076) | Moderate | Kiosk log for every connection | Compliance and GRC Lead | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01 R-006, R-007, R-009, R-011, R-013, R-017, R-030, R-052) and the POA&M (P07 POAM-003, POAM-005, POAM-007, POAM-010, POAM-012, POAM-014, POAM-019). The 6 CSP-related High gaps are also entered in the corrective action program, because a 73.54 program deficiency must be recorded there within 24 hours of discovery (73.77(b)(1)); they were entered on 2026-07-24 and 2026-07-27, within 24 hours of each determination.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Close the seam** | 2026 Q4 | CST evaluations of the 3 changes; IT change gate with CST and 73.58 questions; receive server interface re-homed; CIP-003-9 Section 6.3 detection; paper CAP fallback; integrated runbooks and joint tabletop | G-005, G-006, G-008, G-017, G-038, G-042, G-047 to G-052, G-067, G-077 |
| **2. Monitor and restrict** | 2026 Q4 to 2027 Q1 | SIEM onboarding with boundary-attempt alerting; enclave administrator separation; EP-support administrators in the program; transient asset evidence | G-012, G-018, G-020, G-064, G-065, G-076, G-079 |
| **3. Ready for the outage** | 2027 Q1 (before 2027-03-08) | Contractor training with PMMD and SRI content; tablet labeling; restoration planning for EP support; WMS failover test (P07) | G-015, G-023, G-027, G-041 |
| **4. Sustain** | 2027 Q2 to Q4 | Record retention tagging; vendor contract amendments; Nuclear Oversight 73.55(m) review in 2027 covering the IT seam | G-026, G-081 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met to Met, and CSP-related items are tracked to closure in the CAP.

## 6. Pending regulatory changes
**NRC "Modernizing Security Requirements" proposed rule** (91 FR 38928, 2026-06-26; comments closed 2026-07-27; issued under Executive Order 14300). It was **not final as of 2026-10-05** and is not treated as a current obligation. As proposed, it would:
- replace "high assurance" with "reasonable assurance" in 73.54(a) and other security sections;
- eliminate the introductory paragraph of 73.54 and make conforming changes to 73.54(g);
- update RG 5.71, which the NRC describes as "cutting approximately 19 percent of controls," and allow credit for cybersecurity best practices already in use;
- replace the 73.77 notification categories (1, 4, and 8 hours) and the 24-hour CAP recording with notification under 50.72 or 73.1200 based on the function adversely impacted, and withdraw RG 5.83;
- let future Part 50 and Part 52 licensees elect 73.110.

**Effect on this analysis.** If finalized as proposed, the 73.77 rows (G-046 to G-055) would be restructured, and some RG 5.71 rows could fall away. **The IT-to-CSP seam gaps would not go away**: the 73.54(b)(1) analysis, the 73.54(d)(3) evaluation of modifications, and 73.58 remain in the proposed text. Management will close them regardless.

**Other 2026 NRC proposals** (for example "Regulatory Enhancements for Reactor Licensing, Decommissioning, and Operational Oversight," 91 FR 60702, 2026-09-24, comments due 2026-11-09) were checked for cybersecurity changes; the text mentions cybersecurity only in passing and was not analyzed further.

**NERC.** CIP-003-9 Section 6 became effective 2026-04-01 (G-077). Future effective dates noted, not analyzed: the virtualization revisions including CIP-002-8 and CIP-003-10 (2028-07-01) and CIP-003-11 (2029-07-01).

**CIRCIA.** Proposed only (G-083). Regulatory Affairs will review the final rule within 30 days of publication (P01 R-049).

The `pending_rule_change` column flags each affected row.
