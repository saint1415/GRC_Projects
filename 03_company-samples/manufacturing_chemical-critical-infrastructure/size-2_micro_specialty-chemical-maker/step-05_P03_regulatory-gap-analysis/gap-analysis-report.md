# Regulatory Gap Analysis: Cris Santos Company | Chemical | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (specialty chemical maker) |
| Tier / Vertical | Micro / Chemical (NAICS 325998) |
| Primary benchmark | CFATS RBPS 8 (Cyber), 6 CFR 27.230(a)(8), with CISA's RBPS 8 security measures. **Voluntary** (CFATS authority lapsed; the facility was never tiered) |
| Binding rules analyzed | DOT Hazardous Materials Regulations offeror duties that depend on the company's systems and people; CERCLA and EPCRA release notification. EPA RMP and OSHA PSM applicability |
| Assessment dates | 2026-07-13 to 2026-07-24 (site walkthrough 2026-07-15) |
| Assessor | Office Manager (Security Coordinator) with the Operations Manager; MSP lead technician and control system integrator interviewed |
| Regulatory status checked | 2026-10-05 (eCFR point-in-time 2026-09-23, Federal Register API, uscode.house.gov) |
| Approved | 2026-08-31 by the Owner and President |

## 1. Applicability
Applicability was decided first, from the company's chemicals and quantities (`../00_company-facts.md`, threshold math). Five results:

**1. CFATS (6 CFR Part 27): does not apply, and could not be enforced if it did.**
- The company holds up to 2 totes of 35% hydrogen peroxide: 5,170 lb of solution containing about 1,810 lb of hydrogen peroxide. Hydrogen peroxide is an Appendix A theft/diversion-EXP/IEDP chemical with a minimum concentration of 35% and an STQ of 400 lb, counted only in transportation packagings such as totes (6 CFR 27.203(c); 27.204(b)(3); 72 FR 65396). Either way of counting exceeds 400 lb.
- The company filed a Top-Screen in 2009 and was told in 2010 that it was **not high risk**. It was never tiered, so it never had to meet the RBPS, even while CFATS was in force.
- **Status on 2026-10-05:** the U.S. Code note to 6 U.S.C. 621-629 (laws in effect 2026-09-24) states that the authority "terminated on July 27, 2023." No reauthorization has been enacted, and no CFATS document appears in the Federal Register in 2026.
- **Decision:** RBPS 8 and CISA's RBPS 8 security measures are used as a **voluntary benchmark**. They are the only chemical-sector federal cyber performance standard, they fit a site that holds an explosives precursor, and they describe what a customer or insurer will ask about. The legacy Top-Screen file is still protected as CVI (G-025).

**2. EPA RMP (40 CFR Part 68): does not apply.** No regulated substance in 68.130 is held above its threshold quantity. The only listed substance on site is propane in forklift cylinders (132 lb against a 10,000 lb TQ). Hydrogen peroxide, sodium hydroxide, sodium hypochlorite, phosphoric acid, and isopropyl alcohol are not listed.

**3. OSHA PSM (29 CFR 1910.119): does not apply.** Hydrogen peroxide is listed only at 52% or greater; the company buys 35%. Isopropyl alcohol is capped at 8 drums (2,882 lb), far below the 10,000 lb flammable liquid threshold.

**4. DOT Hazardous Materials Regulations: apply, without a security plan.**
- The company offers Class 8 and Class 3 products for transportation, so it must train its 6 hazmat employees (49 CFR 172.704), keep shipping papers (172.201(e)), and provide a monitored emergency response telephone number (172.604). Pallet shipments over 1,001 lb of Table 2 materials need placards, so annual registration applies (107.601(a)(6)).
- A **transportation security plan is not required** (172.800(b)). The largest packaging shipped is a 275-gal tote, below the 792-gal "large bulk quantity," and none of the any-quantity materials are shipped. Security awareness training still applies to every hazmat employee (172.704(a)(4)).

**5. Other candidates, not applicable or not in force:**
- **USCG MTSA cybersecurity rule** (C-CHEMICAL-R02; 33 CFR Part 101 Subpart F): applies to facilities that must have a security plan under 33 CFR Part 105 (101.605(a)). The site is inland with no marine transfer.
- **CIRCIA** (C-CHEMICAL-R03; proposed 6 CFR Part 226): no final rule as of 2026-10-05, so no obligation exists. As proposed, the company (7 employees, under the SBA standard of 650) would fall under the size criterion, and the CFATS-facility sector criterion is moot while CFATS is lapsed.
- **EAR:** domestic customers only and no controlled technology.

**Why the binding rows matter.** Without CFATS, no federal rule requires this company to secure its batch control system. The binding rules that do touch its systems are small but real: the ERI provider must hold current SDS data before product ships, shipping papers must be retrievable for two years from the SaaS service, and release notices must go out immediately even when the office network is down.

