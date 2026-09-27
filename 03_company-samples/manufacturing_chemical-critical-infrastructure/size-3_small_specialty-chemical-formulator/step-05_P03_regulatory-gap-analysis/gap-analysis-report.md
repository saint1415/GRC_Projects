# Regulatory Gap Analysis: Cris Santos Company | Chemical | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical formulator and packager) |
| Tier / Vertical | Small / Chemical (NAICS 325998) |
| Primary benchmark | CFATS RBPS 8 (Cyber), 6 CFR 27.230(a)(8), with CISA's RBPS 8 security measures. **Voluntary** (CFATS authority lapsed) |
| OT benchmark | NIST CSF 2.0 with NIST SP 800-82 Rev. 3 (voluntary) |
| Secondary regulation (binding) | EPA Risk Management Program, Program 2, 40 CFR Part 68, for the elements that touch the control system |
| Assessment dates | 2026-07-13 to 2026-07-24 (plant walkthrough 2026-07-15); rows G-003, G-040, and G-052 updated 2026-08-14 after P07 testing |
| Assessor | IT Manager with the EHS Manager and the Controls Engineer |
| Regulatory status checked | 2026-09-26 (eCFR point-in-time 2026-09-23, Federal Register, cisa.gov, uscode.house.gov, csrc.nist.gov) |

## 1. Applicability
Applicability was decided first, from the plant's chemicals and quantities (`../00_company-facts.md`, threshold math). Four results:

**1. CFATS (6 CFR Part 27): would apply, but cannot be enforced.**
- The plant holds about 35,000 lb of hydrogen peroxide in 50% solution. Hydrogen peroxide is an Appendix A chemical of interest for theft and diversion at a minimum concentration of 35%, with a screening threshold quantity of 400 lb.
- The company filed a Top-Screen in 2008, was tiered, and ran an approved Site Security Plan.
- **Status on 2026-09-26:** CISA's CFATS page states that "As of July 28, 2023, Congress allowed the statutory authority for the Chemical Facility Anti-Terrorism Standards (CFATS) program (6 CFR Part 27) to expire" and that "CISA cannot enforce compliance with the CFATS regulations at this time." The U.S. Code shows 6 U.S.C. 621-629 as omitted. No reauthorization has been enacted. The House passed a bill in July 2023 that stalled in the Senate.
- **Decision:** RBPS 8 is used as a **voluntary benchmark**. It is still the only chemical-sector federal cyber performance standard, and the plant would be back in scope if Congress reauthorizes CFATS. Legacy CVI is still protected as a precaution (G-025).

**2. EPA RMP (40 CFR Part 68): applies, Program 2.**
- The aqueous ammonia process holds 23,925 lb of ammonia (11,000 gal x 7.50 lb/gal x 29%). The 40 CFR 68.130 listing "Ammonia (conc 20% or greater)" has a 20,000 lb threshold quantity, so the process is covered (68.10(a); 68.115).
- **Program 1 is not available:** the worst-case release reaches public receptors (68.10(j)(2)).
- **Program 3 does not apply:** NAICS 325998 is not in the 68.10(l)(1) list, and the process is not covered by OSHA PSM (68.10(l)(2)).
- **Result:** Program 2 (68.10(k)). The plant is a non-responding stationary source (68.90(b)).
- RMP is not a cyber rule. It is included because its hazard review, safety information, operating procedures, maintenance, and emergency notification elements all depend on the control system (G-041 to G-058).

**3. OSHA PSM (29 CFR 1910.119): does not apply.**
- 29% aqueous ammonia is below the Appendix A listing for ammonia solutions (above 44% by weight).
- 50% hydrogen peroxide is below the 52% listing.
- Hydrochloric acid is listed only as anhydrous, and sulfuric acid only as oleum.
- Isopropyl alcohol stays at 7,205 lb, under the 10,000 lb flammable liquid threshold in (a)(1)(ii).
- **Two limits keep it that way:** buy hydrogen peroxide below 52%, and keep isopropyl alcohol at or under 4 totes. Both are enforced through MOC (POL-01 4.11). Crossing either would also move the ammonia process into RMP Program 3.

**4. Other candidates, not applicable or not in force:**
- **USCG MTSA cybersecurity rule** (C-CHEMICAL-R02; 33 CFR Part 101 Subpart F): applies to facilities that must have a security plan under 33 CFR Part 105 (101.605(a)). The plant is inland with no marine transfer.
- **CIRCIA** (C-CHEMICAL-R03; proposed 6 CFR Part 226): no final rule in the Federal Register as of 2026-09-26, so no obligation exists. As proposed, the company (162 employees, under the SBA standard of 650) would fall under the size criterion. The CFATS-facility sector criterion is moot while CFATS is lapsed.
- **EAR:** the company ships only to U.S. customers and holds no controlled technology.

**Why a binding secondary regulation matters here.** Without CFATS, no federal rule requires this plant to secure its control system. The RMP is the closest binding hook: a manipulated DCS is an equipment malfunction the hazard review must consider (68.50(a)(2); author interpretation, G-045), and the emergency notification path must work when the business network is down (68.90(b)(3)).

