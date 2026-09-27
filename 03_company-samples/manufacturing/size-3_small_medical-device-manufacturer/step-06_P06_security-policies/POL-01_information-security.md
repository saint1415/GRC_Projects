# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | COO |
| Approved by | COO (CEO for the risk acceptance rules in 4.4) |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after a new marketing submission, a major change, or an incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, SA-8, SA-9, CA-2, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.OC-03, GV.SC-05 |
| Regulatory basis | FD&C Act 524B(b)(2) (N31-33-R05); 21 CFR 820.10(c); HIPAA Security Rule for the device cloud, 45 CFR 164.308(a)(1), (a)(2), (a)(8), (b)(1) and 164.316 (N62-R01) |

## 1. Purpose
Set up the Cris Santos Company information and product security program, assign who is accountable, and give every other security policy its authority. The program protects:
- the confidentiality, integrity, and availability of company information and systems;
- the PHI the device cloud holds for hospital customers;
- the cybersecurity of the company's medical devices and their related systems across the total product life cycle.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and temporary staff). Covers all company systems and data, including:
- corporate IT, engineering systems, and the factory floor (MES and test stations);
- the device cloud and the services that support it;
- fielded PM-2 and PM-1 monitors, for the security of their design, software, and updates;
- systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CEO (majority owner) | Approves the security budget; accepts High and Very High risks |
| COO | Program owner; approves policies; accepts Moderate risks |
| IT Manager | Security Officer for corporate IT and designated HIPAA security official for the device cloud (45 CFR 164.308(a)(2)); maintains the risk register and SSP |
| VP Engineering | Secure product development, SBOMs, code signing, and security testing of devices and the device cloud |
| Product Security Lead | Threat models, vulnerability monitoring, coordinated vulnerability disclosure (CVD) |
| VP QA/RA | Section 524B compliance; FDA reporting decisions; keeps product security records in the QMS |
| Compliance Manager (Privacy Officer) | BAAs; breach risk assessments; sanctions decisions with HR |
| All workforce | Follow these policies; report suspected incidents and vulnerabilities immediately |

## 4. Policy statements
4.1 The company must maintain an information and product security program documented in this policy set, the device cloud SSP (P02), and the QMS procedures for product security. (PM-1; GV.PO-01)
4.2 The IT Manager is the designated Security Officer and HIPAA security official for the device cloud. The Product Security Lead is the designated product security contact. Both designations must be in writing. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 A risk assessment must be performed at least annually, after a major change, and before each marketing submission, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and treatment. Product security risks must also be carried in the design risk management file (21 CFR 820.10(c)). (RA-3; PM-9; 164.308(a)(1)(ii)(A)-(B))
4.4 **Risk acceptance authority:** the IT Manager may accept Low and Very Low risks; the COO, Moderate; the CEO, High and Very High, only temporarily and with a dated treatment plan. **A patient-safety risk rated High must never be accepted without remediation.** (PM-9; GV.RM-01)
4.5 Security requirements must be part of design and development for every device and every device cloud release, including threat modeling of the device and its related systems, security testing, and an SBOM. (SA-8; FD&C Act 524B(b)(2)-(3))
4.6 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR and the Privacy Officer must document each sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
4.9 **No BAA, no PHI.** Before any vendor creates, receives, maintains, or transmits PHI for the device cloud, it must sign a subcontractor business associate agreement and complete a security review. (SA-9; GV.SC-05; 164.308(b)(1); 164.314(a))
4.10 Security controls must be evaluated at least annually (P07) and after major changes. The device cloud must also be independently tested at least annually. (CA-2; 164.308(a)(8))
4.11 Security policies, procedures, assessments, risk decisions, and vulnerability and CVD records must be retained for at least 6 years from creation or last effective date, whichever is later. Records that are also QMS records follow the longer QMS retention period. (SI-12; 164.316(b)(2)(i))

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), internal QMS audits, and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved at the level set in 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); QMS design control and risk management procedures; FD&C Act section 524B (21 U.S.C. 360n-2); HIPAA Security Rule, 45 CFR Part 164 Subpart C
