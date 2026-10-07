# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, new contracts, acquisitions, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PL-1, PL-2, RA-1, RA-3, CA-2, CA-7, PS-8, SA-9, SR-1, SR-3, SI-12, CP-1, CP-2, CP-4, CM-1, CM-3, CM-6, SI-1, SI-2, SI-3, PE-1, PE-3 |
| CSF 2.0 | GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OC-03, GV.OV-01, GV.SC-05 |
| Contract and legal drivers | State contract cybersecurity exhibit (SP 800-53 Rev. 5 Moderate; Fla. Stat. 282.318(4)(h)); County A, County B, and City addenda (Fla. Stat. 282.3185(4)); FAR 52.204-21, 52.204-23, 52.204-25, 52.204-30, 52.204-9; Fla. Stat. 501.171(2) and 119.0701 |
| Supporting standards | `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Set up the Cris Santos Company information security program, assign who is accountable, and give every other security policy and standard its authority. The program protects the company's systems and the government building systems, data, and information the company operates or holds for its customers, and it keeps customer buildings safe and secure while the company operates them.

## 2. Scope
All workforce members (employees, temporary staff, and interns) and all subcontractors working under company contracts. It covers company systems, the Integrated Facility Operations Platform (IFOP), customer building systems the company operates or maintains, and customer information in any form, including federal contract information (FCI), CUI, cardholder data, face templates, and security system plans. On GSA systems, GSA's IT security policy applies as well, and the stricter rule wins. Any company or contract acquired by Cris Santos Company is covered from the day it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents, and SOC 2 readiness |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and IFOP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| vCISO | Owns this policy and the program strategy; reports to the audit committee; chairs the AI review group |
| IT Director (Information Security Officer) | Runs the program day to day; owns IT operations and IT contingency planning |
| Security Manager, security analysts, GRC analyst | Security operations, MSSP oversight, vulnerability management, risk register, SSP, POA&M, and standards |
| OT Security Engineer | OT security standards, OT monitoring, and remote access policy for OT |
| Director of Building Technology | Security of the BAS and access control platforms and their change control |
| Contracts Director | Customer and FAR clause compliance; supplier and subcontractor screening; CUI program lead |
| General Counsel | Breach determinations and notices; public records requests; legal privilege |
| Program managers | Customer notices and manual-mode procedures at their contracts |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program based on the NIST SP 800-53 Rev. 5 Moderate baseline, documented in this policy set, the supporting standards, and the System Security Plan. (PL-1; PL-2; GV.PO-01)
4.2 The IT Director is the designated Information Security Officer. The designation must be in writing and reaffirmed each year. (GV.RR-02)
4.3 A risk assessment must be done at least annually, when a new contract or acquisition starts, and after major changes, using NIST SP 800-30 Rev. 1. Risks must be tracked in the risk register with an owner and a treatment. (RA-1; RA-3; GV.RM-01)
4.4 Risk acceptance authority: risk owners may accept Low and Very Low risks; the COO, Moderate; the CEO, High (temporarily, with a dated plan). Very High risks may not be accepted. A risk that could unlock doors, disable a critical facility, or leave a customer building unsafe may not be accepted above Low. (GV.RM-01)
4.5 Security policies must be reviewed at least annually and updated after major changes or incidents. (PL-1; GV.PO-02)
4.6 Supporting standards set the measurable minimums for each policy. They are listed in the standards index, owned by named roles, approved by the parent policy's approver, and reviewed yearly. A standard may not weaken its parent policy. (PL-1; GV.PO-01)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction. (PS-8; GV.RR-04)
4.9 **Vendors and subcontractors.** Before a vendor or subcontractor receives customer data, CUI, FCI, or remote access to customer systems, it must sign the company's security addendum (MFA, broker-only remote access, incident notice within 24 hours, background checks, and the FAR and customer flow-downs that apply) and pass a security review. OT subcontractors and Tier 1 vendors must be reviewed every year. (SA-9; GV.SC-05)
4.10 **Supply chain.** Before buying, installing, or using any telecommunications, video surveillance, networking, or OT equipment or software, including equipment supplied by a subcontractor, the Contracts Director must screen it against FAR 52.204-25 and 52.204-23 and against FASCSA orders in SAM.gov. SAM.gov must be checked for new FASCSA orders at least once every three months. A covered item found in use must be reported to the contracting officer within the clause deadline (1 business day under 52.204-25(d); 3 business days under 52.204-23(c) and 52.204-30(c)). (SR-1; SR-3)
4.11 Security controls must be assessed at least annually by an assessor independent of their operation (P07), as the state contract requires. Results and the POA&M must be reported to the audit committee. (CA-2; CA-7; GV.OV-01)
4.12 Security records (policies, assessments, risk registers, incident records) must be kept at least 3 years, or longer where a contract or Fla. Stat. 119.0701 requires. At contract end, customer public records must be transferred to the customer or kept under the customer's retention rules, and exempt duplicates destroyed. (SI-12)
4.13 **Contingency.** The IFOP must have a contingency plan based on the BIA (P05), with manual-mode (building recovery) procedures for every customer site, starting with the County A EOC and the state data center building, restore tests of each BAS cluster at least quarterly, and a backup ROC failover drill at least twice a year. The plan must be exercised with each customer at least annually. (CP-1; CP-2; CP-4)
4.14 **Change and configuration.** Changes to BAS programs, door schedules, firewall rules, and cloud configuration must be ticketed, approved by someone other than the person making the change, and recorded. OT components must follow the OT hardening standard (STD-01), including removal of default credentials at commissioning. (CM-1; CM-3; CM-6)
4.15 **Patching and malware.** Company endpoints and servers must receive security patches within the STD-09 targets (critical internet-facing within 14 days, others within 30 days). Edge firewall firmware must be reviewed monthly against known exploited vulnerabilities. OT patches and firmware are applied in maintenance windows agreed with the customer. Every company endpoint and server must run endpoint protection or, where OT software does not allow it, application allow-listing. (SI-1; SI-2; SI-3)
4.16 **Physical security.** Offices and the ROC zones are badge-controlled. Visitors must sign in and be escorted. Keys to customer BAS and access control panels must be logged and inventoried quarterly. (PE-1; PE-3)
4.17 **AI governance.** No AI tool or AI feature (including features in customer systems, such as face recognition or video analytics) may be used or switched on without approval through the AI governance process (P10 and STD-05). (PL-4; GV.OC-03)
4.18 **Acquisitions and new contracts.** Security due diligence must be completed before an acquired company or a new contract's systems connect to company systems. (RA-3; CA-3)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (4.8). Compliance is checked through the annual control assessment (P07), monthly security metrics, the access reviews in POL-02, and the quarterly supply chain checks.

## 6. Exceptions
Exceptions follow statement 4.7. They must be written, risk-rated, approved by the authority in 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register (P01); state contract cybersecurity exhibit; County A, County B, and City addenda; FAR clauses in the GSA contract
