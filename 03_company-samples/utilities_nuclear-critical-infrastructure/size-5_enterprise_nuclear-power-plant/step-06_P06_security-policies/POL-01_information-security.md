# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Risk committee of the board (on the recommendation of the executive risk committee); the Chief Nuclear Officer concurs for statements that touch the CSPs |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-10, within the 15 calendar months CIP-003-9 R1 allows), and after major changes, incidents, acquisitions, or a final NRC rule |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-5, SA-9, SR-6, SC-7, CM-4, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.RM-06, GV.OV-01, GV.OC-01, GV.SC-05, ID.IM-01, PR.IR-01 |
| Regulatory basis | 10 CFR 73.54(b)(2), (d)(2), (f), (g), (h); 73.55(m); CIP-003-9 R1 and R3; 17 CFR 229.106 |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of company, client, and personal information, protects the boundary between business systems and the station CDA networks, and supports the company's NRC, NERC, SEC, and state law obligations.

## 2. Scope
All Cris Santos Company workforce members (about 12,000 employees, the supplemental contractors who support refueling outages, and other contractors and vendors with company accounts) at the corporate campus in Florida, the four stations (Florida, Georgia, South Carolina, and Alabama), the Generation Dispatch Center, and the data centers DC-1 and DC-2. Covers all business systems and data, including the two public clouds, SaaS, the plant business networks, Station 4 legacy systems from the 2025-07-01 acquisition date, and the services sold to outside companies (SL-1 monitoring and diagnostics; SL-2 dosimetry processing). **Critical digital assets (CDAs) are governed by each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54.** This policy supports the CSPs and never overrides them; where a CSP or a NERC CIP requirement is stricter, the stricter rule applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reporting (Item 106 governance) |
| Nuclear safety oversight committee | Oversees nuclear safety and security performance, including the cyber security program |
| Audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks jointly; take part in materiality determinations |
| Chief Nuclear Officer | Executive owner of the 73.54 program; authorizing official equivalent for WMS-PBN |
| CISO | Enterprise program owner; chairs the policy governance committee; approves standards |
| Director, Nuclear Cyber Security | Owns the CSPs and the station cyber security programs |
| Director, Nuclear Security | Owns the SGI, access authorization, and fitness-for-duty programs |
| Chief Risk Officer | Enterprise risk management; owns the enterprise risk register |
| Chief Audit Executive; Director, Nuclear Oversight | Independent assessment (Internal Audit, third line) and the 73.55(m) program reviews |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0, with system security plans for tier-1 business systems. Critical digital assets are governed by the NRC-approved cyber security plans, which this policy supports and never overrides. (PM-1; PL-2; GV.PO-01)

4.2 The CISO is the enterprise program owner; the Director, Nuclear Cyber Security owns the cyber security plans; the Director, Nuclear Security owns the SGI, access authorization, and fitness-for-duty programs; the CIP Senior Manager (Vice President, Generation Dispatch and Energy Marketing) is designated as CIP-003-9 R3 requires. Each designation must be in writing. (PM-2; GV.RR-02)

4.3 An enterprise risk analysis must be performed at least annually and after major changes or acquisitions, using NIST SP 800-30 Rev. 1, and rolled up into the enterprise risk register following NIST IR 8286 Rev. 1. (RA-3; PM-9; GV.RM-01)

4.4 Risk may be accepted only at the authority levels in STD-01.1. ER-05 risks at High or above must not be accepted without a dated treatment plan, and no acceptance may waive a regulatory requirement or a cyber security plan commitment. (PM-9; GV.RM-06)

4.5 Policies must be reviewed at least annually; standards and procedures at least annually or when the controls they describe change; NERC CIP cyber security policies at least once every 15 calendar months. (PL-1; GV.PO-02)

4.6 Any deviation from a policy or standard must be approved through the exception process before it takes effect. The exception process cannot be used for a cyber security plan commitment, an SGI requirement, or a NERC requirement; those follow the license change or compliance process. (PL-1; CA-5; GV.PO-02)

4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)

4.8 No vendor may receive network or data access until it has been tiered and assessed under STD-01.3 and its contract has security, incident notice, and confidentiality terms. Contracts inherited through an acquisition must be reviewed within 90 days of closing. (SA-9; SR-6; GV.SC-05)

4.9 Controls for tier-1 business systems and common control providers must be assessed at least annually by an assessor independent of their operation. The cyber security program must be reviewed by Nuclear Oversight at least every 24 months. (CA-2; CA-2(1); ID.IM-01)

4.10 Every acquisition must include security due diligence before closing and an integration plan that brings identity, network, logging, endpoint, and cyber security plan procedures to fleet standards within 12 months of closing. (RA-3; SA-9; GV.OC-01)

4.11 Security documentation must be retained for at least 6 years. Cyber security program records must be retained until the license is terminated, and superseded portions for at least 3 years. (SI-12; GV.PO-02)

4.12 The CISO and the Chief Nuclear Officer must report cybersecurity risk to the board risk committee and the nuclear safety oversight committee at least quarterly, including High and Very High risks, risks outside tolerance, and significant incidents. (PM-9; GV.OV-01)

4.13 No business network, cloud, or SaaS system may connect toward a CDA network. Any new digital device or modification near plant equipment must receive the 73.54(b)(1) analysis and the design change cyber review before it is installed. (SC-7; CM-4; PR.IR-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it, the CSPs, or a NERC CIP requirement.
- STD-01.1 Risk Assessment Standard
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party and Supply Chain Security Standard
- STD-01.4 Audit Logging Standard
- STD-01.5 Configuration and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard (business facilities)
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure (including the design change cyber screening interface)

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certification, the annual Internal Audit assessment (P07), Nuclear Oversight reviews of the security program (73.55(m)), NRC cyber security inspections, and NERC Regional Entity audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract. A violation by a person with unescorted access is also reported to the access authorization program, which decides whether it affects trustworthiness and reliability under 10 CFR 73.56.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method (SP 800-30 Tables G-5 and I-2), approved at the authority level for the residual risk (statement 4.4), recorded in the exception register with compensating controls and an end date, and limited to 12 months. **An exception cannot waive a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement** (statement 4.6). Those follow the CSP change process (73.54(d)(3) and the license change rules), the SGI program, or the NERC compliance process. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details and current examples are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 WMS-PBN SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; station cyber security plans and implementing procedures (controlled documents, not attached).
