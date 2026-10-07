# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-08-24 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AT-1, CM-1, IR-1, PL-1, PS-1, SA-1, SC-1, PL-4, AT-2, IR-6, AC-11, AC-19, AC-20, SA-9, CM-7, PS-7, CM-3, CM-5, SC-8, AC-17 |
| CSF 2.0 | PR.AT-01, RS.MA-01, RS.MA-02, PR.AA-05, ID.AM-02, ID.AM-04, GV.OC-05, GV.SC-04, PR.PS-01, GV.RR-04, DE.CM-06, ID.RA-07, PR.DS-02 |
| HIPAA Security Rule and other drivers | 164.308(a)(3); 164.308(a)(5); 164.308(a)(5)(i); 164.308(a)(6)(ii); 164.308(b)(1); 164.310(b); 164.310(c); 164.312(c)(1); 164.312(e)(1); 164.502(b); see `policy-control-map.csv` for each statement's driver |

## 1. Purpose
Set the rules every workforce member and affiliate user follows when using the system's information, devices, networks, and AI tools.

## 2. Scope
All Cris Santos Company workforce members (employees, medical staff, agency and contracted staff, students, and volunteers) at the 8 hospitals, 3 freestanding emergency departments, 46 clinics, 4 imaging centers, the data centers, and corporate offices in Florida, Georgia, and Alabama, including H-08 and any future acquisition from its closing date. Covers all systems and data, including the data centers, both clouds, SaaS, medical devices, building OT, systems that vendors operate for the system, and the services sold to other organizations (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; training and attestation records |
| Managers | Make sure their staff, students, and agency staff follow it |
| CISO | Approved AI tools list (STD-05.3) with the AI governance committee |
| All users | Follow this policy; report concerns |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Information and systems may be used only for authorized purposes. Looking up one's own record, or the record of a family member, coworker, or public figure, without a job need is prohibited. (PL-4; )
4.2 Every user must complete security and privacy training before first access and annually, and accept this policy each year. (AT-2; PL-4; PR.AT-01)
4.3 Users must report suspicious email, lost devices, and suspected incidents immediately. (IR-6; AT-2; RS.MA-01; RS.MA-02; PR.AT-01)
4.4 Users must lock or tap out of a workstation whenever they step away. (AC-11; )
4.5 Personal devices may reach system data only through the EHR mobile app or the zero-trust gateway; PHI must not be stored on personal devices or personal accounts. (AC-19; AC-20; PR.AA-05; ID.AM-02; ID.AM-04)
4.6 Only AI tools on the approved list (STD-05.3) may be used for work, and any AI feature in a vendor product must be registered with the AI governance committee before use. (SA-9; CM-7; GV.OC-05; GV.SC-04; PR.PS-01)
4.7 Agency staff, students, and contracted clinicians follow this policy in full; their contracts require it. (PS-7; AT-2; GV.RR-04; DE.CM-06; PR.AT-01)
4.8 Nobody may change clinical decision support settings, including the sepsis model threshold, outside change control. (CM-3; CM-5; ID.RA-07; PR.PS-01)
4.9 PHI may be sent only through approved channels: secure clinical messaging, encrypted email, or the EHR. Personal texting and personal email are prohibited for PHI. (SC-8; AC-20; PR.DS-02; ID.AM-02; ID.AM-04)
4.10 Remote work with PHI is allowed only from managed devices through the zero-trust gateway. (AC-17; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the emergency preparedness program's exercises. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, contract, or privileges, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ECIS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the unified emergency preparedness plan.
