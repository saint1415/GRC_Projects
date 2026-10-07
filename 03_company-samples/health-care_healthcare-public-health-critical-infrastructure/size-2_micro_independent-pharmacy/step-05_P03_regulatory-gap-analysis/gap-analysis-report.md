# Regulatory Gap Analysis: Cris Santos Company | Healthcare and Public Health | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Tier / Vertical | Micro / Healthcare and Public Health |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24; eCFR text checked as of 2026-09-23) |
| Secondary rules | The pharmacy's own duties under the DEA rule for electronic prescriptions for controlled substances (21 CFR 1311.200, 1311.205(a), selected 1311.205(b) items, 1311.215, 1311.305) and the CSOS private key rule (21 CFR 1311.30), eCFR text as of 2026-09-23 |
| Assessment dates | 2026-07-13 to 2026-07-24 |
| Assessor | Store Manager (Privacy and Security Officer) with the MSP lead technician |
| Approved | 2026-08-28 by the pharmacist-owner |

## 1. Applicability
**The HIPAA Security Rule applies.** Under 45 CFR 160.103, a covered entity includes a health care provider who transmits health information electronically in connection with a transaction HHS has adopted a standard for. A pharmacy is a health care provider. Its PMS sends retail pharmacy drug claims to PBMs in real time through a claims switch, using the NCPDP Telecommunication Standard adopted for those claims (45 CFR 162.1102(c)). That makes the pharmacy a covered entity.

There is no size exemption. Section 164.306(b) lets a 7-person pharmacy weigh its size, technical capabilities, and costs when deciding *how* to meet each standard, not *whether* to meet it.

**The DEA rules apply directly, whatever HIPAA says.** The pharmacy is a DEA registrant that receives and dispenses electronic prescriptions for controlled substances (EPCS) through the PMS, so the pharmacy duties in 21 CFR 1311.200 and 1311.215 and the recordkeeping rules in 1311.305 apply. It signs Schedule II orders electronically with a CSOS certificate, so 1311.30 applies to the private key. These rows are included because the EPCS rule works like a security rule: logical access, audit trails, daily audit analysis, daily backups, and a one-business-day incident report. Most application requirements in 1311.205(b) fall on the PMS vendor; the pharmacy's duty is to use only an application that meets them (1311.205(a)). Only the 1311.205(b) items the pharmacy can affect or must rely on are analyzed: the dispenser's name on each record (b)(10), which depends on how staff sign in, and the daily backup (b)(17).

**HIPAA rows excluded, with reasons (7 rows):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the pharmacy is not a clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no business associate is a governmental entity.
- **164.314(b) and (b)(2)(i)-(iv)** (group health plans): the pharmacy sponsors no group health plan.

**Other obligations screened (not analyzed row by row):**

| Obligation | Decision | Basis |
|---|---|---|
| HIPAA Breach Notification Rule (C-HPH-R02) | Applies | Drives the P08 notification matrix |
| Fla. Stat. 501.171 | Applies | Florida breach notice; in the P08 matrix |
| Fla. Stat. 893.055(3)(a), (8) and 893.07(4), (5)(b) | Apply | PDMP report by the close of the next business day; PDMP outage rule; 2-year controlled substance records; theft or significant loss reported to the sheriff within 24 hours. These drive P05 and P08 |
| 21 CFR 1301.76(b) | Applies | Theft or significant loss of controlled substances reported in writing to the DEA Field Division Office within one business day of discovery, then DEA Form 106 within 45 days. In the P08 matrix |
| Section 1557, 45 CFR 92.210 | Applies | Florida Medicaid is federal financial assistance. Drives the review of DUR alerts and the controlled substance risk score in P10 |
| HPH CPGs (C-HPH-R08) and 405(d) HICP (C-HPH-R09) | Voluntary | Used to pick practical safeguards; HICP has a small-organization volume |
| HITECH recognized security practices (C-HPH-R10) | Applies as a mitigating factor | OCR must consider recognized security practices in place for the prior 12 months (42 U.S.C. 17941); P01 R-015 |
| 42 CFR Part 2 (C-HPH-R06) | Does not apply | Not a "program" under 42 CFR 2.11: the pharmacy does not hold itself out as providing substance use disorder diagnosis, treatment, or referral |
| FTC Health Breach Notification Rule (C-HPH-R05) | Does not apply | 16 CFR 318.1 excludes HIPAA covered entities |
| CMS emergency preparedness (C-HPH-R07) | Does not apply | Pharmacies are not among the provider and supplier types the rule covers |
| FDA sec. 524B (C-HPH-R04) | Does not apply | A device manufacturer duty; used only as a procurement lever for the packaging equipment |
| CIRCIA (C-HPH-R11) | Not in effect | Proposed only; as proposed, an SBA-small pharmacy outside the health care sector criteria would not be covered |

