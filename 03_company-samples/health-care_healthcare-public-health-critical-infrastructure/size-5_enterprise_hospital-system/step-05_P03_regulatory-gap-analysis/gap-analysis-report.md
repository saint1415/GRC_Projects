# Regulatory Gap Analysis: Cris Santos Company | Healthcare and Public Health | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded for-profit hospital system: 8 hospitals, 1,970 beds; FL, GA, AL) |
| Tier / Vertical | Enterprise / Healthcare and Public Health |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; Subpart C last amended 2020-11-24 per the eCFR version history checked 2026-10-06), all 69 crosswalk rows |
| Other obligations analyzed | HIPAA Breach Notification Rule; HIPAA Privacy Rule safeguards and the affiliated covered entity designation; SEC Form 8-K Item 1.05 and Reg S-K Item 106; CMS emergency preparedness for hospitals (42 CFR 482.15, cyber-relevant parts and the unified program); medical record services (482.24); EMTALA (489.24) for diversion and transfers; Promoting Interoperability (495.24); Section 1557 (45 CFR 92.210); CLIA (42 CFR 493.1291); 42 CFR Part 2 (2.16); FTC Health Breach Notification Rule (screened out); state breach and data security laws (Florida worked example) |
| Voluntary benchmark | HHS Healthcare and Public Health Cybersecurity Performance Goals (CPGs), in `cpg-benchmark.csv` |
| Assessment dates | 2026-05-04 to 2026-06-26 (evidence sampling completed 2026-07-10) |
| Assessors | GRC team (second line) with the Chief Compliance Officer, the Chief Privacy Officer, and the Vice President, Emergency Management; sampling for 10 rows reperformed by Internal Audit |
| Approved | Chief Compliance Officer and CISO, 2026-08-24; roadmap reviewed by the risk committee of the board, 2026-09-15 |

## 1. Applicability
| Obligation | Applies? | Basis |
|---|---|---|
| HIPAA Security Rule (C-HPH-R01) | **Yes** | Health care providers that transmit health information electronically in standard transactions are covered entities (45 CFR 160.103). The hospitals, freestanding EDs, and physician group are designated as one affiliated covered entity (164.105(b)). No size exemption; 164.306(b) affects how, not whether. The system is also a business associate for the SL-1 affiliate practices |
| HIPAA Breach Notification Rule (C-HPH-R02) | **Yes** | Covered entity (164.404-164.408) and business associate (164.410) |
| HIPAA Privacy Rule | **Yes** | Only safeguard, minimum necessary, and affiliated covered entity provisions are analyzed here |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| CMS emergency preparedness, 42 CFR 482.15 (C-HPH-R07) | **Yes** | Every hospital is Medicare-participating. The system elected a unified and integrated program under 482.15(f), so the (f) elements are analyzed too. Elements with no cyber or information dimension (subsistence, evacuation, sheltering, volunteers, 1135 waivers) stay with the Vice President, Emergency Management. 482.15(g) (transplant hospitals) does not apply: no hospital has a transplant program |
| CMS medical record services, 42 CFR 482.24 | **Yes** | Hospital condition of participation; the record integrity, confidentiality, retention, and authentication elements depend on the ECIS |
| EMTALA, 42 CFR 489.24 | **Yes** | Every hospital has dedicated emergency departments, including the freestanding EDs ("regardless of whether it is located on or off the main hospital campus", 489.24(b)). Governs diversion and transfers during an IT outage. The system owns no ambulances, so only the nonhospital-owned ambulance rule applies |
| Promoting Interoperability, 42 CFR 495.24 | **Yes (payment program)** | All 8 hospitals attest as eligible hospitals. From 2023, hospitals meet the measures CMS selects for each EHR reporting period (495.24(f)(1)(i)(A)); the 2026 minimum score is 80 points (495.24(f)(1)(i)(D)). Confirm the current measure list in the latest IPPS final rule |
| Section 1557, 45 CFR 92.210 | **Yes** | Recipient of federal financial assistance (Medicare, Medicaid) operating a health program |
| CLIA, 42 CFR 493.1291 | **Yes, for the 8 hospital laboratories** | Only the test report provisions that depend on the ECIS are analyzed |
| 42 CFR Part 2 (C-HPH-R06) | **Yes, at H-03** | The behavioral health unit with an addiction medicine service is an "identified unit within a general medical facility" that holds itself out as providing SUD treatment (2.11), federally assisted through Medicare participation (2.12(b)(2)(i)). Other hospitals are lawful holders when they receive Part 2 records. ED care for overdoses is not a Part 2 program by itself (2.12(e)(1)) |
| FTC Health Breach Notification Rule (C-HPH-R05) | **No** | 16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example. The Florida Digital Bill of Rights does not apply: a "controller" under Fla. Stat. 501.702 must have more than $1 billion in global gross annual revenue **and** meet one of three tests (50% or more of revenue from online advertising, a consumer smart speaker and voice command service, or an app store with at least 250,000 applications). The system meets the revenue test but none of the three others |
| FDA FD&C Act sec. 524B (C-HPH-R04) | **Not directly** | Duties fall on device manufacturers; the system uses SBOMs, MDS2 forms, and patch support terms in device procurement |
| HPH CPGs (C-HPH-R08) and 405(d) HICP (C-HPH-R09) | **Voluntary** | Benchmarked in `cpg-benchmark.csv`. HICP's large-organization volume applies to a system of this size |
| HITECH recognized security practices (C-HPH-R10) | **Applies as a mitigating factor** | HHS must consider recognized security practices in place for the previous 12 months (42 U.S.C. 17941). The CSF 2.0-aligned program and the CPG benchmark build that record |
| HIPAA Security Rule NPRM (C-HPH-R03) | **Not in force** | Proposed rule only; tracked in `pending_rule_change` |
| CIRCIA (C-HPH-R11) | **Not in force** | No final rule in the Federal Register as of 2026-10-06. If finalized as proposed, it would cover these hospitals (100 or more beds) |
| SOX Section 404 | Separate program | IT general controls over the ERP and payroll (SYS-09) are tested by the SOX program and not repeated here |

