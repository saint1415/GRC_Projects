# Regulatory Gap Analysis: Cris Santos Company | Public Administration | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator, NAICS 541512) |
| Tier / Vertical | Small / Public Administration |
| System | Agency Case Management Platform (ACMP), as bounded in the SSP (P02) |
| Primary requirement set | NIST SP 800-53 Rev. 5 (Release 5.2.0) Moderate baseline, as selected in NIST SP 800-53B, required by every agency contract |
| Secondary overlays | FBI CJIS Security Policy v6.1 (06/25/2026) for AC-02 (N92-R02); IRS Publication 1075 (Rev. 11-2021) for AC-01 (N92-R01) |
| Assessment dates | 2026-07-13 to 2026-07-24 (statuses updated to 2026-08-31, when the P06 policies were approved; the IA-5 finding was added 2026-08-07 from P07 testing) |
| Assessor | IT Manager (Information Security Officer) with the Contracts and Compliance Manager and the Cloud Operations Lead |

## 1. Applicability
The company is a private contractor, not an agency. None of the rules below binds it by its own force except Fla. Stat. 501.171. Each reaches it **through a contract with an agency that is bound**. That is why this analysis starts with the contracts.

### 1.1 SP 800-53 Rev. 5 Moderate: applies by contract
NIST SP 800-53 is a federal standard, not a law for private companies. All 11 agency contracts require the hosted platform to meet the Moderate baseline. The baseline has **177 base controls and 110 enhancements** (287 in the repository catalog). Each row below is one base control, and the Moderate-baseline enhancements for that control are assessed inside the row and named in the `citation` column. This is the same control structure that both overlays use, so one row can serve all three sources.

### 1.2 FBI CJIS Security Policy: applies to AC-02 work through the Security Addendum
- **Legal path.** 28 CFR 20.33(a)(7) lets criminal history record information go "to private contractors pursuant to a specific agreement" with a criminal justice agency. The agreement "must incorporate a security addendum approved by the Attorney General," which the FBI Director issues. The AC-02 contract incorporates that CJIS Security Addendum.
- **What the Addendum requires.** The contractor must "maintain a security program consistent with ... the CJIS Security Policy in effect when the contract is executed and all subsequent versions" (Addendum sec. 3.01). Each contractor employee signs the certification page, and the agency keeps the signed copies (sec. 2.01). CJISSECPOL v6.1 SA-9 repeats that private contractors performing criminal justice functions "shall acknowledge, via signing of the CJIS Security Addendum Certification page ... compliance with all aspects of the CJIS Security Addendum."
- **Version checked.** CJISSECPOL **v6.1, dated 06/25/2026**, approved by the CJIS Advisory Policy Board, read from the policy PDF in the FBI file repository. It supersedes v6.0 (12/27/2024).
- **No size threshold.** Section 1.4: since 2024-10-01, audits sanction the pre-modernization ("existing") requirements and those marked [Priority 1]. [Priority 2] to [Priority 4] requirements are in a zero-cycle that ends **2027-09-30**. The AC-02 contract requires the whole policy now, so every CJIS row is rated today and the priority only sets the order of work.
- **Scope.** Only the platform and the 13 staff who can reach AC-02 data. The state CJIS Systems Agency audits through AC-02.

### 1.3 IRS Publication 1075: applies to AC-01 work through Exhibit 7
- **Legal path.** AC-01 is a state tax agency that receives FTI under IRC 6103(d). Under 26 CFR 301.6103(n)-1(a), a state tax agency may disclose returns and return information to a contractor "to the extent necessary in connection with a written contract" for processing, storage, transmission, and other services. Contractor staff are subject to the penalties of IRC 7213, 7213A, and 7431, and must be told so in writing (301.6103(n)-1(c)-(d)).
- **Contract terms.** Pub. 1075 requires the agency to put Exhibit 7 safeguarding language in the contract and to notify the IRS at least 45 days before a contractor or cloud provider gets FTI (sections 2.E.6.1-2.E.6.2 and Exhibit 6). AC-01 filed that notification in 2024 and named both the company and its cloud provider.
- **Edition checked.** Rev. 11-2021 is the edition served at irs.gov/pub/irs-pdf/p1075.pdf (checked 2026-09-26). It aligns its control section with SP 800-53 Rev. 5.
- **Why the AC-03 tenant holds no FTI.** Human services agencies that receive FTI under IRC 6103(l)(7) "may not contract for services that involve the disclosure of FTI to contractors or sub-contractors" (section 2.C.11.2; Exhibit 6 repeats it). The AC-03 contract forbids FTI in the platform. This analysis tests that rule through PB-04 and PB-09, because tickets and staging copies are the realistic ways FTI could leak into places it is not allowed.

