# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-5, AC-6, AC-6(9), AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| PCI DSS v4.0.1 (N44-45-R01) | 6.5.4, 7.2.1, 7.2.2, 7.2.4, 8.2.1, 8.2.2, 8.2.5, 8.2.6, 8.2.7, 8.4.1 to 8.4.3, 8.4.3, 10.2.1.2 (requirement numbers only; read the text in the company's licensed copy) |

## 1. Purpose
Make sure only authorized people and processes reach the company's information and systems, only to the extent their role requires, and that access ends promptly when it is no longer needed. This policy carries PCI DSS Requirements 7 and 8 for the CDE and applies the same rules to customer data and tier-1 systems.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at the 112 stores in Florida, Georgia, Alabama, South Carolina, and Tennessee, the 2 distribution centers, and headquarters, including the acquired banner (AB) stores from their acquisition date. Covers all systems and data, including stores, colocation, cloud, SaaS, store operational technology, and systems that third parties operate for the company, and the services the company offers to external business clients (SL-1 retail media and SL-2 supplier collaboration).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05) and identity governance |
| Managers and system owners | Approve access; complete certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Director of Store Technology | POS operator IDs and store controller access |
| Vice President, Integration Management Office | Brings AB identities onto the identity platform |
| Client and supplier administrators (SL-1, SL-2) | Manage their own staff accounts under client agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared or group accounts are prohibited, including local administrator accounts on store systems; service and device accounts must be vaulted in PAM. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. CDE access must be certified quarterly and all other access at least every 6 months. (AC-2; AC-6; PR.AA-05)
4.3 Duties that would let one person both change and approve payment switch routing, publish and approve payment page changes, or change and pay supplier bank details must be separated. (AC-5; PR.AA-05)
4.4 MFA is required for all remote network access, all non-console access into the CDE, and all cloud and administrative access. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations, including at AB stores. (PS-4; AC-2; PR.AA-05)
4.6 Accounts inactive for 90 days must be disabled automatically (60 days for SSO accounts), including POS operator IDs and client and supplier portal accounts. (AC-2(3); PR.AA-05)
4.7 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.8 Vendor and remote maintenance access, including refrigeration, building controls, and POS vendors, must go through the zero-trust gateway or PAM with approval and session recording, and be enabled only when needed. Always-on vendor remote tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.9 Customer accounts must be protected with breached-password checks, bot defenses, and a one-time code before saved cards are added or changed. (IA-8; PR.AA-03)
4.10 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)
4.11 Cashiers and leads must use their own POS operator ID; manager overrides must be performed with the manager's own ID, never a shared override code. (IA-2; AC-2; PR.AA-01)
4.12 SL-1 client and SL-2 supplier users must authenticate with MFA, and each client or supplier administrator must attest to its users' access every quarter. (IA-8; AC-2; PR.AA-03)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
The identity governance platform enforces most statements automatically. Compliance is measured through quarterly CDE access certifications, monthly inactive-account reports (including POS operator IDs), PAM session reviews, and the annual Internal Audit assessment (P07). Violations follow PRC-01.1.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. A deviation from a PCI DSS requirement also needs the PCI Program Manager's review, because internal exceptions do not change what the QSA must validate.

## 8. Related documents
POL-01; STD-02.1 to STD-02.3; PRC-02.1 to PRC-02.4; P02 SSP (AC and IA controls; section 11 digital identity); P07 AC-2, AC-2(3), IA-2, IA-5 results; POAM-007, POAM-008, POAM-015.
