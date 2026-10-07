# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-2, AT-3, CM-10, CM-11, AC-11, AC-19, AC-20, AU-6 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.PS-05, DE.CM-03 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 sections 3.3.5 (training), 6.2.2 (awareness and training) |

## 1. Purpose
Set the rules every workforce member and contractor follows when using company systems, field devices, tablets, and phones, and when handling company information.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary workers, including the roughly 4,000 contractor workers on company sites on a typical day) at headquarters, the IOC, the BCC, the Florida regional control room, 60 field offices and yards, and every well site and facility in the Permian, Mid-Continent, and Florida operating areas, including acquired assets (AQ-MC) from the date of closing. Covers all business IT and OT systems and data, including cloud, colocation, SaaS, field devices and communications, systems that vendors operate for the company, and the services the company offers to outside parties (SL-1 owner and partner services; SL-2 water services).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; acknowledgments and training records |
| Managers and field superintendents | Make sure staff and contractors complete training before access |
| Director of OT Security | Role-based OT training content |
| All workforce and contractors | Follow this policy and report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems are for company business; limited personal use is allowed on corporate devices if it creates no risk. No personal use is allowed on HMIs, engineering workstations, or OT networks. (PL-4; GV.PO-01)
4.2 Every workforce member and contractor must acknowledge this policy before receiving access and every year after. (PL-4(1); PR.AT-01)
4.3 Security awareness training is required at hire and annually. Production Controllers, automation technicians and engineers, OT vendors' named staff, and disclosure committee members must complete role-based training before access and annually. (AT-2; AT-3; PR.AT-02)
4.4 Removable media and personal devices must not be connected to HMIs, engineering workstations, or controllers; software and media move into OT only through the OT DMZ scanning station. (CM-11; MP-7; PR.PS-05)
4.5 Users must not install software or connect storage devices to corporate endpoints unless IT approves it. (CM-11; PR.PS-05)
4.6 Field tablets and phones must be enrolled in device management and reported lost within 4 hours so they can be wiped. (AC-19; PR.DS-01)
4.7 Only AI tools on the approved list (STD-05.3) may be used for company work; Restricted data may be entered only into tools approved for it (POL-04 4.7). (PL-4; GV.PO-01)
4.8 Users must access owner, employee, and reservoir data only as their job requires; access is monitored. (AU-6; DE.CM-03)
4.9 Workforce with knowledge of a potential material cybersecurity incident must not trade in company securities and must keep the information confidential until it is public. (PL-4; GV.PO-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems, Wireless, and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring (including OT monitoring at the control centers), the annual Internal Audit assessment (P07), and access certifications. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Contractor violations are handled under the contractor's agreement and can end site access.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. OT exceptions also need the Director of OT Security's sign-off.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FSPA SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance; NIST SP 800-82 Rev. 3.
