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
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-2, AT-3, AC-11, AC-20, CM-11 |
| CSF 2.0 | PR.AT-01, PR.AT-02, PR.PS-05, GV.PO-01 |
| Regulatory and guidance drivers | CSF 2.0 (benchmark); SP 800-82 Rev. 3 3.3.5; 14 CFR 107.12 |

## 1. Purpose
Set clear rules for how workforce members, crew leads, and contractors use company systems, devices, OT, drones, and AI tools, in language and training they can follow in the field.

## 2. Scope
All Cris Santos Company workforce members (year-round employees, seasonal and H-2A workers, contractors, and integrator and vendor staff working on company systems) at the 48 farms, 17 packing sites, 6 irrigation control centers, offices, and both data center campuses in Florida, Georgia, South Carolina, and North Carolina, including acquired operations from their acquisition date. Covers all systems and data, including cloud, data centers, SaaS, operational technology (irrigation, fertigation and chemigation, packing, cold-chain, and drying controls), drones and equipment telematics, systems that vendors operate for the company, and the services offered to external growers (SL-1 and SL-2).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy; training and attestations, including seasonal onboarding |
| Managers and crew leads | Make sure their teams follow it; report misuse |
| Chief Remote Pilot | Drone operations and imagery handling |
| AI governance committee | Approves AI tools and use cases (STD-05.3) |
| All workforce | Follow this policy; report incidents to the SOC |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested a mapped control in 2026 (P07).

4.1 Company systems are for company business; limited personal use is allowed if it creates no risk and involves no worker, grower, or customer data. (PL-4; GV.PO-01)
4.2 Every workforce member must acknowledge this policy before receiving access and every year after; seasonal workers acknowledge at onboarding in English or Spanish. (PL-4(1); PR.AT-01)
4.3 Security awareness training is required at hire and annually, in English and Spanish, with a short field module for crew leads and scouts. (AT-2; PR.AT-01)
4.4 OT operators, irrigation technicians, SCADA engineers, privileged users, and integrator staff must complete role-based OT security training (safe states, remote access rules, change control, social engineering) before receiving OT access and annually after. (AT-3; PR.AT-02)
4.5 Workforce must lock screens and tablets when stepping away; shared tablets must use individual logins. (AC-11; PR.AA-05)
4.6 Users must not install software or connect storage devices unless IT approves it. Integrator and vendor laptops may connect to OT networks only through the gateway or, on site, after a malware scan and approval by the control center manager. (CM-11; AC-20; PR.PS-05)
4.7 Only AI tools on the approved list (STD-05.3) may be used for company work, and only for approved data classes. (PL-4; GV.PO-01)
4.8 Drones may be flown only by certificated remote pilots under the drone program, and imagery that shows people must not be used to evaluate or discipline workers. (PL-4; GV.PO-01)
4.9 Workforce with knowledge of a potential material cybersecurity incident must not trade in company securities and must keep the information confidential until it is public. (PL-4; GV.PO-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems, Personal Devices, and Integrator Laptops Standard
- STD-05.3 Approved AI Tools and Imagery Use Standard

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the annual Internal Audit assessment (P07), access certifications, and OT change and session reviews. Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm. Vendor violations are handled under the contract and STD-01.9.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 FMICP SSP; P03 gap analysis; P05 BIA; P08 runbook and notification matrix; P10 AI governance.
