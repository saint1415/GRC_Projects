# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-07 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Regulatory basis | 9 CFR 417.3(b), 418.2; 21 U.S.C. 350f(d); 21 CFR 121.145; Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully, **and that no product made or stored while controls or records were compromised ships until food safety has been confirmed**.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary and agency workers, and contractors) at the Florida plant and outlet store. Covers all systems and data, including process control systems, cloud and SaaS services, and systems that vendors operate or maintain for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the forensic firm and vendors |
| Controls Engineer | Leads OT containment and recovery; decides safe states with the Operations Manager |
| FSQA Manager | Product hold and release decisions; FSIS, FDA, and customer notification decisions |
| General Manager | Engages counsel and the cyber insurer; approves external communications |
| Maintenance and Refrigeration Manager | Keeps refrigeration running safely; ammonia emergency response under the PSM program |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with ransomware affecting production and cold-chain monitoring (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to their supervisor or the IT incident line. Examples: unexpected HMI or setpoint changes, unknown people at a restricted step, phishing clicks, lost devices, ransom notes, or monitoring alarms that stop arriving. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system. (IR-5)
4.4 **Food safety first.** When an incident affects process controls, CCP monitoring, formulations, or food safety records, the FSQA Manager must place affected product on hold, evaluate it under the HACCP corrective action rules for unforeseen deviations, and document the decision before any of it ships. (IR-4; 9 CFR 417.3(b))
4.5 **Suspected tampering is a food defense event.** Any sign that a setpoint, formulation, CIP valve, or record was changed deliberately must trigger the food defense corrective action procedure and a reanalysis decision. (IR-4; 21 CFR 121.145; 121.157(b)(3))
4.6 Notifications to FSIS, FDA, customers, affected individuals, and law enforcement must meet the deadlines in the P08 notification matrix. The FSQA Manager decides FSIS and FDA notices; legal counsel confirms personal-data notices. (IR-6; RS.CO-02; 9 CFR 418.2; 21 U.S.C. 350f(d))
4.7 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.8 Recovered OT systems must be restored from verified clean backups, and formulations must be compared with the signed master before production restarts. (CP-10; SI-7)
4.9 The incident response plan must be tested at least annually by a tabletop exercise that includes the FSQA Manager and the Controls Engineer, and after any major incident. (IR-3; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and, where relevant, the food defense reanalysis. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.9). Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.8. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; HACCP plans; recall procedure (9 CFR 418.3); food defense plan; PSM emergency response plan
