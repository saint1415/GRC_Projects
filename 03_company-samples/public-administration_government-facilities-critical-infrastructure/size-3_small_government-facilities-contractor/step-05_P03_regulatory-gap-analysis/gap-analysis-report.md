# Regulatory Gap Analysis: Cris Santos Company | Government Services and Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings, NAICS 561210) |
| Tier / Vertical | Small / Government Services and Facilities |
| Primary standard | NIST SP 800-53 Rev. 5, Release 5.2.0 (Aug 27, 2025), **Moderate baseline** from SP 800-53B: 177 base controls with 110 enhancements. **Binding by contract** for the state contract scope; **benchmark** for the rest of the FOTP. OT tailoring from NIST SP 800-82 Rev. 3 (September 2023) |
| Secondary requirements | FAR 52.204-21 (NOV 2021), the 15 basic safeguarding requirements plus the subcontract flow-down; FAR 52.204-23, 52.204-25, 52.204-30, and 52.204-9 for the federal contract. Clause text read from eCFR (point-in-time 2026-09-23) |
| System | Facility Operations Technology Platform (FOTP), per the SSP (P02) |
| Assessment dates | Fieldwork 2026-07-13 to 2026-07-24 (site walkthroughs 2026-07-15 to 2026-07-17). Statuses reflect 2026-08-31, after the P06 policies were approved and the P07 results were in |
| Assessor | IT Manager (Information Security Officer), with the Contracts Manager, Controls Engineering Manager, and Security Systems Supervisor |

## 1. Applicability
The vertical profile names SP 800-53 Rev. 5 as the primary control set because FISMA, IRS Pub. 1075, CJIS, and GovRAMP are all built on it. **But SP 800-53 is a catalog, not a law. It binds a private contractor only through a contract or a federal system authorization.** So the first step was to sort out which customer rules reach this company, and how.

### 1.1 Who the customers are
| Contract | Customer | What the company operates | How security terms reach the company |
|---|---|---|---|
| CT-F | GSA Public Buildings Service (one federal office building) | GSA's BAS on the GSA Building Systems Network (BSN), through GSA's virtual desktop with PIV cards | FAR clauses; the statement of work incorporates the GSA Building Technologies Technical Reference Guide (BTTRG) Version 3.0, dated May 1, 2024 (title and version verified on gsa.gov, IT Security Procedural Guides page, 2026-09-26), and GSA IT Security Policy CIO 2100.1 |
| CT-S | State agency (regional office complex) | The company's own BAS supervisory platform and the agency's access control tenant | Contract cybersecurity exhibit requiring SP 800-53 Rev. 5 Moderate controls. Florida requires state agency IT service contracts to meet state and federal standards including NIST CSF and to assign security responsibilities (Fla. Stat. 282.318(4)(h)) |
| CT-C | County (government center and 4 service centers) | Same platform as CT-S | Security addendum requiring compliance with the county's cybersecurity standards, which the county must adopt consistent with NIST CSF (Fla. Stat. 282.3185(4)(a)) |

### 1.2 Decisions, requirement by requirement
| ID | Requirement | Applies to the company? | Reason |
|---|---|---|---|
| C-GOVERNMENT-R01 | FISMA (44 U.S.C. 3551-3558) | **Indirectly, for CT-F only** | FISMA makes each agency responsible for information systems "used or operated by an agency or by a contractor of an agency" (44 U.S.C. 3554(a)(1)(A)(ii)). The BAS servers on GSA's BSN hold a GSA FISMA Moderate ATO (BTTRG section 1.0), and GSA IT runs their scanning, logging, and POA&M. The company operates them as a contractor, so it must follow GSA policies (BTTRG 1.1: "The vendor/contractor is responsible for adhering to GSA IT policies"), but the ATO and the SP 800-53 control set belong to GSA. **No company-owned system operates on GSA's behalf.** Under 32 CFR 2002.14(h)(2), a contractor system that receives federal information only incidental to providing a service is a non-federal system |
| C-GOVERNMENT-R02 | IRS Pub. 1075 | No | No FTI. The state contract states the company has no access to FTI areas or systems |
| C-GOVERNMENT-R03 | CJIS Security Policy v6.1 | No | The county contract excludes the sheriff's office and jail. Recheck if the scope changes |
| C-GOVERNMENT-R04 | VVSG 2.0 | No | No election systems |
| C-GOVERNMENT-R05 | FERPA | No | No education facilities |
| C-GOVERNMENT-R06 | CIRCIA | Not in force | Proposed rule only (89 FR 23644). Its proposed government facilities criteria target state, local, tribal, and territorial government entities, not their contractors, and the company is below its SBA size standard. Tracked in section 5 |
| C-GOVERNMENT-R07 | SLCGP (6 U.S.C. 665g) | No | A grant condition for governments |
| C-GOVERNMENT-R08 | GovRAMP | Not to the company | GovRAMP verifies cloud providers. The company is not one. It matters for the access control SaaS vendor (reviewed in P09) |

