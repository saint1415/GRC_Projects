# Regulatory Gap Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm, NAICS 561320) |
| Tier / Vertical | Micro / Administrative and Support and Waste Management and Remediation Services |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29, all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`) |
| Secondary rules (binding) | Form I-9, 8 CFR 274a.2 (N56-R03); the E-Verify MOU for Employers; Fla. Stat. 448.095; FCRA employment screening, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02); the FACTA Disposal Rule, 16 CFR 682.3 (N56-R01); the Florida Information Protection Act, Fla. Stat. 501.171 |
| Checked and found not applicable | N56-R04 (HIPAA business associate), N56-R05 (TCPA/TSR), N56-R06 (PCI DSS), N56-R07 (FAR 52.204-21), N56-R08 (NYC Local Law 144), N56-R09 (PHMSA security plans) |
| Text verified | eCFR 8 CFR 274a.2 as of 2026-09-23; E-Verify MOU for Employers (revision date 06/01/13) from e-verify.gov; 2026 Florida Statutes 448.095 and 501.171 from flsenate.gov (read 2026-10-06); 15 U.S.C. 1681b and 1681m from govinfo.gov (2023 edition of the U.S. Code) |
| Assessment dates | 2026-07-20 to 2026-07-31 (office walkthrough 2026-07-22). Row G-123 updated 2026-08-12 with a P07 finding |
| Assessor | Operations Manager (Security and Privacy Lead) with the MSP lead technician; the Onboarding and Payroll Coordinator for the Form I-9, E-Verify, and FCRA rows |
| Approved | 2026-08-31 by the Owner |
| Workbook | `gap-analysis.csv` (149 rows) |

## 1. Applicability
**Step 1 was to look for a cybersecurity rule that binds a 7-person temporary staffing firm. None does.** The vertical profile names NIST CSF 2.0 as the primary benchmark because NAICS 56 has no sector-specific federal cyber mandate. That holds here:

| Candidate | Applies? | Why |
|---|---|---|
| HIPAA Security Rule as a business associate (N56-R04) | **No** | A business associate handles PHI for a covered entity (45 CFR 160.103). The firm places warehouse, event, and office workers, none with clinical duties, and does no work for health care clients involving PHI |
| TCPA and Telemarketing Sales Rule (N56-R05) | **No for this analysis** | The firm does not sell by phone. Recruiters text candidates who opted in; consent details were not analyzed (a contact-consent duty, not a security duty) |
| PCI DSS (N56-R06) | **No** | No payment cards |
| FAR 52.204-21 (N56-R07) | **No** | No federal contracts or subcontracts |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates or jobs (P10) |
| PHMSA security plans (N56-R09) | **No** | No hazardous materials |
| CIRCIA, proposed 6 CFR Part 226 | **No (proposed)** | No final rule as of 2026-09-25 |

**Decision: use NIST CSF 2.0 as the benchmark.** It is voluntary, so status ratings measure the firm against its own Target Profile, not against a legal duty.

**Secondary rules: the binding rules behind the most sensitive records.** A staffing firm keeps SSNs, identity documents, and consumer reports because the law makes it collect them. These rules were assessed at requirement level because they decide how the PATS must protect those records:
- **Form I-9, 8 CFR 274a.2 (N56-R03).** The firm is the employer of record for about 120 new associates a year. It completes Forms I-9 on paper and photocopies every document. **Since 2024-03 it has also scanned each Form I-9 and its document copies into the shared drive.** Under 274a.2(b)(3), copies or electronic images of documents "must either be retained with the Form I-9 or stored with the employee's records and be retrievable consistent with paragraphs (e), (f), (g), (h), and (i)". So the scans pull in the electronic retention standards, including the records security program in (g)(1): access limited to authorized personnel, backup and recovery, trained staff, and a permanent audit record. The electronic signature rules in (h) and (i) do not apply, because the forms are signed on paper. The firm is not a "recruiter or referrer for a fee" for its direct-hire work, because 274a.2(a)(1) limits that term to agricultural associations, agricultural employers, and farm labor contractors.
- **E-Verify MOU.** The firm enrolled on 2024-03-04 because two clients require it. The MOU (revision date 06/01/13) covers user access (Art. II.A.3), the tutorial (II.A.5), photocopies of certain documents (II.A.6), case timing and use limits (II.A.7 and II.A.9 to II.A.11), safeguarding of E-Verify information and passwords (II.A.15), and **immediate breach notice to DHS** (II.A.16).
- **Fla. Stat. 448.095.** Every employer must verify new employees within 3 business days as 8 CFR 274a requires (448.095(2)(a)), document any E-Verify outage ((2)(c)), and keep the documentation at least 3 years ((2)(d)). The E-Verify mandate in (2)(b)2. reaches private employers with 25 or more employees, and the statute defines "employee" as an individual filling a permanent position ((1)(b)). The firm has 7 permanent staff; whether its temporary associates count is not settled. The answer does not change practice, because the MOU already requires E-Verify for all new hires. A voluntary user may also certify its use on the first reemployment tax return each year ((2)(b)3.).
- **FCRA, 15 U.S.C. 1681b(b) and 1681m(a) (N56-R02).** The firm orders about 90 employment background checks a year.
- **FACTA Disposal Rule, 16 CFR 682.3 (N56-R01).** The firm keeps consumer report PDFs.
- **Fla. Stat. 501.171 (2026).** The firm is a "covered entity" (a commercial entity that maintains personal information, 501.171(1)(b)). A name with an SSN, or with a driver license or passport number, is personal information. A financial account number counts only in combination with a code or password that permits access to the account (501.171(1)(g)1.a.(III)), so bank account numbers alone may not trigger notice; the SSNs stored with them do.

**Also checked, outside this workbook:** Title VII, the ADEA, and the ADA apply to the AI match feature and are assessed in P10.

**FAR overhaul numbering.** The requirements analyzed here as FAR 52.204-21 appear as FAR 52.240-93 in awards made under an agency's FAR Part 40 class deviation. The 15 requirements are the same, so these results apply to both. See `00_company-facts.md`.

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategory IDs and outcome text come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows cite the eCFR text current as of 2026-09-23, the U.S. Code, the 2026 Florida Statutes, and the MOU, with short quotes or paraphrases.
2. **Target Profile.** Each subcategory has a priority for the firm's CSF Target Profile (High 26, Medium 54, Low 26), set by the Operations Manager and the Owner from the risk register (P01) and BIA (P05). Subcategories that protect payroll, SSNs, and Form I-9 records are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (CSF 2.0 to SP 800-53 Rev. 5.2.0, SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping, because no official NIST mapping exists for these rules.
4. **Documentary evidence.** Each status rests on a named document or record: user and role lists from the ATS, payroll service, suite, and E-Verify; the shared-drive sharing report and Onboarding folder listing; a mailbox search for SSNs and ID images; MFA settings; the MSP's agent list, patch report, encryption report, and backup job report; vendor contracts; the cyber insurance policy; shredding certificates; a sample of 20 paper Forms I-9 with E-Verify case details; a sample of 20 background check orders and all 4 adverse decisions in 2026; and the walkthrough on 2026-07-22. Interviews covered all 7 staff and the MSP lead technician.
5. **Status.** Met, Partially met, Not met, or Not applicable, **as of the end of fieldwork (2026-07-31)**, except G-123, updated with a P07 finding. Actions completed since then are noted in the remediation column but do not change the status. Gap risk uses the P01 scale.

**Current CSF Tier: Tier 1 (Partial).** Security has been informal and reactive. **Target: Tier 2 (Risk Informed) by 2027-07**, meaning practices approved by the Owner and driven by the risk register. Tier 2 is the right target for a 7-person firm; Tier 3 would need repeatable processes the firm cannot staff.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| CSF 2.0 Govern (31) | 2 | 12 | 17 | 0 |
| CSF 2.0 Identify (21) | 0 | 9 | 12 | 0 |
| CSF 2.0 Protect (22) | 4 | 14 | 2 | 2 |
| CSF 2.0 Detect (11) | 1 | 1 | 9 | 0 |
| CSF 2.0 Respond (13) | 0 | 2 | 11 | 0 |
| CSF 2.0 Recover (8) | 0 | 1 | 7 | 0 |
| **CSF 2.0 subtotal (106)** | **7** | **39** | **58** | **2** |
| Form I-9, 8 CFR 274a.2 (16) | 1 | 6 | 7 | 2 |
| E-Verify MOU (6) | 2 | 1 | 3 | 0 |
| Fla. Stat. 448.095 (4) | 1 | 2 | 1 | 0 |
| FCRA, 15 U.S.C. 1681b(b) and 1681m(a) (4) | 3 | 1 | 0 | 0 |
| Disposal Rule, 16 CFR 682.3 (1) | 0 | 1 | 0 | 0 |
| Fla. Stat. 501.171 (6) | 0 | 3 | 3 | 0 |
| Vertical requirements found not applicable (6) | 0 | 0 | 0 | 6 |
| **Total (149)** | **14** | **53** | **72** | **10** |

Of the 125 unmet or partially met rows, 8 are rated High, 49 Moderate, 66 Low, and 2 Very Low.

**The pattern.** The firm does the hire-by-hire compliance steps well: Section 2 on time in 19 of 20 files, E-Verify for everyone, a standalone FCRA disclosure, written authorization on every order, and a 5-day wait between adverse action letters. But it **does not protect the records those steps create**. SSNs, identity document images, and consumer reports have spread into a shared folder everyone can open, mailboxes, and phones; nobody watches the payroll service; and nothing exists for Respond and Recover. That is typical of a Micro firm: the vendors and the MSP supply most of the Protect outcomes that are Met, and the Govern, Detect, Respond, and Recover outcomes that depend on the firm itself are mostly Not met.

The two CSF rows rated not applicable are PR.AA-04 (identity assertions: the firm uses no single sign-on or federation) and PR.PS-06 (secure software development: the firm writes no software). The two Form I-9 rows rated not applicable cover the remote alternative procedure (not used) and electronic signatures (forms signed on paper).

## 4. Priority gaps
| Gap | Row(s) | Risk | Action | Owner | Target |
|---|---|---|---|---|---|
| Payroll sign-in can be phished (SMS codes); no MFA on MSP-held logins | G-055 | High | Authenticator-app MFA for payroll administrators; MFA on backup and firewall logins | Operations Manager | 2026-10-31 |
| Nobody watches payroll bank changes or exports | G-077 | High | Vendor alerts to the Operations Manager and Owner; monthly review | Operations Manager | 2026-10-31 |
| Onboarding folder and onboarding packets open to all staff | G-057, G-112, G-118 | High | Restrict to the Operations Manager and the Coordinator; recruiters see check status only | Operations Manager | 2026-09-30 |
| No inventory of where SSNs, Form I-9 images, and consumer reports are kept | G-037 | High | Data inventory; delete stray copies in mail and phones | Operations Manager | 2026-10-31 |
| No incident plan; Florida 30-day and DHS notice duties unknown | G-052, G-095, G-128, G-140 | High | P08 runbook and notification matrix; tabletop | Operations Manager | 2026-11-30 |
| Critical vendors never assessed (payroll, ATS, MSP) | G-028 | High | SOC 2 reviews (P09); annual MSP review | Operations Manager | 2026-12-31 |
| Form I-9 scans fall under the electronic standards and meet almost none of them | G-111, G-113, G-121 | Moderate | Keep paper as the only record; check each paper file, then delete the scans and stop scanning | Operations Manager | 2026-12-31 |
| E-Verify access and passwords not safeguarded | G-123, G-127 | Moderate | E-Verify on the termination checklist; password manager | Operations Manager | 2026-09-30 |
| Adverse action before the pre-adverse notice (2 of 4 cases in 2026) | G-136 | Moderate | Recruiters see "in review" only; Coordinator runs every adverse decision | Operations Manager | 2026-09-30 |
| Consumer reports and old records never disposed of | G-038, G-137 | Moderate | Retention schedule; delete report PDFs; certified wiping | Operations Manager | 2026-12-31 |

**Why delete the Form I-9 scans rather than fix them.** Bringing a shared-drive folder up to 274a.2(e) to (g) would take an access-controlled system, a permanent audit trail, a written system description, and periodic quality checks. The firm gains nothing from the scans: the paper originals and photocopies are complete and are the record of retention. Keeping paper only removes 214 sets of identity document images from the most exposed place the firm has. The Owner approved this on 2026-08-31, on the condition that each paper file is confirmed complete before its scan is deleted.

The full list, with evidence, is in `gap-analysis.csv`. Every High and Moderate gap is carried into the risk register (P01) and, where the control was assessed, the POA&M (P07).

## 5. Remediation plan
The plan fits a 7-person firm: most actions are settings in vendor services, one-page procedures, or MSP tasks. The MSP does the technical work under the Operations Manager's direction. Costs are in the P01 treatment summary.

| Phase | Due | Actions | Main rows closed |
|---|---|---|---|
| 1. Access and duties | 2026-09-30 | Policies adopted (POL-02, POL-03, POL-04, effective 2026-09-01); Onboarding folder restricted; termination checklist covering E-Verify; password manager; recruiters limited to check status; FCRA adverse action routed to the Coordinator; first restore test | G-016, G-017, G-018, G-057, G-112, G-118, G-123, G-127, G-136 |
| 2. Payroll and visibility | 2026-10-31 | Authenticator-app MFA for payroll and MSP-held logins; bank-change and export alerts; call-back rule; data and device inventory; stray SSN and ID copies deleted; vendor file with breach contacts; change log for payroll, ATS, and AI settings | G-028 (part), G-032, G-037, G-045, G-054, G-055, G-077, G-142 |
| 3. Response and recovery | 2026-11-30 | P08 runbook trained; tabletop with the MSP; manual payroll drill; contingency plan with E-Verify outage and hurricane steps | G-052, G-086 to G-106, G-131, G-140 |
| 4. Records | 2026-12-31 | Retention schedule; paper Form I-9 index; scans deleted after the paper check; consumer report PDFs deleted; certified wiping; MSP contract amendment; 1-year log retention | G-038, G-110, G-111, G-113 to G-117, G-121, G-137, G-143 |
| 5. Annual cycle | 2027-04-30 to 2027-07-31 | Voluntary E-Verify certification on the first 2027 reemployment return; risk assessment and this workbook updated each July | G-130; GV.OV rows |

**Progress check.** The Operations Manager reports progress to the Owner at a monthly 30-minute meeting, using the P07 POA&M as the tracker.

## 6. Pending changes (not current obligations)
- **CIRCIA** (proposed 6 CFR Part 226): no final rule as of 2026-09-25; nothing to do now.
- **Form I-9:** one related change is already in effect. A DHS rule (90 FR 48799, effective 2025-10-30) removed the automatic extension of many renewal Employment Authorization Documents, so reverification dates for some associates arrive sooner. The firm's onboarding calendar should track them. No proposed change to the retention or electronic storage standards in 274a.2 was identified.
- **Fla. Stat. 448.095 and 501.171:** the 2026 statutes were read; state bills were not tracked. If Florida extended the E-Verify mandate to every private employer, the firm's practice would not change.
- **FCRA:** no pending change to 1681b(b) was identified.
