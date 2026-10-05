# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO, with the Group OT Security Director for OT access |
| Approved by | Group CISO, after board risk committee review |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-17, AC-17(1), IA-1, IA-2, IA-2(1), IA-2(5), IA-5, MA-4, PE-3 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | RBPS 8 (voluntary); 33 CFR 101.650(a) and (f)(3) (Terminal T1); 40 CFR 68.69(d) and 68.87 (control over entrance by contractors); 49 CFR 395.22(b) (ELD accounts) |

## 1. Purpose
Make sure only authorized people, devices, and services can reach group information and control systems, with the least privilege needed, and that every change to a control system can be traced to a person.

## 2. Scope
All group IT and OT systems, including plant and terminal control systems, safety instrumented systems, the OT remote access gateway, telematics and ELDs, and SaaS services operated for the group.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Operates SYS-G1 (SSO, MFA, PAM, identity governance) |
| Group OT Security Director | Operates the OT remote access gateway and sets OT access rules |
| Plant controls engineering managers; Terminal T1 Terminal Manager | Approve OT accounts and remote sessions for their site; manage local OT accounts |
| Plant shift superintendents | Approve each remote engineering session to their plant |
| System and data owners | Approve access and certify it each quarter |
| Hazmat Transport Director of Fleet Technology | Manages ELD and telematics accounts |

## 4. Policy statements
4.1 Every user must have a unique account. **Shared accounts are prohibited**, including integrator team accounts, shared engineering accounts, and shared ELD support accounts. The only exception is a sealed emergency account for a control system, logged when opened and changed after each use. (AC-2; IA-2; IA-2(5); 49 CFR 395.22(b)(2)(ii))

4.2 Access must be based on job need and least privilege and approved by the system owner. OT engineering rights are granted per plant or terminal, not group-wide. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access to SYS-G1 applications and all remote access. Phishing-resistant authenticators are required for administrators and, from 2027-03-31, for every remote session that can change DCS, SIS, or terminal automation configuration. (IA-2(1); IA-2(2); PR.AA-03; 33 CFR 101.650(a)(4))

4.4 Privileged IT and OT domain administrator credentials must be vaulted in PAM and checked out just in time, with session recording. Privileged accounts must be separate from everyday accounts. (AC-6(5); AC-6(2))

4.5 Access must be removed within 4 hours of termination for SYS-G1 accounts and within 24 hours for local OT accounts, and within the same window for contractor personnel when their engagement ends. Access must be certified each quarter. (AC-2(3); PS-4; 33 CFR 101.650(a)(7))

4.6 **OT remote access** is allowed only through the group OT remote access gateway into a site's OT DMZ. Every session must use a named account, be approved by the site (the shift superintendent at a plant; the control room operator at Terminal T1), be recorded, and end when the work ends. **Standing connections and third-party remote access tools are prohibited.** (AC-17; AC-17(1); MA-4; 33 CFR 101.650(f)(3))

4.7 Integrator and vendor accounts must have a group sponsor at the site, expire after 90 days unless renewed, and be used only by the named person. (AC-2; IA-8; 40 CFR 68.87(b)(4))

4.8 **Safety exceptions.** Operator HMIs must not lock out or log out an operator for failed attempts or inactivity. The staffed, badge-controlled control room is the compensating control. Engineering workstations and all remote access must lock and lock out normally. (AC-7; AC-11; AC-2(5))

4.9 **Safety instrumented systems.** SIS program changes require named SIS engineering accounts, the keyswitch in program, and two-person verification. The SIS engineering workstation must not be reachable from the DCS network or the gateway. (AC-3; CM-5; SC-7(21))

4.10 **Default passwords** must be changed before any IT or OT device is used. Where not feasible, compensating controls must be documented. Passwords must meet the group authenticator standard (minimum 14 characters where supported). (IA-5; IA-5(1); 33 CFR 101.650(a)(2)-(3))

4.11 Physical access to control rooms, server rooms, SIS cabinets, and terminal OT equipment is limited to authorized personnel by badge (and TWIC at Terminal T1), monitored, and logged. (PE-3; PE-6; 33 CFR 101.650(i)(1))

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (AC-2, AC-17, MA-4, IA-2, IA-5) and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may permit a standing remote connection into a plant or terminal OT network.

## 7. Related documents
POL-01; group OT security standard (section 4, access); group authenticator standard; division supplements; 33 CFR 101.650(a); 49 CFR 395.22.
