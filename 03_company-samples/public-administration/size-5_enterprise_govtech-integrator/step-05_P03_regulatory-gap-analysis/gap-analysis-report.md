# Regulatory Gap Analysis: Cris Santos Company | Public Administration | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator, NAICS 541512; about 145 agency customers in 16 states) |
| Tier / Vertical | Enterprise / Public Administration |
| Scope | Every hosted environment that holds agency data (ACMC, IES, legacy hosting, AQ-1), the CUI enclave, and enterprise obligations (SEC, state law) |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, as selected in NIST SP 800-53B, required by every agency contract |
| Overlays and other rules | FBI CJIS Security Policy v6.1 (06/25/2026); IRS Publication 1075 (Rev. 11-2021); HIPAA Security and Breach Notification Rules (business associate scope); Medicaid and SNAP confidentiality; Driver's Privacy Protection Act; SEC Form 8-K Item 1.05 and Reg S-K Item 106; Florida law (worked example) and other states' breach laws; FAR and DFARS clauses; CMMC; plus applicability decisions for FedRAMP, GovRAMP, CIRCIA, and SLCGP |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14; statuses updated to 2026-08-28 for the 2026-08-19 ticket finding and the P07 results) |
| Assessors | GRC team and the Director of Regulated Data Compliance (second line) with the Chief Compliance Officer; Internal Audit reperformed the sampling for 5 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-31; roadmap reviewed by the risk committee of the board, 2026-09-10 |

## 1. Applicability
The company is a private contractor, not an agency. Most rules reach it **through contracts with agencies that are bound**; a few bind it **directly**. Each row in `gap-analysis.csv` states its legal path in `applies_at_this_tier`.

