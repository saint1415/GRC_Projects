# Regulatory Gap Analysis: Cris Santos Company | Utilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electric distribution utility, NERC-registered Distribution Provider) |
| Tier / Vertical | Small / Utilities |
| Primary regulation | NERC CIP Reliability Standards under Federal Power Act section 215 (16 U.S.C. 824o), scoped to **CIP-002-5.1a** and **CIP-003-9** (low impact) |
| Secondary | Electric incident and event reporting: NERC **EOP-004-4** and Form **DOE-417** |
| Versions checked | NERC CIP standards page (nerc.com), retrieved 2026-09-26: CIP-002-5.1a in effect since 2016-12-27; CIP-003-9 in effect since 2026-04-01 |
| Assessment dates | 2026-07-20 to 2026-07-31; Section 3.1 row updated after P07 testing (2026-08-12) |
| Assessor | IT Manager (Information Security Lead) with the NERC Compliance Coordinator |

## 1. Applicability
**NERC CIP applies, but only at low impact.** The reasoning, step by step:

1. **Who must comply.** Section 215 of the Federal Power Act gives FERC jurisdiction over "all users, owners and operators of the bulk-power system" and requires them to comply with approved reliability standards (16 U.S.C. 824o(b)(1)). NERC enforces through the Regional Entities; for Florida that is SERC, which took over the former FRCC footprint in 2019.
2. **Registration.** The company is on the NERC Compliance Registry as a Distribution Provider. It meets two criteria in the NERC Statement of Compliance Registry Criteria (Rules of Procedure Appendix 5B): III.a.1, a DP system serving more than 75 MW of peak Load directly connected to the BES (2025 peak: 410 MW), and III.a.2, ownership of Facilities that are part of a required transmission Protection System.
3. **Which DPs the CIP standards reach.** CIP-003-9 (like CIP-002-5.1a) applies to a DP only if it owns one of four things for protecting or restoring the BES (Applicability 4.1.2 and 4.2.1). The company's result for each:

| CIP-003-9 Applicability item | Company fact | In scope? |
|---|---|---|
| 4.2.1.1 UFLS or UVLS system that is part of a required program **and** sheds 300 MW or more automatically under a common control system the entity owns | Feeder UFLS relays shed about 125 MW in stages under PRC-006-SERC-03. Each relay acts on its own; there is no common control system | No |
| 4.2.1.2 Remedial Action Scheme subject to a standard | None | No |
| 4.2.1.3 Protection System (not UFLS or UVLS) that applies to Transmission and is subject to a standard | 115 kV line protection relays at Substation N and Substation E, maintained under PRC-005 | **Yes** |
| 4.2.1.4 Cranking Path or initial switching elements from a Blackstart Resource | None | No |

4. **Everything else is exempt.** For DPs, systems and equipment not listed in 4.2.1 are exempt (section 4.2.3.4). That covers the distribution SCADA, the OMS, the AMI, and the feeder devices. The DCC is also not a "Control Center" in the NERC Glossary, which lists only Reliability Coordinator, Balancing Authority, Transmission Operator, and Generator Operator functions.
5. **Impact rating.** CIP-002-5.1a R1 requires DPs to consider "Protection Systems specified in Applicability section 4.2.1." No asset meets a high (Attachment 1 Section 1) or medium (Section 2) criterion. The relays are **low impact** under Attachment 1 criterion 3.6. Only the **asset** (the substation) must be listed, not the systems themselves (R1 Part 1.3).
6. **Result.** CIP-002-5.1a applies in full, and CIP-003-9 applies through R1 Part 1.2, R2 (Attachment 1), R3, and R4. CIP-004 through CIP-011 and CIP-013 apply only to high or medium impact systems. CIP-012 applies only to entities with Control Centers in other functions, and CIP-014 only to Transmission Owners and Operators. None of these apply. The rows are kept in `gap-analysis.csv` as Not applicable so the decision is visible.

**What CIP does not cover.** The low impact scope is 8 relays at 2 substations. Most of the company's operational cyber risk sits in the distribution SCADA and OMS, which CIP does not reach. Those systems are held to NIST CSF 2.0 with SP 800-82 Rev. 3 as a voluntary benchmark. That benchmark runs through the SSP (P02) and the control assessment (P07), not this table.

**Secondary regulation.** Electric incident and event reporting, which drives the P08 notification matrix:
- **NERC EOP-004-4** lists the Distribution Provider as a responsible entity. It requires an event reporting Operating Plan (R1) and reports by the later of 24 hours or the end of the next business day (R2).
- **Form DOE-417** is mandatory under section 13(b) of the Federal Energy Administration Act of 1974 (Pub. L. 93-275). Electric utilities must give their Balancing Authority the information it needs and file themselves where the BA will not. Criteria were read from the OMB-approved instructions (OMB 1901-0288, approved 2024-05-24, expires 2027-05-31).

**Other vertical regimes considered and not applicable:** TSA Security Directive Pipeline-2021-02G (N22-R02; no pipelines), NRC 10 CFR 73.54 (N22-R03; no reactors), SDWA section 1433 (N22-R04; no water system).

