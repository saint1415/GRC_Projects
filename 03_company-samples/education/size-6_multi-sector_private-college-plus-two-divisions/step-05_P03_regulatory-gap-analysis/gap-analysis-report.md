# Regulatory Gap Analysis: Cris Santos Company Holdings | Educational Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (three divisions plus corporate shared services) |
| Tier / Vertical | Multi-Sector / Educational Services (focus division: Higher Education, Cris Santos College) |
| Primary regulation | FTC Standards for Safeguarding Customer Information (Safeguards Rule), 16 CFR Part 314, as applied to Title IV institutions through the Program Participation Agreement and enforced by Federal Student Aid. Text checked on eCFR as of 2026-09-23 (last amended 88 FR 77508, Nov. 13, 2023) |
| Division regulations | Education Software: COPPA Rule (16 CFR Part 312, as amended 2025) plus FERPA and GLBA duties flowed down by customer contracts, SOC 2 commitments, and FTC Act Section 5. Student Health: HIPAA Security, Privacy, and Breach Notification Rules for nonstudent patients, and FERPA for student records kept for institutions |
| Gap tables | `gap-analysis.csv` (Higher Education, 61 rows); `gap-analysis-education-software.csv` (24 rows); `gap-analysis-student-health.csv` (32 rows) |
| Assessment dates | 2026-06-01 to 2026-07-31, with evidence updated from the P07 assessment (to 2026-08-28) |
| Assessors | Division security and compliance leads with the university registrar, the Student Health Privacy Officer, and Education Software privacy counsel, coordinated by the Group Chief Privacy Officer; reviewed by group internal audit |

## 1. Applicability
### 1.1 Who is what
| Entity | Role under the main rules | Basis |
|---|---|---|
| Cris Santos College (Higher Education) | Title IV institution bound to the FTC Safeguards Rule through its PPA; educational institution under FERPA | FSA Electronic Announcement GENERAL-23-09; 34 CFR 99.1 |
| Education Software | **Operator** under COPPA for the District Platform; **school official** (contractor) for about 6,300 customer institutions under FERPA; **service provider** to about 900 Title IV colleges, which must flow down Safeguards Rule terms (314.4(f)(2)); SOC 2 service organization | 16 CFR 312.2; 34 CFR 99.31(a)(1)(i)(B); 16 CFR 314.4(f) |
| Student Health | **HIPAA covered entity** (bills health plans electronically); for students, a party acting for the college or a contracting college, so their records are those institutions' FERPA records | 45 CFR 160.103; 34 CFR 99.3; HHS and ED Joint Guidance (December 2019) |
| Corporate shared services | Business associate of Student Health (intercompany BAA, 2024); provider of common controls to all divisions | Intercompany agreements |

**The college's Safeguards Rule obligations apply in full.** The college holds customer information on about 1.4 million consumers, far above the 5,000-consumer threshold in 16 CFR 314.6, so the written risk assessment, penetration testing and vulnerability assessments, written incident response plan, and annual board report all apply. 314.4(a)(1)-(3) do not apply because the Qualified Individual is a college employee.

### 1.2 FERPA or HIPAA: the clinic records decision
The scenario's hardest applicability question is which law governs Student Health's records. The decision, confirmed by group legal on 2026-08-14:
- **Students seen at the 22 campus clinics:** Student Health runs these clinics on behalf of Cris Santos College. Their records are the college's **education records** or **treatment records** under FERPA (34 CFR 99.3), and the HIPAA definition of PHI excludes both (45 CFR 160.103, paragraphs (2)(i) and (ii)). The HHS and ED Joint Guidance (December 2019 update, questions 3 and 4) says the same for clinics run on behalf of a university.
- **Students seen at the 58 contract clinics:** the same reasoning applies, but the records belong to the 37 contracting institutions, not to Cris Santos College.
- **Nonstudent patients** (employees, family members, community patients) and **all patients at the 16 community urgent care sites:** PHI under HIPAA.
- **Billing records on students** are education records, not treatment records, because they are not used only for treatment (Joint Guidance question 6).
- **Treatment records lose their status when disclosed beyond treatment.** When campus clinic visit data went to the college warehouse in 2025, those records became education records subject to FERPA consent and legitimate educational interest rules (gap G-048).

Consequences used throughout this sample: Student Health is one covered entity (no hybrid designation is needed, because every component performs covered functions); the college and Education Software are not covered entities; a Student Health breach may need HIPAA notices for nonstudents and contract-driven notices to institutions for students (P08).

