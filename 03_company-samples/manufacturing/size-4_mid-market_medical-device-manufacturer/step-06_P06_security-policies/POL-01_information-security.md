# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, new product submissions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-15, PL-1, PS-8, RA-3, RA-5, RA-5(11), SA-3, SA-8, SA-9, SA-15, SI-2, SI-5, SI-12, CA-2, CA-5, CM-8, SR-5, SR-6 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.RA-01, ID.RA-08, PR.PS-06 |
| Regulatory basis | FD&C Act 524B(b)(1)-(3) (N31-33-R05); 21 CFR 820.10(c); HIPAA 164.308(a)(1), (a)(2), (a)(8), (b)(1); 164.316 (N62-R01) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company security program for the enterprise, the Connected Care Cloud (CCC), the plant, and the company's devices; assign accountability; and give every other security policy and standard its authority. The program protects patients who depend on the company's devices, the PHI the company holds for hospitals, and the company's ability to build and fix its products.

## 2. Scope
All workforce members (employees, contractors, and temporary staff) at the Florida campus and in the field. It covers all company systems and data, including the plant OT and MES, the build and signing pipeline, the CCC, fielded devices to the extent the company designs and supports them, and systems that vendors operate for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber and product security risk; receives quarterly reports |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor; DLP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and program strategy; reports to the audit committee |
| IT Director | Security Officer for IT and plant networks; HIPAA security official for the CCC (45 CFR 164.308(a)(2)) |
| VP QA/RA | Owns section 524B compliance, MDR and 806 decisions, and FDA correspondence |
| VP Engineering | Owns the SPDF, build and signing, and product releases |
| Product Security Manager | Leads the PSIRT, vulnerability monitoring, SBOMs, CVD, and ISAO liaison |
| Security Manager | Security operations, MSSP oversight, vulnerability management for IT, GRC and standards |
| Plant Manager and OT Engineering Manager | Apply policies in the plant; own OT and test station security |
| Compliance and Privacy Officer | BAAs; breach decisions; sanctions with HR |
| Chief Medical Officer | Clinical safety input to risk and AI decisions |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain one security program covering enterprise IT, the CCC, plant OT, and product security. It is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; 164.316(a))
4.2 The IT Director is the designated HIPAA security official for the CCC, the VP QA/RA owns section 524B compliance, and the Product Security Manager leads the PSIRT. Each designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; 164.308(a)(2))
4.3 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Product cybersecurity risk assessments, rating exploitability separately from safety probability, must be updated for every release and every newly identified vulnerability, and reconciled with the risk register each quarter. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B); 524B(b)(2))
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly contribute to patient harm may not be accepted above Low. (PM-9; GV.RM-01)
4.5 **Secure product development.** Every device, device software function, and related system must be designed, developed, and maintained under the secure product development framework (STD-10). Related systems include the CCC, the update service, the build and signing pipeline, and any production software that loads firmware, sets device state, or issues device identities. (SA-3; SA-8; SA-15; PR.PS-06; 524B(b)(2); 21 CFR 820.10(c))
4.6 **Postmarket vulnerability management.** Every released device and CCC version must have a current machine-readable SBOM. Components must be monitored daily against vulnerability sources, including CISA's KEV catalog, and triaged within the service levels in STD-09. Each product must have a justified regular patch cycle and an out-of-cycle path for vulnerabilities that could cause uncontrolled risk. (RA-5; SI-2; SI-5; CM-8; ID.RA-01; 524B(b)(1)-(3))
4.7 **Coordinated vulnerability disclosure.** The company must publish a CVD policy, acknowledge reports within 3 business days, screen each report as a possible complaint, and remain an active member of an ISAO that shares medical device vulnerabilities. (RA-5(11); PM-15; ID.RA-08; 524B(b)(1))
4.8 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, product security metrics (time to patch and time to field deployment), incidents, and roadmap progress. (GV.OV-01; CA-5)
4.9 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 164.316(b)(2)(iii))
4.10 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. No exception may waive a statutory or regulatory requirement. (PL-1)
4.11 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm, from retraining to termination. HR and the Compliance and Privacy Officer document each sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
4.12 **Suppliers.** No subcontractor may create, receive, maintain, or transmit PHI until it signs a subcontractor BAA and passes a security review scaled to its tier (STD-03). Critical software component suppliers must commit in contract to vulnerability notification and support dates. Purchasing must not issue a purchase order without these approvals. (SA-9; SR-5; SR-6; GV.SC-05; 164.308(b)(1))
4.13 Security controls must be independently evaluated at least annually (P07) and after major changes. The assessor must not operate the controls it assesses. (CA-2; 164.308(a)(8))
4.14 Security policies, risk assessments, assessments, and incident records must be retained for 6 years. CVD and PSIRT records follow the same period. Records of corrections and removals not reported to FDA must be kept for 2 years beyond the expected life of the device (21 CFR 806.20(c)). (SI-12; 164.316(b)(2)(i))
4.15 AI tools, and AI functions in products or quality processes, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (section 4.11). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, product security metrics, and internal quality audits.

## 6. Exceptions
Exceptions follow section 4.10. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis and roadmap (P03); FD&C Act section 524B; 21 CFR Parts 803, 806, and 820; HIPAA Security Rule, 45 CFR 164 Subpart C
