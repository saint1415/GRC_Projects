# Regulatory Gap Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm, NAICS 561320) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`) |
| Binding rules for the primary business line | Form I-9, 8 CFR 274a.2 (N56-R03); the E-Verify MOU; Fla. Stat. 448.095; FCRA employment screening, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02); the FACTA Disposal Rule, 16 CFR 682.3 (N56-R01); Fla. Stat. 501.171; ADA medical record confidentiality, 29 CFR 1630.14; Fla. Stat. 400.980 (health care services pool); Fla. Stat. 934.03 (call recording consent) |
| Checked and found not applicable | N56-R04 (HIPAA business associate, with full reasoning), N56-R05 (TCPA/TSR), N56-R06 (PCI DSS), N56-R07 (FAR 52.204-21), N56-R08 (NYC Local Law 144), N56-R09 (PHMSA security plans) |
| Text verified | eCFR as of 2026-09-23 (8 CFR 274a.2; 16 CFR 682.3; 29 CFR 1630.14; 45 CFR 160.103); U.S. Code (15 U.S.C. 1681b, 1681m); 2026 Florida Statutes (501.171 as amended by s. 9, ch. 2026-52; 501.702; 448.095; 400.980; 408.809; 435.04; 934.03); E-Verify MOU for Employers (revision 06/01/13) |
| Assessment dates | 2026-07-13 to 2026-08-07 (HQ 2026-07-21; Branch 6 2026-07-22; On-site Program 2 2026-07-23); evidence refreshed with P07 results through 2026-09-04 |
| Assessor | Security Manager and the GRC analyst with the Director of Compliance and Privacy, the General Counsel, and the vCISO; samples drawn using the co-sourced internal audit firm's sampling table, and the workbook reviewed by that firm |
| Approved | Chief Operating Officer, 2026-09-22 |
| Workbook | `gap-analysis.csv` (157 rows) |

## 1. Applicability
Applicability was decided at intake in the [obligations register](../step-00_P00_intake/obligations-register.csv). This section restates the result for the rules analyzed here.

**Primary business line:** temporary help services in Florida (Light Industrial, Office and Professional, Healthcare Staffing), with the MSP program and direct hire as adjacent services.

**Step 1 was to find a cybersecurity rule that binds a staffing firm. None does,** at this size or any other: the vertical profile names NIST CSF 2.0 as the benchmark because NAICS 56 has no sector-specific federal cyber mandate.

| Candidate | Applies? | Why (citation) |
|---|---|---|
| HIPAA Security Rule as a business associate (N56-R04) | **No** | The Healthcare Staffing unit places nurses and allied staff in hospitals, so this was analyzed closely (row G-152). A business associate creates, receives, maintains, or transmits PHI on behalf of a covered entity "other than in the capacity of a member of the workforce" (45 CFR 160.103). **Workforce** includes persons "whose conduct, in the performance of work for a covered entity ... is under the direct control of such covered entity ... whether or not they are paid by" it (160.103). Placed clinicians work under the facility's direct control, so their access to PHI is the facility's workforce access. The firm's own staff receive no PHI from facilities to perform placement services, and clinicians' health records are the firm's own employment records. Two hospital BAA templates were declined on this basis in 2025. **Recheck** before offering any service the firm itself controls that involves PHI (for example remote coding or billing staff working under the firm's direction) |
| TCPA and Telemarketing Sales Rule (N56-R05) | **No for this analysis** | The firm does not sell by phone. Recruiting texts go to candidates who opted in; TCPA consent details are a contact-consent duty, not a security duty, and were not analyzed |
| PCI DSS (N56-R06) | **No** | No payment cards; clients pay by ACH or check |
| FAR 52.204-21 (N56-R07) | **No** | No federal contracts or subcontracts |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates, jobs, or offices; AI tools are assessed under federal law in P10 |
| PHMSA security plans (N56-R09) | **No** | No hazardous materials |
| CIRCIA, proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25. As proposed, the firm would exceed its SBA size standard, but whether a staffing firm is "in a critical infrastructure sector" under the proposed definition is uncertain; counsel will assess if a final rule is published |
| SEC cybersecurity disclosure rules | **No** | Privately held |

**Decision: use NIST CSF 2.0 as the benchmark,** with a Target Profile approved by the COO. Status ratings for CSF rows measure the firm against its own Target Profile, not a legal duty.

