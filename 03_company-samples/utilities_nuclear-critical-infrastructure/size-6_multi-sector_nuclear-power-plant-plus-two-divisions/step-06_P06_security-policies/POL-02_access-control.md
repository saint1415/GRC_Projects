# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (all divisions and corporate shared services) |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO; noted by the board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | AC-2, AC-2(3), AC-3, AC-6, AC-6(5), AC-17, AC-20, IA-2(1), IA-2(2), IA-3, IA-5, IA-8, PS-4, PS-5, PS-7 |
| CSF 2.0 | PR.AA-01, PR.AA-02, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory drivers | C-NUCLEAR-S01 (73.22(b)); C-NUCLEAR-S02 (73.56(b)(1)(ii), (m)); C-NUCLEAR-R04 (CIP-003-9, CIP-005-7); C-NUCLEAR-S06 (37.43(d)) |

## 1. Purpose
Make sure only the right people and devices reach group systems and information, for only as long as they need to, with special care for people who move between divisions.

## 2. Scope
All group business systems and every identity in SYS-G1, including cross-division, contractor, vendor, and customer identities. Access to CDAs, SGI stand-alone systems, the NERC CIP Electronic Security Perimeter, and the Part 37 vault security systems is governed by those programs, which must be at least as strict as this policy.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Operates SYS-G1, PAM, and identity governance; runs certifications |
| Division security and compliance leads | Approve division roles; certify division application access |
| Station IT managers | Operate station network access control and device checks |
| Outage managers and project managers | Report start and end of every cross-division assignment |
| SGI program owners; access authorization program managers; Radiation Safety Officers | Approve access to SGI, access authorization files, and Part 37 information |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared accounts are prohibited, including vendor and OT support accounts. (AC-2; IA-2; PR.AA-01)

4.2 Access must be role-based and least privilege. Access to CDA work packages and other cyber security sensitive information is limited to roles approved by the fleet cyber security program manager. (AC-3; AC-6; PR.AA-05)

4.3 MFA is required for all workforce access, all remote access, and all privileged access. Administrators must use phishing-resistant authenticators and just-in-time elevation through PAM. Customer administrator accounts on group customer portals must use MFA. (IA-2(1); IA-2(2); AC-6(5); IA-8; PR.AA-03)

4.4 **Cross-division access is assignment-bound.** A person from another division gets station business network and work management access only for a dated outage or project assignment entered in the outage schedule, and the access ends automatically when the assignment ends. Standing cross-division accounts are not allowed after 2027-03-31. (AC-2; AC-2(3); PS-5; PS-7; 73.56(b)(1)(ii))

4.5 **Devices.** Only group-managed devices that pass a device check may join a station business network. Division-managed laptops are placed in a contractor segment with no access to station server subnets. Personal devices are never allowed on station networks. (IA-3; AC-20; PR.IR-01)

4.6 Access must be removed within 4 hours of termination and on the day an assignment ends. Accounts unused for 45 days are disabled; outage logins do not reset the timer for accounts without a current assignment. (PS-4; AC-2(3))

4.7 Access to group systems must be certified quarterly by the business owner; privileged access and access to SGI, access authorization files, and Part 37 information must be certified monthly by the owning program. (AC-2; PR.AA-05)

4.8 **Information restricted by regulation** (SGI under 73.22(b); access authorization files under 73.56(k) and (m); Part 37 security plans and lists under 37.43(d)) may be accessed only by people the owning program has determined to have a need to know and the required trustworthiness and reliability determination. The determination must be documented before access is granted. (AC-3; PS-3; PS-6)

4.9 Default passwords must be changed before any device (including printers, scanners, HMIs, and network equipment) is connected to a group network. Devices are scanned for default credentials monthly. (IA-5; CM-6; PR.AA-01)

4.10 Vendor remote access must use named accounts, MFA, a ticket, a time limit, and session recording. Vendor access to OT, to the NERC CIP environment, and to low impact BES assets must also follow those programs (for example CIP-003-9 Attachment 1 Section 6). (AC-17; MA-4; PR.AA-03; DE.CM-06)

4.11 People with administrative control over station networks that border CSP-protected networks (for example station DMZ firewalls) must be reviewed each year for inclusion in the 73.56 critical group. (PS-3; 73.56(i)(1)(v)(B)(4))

## 5. Compliance and enforcement
Checked through quarterly certifications, monthly device scans, and P07 testing. Violations are handled under POL-01 4.9.

## 6. Exceptions
Under POL-01 4.12. No exception may allow SGI, access authorization files, or Part 37 information to be readable by people without a determination.

## 7. Related documents
POL-01; POL-04; division supplements; SYS-G1 standards; station CSPs; 10 CFR 73.22, 73.56; 10 CFR 37.43; CIP-003-9, CIP-005-7.
