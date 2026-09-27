# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-2, AU-6, AU-11, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, DE.AE-02, PR.PS-04 |
| CISA CPG 2.0 (voluntary) | 1.C, 3.Q, 4.B, 5.A, 5.B, 6.A |
| Other drivers | Fla. Stat. 501.171(3)-(6); PCI DSS v4.0.1 Req. 12.10.1 (SAQ P2PE); lease notice clauses |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, keeps building occupants safe while it does so, and meets its legal and lease notice deadlines.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors), integrators, the MSP, and the guard contractor. Covers incidents affecting any company system or data, including building OT (BAS, access control, video), card payment terminals, and data held by vendors for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the MSP and the forensic firm |
| Director of Engineering | OT safety lead: decides when to isolate the BAS and switch plant equipment to hand control |
| Security Manager | Physical security lead: guard posts, door modes, video evidence |
| Chief Operating Officer | Engages counsel and the cyber insurer; approves external and tenant communications; makes the breach notification decision with counsel |
| Controller | Card compromise response; notifies the acquirer and payment processor |
| Property Managers | Tenant notices and updates for their properties |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with ransomware on building automation systems (P08). Plans must include OT safety steps and manual (degraded-mode) operating procedures for HVAC and doors. (IR-8; CP-2; RS.MA-01; CPG 1.C; 6.A)
4.2 Workforce members and contractors must report any suspected incident **immediately, and within 1 hour at most**, by calling the incident line or telling the security console (staffed 24x7). Examples: phishing clicks, lost devices, unusual BAS behavior, doors or turnstiles acting on their own, unknown remote sessions, card data found anywhere other than a terminal. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; CPG 5.B)
4.3 **Safety first.** When an incident affects building systems, the Director of Engineering (or the on-duty chief engineer) decides whether to isolate OT networks and move to manual operation. Staff must not power off field controllers, door controllers, or life-safety equipment unless the manual procedure says so. (IR-4; RS.MI-01)
4.4 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5)
4.5 The COO, with counsel, must decide whether an incident is a breach of personal information under Fla. Stat. 501.171 and document the decision and its date. If the company decides that notice is not required because the breach will not likely result in identity theft or other financial harm, that decision must be in writing, kept for at least 5 years, and sent to the Department of Legal Affairs within 30 days (501.171(4)(c)). (IR-6)
4.6 Notices to individuals, the Department of Legal Affairs, consumer reporting agencies, tenants under lease clauses, the acquirer, and the cyber insurer must meet the deadlines in the P08 notification matrix. Counsel must confirm each legal notice. (IR-6; RS.CO-02; RS.CO-03; CPG 5.A)
4.7 **Ransom.** No ransom may be paid without approval from the majority owner, counsel, and the cyber insurer, and an OFAC sanctions check. The company will report ransomware to the FBI and CISA. (IR-4; IR-6)
4.8 The incident response plan must be tested at least annually by a tabletop exercise that includes engineering and security console staff, and after any major incident. (IR-3; CPG 1.C)
4.9 **Logging.** Firewalls, the remote access gateway, the identity provider, the cloud tenant, the access control platform (administrator actions), and the BAS server must send security logs to the central log service, kept for at least 1 year. Logs must be reviewed weekly, and alerts for OT events (new remote sessions, BAS program downloads, administrator changes) must reach the MSP's 24x7 monitoring. (AU-2; AU-6; AU-11; DE.AE-02; PR.PS-04; CPG 3.Q; 4.B)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; BIA (P05); manual operating procedures for HVAC and doors (due 2026-12-31); POL-01; Fla. Stat. 501.171; the P2PE Instruction Manual (card terminal incidents)
