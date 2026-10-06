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
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-6, IA-2, IA-2(1), IA-8, AC-2(12), AT-3, PS-4, AC-5, IA-5, AC-17, MA-4, IA-12, AC-3, CM-6 |
| CSF 2.0 | PR.AA-05, PR.AA-03, PR.AA-02, PR.AA-01 |
| Binding rules served | FAR 52.204-21(b)(1)(i)-(ii); FAR 52.204-21(b)(1)(v)-(vi); Fla. Stat. 501.171(2); E-Verify MOU Art. II.A.3; FAR 52.204-21(b)(1)(iii); N56-R03 (8 CFR 274a.2(g)(1)(i)); N56-R02 (15 U.S.C. 1681b(b)) |

## 1. Purpose
Make sure only the right people, services, and devices reach the firm's systems and data, with the least access they need, and that the identity checks protecting money and records (associate bank changes, help desk resets, client integrations) cannot be defeated with information criminals already hold.

## 2. Scope
All Cris Santos Company internal employees, contractors, and temporary associates while they use company systems (the associate app, time clocks, kiosks), at all of its about 520 sites in 38 states and the District of Columbia, including acquired firms from their acquisition date. Covers all systems and data, including cloud, colocation, SaaS, and systems that vendors operate for the firm, and the services the firm offers to clients (SL-1 Workforce Management Platform and SL-2 payrolling).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of Identity and Access Management | Identity platform, account lifecycle, PAM, certifications |
| System owners | Approve role templates and certify access quarterly |
| Senior Vice President, Payroll and Associate Services | Associate bank-change verification and caller verification (STD-02.4, PRC-02.5) |
| Director of Employment Eligibility Compliance | E-Verify accounts (outside SSO) |
| Chief Human Resources Officer | Timely termination events from the HCM system |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Access must be granted on least privilege through identity governance role templates approved by the system owner. (AC-2; AC-6; PR.AA-05)
4.2 Workforce access to company systems must go through SSO with MFA; privileged users must use phishing-resistant keys through PAM. Systems that cannot use SSO (such as E-Verify) need an approved exception with compensating controls. (IA-2; IA-2(1); PR.AA-03)
4.3 Associates and other non-organizational users must sign in with app-based or phishing-resistant authentication, and every new or changed bank account must be confirmed out of band to the contact on file and held for 3 days before its first use (STD-02.4). (IA-8; AC-2(12); PR.AA-03)
4.4 Bank account, address, and MFA changes must not be made by phone on the strength of knowledge questions; callers must be verified through the app or a one-time code sent to the contact on file (PRC-02.5). (IA-8; AT-3; PR.AA-02)
4.5 Access must be disabled within 4 hours of a termination, including E-Verify and every system outside SSO. (AC-2; PS-4; PR.AA-01)
4.6 Access to tier-1 and SOX applications must be certified quarterly by the system owner, and other access semiannually. (AC-2; AC-6; PR.AA-05)
4.7 No person may both change pay rules and release payroll, or both approve and transmit bank or paycard files. (AC-5; PR.AA-05)
4.8 Service accounts and API keys must be unique to each integration and client, stored in the secrets vault, and rotated at least every 90 days; shared accounts for client integrations are prohibited. (IA-5; AC-2; PR.AA-01)
4.9 Remote and vendor access must use the zero-trust access service or the PAM vendor gateway with approval and session recording. (AC-17; MA-4; PR.AA-05)
4.10 MFA resets for privileged and payroll users must be verified by live video with the user's manager confirming identity. (IA-5; IA-12; PR.AA-02)
4.11 Form I-9 document images, E-Verify data, and consumer reports must be accessible only to onboarding, compliance, and screening roles for their region. (AC-3; AC-6; PR.AA-05)
4.12 Default passwords and PINs must be changed before any system or device, including time clocks and kiosks, goes into service. (IA-5; CM-6; PR.AA-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-02.1 Account Management Standard
- STD-02.2 Identification and Authentication Standard
- STD-02.3 Remote and Vendor Access Standard
- STD-02.4 Associate and Client Identity Standard
- PRC-02.1 Access Provisioning Procedure
- PRC-02.2 Access Certification Procedure
- PRC-02.3 Privileged Access Procedure
- PRC-02.4 Emergency (Break-Glass) Access Procedure
- PRC-02.5 Associate Bank-Change and Caller Verification Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), quarterly access certifications, and the fraud and KRI dashboards. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 ALPP SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
