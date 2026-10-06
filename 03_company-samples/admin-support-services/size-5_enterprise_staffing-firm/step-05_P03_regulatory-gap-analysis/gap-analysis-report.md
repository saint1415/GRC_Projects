# Regulatory Gap Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company, NAICS 561320; 38 states and DC) |
| Tier / Vertical | Enterprise / Administrative and Support and Waste Management and Remediation Services |
| Primary benchmark | NIST Cybersecurity Framework (CSF) 2.0, NIST CSWP 29 (2024-02-26), all 106 subcategories, **as a voluntary benchmark** (label `N56-BM`) |
| Binding rules analyzed | Form I-9 retention, inspection, and electronic I-9 standards (8 CFR 274a.2, N56-R03); the E-Verify MOU and the FAR E-Verify clause (48 CFR 52.222-54); state E-Verify law (Florida worked example, Fla. Stat. 448.095); FCRA employment screening (15 U.S.C. 1681b(b), 1681m(a), N56-R02); the FACTA Disposal Rule (16 CFR 682.3, N56-R01); SEC Form 8-K Item 1.05 and Reg S-K Item 106; FAR Basic Safeguarding (48 CFR 52.204-21, N56-R07); NYC Local Law 144 (N56-R08); Title VII and the ADA for AI selection procedures; Colorado SB26-189 (effective 2027-01-01); California CPPA regulations (ADMT, risk assessments, cybersecurity audits) and Civil Rights Council ADS regulations; Illinois Public Act 103-0804; state breach and data security laws (Florida worked example, Fla. Stat. 501.171) |
| Checked and found not applicable | N56-R04 (HIPAA business associate), N56-R05 (TCPA and TSR, outside this security analysis), N56-R06 (PCI DSS), N56-R09 (PHMSA security plans) |
| Text verified | eCFR as of 2026-09-23 (8 CFR 274a.2; 16 CFR 682.3; 45 CFR 160.103; 48 CFR 52.204-21 and 52.222-54; 17 CFR 229.106); U.S. Code (15 U.S.C. 1681b, 1681m; 42 U.S.C. 2000e-2, 12112); 2026 Florida Statutes (501.171, 448.095); E-Verify MOU for Employers (revision 06/01/13); Colorado SB26-189 as signed; California CPPA regulation dates and Civil Rights Council ADS regulations and Illinois P.A. 103-0804 as summarized in `00_universal-framework/cross-sector/us-cross-sector-obligations.md` (Illinois content partially verified) |
| Assessment dates | 2026-06-01 to 2026-07-31 (evidence sampling completed 2026-08-14) |
| Assessors | GRC team (second line) with the Chief Compliance Officer and the Vice President, Employment Compliance; sampling reperformed by Internal Audit for 10 rows |
| Approved | Chief Compliance Officer and CISO, 2026-08-21; roadmap reviewed by the risk and technology committee of the board, 2026-09-10 |
| Workbook | `gap-analysis.csv` (188 rows) |

## 1. Applicability
**No sector cybersecurity rule binds a staffing firm, so CSF 2.0 is the benchmark.** The vertical profile names CSF 2.0 because NAICS 56 has no sector-specific federal cyber mandate. At this size the firm is still a temporary help firm, so that holds. What changes at Enterprise is the number of binding rules around it: SEC disclosure, federal contracts, multi-state privacy and AI laws, and employment eligibility at a scale of about 240,000 hires a year.

