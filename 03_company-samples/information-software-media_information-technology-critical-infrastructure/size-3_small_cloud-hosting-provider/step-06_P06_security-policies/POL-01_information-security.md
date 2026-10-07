# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-25 (replaces the unapproved 2022 drafts) |
| Review cycle | Annually (next review 2027-09-24), and after major changes, incidents, or a FedRAMP sponsor decision |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-10, RA-1, RA-3, PS-8, SA-9, SR-6, SR-8, CA-2, SI-12 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.SC-05, GV.SC-07, ID.IM-01 |
| Regulatory drivers | C-IT-R01 (FedRAMP Rev5 Class C readiness: CDS-CSO-IRP requires policies in the package); C-IT-R05 (bank service provider rule); Fla. Stat. 501.171(2); MSA security commitments |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of customer workloads and data, the tools that reach them, and company information.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors). It covers all company systems and data, including the Hosting Control Plane and Customer Portal (HCP), the private cloud platform at DC-1 and DC-2, and systems that vendors operate for the company (public cloud tenant, SaaS tools, colocation). Customer data in customer VMs is covered to the extent the company can access it.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves the security budget; accepts High and Very High risks; signs bank and agency contracts |
| Chief Operating Officer | Program owner; approves policies; accepts Moderate risks |
| IT Manager (Information Security Officer) | Runs the program day to day; maintains the risk register, SSP, and POA&M; incident commander |
| Director of Platform Engineering, Engineering Manager (Control Plane), Managed Services Lead | Operate controls for the systems they own; write the procedures for their areas |
| Controller | Vendor contracts and vendor reviews; cyber insurance |
| HR Manager | Onboarding, terminations, background checks, training records, sanctions records |
| All workforce | Follow these policies; report suspected incidents to the NOC immediately |

## 4. Policy statements
4.1 The company must maintain an information security program documented in this policy set, the System Security Plan (P02), and the procedures each control owner writes. The FedRAMP Rev5 Class C control list is the control baseline for the HCP. (PM-1; PL-10; GV.PO-01)

4.2 The IT Manager is the designated Information Security Officer. The designation must be in writing and must name a backup (the COO). (PM-2; GV.RR-02)

4.3 A risk assessment must be performed at least annually, using NIST SP 800-30 Rev. 1. It must also be repeated after a major change, a FedRAMP sponsor decision, or a significant incident. Risks must be tracked in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-01)

4.4 **Risk acceptance authority:**
- The IT Manager may accept Low and Very Low risks.
- The COO may accept Moderate risks.
- Only the CEO may accept High and Very High risks, only temporarily, and only with a dated treatment plan.
- A risk that lets one attacker reach many customers at once may not stay at High or above past its due date.
(PM-9; GV.RM-01)

4.5 Security policies must be reviewed at least annually. Each control owner must write and maintain the procedures for their control families and publish them in the policy library. (PL-1; GV.PO-02)

4.6 **Exceptions** to any security policy must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.RM-01)

4.7 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must record each sanction. (PS-8; GV.RR-04)

4.8 **Vendors.** Before a vendor gets access to customer data or administrative access to company systems, the Controller and the IT Manager must complete a risk review. Critical vendors are the colocation providers, the public cloud provider, and the RMM, SIEM, identity, and code hosting vendors. For each critical vendor:
- review its SOC 2 report (or equivalent) every year;
- make sure the contract requires security incident notice to the company within 72 hours or less.
(SA-9; SR-6; SR-8; GV.SC-05; GV.SC-07)

4.9 Security controls must be assessed at least annually by someone who does not operate them (P07), and after major changes. (CA-2; ID.IM-01)

4.10 The IT Manager must keep a register of legal and contractual security requirements, with outside counsel. It includes the bank service provider notification rule, Fla. Stat. 501.171, MSA commitments, and FedRAMP readiness targets. (GV.OC-03)

4.11 Security policies, procedures, risk assessments, assessment results, and incident records must be kept for at least 3 years, or longer where a contract requires. (SI-12)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the reviews required by this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the right authority, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); FedRAMP readiness gap analysis (P03); vendor review records (P09); 12 CFR 53.4, 225.303, 304.24; Fla. Stat. 501.171
