# Regulatory Gap Analysis: Cris Santos Company Holdings | Nuclear Reactors, Materials, and Waste | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Nuclear Reactors, Materials, and Waste (focus division: Nuclear Generation) |
| Primary regulation | 10 CFR 73.54, protection of digital computer and communication systems and networks, with RG 5.71 Rev. 1 (February 2023) as the control benchmark. Text checked on the eCFR (version date 2026-09-23) |
| Division regulations | Engineering and Radiation Services: Safeguards Information (73.21-73.22), 73.56 contractor/vendor program duties, dosimetry rules (20.1501(d), 20.2106), FAR 52.204-21, Part 810. Radioactive Waste Management: 10 CFR Part 37 through the Florida license condition, DOT security plans, RCRA records, and a voluntary CSF 2.0 OT benchmark |
| Gap tables | `gap-analysis.csv` (Nuclear Generation and group-wide rows, G-001 to G-078); `gap-analysis-engineering-radiation-services.csv` (ER-G01 to ER-G41); `gap-analysis-waste-management.csv` (WM-G01 to WM-G43) |
| Assessment dates | 2026-05-04 to 2026-07-31 (Station A walkthrough 2026-06-16), with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the fleet cyber security program manager, the fleet security director, the SGI program manager, and the Florida facility Radiation Safety Officer; coordinated by the Group Chief Risk Officer and reviewed by group internal audit |

## 1. Applicability
### 1.1 Nuclear Generation: the power reactor rules apply in full
**10 CFR 73.54 applies** to "each licensee currently licensed to operate a nuclear power plant under part 50." All 5 units hold Part 50 operating licenses, so each station has an NRC-approved cyber security plan (CSP), approved by license amendment and fully implemented in 2017. There is no size threshold or exemption. Related rules that apply for the same reason:
- **10 CFR 73.77** (cyber security event notifications) applies to "each licensee subject to the provisions of § 73.54 or § 73.110."
- **10 CFR 73.21-73.22** (Safeguards Information): power reactor licensees must keep an information protection system with the 73.22 measures (73.21(a)(1)(i)).
- **10 CFR 73.56** (access authorization), including people whose duties let them act by electronic means against safety, security, or emergency preparedness (73.56(b)(1)(ii)).
- **10 CFR 73.58** (safety/security interface) and **73.55(m)** (security program reviews, which must include an audit of the cyber security program).
- **10 CFR 50.65** (Maintenance Rule) and **50.72** (immediate notifications) are not cyber rules, but the predictive maintenance pilot (P10) and the incident runbook (P08) depend on them.
- **10 CFR 73.110** does not apply: no unit is licensed under Part 53 (G-077).

**What this analysis does and does not test.** The CSPs are inspected by the NRC and reviewed every 24 months by Nuclear Oversight. This group analysis does not re-perform those reviews. It checks each 73.54 paragraph at program level against inspection and review evidence, and it looks closely at the places where the **business side of the group touches the CSP**: the kiosk update path, CDA information in the work management system, cross-division staff, and notification triggers that start in the group SOC. That is where the gaps are.

**The NRC-NERC boundary.** CIP-002-5.1a section 4.2.3.3 exempts "systems, structures, and components that are regulated by the Nuclear Regulatory Commission under a cyber security plan pursuant to 10 C.F.R. Section 73.54." Since the Commission's 2010 balance-of-plant decision (cited in RG 5.71 Rev. 1), balance-of-plant digital assets with a nexus to radiological health and safety are in the CSPs. The division's NERC CIP scope is therefore limited to the fleet operations center (medium impact under criterion 2.11, a Generator Operator control center for more than 1,500 MW in one Interconnection) and low impact BES Cyber Systems at each station's generator interconnection that the boundary analysis left outside the CSPs. The current enforceable versions used here are CIP-002-5.1a, CIP-003-9 (effective 2026-04-01), CIP-004-7, CIP-005-7, CIP-007-6, CIP-008-6, CIP-009-6, CIP-010-4, CIP-011-3, and CIP-013-2.

**DOE-417 does not apply.** The DOE-417 instructions exclude commercial power reactors regulated by the NRC and subject to the Part 73 event notification rules from "Generating Entities," and no division is a Balancing Authority, Reliability Coordinator, or electric utility (G-078).

