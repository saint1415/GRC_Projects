# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, new care sites, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-5, SA-4, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| HIPAA Security Rule | 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(8), (b)(1); 164.316 |
| Other rules | 42 CFR 482.15 (emergency preparedness); 45 CFR 92.210 (decision support tools); 42 CFR 495.24 (security risk analysis measure) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the hospital's information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of patient and hospital information, and its first purpose is safe patient care: keeping clinicians able to treat patients during and after a cyber event.

## 2. Scope
All workforce members (employees, contracted clinicians, independent physicians with privileges, agency staff, students, volunteers, and affiliated practice users) at the main campus and the outpatient center. It covers all systems and data, including medical devices, building and clinical operational technology (OT), systems that business associates and other vendors operate for the hospital, and the EHR services the hospital provides to affiliated practices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, and incidents; is notified before any Very High risk exception |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks; hospital incident commander for hospital-wide emergencies |
| Chief Operating Officer | Executive sponsor and HECS system owner; approves POL-02 to POL-05; accepts Moderate risks; chairs the cyber crisis management team |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| IT Director (HIPAA Security Officer) | Runs the program day to day (45 CFR 164.308(a)(2)); owns the SSP and IT disaster recovery |
| Information Security Manager and security analysts | Security operations, vulnerability management, MSSP oversight, GRC, and standards |
| Compliance and Privacy Officer | HIPAA Privacy Officer and Section 1557 Coordinator; breach determinations; BAAs; sanctions with HR |
| Chief Medical Officer and Chief Nursing Officer | Clinical safety decisions for downtime, diversion, and AI; the CMO chairs the Clinical Decision Support Committee (P10) |
| Director of Emergency Management | Integrates cyber hazards and IT outages into the 42 CFR 482.15 program |
| Director of Biomedical Engineering and Director of Facilities | Security of medical devices and OT, with IT (STD-04) |
| Department leaders | Apply policies in their departments; approve access; own downtime procedures |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The hospital must maintain an information security program that meets the HIPAA Security Rule and is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 164.316(a))

4.2 The IT Director is the designated HIPAA Security Officer. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; 164.308(a)(2))

4.3 An enterprise risk analysis must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. It must cover medical devices, OT, vendors, and AI tools, and it supports the Promoting Interoperability security risk analysis measure. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly cause patient harm may not be accepted above Low. (PM-9; GV.RM-01)

4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, incidents, CPG progress, and progress against the program roadmap. (GV.OV-01; CA-5)

4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 164.316(b)(2)(iii))

4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)

4.8 **Sanctions.** Workforce members who fail to comply with security or privacy policies must be sanctioned in proportion to intent and harm, from retraining to termination or loss of privileges. For independent physicians, sanctions follow the medical staff bylaws. The Compliance and Privacy Officer and HR or the Medical Staff Office must document each sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

4.9 **No BAA, no PHI.** Before any vendor creates, receives, maintains, or transmits PHI for the hospital, it must sign a business associate agreement, pass a security review scaled to its tier (STD-03), and be approved by the Compliance and Privacy Officer. Purchasing must not issue a purchase order to such a vendor without that approval. (SA-9; GV.SC-05; 164.308(b)(1))

4.10 Tier 1 vendors (PHI at scale, privileged or network access, or support for a High-criticality BIA process) must be reassessed each year, including a review of their SOC 2 report or equivalent (STD-03; P09). (SR-6; GV.SC-07)

4.11 **Medical device purchasing.** No networked medical device may be bought or connected without a security review by IT and biomedical engineering, including the manufacturer disclosure statement (MDS2), a software bill of materials where available, the support period, and patching commitments (STD-04). (SA-4; GV.SC-05)

4.12 Security controls must be independently evaluated at least annually (P07) and after major changes. (CA-2; 164.308(a)(8))

4.13 Security policies, procedures, risk analyses, assessments, and incident records must be retained for 6 years from creation or last effective date, whichever is later. (SI-12; 164.316(b)(2)(i))

4.14 **AI governance.** AI tools and decision support features that process PHI or support clinical, coding, or patient-facing decisions must be approved through the AI governance process before use, including EHR features that a vendor upgrade makes available (STD-05; P10). For patient care decision support tools, the Section 1557 Coordinator must record the 45 CFR 92.210(b) identification and (c) mitigation. (PM-9; GV.RM-01)

4.15 **Cyber hazards in emergency preparedness.** The emergency plan's all-hazards risk assessment must include cyber events (ransomware, prolonged EHR loss, device and OT compromise), and the plan must contain an IT outage annex with diversion criteria, reviewed at least every 2 years with the rest of the plan (42 CFR 482.15(a)). (CP-2; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under the HIPAA sanctions procedure (section 4.8). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); HIPAA Security Rule, 45 CFR 164 Subpart C; 42 CFR 482.15; 45 CFR 92.210; emergency operations plan
