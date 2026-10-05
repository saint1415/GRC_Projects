# Regulatory Gap Analysis: Cris Santos Company | Utilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility, NERC-registered Distribution Provider, with a Utility Services line for 4 client utilities) |
| Tier / Vertical | Mid-Market / Utilities |
| Primary regulation | NERC CIP Reliability Standards under Federal Power Act section 215 (16 U.S.C. 824o): **CIP-002-5.1a** and **CIP-003-9** (low impact), with the CIP-004 to CIP-014 applicability decisions recorded |
| Also analyzed (all rules for the primary business line) | NERC **EOP-004-4** and Form **DOE-417** (event and incident reporting); FTC **Identity Theft Red Flags Rule** (16 CFR 681.1) and **Disposal Rule** (16 CFR Part 682); **Fla. Stat. 501.171** (data security, breach notice, disposal) |
| Versions checked | NERC CIP standards page (nerc.com), retrieved 2026-09-26: CIP-002-5.1a in effect since 2016-12-27; CIP-003-9 in effect since 2026-04-01. EOP-004-4 text from nerc.com. 16 CFR 681 and 682 from eCFR (2026-09-23 version). Fla. Stat. 501.171 (2026) from the Florida Legislature site |
| Assessment dates | 2026-07-06 to 2026-07-31 (substation walkthroughs 2026-07-21 to 2026-07-23); Sections 3.1 and 6 rows updated after P07 testing (2026-08-19 and 2026-08-20) |
| Assessor | NERC Compliance Manager and the GRC analyst, with the Information Security Manager and the vCISO; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer (CIP Senior Manager), 2026-09-17 |

## 1. Applicability
**Primary business line:** delivery of electricity over the company's distribution system to about 265,000 retail customers in Florida, with billing and customer service. Utility Services (contract services for 4 client utilities) uses the same CIS, AMI, and contact center, so its customer data duties are analyzed here too; its SOC 2 readiness is in P09.

### 1.1 NERC CIP applies, at low impact only, with one pending scope change
1. **Who must comply.** Section 215 of the Federal Power Act gives FERC jurisdiction over "all users, owners and operators of the bulk-power system" and requires them to comply with approved reliability standards (16 U.S.C. 824o(b)(1)). NERC enforces through the Regional Entities; for Florida that is SERC.
2. **Registration.** The company is on the NERC Compliance Registry as a Distribution Provider. It meets criteria III.a.1 (more than 75 MW of peak Load directly connected to the BES; 2025 peak 1,480 MW) and III.a.2 (owns Facilities that are part of a required transmission Protection System) of the NERC Statement of Compliance Registry Criteria (Rules of Procedure Appendix 5B).
3. **Which DPs the CIP standards reach.** CIP-002-5.1a and CIP-003-9 apply to a DP only if it owns one of four things (Applicability 4.1.2 and 4.2.1). The company's result for each:

| Applicability item | Company fact | In scope? |
|---|---|---|
| 4.2.1.1 UFLS or UVLS system that is part of a required program **and** sheds 300 MW or more automatically under a common control system the entity owns | Feeder UFLS relays at 41 substations shed about 440 MW in stages, but each relay acts on its own; there is no common control system | No (today) |
| 4.2.1.2 Remedial Action Scheme subject to a standard | None | No |
| 4.2.1.3 Protection System (not UFLS or UVLS) that applies to Transmission and is subject to a standard | 26 relays protecting the 230 kV and 115 kV BES line terminals at Substations N, E, L, and H, maintained under PRC-005 | **Yes** |
| 4.2.1.4 Cranking Path or initial switching elements from a Blackstart Resource | None | No |

4. **Everything else is exempt today.** For DPs, systems and equipment not listed in 4.2.1 are exempt (section 4.2.3.4). That covers the distribution SCADA, OMS, AMI, ADMS FLISR pilot, and feeder devices. The DCC is not a "Control Center" in the NERC Glossary, which lists only Reliability Coordinator, Balancing Authority, Transmission Operator, and Generator Operator functions.
5. **Impact rating.** No asset meets a high (Attachment 1 Section 1) or medium (Section 2) criterion. The relays are **low impact** under criterion 3.6, so the 4 substations are listed as assets containing low impact BES Cyber Systems (R1 Part 1.3).
6. **The pending scope change (G-007).** The ADMS project (go-live planned 2027-06) includes an adaptive load-shedding module that operators arm and that then sheds 300 MW or more automatically under one control system. That would bring the UFLS function under section 4.2.1.1 and make the system **medium impact** under Attachment 1 criterion 2.10. The CIP-002-5.1a Guidelines and Technical Basis state that qualifying systems that require a human operator to arm them, but then trigger automatically, are still treated as not requiring human operator initiation. Compliance with CIP-004 to CIP-011 and CIP-013 would be needed from the day the module is placed in service.
7. **Result.** CIP-002-5.1a applies in full. CIP-003-9 applies through R1 Part 1.2, R2 (Attachment 1), R3, and R4. CIP-004 to CIP-011 and CIP-013 apply only to high or medium impact systems; CIP-012 applies to other functions with Control Centers; CIP-014 applies only to Transmission Owners and Operators. Those 11 rows are kept as Not applicable so the decisions are visible, with a watch note for the ADMS decision.

