# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Safety, risk, and reliability committee of the board (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions. CIP-003-9 R1 content is also approved by the CIP Senior Manager at least once every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-2, RA-3, CA-2, CA-5, CA-6, SA-9, SR-5, SR-6, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-01, GV.RR-02, GV.OV-01, GV.RM-01, GV.SC-05 |
| Regulatory basis | FERC Security Program Rev. 3A 3.2 and Section 9; NERC CIP-002-5.1a, CIP-003-9 R1 to R4, CIP-013-2; 18 CFR 12.12, 12.62; 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program for IT and OT, assign accountability from the board to every workforce member, set the policy hierarchy and exceptions process, and give every other security policy its authority. The program protects people downstream of the company's dams, the reliability of its generation, and the confidentiality, integrity, and availability of company and client information, and supports the company's FERC, NERC, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and interns) at the headquarters, 14 offices, two Hydro Operations Centers, the Contract Operations Center, and all 46 developments in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, including the Piedmont developments from their acquisition date. Covers all systems and data: IT, OT (fleet SCADA, plant control, spillway and gate control, dam safety instrumentation and warning), cloud, colocation, SaaS, and systems that vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Safety, risk, and reliability committee of the board | Oversees cybersecurity, physical security, dam safety, and NERC compliance risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations |
| CISO | Program owner for IT and OT security; chairs the policy governance committee; approves standards |
| Senior Vice President, Hydro Operations | CIP Senior Manager (CIP-003-9 R3) |
| Vice President, Dam Safety | Chief Dam Safety Engineer (18 CFR 12.62(a)) |
| Vice President, Corporate Security | FERC primary security contact |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line) |
| All workforce | Follow policies, standards, and procedures; report incidents and suspicious activity |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program for IT and OT aligned to NIST CSF 2.0, using NIST SP 800-82 Rev. 3 as the OT benchmark, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01; GV.PO-02; ID.AM-03)
4.2 The CIP Senior Manager must be identified by name and any change recorded within 30 calendar days; delegations must be documented. A primary FERC security contact, project alternates, and a Chief Dam Safety Engineer must be designated in writing. (PM-2; GV.RR-01; GV.RR-02)
4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, including downstream safety consequences, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; ID.RA-01; ID.RA-03; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Public safety risks at High or above and any NERC CIP noncompliance must not be accepted; they require a dated treatment or mitigation plan. (PM-9; GV.RM-01; GV.RM-02)
4.5 Policies must be reviewed at least annually, and the cyber security policies required by CIP-003-9 R1 must be reviewed and approved by the CIP Senior Manager at least once every 15 calendar months. (PL-1; GV.PO-01; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect. CIP Exceptional Circumstances may be declared only under PRC-01.4 and must be documented. (CA-5; PL-1; ID.IM-01; ID.IM-02; GV.PO-01)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No vendor may receive OT access, remote access, BCSI, or CEII until it is tiered and assessed under STD-01.3 and its contract includes the CIP-013-2 R1.2 terms. The company applies these terms to every OT procurement, not only medium impact ones. (SA-9; SR-5; SR-6; GV.SC-04; GV.SC-05; GV.SC-02)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by an assessor independent of their operation. (CA-2; CA-2(1); ID.IM-01; ID.IM-02)
4.10 Every acquisition must include security due diligence before closing, CIP-002 identification of acquired BES assets at closing, and an integration plan. No acquired OT system may connect to the HOC until it meets fleet standards and has been assessed. (RA-3; CA-3; CA-6; ID.RA-01; ID.RA-03; ID.AM-03)
4.11 Section 9 determinations must be reviewed at least every 12 months and whenever remote capability changes; CIP-002 identifications at least every 15 calendar months. (RA-2; RA-9; ID.RA-04; ID.RA-05; ID.AM-05)
4.12 Records must be retained per the retention schedule: CIP evidence for the NERC audit period, Part 12 permanent project records under 18 CFR 12.12, and other security documentation for at least 7 years. (SI-12; ID.AM-07; ID.AM-08)
4.13 The CISO must report cybersecurity risk to the safety, risk, and reliability committee at least quarterly, including Very High and High risks, risks outside tolerance, NERC self-reports, FERC findings, and material incidents. (PM-9; GV.RM-01; GV.RM-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supply Chain Security Standard (includes the CIP-013-2 plan)
- STD-01.4 Audit Logging and Monitoring Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 OT Security Standard (Section 9 baseline and enhanced measures)
- STD-01.9 NERC CIP Program Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 OT Change Management Procedure
- PRC-01.4 CIP Exceptional Circumstances Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access verifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot excuse a NERC CIP requirement; CIP Exceptional Circumstances follow PRC-01.4 and are reported to the CIP Senior Manager. Requests that would leave a public safety risk at High or above are refused unless a dated treatment plan exists. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HFCDMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