## 2. Method
1. **Requirements.** HIPAA: all 69 rows of the Health Care crosswalk (`02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`), with titles, types, and text from NIST SP 800-66 Rev. 2. NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis uses the current rule's numbering, 164.308(b)(3). DEA: 13 rows built from the regulation's own paragraph structure, summarized in plain words.
2. **Crosswalk.** The HIPAA CSF 2.0 and SP 800-53 columns are an **author mapping**; NIST's official mapping is shown next to it in `nist_official_sp800_53r5_1_1`. No official NIST mapping exists for 21 CFR Part 1311, so those rows are an author mapping.
3. **Documentary evidence.** Each status rests on a named document or record: the PMS user and role lists, the PMS EPCS audit report screen and a review of its 90 retained reports, a sample of 10 EPCS records and a record retrieval test (2026-07-21), the productivity suite user export and security settings, a sample of 10 emails to the ALFs, the MSP's device list, patch report, antivirus console export, and backup job report, the BAA folder, the employee handbook and personnel files, the 2019 policy binder and the 2022 vendor checklist, and a store walkthrough (2026-07-15). Interviews covered all 7 staff and the MSP lead technician.
4. **Status.** Each requirement was rated Met, Partially met, Not met, or Not applicable **as of the end of fieldwork (2026-07-24)**. Fixes made during fieldwork count (the controlled substance permission removed 2026-07-17). Actions completed after fieldwork are noted in the remediation column (for example, the EPCS audit report reviewed 2026-08-12) but do not change the status.

**Addressable is not optional.** For each addressable specification, the pharmacy must implement it, implement an equivalent alternative, or document why neither is reasonable and appropriate (164.306(d)(3)). For every addressable gap below, the pharmacy chose to implement. None is documented as unreasonable. The packaging workstation's encryption is deferred to the next equipment refresh, with physical safeguards and network separation until then; that is a dated plan, not a decision not to implement.

## 3. Results summary
**HIPAA Security Rule (69 rows)**

| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 2 | 16 | 11 | 1 |
| 164.310 Physical safeguards | 1 | 8 | 3 | 0 |
| 164.312 Technical safeguards | 3 | 9 | 0 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 1 | 4 | 0 |
| **Total (69)** | **6** | **38** | **18** | **7** |

Of the 56 unmet or partially met HIPAA rows, 19 are standards, 19 are **Required** implementation specifications, and 18 are **Addressable** specifications. By gap risk: 5 High, 31 Moderate, 20 Low.

**DEA EPCS and CSOS (13 rows)**

| Result | Met | Partially met | Not met |
|---|---|---|---|
| 21 CFR Part 1311 pharmacy duties | 4 | 6 | 3 |

Gap risk for the 9 unmet or partially met DEA rows: 6 Moderate, 3 Low.

**What the numbers say.** The technical safeguards score best, because the PMS vendor and the productivity suite supply most of them (unique PMS accounts, integrity, encryption in transit, the EPCS audit trail). The administrative safeguards score worst: no risk analysis before 2026, no adopted policies, no incident or contingency plan, no training beyond a privacy video, and no review of logs or access. The DEA rows show the same split: everything the **application** must do is done, while most of what the **pharmacy** must do (decide who may alter records, read the daily audit report, report within one business day, keep the CSOS key to its holder) was not.