### 1.3 Excluded requirements, with reasons
- **COPPA for the college:** no students under 13.
- **CIPA (N61-R04):** no division receives E-Rate funds. The District Platform supports customers' filtering, which is their duty.
- **HIPAA hybrid entity designation (N61-R05):** not needed. The college performs no covered functions; Student Health is a separate legal entity whose components all perform covered functions.
- **42 CFR Part 2, FTC Health Breach Notification Rule, FedRAMP, DFARS 252.204-7012:** no Part 2 program, Student Health is a covered entity, no federal agency customers, no CUI.
- **State comprehensive consumer privacy laws** for Education Software were not assessed in this sample; privacy counsel tracks them.

## 2. Regulation-by-division matrix
| Requirement | Higher Education | Education Software | Student Health | Group (corporate) |
|---|---|---|---|---|
| N61-R02 FTC Safeguards Rule (16 CFR 314) | **Primary.** Applies in full through the PPA | Applies by contract as a service provider to Title IV customers (314.4(f)(2)) | Not applicable (not a financial institution) | Provides common controls the college inherits |
| N61-R01 FERPA (34 CFR 99) | **Applies.** Education records in the SIS, LMS, warehouse, and campus clinic records | Applies by contract as a school official for customers (99.31(a)(1)(i)(B); 99.33(a)) | Applies to student records kept for the college and contracting colleges | Warehouse platform operator |
| Title IV program rules (SAIG agreement; 668.16(c); HEA sec. 483) | Applies | Not applicable | Not applicable | Not applicable |
| N61-R03 COPPA (16 CFR 312) | Not applicable (no children under 13) | **Primary.** Operator of the District Platform; 312.8 security program and 312.10 retention | Not applicable | Not applicable |
| N61-R05 / N62-R01 HIPAA Security Rule | Not applicable (no covered functions) | Not applicable | **Primary.** Covered entity for nonstudent PHI | Business associate of Student Health |
| N62-R02 HIPAA Privacy Rule; N62-R03 Breach Notification | Not applicable | Not applicable | Applies (nonstudent PHI) | Applies through the intercompany BAA (164.410 notice to Student Health) |
| N62-R07 Section 1557, 45 CFR 92.210 | Not applicable | Not applicable | Applies (urgent care sites accept Medicaid) | Group AI standard (P10) |
| N51-R01 FTC Act Section 5 | Applies (general) | **Applies** (security, privacy, and AI claims) | Limited | Applies |
| N51-R04 DOJ Data Security Program (28 CFR 202) | Vendor screening | Applies (screened, compliant) | Vendor screening | Group vendor screening |
| Colorado SB26-189 (ADMT), effective 2027-01-01 | Deployer duties for admissions scoring for Colorado online applicants (P10) | Developer duties for analytics features sold to Colorado customers | Carve-out for HIPAA covered entities (except employment decisions) | Group AI standard |
| N61-R04 CIPA; N51-R07 FedRAMP | Not applicable | Not applicable (customer duty; no federal customers) | Not applicable | Not applicable |
| N61-R06 CIRCIA (proposed) | Tracked: proposed rule covers every Title IV institution | Tracked | Tracked | Tracked; not in effect |
| N51-R08 SEC Reg S-K Item 106; Form 8-K Item 1.05 | Via group | Via group | Via group | **Applies** (SEC registrant) |
| State breach notification laws | Each state where affected students reside (Florida worked example: Fla. Stat. 501.171) | Same, plus third-party agent duties to customers where state law sets them, and district contract terms | Same (Florida personal information includes medical information) | Coordinates |
| SOC 2 (contractual) | Out of scope (P09); reviews vendors' reports | Annual Type 2 (P09) | Out of scope (P09) | Group services carved in |

## 3. Method
1. **Requirements.** Higher Education rows are each paragraph of 16 CFR 314.3 and 314.4 at the most granular level the regulation uses, reused from the verified Small education sample and re-checked for this size, plus FERPA and Title IV rows. Education Software rows follow 16 CFR 312.8 and 312.10 (eCFR, current through 2026-09-23) and the contract and SOC 2 commitments. Student Health rows select the HIPAA specifications where its evidence differs from the group's common controls, plus Privacy, Breach Notification, and FERPA rows. Summaries paraphrase public-domain regulatory text; contract rows describe the company's own commitments.
2. **Crosswalk.** Every row carries an **author mapping** to CSF 2.0 and SP 800-53 Rev. 5. No official NIST mapping exists for 16 CFR 314 or 312. HIPAA rows are consistent with the Health Care crosswalk in `02_industry-rules/health-care/`, itself an author mapping.
3. **Evidence.** Interviews with each division's security, privacy, academic, clinical, and legal leads; document review; configuration exports; and P07 test results.
4. **Status.** Met, Partially met, Not met, or Not applicable.

