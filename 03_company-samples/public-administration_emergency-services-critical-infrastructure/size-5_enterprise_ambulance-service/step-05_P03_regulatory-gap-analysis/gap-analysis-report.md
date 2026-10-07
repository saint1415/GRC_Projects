# Regulatory Gap Analysis: Cris Santos Company | Emergency Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider with a managed transportation division and EMS billing services; FL, GA, AL, SC, TN) |
| Tier / Vertical | Enterprise / Emergency Services |
| Regulations analyzed | HIPAA Security Rule (all 69 crosswalk rows; C-EMERGENCY-R04); HIPAA Breach Notification Rule; selected HIPAA Privacy Rule safeguards; SEC Form 8-K Item 1.05 and Reg S-K Item 106; Medicare ambulance documentation rules; state EMS records rules (Florida worked example); state call recording laws (Florida worked example); state breach and data security laws (Florida worked example); Section 1557 (45 CFR 92.210); applicability decisions for the CJIS Security Policy, 28 CFR 20.21 and Part 23, the FCC EAS rules, 42 CFR Part 2, and the FTC Health Breach Notification Rule |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
The Emergency Services sector research was written mostly for public agencies and 911 centers. A private ambulance company is a different kind of entity, so applicability was decided first for every requirement in the vertical registry.

| Regulation | Applies? | Basis |
|---|---|---|
| HIPAA Security Rule (C-EMERGENCY-R04) | **Yes** | A health care provider that transmits health information electronically in standard transactions is a covered entity (45 CFR 160.103). The company bills Medicare, Medicaid in 5 states, and commercial plans electronically. It is also a business associate for SL-1 (46 public EMS agencies) and SL-2 (3 state Medicaid programs and 6 managed care plans). No size exemption; 164.306(b) affects how, not whether |
| HIPAA Breach Notification Rule | **Yes** | Covered entity (164.404-164.408) and business associate (164.410) |
| HIPAA Privacy Rule | **Yes** | Covered entity; only safeguard-related provisions are in scope here |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| Medicare ambulance rules | **Yes** | Medicare Part B ambulance supplier: certification statements (42 CFR 410.40(e)), billing and reporting (410.41(c)), and 7-year documentation retention (424.516(f)) |
| State EMS records rules | **Yes, in all 5 states** | Each state's EMS licensing rules. Florida worked example: Fla. Stat. 401.30 and Rule 64J-1.014, F.A.C. |
| State call recording laws | **Yes** | The company records dispatch and contact center calls. Florida worked example: Fla. Stat. 934.03(2)(g) lets employees of a licensed ambulance service record incoming calls, with limits for 911 and published nonemergency numbers |
| 45 CFR 92.210 (Section 1557) | **Yes** | The company receives federal financial assistance (Medicaid) and operates health programs. The dispatch protocol software and AI call triage support clinical decisions, so they are patient care decision support tools under 45 CFR 92.4 |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside; Florida (Fla. Stat. 501.171) is the worked example |
| FBI CJIS Security Policy (C-EMERGENCY-R01) | **No** | The policy governs access to criminal justice information. The company has no access to state or national criminal justice databases or law enforcement records systems. The CAD-to-CAD hub drops law enforcement fields by design, and the 3 counties that share premise hazard notes confirmed in writing in 2026 that the notes contain none. Under 28 CFR 20.33(a)(7), a private contractor receives criminal history record information only under an agreement with a criminal justice agency for the administration of criminal justice, with an approved security addendum; ambulance service is not that. **Trigger to recheck:** any county request to show law enforcement data in CAD (P01 R-039) |
| 28 CFR 20.21(f) and Part 23 (C-EMERGENCY-R02, R03) | **No** | These apply to state criminal history systems and to federally funded criminal intelligence systems. The company operates neither |
| FCC EAS rules (C-EMERGENCY-R06) | **No** | The company is not an EAS participant and does not originate public alerts |
| CIRCIA (C-EMERGENCY-R05) | **Not in force** | Proposed only (89 FR 23644); no final rule as of 2026-09-25. As proposed, the company would be covered twice over: it is above the SBA size standard in a critical infrastructure sector, and proposed 226.2(b)(5) reaches entities that provide emergency medical services to a population of 50,000 or more. Tracked in P08 |
| HIPAA Security Rule NPRM | **Not in force** | Proposed rule only; tracked in the `pending_rule_change` column |
| 42 CFR Part 2 | **No** | Not a federally assisted substance use disorder program, and ambulance and NEMT operations do not request or receive Part 2 records |
| FTC HBNR | **No** | 16 CFR 318.1 excludes HIPAA covered entities and business associates acting as such |
| SOX Section 404 | Separate program | IT general controls over ERP and payroll (SYS-10) are tested by the SOX program and not repeated here |

