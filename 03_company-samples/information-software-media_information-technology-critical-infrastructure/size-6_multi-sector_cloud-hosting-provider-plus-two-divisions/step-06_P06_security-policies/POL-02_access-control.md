# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the Group identity director) |
| Approved by | Group CISO, under authority of POL-01, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-12, AC-17, CM-5, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory references | FedRAMP Rev5 Class C controls (G1); NIST SP 800-171 Rev. 2 families 3.1 and 3.5 (CUI enclave); 16 CFR 314.4(c)(1) and (c)(5); PCI DSS v4.0.1 Requirements 7 and 8; 45 CFR 164.312(a) and (d) |
| Division supplements | Cloud Hosting: HCP operator and support access, break-glass. Managed IT: RMM technician accounts and client access broker. Payment Processing: CDE roles and merchant users |

## 1. Purpose
Make sure only authorized people and processes reach group systems and customer environments, and only to the extent their job requires.

## 2. Scope
All workforce identities, service identities, and administrator accounts in every division and in corporate shared services; the external identities group systems authenticate (customer users, agency administrators, merchant and biller users, consumers); and every path one division uses to act inside another division's systems or a customer's systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| System owners | Approve access to their systems; define roles |
| Owning division of a regulated environment | Approves any access into G1, the CDE, or the CUI enclave, including access by another division |
| Managers | Request and certify their staff's access every quarter |
| HR | Records joiners, movers, and leavers the same day |

## 4. Policy statements
4.1 Every workforce user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. Identity tenants outside SYS-G1 (including the Managed IT legacy tenant) must be migrated by 2027-03-31; no new federation trust into the HCP or the RMM may be created without the Group CISO's written approval. (IA-2; AC-2; PR.AA-01)

4.2 Access must be role-based and least privilege. Access that lets one division act inside another division's environment or a customer's environment (for example, partner-operator access to managed-hosting tenants) must be scoped to the specific client or tenant the person serves and approved by the owning division. (AC-3; AC-6; PR.AA-05; 16 CFR 314.4(c)(1))

4.3 MFA is required for all workforce access. All privileged access, including partner-operator access and RMM technician access, must use phishing-resistant authenticators by 2026-12-31. (IA-2(1); IA-2(2); PR.AA-03; 16 CFR 314.4(c)(5))

4.4 Privileged access must be granted just in time through SYS-G1 PAM, with approval and session recording. **Standing privileged access is prohibited**, including standing partner-operator access. (AC-6(5); PR.AA-05)

4.5 Privileged and partner-operator sessions must end after 1 hour and use tokens bound to a managed device. Other workforce console sessions must end after 8 hours. Customer-facing sessions follow the product standard. (AC-12)

4.6 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2)

4.7 Managers and system owners must certify access every quarter, including privileged roles, service accounts, partner-operator grants, and RMM technician accounts. (AC-2; AC-6(7))

4.8 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2)

4.9 **Remote and tool-based access.** Remote administrative access must go through the SYS-G1 access broker from managed devices. RMM use must meet these rules: named technician accounts; console access only from approved network locations; and two-person approval for any script or job that targets more than one client or any system in G1, the CDE, or the CUI enclave. Vendor maintenance must go through PAM with recording. (AC-17; CM-5; MA-4)

4.10 **External identities.** MFA must be required for customer tenant root owners now and for all customer administrators by 2027-06-30; for merchant portal users by 2027-01-31; and for consumer bill-pay payee changes. Agency administrators in G1 sign in through agency federation. (IA-8; IA-2)

4.11 **Service identities and secrets.** Services must use short-lived workload identities where the platform supports them. Any static secret must be in the secrets store and rotate at least every 90 days. Credentials must never be stored in tickets, notes, chat, or documentation fields. (IA-5; PR.AA-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
