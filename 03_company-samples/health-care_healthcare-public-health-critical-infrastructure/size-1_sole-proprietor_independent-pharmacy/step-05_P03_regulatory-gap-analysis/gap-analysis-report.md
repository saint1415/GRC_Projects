# Regulatory Gap Analysis: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Tier / Vertical | Sole Proprietorship / Healthcare and Public Health |
| Primary regulation | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24; eCFR text checked as of 2026-09-23) |
| Secondary rules | The pharmacy's own duties under the DEA EPCS rule (21 CFR 1311.200 to 1311.215, 1311.305) and the CSOS private key rule (21 CFR 1311.30), eCFR text as of 2026-09-23 |
| Assessment dates | 2026-08-03 to 2026-08-07 (self-assessment) |
| Assessor | Pharmacist-owner, with the on-call IT consultant (under BAA since 2026-07-31). Evidence is the intake record, the owner's written self-review (EV-036), the vendor reports obtained on 2026-08-05, and the self-assessment tests |
| Adopted | 2026-09-04 |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here. **The HIPAA Security Rule applies.** Under 45 CFR 160.103, a covered entity includes "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter." A pharmacy is a health care provider. Its pharmacy management system (PMS) sends retail pharmacy drug claims to PBMs in real time (EV-005, EV-007), using the NCPDP Telecommunication Standard that HHS adopted for those claims (45 CFR 162.1102). That makes the pharmacy a covered entity. There is no small-pharmacy exemption: 45 CFR 164.306(b) lets the pharmacy weigh its size, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it.

**The test is function, not size.** A cash-only pharmacy that never sent a standard electronic transaction would not be a HIPAA covered entity. This pharmacy could not leave HIPAA without leaving every PBM network, which is not realistic: about 90% of its prescriptions are paid by PBMs (EV-007).

**The DEA rules apply directly, whatever HIPAA says.** The pharmacy is a DEA registrant (EV-025) that receives electronic prescriptions for controlled substances through the PMS, so the pharmacy duties in 21 CFR 1311.200 to 1311.215 and the recordkeeping in 1311.305 apply. It orders Schedule II stock electronically with a CSOS certificate, so 1311.30 applies to the private key. These rows are included because the EPCS rule is a security rule in all but name: logical access, audit trails, daily audit analysis, backups, and a one-business-day incident report. The application's own requirements in 1311.205(b) are the vendor's; the pharmacy's duty is to use only an application that meets them (1311.205(a)), so only the rows the pharmacy must act on are analyzed.

**Workforce.** The pharmacy has no employees, but the relief pharmacist is a **workforce member**: 45 CFR 160.103 defines workforce to include persons whose conduct in their work for a covered entity is under its direct control, whether or not paid by it (EV-021). All workforce specifications therefore apply and are rated below.

**HIPAA rows excluded, with reasons (7 rows):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the pharmacy is not a clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no business associate is a governmental entity.
- **164.314(b)** and its four specifications (group health plans): the pharmacy sponsors no group health plan.

**Other obligations screened (not analyzed row by row):**

| Obligation | Decision | Basis |
|---|---|---|
| HIPAA Breach Notification Rule (C-HPH-R02) | Applies | Drives the P08 notification matrix |
| Fla. Stat. 501.171 | Applies | Florida breach notice; in the P08 matrix |
| Fla. Stat. 893.055(3)(a) and 893.07 | Apply | PDMP report by the close of the next business day; controlled substance records kept at least 2 years. Both drive P05 and P08 |
| Section 1557, 45 CFR 92.210 (parent vertical ID N62-R07) | Applies | Florida Medicaid is federal financial assistance. Drives the decision support review in P10 |
| HPH CPGs (C-HPH-R08) and 405(d) HICP (C-HPH-R09) | Voluntary | Used to pick practical safeguards; HICP has a small-organization volume |
| HITECH recognized security practices (C-HPH-R10) | Applies as a mitigating factor | OCR must consider recognized security practices in place for the prior 12 months |
| 42 CFR Part 2 (C-HPH-R06) | Does not apply | Not a "program" under 42 CFR 2.11: the pharmacy does not hold itself out as providing substance use disorder diagnosis, treatment, or referral |
| FTC Health Breach Notification Rule (C-HPH-R05) | Does not apply | 16 CFR 318.1 excludes HIPAA covered entities |
| CMS emergency preparedness (C-HPH-R07) | Does not apply | Pharmacies are not among the provider and supplier types the rule covers |
| FDA sec. 524B (C-HPH-R04) | Does not apply | A manufacturer duty |
| CIRCIA (C-HPH-R11) | Not in effect | Proposed only; as proposed, an SBA-small pharmacy outside the sector criteria would not be covered |

