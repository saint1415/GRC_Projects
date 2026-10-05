# Access Control Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-02 |
| Owner | IT Security Manager |
| Approved by | Site Vice President |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2022 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | IA-2, AC-2, PS-4, PS-5, IA-2(1), IA-2(2), AC-6, AC-6(2), AC-6(5), AC-17, MA-4, PS-3, AC-3, IA-5 |
| CSF 2.0 | DE.CM-06, GV.RR-04, PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-01 |
| Regulatory drivers | C-NUCLEAR-S06, C-NUCLEAR-S05, C-NUCLEAR-R04, C-NUCLEAR-S02, C-NUCLEAR-S04 |
| Supporting standards | STD-06 Authenticator and privileged access (see `standards-index.md`) |

## 1. Purpose
Make sure only authorized people, with the least access their jobs need, can use business systems and data, and that privileged and vendor access cannot be used as a path toward the CSP boundary.

## 2. Scope
All business network, cloud, and SaaS accounts, including employee, contractor, outage contractor, vendor, service, and administrator accounts. CDA access is governed by the CSP.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Security Manager | Owns this policy; privileged access management; access review program |
| IT Director | Account lifecycle and directory operations |
| Business system owners | Approve access to their systems and review it each quarter |
| HR Director | Accurate and timely hire, transfer, and termination data |
| Director of Security | Access authorization program decisions for people with electronic access in 73.56 scope |
| All users | Protect credentials; never share accounts |

## 4. Policy statements
4.1 Every user must have a unique account. Shared accounts are prohibited, including vendor accounts; where a system cannot support individual accounts, the exception needs compensating controls approved under POL-01 4.8. (IA-2; AC-2; PR.AA-01; C-NUCLEAR-S06)
4.2 Accounts are created only from an approved request or the HR feed, disabled on the HR termination date, and changed on transfer the same day, including removal of prior roles. Outage contractor accounts must carry an end date and be disabled within 5 days of demobilization. (AC-2; PS-4; PS-5; PR.AA-05; C-NUCLEAR-S06)
4.3 MFA is required for all remote access, email, cloud, and SaaS access, and for every administrator logon including site console logons. Administrators must use phishing-resistant authenticators by 2027-01-31. (IA-2(1); IA-2(2); PR.AA-03; C-NUCLEAR-S06)
4.4 **Privileged access.** No standing domain administrator rights. Administrator access is granted just in time through the privileged access broker, with separate administrator accounts that are never used for email or browsing. (AC-6; AC-6(2); AC-6(5); PR.AA-05; C-NUCLEAR-S06)
4.5 Access reviews: each quarter for privileged accounts, the WMS, CAP/EDMS, the access authorization enclave, and GDSR; at least annually for all other access. (AC-2; PR.AA-05; C-NUCLEAR-S05; C-NUCLEAR-S06)
4.6 **Vendor remote access.** Vendors connect only through named, time-limited accounts on the privileged access broker, with MFA and session recording, enabled per session by the system owner. For the dispatch network, vendor remote access must also meet CIP-003-9 Attachment 1 Section 6, including detection of malicious communications. (AC-17; MA-4; PR.AA-05; DE.CM-06; C-NUCLEAR-R04 (CIP-003-9 Att. 1 Sec. 6))
4.7 People whose duties let them act electronically on systems that could adversely impact safety, security, or EP must be in the access authorization program before they receive that access. (PS-3; GV.RR-04; C-NUCLEAR-S02 (73.56(b)(1)(ii)))
4.8 Access authorization files and other Restricted personal information are administered only by named enclave administrators; domain administrators have no inherited access. (AC-3; AC-6; PR.DS-01; C-NUCLEAR-S02 (73.56(m)); C-NUCLEAR-S04)
4.9 Break-glass accounts: two per critical system, sealed offline, tested quarterly, and reviewed after every use. (AC-2; PR.AA-05; C-NUCLEAR-S06)
4.10 Service account passwords must be vaulted and rotated at least annually and when an administrator with knowledge of them leaves. (IA-5; PR.AA-01; C-NUCLEAR-S06)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the metrics reported to the audit committee, and, for anything in 73.54 scope, the 73.55(m) program review. Violations are handled under POL-01 4.13.

## 6. Exceptions
Exceptions follow POL-01 4.8: written, risk-rated, approved by the right authority under POL-01 4.5, recorded in the risk register, and limited to 12 months. No exception may permit a known regulatory noncompliance.

## 7. Related documents
POL-01; STD-06 Authenticator and privileged access standard; P07 POAM-001, POAM-002, POAM-003, POAM-014
