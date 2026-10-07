# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the Group identity director) |
| Approved by | Group CISO, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | State agency contract exhibits (SP 800-53 Rev. 5 Moderate); FAR 52.204-21(b)(1)(i), (ii), (v), (vi); FAR 52.204-9(b); C-GOVERNMENT-R05 (34 CFR 99.31(a)(1)(ii)); N23-R04 (SP 800-171 R2 3.1.1, 3.1.12, 3.5.3); N56-R02 (15 U.S.C. 1681b(b)) |
| Division supplements | Facilities Support: customer tenant administration and federal PIV duties. Construction: CUI enclave access and subcontractor guests. Janitorial and Security: customer-site badges and keys, consumer report access, panel credentials |

## 1. Purpose
Make sure only authorized people and processes reach group systems, customer building systems, and the information in them, and only to the extent their job requires.

## 2. Scope
All workforce identities, integrator and subcontractor identities, service and device accounts, and administrator accounts in every division and in corporate shared services; customer users of the IBOP access control tenants; and physical credentials (badges, keys, PIV cards) the group issues or holds at customer sites.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Group building technology director | Runs the OT remote access service and the IBOP administrator model |
| Division security and compliance leads | Approve division roles; own customer-site credential processes |
| Sponsors (managers) | Sponsor integrator and subcontractor accounts; certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers in the HR system the same day |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited. Device and service passwords must be unique per device and kept in the group password vault. (IA-2; AC-2; IA-5; PR.AA-01)

4.2 Access must be role-based and least privilege. Administration of a customer's access control tenant or building automation system must be granted per customer and just in time through PAM. **Standing administrator roles across customer tenants are prohibited** after 2027-03-31; until then they are a recorded exception. The same person may not both create an administrator account and approve it. (AC-3; AC-5; AC-6; PR.AA-05)

4.3 MFA is required for all workforce, integrator, and subcontractor access to group systems and the IBOP. Administrators must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03)

4.4 **Integrator and subcontractor accounts** must have a named sponsor, be managed in identity governance, expire within 12 months or at the end of the engagement, and be included in quarterly certification. (AC-2; PS-7; PR.AA-01)

4.5 **Termination.** Group system access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Customer-site badges must be disabled and keys and agency-issued PIV cards recovered on the last day; a credential not recovered must be reported to the customer or sponsoring agency the same day (FAR 52.204-9(b)). (PS-4; AC-2; PR.AA-05)

4.6 Managers and system owners must certify access every quarter, including privileged, integrator, and service accounts. (AC-2; PR.AA-05)

4.7 Privileged access to cloud, IBOP, and corporate systems must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 **OT remote access** to any customer site must go only through the group OT remote access service, with MFA, per-session approval, and recording. Vendor remote-support tools, integrator VPNs, and persistent tunnels into customer sites are prohibited; existing ones at acquired sites must be removed by 2026-12-15. (AC-17; MA-4; PR.AA-05)

4.9 Default passwords on controllers, door panels, cameras, and gateways must be changed before a device is connected or a building is turned over. (IA-5; CM-6; PR.AA-01)

4.10 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle, except alarm display screens that show no personal data. Application sessions must end after 30 minutes idle. (AC-7; AC-11; AC-12)

4.11 **Customer users** of IBOP access control tenants must use MFA. A customer that declines must sign a risk acceptance at contract renewal. (IA-8; PR.AA-03)

4.12 **Consumer reports** obtained for employment may be opened only by adjudicators, and only for the employment purpose. (AC-6; PR.AA-05)

4.13 **CUI** may be accessed only in the Construction CUI enclave (SYS-C2), from managed devices, by people approved by the CUI program manager. (AC-3; AC-17; PR.AA-05)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, IBOP and division samples, and quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may permit remote access that bypasses the OT remote access service after 2026-12-15.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; IBOP SSP (P02); common control catalog (P02).
