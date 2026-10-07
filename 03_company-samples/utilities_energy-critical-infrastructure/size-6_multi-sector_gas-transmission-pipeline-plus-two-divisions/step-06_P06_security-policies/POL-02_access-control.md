# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director and the Group OT Security Director) |
| Approved by | Group CISO, under authority of POL-01, 2026-09-22 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(9), AC-17, AC-17(1), AC-20, IA-2, IA-2(1), IA-2(2), IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, DE.CM-06 |
| Regulatory drivers | C-ENERGY-R03 (SD 02G III.C.1 to III.C.5); N21-BM (PR.AA-01, PR.AA-03, PR.AA-05); SSI 1520.9(a)(2) |
| Division supplements | Gas Transmission: control room console access and station unit control panel accounts. Gathering and Production: field device commissioning and cellular gateways. Integrity Services: client tenant administration and engineer access to client and group data |

## 1. Purpose
Make sure only authorized people and processes reach group IT and OT systems and data, and only to the extent their job and the data's need-to-know require.

## 2. Scope
All workforce identities, service accounts, administrator accounts, shared operational accounts, vendor and authorized representative identities, and the external identities (shippers, Integrity Data Platform client users) that group systems authenticate, in every division and in corporate shared services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (directory, sign-in, MFA, PAM, identity governance) as a common control |
| Group OT Security Director | Runs the OT remote access gateway and OT account standards |
| Data and system owners | Approve access to their systems and to SSI sets (need-to-know) |
| Managers | Request and certify their staff's access every quarter |
| Group HR and division HR | Record joiners, movers, and leavers the same day |
| Station and field supervisors | Control shared operational accounts at their sites |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared accounts are prohibited except on OT components where they are critical for operations and no alternative exists. Each shared account must be listed in the shared account register with its owner, its users, and the compensating controls. (IA-2; AC-2; PR.AA-01; SD 02G III.C.4)

4.2 **Shared operational accounts.** Access to a shared account must be limited to the people who need it. Its password must be changed when anyone who knew it leaves or no longer needs it, and in any case on the schedule in 4.3. (AC-2; IA-5; SD 02G III.C.4.a, III.C.4.b)

4.3 **Password resets.** Memorized secrets on Critical Cyber Systems must be reset on the schedule in the TSA implementation plan. For a component that cannot be reset on schedule, the owner must document mitigations and a completion date, and a missed date must be reported under POL-01 4.7. (IA-5; SD 02G III.C.1.a, III.C.1.b)

4.4 **Default credentials** must be changed before any device is connected to a group network. Field devices (RTUs, PLCs, wellhead controllers, flow computers, cellular gateways) must pass a commissioning checklist that confirms this. (IA-5; CM-6; PR.AA-01)

4.5 MFA is required for all workforce access to SSO applications and for every remote session. Administrators must use phishing-resistant authenticators. Where MFA is not used on control room consoles, the division must document compensating controls (staffed room, badge and PIN entry, video, application allowlisting) in its TSA plan or supplement. (IA-2(1); IA-2(2); PR.AA-03; SD 02G III.C.2)

4.6 Access must be role-based and least privilege, with separation of duties for changes to OT logic and setpoints. Standing access to another division's OT networks, historians, or data is prohibited; time-limited access for an approved project is allowed. (AC-3; AC-6; PR.AA-05; SD 02G III.C.3)

4.7 **OT remote access** must go only through the OT remote access gateway, using a division-specific tier, named accounts, MFA, and session recording. Vendor and integrator access must be enabled per session and approved by the system owner. Persistent or always-on vendor connections are prohibited. (AC-17; AC-17(1); MA-4; DE.CM-06)

4.8 Privileged access must be granted just in time through PAM, with approval and session recording. Use of privileged functions must be logged. (AC-6(5); AC-6(9))

4.9 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Contractor and authorized representative accounts must expire at the engagement end date. (PS-4; AC-2)

4.10 Managers and system owners must certify access every quarter, including privileged accounts, OT gateway accounts, shared account registers, and service accounts. (AC-2; PR.AA-05)

4.11 **Domain trusts** must be reviewed at least annually. No trust may exist between corporate and OT domains, and no server that receives data from an OT DMZ may be administered by corporate directory administrators. (AC-3; CA-3; SD 02G III.C.5, III.B.2.a)

4.12 **External identities.** Shipper accounts on the nominations platform and client users of the Integrity Data Platform must be offered MFA. MFA must be required for client administrators now and for all client users by 2027-03-31. (IA-8; IA-2; PR.AA-03)

4.13 Physical access to control rooms, compressor stations, data centers, and OT equipment rooms must be badge-controlled and logged. (PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.12. Compliance is checked through the P07 assessment of SYS-G1 common controls and division samples, quarterly certification results, and the TSA Cybersecurity Assessment Plan.

## 6. Exceptions
Exceptions follow POL-01 section 4.11. No exception may extend a TSA plan date without POL-01 4.7.

## 7. Related documents
POL-01; POL-04 (SSI need-to-know); `division-supplements.md`; common control catalog entries for SYS-G1 (P02); P04 cloud control map.