**Binding rules assessed at requirement level.** At Mid-Market every binding rule for the primary business line is analyzed, with evidence sampling:
- **Form I-9, 8 CFR 274a.2 (N56-R03).** The firm is employer of record for about 13,800 new associates a year and keeps I-9s electronically, so the electronic system standards in (e), documentation in (f), the records security program in (g), and electronic signatures in (h)-(i) apply, along with retention, inspection, copies, and use limits in (b).
- **E-Verify MOU.** Access (Art. II.A.3), tutorial (II.A.5), case numbers on the I-9 (II.A.7), the 3-business-day case timing, no pre-screening, and verifying all new employees (II.A.9-11), safeguarding (II.A.15), and **immediate** breach notice to DHS (II.A.16).
- **Fla. Stat. 448.095.** E-Verify for private employers with 25 or more employees ((2)(b)2.), the annual certification ((2)(b)3.), outage documentation ((2)(c)), and 3-year retention ((2)(d)).
- **FCRA, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02).** About 10,900 consumer reports a year.
- **FACTA Disposal Rule, 16 CFR 682.3 (N56-R01).**
- **Fla. Stat. 501.171 (2026).** Personal information here reaches SSNs, ID numbers, **medical information** (clinician health records, (1)(g)1.a.(IV)), **biometric data** as defined in 501.702 (finger templates from the on-site clocks, (VI); 501.702(4) names fingerprints), and **geolocation** (timekeeping app, (VII)).
- **ADA, 29 CFR 1630.14 (added at this size).** The firm makes post-offer health inquiries of clinicians (immunizations, TB tests, physicals) and periodic inquiries of current clinicians. Information from those must be kept on separate forms, in separate medical files, as confidential medical records ((b)(1), (c)(1)).
- **Fla. Stat. 400.980 (added at this size).** As a registered health care services pool, the firm must obtain level 2 screening (400.980(3); 408.809(1)(e), with rescreening every 5 years under 408.809(2); fingerprint-based checks under 435.04(1)(a)) and verify and keep documentation of each clinician's credentials (400.980(5)). Those records are a security concern because they must stay available and accurate.
- **Fla. Stat. 934.03(2)(d) (added at this size).** The recruiting contact center records calls; interception is lawful when all parties consent.

**Also checked, outside this workbook:** Title VII (42 U.S.C. 2000e-2(b), (k)), the ADEA (29 U.S.C. 623(b)), and the ADA (42 U.S.C. 12112(b)(6)) for the AI tools, assessed in P10. The FLSA payday rule for overtime (29 CFR 778.106) is a driver in the BIA and the payroll outage runbook.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategories come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows were decomposed from the eCFR, U.S. Code, Florida Statutes, and MOU texts listed above, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority (High 49, Medium 46, Low 11), set by the vCISO and the COO from the risk register (P01) and BIA (P05). Subcategories protecting SSNs, bank data, I-9 records, medical information, and payroll are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`; the `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping (no official NIST mapping exists for these rules).
4. **Evidence.** Current state was established from the intake evidence (exports, documents and records collected 2026-06-22 to 2026-07-10, EV-001 to EV-060), gap analysis interviews with the General Counsel, the Onboarding and Compliance Specialists, the Director of Compliance and Privacy and the other process owners (EV-063 to EV-066), walkthroughs of HQ with Branch 1, Branch 6 and On-site Program 2 (2026-07-21 to 2026-07-23, EV-067), the mailbox and file-share searches (EV-072), the TLS scan (EV-074), the residence-state report test (EV-075), the firewall rule review (EV-076), and the samples below (EV-068 to EV-071, EV-073, EV-077). Approvals dated 2026-09-22 are cited from EV-078, and P07 results by the P07 evidence IDs (for example EV-IA-5). The `evidence` column in `gap-analysis.csv` cites the [evidence register](../step-00_P00_intake/evidence-register.csv) ID behind each status.
5. **Evidence sampling.** Where a requirement operates many times, a random sample was tested from a system-generated population collected at intake (for example the 142 terminations in EV-003, the 2026 H1 hires and shift starts in EV-055, the 64 vendors in EV-042, and the 41 critical findings in EV-018), sized with the co-sourced internal audit firm's attribute sampling table (25 items for a control operating many times a year at moderate risk, 50 where the population exceeds 5,000):
   - new associate hires, I-9 Section 2 and E-Verify timing: 50 of about 6,900 (2026 H1);
   - remote I-9 examinations: 15 of about 900;
   - scanned archive forms: 50 of about 74,000;
   - internal staff terminations: 25 of 142;
   - background check rejections: 25 of 310 (2026 H1);
   - onboarding packets (FCRA disclosure and authorization): 25;
   - Healthcare shift starts: 25 of about 10,800 (2026 H1);
   - clinician level 2 screenings: 25 of about 520;
   - credential files: 25 of about 2,600;
   - vendor contracts: 20 of 64;
   - outbound recruiter call recordings: 20;
   - critical vulnerability findings: all 41 (2026 H1);
   - full searches of mailboxes and file shares for document images and SSN extracts.
   Each `evidence` cell names its sample and result.
6. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 2 (Risk Informed).** The program has approved policies and a risk method, but practices are not yet consistent across SaaS, vendors, and AI. **Target: Tier 3 (Repeatable) by 2027-12-31,** in step with the SOC 2 Type 2 observation period.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A | Total |
|---|---|---|---|---|---|
| CSF 2.0 Govern | 9 | 18 | 4 | 0 | 31 |
| CSF 2.0 Identify | 5 | 11 | 5 | 0 | 21 |
| CSF 2.0 Protect | 5 | 15 | 2 | 0 | 22 |
| CSF 2.0 Detect | 2 | 8 | 1 | 0 | 11 |
| CSF 2.0 Respond | 0 | 13 | 0 | 0 | 13 |
| CSF 2.0 Recover | 0 | 7 | 1 | 0 | 8 |
| **CSF 2.0 subtotal** | **21** | **72** | **13** | **0** | **106** |
| Form I-9, 8 CFR 274a.2 | 3 | 12 | 4 | 0 | 19 |
| E-Verify MOU | 1 | 3 | 1 | 0 | 5 |
| Fla. Stat. 448.095 | 2 | 1 | 1 | 0 | 4 |
| FCRA, 15 U.S.C. 1681b(b) and 1681m(a) | 3 | 1 | 0 | 0 | 4 |
| Disposal Rule, 16 CFR 682.3 | 0 | 1 | 0 | 0 | 1 |
| Fla. Stat. 501.171 | 0 | 6 | 0 | 0 | 6 |
| ADA, 29 CFR 1630.14 | 0 | 0 | 2 | 0 | 2 |
| Fla. Stat. 400.980 | 1 | 2 | 0 | 0 | 3 |
| Fla. Stat. 934.03 | 0 | 1 | 0 | 0 | 1 |
| Vertical requirements found not applicable | 0 | 0 | 0 | 6 | 6 |
| **Total** | **31** | **99** | **21** | **6** | **157** |

**Gap risk ratings (120 rows Partially met or Not met):** 11 High, 64 Moderate, 45 Low.

**The pattern.** The program does the visible things well: staff MFA, EDR with 24x7 monitoring, encryption, write-once backups, an FCRA disclosure fixed in 2024, and E-Verify for every hire. The gaps sit where the firm's scale outgrew its controls:
- **identity where money moves:** associate SMS sign-in, push-relay exposure for payroll staff, and a static payroll API key (G-055, G-070);
- **least privilege and minimization for Restricted data:** 262 users with I-9 and consumer report access, 46 with full SSNs, and medical files mixed with credentials (G-057, G-061, G-146);
- **SaaS visibility:** no monitoring of payroll exports, bank changes, or ATS downloads (G-068, G-077);
- **recovery of what the law requires the firm to keep:** the I-9 archive is not backed up, and there is no manual payroll (G-064, G-102, G-122);
- **suppliers:** no tiering, few contract terms, and a credentialing vendor with no SOC 2 report (G-022 to G-031).

Respond and Recover have no Met rows: the runbooks and the BIA exist only since September 2026 and have never been exercised.

