# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | CTO |
| Approved by | Chief Executive Officer |
| Effective date | 2026-09-22 (replaces the December 2025 policy adopted for the SOC 2 Type 1) |
| Review cycle | Annually (next review 2027-09-22), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-1, RA-3, CA-2, CA-7, CM-1, CM-3, SA-3, SA-3(2), SA-8, SA-9, SI-12, SR-6 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.OC-03, GV.SC-05, GV.SC-07, ID.RA-01, PR.PS-06 |
| Also supports | SOC 2 CC1.1 to CC1.5, CC3.1 to CC3.4, CC5.3, CC8.1, CC9.2; FTC Act Section 5 reasonable security (N51-R01) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer worker data and company information, and makes sure the company does what it tells customers it does.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), whether they work in the Florida office or remotely. Covers all company systems and data, including the Workforce Scheduling Platform (WSP), the staging environment, the source repository and CI/CD pipeline, corporate SaaS, laptops, and systems that sub-processors operate for the company. It applies to customer data (customer worker data the company processes as a service provider under the DPA) and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Executive Officer (majority owner) | Approves policies, the security budget, and customer-facing security statements; accepts High and Very High risks |
| CTO | Policy owner for POL-01; system owner of the WSP; accepts Moderate risks |
| COO (privacy lead) | Contracts, DPAs, sub-processor approvals, and breach notification decisions with outside privacy counsel |
| IT Manager (security and compliance lead) | Runs the program day to day; maintains the risk register, SSP, policy set, and SOC 2 program; accepts Low risks |
| Platform Engineering Lead and Engineering Manager | Operate cloud, CI/CD, and secure development controls |
| All workforce | Follow these policies; report suspected incidents immediately (POL-03) |

## 4. Policy statements
4.1 The company must maintain an information security program, documented in this policy set and the System Security Plan (P02), that meets its customer commitments (MSA, DPA, SOC 2) and the reasonable security the FTC expects under Section 5 of the FTC Act. (PM-1; GV.PO-01)
4.2 The IT Manager is the designated security and compliance lead and the COO is the designated privacy lead. Both designations must be in writing. (PM-2; GV.RR-02)
4.3 A risk assessment using NIST SP 800-30 Rev. 1 must be performed at least annually and before major changes, such as a new sub-processor or general availability of an AI feature. Risks must be tracked in the risk register with an owner and a treatment. (RA-3; PM-9; ID.RA-01)
4.4 **Risk acceptance authority:** the IT Manager may accept Low and Very Low risks; the CTO, Moderate; the Chief Executive Officer, High and Very High, only temporarily and with a dated treatment plan. A High risk to the confidentiality of customer data may not be accepted long term. (PM-9; GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.7 **Sanctions.** Workforce members who break security or privacy policies are sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. People Operations documents each sanction. (PS-8; GV.RR-04)
4.8 **Change management and secure development.**
- Every change to production code, infrastructure, or configuration must go through a pull request with at least one approving reviewer who is not the author, and must pass automated tests before deployment. Administrators may not bypass branch protection except for a documented emergency change, which must be reviewed within 1 business day.
- New features that process customer data in a new way, add a sub-processor, or use AI must have a security and privacy review in design, approved by the CTO and the privacy lead.
- Production customer data must not be used in development, test, or staging environments. Test data must be synthetic or masked.
- Engineers must complete secure coding training every year (POL-05 4.3).
(CM-3; SA-3; SA-3(2); SA-8; PR.PS-06)
4.9 **Sub-processors.** Before any vendor receives customer data, it must pass a security review, sign a DPA with security terms, and be announced to customers with the 30 days' notice the DPA promises. The COO must review each sub-processor's SOC 2 report (or equivalent) every year and map its complementary user entity controls to company controls. (SA-9; SR-6; GV.SC-05; GV.SC-07)
4.10 **Accurate security statements.** Security, privacy, and AI statements on the website, in release notes, in questionnaire answers, and in contracts must be reviewed by the IT Manager and the COO before publication and at least quarterly against actual practice. The Chief Executive Officer approves changes to the public security page. A statement found to be inaccurate must be corrected promptly. (CA-7; GV.OC-03)
4.11 Security controls must be assessed independently at least annually (P07) and monitored monthly against the SOC 2 evidence calendar (P09). (CA-2; CA-7; ID.IM-01)
4.12 Security policies, risk assessments, assessment results, and SOC 2 evidence must be retained for at least 3 years. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the SOC 2 examination (P09), and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level set in POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); Gap Analysis (P03); SOC 2 Readiness (P09); customer MSA and DPA; FTC Act Section 5 (15 U.S.C. 45(a)) and FTC "Start with Security" guidance
