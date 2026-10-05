# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-10, within the 15 calendar months CIP-003-9 R1 allows), and after major changes, incidents, acquisitions, or a final NRC rule |
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-1, AT-2, AT-2(3), AT-3, CM-11, AC-20, MP-7, SC-7, IR-6, SA-9 |
| CSF 2.0 | GV.PO-01, GV.RR-04, PR.AT-01, PR.AT-02, PR.PS-05, PR.IR-01, PR.DS-01, DE.AE-07 |
| Regulatory basis | 10 CFR 73.54(c)(1) and (d)(1); 73.22(b)(5); 73.77(a)(3) |

## 1. Purpose
Set the rules every user accepts for company systems, portable media, contractor devices, and AI tools. At a nuclear station, everyday user behavior (plugging in a USB drive, connecting a laptop, posting outage details) can affect the defensive architecture around plant systems.

## 2. Scope
All Cris Santos Company workforce members (about 12,000 employees, the supplemental contractors who support refueling outages, and other contractors and vendors with company accounts) at the corporate campus in Florida, the four stations (Florida, Georgia, South Carolina, and Alabama), the Generation Dispatch Center, and the data centers DC-1 and DC-2. Covers all business systems and data, including the two public clouds, SaaS, the plant business networks, Station 4 legacy systems from the 2025-07-01 acquisition date, and the services sold to outside companies (SL-1 monitoring and diagnostics; SL-2 dosimetry processing). **Critical digital assets (CDAs) are governed by each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54.** This policy supports the CSPs and never overrides them; where a CSP or a NERC CIP requirement is stricter, the stricter rule applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Policy owner; acceptance and training records |
| Vice President, Outage Management | Contractor acceptance before badging |
| Site Cyber Security Program Managers | Portable media kiosks and the CSP rules for media and devices near plant equipment |
| All users | Follow this policy and report concerns |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems are for business use; limited personal use must not affect security or operations. (PL-4; GV.RR-04)

4.2 All users must accept this policy at onboarding and annually; contractors must accept it before badging. (PL-4; AT-2; PR.AT-01)

4.3 Users must not post plant, outage, or security details on social media or public sites. (PL-4(1); PR.AT-01)

4.4 Users must report phishing and suspicious contacts immediately, including calls or messages asking about outages, security, or plant systems. (AT-2(3); IR-6; DE.AE-07)

4.5 Users must not install unapproved software. (CM-11; PR.PS-05)

4.6 Contractor and personal devices may connect only to the contractor or guest segment, never to business networks, and never to plant equipment. (AC-20; SC-7; PR.IR-01)

4.7 All external portable media must be scanned at a kiosk before use on any company system. Personal media must never be connected to plant equipment. (MP-7; PR.DS-01)

4.8 Only AI tools on the approved list (STD-05.3) may be used for company work. (SA-9; PL-4; GV.PO-01)

4.9 Users must complete security awareness training before access and annually, and role-based training where their role requires it. (AT-2; AT-3; PR.AT-01; PR.AT-02)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it, the CSPs, or a NERC CIP requirement.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems, Contractor Devices, and Portable Media Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certification, the annual Internal Audit assessment (P07), Nuclear Oversight reviews of the security program (73.55(m)), NRC cyber security inspections, and NERC Regional Entity audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract. A violation by a person with unescorted access is also reported to the access authorization program, which decides whether it affects trustworthiness and reliability under 10 CFR 73.56.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may waive a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 WMS-PBN SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; station cyber security plans and implementing procedures (controlled documents, not attached).
