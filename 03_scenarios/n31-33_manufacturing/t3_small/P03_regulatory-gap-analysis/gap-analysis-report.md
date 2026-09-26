# Regulatory Gap Analysis: Cris Santos Company | Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| Tier / Vertical | Small / Manufacturing (NAICS 334510) |
| Primary regulation | FD&C Act section 524B, ensuring cybersecurity of devices (21 U.S.C. 360n-2), with the FDA regulations and guidance that carry it out |
| Secondary regulation | HIPAA Security Rule (45 CFR Part 164, Subpart C) and business associate breach notice (45 CFR 164.410), for the device cloud only |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessors | VP QA/RA and Product Security Lead (524B); IT Manager and Compliance Manager (HIPAA) |

## 1. Applicability
**Section 524B applies.** Section 524B(a) covers any person who submits a 510(k), PMA, PDP, De Novo, or HDE for a device that meets the "cyber device" definition in 524B(c). A cyber device:
1. includes software validated, installed, or authorized by the sponsor as a device or in a device;
2. can connect to the internet; and
3. has technological characteristics that could be vulnerable to cybersecurity threats.

How this applies to the company's products:
- **PM-2** meets all three criteria. Its 2024 510(k) was submitted after 524B took effect (90 days after enactment on 2022-12-29, per Pub. L. 117-328 section 3305(d)), so 524B applied to it.
- **AI-001** is planned for a 2027 Q3 submission and will also be a cyber device.
- **PM-1** was cleared in 2019, before the effective date. 524B does not reach that clearance. PM-1 remains subject to the QMSR, MDR, and correction reporting, and to FDA's postmarket cybersecurity expectations.
- **The device cloud** is a "related system" in the statute's words ("the device and related systems"). FDA's guidance says related systems include manufacturer-controlled update servers and connections to health care facility networks.

There is **no size exemption**. The only exemption route is an FDA list of exempt devices published under 524B(d), and no exemption applies here.

**Enforcement.** Failure to comply with 524B(b)(2) is a prohibited act under 21 U.S.C. 331(q)(3). The (b)(2) duty covers the processes that assure cybersecurity and the duty to make patches available.

**What is binding and what is not:**
- **Binding:** the statute and FDA's regulations (21 CFR 803, 806, and 820).
- **Nonbinding:** FDA's guidance documents. The guidance rows below are rated because FDA uses them to decide whether a submission shows a "reasonable assurance" of cybersecurity. They are recommendations, not requirements. The guidance used:
  - *Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions*, issued 2026-02-03 (it supersedes the June 2025 version)
  - *Postmarket Management of Cybersecurity in Medical Devices*, December 2016

**Secondary regulation: HIPAA.** The company is a business associate for the device cloud (`../scenario-facts.md` section 1). The Security Rule applies to it under 45 CFR 164.302, and 164.410 sets its breach notice duty to the hospitals. Excluded, with reasons:
- 164.314(b), group health plans: the company does not administer a group health plan for the hospitals.
- The Privacy Rule: this is a security gap analysis. Privacy duties flow through the BAAs and are handled by the Privacy Officer.

**Not analyzed:** the vertical's defense and export rules (N31-33-R01 to R04). See scenario facts section 1.

## 2. Method
1. **Requirements.** The 524B rows follow the statute's own structure: (a), (b)(1) through (b)(4), (c), and (d). FDA regulation rows cite the CFR section. Guidance rows cite the section of the guidance that explains what FDA expects to see for each statutory element.
2. **Crosswalk.** NIST has published no mapping for section 524B, so every 524B and FDA row carries an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5, labeled as such. HIPAA rows use the Health Care vertical's crosswalk (`02_verticals/n62_health-care/`), which is also an author mapping. NIST's official OLIR 110 controls are shown next to it for comparison.
3. **Evidence.** The current state comes from:
   - interviews with the VP QA/RA, VP Engineering, Product Security Lead, IT Manager, Cloud Operations Lead, and Compliance Manager
   - review of the PM-2 510(k) cybersecurity section, the SBOM, the threat model, the QMS procedures, and 40 BAAs
   - a build server walkthrough on 2026-07-16
4. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| FD&C Act section 524B (statute) | 11 | 0 | 7 | 2 | 2 |
| FDA regulations (21 CFR 803, 806, 820) | 4 | 0 | 4 | 0 | 0 |
| FDA guidance (premarket 2026, postmarket 2016) | 16 | 0 | 10 | 6 | 0 |
| HIPAA Security Rule (business associate scope) | 31 | 6 | 23 | 1 | 1 |
| HIPAA Breach Notification Rule (164.410) | 1 | 0 | 1 | 0 | 0 |
| **Total** | **63** | **6** | **45** | **9** | **3** |

The 54 unmet or partially met rows break down by gap risk as 13 High, 32 Moderate, and 9 Low.

**The main finding:** the company met section 524B *at submission time* for PM-2 and has not kept it up. The statute requires more than documents in a submission. It requires a plan to monitor and address vulnerabilities, processes that are maintained, and patches made available on a regular cycle. Today:
- the SBOM is stale;
- no CVD process exists;
- there is no patch cycle;
- the management plan has never been run.

Every one of these would surface in the AI-001 submission and in any FDA inspection of postmarket activity.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared service password on all PM-2 units; PM-1 shared API keys | Guidance App. 1; 524B(b)(2)(B) | High | Out-of-cycle release with unique credentials; customer advisory (P08) | VP Engineering | 2026-10-11 |
| No coordinated vulnerability disclosure | 524B(b)(1) | High | Publish CVD policy; intake in the eQMS; ISAO membership | Product Security Lead | 2026-10-31 |
| No uncontrolled-risk assessment or ISAO participation | Postmarket guidance (2016) | High | PSIRT procedure (P08); join an ISAO | VP QA/RA | 2026-10-31 |
| No out-of-cycle patch procedure | 524B(b)(2)(B) | High | Expedited release and verification path | VP Engineering | 2026-10-31 |
| No regular patch cycle | 524B(b)(2)(A) | High | Quarterly security maintenance release, justified in the management plan | VP Engineering | 2026-12-31 |
| Stale, single-product SBOM | 524B(b)(3) | High | Automated SBOM in every build | Product Security Lead | 2026-12-31 |
| Signing key without HSM; related systems not in threat model | 524B(b)(2) | High | HSM with two-person signing; extend threat model | VP Engineering | 2026-12-31 |
| Management plan not operated | 524B(b)(1) | High | Named owner, sources, weekly review, records | Product Security Lead | 2026-12-31 |
| Log analytics vendor holds PHI with no BAA | 164.308(b)(1), 164.314(a) | Moderate | Mask identifiers; BAA or replace | Compliance Manager (Privacy Officer) | 2026-10-31 |
| No review of device cloud activity | 164.308(a)(1)(ii)(D) | Moderate | Weekly review; alerts | IT Manager | 2026-11-30 |
| Cyber events missing from MDR and 806 decisions | 21 CFR 803.50, 806.10 | Moderate | Add cybersecurity decision points; train complaint handlers | VP QA/RA | 2026-11-30 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **Section 524B(b)(4) regulations.** FDA may add cybersecurity requirements by regulation. None were found as of 2026-09-25. Watch for any proposed rule.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**. The regulatory agenda projects a final rule in July 2027. If it is finalized as proposed, it would affect the device cloud:
  - MFA would be required (PM-1's shared keys and the absence of MFA on some paths would need attention).
  - Encryption at rest and in transit would be required, with limited exceptions.
  - A written technology asset inventory and network map would be required.
  - Certain systems would have to be restorable within 72 hours.
  - Business associates would have to give notice within 24 hours of activating their contingency plan.
  - A compliance audit would be required at least every 12 months.
- **FDA guidance updates.** The premarket guidance was issued in September 2023 and revised in June 2025 and February 2026. Recheck the current version before each submission.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. None of these proposals is treated as a current obligation.
