# Regulatory Gap Analysis: Cris Santos Company | Government Services and Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings, NAICS 561210) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Primary standard | NIST SP 800-53 Rev. 5, Release 5.2.0 (Aug 27, 2025), **Moderate baseline** from SP 800-53B: 177 base controls with 110 enhancements. **Binding by contract** for the state scope; **benchmark** for the rest of the IFOP. OT tailoring from NIST SP 800-82 Rev. 3 (September 2023) |
| Other rules analyzed (all applicable rules for the primary business line) | FAR 52.204-21 (NOV 2021), its 15 basic safeguarding requirements and flow-down; FAR 52.204-23, 52.204-25, 52.204-30, and 52.204-9 for the federal contract (clause text read from eCFR, point-in-time 2026-09-23); the CUI Program, 32 CFR Part 2002 (eCFR, 2026-09-23), as GSA flows it to the company; Florida duties that reach a contractor, Fla. Stat. 501.171 and 119.0701 (2026 Florida Statutes, read on flsenate.gov 2026-10-07) |
| System | Integrated Facility Operations Platform (IFOP), per the SSP (P02), plus the corporate systems that hold FCI and personal information |
| Assessment dates | Fieldwork 2026-07-06 to 2026-07-31 (site walkthroughs at 8 sites 2026-07-14 to 2026-07-23); statuses refreshed with P07 results through 2026-08-21 |
| Assessors | Security Manager and GRC analyst with the Contracts Director, the OT Security Engineer, and the vCISO; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability
The vertical profile names SP 800-53 Rev. 5 as the primary control set because FISMA, IRS Pub. 1075, CJIS, and GovRAMP are all built on it. **But SP 800-53 is a catalog, not a law. It binds a private contractor only through a contract or a federal system authorization.** So the first step was to sort out which customer rules reach this company, and how. At this size the answer has more parts than at the Small tier: six customers, two critical facilities, and a revenue level that now exceeds the SBA size standard.

### 1.1 Who the customers are
| Contract | Customer | What the company operates | How security terms reach the company |
|---|---|---|---|
| CT-F | GSA Public Buildings Service (5 federal office buildings) | GSA's BAS on the GSA Building Systems Network (BSN), through GSA's virtual desktop with PIV cards | FAR clauses; the statement of work incorporates the GSA Building Technologies Technical Reference Guide (BTTRG) Version 3.0, dated May 1, 2024, GSA IT Security Policy CIO 2100.1, and CUI handling under GSA Order PBS 3490.3 |
| CT-S | State agency (9 buildings, including its data center building) | The IFOP: BAS clusters and the agency's access control tenant | Contract cybersecurity exhibit requiring SP 800-53 Rev. 5 Moderate controls. Florida requires state agency IT service contracts to meet state and federal standards including NIST CSF and to set out security responsibilities (Fla. Stat. 282.318(4)(h), verified 2026-10-07) |
| CT-C1, CT-C2, CT-M | County A, County B, the City | The IFOP for their sites | Security addenda requiring compliance with each local government's cybersecurity standards, which Fla. Stat. 282.3185(4)(a) requires counties and municipalities to adopt consistent with NIST CSF |
| CT-K | School district | Remote access to the district's own BAS server; energy analytics | Contract terms only. A school district is not a "local government" under Fla. Stat. 282.3185(2), which defines that term as "any county or municipality" |

### 1.2 Decisions, requirement by requirement
| ID | Requirement | Applies to the company? | Reason |
|---|---|---|---|
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558) | **Indirectly, for CT-F only** | FISMA makes each agency responsible for information systems "used or operated by an agency or by a contractor of an agency" (44 U.S.C. 3554(a)(1)(A)(ii)). GSA's BAS servers hold a GSA FISMA Moderate ATO and GSA runs their scanning, logging, and POA&M (BTTRG section 1.0). The company must follow GSA IT policies when it operates them (BTTRG section 1.1), but the ATO and its control set belong to GSA. **No company-owned system operates on GSA's behalf.** Under 32 CFR 2002.14(h)(2), a contractor that receives federal information only incidental to providing a service other than processing services does not operate a federal information system |
| C-GOVERNMENT-R02 | IRS Pub. 1075 | No | No FTI. The state contract states the company has no access to FTI areas or systems |
| C-GOVERNMENT-R03 | CJIS Security Policy v6.1 | No | Both county contracts exclude the sheriff's offices, jails, and the 911 center. The County A EOC houses emergency management, not the 911 center. Recheck if the scope changes |
| C-GOVERNMENT-R04 | VVSG 2.0 | No | VVSG governs voting systems. The company maintains only doors and cameras at the elections warehouse; the Supervisor of Elections annex sets the physical access rules, which are analyzed as contract terms (risk R-031) |
| C-GOVERNMENT-R05 | FERPA | No | The school district work is HVAC and BAS only. The company receives no education records, and the contract bars access to student information systems |
| C-GOVERNMENT-R06 | CIRCIA | Not in force | Proposed rule only (89 FR 23644). **Size now matters:** proposed 6 CFR 226.2 would cover an entity in a critical infrastructure sector that exceeds the SBA small business size standard for its NAICS code. At about $100 million in receipts the company exceeds the $47.0 million standard for NAICS 561210, so whether a facilities contractor is "in" the Government Services and Facilities sector would decide coverage if the rule is finalized as proposed. Tracked in section 6 |
| C-GOVERNMENT-R07 | SLCGP (6 U.S.C. 665g) | No | A grant condition for governments |
| C-GOVERNMENT-R08 | GovRAMP | Not to the company today | GovRAMP verifies cloud providers. No contract requires it. It matters for the access control SaaS vendor (P09) and possibly for the 2028 state rebid, because the company hosts BAS supervisory services for the agency |

