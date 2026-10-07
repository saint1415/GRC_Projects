# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Director of Identity and Access Management (with the Director of OT Security for OT access) |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-4, AC-5, AC-6, AC-7, AC-11, AC-17, IA-1, IA-2, IA-2(1), IA-5, IA-8, MA-4, PS-4, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 5.2.3 (network segmentation), 6.2.1 (identity and access), 6.2.10 (remote access) |

## 1. Purpose
Make sure only authorized people, services, and devices reach company information, the SCADA platform, and field devices, only to the extent their role requires, and that access ends promptly when it is no longer needed.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary workers, including the roughly 4,000 contractor workers on company sites on a typical day) at headquarters, the IOC, the BCC, the Florida regional control room, 60 field offices and yards, and every well site and facility in the Permian, Mid-Continent, and Florida operating areas, including acquired assets (AQ-MC) from the date of closing. Covers all business IT and OT systems and data, including cloud, colocation, SaaS, field devices and communications, systems that vendors operate for the company, and the services the company offers to outside parties (SL-1 owner and partner services; SL-2 water services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Runs the identity platform (SYS-05) and identity governance |
| Director of OT Security | Owns the OT identity domain rules, SCADA account procedure (PRC-02.5), and the OT remote access gateway |
| Managers and system owners | Approve access; complete quarterly certifications |
| Production Controller shift leads | Approve each vendor session into SCADA (PRC-02.6) |
| Chief Human Resources Officer | Timely joiner, mover, and leaver events, including contractors |
| Vice President, Integration Management Office | Brings acquired identities and networks onto enterprise platforms |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Every user, service, and device must have a unique identity. Shared accounts are prohibited, except HMI operator stations in badge-controlled control rooms where the SCADA software cannot switch users safely; each such exception must be registered with compensating controls (shift sign-in log, room access control, monthly event review), consistent with the SP 800-82 Rev. 3 OT overlay. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the manager or system owner before it is granted. Controller programming rights are limited to named automation technicians and engineers. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 Duties that could let one person change and approve controller logic, or change owner bank details and release a payment run, must be separated in role design. (AC-5; PR.AA-05)
4.4 MFA is required for all remote access, all cloud and administrative access, all access to the OT DMZ and the OT remote access gateway, and all portal access by owners, partners, and SL-2 customers. Privileged users must use phishing-resistant authenticators. (IA-2(1); IA-2(2); IA-8; PR.AA-03)
4.5 Access, including OT domain and local SCADA accounts, must be disabled the same business day as a termination, and immediately for involuntary terminations. (PS-4; AC-2; PR.AA-05)
4.6 Accounts inactive for 60 days must be disabled automatically, except sealed break-glass accounts. (AC-2(3); PR.AA-05)
4.7 Managers must certify their staff's access every quarter, and the Director of OT Security must certify all OT domain, SCADA, and controller accounts every quarter. (AC-2; PR.AA-05)
4.8 Privileged access must be granted just in time through PAM, recorded, and limited to the approved window. (AC-6; AC-6(9); PR.AA-05)
4.9 Vendor and remote access to OT, including drive, compressor, and SCADA vendors, must go through the OT remote access gateway with a named account, MFA, approval of each session by the shift lead, and session recording. Vendor cloud services must not write setpoints unless the path runs through the gateway and the Director of OT Security approves it. Always-on vendor tools are prohibited. (AC-17; MA-4; PR.AA-05)
4.10 Default passwords must be changed before any device (modem, radio, controller, flow computer, drive, network equipment) or system is connected, and no field device may have a management interface reachable from the internet. (IA-5; SC-7; PR.AA-01)
4.11 The SCADA networks must connect to corporate networks, the cloud, and acquired networks only through an OT DMZ with deny-by-default rules approved by the Director of OT Security. No device may connect to both networks at once. (SC-7; AC-4; PR.IR-01)
4.12 Two sealed break-glass accounts per critical platform, including the SCADA platform and the OT identity domain, must exist, be tested quarterly, and have every use reviewed by the Director of OT Security or the Director of Identity and Access Management. (AC-2; PR.AA-05)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard (includes OT domain and local SCADA accounts)
- STD-02.3 Remote and Vendor Access Standard (IT and OT)
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 SCADA Account Management Procedure
- PRC-02.6 OT Vendor Session Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT monitoring at the control centers), the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Contractor violations are handled under the contractor's agreement and can end site access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. OT exceptions also need the Director of OT Security's sign-off.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FSPA SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; NIST SP 800-82 Rev. 3.