HIPAA exclusions (Not applicable): 164.308(a)(4)(ii)(A), because the system performs no clearinghouse function; 164.314(a)(2)(ii), because there are no arrangements with governmental entities; and 164.314(b) with its four implementation specifications, because the employee health plan is a separate covered entity outside this scope.

## 2. Method
1. **Decompose.** HIPAA Security Rule requirements and their Required and Addressable types come from NIST SP 800-66 Rev. 2 (all 69 rows in the crosswalk in `02_industry-rules/health-care/`). NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis shows the current rule's numbering, 164.308(b)(3). Other obligations were broken into paragraph-level duties from the eCFR text (2026-09-23 versions of 42 CFR 482.15, 482.24, 489.24, 495.24, 493.1291, and 2.16; 45 CFR 92.210, 164.105, and 164.404; 17 CFR 229.106), the SEC's compliance guide for Item 1.05, and the Florida statute text. Summaries are paraphrased; short quotes are marked.
2. **Crosswalk.** HIPAA rows use the Health Care crosswalk (an author mapping for CSF 2.0 and SP 800-53), with NIST's official OLIR mapping to SP 800-53 Rev. 5.1.1 shown beside it. All other rows are author mappings, labeled as such.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and smaller populations used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random or stratified (agency staff, H-08). **55 rows were tested by sampling or full-population analytics; 24 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and has an owner and date. High gaps are in the P01 register and the P07 POA&M.

**Addressable is not optional.** For each addressable specification, the system implements it, implements an equivalent, or documents why neither is reasonable and appropriate (164.306(d)(3)). All addressable gaps below are being implemented. One alternative is documented: HL7 over MLLP inside the segmented data center integration network (164.312(e)(2)(ii); exception EXC-2026-031).

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| HIPAA Security Rule 164.308 | 16 | 13 | 0 | 1 | 30 |
| HIPAA Security Rule 164.310 | 9 | 3 | 0 | 0 | 12 |
| HIPAA Security Rule 164.312 | 6 | 6 | 0 | 0 | 12 |
| HIPAA Security Rule 164.314 | 4 | 0 | 0 | 6 | 10 |
| HIPAA Security Rule 164.316 | 4 | 1 | 0 | 0 | 5 |
| HIPAA Breach Notification Rule (C-HPH-R02) | 9 | 2 | 0 | 0 | 11 |
| HIPAA Privacy Rule | 2 | 1 | 0 | 0 | 3 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| CMS emergency preparedness CoP for hospitals (C-HPH-R07) | 10 | 12 | 0 | 0 | 22 |
| CMS medical record services CoP (42 CFR 482.24) | 2 | 2 | 0 | 0 | 4 |
| EMTALA (42 CFR 489.24) | 1 | 2 | 0 | 0 | 3 |
| Medicare Promoting Interoperability Program (42 CFR 495.24) | 0 | 1 | 0 | 0 | 1 |
| Section 1557 (45 CFR 92.210) | 0 | 3 | 0 | 0 | 3 |
| CLIA (42 CFR 493.1291) | 2 | 1 | 0 | 0 | 3 |
| 42 CFR Part 2 (C-HPH-R06) | 1 | 2 | 0 | 0 | 3 |
| FTC Health Breach Notification Rule (C-HPH-R05) | 0 | 0 | 0 | 1 | 1 |
| State breach and data security laws | 4 | 1 | 0 | 0 | 5 |
| **Total** | **76** | **52** | **0** | **8** | **136** |

