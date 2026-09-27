# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager (business IT) and SCADA Engineer (OT) |
| Approved by | President |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-17, IA-2, IA-2(1), IA-5, MA-4, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Pipeline safety link | 49 CFR 192.631(b)(5) (who may direct or supersede a controller) |

## 1. Purpose
Make sure only authorized people can reach company systems, especially the systems that control the pipeline, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company employees, contractors, and suppliers with access to company systems, at HQ and the Gas Control Center, Compressor Station 1, the field offices, and all field sites. It covers business IT, OT (SCADA, field devices, telecommunications, and the IT/OT DMZ), the cloud tenant, and SaaS services, including systems that suppliers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day |
| IT Manager | Provisions and removes business IT and cloud access |
| SCADA Engineer | Provisions and removes OT access; enables supplier remote sessions |
| Gas Control Manager | Approves all SCADA controller and administrator access |
| All personnel | Protect credentials; never share accounts except as 4.2 allows |

## 4. Policy statements
4.1 Every user must have a unique account on business systems, the cloud tenant, the SCADA application, SCADA servers, and the jump host. (IA-2; AC-2; PR.AA-01)
4.2 **Shared accounts.** The only permitted shared account is the Windows display login on HMI consoles, and it is allowed only because the consoles must never lock a controller out. It must be limited to the consoles, be unusable for remote sign-in, and have its password changed whenever someone with knowledge of it leaves. Each controller must still sign in to the SCADA application with an individual account. Shared administrator accounts are prohibited. (AC-2; IA-5; PR.AA-01)
4.3 Access must be role-based, least-privilege, and approved by the user's manager. OT access also needs the Gas Control Manager's approval. Only controller-role accounts may send commands to field devices. (AC-3; AC-5; AC-6; PR.AA-05)
4.4 MFA is required for email, business SaaS, the cloud console, business VPN, and every remote or administrative connection into the DMZ or OT. Where MFA is not used on control room HMI consoles, the badge-controlled, staffed control room is the documented compensating control. (IA-2(1); PR.AA-03)
4.5 **Supplier remote access** to OT must:
- use a named account with MFA;
- be enabled by the SCADA Engineer for each approved ticket and disabled when the session ends;
- be recorded;
- go through a jump host that company staff do not share.

The controller on duty must be told before any supplier session that can change live SCADA displays or points. (AC-17; MA-4; 192.631(b)(5))
4.6 **Termination.** HR must open a termination ticket on or before the last day. Business and OT access must be disabled the same business day, or immediately for involuntary terminations. Any shared password the person knew must be changed within 24 hours. (PS-4; AC-2)
4.7 Managers must review their staff's access every quarter. The SCADA Engineer and Gas Control Manager must review all OT accounts every quarter. (AC-2; PR.AA-05)
4.8 **Passwords.** Passwords must be at least 14 characters and must not be on the banned list. OT passwords must be changed at least every 12 months. Where a device cannot meet this, the mitigation and timeline must be documented. Manufacturer default passwords must be changed before any device is connected. (IA-5; PR.AA-01)
4.9 Physical access to the Gas Control Center and the backup control room is by badge only. Visitors must be escorted and logged. Keys to field sites must be tracked in a key log. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07) and the access reviews in this policy.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-01; POL-05; OT access procedure; control room management manual; P02 control statements AC-2, AC-17, IA-2, MA-4
