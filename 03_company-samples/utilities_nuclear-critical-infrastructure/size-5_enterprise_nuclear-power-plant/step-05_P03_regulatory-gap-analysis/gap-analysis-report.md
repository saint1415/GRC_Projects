# Regulatory Gap Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded nuclear generation company; four stations, seven units; FL, GA, SC, AL) |
| Tier / Vertical | Enterprise / Nuclear Reactors, Materials, and Waste |
| Primary regulation | **10 CFR 73.54**, with the controls of the NRC-approved cyber security plans (NEI 08-09 template; RG 5.71 Rev. 1 is the NRC's guidance). Text checked on eCFR (version date 2026-09-23) |
| Also analyzed | 10 CFR 73.77 (cyber security event notifications); 10 CFR 73.21-73.22 (Safeguards Information); 10 CFR 73.56(m) and 26.37 (personal information); 10 CFR 73.55(m) and 73.1200; 10 CFR 50.72 and 50.73; NERC CIP (Generation Dispatch Center and low impact station assets); SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example); 10 CFR 20.1501(d) and 20.2106 (dosimetry); 10 CFR Part 810; applicability checks for 73.110, CIRCIA, and HIPAA |
| Assessment dates | 2026-06-01 to 2026-07-31 (station walkthroughs 2026-06-15 to 2026-06-26; evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer, the Director, Nuclear Cyber Security, and the Director, NERC Compliance; Nuclear Oversight reperformed 8 sampled rows |
| Approved | Chief Compliance Officer, Chief Nuclear Officer, and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |
| Workbook | `gap-analysis.csv` (114 rows: G-001 to G-027 73.54 paragraphs, G-028 to G-044 CSP control areas, G-045 to G-053 73.77, G-054 to G-064 SGI, G-065 to G-069 personal information, G-070 to G-073 73.55(m) and 73.1200, G-074 to G-076 event reporting, G-077 to G-096 NERC CIP, G-097 to G-104 SEC, G-105 to G-108 state law, G-109 to G-110 dosimetry, G-111 Part 810, G-112 to G-114 applicability checks) |

## 1. Applicability
The vertical's primary regulation applies in full at this size: the company is a power reactor licensee. Each other rule was checked against its own applicability text.

| Regulation | Applies? | Basis |
|---|---|---|
| 10 CFR 73.54 (C-NUCLEAR-R01) | **Yes** | Applies to licensees "licensed to operate a nuclear power plant under part 50"; all seven units hold Part 50 operating licenses. No size threshold |
| 10 CFR 73.77 (C-NUCLEAR-R03) | **Yes** | Applies to "each licensee subject to the provisions of § 73.54 or § 73.110" |
| 10 CFR 73.110 (C-NUCLEAR-R02) | **No** | Applies to Part 53 licensees that elect it; the company holds Part 50 licenses and has not elected it |
| 10 CFR 73.21-73.22 (C-NUCLEAR-S01) | **Yes** | Power reactor licensees must protect SGI under 73.22 (73.21(a)(1)(i)) |
| 10 CFR 73.56(m); 26.37 (C-NUCLEAR-S02) | **Yes** | Access authorization and fitness-for-duty programs for power reactors |
| 10 CFR 73.55(m); 73.1200 (C-NUCLEAR-S03) | **Yes** | Physical protection program reviews include the cyber security program (73.55(m)(2)); 73.1200 applies to licensees subject to 73.55 |
| 10 CFR 50.72; 50.73 (C-NUCLEAR-S04) | **Yes** | Operating power reactor licensees. 73.77(c)(7) avoids duplicate reports but requires the 73.77 criteria to be indicated |
| NERC CIP (C-NUCLEAR-R04) | **Yes, in part** | Registered Generator Owner and Generator Operator. The Generation Dispatch Center is high impact (CIP-002-5.1a criterion 1.4, because Stations 1 to 3 each exceed 1,500 MW under criterion 2.1). Systems regulated by the NRC under a 73.54 plan are exempt (section 4.2.3.3). Station switchyard interface devices outside 73.54 are low impact (criterion 3.3). CIP-014 does not apply (no qualifying transmission stations) |
| SEC Item 1.05 and Item 106 (C-NUCLEAR-S06) | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| State breach and data security laws (C-NUCLEAR-S07) | **Yes** | Employees and contractors in four states, and SL-2 client workers nationwide; Florida (Fla. Stat. 501.171) is the worked example |
| 10 CFR 20.1501(d); 20.2106 (C-NUCLEAR-S08) | **Yes** | The dosimetry laboratory processes dosimeters as an NVLAP-accredited processor; the fleet keeps dose records |
| 10 CFR Part 810 (C-NUCLEAR-S09) | **Yes** | 810.2(a)(2) covers transfers of reactor technology in the United States or abroad, including access by foreign persons |
| CIRCIA (C-NUCLEAR-R05) | **Not in force** | Final rule not published as of 2026-09-25. As proposed, the company would be covered: it exceeds the SBA size standard for NAICS 221113 (1,150 employees) and owns commercial nuclear power reactors |
| HIPAA | **No** | The dosimetry laboratory processes occupational dose records that client employers keep as employment records; PHI excludes employment records held by a covered entity in its role as employer (45 CFR 160.103), and the lab performs no covered function |
| SOX Section 404 | Separate program | ERP IT general controls are tested by the SOX program and not repeated here |

**The boundary between 73.54 and NERC CIP.** For each station, the categorization record lists which digital assets are CDAs under the CSP (and therefore exempt from CIP) and which BES Cyber Systems are outside that scope. The only station assets outside the 73.54 scope are company-owned switchyard interface devices, rated low impact. The Generation Dispatch Center is not at a station and is fully under CIP.

## 2. Method
1. **Decompose.** The 73.54 rows follow the regulation's own structure: each paragraph that imposes a duty, at the most granular citation that can be verified separately. Brief quotes come from the public-domain eCFR text. The same approach was used for 73.77, 73.21-73.22, 73.55(m), 73.56(m), 26.37, 50.72, 50.73, 20.1501(d), 20.2106, 810.2, and 17 CFR 229.106 (all eCFR, version date 2026-09-23).
2. **CSP control areas.** 73.54(c)(1) requires security controls but does not list them. The controls are commitments in each station's NRC-approved plan, which follows the NEI 08-09 template; RG 5.71 Rev. 1 is the NRC's guidance. Rows G-028 to G-044 assess the plan's control areas by topic. They are named in plain words and do not cite RG 5.71 section numbers, because the guide could not be retrieved from NRC ADAMS during this analysis. The plans themselves are controlled documents and are not reproduced.
3. **NERC CIP.** NERC standards are copyrighted, so rows list the standard and requirement numbers with short topic labels in the assessors' own words. Current enforceable versions were taken from the vertical's requirements file.
4. **Crosswalk.** Every row maps to CSF 2.0 and SP 800-53 Rev. 5. No official NIST mapping exists for these rules, so all mappings are the author's and are labeled that way.
5. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Large populations of key controls used 40 to 60 items chosen at random (stratified by station where stations run different processes); smaller or lower-risk populations used 25; data sweeps covered full populations. **24 rows were tested by sampling or full-population analytics; 12 found exceptions.**
6. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. All High gaps are in the P01 register and the P07 POA&M; Moderate and Low gaps not in the POA&M are tracked in the station corrective action programs or the GRC platform with owners and dates.

**Mandatory is mandatory.** Unlike rules with addressable specifications, every duty in 73.54 and the CSP is a commitment. A Partially met row means the requirement is implemented with a gap at one station or in one process, not that the company chose an alternative. Gaps in the cyber security program are also entered in the station corrective action programs within 24 hours (73.77(b)(1)); this analysis found that step late in 2 sampled cases (G-050).

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| 10 CFR 73.54 paragraphs (G-001 to G-027) | 17 | 10 | 0 | 0 | 27 |
| 10 CFR 73.54(c)(1) CSP control areas (G-028 to G-044) | 12 | 5 | 0 | 0 | 17 |
| 10 CFR 73.77 | 6 | 3 | 0 | 0 | 9 |
| 10 CFR 73.21-73.22 (SGI) | 8 | 3 | 0 | 0 | 11 |
| 10 CFR 73.56(m) and 26.37 | 3 | 2 | 0 | 0 | 5 |
| 10 CFR 73.55(m) and 73.1200 | 4 | 0 | 0 | 0 | 4 |
| 10 CFR 50.72 and 50.73 | 3 | 0 | 0 | 0 | 3 |
| NERC CIP | 16 | 3 | 0 | 1 | 20 |
| SEC Form 8-K Item 1.05 | 2 | 1 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 2 | 2 | 0 | 0 | 4 |
| 10 CFR Part 20 (dosimetry) | 1 | 1 | 0 | 0 | 2 |
| 10 CFR Part 810 | 1 | 0 | 0 | 0 | 1 |
| Applicability checks (73.110, CIRCIA, HIPAA) | 0 | 0 | 0 | 3 | 3 |
| **Total** | **80** | **30** | **0** | **4** | **114** |

**Gap risk levels across all regulations:** High 7, Moderate 18, Low 5.

**Pattern.** The station programs are mature: NRC inspections since 2022 found no issues above very low safety significance, and the CSP control areas at Stations 1 to 3 are met. **Of the 30 Partially met rows, 15 trace to Station 4**, which still runs the prior owner's procedures, forms, and business systems 15 months after the acquisition. The rest are coordination gaps between the corporate SOC and the stations (73.77(a)(2)(iii), (a)(3), (b)(1)), information handling outside approved systems (73.56(m)(4)), and the untested materiality process.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-006 | 73.54(a)(1)(iv) | Wireless sensor gateways with cellular links installed on non-safety equipment at Station 4 without analysis | Disconnect; analyze; CAP entry (POAM-018) | Director, Nuclear Cyber Security | 2026-12-31 |
| G-008 | 73.54(b)(1) | New digital devices at Station 4 not analyzed (2 of 40 sampled design changes) | Same; fleet design change procedure at Station 4 (POAM-018) | Director, Nuclear Cyber Security | 2026-12-31 |
| G-012 | 73.54(c)(2) | Outer defensive level weak at Station 4 (flat network; vendor VPN; cellular gateways) | Segment and retire the VPN (POAM-009); remove gateways (POAM-018) | Vice President, Integration Management | 2027-03-31 |
| G-021 | 73.54(e)(2)(i) | No SIEM or network detection on the Station 4 business network | SIEM, EDR, network detection (POAM-004) | Director, Security Operations | 2026-12-31 |
| G-034 | 73.54(c)(1), wireless | Same as G-006 | POAM-018 | Director, Nuclear Cyber Security | 2026-12-31 |
| G-048 | 73.77(a)(2)(iii) | SOC reports to the FBI or CISA can start the station's 4-hour NRC clock without the station knowing | Station notification step in the SOC procedure (POAM-013) | Director, Security Operations | 2026-10-31 |
| G-098 | Form 8-K Item 1.05 (materiality determination) | Materiality process never exercised on a plant scenario with NRC notifications | Disclosure committee tabletop 2026-11-19 (POAM-013) | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | SOC-to-station notification step and CAP screening (POAM-013); disclosure committee tabletop on 2026-11-19; sensor gateways disconnected and analyzed (POAM-018); SGI copier and sanitization (POAM-023); access authorization exports removed and vendor contract amended (POAM-024); Station 4 SIEM and EDR (POAM-004); CIP-003-9 Section 6 at Station 4 (POAM-025); kiosk at Station 3 receiving (POAM-015); dose record restore test (POAM-019); badging hard stop for training | 73.54(a)(1)(iv), (b)(1), (d)(1), (e)(2)(i); 73.77(a)(2)(iii), (a)(3), (b)(1); 73.22(e), (g)(4); 73.56(m)(3)-(4); CIP-003-9; Item 1.05; 20.2106 | Procedure revisions; tabletop report; CAP entries; analysis records; contract amendment; restore test report |
| 2027 Q1 | Station 4 network segmentation and VPN retirement (POAM-009); Station 4 implementing procedures revised (G-020); restore media verification at Station 3 (G-024); CIP-013 contract amendments (POAM-017); Internal Audit test of Item 106 statements | 73.54(c)(2), (e)(1), (e)(2)(iv); CIP-013-2; Item 106 | Firewall rules; procedure revisions; verification records |
| 2027 Q2 | Station 4 WMS migration (POAM-022); transition services agreement exit | 73.54(c)(2); 50.36(c)(3) context | Migration records |
| 2027 Q3 | Annual gap reassessment; review the status of the NRC proposed rule and RG 5.71 update | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **NRC "Modernizing Security Requirements" proposed rule** (91 FR 38928, 2026-06-26; RIN 3150-AL53; Docket NRC-2025-1303; comments closed 2026-07-27) is **still proposed**. For this analysis, the verified proposals that matter are:
  - replace "high assurance" with "reasonable assurance" in 73.54(a) and related sections;
  - remove the 73.54 introductory paragraph and make the 73.54(g) cyber program review independent of the physical security program review;
  - simplify 73.77 so that a cyberattack that adversely impacted a safety or security function is reported through the 50.72 (or 53.1630) or 73.1200 processes, depending on the function, instead of the separate 1, 4, and 8-hour criteria, with withdrawal of RG 5.83;
  - let new Part 50 and 52 applicants choose 73.110;
  - allow encrypted commercial voice communications for SGI under FIPS 140, and an option to view SGI on networked systems through virtual desktop or thin client designs (73.22(f)(3), (g)(2));
  - update RG 5.71 to cut about 19% of controls and give credit for practices already in use.

  `pending_rule_change` flags each affected row. **None of these proposals is treated as a current change.** Until a final rule takes effect, the current 73.77 clocks, the stand-alone SGI computer rule, and every CSP commitment apply as written (R-064).
- **Other NRC proposals under Executive Order 14300** ("Modernizing Reactor Licensing, Safety Oversight, and Siting Practices," 91 FR 44560; "Regulatory Enhancements for Reactor Licensing, Decommissioning, and Operational Oversight," 91 FR 60702; "Reforming and Modernizing the NRC's Radiation Protection Framework," 91 FR 43456) were noted. Their effect on 50.72, 50.73, or the Part 20 rows was not analyzed.
- **NERC CIP:** future versions take effect in the United States on 2028-07-01 (virtualization revisions, including CIP-003-10), 2028-10-01 (CIP-015-1 internal network security monitoring), and 2029-07-01 (CIP-003-11), per the vertical's requirements file. The GDC plan includes CIP-015-1 preparation (P01 R-016).
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team and the Director, Nuclear Cyber Security keep an evidence index by `req_id`, so the company can respond quickly to an NRC cyber security inspection (IP 71130.10), a NERC Regional Entity audit, or an SEC comment letter. Controlled and SGI material stays in the station programs and is referenced, not copied:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- CAP entries for every cyber program gap in this report (73.77(b)(1));
- Nuclear Oversight 73.55(m) reports and NRC inspection reports;
- the CIP-002 categorization record and NRC-NERC boundary documentation;
- retention: CSP records until license termination and superseded portions for 3 years (73.54(h)); other security documentation at least 6 years (POL-01 4.11).

## 8. Approval
Approved by the Chief Compliance Officer, the Chief Nuclear Officer, and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or within 90 days of any final NRC rule that changes 73.54, 73.77, or 73.22.
