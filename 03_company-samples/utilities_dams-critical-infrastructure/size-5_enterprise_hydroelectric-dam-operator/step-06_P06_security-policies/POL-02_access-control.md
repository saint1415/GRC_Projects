# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management (OT identity domain: Director, OT Security) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions. CIP-003-9 R1 content is also approved by the CIP Senior Manager at least once every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-4, AC-5, AC-6, AC-17, AC-17(1), IA-1, IA-2, IA-2(1), IA-5, MA-4, PS-4, PS-5, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory basis | CIP-004-7 R4 to R6; CIP-005-7 R2 and R3; CIP-007-6 R5; CIP-003-9 Attachment 1 Sections 3 and 6; FERC Security Program Table 9.3a and 9.3b access control; Form 3 Q12 |

## 1. Purpose
Make sure only authorized people and processes reach the company's IT and OT systems and information, only to the extent their role requires, and that access ends promptly when it is no longer needed. For OT, access control is a safety control: it decides who can move a spillway gate.

## 2. Scope
All Cris Santos Company workforce members (employees, seasonal staff, contractors, and interns) at the headquarters, 14 offices, two Hydro Operations Centers, the Contract Operations Center, and all 46 developments in Georgia, Alabama, North Carolina, South Carolina, Tennessee, and Virginia, including the Piedmont developments from their acquisition date. Covers all systems and data: IT, OT (fleet SCADA, plant control, spillway and gate control, dam safety instrumentation and warning), cloud, colocation, SaaS, and systems that vendors operate for the company, and the services the company offers to external clients (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the enterprise identity platform and identity governance |
| Director, OT Security | Runs the OT identity domain, OT PAM, and the Intermediate Systems with OT Network Engineering |
| Director, Hydro Operations Center; plant managers | Approve OT access; HOC shift supervisors approve vendor sessions |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including contractors |
| Director, NERC Compliance | Quarterly CIP access verification evidence |
| Vice President, Integration Management Office | Brings Piedmont identities and access paths to fleet standards |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategories. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited except device and break-glass accounts vaulted in PAM, with the individuals authorized to use them listed. (IA-2; AC-2; PR.AA-01; PR.AA-03; PR.AA-05)
4.2 Access must be role-based, least privilege, and approved by the manager or system owner before it is granted. Electronic and unescorted physical access to CIP-scope systems must be authorized by need under CIP-004-7 R4.1. (AC-2; AC-6; PR.AA-01; PR.AA-05)
4.3 The gate-operate role, the logic-change role, and the approval of logic changes must be held by different people. Engineers must not approve their own changes. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all privileged access, and all cloud access. Interactive Remote Access to OT must go only through the Intermediate Systems, encrypted and with MFA. (IA-2(1); AC-17; PR.AA-01; PR.AA-03; PR.AA-05)
4.5 Electronic and unescorted physical access to CIP-scope systems must be removed within 24 hours of a termination action, and access no longer needed after a transfer by the end of the next calendar day. Other access must be removed the same business day. (PS-4; PS-5; GV.RR-04)
4.6 CIP access must be verified each calendar quarter and privileges every 15 calendar months; other critical systems must be certified quarterly by managers. (AC-2; PR.AA-01; PR.AA-05)
4.7 Vendor remote access to any OT asset, including low impact plants, must be approved per session, visible to the SOC while active, recorded, and able to be disabled at once. Always-on vendor connections are prohibited. (AC-17; AC-17(1); MA-4; PR.AA-05; PR.PS-03)
4.8 No path into OT may exist except the Intermediate Systems and one-way data diodes. Cellular modems, dial-up, or direct vendor links to OT devices are prohibited unless routed through the Intermediate Systems. (SC-7; AC-17; PR.IR-01; PR.DS-01; PR.AA-05)
4.9 Default passwords must be changed before any device is connected; passwords where single-factor is allowed must be at least 14 characters and changed at least every 15 calendar months where technically feasible. (IA-5; PR.AA-01; PR.AA-03)
4.10 The OT identity domain must not trust the corporate domain, and corporate devices must have no route into OT networks. (SC-7; AC-4; PR.IR-01; PR.DS-01; PR.DS-10)
4.11 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director, OT Security or the Director of Identity and Access Management. (AC-2; PR.AA-01; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard (Intermediate Systems; CIP-005-7 R2 and R3; CIP-003-9 Section 6)
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Verification Procedure (quarterly CIP verification)
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the NERC internal controls program, the annual Internal Audit assessment (P07), and access verifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. An exception cannot excuse a NERC CIP requirement.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HFCDMS SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
