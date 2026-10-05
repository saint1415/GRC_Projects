# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Information Security Manager |
| Approved by | Chief Operating Officer (also as CIP Senior Manager for statements 4.4 to 4.6) |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2025 policy) |
| Review cycle | Annually (next review by 2027-09-30), after every Reportable Cyber Security Incident or exercise, and at least every 15 calendar months for CIP topics |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2, CP-12 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| NERC and other | CIP-003-9 R2 Attachment 1 Section 4; EOP-004-4 R1-R2; Form DOE-417; Fla. Stat. 501.171(3)-(6); 16 CFR 681.1(d)(2)(iii) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, safely, and lawfully. The safety of the public and of line crews always comes first; keeping the grid in a known safe state comes before forensic completeness.

## 2. Scope
All workforce members, contractors, and vendors. All systems and data: corporate IT, the DOP, the low impact BES Cyber Systems, the cloud landing zone, customer and Utility Services systems, and vendor-operated systems that hold company or client data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Director of System Operations (or the shift supervisor on duty) | Operational incident commander for OT incidents; decides on isolation and manual operations; files DOE-417 and EOP-004 reports |
| Information Security Manager | Incident commander for IT and data incidents; technical lead for OT incidents; engages the MSSP and the insurer panel |
| OT Engineering Manager | OT containment, clean rebuild, and integrity checks |
| NERC Compliance Manager | Reportable Cyber Security Incident determination support; E-ISAC notice; 72-hour DOE-417 final report; evidence; SERC liaison |
| CIP Senior Manager (Chief Operating Officer) | Approves the Reportable determination and CIP Exceptional Circumstances; leads the crisis team for High-severity incidents |
| General Counsel | Privilege; breach determinations with outside counsel; regulator and law enforcement contact; ransom decisions with the CEO |
| President and CEO | Chairs the crisis team for incidents that reach the board; approves external statements and any extortion payment decision |
| Vice President of Customer Operations and Director of Utility Services | Customer notices; client utility notices |
| Director of Corporate Communications | Customer, media, and staff messages |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan with runbooks for its two highest-impact incident types: (A) intrusion into distribution control systems and (B) ransomware with customer data theft (P08). The CIP low impact Cyber Security Incident response plan is part of this plan. Runbooks must be integrated with the storm and emergency plan and the crisis management plan. (IR-8; RS.MA-01; CIP-003-9 Attachment 1 Section 4.1)

4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most. DCC operators must report unexpected device operations, unknown logins, or alarms they cannot explain to the shift supervisor at once. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)

4.3 Every incident must be identified, classified by severity, logged with the time of discovery, and tracked to closure. Roles are assigned by title in P08. (IR-5; IR-4; CIP-003-9 Attachment 1 Sections 4.1, 4.3, 4.4)

4.4 For any Cyber Security Incident that touches Substations N, E, L, or H, the NERC Compliance Manager and the Information Security Manager must decide whether it is a Reportable Cyber Security Incident, and the CIP Senior Manager must approve the decision. If it is, the E-ISAC must be notified, unless prohibited by law. The company's internal target is within 1 hour of that decision. (IR-6; RS.CO-02; CIP-003-9 Attachment 1 Section 4.2)

4.5 **Safe state first.** For a suspected OT intrusion, the incident commander may order the "manual operations" state: remote control disabled, vendor access disabled, FLISR switched off, and crews dispatched to key substations. Field devices keep their local protection. (CP-12; RS.MI-01)

4.6 The incident response plan, including a Reportable Cyber Security Incident scenario, must be tested at least annually by tabletop or operational exercise. The CIP limit of 36 calendar months must never be exceeded. The plan must be updated within 90 days after each test or real Reportable Cyber Security Incident (CIP allows 180 calendar days). (IR-3; ID.IM-02; CIP-003-9 Attachment 1 Sections 4.5, 4.6)

4.7 Notifications to DOE (Form DOE-417), NERC (EOP-004-4), the E-ISAC, the Balancing Authority and Reliability Coordinator, client utilities, affected customers, consumer reporting agencies, and state regulators (with the Florida Department of Legal Affairs as the worked example) must meet the deadlines in the P08 notification matrix. The time of discovery or determination must be recorded, because the clocks run from it. General Counsel must confirm customer and regulator breach notices. (IR-6; RS.CO-02; RS.CO-03)

4.8 **Client utilities.** As a third-party agent, the company must notify each affected client utility of a breach of a system it maintains as soon as practicable and within the shorter of the client contract (48 hours) and the statutory limit (10 days after determination, Fla. Stat. 501.171(6)), and give the client what it needs for its own notices. (IR-6; GV.SC-08)

4.9 Before any payment to an extortionist, the company must get approval from the President and CEO, General Counsel, and the cyber insurer, and run an OFAC sanctions check. The board must be informed before payment. (IR-4)

4.10 Incident vendors must be engaged through the cyber insurer's hotline before work starts, unless a delay would endanger safety. (IR-7)

4.11 Identity theft Red Flags detected in customer accounts must be handled under the Identity Theft Prevention Program response steps (hold, verify, close fraudulent accounts, notify the customer). (IR-4; 16 CFR 681.1(d)(2)(iii))

4.12 Lessons learned must be documented within 30 days of closing a High-severity incident and added to the risk register and POA&M. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under POL-01 4.10. Compliance is checked through the annual control assessment (P07), exercise records, and the NERC Compliance Manager's calendar.

## 6. Exceptions
Exceptions follow POL-01 4.9. Statements 4.3, 4.4, 4.6, 4.7, and 4.8 carry NERC, federal, state, or contract reporting requirements and cannot be excepted.

## 7. Related documents
P08 incident response runbooks A and B and the notification matrix; CIP low impact cyber security plan; EOP-004 event reporting Operating Plan; storm restoration plan; crisis management plan; STD-08 Logging and monitoring standard; STD-09 Contingency and recovery standard; POL-01
