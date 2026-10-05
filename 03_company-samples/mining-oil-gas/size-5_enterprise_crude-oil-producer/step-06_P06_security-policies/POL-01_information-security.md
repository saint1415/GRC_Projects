# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3 (OT security program), 4.1 (risk management), 4.2 (supply chain) |

## 1. Purpose
Establish the enterprise information and OT security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, owner, partner, and customer information and the safe, reliable operation of field systems, and supports the company's SEC, PHMSA, EPA, and state law obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary workers, including the roughly 4,000 contractor workers on company sites on a typical day) at headquarters, the IOC, the BCC, the Florida regional control room, 60 field offices and yards, and every well site and facility in the Permian, Mid-Continent, and Florida operating areas, including acquired assets (AQ-MC) from the date of closing. Covers all business IT and OT systems and data, including cloud, colocation, SaaS, field devices and communications, systems that vendors operate for the company, and the services the company offers to outside parties (SL-1 owner and partner services; SL-2 water services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Risk committee of the board | Oversees cybersecurity and OT risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| Chief Operating Officer | Business owner of field operations; authorizing official for the FSPA |
| CISO | Program owner for IT and OT security; chairs the policy governance committee; approves standards |
| Director of OT Security | OT security lead; owns STD-01.8 and the OT tailoring register |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, with OT protected according to NIST SP 800-82 Rev. 3, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO is accountable for the IT and OT security program, and the Director of OT Security must be designated in writing as the OT security lead. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Process safety and environmental risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive company data or remote access to IT or OT until it has been tiered and assessed under STD-01.3 and its contract includes the security schedule, including incident notice and, where it holds personal information, breach notice within 10 days of determination. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include an IT and OT security assessment before closing and an integration plan, funded at approval, that brings identity, network, monitoring, and OT change control to enterprise standards within 18 months of closing (PRC-01.4). (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 6 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity and OT risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard (SP 800-82 Rev. 3 overlay and tailoring register)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (IT and OT change boards)
- PRC-01.4 Acquisition Security Integration Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT monitoring at the control centers), the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Contractor violations are handled under the contractor's agreement and can end site access.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a process safety or environmental risk at High or above are refused unless a dated treatment plan exists. OT exceptions also need the Director of OT Security's sign-off. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FSPA SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; NIST SP 800-82 Rev. 3.