**HIPAA Security Rule:** 39 Met, 23 Partially met, 0 Not met, 7 Not applicable (69 rows). Of the 23 partially met rows, 8 are standards, 6 are Required specifications, and 9 are Addressable specifications. No requirement is wholly Not met. The gaps concentrate in H-08, cyber recovery, medical devices, service accounts, and third parties.

**Gap risk levels across all obligations:** High 13, Moderate 27, Low 12.

**The pattern in the hospital rules.** The unified emergency program is mature for hurricanes and mass casualties and almost silent on cyberattacks. The CMS rule does not use the word "cyber," but its all-hazards risk assessment (482.15(a)(1)), its strategies (a)(2), and its medical documentation element (b)(5) are where a multi-hospital EHR outage belongs. EMTALA's diversion definition sets the test the diversion criteria must meet: the hospital "does not have the staff or facilities to accept any additional emergency patients."

**Voluntary CPG self-benchmark (20 goals, `cpg-benchmark.csv`):** Essential 5 Met and 5 Partially met; Enhanced 5 Met and 5 Partially met. None is Not met. The Essential goals still partial (Mitigate Known Vulnerabilities; Strong Encryption; Revoke Credentials for Departing Workforce Members; Unique Credentials; Vendor/Supplier Cybersecurity Requirements) are also HIPAA gaps, so fixing them serves both.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | 164.308(a)(1)(ii)(D) | H-08 legacy EHR, medical device gateways, and building OT are not in the SIEM; H-08 access review is a manual weekly export | SIEM collectors for device gateways and OT; interim H-08 log export to privacy monitoring (POAM-007) | Director of Security Operations | 2026-12-31 |
| G-010 | 164.308(a)(3)(ii)(C) | 4 of 60 sampled departures (all agency or contracted) disabled 2 to 9 days late | Daily reconciliation with the staffing system; agency notice terms with penalties (POAM-002) | Chief Nursing Officer | 2026-12-31 |
| G-019 | 164.308(a)(5)(ii)(D) | 23% of service accounts not vaulted; static integration engine passwords; default passwords on 2 device integration gateways | Vault and rotate service accounts (POAM-001); fix gateways (POAM-010) | Director of Identity and Access Management | 2026-12-31 |
| G-022 | 164.308(a)(7) | Plan does not address a cyber event that reaches both data centers in detail, and does not link to IT-outage diversion criteria beyond H-01 | Update the plan and link it to the diversion criteria (POAM-004) | EHR Technical Director | 2026-12-31 |
| G-024 | 164.308(a)(7)(ii)(B) | Cyber restore exceeds the 24-hour target; no tested fallback for loss of the primary clearinghouse | Isolated recovery environment (POAM-003); clearinghouse surge contract and fallback test (POAM-019) | EHR Technical Director | 2027-03-31 |
| G-048 | 164.312(b) | H-08 EHR, device gateways, and OT logs are not centralized | POAM-007 | Director of Security Operations | 2026-12-31 |
| G-049 | 164.312(c) | No automated reconciliation for misfiled results; emergency build changes without retrospective approval | Reconciliation (POAM-013); change gate (POAM-012) | Vice President, Laboratory Services | 2027-03-31 |
| G-084 | Form 8-K Item 1.05; SEC Release 33-11216 | Quantitative thresholds not updated after the H-08 acquisition; the playbook does not take inputs from hospital incident command (diversion, downtime) | Update thresholds and inputs; joint tabletop 2026-11-18 (POAM-005) | General Counsel | 2026-11-30 |
| G-085 | Form 8-K Item 1.05 (materiality determination) | Escalation timing never tested with hospital incident command; one committee member (COO) joined in 2026 and has not been trained | POAM-005 | General Counsel | 2026-11-30 |
| G-119 | 42 CFR 489.24(b) (definition of "comes to the emergency department"; diversionary status) | Other hospitals have no IT-outage criteria tied to the "staff or facilities" test; no regional coordination rule for several hospitals diverting at once | Adopt the BIA diversion triggers at every hospital with county EMS; coordination through the System Transfer and Command Center (POAM-018) | Vice President, Emergency Management | 2026-12-31 |
| G-122 | 45 CFR 92.210(a) | 4 AI use cases unreviewed; sepsis model version 2 not revalidated locally | Reviews and revalidation (POAM-020; POAM-024) | Chief Medical Information Officer | 2026-12-31 |
| G-124 | 45 CFR 92.210(c) | Sepsis model subgroup gaps found in P10; mitigation not yet at all hospitals | Universal screening at all hospitals; threshold decision (POAM-020) | Chief Medical Information Officer | 2026-12-31 |
| G-125 | 42 CFR 493.1291(a) | No automated reconciliation between analyzer, middleware, and EHR results | Daily reconciliation (POAM-013) | Vice President, Laboratory Services | 2027-03-31 |

