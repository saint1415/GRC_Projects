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
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory and guidance drivers | CSF 2.0 (benchmark); SP 800-82 Rev. 3; 17 CFR 229.106(b)-(c) |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, worker, grower, and customer information, keeps irrigation and packing operations safe and running, and supports the company's food safety, labor, and SEC disclosure obligations.

## 2. Scope
All Cris Santos Company workforce members (year-round employees, seasonal and H-2A workers, contractors, and integrator and vendor staff working on company systems) at the 48 farms, 17 packing sites, 6 irrigation control centers, offices, and both data center campuses in Florida, Georgia, South Carolina, and North Carolina, including acquired operations from their acquisition date. Covers all systems and data, including cloud, data centers, SaaS, operational technology (irrigation, fertigation and chemigation, packing, cold-chain, and drying controls), drones and equipment telematics, systems that vendors operate for the company, and the services offered to external growers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity and OT risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner for IT and OT; chairs the policy governance committee; approves standards |
| Director of OT Security | OT security engineering, OT remote access, OT patching and monitoring |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| System owners (for example, the Vice President, Irrigation and Water Resources) | Accountable for controls on their systems, including SSPs for tier-1 systems |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 The company must maintain an information security program for IT and OT aligned to NIST CSF 2.0, with NIST SP 800-82 Rev. 3 applied to OT, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the owner of the IT and OT security program, and the Director of OT Security as the accountable lead for OT security engineering. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Worker safety and food safety risks at High or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-04)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may access company systems or hold sensitive data until it has been tiered and assessed under STD-01.9 and its contract contains the standard security terms (MFA, incident notice, audit rights, and, for OT vendors, gateway-only access). Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. OT testing must run only in scheduled maintenance windows with the control center manager's approval. (CA-2; CA-7; ID.IM-01)
4.10 Every acquisition must include security due diligence before closing and an integration plan (PRC-01.3) that brings identity, network, logging, backup, and OT remote access to enterprise standards within 12 months of closing. (RA-3; SA-9; GV.SC-06)
4.11 Security documentation, including risk analyses, assessments, and required actions, must be retained for at least 6 years from creation or last effective date, whichever is later. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity and OT risk to the board risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Vulnerability and Patch Management Standard (IT and OT)
- STD-01.4 Audit Logging and Monitoring Standard (with the OT logging profile)
- STD-01.5 Configuration and Change Management Standard (with OT change control)
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Network Security and OT Segmentation Standard
- STD-01.9 Third-Party and Supply Chain Security Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Acquisition Security Integration Procedure
- PRC-01.4 OT Change Procedure (PLC logic, setpoints, fertigation recipes)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and OT change and session reviews. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Vendor violations are handled under the contract and STD-01.9.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a worker safety or food safety risk at High or above are refused unless a dated treatment plan exists, and no exception may waive a binding regulatory requirement. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FMICP SSP; P03 gap analysis; P05 BIA; P08 runbook and notification matrix; P10 AI governance.
