# Regulatory Gap Analysis: Cris Santos Company Holdings | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Mining, Quarrying, and Oil and Gas Extraction (focus division: Crude Oil Production) |
| Primary benchmark (Production) | NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29, all 106 subcategories), applied to OT with NIST SP 800-82 Rev. 3. **Voluntary: no binding federal sector cybersecurity rule applies to the Production division** (section 1.2) |
| Division regulations | Power Generation: NERC CIP-002-5.1a, CIP-003-9 (low impact), CIP-012-2, and EOP-004-4. Crude Logistics: PHMSA 49 CFR Part 195 (control room management, reporting, gathering line classes) and the Hazardous Materials Regulations security plan and training rules (49 CFR 172.800 to 172.804, 172.704) |
| Group-wide | SEC Reg S-K Item 106 and Form 8-K Item 1.05; state breach laws (Florida as the worked example) |
| Gap tables | `gap-analysis.csv` (Crude Oil Production, 108 rows); `gap-analysis-power-generation.csv` (30); `gap-analysis-crude-logistics.csv` (33); `gap-analysis-group.csv` (12) |
| Assessment dates | 2026-05-04 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28, including the 2026-08-13 Permian field test) |
| Assessors | Division security and compliance leads with the Power Generation NERC Compliance Manager and the Crude Logistics Pipeline Compliance Manager, coordinated by the Group General Counsel; reviewed by group internal audit |
| Regulatory driver labels | `N21-BM (...)` points to the Production benchmark; `N22-R01 (CIP-...)` to NERC CIP; `PHMSA 195.xx` and `HMR 172.xxx` to the Crude Logistics rules; `N48-49-R08` to SEC disclosure (see `../00_company-facts.md` section 5) |

## 1. Applicability
### 1.1 Regulation-by-division matrix
| Requirement | Crude Oil Production | Power Generation | Crude Logistics | Group (corporate) |
|---|---|---|---|---|
| NIST CSF 2.0 with SP 800-82 Rev. 3 (N21-BM) | **Primary benchmark** (voluntary) | Group program structure | Group program structure | Group policies (P06) |
| EPA 40 CFR 112.9(c)(4)(iv) (SPCC, production containers) | **Applies** (about 250 batteries use SCADA-transmitted high-level alarms) | Not applicable | Not applicable (breakout tanks are under Part 195) | Not applicable |
| EPA 40 CFR 110.6 (oil discharge notice) | Applies | Applies (fuel and lube oil) | Applies (pipeline and truck releases to water) | Coordinates |
| NERC CIP-002-5.1a, CIP-003-9 (low impact), EOP-004-4 (N22-R01) | Not applicable (no BES assets) | **Primary** (Generator Owner and Generator Operator) | Not applicable | Not applicable |
| NERC CIP-012-2 | Not applicable | **Applies** (the GCC is a Generator Operator Control Center) | Not applicable | Not applicable |
| NERC CIP-004 to CIP-011, CIP-013, CIP-014 | Not applicable | Not applicable (low impact only; not a TO or TOP) | Not applicable | Not applicable |
| Form DOE-417 | Not applicable | Not a required filer (section 1.3) | Not applicable | Not applicable |
| PHMSA 49 CFR Part 195 | Not applicable (production facilities and flow lines are excepted, 195.1(b)(8)) | Not applicable | **Primary**: trunk line in full; 120 miles of regulated rural gathering lines (195.11); about 2,180 miles reporting-regulated-only (195.15) | Not applicable |
| HMR security plan and training (49 CFR 172.800 to 172.804, 172.704) | Not applicable (crude leaves the lease by pipeline or in Crude Logistics trucks) | Not applicable | **Applies** (large bulk Class 3, PG I or II, 172.800(b)(6)) | Not applicable |
| HMR incident reports (49 CFR 171.15, 171.16); FMCSA ELD rules (49 CFR 395.34, 390.36) | Not applicable | Not applicable | Applies | Not applicable |
| TSA pipeline Security Directives (N21-R02) | Not applicable | Not applicable | **Not applicable** (no TSA notice) | Not applicable |
| USCG 33 CFR Part 101 Subpart F (N21-R01) | Not applicable | Not applicable | Not applicable | Not applicable (no MTSA or OCS facilities) |
| CIRCIA (N21-R03), proposed | Tracked only | Tracked only | Tracked only | Tracked only (not in effect) |
| SEC Reg S-K Item 106; Form 8-K Item 1.05 (N48-49-R08) | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach laws | Royalty owners in all 50 states (Florida worked example: Fla. Stat. 501.171) | Employees | Employees and drivers | Coordinates |
| SOC 2 (contractual) | Not in scope (P09) | Not in scope (P09) | Shipper services platform in scope (P09) | Group services carved in |

