# Incident Response and Contingency Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager (Information Security Officer) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, incidents, or exercises |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CP-1, CP-2, CP-4, CP-10, AU-1, AU-2, AU-6, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, RC.RP-04, DE.CM-03, ID.IM-02 |
| Legal drivers | Fla. Stat. 501.171(3)-(6); E-Verify MOU Art. II.A.16; each state's breach law for affected residents; MSP client contracts; 29 CFR 778.106 (payday for overtime) |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery |

## 1. Purpose
Make sure the firm detects, contains, reports, and recovers from security incidents and outages quickly and lawfully, keeps associates paid, keeps clinicians' credentials verifiable, and meets every notice deadline.

## 2. Scope
All workforce members and every system in the APATP boundary, including incidents and outages at vendors that hold firm data or run critical processes (payroll, ATS, credentialing, VMS).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP, vendors, and forensics |
| Chief Operating Officer | Chairs the crisis management team; approves external statements |
| General Counsel | Engages breach counsel through the insurer; leads notice decisions with the Director of Compliance and Privacy |
| Director of Compliance and Privacy | Breach determinations, the decision log, DHS E-Verify notice |
| Director of Payroll and Billing | Payroll containment (bank-change freeze, payment holds) and pay continuity |
| IT Director | Recovery in BIA order; contingency plan owner |
| Chief Financial Officer | Insurance claims, emergency payroll funding, lender communication |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The firm must maintain an incident response plan and runbooks for its most likely incidents, starting with a payroll and HR system breach and a payroll platform outage (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the security hotline. Examples: an MFA prompt you did not start, entering a password on a suspicious page, an associate reporting missing pay or a bank change they did not make, a lost device, a misdirected I-9, consumer report, or medical document. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, rated with the P08 severity scheme, and tracked to closure. Pay diversion cases are security incidents, not payroll errors. (IR-5; IR-4)
4.4 The MSSP must escalate high-severity alerts to the Security Manager within 30 minutes, and the Security Manager must declare severity 1 incidents to the COO within 1 hour. (IR-4)
4.5 The Director of Compliance and Privacy, with the General Counsel and outside counsel, must decide whether an incident is a breach under Fla. Stat. 501.171(1)(a) and the law of each state where affected individuals reside, and must record the time of determination and each decision in the decision log. A determination that notice is not required because the breach will not likely result in identity theft or financial harm must be in writing, kept at least 5 years, and sent to the Department of Legal Affairs within 30 days (501.171(4)(c)). (IR-6)
4.6 Notices must meet the deadlines in the P08 notification matrix, including **DHS E-Verify immediately** for any loss of control of E-Verify data, **MSP clients within 48 hours** under their contracts, individuals and the Department of Legal Affairs within 30 days of determination, and each other state's law. Counsel must confirm each notice. (IR-6; RS.CO-02)
4.7 **Pay continuity.** Diverted pay is still owed. Associates whose pay was diverted must be paid to a verified account or pay card within 1 business day, without waiting for fund recovery. If the payroll platform cannot run, the off-cycle manual payroll procedure (STD-07) must be used so that wages, including overtime, are paid on the regular payday. (IR-4; CP-2)
4.8 No payment to an extortionist may be made without approval from the CEO, the General Counsel, and the cyber insurer, an OFAC sanctions check, and a report to law enforcement. (IR-4)
4.9 The incident response plan must be tested at least annually by tabletop exercise for each runbook, and after any major incident. Staff with incident roles must be trained each year. (IR-2; IR-3; ID.IM-02)
4.10 Lessons learned must be documented within 30 days of closing a severity 1 or 2 incident and added to the risk register and POA&M. (IR-4)
4.11 **Contingency.** The firm must maintain a contingency plan based on the BIA (P05), recover in BIA priority order, test restores of firm-managed data quarterly, and hold a recovery exercise at least annually. (CP-2; CP-4; CP-10; RC.RP-01)
4.12 **Logging.** Systems that hold Restricted data or move money (identity provider, payroll, ATS, credentialing, VMS, cloud, endpoints) must send audit logs to the SIEM, kept 1 year searchable and 3 years in protected storage, with alerts for payroll exports, bank-change spikes, and bulk document downloads (STD-02). (AU-2; AU-6; AU-11; DE.CM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 4.8). Compliance is checked through the annual control assessment (P07), the tabletop exercises, and restore test records.

## 6. Exceptions
Exceptions follow POL-01 4.7. They must be written, risk-rated, approved at the risk acceptance level in POL-01 4.4, and expire within 12 months.

## 7. Related documents
P08 runbooks and notification matrix; P05 BIA; STD-02; STD-07; POL-01; Fla. Stat. 501.171; E-Verify MOU
