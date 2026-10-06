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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, SA-9, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory drivers | CPG 2.0 goals 1.A, 1.B, 1.D, 1.E, 2.C (R05); 17 CFR 229.106 (R04); 11 CCR 7122 and 7150 (R03); PCI DSS Req. 12.1 (R01) |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of tenant, visitor, employee, client, and company information and the safe operation of building systems, and supports the company's obligations under SEC disclosure rules, the CCPA and CPPA regulations, state privacy and breach laws, PCI DSS, and client contracts.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and TRS staff) at all 140 operated properties in Florida, Texas, Georgia, North Carolina, Arizona, and California, including acquired properties from their acquisition date. Covers all systems and data: IT, OT (building automation, access control, video), cloud, colocation, SaaS, systems that integrators and other vendors operate for the company, and the services the TRS offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, disclosure controls, and the CPPA cybersecurity audit |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner for IT and OT security; chairs the policy governance committee; approves standards |
| Director of OT Security | Leads OT security standards, monitoring, and the OT remote access gateway |
| Chief Privacy Officer | Privacy program; CPPA risk assessments; breach determinations with the General Counsel |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, with CISA CPG 2.0 as the IT and OT baseline, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the senior information security officer for IT and OT systems, the Director of OT Security as the lead for building systems security, and the Chief Privacy Officer as the lead for privacy. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Occupant-safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security or privacy policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive access to company systems or to personal information until it has been tiered and assessed under STD-01.3 and its contract includes the security addendum (incident notice within 24 hours, named accounts, OT remote access only through the OT remote access gateway). Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SA-4; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. The assessor for the CPPA cybersecurity audit must meet 11 CCR 7122, and Internal Audit must not audit an area where it developed procedures or made program recommendations. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include IT and OT security due diligence before closing and an integration plan that brings identity, network segmentation, logging, endpoint, backup, and remote access controls to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)
4.11 Security documentation, including risk analyses, assessments, incident records, and materiality determinations, must be retained for at least 7 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and significant incidents. (PM-9; GV.OV-01)
4.13 No AI use case, vendor-enabled video analytics feature, or biometric feature may be used until it is registered in the AI inventory and approved by the AI governance committee at the level its risk tier requires (P10). (RA-3; SA-9; GV.OC-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Architecture Standard (zones and conduits; life-safety design rule)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (including emergency OT changes)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave an occupant-safety risk at High or above are refused unless a dated treatment plan exists. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 BAACS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
