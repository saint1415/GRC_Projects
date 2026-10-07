# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, SA-4, SA-9, SR-6, CM-3, PL-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.OV-01, GV.OC-03, GV.SC-05, GV.SC-07 |
| CISA CPG 2.0 (voluntary) | 1.A, 1.B, 1.D, 1.E, 2.B, 2.C, 3.N |
| Other drivers | Fla. Stat. 501.171(2) (reasonable measures); FTC Act Section 5; PCI DSS v4.0.1 Req. 12.1 (SAQ P2PE) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, tenant, and visitor information, and the safe operation of the building systems the company runs for its tenants.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) at Property A, Property B, Property C, and remote locations. Covers all information systems and data, **including building operational technology (OT)**: the building automation system (BAS), physical access control, video surveillance, and the networks that connect them. It also covers systems and devices that integrators, the managed service provider (MSP), the guard contractor, and other vendors operate or support for the company. Life-safety systems (fire alarm, elevators, emergency voice communication) are covered only by the separation rule in 4.11.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner (CEO) | Approves the security budget; accepts High and Very High risks |
| Chief Operating Officer | Program owner; approves policies; accepts Moderate risks; system owner of the Building Automation and Access Control System (BAACS) |
| IT Manager (security lead) | Runs the program day to day; maintains the risk register, SSP, and POA&M |
| Director of Engineering | Owns BAS security, integrator oversight, and manual operating procedures |
| Security Manager | Owns access control, video, and visitor management security |
| Controller | Owns PCI DSS compliance and the SAQ |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the System Security Plan (P02), and the risk register (P01). The program uses the CISA Cross-Sector Cybersecurity Performance Goals (CPG 2.0) as its baseline, with NIST SP 800-82 Rev. 3 for OT. (PM-1; GV.PO-01; CPG 1.B)
4.2 The IT Manager is the designated security lead. The Director of Engineering and the Security Manager are the named owners of building system security. These designations must be in writing, and IT and engineering staff must meet at least monthly on security. (PM-2; GV.RR-02; CPG 1.A)
4.3 A risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; CPG 2.B)
4.4 **Risk acceptance authority:** the IT Manager may accept Low and Very Low risks; the COO, Moderate; the majority owner, High and Very High, and only temporarily with a dated treatment plan. A risk that could leave a building without working doors or cooling may not be accepted at High. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.6 **Exceptions** to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. OT devices that cannot meet a technical requirement must have a documented compensating control. (PL-1)
4.7 **Sanctions.** Workforce members who break security policies are subject to discipline in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. Contractors who break these policies may lose access and be removed from the contract. (PS-8; GV.RR-04)
4.8 **Vendors with access.** Before a vendor gets remote or administrative access to company systems, or stores personal information for the company, its contract must include the company's security addendum: named accounts, MFA, incident notice to the company within 24 hours of discovery, notice of known vulnerabilities in supplied products, and the right to review its security. Vendors that provide remote management of IT or OT (the MSP and integrators) must be reviewed each year. (SA-4; SA-9; SR-6; GV.SC-05; GV.SC-07; CPG 1.D; 1.E)
4.9 Security controls must be assessed at least annually (P07) by someone who does not operate them, and after major changes. (CA-2; CPG 2.C)
4.10 **Building system changes.** Changes to BAS programs, access control configuration, OT networks, and platform features (including analytics or biometric features offered by a vendor) must be requested, approved by the system owner's delegate, backed up before the change, and recorded. Biometric features require COO approval after an AI risk assessment (P10). (CM-3; CPG 3.N)
4.11 **Life-safety separation.** Fire alarm, elevator, and emergency voice systems must stay on separate networks. The BAS may read fire alarm status only through hardwired, read-only relay points. No change may create a network path from any IT or OT system to a life-safety system. (PL-8)
4.12 Security policies, risk assessments, assessment reports, and incident records must be retained for at least 5 years. (Fla. Stat. 501.171(4)(c) requires 5 years for any written no-harm determination.)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the reviews required in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); CISA CPG 2.0; NIST SP 800-82 Rev. 3; Fla. Stat. 501.171; the vendor security addendum
