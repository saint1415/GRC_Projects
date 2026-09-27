# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | CFO |
| Approved by | CFO, with the VP Operations for statements that affect field operations |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, SA-9, CA-2, CM-4, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-02, GV.OC-03, GV.SC-05 |
| Benchmark (N21-BM) | NIST CSF 2.0 with NIST SP 800-82 Rev. 3, sections 3.3.1 (governance), 3.3.4 (policies), 4.1 (OT risk) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects the safety, reliability, and integrity of field operations, and the confidentiality of royalty owner, employee, and reservoir information.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary workers) at headquarters, both field offices, the Operations Control Center (OCC), and every well site and facility. Covers all business IT and operational technology (OT): corporate systems, SaaS and cloud services, the SCADA system, field controllers, and field communications, including systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks |
| CFO | Program owner and executive sponsor; approves policies; accepts Moderate risks |
| VP Operations | Business owner of field operations and SCADA; must agree to any security decision or risk acceptance that affects field operations or safety |
| IT Manager (Information Security Lead) | Runs the program day to day; maintains the risk register and SSP; owns corporate, cloud, and SaaS security |
| SCADA and Automation Supervisor (OT security lead) | Owns SCADA and field device security; oversees the SCADA integrator |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program, documented in this policy set and the System Security Plan, that covers both business IT and OT. (PM-1; GV.PO-01)
4.2 The IT Manager is the designated Information Security Lead and the SCADA and Automation Supervisor is the designated OT security lead. Both designations must be in writing, with a written split of IT and OT duties. (PM-2; GV.RR-02)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1 and the OT threat guidance in NIST SP 800-82 Rev. 3. Risks must be tracked in the risk register with an owner and treatment. (RA-3; PM-9; ID.RA-05)
4.4 Risk acceptance authority: the IT Manager (or the SCADA and Automation Supervisor for OT-only items) may accept Low risks; the CFO, Moderate, with the VP Operations' agreement if field operations are affected; the majority owner, High and Very High. No risk whose impact includes injury, H2S exposure, or a release to the environment may be accepted at High. (PM-9; GV.RM-02)
4.5 **Safety comes first.** No security control, test, or change may disable, bypass, or slow a safety shutdown or alarm. Any security change to the SCADA system or field controllers must be reviewed for operational and safety impact by the SCADA and Automation Supervisor before it is made. (CM-4; GV.RM-02)
4.6 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and limited to 12 months or less. Exceptions for OT systems also require the VP Operations' agreement. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. Good-faith incident reporting is never sanctioned. (PS-8; GV.RR-04)
4.9 **Suppliers.** No supplier may connect to the SCADA system or receive Restricted data (POL-04) until it has signed the company's security schedule (named accounts, MFA, incident notice, cooperation in breach response) and passed a security review. Existing contracts must add the schedule at renewal. (SA-9; GV.SC-05)
4.10 Security controls must be assessed at least annually by someone independent of their operation (P07), and after major changes. (CA-2; ID.IM-01)
4.11 The company must track the laws and rules that apply to its cybersecurity, and recheck applicability at least annually and when a rule changes or the business changes (for example, acquiring a pipeline or offshore asset). (PL-1; GV.OC-03)
4.12 Security policies, risk assessments, assessment results, and incident records must be retained for at least 3 years. (SI-12; GV.PO-02)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Regulatory Gap Analysis (P03); Emergency Response Plan (spills, fires, H2S)