| Rule | Applies? | Basis |
|---|---|---|
| NIST SP 800-53 Rev. 5 Moderate | **Yes, by contract** | Every agency contract requires the Moderate baseline (177 base controls, 110 enhancements) for hosted systems. Each row is one base control; its Moderate enhancements are assessed inside the row |
| FBI CJIS Security Policy v6.1 (N92-R02) | **Yes, by contract** | 28 CFR 20.33(a)(7) allows CHRI to go to private contractors under an agreement that incorporates the CJIS Security Addendum. All 24 criminal justice agency contracts do. The Addendum binds the company to the policy "in effect when the contract is executed and all subsequent versions" (sec. 3.01). No size threshold |
| IRS Pub. 1075 (N92-R01) | **Yes, by contract** | The 6 state revenue agencies may disclose FTI to contractors under written contracts (26 CFR 301.6103(n)-1(a)); each contract carries Exhibit 7, and each agency's 45-day notification names the company. The IES environments hold no FTI because human services agencies "may not contract for services that involve the disclosure of FTI to contractors" (sec. 2.C.11.2) |
| HIPAA Security and Breach Notification Rules (N92-R03) | **Yes, as a business associate of AG-04 only** | AG-04's Medicaid program is a health plan; the company signed a business associate agreement for enrollment and premium processing, so 164.302 and 164.410 apply to that environment. No other customer has designated the company a business associate |
| Medicaid safeguards (N92-R04) and SNAP disclosure rules | **Yes, by contract** | 42 CFR 431.300-431.307 and 7 CFR 272.1(c) bind the state agencies; the 4 IES contracts flow them down |
| Driver's Privacy Protection Act (N92-R05) | **Yes, directly** | "A State department of motor vehicles, and any officer, employee, or contractor thereof, shall not knowingly disclose" personal information except as permitted (18 U.S.C. 2721(a)). The company is AG-05's contractor |
| SEC Form 8-K Item 1.05 and Reg S-K Item 106 | **Yes, directly** | Publicly traded SEC registrant, not a smaller reporting company |
| Fla. Stat. 501.171 | **Yes, directly** | Third-party agent of Florida agency customers (501.171(1)(h)); reasonable measures (501.171(2)) and 10-day notice to the agency (501.171(6)(a)) |
| Florida Rule 60GG-2 and Fla. Stat. 282.318, 282.3185, 282.3186 | **Agency duties the company supports** | Rule 60GG-2 binds state agencies; it reaches suppliers through contracts (Rule 60GG-2.001(3)(b); 282.318(4)(h)). Ransomware reporting within 12 hours and the ransom-payment ban are agency duties; the company must give agencies what they need in time |
| Other states' breach laws | **Yes** | The law of each state where affected individuals reside, through counsel's state matrix |
| FAR 52.204-21, 52.204-23, 52.204-25 | **Yes, by contract** | Federal Programs contracts and subcontracts |
| DFARS 252.204-7012 | **Yes, by subcontract** | The DoD subcontract involves covered defense information in the CUI enclave |
| CMMC (32 CFR Part 170) | **Yes, phasing in** | Phase 1 began 2025-11-10 (the DFARS CMMC rule's effective date); Phase 2 begins one year later (32 CFR 170.3(e)). The prime expects Level 2 (C3PAO) status for the 2027-04-01 option |
| FedRAMP | **No** | No federal agency uses ACMC or IES. FedRAMP-authorized services are used for FTI and CUI because Pub. 1075 and DFARS require them |
| GovRAMP (N92-R08) | **Voluntary** | Not law. ACMC holds Authorized status because many agency procurements ask for it |
| CIRCIA (N92-R07) | **Not in force** | Final rule not published as of 2026-09-25 |
| SLCGP (N92-R06) | **No** | A grant condition on recipient governments |
| Colorado SB26-189 and other state AI laws | **Not today** | No customers in Colorado or Texas; reassessed before any bid there (P10) |

## 2. Method
1. **Requirements.** One row per Moderate base control (177) from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags. Overlay rows were added only where another rule sets a value or duty beyond the base control text: 12 CJIS rows, 15 Pub. 1075 rows, 9 HIPAA rows, 6 Medicaid and SNAP rows, 3 DPPA rows, 7 SEC rows, 6 state law rows, 10 federal contract and CMMC rows, and 4 applicability rows (FedRAMP, GovRAMP, CIRCIA, SLCGP). Public-domain texts (CFR sections, statutes, CJISSECPOL, Pub. 1075) are quoted or summarized with section numbers.
2. **Crosswalk.** CSF 2.0 subcategories for the 177 base controls come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`). Overlay rows are author mappings and say so. The `regulatory_driver` column shows which overlays also contain each control; HIPAA citations come from the repository HIPAA crosswalk (an author mapping) and apply only to the AG-04 business associate scope.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions in the CSV. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); smaller populations used 12 to 40 items or the full population; ticket and configuration data were checked in full with analytics. Selections were random. **20 rows were tested by sampling or full-population analytics; 15 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable, using the worst environment in scope (`scope_entities`). A control inherited from a FedRAMP-authorized provider is Met when the company's use falls inside the authorization. Gap risk uses the P01 scale; High gaps are in the P01 register and the P07 POA&M.

## 3. Results summary
| Regulation / set | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| SP 800-53 Rev. 5 Moderate baseline | 127 | 48 | 0 | 2 | 177 |
| FBI CJIS Security Policy v6.1 | 2 | 9 | 0 | 1 | 12 |
| IRS Pub. 1075 | 10 | 4 | 1 | 0 | 15 |
| HIPAA (business associate, AG-04) | 5 | 4 | 0 | 0 | 9 |
| Medicaid safeguards (42 CFR 431 Subpart F) | 3 | 1 | 0 | 0 | 4 |
| SNAP (7 CFR Part 272) | 1 | 1 | 0 | 0 | 2 |
| Driver's Privacy Protection Act | 1 | 1 | 0 | 1 | 3 |
| SEC Item 1.05 and Item 106 | 5 | 2 | 0 | 0 | 7 |
| State law (Florida worked example) | 3 | 2 | 0 | 0 | 5 |
| State law (other states) | 1 | 0 | 0 | 0 | 1 |
| FAR clauses | 4 | 0 | 0 | 0 | 4 |
| DFARS 252.204-7012 | 4 | 1 | 0 | 0 | 5 |
| CMMC (32 CFR Part 170) | 0 | 1 | 0 | 0 | 1 |
| FedRAMP, GovRAMP, CIRCIA, SLCGP | 1 | 0 | 0 | 3 | 4 |
| **Total** | **167** | **74** | **1** | **7** | **249** |

**SP 800-53 Moderate by family:**
| Family | Controls | Met | Partially met | N/A |
|---|---|---|---|---|
| AC Access Control | 17 | 9 | 7 | 1 |
| AT Awareness and Training | 4 | 2 | 2 | 0 |
| AU Audit and Accountability | 11 | 9 | 2 | 0 |
| CA Assessment, Authorization, and Monitoring | 7 | 5 | 2 | 0 |
| CM Configuration Management | 12 | 7 | 5 | 0 |
| CP Contingency Planning | 9 | 5 | 4 | 0 |
| IA Identification and Authentication | 10 | 8 | 2 | 0 |
| IR Incident Response | 8 | 5 | 3 | 0 |
| MA Maintenance | 6 | 4 | 2 | 0 |
| MP Media Protection | 7 | 6 | 1 | 0 |
| PE Physical and Environmental Protection | 16 | 15 | 1 | 0 |
| PL Planning | 6 | 5 | 1 | 0 |
| PS Personnel Security | 9 | 6 | 3 | 0 |
| RA Risk Assessment | 6 | 4 | 2 | 0 |
| SA System and Services Acquisition | 11 | 7 | 4 | 0 |
| SC System and Communications Protection | 18 | 14 | 3 | 1 |
| SI System and Information Integrity | 11 | 8 | 3 | 0 |
| SR Supply Chain Risk Management | 9 | 8 | 1 | 0 |
| **Total** | **177** | **127** | **48** | **2** |

**Gap risk levels across all 75 gaps (Partially met or Not met):** High 33, Moderate 33, Low 9.

**Where the gaps are.** ACMC itself is largely compliant (P02: 153 of 177 controls Implemented). Most enterprise gaps sit in four places: the AQ-1 acquisition, legacy hosting, third parties and subcontractors, and processes that span the company (agency notice, disclosure, AI). The one Not met row is Pub. 1075 subcontracting without IRS approval (PB-04).

## 4. Priority gaps (High)
The 33 High gaps fall into eight themes. Each is carried into the risk register (P01) and the POA&M (P07).

| Theme | Rows | Action | Owner | Target |
|---|---|---|---|---|
| AQ-1 acquisition | G-002, G-004, G-006, G-027, G-031, G-062, G-144, G-161, CJ-05, CJ-08 | Restrict the peering (POAM-004); SIEM and 1-year logs (POAM-003); federation, MFA, and removal of standing administrator rights (POAM-001) | Vice President, Integration Management Office | 2027-01-31 |
| Unscreened staff with CJI access | G-116, CJ-01, CJ-03 | Suspend access for 39 AQ-1 staff; reconcile certification pages with every criminal justice agency (POAM-002) | Chief Human Resources Officer | 2026-10-31 |
| CJIS cryptography deadline | G-065, G-145, G-148, CJ-10 | Replace 7 FIPS 140-2 VPN appliances before 2026-09-21 and change default passwords (POAM-006, POAM-007) | Director of Network and Data Center Operations | 2026-09-18 |
| Legacy hosting | G-041, G-059, G-139, G-159 | Immutable backups (POAM-008); replatform or isolate 64 unsupported servers (POAM-005) | Director of Network and Data Center Operations | 2027-06-30 |
| FTI reaching unapproved parties | G-016, G-120, G-135, PB-04, PB-06 | U.S.-only routing (done 2026-08-20); attachment block; subcontractor coverage in IRS notifications (POAM-009, POAM-010) | Director of Regulated Data Compliance | 2026-10-31 |
| Eligibility system recovery | G-055, HP-08 | Parallel restore; retest AG-04 (POAM-015) | President, Eligibility and Enrollment Operations | 2027-02-28 |
| SEC disclosure readiness | G-078, SE-01, SE-02 | Customer-harm factors in the playbook; tabletop with the filing step on 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| AI in eligibility decisions | G-125, SN-02 | Suggestions off from 2026-09-11; review-first design and bias testing before re-enablement (POAM-022) | Chief Data and AI Officer | 2026-12-31 |

The full list, with evidence and samples, is in `gap-analysis.csv`.

## 5. Compliance roadmap
| Quarter | Milestones | Rules served | Evidence produced |
|---|---|---|---|
| 2026 Q3 (by 2026-09-30) | VPN appliance replacement before the CJIS cutoff (POAM-006); default passwords (POAM-007); help desk contract amendment and attachment block (POAM-009) | CJISSECPOL SC-13, IA-5; Pub. 1075 sec. 3.3.1(b), Exhibit 7 | Appliance certificates; routing test; amended contract |
| 2026 Q4 | AQ-1 peering restriction, SIEM onboarding, interim MFA (POAM-003, POAM-004); CJIS screening and certifications (POAM-002); subcontractor coverage (POAM-010); disclosure tabletop (POAM-013); 1-hour notice timer (POAM-014); legacy immutable backups (POAM-008); AI-001 conditions (POAM-022); AG-04 subcontractor BAA; DPPA export control | CJISSECPOL PS-3, AU-11, IA-2(1); Pub. 1075 Exhibit 7; SEC Item 1.05; 45 CFR 164.308(b); 18 U.S.C. 2721(a); 7 CFR 272.4(a)(2) | Screening records; SIEM source list; tabletop report; signed BAA |
| 2027 Q1 | AQ-1 federation (POAM-001); IES DR retest (POAM-015); vendor review backlog (POAM-011); CMMC Level 2 (C3PAO) assessment (POAM-023); Internal Audit capacity (POAM-012); Internal Audit test of Item 106 statements | SP 800-53 AC-2, CP-4, SR-6, CA-2; 32 CFR Part 170; 17 CFR 229.106 | Federation records; DR report; CMMC status; audit report |
| 2027 Q2 | Legacy replatforming (POAM-005); management network segmentation (POAM-024); second VPN edge in DC-2 | SP 800-53 SA-22, SI-2, SC-7, CP-7 | Decommission records; network diagrams |
| 2027 Q3 | Annual reassessment; recheck CJISSECPOL, Pub. 1075, HIPAA NPRM, CIRCIA, and FAR overhaul status | All | Updated P01 and P03 |

## 6. Pending and dated changes
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates will not be acceptable after **2026-09-21**. The 7 appliances are scheduled for replacement on 2026-09-18; any tunnel not cut over by the cutoff is shut down.
- **CJIS zero-cycle end.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30**. The contracts already require them.
- **CMMC phases.** Phase 2 begins **2026-11-10** (one year after the 2025-11-10 start of Phase 1; 32 CFR 170.3(e)(2)); Phase 3 begins one year after that.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**; the regulatory agenda projects a final rule in July 2027. Rows that would change if it is finalized as proposed carry a note in `pending_rule_change` (encryption, MFA, asset inventory, 72-hour restoration, annual compliance audit, vulnerability scanning and penetration testing). None is treated as a current obligation.
- **FAR overhaul.** A proposed rule (FR Doc. 2026-12559) would move information security clauses into FAR part 40. Proposed only.
- **CIRCIA.** The final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC.** A 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **Pub. 1075.** Rev. 11-2021 remains the edition at irs.gov (checked 2026-09-26).

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to a CJIS audit by a state CJIS Systems Agency, an IRS safeguard review of a revenue agency, a HIPAA inquiry through AG-04, a DoD or prime contractor request, an agency supplier assessment, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 register, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook and notification matrix;
- signed CJIS Security Addendum certification lists per agency and authorized FTI staff lists per revenue agency;
- the agency notices for the 2026-08-19 ticket exposure;
- the CUI enclave SSP, plan of action, and SPRS record;
- documentation kept at least 7 years (POL-01 4.11), which also meets the HIPAA 6-year rule (164.316(b)(2)(i)).

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-31. The roadmap was reviewed by the risk committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07, or within 60 days of a new CJISSECPOL version.