| Candidate | Applies? | Why (citation) |
|---|---|---|
| NIST CSF 2.0 | **Yes, voluntary** | Benchmark for the whole program; status measures the firm against its own Target Profile |
| Form I-9 (N56-R03) | **Yes** | Employer of record for associates; electronic I-9 system subject to 274a.2(e)-(i) |
| E-Verify MOU; FAR 52.222-54 | **Yes** | Signed the MOU for Employers; enrolled as a Federal contractor because Government Solutions holds 34 contracts with the FAR E-Verify clause (MOU Art. II.B) |
| State E-Verify laws (Florida: Fla. Stat. 448.095) | **Yes** | Private employer with 25 or more employees (448.095(2)(b)2.); other states' E-Verify laws are handled by the same enterprise process (verify every new hire) |
| FCRA (N56-R02) and Disposal Rule (N56-R01) | **Yes** | Procures about 190,000 consumer reports a year for employment purposes |
| SEC Item 1.05 and Item 106 | **Yes** | Publicly traded SEC registrant, not a smaller reporting company |
| FAR 52.204-21 (N56-R07) | **Yes, for Government Solutions** | 34 federal contracts; federal contract information (agency timesheets, invoices, contract reports) is in SYS-01 and SYS-03. No CUI is handled, so DFARS and NIST SP 800-171 do not apply |
| NYC Local Law 144 (N56-R08) | **Yes, for NYC jobs** | The firm is an employment agency using AI-001 to rank candidates for jobs at 9 NYC branches |
| Title VII and ADA | **Yes** | Employer and employment agency; AI selection procedures assessed in P10 |
| Colorado SB26-189 | **Yes, from 2027-01-01** | The firm does business in Colorado and uses AI-001 in employment decisions about Colorado applicants; the law applies to consequential decisions made on or after 2027-01-01, so these rows measure readiness. No employee-count exemption appears in the signed act |
| California CPPA regulations (CCPA) | **Yes** | The firm is a CCPA "business" (annual gross revenue above $26,625,000), and employee and applicant data are in scope. ADMT duties apply to AI-001 for California applicants from 2027-01-01; risk assessments for existing processing are due by 2027-12-31; the cybersecurity audit applies because the firm meets the revenue test and processes sensitive personal information of more than 50,000 California consumers (first audit period 2027) |
| California Civil Rights Council ADS regulations | **Yes** | FEHA employer using an automated-decision system for California applicants; effective 2025-10-01 |
| Illinois Public Act 103-0804 | **Yes** | Illinois employer using AI in hiring; effective 2026-01-01 (content confirmed only from ilga.gov search snippets; IDHR rules not checked) |
| State breach and data security laws | **Yes** | Associates and candidates live in every state; the law of each state where affected individuals reside applies. Florida (Fla. Stat. 501.171) is the worked example |
| HIPAA as business associate (N56-R04) | **No** | A business associate acts "other than in the capacity of a member of the workforce" of the covered entity (45 CFR 160.103). "Workforce" includes persons whose conduct in the performance of work is under the direct control of the covered entity, "whether or not they are paid by" it. Travel and per diem clinicians work under the hospital's direct control, so they are the hospital's workforce, and the firm itself does not handle PHI for hospitals. The 37 hospital BAAs are contractual commitments |
| TCPA and TSR (N56-R05) | **Partly; outside this analysis** | The TSR does not apply (no telemarketing). TCPA consent rules reach automated recruiting texts; that is a contact-consent duty owned by the Privacy Office, not a security duty |
| PCI DSS (N56-R06) | **No** | The firm accepts no payment cards; paycards are issued and run by a bank program manager |
| PHMSA security plans (N56-R09) | **No** | No hazardous materials |
| CIRCIA (proposed 6 CFR Part 226) | **Not in force** | Final rule not published as of 2026-09-25 |
| SOX Section 404 | Separate program | IT general controls over the payroll engine and ERP are tested by the SOX program and not repeated here |

## 2. Method
1. **Requirements.** The 106 CSF 2.0 subcategories come from NIST's CSF 2.0 core (`00_universal-framework/frameworks/csf2_core.csv`). Regulation rows were broken into citation-level duties from the primary texts listed above, with short quotes or paraphrases. Colorado rows cite C.R.S. 6-1-1703 to 6-1-1705 as enacted by SB26-189.
2. **Target Profile.** Each subcategory has a Target Profile priority (High 49, Medium 50, Low 7) set by the CISO and the Chief Risk Officer from the risk register (P01) and BIA (P05). Subcategories that protect pay, SSNs, and Form I-9 records are High.
3. **Crosswalk.** CSF 2.0 to SP 800-53 Rev. 5 uses the **official NIST informative reference** (SRC-OLIR-CSF-53), kept in full in `nist_official_sp800_53r5`. The `sp800_53_controls` column is a key-control subset chosen by the author. Regulation rows use an author mapping (no official NIST mapping exists for these rules).
4. **Evidence sampling.** Where a requirement operates on a population, the team tested a sample and recorded the population, sample size, and exceptions. Key controls with large populations used 60 items (95% confidence, 5% tolerable deviation, zero expected deviations); lower-risk controls and smaller populations used 25 to 40 items; configuration and account data were checked in full with analytics. Selections were random. **39 rows were tested by sampling or full-population analytics; 24 found exceptions.** Two of those (PR.AT-01, 3% of staff overdue on training, and DE.CM-09, EDR missing only on time clocks and legacy kiosks) were within tolerance and are rated Met.
5. **Rate.** Met, Partially met, Not met, or Not applicable. Each gap is rated with the P01 scale and carries an owner and date. High gaps are in the P01 register and the P07 POA&M.

