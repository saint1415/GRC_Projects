# Regulatory Gap Analysis: Cris Santos Company | Commercial Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| Tier / Vertical | Small / Commercial Facilities (NAICS 531120) |
| Primary benchmark | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary** |
| OT tailoring | NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (final) |
| Secondary standard (binding by contract) | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (October 2024) (C-COMMERCIAL-FACILITIES-R01) |
| Legal baseline | FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02); Fla. Stat. 501.171(2) and (8) |
| Assessment dates | 2026-07-13 to 2026-07-24 (property walkthroughs 2026-07-15 to 2026-07-17) |
| Assessors | IT Manager with the Director of Engineering, Security Manager, and Controller |

## 1. Applicability

### 1.1 What the vertical names, and what binds this company
The vertical overlay names the CISA CPGs, with PCI DSS for payment environments, because **no mandatory sector-specific cybersecurity regulation exists for commercial facilities**. Each candidate was checked for this company:

| Candidate | Applies? | Reason |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 states that the goals are not "Mandated by CISA" and that CISA intends organizations "to voluntarily adopt" them. There are no size tiers: the goals apply to "all critical infrastructure organizations". The COO adopted CPG 2.0 as the company's baseline on 2026-07-10 |
| PCI DSS v4.0.1 (R01) | **Yes, by contract** | The company is a merchant (about 2,100 card transactions a year) and its merchant agreement requires PCI DSS compliance. PCI DSS is an industry standard, not law. Validation type is set by the acquirer, not by PCI SSC |
| FTC Act Section 5 (R02) | **Yes** | No size threshold. It reaches unreasonable data security and misleading statements about data practices |
| Fla. Stat. 501.171 | **Yes** | The company is a "covered entity" (a commercial entity that acquires, maintains, stores, or uses personal information; 501.171(1)(b)). Subsection (2) requires "reasonable measures to protect and secure data in electronic form containing personal information"; subsection (8) requires disposal of customer records. Notice duties are in P08 |
| CCPA/CPRA (R03) | No | The company does not do business in California, and its $20.4 million revenue is below the CPI-adjusted $26,625,000 threshold |
| SEC cybersecurity disclosure (R04) | No | Privately held; not an Exchange Act reporting company |
| CIRCIA (R06) | No (proposed rule only) | No final rule as of 2026-09-26. The NPRM (89 FR 23644, 2024-04-04) proposes **no sector-based criterion for the Commercial Facilities Sector** and relies on the size-based criterion (exceeding the SBA size standard). The company is under its $34.0 million SBA standard, so it would not be covered as proposed |

**Decision.** The binding rules (Florida's "reasonable measures", FTC Section 5) do not say what reasonable security is. The company therefore uses CPG 2.0, the Sector Risk Management Agency's own baseline, to define it, tailored for OT with SP 800-82 Rev. 3. PCI DSS is analyzed as the secondary standard because it is the only binding control set. The CPG rows are rated like requirements so the roadmap can show gaps, but **a CPG gap is not a compliance violation.**

### 1.2 CPG 2.0 version and structure (verified)
Verified on cisa.gov (the CPG 2.0 page and the CPG 2.0 Report, *Cross-Sector Cybersecurity Performance Goals, Version 2.0*, December 2025; the report page is dated 2025-12-11):
- CPG 2.0 replaces CPG 1.0.1 and adds a GOVERN function to align with NIST CSF 2.0.
- **34 goals** in six functions: 1 Govern (1.A-1.E), 2 Identify (2.A-2.E), 3 Protect (3.A-3.S), 4 Detect (4.A-4.B), 5 Respond (5.A-5.B), 6 Recover (6.A). Goal IDs were renumbered from CPG 1.0.1 (for example, v1.0.1 2.F segmentation is now 3.I).
- CPG 2.0 folded the OT-only goals of v1.0.1 into universal goals and added "OT:" guidance lines within goals. The OT lines were used in this analysis.
- Each goal lists NIST CSF 2.0 references, which were used for the crosswalk.

### 1.3 PCI DSS scope and SAQ
- **Card channels.** Card-present and phone bookings at the Property A and Property B management offices, only through 3 terminals from a validated PCI-listed P2PE solution. Rent is paid by ACH. Parking is the parking operator's own merchant account and is **outside the company's PCI scope** (it is a vendor-risk item, P01 R-015).
- **SAQ.** The acquirer requires an annual **SAQ P2PE**. The *PCI DSS v4.0.1 SAQ P2PE* exists (publication date October 2024). Its eligibility criteria: all processing through a validated PCI-listed P2PE solution; the only systems that handle account data are the solution's terminals; the merchant "does not otherwise receive, transmit, or store account data electronically"; any retained data is on paper; and all P2PE Instruction Manual (PIM) controls are implemented. The SAQ covers requirements 3 (paper only), 9.4 (paper only), 9.5, 12.1, 12.6, 12.8, and 12.10.1.
- **Eligibility finding.** Three emails with card numbers were found in the events mailbox, and the PIM inspection and training controls are not done. Both conflict with the eligibility statements. The Controller will not sign the 2026 SAQ P2PE until G-035 is closed and the acquirer confirms the path.
- PCI DSS v4.0.1 is still the current version. PCI SSC ran a request for comments on v4.0.1 from 2026-06-03 to 2026-07-20 toward a next version.

## 2. Method
1. **Requirements.** CPG rows are the 34 goals at goal level, citing the goal ID; summaries paraphrase the goal and its OT line. PCI DSS rows are the eligibility statement plus the 21 requirements listed in the v4.0.1 SAQ P2PE (9.5.1.2.1 is marked "intentionally left blank" in that SAQ). PCI DSS is copyrighted, so rows list requirement numbers with short topic labels written for this analysis; read the official standard for the text. Legal rows cite the statute.
2. **Crosswalk.** CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset selected by the author from the CPG's own references. For goal 3.O, CPG 2.0 lists PR.IR-01 and DE.CM-01, which repeat goal 3.I; an author mapping (PR.DS-11; CP-9, CP-4, CP-10) is used instead and labeled. PCI and legal rows are author mappings.
3. **Evidence.** Interviews (COO, Director of Engineering, 3 chief engineers, Security Manager, Controller, events coordinator, BAS integrator); document review (contracts, the 2025 SAQ P2PE, processor agreement, MSP diagrams); configuration exports (firewalls, identity provider, access control platform roles, backup jobs); the MSP external scan of 2026-07-16; a mailbox search on 2026-07-22; and walkthroughs of all three properties.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 1 | 2 | 2 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 0 | 4 | 1 | 0 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 0 | 14 | 5 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 0 | 1 | 0 |
| **CPG 2.0 subtotal** | **34** | **1** | **24** | **9** | **0** |
| PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) | 22 | 3 | 9 | 9 | 1 |
| Legal baseline (15 U.S.C. 45(a); Fla. Stat. 501.171(2), (8)) | 3 | 0 | 2 | 1 | 0 |
| **Total** | **59** | **4** | **35** | **19** | **1** |

