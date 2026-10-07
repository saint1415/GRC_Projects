# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-02 |
| Owner | Group CISO (operated by the group identity director) |
| Approved by | Group CISO and Group Chief Privacy Officer, under authority of POL-01, 2026-09-17 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-6, AC-6(5), AC-6(7), AC-7, AC-11, AC-12, AC-17, AC-21, IA-2, IA-2(1), IA-2(2), IA-3, IA-5, IA-8, MA-4, PS-4 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01 |
| Regulatory drivers | C-COMMUNICATIONS-R01 (47 CFR 64.2005(a)(2); 64.2010(a)-(f)); N54-R04 (FAR 52.204-21(b)(1)(i)-(iii), (v)-(vi)); MNO customer contract remote access terms |
| Division supplements | Carrier: network element AAA standard; customer authentication standard. Engineering: MNO remote access standard. Tower: RMU and smart lock credential standard |

## 1. Purpose
Make sure only authorized people, processes, and devices reach group systems, networks, and data, and only to the extent their job and the data's permitted purpose require.

## 2. Scope
All workforce identities (including outsourced agents), service accounts, administrator accounts, network element and device accounts, tenant roles on shared platforms, and the external identities (customers, tenant crews) that group systems authenticate.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Runs SYS-G1 (sign-in, MFA, PAM, identity governance) as a common control |
| Carrier network engineering vice president | Runs network element AAA (TACACS+ and RADIUS) |
| Data owners | Approve access to their data; the Carrier CPNI compliance officer approves any affiliate access to CPNI |
| Managers | Request and certify their staff's access every quarter |
| Group HR, division HR, and vendor managers | Record joiners, movers, and leavers the same day, including outsourced agents |
| Service and device account owners | Keep each account's purpose, permissions, and credentials current |

## 4. Policy statements
4.1 Every user must have a unique identity in SYS-G1. Shared or generic accounts are prohibited on every system, including network elements, remote access gateways, and device management interfaces. A documented exception must have compensating controls and an end date. (IA-2; AC-2; IA-5; PR.AA-01; FAR 52.204-21(b)(1)(v))

4.2 Access must be role-based and least privilege. Access to another division's data, including Carrier CPNI, must name the permitted purpose and be approved by that data's owner (for CPNI, the Carrier CPNI compliance officer). Standing cross-tenant access on shared platforms is prohibited; time-limited access for an approved purpose is allowed. (AC-3; AC-6; AC-21; PR.AA-05; 47 CFR 64.2005(a)(2); 47 U.S.C. 222(c)(1))

4.3 MFA is required for all workforce access. IT administrators, network element administrators, and NOC staff must use phishing-resistant authenticators (NOC staff by 2027-03-31). (IA-2(1); IA-2(2); PR.AA-03; FAR 52.204-21(b)(1)(vi))

4.4 **Network elements.** Administration of routers, switches, OLTs, DSLAMs, SBCs, and other network elements must use named accounts through central AAA with MFA, from group jump hosts only. Local accounts must be sealed for break-glass use and their use reviewed within 1 business day. (AC-2; AC-17(3); IA-2; PR.AA-05)

4.5 **Termination.** Access must be disabled within 4 hours of the HR termination event, and immediately for involuntary terminations. Vendors must report outsourced agent and contractor leavers the same business day. (PS-4; AC-2)

4.6 Managers and data owners must certify access every quarter, including privileged, service, and tenant roles. (AC-2; AC-6(7))

4.7 Privileged IT access must be granted just in time through PAM, with approval and session recording. (AC-6(5); PR.AA-05)

4.8 Accounts must lock after 10 failed attempts. Workstations must lock after 10 minutes idle. Application sessions must end after the idle time in the division supplement (no more than 30 minutes). (AC-7; AC-11; AC-12)

4.9 **Remote access into group or customer networks** must go through brokered, recorded sessions with named accounts and MFA. Persistent site-to-site tunnels are prohibited unless approved as an interconnection with a written agreement. (AC-17; CA-3; MA-4; PR.IR-01)

4.10 **Customer authentication for CPNI.** Staff and systems must authenticate customers before disclosing CPNI as the Carrier customer authentication standard requires: call detail by telephone only after a password not prompted by biographical or account information, otherwise only by sending to the address of record or calling the telephone number of record; online access only after authentication without biographical or account information and then a compliant password; in-store access only with a valid photo ID; backup authentication without biographical or account information. Customers must be notified immediately of changes to passwords, backup authentication, online accounts, or the address of record. These rules apply equally to AI channels. (IA-8; IA-5; PR.AA-03; 47 CFR 64.2010(b)-(f))

4.11 **Device credentials.** Default or vendor-supplied passwords must be changed before any device (network element, RMU, smart lock, gateway) is connected. Devices must use certificates or unique credentials where the device supports them. (IA-5; IA-3; CM-6)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment of SYS-G1 common controls, the OSS/BSS, and division samples, and through quarterly certification results.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01; POL-04; `division-supplements.md`; common control catalog entries for SYS-G1 (P02); Carrier customer authentication standard.
