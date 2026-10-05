# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Cybersecurity Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2022 Cybersecurity Incident Response Plan policy section, updated 2025-04) |
| Review cycle | Annually (next review 2027-09-30), and after every Severity 1 incident, exercise, or directive revision |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AT-3, CP-2, CP-9 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-03, RS.CO-02, RS.CO-03, RS.MI-01, RS.MI-02, RC.RP-01, RC.RP-03, ID.IM-02, ID.IM-04 |
| Regulatory basis | C-TRANSPORTATION-R01 (SD 1580-21-01E II.C, II.D; SD 1580/82-2022-01E III.D.4); C-TRANSPORTATION-S01 (1570.203); S02 (1580.203(d)); S03 (1520.9(c)); S04 (236.1029); S05 (part 225); S06 (171.15); S07 (Fla. Stat. 501.171) |
| Supporting standards | STD-02 Logging and monitoring standard; STD-07 Contingency and recovery standard |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from cybersecurity incidents quickly, keeps train movements safe while it does, and meets every TSA, CISA, FRA, and state reporting deadline. This policy and the P08 runbooks together form the Cybersecurity Incident Response Plan required by SD 1580-21-01E II.D.

## 2. Scope
All workforce members, the MSSP, and vendors with access, at every company location and on trains. Covers IT and OT incidents, incidents at vendors that hold company data or run company services (for example the TMS vendor), and incidents in the shared dispatch service for the affiliated and contracted short lines.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Cybersecurity Manager | Incident commander; owns the plan and runbooks; makes or directs CISA reports as primary Cybersecurity Coordinator; may order IT/OT isolation under 4.7 |
| Director of Information Technology | Technical recovery lead; alternate Cybersecurity Coordinator and incident commander |
| Director of Network Operations and the Chief Dispatcher on duty | Decide train movement restrictions; start manual dispatch; alternate Security Coordinator reports when the primary is unavailable |
| Director of Signals and Communications | Field OT containment and local control point operation |
| Director of Safety, Security, and Hazmat | Primary Security Coordinator: TSA (1570.203) and SSI release reports; FRA and hazmat reports; RSSM location answers |
| Chief Operating Officer | Chairs the crisis management team; approves isolation that stops traffic network-wide |
| General Counsel | Engages outside counsel; breach and notification decisions; contract notices |
| Chief Executive Officer | Ransom decision; informs the audit committee chair and the sponsor's operating partner |
| MSSP | 24x7 triage of IT alerts; escalates high-severity alerts within 30 minutes |
| All workforce | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep a Cybersecurity Incident Response Plan for its Critical Cyber Systems, made up of this policy and the P08 runbooks, that names by position who carries out each measure and the resources needed (SD 1580-21-01E II.D.1 and II.D.2). Runbooks must exist at least for ransomware on dispatch and train control back-office systems and for an extended outage or compromise of the TMS vendor. (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the 24/7 NOC or the MSSP hotline. Examples: phishing clicks, a ransom note, strange CAD/CTC or radio behavior, unexpected CTC indications, a lost crew tablet, an unknown device in a tower shelter or signal housing. Good-faith reporting is never disciplined. (IR-6; RS.MA-02)
4.3 Every event must be logged in the incident log with its **identification time**, classified against the directive's definition of a cybersecurity incident (which includes events still under investigation), categorized by severity, and tracked to closure. The incident commander records the reporting decision for every event that meets the definition. (IR-5; RS.MA-03)
4.4 **CISA report.** Cybersecurity incidents involving systems the company operates or maintains must be reported to CISA (www.cisa.gov/report or (844) 729-2472) as soon as practicable and no later than **72 hours** after identification, stating that the report is made to satisfy the reporting requirements of SD 1580-21-01E, with the content in II.C.4. Supplemental information is reported within 24 hours of it becoming available. Company target: the CISA report within 24 hours where facts allow, so that it also satisfies 4.5 (SD 1580-21-01E II.C.5). (IR-6; RS.CO-02)
4.5 **TSA report.** A cyber attack ("Cyber Attack" in Appendix A to 49 CFR part 1570) is a significant security concern that must be reported to TSA within **24 hours of initial discovery** (1570.203), unless a CISA report under 4.4 that names the directive has already been made. Company practice: the Security Coordinator calls the TSA Transportation Security Operations Center within 12 hours of discovery, as recommended by IC Surface-2025-01. When in doubt, report. (IR-6; RS.CO-02)
4.6 **Other reports.** The Director of Safety, Security, and Hazmat makes, as they apply: a prompt report to TSA if SSI may have been released to unauthorized persons (1520.9(c)); FRA reports if an incident causes or contributes to a reportable accident/incident (part 225); a hazmat incident notice to the National Response Center no later than 12 hours after a reportable hazmat incident (171.15); and en route PTC failure reports to the host railroad (236.1029). Personal information breaches are assessed with counsel and notified under the P08 matrix, including Fla. Stat. 501.171. (IR-6; RS.CO-03)
4.7 **Safety first and isolation authority.** When a system that supports movement authority is suspect, the Chief Dispatcher on duty may stop or hold trains and move to manual dispatch (track warrants or local control point operation) without waiting for approval. The incident commander may order isolation of the dispatch zones and field network from IT when an incident could spread to OT, after informing the Director of Network Operations. Network-wide isolation that stops traffic is confirmed by the COO within 1 hour. Systems must not be reconnected to the dispatch zone until the incident commander confirms they are clean. (IR-4; RS.MI-01; SD 1580-21-01E II.D.1.c; SD 1580/82-2022-01E III.D.4)
4.8 **Containment and evidence.** Containment must limit the spread of malware, deny continued attacker access, determine the extent of compromise, and preserve evidence and partially encrypted storage (SD 1580-21-01E II.D.1.a). Forensic work is engaged through counsel and the cyber insurer's process. (IR-4; RS.MI-02)
4.9 **Backups.** Backups used for recovery must be scanned for malicious artifacts when made and when restored in testing (SD 1580-21-01E II.D.1.b; STD-07). (CP-9; RC.RP-03)
4.10 **The RSSM duty continues.** During any outage, the company must still answer a TSA request for RSSM location and shipping information within 30 minutes (1580.203(d)), using the standby extract and printed lists. (CP-2; RS.CO-02)
4.11 No ransom may be paid without the CEO's decision after consulting the sponsor's operating partner, General Counsel, and the cyber insurer, an OFAC sanctions check, and a report to law enforcement. The default position is not to pay while clean backups exist. (IR-4)
4.12 **Exercises.** The plan must be exercised at least once a year, testing at least 2 of the objectives in SD 1580-21-01E II.D.1.a to II.D.1.c, with the positions named in the plan, including the Chief Dispatcher, Director of Network Operations, and Director of Signals and Communications, as active participants (II.D.3). At least every 2 years the exercise must include IT/OT isolation and manual dispatch in CTC territory. (IR-3; ID.IM-02)
4.13 Role-based incident training must be given at hire and yearly to dispatchers, chief dispatchers, PTC administrators, signal maintainers, and the MSSP's analysts assigned to the company, covering how to recognize and report a cyber event and the manual and isolation steps they own. (IR-2; AT-3)
4.14 Lessons learned must be documented within 30 days of closing a Severity 1 or 2 incident or an exercise, and changes made to the plan, the runbooks, training, and the risk register. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under POL-01 statement 4.11. Compliance is checked through the annual control assessment (P07), the CAP, and the exercise reports.

## 6. Exceptions
Exceptions follow POL-01 statement 4.9. No exception may extend a regulatory reporting deadline.

## 7. Related documents
P08 runbooks (`ir-runbook.md`, `ir-runbook-vendor-outage.md`) and notification matrix; STD-02; STD-07; manual dispatch procedure; hazmat security plan; SD 1580-21-01E; 49 CFR 1570.203; 49 CFR 1520.9; 49 CFR parts 171, 225, and 236; Fla. Stat. 501.171