### 1.2 Crude Oil Production: why a voluntary benchmark
No binding federal sector cybersecurity rule applies to an onshore producer. Part 195 excludes onshore production facilities and flow lines (195.1(b)(8)), so the IOC, BCC, and Florida control room are not pipeline control rooms under 195.446. There are no offshore, Outer Continental Shelf, or MTSA-regulated facilities, so neither BSEE rules nor USCG Subpart F apply. MSHA has no cybersecurity rules, and DOE (the sector risk management agency) issues guidance, not rules. The division's binding duties that touch cyber-physical safety are environmental: the SPCC high-level alarm option at about 250 batteries depends on alarms reaching SCADA (G-107), and a discharge to water must be reported to the National Response Center immediately (G-108). The group therefore benchmarks the division against all 106 CSF 2.0 subcategories, with SP 800-82 Rev. 3 supplying the OT practices (architecture in section 5, program content in section 3, and OT guidance for each function in section 6).

### 1.3 Power Generation: NERC categorization and the self-report decision
- **Registration:** Generator Owner and Generator Operator. **Impact:** low only. The largest plant is 640 MW and the GCC dispatches 1,180 MW, below the 1,500 MW bright lines in CIP-002-5.1a criteria 2.1 and 2.11; no planner designation (2.3) or IROL identification (2.6) exists; so no high (criterion 1.4) or medium rating applies. All four assets (P1, P2, P3, and the GCC with its backup function) contain low impact BES Cyber Systems (criteria 3.1 and 3.3).
- **CIP-012-2 applies** because the GCC is a Control Center operated by a Generator Operator, and it sends real-time data about plants it is not co-located with (so the 4.2.3 exemption does not apply). CIP-012-2 became enforceable on 2026-07-01.
- **DOE-417:** the instructions name Balancing Authorities, Reliability Coordinators, electric utilities (entities with distribution facilities), and Generating Entities with 300 MW or more dedicated to end-use customers. The division is none of these, because all its output is sold in wholesale markets. It gives its Balancing Authorities the information they need, and EOP-004-4 accepts a DOE-417 form as the event report format.
- **Possible noncompliance (scenario gap 3).** Since CIP-003-9 took effect on 2026-04-01, Plant P3's turbine vendor has had a standing remote access path with no method to detect malicious communications (Attachment 1 Section 6.3, EG-21), and reviews of OEM transient cyber assets have not been recorded (Section 5.2, EG-16 and EG-17). **Decision (CIP Senior Manager with the Group General Counsel, 2026-09-17):** self-report both issues to the Regional Entity with a mitigation plan, rather than wait for an audit. Reasons: the gap is known and documented here, it began on the effective date, and the fix (moving the P3 path into group PAM with OT sensor rules) is scheduled for 2026-12-31 (POAM-013, POAM-014).

### 1.4 Crude Logistics: which lines and which rules
- **Trunk line (140 miles, 16 inch, intrastate):** a gathering line under 195.2 is 8 5/8 inch or less, so the trunk line is a regulated pipeline covered in full (195.1(a)(3)). Its Pipeline Control Center and backup PCC are control rooms under 195.446. As an intrastate line, its procedures are submitted to the state pipeline safety agency on request (195.446(i)).
- **Regulated rural gathering lines (120 miles):** 6 5/8 to 8 5/8 inch, in or near an unusually sensitive area, above the stress threshold (195.11(a)). They carry the 195.11(b) requirements, including Subpart B reporting.
- **Reporting-regulated-only gathering lines (about 2,180 miles):** annual and accident reports under Subpart B (195.15), but the one-hour telephonic notice of 195.52 does not apply to them (195.15(c)(2)). The P08 matrix keeps this distinction.
- **Trucking:** crude moves in about 1,150 cargo tanks of about 8,400 gallons. UN1267 in Packing Group I or II in a single packaging over 3,000 liters is a large bulk quantity of Class 3 material, so a security plan is required (172.800(b)(6)) with in-depth security training (172.704(a)(5)).
- **TSA:** the Pipeline Security Directives apply only to owners and operators TSA has notified that their pipeline is critical. TSA has not notified the division.

### 1.5 Group-wide screens
USCG Subpart F does not apply (no vessel, MTSA facility, or OCS facility; 33 CFR 101.605(a)). CIRCIA is not in effect; if finalized as proposed, the group would be covered because 45,000 employees exceeds the 1,250-employee SBA standard for NAICS 211120 (13 CFR 121.201). FAR safeguarding and covered-article clauses do not apply (no federal contracts).

