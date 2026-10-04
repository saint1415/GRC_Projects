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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions or Cybersecurity Plan amendments |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-7, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-5(1), MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| 33 CFR Part 101 Subpart F | 101.650(a)(1)-(7); 101.650(e)(3)(v); 101.650(f)(3) |

## 1. Purpose
Make sure only authorized people, devices and processes reach the company's IT and OT, only to the extent their role requires, and that access ends promptly when it is no longer needed. This policy implements the account security measures in 33 CFR 101.650(a) and the remote access measures in 101.650(e)(3)(v) and (f)(3).

## 2. Scope
All Cris Santos Company employees, contractors, temporary staff and interns at headquarters, the enterprise planning center and the 8 terminals (T-01 to T-08) in Florida, Georgia, South Carolina and Texas, including acquired terminals from their acquisition date. Longshore workers ordered through the hiring halls and OEM and vendor technicians are covered when they use company IT or OT, through the hiring hall arrangements and their contracts. Covers all IT and OT systems and data, including cloud, colocation, SaaS, cranes and automation, gate systems, and the services the company provides to outside customers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05), PAM and identity governance |
| Director of OT Engineering | OT accounts, OEM access and compensating controls for OT devices |
| Managers, system owners and Terminal General Managers | Approve access; complete quarterly certifications |
| Chief People Officer | Timely joiner, mover and leaver events |
| Vice President, Integration Management Office | Brings acquired terminals onto the identity platform |
| SL-2 client administrators | Manage their own users under the client agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user, device and service must have a unique identity. Shared accounts are prohibited on IT and OT, including HMIs. Where an OT device cannot support individual accounts, the compensating control must be documented in STD-01.8 and the Cybersecurity Plan. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person override a customs hold and release the same container at the gate, or create and pay a vendor, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for every password-protected IT system, all remote access, all cloud and administrative access and all SL-2 client access. Privileged users must use phishing-resistant authenticators. Remotely accessible OT must use MFA or documented compensating controls. (IA-2(1); IA-2(2); AC-17; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Workforce accounts inactive for 60 days, and SL-2 client accounts inactive for 90 days, must be disabled automatically. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter; SL-2 client administrators must attest to their users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access, including TOS vendor support accounts, must be granted just in time through PAM, recorded and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and OEM remote access to IT or OT must go through the vendor access gateway with per-session approval, MFA and recording. Always-on tunnels and modems are prohibited, and every remotely accessible OT system must have a documented justification. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any IT or OT system is used. Where that is not feasible, the compensating control must be documented. (IA-5; PR.AA-01)
4.11 Password strength and automatic lockout after repeated failed logins must be enforced on every system that can support them, as set in STD-02.2. (IA-5(1); AC-7; PR.AA-01)
4.12 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the CISO. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 OEM Remote Session Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications and, once the Cybersecurity Plans are approved, the annual Plan audits. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ETOP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; the Cybersecurity Plans and FSPs (SSI).
