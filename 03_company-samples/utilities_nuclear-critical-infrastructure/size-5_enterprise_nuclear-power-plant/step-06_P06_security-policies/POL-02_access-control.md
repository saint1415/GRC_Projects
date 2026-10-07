# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-10, within the 15 calendar months CIP-003-9 R1 allows), and after major changes, incidents, acquisitions, or a final NRC rule |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(2), AC-2(3), AC-3, AC-5, AC-6, AC-6(9), AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | 10 CFR 73.54(c)(2); 73.56(m); CIP-003-9 Att. 1 Sec. 6; CIP-004-7 R4 and R5; CIP-005-7 R2; 10 CFR 50.36(c)(3) (record integrity context) |

## 1. Purpose
Make sure only authorized people and services reach company systems, with the least privilege they need, for as long as they need it. This matters most for the work management system (WMS), where clearance and surveillance records must be traceable to one person, and during refueling outages, when up to 1,500 contractors receive accounts at one station.

## 2. Scope
All Cris Santos Company workforce members (about 12,000 employees, the supplemental contractors who support refueling outages, and other contractors and vendors with company accounts) at the corporate campus in Florida, the four stations (Florida, Georgia, South Carolina, and Alabama), the Generation Dispatch Center, and the data centers DC-1 and DC-2. Covers all business systems and data, including the two public clouds, SaaS, the plant business networks, Station 4 legacy systems from the 2025-07-01 acquisition date, and the services sold to outside companies (SL-1 monitoring and diagnostics; SL-2 dosimetry processing). **Critical digital assets (CDAs) are governed by each station's NRC-approved cyber security plan (CSP) under 10 CFR 73.54.** This policy supports the CSPs and never overrides them; where a CSP or a NERC CIP requirement is stricter, the stricter rule applies.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Policy owner; runs the identity platform (SYS-03) |
| System owners (for example, Vice President, Fleet Work Management) | Approve role templates and access requests; certify access quarterly |
| Plant Managers | Approve station roles that touch clearances and surveillances |
| Vice President, Outage Management | Outage contractor coordinators request and end contractor accounts |
| Director, Nuclear Security | Links badging and access authorization events to account changes |
| Director, NERC Compliance | CIP-004 access management for the Generation Dispatch Center |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited, including at work control and outage center kiosks. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)

4.3 One person must not both write and approve the same clearance, release a surveillance result they performed, or create and pay a vendor. Role design and system checks must enforce this. (AC-5; PR.AA-05)

4.4 MFA is required for all remote access, all business system access, and all cloud and administrative access. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)

4.5 Access must be disabled the same business day as a termination, immediately for involuntary terminations, and at badge-out for outage contractors. (PS-4; AC-2; PR.AA-05)

4.6 Temporary accounts must carry an end date that matches the work period; bulk end-date extensions are prohibited. Accounts inactive for 60 days must be disabled automatically. (AC-2(2); AC-2(3); PR.AA-05)

4.7 Managers must certify their staff's access every quarter. (AC-2; PR.AA-05)

4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)

4.9 Vendor and remote maintenance access must go through PAM or the intermediate system with approval and session recording. No remote access to CDAs is permitted under any circumstance. (AC-17; MA-4; PR.AA-05)

4.10 Default passwords must be changed before any device is connected to a company network. (IA-5; PR.AA-01)

4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it, the CSPs, or a NERC CIP requirement.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure (including outage contractors)
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, quarterly access certification, the annual Internal Audit assessment (P07), Nuclear Oversight reviews of the security program (73.55(m)), NRC cyber security inspections, and NERC Regional Entity audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract. A violation by a person with unescorted access is also reported to the access authorization program, which decides whether it affects trustworthiness and reliability under 10 CFR 73.56.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may waive a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 WMS-PBN SSP; P03 gap analysis; P07 assessment and POA&M; P08 runbook and notification matrix; P10 AI governance; station cyber security plans and implementing procedures (controlled documents, not attached).
