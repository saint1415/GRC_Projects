# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director, Identity and Access Management (OT statements jointly with the Director, OT Security) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| NERC CIP | Supports CIP-004-7 R4 to R6, CIP-005-7 R2 and R3, CIP-007-6 R5, CIP-003-9 Attachment 1 Sections 3 and 6 |

## 1. Purpose
Make sure only authorized people and processes reach the company's IT and OT systems and data, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All workforce members, vendor personnel, and client users (SL-1 and SL-2) with access to company systems, including the EMS, the ADMS and OMS, substation systems, the CIS, cloud and SaaS services, and BES Cyber System Information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director, Identity and Access Management | Runs the enterprise identity platform (SYS-08) and identity governance |
| Director, OT Security | Runs the OT identity domains, OT PAM, Intermediate Systems, and jump hosts |
| Managers and system owners | Approve access; complete certifications and CIP quarterly verifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events; personnel risk assessments |
| Director, NERC Compliance | Monitors CIP-004 timelines and evidence |

## 4. Policy statements
4.1 Every user and service must have a unique identity. Shared operator and vendor accounts are prohibited; where a device supports only a shared account, the individuals who know it must be recorded and the account vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted; access to high or medium impact BES Cyber Systems also needs completed CIP training and a current personnel risk assessment. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that would let one person both change and release switching orders, or both administer and audit a control system, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all privileged access, all cloud and SaaS administration, and all access to customer personal information. Privileged and OT remote users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 All Interactive Remote Access to OT must pass through an Intermediate System (EMS and medium impact substations) or an ADMS jump host, with encryption, MFA, and session recording. No other remote path, including vendor-installed appliances or modems, is permitted. (AC-17; MA-4; PR.AA-05)
4.6 Vendor remote access to OT must be off by default, enabled per approved window by the control center, and able to be disabled immediately. (AC-17; AC-2(11); PR.AA-05)
4.7 For individuals with CIP access, unescorted physical access and Interactive Remote Access must be removed within 24 hours of a termination action, and the revocation must be started by the termination action itself, not by the HR record update. (PS-4; AC-2; PR.AA-05)
4.8 For other workforce members, access must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.9 For reassignments and transfers, access no longer needed must be removed by the end of the next calendar day. (PS-5; AC-2; PR.AA-05)
4.10 Authorization records for CIP electronic and unescorted physical access must be verified each calendar quarter, and CIP privileges reviewed at least once every 15 calendar months; other critical system access must be certified quarterly. (AC-2; AC-6(7); PR.AA-05)
4.11 Provisioned access to BES Cyber System Information must be authorized before it is granted and verified at least once every 15 calendar months; BCSI may be stored only in approved repositories. (AC-3; AC-2; PR.DS-01)
4.12 Accounts inactive for 45 days must be disabled automatically, in the enterprise and OT domains. (AC-2(3); PR.AA-05)
4.13 Bulk or high-impact commands in business systems (for example, AMI bulk remote disconnect, full customer data export) must require a second approver and be limited by per-command thresholds. (AC-5; AC-6; PR.AA-05)

## 5. Standards and procedures under this policy
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard (IT and OT)
- PRC-02.1 Access Provisioning and Revocation Procedure (including CIP-004 timelines)
- PRC-02.2 Access Certification and CIP Quarterly Verification Procedure
- PRC-02.3 Privileged and Emergency Access Procedure (IT and OT PAM)

## 6. Compliance and enforcement
Compliance is monitored through identity governance reports, OT PAM records, the CIP quarterly verification, and the annual Internal Audit assessment (P07). Violations are handled under PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7 and `policy-hierarchy.md` section 5. CIP-004 and CIP-005 requirements cannot be excepted internally.

## 8. Related documents
POL-01; POL-04; STD-02.1 to STD-02.3; OT-STD-01; CIP Cyber Security Policy; P02 DOP SSP; P07 AC-2, AC-17, MA-4, and PS-4 results.