**Current CSF Tier: Tier 3 (Repeatable)** for the enterprise program, with Tier 2 practices at ACQ-1. **Target: Tier 3 everywhere by 2027-06, and Tier 4 (Adaptive) for the payroll fraud controls,** because that is where the firm loses money every week.

## 3. Results summary
| Regulation / section | Met | Partially met | Not met | N/A | Rows |
|---|---|---|---|---|---|
| CSF 2.0 Govern | 26 | 5 | 0 | 0 | 31 |
| CSF 2.0 Identify | 14 | 7 | 0 | 0 | 21 |
| CSF 2.0 Protect | 10 | 12 | 0 | 0 | 22 |
| CSF 2.0 Detect | 9 | 2 | 0 | 0 | 11 |
| CSF 2.0 Respond | 11 | 2 | 0 | 0 | 13 |
| CSF 2.0 Recover | 7 | 1 | 0 | 0 | 8 |
| **CSF 2.0 subtotal** | **77** | **29** | **0** | **0** | **106** |
| Form I-9, 8 CFR 274a.2 (N56-R03) | 14 | 5 | 0 | 0 | 19 |
| E-Verify MOU and FAR 52.222-54 | 3 | 3 | 0 | 0 | 6 |
| State E-Verify law (Fla. Stat. 448.095) | 4 | 0 | 0 | 0 | 4 |
| FCRA (N56-R02) | 3 | 1 | 0 | 0 | 4 |
| Disposal Rule (N56-R01) | 0 | 1 | 0 | 0 | 1 |
| SEC Form 8-K Item 1.05 | 1 | 2 | 0 | 0 | 3 |
| SEC Regulation S-K Item 106 | 5 | 0 | 0 | 0 | 5 |
| FAR 52.204-21 (N56-R07) | 13 | 2 | 0 | 0 | 15 |
| NYC Local Law 144 (N56-R08) | 2 | 1 | 0 | 0 | 3 |
| Title VII and ADA (AI selection) | 1 | 1 | 0 | 0 | 2 |
| Colorado SB26-189 (readiness, effective 2027-01-01) | 0 | 0 | 4 | 0 | 4 |
| California CPPA regulations (ADMT readiness, risk assessments, audits) | 0 | 2 | 1 | 0 | 3 |
| California Civil Rights Council ADS regulations | 0 | 1 | 0 | 0 | 1 |
| Illinois Public Act 103-0804 | 0 | 1 | 0 | 0 | 1 |
| State breach and data security laws | 4 | 3 | 0 | 0 | 7 |
| Vertical requirements found not applicable | 0 | 0 | 0 | 4 | 4 |
| **Total** | **127** | **52** | **5** | **4** | **188** |

**Gap risk levels** for the 57 Partially met and Not met rows: High 10, Moderate 37, Low 10.

**The pattern.** The program is mature where it is centrally run (governance, monitoring, response, backups, SEC Item 106, federal contract basics). The gaps sit at three seams: **where money moves on a weak identity check** (associate sign-in, phone verification, pay rule approvals, pay files), **where sensitive data was copied out of the system that protects it** (the data platform, the scanned I-9 archive, records past retention), and **where the firm grew by acquisition** (ACQ-1's terminations, logs, forms, and contracts). The 5 Not met rows are readiness rows for duties that start on 2027-01-01 (4 Colorado rows and the California ADMT row). The AI employment rules already in force (NYC, Illinois, California's Civil Rights Council regulations, and Title VII) share one gap: AI-001 is monitored for bias only on vendor data and NYC data.

