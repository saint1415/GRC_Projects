# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | CA-1, CP-1, IR-1, PL-1, PS-1, RA-1, SA-1, SI-1, SR-1, PM-1, PL-2, PM-2, RA-3, PM-9, RA-7, CA-5, PS-8, SA-9, SR-6, CA-2, CA-2(1), SI-12, CP-2, IR-8 |
| CSF 2.0 | GV.OC-03, GV.PO-01, ID.AM-03, GV.RR-01, GV.RR-02, GV.RM-06, GV.RM-07, GV.OC-02, GV.RM-01, GV.OC-05, ID.IM-01, GV.SC-04, ID.RA-01, ID.AM-07, ID.AM-08, ID.IM-02 |
| HIPAA Security Rule and other drivers | 164.105(b); 164.306(d)(3); 164.308(a)(1); 164.308(a)(1)(ii)(A); 164.308(a)(1)(ii)(B); 164.308(a)(1)(ii)(C); 164.308(a)(2); 164.308(a)(8); 164.308(b)(1); 164.316(b)(2)(i); 164.316(b)(2)(iii); see `policy-control-map.csv` for each statement's driver |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, connect cybersecurity to the unified emergency preparedness program, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of patient, partner, and company information and supports the system's HIPAA, CMS, EMTALA, CLIA, Section 1557, 42 CFR Part 2, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, medical staff, agency and contracted staff, students, and volunteers) at the 8 hospitals, 3 freestanding emergency departments, 46 clinics, 4 imaging centers, the data centers, and corporate offices in Florida, Georgia, and Alabama, including H-08 and any future acquisition from its closing date. Covers all systems and data, including the data centers, both clouds, SaaS, medical devices, building OT, systems that vendors operate for the system, and the services sold to other organizations (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; chairs the policy governance committee; approves standards |
| Director of Security Operations | HIPAA Security Officer for the affiliated covered entity (45 CFR 164.308(a)(2)); runs the SOC |
| Chief Privacy Officer | HIPAA Privacy Officer; breach determinations |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Vice President, Emergency Management | Unified emergency preparedness program (42 CFR 482.15(f)) |
| Hospital presidents | Accountable for their hospital's compliance; name a local security liaison |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The system must maintain an information security program aligned to NIST CSF 2.0 that meets the HIPAA Security Rule and other applicable requirements, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.OC-03; GV.PO-01; ID.AM-03)
4.2 The Director of Security Operations must be designated in writing as the HIPAA Security Officer and the Chief Privacy Officer as the HIPAA Privacy Officer for the affiliated covered entity; each hospital president must name a local security liaison. (PM-2; GV.RR-01; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, covering every hospital from its acquisition date, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-06; GV.RM-07; GV.OC-02)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Patient-safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; RA-7; GV.OC-02; GV.RM-01; GV.OC-05)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; PM-1; GV.OC-03; GV.PO-01)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.OC-03; GV.PO-01; ID.IM-01)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; )
4.8 No vendor may create, receive, maintain, or transmit PHI for the system until a business associate agreement is signed and the vendor has been tiered and assessed under STD-01.3. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.OC-05; GV.SC-04; GV.OC-02)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.RA-01; ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, and endpoint controls to enterprise standards before the acquired hospital connects to the ECIS, and within 12 months of closing. (RA-3; SA-9; GV.RM-06; GV.RM-07; GV.OC-05)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 6 years from creation or last effective date, whichever is later. (SI-12; ID.AM-07; ID.AM-08)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OC-02; GV.RM-01)
4.13 Cyberattacks and prolonged IT outages must be scored in the facility-based and community-based risk assessments of the unified emergency preparedness program, and every hospital must have an IT-outage annex that links to the incident response runbook. (CP-2; IR-8; ID.IM-01; ID.IM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Medical Device Security Standard
- PRC-01.1 HIPAA Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and the emergency preparedness program's exercises. Violations are handled under the HIPAA sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment, contract, or privileges, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a patient-safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ECIS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the unified emergency preparedness plan.
