# Regulatory Gap Analysis: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor, NAICS 562211) |
| Tier / Vertical | Small / Nuclear Reactors, Materials, and Waste |
| Vertical's primary regulation | 10 CFR 73.54 (with RG 5.71 Rev. 1 controls): **not applicable** (section 1) |
| Regulation analyzed | **10 CFR Part 37**, Physical Protection of Category 1 and Category 2 Quantities of Radioactive Material, as imposed on the company by its Florida radioactive materials license condition. Text checked on eCFR (version date 2026-09-23) |
| Secondary benchmark | NIST Cybersecurity Framework (CSF) 2.0, with NIST SP 800-82 Rev. 3 (Guide to OT Security, September 2023) for the plant OT and physical security systems. Voluntary |
| Assessment dates | 2026-07-13 to 2026-07-24 (Plant walkthrough 2026-07-21) |
| Assessor | IT Manager with the Radiation Safety Officer (RSO) and the Compliance and Transportation Manager |
| Workbook | `gap-analysis.csv` (85 rows: G-001 to G-004 reactor rule applicability, G-005 to G-065 Part 37, G-066 to G-085 CSF 2.0 OT benchmark) |

## 1. Applicability

### 1.1 The vertical's primary regulation does not apply
**10 CFR 73.54 does not apply.** The section applies to "each licensee currently licensed to operate a nuclear power plant under part 50" and to combined license holders and applicants under Part 52. The company holds a Florida materials license for waste processing and disused sources. It operates no reactor. For the same reason:
- **10 CFR 73.77** (cyber security event notifications) does not apply. It covers "each licensee subject to the provisions of § 73.54 or § 73.110."
- **10 CFR 73.110** (Part 53 plants) does not apply.
- **Safeguards Information (10 CFR 73.21-73.23)** does not apply. The company is not in any category listed in 73.21(a)(1)(i)-(ii) and does not produce, receive, or acquire SGI. If a reactor customer ever sent SGI, 73.21(a)(1)(iii) would apply to that information.
- **NERC CIP** does not apply. The company is not a NERC-registered entity.
- **CIRCIA** is not in effect: no final rule was published as of 2026-09-25. As proposed (89 FR 23644, proposed 6 CFR 226.2), it would cover critical infrastructure entities that exceed the SBA size standard or meet a sector criterion. The company is below the $47.0 million standard for NAICS 562211. The nuclear criterion covers entities that own or operate "a commercial nuclear power reactor or fuel cycle facility," which the company does not.

These results are recorded as rows G-001 to G-004. Reactor rules can still reach the company through **customer contracts**. Its 2 reactor customers require field crews to follow the reactor sites' access and portable media rules, which come from those customers' own 73.54 programs. These are contract obligations, not regulatory ones. They are handled in POL-05 and P01 R-024.

### 1.2 What the NRC and Florida actually require of this business
**Florida licenses the company, not the NRC.** Florida is an NRC Agreement State (agreement effective 1964, per the NRC Agreement State page for Florida). The Florida Department of Health, Bureau of Radiation Control, licenses and inspects the company under Chapter 64E-5, F.A.C.

**No cyber-specific rule applies to this license.** No NRC or Florida cybersecurity rule for byproduct material licensees like 10 CFR 73.54 was found. The security-relevant binding rule is **10 CFR Part 37**, which Florida applies through a standard license condition. Per Florida's 2023 submission to the NRC (ADAMS ML23178A117):
- The condition requires compliance with Part 37 "except as follows": 37.1, 37.3, 37.7, 37.9, 37.11(a)-(b), 37.13, 37.77(f), 37.105, 37.107, and 37.109 are excluded.
- References to the Commission or NRC are read as the Florida Department of Health, with listed exceptions: fingerprints still go through the NRC Criminal History Program, and license verification may still use the NRC system.
- Event reports under 37.57 and 37.81 go to the Bureau of Radiation Control.

The company's own license must be checked for the exact current wording.

**Why Part 37 applies: the license scope.** Part 37 Subparts B and C apply to anyone who "possesses or uses at any site, an aggregated category 1 or category 2 quantity of radioactive material" (37.3(a)).
- The company's disused sealed source vault holds Cs-137, Co-60, and Am-241/Be sources. Sum-of-fractions against Appendix A reaches the category 2 threshold (for example 27.0 Ci of Cs-137 or 8.10 Ci of Co-60) several times a year before quarterly outbound shipments.
- The license authorizes an aggregated category 2 quantity, and no category 1 quantity.
- Subpart D applies because the company delivers category 2 shipments to a carrier (37.3(b)).