## 4. Priority gaps (High)
| Row | Citation | Gap | Action | Owner | Target |
|---|---|---|---|---|---|
| G-045 | CSF ID.RA-07 | 5 of 40 sampled pay rule changes lacked independent approval | System-enforced second approver (POAM-015) | Vice President, Payroll Technology | 2026-12-31 |
| G-052 | CSF ID.IM-04 | Materiality step untested with the current disclosure committee | Tabletop 2026-11-12 (POAM-013) | General Counsel | 2026-11-30 |
| G-054 | CSF PR.AA-02 | 2 of 10 mystery-shopper calls changed a bank account | Caller verification redesign (POAM-018) | Senior Vice President, Payroll and Associate Services | 2026-12-31 |
| G-055 | CSF PR.AA-03 | Associates sign in with SMS codes; 214 fraudulent bank changes in 2025 | Passkeys or app push; out-of-band confirmation (POAM-001) | Senior Vice President, Payroll and Associate Services | 2027-01-31 |
| G-061 | CSF PR.DS-01 | Untokenized SSNs and bank numbers in the data platform | Tokenize the extract (POAM-004) | Chief Data Officer | 2027-03-31 |
| G-077 | CSF DE.CM-03 | No detection for bulk exports or associate bank-change anomalies | POAM-016; POAM-001 | Director of Security Operations | 2026-12-31 |
| G-141 | Form 8-K Item 1.05 | Process untested with the current committee | POAM-013 | General Counsel | 2026-11-30 |
| G-142 | Form 8-K Item 1.05 (materiality determination) | No quantitative method for a PII breach | Cost model (POAM-013) | General Counsel | 2026-10-31 |
| G-167 | 42 U.S.C. 2000e-2(k); 42 U.S.C. 12112(b)(6) | No firm-data adverse impact monitoring for AI-001 outside NYC | Quarterly monitoring (POAM-014) | Chief Data Officer | 2027-01-31 |
| G-174 | Fla. Stat. 501.171(2) (worked example) | Clear-text sensitive copies weaken the reasonable-measures position | POAM-004 | Chief Data Officer | 2027-03-31 |

**Notable Moderate gaps in the binding rules:** the scanned I-9 archive has no audit trail (G-124, 8 CFR 274a.2(g)(1)(iv)); ACQ-1's Forms I-9 have no agreed path to stay accessible after migration (G-117, (e)(4)); 37 departed users still held E-Verify access (G-126, MOU Art. II.A.3); ACQ-1's FCRA disclosure is not standalone (G-137); electronic consumer reports past retention are not disposed of (G-140, 16 CFR 682.3); 3 of 40 NYC postings lacked the Local Law 144 notice (G-166); and no firm-data bias testing covers California or Illinois applicants (G-187, G-188).

## 5. Compliance roadmap
| Quarter | Milestones | Rules served | Evidence produced |
|---|---|---|---|
| 2026 Q4 | Disclosure playbook cost model and tabletop (POAM-013); ACQ-1 FCRA form replaced (POAM-021); E-Verify reconciliation and offboarding step (POAM-006); pay rule second approver (POAM-015); pay file hashing (POAM-019); caller verification redesign (POAM-018); bulk-export detection (POAM-016); Colorado and California ADMT notices, disclosures, opt-out or exception basis, and request channel designed (POAM-023); CPPA audit scope mapped (G-186); NYC template lock; vendor notice terms (POAM-009); time clock PINs (POAM-024) | SEC Item 1.05; FCRA 1681b(b)(2)(A)(i); MOU Art. II.A.3 and II.A.15; C.R.S. 6-1-1703 to 6-1-1705; 11 CCR 7200 et seq.; 11 CCR 7120-7124; NYC Local Law 144; Fla. Stat. 501.171(6) | Tabletop report; new form; reconciliation reports; workflow configuration; notice templates |
| 2027 Q1 | Associate passkeys and bank-change confirmation (POAM-001); data platform tokenization (POAM-004); I-9 archive moved with audit trail and index (POAM-007); ACQ-1 Forms I-9 migrated and ACQ-1 cut over (2027-03-31); client integration credentials (POAM-008); firm-data bias monitoring including California and Illinois applicants (POAM-014); FAR timesheet portal for the last 4 contracts (POAM-022) | 8 CFR 274a.2(b)(2)(ii), (e)(4), (g)(1)(iv); Fla. Stat. 501.171(2); Title VII 703(k); 2 CCR 11008 et seq.; P.A. 103-0804; FAR 52.204-21(b)(1)(iii) | Tokenization design and test; archive audit logs; bias monitoring report |
| 2027 Q2 | Retention purges live (POAM-005); kiosk segmentation complete (POAM-012); Internal Audit test of Item 106 statements | 16 CFR 682.3; Fla. Stat. 501.171(8); 8 CFR 274a.2(b)(2)(i)(A) | Purge logs; certificates of destruction |
| 2027 Q3 to Q4 | Annual gap reassessment; review state AI and privacy law changes; CPPA risk assessments completed by 2027-12-31 (G-185) | All; 11 CCR 7150-7157 | Updated P01 and P03; CPPA risk assessment records |