## 2. Method
1. **Requirements.** Rows follow each standard's own structure (requirement, part, Attachment 1 section). Summaries are written in this repository's own words; the standards' text is not reproduced. The requirement type column records the standard's Violation Risk Factor.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** NIST has not published an official mapping for NERC CIP.
3. **Evidence.** Current state came from:
   - interviews with the CIP Senior Manager, the Manager of Engineering and Protection, the Manager of System Operations, the NERC Compliance Coordinator, and the SCADA/OT Administrator
   - the CIP-002 record, the policy and plan versions, and the EOP-004 Operating Plan
   - gateway and jump host configurations and PRC-005 test logs
   - walkthroughs of Substation N and Substation E on 2026-07-28
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable.

## 3. Results summary
| Standard | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CIP-002-5.1a (R1, R2) | 5 | 1 | 0 | 0 |
| CIP-003-9 (R1-R4, Attachment 1) | 15 | 10 | 4 | 2 |
| CIP-004 to CIP-014 (11 standards) | 0 | 0 | 0 | 11 |
| EOP-004-4 (secondary) | 2 | 0 | 0 | 0 |
| DOE-417 (secondary) | 0 | 1 | 1 | 0 |
| **Total (52)** | **22** | **12** | **5** | **13** |

Of the 17 unmet or partially met rows, 8 are rated High, 5 Moderate, and 4 Low.

**Potential noncompliance to self-report.** Eight rows (five issues) describe potential violations of an enforceable standard, not only weaknesses:
- R1 Part 1.2.6: the policy lacked the vendor access topic from 2026-04-01 to 2026-09-04
- Attachment 1 Section 3.1: Substation E's open access list, from its 2025 commissioning to 2026-08-13
- Section 4.5: the plan test missed since 2026-06-15
- Sections 5.2.1 and 5.2.2: no review of contractor laptops
- Section 6: vendor remote access controls absent since 2026-04-01 (rows 6.1 to 6.3)

The CIP Senior Manager decided on 2026-09-04 to **self-report** them to SERC by 2026-09-30, with mitigation plans. A "Self-Report" is the Compliance Monitoring and Enforcement Program term (NERC Rules of Procedure Appendix 4C) for a registered entity reporting that it has, or may have, violated a standard. Finding and fixing these before an audit is the reason for this analysis.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Vendor remote access: shared standing account, no detection | CIP-003-9 Att. 1 Sec. 6.1-6.3 | High | Named vendor accounts with MFA; access off by default; detection on the OT DMZ firewall, then passive OT monitoring | Vice President of Operations; IT Manager | 2026-10-31 (detection); 2026-11-30 (accounts) |
| Plan test missed | Att. 1 Sec. 4.5 | High | Tabletop of a Reportable Cyber Security Incident | NERC Compliance Coordinator | 2026-10-20 |
| Contractor laptops not reviewed | Att. 1 Sec. 5.2.1-5.2.2 | High | Pre-connection checklist and contract clause | Manager of Engineering and Protection | 2026-10-31 |
| Open access list at Substation E (corrected) | Att. 1 Sec. 3.1 | High | Access list check in the substation change procedure | Manager of Engineering and Protection | 2026-10-31 |
| Self-report and mitigation plans | CIP-003-9 R1; R2 | High | File with SERC; track mitigation to completion | NERC Compliance Coordinator | 2026-09-30 |
| Untracked control house keys | Att. 1 Sec. 2 | Moderate | Rekey Substation N and E, then all; key log | Manager of Engineering and Protection | 2026-10-31 |
| E-ISAC step outdated; DOE-417 cyber criteria missing | Att. 1 Sec. 4.2; DOE-417 | Moderate | P08 matrix and DCC checklist; agree filing with the BA | Manager of System Operations | 2026-10-15 |
| Removable media scanning informal | Att. 1 Sec. 5.3 | Moderate | Scanning kiosks and procedure | SCADA/OT Administrator | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01: R-001, R-003, R-004, R-005, R-013, R-022, R-031) and the POA&M (P07).

## 5. Pending regulatory changes
These versions are approved but **not yet in effect**. None is treated as a current obligation. Dates are from the NERC CIP standards page.
- **CIP-002-8 and CIP-003-10, 2028-07-01.** Part of the virtualization revisions to CIP-002 through CIP-013. They add terms such as Shared Cyber Infrastructure. The company runs no virtualized systems at its BES substations, so little change is expected.
- **CIP-003-11, 2029-07-01.** It rewrites the low impact electronic access controls (Attachment 1 Section 3.1). For all routable access, not only vendor access, the company will have to:
  - detect known or suspected malicious communications
  - authenticate each user before allowing network access
  - protect authentication data in transit
  - keep methods to determine and disable vendor access (moved from Section 6)

  The monitoring and MFA work planned for 2026-2027 is designed to meet this early.
- **CIP-015-1 (2028-10-01) and CIP-015-2 (2029-10-01),** internal network security monitoring: aimed at high and medium impact systems. Recheck applicability when effective.
- **EOP-004-5, 2027-10-01:** update the event reporting Operating Plan.
- **DOE-417:** the current OMB approval expires 2027-05-31. Check for a revised form.
- **Watch item:** DOE issued a request for information (FR Doc. 2026-18370, 2026-09-09) under an executive order on bulk-power system security. It is not a requirement today.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
