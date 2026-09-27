# Regulatory Gap Analysis: Cris Santos Company | Health Care and Social Assistance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| Tier / Vertical | Micro / Health Care and Social Assistance |
| Regulation analyzed | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) |
| Assessment dates | 2026-07-20 to 2026-07-31 |
| Assessor | Office Manager (Privacy and Security Officer) with the MSP lead technician |
| Approved | 2026-08-31 by the owner physician |

## 1. Applicability
The HIPAA Security Rule **applies**. The practice is a health care provider that sends claims and eligibility requests electronically in standard transactions through its EHR's clearinghouse. That makes it a covered entity under 45 CFR 160.103.

There is no size exemption. Section 164.306(b) lets a 7-person office weigh its size, complexity, technical capabilities, and costs when deciding *how* to meet each standard, not *whether* to meet it.

**Excluded, with reasons (7 rows):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the practice is not a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): none exist.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans): the practice does not administer a group health plan.

**Related rules considered but not analyzed row by row:** the Breach Notification Rule (45 CFR 164.400-414) drives the P08 notification matrix. 42 CFR Part 2 does not apply (no federally assisted SUD program).

## 2. Method
1. **Requirements.** All 69 rows of the Health Care crosswalk, taken from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool), with their Required/Addressable designations.
2. **Crosswalk.** Each requirement is mapped to CSF 2.0 and SP 800-53 Rev. 5 using `02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`. That mapping is an **author mapping**, not NIST's official mapping, which is not yet published for CSF 2.0.
3. **Documentary evidence.** Each status rests on a named document or record: the EHR user and role lists, the productivity suite user export and security settings, the MSP's device list, patch report, antivirus console export, and backup job report, the BAA folder, the new-hire video sign-in sheet, the 2019 checklist, and a walkthrough of the suite on 2026-07-22. Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-31)**. Actions completed since then are noted in the remediation column (for example, the productivity suite BAA accepted 2026-08-14) but do not change the status.

**Addressable is not optional.** For each addressable specification, the practice must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). For every addressable gap below, the practice chose to implement. None is being documented as unreasonable.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 3 | 15 | 11 | 1 |
| 164.310 Physical safeguards | 2 | 7 | 3 | 0 |
| 164.312 Technical safeguards | 5 | 7 | 0 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 1 | 4 | 0 |
| **Total (69)** | **10** | **34** | **18** | **7** |

Of the 52 unmet or partially met rows, 18 are standards, 17 are **Required** implementation specifications, and 17 are **Addressable** specifications. By gap risk: 5 High, 28 Moderate, 19 Low.

