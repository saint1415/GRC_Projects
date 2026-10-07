# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Director of IT and Cybersecurity (CySO) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 version) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents or changes to the Coast Guard rule |
| Implements (SP 800-53 Rev. 5) | IA-2, AC-2, AC-3, AC-5, AC-6, IA-2(1), IA-2(2), IA-2(8), AC-6(2), AC-6(5), PS-4, PS-5, AU-6, AC-7, AC-11, IA-5, CM-6, AC-17, MA-4, PE-3, PE-6, IA-8, SC-7, SC-7(5), AC-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-05, PR.AA-03, DE.CM-06, PR.AA-06, PR.IR-01 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.650(a)(1), 101.650(a)(2)-(3), 101.650(a)(4), 101.650(a)(5), 101.650(a)(6), 101.650(a)(7), 101.650(e)(3)(v), 101.650(f)(3), 101.650(g)(4), 101.650(h)(1)-(2), 101.650(i)(1) |
| Other requirements | 33 CFR 105.265(a)(7) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |
| Handling | Internal |

## 1. Purpose
Make sure only authorized people can reach terminal systems, data and equipment controllers, and only to the extent their job requires.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary staff and contractors) at Terminal 1, Terminal 2, the off-dock depot and the headquarters office, plus longshore labor and vendor technicians whenever they use company IT or OT. It covers every system and data set: the cloud landing zone, SaaS services, gate systems, crane and yard equipment controllers (OT), security systems, and systems that vendors operate or support for the company, including any terminal the company acquires, from the day it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers (terminal General Managers, Depot Manager, department heads) | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Starts onboarding, transfer and termination workflows on or before the effective day |
| Director of IT and Cybersecurity (CySO) | Provisions and removes IT access; runs the identity provider and privileged access management |
| Director of Maintenance and Engineering | Approves vendor remote sessions to OT; manages HMI and controller accounts |
| TOS Application Manager | Manages TOS roles, gate module accounts and the customs hold override role |
| Director of Port Security (T1 FSO) and T2 Security Lead (T2 FSO) | Revoke TWIC and PACS access; control keys and badges for gate server rooms and crane electrical houses |
| Workforce, longshore labor and vendors | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique named account. Shared or generic accounts are prohibited, including at the gate booths and on crane engineering workstations. Users must keep separate credentials on critical IT and OT systems. Where a device cannot support unique accounts (for example some HMIs), the exception must document compensating controls. (IA-2; AC-2; PR.AA-01; PR.AA-02; 101.650(a)(6))

4.2 Access must be role-based, least-privilege and approved by the user's manager before it is granted. TOS administration, billing and customs hold override rights must be separated, and every hold override needs a second approver. (AC-2; AC-3; AC-5; AC-6; PR.AA-05; 101.650(a)(5); 33 CFR 105.265(a)(7))

4.3 **MFA** is required for all identity provider users, the staff VPN, cloud administration, and any remote access to OT. Administrators must use phishing-resistant authenticators by 2027-03-31. Where MFA is not feasible, the compensating controls must be documented. Gate booth workstations use badge tap plus PIN. (IA-2(1); IA-2(2); IA-2(8); PR.AA-03; 101.650(a)(4))

4.4 **Privileged access.** No standing domain, identity provider or TOS administrator rights. Administrators must use separate administrator accounts and request just-in-time elevation through privileged access management; service account credentials must be vaulted and rotated. (AC-6; AC-6(2); AC-6(5); PR.AA-05; 101.650(a)(5))

4.5 **Termination and transfer.** HR must start the termination workflow on or before the last day. All accounts, including TOS gate module accounts and PACS badges at both terminals and the depot, must be disabled the same business day, or immediately for an involuntary termination. Transfers must lose prior roles within 5 business days. (PS-4; PS-5; AC-2; PR.AA-05; 101.650(a)(7))

4.6 Managers must review their staff's TOS roles and identity provider access every quarter. The Vice President, Terminal Operations must review all customs hold overrides each month. (AC-2; AC-6; AU-6; PR.AA-05; 101.650(a)(5))

4.7 Accounts must lock after 10 failed sign-in attempts on every password-protected IT system, including gate servers. Office and gate workstations must lock after 10 minutes idle. (AC-7; AC-11; PR.AA-03; 101.650(a)(1))

4.8 Default passwords must be changed before any IT or OT system or device is used, including during vendor commissioning. Passwords must be at least 14 characters and must not appear on the banned-password list. Devices that cannot meet this must use the strongest setting they support, recorded as an exception. (IA-5; CM-6; PR.AA-01; 101.650(a)(2)-(3))

4.9 **Emergency access.** Two break-glass administrator accounts must exist for each critical system (identity provider, cloud, TOS and gate servers), sealed and stored offline in the FSO safes at T1 and T2, tested quarterly, and used only when normal access is unavailable. The CySO reviews every use. (AC-2; PR.AA-05; 101.650(g)(4))

4.10 **Remote access.** Staff remote access is allowed only through the company VPN with MFA. All vendor and MSSP remote access must go through the privileged remote access service with named accounts, MFA, per-session approval by the system owner, and recording. Remote access to OT is off by default; each remotely accessible OT system needs a documented justification, and OT must not be connected to the internet unless explicitly required for operation. (AC-17; MA-4; PR.AA-05; DE.CM-06; 101.650(e)(3)(v); 101.650(f)(3))

4.11 Physical access to OT and related IT equipment (gate server rooms, crane electrical houses and network cabinets at both terminals and the depot) must be limited to authorized people and logged. The FSOs must review keys and badges each quarter. (PE-3; PE-6; PR.AA-06; 101.650(i)(1))

4.12 Customer portal accounts for trucking companies and cargo owners must be email-verified; their administrator accounts must use MFA by 2027-03-31; accounts inactive for 180 days must be disabled. (IA-8; AC-2; PR.AA-03; 101.650(a)(4))

4.13 **Network segmentation.** OT at each terminal must sit in an OT zone separated from IT by an industrial firewall that denies traffic by default and allows only documented flows. All connections between IT and OT must be logged and monitored. Security systems (PACS and CCTV) sit in their own zone. T2 must meet this by 2027-03-31. (SC-7; SC-7(5); AC-4; PR.IR-01; 101.650(h)(1)-(2))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination of employment or of a contract, depending on intent and harm. For longshore labor, the company may refuse further access to its systems and refer the matter to the hiring hall. Compliance is checked through the annual independent assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)), the annual Cybersecurity Plan audit once the Plan is approved (101.630(f)), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months. Where a Subpart F measure is not technically feasible (for example MFA on an HMI in a crane cab), the compensating control must be documented for the Cybersecurity Plan, as 101.650 allows.

## 7. Related documents
POL-01; POL-05; STD-01 OT security; STD-02 authenticator and privileged access; STD-04 vendor and remote access; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5, MA-4