The 54 unmet or partially met rows break down by gap risk as 4 High, 27 Moderate, and 23 Low. All four High gaps are CPG goals (1.E, 3.F, 3.I, 3.O).

**The pattern.** The office IT is in reasonable shape (MFA, EDR, patching, a cloud access control platform). **The building systems were never treated as IT**, and almost every Not met CPG row is an OT gap:
- The integrator reaches the BAS through an always-on tool with a shared account and no MFA (1.E, 3.C, 3.F).
- OT devices share networks with office PCs (3.I), have default passwords (3.A), and are neither inventoried (2.A, 2.E) nor logged (3.Q).
- The BAS could not be rebuilt: no isolated backups, no controller programs, no manual procedures (3.O, 6.A).

**PCI DSS findings are about paper and email, not systems.** The P2PE terminals keep card data out of company systems, but the events desk works around them.

## 4. Priority gaps and roadmap
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Integrator remote access without MFA or approval | CPG 1.E, 3.F | High | Remote access gateway with named accounts, MFA, per-session approval, recording | Director of Engineering | 2026-10-31 |
| No OT segmentation | CPG 3.I | High | OT segments with deny-by-default rules at all three properties (SP 800-82 Rev. 3 zones) | IT Manager | 2027-03-31 |
| BAS backups not isolated, incomplete, untested | CPG 3.O | High | Immutable separate-account backups; controller programs after each change; quarterly restore test | IT Manager | 2026-12-31 |
| Card data in email; PIM controls missing | SAQ P2PE eligibility | Moderate | Purge and block; PIM controls; confirm with the acquirer | Controller | 2026-10-31 |
| Card data and security codes on paper | PCI DSS 3.2.1, 3.3.1.2, 9.4.1, 9.4.6 | Moderate | Stop paper capture; shred binder | Controller | 2026-09-30 |
| Default passwords on OT devices | CPG 3.A | Moderate | Change defaults; commissioning checklist | Director of Engineering | 2026-09-30 |
| Shared accounts in BAS, integrator, and guard access | CPG 3.C | Moderate | Named accounts | Director of Engineering | 2026-12-31 |
| No degraded-mode or recovery procedures | CPG 6.A | Moderate | Manual operating procedures per property | Director of Engineering | 2026-12-31 |
| No vendor incident notice clauses | CPG 1.D | Moderate | Security addendum with 24-hour notice | COO | 2026-12-31 |
| Visitor ID scans kept indefinitely | Fla. Stat. 501.171(8) | Moderate | Retention schedule and purge | Security Manager | 2026-11-30 |
| No central logging | CPG 3.Q | Moderate | MSP log service, 1-year retention | IT Manager | 2027-01-31 |

**Before signing the 2026 SAQ P2PE:** close G-035 to G-040 and G-042 to G-046 (eligibility, paper data, and PIM controls), and record the acquirer's confirmation. If card data is found in email again, the company is not eligible for SAQ P2PE for that channel and must ask the acquirer how to validate.

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **CIRCIA:** the final rule was not published as of 2026-09-26. If the final rule keeps the NPRM's approach, the company stays out of scope. If it adds a Commercial Facilities sector criterion (the NPRM said CISA would consider revenue or employee thresholds), the P08 matrix must add 72-hour incident and 24-hour ransom payment reports to CISA. CPG 5.B already points reporting toward CISA voluntarily.
- **PCI DSS:** the June-July 2026 request for comments starts work on the next version. No publication date was found. v4.0.1 remains in force.
- **NIST SP 800-82 Rev. 4** is an initial public draft (2026-09-21). It is not used; Rev. 3 remains the final guide.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

None of these is treated as a current obligation.
