# Regulatory Gap Analysis: Cris Santos Company | Utilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Electric Cooperative, Inc. (member-owned electric distribution cooperative; RUS electric distribution borrower) |
| Tier / Vertical | Micro / Utilities |
| Primary regulation | RUS electric system operations and maintenance rule, **7 CFR Part 1730, Subpart B** (1730.20 to 1730.29), binding through the cooperative's RUS loan contract and mortgage |
| Secondary | Form **DOE-417** electric emergency incident reporting (Federal Energy Administration Act of 1974 sec. 13(b), Pub. L. 93-275; OMB 1901-0288); Florida Information Protection Act, **Fla. Stat. 501.171** |
| Registry default replaced | NERC CIP Reliability Standards (N22-R01): not applicable, the cooperative is not NERC-registered (section 1) |
| Versions checked | 7 CFR Part 1730 read from eCFR, point-in-time 2026-09-23. NERC Rules of Procedure Appendix 5B, Revision 8 (effective 2024-06-27). Form DOE-417 and instructions from the OMB-approved collection (expires 2027-05-31). Fla. Stat. 501.171 and 366.02 (2026) from the Florida Legislature site |
| Assessment dates | 2026-07-20 to 2026-07-31; G-006 and G-007 updated after P07 field testing (2026-08-11) |
| Assessor | Office and Finance Manager (Security Coordinator) and the Line Superintendent, with the MSP lead technician |
| Approved | 2026-08-31 by the General Manager |

## 1. Applicability
**The registry's primary regulation, NERC CIP, does not apply.** The reasoning:

1. **Who must comply with CIP.** Federal Power Act section 215 (16 U.S.C. 824o) reaches users, owners, and operators of the bulk-power system, and NERC applies its standards to entities on the NERC Compliance Registry. The CIP standards then apply to a Distribution Provider only if it owns certain protection or restoration equipment.
2. **Registration test.** The NERC Statement of Compliance Registry Criteria (Rules of Procedure Appendix 5B, Revision 8) registers a Distribution Provider only if it meets one of the criteria below. The cooperative meets none:

| Appendix 5B criterion (summary) | Cooperative fact | Met? |
|---|---|---|
| III.a.1: DP system serving more than 75 MW of peak Load directly connected to the BES | 2025 peak 2.6 MW, served from a 69 kV radial tap owned by the G&T | No |
| III.a.2: owns a required UVLS program, Remedial Action Scheme, or transmission Protection System | None. The G&T owns the high-side circuit switcher and its protection | No |
| III.a.3: responsible for Nuclear Plant Interface Requirements | None | No |
| III.a.4: field switching for a Transmission Operator restoration plan | None | No |
| III.b: UFLS-only DP that owns UFLS relays in a required program | No UFLS relays; the G&T carries the required UFLS program at its own substations and confirmed in writing in 2024 that it does not rely on cooperative equipment | No |

3. **Material impact.** Appendix 5B also lets NERC register an entity below the criteria if it has a material impact on bulk power system reliability, decided by the NERC-led Registration Review Panel. One of the listed factors is whether misuse of the entity's cyber assets could harm an associated Balancing Authority or Transmission Operator. With 2.6 MW of load on one radial tap, the cooperative does not expect this, and neither NERC nor its Regional Entity has contacted it.
4. **Result.** No CIP standard and no NERC EOP-004 duty applies. The four vertical registry IDs and NERC EOP-004 are recorded as Not applicable in `gap-analysis.csv` (G-046 to G-050): NERC CIP (N22-R01), TSA pipeline directives (N22-R02), NRC 10 CFR 73.54 (N22-R03), and SDWA section 1433 (N22-R04, the cooperative serves the county water plant but does not operate it).

**What does apply: the RUS rule.** The cooperative is an RUS electric distribution borrower. 7 CFR Part 1730 states the policies and procedures that clarify and implement the operations and maintenance provisions of the borrower's security instrument and loan contract (1730.1(b)). It requires each borrower to keep records of the "physical, cyber and electrical condition and security" of its system (1730.20), to perform a Vulnerability and Risk Assessment (1730.27), and to keep an Emergency Restoration Plan with a Business Continuity Section for computer and financial systems (1730.28(c)(4)). The General Manager must certify both to RUS before a new loan is considered (1730.26(b)). There is no size exemption. The rule is not a cyber standard, so it says *what* must exist (a VRA, an ERP, records, inspections) but not *which* controls. NIST CSF 2.0 with SP 800-82 Rev. 3 supplies the control benchmark in P02 and P07.

