# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | VP Operations |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.230(a)(8), voluntary benchmark); SP 800-82 Rev. 3 sec. 6.2.1 and 6.2.10 |

## 1. Purpose
Make sure only authorized people can reach company systems and the process controls, only to the extent their job requires, and that every change to the process can be traced to a person.

## 2. Scope
All workforce members and contractors. All systems: office IT, SaaS, the cloud tenant, and OT (DCS, SIS, PLCs, historian, OT network, and loading rack cards).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day, including OT accounts and rack cards |
| IT Manager | Provisions and removes IT, SaaS, cloud, and remote access |
| Controls Engineer | Provisions and removes DCS, SIS, PLC, and historian accounts; reviews OT access quarterly |
| Shift Supervisors | Approve each integrator remote session on their shift |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, **including on DCS operator stations and HMIs**. Shared or generic accounts are prohibited. Where a device cannot support unique accounts, the exception must name the compensating controls. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the user's manager (for OT, by the Controls Engineer). DCS roles are operator, supervisor, and engineer. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, the ERP, the identity provider, the cloud console, and all remote access. Administrators and any remote session that can change DCS or SIS configuration must use phishing-resistant authenticators. (IA-2(1); PR.AA-03)
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT and the Controls Engineer must disable all access **the same business day**, including DCS and SIS accounts and loading rack driver cards. Involuntary terminations are disabled immediately. (PS-4; AC-2)
4.5 Managers must review their staff's access every quarter. The Controls Engineer must review all DCS, SIS, historian, and rack card accounts every quarter. (AC-2; AC-6)
4.6 **Remote access to OT.** Remote access to OT is allowed only through the company remote access gateway in the OT DMZ. It must use named accounts, MFA, and per-session approval by the Shift Supervisor, and every session must be recorded. Sessions end when the work is done. Always-on remote tools, and remote tools installed on OT workstations, are prohibited. Vendors must sign the rules of behavior before their first session. (AC-17; MA-4; PS-7; PR.AA-05)
4.7 **Safety tailoring.** Operator HMIs must not lock the screen or lock out accounts after failed logins, so operators are never locked out during an upset. The staffed, badge-controlled control room is the compensating control. The EWS and all other workstations lock after 10 minutes idle and lock accounts after 5 failed attempts. (AC-7; AC-11)
4.8 **SIS access.** SIS engineering software may be installed only on the dedicated SIS laptop, kept locked by the Controls Engineer. The SIS keyswitch stays in run. Moving it to program needs an approved MOC or proof test work order. Returning it to run needs a second person to verify, and the Shift Supervisor checks it each shift. (AC-3; CM-5; PR.AA-05)
4.9 Passwords must be at least 14 characters where the system supports it. Default passwords must be changed before a device is connected, including PLCs and network devices. (IA-5; PR.AA-03)
4.10 Physical access to the control room, server room, and engineering office is limited by badge to authorized staff. Visitors and contractors are escorted. (PE-3; PR.AA-06)
4.11 Two-person approval is required for master recipe releases and for hydrogen peroxide inventory adjustments in the ERP. (AC-5; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Compliance is checked through the annual control assessment (P07) and the quarterly access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the CEO for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT remote access procedure (due 2026-12-31); integrator rules of behavior; P02 control statements AC-2, AC-17, IA-2, CM-5
