# Regulatory Gap Analysis: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (privately owned community water system, 330 persons served) |
| Tier / Vertical | Sole Proprietorship / Water and Wastewater Systems |
| Applicability tested first | SDWA section 1433, 42 U.S.C. 300i-2 (C-WATER-R01): **not applicable**. CIRCIA (C-WATER-R02): **proposed only** |
| Regulation analyzed | The national primary drinking water regulation duties a cyber event would trigger: public notification (40 CFR Part 141 Subpart Q), Ground Water Rule compliance monitoring, treatment technique, and reporting (141.403(b)(3), 141.404(c), 141.405), and reporting and records (141.31, 141.33) |
| Voluntary benchmark | The 300i-2(a)(1)(A) and (b) elements, and NIST CSF 2.0 outcomes with OT guidance from NIST SP 800-82 Rev. 3 |
| Also analyzed | Fla. Stat. 501.171 (customer data), narrowly |
| Versions checked | 40 CFR Part 141 sections read from the eCFR (version date 2026-09-23); 42 U.S.C. 300i-2 statute text; EPA AWIA section 2013 page (last updated May 14, 2026); Fla. Stat. 501.171 (2026) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Owner-operator, with the on-call IT technician (confidentiality agreement since 2026-07-15). Evidence is self-attested, checked on screen or at the panel where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
**SDWA section 1433 does not apply (G-001, G-002).** The risk and resilience assessment and the emergency response plan are duties of each "community water system serving a population of greater than 3,300 persons" (42 U.S.C. 300i-2(a)(1) and (b)). This system serves 330 persons. Business size plays no part: the only test is population served, and the system is a tenth of the threshold. The statute does tell EPA to give "guidance and technical assistance to community water systems serving a population of less than 3,300 persons" (300i-2(e)), and EPA lists a Small System Risk and Resilience Assessment Checklist and cyber incident resources on its AWIA section 2013 page. This analysis uses the statute's elements as a **voluntary** checklist (G-018 to G-024). They are not legal duties for this system.

**CIRCIA does not apply (G-003).** No final rule had been published as of 2026-09-25. Even as proposed, the system would fall outside both tests: it is SBA-small (proposed 226.2(a) size test), and the water-sector criterion covers systems serving more than 3,300 people.

**What does bind the business.** The system is a community water system under 40 CFR 141.2 (138 connections used by year-round residents), so all of 40 CFR Part 141 applies at any size. Three parts of it decide what a cyber event costs:
- **Public notification (Subpart Q).** A waterborne emergency, "such as a failure or significant interruption in key water treatment processes", requires a Tier 1 notice and consultation with the primacy agency within 24 hours (141.202(a) Table 1 item (7) and (b)). A remote change that stops the chlorine feed is exactly that kind of interruption.
- **Ground Water Rule.** Because the owner notified the state that the wells get 4-log virus treatment, the system does daily grab-sample compliance monitoring (141.403(b)(3)(i)(B)). If 4-log treatment is not restored within **4 hours**, that is a treatment technique violation (141.404(c)) needing a Tier 2 notice within 30 days (141.404(d), 141.203(b)). If the state-specified minimum residual is not restored within 4 hours, the state must be told **by the end of the next business day** (141.405(a)(1)).
- **Reporting and records.** Notice certification within 10 days (141.31(d)(1)); records kept 3, 5, or 10 years (141.33, 141.405(b)).

These rules say nothing about passwords or MFA. They set the **clocks and consequences** that the cyber controls in the benchmark must protect. That is why the benchmark rows are judged against them.

**Fla. Stat. 501.171** applies narrowly: the billing vendor holds customer portal user names and passwords, which are personal information under 501.171(1)(g)1.b (G-038 to G-040).