**The waste exemption does not help.** Section 37.11(c) exempts radioactive waste containing category 1 or 2 quantities from Subparts B, C, and D if four security measures are met. However, "any radioactive waste that contains discrete sources, ion-exchange resins, or activated material that weighs less than 2,000 kg (4,409 lbs) is not exempt." The vault holds discrete sources, so it is fully subject. The bulk resin liner pad also falls under the non-exempt categories. It has stayed below category 2 in practice, but that has never been documented (G-005).

**What Part 37 requires that touches information security.** Part 37 is a physical protection rule, but four of its duties are information security duties in practice:
- **37.43(d)** protection of the security plan, implementing procedures, and the list of approved individuals: need-to-know, trustworthiness and reliability checks, an access list, written procedures, and "Information stored in nonremovable electronic form must be password protected."
- **37.31** protection of background investigation records and personal information.
- **37.49(c)** continuous and alternative data transmission and processing for the security systems, "not subject to the same failure modes as the primary systems."
- **37.101** safeguards "against tampering with and loss of records."

**Other binding rules considered and not decomposed here:**
- **Florida rules** (C-NUCLEAR-S02): Chapter 64E-5, F.A.C., including 64E-5.320 (security of stored sources), 64E-5.332 (transfer for disposal and manifests), 64E-5.343 (stolen, lost, or missing sources), and 64E-5.344 (incidents). They drive P08 notifications.
- **DOT hazmat security plan** (C-NUCLEAR-S03): 49 CFR 172.800(b)(15) requires a transportation security plan for NRC category 1 and 2 materials. Under 172.802(c), the plan must be available to employees "consistent with personnel security clearance or background investigation restrictions and a demonstrated need to know." The DOT plan sits in the same broadly shared folder, so the G-031 to G-036 fixes cover it too.
- **RCRA** (C-NUCLEAR-S04): Florida has an EPA-authorized hazardous waste program (base authorization effective 1985-02-12, 50 FR 3908; revisions effective 2026-05-26, 91 FR 14648). The company's permitted storage facility keeps an operating record and manifests under 40 CFR Part 264 Subpart E (264.71 to 264.74). These are record integrity and availability duties, used in the BIA (P05) and backup planning. They contain no cybersecurity control requirements.
- **Florida breach notification** (C-NUCLEAR-S06): Fla. Stat. 501.171 applies to employee and background investigation personal information (P08).

### 1.3 Why a voluntary OT benchmark is added
Part 37 does not address the plant OT network (PLCs, HMIs, historian) or cybersecurity of the security systems beyond communications continuity. Management adopted **CSF 2.0**, using **SP 800-82 Rev. 3** for OT-specific practice, as the benchmark for these systems (rows G-066 to G-085). SP 800-82 Rev. 3 treats physical access control systems as OT (section 2.3.6), which is why the PACS and video systems are assessed in both parts. SP 800-82 Rev. 3 section 6 is organized by CSF 1.1 categories; the CSF 2.0 subcategory chosen for each row is the author's mapping.

## 2. Method
1. **Requirements.** Part 37 rows follow the regulation's own structure: each paragraph that imposes a duty on this licensee, at the most granular citation that can be verified separately. Definitions, purpose, and enforcement sections excluded by the license condition are not rows, except 37.105, which is shown as not applicable. Brief quotes come from the public-domain eCFR text.
2. **Requirement type.** "Mandatory (license condition)" for Part 37. "Voluntary benchmark" for CSF rows.
3. **Crosswalk.** No official NIST mapping exists for Part 37, so the CSF 2.0 and SP 800-53 mappings are the author's. For the CSF rows, the SP 800-53 controls are a subset of NIST's official CSF 2.0 to SP 800-53 Rev. 5.2.0 reference.
4. **Evidence.** Interviews (General Manager, RSO, IT Manager, HR Manager, Operations Manager, Maintenance and Controls Supervisor, Compliance and Transportation Manager, a shift lead), document review (security plan Rev. 2, procedures, background files sampled 5 of 14, training and test records), configuration exports (folder permissions, remote access appliance, firewall, historian), and the Plant walkthrough.
5. **Status.** Met, Partially met, Not met, or Not applicable.

## 3. Results summary

### 3.1 10 CFR Part 37 (61 rows)
| Part 37 subpart | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| A General provisions (37.11(c)) | 0 | 1 | 0 | 0 | 1 |
| B Background investigations and access authorization (37.21-37.33) | 11 | 4 | 1 | 0 | 16 |
| C Physical protection during use (37.41-37.57) | 12 | 14 | 6 | 1 | 33 |
| D Physical protection in transit (37.71-37.81) | 4 | 3 | 0 | 1 | 8 |
| F-G Records and inspections (37.101-37.105) | 1 | 1 | 0 | 1 | 3 |
| **Total** | **28** | **23** | **7** | **3** | **61** |

**Pattern.** The physical program is sound: security zone, IDS, LLEA coordination, background investigations, carrier controls. The gaps fall where Part 37 meets IT. Six of the 7 Not met rows are **37.43(d) information protection** (G-031 to G-035, G-037). The other is the overdue access authorization review (G-021).

