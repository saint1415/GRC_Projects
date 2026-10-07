# Regulatory Gap Analysis: Cris Santos Company | Emergency Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| Tier / Vertical | Micro / Emergency Services |
| Regulation analyzed | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) (C-EMERGENCY-R04) |
| Assessment dates | 2026-07-27 to 2026-08-07 |
| Assessor | Office Manager (Privacy and Security Officer) with the MSP lead technician |
| Approved | 2026-09-04 by the Owner |

## 1. Applicability
Applicability was checked first for every requirement in the vertical registry, because the Emergency Services sector research was written mostly for public agencies and 911 centers. A 7-person private company that does only non-emergency transport is a different kind of entity.

| Registry ID | Requirement | Applies? | Reason |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule | **Yes** | See below |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | **No** | The policy governs access to criminal justice information. The company has no link to the county 911 center or to any law enforcement system, and its platform holds only trip and patient care data |
| C-EMERGENCY-R02, R03 | 28 CFR 20.21(f); 28 CFR Part 23 | **No** | These apply to state criminal history systems and to federally funded criminal intelligence systems. The company operates neither |
| C-EMERGENCY-R05 | CIRCIA | **Not yet (proposed only)** | No final rule was in the Federal Register as of 2026-09-25. The company is under the SBA size standard. The proposed sector criterion (proposed 6 CFR 226.2(b)(5)) covers an entity that provides emergency medical services "to a population equal to or greater than 50,000 individuals". Whether a company that does only scheduled, non-emergency transport "provides emergency medical services to a population" is unclear in the proposal. Recheck when a final rule is published |
| C-EMERGENCY-R06 | FCC EAS cybersecurity rule (47 CFR Part 11) | **No** | The company is not an EAS participant |

**Why HIPAA applies.** A "covered entity" includes "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter" (45 CFR 160.103). The company furnishes and bills for health care, so it is a health care provider. Its billing company sends its claims to Medicare, Medicaid, and commercial plans electronically, and a covered entity may use a business associate, including a clearinghouse, to conduct those transactions (45 CFR 162.923(c)).

**A size point that does not change the answer.** With about 6 full-time equivalent employees, the company is a "small supplier" for Medicare (fewer than 10 full-time equivalent employees, 42 CFR 424.32(d)(1)(viii)(B)), so Medicare would accept its claims on paper (424.32(d)(3)(ii)). The company still chooses electronic billing, and that choice is what makes it a covered entity. If it ever moved every payer to paper claims, HIPAA coverage would need to be re-examined with counsel. Nothing in this plan assumes that.

There is no size exemption. Section 164.306(b) lets a 7-person company weigh its size, complexity, technical capabilities, and costs when deciding *how* to meet each standard, not *whether* to meet it.

**Excluded, with reasons (7 rows):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the company is not a clearinghouse.
- **164.314(a)(2)(ii)** (arrangements with governmental entities): no governmental entity is a business associate of the company.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans): the company does not administer a group health plan.

**Related obligations considered but not analyzed row by row** (Micro tier: primary regulation only):
- The HIPAA Breach Notification Rule (45 CFR 164.400-414) and Fla. Stat. 501.171 drive the P08 notification matrix.
- Medicare ambulance documentation: a certification statement for scheduled repetitive trips dated no earlier than 60 days before the trip (42 CFR 410.40(e)(2)), and for unscheduled facility trips within 48 hours after (410.40(e)(3)(i)), with documentation kept 7 years (424.516(f)). The PCS sample (3 of 20 dialysis trips without a current PCS) is carried as risk R-012 and into POL-04.
- Florida EMS records: patient care records to the receiving hospital and confidentiality of records with patient examination or treatment information (Fla. Stat. 401.30(2), (4)); 5-year retention and record availability to the hospital within 48 hours (Rule 64J-1.014, F.A.C.). These are handled in POL-04 and the BIA.