## 2. Method
1. **Requirements.** HIPAA: all 69 rows of the Health Care crosswalk (`02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`); titles, types, and text from NIST SP 800-66 Rev. 2. NIST's dataset numbers the written-contract specification 164.308(b)(4); this analysis uses the current rule's 164.308(b)(3). DEA: 14 rows built from the regulation's own paragraph structure, summarized in plain words.
2. **Crosswalk.** HIPAA CSF 2.0 and SP 800-53 columns are an **author mapping**; NIST's official OLIR 110 mapping is shown next to it in `nist_official_sp800_53r5_1_1`. No official NIST mapping exists for 21 CFR Part 1311, so those rows are an author mapping.
3. **Evidence.** Current state was established from the intake evidence (PMS user list and role settings, the EPCS audit report screen, the remote-support agent settings, desktop and router settings, the BAA folder, statements, license records, and the store walk-through on 2026-07-29) and the owner's written self-review, checked on screen with the IT consultant from 2026-08-03 to 2026-08-05 (EV-036). The vendor's SOC 2 and EPCS certification reports and the BAA terms review are dated 2026-08-05 (EV-037 to EV-039). Where the self-assessment tests had run (2026-08-06: the sample of 10 EPCS records and the record retrieval test), their results are cited too. The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
4. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale. Addressable is not optional: every addressable gap below is being implemented, and none is documented as unreasonable under 164.306(d)(3).

## 3. Results summary
**HIPAA Security Rule (69 rows)**

| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 2 | 15 | 12 | 1 |
| 164.310 Physical safeguards | 2 | 6 | 4 | 0 |
| 164.312 Technical safeguards | 3 | 6 | 3 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 1 | 4 | 0 |
| **Total (69)** | **7** | **32** | **23** | **7** |

Of the 55 unmet or partially met HIPAA rows, 20 are standards, 18 are **Required** specifications, and 17 are **Addressable** specifications. Gap risk: 2 High, 29 Moderate, 24 Low.

**DEA EPCS and CSOS (14 rows)**

| Result | Met | Partially met | Not met |
|---|---|---|---|
| 21 CFR 1311 pharmacy duties | 6 | 4 | 4 |

Gap risk for the 8 unmet or partially met rows: 5 Moderate, 3 Low. The pattern is clear: everything the **vendor** must do under the EPCS rule is done and certified; most of what the **pharmacy** must do (own accounts, read the daily audit report, report within one business day, protect the CSOS key) is not.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Turn on built-in full-disk encryption on the counter desktop; delete the mailing-list export | 164.312(a)(2)(iv) | High | 2026-09-15 |
| 2 | Accept the email and file suite BAA; turn on cloud fax MFA | 164.308(b)(1); 164.312(d) | Moderate | 2026-09-15 |
| 3 | Own PMS and desktop accounts for each pharmacist; pharmacist role for daily work; MFA for the administrator role in the store; 3-minute lock | 164.312(a)(2)(i); 164.312(a)(2)(iii); 21 CFR 1311.200(e); 1311.205(b)(10) | Moderate | 2026-09-30 |
| 4 | Read the daily EPCS audit report every business morning; follow the P08 one-business-day reporting steps | 164.308(a)(1)(ii)(D); 21 CFR 1311.215(c) | Moderate | 2026-09-30 |
| 5 | Move the CSOS key to the owner's own desktop account; 24-hour revocation step in P08 | 21 CFR 1311.30 | Moderate | 2026-09-30 |
| 6 | Adopt POL-01 (policies, sanctions, Security Officer designation, retention) and the P08 runbook | 164.316; 164.308(a)(1)(ii)(C); 164.308(a)(2); 164.308(a)(6) | Moderate | 2026-09-04 (done) |
| 7 | Paper downtime kit, weekly printed active-patient medication list, transfer arrangement with a nearby pharmacy | 164.308(a)(7)(ii)(C) | High | 2026-10-31 |
| 8 | Separate guest and camera networks | 164.312(e)(1) | Moderate | 2026-10-31 |
| 9 | Annual security course for both pharmacists; monthly reminders | 164.308(a)(5) | Moderate | 2026-11-30 |
| 10 | Sealed recovery codes and emergency access sheet; wipe the old desktop | 164.312(a)(2)(ii); 164.310(d)(2)(i) | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**; the regulatory agenda projects a final rule in July 2027. It is not a current obligation. If finalized as proposed, it would remove the addressable designation (affecting the 17 addressable gaps), require encryption of ePHI at rest and in transit with limited exceptions, require MFA, require a written technology asset inventory and network map, require penetration testing at least every 12 months and vulnerability scanning, require restoring certain systems within 72 hours, require a compliance audit at least every 12 months, and require business associates to notify the pharmacy within 24 hours of activating their contingency plans. The last item matters most here: in a PMS vendor outage (P08), the pharmacy would get a guaranteed early warning. The `pending_rule_change` column flags the affected rows. The DEA rows use the eCFR text as of 2026-09-23; recheck it at each annual review.