**What CIP does not cover.** The low impact scope is 26 relays at 4 substations. Most of the company's operational cyber risk sits in the distribution SCADA, OMS, field network, and AMI, which CIP does not reach. Those systems are held to NIST CSF 2.0 with SP 800-82 Rev. 3 as a voluntary benchmark in the SSP (P02) and the control assessment (P07).

### 1.2 Other rules for the primary business line
| Regulation | Applies? | Basis |
|---|---|---|
| NERC EOP-004-4 | **Yes** | The Distribution Provider is a listed responsible entity (Applicability 4.1.7). DP event types: damage or destruction of its Facility from actual or suspected intentional human action; physical threats or suspicious devices or activity at its Facility; uncontrolled loss of firm load of 200 MW or more for 15 minutes or more resulting from a BES Emergency |
| Form DOE-417 | **Yes** | Mandatory under section 13(b) of the Federal Energy Administration Act of 1974 (15 U.S.C. 772(b)). Electric utilities give their Balancing Authority the information it needs and file themselves where the BA will not. Criteria read from the OMB-approved instructions (OMB 1901-0288, expires 2027-05-31) |
| FTC Identity Theft Red Flags Rule, 16 CFR 681.1 | **Yes** | The rule applies to creditors under FTC jurisdiction (681.1(a)). The company is a "creditor" under 15 U.S.C. 1681m(e)(4) because it regularly obtains consumer reports in connection with credit transactions (deferred payment for electric service). 681.1(b)(3)(i) names a "utility account" as an example of a covered account. The rule has no size exemption; the Program must be "appropriate to the size and complexity" of the company (681.1(d)(1)) |
| FTC Disposal Rule, 16 CFR Part 682 | **Yes** | Applies to any person under FTC jurisdiction that possesses consumer information for a business purpose (682.2(b)); the company keeps consumer report data for deposit decisions |
| Fla. Stat. 501.171 | **Yes** | The company is a "covered entity" (a corporation that maintains personal information) for its own customers, and a "third-party agent" (501.171(1)(h)) for the 4 client utilities, which are covered entities or governmental entities for the notice duties. Personal information held includes SSNs, driver license numbers, and bank account numbers. About 6% of residential accounts have out-of-state addresses, so notice follows the law of each state where affected individuals reside, with Florida as the worked example |

**Considered and not applicable:** TSA Security Directive Pipeline-2021-02G (N22-R02; no pipelines), NRC 10 CFR 73.54 (N22-R03; no reactors), SDWA section 1433 (N22-R04; no water system), SEC cybersecurity disclosure rules (privately held), CIRCIA (final rule not published; proposed only), and 16 CFR 681.2 (the company is not a card issuer). PCI DSS is a contractual obligation through the payment processor; card data never enters company systems, so it is noted and not assessed.

## 2. Method
1. **Requirements.** NERC rows follow each standard's own structure (requirement, part, Attachment 1 section), with summaries in this repository's own words; the `requirement_type` column records the Violation Risk Factor. FTC rows follow the CFR paragraph structure (16 CFR 681.1(c) to (f); 682.3(a)). Florida rows follow the statute's subsections. Text was read from the primary sources listed above.
2. **Crosswalk.** Each applicable row maps to CSF 2.0 and SP 800-53 Rev. 5. **This is an author mapping.** NIST has not published an official mapping for NERC CIP, EOP-004, DOE-417, the FTC rules, or Fla. Stat. 501.171.
3. **Evidence.** Interviews with the CIP Senior Manager, the Director of Engineering and Protection, the Director of System Operations, the OT Engineering Manager, the Vice President of Customer Operations, the Credit and Collections Manager, and the Director of Utility Services; document review (CIP-002 records, policy and plan versions, delegations, the EOP-004 Operating Plan, the Identity Theft Prevention Program, client contracts); configuration exports (gateways, jump hosts, CIS roles); and walkthroughs of all 4 BES substations (2026-07-21 to 2026-07-23) and all 5 operations sites.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were drawn at random from system-generated populations, with sizes from the co-sourced internal audit firm's attribute sampling table:
   - jump host vendor sessions: 25 of 412 (2026-04-01 to 2026-07-31);
   - relay test connections by contractor laptops: all 10 in 2026 (4 at N and E, 6 at L and H);
   - CIP awareness completion: full population (828 of 850 staff);
   - move-in identity verification: 25 of about 24,000 (2026-06);
   - portal account takeover case files: all 14 from 2025;
   - EOP-004 event reports: all 2 in the last 12 months;
   - client contracts: all 4; Red Flags service provider contracts: all 3;
   - paper disposal: inspection of all 5 sites.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Regulation | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| CIP-002-5.1a (R1, R2, and the ADMS criterion 2.10 row) | 6 | 1 | 0 | 0 | 7 |