## 4. Priority gaps
| Gap | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| No downtime procedure; dispensing stops in a PMS or internet outage | 164.308(a)(7), (a)(7)(ii)(C) | High | Contingency plan with a downtime card at each station and the partner pharmacy arrangement | Store Manager | 2026-11-30 |
| Backups never tested and not immutable | 164.308(a)(7)(ii)(A) | High | Restore test by 2026-09-30; 90-day immutable versions and console MFA by 2026-10-31 | Store Manager (MSP performs) | 2026-10-31 |
| Late malware detection; unprotected packaging workstation | 164.308(a)(5)(ii)(B) | High | MSP-managed EDR; phishing training; packaging workstation segment | Store Manager | 2026-12-31 |
| Risk management not yet carried out | 164.308(a)(1)(ii)(B) | High | Carry out the P01 treatments | Store Manager | 2026-12-31 |
| Daily EPCS audit report never read; no one-business-day report | 21 CFR 1311.215(c); 164.308(a)(1)(ii)(D) | Moderate | Pharmacist on duty reviews it each business day; POL-03 reporting steps | Pharmacist-owner | 2026-09-30 |
| CSOS key used by someone other than its holder | 21 CFR 1311.30(a)-(d) | Moderate | Revoked and replaced (done 2026-08-03); own certificate for the Store Manager under a power of attorney | Pharmacist-owner | 2026-10-31 |
| No written decision on who may alter controlled substance records | 21 CFR 1311.200(e); 164.308(a)(4)(ii)(B) | Moderate | POL-02 B.2; permission already limited to pharmacists | Pharmacist-owner | 2026-09-30 |
| EPCS audit report never obtained | 21 CFR 1311.200(a)-(b) | Moderate | Report obtained and determination recorded 2026-08-12; repeat with each new report | Pharmacist-owner | 2026-08-12 |
| Shared open PMS sessions put the wrong name on dispensing records | 21 CFR 1311.205(b)(10); 164.312(a)(2)(iii) | Moderate | 15-minute timeout with quick re-sign-in; individual desktop accounts | Store Manager | 2026-10-31 |
| No termination procedure | 164.308(a)(3)(ii)(C) | Moderate | Last-day checklist; monthly reconciliation | Store Manager | 2026-09-30 |
| Two vendors handle ePHI without a BAA | 164.308(b)(1), (b)(3); 164.314(a) | Moderate | BAAs with the delivery app and packaging equipment vendors, or replace them | Store Manager | 2026-10-31 |
| Unencrypted desktops | 164.312(a)(2)(iv) | Moderate | Full-disk encryption on all 5 desktops | Store Manager (MSP performs) | 2026-10-31 |
| No second factor for in-store PMS sign-in or the backup console | 164.312(d) | Moderate | Vendor second-factor option; console MFA | Store Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person pharmacy: most actions are one-page procedures, PMS settings, or MSP work, not new systems. The MSP performs the technical work under the Store Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Gaps closed (citation) |
|---|---|---|---|
| 1. Controlled substance duties and access | 2026-09-30 | Daily EPCS report review and DEA reporting steps; EPCS stop-and-resume and CSOS revocation steps; written authorization for controlled substance record changes; termination checklist and onboarding approval line; sanctions and retention rules; workforce use rules with signed acknowledgments; incident log and assessment of the March 2026 fax; first restore test | 21 CFR 1311.215(c), 1311.200(c)-(e), 1311.30(e); 164.308(a)(1)(ii)(C), (D); 164.308(a)(3), (a)(3)(ii)(A), (C); 164.308(a)(4)(ii)(B); 164.308(a)(6), (a)(6)(ii); 164.308(a)(7)(ii)(D); 164.310(b); 164.316(b), (b)(2)(i), (ii) |
| 2. Visibility and hardening | 2026-10-31 | Device and ePHI inventory; desktop encryption; individual desktop accounts with screen lock; 15-minute PMS timeout; monthly account and log review; annual training and phishing simulations; Wi-Fi and password rules; automatic email encryption rule; BAAs for the delivery app and packaging vendor; subcontractor BAA confirmation; backup upgrade with console MFA; own CSOS certificate for the Store Manager | 164.308(a)(1)(ii)(A); 164.308(a)(4), (a)(4)(ii)(C); 164.308(a)(5), (a)(5)(ii)(A), (C), (D); 164.308(a)(7)(ii)(A); 164.308(b)(1), (b)(3); 164.310(c), (d), (d)(2)(iii), (d)(2)(iv); 164.312(a), (a)(2)(iii), (a)(2)(iv), (e)(2)(ii); 164.314(a), (a)(2)(iii), (a)(3)(i); 21 CFR 1311.205(b)(10), 1311.30(a)-(d) |
| 3. Resilience | 2026-11-30 | Contingency plan with disaster recovery steps, downtime card (including the duplicate-prescription check), emergency access, facility and hurricane sections; cellular failover router; incident response tabletop | 164.308(a)(7), (a)(7)(ii)(B), (C); 164.310(a), (a)(2)(i), (a)(2)(ii); 164.312(a)(2)(ii); 21 CFR 1311.200(g)-(h) |
| 4. Detection and segmentation | 2026-12-31 | MSP-managed EDR; network segments for the packaging workstation and for phones and cameras; in-store PMS second factor; one year of suite logs; disposal and maintenance records; 24-hour incident notice in BAAs at renewal | 164.308(a)(1)(ii)(B); 164.308(a)(5)(ii)(B); 164.312(a)(2)(i), (b), (d), (e)(1); 164.310(a)(2)(iv), (d)(2)(i), (d)(2)(ii); 164.314(a)(2)(i) |
| 5. Annual cycle | 2027-07-31 to 2027-08-31 | Risk analysis update (July); independent evaluation and policy review (August) | 164.308(a)(1), (a)(8); 164.316(b)(2)(iii) |

