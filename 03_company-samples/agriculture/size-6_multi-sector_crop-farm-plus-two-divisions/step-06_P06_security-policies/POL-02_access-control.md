# Access Control Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crop Farming, Food Processing, Farm Supply) and corporate shared services |
| Policy ID | POL-02 |
| Owner | Group CISO |
| Approved by | Group CISO, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | IA-2, AC-2, AC-2(1), IA-2(1), IA-2(2), AC-6(5), AC-6(9), PS-4, AC-2(3), AC-6(7), AC-17, MA-4, AC-17(1), IA-5, AC-7, AC-11, AC-2(5), AC-2(2), IA-8, SC-7, AC-4 |
| CSF 2.0 | PR.AA-01, PR.AA-05, PR.AA-03, DE.CM-06, PR.IR-01 |
| Division supplements | Crop Farming: OT access standard and seasonal accounts; Food Processing: contractor access to refrigeration controls; Farm Supply: card data environment and portal administrators |

## 1. Purpose
Make sure only authorized, identified people and devices can reach group systems and OT, with the least access they need, for only as long as they need it, including a seasonal workforce of about 11,500 people.

## 2. Scope
All group IT and OT systems, cloud accounts, the FMIS and other SaaS, harvest tablets, ROC SCADA, plant OT, and the legacy farm operations directory until it is retired.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group identity director | Operates SYS-G1 identity governance, MFA, and PAM |
| Division security and compliance leads | Approve division role catalogs; run quarterly certifications |
| OT security managers | Own OT account types, HMI tailoring, and vendor access to OT |
| Group HR director | Sends joiner, mover, leaver, season-start, and season-end events |
| Managers and crew supervisors | Request and confirm access for their staff |

## 4. Policy statements
4.1 Every user must have a unique, named account. Shared accounts are prohibited except HMI shift operator accounts approved by the OT security manager under the OT tailoring rules in 4.9. (IA-2; AC-2; PR.AA-01)

4.2 All accounts must be created, changed, and disabled through SYS-G1 identity governance driven by HR events. Systems that cannot federate (including the legacy farm operations directory until retired) must follow the same events by documented manual procedure within the same deadlines. (AC-2; AC-2(1); PR.AA-05)

4.3 MFA is required for all remote access, all privileged access (including OT domain administrators and engineering accounts), and all access to Restricted data. Administrators must use phishing-resistant MFA. (IA-2(1); IA-2(2); PR.AA-03)

4.4 Privileged access, including OT engineering and domain administration, must go through group PAM with just-in-time elevation and session recording. (AC-6(5); AC-6(9); PR.AA-05)

4.5 Access must be removed within 4 hours of termination. **Seasonal and H-2A workers' access must be disabled on the season-end date HR records for each crew.** (PS-4; AC-2(3); PR.AA-05)

4.6 Access to every application, OT system, and the FMIS tenant must be certified each quarter by the data or system owner. (AC-6(7); AC-2; PR.AA-05)

4.7 **Vendor and integrator remote access** must use named identities, MFA, and group PAM sessions approved for a defined window, to a managed jump host. Always-on vendor remote access tools are prohibited. (AC-17; MA-4; AC-17(1); DE.CM-06)

4.8 Default credentials must be changed before any device, including modems, gateways, and controllers, is connected; credentials for OT devices must be stored in the group vault. (IA-5; PR.AA-01)

4.9 **OT tailoring.** HMIs may stay signed in on shift accounts and may be exempt from lockout and screen lock only when the OT security manager documents the safety reason and compensating controls (badge-controlled rooms, CCTV, engineering changes under named accounts). (AC-7; AC-11; AC-2(5); PR.AA-05)

4.10 Each critical system, including ROC SCADA and plant OT, must have sealed break-glass accounts tested every quarter. (AC-2(2); PR.AA-05)

4.11 Customer-facing services (the Grower Agronomy Portal, e-commerce) must offer MFA, and must require it for cooperative and customer administrators. (IA-2; IA-8; PR.AA-03)

4.12 Network access to OT is allowed only through approved paths: from the OT DMZ, from managed engineering workstations, or through group PAM. No system on a corporate or cloud network may open connections directly into an OT network. (SC-7; AC-4; PR.IR-01)

## 5. Compliance and enforcement
Compliance is checked through the annual common control assessment and division samples (P07), quarterly access certifications, the annual supplement attestations, and OT change reviews. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions follow POL-01 4.11. OT exceptions also need the division OT security manager's written safety reasoning.

## 7. Related documents
POL-01; POL-05; Crop Farming and Food Processing supplements (`division-supplements.md`); SYS-G1 runbooks.
