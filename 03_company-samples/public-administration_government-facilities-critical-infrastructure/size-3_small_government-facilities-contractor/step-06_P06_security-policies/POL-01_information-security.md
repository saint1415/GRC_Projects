# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Owner | Chief Operating Officer |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, new contracts, or incidents |
| Implements (SP 800-53 Rev. 5) | PL-1, PL-2, RA-1, RA-3, CA-2, PS-8, SA-9, SR-1, SR-3, SI-12, CP-1, CP-2, CP-4, CM-1, CM-3, CM-6, SI-1, SI-2, SI-3, PE-1, PE-3, PE-8 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.SC-05 |
| Contract and legal drivers | State contract cybersecurity exhibit (SP 800-53 Rev. 5 Moderate); county security addendum; FAR 52.204-21, 52.204-23, 52.204-25, 52.204-30; Fla. Stat. 501.171(2) and 119.0701 |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy its authority. The program protects the company's systems and the government building systems, data, and information the company operates or holds for its customers.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff) and subcontractors working under company contracts. Covers company systems, the Facility Operations Technology Platform (FOTP), customer building systems the company operates or maintains, and customer information in any form, including federal contract information (FCI), CUI, cardholder data, and security system plans. On GSA systems, GSA's IT security policy applies as well, and the stricter rule wins.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Majority owner | Approves the security budget; accepts High and Very High risks |
| Chief Operating Officer | Program owner; approves policies; accepts Moderate risks; system owner of the FOTP |
| IT Manager (Information Security Officer) | Runs the program day to day; maintains the risk register, SSP, and POA&M |
| Contracts Manager | Customer and FAR clause compliance; supplier screening; CUI program lead; subcontract flow-downs |
| Controls Engineering Manager and Security Systems Supervisor | Security of the BAS and access control platforms they own |
| Site Managers | Customer notices and local procedures at their contract |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program based on the NIST SP 800-53 Rev. 5 Moderate baseline, documented in this policy set and the System Security Plan. (PL-1; PL-2; GV.PO-01)
4.2 The IT Manager is the designated Information Security Officer. The designation must be in writing. (GV.RR-02)
4.3 A risk assessment must be done at least annually, when a new contract starts, and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and treatment. (RA-1; RA-3; GV.RM-01)
4.4 Risk acceptance authority: the IT Manager may accept Low risks; the COO, Moderate; the majority owner, High and Very High. A risk that could unlock doors or disable building services at a customer site may not be accepted at High or above without a dated treatment plan. (GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.6 Exceptions to any security policy must be requested in writing, risk-rated, approved per 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.7 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)
4.8 **Vendors and subcontractors.** Before a vendor or subcontractor receives customer data, CUI, FCI, or remote access to customer systems, it must sign the company's security addendum (MFA, incident notice within 24 hours, and the FAR and customer flow-downs that apply) and pass a security review. (SA-9; GV.SC-05)
4.9 **Supply chain.** Before buying or deploying any telecommunications, video surveillance, networking, or OT equipment or software, the Contracts Manager must screen it against FAR 52.204-25 and 52.204-23 and against FASCSA orders in SAM.gov. SAM.gov must be checked for new FASCSA orders at least every three months. A covered item found in use must be reported to the contracting officer within the clause deadline (one business day under 52.204-25(d)). (SR-1; SR-3)
4.10 Security controls must be assessed at least annually by someone independent of their operation (P07), as the state contract requires. (CA-2)
4.11 Security records (policies, assessments, risk registers, incident records) must be kept at least 3 years, or longer where a contract or Fla. Stat. 119.0701 requires. At contract end, customer public records must be transferred to the customer or kept under the customer's retention rules, and exempt duplicates destroyed. (SI-12)
4.12 **Contingency.** The FOTP must have a contingency plan based on the BIA (P05), with manual-mode (building recovery) procedures for every state and county building, and restore tests at least quarterly. The plan must be exercised with each customer at least annually. (CP-1; CP-2; CP-4)
4.13 **Change and configuration.** Changes to BAS programs, door schedules, firewall rules, and cloud configuration must be ticketed in the CMMS, approved by the component owner, and recorded. OT components must follow a documented hardening baseline, including removal of default credentials at commissioning. (CM-1; CM-3; CM-6)
4.14 **Patching and malware.** Company endpoints and servers must receive security patches within 30 days (14 days for critical, internet-facing systems such as edge firewalls). OT patches are applied in maintenance windows agreed with the customer. Every company endpoint and server must run endpoint protection or, where the OT software does not allow it, application allow-listing. (SI-1; SI-2; SI-3)
4.15 **Physical security.** The ROC suite is badge-controlled. Visitors must sign in and be escorted. Keys to customer BAS panels must be logged. (PE-1; PE-3; PE-8)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07), the access reviews in POL-02, and the quarterly supply chain checks.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; System Security Plan (P02); Risk Register (P01); state contract cybersecurity exhibit; county security addendum; FAR clauses in the GSA contract
