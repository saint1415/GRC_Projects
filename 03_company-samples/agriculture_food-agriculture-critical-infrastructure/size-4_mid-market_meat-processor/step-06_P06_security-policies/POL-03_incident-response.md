# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 IT-only policy) |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-2(1), CP-10 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, RC.RP-05, ID.IM-02 |
| Rules | 9 CFR 417.3(b); 9 CFR 418.2; 29 CFR 1910.119(m)-(n); 40 CFR 68.81, 68.95; 40 CFR 302.6; Fla. Stat. 501.171 |
| Supporting standards | STD-04 Logging and monitoring; STD-06 OT backup and recovery |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents in IT and OT quickly, keeps unsafe product out of commerce, keeps people safe around the ammonia systems, and meets every legal and contractual deadline.

## 2. Scope
All security incidents and suspected incidents affecting company IT or OT systems, data, or vendors that hold company data, including suspected tampering with process setpoints, formulations, or food safety records. Applies at both plants and the corporate offices.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander; coordinates the MSSP and forensics |
| Controls Engineering Manager | OT lead: safe state, OT containment, verified restore |
| Vice President of Food Safety and Quality Assurance | Food safety lead: product holds, FSIS notification, customer food safety notices |
| Director of Engineering and Maintenance | Refrigeration and ammonia safety; PSM and RMP emergency plans and investigations |
| IT Director | IT technical recovery |
| Chief Operating Officer | Chairs the crisis management team; approves external statements |
| General Counsel | Legal decisions; engages outside counsel; breach determinations; decision log |
| Plant Managers | Line stop and restart decisions at their plant |
| MSSP | 24x7 IT detection, first containment, and escalation within 30 minutes for high severity |
| All workforce | Report suspected incidents and unexplained setpoint or recipe changes immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely and most harmful incidents. At minimum these are ransomware halting processing lines and cold-chain monitoring, and suspected tampering with process setpoints or formulations through the control system (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to their supervisor or the security line. Examples: phishing clicks, lost devices, HMIs behaving oddly, setpoints or recipes nobody approved, unknown people near control panels. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized by severity, and tracked to closure. **The time of discovery and the time of every product-affecting event (last trusted CCP reading, start of manual monitoring) must be recorded.** (IR-5; IR-4)
4.4 A severity 1 incident (any ransomware, any confirmed or suspected process tampering, or an outage expected to exceed a High-criticality MTD) must activate the crisis management team, chaired by the COO, within 2 hours. (IR-4; RC.RP-01)
4.5 **Product first.** When CCP control or monitoring is lost or cannot be trusted, the plant FSQA Manager must hold affected product and review it as an unforeseen deviation under 9 CFR 417.3(b). Any unexplained difference between running setpoints or formulations and the approved versions must be treated as possible intentional adulteration until the VP FSQA rules it out. (IR-4; RS.AN-03; 9 CFR 417.3(b))
4.6 **People first around ammonia.** When supervisory control of a refrigeration system is lost or suspected compromised, the engine room must switch to the manual operation procedure, and the Director of Engineering and Maintenance must decide whether a PSM and RMP incident investigation is required (29 CFR 1910.119(m); 40 CFR 68.81). (CP-2(1); RS.MA-01)
4.7 Notifications to FSIS, release reporting agencies, individuals, the Florida Department of Legal Affairs, consumer reporting agencies, the cyber insurer, customers, and law enforcement must meet the deadlines in the P08 notification matrix. The General Counsel or outside counsel must confirm each legal notification. The VP FSQA decides FSIS notifications under 9 CFR 418.2. (IR-6; RS.CO-02; RS.CO-03)
4.8 The cyber insurer must be notified through its hotline before incident response vendors are engaged, as the policy requires. (IR-7)
4.9 No ransom may be paid without approval from the CEO, the General Counsel, and the insurer, a documented OFAC sanctions check, and a report to law enforcement. Paying never makes held product safe or removes a notification duty. (IR-4)
4.10 **Verified restart.** No line may restart after an OT incident until the Controls Engineering Manager confirms PLC programs, recipes, and setpoints match the approved versions, and the Plant FSQA Manager signs the restart checklist. (CP-10; RC.RP-05)
4.11 Incident response must be exercised at least annually for each runbook, with plant leadership, FSQA, and engineering, and at least one exercise a year with outside counsel and the executive team. (IR-3; ID.IM-02)
4.12 Lessons learned must be documented within 30 days of closing a major incident and fed into the risk register (P01), the POA&M (P07), the HACCP reassessment, and the food defense plans. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Checked through the annual independent assessment (P07) and exercise reports. Violations are handled under POL-01 section 5.

## 6. Exceptions
Follow POL-01 section 4.8. No exception may extend a legal notification deadline or allow release of held product without FSQA review.

## 7. Related documents
P08 `ir-runbook.md`, `ir-runbook-process-tampering.md`, and `notification-matrix.csv`; POL-01; STD-04; STD-06; HACCP corrective action procedures; recall procedures; PSM and RMP emergency plans
