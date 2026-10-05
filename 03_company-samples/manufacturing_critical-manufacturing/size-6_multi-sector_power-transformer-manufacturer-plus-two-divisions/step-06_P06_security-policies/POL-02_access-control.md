# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Version | v2026.1 |
| Owner | Group CISO (operated by the Group identity director) |
| Approved by | Group CISO, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, GV.RR-04 |
| Regulatory and contract drivers | Utility addendum secs. 3 and 6 (CIP-013-2 R1 Parts 1.2.3 and 1.2.6 flow-down); client CIP-004-7 terms (Grid Engineering); N22-R01 CIP-004-7 and CIP-005-7 (Electric Utility); N54-R04 FAR 52.204-21(b)(1)(i), (v), (vi) |
| Division supplements | Manufacturing: OEM access at plants, HMI accounts, field service access to utility sites. Electric Utility: CIP-004-7 access management and CIP-005-7 Interactive Remote Access. Grid Engineering: client access and BCSI folder authorization |

## 1. Purpose
Make sure only authorized people and processes reach group systems, plant and utility control systems, and customer systems, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, and administrator accounts in every division and in corporate shared services; vendor and OEM accounts; local accounts in plant OT and in the Electric Utility's Electronic Security Perimeters; and the access group staff hold to customer and client systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data and system owners | Approve access to their systems and company codes (for example, the VP manufacturing operations for GEPS scheduling) |
| Managers | Request and certify their staff's access every quarter |
| Group HR | Records joiners, movers, and leavers in the HR system the same day |
| Service account owners | Keep each service account's purpose, scope, and credentials current |
| Director of OT engineering; plant managers | Own plant OT accounts and OEM access at their plants |
| Electric Utility NERC compliance director | Owns CIP-004-7 access authorization, review, and revocation for BES Cyber Systems and BCSI |

## 4. Policy statements
4.1 Every user must have a unique identity. Shared or generic accounts are prohibited. Where an OT device supports only one shared account (some HMIs and controllers), the plant must document the exception with compensating controls (physical access, a logbook, password change when staff leave). (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege. Access to another division's GEPS company code needs that division's data owner approval. Roles that both create suppliers and approve payments, or both release schedules and change bills of materials, must be separated. (AC-3; AC-5; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access to group IT systems. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Service accounts** must have a named owner, be managed in identity governance, be scoped to one purpose and one target (for example, one integration hub account per plant), use workload identity where the platform supports it, rotate any static key at least every 90 days, and be included in access certification. (AC-2; AC-6; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and at once for involuntary terminations. Where a customer or client term requires notice (for example, the utility addenda: within 1 business day), the responsible team must send it from the same HR event. For BES Cyber System access, the Electric Utility must complete removal within 24 hours of the termination action (CIP-004-7 R5 Part 5.1). (PS-4; PS-7; AC-2; GV.RR-04)

4.6 Managers and system owners must certify access every quarter, including privileged and service accounts. Accounts inactive for 90 days must be disabled. (AC-2; AC-2(3); AC-6(7))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle, except operator HMIs where a lock would create a safety risk; those must be in physically controlled areas. (AC-7; AC-11; AC-12)

4.9 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.10 **Vendor and OEM remote access** must use only the group OEM remote access gateway (plants) or the Electric Utility's Intermediate Systems (CIP-005-7), with named accounts, MFA, per-session approval by the site, and session recording. Always-on modems, cellular routers, and vendor-installed remote tools are prohibited. (AC-17; MA-4; PR.AA-03)

4.11 **Separation of IT, OT, and CIP identities.** Identities used inside plant OT zones and inside Electronic Security Perimeters must be separate from the corporate directory. No directory trust may exist between the corporate domain and any plant or acquired domain. (AC-2; AC-3; PR.AA-05)

4.12 **Customer and client systems.** Staff may access utility and client systems only through the means the customer provides, under the customer's terms, and only while assigned to the work. (AC-20; AC-17)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and the Electric Utility's CIP-004-7 access reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. No exception may allow an always-on OEM connection.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02); group OT security standard; Electric Utility CIP-004-7 and CIP-005-7 programs.