### 1.4 Florida Rule 60GG-2, F.A.C.: binds state agencies; reaches the company only by contract
- Rule 60GG-2.001(1)(b) says "Agencies must comply with these standards." "Agency" has the meaning of "state agency" in Fla. Stat. 282.0041 (Rule 60GG-2.001(2)(a)1.). The company is not an agency.
- The rule reaches vendors through procurement. Each agency must ensure that "solicitations, contracts, and service-level agreements" meet or exceed the NIST Cybersecurity Framework (Rule 60GG-2.001(3)(b); Fla. Stat. 282.318(4)(h)). Agencies must also require suppliers, by contract where necessary, to implement appropriate measures and must routinely assess them (Rule 60GG-2.002(6)).
- The current rule text (effective 2022-09-18) is modeled on NIST CSF version 1.1. The AC-01 and AC-03 contracts meet this duty by requiring the SP 800-53 Moderate baseline, which is more detailed than the CSF. **No separate rows** are needed; the Moderate rows cover it, and supplier assessment by the agencies is supported by the P09 readiness work.

### 1.5 Other rules considered
| Rule | Decision | Why |
|---|---|---|
| Fla. Stat. 501.171 | **Applies directly** | The company is a "third-party agent" (501.171(1)(h)). It must "take reasonable measures to protect and secure data in electronic form containing personal information" (501.171(2)) and notify the agency of a breach "no later than 10 days" after determining it (501.171(6)(a)). Tested through the IR rows and in P08 |
| Fla. Stat. 282.318, 282.3185, 282.3186 | Agency duties the company must support | State agencies and local governments must report ransomware incidents within 12 hours of discovery, and may not pay a ransom (282.3186). These are agency duties; the company's contracts require it to give the agency what it needs in time (P08) |
| SNAP (7 CFR 272.1(c)) and Medicaid (42 CFR 431.300-431.307) confidentiality | Reach AC-03 data by contract | Use and disclosure are limited to program administration; access is limited to persons under comparable confidentiality standards (431.306(b)). Covered by AC and PS rows |
| HIPAA Security Rule | Not applicable | No customer has designated the company a business associate; AC-03 placed its eligibility case functions outside its health care component (45 CFR 164.105) |
| GovRAMP (formerly StateRAMP) | Voluntary; assurance option | A verification program, not law. stateramp.org now redirects to govramp.org. Considered in P09 |
| CIRCIA | Proposed only | No final rule as of 2026-09-25. Not treated as an obligation |
| Driver's Privacy Protection Act; FAR 52.204-21 | Not applicable | No motor vehicle agency customers; no federal contracts |

## 2. Method
1. **Requirements.** One row per Moderate base control (177), from the repository copy of the SP 800-53 Rev. 5.2.0 catalog and its baseline flags. Overlay rows were added only where CJISSECPOL v6.1 or Pub. 1075 sets a value or duty beyond the base control text (12 CJIS rows, 15 Pub. 1075 rows). Each overlay row quotes or summarizes the section it cites; both documents are U.S. government works.
2. **Crosswalk.** CSF 2.0 subcategories come from NIST's official CSF 2.0 informative references to SP 800-53 Rev. 5.2.0 (`00_universal/crosswalks/csf2_to_sp800-53r5.csv`). 42 base controls have no informative reference and show none. Overlay rows are mapped by the author, and the `crosswalk_source` column says so. The `regulatory_driver` column shows which overlay also contains the control (Pub. 1075 section 4 does not include 18 of the 177 base controls, for example CP-6 and CP-7).
3. **Evidence.** Interviews (COO, IT Manager, Contracts and Compliance Manager, Director of Engineering, Cloud Operations Lead, Customer Support Manager, HR Manager), cloud and identity provider configuration exports, HR screening files, the AC-01 and AC-02 contracts, the 2025 penetration test report, and a headquarters walkthrough on 2026-08-05.
4. **Status.** Met, Partially met, Not met, or Not applicable. A control inherited from the FedRAMP-authorized cloud provider is rated Met when the company's use of the service falls inside the provider's authorization. Gap risk uses the P01 scale.

