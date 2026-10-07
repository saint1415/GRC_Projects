# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, a TSA directive revision, or a significant incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, CM-4, SA-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.IM-01 |
| Regulatory basis | TSA SD Pipeline-2021-02G Sections II.A.3-4, II.B, III.G, IV, VI; SD Pipeline-2021-01G Section II.B; 49 CFR 192.631(f) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company cybersecurity program for business IT and operational technology (OT), assign accountability, and give every other security policy and standard its authority. The program protects the safe and reliable operation of the pipeline and the laterals the company operates for others first, then the confidentiality, integrity, and availability of company information. It is also how the company meets its TSA security directives.

## 2. Scope
All employees, contractors, authorized representatives, and managed service providers with access to company systems, at headquarters and the Gas Control Center (GCC), the Backup Control Center (BCC), the 5 compressor stations, the 6 area offices, and all field sites. It covers business IT, OT (SCADA, station control systems, field devices, telecommunications, and the IT/OT DMZs), the cloud landing zone, and SaaS services, including systems that suppliers operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; approves the risk appetite each year; receives quarterly reports on top risks, POA&M status, TSA matters, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and PSGCS system owner; approves POL-02 to POL-05; accepts Moderate risks; approves any precautionary shutdown for cyber reasons |
| vCISO | Owns this policy and the program strategy; reviews the TSA plans each year; reports to the audit committee |
| Security Manager | Runs the program day to day; primary TSA Cybersecurity Coordinator; owns the SSP and the TSA plans |
| OT Security Engineers | OT access, monitoring, and patch mitigations; one is an alternate Cybersecurity Coordinator |
| IT Director | Business IT and cloud security; alternate Cybersecurity Coordinator |
| Director of Gas Control | Makes sure security changes to OT follow control room management procedures (192.631); may isolate OT from IT at any time |
| SCADA and OT Engineering Manager | Secure administration of the PSGCS |
| General Counsel | Legal privilege, breach decisions, SSI and CEII questions, contract terms |
| Co-sourced internal audit | Independent annual assessment (P07) and the assessments in the TSA Cybersecurity Assessment Plan |
| All personnel | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain a cybersecurity program covering business IT and OT, documented in this policy set, the supporting standards, the System Security Plan, and the TSA-approved Cybersecurity Implementation Plan. (PM-1; GV.PO-01; SD 02G II.B)
4.2 The Security Manager is the primary TSA Cybersecurity Coordinator. At least one alternate must be designated, and at least one coordinator must be a U.S. citizen eligible for a security clearance. Changes to coordinator contact information must reach TSA within 7 days. (PM-2; GV.RR-02; SD 01G II.B.1)
4.3 A risk assessment covering business IT and OT must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. A risk that could cause loss of pipeline control or public harm may not be accepted above Moderate. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, TSA submissions and inspections, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes, a directive revision, or an incident. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. An exception that touches a measure in the TSA-approved plan must also be reviewed by the Cybersecurity Coordinator for TSA notice. (PL-1)
4.8 **Pipeline safety comes first.** No security control may be installed, changed, or tested on OT in a way that could affect control room operations unless it has gone through the management of change (MOC) process with Gas Control sign-off, as 49 CFR 192.631(f) requires. (CM-3; GV.OC-03)
4.9 **TSA plan amendments.** Every MOC request must answer whether the change is a permanent change (one intended to be in effect for 45 or more calendar days, SD 02G VI.C) to a measure in the TSA-approved Cybersecurity Implementation Plan. If it is, the Cybersecurity Coordinator must file an amendment request with TSA no later than 50 calendar days after the change takes effect. (CM-4; GV.OC-03; SD 02G VI.B-D)
4.10 **No OT access without terms.** Suppliers and authorized representatives with access to OT, SSI, or Restricted information must have written security requirements in their contract before access is granted: the TSA measures they perform, access only through the remote access gateway, named technicians, incident notice within 24 hours, and return or destruction of company data at exit. Purchasing must not issue a purchase order without the Security Manager's approval. (SA-4; SA-9; GV.SC-05; SD 02G II.A.3-4)
4.11 Tier 1 suppliers (OT access, SSI or Restricted data, or support for a High-criticality BIA process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07)
4.12 Security controls must be assessed under the TSA-approved Cybersecurity Assessment Plan: at least one-third of the plan's measures each year and all of them over three years, an architecture design review at least every two years, and an annual report to TSA. The co-sourced internal audit firm performs the assessments. (CA-2; ID.IM-01; SD 02G III.G)
4.13 Security records (policies, risk assessments, TSA plans and reports, assessment results, incident records) must be kept for at least 5 years. Records that PHMSA requires, including 192.631(j) records, must be kept for the period that rule requires. SSI records follow POL-04. (SI-12; GV.PO-02; SD 02G IV.A, IV.C)
4.14 AI tools that process Restricted or SSI data, or that inform controllers, patrols, or maintenance decisions, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations may lead to retraining, written warning, loss of access, or termination, depending on intent and impact. For contractors and authorized representatives, violations may lead to removal of access and contract action. Compliance is checked through the annual control assessment (P07), quarterly access reviews, TSA inspections, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); TSA Cybersecurity Implementation Plan, Incident Response Plan, and Assessment Plan (SSI); control room management manual; O&M manual (49 CFR 192.605); emergency plan (49 CFR 192.615)
