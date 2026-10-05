# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director and the Group OT security director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-17, AC-17(1), IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory links | NERC CIP-004-7 R4 to R6 and CIP-005-7 R2 (TCC); CIP-003-9 Attachment 1 Sections 2, 3.1, and 6 (low impact substations); client CIP-013-2 Part 1.2.3 and 1.2.6 terms (Engineering Services); FAR 52.204-21(b)(1)(i)-(vi) |
| Division supplements | Electric Utility: TCC CIP access program, DOP operator roles, AMI bulk command approval. Gas Production: field SCADA accounts. Engineering Services: client access and client notices |

## 1. Purpose
Make sure only authorized people and processes reach group systems and data, and only to the extent their job requires. In OT, access control also protects public and crew safety.

## 2. Scope
All workforce identities, service accounts, administrator accounts, and vendor and affiliate identities in every division and in corporate shared services, for IT and OT systems, and the external identities (customers, royalty owners) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group OT security director | Runs SYS-G4 and its entitlement model |
| OT owners (Electric Utility distribution operations director; system operations director for the TCC; Gas Production SCADA and automation manager) | Approve who may reach their environment, and each remote session |
| Data owners | Approve access to Restricted data, including BCSI and CEII locations |
| Managers | Request and certify their staff's access every quarter |
| HR | Record joiners, movers, and leavers in the HR system the same day |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited, except for documented device limitations (for example, field devices that support one account), which require compensating controls and an owner. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege, and the owner must approve it. Access to BES Cyber System Information, CEII, and client BCSI is allowed only through authorized access lists for each designated storage location. (AC-3; AC-6; PR.AA-05; CIP-004-7 R4, R6)

4.3 MFA is required for all workforce access to IT systems and for all remote access into any OT environment. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03; CIP-005-7 R2 Part 2.3)

4.4 **OT remote access** must go only through SYS-G4, or, for the TCC, through its CIP-005 Intermediate System. Every vendor and affiliate session must be approved by the OT owner for that session and tied to a work order. **Standing remote access for vendors and affiliate staff is prohibited** after 2027-03-31. Sessions must be recorded, and vendor sessions must be checked for known or suspected malicious communications. (AC-17; AC-17(1); MA-4; CIP-003-9 Attachment 1 Section 6; CIP-005-7 R2 Parts 2.4-2.5)

4.5 **One environment per entitlement.** No account may reach more than one division's OT environment unless each OT owner has approved it for a named purpose. (AC-6; AC-6(5))

4.6 **Termination.** IT and OT access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. For CIP access, removals must also meet CIP-004-7 R5 and R6. Contractor accounts must expire automatically at the assignment end date. Engineering Services must notify clients of departures within the time each client contract sets. (PS-4; PS-7; AC-2(3))

4.7 Managers and owners must certify access every quarter, including privileged and service accounts. Inactive accounts must be disabled after 45 days. (AC-2; AC-6(7); CIP-004-7 R4 Parts 4.2-4.3)

4.8 Privileged access to IT systems must be granted just in time through PAM with session recording. OT administrator rights must be tiered by environment and function. (AC-6(5); PR.AA-05)

4.9 Accounts must lock after 10 failed attempts and workstations after 10 minutes idle. **Exception:** operator consoles at the TCC, DCC, and POC must alarm instead of locking, because a locked console can endanger operations; the operating floor's physical controls compensate. (AC-7; AC-11)

4.10 Each critical system must have sealed break-glass accounts, tested quarterly and reviewed after every use. (AC-2)

4.11 **Separation of duties for high-impact commands.** Bulk AMI remote disconnects above the threshold in the Electric Utility supplement, and switching orders, require two people. (AC-5)

4.12 Physical access to control centers, substations, the POC, and server rooms must be authorized by the owner, reviewed every quarter, and logged. (PE-2; PE-3; PR.AA-06; CIP-006-6 R1; CIP-003-9 Attachment 1 Section 2)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 and SYS-G4 common controls, division samples, CIP-004-7 quarterly verifications, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; the Electric Utility CIP-004-7 access management program; SYS-G4 operating procedures.
