# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager (proposed CySO) |
| Approved by | General Manager |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.650(a)(1)-(7), 101.650(e)(3)(v), 101.650(f)(3), 101.650(i)(1) |

## 1. Purpose
Make sure only authorized people can reach terminal systems and equipment controllers, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff and contractors), plus longshore labor and vendor technicians whenever they use company IT or OT. Covers every system and data set at the Florida terminal, including the cloud tenant, SaaS services, crane and yard equipment controllers (OT), and systems that vendors operate or support for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager, Maintenance Manager and other managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Specialist | Opens onboarding, transfer and termination tickets on or before the effective day |
| IT Manager (proposed CySO) | Provisions and removes IT access; runs the identity provider; approves vendor remote sessions to IT |
| Maintenance Manager | Approves vendor remote sessions to OT; manages HMI and controller accounts |
| Security and Safety Manager (FSO) | Revokes TWIC and PACS access; controls keys to the gate server room and crane electrical houses |
| Workforce and longshore labor | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique named account. Shared or generic accounts are prohibited, including at the gate booths. Users must keep separate credentials on critical IT and OT systems. A documented exception must have compensating controls. (IA-2; AC-2; PR.AA-01; 101.650(a)(6))
4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. Administrators must use a separate administrator account for administrative work. TOS administrator and customs hold override rights must be kept to the minimum number of people. (AC-2; AC-3; AC-6; PR.AA-05; 101.650(a)(5))
4.3 **MFA** is required for all users of the identity provider (TOS, email and SaaS), the staff VPN, cloud administration, and any remote access to OT. Administrators must use phishing-resistant authenticators. Where MFA is not feasible (for example HMIs in crane cabs), the compensating controls must be documented. Gate booth workstations use badge tap plus PIN. (IA-2(1); IA-2(2); PR.AA-03; 101.650(a)(4))
4.4 **Termination.** HR must open a termination ticket on or before the last day. IT must disable the user's accounts the same business day, or immediately for an involuntary termination. The FSO must revoke PACS access on the same day. (PS-4; AC-2; 101.650(a)(7))
4.5 Managers must review their staff's TOS roles and identity provider access every quarter. The Operations Manager must review every use of the customs hold override each month. (AC-2; AC-6)
4.6 Accounts must lock after 10 failed sign-in attempts on every password-protected IT system, including the VPN and gate servers. Office and gate workstations must lock after 10 minutes idle. (AC-7; AC-11; 101.650(a)(1))
4.7 Default passwords must be changed before any IT or OT system or device is used, including during commissioning by a vendor. Passwords must be at least 12 characters and must not appear on the banned-password list. Devices that cannot meet this must use the strongest setting they support, recorded as an exception. (IA-5; 101.650(a)(2)-(3))
4.8 **Emergency access.** Two break-glass administrator accounts must exist, sealed and stored offline in the FSO safe, tested quarterly, and used only when the identity provider is unavailable. The CySO reviews every use. (AC-2)
4.9 **Remote access.** Staff remote access is allowed only through the company VPN with MFA. Vendor and MSP remote access must use named accounts with MFA, be approved per session by the system owner, and be recorded. Remote access to OT is off by default; each remotely accessible OT system needs a documented justification. OT must not be connected to the internet unless explicitly required for operation. (AC-17; MA-4; 101.650(e)(3)(v); 101.650(f)(3))
4.10 Physical access to OT and related IT equipment (the gate server room, crane electrical houses and network cabinets) must be limited to authorized people and logged. Keys and badges must be reviewed quarterly by the FSO. (PE-3; 101.650(i)(1))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or of a contract, depending on intent and harm. For longshore labor, the company may refuse further access to its systems and refer the matter to the hiring hall. Compliance is checked through the annual control assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)) and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. Where a Subpart F measure is not technically feasible, the compensating control must be documented for the Cybersecurity Plan.

## 7. Related documents
POL-01; POL-05; access review procedure (due 2026-10-31); P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5
