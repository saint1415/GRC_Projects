# Regulatory Gap Analysis: Cris Santos Company | Water and Wastewater Systems | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (investor-owned community water system) |
| Tier / Vertical | Small / Water and Wastewater Systems |
| Primary regulation | SDWA section 1433, Community water system risk and resilience, 42 U.S.C. 300i-2 (as amended by AWIA 2018 section 2013; text in effect on 2026-09-25 per uscode.house.gov) |
| Benchmark for the cyber element | NIST CSF 2.0 outcomes, with OT guidance from NIST SP 800-82 Rev. 3 (September 2023) |
| Secondary regulation | SDWA public notification rule, 40 CFR Part 141 Subpart Q (Tier 1 notice), plus 40 CFR 141.31(d) and 141.33(e) |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | IT Manager with the Operations Manager and the Water Quality Supervisor |

## 1. Applicability
**SDWA section 1433 applies.** Two facts decide it:
- The company is a **community water system**: a public water system that serves at least 15 service connections used by year-round residents, or regularly serves at least 25 year-round residents (42 U.S.C. 300f(15)). It has about 18,400 connections.
- It serves a **population of 46,200**, which is "greater than 3,300 persons" (42 U.S.C. 300i-2(a)(1)). There is no business-size exemption. Being SBA-small does not matter here; population served is the only threshold.

**Deadlines for this system (size category 3,301-49,999):**

| Item | Rule | Date for this system |
|---|---|---|
| First RRA certification | Prior to June 30, 2021 (300i-2(a)(3)(A)(iii)) | Certified June 2021 |
| First ERP certification | Not later than 6 months after completing the RRA (300i-2(b)); EPA listed December 31, 2021 for this category | Certified December 2021 |
| RRA five-year review | At least once every 5 years after the certification deadline, then certify the review (300i-2(a)(3)(B)); EPA lists June 30, 2026 for this category | **Certified 2026-06-26** |
| ERP five-year review | EPA: ERP certifications are due six months from the date of the RRA certification; EPA's table shows December 31, 2026 for systems that certify the RRA on the last day | **Due by 2026-12-26** (six months after 2026-06-26). Internal target 2026-12-11 |
| Record retention | Keep the RRA and ERP for 5 years after each certification (300i-2(d)) | Ongoing |
| Next RRA review | Five years after the 2026 cycle | By June 30, 2031 |

Sources: statute text at uscode.house.gov (42 U.S.C. 300i-2); EPA "AWIA Section 2013" page (last updated May 14, 2026), which gives the second-cycle dates and the six-month ERP rule.

**Watch item on population growth.** The service area is growing. If the population served reaches 50,000 before the next cycle, the company would move into the 50,000-99,999 category, which EPA lists with earlier cycle dates (December 31 for the RRA). The Operations Manager will confirm with EPA which category applies to the 2031 review if that happens.

**What the statute does and does not require.** Section 1433 requires the RRA to assess the resilience of "electronic, computer, or other automated systems (including the security of such systems)" (300i-2(a)(1)(A)(ii)), and the ERP to include strategies to improve "the physical security and cybersecurity of the system" (300i-2(b)(1)). It does not prescribe controls. EPA's page states that EPA "does not require water systems to use any designated standards, methods, or tools", but the system is responsible for fully addressing the statute. This analysis therefore uses **NIST CSF 2.0** outcomes as the yardstick for the cyber element and **NIST SP 800-82 Rev. 3** for how to apply each outcome to OT. The 25 benchmark rows (G-020 to G-044) are voluntary outcomes used to judge whether the cyber element was actually assessed. They are not separate legal requirements.

**Excluded, with reasons:**
- **300i-2(f)** (alternative path using EPA-recognized technical standards): the company certifies under (a) and (b) directly. Not applicable.
- **300i-2(e) and (g)** (EPA guidance to small systems; grant program): duties of EPA, not of the system.
- Wastewater (POTW) planning: the company operates no wastewater system.

**Secondary regulation.** Small tier covers the primary regulation plus the most relevant secondary one. The SDWA **public notification rule** was chosen because a cyber-caused failure or significant interruption in key treatment processes is a "waterborne emergency" that requires a **Tier 1 notice within 24 hours** and **consultation with the primacy agency within 24 hours** (40 CFR 141.202(a) Table 1 item (7) and (b)). That is the binding clock that the ERP's cyber procedures must support. Other rules considered:
- **CIRCIA** (6 U.S.C. 681-681g; proposed 6 CFR Part 226): **not in effect**. No final rule had been published as of 2026-09-25. The proposal would cover community water systems serving more than 3,300 people regardless of business size. Tracked in the `pending_rule_change` column only.
- **Fla. Stat. 501.171**: applies to customer personal information in the CIS. It drives the customer-data notice rows in the P08 notification matrix and is not re-analyzed here.

