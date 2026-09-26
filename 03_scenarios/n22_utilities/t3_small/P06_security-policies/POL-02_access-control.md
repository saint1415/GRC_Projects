# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | President and CEO; CIP Senior Manager for statements 4.6, 4.7, 4.8, and 4.10 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-04), and after major changes or incidents. CIP topics at least every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| NERC and other | CIP-003-9 R2 Attachment 1 Sections 2, 3, and 6 |

## 1. Purpose
Make sure only authorized people and systems can reach company systems, substations, and data, and only as far as their job requires. Access to OT gets the strictest rules, because a wrong command can cut power or endanger crews.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every company site, including substations and crew yards. Covers all company systems and data: corporate IT, the Distribution Operations Platform, the low impact BES Cyber Systems at Substation N and Substation E, the cloud tenant, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets the same day; collects keys and badges |
| IT Manager | Provisions and removes IT access; runs the identity provider and firewalls |
| SCADA/OT Administrator | Provisions and removes OT accounts; runs the jump host |
| Manager of Engineering and Protection | Approves substation physical access and relay access |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account on every system, including SCADA HMIs and the jump host. Shared or generic accounts are prohibited. The shared HMI operator accounts must be replaced by 2026-12-31. Until then, the DCC operator log must record who is at each console. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least-privilege, and approved by the user's manager before it is granted. SCADA administrator rights are limited to the SCADA/OT Administrator and the OT technician. (AC-2; AC-3; AC-6; PR.AA-05)

4.3 MFA is required for email, the CIS, the OMS, the AMI head-end, the cloud console, the VPN, and every remote path into the OT network, including the jump host. Cloud and OT administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Termination.** HR must open a termination ticket on or before the last day. IT and the SCADA/OT Administrator must disable all access the same business day, or immediately for involuntary terminations. Keys and badges must be collected before final pay is released. (PS-4; AC-2)

4.5 Managers must review their staff's access every quarter. The SCADA/OT Administrator must review SCADA, OT domain, and jump host accounts every quarter with the Manager of System Operations. (AC-2; AC-6; PR.AA-05)

4.6 **Vendor remote access.** Vendor electronic remote access to OT, including to Substation N and Substation E, must:
- use named vendor accounts with MFA through the jump host only;
- be disabled by default, and enabled by the DCC for a stated purpose and end time;
- be recorded, so the company can always tell which vendor had access to what and when;
- be disabled at once by the DCC if misuse is suspected;
- be monitored for known or suspected malicious communications.

(AC-17; MA-4; SI-4; PR.AA-05; CIP-003-9 Attachment 1 Section 6)

4.7 **Electronic access to low impact assets.** Routable communication into or out of Substation N and Substation E must be limited to the flows documented as necessary, enforced by the substation gateway. The access lists must be checked after every change and every commissioning, and reviewed at least annually. (SC-7; AC-4; CM-6; PR.IR-01; CIP-003-9 Attachment 1 Section 3.1)

4.8 Dial-up connectivity to relays or substation devices is prohibited. If a device ever needs it, it must be authenticated, approved by the CIP Senior Manager, and recorded. (AC-17; CIP-003-9 Attachment 1 Section 3.2)

4.9 Passwords must be at least 14 characters and must not be on the banned-password list. Relay and gateway passwords must be unique per substation and changed after every contractor visit. (IA-5)

4.10 **Physical access.** Substation control houses and the DCC must be locked or badge-controlled, with access based on need. Every key must be logged to a person and reconciled quarterly, and lost or unreturned keys must trigger rekeying. The cabinets that hold the substation gateways must be locked, and their keys held only by protection staff. (PE-2; PE-3; PR.AA-06; CIP-003-9 Attachment 1 Section 2)

4.11 Accounts lock after 10 failed sign-in attempts, and workstations lock after 10 minutes idle. SCADA HMI operator consoles are exempt from both, because locking an operator out during an event is unsafe; the DCC's badge control and 24x7 staffing compensate. (AC-7; AC-11)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual control assessment (P07), the quarterly access reviews, and the key log reconciliation.

## 6. Exceptions
Exceptions follow POL-01 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. Statements 4.6 to 4.8 and 4.10 carry NERC requirements and cannot be excepted.

## 7. Related documents
POL-01; POL-05; OT account procedure (due 2026-11-30); jump host procedure; key log; P02 control statements AC-2, AC-17, IA-2(1), PE-3