## 2. Method
1. **Requirements.** Production rows are the 106 CSF 2.0 subcategories, quoted from the CSF 2.0 core, plus two EPA rows. NERC rows follow each standard's requirement and Attachment 1 structure (CIP-002-5.1a, CIP-003-9, CIP-012-2, EOP-004-4, read from the NERC standard documents). Part 195, HMR, and FMCSA rows follow the CFR section structure (eCFR, current through 2026-09-23). Group rows follow 17 CFR 229.106, Form 8-K Item 1.05, and Fla. Stat. 501.171.
2. **Crosswalk.** For CSF rows, SP 800-53 Rev. 5 controls come from NIST's official CSF 2.0 informative references (column `nist_official_sp800_53r5`); `sp800_53_controls` is the author's key-control selection, and the SP 800-82 Rev. 3 section (`sp800_82r3_reference`) is an author mapping because SP 800-82 Rev. 3 is organized by CSF 1.1 categories. All NERC, PHMSA, HMR, FMCSA, SEC, and state rows carry an **author mapping**.
3. **Evidence.** Interviews with each division's operations, compliance, and security leaders; document review; firewall and PAM configuration exports; the CIP-003-9 evidence binder; control room procedures and training records; the hazmat security plan; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results
### 3.1 Crude Oil Production (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| GOVERN subcategories (31) | 23 | 8 | 0 | 0 |
| IDENTIFY subcategories (21) | 10 | 11 | 0 | 0 |
| PROTECT subcategories (22) | 9 | 13 | 0 | 0 |
| DETECT subcategories (11) | 8 | 3 | 0 | 0 |
| RESPOND subcategories (13) | 10 | 3 | 0 | 0 |
| RECOVER subcategories (8) | 7 | 1 | 0 | 0 |
| **CSF 2.0 subtotal (106)** | **67** | **39** | **0** | **0** |
| EPA SPCC and discharge notice rows (2) | 0 | 2 | 0 | 0 |
| **Total (108)** | **67** | **41** | **0** | **0** |

Of the 41 partially met rows, 10 are rated High, 24 Moderate, and 7 Low. Governance, detection, response, and recovery planning are largely in place because they come from the group program. The gaps concentrate in **PROTECT and IDENTIFY**, at the OT edge: shared paths into the OT DMZ (PR.AA-05, PR.IR-01), field device credentials and change control (PR.AA-03, ID.RA-07), the KEV backlog (ID.RA-01, PR.PS-02), incomplete field device backups (PR.DS-11, RC.RP-03), and the Mid-Continent legacy SCADA (PR.AA-01, DE.CM-06).

### 3.2 Power Generation (`gap-analysis-power-generation.csv`)
| Standard | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| NERC CIP-002-5.1a (6) | 6 | 0 | 0 | 0 |
| NERC CIP-003-9 (17) | 12 | 3 | 1 | 1 |
| NERC EOP-004-4 (2) | 1 | 1 | 0 | 0 |
| NERC CIP-012-2 (2) | 1 | 1 | 0 | 0 |
| NERC CIP-004 to CIP-011 and CIP-013 (1) | 0 | 0 | 0 | 1 |
| NERC CIP-014-3 (1) | 0 | 0 | 0 | 1 |
| DOE-417 (1) | 0 | 0 | 0 | 1 |
| **Total (30)** | **20** | **5** | **1** | **4** |

Of the 6 unmet rows, 1 is High (EG-21, Plant P3 vendor access), 3 are Moderate, and 2 are Low. The program is mature and was audited without findings in 2024; the gaps are the new CIP-003-9 Section 5.2 and 6 obligations, the shared IT/OT paths that Section 3.1 rules now permit (EG-10), and two documentation items (EG-24, EG-27).

### 3.3 Crude Logistics (`gap-analysis-crude-logistics.csv`)
| Rule set | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| PHMSA Part 195 (20) | 11 | 8 | 1 | 0 |
| HMR (10) | 5 | 5 | 0 | 0 |
| FMCSA (2) | 0 | 2 | 0 | 0 |
| TSA (1) | 0 | 0 | 0 | 1 |
| **Total (33)** | **16** | **15** | **1** | **1** |

Of the 16 unmet rows, 1 is High (LG-09, the overdue backup SCADA test), 8 are Moderate, and 7 are Low. **Not met:** 195.446(c)(4). The last backup SCADA test was 2025-04-22, so the 15-month interval ran out on 2026-07-22. The test is scheduled for 2026-10-31. The other gaps share one cause: control room and hazmat programs were written for hydraulic, equipment, and physical threats, and cyber was never added (controller roles and training, change coordination, the security plan risk assessment, and in-depth training).

