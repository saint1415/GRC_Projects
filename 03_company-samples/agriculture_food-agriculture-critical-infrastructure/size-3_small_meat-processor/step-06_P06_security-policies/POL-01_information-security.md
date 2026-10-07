# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | General Manager |
| Approved by | General Manager |
| Effective date | 2026-09-07 |
| Review cycle | Annually (next review 2027-09-04), and after major changes, incidents, or a food defense reanalysis |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CM-3, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OC-03, GV.RM-01, GV.SC-05, ID.RA-01 |
| Regulatory basis | 21 CFR 121.4(d), 121.157; 9 CFR 417.4(a)(3), 417.5(d); NIST SP 800-82 Rev. 3 (benchmark) |

## 1. Purpose
Set up the Cris Santos Company information security program for both business IT and plant operational technology (OT), assign who is accountable, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company information and, above all, **the integrity of the systems that make and record safe food**.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary and agency workers, and contractors) at the Florida plant and outlet store. Covers all systems and data, including process control systems (PLCs, HMIs, SCADA, historian, recipe and batch system, refrigeration controls, cold-chain monitoring), cloud and SaaS services, and systems that vendors operate or maintain for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks |
| General Manager | Program owner; approves policies; accepts Moderate risks; signs the food defense plan |
| IT Manager | Security lead for IT and OT; maintains the risk register and SSP |
| Controls Engineer | OT system owner; runs OT change control |
| FSQA Manager | Food Defense Coordinator; decides product holds and FSIS and FDA notifications |
| Maintenance and Refrigeration Manager | Refrigeration controls and contractor oversight |
| All workforce | Follow these policies; report suspicious activity immediately |

## 4. Policy statements
4.1 The company must maintain an information security program covering IT and OT, documented in this policy set and the System Security Plan. (PM-1; GV.PO-01)
4.2 The IT Manager is the designated security lead for IT and OT, and the FSQA Manager is the designated Food Defense Coordinator. Both designations must be in writing. (PM-2; GV.RR-02; 21 CFR 121.4(d))
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and must include scenarios in which process controls are used to adulterate food or disrupt CCPs. Risks must be tracked in the risk register with an owner and a treatment. (RA-3; PM-9; ID.RA-01)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the General Manager, Moderate; the majority owner, High and Very High. A risk that could put adulterated product into commerce must not be accepted at High; it must be treated. (PM-9; GV.RM-01)
4.5 **Security and food defense work together.** The FSQA Manager must receive the risk register each year and after each update, and must decide whether new information requires a food defense reanalysis. (RA-3; 21 CFR 121.157(b)(2))
4.6 **OT change control.** No change to a PLC program, HMI, recipe or formulation, setpoint range, smokehouse cycle, or OT network may go live without a recorded request, a test, Controls Engineer approval and, for any change that touches a CCP or an actionable process step, FSQA Manager approval and a food defense reanalysis check. (CM-3; PR.PS-01; 21 CFR 121.157(b)(1), (c); 9 CFR 417.4(a)(3))
4.7 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.8 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.9 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. Intentional tampering with process controls or food safety records is grounds for termination and referral to law enforcement. HR must document each sanction. (PS-8; GV.RR-04)
4.10 Before a vendor gets remote access to OT or handles Restricted data, it must accept the company's security terms (named accounts, MFA, approved sessions, incident notice) and complete a security review. Critical vendors are reviewed each year, using a SOC 2 report where available. (SA-9; SR-6; GV.SC-05)
4.11 Security controls must be assessed at least annually (P07) and after major changes. (CA-2)
4.12 Security documentation must be retained for at least 3 years. Food safety and food defense records follow their own retention rules (9 CFR 417.5(e); 21 CFR 121.315), which POL-04 sets out. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.9). Compliance is checked through the annual control assessment (P07), OT change audits, and food defense verification (21 CFR 121.150).

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); food defense plan; HACCP plans; OT change procedure
