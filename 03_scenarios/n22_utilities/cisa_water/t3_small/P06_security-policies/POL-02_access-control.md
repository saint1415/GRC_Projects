# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, AC-17(1), IA-2, IA-2(1), IA-5, MA-4, PS-4, CM-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory basis | SDWA section 1433 automated-systems security, 42 U.S.C. 300i-2(a)(1)(A)(ii); ERP cybersecurity strategies, (b)(1) |

## 1. Purpose
Make sure only authorized people can reach company systems, and especially the systems that control water treatment, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and interns) at WTP-1, WTP-2, the administration office, and remote sites. Covers all systems and data, including operational technology (the Water Treatment SCADA System, PLCs, RTUs, and telemetry) and systems that service providers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| Chief Plant Operators | Approve each vendor remote session to OT; review HMI accounts quarterly |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day, listing OT accounts |
| IT Manager | Provisions and removes business and remote access; runs the identity provider |
| SCADA and Instrumentation Technicians | Provision and remove HMI, PLC, and device accounts |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account, including on HMIs and the engineering workstation. Shared or generic accounts are prohibited. Documented exceptions must have compensating controls. (IA-2; AC-2)
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. HMI roles are view, operate, and engineer. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, the identity provider, cloud administration, the CIS, and **all remote access to OT**. Administrator and integrator accounts must use phishing-resistant authenticators. (IA-2(1); PR.AA-03)
4.4 **Remote access to OT** is allowed only through the company-controlled remote access gateway. Each vendor session must be requested in advance, approved by the on-duty Chief Plant Operator, time-limited, and recorded. Always-on remote access tools are prohibited. (AC-17; AC-17(1); MA-4)
4.5 **Termination.** HR must open a termination ticket on or before the last day, listing any OT, VPN, and device accounts. IT and the SCADA technicians must disable all access **the same business day**, or immediately for involuntary terminations. (PS-4; AC-2)
4.6 Managers must review their staff's access every quarter. The Chief Plant Operators review HMI and VPN accounts; the Customer Service and Billing Manager reviews CIS roles. (AC-2; AC-6)
4.7 Business accounts lock after 10 failed sign-in attempts, and workstations lock after 10 minutes idle. Operator HMIs in staffed control rooms are exempt from lockout and screen lock so alarms are always visible; failed HMI logons must be logged instead (SP 800-82r3 OT overlay). (AC-7; AC-11)
4.8 Default and commissioning passwords must be changed before a device is connected, and stored in the company password vault. Passwords must be at least 14 characters and not on the banned-password list. (IA-5)
4.9 PLC key switches must stay in RUN. Program mode requires the Operations Manager's approval, a change record, and a return to RUN when the work ends. (CM-5)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT remote access procedure (due 2026-12-31); P02 control statements AC-2, AC-17, MA-4