**What binds the company, and at what size.** None of these rules has a size exemption. The SBA-small status changes nothing: the FAR clauses apply to every contractor that signs them, and the state exhibit applies regardless of headcount.

- **SP 800-53 Rev. 5 Moderate: binding by contract** for systems that store or process state agency data (the BAS supervisory platform, the state access control tenant, the jump host, the cloud tenant). **Benchmark** for the county scope. The county standards are CSF-based, and using one control set for both is simpler than keeping two.
- **FAR 52.204-21: binding** for any company system that processes, stores, or transmits federal contract information: the CMMS (GSA work orders), email, file storage, and laptops.
- **CUI.** GSA marks sensitive building drawings as CUI (Physical Security category) under GSA Order PBS 3490.3 CHGE 1, which requires holders to protect them under 32 CFR Part 2002. The CT-F statement of work carries this requirement. The contract does not cite NIST SP 800-171, so the company handles CUI under the 800-53 media and access controls (MP-2 to MP-5, AC-3, AC-21, SC-8). **Watch item:** if GSA adds a CUI clause citing SP 800-171, a separate assessment is needed.
- **Supply chain clauses (52.204-23, -25, -30): binding**, with short reporting clocks (section 4).

### 1.3 OT tailoring
The controls were applied to OT components (BACnet controllers, door controllers, edge firewalls, engineering workstations) using the OT guidance in NIST SP 800-82 Rev. 3. Examples: vulnerability scanning of OT uses passive discovery and approved windows, not live active scans (RA-5). Where BACnet cannot encrypt, segmentation compensates (SC-8, SC-7). No control was tailored out. Three developer controls (SA-10, SA-11, SA-15) were assessed against the company's vendors, because the company develops no software.

