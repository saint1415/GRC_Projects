# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | OT Security Manager (OT) and IT Director (IT) |
| Approved by | Chief Operating Officer (CIP Senior Manager) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy, which was written mainly for IT) |
| Review cycle | Annually (next review by 2027-09-30); CIP-003-9 R1 topics within 15 calendar months; and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | AC-2, IA-2, AC-6, PS-4, AC-17, AC-17(1), AC-17(3), IA-2(1), MA-4, AU-6, SI-4, AC-4, AC-3, SC-7, CA-9, AC-6(5), IA-5, PE-2, PE-3, AC-18 |
| CSF 2.0 | PR.AA-01, PR.AA-05, DE.CM-06, PR.IR-01, PR.AA-06 |
| Regulatory drivers | C-DAMS-R01 (FERC Security Program Rev. 3A); C-DAMS-R02 (18 CFR 12.10); C-DAMS-R03 (NERC CIP-003-9, CIP-012-2, EOP-004-4) where cited below |
| Supporting standards | See `standards-index.md` |

## 1. Purpose
Control who and what can reach company systems, with the strictest rules for the control systems that operate spillway gates and generating units.

## 2. Scope
All accounts, devices, and connections to corporate IT, the cloud landing zone, and the HCDMS, including OEM and RMOS client connections.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| OT Security Manager | OT accounts, jump hosts, vendor and client connections, OT access reviews |
| IT Director | Identity provider, corporate and cloud accounts |
| ROC Manager and Plant Managers | Approve operator access; approve each remote session to OT on shift |
| Corporate Security Manager | Physical access to control rooms, powerhouses, and gate houses |
| HR Director | Same-day termination notices to IT and OT |

## 4. Policy statements
Each statement ends with the SP 800-53 controls, CSF 2.0 subcategory, and regulatory driver it implements.

4.1 Every person must use a unique account. Shared or group accounts are prohibited on SCADA, HMIs, jump hosts, and firewalls; where a device cannot support unique accounts, the exception must be approved under POL-01 4.4 with physical and logging controls and listed in the OT asset inventory. (AC-2; IA-2; PR.AA-01; C-DAMS-R01 (Table 9.3b access control))
4.2 OT access is granted on the approval of the ROC Manager or Plant Manager for the role, and reviewed quarterly for operator and engineering accounts and monthly for administrator accounts. (AC-2; AC-6; PR.AA-05; C-DAMS-R01 (Table 9.3a access control (enforce access control policies)))
4.3 Access is removed by the end of the termination day for corporate, cloud, and OT accounts; shared device passwords known to the leaver are changed within 24 hours. (PS-4; AC-2; PR.AA-05; C-DAMS-R01 (Table 9.3a access control))
4.4 All remote access to OT, by staff or vendors, must go through the OT DMZ jump hosts with MFA, session approval by the ROC shift supervisor, and session recording. Direct VPNs to plant firewalls, cellular modems in control panels, and other remote paths are prohibited unless approved by the COO as an exception and listed in the connection register. (AC-17; AC-17(1); AC-17(3); IA-2(1); PR.AA-05; C-DAMS-R01 (Table 9.3a access control (remote and third-party); Form 3 Q12a); C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 6.1-6.2))
4.5 Vendor remote sessions to OT must be monitored for malicious communications and their activity logs reviewed at least weekly. Vendor access is enabled only for the approved session and disabled after it. (MA-4; AU-6; SI-4; DE.CM-06; C-DAMS-R01 (Form 3 Q12b-12c); C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 6.2-6.3))
4.6 RMOS client connections terminate in a separate RMOS zone and may reach only that client's objects in SCADA. Client users of the portal sign in with MFA and see only their own projects. (AC-4; AC-3; SC-7; PR.IR-01; C-DAMS-R01 (Table 9.3a access control and functional segregation; FAQ Q10))
4.7 OT networks are separated from corporate networks and the internet, and segmented by site and function. Only necessary inbound and outbound access is permitted at each asset with low impact BES Cyber Systems, with a documented reason for each rule; firewall rules are reviewed at least every 12 months. (SC-7; AC-4; CA-9; PR.IR-01; C-DAMS-R01 (Table 9.3a access control and functional segregation; Form 3 Q11, Q22); C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 3.1))
4.8 Privileged OT access uses separate administrator accounts, unique local administrator passwords stored in the vault, and least privilege. (AC-6; AC-6(5); IA-5; PR.AA-05; C-DAMS-R01 (Table 9.3b access control (least privilege)))
4.9 Default passwords must be changed before any device is connected, including field devices, modems, and panel web interfaces. Passwords for SCADA and jump hosts have at least 14 characters. (IA-5; PR.AA-01; C-DAMS-R01 (Table 9.3b access control (passwords); Form 1 Q6, Q9))
4.10 Physical access to control rooms, powerhouses, gate houses, firewall rooms, and instrument houses is limited to authorized people, reviewed quarterly, and logged. (PE-2; PE-3; PR.AA-06; C-DAMS-R01 (Table 9.3a general (physical security)); C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 2))
4.11 Wireless and cellular connections to OT require a risk assessment and approval before installation and must appear in the connection register. (AC-18; PR.IR-01; C-DAMS-R01 (Table 9.3a general (wireless); Table 9.3b wireless))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly OT access reviews, NERC compliance evidence reviews by the NERC Compliance Manager, and metrics reported to the audit committee. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions must be requested in writing, risk-rated, approved under POL-01 4.4, recorded in the risk register, and limited to 12 months. No exception may waive a FERC or NERC requirement.

## 7. Related documents
POL-01; STD-01 OT network segmentation and remote access; STD-04 OT access, account, and authenticator standard; STD-12 physical security of cyber assets; CIP-003 plan