### 1.2 Engineering and Radiation Services: reactor rules reach it as an SGI holder and a contractor/vendor
The division is not a licensee under Part 50, but three power reactor rules reach it directly:
- **SGI.** 73.21(a)(1) applies to "each licensee, certificate holder, applicant, or other person who produces, receives, or acquires Safeguards Information." The division receives power reactor SGI from the group's stations and 14 external utilities, so it must keep an information protection system with the 73.22 measures (73.21(a)(1)(i)).
- **Access authorization.** Licensees may accept a contractor/vendor program "in part or whole" (73.56(a)(4)), and 73.56(k), (m), and (o) speak directly to "contractors or vendors." The division runs the contractor/vendor program used by about 900 outage workers a year at group stations and by external clients.
- **Dosimetry.** 20.1501(d) requires customer licensees to use an NVLAP-accredited processor. The duty is on the customers, but the division's accreditation is what they rely on, and the division keeps their 20.2106 records.

The division's other obligations come from contracts and its federal work: FAR 52.204-21 in DOE contracts (N54-R04; 15 basic safeguarding requirements, ER-G24 to ER-G38), Part 810 for reactor technology transfers, and client quality assurance requirements flowed down from 10 CFR Part 50, Appendix B. It has **no DoD contracts** (DFARS 252.204-7012 and CMMC do not apply), **no PHI** (not a HIPAA business associate), and is **not a financial institution** (FTC Safeguards Rule does not apply).

