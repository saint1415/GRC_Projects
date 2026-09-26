# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. |
| Policy ID | POL-03 |
| Owner | IT Manager (Information Security Officer) |
| Approved by | Audit and Risk Committee of the Board of Directors, 2026-08-27 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.MI-01, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| Interagency Guidelines (12 CFR 30 App. B) | III.C.1.g; Supplement A (response programs and customer notice); 12 CFR Part 53; 12 CFR 225.302; 12 CFR 21.11 |

## 1. Purpose
Make sure the bank detects, contains, reports, and recovers from security incidents and payment fraud quickly and lawfully. This policy sets up the response program the Guidelines ask the bank to adopt (III.C.1.g) and that Supplement A describes, and it sets the regulator notice duties of 12 CFR Part 53.

## 2. Scope
All Cris Santos Bank workforce members (directors, officers, employees, contractors, and temporary staff) at the six branches and the operations center. Covers all systems and data, including systems that service providers operate for the bank. It applies to customer information, bank information, and the funds that move through the bank's payment systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager (ISO) | Incident commander for security incidents; coordinates the MSSP, providers, and forensics; keeps the incident register |
| President and CEO | With the ISO, decides whether an incident is a notification incident; makes the OCC and Federal Reserve notices |
| Deposit Operations Manager | Wire recalls and account holds for payment fraud |
| BSA/AML Officer | SAR decisions and filing; law enforcement liaison |
| Compliance Officer | Customer notice determinations and notices; state breach law analysis with counsel |
| Chief Operating Officer | Service provider escalation; business continuity activation |
| All workforce | Report suspected incidents and fraud immediately |

## 4. Policy statements
4.1 The bank must maintain an incident response plan and runbooks for its most likely incidents, starting with business email compromise and fraudulent wires (P08). (IR-8; RS.MA-01; III.C.1.g)
4.2 Workforce members must report a suspected fraudulent payment request **within 15 minutes**, and any other suspected incident immediately and within 1 hour at most, to the ISO incident line and, for fraud, to the BSA/AML Officer. Examples: a wire request that fails callback, a customer reporting an unknown transfer, a phishing click, a lost device, misdirected customer information. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged in one incident register, categorized, linked to any BSA case number, and tracked to closure. (IR-5)
4.4 **Notification incident determination.** As soon as possible after a computer-security incident is identified, the ISO and the President and CEO must decide whether it is a notification incident under 12 CFR 53.2(b)(7), using the criteria in the P08 runbook, and record the date and time of the determination. If it is, the OCC supervisory office must receive notice as soon as possible and **no later than 36 hours after the determination** (12 CFR 53.3). If the incident also affects the holding company, the Federal Reserve must receive notice within the same 36 hours (12 CFR 225.302). (IR-6; RS.CO-02)
4.5 **Sensitive customer information.** When the bank becomes aware of unauthorized access to or use of sensitive customer information, it must notify the OCC as soon as possible and investigate promptly whether the information has been or will be misused. If misuse has occurred or is reasonably possible, the Compliance Officer must notify affected customers as soon as possible, unless law enforcement asks in writing for a delay (Supplement A II.A.1.b, III.A). State breach notice duties, including Fla. Stat. 501.171, must be met on the timelines in the P08 notification matrix. Counsel confirms each notice. (IR-6; RS.CO-03)
4.6 **SARs and law enforcement.** The BSA/AML Officer must file SARs within the time limits of 12 CFR 21.11(d). When a reportable violation is ongoing, the bank must immediately notify law enforcement and the OCC by telephone, in addition to filing a timely SAR. SAR information is confidential under 12 CFR 21.11(k). (IR-6; RS.CO-02)
4.7 **Fraudulent payments.** For a suspected fraudulent wire or ACH payment, the Deposit Operations Manager must immediately request a recall from the beneficiary bank, place holds where the bank can, and report the fraud to the FBI through the Internet Crime Complaint Center (IC3). (IR-4; RS.MI-01)
4.8 No ransom or extortion payment may be made without approval from the board, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 Incident notices received from bank service providers under 12 CFR 53.4 go to the designated contacts (the ISO and the COO, through a monitored shared mailbox and phone line) and are logged as incidents. (IR-6; GV.SC)
4.10 The incident response plan must be tested at least annually by tabletop exercise, with branch, wire-room, BSA, and compliance participants, and after any major incident. (IR-3)
4.11 Lessons learned must be documented within 30 days of closing an incident, added to the risk register, and used to update training. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under the sanctions procedure (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. No exception may waive a regulatory notice requirement.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-02 (wire callback); 12 CFR Part 53; 12 CFR 225 Subpart N; 12 CFR 30 App. B Supplement A; 12 CFR 21.11; Fla. Stat. 501.171
