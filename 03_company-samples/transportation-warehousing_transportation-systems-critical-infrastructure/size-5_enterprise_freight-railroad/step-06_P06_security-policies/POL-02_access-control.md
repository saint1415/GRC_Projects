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
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-17, IA-1, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05 |
| TSA / regulatory basis | SD 1580/82-2022-01E Sec. III.C (all paragraphs) |

## 1. Purpose
Make sure only authorized people, devices, and processes reach the company's systems, and only to the extent their role requires, so that no one can issue movement authority, change a train control configuration, or reach OT without approval, and access ends promptly when it is no longer needed.

## 2. Scope
All employees and contractors at the 64 railroads, including acquired railroads from their closing date; all IT and OT systems, including the TDPB (CAD, PTC back office, CTC code servers), the OT directory, wayside and field devices, cloud, SaaS, and vendor-operated systems; and SL-1 and SL-2 customer users.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-06), PAM, and identity governance |
| Director of OT Security | Owns access rules for OT, the OT directory design, and shared-account exceptions |
| Managers and system owners | Approve access; complete quarterly certifications |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events |
| Vice President, Integration Management Office | Brings acquired railroad identities onto the identity platform |
| Customer administrators (SL-1, SL-2) | Manage their own staff's accounts under service agreements |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user and service must have a unique identity. Shared accounts are prohibited unless critical for operations and approved under STD-02.4; their passwords must be changed whenever a person with knowledge no longer needs access. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties must be separated so that no one person can both issue movement authority and change territory tables or CAD configuration, or both administer PTC servers and hold PTC cryptographic keys. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all privileged access, all cloud administration, and all customer access to SL-1 and SL-2. Privileged users must use phishing-resistant authenticators. Where OT components cannot support MFA, the compensating controls in the CIP apply. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Accounts inactive for 45 days must be disabled automatically; customer accounts inactive for 90 days must be disabled. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter, and customer administrators must attest to their users quarterly. (AC-2; PR.AA-05)
4.8 Privileged access to Critical Cyber Systems must be checked out through PAM for each session, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote maintenance access, including OT and wayside vendors, must go through the PAM gateway with approval and session recording. Vendor-owned modems or always-on remote tools on company OT networks are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device is connected, and memorized secrets must follow STD-02.2, which sets reset criteria in line with NIST SP 800-63B. (IA-5; PR.AA-01)
4.11 Directory and domain trust relationships must be inventoried, justified, and reviewed at least annually under STD-02.4; trusts from the corporate directory into the OT directory are prohibited. (AC-2; CA-3; PR.AA-05)
4.12 Two sealed break-glass accounts per critical platform must exist, be tested quarterly, and have every use reviewed by the Director of Security Operations. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote, Vendor, and External System Access Standard
- STD-02.4 OT Access, Shared Account, and Trust Relationship Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), and access certifications. Violations are handled under PRC-01.1 (POL-01 statement 4.7).

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Exceptions for shared accounts or MFA on Critical Cyber Systems must match the compensating controls stated in the CIP.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 TDPB SSP; P08 runbook; applicable regulations listed in P03.