## 4. Priority gaps
| Gap | Row(s) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Weak authentication where pay can be redirected (associate SMS codes, push relay, static API key) | G-055, G-070 | High | Associate app-based codes or passkeys and bank-change hold; phishing-resistant keys for payroll and administrators; key rotation and secret scanning | IT Director | 2026-12-31 (keys 2026-10-15) |
| Least privilege for I-9 images, consumer reports, SSNs, and medical files | G-057, G-112, G-121 | High | Role redesign; quarterly ATS role review; payroll role split | Director of Compliance and Privacy | 2026-12-31 |
| Data inventory and minimization | G-037, G-061 | High | Data inventory; last-4 masking in the warehouse; purge file-share extracts | Director of Compliance and Privacy / Security Manager | 2026-12-31 |
| I-9 archive backups and restore testing | G-064, G-122 | High | Archive in the backup plan with write-once retention; quarterly restore tests | IT Director | 2026-12-31 |
| No monitoring of SaaS activity | G-068, G-077 | High | SaaS log connectors and alert rules for exports, bank changes, downloads | Security Manager | 2027-01-31 |
| No off-cycle manual payroll | G-102 | High | Written and tested procedure with the bank and payroll vendor | Director of Payroll and Billing | 2026-12-31 |
| Florida reasonable measures for the largest SSN stores | G-140 | High | Close the P01 High and Very High risks on schedule | Chief Operating Officer | 2027-03-31 |
| ADA medical files not separate or confidential | G-146, G-147 | Moderate | Separate medical category; clearance-only views; scoped client release | Credentialing Manager | 2027-01-31 |
| Electronic I-9 program (QA, system description, procedures, audit trail) | G-114, G-118, G-120, G-124 | Moderate | I-9 program documentation; quarterly QA; archive logging | Director of Compliance and Privacy | 2026-12-31 |
| E-Verify access for departed users | G-126 | Moderate | Deactivate; termination checklist; monthly reconciliation | Director of Compliance and Privacy | 2026-10-31 |
| Supplier risk program | G-022, G-025, G-026 | Moderate | STD-03 with tiers, contract terms, and annual reviews | Security Manager | 2026-12-31 |
| No change control for SaaS and AI settings | G-045 | Moderate | SaaS change log with approval | IT Director | 2026-12-31 |
| Breach notices: templates and scoping | G-141, G-142 | Moderate | Templates; residence-state report; tabletop | General Counsel | 2026-11-30 |
| Recorded outbound calls without consent | G-151 | Moderate | Announcement or recording off | Contact Center Manager | 2026-11-30 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | API key rotated and moved to the secrets service; departed E-Verify and VMS accounts removed; AI ranking in sort-only mode; recording announcement; notice templates and the first tabletop (2026-11-12); I-9 and consumer report access restricted; warehouse masking; archive backups; contingency plan and manual payroll procedure; vendor tiering; associate portal sign-in upgrade | G-037, G-055, G-057, G-061, G-064, G-070, G-102, G-122, G-126, G-141, G-142, G-151 |
| **2. Build** | 2027 Q1 | SaaS logs and alerts in the SIEM; phishing-resistant keys for payroll and administrators; ADA medical file separation; first records purge; standards STD-01 to STD-10 issued; SaaS change control; payroll outage tabletop (2027-02-17); kiosk segmentation; SOC 2 Type 1 (2027-03-31) | G-045, G-068, G-077, G-146, G-147, G-038 |
| **3. Prove** | 2027 Q2-Q3 | SOC 2 Type 2 observation (2027-04-01 to 2027-09-30); quarterly restore tests; first annual DR exercise; mock I-9 inspection; Tier 1 vendor reviews | G-049 to G-052, G-099 to G-104, G-110 |
| **4. Sustain** | 2027 Q4 | Annual risk assessment (July 2027); SOC 2 Type 2 report (by 2027-11-30); second P07 assessment; CSF Tier 3 self-assessment | GV.OV and ID.IM rows |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending and recent changes (not current obligations unless stated)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25. See section 1.
- **Employment authorization documents (in effect):** a DHS interim final rule (90 FR 48799, effective 2025-10-30) removed the automatic extension of many renewal EADs. Reverification alerts in the I-9 module were updated in 2026-01; the change shortens lead time for some associates.
- **Remote I-9 alternative procedure (in effect):** available only to E-Verify participants in good standing (88 FR 47749). An MOU violation (G-126) could cost the firm the remote option it uses for about 1,800 hires a year.
- **EEOC:** on 2026-07-23 the EEOC **proposed** removing the EEO-1 to EEO-6 reporting requirements (91 FR 46332). Proposed only; not treated as current law. See P10 for the federal posture on disparate impact.
- **Fla. Stat. 501.171:** amended in 2026 (s. 9, ch. 2026-52); the 2026 text was used. Florida bills were not tracked.
- **Colorado SB26-189** (automated decision-making in consequential decisions, effective 2027-01-01): applies to deployers doing business in Colorado; not applicable while the firm operates only in Florida (P10).
- **FCRA:** no pending change to 15 U.S.C. 1681b(b) was identified.
- **HIPAA Security Rule NPRM** (90 FR 898): proposed only, and it would not change the business associate finding.
