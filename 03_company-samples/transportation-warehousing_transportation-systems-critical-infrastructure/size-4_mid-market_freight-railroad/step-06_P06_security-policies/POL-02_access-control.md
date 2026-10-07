# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Cybersecurity Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | C-TRANSPORTATION-R01 (SD 1580/82-2022-01E III.C.1 to III.C.6) |
| Supporting standards | STD-06 Authenticator, privileged, and shared account standard; STD-04 Field OT security standard |

## 1. Purpose
Make sure only authorized people and systems can reach company systems, including the dispatch, PTC, and field systems that control train movement, and only to the extent their job requires.

## 2. Scope
All workforce members, vendors, and service accounts with access to company systems: the directory and identity provider, CAD/CTC consoles and servers, the PTC back office and administration workstations, CTC field communication controllers, radio gateways, detectors and crossing monitors, cloud accounts, the TMS, the ERP, and crew tablets.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and department heads | Request and approve access; complete quarterly access reviews for their staff |
| System owners (Director of Network Operations for CAD/CTC; PTC Program Manager for the BOS; Director of Signals and Communications for field devices; Director of Customer Service and Car Management for the TMS) | Approve role design; review application roles and privileged rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| Director of Information Technology | Runs the directory, identity provider, and provisioning; owns break-glass accounts |
| Cybersecurity Manager | Runs privileged access management (PAM) and vendor access; reviews privileged activity; owns this policy |
| Workforce | Protect credentials; never share accounts or passwords |

## 4. Policy statements
4.1 Every user must have a unique, named account. Shared accounts are allowed only where the device cannot support named accounts and the account is critical for operations (for example some field controller maintainer accounts). Each shared account must be on the shared account inventory, vaulted in PAM, and released per session. Shared dispatcher logins are prohibited. (IA-2; AC-2; PR.AA-01; SD III.C.4.a)
4.2 **Shared account passwords** must be changed whenever a person who knew them leaves the company or no longer needs access, and at least every 12 months. (IA-5; AC-2; SD III.C.4.b)
4.3 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. No person may hold both field signal maintainer rights and CAD/CTC administrator rights, and dispatchers may not hold administrator rights on the system they dispatch on. (AC-2; AC-3; AC-5; AC-6; PR.AA-05; SD III.C.3)
4.4 **MFA** is required for all remote access, email, cloud consoles, the TMS, the ERP, and the PAM jump hosts. Administrators must use phishing-resistant authenticators (security keys). Finance, HR, and IT users must move to phishing-resistant MFA by 2027-03-31. Where an OT component cannot support MFA (for example dispatch consoles at shift handover, field controllers, and onboard units), the compensating controls documented in the CIP apply and must be listed in STD-06 with a completion timeframe. (IA-2(1); IA-2(2); PR.AA-03; SD III.C.1.b and III.C.2)
4.5 **Termination.** HR must record the termination on or before the last day. Directory and identity provider access must be disabled automatically that day, or immediately for involuntary terminations. Crew tablet, TMS, CAD/CTC, BOS, and badge access must be removed within 24 hours, and shared passwords the person knew must be changed under 4.2. (PS-4; AC-2)
4.6 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.7 **Access reviews.** Managers must review their staff's access each quarter. System owners must review CAD/CTC, BOS, TMS application roles and all privileged rights each quarter. Domain trust relationships must be reviewed each year. (AC-2; AC-6; SD III.C.5)
4.8 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through PAM, with sessions recorded. No vendor or service account may hold standing domain administrator rights. (AC-6(2); AC-6(5))
4.9 Accounts lock after 10 failed sign-in attempts. Office workstations lock after 10 minutes idle. Dispatch consoles lock only at shift handover or when the dispatcher signs out, because an automatic lock could interrupt movement authority; this is a documented exception under the CIP. (AC-7; AC-11)
4.10 **Emergency access.** Break-glass accounts for the identity provider, directory, cloud organization, PAM, CAD/CTC, and BOS must be stored sealed and offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Cybersecurity Manager within 1 business day. (AC-2)
4.11 Passwords must be at least 14 characters and not on the banned-password list. They are reset only on evidence of compromise or under 4.2, consistent with NIST SP 800-63. Default vendor credentials must be changed before any device connects to a company network, including field modems and crossing monitors. (IA-5; SD III.C.1.a)
4.12 **Vendor remote access** must use named accounts with MFA through the PAM jump host, be approved per session by the system owner, be recorded, and end when the work is complete. Always-on vendor connections (site-to-site VPNs, cellular modems with inbound access) are prohibited. (AC-17; MA-4; PR.AA-05)
4.13 **Physical access to field equipment.** Signal housings, tower shelters, and locomotive PTC housings must be locked or sealed (49 CFR 236.3; SD III.C.6), keys must be controlled under STD-11, and badge access to the NOCs and data centers must be reviewed quarterly. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.11. Compliance is checked through the annual independent assessment (P07), the quarterly access reviews, and the CAP.

## 6. Exceptions
Exceptions follow POL-01 statement 4.9. An exception that touches a CIP measure needs TSA approval of a CIP amendment.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; STD-11; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5; P07 findings for AC-02, AC-05, AC-06, AC-17, IA-02, IA-05, MA-04, PS-04; SD 1580/82-2022-01E Section III.C