## 3. Results summary
| Family | Controls | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| AC Access Control | 17 | 6 | 10 | 0 | 1 |
| AT Awareness and Training | 4 | 0 | 3 | 1 | 0 |
| AU Audit and Accountability | 11 | 4 | 4 | 3 | 0 |
| CA Assessment, Authorization, and Monitoring | 7 | 1 | 5 | 1 | 0 |
| CM Configuration Management | 12 | 2 | 9 | 1 | 0 |
| CP Contingency Planning | 9 | 1 | 4 | 4 | 0 |
| IA Identification and Authentication | 10 | 4 | 6 | 0 | 0 |
| IR Incident Response | 8 | 1 | 5 | 2 | 0 |
| MA Maintenance | 6 | 2 | 3 | 0 | 1 |
| MP Media Protection | 7 | 3 | 3 | 0 | 1 |
| PE Physical and Environmental Protection | 16 | 14 | 2 | 0 | 0 |
| PL Planning | 6 | 1 | 5 | 0 | 0 |
| PS Personnel Security | 9 | 1 | 7 | 1 | 0 |
| RA Risk Assessment | 6 | 2 | 4 | 0 | 0 |
| SA System and Services Acquisition | 11 | 1 | 9 | 1 | 0 |
| SC System and Communications Protection | 18 | 11 | 6 | 0 | 1 |
| SI System and Information Integrity | 11 | 4 | 7 | 0 | 0 |
| SR Supply Chain Risk Management | 9 | 1 | 5 | 3 | 0 |
| **SP 800-53 Moderate subtotal** | **177** | **59** | **97** | **17** | **4** |
| CJIS Security Policy v6.1 overlay | 12 | 3 | 7 | 1 | 1 |
| IRS Pub. 1075 overlay | 15 | 4 | 8 | 3 | 0 |
| **Total rows** | **204** | **66** | **112** | **21** | **5** |

Of the 133 rows with a gap, 38 are rated High, 49 Moderate, 41 Low, and 5 Very Low. All 16 Physical and Environmental controls for the production facilities are inherited from the cloud provider; only the office and remote-work rules (PE-1, PE-17) are gaps.

## 4. Priority gaps and roadmap
The High gaps fall into seven themes. Each theme is carried into the risk register (P01) and the POA&M (P07).

| Theme | Rows | Action | Owner | Target |
|---|---|---|---|---|
| Unscreened staff with access to CJI and FTI | G-116, G-119, G-019, G-083, CJ-01, CJ-03, PB-01 | Remove access for the 4 unscreened staff now; finish fingerprint checks, Security Addendum certifications, Pub. 1075 investigations, and training; screening gate in onboarding | HR Manager | 2026-10-31 |
| FTI and CJI flowing to places they are not allowed | G-016, G-131, G-135, PB-04, PB-09 | Block regulated attachments to the ticketing vendor; disclose the 2025 staging copy and the ticket exposure to the AC-01 disclosure officer; technical block on production data in non-production | Contracts and Compliance Manager; Director of Engineering | 2026-10-15 |
| Logging, retention, and monitoring | G-027, G-030, G-031, G-161, CJ-08, PB-10 | 7-year write-once log archive in a separate account; managed 24x7 detection | Cloud Operations Lead; IT Manager | 2026-12-31 |
| Recovery from ransomware or account compromise | G-053, G-055, G-056, G-059 | Immutable backups in a separate account and second U.S. region; contingency plan; quarterly restore tests | Cloud Operations Lead | 2026-12-31 (first full restore test 2027-01) |
| Privileged access and secrets | G-002, G-006, G-065 | Just-in-time administrator access; tenant-scoped support roles; secrets moved out of the pipeline | Cloud Operations Lead; Director of Engineering | 2027-01-31 |
| Cryptography | G-145, G-148, CJ-10, PB-07 | FIPS 140-3 certified modules for CJI in transit by the CJIS date; module inventory; SLA amendment with AC-01 | Cloud Operations Lead | 2026-09-21 (CJI paths), 2026-12-31 (all) |
| Incident reporting to agencies | G-074, G-076, CJ-09, PB-11 | P08 runbook and notification matrix; 1-hour internal reporting rule; tabletop with AC-01 and AC-02 | Contracts and Compliance Manager | 2026-11-30 |

Also High: vulnerability scanning and patch deadlines (G-126, G-159), outbound network filtering (G-004, G-144), and supplier reviews (G-173).

The full list, with evidence, is in `gap-analysis.csv`.

## 5. Pending and dated changes
- **CJIS FIPS 140-2 cutoff.** CJISSECPOL v6.1 SC-13 states that FIPS 140-2 certificates "will not be acceptable after September 21, 2026." This date falls three weeks after approval; the CJI transmission paths are scheduled to switch by then (CJ-10).
- **CJIS zero-cycle end.** [Priority 2] to [Priority 4] requirements become sanctionable in audits after **2027-09-30**. The AC-02 contract already requires them.
- **New CJISSECPOL versions.** The Security Addendum binds the company to "all subsequent versions." CJ-02 adds a 60-day review of each new version.
- **Pub. 1075.** Rev. 11-2021 remains the edition at irs.gov. Recheck each July before the SSP review.
- **CIRCIA.** Proposed rule only (89 FR 23644). The proposed size-based criterion would not reach an SBA-small company; the sector criteria must be rechecked when a final rule is published.
- **SP 800-53.** Release 5.2.0 is current. Future releases will be picked up at the annual SSP review.
