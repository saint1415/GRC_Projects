# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-12, AC-17, AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | N42-R03 (SP 800-171 R2 3.1.1 to 3.1.22, 3.5.1 to 3.5.11, 3.7.5); N42-R04 (52.204-21(b)(1)(i)-(vi)); N44-45-R01 (PCI DSS v4.0.1 Req. 7, 8) |
| Division supplements | IT Distribution: FFE access and the CUI roster. Logistics: handheld sign-in, temporary agency workers, OT vendor access. Online Retail: contact center desktops, seller data, consumer accounts |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems and data, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, administrator accounts, and vendor accounts in every division and in corporate shared services, and the external identities (resellers, 3PL clients, consumers, marketplace sellers) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data and system owners | Approve access to their systems; integration center managers approve the CUI roster |
| Managers | Request and certify their staff's access every quarter |
| Group HR and staffing agencies | Record joiners, movers, leavers, and agency assignment end dates the same day |
| Service account owners | Keep each service account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited, including on handhelds and DC equipment. A documented exception must have compensating controls and a replacement date. (IA-2; AC-2; PR.AA-01; 3.5.1)

4.2 Access must be role-based and least privilege, approved by the system owner. Access to CUI requires membership of the CUI roster, completed CUI training, and approval by an integration center manager. (AC-3; AC-6; PR.AA-05; 3.1.1, 3.1.2, 3.1.5)

4.3 MFA is required for all workforce access. Administrators and all users of the Federal Fulfillment Enclave must use phishing-resistant authenticators. MFA is required for every access into the cardholder data environment. (IA-2(1); IA-2(2); PR.AA-03; 3.5.3; PCI DSS 8.4.2)

4.4 **Service accounts** must have a named owner, be managed in identity governance, keep secrets in the group secrets vault, and rotate static secrets at least every 90 days. (AC-2; IA-5; PR.AA-01)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Temporary agency worker accounts must expire automatically at the assignment end date. (PS-4; AC-2; 3.9.2)

4.6 Managers and system owners must certify access every quarter, including privileged, service, and vendor accounts. Accounts unused for 60 days (35 days in the FFE) must be disabled automatically. (AC-2; AC-2(3); 3.5.6; PCI DSS 7.2.4)

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05; 3.1.6, 3.1.7)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle (5 minutes in the FFE). Application sessions must end after 30 minutes idle (15 minutes in the FFE). (AC-7; AC-11; AC-12; 3.1.8, 3.1.10, 3.1.11)

4.9 **Vendor and remote maintenance access**, including to DC automation and PLCs, must go through group PAM with named accounts, MFA, approval for each session, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4; 3.7.5)

4.10 **External systems.** CUI must not be stored, processed, or shared on any system outside the CMMC assessment scope, including the commercial collaboration tenant and the commercial ERP. (AC-20; 3.1.20)

4.11 **External identities.** Reseller administrators, 3PL client users, and marketplace sellers must use MFA. Consumer accounts must be offered MFA or passkeys, with step-up checks before stored payment tokens or addresses change. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 5. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, and the PCI DSS ROC.

## 6. Exceptions
Exceptions follow POL-01 section 4.14.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