**What the numbers say.** The technical safeguards score best, because the SaaS vendors and the MSP supply most of them (encryption in transit, unique IDs, integrity). The administrative safeguards score worst: the practice had no risk analysis since 2019, no adopted policies, no incident or contingency plan, no training after hire, and no review of logs or access.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Shared-drive backup never tested and not immutable | 164.308(a)(7)(ii)(A), (D) | High | Restore test; 90-day immutable versions; quarterly tests | Office Manager (MSP performs) | 2026-09-30 first test; 2026-10-31 upgrade |
| No contingency plan | 164.308(a)(7) | High | Short plan from the BIA with downtime kit and hurricane checklist | Office Manager | 2026-11-30 |
| No malware training; no behavior-based detection | 164.308(a)(5)(ii)(B) | High | Training plus phishing simulations; MSP-managed EDR | Office Manager | 2026-12-31 |
| Risk management not yet carried out | 164.308(a)(1)(ii)(B) | High | Execute the P01 treatments | Office Manager | 2026-12-31 |
| Missing BAAs (productivity suite, AI scribe) | 164.308(b)(1), 164.314(a) | Moderate | Suite BAA accepted 2026-08-14; AI scribe recording paused until BAA signed | Office Manager; Associate Physician | 2026-09-30 |
| No termination procedure | 164.308(a)(3)(ii)(C) | Moderate | Last-day checklist; monthly reconciliation | Office Manager | 2026-09-30 |
| No audit log or access review | 164.308(a)(1)(ii)(D) | Moderate | Monthly review with a checklist | Office Manager | 2026-10-31 |
| No sanctions rule | 164.308(a)(1)(ii)(C) | Moderate | POL-02 Part A sanctions rule | Owner Physician | 2026-09-30 |
| Unencrypted desktops | 164.312(a)(2)(iv) | Moderate | Full-disk encryption | Office Manager (MSP performs) | 2026-10-31 |
| No MFA on MSP-held administrator logins | 164.312(d) | Moderate | MFA on backup console and firewall | Office Manager (MSP performs) | 2026-09-30 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person office: most actions are one-page procedures or MSP settings, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Contracts and access | 2026-09-30 | Accept suite BAA (done 2026-08-14); AI scribe BAA or stop recording; termination checklist; onboarding access line; sanctions and retention rules (POL-02 Part A); workstation rules and signed acknowledgments; MFA on MSP-held admin logins; first restore test | 164.308(b)(1), (b)(4), 164.314(a), (a)(2)(i), (a)(3)(i); 164.308(a)(3), (a)(3)(ii)(C), (a)(4)(ii)(B); 164.308(a)(1)(ii)(C); 164.316(b), (b)(2)(i); 164.310(b); 164.312(d); 164.308(a)(7)(ii)(D) |
| 2. Visibility and hardening | 2026-10-31 | Device and ePHI inventory; desktop encryption; remove screen-lock exceptions and fit privacy filters; remove unneeded EHR admin roles; monthly log and access review starts; annual training and phishing simulations start; number matching for MFA; Wi-Fi password change; automatic email encryption rule; incident log; backup upgrade; subcontractor BAA confirmation; policies published to staff | 164.308(a)(1)(ii)(A), (D); 164.308(a)(4), (a)(4)(ii)(C); 164.308(a)(5), (a)(5)(ii)(A), (C), (D); 164.308(a)(6)(ii); 164.308(a)(7)(ii)(A); 164.310(c), (d), (d)(2)(iii), (d)(2)(iv); 164.312(a), (a)(2)(iii), (a)(2)(iv), (e)(2)(ii); 164.314(a)(2)(iii); 164.316(b)(2)(ii) |
| 3. Resilience | 2026-11-30 | Contingency plan with disaster recovery steps, downtime kit, emergency access, and facility sections; incident response tabletop | 164.308(a)(6), (a)(7), (a)(7)(ii)(B), (C); 164.310(a), (a)(2)(i), (a)(2)(ii); 164.312(a)(2)(ii) |
| 4. Detection and records | 2026-12-31 | MSP-managed EDR; one year of suite logs; disposal records; maintenance records | 164.308(a)(5)(ii)(B); 164.308(a)(1)(ii)(B); 164.312(b); 164.310(d)(2)(i), (a)(2)(iv) |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk analysis update (July); independent evaluation and policy review (August) | 164.308(a)(1), (a)(8); 164.316(b)(2)(iii) |

Items already closed by approval on 2026-08-31: adopted policies (164.316(a)) and the approved BIA (164.308(a)(7)(ii)(E)). They remain "Not met" and "Partially met" in the CSV because the status reflects fieldwork.

**Progress check.** The Office Manager reports progress to the owner physician at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of the items below is treated as a current obligation. If the rule is finalized as proposed, these verified proposals would affect this practice:
- The distinction between "required" and "addressable" would be removed. The 17 addressable gaps above would become mandatory. The practice is already implementing all of them.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (desktops and outside email today).
- MFA would be required, with limited exceptions (the two MSP-held administrator logins today).
- A written technology asset inventory and network map would be required (no inventory exists today).
- Penetration testing would be required at least every 12 months, and vulnerability scanning would also be required (none today).
- Certain systems and data would have to be restorable within 72 hours (the shared drive restore is unproven).
- A compliance audit would be required at least every 12 months.
- Business associates would have to notify the practice within 24 hours of activating their contingency plans (to add to BAAs at renewal).

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row.
