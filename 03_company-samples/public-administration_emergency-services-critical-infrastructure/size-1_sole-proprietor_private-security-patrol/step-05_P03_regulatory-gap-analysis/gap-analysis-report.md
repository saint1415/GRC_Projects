# Regulatory Gap Analysis: Cris Santos Company | Emergency Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Tier / Vertical | Sole Proprietorship / Emergency Services |
| Regulations analyzed (binding) | **Fla. Stat. 501.171** (reasonable measures, breach notice, disposal) and the information and records duties of **Fla. Stat. Chapter 493** (private security licensing), with **Fla. Stat. 934.03(2)(d)** for body-camera audio. Statute text read from the 2026 Florida Statutes on flsenate.gov on 2026-10-07 |
| Also binding | Client patrol agreements: confidentiality, incident notice, and return-of-information clauses (contract, not law) |
| Yardstick | **NIST CSF 2.0**, at category level (22 categories), used as a **benchmark only** to judge "reasonable measures" under 501.171(2) |
| Regulation named in the scenario brief | HIPAA Security Rule (C-EMERGENCY-R04). **Does not apply** (section 1.1) |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment; tests 2026-08-12) |
| Assessor | Owner, with the on-call IT technician (confidentiality agreement since 2026-08-07). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-08-31 |

## 1. Applicability
### 1.1 The vertical's registry requirements do not reach this business
The Emergency Services registry was built for public agencies, 911 centers, and ambulance services. Each requirement was checked against a one-person private patrol.

| Registry ID | Requirement | Applies? | Reason |
|---|---|---|---|
| C-EMERGENCY-R04 | HIPAA Security Rule, 45 CFR Part 164, Subpart C | **No** | A covered entity is a health plan, a clearinghouse, or "a health care provider who transmits any health information in electronic form in connection with a transaction covered by this subchapter" (45 CFR 160.103). The owner gives first aid on patrol and writes injury notes, but bills no one for health care and conducts no HIPAA standard transactions. Nor is the owner a business associate: no covered entity hires the patrol to handle health information. Injury notes are still "personal information" under Fla. Stat. 501.171(1)(g)1.a.(IV), so they are protected under section 1.2 |
| C-EMERGENCY-R01 | FBI CJIS Security Policy v6.1 | **No** | It governs access to criminal justice information. The business has no connection to criminal justice systems and no agreement with a criminal justice agency. The Division of Licensing, not the agency, receives applicants' criminal history results (Fla. Stat. 493.6108(1)(a), 493.6121(5)). **Trigger to recheck:** any offer by a law enforcement contact to share warrant, criminal history, or intelligence data. POL-01 9.6 forbids accepting it (P01 R-013) |
| C-EMERGENCY-R02, R03 | 28 CFR 20.21(f); 28 CFR Part 23 | **No** | They govern state criminal history systems and federally funded criminal intelligence systems. The business operates neither |
| C-EMERGENCY-R05 | CIRCIA, proposed 6 CFR 226 | **No (proposed rule only, and would not reach the business as drafted)** | No final rule as of 2026-09-25. Proposed 226.2(a) covers entities above the SBA size standard; the business is far under the $29.0 million standard for NAICS 561612. Proposed 226.2(b)(5) covers entities that provide law enforcement, fire and rescue, emergency medical services, emergency management, or public works "to a population equal to or greater than 50,000 individuals" (89 FR 23644, 2024-04-04). A private patrol guarding 7 client properties provides none of these to a population (author's reading). Recheck when a final rule is published |
| C-EMERGENCY-R06 | FCC EAS cybersecurity rules, 47 CFR Part 11 | **No** | Not an EAS participant; originates no public alerts |

### 1.2 What does bind the owner
- **Fla. Stat. 501.171 (primary).** A "covered entity" includes "a sole proprietorship ... that acquires, maintains, stores, or uses personal information" (501.171(1)(b)), with no size threshold. Incident reports name about 90 people with a driver license or ID number (501.171(1)(g)1.a.(II)) and about 15 with injury notes ((IV)). A name with "any information regarding an individual's geolocation" is also personal information ((VII)); the patrol app's GPS tracks are the owner's own, but reports that place a named person at a site at a set time may qualify, and counsel is asked to confirm. Body-camera video is **not** "biometric data": 501.171(1)(g)1.a.(VI) uses the 501.702 definition, which excludes photographs and video or audio recordings. Encrypted information is excluded (501.171(1)(g)2.). The business has no federal functional regulator, so the deemed-compliance path in 501.171(4)(g) is not available.
- **Fla. Stat. Chapter 493 (the governing licensing law).** The business must hold a Class "B" agency license (493.6301(1)) and the owner a Class "D" license (493.6301(5)). Three provisions bear on information: "any unauthorized release of information acquired as a result of activities regulated under this chapter" is grounds for discipline (493.6118(1)(e)); no licensee may "willfully make a false statement or report" to a client or the department (493.6119(4)); and records must be provided on request, "maintained in this state for a period of 2 years at the principal place of business," and made available immediately (493.6121(2)). Conduct rules with no information element (uniforms, use of force, impersonation, advertising) are outside a security gap analysis; the owner self-attests compliance. The department's rules in Chapter 5N-1, F.A.C. could not be reached from this environment, so counsel is asked to confirm that no rule adds record-keeping or data duties (action 10).
- **Fla. Stat. 934.03.** Interception of an oral communication is lawful when "all parties have given prior consent" (934.03(2)(d)). The body camera records audio, so this applies to some patrol conversations (row G-018).
- **Client patrol agreements.** All 7 contain confidentiality, 2-hour and 24-hour notice, and return-of-information clauses (rows G-019 to G-021).

### 1.3 Yardstick for "reasonable measures"
501.171(2) does not define reasonable measures. The owner uses **NIST CSF 2.0** at category level as the yardstick, because it is the sector-neutral baseline and its official mapping to SP 800-53 is in this repository. The CSF rows are rated like requirements so the action list shows gaps, but **a CSF gap is not a violation.** The statute, licensing, and contract rows are.

**Considered and not applicable:** Florida Digital Bill of Rights (a "controller" under Fla. Stat. 501.702 must exceed $1 billion in global gross annual revenue and meet one of three further tests; the business has about $180,000); PCI DSS (no cards accepted; clients pay by ACH or check); SEC disclosure rules (not a public company).

**Excluded rows, with reasons (4):** G-005 (fewer than 1,000 individuals in all records), G-011 (investigative files: no private investigation), G-016 (no employees), and G-017 (firearm and detention rules need a Class "G" license, which the owner does not hold).

## 2. Method
1. **Requirements.** 501.171 was decomposed by subsection. Chapter 493 rows cover each provision that bears on information, records, or the licenses those duties attach to, at the most specific citation. CSF rows are the 22 CSF 2.0 categories from `00_universal-framework/frameworks/csf2_core.csv`, with the key subcategories named. **43 rows in total.**
2. **Requirement type.** Florida duties are "shall" or grounds-for-discipline duties. Contract rows are labeled "Contractual". CSF rows are labeled "Benchmark (not binding)".
3. **Crosswalk.** Statute and contract rows use an **author mapping** to CSF 2.0 and SP 800-53; no official NIST mapping of these sources exists. CSF rows use the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, in `00_universal-framework/crosswalks/`); the controls listed are the author's key-control subset of that mapping.
4. **Evidence.** Self-attested by the owner and checked on screen with the IT technician on 2026-08-12: account security pages and sign-in tests, the patrol app user list and AI settings, the code spreadsheet and phone, the body-camera card and sharing links, the router admin page, the vehicle and key ring, the 7 client agreements (read 2026-08-11), and the license and insurance documents.
5. **Status.** Met, Partially met, Not met, or Not applicable as of the end of fieldwork (2026-08-14). Fixes since then appear in the remediation columns, not as a changed status. Gap risk uses the P01 scale.