## 2. Method
1. **Requirements.** Binding rows follow the CFR structure at paragraph level, with brief quotes. Voluntary rows follow 300i-2(a)(1)(A)(i)-(vi) and (b)(1)-(4). Benchmark rows use the CSF 2.0 subcategories that matter most for a remote-accessed PLC panel, each tied to the SP 800-82 Rev. 3 section that explains it for OT.
2. **Crosswalk.** CFR, statute, and Florida rows are an **author mapping** (no official mapping exists). Benchmark rows use a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`); IA-2(1) and MA-4 are labeled as author additions.
3. **Evidence.** Self-attested and checked with the IT technician: portal user list and audit log, router and laptop settings (2026-07-23), the panel walkthrough, the 2024 notice file, the operating log, and vendor terms.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 levels.

## 3. Results summary
| Group | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| Applicability (SDWA 1433, CIRCIA) | 3 | 0 | 0 | 0 | 3 |
| 40 CFR 141 Subpart Q public notification | 6 | 2 | 4 | 0 | 0 |
| 40 CFR 141 Subpart S Ground Water Rule | 4 | 1 | 2 | 1 | 0 |
| 40 CFR 141.31 and 141.33 reporting and records | 4 | 4 | 0 | 0 | 0 |
| 300i-2 elements (voluntary) | 7 | 3 | 4 | 0 | 0 |
| OT cyber benchmark (CSF 2.0 with SP 800-82r3) | 13 | 1 | 2 | 10 | 0 |
| Fla. Stat. 501.171 | 3 | 0 | 3 | 0 | 0 |
| **Total (40)** | **40** | **11** | **15** | **11** | **3** |

Of the 26 unmet or partially met rows, gap risk is **4 High, 12 Moderate, and 10 Low**.

**The main finding.** The paperwork duties are in good shape: the 2024 boil water notice went out in about 10 hours and was certified on time, and every records row is met. The weakness is that **nothing protects the 4-hour clock**. The chlorine feed can be stopped from the portal with one reused password (G-027) or through the integrator's always-on account (G-028), the owner did not know the next-business-day state notice existed (G-014), and the steps to restore the feed by hand live only in the owner's head (G-013). Three of the four High gaps are about who can reach the panel.

**What is working.** Compliance monitoring is a daily grab sample with a field test kit, so it does not depend on any computer (G-012). Every pump has a hand switch, and the chlorine pump cannot exceed its mechanical stroke setting (G-036).

## 4. Action list (half page)
In order. The first five cost nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | App-based MFA on every portal account; named account for the relief operator | G-027, G-026 | High | 2026-09-15 |
| 2 | Disable the integrator's account between owner-approved sessions; maintenance log | G-028 | High | 2026-09-15 |
| 3 | Router: new password, firmware update, recorded settings (remote administration already off) | G-030 | Moderate | 2026-09-15 |
| 4 | Notice decision sheet in the well house binder: cyber trigger, 4-hour clocks, next-business-day state notice, Tier 2 template, offline contact list | G-004, G-005, G-007, G-008, G-014 | Moderate | 2026-09-30 |
| 5 | Walk through the P08 runbook with the relief operator and IT technician | G-024, G-034 | Moderate | 2026-09-30 |
| 6 | Two owner-held copies of the current PLC program and HMI project | G-029 | Moderate | 2026-10-15 |
| 7 | Written dose table, manual-operation sheet, and restore steps | G-013, G-035 | High | 2026-10-31 |
| 8 | Monthly portal log review | G-033 | Moderate | 2026-10-31 |
| 9 | Integrator contract terms; billing vendor SOC 2 report and breach notice terms | G-037, G-021, G-038, G-039 | Moderate | 2026-10-31 |
| 10 | Firmware and default passwords on the PLC and HMI with the integrator; cybersecurity course | G-026, G-031, G-032 | High | 2026-11-30 |

High and Moderate gaps are linked to the risk register (P01: R-001, R-002, R-003, R-004, R-005, R-008, R-010, R-013) and to the POA&M (P07).

## 5. Pending regulatory changes
None of these is a current obligation.
- **CIRCIA** (proposed 6 CFR Part 226; NPRM 89 FR 23644, April 4, 2024): still proposed. As proposed, this system would not be covered (G-003). Recheck when a final rule is published.
- **NIST SP 800-82:** this analysis uses Rev. 3 (September 2023), the current final version. Recheck section references when a newer revision is final.
- **EPA's 2023 sanitary survey cyber memorandum** is reported in the vertical profile as withdrawn in October 2023. That status was not re-verified for this analysis, and the memorandum is not relied on.
- **Population growth.** If the subdivision ever grew past 3,300 persons served, section 1433 would apply. At 138 lots that is not realistic, but the row stays in the annual review.
