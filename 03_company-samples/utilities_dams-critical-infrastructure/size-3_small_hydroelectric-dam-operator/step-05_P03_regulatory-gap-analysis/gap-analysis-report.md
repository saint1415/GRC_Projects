# Regulatory Gap Analysis: Cris Santos Company | Dams | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project, Florida) |
| Tier / Vertical | Small / Dams |
| Primary program analyzed | FERC Division of Dam Safety and Inspections, *FERC Security Program for Hydropower Projects*, Revision 3A (March 30, 2016), as applied to a **Security Group 2** dam. Source: https://www.ferc.gov/sites/default/files/2020-04/security.pdf (fetched 2026-09-26) |
| Secondary regulation | 18 CFR Part 12, Safety of Water Power Projects and Project Works: incident reporting (12.10) and the related security, records, EAP, gate, and Owner's Dam Safety Program duties (eCFR version 2026-09-23) |
| Also checked | NERC CIP applicability (BES definition, Inclusion I2) |
| Assessment dates | 2026-07-13 to 2026-07-24 (Section 9 determination on 2026-07-16) |
| Assessors | Compliance and Security Coordinator and Controls Engineer, with the Chief Dam Safety Engineer and IT Manager |

## 1. Applicability
**The FERC Security Program applies.** The company is a FERC licensee, and 18 CFR Part 12 applies to any project licensed under Part I of the Federal Power Act (12.1(a)(1)). The Security Program is D2SI guidance that FERC engineers inspect against during dam safety inspections (Rev. 3A sections 2.0 and 3.0), under the Regional Engineer's supervisory authority over project "safety, stability, security, and integrity" (18 CFR 12.4(b)(1)(i)). Failure to comply with an order or directive under Part 12 can lead to civil penalties, orders to cease generation, or license revocation (12.4(d)).

**Size does not matter; the Security Group does.** The program has no employee or revenue threshold. Duties depend on the dam's Security Group, which FERC assigns from consequence, vulnerability, and likelihood of attack (the DAMSVR method). The criteria are not public (Rev. 3A 3.3.1 to 3.3.3). FERC placed this dam in **Security Group 2** (January 2010 regrouping letter to the prior licensee, confirmed at the 2025-10-21 inspection). Table 3.3.8 gives Group 2 these duties:

| Duty (Table 3.3.8) | Group 2 | This project |
|---|---|---|
| Security Assessment (annual update, reprint at least every 10 years) | Required | Rows G-011, G-021 to G-023 |
| Vulnerability Assessment | Not required (unless a permanent facility closure is requested) | G-016: Not applicable |
| Security Plan (annual update) with the Internal Emergency Response sub-element | Required | G-012, G-013, G-024 to G-030 |
| Rapid Recovery sub-element | Group 1 only | G-015: Not applicable |
| Security Plan exercise | Strongly recommended | G-014 |
| Annual Security Compliance Certification Letter by December 31 | Required | G-017, G-031 to G-034 |

**Section 9 (Computer Security and SCADA) applies, and at the Critical level.** Every Group 1 and 2 dam must answer Form 3 Questions 1-4 (Rev. 3A 9.1.1). The answers on 2026-07-16 were Yes to remote data acquisition, remote generation control, and remote control of water retention features (the 2024 after-hours remote operation), and No to interconnection with other dams. The consequence test in Table 9.1c then showed:
- **Gate control:** an uncontrolled gate opening would affect more than 60 people within 3 miles of the dam (the EAP inundation maps show the downstream town of about 2,400 residents). That exceeds the Table 9.1c threshold, so gate control is a **Critical** cyber asset.
- **Generation:** the powerhouse is 30 MW, under the 100 MW line, so loss of generation alone would be Non-critical (Table 9.1c note 3), and the units have no black start capability (note 4).
- **One network:** the dam and powerhouse share one control LAN. FERC's FAQ (Question 1) says the consequence for a shared network comes from the higher of the two assets. The whole PCDMS is therefore treated as Critical, which requires **baseline and enhanced measures** (Tables 9.3a and 9.3b), answers to Form 3 Questions 5-33, and a plan and schedule for each negative answer (9.1.1.3).

