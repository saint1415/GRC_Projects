# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Executive Officer |
| Effective date | 2026-09-22 (replaces the December 2025 policy adopted for the SOC 2 Type 1) |
| Review cycle | Annually (next review 2027-09-22), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-03 |
| Also supports | SOC 2 CC7.3 to CC7.5; DPA incident notice commitment (72 hours, 48 hours for 3 customers); state breach laws (P08); FTC Data Breach Response guidance |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully, and notifies customers within the time the DPA promises.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), whether they work in the Florida office or remotely. Covers all company systems and data, including the Workforce Scheduling Platform (WSP), the staging environment, the source repository and CI/CD pipeline, corporate SaaS, laptops, and systems that sub-processors operate for the company. It applies to customer data (customer worker data the company processes as a service provider under the DPA) and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; owns the plan and runbooks |
| Platform Engineering Lead | Technical lead: containment, evidence, and recovery |
| COO (privacy lead) | Decides, with outside privacy counsel, whether an incident requires customer, individual, or regulator notice; engages the cyber insurer |
| Customer Support Manager | Keeps the customer security contact list; sends approved customer notices |
| CTO | Approves shutdowns and customer-impacting containment |
| Chief Executive Officer | Approves external statements and any extortion payment decision |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with cloud credential compromise exposing customer data (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, by paging the on-call engineer or posting in the security incident channel. Examples: a leaked key or secret, an unexpected cloud alert, a lost laptop, customer data sent to the wrong customer, or a phishing click. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged in the engineering ticket system with the security label, given a severity (SEV-1 customer data exposed or platform down; SEV-2 contained or limited impact; SEV-3 no customer impact), and tracked to closure. The IT Manager reviews open incidents monthly. (IR-4; IR-5; RS.MA-03)
4.4 **Customer notice.** When an incident affecting customer data is confirmed, affected customers must be notified without undue delay and within 72 hours of confirmation, or 48 hours for the 3 customers whose contracts say so. The Customer Support Manager must keep a security contact for every customer and verify the list quarterly. (IR-6; RS.CO-02)
4.5 **Legal notices.** Notices to individuals, regulators, and consumer reporting agencies must meet the deadlines in the P08 notification matrix. For customer worker data the company acts as the customers' service provider, so it notifies customers and supports their notices unless a contract or law requires more. Outside privacy counsel must confirm each legal notice. (IR-6; RS.CO-02; RS.CO-03)
4.6 Evidence must be preserved before systems are changed where it is safe to do so: cloud audit logs, access logs, snapshots, and credentials, with a chain-of-custody record. (IR-4)
4.7 No ransom or extortion payment may be made without approval from the Chief Executive Officer, outside counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.8 On-call engineers and support leads must receive incident response training each year. The plan must be tested at least annually by tabletop exercise (the first on 2026-11-18) and after any major incident. (IR-2; IR-3)
4.9 Lessons learned must be documented within 30 days of closing a SEV-1 or SEV-2 incident and added to the risk register and POA&M. (IR-4; ID.IM-03)
4.10 Until the disaster recovery plan is approved (due 2027-01-31, when contingency requirements will be added to this policy), recovery must follow the priorities in the BIA (P05). (CP-1; RC.RP-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.7. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the SOC 2 examination (P09), and the access reviews in POL-02.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved at the level set in POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; P05 BIA; POL-01; POL-02; customer DPA; Fla. Stat. 501.171
