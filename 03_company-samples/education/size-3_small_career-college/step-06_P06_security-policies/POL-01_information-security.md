# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Policy ID | POL-01 |
| Owner | IT Director (Qualified Individual) |
| Approved by | Campus President |
| Approved / effective | Approved 2026-08-21; effective 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after material changes, security events, or a new risk assessment |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, RA-3, CA-2, CA-7, CA-8, RA-5, SA-9, SR-6, CM-3, CM-4, AT-3, PS-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-02, PR.PS-01, PR.AT-02 |
| Regulatory basis | FTC Safeguards Rule 16 CFR 314.3(a) and 314.4(a), (b), (d)-(g), (i) (N61-R02); FERPA 34 CFR 99.31(a)(1) (N61-R01) |

## 1. Purpose
Set up the college's information security program, assign who is accountable, and give every other security policy its authority. This policy set (POL-01 to POL-05), together with the System Security Plan (P02), is the college's **written information security program** required by 16 CFR 314.3(a). It replaces the 2023 WISP. The program protects customer information (16 CFR 314.2(d)), such as financial aid records, and students' education records under FERPA.

## 2. Scope
All Cris Santos Company workforce members: employees, full-time and adjunct faculty, contractors, and student workers. It also binds service providers that access college systems under contract, such as the financial aid servicer. It covers all college systems and data, including systems that vendors operate for the college, and information in any format (electronic and paper).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of Managers (chair: majority owner) | Receives the Qualified Individual's written report at least annually; the chair accepts High and Very High risks and approves the security budget |
| Campus President | Program executive; approves policies; accepts Moderate risks; confirms each year that security staff kept their knowledge current (314.4(e)(4)) |
| IT Director (Qualified Individual) | Oversees, implements, and enforces the program (16 CFR 314.4(a)); maintains the risk register, SSP, and POA&M; approves any encryption or MFA alternative in writing |
| Registrar (FERPA compliance officer) | Owns education records policy; data owner for the SIS |
| Director of Financial Aid | Data owner for the FAMS and SAIG access; manages the financial aid servicer relationship |
| Data owners (Registrar, Director of Financial Aid, Dean of Academic Affairs, Director of Admissions) | Approve access to their systems and perform access reviews (POL-02) |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The college must maintain a written information security program made up of this policy set, the System Security Plan, the risk register, and the POA&M. Its safeguards must fit the college's size, complexity, and the sensitivity of the customer information it holds. (PM-1; GV.PO-01; 314.3(a))

4.2 The IT Director is the Qualified Individual. The designation must be in writing, signed by the Campus President, and renewed whenever the role changes hands. (PM-2; GV.RR-02; 314.4(a))

4.3 A written risk assessment must be performed at least annually (each July) and after any material change, such as a new program modality, a new system that stores customer information, or a new AI use. It must use NIST SP 800-30 Rev. 1 and include the criteria required by 314.4(b)(1). Risks must be tracked in the risk register with an owner and treatment. (RA-3; PM-9; ID.RA-01; 314.4(b)(1)-(2))

4.4 Risk acceptance authority: the IT Director may accept Low and Very Low risks; the Campus President, Moderate; the Board chair, High and Very High, and only temporarily with a dated treatment plan. A risk that could put Title IV eligibility or administrative capability at stake may not be accepted at High. (PM-9; GV.RM-01)

4.5 The Qualified Individual must report in writing to the Board of Managers at least annually, each October. The report must cover the overall status of the program and compliance with 16 CFR Part 314, and material matters: the risk assessment, risk and control decisions, service provider arrangements, test results, security events and management's responses, and recommended changes. (PM-9; GV.OV-01; 314.4(i)(1)-(2))

4.6 Security policies must be reviewed at least annually and updated after material changes, security events, or a new risk assessment. (PL-1; GV.PO-02; 314.4(g))

4.7 Exceptions to any security policy must be requested in writing, risk-rated, approved according to 4.4, recorded in the risk register, and limited to 12 months or less. An alternative to encryption (314.4(c)(3)) or to MFA (314.4(c)(5)) is valid only if the Qualified Individual approves it in writing and it is recorded as an exception. (PL-1; GV.RM-01)

4.8 **Service providers.** Before a vendor or servicer receives, maintains, or can access customer information or education records:
- the IT Director must complete a security review (a current SOC 2 Type 2 report or the college's security questionnaire);
- the contract must require the provider to implement and maintain safeguards, including MFA, encryption, and notice to the college of any security incident affecting college data within 72 hours;
- the contract must meet the FERPA school-official conditions: the provider performs an institutional function, is under the college's direct control for use and maintenance of the records, and may not redisclose them or use them for other purposes, including training its models.

Each provider must be reassessed at least annually, based on risk (P09). (SA-9; SR-6; GV.SC-05; GV.SC-07; 314.4(f)(1)-(3); 34 CFR 99.31(a)(1)(i)(B))

4.9 **Testing.** Controls must be tested:
- an independent control assessment every year (P07);
- vulnerability scans at least every six months, after material changes, and when circumstances may materially affect the program;
- an external penetration test every year, scoped from the risk assessment.

The college does not have continuous monitoring today, so the penetration test and six-month scans are required, not optional. (CA-2; CA-8; RA-5; ID.IM-02; 314.4(d)(1)-(2))

4.10 **Sanctions.** Workforce members and contractors who fail to comply with security or privacy policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, termination of employment, or termination of contract. HR and the policy owner must document each sanction. (PS-8; GV.RR-04)

4.11 **Change management.** Changes to the SIS, FAMS, identity provider, integration server, cloud tenant, and campus firewall must follow the change procedure:
- a written request that names the business reason and the data affected;
- a test outside production where the vendor provides one;
- approval by the IT Director and the data owner before the change;
- an entry in the change log.

Emergency changes may be made first, but they must be logged and approved within 2 business days. (CM-3; CM-4; PR.PS-01; 314.4(c)(7))

4.12 IT staff must complete security-specific training each year and follow CISA and FSA cybersecurity alerts. The Campus President must confirm completion in the annual Board report. When 24x7 detection is needed and the IT team cannot provide it, the college must use a qualified service provider. (AT-3; PR.AT-02; 314.4(e)(2)-(4))

4.13 The Qualified Individual must review the POA&M monthly and report program metrics to the Campus President quarterly. The program must be adjusted after testing, material changes, risk assessments, and security events. (CA-7; ID.IM-01; 314.4(g))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.10). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the annual Board report.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level in 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); POA&M (P07); FTC Safeguards Rule 16 CFR Part 314; FERPA 34 CFR Part 99; FSA Electronic Announcement GENERAL-23-09
