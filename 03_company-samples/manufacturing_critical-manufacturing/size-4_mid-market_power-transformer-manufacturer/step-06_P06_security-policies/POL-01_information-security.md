# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-4, SA-8, SA-9, SR-2, SR-3, SR-6, SI-7, CP-2, SR-11, SA-11, CM-8, CP-4 |
| CSF 2.0 | GV.OC-03, GV.RM-02, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-08, ID.RA-09, PR.PS-06 |
| Drivers | CSF 2.0 benchmark (voluntary); FAR 52.204-21, -23, -25, -30; utility addenda (CIP-013-2 R1.2 flow-down); FMS subscription agreements; 15 CFR 762.6 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program for office IT, both plants' control systems, the products and services the company supplies to utilities, and its cloud services; assign accountability; and give every other security policy and standard its authority. The program protects worker safety, the integrity of grid equipment, and the confidentiality, integrity, and availability of company and customer information.

## 2. Scope
All workforce members (employees, contractors, and temporary staff) at HQ, Plant 1, Plant 2, and in the field. It covers all company systems and data: office IT, the cloud landing zone, plant control and test systems, the product software pipeline, the FMS, and systems that suppliers operate for the company. It also covers any site or business acquired by the company, from the date of acquisition.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents, and the appetite measures |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; EPSP system owner; approves POL-02 to POL-05 and the standards index; accepts Moderate risks; chairs the crisis management team |
| vCISO | Owns this policy and the program strategy; reports to the audit committee; member of the AI review group |
| Security Manager | Runs the program day to day; owns POL-02 and POL-03; incident commander; maintains the risk register |
| IT Director | IT operations, landing zone, backups, and recovery |
| OT Security Engineer | OT security architecture and monitoring at both plants |
| Director of Manufacturing Engineering and Plant Managers | Apply policies on the plant floor; own OT changes and safe-state decisions |
| VP Engineering | Product security for software and firmware supplied to utilities |
| Director of Digital Services | Security of the FMS as a customer service |
| General Counsel | Obligations register; legal and contractual notices |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program covering office IT, both plants' control systems, the products and services supplied to utilities, and cloud services, documented in this policy set, the supporting standards, and the System Security Plan (P02). NIST CSF 2.0, with NIST SP 800-82 Rev. 3 for OT, is the benchmark. (PM-1; GV.PO-01)

4.2 The Security Manager is the security program lead, the OT Security Engineer is the OT security lead, and the VP Engineering is the product security lead. These designations must be in writing, in job descriptions, and reaffirmed each year. (PM-2; GV.RR-02)

4.3 A cybersecurity risk assessment must be performed at least annually and after major changes, including acquisitions and new customer services, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05; GV.RM-06)

4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks; the COO, Moderate; the CEO, High for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks to worker safety or to the integrity of products, software, or advisories delivered to utilities may not be accepted above Low. (PM-9; GV.RM-02)

4.5 The vCISO must report to the audit committee each quarter on top risks, POA&M status, incidents, and the risk appetite measures. (PM-9; CA-5; GV.OV-01)

4.6 The General Counsel must keep an obligations register of every legal, regulatory, and contractual cybersecurity duty, with an owner and trigger for each: the 31 utility addenda, the FMS subscription agreements, FAR 52.204-21, 52.204-23, 52.204-25, and 52.204-30, 15 CFR 762.6, and Fla. Stat. 501.171. The register must be checked monthly and reviewed in full each quarter. Contracts with security terms must be reviewed by the General Counsel and the Security Manager before signature. (SA-4; PM-1; GV.OC-03)

4.7 Suppliers must be tiered under STD-03 by their access to company systems, their effect on products, and their support of High-criticality processes. Tier 1 suppliers (including the MSSP, cloud, identity, ERP, and EDI providers, OEMs with remote access, the TMU electronics supplier, and AI service vendors) must accept security terms covering incident notice, vulnerability disclosure, remote access rules, and software integrity, and must be reviewed annually (SOC 2 report or equivalent; P09). (SR-2; SR-6; SA-9; GV.SC-05; GV.SC-07)

4.8 **Product security.** The VP Engineering must run intake for vulnerabilities in the firmware and software the company supplies, track each to resolution, and disclose known vulnerabilities to the addendum utilities within 30 days. The Director of Quality must verify the hash or signature of every firmware image on receipt and before loading at final test. Company software must be signed only through the hardware-backed signing service with 2-person approval, and each release must have a software bill of materials. (SI-7; SR-11; SA-8; ID.RA-08; ID.RA-09)

4.9 **Secure development.** Software the company builds for customers (the TMU configuration software and the FMS) must follow STD-10, which is aligned to the NIST Secure Software Development Framework: code review, dependency scanning, security testing before release, and protected build systems. (SA-8; SA-11; PR.PS-06)

4.10 The company must not buy or use covered telecommunications or video surveillance equipment (FAR 52.204-25), Kaspersky covered articles (FAR 52.204-23), or articles prohibited by an applicable FASCSA order (FAR 52.204-30). All technology purchases, including plant purchases, must go through central purchasing for these checks. Any covered item found must be reported to the Contracts and Trade Compliance Manager the same day. (SR-3; CM-8; GV.SC-05)

4.11 Security policies must be reviewed at least annually and after major changes or incidents. Standards must be reviewed annually by their owners. Security controls must be independently assessed at least annually (P07). (PL-1; CA-2; GV.PO-02)

4.12 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-02)

4.13 **Sanctions.** Workforce members and contractors who break security policies must face consequences in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each case. Good-faith incident reports are never sanctioned. (PS-8; GV.RR-04)

4.14 The company must keep the business impact analysis current and a contingency plan under STD-07 that covers the ERP, both MES instances, both plants' OT recovery and manual operations, and the FMS, and must test recovery of every High-criticality process at least annually. (CP-2; CP-4; ID.IM-04; RC.RP-01)

4.15 Any AI tool or AI feature that processes Restricted data, makes or informs decisions about people, or produces advisories for customers must be approved through the AI governance process (P10) before use, including AI features turned on in existing software. (PM-9; SA-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under section 4.13. Compliance is checked through the annual independent assessment (P07), quarterly access reviews, the monthly obligations register check, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.12. They must be written, risk-rated, approved by the right authority under section 4.4, recorded in the risk register, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); gap analysis and roadmap (P03); P08 runbooks and notification matrix; P10 AI governance process; NIST CSF 2.0; NIST SP 800-82 Rev. 3
