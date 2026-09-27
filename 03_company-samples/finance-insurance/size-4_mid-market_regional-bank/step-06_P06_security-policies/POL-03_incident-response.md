# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A., and its parent Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Information Security Officer |
| Approved by | Board Risk Committee, 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| Interagency Guidelines (12 CFR 30 App. B) | III.C.1.g; Supplement A; 12 CFR Part 53; 12 CFR 225.302; 12 CFR 21.11 |
| Supporting standards | STD-02 Logging and monitoring; STD-08 Contingency and recovery |

## 1. Purpose
Make sure the bank detects, contains, reports, and recovers from security incidents, payment fraud, and service provider incidents quickly and lawfully. This policy sets up the response program the Guidelines ask the bank to adopt (III.C.1.g) and that Supplement A describes, and it sets the notice duties of 12 CFR Part 53 for the bank, its holding company, and its respondent institutions.

## 2. Scope
All workforce members, all systems and data (including those operated by service providers), the funds that move through the bank's payment systems, and the correspondent services the bank provides to respondent institutions.

## 3. Roles and responsibilities
The response runs on three tiers (details in the P08 runbooks).

| Role | Responsibility |
|---|---|
| Crisis management team (chair: Chief Operating Officer) | Business continuity, customer and respondent communications, resources, ransom decision recommendation |
| President and CEO, with the ISO and General Counsel | Decide whether an incident is a notification incident and make the OCC and Federal Reserve notices |
| Information Security Officer | Incident commander for security incidents; coordinates the MSSP, forensics, and providers; keeps the incident register |
| General Counsel | Privilege protocol; engages outside counsel and forensics; confirms every external notice |
| Director of Payments Operations | Wire recalls and holds for payment fraud |
| BSA/AML Officer | SAR decisions and filing; law enforcement liaison |
| Chief Compliance Officer | Customer notice determinations and state breach law analysis with General Counsel |
| Correspondent Services Director | Notices to respondent institutions |
| Director of Marketing and Communications | Customer and media statements approved by the CEO |
| All workforce | Report suspected incidents and fraud immediately |

## 4. Policy statements
4.1 The bank must maintain an incident response plan and runbooks for its most likely and most severe incidents: business email compromise and fraudulent wires, and a core processor or other critical provider outage caused by a cyberattack (P08). (IR-8; RS.MA-01; III.C.1.g)
4.2 Workforce members must report a suspected fraudulent payment request or an unexpected contact-information change **within 15 minutes**, and any other suspected incident immediately and within 1 hour at most, to the incident line and, for fraud, to the BSA/AML Officer. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every security incident and payment-fraud event must be logged in one incident register, linked to any BSA case number, with the time the bank first learned of it, and tracked to closure. (IR-5; IR-4)
4.4 **Crisis management.** For a severity 1 incident (per the P08 runbooks), the crisis management team must convene within 2 hours. The CEO informs the Board Risk Committee chair and the holding company's board the same day. (IR-4; RC.RP-01)
4.5 **Notification incident determination.** As soon as possible after a computer-security incident is identified, and at each major change in its scope, the CEO, the ISO, and General Counsel must decide whether it is a notification incident under 12 CFR 53.2(b)(7), using the criteria in the P08 runbooks, and record the date, time, and reasons. If it is, the OCC must receive notice as soon as possible and **no later than 36 hours after the determination** (12 CFR 53.3), and the Federal Reserve must receive the holding company's notice within the same period (12 CFR 225.302). (IR-6; RS.CO-02)
4.6 **Notices to respondent institutions.** When an incident has disrupted, or is reasonably likely to disrupt, correspondent services to a respondent bank for 4 or more hours, the Correspondent Services Director must notify the respondent's designated point of contact as soon as possible (12 CFR 53.4 and the parallel provisions, per General Counsel), and credit union respondents under their agreements. (IR-6; GV.SC)
4.7 **Notices from service providers.** Notices received from bank service providers go to the designated contacts (the ISO and the COO, through a monitored shared mailbox and phone line) and are logged as incidents. (IR-6; GV.SC)
4.8 **Sensitive customer information.** When the bank becomes aware of unauthorized access to or use of sensitive customer information, it must notify the OCC as soon as possible and investigate promptly whether the information has been or will be misused. If misuse has occurred or is reasonably possible, the Chief Compliance Officer must notify affected customers as soon as possible, unless law enforcement asks in writing for a delay (Supplement A II.A.1.b, III.A). State breach notice duties must be met under the law of each state where affected individuals reside, on the timelines in the P08 notification matrix. General Counsel confirms each notice. (IR-6; RS.CO-03)
4.9 **SARs and law enforcement.** The BSA/AML Officer must file SARs within the time limits of 12 CFR 21.11(d). When a reportable violation is ongoing, the bank must immediately notify law enforcement and the OCC by telephone, in addition to filing a timely SAR. SAR information is confidential under 12 CFR 21.11(k). (IR-6; RS.CO-02)
4.10 **Fraudulent payments.** For a suspected fraudulent wire or ACH payment, the Director of Payments Operations must immediately request a recall from the beneficiary bank, place holds where the bank can, and report the fraud to the FBI through the Internet Crime Complaint Center (IC3). (IR-4; RS.MI-01)
4.11 **Privilege and insurance.** For any incident that may lead to notices or claims, General Counsel engages outside counsel, who engages the forensic firm. The CFO notifies the cyber insurer through its hotline before response vendors are engaged, and the bond carrier for fraud losses. (IR-7; RS.CO-03)
4.12 **Ransom and extortion.** No ransom or extortion payment may be made without approval from the board, General Counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.13 The plan must be tested at least annually by an executive tabletop covering the notification incident determination, and by a technical or operational exercise for each runbook. Branch, wire room, correspondent, BSA, and compliance staff take part. (IR-3; IR-2)
4.14 Lessons learned must be documented within 30 days of closing an incident, added to the risk register, and used to update training and the runbooks. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.8). Compliance is checked through the annual independent assessment (P07), the annual tabletop, and a quarterly review of the incident register by the CRO.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. No exception may waive a regulatory or respondent notice requirement.

## 7. Related documents
P08 runbooks and notification matrix; POL-01; POL-02 (callback and contact-change verification); STD-02; STD-08; 12 CFR Part 53; 12 CFR 225 Subpart N; 12 CFR 30 App. B Supplement A; 12 CFR 21.11