## 6. Pending regulatory changes
- **Colorado SB26-189** is enacted, not proposed. It takes effect 2027-01-01 and applies to consequential decisions made on or after that date; the attorney general must adopt rules on post-adverse-outcome disclosures by 2027-01-01. The firm treats it as a readiness item now and a current obligation from 2027-01-01.
- **California CPPA regulations** took effect 2026-01-01 with dated phase-ins: ADMT compliance by 2027-01-01 for existing uses, risk assessments for existing processing by 2027-12-31 (submission by 2028-04-01), and, for a business with 2026 revenue over $100 million, a first cybersecurity audit covering 2027 with the report due 2028-04-01. These are dated obligations, tracked as readiness rows now.
- **Connecticut Public Act 26-15** (effective 2026-10-01, per the Connecticut Attorney General) requires employers to give written notice when AI is used in decisions affecting terms or conditions of employment. Only the Attorney General's release was read; counsel is confirming the text before the firm relies on it, and Connecticut postings already carry the AI notice used for Illinois.
- **Illinois:** IDHR rules implementing Public Act 103-0804 are pending and were not checked.
- **CIRCIA:** the final rule had not been published as of 2026-09-25. Reporting to CISA is voluntary until it takes effect.
- **FAR:** the FAR CUI proposed rule (2025-01-15) and the FAR cyber incident reporting proposed rule (2023-10-03) remain proposed, and the FAR overhaul proposed rule (2026-06-23) is not final. None is treated as current.
- **Form I-9 and E-Verify:** a Federal Register search for "274a.2" (2025-01-01 to 2026-09-25) found no proposed change to the retention or electronic I-9 standards assessed here.
- **SEC:** a 2025 petition asks the SEC to rescind Item 1.05. No SEC proposal to amend or rescind was found as of 2026-09-25, so Item 1.05 and Item 106 remain in force.
- **Federal disparate impact posture:** see P10 section 3. The statute (42 U.S.C. 2000e-2(k)) is unchanged and private claims remain available.

## 7. Regulator-ready package
The GRC team keeps an evidence binder in the GRC platform, indexed by `req_id`, so the firm can respond quickly to an ICE Form I-9 inspection notice (3 business days, 8 CFR 274a.2(b)(2)(ii)), a DHS E-Verify compliance inquiry, an FTC or CFPB FCRA inquiry, a federal contracting officer's request, a NYC DCWP inquiry, a state attorney general breach inquiry, or an SEC comment letter:
- this report, `gap-analysis.csv`, and the sample selections with exceptions for every sampled row;
- the electronic I-9 system description (8 CFR 274a.2(e)(5)) and procedures PRC-09.1 to PRC-09.4;
- the P01 risk analysis, P02 SSP, P05 BIA, P06 policy set, P07 assessment and POA&M, and P08 runbook;
- the NYC bias audit report and public summary, and the P10 AI governance file;
- breach notification files and the state law matrix.

## 8. Approval
Approved by the Chief Compliance Officer and the CISO on 2026-08-21. The roadmap was reviewed by the risk and technology committee of the board on 2026-09-10. Next reassessment: 2027-06 to 2027-07.