## 2. Method
1. **Requirements.** RBPS 8 was decomposed into its text in 6 CFR 27.230(a)(8) (G-002 to G-006), CISA's published RBPS 8 security measures (G-007 to G-020), and related RBPS items that support cyber: (a)(12) personnel surety, (a)(15) and (a)(16) incident reporting and records, (a)(17) officials and organization, and 27.400 CVI (G-021 to G-025). The OT benchmark rows use CSF 2.0 subcategories with the matching SP 800-82 Rev. 3 section (G-026 to G-040). RMP rows follow the Part 68 section structure (G-041 to G-058).
2. **Crosswalk.** CFATS and RMP rows are mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author; no official NIST mapping exists for 6 CFR Part 27 or 40 CFR Part 68. OT benchmark rows use the official CSF 2.0 to SP 800-53 Rev. 5.2.0 mapping (`00_universal-framework/crosswalks/csf2_to_sp800-53r5.csv`).
3. **Evidence.** Interviews (Plant Manager, EHS Manager, Controls Engineer, Process Engineer, IT Manager, 3 Shift Supervisors, and the DCS integrator), document review, firewall and DCS exports, and the plant walkthrough.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CFATS RBPS text, 6 CFR 27.110-27.400 (voluntary) | 0 | 8 | 2 | 1 | 11 |
| CISA RBPS 8 security measures (voluntary guidance) | 1 | 4 | 9 | 0 | 14 |
| OT benchmark: CSF 2.0 with SP 800-82 Rev. 3 (voluntary) | 0 | 4 | 11 | 0 | 15 |
| EPA RMP Program 2, 40 CFR Part 68 (binding) | 8 | 10 | 0 | 0 | 18 |
| **Total** | **9** | **26** | **22** | **1** | **58** |

Of the 48 gaps (Partially met or Not met), **13 are High**, 28 are Moderate, and 7 are Low.

**Reading the results.** The plant does well on traditional process safety: 8 of the 9 Met rows are RMP elements (the ninth is G-019, backup power for critical cyber systems), and none of the RMP rows is Not met. It does poorly on the cyber side, with 22 Not met rows, all in the voluntary benchmarks. The 10 Partially met RMP rows are where the two worlds meet. The RMP program is sound, but it treats the DCS as trustworthy equipment.

## 4. Priority gaps and roadmap
All 13 High gaps are listed, in target date order.

| Gap | Rows | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| SIS writable from the DCS EWS; keyswitch left in program | G-040, G-052 | High | Keyswitch locked in run (done 2026-08-12); remove SIS software from the EWS; keyswitch step and second-person check in the proof test procedure | Controls Engineer | 2026-10-15 |
| Emergency notification depends on the business network | G-055 | High | Cellular phones, printed call lists, and a radio to the gate | EHS Manager | 2026-10-31 |
| Unmanaged, always-on integrator remote access | G-004, G-012 | High | Remote access gateway in an OT DMZ with named accounts, MFA, per-session approval, and recording; remote access standard (POL-02 4.6) | IT Manager | 2026-11-30 |
| No OT incident response capability | G-016 | High | OT runbook (P08) and a tabletop exercise | IT Manager | 2026-11-30 |
| Control logic and recipe changes outside MOC | G-032 | High | Configuration baseline; MOC covers control system changes; two-person recipe approval | Process Engineer | 2026-11-30 |
| No attribution of changes in the control room | G-003 | High | Unique DCS accounts; media scanning station | Controls Engineer | 2026-12-31 |
| OT backups share the fate of the DCS; recovery would take weeks | G-020, G-036 | High | Offline immutable copies; OT contingency plan; quarterly restore test on spare hardware | Controls Engineer | 2026-12-31 |
| No owner or program for OT security since the lapse | G-002 | High | Adopt this benchmark and the P07 POA&M as the plant cyber program | VP Operations | 2026-12-31 |
| Business network can reach the DCS | G-035 | High | OT DMZ, historian replica, deny-by-default rules | Controls Engineer | 2027-01-31 |
| Cyber-initiated malfunctions missing from the RMP hazard review | G-045 | High | Add control system compromise scenarios (P01 R-001, R-002, R-007) to a hazard review revalidation | EHS Manager | 2027-03-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

**Roadmap by quarter:**
- **2026 Q4 (quick wins and the remote access path):** SIS hardening, cellular notification, termination checklist for OT accounts, remote access gateway, MOC screening question, advisory subscriptions, OT tabletop.
- **2027 Q1 (architecture and recovery):** OT DMZ and firewall rebuild, offline backups and restore testing, passive monitoring sensor, OT training for all production staff, hazard review revalidation.
- **2027 Q2-Q4 (lifecycle):** quarterly patching with compensating controls, DCS upgrade at the 2027 turnaround with security requirements and a hazard review before startup (G-017, G-048), security network segment for cameras and badges (G-006).

## 5. Pending regulatory changes
None of these is treated as a current obligation.
- **CFATS reauthorization.** If Congress reauthorizes CFATS, RBPS 8 becomes enforceable again for tiered facilities, and CISA would contact facilities about next steps. The benchmark rows here would become the starting point for a Site Security Plan update. Status checked 2026-09-26: not reauthorized.
- **CIRCIA final rule (proposed 6 CFR Part 226; NPRM 89 FR 23644, 2024-04-04).** The proposed rule would require covered entities to report covered cyber incidents within 72 hours and ransom payments within 24 hours. CISA held more town halls in 2026 (91 FR 6794; 91 FR 30498). No final rule has been published. Recheck the size and sector criteria when it is final.
- **EPA RMP proposal (91 FR 8970, 2026-02-24; comments closed 2026-04-10).** "Accidental Release Prevention Requirements: Risk Management Programs Under the Clean Air Act; Common Sense Approach to Chemical Accident Prevention," a proposed rule that would revise Part 68. Rows G-043, G-046, G-053, G-055, and G-057 are flagged. Until a final rule is published, the current Part 68 text governs. This includes the 2027-05-10 compliance date for standby power for release monitoring equipment (68.10(g)(1)), which G-046 already meets.
- **NIST SP 800-82 Rev. 4 (initial public draft, 2026-09-21; comments due 2026-11-30).** This is a draft. The benchmark stays on Rev. 3 (September 2023) until Rev. 4 is final, and then the section references in G-026 to G-040 should be rechecked.
