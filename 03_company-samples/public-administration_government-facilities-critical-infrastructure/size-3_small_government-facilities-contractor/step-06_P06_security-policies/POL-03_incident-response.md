# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01 |
| Contract and legal drivers | State and county contracts (notice within 24 hours); GSA contract (immediate report to GSA IT, BTTRG section 1.6.1; FAR 52.204-25(d) one business day); Fla. Stat. 501.171(6) (third-party agent notice within 10 days) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, meets every customer notice deadline, and never leaves a customer building unsafe or unsecured while doing so.

## 2. Scope
All Cris Santos Company workforce members and subcontractors. Covers incidents affecting company systems, the FOTP, customer building systems the company operates or maintains, customer data held by the company, and company staff conduct on GSA systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates forensics |
| Director of Operations | Operations lead: building safety, manual-mode procedures, technician dispatch |
| Site Managers | Notify their customer within contract deadlines; coordinate with customer security staff |
| Contracts Manager | Contract and FAR notices (for example 52.204-25(d)); keeps the notice log |
| Chief Operating Officer | Engages counsel and the cyber insurer; approves external statements |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep an incident response plan and runbooks for its most likely incidents, starting with intrusion into building access control and automation systems (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately, and within 1 hour at most**, to the ROC line or the IT Manager. Examples: unexpected door unlocks or schedule changes, unknown remote sessions, setpoint changes nobody made, lost laptops or PIV cards, misdirected drawings, phishing clicks. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 **Safety first.** If an incident affects doors, life-safety-related building functions, or environmental conditions, the operations lead must put the affected building into a safe state (manual mode, doors secured, customer security staff informed) before technical investigation continues. (IR-4)
4.4 Every incident must be logged, categorized, and tracked to closure in the CMMS security category. (IR-5)
4.5 **Customer notice.** The Site Manager must notify the affected customer within the contract deadline: within 24 hours of discovery for the state and county, and immediately for anything touching GSA systems, GSA data, or company staff with GSA access. Notice must come early enough for the customer to meet its own deadlines (for example a county's 48-hour or 12-hour report to the state under Fla. Stat. 282.3185(5)). (IR-6; RS.CO-02)
4.6 Legal notices (for example Fla. Stat. 501.171 breach notices and FAR clause reports) must follow the P08 notification matrix. Legal counsel must confirm each notice about personal information. (IR-6; RS.CO-03)
4.7 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. The company must not pay on a customer's behalf; Florida counties, municipalities, and state agencies may not pay ransoms (Fla. Stat. 282.3186). (IR-4)
4.8 The plan must be tested at least annually by a tabletop exercise with each customer, and after any major incident. (IR-3)
4.9 Incident responders, ROC operators, and Site Managers must receive incident response training within 30 days of assignment and annually. (IR-2)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register. (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Compliance is checked through the annual control assessment (P07) and each exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-02; customer contracts; GSA BTTRG section 1.6
