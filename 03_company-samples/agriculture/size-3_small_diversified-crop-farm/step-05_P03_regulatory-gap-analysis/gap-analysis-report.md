# Regulatory Gap Analysis: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm, NAICS 111998) |
| Tier / Vertical | Small / Agriculture, Forestry, Fishing and Hunting |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark**. NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (September 2023), applied to the irrigation and pump-house OT |
| Secondary regulation | FDA Produce Safety Rule record requirements, 21 CFR Part 112, Subpart O (binding; the farm is a covered farm) |
| Also checked | H-2A earnings records (20 CFR 655.122(j)); Florida data security, disposal, and breach notice (Fla. Stat. 501.171, 2026 statutes); PCI DSS as a contract term; 21 CFR Part 121 (N11-R01), found not applicable |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | Operations and Technology Manager (security lead), with the Food Safety and Packing Lead, Office and HR Manager, and Irrigation Technician |
| Workbook | `gap-analysis.csv` (124 rows) |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here. **Step 1 was to find the rule that binds the farm. None of the candidates is a cybersecurity rule that applies to this farm.**

| Candidate | Applies? | Why (citation) |
|---|---|---|
| FSMA intentional adulteration rule, 21 CFR Part 121 (vertical requirement **N11-R01**) | **No** | Part 121 applies to "a domestic or foreign food facility ... required to register under section 415" of the FD&C Act (21 CFR 121.1). Farms do not have to register (21 CFR 1.226(b)). The operation meets the primary production farm definition in 21 CFR 1.227: it grows and harvests crops and packs and holds only its own raw agricultural commodities, with no manufacturing or processing. Two exemptions would also apply: the very small business exemption (under $10,000,000 a year in human food sales, inflation-adjusted, 3-year average; 21 CFR 121.3 and 121.5(a)) and the exemption for farm activities subject to the Produce Safety standards (121.5(d)). Part 121 is also a food defense rule, not an IT security rule |
| Reportable Food Registry, 21 U.S.C. 350f(d) | **No** | The reporting duty falls on a "responsible party," the person who registers a food facility (350f(a)(1)). The farm registers no facility. It stays in the P08 matrix as a buyer-coordination item |
| CIRCIA, 6 U.S.C. 681-681g; proposed 6 CFR Part 226 | **No (proposed, and would not cover the farm as proposed)** | No final rule as of 2026-09-25. As proposed, food and agriculture entities would be covered only if they exceed the SBA size standard; there is no agriculture sector-based criterion. The farm is under the $2.5 million standard for NAICS 111998 (13 CFR 121.201) |
| SEC cybersecurity disclosure rules | No | Privately held |
| FAR 52.204-21 and 52.204-25 | No | No federal contracts or subcontracts. The NRCS conservation contract is a cost-share agreement, not a procurement contract |
| FTC Act Section 5 | Background only | Applies to the farm's own privacy and security promises (for example, the online store privacy notice). Not decomposed into rows |

**Decision: use NIST CSF 2.0 as the benchmark, with SP 800-82 Rev. 3 for OT.** This follows the vertical profile: primary agricultural production has no binding federal cybersecurity regulation, and CSF 2.0 is the sector-neutral baseline. SP 800-82 Rev. 3 is NIST's OT guide. Its Section 6 applies the Cybersecurity Framework to OT, and its Appendix F is an OT overlay for SP 800-53 Rev. 5. Because SP 800-82 Rev. 3 predates CSF 2.0 and was written against CSF 1.1, its OT guidance is applied here to the matching CSF 2.0 subcategories (author mapping, column `ot_application_sp800_82r3`). Neither document is binding. Status ratings measure the farm against a voluntary Target Profile, not against a legal duty.

**Secondary regulation: the Produce Safety Rule record requirements.** The farm is a covered farm, because its average annual produce sales over the prior 3 years exceed the inflation-adjusted $25,000 threshold (21 CFR 112.4(a)). Subpart O is the most relevant binding rule for the primary system: it requires records that are created at the time of the activity, accurate, legible, indelible, and signed by the person who did the work (112.161(a)), kept for 2 years (112.164(a)(1)), and produced for FDA within 24 hours when kept off site (112.166(a)). Those records live in SYS-01. Only the record requirements were assessed; the Rule's food safety standards (water, soil amendments, and so on) are outside a cybersecurity gap analysis.

**Also checked, because they bind the farm's data:**
- **H-2A earnings records**, 20 CFR 655.122(j): the farm employs 4 H-2A workers. Field tally in SYS-01 is part of the earnings record.
- **Fla. Stat. 501.171**: the farm is a "covered entity" (a commercial entity that maintains personal information). The 2026 statute requires reasonable security measures (subsection (2)), disposal of customer records (8), and breach notices (3)-(6). Its definition of personal information now includes **geolocation** (501.171(1)(g)1.a.(VII)), which reaches the operator location histories in the equipment telematics portal (SYS-08).
- **PCI DSS** applies through the acquirer agreement, not by law. Requirement text is copyrighted and is not reproduced.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current as of 2026-09-23 and the 2026 Florida Statutes, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the farm's CSF Target Profile (High 36, Medium 39, Low 31), set by the security lead and the majority owner from the risk register (P01) and BIA (P05).
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping (no official NIST mapping exists).
4. **Evidence.** Current state was established from the intake evidence (exports, documents, contracts, and the walk-throughs of both blocks on 2026-07-08 and 2026-07-09), gap analysis interviews with the majority owner, Farm Manager, Operations and Technology Manager, Irrigation Technician, Food Safety and Packing Lead, and Office and HR Manager (EV-049), interviews with 6 other staff (EV-050), the MSP technician and the integrator's field engineer (EV-053), an account and records review with a sample of 20 harvest records (EV-051), and a walkthrough of headquarters, the pump house, and the North Block on 2026-07-20 (EV-052). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 1 (Partial).** Security has been ad hoc and informal. **Target: Tier 2 (Risk Informed) by 2027-08**, meaning practices approved by the majority owner and driven by the risk register, which is realistic for a 15-person farm with a part-time security lead.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 4 | 13 | 14 | 0 |
| CSF 2.0 Identify (21) | 3 | 9 | 9 | 0 |
| CSF 2.0 Protect (22) | 2 | 12 | 7 | 1 |
| CSF 2.0 Detect (11) | 0 | 1 | 10 | 0 |
| CSF 2.0 Respond (13) | 0 | 2 | 11 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 7 | 0 |
| **CSF 2.0 subtotal (106)** | **9** | **38** | **58** | **1** |
| Produce Safety records, 21 CFR 112 Subpart O (7) | 2 | 4 | 1 | 0 |
| H-2A earnings records, 20 CFR 655.122(j) (3) | 0 | 3 | 0 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 3 | 3 | 0 |
| PCI DSS, contractual (1) | 1 | 0 | 0 | 0 |
| 21 CFR Part 121, N11-R01 (1) | 0 | 0 | 0 | 1 |
| **Total (124)** | **12** | **48** | **62** | **2** |