**State status.** Under Fla. Stat. 366.02(4) the cooperative is an "electric utility", but 366.02(8) excludes cooperatives organized under the Rural Electric Cooperative Law from "public utility". No Florida cybersecurity rule applies. Fla. Stat. 501.171 applies because its "covered entity" definition names cooperatives and the cooperative holds Social Security numbers and the medical-needs list.

**Secondary regulation: DOE-417.** The form's definition of electric utility includes rural electric cooperatives. Electric utilities must give their Balancing Authority the information it needs and file the form themselves where the BA will not (instructions, Who Must Submit 1.a). The 1-hour criteria that matter here are criterion 3 (a cyber event that causes interruptions of electrical system operations) and criterion 4 (complete operational failure or shut-down of the distribution system). Criterion 2 uses the NERC term "Reportable Cyber Security Incident" and is not expected to apply to an unregistered entity. Criterion 11 (a cyber event that could affect reliability) has a 6-hour clock. The 50,000-customer criterion cannot be met with about 820 meters.

## 2. Method
1. **Requirements.** Rows follow the official structure of 7 CFR Part 1730 Subpart B, section by section and paragraph by paragraph, with short quotes where the wording matters. Section 1730.20 was split into its five separate duties. Section 1730.29 (grantees) adds no duty for this borrower and has no row. DOE-417 rows follow the form's own criteria and instructions. Florida rows follow 501.171 subsections.
2. **Crosswalk.** Each row is mapped to CSF 2.0 and SP 800-53 Rev. 5. These are **author mappings**: NIST has published no mapping for 7 CFR 1730, DOE-417, or 501.171.
3. **Documentary evidence.** Each status rests on a named record: the 2005 VRA, the 2021 ERP and its contact list and signature page, the 2023 RUS Form 300 and CAP file, Board minutes, inspection schedules and forms, exercise sign-in sheets, the G&T's 2024 UFLS letter, vendor contracts, the SCADA and AMI user lists, the shared drive listing, and the Substation 1 and line recloser walkthrough on 2026-07-23. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. G-006 and G-007 also reflect P07 field testing on 2026-08-11. Later actions are noted in the remediation column but do not change the status.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 1730.20 General (5 duties) | 1 | 3 | 1 | 0 |
| 1730.21 Inspections and tests | 0 | 2 | 0 | 0 |
| 1730.22 to 1730.25 Borrower analysis, RUS review, corrective action | 2 | 1 | 2 | 1 |
| 1730.26 Certification | 0 | 0 | 1 | 1 |
| 1730.27 Vulnerability and Risk Assessment | 0 | 8 | 1 | 0 |
| 1730.28 Emergency Restoration Plan | 3 | 6 | 3 | 1 |
| **7 CFR 1730 subtotal (37)** | **6** | **20** | **8** | **3** |
| DOE-417 reporting | 0 | 0 | 4 | 0 |
| Fla. Stat. 501.171 | 0 | 3 | 1 | 0 |
| Applicability rows (N22-R01 to N22-R04, EOP-004) | 0 | 0 | 0 | 5 |
| **Total (50)** | **6** | **23** | **13** | **8** |

Of the 36 unmet or partially met rows, by gap risk: 6 High, 19 Moderate, 11 Low.