**NERC CIP does not apply.** Under NERC's Bulk Electric System definition, a generating resource is included under I2 only when connected at 100 kV or above and rated over 20 MVA per unit or 75 MVA per plant (NERC BES Definition Reference Document, version 3, April 30, 2026). The three units are about 11 MVA each (about 33 MVA total), connected at 69 kV, and none is a blackstart resource. The company is not NERC-registered, so the Section 9 note about assets that fall under both FERC D2SI and NERC CIP (Rev. 3A 9.4) does not arise.

**Which revision.** Revision 3A is the latest version this analysis could confirm on ferc.gov (the PDF, the Revision 3/3A change notice, and the FAQ were all retrieved on 2026-09-26). The FERC program web page refused automated access (HTTP 403), so a newer revision could not be ruled out. **Action:** the Compliance and Security Coordinator will confirm the current revision with the Regional Engineer before the 2026-11-17 inspection.

**Secondary regulation.** 18 CFR 12.10 is the most relevant binding rule for this work. A "condition affecting the safety of a project" expressly includes misoperation of a gate (12.3(b)(4)(ii)), unusual instrumentation readings ((viii)), and "security incidents (physical and/or cyber)" ((xi)). So a cyber event on the gate or unit controls must be reported to the Regional Engineer as soon as practicable, preferably within 72 hours (12.10(a)(1)). That clock drives the P08 runbook.

## 2. Method
1. **Requirements.** Rows follow the program's own structure: section 3.2 licensee responsibilities, the Group 2 duties in 3.3.2 and Table 3.3.8, sections 4, 6, 7, and 8, each line of the Section 9 baseline and enhanced measures (Tables 9.3a and 9.3b), the Form 3 questions not already covered by those lines, and three Form 1 physical checklist items. Items for Group 1 only are listed as Not applicable so the reader can see the line. Part 12 rows cite section and paragraph. FERC documents are U.S. government works; short phrases are quoted where the wording matters.
2. **Crosswalk.** Each row maps to CSF 2.0 subcategories and SP 800-53 Rev. 5 controls. **This is an author mapping.** NIST has not published a mapping for the FERC program. The program's own Table 9.3a and 9.3b cite NIST SP 800-82 sections; the mapping here uses SP 800-82 Rev. 3 (the current OT guide) and its SP 800-53 overlay as the bridge.
3. **Evidence.** Interviews (Vice President of Operations, Plant Manager, Chief Dam Safety Engineer, Operations Supervisors, Controls Engineer, IT Manager, Compliance and Security Coordinator), review of the 2017 Security Assessment, the 2022 Security Plan, the 2019-2025 certification letters, the EAP and Owner's Dam Safety Program, the OT firewall rule export, the HMI user list, and a site walkthrough on 2026-08-05.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Sec. 3 Requirements and responsibilities | 4 | 9 | 2 | 2 | 17 |
| Sec. 4 Threat notification and communications | 2 | 1 | 0 | 0 | 3 |
| Sec. 6 Security Assessment | 0 | 2 | 1 | 0 | 3 |
| Sec. 7 Security Plan | 2 | 4 | 1 | 0 | 7 |
| Sec. 8 Annual certification letter | 1 | 1 | 2 | 0 | 4 |
| Sec. 9 and Form 3 Computer security and SCADA | 2 | 13 | 17 | 0 | 32 |
| Appendix A Form 1 (physical checklist) | 0 | 2 | 1 | 0 | 3 |
| 18 CFR Part 12 (secondary) | 5 | 2 | 0 | 0 | 7 |
| NERC CIP (applicability) | 0 | 0 | 0 | 1 | 1 |
| **Total** | **16** | **34** | **24** | **3** | **77** |

Of the 58 unmet or partially met rows, 1 is rated Very High, 21 High, 26 Moderate, and 10 Low.

