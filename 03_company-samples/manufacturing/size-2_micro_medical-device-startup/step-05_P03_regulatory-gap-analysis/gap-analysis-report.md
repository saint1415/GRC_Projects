# Regulatory Gap Analysis: Cris Santos Company | Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| Tier / Vertical | Micro / Manufacturing (NAICS 334510) |
| Primary regulation | FD&C Act section 524B, ensuring cybersecurity of devices (21 U.S.C. 360n-2), with the FDA regulations and guidance that carry it out |
| Focus | **Premarket readiness** for the first 510(k) (target 2027-03-31): threat model, SBOM, cybersecurity management plan |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessors | QA/RA Manager and Head of Engineering, with the regulatory consultant |
| Approved | 2026-08-31 by the CEO |

## 1. Applicability
**Section 524B applies to the planned 510(k).** Section 524B(a) covers any person who submits a 510(k), PMA, PDP, De Novo, or HDE for a device that meets the "cyber device" definition in 524B(c). A cyber device:
1. includes software validated, installed, or authorized by the sponsor as a device or in a device;
2. can connect to the internet; and
3. has technological characteristics that could be vulnerable to cybersecurity threats.

WM-1 meets all three. The sensor and hub run firmware, the hub uses Wi-Fi to reach the cloud service, and the sensor uses Bluetooth Low Energy. FDA's guidance lists Wi-Fi, Bluetooth Low Energy, and cloud connections among the features that give a device the "ability to connect to the internet" (section VII.B). The section took effect 90 days after enactment on 2022-12-29 (Pub. L. 117-328, section 3305(d)), long before this submission.

- **No size exemption.** The statute has no headcount or revenue threshold. The only exemption is an FDA list under 524B(d); none covers WM-1.
- **Enforcement.** Failure to comply with 524B(b)(2) is a prohibited act under 21 U.S.C. 331(q)(3).
- **Related systems.** FDA considers related systems to include manufacturer-controlled update servers and connections to health care facility networks (guidance section VII.C.2). For this company, that brings the cloud service's update function, the CI pipeline, the signing key, and the contract manufacturer's provisioning step into scope.

**The QMSR applies even though production is outsourced.** 21 CFR Part 820 took effect on 2026-02-02 (final rule 89 FR 7496, published 2024-02-02). Section 820.1(a) applies it to manufacturers engaged in the design of finished devices and names specification development. The 820.3 definition of manufacturer includes anyone who designs a finished device. Section 820.10(c) requires ISO 13485 design and development controls (clause 7.3) for class II devices. A manufacturer that performs only some operations complies with the requirements for those operations (820.1(a)). The company therefore owns design controls, purchasing controls over the contract manufacturer, and records, while the contract manufacturer runs production controls under the quality agreement. FDA's guidance treats cybersecurity as part of the QMSR (section IV.A).

**What is binding and what is not:**
- **Binding:** the statute; 21 CFR Part 820; Parts 803 and 806 once the device is in commercial distribution.
- **Nonbinding:** FDA's guidance. The guidance rows are rated because FDA uses them to judge whether a submission shows a reasonable assurance of cybersecurity. They are recommendations. The guidance used:
  - *Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions*, issued 2026-02-03 (supersedes the June 27, 2025 version; verified from the FDA PDF)
  - *Postmarket Management of Cybersecurity in Medical Devices*, December 2016 (cited by the 2026 guidance for controlled and uncontrolled risk)

**Rules that apply only after marketing.** Medical device reporting (Part 803), corrections and removals (Part 806), and complaint records (820.35(a)) apply once WM-1 is in commercial distribution. They are rated here because the cybersecurity management plan must say how they will be used, and the procedures must exist before launch.

**Not analyzed, with reasons:**
- HIPAA Security Rule: the company holds no PHI today. It will become a business associate when hospital data flows into the cloud service after clearance. Planned in the P01 and P09 roadmaps, not rated here.
- DFARS, CMMC, ITAR, EAR (N31-33-R01 to R04): see `../00_company-facts.md` section 1.
- Guidance Appendix 3 (IDE documentation): no clinical investigation is planned (row G-042).

## 2. Method
1. **Requirements.** The 524B rows follow the statute's own structure: (a), (b)(1) through (b)(4), (c), and (d). QMSR rows cite the CFR section and the ISO 13485 clause number with a short topic label in our own words (ISO 13485 is copyrighted). Guidance rows cite the section of the 2026 guidance that says what FDA expects for each element.
2. **Crosswalk.** NIST has published no mapping for section 524B, Part 820, or the FDA guidance. Every row carries an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such.
3. **Documentary evidence.** Each status rests on a named document or record: the regulatory strategy memo, the design input document, the radio link threat spreadsheet, the component spreadsheet, the draft MDR and complaint procedures, the quality agreement, the supplier file, the draft labeling, and walkthroughs of the build and release process (2026-07-22). Interviews covered the Head of Engineering, Firmware Engineer, Cloud Software Engineer, Verification and Test Engineer, QA/RA Manager, and the regulatory consultant.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. For a premarket company, "Not met" usually means "not yet written," and the target date is set against the submission date.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FD&C Act section 524B (statute) | 11 | 1 | 2 | 6 | 2 |
| QMSR (21 CFR Part 820) | 9 | 0 | 8 | 1 | 0 |
| FDA regulations after marketing (21 CFR 803, 806) | 2 | 0 | 1 | 1 | 0 |
| FDA premarket guidance (2026-02-03) | 20 | 0 | 5 | 13 | 2 |
| FDA postmarket guidance (Dec. 2016) | 1 | 0 | 1 | 0 | 0 |
| **Total** | **43** | **1** | **17** | **21** | **4** |