### 1.3 Radioactive Waste Management: Part 37 by license condition at one facility
**Neither facility is an NRC licensee.** Both are licensed by Agreement States. The Florida facility holds a Florida Department of Health specific license that applies 10 CFR Part 37 through the standard license condition (Florida's 2023 submission to the NRC, ADAMS ML23178A117), with references to the NRC read as the Florida Department of Health and event reports under 37.57 and 37.81 going to the Bureau of Radiation Control. The facility's sealed source vault holds an aggregated **category 2** quantity, and the waste exemption in 37.11(c) does not apply because the vault holds discrete sources.

**The second facility** (in another southeastern Agreement State) is not authorized for a category 1 or 2 quantity, so Part 37 Subparts B and C do not apply there (WM-G01). Its security network was separated in 2025 as good practice.

**No cyber-specific rule applies to either license.** As in the industry's Small sample, Part 37 is a physical protection rule, but four of its duties are information security duties in practice: protection of the security plan and lists (37.43(d)), protection of background information (37.31), continuous and alternative data transmission for security systems (37.49(c)), and safeguards against tampering with and loss of records (37.101). For the processing OT, management adopted **NIST CSF 2.0 with SP 800-82 Rev. 3** as a voluntary benchmark (C-NUCLEAR-S12; 12 rows).

Other binding rules: the DOT hazmat security plan for category 2 shipments (49 CFR 172.800(b)(15) and 172.802; N56-R09), RCRA operating records for mixed waste through EPA-authorized state programs (40 CFR 264.73-264.74), FCRA and the FTC Disposal Rule for driver background reports (N56-R02, N56-R01), and FAR 52.204-21 on the DOE remediation contract (N56-R07).

### 1.4 Group-wide obligations
- **SEC:** Form 8-K Item 1.05 and Regulation S-K Item 106 (the group is an SEC registrant).
- **State breach notification:** each state where affected individuals reside, with Fla. Stat. 501.171 as the worked example. The dosimetry service holds names, dates of birth, and Social Security numbers for about 310,000 monitored individuals on behalf of its customers, which makes it a **third-party agent** under Florida law (notice to the customer within 10 days).
- **CIRCIA:** not in effect. No final rule was published as of 2026-09-25. As proposed, the group would be covered.
- **OFAC:** sanctions check before any ransom payment.

## 2. Regulation-by-division matrix
| Requirement | Nuclear Generation | Engineering and Radiation Services | Radioactive Waste Management | Group (corporate) |
|---|---|---|---|---|
| C-NUCLEAR-R01 10 CFR 73.54 with RG 5.71 Rev. 1 | **Primary.** All 5 units (Part 50) | Not a licensee. Client CSP rules apply on client sites by contract | Not applicable (no reactor) | Shared services must not become a path to CDAs; SYS-G1 to SYS-G3 do not reach CDAs |
| C-NUCLEAR-R02 10 CFR 73.110 | Not applicable (no Part 53 license) | Not applicable | Not applicable | Not applicable |
| C-NUCLEAR-R03 10 CFR 73.77 | Applies (1, 4, and 8-hour notices; 24-hour CAP records) | Not directly; its staff can trigger a station clock | Not applicable | Group SOC reports to the FBI or CISA can start a 4-hour station clock (73.77(a)(2)(iii)) |
| C-NUCLEAR-R04 NERC CIP | Applies to the fleet operations center (medium) and station low impact assets outside the CSPs | Not applicable | Not applicable | Corporate network sits next to the Electronic Security Perimeter |
| C-NUCLEAR-S01 SGI (73.21-73.22) | Applies (licensee) | **Applies** (receives power reactor SGI) | Not applicable (no SGI received; Part 37 information is protected under 37.43(d)) | SGI never on SYS-G1 to SYS-G3 |
| C-NUCLEAR-S02 Access authorization (73.56) | Applies (licensee program) | **Applies** (contractor/vendor program) | Crews are subject to the station programs when on site | Group identity admins with station DMZ rights evaluated for 73.56(i)(1)(v)(B)(4) |
| C-NUCLEAR-S03 73.58; 73.55(m) | Applies | Not applicable | Not applicable | Not applicable |
| C-NUCLEAR-S04 / S05 50.65; 50.72 | Applies | Not applicable | Not applicable | Not applicable |
| C-NUCLEAR-S06 10 CFR Part 37 | Not applicable (reactor security is under 73.55) | Not applicable | **Applies** at the Florida facility (license condition); not at the second facility | Part 37 events in the group matrix |
| C-NUCLEAR-S07 RCRA records | Not applicable | Not applicable | Applies (mixed waste) | Not applicable |
| C-NUCLEAR-S08 Dosimetry (20.1501(d), 20.2106) | Customer of the dosimetry service | **Applies** (accredited processor; hosts customer records) | Customer of the dosimetry service | Not applicable |
| C-NUCLEAR-S09 Part 810 | Not applicable (no foreign assistance) | Applies | Not applicable | Export control officer |
| N54-R04 / N56-R07 FAR 52.204-21 | Not applicable | Applies (DOE contracts) | Applies (DOE remediation contract) | Group common controls support both |
| N56-R09 DOT security plan | Not applicable (spent fuel shipments not in scope of this analysis) | Not applicable | Applies (category 2 shipments) | Not applicable |
| N56-R01 / N56-R02 FCRA, Disposal Rule | Applies to hiring generally (not analyzed) | Same | Applies (driver background reports) | Group HR |
| C-NUCLEAR-S10 SEC | Via group | Via group | Via group | **Applies** |
| C-NUCLEAR-S11 State breach notification | Applies (employee and contractor data) | Applies, including third-party agent duties for dosimetry customers | Applies | Coordinates |
| C-NUCLEAR-S12 CSF 2.0 OT benchmark | CSP governs CDAs instead | Not applicable | Applies (voluntary) | Not applicable |
| C-NUCLEAR-R05 CIRCIA | Tracked only (proposed) | Tracked only | Tracked only | Tracked only |

## 3. Method
1. **Requirements.** Rows follow each regulation's own structure, at the most granular paragraph that can be verified separately on the eCFR (version date 2026-09-23). Brief quotes come from the public-domain eCFR text. RG 5.71 rows cite the guide's section and appendix numbers (Rev. 1, February 2023) and summarize the control in our own words. NERC CIP rows list requirement numbers with short topic labels in our own words. FAR 52.204-21 rows use the clause's own paragraph numbers.
2. **Requirement type.** "Mandatory (regulation)" or "(CSP license condition)" for NRC rules; "NRC guidance" for RG 5.71, which is an acceptable approach rather than a rule (the licensing basis is each station's approved CSP); "Mandatory (Agreement State license condition)" for Part 37; "Contractual" or "Voluntary benchmark" where that is the source.
3. **Crosswalk.** No official NIST mapping exists for these rules, so every CSF 2.0 and SP 800-53 mapping is an **author mapping**. For the CSF benchmark rows, the SP 800-53 controls come from NIST's CSF 2.0 to SP 800-53 Rev. 5.2.0 reference.
4. **Evidence.** NRC inspection reports, Nuclear Oversight reviews, CSP implementing procedures (read on the CST program network; nothing copied out), CAP records, interviews with the three CSTs, the fleet security director, the SGI program manager, the access authorization program manager, the dosimetry laboratory director, and the Florida Radiation Safety Officer, configuration exports, and P07 test results.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk levels follow the P01 scale.

## 4. Results
### 4.1 Nuclear Generation and group-wide rows (`gap-analysis.csv`)
| Regulation | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| 10 CFR 73.54 (by paragraph) | 15 | 5 | 0 | 0 | 20 |
| RG 5.71 Rev. 1 benchmark (CSP interface) | 5 | 5 | 0 | 0 | 10 |
| 10 CFR 73.77 | 6 | 2 | 1 | 0 | 9 |
| 10 CFR 73.21-73.22 (SGI) | 5 | 2 | 1 | 0 | 8 |
| 10 CFR 73.56 | 6 | 1 | 0 | 0 | 7 |
| 10 CFR 73.58 and 73.55(m) | 4 | 1 | 0 | 0 | 5 |
| 10 CFR 50.65 and 50.72 | 3 | 1 | 0 | 0 | 4 |
| NERC CIP | 5 | 3 | 0 | 0 | 8 |
| Group-wide (SEC, state breach law, OFAC, CIRCIA) | 2 | 2 | 0 | 1 | 5 |
| Applicability decisions (73.110, DOE-417) | 0 | 0 | 0 | 2 | 2 |
| **Total (78)** | **51** | **22** | **2** | **3** | **78** |

Of the 24 gap rows, 7 are rated High and 17 Moderate.

**The CSPs themselves are sound.** Every 73.54 paragraph that the NRC inspects at the CDA level is Met, and there are no open NRC findings. The five Partially met 73.54 rows are all about the **interface with the business side**:
- **73.54(c)(2) and RG 5.71 C.7, C.3.7, B.1.19 (High):** the kiosk update path. Malware signatures and kiosk software reach the 9 PMMD kiosks from a server on the plant business network, and the packages are not checked against vendor signatures. RG 5.71 C.7 asks that data and software moved to higher levels use a validation process "trustworthy at or above the trust level" of the device it goes to. The kiosks are CSP controls, but their content currently inherits the trust of the business network. The finding was entered in the station CAP within 24 hours (73.77(b)(1)).
- **73.54(d)(2) (High):** business-side risks that could reach CDAs were not part of the CSP risk process until the 2026 group analysis. The clearest example is CDA work packages (identifiers, firmware versions, network details for 5 units) readable by all about 7,300 work management users.
- **73.54(d)(1), (d)(4), (e)(2):** outage vendor briefings on PMMD rules, notification triggers, and the missing SOC-to-CST handoff.

**Not met (2):**
- **73.77(a)(2)(iii):** the group matrix tells staff to report attacks to the FBI and CISA but does not say that such a report, for an event related to the cyber security program for 73.54 systems, starts a 4-hour NRC clock (scenario gap 8).
- **73.22(e):** P07 testing found 6 networked multifunction printers in the Station A and B security buildings with manufacturer default admin passwords, used to copy SGI. 73.22(e) requires reproduction equipment to be "evaluated to ensure that unauthorized individuals cannot access Safeguards Information" through retained memory or network connectivity.

**NERC CIP:** Station C's low impact plan lacks the CIP-003-9 Section 6 vendor remote access methods that became enforceable on 2026-04-01; 2 ESP inbound rules from the corporate network lack documented reasons (CIP-005-7); and CIP-008-6 R4 (E-ISAC and CISA within 1 hour of determining a Reportable Cyber Security Incident, end of next calendar day for an attempt to compromise) is not in the group matrix.

### 4.2 Engineering and Radiation Services (`gap-analysis-engineering-radiation-services.csv`)
| Regulation or source | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| SGI (73.21-73.22) | 6 | 2 | 2 | 0 | 10 |
| 73.56 contractor/vendor program | 3 | 1 | 2 | 0 | 6 |
| Dosimetry (20.1501(d), 20.2106) | 2 | 1 | 0 | 0 | 3 |
| Contracts and state breach law | 0 | 2 | 0 | 0 | 2 |
| Part 810 and client QA requirements | 0 | 2 | 0 | 0 | 2 |
| FAR 52.204-21 (DOE contracts) | 14 | 1 | 0 | 0 | 15 |
| Applicability decisions (DFARS/CMMC, HIPAA, FTC Safeguards Rule) | 0 | 0 | 0 | 3 | 3 |
| **Total (41)** | **25** | **9** | **4** | **3** | **41** |

Of the 13 gap rows, 3 are High, 8 Moderate, and 2 Low.

**Not met (4):**
- **73.56(k) and 73.56(m) (High):** contractor/vendor access authorization files for about 2,900 outage workers sit in engineering project shares. Project team members can read them, but they are not people "who collect, process, or have access to personal information" under a trustworthiness and reliability determination for that purpose (scenario gap 5).
- **73.22(b)(1):** need-to-know determinations are not documented for 31 contractor engineers (scenario gap 4).
- **73.22(e):** one office copied SGI on a networked scanner (scenario gap 4).

**Partially met, worth noting:** dosimetry customer administrators sign in with a password only (20.2106(d) says the records "should be protected from public disclosure"); customer contracts require notice within 72 hours of confirming an incident, and Florida law requires a third-party agent to notify the covered entity within 10 days, but neither is in the group matrix; and engineers use a generative AI assistant without a quality assurance rule for safety-related work.

### 4.3 Radioactive Waste Management (`gap-analysis-waste-management.csv`)
| Regulation or source | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| Applicability (Part 37 by facility) | 1 | 0 | 0 | 0 | 1 |
| 10 CFR Part 37 (Florida license condition) | 14 | 5 | 1 | 0 | 20 |
| DOT security plan, RCRA records, FCRA and Disposal Rule, FAR 52.204-21 | 6 | 2 | 0 | 0 | 8 |
| CSF 2.0 OT benchmark (voluntary) | 4 | 5 | 3 | 0 | 12 |
| Group policy (inheritance, supplement alignment) | 0 | 0 | 2 | 0 | 2 |
| **Total (43)** | **25** | **12** | **6** | **0** | **43** |

Of the 18 gap rows, 6 are High, 10 Moderate, and 2 Low.

**The physical program is sound; the gaps are where Part 37 meets the network.** The Florida vault's intrusion detection and PACS share the facility business network with no alternate path. 37.49(c)(2) requires that alternative communications and data transmission "may not be subject to the same failure modes as the primary systems" (Not met, High). The same dependence makes 37.49(a)(1) and (c)(1) Partially met. In the OT benchmark, vendor remote access to processing PLCs uses a shared account without MFA or session monitoring (PR.AA-03 and DE.CM-06, Not met).

**Group policy rows (Not met):** the division has no inheritance matrix for group common controls and its supplement was last aligned in 2024 (scenario gap 9). Without the matrix it cannot show that Part 37 and RCRA records rely on group immutable backups (37.101, Partially met).

### 4.4 Overall
Across all 162 rows: **101 Met, 43 Partially met, 12 Not met, and 6 Not applicable.** Of the 55 gap rows, **16 are High, 35 Moderate, and 4 Low.**

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Kiosk update path not validated (3) | NG | 73.54(c)(2); RG 5.71 C.7, C.3.7, B.1.19 | High | Signature verification on server and kiosks; restricted segment; CST release step; replace Station B kiosk OS | Fleet cyber security program manager | 2026-11-30 (OS 2026-12-31) |
| 2 | SGI reproduction on networked devices (4; P07) | NG, ER | 73.22(e), (g)(4) | High | Change printer passwords; stand-alone copiers; sanitize device storage; evaluate every reproduction device | Fleet security director; SGI program manager | 2026-10-31 |
| 3 | Contractor/vendor access authorization files exposed (5) | ER | 73.56(k), (m), (o)(1) | High | Restricted repository owned by the program; access review; write-once retention | Contractor/vendor access authorization program manager | 2026-11-30 |
| 4 | Vault security systems on the business network (7) | WM | 37.49(a)(1), (c)(1)-(2); PR.IR-01 | High | Security network; cellular alternate path | Florida facility Radiation Safety Officer | 2026-12-31 |
| 5 | Vendor remote access to PLCs (7) | WM | PR.AA-03; DE.CM-06 | High | Named per-session access with MFA and recording | Radioactive Waste Management OT lead | 2026-11-30 |
| 6 | CDA information in business systems (2) | NG | 73.54(d)(2); 73.22(g)(1) | High | Restricted CDA module and label; SGI marking scan; transmittal screening | Work management director; fleet security director | 2026-12-31 |
| 7 | Multi-regulator notification (8) | All | 73.77(a)(2)(i), (a)(2)(iii), (a)(3); CIP-008-6 R4; 37.57; Fla. Stat. 501.171(6); contracts; Form 8-K Item 1.05 | Moderate | Complete the matrix (P08); SOC trigger list; joint SOC and CST drill; disclosure committee tabletop | Group General Counsel | 2026-12-15 |
| 8 | SGI need-to-know and access list (4) | ER | 73.22(b)(1); 73.21(a)(1) | Moderate | Document determinations; quarterly reconciliation | SGI program manager | 2026-11-30 |
| 9 | AI and business-side changes not screened (10) | NG, ER | 73.58(b)-(c); 50.65(a)(1); client QA requirements | Moderate | 73.58 screen and Maintenance Rule review of the pilot; QA rule for engineering AI (P10) | Fleet engineering director; Engineering and Radiation Services chief engineer | 2026-12-31 |
| 10 | Waste division inheritance and supplement drift (9) | WM | POL-01 4.5, 4.6; 37.101 | Moderate | Inheritance matrix; re-issue supplement; annual attestation | Radioactive Waste Management security and compliance lead | 2026-12-31 |
| 11 | Dosimetry portal authentication (6) | ER | 20.2106(d); customer contracts | Moderate | MFA for customer administrators, then all users | Dosimetry laboratory director | 2026-12-31 |
| 12 | NERC CIP items | NG | CIP-003-9 Attachment 1 Section 6; CIP-005-7 | Moderate | Station C vendor remote access methods; ESP rule review | CIP Senior Manager | 2026-12-31 to 2027-03-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). POAM-021 to POAM-025 trace directly to rows in this analysis that P07 did not test (ER-G02 and ER-G04; G-065; G-055 and G-060; ER-G23; G-024).

**CSP items stay in the CAP.** Roadmap items 1 and 2 are deficiencies in or next to a station CSP or the SGI program. They were entered in the station CAP and cannot be risk-accepted (P01 section 1). The roadmap tracks them; the CAP is the record of correction.

## 6. Pending regulatory changes
**NRC "Modernizing Security Requirements" (91 FR 38928, 2026-06-26; Docket NRC-2025-1303; comments closed 2026-07-27).** Proposed only and **not final as of 2026-09-25**. Read from the Federal Register text, it would:
- replace "high assurance" with "reasonable assurance" in 73.54(a), 73.56(c), and 73.22(f)(3), among others, and remove 73.54's introductory implementation paragraph;
- replace the specific 73.77 notification categories (including the 4-hour FBI-report trigger and the 24-hour CAP recording) with notification under 50.72 or 73.1200 "based on the function adversely impacted (safety or security)," and withdraw RG 5.83;
- update RG 5.71 in ways the NRC says would cut "approximately 19 percent of controls";
- let licensees set risk-based security program review periods in place of the fixed 24 months in 73.55(m);
- revise 73.22(f)(3) and (g) to allow encrypted transmission of SGI using an active FIPS 140 version. 73.22(e), the basis for roadmap item 2, would not change.

None of this is treated as current. The `pending_rule_change` column flags each affected row. The CSPs are license conditions, so even a final rule would change station practice only through a CSP change that follows the final rule. P01 GR-16 and NG-021 track the risk that staff act on the proposal early.

**NRC Part 37 proposal (91 FR 17893, 2026-04-09; Docket NRC-2025-1238).** Not final as of 2026-09-25. As proposed it would remove 37.49(c) (continuous and alternative communications and data transmission), the weekly category 2 verification in 37.49(a)(3)(ii), and 37.51, and change LLEA coordination to at least every 3 years. Florida would apply any final change only by updating its license condition. **The group's position:** even without 37.49(c), 37.49(a)(1) still requires continuous monitoring or an alarm and response when monitoring is lost, so roadmap item 4 goes ahead under CSF PR.IR-01.

**NERC CIP:** CIP-003-10 and CIP-003-11, CIP-008-7.1, and CIP-015-1 (internal network security monitoring) are approved for future enforcement (2028 to 2029). They are noted, not analyzed.

**CIRCIA:** no final rule as of 2026-09-25. Not treated as an obligation.