## 2. Method
1. **Requirements.** Statutory rows follow the structure of 42 U.S.C. 300i-2 at paragraph level, quoting the text briefly. Benchmark rows use CSF 2.0 subcategories that matter most for a SCADA system, each tied to the SP 800-82 Rev. 3 section that explains it for OT (for example sec. 6.2.10, Remote Access, and sec. 5.2.3, Network Security). Secondary rows follow 40 CFR 141.202, 141.205, 141.31(d), and 141.33(e).
2. **Crosswalk.** Statutory and public notification rows were mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author (no official mapping exists). Benchmark rows use a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Controls added beyond that mapping (IA-2(1), IA-2(2), MA-4, AC-3) are labeled as author additions in the `crosswalk_source` column.
3. **Evidence.** Interviews (General Manager, Operations Manager, IT Manager, both Chief Plant Operators, SCADA and Instrumentation Technicians, Water Quality Supervisor, Safety and Compliance Coordinator), document review (2021 RRA and ERP, 2026 review memo, public notice SOP, contracts), configuration exports (firewall, VPN, HMI user lists), and the external exposure scan and site visits from P07.
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Group | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| 300i-2(a) Risk and resilience assessment | 11 | 5 | 6 | 0 | 0 |
| 300i-2(b)-(d), (f) ERP, coordination, records, alternative path | 8 | 2 | 5 | 0 | 1 |
| Cyber element benchmark (CSF 2.0 with SP 800-82r3) | 25 | 2 | 7 | 16 | 0 |
| 40 CFR 141 Subpart Q public notification (secondary) | 7 | 5 | 2 | 0 | 0 |
| **Total (51)** | **51** | **14** | **20** | **16** | **1** |

Of the 36 unmet or partially met rows, 12 are rated High, 20 Moderate, and 4 Low.

**The main finding.** The company met every statutory deadline and its certifications are correct on their face (G-010, G-011). The weakness is substance: the June 2026 certification states that the RRA was reviewed, but the automated-systems element was a 2021 checklist carried forward (G-004). Measured against CSF 2.0, **16 of 25 cyber outcomes are not met**, including every remote access, credential, backup, incident response plan, and recovery outcome for the SCADA system. The same gap flows into the ERP: it has no cybersecurity strategies (G-013), no OT incident procedure (G-014), and no cyber detection strategy (G-016). The ERP must incorporate the findings of the assessment (300i-2(b)), so the RRA addendum has to come first.

**What is working.** The company can run both plants manually, and its chemical feed pumps have hardwired limits and independent alarms that SCADA cannot override (G-038). Physical security (G-030), the emergency interconnect and generators (G-015), and Tier 1 notice mechanics (G-046, G-047, G-049) are sound.

## 4. Priority gaps and roadmap
The roadmap works back from the ERP certification date (2026-12-26).

| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Cyber element not actually assessed | 300i-2(a)(1)(A)(ii) (G-004) | High | RRA cyber addendum from P01 and this analysis; request EPA's free Water Sector Cybersecurity Evaluation | IT Manager | 2026-11-13 |
| No offline backup of PLC logic and HMI projects | CSF PR.DS-11 (G-033) | High | Monthly and after-change offline backups | Operations Manager | 2026-10-15 |
| No MFA on remote access to OT | CSF PR.AA-03 (G-028) | High | MFA on VPN and vendor gateway | IT Manager | 2026-10-31 |
| Uncontrolled vendor remote access | CSF PR.AA-05 (G-029) | High | Remove always-on agent; approved, recorded sessions | Operations Manager | 2026-10-31 |
| PLCs in remote-program mode; exposed modems | CSF PR.PS-01 (G-034) | High | Key switches to RUN; modem hardening | SCADA and Instrumentation Technician | 2026-10-31 |
| No OT incident plan or recovery procedure | CSF RS.MA-01, RC.RP-01 (G-041, G-043) | High | OT playbook (P08) and recovery procedure in the ERP | IT Manager; Operations Manager | 2026-12-11 |
| ERP lacks cyber strategies and procedures | 300i-2(b)(1)-(2) (G-013, G-014) | High | Revise ERP with cyber strategies, OT playbook, manual-mode procedures | IT Manager; Operations Manager | 2026-12-11 |
| Shared and default credentials | CSF PR.AA-01 (G-027) | High | Named HMI accounts; change commissioning passwords | Operations Manager | 2026-12-31 |
| No OT vulnerability identification | CSF ID.RA-01 (G-025) | High | Quarterly exposure scans; annual OT vulnerability review | IT Manager | 2026-12-31 |
| Weak IT/OT segmentation | CSF PR.IR-01 (G-037) | High | OT DMZ; remove dual-homed historian | IT Manager | 2027-03-31 |
| Cyber trigger missing from Tier 1 notice SOP | 40 CFR 141.202(a) (G-045) | Moderate | Add trigger and decision owner | Water Quality Supervisor | 2026-12-11 |
| No offline customer contact list for notices | 40 CFR 141.202(c) (G-048) | Moderate | Monthly offline export in the ERP binder | Customer Service and Billing Manager | 2026-10-31 |

**Key milestones:**
- 2026-10-31: remote access fixed (G-028, G-029), PLC and modem hardening (G-034), OT backups (G-033).
- 2026-11-13: RRA cyber addendum complete (G-001, G-002, G-004 to G-007).
- 2026-11-30: OT cyber tabletop (G-044) and LEPC briefing (G-017).
- 2026-12-11: revised ERP approved and certified to EPA (G-012 to G-016, G-041 to G-043, G-045).

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory and guidance changes
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024) is **still proposed**. CISA held further town halls in June 2026 on scope and burden. If finalized as proposed, the company would be a covered entity through the water-sector criterion (community water system serving more than 3,300 people) even though it is SBA-small. It would then need to report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours, and preserve related data. Rows G-036, G-041, and G-042 are flagged. None of this is treated as a current obligation.
- **NIST SP 800-82 Rev. 4** was released as an initial public draft (CSRC planning note dated 2026-09-21; comments due 2026-11-30). This analysis uses Rev. 3, the current final version. Re-check the section references when Rev. 4 is final.
- **EPA sanitary survey cyber memorandum** (2023): withdrawn in October 2023 according to the vertical profile. Not relied on here.