## 2. Method
1. **Requirements.** All 69 rows of the Health Care crosswalk, taken from NIST SP 800-66 Rev. 2 (NIST's dataset in its Cybersecurity and Privacy Reference Tool), with their Required/Addressable designations.
2. **Crosswalk.** Each requirement is mapped to CSF 2.0 and SP 800-53 Rev. 5 using `02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`. That mapping is an **author mapping**, because NIST has not published a HIPAA to CSF 2.0 mapping. NIST's official SP 800-53 mapping is shown next to it in the `nist_official_sp800_53r5_1_1` column.
3. **Documentary evidence.** Each status rests on a named document or record: the platform user, role, and security settings exports; the suite user export and MFA report; the MSP device list, patch report, antivirus export, encryption report, and backup job report; the MDM compliance report; the BAA folder; personnel files; the video sign-in sheet; the 2024 hospital questionnaire; and a walkthrough of the office, garage, and both ambulances on 2026-07-28. Interviews covered the Owner, the Office Manager, the Scheduler-Dispatcher, two EMTs, the Medical Director, and the MSP lead technician.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-08-07)**. Actions completed since then are noted in the remediation column (for example, the phone vendor BAA signed 2026-08-21) but do not change the status.

**Addressable is not optional.** For each addressable specification, the company must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). The company chose to implement every addressable gap below. One will be met with a documented equivalent measure: the dispatch desktop keeps its board on screen, so instead of automatic logoff (164.312(a)(2)(iii)) the company will turn the screen away from the door, fit a privacy filter, and move to named accounts with a quick re-sign-in.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 2 | 15 | 12 | 1 |
| 164.310 Physical safeguards | 2 | 7 | 3 | 0 |
| 164.312 Technical safeguards | 4 | 7 | 1 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 1 | 4 | 0 |
| **Total (69)** | **8** | **34** | **20** | **7** |

Of the 54 unmet or partially met rows, 18 are standards, 18 are **Required** implementation specifications, and 18 are **Addressable** specifications. By gap risk: 7 High, 28 Moderate, 19 Low.