| CIP-003-9 (R1 to R4, Attachment 1) | 21 | 8 | 0 | 2 | 31 |
| CIP-004 to CIP-014 (11 standards) | 0 | 0 | 0 | 11 | 11 |
| **NERC CIP subtotal** | **27** | **9** | **0** | **13** | **49** |
| EOP-004-4 | 2 | 0 | 0 | 0 | 2 |
| DOE-417 | 1 | 1 | 0 | 0 | 2 |
| FTC Red Flags Rule (16 CFR 681) | 2 | 6 | 3 | 1 | 12 |
| FTC Disposal Rule (16 CFR 682) | 0 | 1 | 0 | 0 | 1 |
| Fla. Stat. 501.171 | 1 | 5 | 0 | 0 | 6 |
| **Total** | **33** | **22** | **3** | **14** | **72** |

**Gap risk ratings (25 rows Partially met or Not met):** 9 High, 13 Moderate, 3 Low.

**Reading the results.** The CIP low impact program is mature for a Distribution Provider: the policy, awareness, incident response plan, removable media, and the new CIP-003-9 vendor remote access controls were all in place on time. The CIP gaps come from two events, not from a missing program: the transfer of Substations L and H in 2025, which was not run through an asset onboarding checklist, and a contractor's cellular modem at Substation H. The weakest area is the Identity Theft Prevention Program, which has not kept up with the portal, IVR, and Utility Services; all 3 Not met rows are there.

### Potential noncompliance to self-report
Seven CIP-003-9 rows (three issues) describe potential violations of an enforceable standard, not only weaknesses:
- **Substation H modem** (Attachment 1 Section 3.1 and Sections 6.1 to 6.3, G-021 and G-034 to G-036): routable access outside the gateway from 2025-10-14, and an undetected vendor remote access path from 2026-04-01, both until 2026-08-20.
- **Contractor laptops at L and H** (Sections 5.2.1 and 5.2.2, G-030 and G-031): no review before connection since 2025-06-01.
- **Keys at L and H** (Section 2, G-019): 2 unaccounted keys since 2025-06-01.

The CIP Senior Manager decided on 2026-09-17 to **self-report** them to SERC by 2026-09-30, with mitigation plans. A "Self-Report" is the Compliance Monitoring and Enforcement Program term (NERC Rules of Procedure Appendix 4C) for a registered entity reporting that it has, or may have, violated a standard. The NERC Compliance Manager, who reports to the General Counsel, owns the filing.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| ADMS load-shedding module would be medium impact with no program | CIP-002-5.1a Att. 1 criterion 2.10 (G-007) | High | Board decision: redesign or funded medium impact program before go-live; CIP-002 check at every OT gate | Chief Operating Officer | 2026-12-10 |
| Substation H modem bypassed gateway and vendor access controls | CIP-003-9 Att. 1 Sec. 3.1, 6.1-6.3 (G-021, G-034 to G-036) | High | Survey 74 substations; contract ban; sensors at the 4 BES substations; self-report | Director of Engineering and Protection; Information Security Manager | 2026-11-30 (survey); 2027-03-31 (sensors) |
| Contractor laptops not reviewed at L and H | Att. 1 Sec. 5.2.1-5.2.2 (G-030, G-031) | High | Pre-connection checklist and contract clause | Director of Engineering and Protection | 2026-10-31 |
| Low impact plan implementation for newly acquired assets | CIP-003-9 R2 (G-017) | High | Asset onboarding checklist for any new low impact asset | CIP Senior Manager | 2026-12-31 |
| Customer identity data concentration and broad access | Fla. Stat. 501.171(2) (G-067) | High | Minimize and expire the CIS export; cut bulk export rights | Vice President of Customer Operations | 2027-03-31 |
| Identity Theft Prevention Program stale (update, training, service providers) | 16 CFR 681.1(c), (d), (e)(3)-(4) (G-054 to G-059, G-062, G-063) | Moderate | Rewrite with counsel; board committee approval 2026-12-10; training; vendor clauses | Vice President of Customer Operations | 2026-12-10 to 2027-03-31 |
| Unaccounted keys at L and H | Att. 1 Sec. 2 (G-019) | Moderate | Rekey and reconcile | Director of Engineering and Protection | 2026-10-31 |
| DOE-417 filing not agreed with the BA | DOE-417 (G-052) | Moderate | Written agreement; drill | Director of System Operations | 2026-11-30 |
| Third-party agent notice to clients untested; multi-state notice | 501.171(4), (6) (G-069, G-071) | Moderate | Client drill; state playbook | Director of Utility Services; General Counsel | 2026-11-30 to 2027-03-31 |
| Disposal of consumer and customer records | 16 CFR 682.3(a); 501.171(8) (G-066, G-072) | Moderate | Locked bins at all sites; retention and purge jobs | Vice President of Customer Operations | 2027-03-31 |

