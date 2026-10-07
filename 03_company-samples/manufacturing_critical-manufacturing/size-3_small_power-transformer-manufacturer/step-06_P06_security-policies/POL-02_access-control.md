# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | IT Manager |
| Approved by | VP Operations, 2026-09-04 |
| Effective date | 2026-09-08 |
| Review cycle | Annually (next review by 2027-09-08), and after major changes or incidents |
| Replaces | IT handbook (2021), for the topics covered here |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, GV.RR-04, DE.CM-06 |
| Contract and regulatory drivers | FAR 52.204-21(b)(1)(i), (ii), (v), (vi); Utility addenda secs. 3 and 6 (CIP-013-2 R1.2.3, R1.2.6 flow-down); CSF 2.0 benchmark |

## 1. Purpose
Make sure only authorized people and suppliers can reach company systems and plant equipment, only to the extent their job requires, and that access ends on time.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary workers, and contractors) on the Florida campus and in the field. Covers office IT, plant control systems (OT), the high-voltage test bay, cloud and SaaS services, and systems that service providers operate for the company. It applies to all company information, customer information shared under NDA, and federal contract information (FCI).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Department managers | Request and approve access for their staff; complete quarterly access reviews |
| HR Manager | Opens onboarding, transfer, and termination tickets on or before the effective date |
| IT Manager | Provisions and removes IT, ERP, and cloud access; runs the identity provider |
| Controls Engineer | Manages HMI, engineering workstation, and OEM remote access; approves each OEM session |
| Production Planning Manager | Manages MES and kiosk accounts |
| Field Service Manager | Sends access-revocation notices to utilities; manages field laptops |
| Workforce | Protect credentials; never share accounts, PINs, or badges |

## 4. Policy statements
4.1 Every user must have a unique account. Shared or generic accounts are prohibited, including on HMIs, test PCs, and OEM remote access. Where plant equipment cannot support individual accounts, a documented exception must name the compensating controls (role accounts with individual PINs, physical access limits, and logging). (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based, least-privilege, and approved by the user's manager before it is granted. No more than 2 named administrators may hold ERP super-user rights, and no user may both maintain supplier bank details and approve payments. (AC-2; AC-3; AC-6; PR.AA-05)

4.3 MFA is required for email, the ERP, the identity provider, the VPN, cloud administration, and all remote access into the plant. Administrators must use phishing-resistant hardware security keys. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Termination.** HR must open a termination ticket on or before the last day. All access, including MES and kiosk accounts, badges, and OEM or utility access, must be disabled **the same business day**, or immediately for involuntary terminations. For field technicians, the Field Service Manager must notify each addendum utility within 1 business day that the technician's access should no longer be granted. (PS-4; AC-2; GV.RR-04)

4.5 Managers must review their staff's ERP roles, MES accounts, and shared-folder access every quarter. The IT Manager must review cloud administrator roles, and the Controls Engineer must review OEM and OT accounts, every quarter. (AC-2; AC-6)

4.6 Default passwords must be changed before any system or device, including HMIs, controllers, network equipment, and cameras, is connected to a company network. Unused web or remote configuration interfaces must be turned off. (IA-5; CM-7)

4.7 Passwords must be at least 14 characters and must not appear on the banned-password list. Local administrator passwords must be unique per device and managed by the IT tool. Passwords must be kept in the company password manager and never saved in browsers on shared devices. (IA-5)

4.8 **Supplier remote access into the plant** must go through the company remote access gateway, with a named account, MFA, per-session approval by the Controls Engineer, and session recording. OEM cellular routers must stay powered off except during an approved session. MSP and ERP vendor access must use named VPN accounts with MFA. (AC-17; MA-4; DE.CM-06)

4.9 **Access to utility systems.** Field technicians may connect to a utility's systems only through that utility's own MFA-protected remote access, one session at a time, from a named company laptop. (AC-17; Utility addendum sec. 6)

4.10 Two break-glass administrator accounts must exist for the identity provider and cloud tenant. Their credentials must be stored sealed and offline, tested quarterly, and used only when normal sign-in is unavailable. Every use is reviewed by the IT Manager. (AC-2)

4.11 Accounts lock after 10 failed sign-in attempts. Office endpoints lock after 10 minutes idle. Kiosks return to the sign-in screen after each transaction. (AC-7; AC-11)

4.12 Federal contract information must be accessible only to the named project team. (AC-3; FAR 52.204-21(b)(1)(i))

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.12. Consequences range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), access reviews, and the quarterly obligations register review.

## 6. Exceptions
Exceptions follow POL-01 statement 4.11. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months. Exceptions for plant equipment that cannot technically meet a statement (for example, an HMI without individual accounts) must name the compensating controls.

## 7. Related documents
POL-01; POL-04; POL-05; access review procedure; OEM remote access procedure; P02 control statements AC-2, AC-6, AC-17, IA-5, MA-4
