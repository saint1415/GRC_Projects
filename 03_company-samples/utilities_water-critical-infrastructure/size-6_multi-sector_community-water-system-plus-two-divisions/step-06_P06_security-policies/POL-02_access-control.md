# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO, with the Group OT Security Director for OT access |
| Approved by | Group CISO under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-2(2), AC-3, AC-4, AC-6, AC-6(5), AC-17, AC-20, CA-3, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory drivers | C-WATER-R01 (300i-2(a)(1)(A)(ii)); N23-R03 (NIST SP 800-171 3.1.1, 3.1.3, 3.1.20, 3.5.3); N56-R07 (FAR 52.204-21(b)(1)(i), (v), (vi)) |
| Division supplements | Water Utility: control room shift sessions and HMI roles. Construction: CUI enclave identity tenant; commissioning laptops. Environmental Services: client site gateways |

## 1. Purpose
Make sure only authorized people, services, and devices can reach group systems, with no more access than they need, and that every path into OT is controlled, approved, and recorded.

## 2. Scope
All accounts and access paths to IT and OT systems in every division, including vendor and sister-division access, service accounts, device credentials, and emergency accounts.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Operates SYS-G1 (single sign-on, MFA, PAM, identity governance) |
| Group OT Security Director | Operates SYS-G4; approves OT access exceptions |
| System owners (for example the RS-1 Director of Operations) | Approve access to their systems; certify it every quarter |
| Control room shift supervisors | Approve each remote OT session in real time |
| Construction security and compliance lead | Operates the CUI enclave identity tenant (SYS-C2) |
| Managers | Request access for their staff and report role changes the same day |

## 4. Policy statements
4.1 Every user must have a named account. Shared accounts are prohibited, including on HMIs, with one exception: a continuously staffed control room may keep a shift session open on operator HMIs if each operator signs in by name to make changes. (AC-2; IA-2; PR.AA-01)

4.2 Access must follow least privilege. HMI roles (viewer, operator, supervisor, engineer) must limit who can change setpoints, alarm limits, modes, and PLC programs. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all remote access, all privileged access, and all cloud and SaaS access. Administrators must use phishing-resistant MFA. (IA-2(1); IA-2(2); PR.AA-03; NIST SP 800-171 3.5.3)

4.4 **OT remote access** is allowed only through the group OT remote access gateway (SYS-G4), with MFA, **approval of each session** by the asset owner's shift supervisor, and session recording. Always-on vendor remote tools are prohibited. No exception may waive per-session approval for any group of users, including sister-division staff. Recordings of vendor and commissioning sessions must be reviewed weekly by the asset owner. (AC-17; MA-4; PR.AA-05)

4.5 Access must be removed within 4 hours of a termination and reviewed within 5 business days of a transfer. (PS-4; AC-2)

4.6 System owners must certify IT and OT accounts, including SYS-G4 gateway accounts, every quarter, and privileged accounts every month. (AC-2; PR.AA-05)

4.7 Privileged access must be checked out through group PAM with just-in-time elevation and session recording. Engineering workstations must not grant standing local administrator rights. (AC-6; AC-6(5))

4.8 Default credentials must be changed before any device enters service, including PLCs, RTUs, HMIs, cellular modems, and client site gateways. (IA-5; CM-6; FAR 52.204-21(b)(1)(vi))

4.9 Emergency (break-glass) accounts must be sealed, monitored, and rotated after each use. (AC-2(2); IA-5)

4.10 A device not owned by the asset owner (a vendor laptop or a sister division's commissioning laptop) may connect to OT only on a maintenance segment, after malware scanning, and under a written interconnection agreement. (AC-20; CA-3; NIST SP 800-171 3.1.20)

4.11 Covered defense information may be accessed only inside the CUI enclave (SYS-C2), through its own identity tenant with phishing-resistant MFA. (AC-4; NIST SP 800-171 3.1.3)

## 5. Compliance and enforcement
Checked through P07 (AC-2, AC-6, AC-6(5), AC-17, IA-2, IA-2(1), IA-5, MA-4, PS-4), quarterly access certifications, and gateway session reviews. Violations are handled under POL-01 4.7.

## 6. Exceptions
Exceptions follow POL-01 4.10. Statement 4.4 has no exceptions for per-session approval.

## 7. Related documents
POL-01; POL-04; group OT security standard; `division-supplements.md`; P02 SSP for RS1-SCADA.