## 4. Results
### 4.1 Higher Education: Safeguards Rule, FERPA, and Title IV (`gap-analysis.csv`)
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| 314.3(a) Written program | 1 | 0 | 0 | 0 |
| 314.4(a) Qualified Individual | 1 | 0 | 0 | 3 |
| 314.4(b) Risk assessment | 5 | 0 | 0 | 0 |
| 314.4(c) Safeguards | 3 | 8 | 0 | 0 |
| 314.4(d) Testing and monitoring | 2 | 2 | 0 | 0 |
| 314.4(e) Personnel | 4 | 0 | 0 | 0 |
| 314.4(f) Service providers | 0 | 3 | 0 | 0 |
| 314.4(g) Evaluate and adjust | 1 | 0 | 0 | 0 |
| 314.4(h) Incident response plan | 7 | 1 | 0 | 0 |
| 314.4(i) Report to the board | 2 | 1 | 0 | 0 |
| 314.4(j) FTC notification | 0 | 2 | 0 | 0 |
| 314.6 Exception | 0 | 0 | 0 | 1 |
| **Safeguards Rule subtotal (47)** | **26** | **17** | **0** | **4** |
| FERPA, 34 CFR Part 99 (10) | 4 | 6 | 0 | 0 |
| Title IV requirements (4) | 2 | 2 | 0 | 0 |
| **Total (61)** | **32** | **25** | **0** | **4** |

Of the 25 partially met rows, 7 are rated **High**, 16 **Moderate**, and 2 **Low**. Nothing is wholly unmet: the college has a defined program (Qualified Individual, written risk assessment, incident response plan, annual board report, MFA, encryption), and its gaps are about **scope**. The program stops at the edge of the college, but the college's data does not: it sits on a sister division's platform (314.4(f); FERPA 99.31(a)(1)(i)(B)), is reachable by that division's support staff (314.4(c)(1)), and received another division's clinic data (FERPA 99.3, 99.31(a)(1)(ii)).

### 4.2 Education Software (`gap-analysis-education-software.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| COPPA (312.8, 312.10, 312.5) | 4 | 6 | 1 | 0 |
| FERPA and Safeguards Rule duties flowed down by customers | 1 | 2 | 0 | 0 |
| Customer contracts and SOC 2 commitments | 0 | 1 | 2 | 0 |
| FTC Act, DOJ Data Security Program, Colorado SB26-189, FedRAMP, CIPA, SEC | 2 | 2 | 1 | 2 |
| **Total (24)** | **7** | **11** | **4** | **2** |

**Not met:** 312.10 (data of 212 former districts kept past contract end); the SOC 2 system description omits the AI tutor and its model provider; no subprocessor notice to pilot districts; and the Colorado developer documentation (not yet in force, due before 2027-01-01). **High partials:** standing support access (312.8(a) and (b)(3); FERPA direct control), school authorization for the AI tutor in 31 districts (312.5(a)(1)), and a trust-page statement that staff access data only with permission, which the access model contradicts (FTC Act Section 5).

**COPPA and schools.** The 2025 amendments did not codify a school authorization exception. The FTC said it would not finalize its ed tech proposals while the Department of Education considers FERPA changes, and will keep enforcing COPPA in ed tech consistent with its existing guidance (90 FR 16918). Education Software therefore relies on district authorization limited to the school's educational purpose, and treats the AI tutor as a material change that needs fresh authorization (312.5(a)(1)).

### 4.3 Student Health (`gap-analysis-student-health.csv`)
| Obligation group | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| HIPAA Security Rule (19 selected rows) | 9 | 8 | 2 | 0 |
| HIPAA Privacy Rule | 0 | 1 | 1 | 0 |
| HIPAA Breach Notification Rule | 3 | 1 | 0 | 0 |
| FERPA (records kept for institutions) | 0 | 2 | 1 | 0 |
| Section 1557, state recording laws, Part 2, FTC HBNR | 0 | 1 | 1 | 2 |
| **Total (32)** | **12** | **13** | **5** | **2** |

The selected Security Rule rows focus on specifications where Student Health's evidence differs from the group's. All other specifications rely on group common controls, which is why documenting inheritance (scenario gap 4) matters.

**Not met:** 164.502(a) (the utilization extract disclosed nonstudent PHI to the college warehouse without a permission); 34 CFR 99.33(a) (contract-college student records went to the same warehouse); 164.308(a)(7)(ii)(D) (file server restores never tested); 164.316(b)(2)(iii) (standards not updated since 2023); and 45 CFR 92.210 (no decision support tool inventory).

