# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | COO |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), after every tabletop, and after any major incident |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| PCI DSS v4.0.1 | 12.10 (including 12.10.7) |
| FTC Safeguards Rule | 16 CFR 314.4(h), (j) |
| Bank service provider notice | C-FINANCIAL-R01 (12 CFR 53.4) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly. Every notice owed to card brands, the sponsor bank, the FTC, merchants, and affected individuals must go out on time.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and contractors) and all company systems, data, and service providers. It covers any security event affecting the confidentiality, integrity, or availability of account data, customer information, or the processing services.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander; runs the response; engages the managed detection service and forensic firm |
| Platform Engineering Lead | Technical lead for cloud containment and recovery |
| Compliance and Risk Manager | Owns the notification matrix; sponsor bank and card brand notices; coordinates counsel |
| COO | Declares a major incident; approves external communications; engages the cyber insurer |
| Majority owner and CEO | Decides on ransom questions and any action affecting the sponsor relationship |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep a written incident response plan (this policy and the P08 runbooks) covering:
- the seven areas in 16 CFR 314.4(h)(1)-(7): goals, internal processes, roles and decision authority, communications, remediation, documentation, and post-event revision
- the PCI DSS 12.10.1 elements: roles, communication and contact strategies, including card brand notice; incident procedures; business recovery; data backup; legal reporting; coverage of critical components; and the payment brands' incident response procedures

(IR-8; RS.MA-01; PCI DSS 12.10.1; 16 CFR 314.4(h))

4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, through the security on-call number or the incident channel. Examples: phishing clicks, lost laptops, card numbers found in the wrong place, unexpected changes to the payment page. Good-faith reports are never sanctioned. The incident response team must be available 24 hours a day, 7 days a week. (IR-6; RS.MA-02; PCI DSS 12.10.3)

4.3 Security alerts from the SIEM, intrusion detection, change- and tamper-detection, and file integrity monitoring must be monitored and answered 24x7. (IR-4; SI-4; DE.AE-02; PCI DSS 10.4.1, 12.10.5)

4.4 Every incident must be logged, categorized, and tracked to closure in the incident log. (IR-5; RS.MA-02)

4.5 **Suspected account data compromise.** The team must:
- preserve evidence (do not wipe, reboot, or log in to compromised systems with administrator credentials)
- notify the sponsor bank immediately
- make sure the compromise is reported to Visa within three calendar days of reasonable suspicion or confirmation, and meet each other card brand's rules through the sponsor bank
- engage a PCI Forensic Investigator when a brand requires one

(IR-4; IR-6; RS.AN-03; RS.CO-02; PCI DSS 12.10.1)

4.6 **Sponsor bank notice under 12 CFR 53.4.** For every incident, the incident commander and the Compliance and Risk Manager must decide, and record, whether the incident has materially disrupted or degraded covered services (clearing, settlement, reconciliation, or merchant funding files) for the sponsor bank for four or more hours, or is reasonably likely to. If so, the bank's designated point of contact must be notified as soon as possible. If the bank has not provided a contact, notify its CEO and CIO. The designated contacts must be kept on file and confirmed every quarter. (IR-6; RS.CO-02; C-FINANCIAL-R01 (12 CFR 53.4))

4.7 **FTC notice.** Counsel and the Compliance and Risk Manager must decide whether an event is a notification event under 16 CFR 314.2: unauthorized acquisition of unencrypted customer information. If it involves the information of at least 500 consumers, the FTC must be notified through its online form as soon as possible and no later than 30 days after discovery. The company counts affected cardholders toward the 500. (IR-6; RS.CO-02; 16 CFR 314.4(j))

4.8 **Merchant and state notices.** When account data or merchant information is affected, the company must notify affected merchants quickly enough for them to meet their own duties, and in any case within the shortest period that state law sets for a third-party agent (10 days under Fla. Stat. 501.171(6)). It must also meet the breach laws of each state where affected individuals reside, for data it owns (for example merchant owner data). Counsel must confirm each notice. (IR-6; RS.CO-03)

4.9 **Card data found where it should not be.** When PAN is found outside the CDE (tickets, email, chat, the data warehouse, logs), the finder must report it under 4.2. The team must then:
- determine how it got there
- securely delete it or move it into the CDE
- decide whether it was exposed, and handle it as an incident if so
- fix the cause

(IR-4; SI-12; RS.AN-03; PCI DSS 12.10.7)

4.10 No ransom or extortion payment may be made without approval from the majority owner and CEO, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)

4.11 The plan must be reviewed, updated, and tested at least annually by tabletop exercise, and after any major incident. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.12 Incident response staff must be trained on their duties at least annually. (IR-2; PR.AT-02; PCI DSS 12.10.4)

4.13 Lessons learned must be documented within 30 days of closing an incident. The plan must be updated, and new risks added to the risk register. (IR-4; ID.IM-04; PCI DSS 12.10.6; 16 CFR 314.4(h)(7))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.14. Compliance is checked through the annual tabletop (4.11), the quarterly reviews in POL-01 4.7, and the annual control assessment (P07).

## 6. Exceptions
Exceptions follow POL-01 section 4.13. They must be written, risk-rated, approved by the policy owner (or by the majority owner and CEO for High risk), and expire within 12 months. No exception may delay a legally required notice.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-04; Visa What To Do If Compromised (v10.0); 12 CFR 53.4; 16 CFR 314.4(h), (j); Fla. Stat. 501.171