**One exercise, several rules.** The 2026-11-18 multi-hospital ransomware and downtime exercise (POAM-004) is designed to count as the additional annual exercise under 482.15(d)(2)(ii), test the contingency plan under 164.308(a)(7)(ii)(D), test EMTALA-compliant diversion and paper transfers (489.24(b), (e)(2)(iii)), and rehearse the SEC materiality step with the disclosure committee (Item 1.05). The after-action report is filed in the emergency program binder (482.15(d)(2)(iii)) and the GRC evidence binder.

## 5. Compliance roadmap
| Quarter | Milestones | Obligations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Multi-hospital exercise with the disclosure committee (POAM-004, POAM-005); diversion criteria at every hospital and cyber hazards in the unified plan (POAM-018); service account vaulting (POAM-001); agency reconciliation (POAM-002); device gateway passwords (POAM-010); H-08 EDR and encryption (POAM-022); Part 2 flagging and procedures (POAM-021); sepsis model revalidation and 92.210 inventory (POAM-020); AI reviews (POAM-024); affiliate account cleanup (POAM-015) | 164.308(a)(3)(ii)(C), (a)(5)(ii)(D), (a)(7), 164.312(a)(2)(iv); 482.15(a)(1)-(3), (d)(2); 489.24(b); Item 1.05; 92.210; 2.16(a) | After-action report; updated unified plan; vault reports; Part 2 procedures; revalidation report |
| 2027 Q1 | Isolated recovery environment and 24-hour restore test (POAM-003); clearinghouse surge contract and fallback test (POAM-019); result reconciliation (POAM-013); SIEM collectors for devices and OT (POAM-007); device discovery at all hospitals (POAM-008); vendor reassessments cleared (POAM-014); H-08 conversion (2027-03-01) | 164.308(a)(7)(ii)(B), (a)(1)(ii)(D), 164.312(b), (c); 493.1291(a); 482.15(b)(5); 482.24(b) | Restore test report; reconciliation reports; SIEM source list; vendor register |
| 2027 Q2 | Unsupported device deviations and replacements (POAM-009); NAC at H-06 to H-08 (POAM-023); downtime training to 95% (POAM-016) | 164.308(a)(1)(ii)(B), (a)(7)(ii)(C); 482.15(d)(1) | Deviation records; NAC coverage; training reports |
| 2027 Q2 to Q3 | Annual risk analysis and gap reassessment; review NPRM and CIRCIA status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**; the regulatory agenda projects a final rule in July 2027. 35 HIPAA rows carry a note in `pending_rule_change`. If finalized as proposed, the verified proposals that matter most here are: removal of the addressable designation; encryption of all ePHI at rest and in transit with limited exceptions (H-08 endpoints and the MLLP segment); MFA; a written technology asset inventory and network map (medical devices); penetration testing at least every 12 months and vulnerability scanning; restoring certain systems within 72 hours (the vault restore and H-08); a compliance audit at least every 12 months; and business associate notice within 24 hours of activating a contingency plan. None of these is treated as a current obligation.
- **CIRCIA** (proposed 6 CFR Part 226): no final rule as of 2026-10-06. The proposal would cover hospitals with 100 or more beds, which includes all 8 hospitals, and would add a 72-hour incident report and a 24-hour ransom payment report to CISA. Tracked in the P08 matrix only.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 or Item 106 was found; both remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the system can respond quickly to an OCR data request, a CMS or state survey (including an EMTALA complaint survey), an accrediting organization survey, a CLIA inspection, or an SEC comment letter:
- this report, `gap-analysis.csv`, `cpg-benchmark.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the unified emergency plan, facility risk assessments, training records, and after-action reports;
- diversion logs and EMS notifications;
- the affiliated covered entity designation and Security Officer designation;
- breach logs and notification files;
- 92.210 inventory and mitigation records (from P10);
- documentation retained 6 years (164.316(b)(2)(i)).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-24. The roadmap was reviewed by the risk committee of the board on 2026-09-15. Next reassessment: 2027-05 to 2027-06.