## 2. Method
1. **Requirements.** One row per Moderate base control (rows G-001 to G-177), with its Moderate enhancements listed in the citation column; 20 FAR rows (G-178 to G-197) cited to clause paragraph.
2. **Crosswalk.**
   - 134 control rows use NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`).
   - The other 43 control rows, and all FAR rows, are author mappings, labeled as such. FAR rows map to SP 800-53 through the SP 800-171 Rev. 2 lineage of the 15 requirements.
3. **Evidence.** Interviews, configuration exports (identity provider, cloud IAM, edge firewalls, access control administrator lists), CMMS asset lists, contracts and purchase records, the three site walkthroughs, and the P07 tests.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

The same statements appear in the SSP control table (P02), so the two documents do not drift apart.

## 3. Results summary
### 3.1 SP 800-53 Rev. 5 Moderate baseline (177 base controls)
| Family | Met | Partially met | Not met |
|---|---|---|---|
| AC Access Control | 3 | 11 | 3 |
| AT Awareness and Training | 0 | 3 | 1 |
| AU Audit and Accountability | 1 | 7 | 3 |
| CA Assessment, Authorization, and Monitoring | 2 | 4 | 1 |
| CM Configuration Management | 1 | 7 | 4 |
| CP Contingency Planning | 0 | 3 | 6 |
| IA Identification and Authentication | 3 | 6 | 1 |
| IR Incident Response | 2 | 3 | 3 |
| MA Maintenance | 0 | 5 | 1 |
| MP Media Protection | 1 | 4 | 2 |
| PE Physical and Environmental Protection | 8 | 7 | 1 |
| PL Planning | 3 | 2 | 1 |
| PS Personnel Security | 1 | 6 | 2 |
| RA Risk Assessment | 5 | 0 | 1 |
| SA System and Services Acquisition | 2 | 9 | 0 |
| SC System and Communications Protection | 12 | 6 | 0 |
| SI System and Information Integrity | 4 | 6 | 1 |
| SR Supply Chain Risk Management | 0 | 4 | 5 |
| **Total (177)** | **48** | **93** | **36** |

Most "Met" rows are inherited from the cloud provider, the SaaS vendors, or the office landlord (PE, SC). The weak families are the ones that matter most for operating OT remotely: contingency planning, supply chain, audit, and configuration management.

### 3.2 FAR clauses (20 rows)
| Clause | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 52.204-21(b)(1) (15 requirements) | 6 | 7 | 1 | 1 |
| 52.204-21(c) flow-down | 0 | 0 | 1 | 0 |
| 52.204-23, -25, -30, 52.204-9 | 1 | 1 | 2 | 0 |
| **Total (20)** | **7** | **8** | **4** | **1** |

The **N/A** row is 52.204-21(b)(1)(xi) (subnetworks for publicly accessible components); the company hosts none.

### 3.3 Gap risk (Partially met and Not met rows, 141 in total)
| Gap risk | Rows |
|---|---|
| Very High | 2 |
| High | 12 |
| Moderate | 55 |
| Low | 66 |
| Very Low | 6 |

## 4. Priority gaps and roadmap
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Uncontrolled remote access to OT (integrator tool, jump host bypassed) | AC-17; MA-4 | Very High | Remove the tool; jump host with MFA, approval, and recording | IT Manager | 2026-10-15 |
| Possible covered video equipment; no supplier screening | FAR 52.204-25(b)(2), (d); SR-3 | High | Confirm by 2026-09-30; report within 1 business day if covered; replace by 2026-10-31 | Contracts Manager | 2026-10-31 |
| Default and shared credentials on OT | IA-2; IA-5 | High | Change defaults; named accounts; password vault | Controls Engineering Manager | 2026-10-15 |
| No OT segmentation at county service centers | SC-7 | High | OT VLANs, deny-by-default | IT/OT Systems Administrator | 2027-01-31 |
| Edge firmware behind; no vulnerability scanning | SI-2; RA-5 | High | Update firmware; monthly scans; passive OT discovery | IT/OT Systems Administrator | 2026-11-30 |
| Backups exposed; no alternate storage; no contingency plan or tests | CP-2; CP-4; CP-6; CP-9 | High | Immutable separate-account backups; manual-mode procedures per building; quarterly restore tests | IT Manager / Director of Operations | 2026-12-31 |
| No monitoring of OT, remote sessions, or admin actions | SI-4; AU-6 | High / Moderate | Log workspace, weekly review, alerts | IT Manager | 2027-01-31 |
| CUI drawings not controlled | MP-3; MP-4; AC-21; SC-8 | Moderate | Restricted CUI library; marking; encrypted transfer; training | Contracts Manager | 2026-11-30 |
| No subcontractor flow-downs or security terms | FAR 52.204-21(c); SA-9; PS-7 | Moderate | Subcontractor security addendum | Contracts Manager | 2026-12-31 |
| Late deprovisioning; PIV card not returned | AC-2; PS-4; FAR 52.204-9(b) | Moderate | Termination checklist with same-day disable and PIV return | HR Manager | 2026-09-30 |

**Reporting clocks in the supply chain clauses (verified in eCFR):**
- 52.204-25(d): report covered telecommunications or video surveillance equipment within **one business day** of identification, with further information within 10 business days.
- 52.204-23(c): report Kaspersky covered articles within **3 business days**.
- 52.204-30(c): check SAM.gov for FASCSA orders at least once every three months and report within **3 business days**.

High and Moderate gaps feed the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **FAR overhaul (RFO).** The proposed rule (FR Doc. 2026-12559, June 23, 2026) would move information security clauses into a new FAR part 40, renumber 52.204-21 as 52.240-5, and add CUI clauses requiring NIST SP 800-171 Rev. 3. **Proposed only**; comments closed 2026-07-23. Flagged in the `pending_rule_change` column of the FAR rows.
- **NIST SP 800-82 Rev. 4.** Initial public draft published 2026-09-21 (comments due 2026-11-30). It restructures the guide around CSF 2.0 and adds building automation systems. **Draft only.** Rev. 3 remains the OT reference here. Flagged on the OT rows (AC-17, CM-6, CM-8, CP-2, RA-5, SC-7, SI-4).
- **CIRCIA.** No final rule as of 2026-09-25. Reporting is voluntary.