Of the 110 unmet or partially met rows, 17 are rated High, 51 Moderate, 41 Low, and 1 Very Low.

**The pattern:** the farm has started to govern and assess (Govern and Identify are about half met or partly met, mostly because of the 2026 risk assessment), but it **cannot detect, respond to, or recover from** an attack: 28 of the 32 Detect, Respond, and Recover subcategories are Not met. The OT picture is the same: the irrigation system can be reached from the office network and the integrator's remote tool, and nobody would see a change.

The not applicable CSF row is PR.PS-06 (secure software development): the farm writes no software. PLC logic written by the integrator is covered by ID.RA-07 (change control) and GV.SC-05 (supplier requirements).

## 4. Priority gaps and roadmap
| Gap | Row(s) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Integrator always-on remote access; no supplier security terms | G-026, G-055, G-078 | High | Jump host with named accounts, MFA, and session logging; security terms in the integrator agreement | Operations and Technology Manager | 2026-10-31 (access); 2026-12-31 (terms) |
| Flat network; OT reachable from office and Wi-Fi | G-071 | High | Separate OT, office, and packing shed networks with firewall rules | Operations and Technology Manager | 2026-12-31 |
| Backups exposed and untested; PLC program held only by the integrator | G-064, G-101 | High | Immutable second-region backups; quarterly restore tests; versioned PLC and HMI backups | Operations and Technology Manager | 2026-12-31 |
| No freeze-protection resilience or written manual procedure | G-073 | High | Standalone alarm dialer; freeze-night staffing; manual start procedure tested each November | Farm Manager | 2026-11-15 |
| No endpoint detection or OT change alerting | G-079 | High | EDR with after-hours alerting; setpoint and schedule change alerts | Operations and Technology Manager | 2027-01-31 |
| Shared and default credentials (tally tablets, HMI, OT devices) | G-053, G-108, G-114 | High | Named accounts and PINs; change defaults; password manager | Farm Manager / Operations and Technology Manager | 2026-11-30 |
| Departed accounts active; personnel files over-shared | G-057, G-117 | High | Same-day removal; season-end reviews; restrict the personnel library | Office and HR Manager | 2026-10-31 |
| No change control for PLC, HMI, and pivot settings | G-045 | High | Change log approved by the Irrigation Technician | Irrigation Technician | 2026-11-30 |
| HMI and OT firmware never patched; no vulnerability scanning | G-066, G-039 | High | Integrator-tested quarterly HMI patching; monthly scans of office and cloud; annual OT review | Operations and Technology Manager | 2027-01-31 |
| No security awareness training; no Spanish materials | G-059 | High | Annual training at the pre-season meeting in English and Spanish; phishing exercises | Operations and Technology Manager | 2026-11-30 |
| Produce Safety and H-2A records depend on one SaaS copy | G-110, G-111, G-113, G-115, G-116 | Moderate | Monthly SYS-01 export; retention schedule (2 years Produce Safety; 3 years H-2A) | Food Safety and Packing Lead / Office and HR Manager | 2026-12-31 |
| No breach procedure or notice templates | G-118, G-119 | Moderate | P08 notification matrix (approved 2026-08-31); English and Spanish templates; tabletop | Majority owner and General Manager | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **CIRCIA** (6 CFR Part 226, proposed, 89 FR 23644): no final rule as of 2026-09-25. As proposed it would not cover the farm (section 1). Recheck when a final rule publishes, because scope may change.
- **NIST SP 800-82 Rev. 4**: NIST posted an initial public draft with comments due 2026-11-30 (CSRC planning note of 2026-09-21). It is a draft and was not used. Rows with an OT note flag it in `pending_rule_change`.
- **H-2A rules (20 CFR Part 655):** the Department of Labor proposed on 2025-07-02 (90 FR 28919) to rescind provisions of its 2024 farmworker protections final rule (89 FR 33898), which amended 20 CFR 655.122. No final rescission was found in the Federal Register as of 2026-09-25. Whether the proposal would change the content of the earnings records in 655.122(j)(1) was not verified. The farm follows the current text.
- **No pending changes** were found in the Federal Register for 21 CFR Part 112 after the 2024 agricultural water rule (89 FR 37448, 2024-05-06, which also amended 112.161 at 89 FR 37519) and its 2024-09-24 follow-up notice. Fla. Stat. 501.171 was read as the 2026 statute; state bills were not tracked.
