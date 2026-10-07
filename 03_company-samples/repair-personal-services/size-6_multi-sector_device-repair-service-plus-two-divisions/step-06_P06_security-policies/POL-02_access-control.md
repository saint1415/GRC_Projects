# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-7, AC-11, AC-12, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05 |
| Regulatory drivers | N81-R02 (Fla. Stat. 501.171(2)); N81-R03 and N44-45-R01 (PCI DSS v4.0.1 Req. 7, 8); N54-R06 (45 CFR 164.308(a)(3), (a)(4); 164.312(a), (d)); Manufacturer A and B agreements (named, MFA-protected portal accounts) |
| Division supplements | Device Repair: bench accounts, passcode vault access, manufacturer portals. Electronics Retail: POS and back office. IT Support: RMM, remote support, and the customer credential vault |

## 1. Purpose
Make sure only authorized people and processes reach group systems, customer devices, and managed customers' systems, and only to the extent their job requires.

## 2. Scope
All workforce identities, service accounts, administrator accounts, and shared or device accounts in every division and in corporate shared services, the accounts the group holds on manufacturer and partner portals, and the external identities (customers and business account administrators) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Data owners (division leads; Group Chief Privacy Officer for customer data) | Approve access to their systems and data |
| Managers and store managers | Request and certify their staff's access every quarter |
| Group HR | Records joiners, movers, and leavers in the HR system the same day |
| Service account and portal account owners | Keep each account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. **Shared or generic accounts are prohibited, including bench workstation logins and manufacturer portal logins.** Existing shared bench logins at in-store repair counters must be replaced with named accounts by 2026-12-31. (IA-2; AC-2; PR.AA-01; PCI DSS 8.2.1; Manufacturer A and B agreements; 164.312(a)(2)(i))

4.2 Access must be role-based and least privilege. STPP access must be scoped to the user's store, region, or depot. Passcode vault fields may be read only by the technician assigned to the ticket, with re-authentication. (AC-3; AC-6; IA-11; PR.AA-05; PCI DSS 7.2)

4.3 MFA is required for all workforce access. Administrators must use phishing-resistant authenticators. **RMM and remote support administrators must use phishing-resistant authenticators by 2026-12-31.** Remote workforce access must use phishing-resistant authenticators by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03; PCI DSS 8.4; 164.312(d))

4.4 **Service and interface accounts** must have a named owner, be managed in identity governance, use workload identity where the platform supports it, rotate any static secret at least every 90 days, and be included in access certification. (AC-2; IA-5; PR.AA-01; PCI DSS 8.6)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor accounts must expire automatically at the assignment end date. (PS-4; AC-2; PCI DSS 8.2.5; 164.308(a)(3)(ii)(C))

4.6 Managers and data owners must certify access every quarter, including privileged, service, portal, and RMM accounts. (AC-2; AC-6(7); PCI DSS 7.2.4; 164.308(a)(4)(ii)(C))

4.7 Privileged access must be granted just in time through PAM, with approval and session recording. **No standing global administrator accounts are allowed in the RMM or the remote support tool, except two sealed break-glass accounts.** (AC-6(5); PR.AA-05; 164.308(a)(4)(ii)(B))

4.8 **Actions on customer systems.** An RMM script or policy that will run on more than 50 managed customers, or on any customer's domain controllers or backup systems, must be approved by a second authorized person before release. The AI remediation agent may run only allow-listed actions under a scoped role (P10). (AC-6; CM-3; 164.308(a)(1)(ii)(B))

4.9 Accounts must lock after 10 failed attempts. Workstations, including bench workstations, must lock after 10 minutes idle. Application sessions must end after 30 minutes idle. (AC-7; AC-11; AC-12; PCI DSS 8.2.8; 164.312(a)(2)(iii))

4.10 **Emergency access.** Each critical system must have sealed break-glass accounts, tested quarterly, used only when normal sign-in is unavailable, and reviewed after every use. (AC-2; 164.312(a)(2)(ii))

4.11 Vendor and remote maintenance access must go through group PAM with named accounts, MFA, and recording. Persistent vendor tunnels are prohibited. (AC-17; MA-4; PCI DSS 8.2.2)

4.12 **External identities.** Customer sign-in on SYS-G4 must offer MFA. MFA must be required for business account administrators. A repair device may be released only to the person on the ticket, verified by claim tag and name, or by a one-time code for high-value devices. (IA-8; IA-2; PR.AA-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, division samples, quarterly certification results, the QSA ROCs, and the IT Support SOC 2 examination.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04 (customer data access standard); `division-supplements.md`; common control catalog entries for SYS-G1 (P02).