**What binds the company, and at what size.** None of these rules has a size exemption that helps the company. Crossing the SBA standard changes only the CIRCIA watch item. The FAR clauses apply to every contractor that signs them, and the state exhibit applies regardless of headcount.

- **SP 800-53 Rev. 5 Moderate: binding by contract** for components that store or process state agency data (the CT-S clusters and tenant, the broker, the landing zone). **Benchmark** for the County A, County B, and City scope, whose CSF-based standards are met more simply with one control set.
- **FAR 52.204-21: binding** for company systems that process, store, or transmit federal contract information: the CMMS, email, file storage, and laptops.
- **CUI.** GSA marks sensitive building drawings as CUI under GSA Order PBS 3490.3 CHGE 1, and the statement of work requires the company, as an authorized holder, to protect them under 32 CFR Part 2002. The contract does not cite NIST SP 800-171. The company handles CUI in its CUI library under the 800-53 media and access controls, and analyzes the authorized holder duties in 2002.14, 2002.16, and 2002.20 directly (6 rows). **Watch item:** 32 CFR 2002.14(h)(2) tells agencies to use SP 800-171 when they set requirements for non-federal systems, and the proposed FAR overhaul would add SP 800-171 Rev. 3 clauses (section 6).
- **Supply chain and PIV clauses (52.204-23, -25, -30, -9): binding**, with short reporting clocks (section 4) and flow-downs to subcontractors.
- **Florida:** the company is a third-party agent for its customers' personal information and a covered entity for its own employee data (Fla. Stat. 501.171), and a contractor with public records duties (Fla. Stat. 119.0701).

### 1.3 OT tailoring
The controls were applied to OT components (BACnet controllers, door controllers, edge firewalls, engineering workstations, OT sensors) using NIST SP 800-82 Rev. 3. Examples: vulnerability identification on OT uses passive discovery and approved windows, not live active scans (RA-5). Where BACnet cannot encrypt, segmentation compensates (SC-8, SC-7). Where field devices cannot do lockout or MFA, broker-only management access compensates (AC-7, IA-2). No base control was tailored out; three enhancements are not applicable (IA-2(12), IA-8(1), SA-4(10)) because the IFOP has no federal users and accepts no PIV credentials.

