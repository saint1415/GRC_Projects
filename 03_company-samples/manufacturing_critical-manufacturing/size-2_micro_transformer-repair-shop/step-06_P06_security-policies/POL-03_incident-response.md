# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Security Coordinator) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required an outside notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, SR-8 |
| CSF 2.0 | ID.IM-02, ID.IM-04, RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.MI-01, RC.RP-02, RC.CO-03 |
| Binding duties carried | G&T cooperative exhibit secs. 1-2 (CIP-013-2 R1.2.1-R1.2.2 flow-down); FAR 52.204-25(d) and 52.204-23(c); Fla. Stat. 501.171(3)-(6) |

## 1. Purpose
Make sure the shop spots, contains, reports, and recovers from security incidents quickly and safely, protects people and equipment first, and meets every notice deadline it owes to customers, the government, and employees.

## 2. Scope
All employees and every system and copy of company information, including systems the MSP and SaaS vendors run for the shop and the shop equipment (test PC and test set, drying oven controls and modem, winding machine, camera recorder). A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information; interference with a computer or a piece of shop equipment; lost or stolen devices or badges; and a fraudulent payment request.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager | Incident lead; keeps the incident log; sends notices with counsel |
| Owner | Backup incident lead; calls the cyber insurer; approves outside communications, spending, shutdowns, and any ransom decision |
| Shop Manager | Puts the oven and test bay in a safe state; decides when shop equipment may restart |
| MSP | Technical response for computers, network, and suite: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All employees | Report suspected incidents at once |

## 4. Policy statements
4.1 The shop must keep an incident response runbook for its most likely serious incident, ransomware that stops production (P08), with a printed binder (runbook, contacts, notification matrix, notice templates, paper travelers, and paper test forms) in the office and in the Owner's truck. (IR-8; ID.IM-04)

4.2 Employees must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, in person or by phone. If the Office Manager cannot be reached, report to the Owner. Examples: clicking a suspicious link, a ransom note or files that will not open, an HMI or test PC behaving on its own, a lost laptop, phone, or substation badge, or an email asking to change bank details. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. (IR-5)

4.4 **Safety first on the shop floor.** If an incident touches the oven, oil rig, or test bay, the Shop Manager must first put the equipment in a safe state (finish or stop the cycle locally; de-energize the test bay). No shop equipment may restart after an incident until the Shop Manager has checked its settings and programs against the saved copies. (IR-4; RS.MI-01; RC.RP-02)

4.5 Notices to the cooperative, the contracting officer, employees, the Florida Department of Legal Affairs, consumer reporting agencies, and customers must meet the deadlines in the P08 notification matrix. Counsel reviews each legal notice before it is sent. The cooperative's 72-hour clock runs from **confirmation** of an incident related to the services the shop supplies; the Florida 30-day clock runs from **determination** of a breach. (IR-6; RS.CO-02; cooperative exhibit sec. 1; Fla. Stat. 501.171(4))

4.6 For any suspected ransomware, data theft, account takeover, or payment fraud, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. For payment fraud, the Office Manager must also call the bank at once to try to recall the payment. (IR-4; RS.MA-01)

4.7 No ransom may be paid without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.8 Vendors must report incidents to the Office Manager as their terms require (POL-02 A.5). The Office Manager logs each report and handles it under this policy. (SR-8; IR-6)

4.9 The cooperative must be kept informed and response coordinated with it for any incident notified under 4.5, until closure. (IR-4; RS.MA-01; cooperative exhibit sec. 2)

4.10 Evidence must be preserved before devices are wiped: the MSP exports logs and keeps images when the forensic firm asks, with a record of who handled what. (IR-4; RS.AN-03)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required an outside notice or outside help, and fed into the risk register and training. Customers affected by an outage are told when service is restored. (IR-4; ID.IM-02; RC.CO-03)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a required notice or a safety step.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; obligations list (POL-02 A.10); cooperative exhibit; Fla. Stat. 501.171
