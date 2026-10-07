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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or product launches |
| Implements (SP 800-53 Rev. 5) | AC-1, IA-1, IA-2, AC-2, AC-6, IA-2(1), IA-2(2), AC-6(9), PS-4, AC-5, SC-12, AU-10, IA-5, AC-17, MA-4, CM-6, IA-3, SC-17 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory basis | FD&C Act 524B(b)(2) (N31-33-R05); HIPAA 164.308(a)(3), (a)(4), 164.312(a), (d) (business associate services) |

## 1. Purpose
Make sure only authorized people, services, and devices can reach company systems, code, signing keys, plant systems, and customer data, with the least access they need.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at every site: headquarters, the FL-1, MN-1, and TX-1 plants, the R&D centers, the RCM monitoring centers, and remote work, including the acquired infusion business from its acquisition date. Covers all systems and data, including cloud, colocation, SaaS, plant OT, the Device Software Factory, and systems that business associates, contract manufacturers, and other vendors operate for the company, and the products and services the company provides to customers and consumers (fielded devices, the DDC, the RCM service, and the consumer companion app).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Owns the identity platform and this policy |
| System owners | Approve role templates and certify access |
| Director of Build and Release Engineering | Signing groups and HSM access |
| Vice President, Manufacturing Systems | Plant MES and station access |
| Chief Human Resources Officer | HR events that drive joiners, movers, and leavers |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user must have a unique identity; shared or generic accounts are prohibited except documented service accounts with named owners. (IA-2; AC-2; PR.AA-01)
4.2 Access must be granted through identity governance using role templates approved by the system owner, with least privilege. (AC-2; AC-6; PR.AA-05)
4.3 MFA is required for all remote, administrative, and sensitive access, and for all access to source repositories, the signing portal, and PHI. (IA-2(1); IA-2(2); PR.AA-03)
4.4 Privileged access must be just in time through PAM with session recording; no standing administrator roles in production cloud accounts, build infrastructure, or HSMs. (AC-6; AC-6(9); PR.AA-05)
4.5 Access must be disabled the same business day as termination, and contractor access must end automatically on the contract end date. (PS-4; AC-2; PR.AA-05)
4.6 Access to PHI, source code, signing systems, and plant MES must be certified quarterly by the system owner. (AC-2; PR.AA-05)
4.7 Firmware signing requires two approvers from the product line's signing group, neither of whom submitted the request, through the HSM signing service (STD-02.4). No signing key may exist outside an HSM. (AC-5; SC-12; AU-10; PR.AA-05)
4.8 Service accounts and pipeline credentials must be short-lived or rotated at least every 90 days, and must not have write access to released artifacts. (IA-5; AC-6; PR.AA-01)
4.9 Vendor remote access must go through the zero-trust access service and PAM, be approved per session for plant OT, and be recorded. (AC-17; MA-4; PR.AA-05)
4.10 Default and vendor-supplied credentials must be changed before any system, station, fixture, or device is connected to a company network. (IA-5; CM-6; PR.AA-01)
4.11 Emergency (break-glass) accounts must be sealed, monitored, tested quarterly, and used only under PRC-02.4. (AC-2; PR.AA-05)
4.12 Devices and programming stations must authenticate with certificates from the manufacturing PKI; new products must not use shared or per-customer keys. (IA-3; SC-17; PR.AA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 Code Signing and Key Management Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 DSF-MES SSP; P08 runbook and notification matrix; P10 AI governance; applicable regulations listed in P03.