## 3. Results summary
| Source | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| Fla. Stat. 501.171 | 0 | 3 | 3 | 1 | 7 |
| Fla. Stat. Chapter 493 | 3 | 4 | 0 | 3 | 10 |
| Fla. Stat. 934.03 | 0 | 1 | 0 | 0 | 1 |
| Client patrol agreements | 0 | 2 | 1 | 0 | 3 |
| NIST CSF 2.0 benchmark | 1 | 11 | 10 | 0 | 22 |
| **Total** | **4** | **21** | **14** | **4** | **43** |

Of the 35 rows with gaps, 5 are rated **High**, 18 **Moderate**, and 12 **Low**. The High rows are G-001 (501.171(2) reasonable measures), G-009 (493.6118(1)(e) unauthorized release), G-019 (contract confidentiality), G-031 (CSF PR.AA), and G-033 (CSF PR.DS).

**The main finding.** The licensing basics are in order: both licenses are current, the insurance is on file, and the backup agency is licensed (3 of 7 applicable Chapter 493 rows Met). What is weak is **custody of what clients entrust to the owner**. Codes sit in four places, keys hang on a labeled ring, former client staff can still read reports, and video leaves by public links. Each is a path to an "unauthorized release of information acquired as a result of activities regulated under this chapter" (493.6118(1)(e)), which is a licensing matter as well as a 501.171 and contract matter.

## 4. Action list (half page)
In order. The first five cost nothing.

| # | Action | Rows | Gap risk | Target |
|---|---|---|---|---|
| 1 | Adopt POL-01 (written program, designation, retention, AI and recording rules) | G-001, G-010, G-025 | High | 2026-08-31 (done) |
| 2 | Codes into the password manager vault and one sealed paper copy in the safe; delete the spreadsheet, note, and texts; remove the former client's codes | G-009, G-019, G-021 | High | 2026-09-15 |
| 3 | App-based MFA on the patrol app admin account and email; password manager | G-031 | High | 2026-09-15 |
| 4 | Remove the 3 stale portal accounts; expire the 14 public video links | G-009, G-021 | High | 2026-09-15 |
| 5 | Adopt and print the P08 runbook and notification matrix (30-day Florida clock, 2-hour client clause, department claim notice) | G-002 to G-004, G-013, G-020 | Moderate | 2026-09-30 |
| 6 | Separate laptop accounts; versioned backup; camera card copied off and cleared each week | G-033, G-012 | High | 2026-10-31 |
| 7 | Coded key tags, vehicle lockbox, monthly key count | G-019 | High | 2026-10-31 |
| 8 | Vendor list with security contacts; ask the patrol app vendor to confirm 10-day notice | G-006, G-027 | Moderate | 2026-10-31 |
| 9 | Announce recording at every contact; counsel advice on audio | G-018 | Moderate | 2026-10-31 |
| 10 | Counsel review: 493.6121(2) and cloud storage; Chapter 5N-1, F.A.C.; geolocation in reports | G-012, G-001 | Moderate | 2026-12-31 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending changes to watch
- **CIRCIA** (C-EMERGENCY-R05) is still proposed. As drafted it would require reports to CISA within 72 hours of a reasonable belief that a covered cyber incident occurred and within 24 hours of a ransom payment, but section 1.1 explains why the draft would not reach this business. Recheck when a final rule is published.
- **Fla. Stat. 501.171.** The 2026 text lists biometric data and geolocation as personal information. Recheck the definitions each year.
- **Chapter 493.** Recheck each year, and before adding armed work (Class "G"), employees, or investigative services, each of which turns on rows now marked not applicable.
