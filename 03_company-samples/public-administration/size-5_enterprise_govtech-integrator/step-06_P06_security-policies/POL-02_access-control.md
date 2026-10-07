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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, acquisitions, or new CJISSECPOL versions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-7, AC-17, IA-2, IA-4, IA-5, IA-8, PS-3, PS-4, PS-6, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, GV.RR-04 |
| Key requirements | CJISSECPOL v6.1 AC-2, AC-7, IA-2(1), IA-2(2), PS-3; Pub. 1075 Exhibit 7 I(2); 45 CFR 164.308(a)(3)-(4), 164.312(a), (d) (AG-04 scope) |

## 1. Purpose
Make sure only screened, authorized people reach company systems and agency data, with the least access they need, strong authentication, and prompt removal.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and subcontractor staff) in every state and delivery center, including AQ-1 staff from the acquisition date. Covers all company systems, the hosted agency environments (ACMC, IES, legacy hosting, AQ-1), the CUI enclave, and all agency data the company receives, wherever it is stored or processed.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Owns this policy and the identity platform |
| System owners | Approve role templates; certify access quarterly |
| Director of Regulated Data Compliance | Screening and certification records for CJI and FTI access |
| Chief Human Resources Officer | Hiring, transfer, and termination events |
| Agency administrators (customer role) | Manage their own users in ACMC and IES under contract |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user must have a unique identifier; shared and generic accounts are prohibited, including for agency users. (IA-4; AC-2; PR.AA-01)
4.2 Access must be granted through role templates approved by the system owner and limited to what the role needs; administrative rights must be granted just in time through PAM, with no standing administrator rights. (AC-6; AC-2; PR.AA-05)
4.3 All workforce users must use MFA; privileged users must use phishing-resistant security keys. Agency users must authenticate through their agency identity provider with MFA or through local accounts that require MFA. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.4 Accounts must lock after 5 consecutive invalid attempts within 15 minutes and stay locked until an administrator releases them. (AC-7; PR.AA-03)
4.5 Access must be disabled the same business day as termination. Subcontractors must report terminations within 1 business day, and their access must be disabled on receipt. (PS-4; PS-7; AC-2; PR.AA-01)
4.6 System owners must certify workforce access quarterly and privileged access monthly. (AC-2; PR.AA-05)
4.7 Remote administrative access must go through the zero-trust access broker and PAM from company-managed devices, with sessions recorded. (AC-17; PR.AA-05)
4.8 Service credentials must be stored in the secrets manager; default vendor passwords must be changed before a device is connected, and default-credential scans must run quarterly. (IA-5; PR.AA-01)
4.9 Break-glass accounts must be sealed, monitored, and tested quarterly. (AC-2; PR.AA-05)
4.10 No one may access CJI until a fingerprint-based check is complete, the CJIS Security Addendum certification page is signed and held by the agency, and CJIS training is complete. No one may access FTI until the Pub. 1075 background investigation, penalty notice, and disclosure awareness training are complete. (PS-3; PS-6; AT-2; GV.RR-04)
4.11 Support access to CJI, FTI, and ePHI tenants must be scoped to one tenant, linked to a ticket, and granted just in time. (AC-3; AC-6; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Break-Glass Access Procedure
- PRC-02.5 CJIS and FTI Screening Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and agency audits (CJIS audits, IRS safeguard reviews). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. No exception may be granted against a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term, or a statute.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ACMC SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; agency contracts; CJIS Security Policy v6.1; IRS Publication 1075.
