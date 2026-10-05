# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | Security Manager, with the SCADA and Automation Manager for OT statements |
| Approved by | Chief Operating Officer, with the VP Operations agreeing to the OT statements |
| Approval date | 2026-09-16 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | AC-1, AC-2, AC-3, AC-4, AC-6, AC-6(2), AC-6(5), AC-7, AC-11, AC-17, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PE-2, PE-3, PS-4, PS-5, SC-7 |
| CSF 2.0 | PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.IR-01 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 5.2.2 (physical security), 5.2.3 (network architecture), 6.2.1 (identity and access), 6.2.10 (remote access) |
| Binding rules referenced | Fla. Stat. 501.171(2) (reasonable security measures for personal information) |
| Supporting standards | STD-04 Remote and third-party access standard; STD-06 Identity, authenticator, and privileged access standard; STD-01 Secure configuration, network, and encryption standard |

## 1. Purpose
Make sure only authorized people, vendors, and devices can reach company systems, the SCADA network, and field equipment, and only to the extent their job requires.

## 2. Scope
All workforce members, vendors, shippers, and service accounts with access to company systems at headquarters, the field offices, the OCC, the BCC, and field sites, and in all cloud and SaaS services. It covers SCADA servers, HMIs, engineering workstations, field controllers, flow computers, and every remote access path to them.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Managers and Field Superintendents | Request and approve access for their staff; complete quarterly access reviews |
| HR Director | Records hires, transfers, and terminations in the HR system on or before the effective date |
| VP IT | Runs the identity provider, provisioning, and privileged access management for IT and cloud |
| SCADA and Automation Manager | Provisions and removes SCADA, OT directory, and controller accounts; reviews them quarterly |
| OT Security Engineer | Runs the jump host and the OT DMZ; reviews vendor sessions weekly and IT/OT rules quarterly |
| OCC shift lead | Approves each vendor remote session to the SCADA network |
| Control Room Manager | Approves physical access to the OCC, BCC, and server rooms |
| Data owners (Production Accounting Director, Measurement Supervisor, Reservoir Engineering Manager) | Approve access to Restricted and Confidential data in their systems |
| Workforce and vendors | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account on every system, including SCADA HMIs and engineering workstations. Shared or generic accounts are prohibited. The shared engineering account on the South Florida and BCC HMIs must be replaced by named accounts from the OT directory by 2027-03-31; until then it is a documented exception with compensating controls (a shift sign-in log tied to badge records, and a monthly event review by the SCADA and Automation Manager), consistent with the SP 800-82 Rev. 3 OT overlay. (IA-2; AC-2; PR.AA-01)
4.2 Access must be role-based, least-privilege, and approved by the user's manager and, for Restricted or Confidential data, the data owner before it is granted. Controller programming rights are limited to named automation technicians and engineers. (AC-2; AC-3; AC-6; PR.AA-05)
4.3 MFA is required for email, SaaS applications, the corporate VPN, the cloud console, the OT jump host, the field data capture app, and the shipper portal. IT and cloud administrators must use phishing-resistant hardware keys, and SCADA server and engineering workstation administrators must do so by 2027-06-30. (IA-2(1); IA-2(2); PR.AA-03)
4.4 **Termination.** HR must record the termination on or before the last day. Identity provider access is disabled automatically that day, or immediately for involuntary terminations. SCADA local accounts, OT directory accounts, badges, and field gate combinations must be disabled or changed within 1 business day, and controller passwords known to the leaver within 5 business days. Contractor access ends on the contract end date. (PS-4; AC-2)
4.5 **Transfers.** Access from a prior role must be removed within 5 business days of a transfer unless the new manager approves keeping it. (PS-5; AC-2)
4.6 **Access reviews.** Managers must review their staff's access every quarter. The SCADA and Automation Manager must review all SCADA, OT directory, and controller accounts every quarter (annually before 2026-10). The Measurement Supervisor must review shipper portal accounts every quarter with each shipper's contact. Data owners must review access to Restricted data every quarter. (AC-2; AC-6; PR.AA-05)
4.7 **Privileged access.** Administrators must use a separate privileged account for administration. Cloud, directory, and identity provider administration must go through privileged access management with just-in-time elevation and session logging; SCADA server and engineering workstation administration must be added by 2027-06-30. No vendor or service account may hold standing administrator rights. (AC-6(2); AC-6(5))
4.8 Corporate accounts lock after 10 failed sign-in attempts, and corporate devices lock after 10 minutes idle. OCC HMIs are exempt from lockout and screen lock so alarms stay visible; the OCC must remain badge-controlled and staffed at all times. HMIs at the South Florida office and the BCC, which are not always staffed, must lock after 15 minutes idle. (AC-7; AC-11; PR.AA-03)
4.9 **Emergency access.** Break-glass accounts must exist for the identity provider, the cloud organization, and the SCADA servers at the OCC and the BCC. They must be sealed and stored offline, tested quarterly, and used only when normal access fails. Every use must be reviewed by the Security Manager (or, for SCADA, the SCADA and Automation Manager) within 1 business day. (AC-2)
4.10 Passwords must be at least 14 characters and must not appear on the banned-password list. Service account credentials must be vaulted and rotated at least annually. **Default passwords on any device (modems, cellular gateways, radios, controllers, drives, flow computers, network equipment) must be changed before the device is connected.** Vendor-wide shared passwords are prohibited on company equipment. Controller passwords must be unique per area and changed when anyone who knows them leaves. (IA-5; PR.AA-01)
4.11 **Vendor and remote access to OT.** Remote access to the SCADA network and to field devices is allowed only through the company jump host in the OT DMZ, with a named account and MFA for each person, per-session approval by the OCC shift lead, session recording, and disconnection when the work ends. Always-on vendor paths (cellular gateways, support modems, remote control tools) are prohibited. The existing exceptions (the compressor packager's gateways and the flow computer vendor's modem) must be removed by 2026-11-30, and their inbound internet access was blocked on 2026-08-13. (AC-17; MA-4; PR.AA-05)
4.12 **IT/OT boundary.** The SCADA network may connect to the corporate network and the cloud only through an OT DMZ with deny-by-default rules approved by the SCADA and Automation Manager: at the OCC today, and at the BCC and the South Florida office by 2027-03-31. No device may be connected to both networks at once. No field device, gateway, or modem may have a management interface reachable from the internet. The OT Security Engineer must review the IT/OT rule sets every quarter. (SC-7; AC-4; PR.IR-01)
4.13 **Physical access.** The OCC, the BCC, and server rooms are badge-controlled, with access approved by the Control Room Manager and reviewed quarterly. Field gate combinations must be changed at least quarterly and whenever a holder leaves. RTU and controller cabinets must be locked, and door switches must be fitted at each cabinet replacement. (PE-2; PE-3; PR.AA-06)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.8). Compliance is checked through the annual independent control assessment (P07), the quarterly access reviews, and the weekly review of jump host sessions.

## 6. Exceptions
Exceptions follow POL-01 section 4.10. Exceptions for OT systems require the VP Operations' agreement.

## 7. Related documents
POL-01; POL-05; STD-01; STD-04; STD-06; P02 control statements AC-2, AC-6, AC-17, IA-2, IA-5, MA-4, SC-7; P07 findings for AC-2, AC-17, IA-5, MA-4, PS-4, and SC-7
