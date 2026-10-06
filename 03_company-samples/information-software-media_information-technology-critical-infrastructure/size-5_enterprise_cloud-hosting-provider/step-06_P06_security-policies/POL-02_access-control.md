# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management |
| Approved by | Executive risk committee |
| Approval date | 2026-09-08 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-5, AC-6, AC-17, IA-2, IA-5, IA-12, PS-4, MA-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | FedRAMP (C-IT-R01) Class C and Class D AC, IA, PS controls; DFARS flow-down (C-IT-R03); HIPAA 164.312(a), (d) (business associate) |

## 1. Purpose
Make sure only authorized people and services reach company systems and customer resources, with the least privilege they need, and that privileged access to provider tooling is controlled tightly enough that one stolen session cannot change many customers.

## 2. Scope
All workforce, contractor, supplier, service, and automation identities; all regions, G1, corporate IT, the legacy AQ-1 directory and RMM tool until retired, and SaaS. Customer identities in the customer identity service are governed by customers; this policy covers the company's controls over that service.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Policy owner; runs the workforce identity platform and PAM |
| System owners | Approve role definitions and certify access quarterly |
| Chief Human Resources Officer | Sends hire, move, and termination events; confirms U.S.-person status for G1 roles |
| Managers | Request and certify access for their staff |
| Senior Vice President, Managed Infrastructure Services | Accountable for AQ-1 technician access until migration |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every person and service must use a unique identity; shared accounts are prohibited except break-glass accounts under PRC-02.4. (AC-2; IA-2; PR.AA-01)
4.2 Workforce access must be granted from role templates approved by the system owner, provisioned through identity governance, and certified quarterly for privileged roles and semiannually for other roles. (AC-2; AC-6; PR.AA-05)
4.3 All workforce access must use phishing-resistant MFA (FIDO2) through the workforce identity platform. Other MFA methods are allowed only under an approved exception with an end date (STD-02.2). (IA-2; IA-2(1); IA-2(2); PR.AA-03)
4.4 Privileged access to production, G1, and provider tooling must be just-in-time through PAM, time-limited, session-recorded, and re-authenticated at elevation. Standing privileged grants are prohibited. (AC-6; AC-2(11); AC-17; PR.AA-05)
4.5 Duties must be separated so that no one person can author, approve, and release a change to production or provider tooling. (AC-5; PR.AA-05)
4.6 G1 roles may be granted only to U.S. persons verified by HR and identity-proofed under STD-02.2. (PS-3; IA-12; PR.AA-02)
4.7 Access must be disabled the same business day as termination for employees and contractors; contractor end dates must be held in identity governance. (PS-4; AC-2; PR.AA-05)
4.8 Operator access to customer resources requires a customer-approved access request, except under a declared incident with the CISO's approval, and must be logged and reported to the customer. (AC-3; AU-2; PR.AA-05)
4.9 Supplier and vendor remote access, including maintenance and diagnostics, must go through PAM with approval and session recording (STD-02.3). (MA-4; AC-17; PR.AA-05)
4.10 Default and vendor-supplied credentials must be changed before a device or service is connected; secrets must be stored in the approved vault and rotated per STD-02.2. (IA-5; PR.AA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote, Privileged, and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access (Just-in-Time) Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), the FedRAMP independent assessment, and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.6), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions to this policy follow the process in POL-01 section 7 and `policy-hierarchy.md` section 5 (PRC-01.2).

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 HCP-G SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
