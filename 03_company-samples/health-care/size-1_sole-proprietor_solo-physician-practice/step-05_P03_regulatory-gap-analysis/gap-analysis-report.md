# Regulatory Gap Analysis: Cris Santos Company | Health Care and Social Assistance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Tier / Vertical | Sole Proprietorship / Health Care and Social Assistance |
| Regulation analyzed | HIPAA Security Rule, 45 CFR Part 164, Subpart C (in force; last amended 2020-11-24) |
| Assessment dates | 2026-07-20 to 2026-07-24 (self-assessment) |
| Assessor | Physician-owner, with the on-call IT consultant (under BAA since 2026-07-17). Evidence is self-attested |
| Adopted | 2026-08-31 |

## 1. Applicability
**The HIPAA Security Rule applies.** Under 45 CFR 160.103, a covered entity includes "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter." The physician is a health care provider. The practice's billing company submits claims electronically to Medicare, Florida Medicaid, and commercial plans on the practice's behalf. Those are standard transactions, and 45 CFR 162.923(c) lets a covered entity use a business associate to conduct them. Using a billing company does not move the obligation away from the practice. It is how the practice conducts its transactions.

**The test is function, not size.** A physician who ran a cash-only direct primary care practice, never billed insurance, and never conducted a standard electronic transaction (directly or through anyone else) would not be a HIPAA covered entity, whatever its size. This practice would become exempt only by giving up electronic claims, which is not realistic with Medicare and Medicaid patients.

There is no small-practice exemption. 45 CFR 164.306(b) lets the practice weigh its size, capabilities, and costs when choosing *how* to meet each standard, not *whether* to meet it.

**Excluded, with reasons (7 rows):**
- **164.308(a)(4)(ii)(A)** (isolating clearinghouse functions): the practice is not a clearinghouse.
- **164.314(a)(2)(ii)** (other arrangements): no business associate is a governmental entity.
- **164.314(b)** and its four specifications (group health plans): the practice sponsors no group health plan.

**Workforce specifications.** The practice has no workforce other than the owner (45 CFR 160.103 defines workforce as employees, volunteers, trainees, and others under the practice's direct control). Workforce clearance (164.308(a)(3)(ii)(B)) is addressed by documenting that it is not reasonable and appropriate today, as 164.306(d)(3)(ii)(B) permits. The other workforce specifications still apply to contractor access and are rated below.

## 2. Method
1. **Requirements.** All 69 rows of the Health Care crosswalk (`02_industry-rules/health-care/hipaa-security-rule-crosswalk.csv`). Titles, types, and text come from NIST SP 800-66 Rev. 2.
2. **Crosswalk.** CSF 2.0 and SP 800-53 columns are an **author mapping**, not NIST's official mapping (see the crosswalk README).
3. **Evidence.** Self-attested by the owner, checked where possible by looking at the setting on screen with the IT consultant (EHR user list, device settings, BAA folder, suite walkthrough on 2026-07-21).
4. **Status.** Met, Partially met, Not met, or Not applicable. Addressable is not optional: each addressable gap is being implemented, or (for workforce clearance) documented under 164.306(d)(3).

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 164.308 Administrative safeguards | 5 | 16 | 8 | 1 |
| 164.310 Physical safeguards | 4 | 6 | 2 | 0 |
| 164.312 Technical safeguards | 5 | 6 | 1 | 0 |
| 164.314 Organizational requirements | 0 | 4 | 0 | 6 |
| 164.316 Policies, procedures, documentation | 0 | 1 | 4 | 0 |
| **Total (69)** | **14** | **33** | **15** | **7** |

Of the 48 unmet or partially met rows, 16 are standards, 17 are **Required** specifications, and 15 are **Addressable** specifications. Gap risk: 3 High, 24 Moderate, 21 Low.

## 4. Action list (half page)
In order. The first five cost nothing and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Turn on built-in full-disk encryption on the laptop | 164.312(a)(2)(iv) | High | 2026-09-15 |
| 2 | Turn on MFA for email and the cloud fax portal; password manager | 164.312(d); 164.308(a)(5)(ii)(D) | High | 2026-09-15 |
| 3 | Adopt POL-01 (policies, sanctions, Security Officer designation, retention) | 164.316; 164.308(a)(1)(ii)(C); 164.308(a)(2) | Moderate | 2026-08-31 (done) |
| 4 | Keep the IT consultant's unattended remote access off (turned off 2026-07-23); owner-watched sessions only | 164.308(a)(3)(ii)(A) | Moderate | 2026-09-30 |
| 5 | Adopt and print the P08 runbook and contacts | 164.308(a)(6) | Moderate | 2026-09-30 |
| 6 | BAAs or replacements: email and file provider, answering service; stop the AI scribe | 164.308(b)(1); 164.314(a) | Moderate | 2026-10-31 |
| 7 | Move patient texts and photos into the EHR portal and app | 164.312(e)(1); 164.308(a)(7)(ii)(A) | Moderate | 2026-10-31 |
| 8 | Monthly review of EHR audit log and email sign-in history | 164.308(a)(1)(ii)(D) | Moderate | 2026-10-31 |
| 9 | Annual security course and monthly reminders for the owner | 164.308(a)(5) | Moderate | 2026-11-30 |
| 10 | Coverage arrangement, sealed recovery codes, paper downtime notes | 164.308(a)(7)(ii)(C); 164.312(a)(2)(ii) | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
The **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**; the regulatory agenda projects a final rule in July 2027. It is not a current obligation. If finalized as proposed, it would remove the addressable designation (affecting the 15 addressable gaps), require encryption of ePHI at rest and in transit with limited exceptions, require MFA, require a written technology asset inventory and network map, require penetration testing at least every 12 months and vulnerability scanning, require restoring certain systems within 72 hours, and require a compliance audit at least every 12 months. The `pending_rule_change` column flags the affected rows.