Items already closed by approval or action after fieldwork: adopted policies (164.316(a), 2026-08-28), the approved BIA (164.308(a)(7)(ii)(E), 2026-08-28), the first independent evaluation (164.308(a)(8), 2026-08-06), and the EPCS audit report determination (21 CFR 1311.200(a)-(b) and 1311.205(a), 2026-08-12). They keep their fieldwork status in the CSV.

**Progress check.** The Store Manager reports progress to the pharmacist-owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06; RIN 0945-AA22) is **still proposed**. The regulatory agenda projects a final rule in July 2027. None of the items below is treated as a current obligation. If the rule is finalized as proposed, these verified proposals would affect this pharmacy:
- The distinction between "required" and "addressable" would be removed. The 18 addressable gaps above would become mandatory. The pharmacy is already implementing all of them.
- All ePHI would have to be encrypted at rest and in transit, with limited exceptions (desktops, the packaging workstation, and outside email today).
- MFA would be required, with limited exceptions (in-store PMS sign-in and the backup console today).
- A written technology asset inventory and network map would be required (no inventory exists today).
- Penetration testing would be required at least every 12 months, and vulnerability scanning would also be required (none today).
- Certain systems and data would have to be restorable within 72 hours (the shared drive and packaging workstation restores are unproven).
- A compliance audit would be required at least every 12 months.
- Business associates would have to notify the pharmacy within 24 hours of activating their contingency plans. In a PMS vendor outage, that would give the pharmacy a guaranteed early warning (to add to BAAs at renewal).

The `pending_rule_change` column in `gap-analysis.csv` flags each affected row. The DEA rows use the eCFR text as of 2026-09-23; 21 CFR 1311.25 was last amended on 2025-10-02 (90 FR 47580). Recheck Part 1311 at each annual review.
