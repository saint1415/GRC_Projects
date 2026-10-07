# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director and the Group OT security director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | 9 CFR 417.5(b) (attributable CCP entries); 21 CFR 121.135(a), 121.305(f) (Plant 6); PCI DSS Req. 7, 8 (Grocery Retail) |
| Division supplements | Meat Processing: HMI sign-in, formulation approval, OT engineering access. Food Distribution: telematics and DC automation accounts. Grocery Retail: CDE access and customer accounts |

## 1. Purpose
Make sure only authorized people and processes reach group IT and OT systems and data, and only to the extent their job requires, so that every change to product settings and every food safety record can be tied to a person.

## 2. Scope
All workforce identities, service accounts, administrator accounts, OT operator and engineering accounts, vendor and integrator accounts, and the external identities that group systems authenticate (loyalty customers, 3PL portal users).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (directory, sign-on, MFA, PAM, identity governance) as a common control |
| Group OT security director | Runs SYS-G5 (OT remote access gateway) and the OT account standard |
| Plant controls engineers | Maintain HMI, SCADA, and MES accounts and roles at their plant |
| Managers and data owners | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers (including agency workers) the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited. HMI operator sign-in must be named (badge and PIN is acceptable) at every plant by 2027-06-30; until then, shared HMI accounts are a recorded exception with compensating controls (supervisor sign-off of setpoint changes, CCTV). (IA-2; AC-2; PR.AA-01; 9 CFR 417.5(b))

4.2 Access must be role-based and least privilege. Formulation and cure or brine setpoint changes require an author and a different approver in MES or the recipe master library. Recipe library administration must be separate from cloud platform administration. (AC-3; AC-5; AC-6; PR.AA-05; 21 CFR 121.135(a))

4.3 MFA is required for all workforce access to IT systems and for all remote, administrator, and OT engineering access. Administrators and OT engineers must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS Req. 8.4)

4.4 **Service accounts** must have a named owner, be managed in identity governance, and, if privileged, be vaulted in PAM with interactive sign-in disabled. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access, including badges, must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Agency worker and contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2)

4.6 Managers and data owners must certify access every quarter, including privileged, OT engineering, and service accounts. (AC-2; PR.AA-05)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 IT accounts must lock after 10 failed attempts and workstations after 10 minutes idle. HMIs are excluded from lockout because operator lockout during a process upset is a safety risk; HMI sessions must be bound to a named operator once 4.1 is in place. (AC-7; AC-11)

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 **Remote and vendor access to OT** must go through SYS-G5 with named accounts, MFA, approval, and recording. Always-on vendor VPNs, vendor remote tools outside SYS-G5, and cellular modems on control systems are prohibited. Existing ones at Plants 2 and 5 and three DCs must be removed by 2026-12-31 (DCs by 2027-03-31). (AC-17; MA-4)

4.11 **External identities.** Loyalty and online customer accounts must offer MFA and use risk-based step-up for sensitive actions. 3PL portal users must use MFA. Telematics portal users must be named. (IA-8; IA-2; PR.AA-03)

4.12 **Default credentials** must be changed before any device, including OT devices, is connected to a group network. (IA-5; CM-6; PCI DSS Req. 2.2)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 and SYS-G5 common controls, division samples, quarterly certification results, and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. The HMI exception in 4.1 expires 2027-06-30.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 and SYS-G5 (P02).
