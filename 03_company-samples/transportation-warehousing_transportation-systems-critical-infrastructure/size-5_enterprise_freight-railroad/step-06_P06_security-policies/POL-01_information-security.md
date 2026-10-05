# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Information Security Officer (CISO) |
| Approved by | Board safety, security, and risk committee, on the recommendation of the executive risk committee (2026-09-08) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or a TSA Security Directive renewal with substantive changes |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, RA-3, CA-2, CA-2(1), CA-5, PS-8, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| TSA / regulatory basis | SD 1580/82-2022-01E Sec. II.B, III.F, VI; SD 1580-21-01E Sec. II.B; 49 CFR 1570.201; 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every employee, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the safety, integrity, and availability of rail operations and the confidentiality of Sensitive Security Information (SSI), personal information, and customer data, and supports the company's TSA, FRA, SEC, and state law obligations.

## 2. Scope
All Cris Santos Company employees and contractors at the 64 railroads, about 290 field sites, both NOCs, DC-1 and DC-2, including acquired railroads from their closing date. Covers all IT and OT systems and data, including cloud, SaaS, wayside and onboard equipment, systems that vendors operate for the company, and the technology services sold to unaffiliated railroads (SL-1 and SL-2). Where a TSA Security Directive or the TSA-approved Cybersecurity Implementation Plan (CIP) sets a stricter requirement for the Covered Railroads, that requirement applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board safety, security, and risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; primary TSA Cybersecurity Coordinator; chairs the policy governance committee; approves standards |
| Assistant Vice President, Rail Security | Primary TSA Security Coordinator (49 CFR 1570.201); SSI program; hazmat security plan |
| Director of OT Security | OT security for dispatch, PTC, CTC, and wayside; alternate Cybersecurity Coordinator |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All employees and contractors | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 and NIST SP 800-82 Rev. 3, documented in this policy hierarchy, in system security plans for tier-1 systems, and, for the Covered Railroads, in the TSA-approved CIP. (PM-1; PL-2; GV.PO-01)
4.2 The company must designate in writing a primary and at least one alternate Cybersecurity Coordinator and Security Coordinator at the corporate level, keep at least one U.S. citizen eligible for a security clearance among the Cybersecurity Coordinators, and file changes with TSA within 7 days. (PM-2; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Rail safety risks at Moderate or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. A deviation from a CIP measure also needs a CIP amendment check. (PL-1; CA-5; GV.PO-02)
4.7 Employees who violate security policies must be sanctioned under PRC-01.1 and the applicable collective bargaining agreement procedures, in proportion to intent and harm. (PS-8; GV.RR-04)
4.8 No vendor may access Critical Cyber Systems, SSI, or personal information until it has been tiered and assessed under STD-01.3 and its contract includes security, notification, and CIP terms. The company keeps responsibility for CIP measures performed by an MSSP or authorized representative. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation, and the Cybersecurity Assessment Plan must cover at least one-third of CIP measures each year and all of them over three years. (CA-2; CA-2(1); ID.IM-01)
4.10 Every acquisition must include security due diligence before closing, a TSA filing plan (coordinator data within 7 days; CIP amendment within 50 days), and an integration plan that brings identity, network, logging, and endpoint controls to enterprise standards. (RA-3; SA-9; GV.OC-03)
4.11 Security documentation, including risk analyses, assessments, CIP and CAP records, and required actions, must be retained for at least 7 years, and SSI must be handled under POL-04. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board safety, security, and risk committee at least quarterly, including Very High and High risks, risks outside tolerance, and material incidents. (PM-9; GV.OV-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and Cybersecurity Assessment Plan Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration, Change, and Patch Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 Network Zone and Segmentation Standard
- PRC-01.1 Security Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (including PTC configuration control)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the Cybersecurity Assessment Plan, and access certifications. Violations are handled under PRC-01.1 (statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Requests that would leave a rail safety risk at Moderate or above are refused unless a dated treatment plan exists. An exception to a CIP measure cannot take effect until the CISO has decided whether a CIP amendment or a notice to TSA is required. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TDPB SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
