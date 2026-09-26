# Regulatory Gap Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm, NAICS 561320) |
| Tier / Vertical | Small / Administrative and Support and Waste Management and Remediation Services |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`) |
| Secondary rules (binding) | Form I-9 retention, inspection, and electronic I-9 standards, 8 CFR 274a.2 (N56-R03); the E-Verify MOU; Florida's E-Verify statute, Fla. Stat. 448.095; FCRA employment screening, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02); the FACTA Disposal Rule, 16 CFR 682.3 (N56-R01); the Florida Information Protection Act, Fla. Stat. 501.171 |
| Checked and found not applicable | N56-R04 (HIPAA business associate), N56-R05 (TCPA/TSR), N56-R06 (PCI DSS), N56-R07 (FAR 52.204-21), N56-R08 (NYC Local Law 144), N56-R09 (PHMSA security plans) |
| Text verified | eCFR (8 CFR 274a.2; 16 CFR 682.3) as of 2026-09-23; U.S. Code (15 U.S.C. 1681b, 1681m) from uscode.house.gov; 2026 Florida Statutes (501.171 as amended by ch. 2026-52; 448.095); E-Verify MOU for Employers (revision 06/01/13) and ICE notice 88 FR 47749 on the remote alternative procedure |
| Assessment dates | 2026-07-13 to 2026-07-24 (HQ walkthrough 2026-07-15; Branch 3 walkthrough 2026-07-16). Row G-129 updated 2026-08-07 with a P07 finding |
| Assessor | IT Manager (Information Security Lead) with the HR and Compliance Manager and the Payroll Manager |
| Workbook | `gap-analysis.csv` (151 rows) |

## 1. Applicability
**Step 1 was to find a cybersecurity rule that binds a temporary staffing firm. None does.** The vertical profile names NIST CSF 2.0 as the primary benchmark because NAICS 56 has no sector-specific federal cyber mandate. That holds for this firm:

| Candidate | Applies? | Why (citation) |
|---|---|---|
| HIPAA Security Rule as a business associate (N56-R04) | **No** | A business associate creates, receives, maintains, or transmits PHI for a covered entity (45 CFR 160.103). The firm places warehouse, light industrial, and office workers, none with clinical duties, and does no work for health care clients involving PHI. Its group health plan for eligible associates is fully insured; plan-level HIPAA duties were not analyzed |
| TCPA and Telemarketing Sales Rule (N56-R05) | **No for this analysis** | The firm does not sell goods or services by phone. Recruiting texts go to candidates who opted in through the ATS. TCPA consent details were not analyzed; they are a contact-consent duty, not a security duty |
| PCI DSS (N56-R06) | **No** | The firm takes no payment cards; clients pay by ACH or check |
| FAR 52.204-21 (N56-R07) | **No** | No federal contracts or subcontracts |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates, jobs, or offices. The AI tool is assessed under federal law in P10 |
| PHMSA security plans (N56-R09) | **No** | The firm does not offer or transport hazardous materials |
| CIRCIA, proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25, and the firm is not in a proposed sector criterion and is under its SBA size standard |

**Decision: use NIST CSF 2.0 as the benchmark.** It is voluntary. Status ratings measure the firm against its own Target Profile, not against a legal duty.

**Secondary rules: the binding rules that govern the data in the primary system.** A staffing firm's most sensitive records exist because the law requires them. The firm is the employer of record for about 2,000 new associates a year, so it completes and keeps a Form I-9 for each one, runs E-Verify, and orders consumer reports for most placements. These rules were assessed at requirement level because they decide how the APATP must protect those records:
- **Form I-9, 8 CFR 274a.2 (N56-R03).** Retention and inspection (b)(2), document copies (b)(3), use limits (b)(4), and, because the firm completes and keeps I-9s electronically, the electronic system standards in (e), documentation in (f), records security program in (g), and electronic signatures in (h)-(i). Paragraph (g)(1) is effectively a small security control set: access limited to authorized personnel, backup and recovery, trained staff, and a permanent audit record of every change.
- **E-Verify MOU.** The firm signed the MOU for Employers. Its Article II.A covers user access (II.A.3), the tutorial (II.A.5), case timing and use limits (II.A.7-11), safeguarding information and passwords (II.A.15), and **immediate breach notice to DHS** (II.A.16). Paragraph numbers follow the MOU template posted on e-verify.gov (revision 06/01/13).
- **Fla. Stat. 448.095.** Since 2023-07-01, a private employer with 25 or more employees must use E-Verify for new employees (448.095(2)(b)2.), certify compliance on its first reemployment tax return each year ((2)(b)3.), document any E-Verify outage ((2)(c)), and keep the documentation and verifications at least 3 years ((2)(d)). Checked 2026 statute: the 25-employee threshold is unchanged. The statute defines "employee" as someone filling a permanent position (448.095(1)(b)). Whether temporary associates are covered was not resolved here, and it does not matter in practice: the MOU requires the firm to verify all new employees and not selectively (II.A.11).
- **FCRA, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02).** Certification to the screening provider, the standalone disclosure and written authorization, and the pre-adverse and adverse action notices.
- **FACTA Disposal Rule, 16 CFR 682.3 (N56-R01).** Reasonable measures when disposing of consumer report information.
- **Fla. Stat. 501.171 (2026).** The firm is a "covered entity" (a commercial entity that maintains personal information). Personal information includes a name with an SSN, a driver license or passport number, or **geolocation**, which reaches the timekeeping app's clock-in locations. A financial account number counts only in combination with a code or password that permits access (501.171(1)(g)1.a.(III)), so direct deposit numbers alone may not trigger notice; the SSNs stored with them do. Subsections (2) security, (3)-(6) notice, and (8) disposal were assessed.

**Also checked, outside this workbook:** Title VII's disparate impact provision (42 U.S.C. 2000e-2(k)) and the ADA's selection criteria provision (42 U.S.C. 12112(b)(6)) apply to the AI screening tool and are assessed in P10.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current as of 2026-09-23, the U.S. Code, the 2026 Florida Statutes, and the E-Verify MOU, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the firm's CSF Target Profile (High 35, Medium 48, Low 23), set by the IT Manager and the COO from the risk register (P01) and BIA (P05). Subcategories that protect SSNs, I-9 records, and payroll are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping (no official NIST mapping exists for these rules).
4. **Evidence.** Interviews (COO, Controller, Payroll Manager, HR and Compliance Manager, Director of Recruiting, 3 Onboarding Specialists, 2 Branch Managers, 8 other staff, the managed IT provider), document review, configuration exports, a sample of 25 associate I-9s with E-Verify cases, 20 background check rejections, a 30-form sample of the scanned I-9 archive, and walkthroughs of HQ and Branch 3.
5. **Status.** Met, Partially met, Not met, or Not applicable. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 1 (Partial).** Security has been informal and reactive. **Target: Tier 2 (Risk Informed) by 2027-08**, meaning practices approved by leadership and driven by the risk register.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 1 | 14 | 16 | 0 |
| CSF 2.0 Identify (21) | 0 | 11 | 10 | 0 |
| CSF 2.0 Protect (22) | 3 | 14 | 4 | 1 |
| CSF 2.0 Detect (11) | 0 | 4 | 7 | 0 |
| CSF 2.0 Respond (13) | 0 | 0 | 13 | 0 |
| CSF 2.0 Recover (8) | 0 | 0 | 8 | 0 |
| **CSF 2.0 subtotal (106)** | **4** | **43** | **58** | **1** |
| Form I-9, 8 CFR 274a.2 (19) | 3 | 12 | 4 | 0 |
| E-Verify MOU (5) | 1 | 1 | 3 | 0 |
| Fla. Stat. 448.095 (4) | 2 | 1 | 1 | 0 |
| FCRA, 15 U.S.C. 1681b(b) and 1681m(a) (4) | 2 | 1 | 1 | 0 |
| Disposal Rule, 16 CFR 682.3 (1) | 0 | 1 | 0 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 3 | 3 | 0 |
| Vertical requirements found not applicable (6) | 0 | 0 | 0 | 6 |
| **Total (151)** | **12** | **62** | **70** | **7** |

Of the 132 unmet or partially met rows, 9 are rated High, 68 Moderate, 53 Low, and 2 Very Low.

**The pattern:** the firm does the compliance steps that happen once per hire fairly well (Section 2 timing, E-Verify cases, FCRA authorization and adverse action letters, electronic signatures), but it **does not protect the records those steps create**. SSNs, I-9 images, and consumer reports are copied to places many people can reach, kept forever, backed up in ways an attacker could destroy, and not watched. Respond and Recover are entirely Not met: nothing existed before the P08 runbook.

The not applicable CSF row is PR.PS-06 (secure software development): the firm writes no software. The integration service is a vendor connector the IT Manager configures, covered by PR.PS-01 and ID.RA-07.

## 4. Priority gaps and roadmap
| Gap | Row(s) | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Payroll platform sign-in can be phished; credentials outside SSO | G-053, G-055 | High | SSO with number-matching MFA; E-Verify and payroll on the termination checklist | IT Manager | 2026-11-30 |
| SSNs and bank accounts over-copied and over-shared | G-037, G-057, G-061, G-140 | High | Data inventory; remove full SSNs from the reporting database; split ATS roles | IT Manager / HR and Compliance Manager | 2026-11-30 |
| Backups (including the I-9 archive) exposed and untested | G-064, G-122 | High | Immutable separate-account backups; restore test 2026-10-15 | IT Manager | 2026-12-31 |
| No monitoring of payroll exports, bank changes, or ATS downloads | G-077 | High | Weekly review and alerts; 1-year log retention | IT Manager | 2026-11-30 |
| I-9 access limited to authorized personnel; audit trail and system documentation | G-118, G-120, G-121, G-124 | Moderate | Restrict I-9 images; archive logging; I-9 system description and procedure | HR and Compliance Manager | 2026-12-31 |
| E-Verify access, credential sharing, and DHS breach notice | G-126, G-129, G-130 | Moderate | Deactivate departed users; named accounts only; DHS notice step in P08 | HR and Compliance Manager | 2026-09-30 (access); 2026-11-30 (notice) |
| FCRA disclosure not standalone | G-136 | Moderate | Disclosure-only page reviewed by counsel | HR and Compliance Manager | 2026-09-30 |
| No breach notice procedure (Florida 30 days) | G-141, G-142 | Moderate | P08 matrix and templates; tabletop | HR and Compliance Manager | 2026-11-30 |
| No change control (AI tool mode switched without review) | G-045 | Moderate | Change log with COO approval for payroll, I-9, and AI settings | IT Manager | 2026-11-30 |
| No manual payroll procedure | G-073 | Moderate | Off-cycle payroll from the prior register | Payroll Manager | 2026-12-31 |
| Electronic media disposal and retention | G-038, G-139, G-145 | Moderate | Retention schedule; certified device destruction; purge | HR and Compliance Manager / IT Manager | 2026-12-31 |

The full list, with evidence, is in `gap-analysis.csv`. High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07).

## 5. Pending changes (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226, 89 FR 23644): no final rule as of 2026-09-25; the firm would not be covered as proposed.
- **Form I-9 and E-Verify:** a Federal Register search for "274a.2" (2025-01-01 to 2026-09-25) found no proposed change to the retention or electronic I-9 standards assessed here. One related change is already in effect: a DHS interim final rule (90 FR 48799, effective 2025-10-30) ended automatic extension of many renewal EADs, which shortens reverification lead time for some associates; onboarding reverification alerts should reflect it. The remote alternative procedure (88 FR 47749) remains available only to E-Verify participants in good standing, so an MOU violation (G-126, G-129) could also cost the firm the remote option it uses for Office and Administrative hires.
- **Fla. Stat. 448.095:** 2026 statute read; state bills were not tracked. Expansion of the E-Verify duty to all employers would not change the firm's position.
- **Fla. Stat. 501.171:** amended in 2026 (ch. 2026-52); the 2026 text was used. State bills were not tracked.
- **FCRA:** no pending change affecting 1681b(b) was identified; the CFPB withdrew its 2024 circular on background dossiers and algorithmic worker scores on 2025-05-12 (the statute itself is unchanged; see P10).