High and Moderate gaps are carried into the risk register (P01: R-003, R-005, R-006, R-008, R-009, R-010, R-019, R-020, R-023, R-024, R-025, R-042, R-043) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Rows closed (examples) |
|---|---|---|---|
| **1. Self-report and contain** | 2026 Q3-Q4 | SERC self-report filed (2026-09-30); modem removed (done); rekey L and H; contractor laptop checklist; substation survey; DOE-417 agreement with the BA; multi-state notice playbook | G-019, G-021, G-030, G-031, G-034, G-035, G-052, G-069 |
| **2. Decide and rewrite** | 2026 Q4 | Board decision on the ADMS design (2026-12-10); rewritten Identity Theft Prevention Program approved by the board committee; covered-account assessment; asset onboarding checklist | G-007, G-017, G-054 to G-056, G-059, G-061, G-064 |
| **3. Build** | 2027 Q1 | OT sensors at the 4 BES substations; Red Flags training and service provider clauses; CIS export minimized; portal alerts; client notification drill | G-036, G-057, G-062, G-063, G-067, G-071 |
| **4. Sustain and prepare** | 2027 Q2-Q4 | Retention and purge jobs live; CIP-003 tabletop combined with a storm (2027-02, ahead of the 2027-10-08 deadline); next CIP-002 review by 2027-03-09; if the ADMS goes ahead as designed, the medium impact program runs before go-live | G-066, G-072, and the watch items below |

Progress is reported each quarter to the audit committee as the count of rows moving from Partially met or Not met to Met, plus the status of each SERC mitigation milestone.

## 6. Pending regulatory changes
These versions are approved but **not yet in effect**, or are only proposed. None is treated as a current obligation. NERC dates are from the NERC CIP standards page.
- **CIP-002-8, CIP-003-10, and the other virtualization revisions, 2028-07-01.** They add terms such as Shared Cyber Infrastructure. The company runs no virtualized systems at its BES substations; the ADMS design should be checked against them if it goes ahead.
- **CIP-003-11, 2029-07-01.** It rewrites the low impact electronic access controls (Attachment 1 Section 3.1). For all routable access, not only vendor access, the company will have to detect known or suspected malicious communications, authenticate each user before allowing access, protect authentication data in transit, and keep methods to determine and disable vendor access (moved from Section 6). The substation sensors and the PAM extension planned for 2026-2027 are designed to meet this early.
- **CIP-015-1 (2028-10-01) and CIP-015-2 (2029-10-01),** internal network security monitoring for high and medium impact systems: relevant only if the ADMS module becomes medium impact.
- **CIP-013-3 (2028-07-01) and further FERC-directed supply chain revisions:** recheck whether any low impact obligations are added.
- **EOP-004-5, 2027-10-01:** update the event reporting Operating Plan.
- **DOE-417:** the current OMB approval expires 2027-05-31. Check for a revised form.
- **CIRCIA (6 U.S.C. 681b):** the final rule has not been published; the proposed 72-hour and 24-hour reporting would not apply until a final rule takes effect.
- **Watch item:** DOE issued a request for information (FR Doc. 2026-18370, 2026-09-09) under an executive order on bulk-power system security. It is not a requirement today.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
