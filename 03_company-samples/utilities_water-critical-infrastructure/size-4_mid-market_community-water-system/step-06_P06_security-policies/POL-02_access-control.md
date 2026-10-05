# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Director (security officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-5, AC-6, AC-6(2), AC-6(5), AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-3, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| Regulatory drivers | SDWA section 1433, 42 U.S.C. 300i-2(a)(1)(A)(ii) and (b)(1) (C-WATER-R01); Fla. Stat. 501.171(2) |
| Supporting standards | STD-01 OT security; STD-04 Authenticator and privileged access; STD-08 Vendor and OT remote access |

## 1. Purpose
Make sure that only authorized people and processes can reach company systems and data, with the least access they need, and that every control action on the water system can be traced to a person.

## 2. Scope
All accounts on all systems: business IT, cloud and SaaS, and every OT component (HMIs, SCADA servers, engineering workstations, PLCs, RTUs, controllers, modems, and network devices) at every plant and site, including acquired systems. Covers employees, contractors, integrators, vendors, and service accounts. Covers physical access to plants, the ROC, and remote sites.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Director | Owns this policy; identity provider, gateway, privileged access management |
| SCADA and Controls Engineering Manager | OT accounts, device credentials, and integrator access at the platform level |
| ROC Supervisor | Approves each vendor and integrator remote session into OT |
| Plant Managers | Approve OT access for their plants; run key control at their sites |
| HR Director | Sends terminations and transfers the same day; termination checklist includes OT accounts |
| Security Manager | Quarterly access reviews; monitoring of remote sessions |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are prohibited, including on HMIs and engineering workstations. Named HMI accounts must be in place at Lakes and Ridge by 2026-12-31 and at the small systems by 2027-03-31; until then, shared logins are recorded as a time-limited exception with shift logs as a compensating control. (IA-2; AC-2; PR.AA-01)
4.2 MFA is required for all remote access to OT, all remote access to business systems, and all privileged access. Administrators and integrators must use phishing-resistant authenticators by 2027-03-31. (IA-2(1); IA-2(2); PR.AA-03)
4.3 **Remote access to OT is allowed only through the OT remote access gateway**, with MFA, per-session approval by the ROC Supervisor (or the Plant Manager for a client-requested session), session recording, access limited to named targets, and automatic termination at the end of the approved window. Always-on remote agents, direct VPNs into control networks, and vendor-owned remote tools are prohibited. (AC-17; MA-4; PR.AA-05; DE.CM-06)
4.4 Access must follow least privilege. Operators hold operate rights; only named SCADA engineers hold engineering rights. Integrators may write logic, but loading it to a controller needs company approval through change control. (AC-6; AC-5; PR.AA-05)
4.5 Access must be requested through a ticket and approved by the system owner (for OT, the Plant Manager). All accounts, including OT local accounts, must be disabled within 24 hours of termination, and within 1 hour for involuntary terminations of staff with OT or administrator access. Transfers must remove prior access within 5 business days. (AC-2; PS-4)
4.6 Access to OT, to privileged roles, and to Restricted and Confidential data systems must be reviewed every quarter by the system owner. Other access is reviewed every year. (AC-2; PR.AA-05)
4.7 Default and commissioning credentials must be changed before any device is connected. Device and service credentials must be stored in the company vault and rotated as STD-04 requires. Passwords must not be kept in spreadsheets or with integrators. (IA-5; PR.AA-01)
4.8 Administrators must use separate privileged accounts, elevated through privileged access management with just-in-time access and recorded sessions, for all administration planes (cloud, directory, SaaS, firewalls, gateway, and SCADA servers) by 2027-03-31. (AC-6(2); AC-6(5))
4.9 Service accounts must be non-interactive, vaulted, and rotated at least annually or use managed identities. Non-expiring passwords require a documented exception. (IA-5; AC-2)
4.10 Physical access to plants, the ROC, and control rooms requires a badge, reviewed quarterly. Keys to small-system sites and control panels must be inventoried, issued by name, and changed when a key is lost or a key holder leaves. Panels must be locked when unattended. (PE-3; PR.AA-06)
4.11 Break-glass accounts for the identity provider, cloud, gateway, and SCADA servers must be sealed, stored offline, and tested every quarter. Any use alerts the Security Manager. (AC-2)
4.12 **Control room HMIs.** Operator HMIs in staffed, badge-controlled control rooms may stay unlocked so that alarms are never missed, as the SP 800-82 Rev. 3 OT overlay allows. Engineering workstations and remote sessions lock after 15 minutes. (AC-11; AC-7)

## 5. Compliance and enforcement
Checked through quarterly access reviews, gateway session reviews, and the annual assessment (P07). Violations are handled under POL-01 statement 4.8.

## 6. Exceptions
Under POL-01 statement 4.7. Every remote access exception must be approved by the COO and expires within 90 days.

## 7. Related documents
POL-01; POL-05; STD-01; STD-04; STD-08; SSP (P02) sections 10 and 11; P08 runbooks