**What the numbers say.** The cooperative does well on the traditional utility duties RUS has reviewed for years: maintenance, the 2023 corrective action plan, backup power for headquarters, and the FEMA section of the ERP. It does poorly wherever the word "cyber" or "business systems" appears. The VRA predates every digital system the cooperative now runs, the ERP has no Business Continuity Section, field devices are inspected for poles and oil but never for firmware or passwords, and no one knew the DOE-417 reporting duty existed. All four DOE-417 rows are Not met.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| G-038, G-039 | DOE-417 Who must submit; criteria 3 and 4 | High | Filing arrangement with the G&T and BA; DOE-417 account; 1-hour step in P08 | Line Superintendent | 2026-10-31 |
| G-016, G-021 | 1730.27(a), (c)(5) | High | VRA update built from P01 and the 1730.27(c) rows | Office and Finance Manager | 2026-12-31 |
| G-006 | 1730.21(a)-(b) | High | Yearly firmware and password check of every OT device; quarterly external scan | Line Superintendent | 2026-12-31 |
| G-030 | 1730.28(c)(4) | High | ERP Business Continuity Section from the BIA (P05) | General Manager | 2027-01-31 |
| G-015 | 1730.26(b) | Moderate | VRA and ERP certification letter for the 2027 loan | General Manager | 2027-01-31 |
| G-002, G-023 | 1730.20; 1730.27(c)(7) | Moderate | OT inventory with firmware versions | Line Superintendent | 2026-10-31 |
| G-027, G-034 | 1730.28(c)(1), (e) | Moderate | Current contact list; ERP copies in trucks and at homes | Office and Finance Manager | 2026-10-31 |
| G-005 | 1730.20 (portions operated by others) | Moderate | Security terms for the SCADA vendor and MSP; yearly review | General Manager | 2026-12-31 |
| G-042, G-045 | 501.171(2), (8) | Moderate | SSN scans removed after a retention check; download alerts | Office and Finance Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01, mainly R-012, R-013, R-014, R-006) and, where the control was assessed, the POA&M (P07).

**Remediation plan.** The plan fits a 7-person cooperative and is built around the RUS calendar:

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Reporting and contacts | 2026-10-31 | DOE-417 arrangement and runbook steps; Florida notice steps; ERP contact list rebuilt and copies distributed; post-event contact check; county asked about national security assets; OT inventory | G-002, G-004, G-019, G-023, G-027, G-034, G-038 to G-041, G-043 |
| 2. VRA update | 2026-12-31 | Adopt P01, P05 dependencies, critical assets and critical loads into the VRA; inspection forms gain security and firmware checks; vendor contract terms; SSN scan clean-up | G-005, G-006, G-016 to G-018, G-020 to G-022, G-024, G-042, G-044, G-045 |
| 3. ERP update and certification | 2027-01-31 | Business Continuity Section, cyber annex (P08), chain of command, General Manager signature, Board approval; certification letter ready | G-015, G-025, G-028, G-030, G-032, G-033 |
| 4. RUS review preparation | 2027-02-28 | Borrower analysis with operator performance review and cyber trends; Form 300 | G-008 to G-011 |
| 5. Exercise | 2027-05-31 | ERP exercise with a SCADA intrusion scenario; after-action note | G-035 to G-037 |

G-003 (security budget) closes with the Board's approval on 2026-09-17. G-007 (security determinations at inspections, physical items) runs to 2027-03-31 with the re-keying work.

**Progress check.** The Security Coordinator reports progress to the General Manager at the monthly staff meeting, using the P07 POA&M as the tracker, and to the Board of Trustees each quarter.

## 5. Pending regulatory changes
- **7 CFR Part 1730:** no pending amendment found (eCFR point-in-time 2026-09-23). The last changes were 89 FR 17276 (2024-03-11) to 1730.24 and the OMB number.
- **DOE-417:** OMB approval of the current form expires 2027-05-31. Check for a revised form before then.
- **NERC CIP:** future versions take effect from 2028 (virtualization revisions) and 2029 (CIP-003-11). They change requirements for registered entities, not who registers, so the cooperative stays out of scope unless its facts change (G-046).
- **CIRCIA:** the final rule implementing the Cyber Incident Reporting for Critical Infrastructure Act had not been published as of 2026-09-25. It is not a current obligation. Whether a final rule would cover the cooperative was not assessed.
- **DOE bulk-power system Executive Order:** DOE issued a request for information (2026-09-09) implementing an August 2026 Executive Order on securing the bulk-power system supply chain. Watch for any prohibition that reaches distribution equipment bought with the 2027 RUS loan.