HIPAA exclusions (Not applicable, 7 rows): 164.308(a)(4)(ii)(A), because the company performs no clearinghouse function; 164.314(a)(2)(ii), because the company is not a governmental entity (its public agency clients use BAAs); and 164.314(b) with its four implementation specifications, because the employee health plan is a separate covered entity handled by the benefits program.

## 2. Method
1. **Decompose.** HIPAA Security Rule requirements and their Required and Addressable types come from NIST SP 800-66 Rev. 2 (all 69 rows in the Health Care crosswalk). Other regulations were broken into citation-level duties from the eCFR text (45 CFR 164.402-164.414, 42 CFR 410.40-410.41, 424.516, 45 CFR 92.210, and 17 CFR 229.106), the SEC's compliance guide for Item 1.05, and the Florida statute and rule text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. HIPAA rows use the Health Care crosswalk (an author mapping, because NIST's official mapping is not yet published for CSF 2.0), with NIST's official SP 800-53 mapping shown in the `nist_official_sp800_53r5_1_1` column. Other rows are author mappings and are labeled that way.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and smaller populations used 25 to 40 items; configuration and account data were checked in full with analytics. Samples that included the acquired operations were stratified so AQ-01 and AQ-02 got their own items. Selections were random. **33 rows were tested by sampling or full-population analytics; 18 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**Addressable is not optional.** For each addressable specification, the company implements it, implements an equivalent, or documents why neither is reasonable and appropriate (164.306(d)(3)). One equivalent is documented: dispatch consoles do not auto-lock (164.312(a)(2)(iii)) because dispatchers must see live calls, so the badge-controlled dispatch floor is the equivalent measure (exception EXC-2026-008). All other addressable gaps below are being implemented.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| HIPAA Security Rule 164.308 | 14 | 15 | 0 | 1 | 30 |
| HIPAA Security Rule 164.310 | 10 | 2 | 0 | 0 | 12 |
| HIPAA Security Rule 164.312 | 6 | 6 | 0 | 0 | 12 |
| HIPAA Security Rule 164.314 | 3 | 1 | 0 | 6 | 10 |
| HIPAA Security Rule 164.316 | 5 | 0 | 0 | 0 | 5 |
| HIPAA Breach Notification Rule | 9 | 2 | 0 | 0 | 11 |
| HIPAA Privacy Rule | 1 | 1 | 0 | 0 | 2 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| Medicare ambulance rules | 2 | 1 | 0 | 0 | 3 |
| State EMS records rules (generic plus Florida worked example) | 6 | 0 | 0 | 0 | 6 |
| State call recording laws | 1 | 1 | 0 | 0 | 2 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| Section 1557 (45 CFR 92.210) | 0 | 3 | 0 | 0 | 3 |
| Registry and other rules found not applicable (CJIS, 28 CFR 20.21, 28 CFR Part 23, FCC EAS, 42 CFR Part 2, FTC HBNR) | 0 | 0 | 0 | 6 | 6 |
| **Total** | **66** | **35** | **0** | **13** | **114** |

**HIPAA Security Rule:** 38 Met, 24 Partially met, 0 Not met, 7 Not applicable (69 rows). Of the 24 partially met rows, 8 are standards, 8 are Required specifications, and 8 are Addressable specifications. No requirement is wholly Not met; the gaps are concentrated in the acquired operation (AQ-01), dispatch recovery time, fleet devices, and the managed transportation network.