**The extract was assessed as a possible breach.** P03 fieldwork identified the utilization extract on 2026-07-22. Student Health opened a four-factor risk assessment under 164.402 on 2026-07-24 for about 41,000 nonstudent patients whose visit data reached the college warehouse, revoked warehouse access to the tables on 2026-08-07, and completed the assessment on 2026-09-11, inside the 60-day outer limit counted from 2026-07-22. The extract held record numbers, birth years, ZIP codes, visit dates, clinics, and diagnosis categories, but no names; 6 college analysts ran aggregate queries only; and each signed an attestation that no copies exist. The Privacy Officer and counsel concluded a **low probability of compromise**, so no breach notice is required, and the file is kept for 6 years (SH-G22). The disclosure itself was still impermissible (SH-G20, Not met). The 3 affected contracting colleges are being told so they can record the disclosure under 99.32 and make their own decisions.

**MFA is a policy gap, not a HIPAA gap today.** 164.312(d) requires verifying identity, which passwords can do. The group policy requires MFA, and the HIPAA Security Rule NPRM would require it, so the legacy domain is tracked as POAM-017 but rated Met for the current rule.

## 5. Group roadmap
| # | Gap (scenario gap) | Divisions | Citation | Risk | Action | Owner | Target |
|---|---|---|---|---|---|---|---|
| 1 | Standing cross-tenant support access (1) | ES, HE | 314.4(c)(1); 99.31(a)(1)(i)(B); 312.8(b)(3); FTC Act Section 5 | High | Ticket-bound, customer-approved, time-limited access; correct the trust page now | Education Software CISO | 2026-12-31 |
| 2 | Clinic extract into the warehouse (2) | SH, HE | 164.502(a); 99.3; 99.33(a); 99.31(a)(1)(ii) | High | Purge (the 164.402 assessment is complete); notify 3 colleges; warehouse role redesign and purpose tags | Group Chief Privacy Officer | 2026-10-31 (purge); 2027-03-31 (roles) |
| 3 | Intercompany service provider terms (3) | HE, ES | 314.4(f)(1)-(3); 99.31(a)(1)(i)(B) | High | Revised intercompany agreement with safeguards, 24-hour notice, right to assess; annual assessment | Group General Counsel | 2026-12-31 |
| 4 | AI tutor commitments and COPPA (6) | ES | 312.5(a)(1); 312.8(b)(2), (b)(4); SOC 2 description; subprocessor clause | High | Children's privacy review; district authorization; description update; red-team testing | Education Software chief product officer | 2026-12-31 |
| 5 | Admissions scoring (5) | HE | Title VI; Section 504; Colo. SB26-189 | High | Bias testing, applicant notice, human review rule (P10) | Vice president of admissions | 2026-12-31 |
| 6 | COPPA retention (6) | ES | 312.10 | Moderate | Delete and certify; automate deletion | Education Software privacy counsel | 2026-12-31 |
| 7 | Multi-regulator notification not exercised (7) | All | 314.4(h)(4), (j); SAIG agreement; 164.404; Form 8-K Item 1.05 | Moderate | Complete the matrix with contract terms; cross-division tabletop | Group General Counsel | 2026-12-15 |
| 8 | Student Health integration (4) | SH | 164.308(a)(8); 164.316(b)(2)(iii); 164.308(a)(7)(ii)(D) | Moderate | Inheritance matrix; re-issued supplement; restore tests; identity migration | Student Health security and compliance lead | 2027-03-31 |
| 9 | Legacy campuses (8) | HE | 314.4(c)(3), (c)(5), (d)(2)(i) | Moderate | Penetration test scope; MFA or retirement; encryption | College chief information officer | 2027-06-30 |

High and Moderate gaps are carried into the registers (P01) and the POA&M (P07; POAM-020 to POAM-024 trace directly to this analysis). The Qualified Individual's report to the college board of trustees on 2026-10-20 will present section 4.1 as the compliance status required by 314.4(i)(1).

## 6. Pending regulatory changes
- **16 CFR Part 314:** no pending FTC amendment was identified. The 314.4(j) FTC notice took effect May 13, 2024 (314.5).
- **CIRCIA (N61-R06)** is **still proposed** (89 FR 23644; final rule not published as of 2026-09-25). The proposed rule would cover every Title IV institution regardless of size and require CISA reports within 72 hours of a covered cyber incident and 24 hours after a ransom payment. Flagged in the `pending_rule_change` column; not treated as a current obligation.
- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is **still proposed**; the regulatory agenda projects a final rule in July 2027. If finalized as proposed it would affect Student Health's addressable gaps (encryption at rest, restore within 72 hours, MFA, a compliance audit at least every 12 months). Flagged in the Student Health table.
- **COPPA and ed tech:** the FTC may revisit school authorization after the Department of Education updates FERPA rules (90 FR 16918). Flagged on ES-G11.
- **Colorado SB26-189** takes effect 2027-01-01, with AG rules due by then; its status is unsettled by litigation and federal preemption efforts (see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`).
- **FSA and NIST SP 800-171:** FSA has encouraged institutions to adopt NIST SP 800-171 but the current requirement is the Safeguards Rule. Tracked as guidance.