The 38 unmet or partially met rows break down by gap risk as 15 High, 15 Moderate, and 8 Low.

**What the numbers say.** The engineers built the security features they know (secure boot, signed updates, TLS). The company has not built the **documents and processes** section 524B asks for: nothing records what the threats are, what software is inside, who watches for new vulnerabilities, or how a fix reaches the field. That is normal for a 7-person startup 8 months before submission, and it is fixable, but it is the critical path: most High gaps must close before design freeze (2026-12-31), because the fixes change the design.

**Three findings would stop a submission on their own:**
1. **Shared secrets on every unit** (G-032, G-033). One maintenance password and one API key for every hub contradict the guidance directly.
2. **No SBOM and no vulnerability analysis** (G-009, G-028, G-029). The statute requires the SBOM.
3. **No plan** (G-003, G-004, G-040). The statute requires the postmarket plan with coordinated vulnerability disclosure.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared hub password and API key | Guidance App. 1 (authentication, cryptography); 524B(b)(2) | High | Per-device credentials and certificates provisioned at the contract manufacturer | Firmware Engineer | 2026-12-31 |
| Signing key on a laptop | Guidance App. 1 (cryptography); 524B(b)(2) | High | HSM-backed key, two-person approval, release pipeline | Head of Engineering | 2026-12-31 |
| No CVD policy or security contact | 524B(b)(1) | High | Publish CVD policy; intake in the eQMS; join an ISAO | Head of Engineering | 2026-10-31 |
| No system threat model | Guidance V.A.1; 524B(b)(2) related systems | High | Full system threat model including the update path and contract manufacturer provisioning | Head of Engineering | 2026-11-30 |
| No security design inputs | 820.10(c) (ISO 13485 cl. 7.3.3) | High | Security requirements traced to controls and tests | Head of Engineering | 2026-11-30 |
| No SBOM or vulnerability analysis | 524B(b)(3); guidance V.A.4 | High | SBOM in every CI build; composition analysis; KEV check | Head of Engineering | 2026-12-31 |
| No cybersecurity risk assessment | Guidance V.A.2 | High | Exploitability-based assessment linked to the safety file | Head of Engineering | 2026-12-31 |
| No management plan | 524B(b)(1); guidance VI.B | High | Controlled QMS document with all VI.B elements | Head of Engineering | 2026-12-31 |
| No security testing | Guidance V.C; 820.10(c) (cl. 7.3.6) | High | Static and composition analysis in CI; fuzzing; third-party penetration test and retest | Verification and Test Engineer | 2027-01-31 |
| Unauthenticated BLE pairing | Guidance V.A.3 | Moderate | Authenticated pairing and message authentication | Firmware Engineer | 2026-12-31 |
| No security terms with the contract manufacturer | 820.10(a) (ISO 13485 cl. 4.1.5, 7.4) | Moderate | Quality agreement security terms; controlled provisioning transfer | QA/RA Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan (premarket readiness roadmap)
The plan fits a 7-person company: engineers write the design records as part of the design work, the regulatory consultant reviews them, and a test lab provides the independent testing. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed |
|---|---|---|---|
| 1. Intake and quick fixes | 2026-10-31 | CVD policy and security contact; ISAO membership; rotate the leaked API key; maintenance page off by default on evaluation units | G-004, G-043 |
| 2. Design records | 2026-11-30 | System threat model; security design inputs; secure product development procedure; QMS manual update on outsourced operations; pre-submission meeting request | G-005, G-006, G-012, G-013, G-014, G-023, G-024 |
| 3. Design changes before freeze | 2026-12-31 | Per-device credentials and certificates; authenticated BLE; maintenance page off by default; HSM-backed signing; SBOM in CI with support data; composition analysis; cybersecurity risk assessment; architecture views; management plan; contract manufacturer security terms and provisioning transfer | G-003, G-009, G-015, G-016, G-017, G-018, G-025 to G-029, G-032, G-033, G-034, G-036, G-037, G-040 |
| 4. Verification and postmarket procedures | 2027-01-31 | Third-party penetration test and retest; security review of anomalies; patch cycle and out-of-cycle procedure; metrics; security event logging; release tooling validation; complaint, MDR, and correction procedures with cybersecurity decision points | G-007, G-008, G-019 to G-022, G-030, G-031, G-035, G-038 |
| 5. Submission | 2027-02-26 | Assemble the cybersecurity section; customer security labeling; consultant review | G-002, G-039 |

**Progress check.** The QA/RA Manager reports progress to the CEO at a monthly 30-minute meeting, using the P07 POA&M and this roadmap. Any item that slips past design freeze is escalated because it will move the submission date (P01 R-003).

## 6. Pending regulatory changes
- **Section 524B(b)(4) regulations.** FDA may add cybersecurity requirements by regulation. None were found as of 2026-09-25. Recheck before submission.
- **FDA guidance updates.** The premarket guidance was issued in September 2023 and revised in June 2025 and February 2026. Recheck the current version before the pre-submission meeting and again before submission.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**. It does not apply to the company today. If finalized as proposed before the company becomes a business associate, it would shape the cloud service program (for example, MFA, encryption, and a written asset inventory and network map).
- **CIRCIA:** proposed rule only; not in effect.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these proposals is treated as a current obligation.
