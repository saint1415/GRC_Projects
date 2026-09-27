# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-6(5), AC-17, IA-2, IA-2(1), IA-2(2), IA-3, IA-5, MA-4, PS-4, PS-5, CM-7, CM-14 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.PS-03 |
| Regulatory basis | HIPAA 164.308(a)(3)-(a)(4), 164.312(a), (d) (N62-R01); FD&C Act 524B(b)(2) (N31-33-R05); FDA premarket guidance Appendix 1 (authentication and authorization; nonbinding) |
| Supporting standards | STD-06 Authenticator and privileged access; STD-04 OT security |

## 1. Purpose
Make sure only authorized people, services, and devices can reach company systems, the PHI the company holds for hospitals, the signing and provisioning paths, and the functions of shipped devices, and only to the extent their role requires.

## 2. Scope
All company systems in the Device Lifecycle Platform (SSP, P02), including plant floor stations, the CCC, the build and signing service, and the service and factory functions of shipped devices. It covers workforce, contractors, vendors, and hospital users of the CCC.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Director | Owns this policy; runs the identity provider and access reviews |
| System owners (Director of Cloud Operations, VP Engineering, Plant Manager, VP QA/RA) | Approve access to their systems; review access each quarter |
| Product Security Manager | Device credential and certificate design; signing approvals |
| HR Director | Timely notice of hires, transfers, and terminations |
| OT Engineering Manager | Plant floor accounts and vendor access to OT |
| All workforce | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user of a company system must have a unique identity. Shared operator logins on MES terminals and test stations must be replaced by individual badge-based login by 2027-03-31; until then, shared passwords must be changed whenever an operator with the password leaves. (IA-2; AC-2; PR.AA-01; 164.312(a)(2)(i))
4.2 Access must be approved by the system owner, limited to what the role needs, and granted through role groups in the identity provider where the system supports it. (AC-2; AC-3; AC-6; PR.AA-05; 164.308(a)(4)(ii)(B))
4.3 MFA is required for all workforce access to company systems. Administrators of the cloud, identity provider, repositories, signing service, and CCC must use phishing-resistant authenticators. (IA-2(1); IA-2(2); PR.AA-03; 164.312(d))
4.4 Privileged access to CCC production, the signing service, and the identity provider must be just-in-time, time-limited, approved, and logged. No one may hold standing write access to all hospital tenants after 2026-12-31. (AC-6(5); AC-2; PR.AA-05; 164.308(a)(4))
4.5 System owners must review access to the CCC, the landing zone, repositories, the signing service, PLM, eQMS, and the MES each quarter and remove access that is no longer needed. (AC-2; PR.AA-05; 164.308(a)(4)(ii)(C))
4.6 HR events drive access: accounts are disabled on the day of termination; prior roles are removed within 5 business days of a transfer. (PS-4; PS-5; AC-2; 164.308(a)(3)(ii)(C))
4.7 Release signing requires two approvers in the HSM. No one may author, approve, and sign the same release, and no one may change and release test station software without a second reviewer. (AC-5; CM-14; PR.AA-05; 524B(b)(2))
4.8 Vendor and remote administrative access must go through the privileged access broker, be approved per session, and be recorded. Persistent vendor VPNs into the plant OT network are prohibited after 2026-12-31. (AC-17; MA-4; PR.PS-03; 164.312(e)(1))
4.9 **Device credentials.** Shipped devices must not contain shared, default, or hardcoded credentials. Service and factory modes must be disabled before shipment and must require a per-device credential or a signed service token to enable. Final test must verify the disabled state and record it in the device history record. (IA-5; IA-3; CM-7; PR.AA-01; 524B(b)(2))
4.10 Devices must authenticate to the CCC with unique certificates. Per-hospital shared keys (VM-5) must be rotated at least yearly until the product reaches end of support. (IA-3; IA-5(2); PR.AA-04)
4.11 Break-glass accounts for the cloud organization, identity provider, and CCC must be sealed, stored offline, and tested each quarter. (AC-2; 164.312(a)(2)(ii))
4.12 Passwords and other authenticators must meet STD-06. (IA-5; 164.308(a)(5)(ii)(D))

## 5. Compliance and enforcement
The IT Director reports quarterly on access review completion, privileged access exceptions, and break-glass tests. Violations are handled under POL-01 section 4.11.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. Statement 4.9 has no exceptions for new shipments.

## 7. Related documents
POL-01; STD-04; STD-06; SSP (P02); P07 findings for AC-2, AC-6, IA-5, MA-4
