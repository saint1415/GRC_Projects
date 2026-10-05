# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Information Security Manager |
| Approved by | Chief Operating Officer (also as CIP Senior Manager for statements 4.6 to 4.9 and 4.12) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2025 policy) |
| Review cycle | Annually (next review by 2027-09-30), and after major changes or incidents. CIP topics at least every 15 calendar months |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4, PS-5, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| NERC and other | CIP-003-9 R2 Attachment 1 Sections 2, 3, and 6; 16 CFR 681.1(d)(2) (account access red flags) |

## 1. Purpose
Make sure only authorized people and systems can reach company systems, substations, and data, and only as far as their job requires. Access to OT gets the strictest rules, because a wrong command can cut power or endanger crews. Access to customer identity data is limited because it is the data identity thieves want.

## 2. Scope
All workforce members, contractors, and vendors at every company site, including substations and crew yards. Covers corporate IT, the DOP, the low impact BES Cyber Systems at Substations N, E, L, and H, the cloud landing zone, the CIS, AMI head-end, contact center platform, and every system vendors operate for the company, including the Utility Services client partitions.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Opens onboarding, transfer, and termination tickets the same day; collects keys and badges |
| Director of Information Technology | Provisions and removes IT, cloud, and SaaS access; runs the identity provider and PAM |
| OT Engineering Manager | Provisions and removes OT domain, SCADA, and jump host accounts; owns the OT privileged accounts |
| Director of System Operations | Enables vendor remote access sessions from the DCC; approves HMI access |
| Director of Engineering and Protection | Approves substation physical access, keys, and relay access |
| Vice President of Customer Operations and Director of Utility Services | Approve CIS, AMI, and export rights for customer and client data |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account on every system, including SCADA servers, HMIs, jump hosts, relays where the device supports it, and SaaS consoles. Shared or generic accounts are prohibited. The 3 shared SCADA administrator accounts must be replaced by named, vaulted accounts by 2026-12-31; until then each password must be changed after every vendor session. (IA-2; IA-4; AC-2; PR.AA-01)

4.2 Access must be role-based and least-privilege, and approved by the user's manager and the data or system owner before it is granted. SCADA administrator rights are limited to named OT engineers. Bulk export rights in the CIS and bulk command rights in the AMI head-end are limited to named roles approved by the Vice President of Customer Operations. (AC-2; AC-3; AC-6; PR.AA-05)

4.3 **Two-person rule for high-impact commands.** AMI remote disconnects of more than 50 meters at once, switching orders, and SCADA database changes must have an author and a different approver. (AC-5; PR.AA-05)

4.4 MFA is required for email, the CIS, the OMS, the AMI head-end, the cloud console, the VPN, the tablets, and every remote path into the OT network, including the jump hosts. Administrators and vendor jump host users must use phishing-resistant authenticators by 2027-03-31. (IA-2(1); IA-2(2); PR.AA-03)

4.5 **Privileged access.** Administrator rights in IT, cloud, SaaS, and OT must be granted through the PAM tool with check-out per session, separate from everyday accounts, and recorded. PAM must cover OT by 2026-12-31. (AC-6(2); AC-6(5); PR.AA-05)

4.6 **Vendor remote access.** Vendor electronic remote access to OT, including to Substations N, E, L, and H, must:
- use named vendor accounts with MFA through the jump hosts only;
- be disabled by default, and enabled by the DCC for a stated purpose and end time;
- be recorded, so the company can always tell which vendor had access to what and when;
- be disabled at once by the DCC if misuse is suspected;
- be monitored for known or suspected malicious communications.

No other vendor remote access path (modems, cellular routers, vendor-owned remote tools) is permitted at any substation. (AC-17; MA-4; SI-4; PR.AA-05; CIP-003-9 Attachment 1 Section 6)

4.7 **Electronic access to low impact assets.** Routable communication into or out of Substations N, E, L, and H must be limited to the flows documented as necessary, enforced by the substation gateway. Access lists and remote access paths must be checked after every change, every commissioning, and every contractor visit that installs equipment, and reviewed at least annually. (SC-7; AC-4; CM-6; PR.IR-01; CIP-003-9 Attachment 1 Section 3.1)

4.8 Dial-up connectivity to relays or substation devices is prohibited. If a device ever needs it, it must be authenticated, approved by the CIP Senior Manager, and recorded. (AC-17; CIP-003-9 Attachment 1 Section 3.2)

4.9 **IT/OT boundary.** All traffic between corporate IT and OT must pass through the OT DMZ. No direct rule from the corporate network to SCADA, historian, or engineering workstations is permitted. Firewall rules between IT and OT must be reviewed each quarter with OT sign-off. (SC-7; AC-4; PR.IR-01)

4.10 **Joiners, movers, leavers.** HR must open a termination ticket on or before the last day. All access, including OT domain accounts, must be disabled the same business day, or immediately for involuntary terminations. Transfers must trigger removal of the old roles within 5 business days. Keys and badges must be collected before final pay is released. (PS-4; PS-5; AC-2)

4.11 Managers must review their staff's access every quarter. The OT Engineering Manager must review SCADA, OT domain, and jump host accounts every quarter with the Director of System Operations. Accounts unused for 45 days must be disabled. (AC-2; AC-2(3); PR.AA-05)

4.12 **Physical access.** Substation control houses, the DCC, and the backup DCC must be locked or badge-controlled, with access based on need. Every key must be logged to a person and reconciled quarterly; lost or unreturned keys must trigger rekeying within 30 days. When the company takes over a substation, its locks must be changed before it is placed in service under the company. Gateway cabinets must be locked, with keys held only by protection staff. (PE-2; PE-3; PR.AA-06; CIP-003-9 Attachment 1 Section 2)

4.13 Passwords must be at least 14 characters and not on the banned-password list. Relay, gateway, and router passwords must be unique per site, changed from vendor defaults before commissioning, vaulted, and changed after every contractor visit. (IA-5; CM-6)

4.14 Accounts lock after 10 failed sign-in attempts, and workstations lock after 15 minutes idle. SCADA HMI operator consoles are exempt from both, because locking an operator out during an event is unsafe; the DCC's badge control, named accounts, and 24x7 staffing compensate. (AC-7; AC-11)

## 5. Compliance and enforcement
Violations are handled under POL-01 4.10. Compliance is checked through the annual control assessment (P07), quarterly access reviews, the key register reconciliation, and the NERC Compliance Manager's internal CIP checks.

## 6. Exceptions
Exceptions follow POL-01 4.9. Statements 4.6 to 4.8 and 4.12 carry NERC requirements and cannot be excepted.

## 7. Related documents
POL-01; POL-05; STD-06 Authenticator and privileged access standard; STD-07 OT network and remote access standard; OT account procedure (due 2026-11-30); DCC vendor access procedure; key register; P02 control statements AC-2, AC-17, IA-2(1), PE-3