### 3.4 Group-wide (`gap-analysis-group.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| SEC (Reg S-K Item 106; Form 8-K Item 1.05) (3) | 2 | 1 | 0 | 0 |
| State breach laws (generic plus the Florida worked example) (6) | 1 | 5 | 0 | 0 |
| Applicability screens (USCG, CIRCIA, FAR) (3) | 0 | 0 | 0 | 3 |
| **Total (12)** | **3** | **6** | **0** | **3** |

All 6 unmet group rows are partially met: 3 Moderate and 3 Low. The SEC disclosures are in place, but the materiality process and the state notice process have never been rehearsed for an incident that crosses divisions (scenario gap 7), and royalty owner exports on file shares weaken the reasonable-measures duty (GG-05).

## 4. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Shared IT/OT paths: historian connector and jump servers (1) | All | CSF PR.AA-05, PR.IR-01; CIP-003-9 Att. 1 Sec. 3.1; 195.446(f) | High | Division-only jump servers; one-way read-only historian push | Group OT Security Director; Group data platform director | 2027-03-31 |
| 2 | Mid-Continent legacy SCADA (2) | Production | CSF PR.AA-01, DE.CM-06, PR.DS-11 | High | Integrator access through PAM; logging; offline backups; migration by 2027-09-30 | Production Vice President of Operations Technology | 2026-12-31 (interim) |
| 3 | Plant P3 vendor access and transient cyber asset records (3) | Power Generation | CIP-003-9 R2, Att. 1 Sec. 5.2, 6.3 | High | Self-report; PAM path with OT sensor rules; recorded reviews | CIP Senior Manager | 2026-12-31 |
| 4 | Backup PCC test overdue; training, point-to-point records (4) | Crude Logistics | 195.446(c)(2), (c)(4), (h) | High | Test by 2026-10-31; re-verify points; add SCADA loss and manipulation to training | Pipeline Control Center Manager | 2027-03-31 |
| 5 | Hazmat security plan lacks cyber en route risks; camera AI in discipline (5) | Crude Logistics | 172.802(a), (a)(3); 172.704(a)(5); 49 CFR 390.36 | Moderate | Plan and training update; human review of AI scores | Fleet Safety Director | 2027-03-31 |
| 6 | Crude Logistics inheritance undocumented (6) | Crude Logistics | CSF GV.RR-02; 172.802(b)(2) | Moderate | Inheritance matrix | Crude Logistics security and compliance lead | 2026-12-31 |
| 7 | Notification matrix not exercised (7) | All | 195.52; 40 CFR 110.6; CIP-003-9 Att. 1 Sec. 4.2; Form 8-K Item 1.05; state laws | Moderate | Cross-division tabletop with the disclosure committee | Group General Counsel | 2026-12-15 |
| 8 | Predictive maintenance model without safety review (8) | Production | CSF ID.RA-07, GV.RM-07 | High | Advisory mode; safety management of change; council approval (P10) | Production Vice President of Operations Technology | 2026-12-31 |
| 9 | Crude Logistics supplement drift (9) | Crude Logistics | CSF GV.PO-02 | Moderate | Re-issue supplement | Crude Logistics security and compliance lead | 2026-11-30 |
| 10 | Royalty owner exports on file shares | Production; group | Fla. Stat. 501.171(2); state laws | Moderate | Stop exports; state-of-residence report | Production Accounting Vice President | 2026-12-31 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07). The P07 assessment confirmed several of them (POAM-013 to POAM-018 and POAM-021 cite both sources); POAM-022, POAM-023, and POAM-025 come from this analysis alone.

## 5. Pending regulatory changes
None of these is a current obligation. The `pending_rule_change` column flags affected rows.
- **CIRCIA final rule (N21-R03).** Not published as of 2026-09-25. If finalized as proposed, the group would report covered cyber incidents to CISA within 72 hours and ransom payments within 24 hours.
- **NERC CIP revisions.** Per NERC, the virtualization revisions (including CIP-003-10) are subject to future enforcement on 2028-07-01, CIP-003-11 on 2029-07-01, and CIP-015-1 (internal network security monitoring, high and medium impact only) on 2028-10-01. The Power Generation division reviews each before its date; none changes the low impact categorization.
- **TSA surface cyber risk management rule** (NPRM 2024-11-07; not final). Relevant only if TSA designates the trunk line or a gathering system.
- **Business changes that would change applicability:** a plant or GCC reaching 1,500 MW (medium impact), selling generation to end-use customers (DOE-417 filing), a trunk line becoming interstate (PHMSA rather than state inspection), or any offshore or waterfront acquisition (USCG Subpart F).