**What the numbers say.** The technical safeguards score best, because the SaaS vendors supply most of them (encryption in transit, integrity of signed records, audit records). The one technical gap that matters most is sign-in: the platform that holds every trip record has no MFA and a shared dispatch login (164.312(a)(2)(i), (d)). The administrative safeguards score worst. Before this work the company had no risk analysis, no policies, no incident or contingency plan, no training after hire, and no review of logs or accounts.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No contingency plan; manual dispatch never practiced while dialysis runs depend on it | 164.308(a)(7), (7)(ii)(C), (D) | High | Contingency plan from the BIA; nightly run sheet; quarterly drill; restore tests | Owner; Scheduler-Dispatcher | 2026-10-31 drill; 2026-11-30 plan |
| No MFA on the operations platform, backup console, or firewall | 164.312(d) | High | MFA for every platform user; MFA on MSP-held logins | Office Manager | 2026-10-31 |
| Backups deletable by one password and never tested | 164.308(a)(7)(ii)(A), (D) | High | Immutable 90-day versions; first restore test | Office Manager (MSP performs) | 2026-09-30 test; 2026-10-31 upgrade |
| No behavior-based detection; no after-hours alerts; no phishing training | 164.308(a)(5)(ii)(B) | High | MSP-managed EDR with after-hours monitoring; training | Office Manager | 2026-12-31 |
| Risk treatments approved but not yet carried out | 164.308(a)(1)(ii)(B) | High | Execute the P01 treatments | Office Manager | 2026-12-31 |
| Shared dispatch login | 164.312(a)(2)(i) | Moderate | Named dispatch accounts with quick sign-in | Scheduler-Dispatcher | 2026-10-31 |
| No termination procedure (two former EMT accounts active) | 164.308(a)(3)(ii)(C) | Moderate | Last-day checklist; monthly reconciliation | Office Manager | 2026-09-30 |
| Missing or unconfirmed BAAs (phone and fax vendor; AI feature) | 164.308(b)(1), 164.314(a) | Moderate | Phone BAA signed 2026-08-21; AI feature confirmation | Owner | 2026-10-15 |
| No audit log or export review | 164.308(a)(1)(ii)(D) | Moderate | Weekly export check; monthly review | Office Manager | 2026-10-31 |
| Unencrypted office desktops | 164.312(a)(2)(iv) | Moderate | Full-disk encryption | Office Manager (MSP performs) | 2026-10-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person company: most actions are one-page procedures, vendor settings, or MSP work, not new systems. The MSP performs the technical work under the Office Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Contracts and access | 2026-09-30 | Phone BAA (done 2026-08-21); termination and onboarding checklist; sanctions and retention rules (POL-02 Part A); workstation rules and signed acknowledgments; policies published; first restore test; security folder | 164.308(b)(4); 164.308(a)(3), (a)(3)(ii)(A), (a)(3)(ii)(C); 164.308(a)(1)(ii)(C); 164.308(a)(6); 164.310(b); 164.316(a), (b), (b)(2)(i), (b)(2)(ii) |
| 2. Sign-in and visibility | 2026-10-31 | MFA on the platform, backup console, and firewall; named dispatch accounts; AI feature confirmation; desktop encryption; screen and privacy filter at the dispatch desk; device and ePHI inventory; monthly log and access review; reminders; password rules; emergency access credential; email encryption rule; backup upgrade; subcontractor confirmations; BA report log; network cabinet; manual dispatch procedure and first drill; incident log | 164.312(d); 164.312(a), (a)(2)(i), (a)(2)(ii), (a)(2)(iii), (a)(2)(iv), (e)(2)(ii); 164.308(b)(1); 164.314(a), (a)(2)(iii), (a)(3)(i); 164.308(a)(1)(ii)(A), (a)(1)(ii)(D), (a)(4), (a)(4)(ii)(B), (a)(4)(ii)(C), (a)(5)(ii)(A), (a)(5)(ii)(D), (a)(6)(ii), (a)(7)(ii)(A), (a)(7)(ii)(C); 164.310(a), (c), (d), (d)(2)(iii) |
| 3. Resilience | 2026-11-30 | Contingency plan with recovery steps, facility access, and the hurricane checklist | 164.308(a)(7), (a)(7)(ii)(B), (a)(7)(ii)(E); 164.310(a)(2)(i), (a)(2)(ii) |
| 4. Detection and records | 2026-12-31 | MSP-managed EDR with after-hours monitoring; annual training and phishing simulations; one year of suite logs; disposal and maintenance records; BA notice terms at renewal; quarterly restore tests and drills under way | 164.308(a)(5), (a)(5)(ii)(B), (a)(5)(ii)(C); 164.308(a)(1)(ii)(B); 164.308(a)(7)(ii)(D); 164.312(b); 164.310(a)(2)(iv), (d)(2)(i), (d)(2)(iv); 164.314(a)(2)(i) |
| 5. Annual cycle | 2027-08-31 | Risk analysis update; independent evaluation; policy review | 164.308(a)(1), (a)(8); 164.316(b)(2)(iii) |

Items already closed by approval on 2026-09-04: adopted policies (164.316(a)), the incident response policy and runbook (164.308(a)(6)), and the approved BIA (164.308(a)(7)(ii)(E)). They remain "Not met" and "Partially met" in the CSV because the status reflects fieldwork.

**Progress check.** The Office Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of the items below is treated as a current obligation. If the rule is finalized as proposed, these verified proposals would affect this company:
- The distinction between "required" and "addressable" would be removed. The 18 addressable gaps above would become mandatory. The company is already implementing all of them.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (the office desktops and outside email today).
- MFA would be required, with limited exceptions (the platform, backup console, and firewall today).
- A written technology asset inventory and network map would be required (no inventory exists today; the hotspots were on no list).
- Penetration testing would be required at least every 12 months, and vulnerability scanning would also be required (none today).
- Certain systems and data would have to be restorable within 72 hours (the suite backup restore is unproven).
- A compliance audit would be required at least every 12 months.
- Business associates would have to notify the company within 24 hours of activating their contingency plans (to add to BAAs at renewal).

**CIRCIA** (C-EMERGENCY-R05) is also still proposed; see section 1.

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row (33 rows).
