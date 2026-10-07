# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Crop Farming, Food Processing, Farm Supply) and corporate shared services |
| Policy ID | POL-03 |
| Owner | Group CISO |
| Approved by | Board risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | IR-6, IR-4, IR-8, CP-12, SI-17, IR-3, IR-5, AU-9 |
| CSF 2.0 | RS.MA-02, RS.MA-03, RS.MI-01, RS.CO-02, RS.MA-04, RS.AN-07, ID.IM-03 |
| Division supplements | Crop Farming: freeze-night and fertigation playbooks; Food Processing: food defense and ammonia release steps; Farm Supply: card brand and cooperative notices |

## 1. Purpose
Detect, contain, and recover from cybersecurity incidents across IT and OT, protect people and food safety first, and meet every notice duty on time across divisions, regulators, customers, and investors.

## 2. Scope
All divisions, corporate shared services, and suppliers acting for the group, for any incident affecting group systems, OT, or data.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Incident commander | Group SOC director (backup: Group CISO) |
| OT safety lead | Division OT security manager with the ROC lead or plant manager |
| Notifications | Group General Counsel with outside counsel; division leads for buyer, customer, and cooperative notices |
| Disclosure committee | SEC materiality |
| All workforce | Report suspected incidents and unexpected equipment behavior immediately |

## 4. Policy statements
4.1 Suspected incidents, including unexpected starts, stops, or setpoint changes on any OT, must be reported to the SOC within 1 hour of discovery. (IR-6; IR-4; RS.MA-02)

4.2 One severity scale applies in all divisions. Severity 1 includes any confirmed manipulation of OT, any incident in a shared service, and any incident affecting more than one division. (IR-4; IR-8; RS.MA-03)

4.3 **Safety first.** On suspected OT compromise, operators must put affected equipment in its documented safe state or manual control before any other action, and must not return it to automatic control until the OT security manager approves. (IR-4; CP-12; SI-17; RS.MI-01)

4.4 The Group General Counsel must keep a multi-regulator notification matrix covering state breach laws, SEC disclosure, FDA records and reportable food duties, release reporting for ammonia, buyer, customer, and cooperative contract terms, card brand and acquirer terms, and federal contract clauses; it must be exercised in a cross-division tabletop every year. (IR-6; IR-8; IR-3; RS.CO-02)

4.5 Each notice clock must be recorded when it starts (discovery, determination, or contract trigger), and the shortest clock drives the plan. (IR-6; IR-5; RS.CO-02)

4.6 Severity 1 incidents must be escalated to the disclosure committee within 24 hours of declaration so materiality can be decided without unreasonable delay. (IR-6; RS.CO-02)

4.7 No ransom may be paid without board risk committee approval, counsel and insurer involvement, and an OFAC sanctions check. Payment does not remove any notice duty. (IR-4; RS.MA-04)

4.8 Any incident that could affect food safety or lot traceability must be reported to the Group VP Food Safety and Quality at declaration so the reportable food and recall decisions are made in time. (IR-6; IR-4; RS.CO-02)

4.9 Evidence, including OT logs, PLC programs, and HMI images, must be preserved before rebuilding, with chain of custody. (IR-4; AU-9; RS.AN-07)

4.10 Lessons learned must be held within 14 days of recovery and documented within 30 days, and must update the registers, POA&M, and runbooks. (IR-4; IR-8; ID.IM-03)

## 5. Compliance and enforcement
Compliance is checked through the annual common control assessment and division samples (P07), quarterly access certifications, the annual supplement attestations, and OT change reviews. Violations are handled under POL-01 4.14.

## 6. Exceptions
Exceptions follow POL-01 4.11. OT exceptions also need the division OT security manager's written safety reasoning.

## 7. Related documents
P08 runbook and notification matrix; POL-01; division supplements.