## 2. Method
1. **Requirements.** RBPS 8 was broken into its text in 6 CFR 27.230(a)(8) (G-002 to G-006), CISA's published RBPS 8 security measures (G-007 to G-020, as read for the chemical Small sample on 2026-09-26; cisa.gov refused automated access on 2026-10-05, so the list was not re-read), and the related RBPS items that support cyber: (a)(12) personnel surety, (a)(15) and (a)(16) incident reporting and records, (a)(17) officials, and 27.400 CVI (G-021 to G-025). The DOT, RMP, PSM, and release reporting rows follow the CFR section structure (G-026 to G-034), read from eCFR on 2026-10-05.
2. **Crosswalk.** All rows are mapped to CSF 2.0 and SP 800-53 Rev. 5 by the author. No official NIST mapping exists for 6 CFR Part 27, CISA's guidance, 49 CFR, 40 CFR, or 29 CFR.
3. **Documentary evidence.** Each status rests on a named document or record: the HMI user list and services list, the portal account page and session log, SaaS user exports and MFA settings, the DOT training binder, the registration certificate, a June 2026 shipping paper sample, the ERI provider's SDS list, the emergency action plan, the Top-Screen file, and the site walkthrough on 2026-07-15. Interviews covered all 7 employees, the MSP lead technician, and the integrator.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Actions completed since then are noted in the remediation column (for example, the new operator's DOT training on 2026-08-14) but do not change the status. Gaps were rated with the P01 risk scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CFATS RBPS text, 6 CFR 27.200-27.400 (voluntary) | 1 | 5 | 4 | 1 | 11 |
| CISA RBPS 8 security measures (voluntary guidance) | 0 | 4 | 10 | 0 | 14 |
| DOT Hazardous Materials Regulations (binding) | 3 | 2 | 0 | 1 | 6 |
| Process safety applicability and release reporting (binding where applicable) | 0 | 1 | 0 | 2 | 3 |
| **Total** | **4** | **12** | **14** | **4** | **34** |

Of the 26 gaps (Partially met or Not met), **8 are High**, 12 are Moderate, and 6 are Low.

**Reading the results.** The company does well on the binding transport rules it already knew about: registration, training records, and shipping paper retention are Met. It does poorly on cyber, with all 14 Not met rows in the voluntary benchmark. That is typical for a business of 7 people with no IT staff. The two binding gaps (G-028, G-031) and the release reporting gap (G-034) are cheap to close and carry legal exposure, so they come first.

## 4. Priority gaps and roadmap
All 8 High gaps, in target date order, plus the binding gaps.

| Gap | Rows | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| New hazmat employee untrained past 90 days | G-028 | Moderate (binding) | Training completed 2026-08-14; due dates on the onboarding checklist | Operations Manager | 2026-08-14 |
| No security program, owner, or policies | G-002, G-007 | High | Adopt POL-02 to POL-04 and this benchmark; Owner approves every recipe and alarm limit change | Owner and President | 2026-09-30 |
| Release reporting depends on the office network | G-034 | Moderate (binding) | Printed call list with RQs in gallons at the exit and dock | Operations Manager | 2026-09-30 |
| Unmanaged, always-on integrator remote access | G-004, G-012 | High | Gateway off except watched sessions; named portal accounts with MFA; remote access rule | Operations Manager | 2026-10-31 |
| Shared HMI login with engineering rights | G-003 | High | Named HMI logins and roles; passwords changed; USB storage blocked | Operations Manager | 2026-11-30 |
| No cyber incident response | G-016 | High | P08 runbook and a tabletop with the MSP and integrator | Operations Manager | 2026-11-30 |
| ERI provider not confirmed current | G-031 | Moderate (binding) | Provider confirms each SDS update; quarterly comparison | QC Technician | 2026-11-30 |
| No recovery path for blending | G-020 | High | Contingency plan; weekly offline export; restore test on spare hardware | Operations Manager | 2026-12-15 |
| HMI unpatched and unmonitored for advisories | G-017 | High | Quarterly advisory report; segment and allowlisting; supported HMI PC in 2027 | Operations Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

**Roadmap:**
- **By 2026-09-30 (no-cost fixes):** policies adopted; door code and shared passwords changed; termination checklist; MFA on the accounting service for all users; printed call list; open share link removed; incident log started.
- **2026 Q4 (the remote access path and the HMI):** named portal accounts with MFA; remote desktop off; named HMI logins and audit trail; HMI network segment; allowlisting; scanned USB stick; training and phishing simulations; tabletop exercise; backup and restore test.
- **2027 (lifecycle):** supported HMI PC at the year-end shutdown with security requirements in the purchase; yearly independent assessment; integrator and MSP contract terms at renewal.

## 5. Pending regulatory changes
None of these is treated as a current obligation.
- **CFATS reauthorization.** If Congress reauthorizes CFATS, the company's hydrogen peroxide holdings still exceed the STQ. Recheck the facility's status and any request for a new Top-Screen at that time. Status checked 2026-10-05: not reauthorized.
- **CIRCIA final rule (proposed 6 CFR Part 226; NPRM 89 FR 23644, 2024-04-04).** The proposed rule would require covered entities to report covered cyber incidents within 72 hours and ransom payments within 24 hours. No final rule has been published. Recheck the size and sector criteria when it is final.
- **EPA RMP proposal (FR Doc. 2026-03633, published 2026-02-24).** A proposed revision of Part 68. The company is outside Part 68 today. Recheck the applicability screen (G-032) if a final rule changes the list of regulated substances or the thresholds.
