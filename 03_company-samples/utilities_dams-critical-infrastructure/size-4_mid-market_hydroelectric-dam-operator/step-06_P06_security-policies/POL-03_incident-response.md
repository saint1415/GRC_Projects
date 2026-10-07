# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | OT Security Manager (OT incidents) and IT Director (IT incidents) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2024 policy, which was written mainly for IT) |
| Review cycle | Annually (next review by 2027-09-30); CIP-003-9 R1 topics within 15 calendar months; and after major changes or significant incidents |
| Implements (SP 800-53 Rev. 5) | IR-4, CP-2, IR-6, IR-8, CP-2(1), IR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, ID.IM-02, ID.IM-03 |
| Regulatory drivers | C-DAMS-R01 (FERC Security Program Rev. 3A); C-DAMS-R02 (18 CFR 12.10); C-DAMS-R03 (NERC CIP-003-9, CIP-012-2, EOP-004-4) where cited below |
| Supporting standards | See `standards-index.md` |

## 1. Purpose
Make sure cyber and physical security incidents are detected, contained, reported, and recovered from, with the safety of the dams and the people downstream ahead of every other goal.

## 2. Scope
All security incidents affecting the HCDMS, corporate IT, the cloud, RMOS clients, or company data, and suspicious activity at any project.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| ROC shift supervisor | Incident commander on shift for OT incidents until the Vice President of Generation Operations takes over |
| IT Director | Incident commander for IT incidents |
| Chief Dam Safety Engineer | EAP decisions and 18 CFR 12.10 reports |
| Corporate Security Manager | FERC security incident reports; law enforcement |
| NERC Compliance Manager | CIP-003 E-ISAC notice and EOP-004 reports |
| General Counsel | Legal privilege, breach decisions, client notices, ransom decisions |
| Crisis management team (chair: COO) | Business decisions in a major incident |

## 4. Policy statements
Each statement ends with the SP 800-53 controls, CSF 2.0 subcategory, and regulatory driver it implements.

4.1 Safety first: in any incident that could affect gates or units, operators put the affected gates and units in local control and confirm their physical positions before investigation starts. (IR-4; CP-2; RS.MA-01; C-DAMS-R01 (Rev. 3A 7.4.1))
4.2 Everyone must report suspected incidents immediately to the ROC (24x7) or the IT service desk. The ROC shift supervisor declares OT incidents; the IT Director declares IT incidents. (IR-6; IR-4; RS.MA-02; C-DAMS-R01 (Form 3 Q25a))
4.3 The company keeps incident response plans and runbooks (P08) that identify, classify, and handle Cyber Security Incidents, assign roles, and determine whether an incident is a Reportable Cyber Security Incident. (IR-8; IR-4; RS.MA-01; C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 4.1, 4.3, 4.4))
4.4 A cyber or physical security incident affecting project works, gates, units, or instrumentation is a condition affecting project safety. The Chief Dam Safety Engineer reports it to the Regional Engineer as soon as practicable after discovery, preferably within 72 hours, and files the written report when directed. (IR-6; RS.CO-02; C-DAMS-R02 (12.10(a); 12.3(b)(4)(ii), (viii), (xi)))
4.5 Suspicious activity and security incidents are reported to the FERC Regional Office as soon as practical (usually within one working day), unless law enforcement restricts reporting; HSIN reporting is also used. (IR-6; RS.CO-02; C-DAMS-R01 (Rev. 3A 3.2; 4.2))
4.6 Reportable Cyber Security Incidents involving the low impact BES assets are reported to the E-ISAC. EOP-004-4 events are reported per the Operating Plan by the later of 24 hours after recognition or the end of the next business day. (IR-6; RS.CO-02; C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 4.2; EOP-004-4 R2))
4.7 When an incident could become a project emergency, EAP procedures take precedence; cyber triggers are part of every EAP and Internal Emergency Response sub-element. (IR-8; CP-2(1); RS.MA-01; C-DAMS-R01 (Rev. 3A 3.2; 7.4.1); C-DAMS-R02 (related EAP duties))
4.8 Breach decisions: the General Counsel decides whether personal information was breached and gives notice under the law of each state where affected individuals reside (in Florida, no later than 30 days after determination). RMOS clients are told of any incident affecting their data or connections within 24 hours. (IR-6; RS.CO-03; Fla. Stat. 501.171; RMOS contracts)
4.9 No ransom may be paid without approval by the CEO, advice of counsel, notice to the insurer, and an OFAC sanctions check. Payment never removes a reporting duty. (IR-4; RS.MA-01; OFAC advisory (2021-09-21))
4.10 Plans are tested at least every 12 months, including one OT exercise that involves the EAP, law enforcement, and an RMOS client every 2 years, and the CIP-003 test at least every 36 calendar months. Plans are updated within 180 calendar days after a test or actual Reportable Cyber Security Incident. (IR-3; ID.IM-02; C-DAMS-R03 (CIP-003-9 Att. 1 Sec. 4.5, 4.6); C-DAMS-R01 (Form 3 Q26a-28))
4.11 Lessons learned are documented within 30 days after each significant incident and fed into the risk register and the Security Plans. (IR-4; ID.IM-03; C-DAMS-R01 (Form 3 Q27-28))

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), quarterly OT access reviews, NERC compliance evidence reviews by the NERC Compliance Manager, and metrics reported to the audit committee. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions must be requested in writing, risk-rated, approved under POL-01 4.4, recorded in the risk register, and limited to 12 months. No exception may waive a FERC or NERC requirement.

## 7. Related documents
POL-01; P08 runbooks and notification matrix; EAPs; Security Plans (Internal Emergency Response); CIP-003 plan; EOP-004 Operating Plan
