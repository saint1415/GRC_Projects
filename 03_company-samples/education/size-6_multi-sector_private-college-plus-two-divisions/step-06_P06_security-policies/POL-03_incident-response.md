# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO; notifications owned by the Group General Counsel |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after every Severity 1 incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, CA-5 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-04 |
| Regulatory basis | 16 CFR 314.4(h)(1)-(7) and (j); SAIG Enrollment Agreement; 45 CFR 164.308(a)(6), 164.400-414; 16 CFR 312.8; Form 8-K Item 1.05; state breach laws (Florida worked example: Fla. Stat. 501.171) |
| Runbook | P08 `ir-runbook.md` and `notification-matrix.csv` |

## 1. Purpose (goals of the plan)
Detect, contain, and recover from security events quickly; protect students, families, patients, and customers; meet every legal and contractual notice duty on time in every division; and learn from each event. Together with the P08 runbook, this policy is the college's written incident response plan under 16 CFR 314.4(h). The goals are: limit harm to people, restore the services the BIA ranks first (P05), make each legal determination on documented facts, and fix the weaknesses the event exposed.

## 2. Scope
All security events affecting group systems or data, including events at service providers and events in one division that affect another division's data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Incident commander for Severity 1 and 2 |
| Group CISO | Executive lead; briefs the board risk committee |
| Group General Counsel | Owns the notification matrix; engages breach counsel; approves every external notice |
| College CISO (Qualified Individual) | Determines whether an FTC notification event occurred and its discovery date; owns the FSA report with the executive director of financial aid |
| Student Health Privacy Officer | Runs the HIPAA four-factor assessment and HIPAA notices; classifies affected records as PHI or FERPA records |
| Education Software CISO and privacy counsel | Customer, district, and COPPA-related decisions and notices |
| University registrar | Records unauthorized disclosures in FERPA disclosure records (34 CFR 99.32) |
| Disclosure committee | SEC materiality |
| Division liaisons | Represent each division on the incident bridge |

## 4. Policy statements
4.1 Workforce members must report suspected security incidents to the group SOC immediately, and no later than 1 hour after noticing them. Reports from students, customers, vendors, and researchers must be routed to the SOC the same day. (IR-6; RS.MA-01; 314.4(h)(2))

4.2 One group severity scale applies in every division. Severity 1 is confirmed encryption or exfiltration in a shared service or platform, or Restricted data of more than one division or more than 10,000 people involved. (IR-4; RS.MA-03)

4.3 Every incident must be logged in the SOC case system with a timeline, actions, decisions, evidence, and the legally relevant dates (discovery, determination, materiality). (IR-5; RS.MA-02; 314.4(h)(6))

4.4 **Regulatory determinations** must be made and documented by the designated official for each division, with counsel: the Qualified Individual for FTC notification events (16 CFR 314.2 and 314.4(j)) and the FSA report; the Student Health Privacy Officer for HIPAA breaches (164.402) and for whether affected clinic records are PHI or FERPA records; Education Software privacy counsel for customer and district notices. (IR-6; RS.AN-03)

4.5 The Group General Counsel must maintain the notification matrix covering FSA, the FTC, HHS, customers and contracting colleges, each state where affected individuals reside, insurers, and the SEC, and must update it within 30 days of any change in law, contract, or organization. (IR-6; IR-8; RS.CO-02; 314.4(h)(4))

4.6 **Intercompany notice.** A division or corporate team that learns of an event affecting another division's data must notify that division's designated official within 24 hours. Because knowledge of agents can start a clock (for example 16 CFR 314.4(j)(2) and 45 CFR 164.404(a)(2)), the receiving division must plan its deadlines from the earliest date anyone in the group knew. (IR-6; RS.CO-02)

4.7 The disclosure committee must be convened within 24 hours of a Severity 1 declaration to begin the materiality assessment. (IR-6; GV.OC-03)

4.8 **Ransom decisions** require the board risk committee, counsel, the cyber insurer, and an OFAC sanctions check before any payment. Paying does not remove any notice duty when data was taken. (IR-4)

4.9 During an incident, responders must use out-of-band communications (crisis line and managed mobile devices) and the printed incident binder. (IR-4; RS.CO-03)

4.10 Lessons learned must be held within 14 days of recovery and documented within 30 days of closing the incident. Every weakness found must become a POA&M item with an owner and a date. (IR-4; CA-5; ID.IM-04; 314.4(h)(5), (h)(7))

4.11 Technical playbooks must be tested every quarter. A cross-division tabletop that includes notification decisions must be held at least once a year. (IR-3; ID.IM-02)

4.12 The incident response plan must address the seven elements of 16 CFR 314.4(h): goals, internal processes, roles and decision authority, communications and information sharing, remediation of weaknesses, documentation and reporting, and evaluation and revision. (IR-8; RS.MA-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7. Compliance is checked through the P07 assessment (IR controls), exercise reports, and post-incident reviews.

## 6. Exceptions
None. Notice deadlines cannot be excepted.

## 7. Related documents
POL-01; POL-04; P08 runbook and notification matrix; P05 BIA recovery order; division supplements.
