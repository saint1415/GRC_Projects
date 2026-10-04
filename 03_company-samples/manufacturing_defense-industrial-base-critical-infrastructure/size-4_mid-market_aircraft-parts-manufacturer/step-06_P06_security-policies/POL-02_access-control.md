# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(2), AC-6(7), AC-6(9), AC-7, AC-11, AC-12, AC-17, AC-18, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-3, PS-4, PS-5 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| SP 800-171 Rev. 2 | 3.1.1 to 3.1.20, 3.5.1 to 3.5.11, 3.7.5, 3.9.1, 3.9.2 |
| Export control | 22 CFR 120.56 (release); technology control plan |
| Supporting standards | STD-06 Identity and privileged access; STD-04 OT and shop-floor security |

## 1. Purpose
Make sure only authorized people, devices, and systems can reach CUI and company systems, and only to the extent their job requires. Because much of the company's CUI is ITAR technical data, access also depends on U.S.-person status.

## 2. Scope
All workforce members, vendors, partners, and service accounts with access to company systems at both plants and in all cloud and SaaS services, including MES and DNC terminals, shop-floor servers, operational technology, and vendor remote support.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers | Request and approve access; complete quarterly access reviews for their staff |
| System owners (PLM, MES, MFT, cloud accounts) | Approve role design; review privileged and export rights quarterly |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| Director of Trade Compliance and Contracts | Confirms U.S.-person status before enclave access; maintains the technology control plan |
| Security Manager | Runs the identity provider, privileged access broker, and vendor access |
| Manufacturing Systems Manager | Runs MES and DNC accounts and shop-floor terminals |
| Workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on MES and DNC terminals. **Plant 2 exception until 2027-01-31**, approved by the COO under POL-01 4.7 with the compensating controls in SSP section 11. (IA-2; AC-2; 3.5.1; 3.5.2)
4.2 Enclave access, and any access to ITAR technical data, requires confirmation of U.S.-person status by the Director of Trade Compliance and Contracts before the account is enabled. Foreign persons may not receive enclave accounts unless an export authorization covers the data. (AC-2; PS-3; 22 CFR 120.56)
4.3 Access must be role-based, least-privilege, and approved by the user's manager and the system owner before it is granted. Program-edit rights in MES and DNC are limited to NC programmers and manufacturing engineers. (AC-2; AC-3; AC-6; CM-5; PR.AA-05; 3.1.2; 3.1.5)
4.4 MFA is required for all access to enclave services and for all corporate accounts. Administrators must use hardware security keys. All enclave users must use phishing-resistant authenticators by 2027-01-31. Local administrator access to shop-floor servers must go through the access broker with MFA. (IA-2(1); IA-2(2); PR.AA-03; 3.5.3)
4.5 **Termination.** HR must record the termination on or before the last day. Enclave and corporate access must be disabled automatically that day, or immediately for involuntary terminations. Badges must be disabled within 24 hours, and any credential the person knew must be changed. (PS-4; AC-2; 3.9.2)
4.6 **Transfers.** Access from the prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.7 **Access reviews.** Managers must review their staff's enclave, PLM, MES, MFT, and cloud access every quarter. System owners must review privileged, export, and partner accounts every quarter. Accounts inactive for 45 days are disabled automatically. (AC-2; AC-6(7); 3.1.1; 3.5.6)
4.8 **Privileged access.** Administrators must use a separate privileged account, elevated just in time through the access broker, with sessions logged. Standing administrator rights are not allowed for vendor or service accounts. When a system or site is acquired, all inherited accounts must be reviewed within 30 days. (AC-6(2); AC-6(9); 3.1.6; 3.1.7)
4.9 Accounts lock after 10 failed sign-in attempts. Workstations and terminals lock after 15 minutes idle with a pattern-hiding screen; terminals use badge tap-out. Enclave sessions end after 30 minutes idle and 12 hours total. (AC-7; AC-11; AC-12; 3.1.8; 3.1.10; 3.1.11)
4.10 **Remote access** to the enclave is allowed only through the virtual desktop gateway with MFA and a compliant device. No other inbound path may be created. (AC-17; 3.1.12 to 3.1.15)
4.11 **Vendor remote access** (machine tool, additive printer, test equipment, and software vendors) must use named accounts with MFA through the company access broker, be approved per session, be recorded, and end when the work is complete. Vendor-supplied remote tools are prohibited. (MA-4; 3.7.5)
4.12 Passwords must be at least 14 characters and not on the banned-password list. Service account and machine credentials must be stored in the vault, never in plain text, and rotated at least annually and when anyone who knew them leaves. (IA-5; 3.5.7 to 3.5.10)
4.13 **External systems.** CUI may not be processed on external systems, including public or corporate AI services and vendor clouds, unless the system is inside the assessed boundary or approved under POL-01 4.3. Public AI and file-sharing services are blocked from enclave networks. (AC-20; 3.1.20)
4.14 **Wireless.** No wireless access on enclave VLANs. Wireless networks that reach in-scope systems must use enterprise authentication. (AC-18; 3.1.16; 3.1.17)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Compliance is checked through the quarterly access reviews, the annual self-assessment, and the co-sourced internal audit (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.7. The Plant 2 shared-login exception in 4.1 expires on 2027-01-31 and cannot be extended past the C3PAO assessment.

## 7. Related documents
POL-01; POL-05; STD-04; STD-06; technology control plan; P02 control statements AC-2, AC-6, IA-2, IA-5; P07 findings for AC-02, AC-06, IA-02, IA-05, MA-04, PS-04
