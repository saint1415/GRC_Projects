# Regulatory Gap Analysis: Cris Santos Company | Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer; plants FL-1, MN-1, TX-1) |
| Tier / Vertical | Enterprise / Manufacturing (NAICS 334510) |
| Primary regulation | FD&C Act section 524B, ensuring cybersecurity of devices (21 U.S.C. 360n-2), with the FDA regulations and guidance that carry it out |
| Also analyzed | HIPAA Security Rule and breach notice as a business associate (DDC and RCM); FTC Health Breach Notification Rule (consumer companion app); SEC Form 8-K Item 1.05 and Reg S-K Item 106; state breach and data security laws (Florida worked example) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer; the CQRO and the VP Product Security for the FDA rows; the Chief Privacy Officer for the HIPAA and FTC rows; sampling reperformed by Internal Audit for 8 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Applicability
| Regulation | Applies? | Basis |
|---|---|---|
| FD&C Act 524B (N31-33-R05) | **Yes** | Section 524B(a) covers any person who submits a 510(k), PMA, PDP, De Novo, or HDE for a cyber device, defined in 524B(c) as a device that includes sponsor-validated software, can connect to the internet, and has technological characteristics that could be vulnerable to cybersecurity threats. It took effect 90 days after enactment on 2022-12-29 (Pub. L. 117-328 section 3305(d)). No size exemption; the only exemption route is an FDA list under 524B(d), and none applies. Failure to comply with 524B(b)(2) is a prohibited act under 21 U.S.C. 331(q)(3) |
| 524B, by product | **Current products** | CR-100 (2023), VM-700 and DG-10 (2024), HB-40 (2024), and the IV-300 second-generation module (2025) were submitted after the effective date. AI-001 (planned 2027) will be. **VM-500 (cleared 2019), IV-300 as originally cleared (2021), and US-20 (2022)** were cleared before it, so 524B does not reach those clearances; they remain subject to the QMSR, MDR, and correction and removal rules and to FDA's postmarket expectations. The DDC update service, DG-10 gateways, and the build and signing path are "related systems" |
| QMSR, 21 CFR 803 and 806 | **Yes** | Registered manufacturer of class II devices at three plants. Only the provisions that cybersecurity events touch are analyzed (design and development, complaint and servicing records, MDR, corrections and removals) |
| FDA cybersecurity guidance | **Nonbinding** | *Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions* (issued 2026-02-03, superseding the June 2025 version) and *Postmarket Management of Cybersecurity in Medical Devices* (December 2016, docket FDA-2015-D-5105). They are rated because FDA uses them to judge a "reasonable assurance" of cybersecurity; they are recommendations, not requirements |
| HIPAA Security Rule (N62-R01) | **Yes, business associate scope** | The company is not a covered entity: it does not bill payers or conduct standard transactions (45 CFR 160.103). It is a business associate for about 3,400 customers through the DDC and RCM, so the Security Rule applies to those services (164.302), BAA terms follow 164.314(a), and subcontractors need BAAs (164.308(b)(1), 164.314(a)(2)(iii)) |
| HIPAA Breach Notification Rule (N62-R03) | **Yes, 164.410** | Business associate notice to covered entities; the covered entities give notice to individuals, HHS, and media |
| FTC Health Breach Notification Rule (N62-R06) | **Yes, consumer app only** | The companion app is a personal health record offered directly to consumers (it draws information from the HB-40, the user, and the phone's health platform, and is managed by the user), so the company is a vendor of personal health records (16 CFR 318.2). 318.1(a) excludes covered entities and business associate activities, so the rule does **not** reach the DDC or RCM |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded registrant, not a smaller reporting company |
| State breach and data security laws | **Yes** | The law of each state where affected individuals reside (workforce, consumer app users, and, as an agent, customers' patients); Florida (Fla. Stat. 501.171) is the worked example |
| HIPAA Security Rule NPRM (N62-R04) | **Not in force** | Proposed rule only; tracked in `pending_rule_change` |
| CIRCIA | **Not in force** | Final rule not published as of 2026-09-25. The proposed rule's critical manufacturing criteria would reach class II and III device makers, so recheck when final |
| DFARS 7012, CMMC, ITAR, EAR, FAR 52.204-25 | **No** | See `../00_company-facts.md` section 1 |
| SOX Section 404 | Separate program | IT general controls over ERP are tested by the SOX program and not repeated here |

HIPAA exclusions (Not applicable): 164.308(a)(4)(ii)(A), because the company performs no clearinghouse function; 164.314(a)(2)(ii), because there are no arrangements between governmental entities; and 164.314(b) with its four implementation specifications, because the company does not act for a group health plan in these services (its employee plan is a separate covered entity handled by the benefits program).

## 2. Method
1. **Decompose.** The 524B rows follow the statute's own structure: (a), (b)(1) through (b)(4), (c), and (d). FDA regulation rows cite the CFR section. Guidance rows cite the section of each guidance that explains what FDA expects. HIPAA Security Rule rows and their Required and Addressable types come from NIST SP 800-66 Rev. 2 (all 69 rows in the Health Care crosswalk). Other regulations were broken into citation-level duties from the eCFR text (2026-09-23 versions of 16 CFR Part 318, 17 CFR 229.106, 21 CFR 803, 806, and 820, and 45 CFR 164.314 and 164.410), the U.S. Code text of 21 U.S.C. 360n-2, the SEC's compliance guide for Item 1.05, and the Florida statute text.
2. **Crosswalk.** Each row maps to CSF 2.0 and SP 800-53 Rev. 5. NIST has published no mapping for section 524B, FDA regulations, or the FTC and SEC rules, so those rows carry an **author mapping**, labeled as such. HIPAA rows use the Health Care crosswalk (also an author mapping for CSF 2.0), with NIST's official OLIR 110 controls shown in `nist_official_sp800_53r5_1_1`.
3. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); populations under 250 and lower-risk controls used 25 to 40 items; small populations (submissions, uncontrolled-risk cases, subcontractors) were tested in full. **27 rows were tested by sampling or full-population review; 9 found exceptions.**
4. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**Addressable is not optional.** For each addressable HIPAA specification, the company implements it, implements an equivalent, or documents why neither is reasonable and appropriate (164.306(d)(3)). All addressable gaps below are being implemented; none is documented as unreasonable.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| FD&C Act section 524B (statute) | 3 | 6 | 0 | 2 | 11 |
| QMSR (21 CFR 820.10(c), 820.35) | 2 | 1 | 0 | 0 | 3 |
| MDR (21 CFR 803) | 3 | 0 | 0 | 0 | 3 |
| Corrections and removals (21 CFR 806) | 0 | 2 | 0 | 0 | 2 |
| FDA premarket cybersecurity guidance (2026) | 7 | 8 | 0 | 0 | 15 |
| FDA postmarket cybersecurity guidance (2016) | 1 | 1 | 0 | 0 | 2 |
| HIPAA Security Rule 164.308 | 21 | 8 | 0 | 1 | 30 |
| HIPAA Security Rule 164.310 | 12 | 0 | 0 | 0 | 12 |
| HIPAA Security Rule 164.312 | 9 | 3 | 0 | 0 | 12 |
| HIPAA Security Rule 164.314 | 1 | 3 | 0 | 6 | 10 |
| HIPAA Security Rule 164.316 | 5 | 0 | 0 | 0 | 5 |
| HIPAA Breach Notification Rule, business associate (N62-R03) | 5 | 0 | 0 | 0 | 5 |
| FTC Health Breach Notification Rule (N62-R06) | 0 | 5 | 3 | 0 | 8 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| State breach and data security laws | 3 | 1 | 0 | 0 | 4 |
| **Total** | **78** | **40** | **3** | **9** | **130** |

**HIPAA Security Rule (business associate scope):** 48 Met, 14 Partially met, 0 Not met, 7 Not applicable (69 rows). Of the 14 partially met rows, 5 are standards, 6 are Required specifications, and 3 are Addressable specifications.

**Gap risk levels across all regulations:** High 7, Moderate 31, Low 5.

**The main findings:**
- **Section 524B is met for current products at submission, and mostly kept up after.** SBOMs, CVD, ISAO membership, security testing, and KEV monitoring are in place. The gaps are in build integrity (provenance, promotion before approval, MN-1 stations) and in the IV-300 second-generation line, which the acquired team still runs outside the enterprise PSIRT process.
- **Legacy products carry the largest safety exposure but sit outside 524B.** VM-500 and first-generation IV-300 designs are handled through the QMS, MDR, and correction duties and the postmarket guidance (P01 R-001).
- **The FTC rule is the newest obligation and the least prepared.** Applicability was confirmed in 2026-07; there is no FTC notice procedure, no annual log, and no governance of third-party kits in the app.
- **Disclosure readiness is untested for the incident type most specific to this company:** a fielded-device vulnerability.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-005 | 524B(b)(2); 21 U.S.C. 331(q)(3) | Firmware build integrity: no signed provenance; 3 of 40 releases promoted before PLM approval; MN-1 stations verify by checksum | POAM-004; POAM-010; POAM-019 | Chief Technology Officer | 2027-03-31 |
| G-032 | Premarket guidance Appendix 1 (authentication) | Per-hospital pre-shared keys and TLS 1.0 on 62,000 first-generation IV-300 modules | Module swap; key rotation; edge isolation (POAM-023) | Vice President, Integration Management Office | 2027-06-30 |
| G-033 | Premarket guidance Appendix 1 (integrity and updates) | Legacy IV-300 1.x signing workstation; unsigned first-generation drug libraries; MN-1 checksum stations | POAM-001; POAM-019; POAM-023 | Director of Build and Release Engineering | 2027-03-31 |
| G-060 | 45 CFR 164.308(a)(7)(ii)(B) | RCM recovered in 3.5 h against a 2 h RTO | Automate recovery and retest (POAM-026) | Vice President, Remote Monitoring Services | 2027-01-31 |
| G-112 | 16 CFR 318.3(a) | No procedure to notify individuals, the FTC, and media; no kit governance | FTC procedure, templates, kit release gate (POAM-021) | Chief Privacy Officer | 2026-12-31 |
| G-119 | Form 8-K Item 1.05; SEC Release 33-11216 | Materiality process never exercised for a fielded-device incident; three new members | Device scenario; tabletop 2026-11-19 (POAM-014) | General Counsel | 2026-11-30 |
| G-120 | Form 8-K Item 1.05 (materiality determination) | No written path from a PSIRT severity-1 declaration to the disclosure committee | POAM-014 | General Counsel | 2026-11-30 |

## 5. Compliance roadmap
| Quarter | Milestones | Regulations served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure committee device tabletop and playbook update (POAM-014); FTC procedure, templates, processor notices, and kit gate (POAM-021); subcontractor BAAs and BAA terms register, Florida 10-day agent notice training (POAM-022); 806 decision field (POAM-015); IV-300 v2 into the PSIRT case system and threat model (POAM-023); CI runner workload identity (POAM-003); HSM failover test (POAM-012) | SEC Item 1.05; 16 CFR 318.3-318.6; 164.308(b)(1), 164.314(a); Fla. Stat. 501.171(6); 21 CFR 806.10, 806.20; 524B(b)(1), (b)(2) | Tabletop report; FTC procedure; signed BAAs; register export; PSIRT records |
| 2027 Q1 | Legacy signing moved into the HSM service (POAM-001); RCM recovery retest (POAM-026); firmware provenance and promotion gate (POAM-004, POAM-010); MN-1 station signature verification and segmentation (POAM-019, POAM-006); update adoption dashboard (POAM-024); Internal Audit test of Item 106 statements | 524B(b)(2); premarket guidance Appendix 1 and V.A.6; 164.308(a)(7); Item 106 | Key ceremony record; DR retest report; provenance samples; adoption metrics |
| 2027 Q2 | First-generation IV-300 module swap reaches 60% of pumps; VM-500 end-of-support notice and trade-in program; supplier SBOM coverage 75% (POAM-005, POAM-023) | Postmarket guidance VII.B; premarket guidance V.A.4, VI.A; 164.312(d), (e) | Swap records; customer notices; supplier SBOM register |
| 2027 Q3 | Annual gap reassessment; AI-001 submission readiness review (524B content); review NPRM and CIRCIA status | All | Updated P01 and P03 |

## 6. Pending regulatory changes
- **Section 524B(b)(4) regulations.** FDA may add cybersecurity requirements by regulation. None were found as of 2026-09-25.
- **FDA guidance updates.** The premarket guidance was issued in September 2023 and revised in June 2025 and February 2026. Recheck the current version before each submission, including the AI-001 submission.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. 13 HIPAA rows carry a note in `pending_rule_change`. If finalized as proposed, the verified proposals that matter most for the business associate services are: removal of the addressable designation; encryption of all ePHI at rest and in transit with limited exceptions (first-generation IV-300 modules); MFA; a written technology asset inventory and network map; penetration testing at least every 12 months and vulnerability scanning; restoring certain systems within 72 hours; a compliance audit at least every 12 months; and business associate notice within 24 hours of activating a contingency plan. None of these is treated as a current obligation.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the company can respond quickly to an FDA inspection or information request, a customer's BAA audit, an OCR data request, an FTC inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- per product: the 524B submission content, the current SBOM, the postmarket management plan, PSIRT case history, advisories, and 806 decisions;
- the BAA register with notice terms, the subcontractor BAA register, and the breach log (HIPAA and FTC matters);
- document retention of 6 years for HIPAA documentation (164.316(b)(2)(i)) and, for 806.20 records, 2 years beyond the expected life of the device.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