### 3.2 CSF 2.0 OT benchmark (20 rows)
| CSF 2.0 function | Met | Partially met | Not met | Total |
|---|---|---|---|---|
| Govern | 0 | 1 | 2 | 3 |
| Identify | 0 | 1 | 3 | 4 |
| Protect | 0 | 6 | 3 | 9 |
| Detect | 0 | 0 | 2 | 2 |
| Respond | 0 | 0 | 1 | 1 |
| Recover | 0 | 0 | 1 | 1 |
| **Total** | **0** | **8** | **12** | **20** |

No CSF row is fully met. That is typical for a small operator whose OT was installed by vendors and has never had a security owner.

### 3.3 Overall
Across all 85 rows: 28 Met, 31 Partially met, 19 Not met, and 7 Not applicable (4 reactor rules plus 37.53, 37.77/37.79(a)(1), and 37.105). Of the 50 gap rows, 10 are rated High, 30 Moderate, and 10 Low.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Security plan, procedures, and approved list readable by 23 users; no procedure; no access list | 37.43(d)(1)-(3), (5)-(6) | High | Restricted library; SEC-10 Information Protection procedure; information access list and determinations | Radiation Safety Officer | 2026-09-30 |
| PACS and video share the business network; no alternate path | 37.49(c)(1)-(2); 37.41(b); PR.IR-03 | High | Security VLAN with dedicated switches, firewall, and UPS; local annunciator; plan Rev. 3 | General Manager | 2026-12-15 |
| Historian dual-homed; security systems on business network | PR.IR-01 | High | Historian DMZ replica; security VLAN | IT Manager | 2026-12-31 |
| Vendor remote access with shared account, no MFA | PR.AA-03; DE.CM-06 | High | Per-session access, named accounts, MFA, recording | Maintenance and Controls Supervisor | 2026-10-31 |
| Part 37 records exposed to loss with production | 37.101 | High | Immutable separate-account backups; restore test including Part 37 records | IT Manager | 2026-12-31 |
| No OT or security-system incident plan | RS.MA-01; 37.57(b) | High | P08 runbook; SEC-09 cyber indicators; tabletop | IT Manager | 2026-11-30 |
| Event procedures name the NRC, not Florida | 37.57; 37.81 | Moderate | Correct SEC-05 and TR-06 | Radiation Safety Officer | 2026-09-30 |
| Background files open to payroll clerk | 37.31(a)-(b) | Moderate | Restricted library; procedure | HR Manager | 2026-09-30 |
| Late removal from the approved list | 37.23(e)(5) | Moderate | HR-triggered same-day removal; monthly reconciliation | HR Manager | 2026-10-31 |
| Overdue reviews | 37.33; 37.55 | Moderate | 2026 reviews covering electronic systems | Radiation Safety Officer | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Before the next State inspection:** the September 2026 items (information protection, background files, event contacts, overdue refresher training) cost staff time only and should be closed first.

## 5. Pending regulatory changes
The NRC proposed **"Modernizing Requirements Relating to Physical Protection of Category 1 and Category 2 Quantities of Radioactive Material"** (91 FR 17893, 2026-04-09; comments closed 2026-05-11; Docket NRC-2025-1238). It was **not final as of 2026-09-25**. As proposed, it would:
- stop requiring transmission of reviewing official certifications (37.23(b)(2)) and remove 10-year reinvestigations (37.25(c));
- change refresher training from every 12 months to at least every 3 years (37.43(c)(3)), and LLEA coordination from every 12 months to at least every 3 years (37.45(d));
- **remove weekly category 2 verification (37.49(a)(3)(ii)), the continuous and alternative communication and data transmission requirement (37.49(c)), and the maintenance and testing program (37.51)**;
- allow key removal for mobile devices (37.53(b)).

**It would not change 37.43(d), 37.31, or 37.101.** The information protection gaps remain mandatory whatever happens.

**Florida timing.** Florida applies Part 37 through its license condition, so any final NRC change reaches the company only when Florida updates the condition. The NRC says Agreement States "should also remove those requirements" to stay compatible. Until then, the current text applies.

**The company's position.** Even if 37.49(c) and 37.51 go away, 37.49(a)(1) still requires continuous monitoring and detection, or an alarm and response when that capability is lost. Management will therefore finish the security VLAN and PACS maintenance work under CSF PR.IR-03 and PR.PS-02, not only because of 37.49(c).

The `pending_rule_change` column flags each affected row. None of these proposals is treated as a current change. The NRC's other 2026 proposals under Executive Order 14300 (for example "Modernizing Materials Licensing," 91 FR 38124, and "Integrated Low-Level Radioactive Waste Disposal," 91 FR 40290) were noted, but their effect on this company was not analyzed.
