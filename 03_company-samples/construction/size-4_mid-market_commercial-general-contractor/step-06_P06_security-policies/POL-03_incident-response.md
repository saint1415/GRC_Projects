# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Security Manager |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, exercises, or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.AN-03, RS.MI-01, RC.RP-01, ID.IM-03 |
| Federal contract requirements | DFARS 252.204-7012(c) to (g), (m)(2)(ii) (N23-R03); FAR 52.204-25(d) (N23-R02); SP 800-171 Rev. 2 3.6.1 to 3.6.3; Fla. Stat. 501.171 |
| Supporting standards | STD-02 Logging and monitoring; STD-07 Contingency and recovery |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully. The two most consequential incident types are business email compromise that redirects a payment, where minutes matter for a bank recall, and a cyber incident affecting covered defense information, where the 72-hour DoD reporting clock starts at discovery.

## 2. Scope
All workforce members and all company systems, including the CPE and systems that vendors operate for the company. It also covers incidents reported to the company by subcontractors that hold CUI or FCI.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Security Manager | Incident commander for security incidents; coordinates the MSSP, forensics, and evidence preservation |
| Chief Operating Officer | Crisis lead for incidents that affect operations, clients, or the Army Corps of Engineers; approves external statements |
| Chief Financial Officer | Leads any payment-diversion response; notifies the cyber insurer through the carrier hotline |
| General Counsel | Directs privileged investigation; decides breach notices and federal reporting content |
| Director of Contracts and Compliance | Files DIBNet and Section 889 reports; Contracting Officer contact; holds a medium assurance certificate |
| FC-4 Project Executive | Contacts the A&E firm and trades for CUI incidents; collects subcontractor incident numbers |
| Controller | Calls the bank to request recalls; freezes payment changes |
| MSSP | 24x7 detection and containment for the corporate environment; calls the Security Manager within 30 minutes of a high-severity alert |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most consequential incident types: business email compromise (P08 `ir-runbook.md`) and compromise of covered defense information (P08 `ir-runbook-cui-incident.md`). The plan must integrate crisis management, legal privilege, and insurer notice. (IR-8; RS.MA-01)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, by calling the security incident line. Examples:
- an unexpected MFA prompt, or a sign-in alert they did not cause
- a request to change bank or remittance details, even if it looks routine
- a lost or stolen device or security key
- CUI found anywhere outside the CPE, or sent to someone outside the FC-4 distribution list
- a subcontractor reporting its own incident

Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the security ticket queue. (IR-5)
4.4 **Suspected payment diversion.** The Controller must call the bank to request a recall as soon as a diversion is suspected, and a complaint must be filed with the FBI's Internet Crime Complaint Center (IC3) the same day. No payment change received in the suspected window may be used until it is re-verified under POL-01 4.8. (IR-4; RS.MI-01)
4.5 **Possible CUI incidents.** Any event that may affect a covered contractor information system or covered defense information, including CUI found on an unauthorized system, must be treated as a possible cyber incident. The Security Manager must start the review for evidence of compromise required by DFARS 252.204-7012(c)(1)(i) at once and record the discovery time. (IR-4; RS.AN-03)
4.6 **DoD reporting.** Cyber incidents affecting covered defense information must be reported to DoD at https://dibnet.dod.mil within 72 hours of discovery (DFARS 252.204-7012(c)(1)(ii)). At least two people must hold a valid DoD-approved medium assurance certificate at all times ((c)(3)). Isolated malicious software must go to the DoD Cyber Crime Center, not the Contracting Officer ((d)). (IR-6; RS.CO-02)
4.7 **Preservation.** At the start of every incident, identity, mailbox, CPE, SYS-01, ERP change, and firewall logs must be exported before default retention deletes them. For incidents reported to DoD, images of all known affected systems and relevant monitoring data must be kept for at least 90 days from the report, and DoD requests for access or damage assessment information must be honored (DFARS 252.204-7012(e) to (g)). (IR-4; AU-11)
4.8 **Section 889 reports.** The Director of Contracts and Compliance must report covered telecommunications or video surveillance equipment identified during contract performance to the Contracting Officer (DoD: https://dibnet.dod.mil) within one business day of identification, and further mitigation information within 10 business days of that report (FAR 52.204-25(d)(2)). (IR-6)
4.9 **Subcontractor incidents.** Subcontracts involving CUI must require the subcontractor to report to DoD and give the company the DoD incident report number as soon as practicable (DFARS 252.204-7012(m)(2)(ii)). The FC-4 Project Executive records the number and the Security Manager assesses any effect on company systems. (IR-6; RS.CO-03)
4.10 For every incident, General Counsel must determine and document whether personal information was accessed, as defined in Fla. Stat. 501.171(1)(g) or in the law of any other affected individual's state, and whether client facility security details or MBSS client systems were affected. Notifications must meet the deadlines in the P08 notification matrix. (IR-6; RS.CO-02)
4.11 The cyber insurer must be notified through the carrier hotline before incident vendors are engaged, unless delay would cause harm. (IR-7)
4.12 The incident response plan must be tested at least annually for each runbook, including a DIBNet reporting drill for the CUI runbook, and after any major incident. Incident team members, the Director of Contracts and Compliance, and the FC-4 Project Executive must be trained on their duties each year. (IR-2; IR-3)
4.13 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and training. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.18. Compliance is checked through the annual control assessment (P07), exercises, and incident reviews.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may be granted against a contract reporting deadline.

## 7. Related documents
P08 runbooks and notification matrix; POL-01; POL-04; STD-02; STD-07; DFARS 252.204-7012; FAR 52.204-25; Fla. Stat. 501.171; cyber insurance policy
