# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes (for example the 2027 DCS upgrade), acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-1, RA-3, CA-2, CA-5, CM-3, SA-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-06, GV.SC-07 |
| Regulatory drivers | C-CHEMICAL-R02 (33 CFR 101.620, 101.625, 101.630, 101.650(e)-(f)); 40 CFR 68.15, 68.75; 29 CFR 1910.119(l); 49 CFR 172.802; C-CHEMICAL-R01 (voluntary benchmark) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-08) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of company information and of the control systems that keep the plants, the marine terminal, workers, and neighbors safe.

## 2. Scope
All employees, contractors, and vendors at the Port plant (including the marine terminal), the Inland plant, the Distribution center, and corporate headquarters. It covers all IT and OT systems (SYS-01 to SYS-20), the cloud landing zone, TTRS and its field gateways, and systems that vendors operate for the company. The Inland plant and Distribution center are outside the Port plant Facility Security Plan, but this policy applies the same minimum standards there.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber and process safety risk; receives quarterly reports |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; approves POL-02 to POL-05 and standards; accepts Moderate risks; chairs the crisis management team |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| Information Security Manager | Runs the program day to day; **Cybersecurity Officer (CySO)** for the Port plant under 33 CFR 101.620(b)(3) |
| OT Security Engineer | Alternate CySO; OT security architecture and monitoring |
| Port Plant Manager and Inland Plant Manager | System owners for their plants' process control systems; the Port Plant Manager is the RMP qualified person (40 CFR 68.15(b)) |
| VP EHS and Process Safety | RMP, PSM, EPCRA, and DOT security plan; senior management official for the DOT plan (49 CFR 172.802(b)(1)) |
| Facility Security Officer | FSP, physical security, MTSA reporting |
| Controls Engineering Manager | Configuration and recovery of all OT systems |
| GRC Analyst | Risk register, POA&M, policy reviews, vendor reviews |
| Co-sourced internal audit firm | Independent annual assessment (P07) and, from approval, the annual Cybersecurity Plan audit |
| All workforce | Follow the policies and report suspected incidents to the CySO or the control room immediately |

## 4. Policy statements
4.1 The company must maintain an information security program for IT and OT, documented in this policy set, the supporting standards, the System Security Plans, and, for the Port plant, the Coast Guard-approved Cybersecurity Plan. (PM-1; PL-2; GV.PO-01; 33 CFR 101.620(b)(1))
4.2 The company must designate in writing, by name and title, a CySO and at least one alternate for the Port plant, reachable 24 hours a day. The Coast Guard must be told of any change within 96 hours. (PM-2; GV.RR-02; 33 CFR 101.620(b)(3); 101.630(e)(4))
4.3 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. At the Port plant it must also meet the Cybersecurity Assessment requirements of 33 CFR 101.650(e)(1) (all networks, every critical IT and OT asset, KEVs). Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. No risk that could plausibly cause a toxic release, decomposition, or overfill may be accepted above Moderate. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on top risks, POA&M status, incidents, and progress on the USCG roadmap. (GV.OV-01; CA-5)
4.6 Policies must be reviewed at least annually and after major changes or incidents; standards at least annually by their owners. (PL-1; GV.PO-02)
4.7 Exceptions to any policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months. At the Port plant, an exception that departs from the approved Cybersecurity Plan also needs Coast Guard notice under 33 CFR 101.665. (PL-1; GV.PO-02)
4.8 **Sanctions.** Workforce members who break security policies are sanctioned in proportion to intent and harm, from retraining to termination. HR documents each sanction. (PS-8; GV.RR-04)
4.9 **Vendors.** Before a vendor gets access to OT, critical IT systems, SSI, or formulations, it must pass a security review scaled to its tier, and its contract must require notice of cybersecurity vulnerabilities and reportable cyber incidents without delay (STD-04). Cybersecurity capability must be an evaluation criterion for every IT and OT purchase. (SA-4; SA-9; SR-6; GV.SC-05; GV.SC-06; 33 CFR 101.650(f)(1)-(2))
4.10 Tier 1 vendors (OT access, critical IT, or TTRS sub-service providers) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-04; P09). (SR-6; GV.SC-07)
4.11 **Management of change.** Changes to process control logic, setpoints, alarm limits, SIS logic, terminal automation, OT network rules, and the maximum intended inventories in the process safety information must go through management of change, including a process safety review and a security impact question. The inventory limits that keep the Inland plant outside RMP and keep the Port flammables warehouse below the PSM threshold must not be raised without an MOC approved by the VP EHS and Process Safety. (CM-3; CM-4; 40 CFR 68.75; 29 CFR 1910.119(l))
4.12 Security controls must be independently evaluated at least annually (P07). Assessors and Cybersecurity Plan auditors must not have regularly assigned cybersecurity duties at the facility and must be independent of the measures they audit. (CA-2; GV.OV-01; 33 CFR 101.630(f)(4))
4.13 Security policies, risk assessments, assessments, training, drill and exercise records, and incident records must be kept for at least the periods in STD-03 and the FSP, and never less than 2 years for USCG cybersecurity records (33 CFR 101.640; 105.225). (SI-12; AU-11)
4.14 AI tools must be approved through the AI governance process before use. No AI tool may write to a control system or release a safety document without human review (STD-07; P10). (PM-9; GV.RM-01)
4.15 Cyber-initiated failure scenarios from the risk register must be considered in every RMP and PSM process hazard analysis and revalidation. (RA-3; 40 CFR 68.67(c)(4); 29 CFR 1910.119(e)(3)(iv))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), the annual Cybersecurity Plan audit, quarterly access reviews, and the metrics reported to the audit committee. Violations are handled under 4.8.

## 6. Exceptions
Exceptions follow section 4.7.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); Gap analysis and USCG roadmap (P03); Facility Security Plan (SSI); RMP and PSM program documents; DOT hazmat security plan
