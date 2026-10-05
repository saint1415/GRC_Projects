# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Security Manager (with the SCADA and OT Engineering Manager for OT) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-2, PE-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | TSA SD Pipeline-2021-02G Section III.C (C.1 to C.5); 49 CFR 192.631(b)(5) |
| Supporting standards | STD-04 OT remote access and field device standard; STD-06 Authenticator and privileged access standard |

## 1. Purpose
Make sure only authorized people can reach company systems, especially the Critical Cyber Systems that control the pipeline, and only to the extent their job requires.

## 2. Scope
All employees, contractors, authorized representatives, and managed service providers with access to company systems, at all sites. It covers business IT, OT, the cloud landing zone, and SaaS services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Opens onboarding, transfer, and termination tickets the same day; the ticket drives business IT and OT removal |
| IT Director | Provisions and removes business IT and cloud access |
| SCADA and OT Engineering Manager | Provisions and removes OT domain, SCADA, station, and field device access |
| OT Security Engineers | Run the remote access gateway, privileged account reviews, and the password reset schedule |
| Director of Gas Control | Approves all SCADA controller, supervisor, and engineering roles; is notified before any change that affects what a controller sees or controls |
| Shift supervisor on duty | Approves each vendor remote session to OT |
| All personnel | Protect credentials; never share accounts except as 4.2 allows |

## 4. Policy statements
4.1 Every user must have a unique account on business systems, the cloud, the remote access gateway, the OT domain, the SCADA application, and station HMIs. (IA-2; AC-2; PR.AA-01; SD 02G III.C)
4.2 **Shared accounts** are allowed only where operationally necessary and approved by the Director of Gas Control and the Security Manager, and must be listed in the TSA plan with the reason. Each must be limited to the device it serves, unusable for remote sign-in, and limited to operator rights. Its password must be changed within 24 hours after anyone who knew it no longer needs access. Shared administrator accounts are prohibited. The shared station logins at Compressor Stations 2, 4, and 5 must be replaced with individual logins by 2027-06-30. (AC-2; IA-5; PR.AA-01; SD 02G III.C.4)
4.3 Access must be role-based, least-privilege, and approved by the user's manager. OT roles also need the Director of Gas Control's approval. Only controller and supervisor roles may send commands to field devices. No person may approve their own SCADA change. (AC-3; AC-5; AC-6; PR.AA-05; SD 02G III.C.3)
4.4 OT privileged accounts must be named, used only from engineering workstations or the remote access gateway, and limited to 4 OT domain administrators. They must be reviewed every quarter. (AC-6(5); PR.AA-05)
4.5 MFA is required for business IT, the cloud, the remote access gateway, and every privileged logon to OT. Where MFA is not used on control room HMIs (49 CFR 192 control rooms), the staffed, badge-controlled control room with CCTV is the compensating control, documented in the TSA plan. Station HMIs must have documented compensating controls until individual logins are in place. (IA-2(1); PR.AA-03; SD 02G III.C.2)
4.6 **Remote access to OT** is allowed only through the remote access gateways at the GCC and BCC, with:
- a named account and MFA;
- approval of each vendor session by the shift supervisor on duty, for a stated purpose and time window;
- session recording and SIEM logging;
- notice to the controller on duty before any session that can change live SCADA displays, points, or station settings.

Any other path into OT, including modems and cellular devices installed by suppliers, is prohibited and must be removed when found. (AC-17; MA-4; PR.AA-05; SD 02G III.B.1.b, III.C; 192.631(b)(5))
4.7 **Termination and transfer.** HR must open the ticket on or before the last day. Business and OT access must be removed within 1 business day, and immediately for involuntary terminations. On transfer, roles not needed in the new job must be removed within 5 business days. (PS-4; PS-5; AC-2; SD 02G III.C.4.b)
4.8 Managers must review their staff's access every quarter. The SCADA and OT Engineering Manager and the Director of Gas Control must review all OT and field device accounts every quarter. (AC-2; PR.AA-05)
4.9 **Passwords and resets.** Passwords must be at least 14 characters and not on the banned list where the system allows. OT account passwords must be reset at least every 12 months and field device passwords at least every 24 months, as the TSA plan schedules. Where a component cannot be reset on schedule, the mitigation and a completion timeframe must be documented, and TSA must be told if the timeframe will be missed. Manufacturer default passwords must be changed before any device is connected. (IA-5; PR.AA-01; SD 02G III.C.1)
4.10 The OT domain must have no trust with the business domain. Any new domain trust needs Security Manager approval and is reviewed every year. (AC-3; SD 02G III.C.5)
4.11 Physical access to control rooms, server rooms, and station control buildings is by badge only. Control room access lists are approved by the Director of Gas Control and reviewed quarterly. Visitors must be escorted and logged. (PE-2; PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors and authorized representatives, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07), quarterly access reviews, and TSA inspections.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the right authority under POL-01 section 4.4, and expire within 12 months.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; OT access procedure (OT-PR-02); control room management manual; P02 control statements AC-2, AC-17, IA-2, IA-5, MA-4