**Gap risk levels across all regulations:** High 12, Moderate 20, Low 3.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | 164.308(a)(1)(ii)(D) | AQ-01 legacy CAD and directory not in the SIEM; CAD lookups reviewed only quarterly | SIEM collectors; weekly automated lookup review (POAM-005) | Director of Security Operations | 2026-12-31 |
| G-010 | 164.308(a)(3)(ii)(C) | 2 of 60 sampled terminations disabled 3 and 5 business days late (both AQ-01) | Federation; interim daily reconciliation (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| G-019 | 164.308(a)(5)(ii)(D) | Default passwords on 4 radio console gateways; shared MDC logins | Vault and scan gateways (POAM-012); named MDC sign-in (POAM-003) | Vice President, Communications Centers | 2026-12-31 |
| G-022 | 164.308(a)(7) | Contingency plan lacks RCC-3 failover and automated cutover; AQ-01 not in the enterprise plan | Plan update (POAM-011); AQ-01 plan and migration (POAM-007) | Director of CAD and Dispatch Systems | 2027-01-31 |
| G-023 | 164.308(a)(7)(ii)(A) | AQ-01 legacy CAD backed up nightly to a local appliance and never restore-tested | Restore test; cloud backups; migration (POAM-007) | Vice President, Integration Management Office | 2027-03-31 |
| G-024 | 164.308(a)(7)(ii)(B) | Regional CAD failover 1 h 25 min against a 1 h RTO | Automate cutover and retest (POAM-011) | Director of CAD and Dispatch Systems | 2027-01-31 |
| G-048 | 164.312(b) | No audit log forwarding from the AQ-01 legacy CAD | POAM-005 | Director of Security Operations | 2026-12-31 |
| G-051 | 164.312(d) | MFA on 62% of network provider portal accounts; shared hospital portal logins | MFA for all provider accounts (POAM-013); hospital portal cleanup (POAM-002) | President, Managed Transportation | 2026-12-31 |
| G-083 | Form 8-K Item 1.05; SEC Release 33-11216 | Playbook never exercised for a dispatch outage; 2 new committee members | Update playbook; tabletop 2026-11-18 (POAM-014) | General Counsel | 2026-11-30 |
| G-084 | Form 8-K Item 1.05 (materiality determination) | Worksheet leaves out county penalties, agreement default risk, and public safety effects | POAM-014 | General Counsel | 2026-11-30 |
| G-107 | 45 CFR 92.210(b) | Dispatch protocol software (uses patient age as an input) and other non-automated tools not inventoried | Extend the inventory (POAM-020) | Chief Medical Officer | 2026-11-30 |
| G-108 | 45 CFR 92.210(c) | Mitigation records missing for the protocol software; vendor accuracy data by language not received for AI-001 | POAM-020 | Chief Medical Officer | 2027-03-31 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee tabletop and playbook update (POAM-014); AQ-01 termination reconciliation and first federation wave (POAM-001); SIEM collectors for AQ-01 (POAM-005); dispatch change board (POAM-006); radio console gateway credential vaulting (POAM-012); first RCC-4 manual dispatch drill (POAM-007); network provider MFA and field masking (POAM-013); hospital portal cleanup (POAM-002); AQ-02 BAA review (POAM-022); AQ-01 encryption and EDR (POAM-023); 92.210 inventory of protocol and non-automated tools (POAM-020); AQ-01 certification statement linking (POAM-021) | SEC Item 1.05; HIPAA 164.308(a)(1)(ii)(D), (a)(3), (a)(5)(ii)(D), (b)(1); 164.312(a)(2)(iv), (b), (d); 92.210(b); 42 CFR 410.40(e) | Tabletop report; federation records; SIEM source list; change board minutes; MFA reports; signed BAAs |
| 2027 Q1 | Automated CAD failover and retest; RCC-3 failover test (POAM-011); AQ-01 SD-WAN and VPN restriction (POAM-016); AQ-01 CAD migration and restore test (POAM-007); router replacement wave 1 (POAM-009); fleet device inventory 98% (POAM-010); telephony RTO contract change (POAM-019); 92.210 mitigation records (POAM-020); Internal Audit test of Item 106 statements | HIPAA 164.308(a)(7); 164.310(d); 164.312(e); 92.210(c); Item 106 | DR test report; migration sign-off; inventory report; mitigation records |
| 2027 Q2 | Router replacement complete (POAM-009); legacy PSAP links upgraded with the counties (POAM-017); network agreement renewals with breach notice terms | HIPAA 164.308(a)(5)(ii)(B); 164.312(e)(2)(ii); Fla. Stat. 501.171(6) | Replacement records; TLS scans; signed agreements |
| 2027 Q3 | Annual risk analysis and gap reassessment; review NPRM and CIRCIA status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. 35 HIPAA rows carry a note in `pending_rule_change`. If finalized as proposed, the verified proposals that matter most here are: removal of the addressable designation; encryption of all ePHI at rest and in transit with limited exceptions (AQ-01 workstations and the 4 legacy PSAP links); MFA (network provider and hospital portals); a written technology asset inventory and network map (fleet devices); penetration testing at least every 12 months and vulnerability scanning; restoring certain systems within 72 hours (AQ-01 legacy CAD); a compliance audit at least every 12 months; and business associate notice within 24 hours of activating a contingency plan (which would apply to the company as a business associate for SL-1 and SL-2). None of these is treated as a current obligation.
- **CIRCIA** (C-EMERGENCY-R05): the final rule had not been published as of 2026-09-25. As proposed, it would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment. Reporting to CISA is voluntary until it takes effect.
- **SEC:** no SEC proposal to amend or rescind Item 1.05 was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an OCR data request, a state EMS inspection or license review, a Medicare audit, a county contract audit, a Medicaid broker contract review, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the latest breach log submissions and notification files;
- manual dispatch drill and failover test records for each communications center;
- the state requirements matrix and counsel's call recording memo;
- 92.210 inventory and mitigation records (from P10);
- county confirmations that premise hazard notes contain no criminal justice information;
- document retention of 6 years (164.316(b)(2)(i)).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
