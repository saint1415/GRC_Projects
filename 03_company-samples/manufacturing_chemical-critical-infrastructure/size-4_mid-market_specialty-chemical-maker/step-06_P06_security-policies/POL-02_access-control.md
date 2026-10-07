# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Information Security Manager (CySO) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy; now covers OT explicitly) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-2(3), AC-3, AC-5, AC-6, AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-5, PE-2, PE-3, PS-4, PS-5, MA-4 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.AA-06 |
| Regulatory drivers | C-CHEMICAL-R02 (33 CFR 101.650(a)(1)-(7), (f)(3), (i)(1)); 49 CFR 172.802(a)(2); 49 CFR 1520.9; C-CHEMICAL-R01 (voluntary benchmark) |
| Supporting standards | STD-01 OT Security; STD-08 Authenticator and Privileged Access |

## 1. Purpose
Make sure only authorized, identified people and devices can reach company systems, control systems, and sensitive information, with the least privilege they need, and that access ends when the need ends.

## 2. Scope
All accounts on IT, cloud, SaaS, and OT systems at all sites, including local accounts on DCS, SIS, PLC, HMI, terminal, and loading bay systems; loading bay driver cards; and vendor accounts on the OT remote access gateway.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Information Security Manager (CySO) | Owns this policy; reviews privileged access quarterly |
| IT Director | Identity provider, directory, privileged access vault, cloud roles |
| Controls Engineering Manager | OT accounts and roles at both plants; OT access reviews |
| HR Director | Joiner, mover, and leaver events, including OT accounts and driver cards on the checklist |
| Distribution and Fleet Manager | Driver card approvals for carriers and company drivers |
| Facility Security Officer | Physical access, TWIC, escorts |
| Managers | Approve access and review their staff's access each quarter |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are not allowed, except documented operator console positions until 2027-03-31 under an approved exception with compensating controls (staffed, badge-controlled control room; console logs). (IA-2; AC-2; 33 CFR 101.650(a)(6))
4.2 Users must keep separate credentials for critical IT and OT systems; an OT account may never reuse an IT password. (IA-2; IA-5; 33 CFR 101.650(a)(6))
4.3 Access must be approved by the user's manager and the system owner, and granted at the least privilege needed for the job. Recipe release and control logic loading require two different people. (AC-2; AC-5; AC-6; 33 CFR 101.650(a)(5))
4.4 Privileged and administrator accounts must be separate from everyday accounts, held in the privileged access vault where technically possible, and reviewed quarterly. (AC-6(5); PR.AA-05)
4.5 MFA is required for all access to IT systems, cloud consoles, and SaaS, and for every remote session into OT. Phishing-resistant authenticators are required for administrators and for remote sessions that can change control system configuration from 2027-03-31. Where MFA is not technically feasible, compensating controls must be documented and approved by the CySO. (IA-2(1); 33 CFR 101.650(a)(4))
4.6 Passwords must meet STD-08 (14 characters minimum where supported). Default passwords must be changed before any IT or OT device is used; where a default cannot be changed, compensating controls must be documented. (IA-5; 33 CFR 101.650(a)(2)-(3))
4.7 IT systems must lock accounts after 10 failed sign-in attempts. Operator consoles are exempt from lockout and screen lock for safety; the staffed control room compensates. (AC-7; AC-11; 33 CFR 101.650(a)(1))
4.8 Remote access to OT must go only through the OT remote access gateway, with a named account, MFA, per-session approval recorded in the gateway, and session recording. Third-party sessions must be reviewed monthly. Always-on remote tools are prohibited at both plants. (AC-17; MA-4; 33 CFR 101.650(f)(3))
4.9 Leavers' access must be removed the same day, including OT accounts and driver cards. Movers' prior access must be removed within 5 business days. (PS-4; PS-5; AC-2; 33 CFR 101.650(a)(7))
4.10 Managers and system owners must review user access quarterly; OT access, driver cards, and gateway accounts are included. (AC-2; PR.AA-05)
4.11 Physical access to control rooms, OT server rooms, rack rooms, SIS cabinets, and field I/O cabinets must be limited to an authorized list and logged. (PE-2; PE-3; 33 CFR 101.650(i)(1))
4.12 Access to SSI (the FSP, the Facility Security Assessment, the Cybersecurity Plan) and legacy CVI is limited to named people with a need to know. (AC-3; 49 CFR 1520.9)

## 5. Compliance and enforcement
Checked through quarterly access reviews, gateway session reviews, and the P07 assessment. Violations are handled under POL-01 4.8.

## 6. Exceptions
Under POL-01 4.7. The shared console exception (4.1) expires 2027-03-31.

## 7. Related documents
POL-01; POL-04; STD-01; STD-08; SSP (P02); FSP (SSI)