## 2. Method
1. **Requirements.** One row per Moderate base control (G-001 to G-177), with its Moderate enhancements listed in the citation column and assessed inside the row; 22 FAR rows (G-178 to G-199) cited to clause paragraph; 6 CUI rows (G-200 to G-205) and 5 Florida rows (G-206 to G-210) decomposed from the regulation text. Total: 210 rows.
2. **Crosswalk.**
   - 134 control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`).
   - The other 43 control rows, and all FAR, CUI, and Florida rows, are author mappings, labeled as such. FAR rows map to SP 800-53 through the SP 800-171 Rev. 2 lineage of the 15 requirements.
3. **Evidence.** Interviews with control owners and all five program managers; configuration exports (identity provider, cloud IAM, broker, edge firewalls, tenant administrator lists, BAS cluster user lists); CMMS records; contracts, subcontracts, and purchase records; walkthroughs at 8 sites (3 federal buildings, the state data center building, the County A government center, EOC, and elections warehouse, and one City building); and the P07 tests.
4. **Evidence sampling.** Where a requirement operates many times, a sample was tested rather than the whole population. Samples were drawn at random from system-generated populations using the co-sourced internal audit firm's attribute sampling table (25 items for a control operating many times a year at moderate risk; 5 to 15 for monthly or less frequent controls):
   - terminations: 25 of 96; transfers: 15 of 41; new hires: 25 of 118;
   - PIV holder departures: 25;
   - BAS program change tickets: 25; IT change tickets: 15;
   - backup job days: 30 of 30 (July 2026);
   - CUI drawing transfers: 20; purchase orders for network, video, and OT equipment: 25;
   - incident records: 10 of 37;
   - subcontract files: all 7 OT subcontractors and all 9 FCI subcontracts.
   Each `evidence` cell names the sample and its result where one was used.
5. **Status.** Met, Partially met, Not met, or Not applicable. A base control row is Met only when the base control and all of its Moderate enhancements are implemented. Gap risk uses the P01 scale.

The same statements appear in the SSP control table (P02), so the two documents do not drift apart.

## 3. Results summary
### 3.1 SP 800-53 Rev. 5 Moderate baseline (177 base controls)
| Family | Met | Partially met | Not met |
|---|---|---|---|
| AC Access Control | 4 | 13 | 0 |
| AT Awareness and Training | 2 | 2 | 0 |
| AU Audit and Accountability | 3 | 8 | 0 |
| CA Assessment, Authorization, and Monitoring | 2 | 5 | 0 |
| CM Configuration Management | 1 | 11 | 0 |
| CP Contingency Planning | 1 | 8 | 0 |
| IA Identification and Authentication | 3 | 7 | 0 |
| IR Incident Response | 3 | 5 | 0 |
| MA Maintenance | 1 | 5 | 0 |
| MP Media Protection | 3 | 4 | 0 |
| PE Physical and Environmental Protection | 13 | 3 | 0 |
| PL Planning | 3 | 3 | 0 |
| PS Personnel Security | 6 | 3 | 0 |
| RA Risk Assessment | 5 | 1 | 0 |
| SA System and Services Acquisition | 3 | 8 | 0 |
| SC System and Communications Protection | 14 | 4 | 0 |
| SI System and Information Integrity | 6 | 5 | 0 |
| SR Supply Chain Risk Management | 1 | 7 | 1 |
| **Total (177)** | **74** | **102** | **1** |

**Reading the results.** The company has a defined program with gaps in scale. Strong areas are identity for company users, cloud design, backups, physical security, and personnel screening. The weak families are the ones that matter most for operating OT for many customers through many subcontractors: configuration management, contingency planning, audit and monitoring, maintenance, acquisition, and supply chain. The one Not met row is SR-10 (no inspection of OT parts on receipt).

### 3.2 Other rules (33 rows)
| Rule | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| FAR 52.204-21(b)(1) (15 requirements) | 13 | 1 | 0 | 1 | 15 |
| FAR 52.204-21(c) flow-down | 0 | 1 | 0 | 0 | 1 |
| FAR 52.204-23, -25, -30 and their flow-downs | 2 | 2 | 0 | 0 | 4 |
| FAR 52.204-9(b) and (d) | 0 | 2 | 0 | 0 | 2 |
| CUI Program, 32 CFR 2002.14, 2002.16, 2002.20 | 2 | 4 | 0 | 0 | 6 |
| Florida, Fla. Stat. 501.171 and 119.0701 | 1 | 4 | 0 | 0 | 5 |
| **Total (33)** | **18** | **14** | **0** | **1** | **33** |

The **N/A** row is 52.204-21(b)(1)(xi) (subnetworks for publicly accessible components); the company hosts none in its own networks. The FAR basic safeguarding requirements are largely Met because the FCI systems are the company's best-protected IT; the gaps are in flow-downs to subcontractors.

### 3.3 All rows
| Status | Rows |
|---|---|
| Met | 92 |
| Partially met | 116 |
| Not met | 1 |
| Not applicable | 1 |
| **Total** | **210** |

### 3.4 Gap risk (Partially met and Not met rows, 117 in total)
| Gap risk | Rows |
|---|---|
| Very High | 2 |
| High | 20 |
| Moderate | 47 |
| Low | 46 |
| Very Low | 2 |

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Subcontractor remote access outside the broker at 11 sites; legacy VPN profiles | AC-17; MA-4; IA-8 | Very High | All subcontractors onto the broker; tools removed; management only from the broker | OT Security Engineer | 2026-12-31 |
| Default and shared field device credentials; shared accounts on 3 clusters and one tenant | IA-5; IA-2; CM-6 | High | Change defaults; vault for all 46 sites; named accounts | OT Security Engineer; Controls Engineering Manager | 2026-12-31 |
| Subcontractors not bound or reviewed; flow-downs missing; subcontractor equipment not screened | SA-9; PS-7; SR-3; FAR 52.204-21(c), 52.204-25(b)(2) and (d), 52.204-9(d) | High | Security addendum with FAR flow-downs for every subcontractor; screening of subcontractor-supplied equipment | Contracts Director | 2026-12-31 |
| OT activity not monitored | AU-2; AU-6; SI-4 | High | OT events to the SIEM by 2027-01-31; sensors at all sites by 2027-06-30 | OT Security Engineer | 2027-06-30 |
| No IFOP contingency plan; manual-mode procedures missing for 4 customers; recovery unproven | CP-2; CP-4; CP-10 | High | EOC procedure 2026-12-15; plan and quarterly cluster restore tests | IT Director (ISO) | 2027-03-31 |
| No OT segmentation at 17 sites | SC-7; AC-4 | High | OT VLANs with County B and City IT | OT Security Engineer | 2027-06-30 |
| OT inventory not reconciled; no OT vulnerability identification; firmware behind; unsupported workstations | CM-8; RA-5; SI-2; SA-22 | High | Passive discovery at all sites; firmware program; replace 9 workstations | OT Security Engineer | 2027-06-30 |
| Customer tenant access removed by hand; reviews twice a year | AC-2; PS-4; Fla. Stat. 501.171(2) | Moderate | Federate tenants; quarterly reviews | Security Systems Manager | 2027-03-31 |
| CUI sent by email outside the library; derivative copies unmarked | MP-4; AC-21; 32 CFR 2002.16(a)(3)-(4), 2002.20(a)(1) | Moderate | Data loss rule on CUI markings; subcontractor CUI terms | Contracts Director | 2026-12-31 |
| BAS changes not consistently approved or integrity-checked | CM-3; SI-7 | Moderate | CMMS approval step; hash check before download | Director of Building Technology | 2027-03-31 |

**Reporting clocks in the FAR clauses (verified in eCFR, 2026-09-23):**
- 52.204-25(d): report covered telecommunications or video surveillance equipment within **1 business day** of identification, with further information within 10 business days.
- 52.204-23(c): report Kaspersky covered articles within **3 business days**, then 10 business days.
- 52.204-30(c): check SAM.gov for FASCSA orders at least once every three months and report within **3 business days**, then 10 business days.

High and Moderate gaps feed the risk register (P01) and the POA&M (P07).

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Close the doors** | 2026 Q4 | Remote unlock removed at the elections warehouse cage (before 2026-11-03); cellular modem removed; subcontractors onto the broker; defaults changed; subcontractor addendum and FAR flow-downs; EOC manual-mode procedure; County A tabletop | AC-17; MA-4; IA-5; IA-8; SA-9; PS-7; FAR 52.204-21(c), 52.204-9(d); CP-2 (EOC) |
| **2. See and recover** | 2027 Q1 | OT events in the SIEM; quarterly cluster restore tests; IFOP contingency plan; tenant federation and quarterly reviews; standards STD-01 to STD-03 issued; edge firmware program | AU-2; AU-6; CP-2; CP-4; CP-10; AC-2; CM-6; SI-2 |
| **3. Segment and inventory** | 2027 Q2 | OT VLANs at the 17 flat sites; passive sensors at all 46 sites; unsupported workstations replaced; SOC 2 Type 1 (P09) | SC-7; AC-4; CM-8; RA-5; SI-4; SA-22 |
| **4. Sustain and prove** | 2027 Q3-Q4 | SOC 2 Type 2 observation period 2027-07-01 to 2027-12-31; annual risk assessment (July 2027); second independent assessment; interconnection agreements renewed | CA-2; CA-7; CA-3; SR-6 |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending changes (not current obligations)
- **CIRCIA.** No final rule as of 2026-09-25; reporting is voluntary. If finalized as proposed, the size-based criterion in proposed 6 CFR 226.2 could reach the company because it exceeds its SBA size standard (section 1.2). The P08 matrix carries the proposed 72-hour and 24-hour clocks as "not yet required".
- **FAR overhaul (RFO).** The proposed rule (FR Doc. 2026-12559, June 23, 2026) would move information security clauses into FAR part 40, renumber 52.204-21 as 52.240-5, and add CUI clauses (52.240-6 and -7) requiring NIST SP 800-171 Rev. 3 and CUI incident reporting within 72 hours of discovery. **Proposed only**; comments closed 2026-07-23. Flagged in the `pending_rule_change` column of the FAR and CUI rows. If finalized, the CUI library and the FCI systems would need an SP 800-171 Rev. 3 assessment; the official CSF 2.0 to SP 800-171 Rev. 3 crosswalk in `00_universal-framework/crosswalks/` gives a starting point.
- **NIST SP 800-82 Rev. 4.** Initial public draft published 2026-09-21 (comments due 2026-11-30), confirmed on the NIST CSRC publication page. **Draft only.** Rev. 3 remains the OT reference here. Flagged on the OT rows (for example AC-17, CM-6, CM-8, CP-2, RA-5, SC-7, SI-4).
- **GovRAMP.** Not law and not in any current contract; watch for the 2028 state rebid.
