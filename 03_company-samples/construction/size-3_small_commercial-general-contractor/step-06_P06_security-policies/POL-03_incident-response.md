# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | CFO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-03 |
| Federal contract requirements | FAR 52.204-25(d) (N23-R02); DFARS 252.204-7012(c)-(e) if covered defense information is ever held (N23-R03); Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully. The most likely incident is business email compromise that redirects a payment, so speed of contact with the bank matters most.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, temporary staff, and interns) at the main office, the equipment yard, and every jobsite. Covers all company systems and data, including systems that vendors operate for the company, and company-issued devices wherever they are used.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the MSP and forensic firm |
| CFO | Leads any payment-diversion response; engages counsel and the cyber insurer; approves external communications |
| Accounting Manager | Contacts the bank for recall; freezes payment changes |
| Contracts Administrator | Federal reports (Section 889; DoD reports if ever applicable) and Contracting Officer contact |
| Project Managers | Contact owners and subcontractors by phone to numbers on file |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with business email compromise (P08). (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, by calling the IT incident line. Examples:
- an unexpected MFA prompt
- a request to change bank details, even if it looks routine
- a lost device
- a suspicious email
- FCI sent to the wrong place

Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5)
4.4 **Suspected payment diversion.** The Accounting Manager must call the bank to request a recall of the funds as soon as a diversion is suspected. A complaint must be filed with the FBI's IC3 as soon as possible (IC3 PSA I-091124-PSA). No payment change received in the suspected window may be used until it is re-verified under POL-01 4.7. (IR-4; RS.MI-01)
4.5 For every incident, the CFO, with counsel, must determine and document two things:
- whether personal information was accessed, as defined in Fla. Stat. 501.171(1)(g) (which includes an email address with its password) or in the law of any other affected individual's state;
- whether any covered defense information was involved.
(IR-6)
4.6 Notifications must meet the deadlines in the P08 notification matrix, and counsel must confirm each one. (IR-6; RS.CO-02; RS.CO-03)
4.7 **Section 889 reports.** The Contracts Administrator must report covered telecommunications or video surveillance equipment to the Contracting Officer (DoD: https://dibnet.dod.mil) within one business day of identification. Further mitigation information must follow within 10 business days (FAR 52.204-25(d)(2)). (IR-6)
4.8 **Evidence.** Identity provider, mailbox, ERP change, and firewall logs must be exported at the start of every incident, before default retention deletes them. If covered defense information is ever involved, images of affected systems must be kept for at least 90 days from the report (DFARS 252.204-7012(e)). (IR-4; AU-11)
4.9 The incident response plan must be tested at least annually by tabletop exercise, and after any major incident. (IR-3)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and training. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.14. Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the CMMC self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the President for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; FAR 52.204-25; Fla. Stat. 501.171; cyber insurance policy