**The pattern.** The physical security program is mostly sound: key control, law enforcement contacts, threat-level procedures, and the Part 12 reporting, EAP, and gate testing duties are met. The failures cluster in two places:
- **Cyber (Section 9):** 30 of the 32 Section 9 and Form 3 rows are unmet or partially met. The program was never extended to the control system, even after remote operation was added in 2024.
- **Paperwork FERC relies on:** the Security Assessment and Security Plan were not updated for three years, yet the certification letters said they were current. That is the most sensitive finding, because it concerns statements made to the regulator.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Remote and vendor access uncontrolled (password-only OT VPN, shared HMI account, always-on vendor links) | 9.3a access control; Form 3 Q12 | Very High | Jump host with MFA, named accounts, on-demand vendor sessions, weekly log review | Controls Engineer | 2026-12-31 (MFA and view-only after hours by 2026-11-30) |
| Certification letters overstated compliance; Section 9 never addressed | 8.0 | High | Corrected statement plus plan and schedule to the Regional Engineer | Vice President of Operations | 2026-09-30 |
| No Cyber/SCADA Security Plan; Security Plan and Security Assessment not updated since 2022 | 3.3.2; 6.4; 7.2; 7.5 | High | Updates plus a Cyber/SCADA annex built from the P02 SSP | Compliance and Security Coordinator; Controls Engineer | 2026-11-15 |
| IT/OT segregation bypassed by the dual-homed engineering workstation | 9.3a segregation; Form 3 Q11 | High | Remove the corporate interface; allow-list firewall rules | Controls Engineer | 2026-10-31 |
| Cyber events not named as 18 CFR 12.10 conditions; no link from cyber event to the EAP | 12.10(a); 7.4.1 | High | Update the ODSP, POL-03, and the Internal Emergency Response sub-element; P08 runbook | Chief Dam Safety Engineer | 2026-10-31 |
| No OT asset inventory or criticality record | 9.2 | High | Inventory with criticality | Controls Engineer | 2026-12-31 |
| OT backups untested and not isolated | 9.3a restoration | High | Offline and cloud copies; annual restore test | Controls Engineer | 2026-12-31 |
| No OT monitoring, vulnerability assessment, or patching | 9.3a intrusion detection; 9.3b vulnerability assessment; Form 3 Q14, Q15 | High | Log forwarding and passive monitoring; outside assessment; SCADA upgrade | Controls Engineer | 2027-02-28 to 2027-06-30 |
| CEII open to all staff | Form 1 Q22; 3.2 OPSEC; 18 CFR 388.113 | Moderate | Restricted CEII library and marking | IT Manager | 2026-10-31 |
| Default passwords on gate panels and gauge modems | Form 1 Q6, Q9; 9.3b access control | Moderate | Change now; private APN | Controls Engineer; Chief Dam Safety Engineer | 2026-09-30 and 2026-10-15 |

The full list, with evidence, is in `gap-analysis.csv`. High and Very High gaps are carried into the risk register (P01) and the POA&M (P07). The plan and schedule that Section 9.1.1.3 asks for is the P07 POA&M, filtered to the Section 9 rows.

## 5. Pending regulatory changes
- **FERC Security Program:** no newer revision confirmed (see section 1). Recheck with the Regional Engineer before each inspection.
- **CIRCIA** (6 U.S.C. 681b; proposed 6 CFR Part 226): the final rule has not been published as of 2026-09-25, so reporting to CISA is voluntary. The proposed rule has no dams-specific criterion, and the company is below the SBA size standard used in the proposed scope, so it would likely be outside the rule if finalized as proposed. Recheck when the final rule appears.
- **NERC CIP:** the approved future revisions (virtualization changes effective 2028-07-01, CIP-015 in 2028 and 2029) do not change BES inclusion, so they would not reach this plant unless its units, capacity, or interconnection voltage change.

The `pending_rule_change` column in `gap-analysis.csv` records this per row. None of these is treated as a current obligation.
